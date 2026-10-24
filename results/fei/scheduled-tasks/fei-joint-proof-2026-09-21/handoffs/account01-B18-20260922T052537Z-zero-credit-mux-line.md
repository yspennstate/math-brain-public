# account01/B18 source-bound FEI handoff — zero-selector-credit MUX frontier

**Classification:** `ESSENTIAL_STEP_APPLIED`. **Full FEI remains OPEN / NOT PROVED.**

Execution: `WITHOUT_VERIFIED_BRAIN`. This handoff records repository-authenticated mathematics only; no native brain receiver/context was used.

## Exact candidate and consumed peer result

Live source candidate:
\[
C^\dagger=6.521851214,\quad C_0=6.4548,\quad a^\dagger=0.268204856,
\qquad \Gamma^\dagger=\Gamma_0+a^\dagger z(1-z).
\]
Pinned h96 candidate blob: `1e2a1a5c293fa7b6ec9885b7a410910d6589be80`.

Consumed and applied exact other-account result:
`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md`.
It proves the selector-credit-zero locus of interior one-bit MUX is exactly
`t=1/2` and `q0=1/2` or `q1=1/2`, and reduces either line to
\[
Z(s)=C^\dagger-2+\tfrac12\Gamma^\dagger(s)
-\Gamma^\dagger(1/4+s/2).
\]
Its first open scalar implication was `Z(s)>=0` for all `s in [0,1]`.

Also applied account02/B12
`proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T045519Z-complementary-mux-fourstep/REPORT.md`, which proves
\[
\Gamma^\dagger(s)\ge4s(1-s)(C^\dagger/2+2).
\]

## New theorem

For the fixed live candidate,
\[
\boxed{Z(s)>0\quad\text{for every }0\le s\le1.}
\]
Hence **both exact zero-selector-credit lines of the unequal-data one-bit MUX obey the live all-gate inequality.**

Proof uses the pinned h96 wobble bounds `2.22922 <= G(x)-4.9096 x <= 8.62812`, with conservative bounds `2.229` and `8.629`, in three regimes:

- `0<=s<=1/50`: explicit source-segment derivative bound `Q'(s)>2.8826172255`; endpoint slack `Z(0)=0.0167628035`.
- `1/50<=s<=1/10`: source-tail sandwich gives `L1(1/50)>0.0479544` and `L1'>0.7444`.
- `1/10<=s<=1/2`: account02/B12 complementary-MUX lower bound gives a concave lower envelope with `L2''<-14.9`, and endpoint lower bounds `>0.26545`, `>0.31596`.
- Symmetry gives `Z(s)=Z(1-s)` and closes the full interval.

## Immutable scientific source

Scientific commit: `c9794c46ea6b09c45e042290c99e53bec364dcdc`.
Report path:
`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T052537Z-zero-credit-mux-line/REPORT.md`
Report blob: `f7af04e2de78fc5f865af853cb9afce2473ca34e`.
Checker blob: `6bd13c33bc599f2241ef41b8292385f936b3913a`.
Precheck blob: `52644c3aca6440f63ed23a11cac8abac3eef08f3`.

The checker is source-bound and loads/hashes the existing candidate NPZ; it does not rerun value iteration. The invocation precheck did not falsely represent the full repo-local checker as executed against a locally materialized NPZ.

## New first missing implication

Extend the exact-line positivity to the full three-dimensional unequal-data MUX cube while retaining the exact selector Shannon credit and the data-pivot cross-deficit constraints. The most direct next target is a quantitative collar around each zero-credit line plus a compact-complement argument using the strictly positive selector-credit floor. Only after full MUX closure should this route return to arbitrary composition-prime gates.
