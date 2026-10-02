# anny — Booking System

<img src="assets/anny-app-nacht-512.png" alt="anny Nacht butterfly" width="128" height="128">

**Create and run a custom booking system directly in chat.**

This plugin connects Grok Bot and Cursor to anny Admin. Describe your business and what should be bookable: anny can implement supported configuration, verify availability, and help manage daily booking operations in the conversation.

- Set up workspace management, desk sharing, hot desks, offices, meeting rooms and shared equipment for employees.
- Offer appointments, consultations, rentals, classes and events to customers.
- Combine internal community-restricted resources with public customer services.
- Configure free and paid services, prices, availability, capacity and booking rules.
- Create administrative bookings for customers or employees, provide returned payment links, and manage approvals, rescheduling, cancellations and recurring bookings.

## Connection

The plugin contains one remote MCP server: `https://b.anny.co/mcp/admin`. It uses Streamable HTTP and OAuth with dynamic client registration. Each user signs in to their own anny account through the host's connection flow; available actions follow that account's permissions. No credentials or API keys are bundled.

In Grok Bot, install the plugin from Marketplace once it is listed, complete OAuth in the browser, and confirm that it appears under Installed. This repository is being prepared for review and is not yet a Marketplace listing.

For Cursor development, the documented local-plugin location is `~/.cursor/plugins/local/anny/`; place this repository's contents there and restart Cursor. Installing there is a Cursor IDE development test, not proof of a Grok Bot installation. See the [official plugin guide](https://cursor.com/docs/plugins).

## Try these requests

> Set up a booking system for my business, for employees, customers, or both.

> Set up our office with 20 desks and two meeting rooms for desk sharing.

> Add online onboarding sessions with our consultant: one hour for EUR 120, available to customers.

> Show our bookings next week and help me manage resources and availability.

## Boundaries

Authentication, payment-provider onboarding, Teams/calendar connections and SSO may require an external step. The plugin can provide supported guidance and verified links; it does not complete those connections by inventing settings. Customers complete payment outside the conversation. A payment link is not proof of payment.

This is the administration plugin. Personal self-service reservations use anny's customer booking interface or a separately connected Customer integration.

## Walkthrough and verification

[Watch the anny Booking System walkthrough](https://www.youtube.com/watch?v=LdH-W2crhes). This existing video shows the Admin MCP in ChatGPT. It illustrates the workflow but is not evidence of an end-to-end Grok Bot test.

The reusable acceptance cases in [review/test-cases.json](review/test-cases.json) follow the walkthrough: office setup, paid onboarding, community membership, a Desk 6 test booking and verification, plus payment onboarding, SSO and bank-transfer boundaries. See [review/status.json](review/status.json) for current validation status.

## Package

The Cursor plugin manifest is `.cursor-plugin/plugin.json`. The package contains the anny booking skill, the remote Admin MCP declaration and original Nacht PNG icons. There are no executable runtime hooks or local server dependencies.

Build and validate a reproducible ZIP with Python 3.9 or newer:

```sh
python3 scripts/build_plugin.py
```

The Marketplace publisher application uses this public repository URL, rather than a ZIP upload. The ZIP is supplied for local review and transfer.

## Publisher and support

Publisher: **anny GmbH**.

[Website](https://anny.co/en/) · [Support](https://anny.co/en/contact) · [Privacy](https://anny.co/en/privacy) · [Terms](https://anny.co/en/terms)

The Nacht artwork is original anny branding supplied for this integration. No open-source license grant is declared by this package; anny trademarks and artwork remain owned by their respective rights holder.
