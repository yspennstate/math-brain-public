# MOC4 account04/B08 — pair-specific endpoint roofs and exact support-face degeneracy

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal 4-by-4 Marcus–de Oliveira target  
**Worker:** account04/B08  
**Candidate:** `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN_RESEARCH`.

## 1. Source-exact target and live proof chain

For complex normal `4 x 4` matrices with spectra `a_1,...,a_4` and `b_1,...,b_4`, the target is

\[
\det(A+B)\in\operatorname{conv}\left\{z_\sigma:=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\tag{MOC4}
\]

Fix a support direction `eta` and write

\[
H_\sigma=\Re(\eta z_\sigma),\qquad M=\max_\sigma H_\sigma,
\]

and for a true unitary `U`,

\[
h(U)=\Re\!\left(\eta\det(D_a+UD_bU^*)\right).
\]

The exact source boundary is the MOC4 target in `scheduled_tasks/work/shared/collective-open-problems-2026-09-22/TARGETS.md`, which records the checked 2025 Bebiano–da Providencia survey, Drury's weakened n=4 result, and the 2026 variational obstruction. No unrestricted Marcus–de Oliveira claim is made.

The current chain uses these completed campaign inputs.

1. **Own preceding theorem, account04/B08, `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`**, report blob `ccc5358d81a9432f3764a9a89be9a01c6bb54e26`. For every row or column transposition `tau`, the exact arithmetic data of the averaged pair `(U,tau U)` admits one genuine common probability lift to the 24 permutation endpoints. It already implies `(h(U)+h(tau U))/2 <= M`.
2. **Campaign lead account03/B07**, run `20260922T013930Z-account03-B07-MOC4-r11`, report blob `47f09f9f722aa8501330ca532a2ca261474c681c`. A common permutation lift for an individual zero-entry unitary is false; hence a valid argument must use the pair-symmetrized structure or the true maximizer equations, not resurrect a universal coefficient lift.
3. **Assigned partner account01/B09**, run `20260922T024937Z-account01-B09-MOC4-r12`, report blob `5d9042a1e0e582c4b9da2a840c23ce3b6b60dcf6`, candidate `MOC4-SIMPLE-COMPLEX-EVEN-LIFT-v1`. It gives a dense true orthogonal unitary and simple nonreal spectra for which a universal positive exterior-square endpoint lift fails by an exact facet, while the determinant has an explicit positive three-vertex MOC4 certificate. Thus any surviving proof must be maximizer-local rather than an unconditional channel-lift theorem.
4. **account03/B20, `MOC4-PAIR-TWIRL-TWO-POINT-v1`**, handoff `20260922T0305Z-account03-B20-pair-twirl-two-point.md`. Summing the preceding pair inequality over the six transpositions converts a positive support gap into a quantitative pair-Hessian trace collar.

The new result sharpens the pair inequality from the crude endpoint roof `M` to the exact roof determined by the two-point transposition matching on `S_4`.

## 2. Exact pair-specific endpoint roof

For a row transposition `tau` acting on row labels, define

\[
R^{\rm row}_\tau
:=\max_{\sigma\in S_4}\frac{H_\sigma+H_{\sigma\circ\tau}}2.
\tag{1}
\]

For a column transposition define

\[
R^{\rm col}_\tau
:=\max_{\sigma\in S_4}\frac{H_\sigma+H_{\tau\circ\sigma}}2.
\tag{2}
\]

### Theorem — `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`

For every true `U in U(4)` and every row transposition `tau`,

\[
\boxed{\frac{h(U)+h(\tau U)}2\le R^{\rm row}_\tau.}
\tag{3}
\]

For every column transposition,

\[
\boxed{\frac{h(U)+h(U\tau)}2\le R^{\rm col}_\tau.}
\tag{4}
\]

In particular, if `H_(1)>=H_(2)>=...` are the endpoint support values in decreasing order, then

\[
R^{\rm row}_\tau,R^{\rm col}_\tau\le\frac{H_{(1)}+H_{(2)}}2,
\tag{5}
\]

so every pair twirl is bounded by the average of the two largest target endpoint supports, not merely by the largest one.

### Proof

Consider a row transposition. By `MOC4-PAIR-SYMMETRIZED-COMMON-LIFT-v1`, there is a probability law `lambda` on `S_4` whose endpoint data reproduce the exact averaged one-minor, complementary-pair and signed-standard data of `(U,tau U)`. Since the determinant support is linear in those data,

\[
\alpha:=\frac{h(U)+h(\tau U)}2=\sum_\sigma\lambda_\sigma H_\sigma.
\tag{6}
\]

The averaged data are invariant under swapping the same two row labels. Therefore the pushforward of `lambda` by

\[
\sigma\mapsto\sigma\circ\tau
\]

is another lift of the same averaged data. Average the two laws. The resulting law `\widetilde\lambda` is still an exact lift and satisfies

\[
\widetilde\lambda_\sigma=\widetilde\lambda_{\sigma\circ\tau}.
\tag{7}
\]

A nontrivial transposition has no fixed permutation under this action, so `S_4` decomposes into twelve two-point orbits `{sigma,sigma o tau}`. Equation (6) can therefore be regrouped as a convex combination of their endpoint averages:

\[
\alpha=\sum_{\{\sigma,\sigma\circ\tau\}}w_{\{\sigma,\sigma\circ\tau\}}
\frac{H_\sigma+H_{\sigma\circ\tau}}2,
\quad w\ge0,\quad\sum w=1.
\tag{8}
\]

Hence `alpha<=R^row_tau`, proving (3). The column case is identical with the action `sigma -> tau o sigma`. Finally, every two-point orbit contains two distinct permutations, so its average is at most `(H_(1)+H_(2))/2`, proving (5). ∎

This proof uses the actual common unitary through the already-proved pair-symmetrized lift. It does not assume that the data of a single `U` admit a positive endpoint representation, which the lead and partner have refuted.

## 3. Exact characterization of the endpoint-face degeneracy

Define the pair gaps

\[
g^{\rm row}_\tau:=2M-\max_\sigma(H_\sigma+H_{\sigma\circ\tau})
=2(M-R^{\rm row}_\tau)\ge0,
\tag{9}
\]

and analogously `g^col_tau`.

The gap vanishes **if and only if** the maximizing endpoint face contains a transposition edge of the appropriate type. Indeed, `R_tau=M` can occur only if some two distinct paired endpoints both have support `M`; conversely such a maximizing pair gives `R_tau=M`.

Thus endpoint degeneracy is now more precise than merely “the support maximum is nonunique”:

- a support face with several maximizers but no `tau`-adjacent maximizing pair still has `g_tau>0`;
- if the top endpoint is unique, then all twelve row/column pair gaps are strictly positive;
- equality in the pair roof is possible only through a probability lift supported on endpoint pairs that attain the corresponding pair roof.

This is the boundary characterization relevant to the B08 assignment. The transposition Cayley graph on the 24 endpoints, rather than support-face multiplicity alone, controls which endpoint degeneracies can saturate a genuine pair twirl.

## 4. Quantitative collar for a hypothetical support violator

Suppose `U_*` is a global support maximizer and

\[
h(U_*)=M+\gamma,\qquad \gamma>0.
\tag{10}
\]

Then (3) gives, for every row transposition,

\[
h(\tau U_*)\le M-\gamma-g^{\rm row}_\tau,
\tag{11}
\]

hence

\[
\boxed{h(U_*)-h(\tau U_*)\ge2\gamma+g^{\rm row}_\tau.}
\tag{12}
\]

The same holds for columns. On the affine Bloch pair sphere, identity and the label-swap antipode differ by twice the pair radius at a pair-orbit maximum. Therefore the pair curvature/radius is bounded below by

\[
\gamma+\frac{g_\tau}{2}.
\tag{13}
\]

This improves the previous `>=gamma` collar and adds a term coming purely from the target support-face geometry.

There is also an immediate support-independent corollary. If the endpoint maximum is unique and

\[
\delta=H_{(1)}-H_{(2)}>0,
\]

then every `g_tau>=delta`, because every transposition pair uses two distinct endpoints. Thus every violating maximizer satisfies

\[
h(U_*)-h(\tau U_*)\ge2\gamma+\delta
\tag{14}
\]

for all twelve row/column swaps.

## 5. Strengthened Spin(6) Hessian collar

Apply the theorem to the same six column transpositions used by account03/B20. Let

\[
G=\sum_{\tau\in T_6}g^{\rm col}_\tau.
\]

Using that worker's exact notation `s(U)=k+x` and identity

\[
\sum_{\tau\in T_6}s(UP_\tau)=2k+6c,
\]

summing (4) gives

\[
4k+3x+3c\le6M-\frac G2.
\tag{15}
\]

At a violator `k+x=M+gamma`, this is equivalent to

\[
\boxed{2k+3(x-c)\ge6\gamma+\frac G2.}
\tag{16}
\]

Combining with the exact pair-Hessian trace identity quoted by account03/B20,

\[
\operatorname{Tr}H_{\rm pair}=-8[2k+3(x-c)],
\]

gives

\[
\boxed{\operatorname{Tr}H_{\rm pair}\le-48\gamma-4G.}
\tag{17}
\]

If the endpoint maximizer is unique with global endpoint gap `delta`, then `G>=6delta`, and therefore

\[
\operatorname{Tr}H_{\rm pair}\le-48\gamma-24\delta.
\tag{18}
\]

This is a strict quantitative strengthening of the existing curvature collar. It does not by itself contradict global maximality; the remaining proof must combine it with the full Spin(6) stationarity equations and structured six-fiber support coefficients.

## 6. Direct application of the assigned partner's exact adversary

The assigned partner account01/B09's latest exact datum uses

```text
U =
[  636/1105,  -423/1105,   -12/65,   -772/1105 ]
[ 3576/5525,    332/5525, -144/325,  3411/5525 ]
[   164/425,     348/425,      9/25,    -96/425 ]
[      27/85,       -36/85,       4/5,       24/85 ]
```

with simple nonreal spectra

`a=(-4+4i,-i,-3+2i,-4-4i)`,  
`b=(-4-4i,2-i,2-4i,4-i)`.

For the real-part support direction, exact arithmetic gives top endpoint support `M=256`, second support `240`, so `delta=16`. The six row pair gaps are

`186, 16, 24, 168, 50, 302`,

and the six column pair gaps are

`24, 50, 412, 192, 16, 168`.

Their sums are respectively `746` and `862`. Direct exact determinant recomputation verifies every corresponding pair inequality (3)–(4). This is an important negative control: the partner's exterior-square positive endpoint lift is known to fail, yet the new theorem still holds because it uses only the pair-symmetrized lift, which is the genuinely valid structure.

The accompanying standard-library verifier uses `fractions.Fraction`, verifies exact orthogonality, the partner's exact determinant, all 24 endpoint supports, all twelve endpoint pair gaps, and all twelve physical row/column-swap inequalities. Its terminal marker is

`PASS MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`.

The script is a representative exact check; the theorem is the analytic orbit-symmetrization proof above.

## 7. Compact conditional end-to-end argument and first missing implication

A surviving full-proof route is now:

1. If MOC4 fails, separate the determinant from the 24-point hull by a real support direction and choose a global true-unitary maximizer.
2. By the earlier generic strict-support reduction, after an arbitrarily small source-valid perturbation it suffices to treat simple nonzero spectra with a unique maximizing endpoint and a positive target support gap.
3. The present theorem supplies a **strict positive pair-specific endpoint gap on all twelve pair orbits**, hence the stronger quantitative pair and Hessian collars (12) and (17).
4. Apply account01/B07's exact Spin(6) stationarity equations, together with the team's strict odd-overlap/Cartan collars and the exact six-fiber support identity.
5. Exclude such a globally maximizing strict-interior point; continuity then returns the singular/repeated/degenerate cases already covered by the reduction.

The first unpaid implication is therefore sharpened to:

> **`MOC4-GAPPED-STATIONARY-SIX-FIBER-v1` (OPEN).** For a global true-unitary support maximizer with structured spectral coefficients, full Spin(6) stationarity, strict odd-overlap conditions, and positive pair-specific endpoint gaps `g_tau` satisfying the exact collars above, prove the six-fiber target support inequality. Equivalently, construct a genuine source-valid target counterexample satisfying all these conditions.

This is narrower than the already-refuted unconditional positive channel-lift, parity-only, or generic nonmonomial-stationarity routes. No unsupported replacement condition is being counted as closure.

## 8. Status, failures, provenance and non-claims

- `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`: **proved**, conditional only on the already-proved pair-symmetrized common-lift theorem whose proof is in the cited preceding report.
- Pair-support-face saturation is characterized by the presence of a maximizing transposition edge.
- The assigned partner's universal even-channel lift remains **refuted**; the new theorem does not revive it.
- The lead's zero-entry common-lift shortcut remains **refuted**.
- MOC4 remains **OPEN**. No full-proof candidate, publication claim, or n>4 claim is made.
- No benchmark material, held-out answers, credentials, scheduler identifiers, machine-local paths, unrelated private data, email/Drive data, paid model/API, Codex, remote workflow, or public release was used.

Primary recipients: campaign lead account03/B07, assigned partner account01/B09, account03/B20 for the strengthened Hessian collar, and account01/B07 for integration with exact stationarity.
