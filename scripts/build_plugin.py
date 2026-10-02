#!/usr/bin/env python3
"""Check the Cursor plugin package and produce a reproducible review ZIP."""

from pathlib import Path
import hashlib
import json
import re
import struct
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def build():
    manifest = json.loads((ROOT / '.cursor-plugin/plugin.json').read_text())
    require(manifest['name'] == 'anny', 'Unexpected plugin identity')
    require(re.fullmatch(r'\d+\.\d+\.\d+', manifest['version']), 'Invalid version')
    require(manifest['author']['name'] == 'anny GmbH', 'Unexpected publisher')
    require(manifest['skills'] == 'skills/', 'Invalid skill path')
    require(manifest['mcpServers'] == 'mcp.json', 'Invalid MCP path')
    require(manifest['logo'] == 'assets/anny-app-nacht-1024.png', 'Unexpected logo')
    require(manifest['description'] and manifest['displayName'], 'Missing listing copy')
    require(not any(k in manifest for k in ['hooks', 'commands', 'agents', 'variables']), 'Unexpected runtime components')

    mcp = json.loads((ROOT / 'mcp.json').read_text())
    require(mcp == {'mcpServers': {'anny-admin': {'url': 'https://b.anny.co/mcp/admin'}}},
            'Expected only the public Admin endpoint, without credentials')

    skill = ROOT / 'skills/anny-booking/SKILL.md'
    content = skill.read_text()
    require(content.startswith('---\nname: anny-booking\ndescription: '), 'Invalid skill frontmatter')
    require('\n---\n' in content[4:], 'Unclosed frontmatter')
    require(len(content.splitlines()[2]) - len('description: ') <= 1024, 'Description is too long')
    require(not re.search(r'TODO|FIXME|\[INSERT|<placeholder>', content), 'Unfinished skill')

    files = ['.cursor-plugin/plugin.json', 'mcp.json', 'README.md',
             'skills/anny-booking/SKILL.md', 'assets/anny-app-nacht-1024.png',
             'assets/anny-app-nacht-512.png']
    for relative in files:
        path = ROOT / relative
        require(path.is_file() and not path.is_symlink(), f'Missing or linked file: {relative}')
        require(path.resolve().is_relative_to(ROOT), 'Path escapes package')
    for size in (512, 1024):
        data = (ROOT / f'assets/anny-app-nacht-{size}.png').read_bytes()
        require(data[:8] == b'\x89PNG\r\n\x1a\n', 'Invalid PNG')
        require(struct.unpack('>II', data[16:24]) == (size, size), 'Wrong image dimensions')

    cases = json.loads((ROOT / 'review/test-cases.json').read_text())['cases']
    require(len(cases['positive']) == 5 and len(cases['negative']) == 3, 'Incomplete anny acceptance suite')
    for case in cases['positive']:
        require(all(isinstance(case.get(k), str) and case[k] for k in
                    ['description', 'prompt', 'tools_triggered', 'expected_behavior']), 'Incomplete positive case')
    for case in cases['negative']:
        require(case.get('description') and case.get('prompt'), 'Incomplete boundary case')

    out = ROOT / 'dist' / f'anny-grok-{manifest["version"]}.zip'
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in sorted(files):
            entry = zipfile.ZipInfo(f'anny/{relative}', (1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (ROOT / relative).read_bytes())
    with zipfile.ZipFile(out) as archive:
        require(archive.testzip() is None, 'Corrupt ZIP')
        for relative in files:
            require(archive.read(f'anny/{relative}') == (ROOT / relative).read_bytes(), 'ZIP/source mismatch')
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    (out.parent / 'SHA256SUMS').write_text(f'{digest}  {out.name}\n')
    print(f'Validated {len(files)} package files and eight acceptance scenarios.')
    print(f'Built {out.relative_to(ROOT)}; SHA-256 {digest}')
    print('This validates the package, not Grok Bot OAuth or end-to-end behavior.')


if __name__ == '__main__':
    build()
