# FXVN Open Trading Protocol (FXOTP)

## Specification Draft v0.1

**Status:** Draft  
**Protocol:** FXOTP  
**Version:** 0.1  
**Maintainer:** FXVNPro

---

## 1. Introduction

FXVN Open Trading Protocol (FXOTP) is an open protocol for representing
structured trading instructions in a platform-independent and
broker-independent format.

The goal of FXOTP is to provide a common language between trading signal
sources, trading applications, automation tools, and execution platforms.

FXOTP does not define a trading strategy.

FXOTP defines how a trading instruction can be represented and exchanged.

---

## 2. Basic Architecture

A typical FXOTP workflow is:

Signal Source → Parser → FXOTP Message → Connector → Execution Platform

Possible signal sources include:

- Telegram
- TradingView
- Websites
- Social platforms
- AI applications
- Trading communities
- Custom software
- Manual input

Possible destinations include:

- MetaTrader 4
- MetaTrader 5
- Trading applications
- Analytics systems
- Risk management systems
- Other FXOTP-compatible platforms

---

## 3. Design Principles

FXOTP should remain:

- Open
- Simple
- Human readable
- Machine readable
- Platform independent
- Broker independent
- Extensible
- Security conscious

FXOTP should not require broker credentials or other sensitive credentials
inside protocol messages.

---

## 4. Basic FXOTP Message

A basic FXOTP trading instruction may look like this:

```json
{
  "protocol": "FXOTP",
  "version": "0.1",
  "id": "FXOTP-EXAMPLE-0001",
  "created_at": "2026-09-30T08:30:00Z",

  "instrument": {
    "symbol": "XAUUSD",
    "asset_class": "metal"
  },

  "action": "BUY",

  "entry": {
    "type": "market",
    "price": 3825.00
  },

  "stop_loss": {
    "price": 3815.00
  },

  "take_profit": [
    {
      "price": 3840.00
    },
    {
      "price": 3850.00
    }
  ]
}
