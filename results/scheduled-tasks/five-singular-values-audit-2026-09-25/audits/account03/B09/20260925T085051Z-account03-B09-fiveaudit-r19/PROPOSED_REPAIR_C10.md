# Proposed C10 — Lemma 5.1, source line 398 / PDF page 9

Literal issue: the displayed density formula is written without an “almost every” qualifier,
but at the critical value z=v the denominator sqrt(|a||z-v|) vanishes while the strict
indicator is zero. The product is therefore not a defined real-valued expression at that
single point.

This does not affect the law: the critical preimage is {Y=m}, which has probability zero
because Y has a density. Density versions are defined only almost everywhere.

Minimal repair: state the formula for almost every z (or for z!=v) and set p_T(v)=0
(or any finite value). The density bound, interval-preimage estimate, constants and
downstream theorem are unchanged.

Status: literal display GAP / repaired lemma PASS.
