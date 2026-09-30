# FXOTP Roadmap

This roadmap describes the planned development of the
FXVN Open Trading Protocol (FXOTP).

FXOTP is developed incrementally. Features may change during
the 0.x development series before the first stable 1.0 release.

---

## v0.1 — Protocol Foundation

Status: In Progress

- [x] Public GitHub repository
- [x] Apache License 2.0
- [x] README
- [x] Security policy
- [x] Contribution guidelines
- [x] Code of Conduct
- [x] Initial protocol specification
- [x] FXOTP signal JSON Schema
- [x] XAUUSD example message
- [x] Python reference validator
- [x] Automated GitHub validation

Remaining:

- [ ] Additional example messages
- [x] Initial test suite
- [ ] Error code specification
- [x] Protocol governance

---

## v0.2 — Trading Instruction Model

Planned:

- Market orders
- Limit orders
- Stop orders
- Multiple take-profit targets
- Stop-loss representation
- Risk representation
- Trade modification
- Trade cancellation
- Message validation rules

Goal:

Define a consistent trading instruction model that can be
implemented independently by different applications.

---

## v0.3 — Symbol Normalization

Planned:

- Forex symbols
- Metals
- Crypto assets
- Indices
- Commodities
- Canonical symbol format
- Symbol alias format
- Broker suffix and prefix handling

Examples:

GOLD → XAUUSD

XAU/USD → XAUUSD

XAUUSDm → XAUUSD

XAUUSD.a → XAUUSD

The public normalization specification will remain independent
from proprietary broker-specific FXVNPro production data.

---

## v0.4 — Reference Parser

Planned:

- Plain-text signal parsing
- Common signal layouts
- FXOTP message generation
- Validation integration
- Parser test cases

Example:

GOLD BUY 3825

SL 3815

TP1 3840

TP2 3850

becomes a structured FXOTP message.

---

## v0.5 — MT5 Reference Integration

Planned:

- Minimal MT5 reference connector
- FXOTP message interpretation
- Symbol mapping example
- Execution safety examples
- Documentation

The reference connector will demonstrate interoperability
without exposing proprietary FXVNPro production infrastructure.

---

## v0.6 — MT4 Reference Integration

Planned:

- Minimal MT4 reference connector
- FXOTP message interpretation
- Documentation
- Interoperability examples

---

## v0.7 — Developer SDKs

Planned:

- JavaScript SDK
- Python SDK
- Message creation helpers
- Validation helpers
- Documentation and examples

---

## v0.8 — Trade Results

Planned:

- Trade result schema
- Execution status
- Opened trade representation
- Closed trade representation
- Profit/loss result representation
- Error reporting

---

## v0.9 — Interoperability Candidate

Planned:

- Specification review
- Compatibility testing
- Security review
- Documentation review
- Community feedback
- Breaking-change review

Goal:

Prepare the protocol for its first stable release.

---

## v1.0 — First Stable FXOTP Specification

Target characteristics:

- Stable core message format
- Documented compatibility rules
- Formal JSON schemas
- Reference validator
- Reference implementations
- Developer documentation
- Security guidance
- Versioning policy

FXOTP 1.0 will represent the first stable protocol release.

---

## Future Exploration

Possible future work may include:

- Additional trading platforms
- WebSocket transport examples
- Webhook integrations
- Additional asset classes
- Advanced order relationships
- Portfolio instructions
- Trade lifecycle events
- Interoperability certification tools

These items are exploratory and are not commitments.

---

## Project Principles

Development should continue to prioritize:

- Open interoperability
- Platform independence
- Broker independence
- Security
- Simplicity
- Backward compatibility
- Clear documentation

Commercial sponsorship does not provide control over the
FXOTP technical roadmap.
