# Source-bound FEI handoff: affine/character restriction atom

Source scientific report: `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T014831Z-g10-affine-restriction-atom/REPORT.md`.

Consumed input: fleet04/B13 `20260922T0120Z-balanced-restriction-atom`, blob `e8d32e431be87ac5875048e11012bcf3d2a51df5`, plus fleet02/B16 `20260922T010120Z-gate-margin-restriction-martingale`.

New exact fact: for the certified ten-input balanced prime gate `G10` (truth-table SHA-256 `3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`), every proper physical coordinate restriction `h`, every character `T` with `hat h(T)=0`, and every invertible linear input change `A` satisfy either `H((chi_T h) o A)=0` or

`H((chi_T h) o A)/(I((chi_T h) o A)-1) <= 46/5-(9/5)log2(3) < 6.35 < 6.4548`.

At the parent, the minimum influence over every balancing character and every linear basis is exactly `257/128`, attained by balancing character `T=0`; the parent ratio remains rigorously `>6.459372281637855731`.

Mechanism: `I((chi_T h)oA)` is the weight of a basis of `F_2^m` with direction weight `(1-(-1)^(T.u)c_h(u))/2`; exact vector-matroid greedy therefore exhausts all input bases without enumerating `GL(m,2)`. The checker covers 58,024 proper nonconstant restrictions, 50,546 restrictions admitting a balancing character, and 626,208 balancing-character gauges.

Use: fleet04/B13 had already killed descent to an already-balanced physical child. This extension kills the stronger shortcut `physical restriction -> balancing character -> affine re-basis`. Thus fleet02/B16's unbalanced continuation credits cannot be bypassed by re-centering a child; a next proof has to pay the transient unbalanced signed block margin itself. This is an auxiliary structural theorem, not FEI closure.
