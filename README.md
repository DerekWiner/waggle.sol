# Waggle

**Proposed interaction and action layer in the Alvearium architecture.**

This repository contains Waggle-related code, scripts and design material. Its intended role is to provide user-facing interaction and action interfaces for the wider Alvearium ecosystem.

## Intended responsibility

- User and agent interaction surfaces.
- Explicit action requests and status reporting.
- Interfaces to approved identity, governance or execution components.
- Clear separation between a proposed interaction and an action that has actually completed.

## Implementation status

Treat the code in this repository as the source of truth for implemented behaviour. Architecture documents describe intended capabilities and are not proof that those capabilities are deployed.

Before relying on a contract, inspect its source, tests, compiler version, dependencies and deployment configuration. Do not assume that a domain name, token, DAO, education or therapy integration is operational because it appears in a design document.

## Review and development

Inventory contracts, scripts, tests, generated files and assets. Remove or consolidate assets only after verifying they are not referenced by code, documentation, releases or external publications.

## Security

Do not use example contracts or scripts with real funds or production permissions without an independent review. Never commit private keys, seed phrases or live service credentials.

## License

Review the current `LICENSE` before reuse. The custom Alvearium terms need a deliberate project-wide licensing decision.
