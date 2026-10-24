# B11 / A052 — critical slack and child-ratio stability

**Run:** `20261012T001104Z-account01-B11-a052-critical-slack`  
**Primary packet:** A052 (Critical-source structure)  
**Attempt:** `A052-CRITICAL-SLACK-2`  
**Claim:** `B11-A052-CRITICAL-SLACK-v1`  
**Gap:** `G-CRITICAL-STEP`  
**Status:** structural theorem proved, independent review pending; full FEI OPEN.

## Prior status

The current critical-pruning lemma established only

`Delta_i H >= R(f) I_i(f)`

for every coordinate of a descendant-critical Boolean source.  It did not
identify what the surplus measures.  The earlier A052 theorem classified
exact tensor products of critical factors but left near-tensor and local
stability open.

## New exact identity

For the physical children `f_i^+`, `f_i^-`, write `I_sigma`, `H_sigma`,
and `r_sigma=H_sigma/I_sigma` for nonconstant children.  With
`R=H(f)/I(f)`,

\[
\boxed{
\Delta_iH-RI_i(f)
=\frac12\sum_{\sigma:I_\sigma>0}
I_\sigma(R-r_\sigma).}
\]

This is exact.  It follows from the physical edge-counting identity
`(I_++I_-)/2=I(f)-I_i(f)` and the definition of `Delta_iH`.

For a descendant-critical source every term on the right is nonnegative.
Consequently, for every `t>0`,

\[
\frac12\sum_{\sigma:r_\sigma\le R-t}I_\sigma
\le\frac{\Delta_iH-RI_i(f)}{t}.
\]

Thus zero slack forces every nonconstant child to have exactly the parent
ratio.  If the slack is at most `epsilon` times average child influence,
the influence-weighted probability of a ratio loss at least `t` is at most
`epsilon/t`.

## Structural movement

The result turns the previous sign condition into a quantitative plateau
theorem.  Small local slack means almost all surviving child influence stays
near the extremal ratio; equality means the split remains entirely on the
ratio plateau.  This is the exact stability interface needed before any
stopping-tree argument can claim that near-critical descendants remain hard.

For an equal-ratio critical tensor product, both `Delta_iH` and `I_i` are
inherited from the factor containing coordinate `i`.  Hence the slack identity
is tensor-compatible and gives no spurious dimension gain.

## Mandatory controls

- Raw connected-support components are not physical children, so the known
  component entropy and component ratio counterexamples remain intact.
- Equal-ratio tensor powers remain critical and inherit factor slack exactly.
- One-point surgery of a lifted hard core need not be critical.  Passing to
  a maximum-ratio physical descendant can discard the surgery; the theorem
  applies only after that actual critical reduction.
- No descendant is assumed to be critical relative to itself.  Only its
  ratio comparison with the fixed critical root is used.

## Verification

`python3 verify_critical_slack.py` exhaustively checked 32,902 Boolean truth
tables through four variables and 130,933 relevant coordinate identities.
There were zero failures.  Floating entropy values are diagnostic; the
all-dimensional result rests on the exact displayed algebra.

## Remaining obstacle

The new identity supplies no universal upper bound for the slack.  The live
target is to prove that every tensor-prime descendant-critical source has at
least one coordinate with bounded `Delta_iH/I_i`, or else construct a genuine
critical prime family where this minimum diverges.  Full FEI remains open.

## Source pins and routing

- B11 contract blob: `faaa0875ddb129d134bb62abb513f3795e88b590`.
- Prior A052 theorem blob: `9ef2713e0ad9fbecc4cad44164d7bb814f14a00f`.
- Prior A052 claim blob: `12de8832bb58c8d2aace637b5ae6e82429724050`.
- Current critical-pruning derivation:
  `reports/fei-2026-10-11/runs/B20/20261011T232144Z-account01-B20-a096-critical-pruning/NEXT_LEMMA_DERIVATION.tex`.

Route to A054, A055, A090, A094, A096 and B20.  No independent acceptance is
claimed.
