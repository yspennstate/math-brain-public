# account03/B15 — iterating the shared-core gate obstruction

**Run:** `20260922T012556Z-account03-B15-r11`  
**Outcome:** `CANDIDATE_REFUTED` for freezing the all-gate center cap at the preceding finite shared-graft witness; new certified FEI lower bound.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository sources were read through the authorized connector, but no authenticated mathematical-brain retrieval/context was consumed.

## 1. Exact live target and candidate version

The current owner convergence order supersedes the older packet-only B15 duty. The common target is the all-gate inequality

\[
\Gamma(p_{out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for one symmetric nonnegative potential and every Boolean gate, arity and product bias. At uniform bias for a balanced gate, (G) reduces exactly to

\[
H(G)\le \Gamma(1/2)(I(G)-1).
\tag{1.1}
\]

Thus every explicit balanced gate supplies a lower bound on the center cap through

\[
R(G):=\frac{H(G)}{I(G)-1}.
\tag{1.2}
\]

Relative to the old read-once reference potential with center `C0=6.4548`, the owner's comparable gate margin is

\[
c_G=4(R(G)-C_0)
\tag{1.3}
\]

at such a balanced uniform point, because the Poincare margin denominator is `(I-1)/4`.

**Prior missing implication / candidate version.** The latest named other-account result consumed is account01/B18,

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`, blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`.

It refutes the earlier `PRIME-GATE-LIFT` cap and constructs an actual balanced monotone Boolean gate `F2` with certified

\[
R(F_2)>6.521850763518463531668608228451477683404661344.
\tag{1.4}
\]

It also proves the exact recurrence needed to ask whether this finite witness is stable under another round of the *same source-valid shared-coordinate mechanism*. The decisive question attacked here is therefore:

> Can the account01/B18 shared-core transformation be iterated on its own output with a strictly positive certified gain, thereby falsifying any successor that freezes `Gamma(1/2)` at the `F2` value?

## 2. Exact recurrence consumed and applied

Account01/B18 proves the following source-exact transformation. For a balanced monotone gadget with

\[
R=\frac{H}{I-1},
\]

influence `I`, and a designated singleton Fourier coefficient `c`, first take its depth-four disjoint self-composition and then apply the nine-host shared-core graft. Set

\[
\alpha=\frac9{256},\qquad B=\frac{257}{256},\qquad d_0=\frac{133}{128},
\]

\[
K(b)=H_{core}(b)+\alpha\bigl[-\phi(b^2)+16(1-b^2)\bigr],
\qquad \phi(t)=-t\log_2t.
\]

Then exactly

\[
I'=\frac{261}{128}+\alpha(I^4-1),
\tag{2.1}
\]

\[
c'=\frac{57}{256}+\frac{c^4}{256},
\tag{2.2}
\]

and

\[
\boxed{
R'-R=\frac{K(c^4)-d_0R}{\alpha I^4+B}.
}
\tag{2.3}
\]

Every step preserves an actual finite balanced monotone Boolean function; this is not a non-Boolean spectral relaxation. The physical lattice/core Fourier coefficients are the exact ones from the source-bound construction, not interpolated packet masses.

For `F2`, account01/B18 supplies the exact influence

\[
I_2=\frac{784028312243315011737}{295147905179352825856}
\]

and the preceding singleton recurrence, so equations (2.1)--(2.3) can be applied without introducing a new heuristic quantity.

## 3. New certified calculation: four further positive rounds

`CHECKER.py` reconstructs the same nine-bit core and host masks used by the peer source, uses exact `Fraction` coefficients, and evaluates every logarithm with outward-rounded 100-digit decimal intervals. `ln` is enclosed by a finite atanh series with an explicit positive remainder; `log2` is then obtained by interval division by the similarly enclosed `ln 2`. The peer `F2` displayed certified value is widened by a full `1e-45` on each side before it is consumed.

The recurrence yields:

| gate | certified lower bound for `R=H/(I-1)` | certified gain lower bound |
|---|---:|---:|
| `F3` | `6.521850915855717179433677705767749220354801820759...` | `1.5233725364776506947e-7` |
| `F4` | `6.521850948564444896549107534570775248275596929863...` | `3.2708727717115429828e-8` |
| `F5` | `6.521850949550445945815392134063644137837370964840...` | `9.8600104926628459e-10` |
| `F6` | `6.521850949550448184840160538860511501288648868305...` | `2.2390247684047968e-15` |

Every displayed gain is strictly positive after outward rounding. Hence

\[
\boxed{
R(F_6)>6.5218509495504481848401605388605.
}
\tag{3.1}
\]

Balanced disjoint self-composition of `F6` gives finite Boolean functions with ordinary `H/I` approaching `R(F6)`. Therefore the present construction certifies

\[
\boxed{
C_{FEI}>6.5218509495504481848401605388605.
}
\tag{3.2}
\]

This is a lower bound, not a finite universal upper bound and not a proof of FEI.

In the owner's requested gate-margin units, (1.3) gives

\[
\boxed{
c_{F_6}>0.2682037982017927393606421554420.}
\tag{3.3}
\]

This is about `60.99` times the current read-once certificate's quoted worst AND margin `0.0043974201`. The comparison is only to explain scale: the explicit balanced gate itself already falsifies any assertion that the read-once/AND margin is globally extremal.

## 4. Exact failed claim and what survives

**REFUTED.** Any all-gate candidate with center cap

\[
\Gamma(1/2)\le 6.5218509495504481848401605388605
\]

cannot satisfy (G) universally, because the actual balanced Boolean gate `F6` violates (1.1). In particular, freezing the successor potential at the preceding `F2` cap is decisively false.

This does **not** refute the gate reformulation itself. It also does not refute the account02/B17 composition cocycle. That cocycle instead strengthens the implication: if `F6` decomposes as a disjoint functional composition, some composition-prime factor inherits a gate-margin obstruction at least as large as the composite's normalized margin. The new obstruction therefore cannot be dismissed as accumulation of mild disjoint gates.

The mechanism that raises the lower bound is the shared-coordinate graft, exactly the interference mechanism excluded from ordinary disjoint composition.

## 5. Replacement obligation and next attack

The recurrence reveals why simply setting the potential center equal to the newest finite witness is unstable. The designated singleton coefficient evolves by

\[
c_{r+1}=\frac{57}{256}+\frac{c_r^4}{256},
\]

while the sign of the next ratio increment is controlled by

\[
K(c_r^4)-\frac{133}{128}R_r.
\tag{5.1}
\]

The replacement obligation is therefore **not** another finite cap chosen from the latest witness. Before proposing a new universal potential envelope, the team should analyze the iterated shared-core family (and, if useful, the same construction with a different self-composition depth) to obtain a rigorous supremum or a further explicit obstruction. Only after that should the all-prime/all-bias inequality be attacked at a cap above the entire certified family.

The current calculation strongly suggests rapid saturation for the fixed depth-four map, but no limiting value is promoted here: the theorem proved in this run is only the four finite strict gains and the lower bound (3.2).

## 6. Status fields for the common proof programme

- `candidate_version`: all-gate center-cap successor after account01/B18 `F2` / prior `PRIME-GATE-LIFT` repair.
- `prior_missing_implication`: determine whether the newest shared-graft witness is stable under its own exact source-valid transform before freezing another center cap.
- `new_proved_inference`: four further source-valid shared-graft rounds have rigorously positive gains; `C_FEI > 6.5218509495504481848401605388605`.
- `exact_failed_claim`: a universal all-gate potential can have center at or below the preceding `F2` witness; more generally every cap at or below (3.1) is impossible.
- `replacement_obligation`: analyze/upper-control the iterated shared-coordinate obstruction before fixing a universal center; then prove the all-prime/all-bias gate inequality or exhibit another larger gate margin.
- `consumed_peer_artifact`: account01/B18 `20260922T0117Z-recursive-shared-graft/REPORT.md`, blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`.
- `applied_to_claim`: uniform balanced specialization of the owner's all-gate inequality, retaining the actual Boolean shared-coordinate construction.
- `next_recipient`: account03/B18 (Campaign-B/gate integration lead), with account02/B17 as the prime-gate/cocycle adversary partner.
- `implication_to_full_FEI`: lower-bound/candidate-elimination only. Full FEI remains **OPEN** until one finite dimension-independent upper bound is proved for all gates/biases.

No novelty or publication-priority claim is made here. The external/source-bound seed provenance and all prior construction provenance remain as recorded in the consumed peer report.
