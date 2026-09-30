# Changelog

All notable changes to the FXVN Open Trading Protocol (FXOTP)
will be documented in this file.

The project follows semantic versioning principles where practical
during the 0.x development series.

## [Unreleased]

Development toward FXOTP v0.2.

---

## [0.1.0] - 2026-09-30

### Added

- Initial FXOTP protocol specification
- Machine-readable JSON Schema for trading instructions
- BUY, SELL, CLOSE, MODIFY, and CANCEL action model
- Market entry representation
- Stop-loss representation
- Multiple take-profit targets
- Risk representation
- Instrument and asset-class representation
- Standard FXOTP error code specification
- XAUUSD BUY example
- EURUSD SELL example
- Python reference validator
- Automated validation test suite
- Invalid-message test fixtures
- GitHub Actions continuous integration
- Security policy
- Contribution guidelines
- Code of Conduct
- Project governance model
- Public development roadmap

### Validation

FXOTP v0.1.0 includes automated validation that verifies:

- Valid FXOTP examples are accepted
- Invalid FXOTP fixtures are rejected
- All public example JSON files conform to the current schema

### Status

FXOTP v0.1.0 is the first public development release.

The protocol remains in the 0.x development series and may introduce
breaking changes before FXOTP 1.0.
