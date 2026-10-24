# B11 / A052 — annealed upper-set envelope and critical coordinate witness

## Status

**PROVED (pending independent review):** an all-dimensional Jensen envelope converts the expected upward potential of genuine physical restrictions into a static functional of the parent spectral law.  The functional has an exact nonnegative coordinate decomposition.  Combined with the source-complete A052 restriction-persistence theorem, every finite-dimensional maximizer with ratio (R) has a physical coordinate whose normalized conditional-absence surprisal is at least (R/4-O(1)).

**OPEN:** no dimension-independent upper payment for that coordinate charge is proved.  Full FEI remains open.

## Frozen packet and objective

- Primary packet: **A052 (Critical-source structure)**.
- Attempt: `A052-ANNEALED-UPPERSET-4`.
- Stable gap: `G-CRITICAL-U-PAYMENT`.
- Claim version: `B11-A052-ANNEALED-UPPERSET-v1`.
- Bounded objective: combine the exact descendant-ratio deficit/persistence identities with a phase-free upper-set constraint and obtain a useful physical coordinate when the critical ratio is large.

This is a mechanism pivot after three A052 attempts: instead of further tensor/component pruning, it anneals the physical restriction phases and uses joint concavity before exposing upper-set zeros.

## Sources actually used

1. Owner control revision `2026-10-12.1`, Brain commit `40210272c19f43fed84f6a67653f9a04b0e11e28` (`scheduled_tasks/work/shared/full-fei-only-2026-10-12/ORDER.md`, `CASE_TARGETS.json`).
2. Canonical B11 compact contract, blob `faaa0875ddb129d134bb62abb513f3795e88b590` (`assignments/B11.json`).
3. A052 critical-slack report, blob `9f0d4ec16e611bc845c92b6b2173b0eae7d34ac7`, proving
   \[
   \Delta_iH-RI_i=\tfrac12\sum_\sigma I(f_i^\sigma)(R-R(f_i^\sigma)).
   \]
4. A052 restriction-persistence proof `RANDOM_RESTRICTION_U_PERSISTENCE.tex`, blob `a8affd77c47ac63e8b37dbffe03436c6851097fd`, read at canonical commit `d41dd05c667aa82d22d66f02d93c067d794d809a`.
5. The earlier all-block critical theorem in `proofnet24/P03-fei/fleet-2026-09-21/account02/B14/20260921T175746Z-block-js-critical-han/REPORT.md`, blob `f490ce01f24431ee2a8b54d8e64cc9336c46ac6f`, used only for the already-proved high-ratio consequence (p_i<1/2) (and \(\Psi(p_i)/p_i\ge R\)).

No registry label was treated as proof, and no protected or held source was accessed.

## New theorem

Let (p(T)=\widehat f(T)^2).  Retain each coordinate independently with probability (t), write the live set as (J), uniformly assign (J^c), and call the restricted function (g=f_{J,X}).  Define

\[
m_J(A)=\Pr_{S\sim p}[S\cap J=A],\qquad
\pi(A)=\Pr_{S\sim p}[S\supseteq A].
\]

Then for every genuine Boolean (f), every dimension, and every (t\in[0,1]),

\[
\mathbb E_{J,X}U(g)
\le F_t(p):=
\mathbb E_J\sum_{A\subseteq J}m_J(A)\log_2\frac{\pi(A)}{m_J(A)}.
\]

The proof is exact.  For the restricted squared coefficient (q_A=\widehat g(A)^2) and restricted upper mass \(\Pi_A\), physical-restriction orthogonality gives

\[
\mathbb E_Xq_A=m_J(A),\qquad \mathbb E_X\Pi_A=\pi(A).
\]

The function \(\phi(x,y)=x\log_2(y/x)\) is jointly concave on \(0\le x\le y\), so Jensen applies term by term.  This is an upper envelope, not the previously available lower-persistence direction.

## Exact coordinate decomposition

Fix a coordinate order.  For each observed intersection (A=S\cap J), expose the absent coordinates of (J\setminus A) in that order.  Charge coordinate (i) the conditional surprisal of its absence after the present coordinates and earlier absent coordinates have been revealed.  The resulting nonnegative charges (C_i(t)) telescope exactly:

\[
F_t(p)=\sum_i C_i(t).
\]

If (p_i=\Pr[i\in S]=\operatorname{Inf}_i(f)), then (p_i=0\Rightarrow C_i(t)=0), and hence some physical coordinate satisfies

\[
\frac{C_i(t)}{p_i}\ge \frac{F_t(p)}{I(f)}.
\]

The full formula and endpoint handling are in `ANNEALED_UPPER_SET_ENVELOPE.tex`.

## Critical-maximizer consequence

Let (f) attain (c_n=R=H(f)/I(f)).  Combining the envelope with the proved A052 persistence theorem, at (t=1/2),

\[
\frac{C_i(1/2)}{p_i}
\ge \frac{F_{1/2}(p)}{I(f)}
\ge \frac{R-2}{4}-\frac{1}{2\ln2}
+\frac{\mathbb E\operatorname{Var}(g)+\tfrac12\mathbb E b(g)}{I(f)}
\]

for at least one (i), where (b(g)=\widehat g(\varnothing)^2\log_2(1/\widehat g(\varnothing)^2)).  Therefore an unbounded sequence of critical ratios would force a coordinate-level conditional-absence charge growing at least as (R/4-O(1)).  For (R>4), the prior all-block theorem already gives (p_i<1/2) for every nontrivial coordinate, so the witness is neither high-influence nor spectrally determined.

This is the requested useful-coordinate alternative, not yet a structural contradiction.

## Verification

Command:

```text
python3 verify_envelope.py
```

`verify_envelope.py` independently enumerates all 65,812 Boolean truth tables through four variables (65,804 nonconstant).  For every function it computes literal physical restrictions and verifies:

- (F_{1/2}(p)-\mathbb E U(f_{J,X})\ge0);
- the coordinate charges telescope to (F_{1/2});
- \(\max_i C_i/p_i\ge F_{1/2}/I\).

The minimum envelope margin was zero (allowed equality), the largest numerical chain error was (8.89\times10^{-16}), and the minimum coordinate-witness margin was zero.  Fixed-(n) maximizers were also checked against the full persistence inequality, including variance and (b(g)).  Named controls include the four-bit sparse point defect, a disjoint near-tensor of two two-bit point defects, a fresh selector, and a parity atom.  Exact output is archived in `CHECK.out`.

The enumeration is diagnostic; the theorem itself is analytic and all-dimensional.

## Previous bound versus new bound

- Previous A052 state: a lower persistence bound forced large average (U/I) on a restriction frontier, but there was no independently derived upper-set envelope or coordinate-local consequence.
- New state: the frontier obeys the exact phase-free upper envelope (\mathbb EU\le F_t(p)), and (F_t) decomposes into nonnegative physical-coordinate charges.  Thus high critical ratio forces a named coordinate with a quantitatively large normalized charge.
- What did not move: no universal constant bounds (C_i/p_i) on maximizer spectra.

## Falsifier and scope checks

- **Parity-zero erasure:** a parity spectral atom has (F_t=0); the checker confirms equality.  The theorem does not invent a payment where restriction phases erase it.
- **Sparse point defect / rare activation:** the bound retains the nonflat terminal spectrum and all logarithms; the four-bit maximizer has (F/I\approx0.73188), not zero.
- **Near tensor:** the disjoint two-block control is checked directly; no false shared-input additivity is assumed.
- **Fresh selector/addressing:** checked as a genuine three-bit Boolean function; no selector-only payment is asserted.
- **Arbitrary spectral laws:** the envelope holds for laws, but the critical consequence is asserted only for genuine Boolean maximizers.  An arbitrary law is not a FEI counterexample or a Boolean critical family.

## Exact remaining obstacle and next action

The unpaid lemma is now:

> For every ratio-critical Boolean spectrum, prove that every physical coordinate satisfies (C_i(1/2)\le Kp_i) for an absolute (K) (equivalently, bound the maximizing witness selected above), or construct a genuine Boolean critical family for which the maximum normalized charge diverges.

Together with the displayed lower witness, the first alternative would bound (R\le 4K+2+2/\ln2) (with the retained terminal terms only improving this).  A merely existential low-charge coordinate would not suffice.  The next attempt should attack the maximum coordinate charge using the all-block erasure inequalities and Boolean signed-convolution constraints, not by replacing (p) with an arbitrary distribution.

## Review and routing

- Status: proved by this run, **independent review pending**.
- Requested reviewers: A090 and A094.
- Next consumers: A055, A096, A099, B20.
- Full FEI: **OPEN**.
