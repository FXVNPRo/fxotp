# Security Policy

## Reporting a Vulnerability

Security is important to the FXVN Open Trading Protocol (FXOTP).

If you discover a potential security vulnerability, please do not report
sensitive security issues through a public GitHub Issue.

Please contact the FXOTP maintainers privately so the issue can be reviewed
before public disclosure.

A dedicated security contact method will be added as the project develops.

## Scope

FXOTP is an open protocol specification and reference implementation for
interoperability between trading signals, applications, and execution platforms.

Reference implementations are intended to demonstrate how FXOTP-compatible
systems can communicate.

Applications implementing FXOTP are responsible for their own security,
including:

- Authentication
- Authorization
- Trade confirmation
- Risk controls
- Credential management
- Network security
- Execution safeguards
- API security

## Sensitive Information

FXOTP protocol messages should never contain:

- Broker account passwords
- Private keys
- Recovery phrases
- API secrets
- Authentication tokens
- Payment credentials
- Other sensitive user credentials

Implementations should keep authentication and sensitive credentials outside
the FXOTP message format.

## Trading Safety

FXOTP itself does not guarantee trade execution, profitability, or protection
against trading losses.

Implementations that execute trades should provide appropriate validation,
risk controls, and user safeguards before sending instructions to a trading
platform.

## Reference Implementations

Reference implementations included in this repository are provided for
interoperability testing, development, and educational purposes.

Production systems may require additional security controls beyond those
demonstrated by the reference implementations.

## Supported Versions

FXOTP is currently under active development.

| Version | Supported |
| ------- | --------- |
| 0.x     | Yes       |
| 1.x     | Planned   |

This policy will be updated as the protocol approaches its first stable release.
