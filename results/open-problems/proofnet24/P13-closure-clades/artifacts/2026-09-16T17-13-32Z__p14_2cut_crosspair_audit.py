#!/usr/bin/env python3
"""Independent exact symbolic audit of P14-2CUT-CROSSPAIR-55.

Checks the three polynomial identities stated in
proofnet24/P14-probability-correlation/runs/2026-09-16/2026-09-16T16-20-50Z__report.md
(creation commit 65da1db0b647bb91eff8cd1d98215943076366ea).

This is a P13-directed peer audit of that concrete algebraic lemma only.
"""
import sympy as sp

DA, CA, DAe, CAe, DB, CB, DBf, CBf = sp.symbols(
    "DA CA DAe CAe DB CB DBf CBf"
)

# No actual separator edge h=xy.
Z = DA*DB + CA*DB + DA*CB
Ze = DAe*(DB + CB) + CAe*DB
Zf = DBf*(DA + CA) + CBf*DA
Zef = DAe*DBf + CAe*DBf + DAe*CBf
factor = (DA*CAe - CA*DAe)*(DB*CBf - CB*DBf)
assert sp.expand(Ze*Zf - Z*Zef - factor) == 0

# Actual separator edge h=xy is allowed.
Z2 = 2*DA*DB + CA*DB + DA*CB
Ze2 = DAe*(2*DB + CB) + CAe*DB
Zf2 = DBf*(2*DA + CA) + CBf*DA
Zef2 = 2*DAe*DBf + CAe*DBf + DAe*CBf
assert sp.expand(Ze2*Zf2 - Z2*Zef2 - factor) == 0

# Pair (h,e), e in A.
Zh = DA*DB
Zhe = DAe*DB
factor_he = DB**2*(DA*CAe - CA*DAe)
assert sp.expand(Zh*Ze2 - Z2*Zhe - factor_he) == 0

print("PASS: P14-2CUT-CROSSPAIR-55 exact symbolic identities")
print("checked: no-separator cross pair; separator-present cross pair; separator-edge pair")
