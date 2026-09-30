# FXOTP Error Codes

## Specification Draft v0.1

**Status:** Draft  
**Protocol:** FXOTP  
**Version:** 0.1  
**Maintainer:** FXVNPro

---

## 1. Purpose

FXOTP error codes provide a common way for implementations to describe
validation, compatibility, mapping, and execution errors.

The goal is to allow different FXOTP-compatible applications to report
failures consistently.

An FXOTP error code describes what went wrong.

It does not define how an application must display the error to a user.

---

## 2. Error Code Format

FXOTP error codes use the following format:

`FXOTP-XXXX`

Example:

`FXOTP-1003`

Implementations should provide both:

- A machine-readable error code
- A machine-readable error type
- A human-readable message

Example:

{
  "code": "FXOTP-1003",
  "type": "INVALID_ACTION",
  "message": "Trading action is not supported."
}

---

## 3. Error Categories

Initial FXOTP error codes are divided into the following ranges:

| Range | Category |
|---|---|
| FXOTP-1000–1099 | Message and validation errors |
| FXOTP-1100–1199 | Protocol and version errors |
| FXOTP-2000–2099 | Instrument and symbol errors |
| FXOTP-3000–3099 | Execution errors |
| FXOTP-4000–4099 | Risk and safety errors |
| FXOTP-9000–9999 | Implementation-specific or unknown errors |

Future specifications may define additional ranges.

---

## 4. Message and Validation Errors

### FXOTP-1001 — INVALID_MESSAGE

The FXOTP message is malformed or does not satisfy the required schema.

Example causes:

- Invalid JSON
- Incorrect field types
- Unexpected message structure
- Invalid message structure

---

### FXOTP-1002 — MISSING_REQUIRED_FIELD

A required FXOTP field is missing.

Implementations should identify the missing field when possible.

Example:

{
  "code": "FXOTP-1002",
  "type": "MISSING_REQUIRED_FIELD",
  "message": "Required field 'action' is missing."
}

---

### FXOTP-1003 — INVALID_ACTION

The requested trading action is not supported by the applicable
FXOTP specification.

Initial FXOTP actions include:

- BUY
- SELL
- CLOSE
- MODIFY
- CANCEL

---

### FXOTP-1004 — INVALID_ENTRY

The entry instruction is invalid.

Possible causes include:

- Unsupported entry type
- Invalid entry price
- Missing required entry information

---

### FXOTP-1005 — INVALID_STOP_LOSS

The stop-loss representation is invalid.

Possible causes include:

- Invalid price
- Invalid data type
- Unsupported stop-loss representation

---

### FXOTP-1006 — INVALID_TAKE_PROFIT

One or more take-profit targets are invalid.

Possible causes include:

- Invalid target price
- Invalid data type
- Invalid take-profit structure

---

### FXOTP-1007 — INVALID_RISK

The risk representation is invalid or unsupported.

Possible causes include:

- Invalid risk type
- Invalid risk value
- Unsupported risk representation

---

## 5. Protocol and Version Errors

### FXOTP-1101 — UNSUPPORTED_PROTOCOL

The message does not identify a supported protocol.

Example:

{
  "protocol": "UNKNOWN"
}

An FXOTP implementation should not silently interpret another protocol
as FXOTP.

---

### FXOTP-1102 — UNSUPPORTED_VERSION

The receiving implementation does not support the FXOTP version
specified by the message.

Implementations should not silently interpret an unsupported protocol
version as another version.

For example, an implementation supporting FXOTP 0.1 should explicitly
handle a message declaring an unsupported future version.

---

## 6. Instrument and Symbol Errors

### FXOTP-2001 — INVALID_INSTRUMENT

The instrument representation is invalid.

Possible causes include:

- Missing symbol
- Invalid asset class
- Invalid instrument structure

---

### FXOTP-2002 — SYMBOL_NOT_SUPPORTED

The canonical FXOTP symbol is valid, but the receiving implementation
or execution platform does not support that instrument.

This does not necessarily mean the FXOTP message itself is invalid.

---

### FXOTP-2003 — SYMBOL_MAPPING_FAILED

The implementation could not map the canonical FXOTP symbol to the
symbol required by the destination platform.

Example:

FXOTP canonical symbol:

`XAUUSD`

Possible destination symbols:

- XAUUSD
- XAUUSDm
- XAUUSD.a
- GOLD

Symbol normalization and broker/platform mapping are defined separately
from the core error code specification.

---

## 7. Execution Errors

Execution errors describe failures that occur after a valid FXOTP
instruction reaches an execution-capable implementation.

### FXOTP-3001 — EXECUTION_REJECTED

The execution platform rejected the trading instruction.

The implementation may provide a safe human-readable explanation when
available.

---

### FXOTP-3002 — MARKET_UNAVAILABLE

The requested market or instrument is currently unavailable for execution.

Possible causes include:

- Market closed
- Instrument disabled
- Trading temporarily unavailable

---

### FXOTP-3003 — INVALID_ORDER_PARAMETERS

The destination platform rejected one or more translated order parameters.

Examples may include:

- Invalid price
- Invalid volume
- Invalid stop distance
- Unsupported order parameters

---

### FXOTP-3004 — INSUFFICIENT_MARGIN

The execution platform reported insufficient margin for the requested order.

This error represents an execution result and does not mean that the
original FXOTP message was structurally invalid.

---

### FXOTP-3005 — EXECUTION_TIMEOUT

The execution request did not complete within the implementation's
allowed time.

Implementations should take care to avoid duplicate execution when
retrying after a timeout.

---

## 8. Risk and Safety Errors

### FXOTP-4001 — RISK_LIMIT_EXCEEDED

The instruction exceeds a configured risk limit.

The limit may be defined by:

- The user
- The receiving application
- The execution connector
- The destination platform

---

### FXOTP-4002 — EXECUTION_BLOCKED

A safety or risk-control system prevented execution.

Examples may include:

- Trading disabled
- Maximum exposure reached
- Safety lock active
- Execution policy rejected the instruction

---

### FXOTP-4003 — USER_CONFIRMATION_REQUIRED

The implementation requires explicit user confirmation before the
instruction may be executed.

This allows FXOTP-compatible applications to support workflows where
a trading instruction is prepared automatically but execution remains
under user control.

---

## 9. Unknown and Implementation-Specific Errors

### FXOTP-9000 — UNKNOWN_ERROR

An error occurred that cannot be represented by a more specific
standard FXOTP error code.

Implementations should prefer a specific standard error whenever possible.

---

### FXOTP-9001–9999 — IMPLEMENTATION_SPECIFIC

This range is reserved for implementation-specific errors.

Applications using this range should document their own error codes.

Implementation-specific codes must not redefine the meaning of standard
FXOTP error codes.

Example:

`FXOTP-9101`

may be used internally by an implementation, but its meaning is not
defined by the core FXOTP specification.

---

## 10. Error Response Example

A future FXOTP-compatible implementation may return an error object such as:

{
  "protocol": "FXOTP",
  "version": "0.1",
  "status": "error",
  "error": {
    "code": "FXOTP-2003",
    "type": "SYMBOL_MAPPING_FAILED",
    "message": "Unable to map XAUUSD to a destination platform symbol."
  }
}

The exact response-message schema will be defined separately.

This document defines the error identifiers and their intended meaning,
not a final transport or response format.

---

## 11. Error Handling Principles

FXOTP-compatible implementations should follow several general principles.

### Prefer specific errors

When possible, implementations should return a specific error such as:

`FXOTP-2003 SYMBOL_MAPPING_FAILED`

instead of:

`FXOTP-9000 UNKNOWN_ERROR`

### Preserve protocol meaning

Standard FXOTP error codes should have the same meaning across
independent implementations.

### Separate validation from execution

A message may be structurally valid but still fail during execution.

For example:

Valid FXOTP message
→ valid XAUUSD BUY instruction
→ destination platform rejects order
→ FXOTP-3001 EXECUTION_REJECTED

This should not be reported as INVALID_MESSAGE.

### Avoid silent failures

Implementations should provide an explicit error when an instruction
cannot be processed safely.

---

## 12. Security Considerations

Error messages should not expose sensitive information.

Implementations should never include the following in externally
returned FXOTP error responses:

- Broker passwords
- API secrets
- Authentication tokens
- Private keys
- Recovery phrases
- Payment credentials
- Internal credentials
- Sensitive personal information

Detailed internal errors may be logged privately while returning a safer
standard FXOTP error to external clients.

For example, an internal connector error containing authentication
details should be converted into an appropriate safe FXOTP error before
being returned externally.

---

## 13. Compatibility

Standard FXOTP error codes should retain their meaning once published
in a stable protocol release.

New error codes may be added in future versions.

Existing error codes should not be reused for unrelated errors.

Applications should ignore unknown optional error metadata when it is
safe to do so, but should preserve the standard error code and type.

---

## 14. Relationship to the Core Schema

The FXOTP signal schema determines whether a structured trading
instruction conforms to the protocol message format.

The error code specification describes why processing may fail.

Conceptually:

Signal
→ FXOTP message
→ Schema validation
→ Application processing
→ Symbol mapping
→ Risk controls
→ Execution

An error may occur at any applicable stage.

Examples:

- Schema validation failure → FXOTP-1001
- Invalid action → FXOTP-1003
- Unsupported version → FXOTP-1102
- Symbol mapping failure → FXOTP-2003
- Execution rejected → FXOTP-3001
- Risk limit exceeded → FXOTP-4001

---

## 15. Future Work

Future FXOTP versions may define:

- Formal error response JSON Schema
- Warning codes
- Retry guidance
- Temporary vs permanent errors
- Transport errors
- Execution result codes
- Partial execution errors
- Multi-target execution errors
- Standard diagnostic metadata

These additions should preserve compatibility with existing standard
error codes whenever possible.

---

## 16. Status

This error code specification is part of the FXOTP 0.x development series.

The error model may evolve before FXOTP 1.0.

Feedback and implementation experience are encouraged before the
first stable protocol release.
