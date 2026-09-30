# FXVN Open Trading Protocol (FXOTP)

**An open protocol for structured trading signals and interoperability
between trading applications and execution platforms.**

FXOTP defines a simple, platform-independent format for representing
trading signals, execution instructions, risk parameters and trade results.

## Why FXOTP?

Trading signals are distributed through many different systems:

- Telegram
- TradingView
- Websites
- Social platforms
- AI applications
- Trading communities
- Custom trading software

Each system uses different formats.

FXOTP provides a common language between them.

## Architecture

Telegram ─────┐
TradingView ──┤
Web / API ────┤
AI ───────────┼──> FXOTP ──> MT4
Custom Apps ──┘          ├──> MT5
                         └──> Other Platforms

## Example

Input:

GOLD BUY 3825
SL 3815
TP1 3840
TP2 3850

FXOTP representation:

{
  "protocol": "FXOTP",
  "version": "1.0",
  "symbol": "XAUUSD",
  "side": "BUY",
  "entry": {
    "type": "market",
    "price": 3825
  },
  "stop_loss": 3815,
  "take_profit": [
    3840,
    3850
  ]
}

## Core Principles

- Open
- Platform independent
- Broker independent
- Human readable
- Machine readable
- Extensible
- Security conscious

## Project Status

FXOTP is currently under active development.

Current milestone: FXOTP v0.1 Specification Draft.

## Roadmap

- [x] Initial protocol architecture
- [ ] Signal Schema
- [ ] Symbol Normalization
- [ ] Result Schema
- [ ] Reference Parser
- [ ] MT4 Reference Connector
- [ ] MT5 Reference Connector
- [ ] JavaScript SDK
- [ ] Python SDK
- [ ] FXOTP v1.0

## Documentation

Documentation is available in the `/docs` and `/specification` directories.

## Contributing

Contributions, technical discussions, interoperability testing and
documentation improvements are welcome.

See `CONTRIBUTING.md`.

## Security

Please do not publicly disclose security vulnerabilities.

See `SECURITY.md`.

## License

Licensed under the Apache License 2.0.

## Maintained by

FXVNPro

Open trading infrastructure for traders, developers and trading applications.
