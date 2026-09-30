# Contributing to FXOTP

Thank you for your interest in the FXVN Open Trading Protocol (FXOTP).

FXOTP is an open project focused on creating a simple, interoperable standard
for structured trading signals and communication between trading applications
and execution platforms.

Contributions from developers, traders, researchers, and platform builders
are welcome.

## Ways to Contribute

You can contribute by:

- Improving the FXOTP specification
- Reporting bugs or inconsistencies
- Suggesting protocol improvements
- Adding trading signal examples
- Improving symbol normalization
- Improving documentation
- Building reference parsers
- Building reference connectors
- Testing interoperability
- Suggesting support for additional platforms

You do not need to be an expert developer to contribute.

Documentation improvements, examples, testing, and technical feedback are
also valuable contributions.

## Before Contributing

Before starting significant work, please check existing GitHub Issues and
Discussions.

For major protocol changes, please open an Issue first so the proposed change
can be discussed before implementation.

## Pull Requests

When submitting a Pull Request:

1. Keep the change focused on one topic.
2. Explain what the change does.
3. Explain why the change is useful.
4. Update documentation when necessary.
5. Add examples or tests when appropriate.
6. Do not include sensitive information or credentials.

Small and focused Pull Requests are preferred.

## Protocol Changes

Changes to the FXOTP specification should prioritize:

- Interoperability
- Backward compatibility
- Simplicity
- Security
- Platform independence
- Broker independence
- Human readability
- Machine readability

Protocol changes should not be designed around the requirements of a single
broker, trading platform, sponsor, or commercial product.

## Security

Do not report security vulnerabilities through public GitHub Issues.

Please follow the instructions in `SECURITY.md`.

Never include:

- Broker passwords
- Private keys
- Recovery phrases
- API secrets
- Authentication tokens
- Payment credentials
- Personal user data

in Issues, Pull Requests, examples, test data, or protocol messages.

## Reference Implementations

Reference implementations are intended to demonstrate FXOTP interoperability.

They should remain understandable, portable, and independent from proprietary
FXVNPro production systems.

Commercial FXVNPro infrastructure, private APIs, authentication systems,
payment systems, proprietary trading logic, and production credentials are
outside the scope of this repository.

## Code and Documentation

Please keep code and documentation clear and easy to understand.

Where possible:

- Use descriptive names
- Avoid unnecessary dependencies
- Include comments for non-obvious behavior
- Provide examples
- Keep platform-specific logic isolated

## Community Conduct

Be respectful and constructive when participating in Issues, Discussions,
Pull Requests, and other project communication.

A formal Code of Conduct is maintained separately in `CODE_OF_CONDUCT.md`.

## License

By contributing to FXOTP, you agree that your contributions will be licensed
under the Apache License 2.0 used by this project.

## Questions

If you are unsure whether an idea belongs in FXOTP, open a GitHub Issue or
Discussion before implementing it.

We welcome ideas that help make trading applications more interoperable,
open, secure, and easier to integrate.
