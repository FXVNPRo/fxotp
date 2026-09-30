# FXOTP Governance

This document describes how the FXVN Open Trading Protocol (FXOTP)
project is maintained and how technical decisions are made.

FXOTP is an open-source project maintained by FXVNPro with community
participation encouraged through GitHub.

---

## 1. Project Mission

The mission of FXOTP is to provide an open, simple, secure, and
platform-independent protocol for structured trading instructions
and interoperability between trading applications.

FXOTP is intended to remain:

- Open
- Broker independent
- Platform independent
- Extensible
- Security conscious
- Implementable by independent developers

---

## 2. Maintainers

Project maintainers are responsible for:

- Maintaining the FXOTP specification
- Reviewing Pull Requests
- Reviewing protocol proposals
- Managing releases
- Maintaining reference implementations
- Maintaining documentation
- Coordinating security disclosures
- Protecting compatibility and project integrity

The initial project maintainer is FXVNPro.

Additional maintainers may be added as the project and contributor
community develops.

---

## 3. Community Participation

Anyone may participate in FXOTP through:

- GitHub Issues
- GitHub Discussions
- Pull Requests
- Documentation contributions
- Reference implementations
- Testing
- Protocol proposals
- Interoperability feedback

Contributors do not need to be affiliated with FXVNPro.

---

## 4. Technical Decisions

Minor changes may be accepted through normal Pull Request review.

Significant protocol changes should normally begin with a public
GitHub Issue or Discussion.

Examples of significant changes include:

- Adding required protocol fields
- Removing protocol fields
- Changing field semantics
- Introducing new message types
- Changing compatibility behavior
- Changing security-sensitive behavior

Technical decisions should consider:

- Interoperability
- Security
- Simplicity
- Backward compatibility
- Implementation experience
- Platform independence
- Broker independence

---

## 5. Protocol Proposals

Major protocol changes may be documented as an FXOTP proposal.

A proposal should explain:

1. The problem being solved
2. The proposed change
3. Example messages
4. Compatibility impact
5. Security considerations
6. Alternatives considered

The proposal process may become more formal as the project grows.

---

## 6. Releases

FXOTP uses versioned releases.

During the 0.x development series, breaking changes may occur.

The first stable protocol specification will be FXOTP 1.0.

Stable releases should document:

- Protocol changes
- Compatibility impact
- Schema changes
- Security considerations
- Migration guidance when necessary

---

## 7. Sponsorship and Independence

FXOTP may receive financial support from individuals, companies,
infrastructure providers, brokers, technology companies, and other
organizations.

Financial support does not provide:

- Ownership of the FXOTP protocol
- Special voting rights
- Control over technical decisions
- Preferential protocol treatment
- Access to private user information
- Access to proprietary FXVNPro infrastructure
- Authority over security decisions

Sponsors may propose features and participate in public technical
discussions under the same project rules as other participants.

---

## 8. Commercial Implementations

FXOTP may be implemented by commercial and non-commercial applications.

FXVNPro may operate commercial products that implement FXOTP.

Other organizations and developers may also create independent
FXOTP-compatible products subject to the project's open-source license
and applicable specifications.

The FXOTP project itself remains separate from proprietary FXVNPro
production infrastructure.

---

## 9. Security Decisions

Security-sensitive issues may be discussed privately before public
disclosure.

Maintainers may temporarily restrict technical details when necessary
to investigate or mitigate a vulnerability.

Security reporting procedures are documented in `SECURITY.md`.

---

## 10. Conflicts of Interest

Participants should disclose relevant commercial or organizational
interests when proposing changes that could materially benefit a
specific company, product, broker, or platform.

A disclosed commercial interest does not automatically disqualify a
proposal.

Technical merit and interoperability should remain the primary
considerations.

---

## 11. Governance Evolution

This governance model is intentionally simple during the early stages
of FXOTP.

As the contributor community grows, governance may evolve to include:

- Additional maintainers
- Maintainer voting
- Formal protocol proposals
- Working groups
- Release managers
- Independent technical reviewers

Material governance changes should be documented publicly.

---

## 12. Guiding Principle

FXOTP should evolve according to what improves open trading
interoperability, not according to the interests of any single
commercial participant.
