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

```text
FXOTP-XXXX
