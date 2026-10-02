# Grok Bot marketplace preparation

Researched on 3 October 2026.

## Distribution route

Grok Bot uses plugins connected to the user's Cursor account. The relevant publisher route for this integration is the [Cursor Marketplace application](https://cursor.com/marketplace/publish), which accepts a public plugin repository. The Grok Build plugin catalog uses a different GitHub pull-request workflow; it is not the target of this package. Public Bot templates are also a separate sharing mechanism and do not replace this MCP plugin submission.

This package uses the documented Cursor Plugin format so that the manifest can carry a display name, committed logo and explicit skill/MCP paths. Cursor also accepts portable Agent Plugins, which is the format of anny's existing OpenAI package.

## Application copy

- Organization name: anny GmbH
- Organization handle: anny
- Display name: anny — Booking System
- Website: https://anny.co/en/
- Repository: https://github.com/anny-co/grok-plugin
- Logo: the committed assets/anny-app-nacht-1024.png, using a commit-pinned public raw URL in the form
- Contact: the signed-in publisher's existing anny business email
- Requested destination: Grok Bot's plugin catalog and Cursor Marketplace

Description:

anny is a booking system plugin for Grok Bot and Cursor. Create a custom booking system directly in chat and manage booking operations end to end: desk sharing, workspaces, meeting rooms, appointments, rentals, and free or paid service bookings for employees and customers. It connects to the anny Admin MCP over Streamable HTTP with per-user OAuth. Configure resources, services, prices, availability and community access; create and manage administrative bookings and provide returned payment links. Payment-provider onboarding, SSO and integrations use the appropriate external setup flow. Publisher: anny GmbH. Please include the approved plugin in the Grok Bot plugin catalog as well as Cursor Marketplace. Reference walkthrough (recorded in ChatGPT using the same MCP): https://www.youtube.com/watch?v=LdH-W2crhes

## Final boundary

The user requested preparation through the last step, without submitting. Leave Submit Application unclicked. Clicking it also accepts the Publisher Terms, so those terms have not been accepted on the user's behalf.

The current form shows an individual Cursor owner. The organization name is publisher branding and does not turn that personal account into a Cursor team. Do not claim team ownership, namespace availability or review acceptance from filled fields alone.

## Verification

The repository includes five positive and three negative walkthrough-aligned acceptance scenarios and broader discovery prompts. These are anny's chosen test coverage, not a stated Cursor minimum. Static validation checks packaging, metadata, paths, original artwork and the single Admin endpoint. Production OAuth and end-to-end behavior in Grok Bot remain to be verified; the existing ChatGPT recording must be labelled accordingly.

## Official sources

- [Grok Bot connector setup](https://cursor.com/help/grok-bot/connect-plugins)
- [Grok Bot computer and apps](https://docs.x.ai/grok-bot/computer-and-apps)
- [Cursor plugin formats and submission](https://cursor.com/docs/reference/plugins)
- [Cursor MCP transport and OAuth support](https://cursor.com/docs/mcp)
- [Cursor plugin installation and local development](https://cursor.com/docs/plugins)
- [Grok Bot changelog](https://x.ai/changelog/bot)
- [Separate Grok Build marketplace announcement](https://x.ai/news/grok-plugin-marketplace)
