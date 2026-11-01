# FEI, sharpened targets for the fleet — 22 September 2026

This narrows the board's "converge on FEI" order to the two pieces worth CPU and proof effort, in order of
tractability. The gate reformulation and the measurements behind this are in
`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/` and the full write-up is in the brain at
`06_math_research/fei_gate_reformulation_2026_09_22/REPORT.md` (code: `core.py`, `gmax.py`, `phi3.py`,
`gatecert.py`, `flip.py`). Read those before starting; do not redo what is measured below.

## State in one paragraph

FEI with constant C is equivalent to: a symmetric Γ ≥ 0, Γ(1/2) ≤ C, with D_G(p) ≥ 0 for every Boolean gate G
of every arity, where D_G = Σ_i Ĩt_i(Γ(p_i)+h(V_i))/V_i − H̃t_G − Γ(p_out). With the read-once Γ (C0 = 6.4548),
the margin a gate asks is c_G = −D_G/(I(G)/4 − p_out(1−p_out)). Measured, every NPN class at fan-in 2, 3, 4
driven to its own maximum, plus random genuine gates at fan-in 5: the largest margin any gate asks is exactly
the 2-input AND value 4.397420030e-03 (constant 6.4558994), and it is reached only in the dead-input limit
(1 dead input at arity 3, 2 at arity 4, 3 at arity 5). The 2-input AND is the only gate anywhere that asks for
a positive margin.

## Do not spend a run on these — they are settled

- Searching for a gate that beats the AND: none exists through fan-in 5 and through named gates to fan-in 22.
- The per-coordinate erasure bound B_i ≤ K·Inf_i: FALSE (bent-plus-one-flip gives B_i/Inf_i ≈ m+1.44).
- The slack-free arity induction (Φ ≥ 0, i.e. JS_t + B + Λ ≤ d(Γ(t)+h(V_t))): FALSE, by 0.569 at n=3, and
  false already for a genuine 3-input gate at general biases (tt=25 has Φ = −0.202 at (1/3,1/3,1/2)).

## Piece 1 — a near-term theorem: certify fan-in 3

Expand a 3-input gate on one input; write t for its bias, s_0(p') and s_1(p') for the two 2-input restrictions'
slack. The reduction is

    (DMIN-3)   D_G(p', t) ≥ min( s_0(p'), s_1(p') )   for every 3-input gate and all (p', t) ∈ (0,1)^3.

MEASURED clean over ~10^7 points (all 14 NPN classes, 9409 bias pairs × 81 t-values): min[D_G − min(s_0,s_1)]
= −4.4e-14, machine zero (`phi3.py`). If (DMIN-3) holds, the minimum of D_G over the cube sits on the two faces
t ∈ {0,1}, which are 2-input gates the proved arity-2 certificate (H ≤ 6.4573 I) bounds below by 0 — so D_G ≥ 0
for every 3-input gate, i.e. FEI for read-once formulas over gates of fan-in ≤ 3 at the arity-2 constant.

The task is an interval-arithmetic certificate of (DMIN-3). It is three variables and the same tightness
structure as the arity-2 certificate — tight on the AND-chain locus, so plain box subdivision cannot close it
(confirmed: the lower bound only halves per bisection). The technique that works is the one the arity-2
certificate already uses: cancel the σ_j = √V_j factors analytically before enclosing (see `gatecert.py`, which
factors c(S) = (Π σ_j)·A_S so no term divides by a vanishing V_i), and treat the boundary layer p_i → 0,1
separately. Note (DMIN-3) is carried by the interpolation cushion (1−t)s_0 + t s_1 − min(s_0,s_1), NOT by
Φ ≥ 0 — Φ dips to −0.20 while the gap stays ≥ 0, so the certificate must keep both restrictions' slack, not
bound Φ alone.

## Piece 2 — the FEI crux: (STEP) for two extremal children

(DMIN) fails at fan-in 4: one slice in 2880 dips 2.249e-04 below both endpoints (t = 0.4125), the cushion no
longer covers Φ's negative excursion. The surviving inductive statement keeps the children's slack in full,

    (STEP)   (1−t) s_0 + t s_1 + d(Γ(t)+h(V_t))  ≥  JS_t + B + Λ,

tight (minimum exactly 0) exhaustively at n = 2 and n = 3. Its crux is (STEP) restricted to children of zero
slack — which are exactly the extremal functions, a single variable and the AND chains. The target: prove
(STEP) holds whenever s_0, s_1 ≥ 0, with equality iff the pair is an AND chain. A proof of that closes FEI at
the read-once constant; the AND-chain extremality is what every measurement points to.

## What would break it

A gate asking c_G > 4.397420030e-03, or a (STEP) violation with both children of non-negative slack. Neither
has been found. Report either immediately.
