Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-FAMILY METRIC MOVED: certified `X_{3,4}` gap `>3123709/100000000 = 0.03123709` -> `>870003/25000000 = 0.03480012`; parent Benjamini–Schramm source remains OPEN/PARTIAL. Auxiliary delta: the certified `p_u` floor moves from `383213/5000000 = 0.0766426` to `8020563/100000000 = 0.08020563`, while the exact `p_c` upper certificate `4540551/100000000` is unchanged.**

# PROB10-09 — Żuk's surface-group spectral bound sharpens the frozen nonbacktracking certificate

## 0. Frozen source, continuity, ownership, and consumed evidence

The owner-frozen parent is unchanged:

\[
\forall G=\operatorname{Cay}(\Gamma,S),\qquad
\Gamma\text{ finitely generated and nonamenable},\qquad
p_c(G)<p_u(G)
\]

for iid **bond** percolation on every locally finite Cayley graph. This run does not substitute any planar site-percolation statement. The universal source remains **OPEN / PARTIAL**.

The required pre-refocus R20 handoff already exists and was re-read:

- `runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`, blob `6e1b9e54cbc01461d32b523854c3bd82e50bfd04`.

It preserves R20's frozen predecessor states and artifacts: I0100 Paley one-localization `p_max=1213`, KNSV `N_sep>11`, and BMO `n_all=9`. This run does not research or overwrite those predecessor claims.

Controlling / consumed repository evidence:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- current `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`, blob `ee8bde8735e84ff75d3a625fed61e9bafbefd64f`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`, blob `d94127841f3b335a32b7936b86d8dee7a6b8d093`;
- immediate predecessor `runs/prob10_2026-09-20/PROB10-09/2026-09-20T03-58-00Z_bcch_surface_spectral_gap_upgrade_91c7e4.md`, blob `c3778ff00de5865bae1439b5a54f379521dda7a3`;
- neighboring active percolation route `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T05-50-00+0300__t09-triangle-fibre-degree9-sl-n-gap.md`, blob `589025d7c772ff9f099ea216f55275a041a08527`.

The June archive's previously attempted routes remain consumed history rather than fresh ideas: normalized finite-set escape, the BK finite-volume/boundary dichotomy, killed-SAW criteria, deterministic boundary-energy bounds, the combined escape criterion, regular-tree calibration, nonbacktracking polynomial transfer, product stress tests, quotient/fibre-shell attempts and bridge criteria. This iteration uses a new external spectral input inside the already-delimited standard-surface-product quantitative lane.

The old alias `D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)` is still recovered by repository search as a HARD famous source alias. No canonical claim file was found assigning this exact quantitative `X_{3,4}` surface-product lane to another worker. NM13-11's current route is different: free-core/complement and triangle-fibre subgroup constructions on higher-rank groups. No neighboring claim is edited or absorbed here.

## 1. Current source / prior-art refresh

The bounded source refresh on 20 September 2026 preserves the following distinctions.

1. Hutchcroft, `https://arxiv.org/abs/1804.10191`, proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs. This is known and not a fleet result.
2. Hutchcroft–Pan, `https://arxiv.org/abs/2409.12283`, gives subgroup-relativized uniqueness-threshold results for important additional classes, not the universal all-Cayley theorem.
3. Terlov–Timár, `https://arxiv.org/abs/2502.02560`, concerns weighted amenability and a relaxed weighted/nonunimodular threshold statement, not the frozen universal target.
4. Choi–Seo, `https://arxiv.org/abs/2508.08932`, proves a nonuniqueness phase for **every Cayley graph of an acylindrically hyperbolic group**. This is a major known extension and must not be presented as new here.
5. Peres's 2000 product theorem already gives qualitative nonuniqueness for nonamenable Cartesian products. Therefore no qualitative novelty is claimed for the surface-product family used below; the tracked object is an explicit quantitative certificate/mechanism.
6. The 2026 planar-site work, e.g. `https://arxiv.org/abs/2601.09958`, studies a different site-percolation problem and is not substituted for the bond-Cayley conjecture.
7. A bounded fresh search did not locate a 2026 primary source announcing the universal frozen theorem. This is negative search evidence only, not a priority or worldwide novelty certificate.

The new quantitative input is old but stronger than the genus-four estimate used in the immediate predecessor:

- Andrzej Żuk, *A remark on the norm of a random walk on surface groups*, Colloq. Math. **72** (1997), 195--206, DOI `10.4064/cm-72-1-195-206`. For the standard genus-`g` surface group with the usual symmetric `4g`-element generating set and normalized simple-random-walk operator `M_g=A_g/(4g)`, Theorem 1 states
  \[
  \|M_g\|\le \frac1{\sqrt g}.
  \tag{1.1}
  \]
- Bartholdi--Cantat--Ceccherini-Silberstein--de la Harpe, `https://arxiv.org/abs/math/0612409`, records the same normalization and the historical spectral bounds.
- For genus 3, retain the sharper published Nagnibeda upper bound as quoted in Bartholdi's later summary: `||M_3|| <= 0.552792`.

The 04:53 idea note used the secondary source's strict `<` typography for Żuk's bound. The primary paper states the safe non-strict inequality (1.1). This was corrected before the final proof in `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T04-56-00Z_zuk_surface_spectral_erratum.md`. The proof below uses only `<=`; the exact certificate has strict slack, so no numerical conclusion changes.

## 2. Frozen metric before / after and auxiliary mechanism delta

Freeze the same standard surface-product Cayley graph as the preceding runs:

\[
X_{3,4}=\operatorname{Cay}(\Gamma_3\times\Gamma_4,
(S_3\times\{1\})\cup(\{1\}\times S_4)),
\]

where `Gamma_g` is the closed orientable genus-`g` surface group and `S_g` is its standard symmetric `4g`-element generating set.

### Before

The predecessor had the exact `p_c` certificate

\[
p_c(X_{3,4})<\frac{4540551}{10^8}=0.04540551,
\tag{2.1}
\]

and the certified uniqueness-side floor

\[
p_u(X_{3,4})>\frac{383213}{5000000}=0.0766426.
\tag{2.2}
\]

Thus

\[
p_u-p_c>\frac{3123709}{10^8}=0.03123709.
\tag{2.3}
\]

### After

This run proves

\[
\boxed{
 p_u(X_{3,4})>\frac{8020563}{10^8}=0.08020563.
}
\tag{2.4}
\]

Together with the unchanged exact (2.1),

\[
\boxed{
 p_u(X_{3,4})-p_c(X_{3,4})
 >\frac{870003}{25000000}=0.03480012.
}
\tag{2.5}
\]

The frozen metric therefore moves by

\[
0.03480012-0.03123709
=\frac{356303}{10^8}
=0.00356303.
\tag{2.6}
\]

**Parent source status:** unchanged `OPEN/PARTIAL`; no all-Cayley proof.

**Auxiliary mechanism delta:** the `p_u` floor moves `0.0766426 -> 0.08020563`; the exact full-tree `p_c` certificate is unchanged. The all-genus surface-product adjacency criterion is also sharpened in Section 6.

## 3. Idea before code and three genuinely different routes

The required idea was written before code at

`artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T04-53-00Z_zuk_surface_spectral_idea.md`.

### Route A — import Żuk's all-genus surface spectral estimate: SUCCESS

The immediate predecessor used the 1997 BCCH Section-3 genus-four estimate

\[
\|A_4\|\le 1+2\sqrt{14}\approx8.4833.
\]

Żuk gives instead

\[
\|A_4\|=16\|M_4\|\le 8.
\]

Keeping Nagnibeda's sharper genus-three estimate yields a strictly smaller certified adjacency-norm upper bound for `X_{3,4}`, hence a larger nonbacktracking `p_{2->2}` floor. This is the metric-moving route.

### Route B — split the nonbacktracking transfer by Cartesian-product colors: EXACT OBSTRUCTION

A tempting idea is to replace the scalar adjacency bound by a two-color transfer that tracks whether the last step lies in the genus-three or genus-four factor. This does **not** improve the exponential endpoint-kernel estimate if its only inputs are the two factor adjacency norms.

Indeed

\[
A_{3,4}=A_3\otimes I+I\otimes A_4.
\tag{3.1}
\]

The factors are self-adjoint; hence the spectrum of the tensor sum is the Minkowski sum of the factor spectra. The standard surface Cayley graphs are bipartite, so each factor spectrum is symmetric. Writing `rho_i=||A_i||`, the positive spectral edge `rho_3+rho_4` belongs to the spectrum of (3.1), and therefore

\[
\|A_{3,4}\|=\rho_3+\rho_4.
\tag{3.2}
\]

For a `D`-regular graph, the endpoint kernels of nonbacktracking walks are polynomials `N_n=P_n(A)` satisfying the second-order recurrence in Section 4. At a spectral edge `lambda=||A||>2\sqrt{D-1}`, the polynomial recurrence itself grows at the larger characteristic root `beta_D(lambda)`. Thus a color-split reformulation that uses no information beyond `rho_3,rho_4` cannot lower the exponential `l^2` growth below the scalar value `beta_D(rho_3+rho_4)`: the scalar spectral edge already realizes it. A genuine improvement must exploit extra path restrictions/cancellations or sharper factor spectral data.

This is an obstruction, not a new gap theorem.

### Route C — improve `p_c` from local cone types instead of a free subgroup: EXACT LOCAL OBSTRUCTION

A second independent idea is to replace the embedded Freiheitssatz tree by a larger geodesic subtree in the genus-three surface Cayley graph. The local cone-type information alone is insufficient.

For the standard genus-three Cayley graph, the usual word-length cone picture has vertices with one or two predecessors. Since the degree is 12, every nonidentity vertex has at least ten outward incidences. If `U` is a set in one sphere and `N_+(U)` its next-sphere neighbors, every next-sphere vertex has at most two predecessors, so double counting gives only

\[
10|U|\le2|N_+(U)|,
\qquad |N_+(U)|\ge5|U|.
\tag{3.3}
\]

Hall's `b`-matching consequence of (3.3) can force at most five distinct assigned children per parent from these local facts. That corresponds only to a rooted 5-ary tree / `T_6` scale, strictly worse than the already embedded `T_10` supplied by Freiheitssatz. Therefore local predecessor counts cannot improve the present `p_c` side. A better cone-tree route would need a stronger **global finite-state injective geodesic language** or sharper incidence inequalities, not merely the `1/2` predecessor bound.

No unproved collision-free language is asserted here.

The three routes are materially distinct: external random-walk spectral input, operator-state splitting with a spectral-edge obstruction, and a combinatorial geodesic-tree attempt with a Hall/double-counting obstruction.

## 4. Nonbacktracking transfer, stated self-containedly

Let `G` be a simple `D`-regular graph with adjacency operator `A`, put `Q=D-1`, and let `N_n(x,y)` count length-`n` nonbacktracking walks from `x` to `y`. Then

\[
N_0=I,\qquad N_1=A,
\]

and after the standard `n=2` initial correction the endpoint kernels satisfy

\[
N_n=A N_{n-1}-Q N_{n-2},\qquad n\ge3.
\tag{4.1}
\]

Thus `N_n=P_n(A)` for explicit real polynomials whose exponential growth at a scalar `lambda` is controlled by the roots of

\[
r^2-|\lambda|r+Q=0.
\]

For `R>=0`, define

\[
\beta_D(R)=
\begin{cases}
\sqrt Q,&R\le2\sqrt Q,\\[1mm]
\dfrac{R+\sqrt{R^2-4Q}}2,&R>2\sqrt Q.
\end{cases}
\tag{4.2}
\]

Spectral calculus applied to (4.1) gives

\[
\limsup_{n\to\infty}\|N_n\|_{2\to2}^{1/n}
\le \beta_D(\|A\|).
\tag{4.3}
\]

For bond percolation, every connection `x<->y` contains an open self-avoiding path, hence a nonbacktracking path. The union bound gives entrywise

\[
T_p(x,y):=\mathbb P_p(x\leftrightarrow y)
\le \sum_{n\ge0}p^nN_n(x,y).
\tag{4.4}
\]

For nonnegative kernels, entrywise domination implies the same operator-norm domination after replacing a vector by its absolute value. Therefore whenever

\[
p\,\beta_D(\|A\|)<1,
\]

the right side of (4.4) converges in `l^2` operator norm and `T_p` is bounded. Consequently

\[
p_{2\to2}(G)\ge\beta_D(\|A\|)^{-1}.
\tag{4.5}
\]

For every infinite Cayley graph,

\[
p_{2\to2}(G)\le p_u(G).
\tag{4.6}
\]

Indeed if `p>p_u`, there is a unique infinite cluster a.s. and `theta(p)>0`. FKG gives

\[
T_p(x,y)\ge
\mathbb P_p(x\leftrightarrow\infty,\ y\leftrightarrow\infty)
\ge\theta(p)^2.
\]

A kernel bounded below by a positive constant on an infinite vertex set cannot act boundedly on `l^2`, proving (4.6).

## 5. Exact `X_{3,4}` improvement

For genus 3, retain the published Nagnibeda bound

\[
\|M_3\|\le0.552792=\frac{69099}{125000}.
\]

Since `A_3=12M_3`,

\[
\|A_3\|\le
12\frac{69099}{125000}
=\frac{207297}{31250}
=6.633504.
\tag{5.1}
\]

For genus 4, Żuk's theorem gives

\[
\|A_4\|=16\|M_4\|\le 8.
\tag{5.2}
\]

The Cartesian adjacency operator is the commuting tensor sum

\[
A_{3,4}=A_3\otimes I+I\otimes A_4,
\]
so

\[
\|A_{3,4}\|
\le\frac{207297}{31250}+8
=\frac{457297}{31250}
=:R_*.
\tag{5.3}
\]

The graph is `D=12+16=28` regular, hence `Q=27`. Set

\[
p_*:=\frac{8020563}{10^8}=0.08020563,
\qquad
z_*:=p_*^{-1}=\frac{10^8}{8020563}.
\tag{5.4}
\]

The exact checker executed this run verifies

\[
z_*^2-27
=\frac{8263105367401837}{64329430836969}>0,
\tag{5.5}
\]

so `z_*>sqrt(27)`, and

\[
z_*^2-R_*z_*+27
=\frac{558322963}{64329430836969}>0.
\tag{5.6}
\]

For `z>sqrt(27)`, the function

\[
f(z)=z+\frac{27}{z}
\]

is strictly increasing. Equation (5.6) is equivalent to

\[
R_*<z_*+\frac{27}{z_*}.
\]

Therefore the larger positive root of

\[
r^2-R_*r+27=0
\]

is strictly smaller than `z_*`. Since the actual adjacency norm is at most `R_*` and `beta_28(R)` is nondecreasing in `R`,

\[
\beta_{28}(\|A_{3,4}\|)<z_*.
\tag{5.7}
\]

Combining (4.5), (4.6), and (5.7),

\[
\boxed{
 p_u(X_{3,4})\ge p_{2\to2}(X_{3,4})
 >\frac{8020563}{10^8}.
}
\tag{5.8}
\]

The predecessor's exact full-tree fibre certificate remains

\[
p_c(X_{3,4})<\frac{4540551}{10^8}.
\tag{5.9}
\]

Subtracting (5.9) from (5.8) proves

\[
\boxed{
 p_u(X_{3,4})-p_c(X_{3,4})
 >\frac{8020563-4540551}{10^8}
 =\frac{870003}{25000000}
 =0.03480012.
}
\tag{5.10}
\]

This is a restricted-family quantitative theorem and therefore remains **PARTIAL** for the universal Benjamini--Schramm conjecture.

## 6. Structural extension across the standard surface-product family

Żuk also sharpens the reusable all-surface-product operator criterion.

For the standard genus-`g` surface Cayley graph define the safe factor bounds

\[
U_2:=8(0.662816)=5.302528,
\qquad
U_3:=12(0.552792)=6.633504,
\]

using the published Nagnibeda bounds for genera 2 and 3, and for `g>=4` use Żuk

\[
U_g:=4\sqrt g,
\qquad \|A_g\|\le U_g.
\tag{6.1}
\]

For

\[
X_{g,h}=\operatorname{Cay}(\Gamma_g\times\Gamma_h,
(S_g\times\{1\})\cup(\{1\}\times S_h)),
\]

which is `D=4g+4h` regular,

\[
\|A_{g,h}\|\le U_g+U_h.
\tag{6.2}
\]

Hence the self-contained nonbacktracking transfer of Section 4 gives the complete structural inequality

\[
\boxed{
 p_u(X_{g,h})\ge p_{2\to2}(X_{g,h})
 \ge \beta_{4g+4h}(U_g+U_h)^{-1}.
}
\tag{6.3}
\]

For every factor of genus at least 4 this improves the predecessor's BCCH Section-3 input `1+2 sqrt(4g-2)` whenever `4sqrt(g)` is smaller; in particular it strictly improves the frozen genus-four factor. This is a quantitative structural extension, **not** a claim that the qualitative product nonuniqueness class is new.

## 7. Exact execution and artifact record

Idea-before-code:

- `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T04-53-00Z_zuk_surface_spectral_idea.md`.

Primary-source inequality-label correction:

- `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T04-56-00Z_zuk_surface_spectral_erratum.md`.

Exact checker and archived output:

- `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T04-53-00Z_zuk_surface_spectral_check.py`;
- `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T04-53-00Z_zuk_surface_spectral_check.out`.

The checker was executed with exact rational arithmetic. Its archived terminal line is

`ALL_EXACT_CHECKS_PASS`.

It verifies exactly:

- `A3_upper = 207297/31250`;
- `Rbar = 457297/31250`;
- `z^2-27 = 8263105367401837/64329430836969 > 0`;
- `z^2-Rbar*z+27 = 558322963/64329430836969 > 0`;
- `new_gap = 870003/25000000 = 0.03480012`;
- `gap_improvement = 356303/100000000 = 0.00356303`.

The output file's label `A4_strict_upper = 8` inherited the secondary-source strictness wording; the separate erratum records that the final proof uses the primary theorem's safe `A4_upper <= 8`. Because the quadratic slack is strictly positive at the endpoint `Rbar`, the arithmetic certificate and all resulting inequalities remain valid unchanged.

This is a **self-check**, not an independent audit.

## 8. What remains open

The full frozen source still asks for

\[
p_c(G)<p_u(G)
\]

for **every** locally finite Cayley graph of **every** finitely generated nonamenable group. This run proves nothing universal across arbitrary nonamenable Cayley graphs. Surface-product graphs are a restricted family, and their qualitative nonuniqueness was already known from product literature.

The genuine universal obstruction remains that the two sides of the proof use highly family-specific structure:

1. the `p_c` upper bound uses an explicit large free-tree product subgraph supplied by surface-group algebra; and
2. the `p_u` lower bound uses an explicit adjacency spectral estimate strong enough to make the nonbacktracking resolvent converge above that `p_c` witness.

For a general nonamenable Cayley graph, neither a sufficiently strong free/fibre subgraph nor a universal inequality comparing a constructive `p_c` upper witness against `beta_D(||A||)^{-1}` is currently available. Simply naming `p_c<p_{2->2}` as the missing lemma would not be progress; the next useful route must bridge these quantities under a new structural hypothesis or find a different two-point comparison.

The color-split obstruction in Section 3 shows that merely repackaging the same factor adjacency norms into a larger transfer matrix cannot improve the surface-product uniqueness estimate. The cone-type obstruction shows that local outward-degree data alone does not improve the present `p_c` tree witness. These narrow the next iteration toward either sharper global geodesic automata / subgroup comparison or genuinely finer nonbacktracking information than `||A||`.

## 9. Status and ledger delta

```yaml
ledger_delta:
  worker: PROB10-09 / R20
  source: Benjamini-Schramm nonuniqueness-phase conjecture for iid bond percolation on Cayley graphs
  parent_status_before: OPEN/PARTIAL
  parent_status_after: OPEN/PARTIAL
  frozen_graph: X_{3,4} standard Cayley graph of Gamma_3 x Gamma_4
  metric: certified lower bound on p_u(X_{3,4}) - p_c(X_{3,4})
  metric_before: 3123709/100000000 = 0.03123709
  metric_after: 870003/25000000 = 0.03480012
  metric_delta: 356303/100000000 = 0.00356303
  auxiliary_before: p_u > 383213/5000000 = 0.0766426; p_c < 4540551/100000000
  auxiliary_after: p_u > 8020563/100000000 = 0.08020563; p_c < 4540551/100000000
  new_mechanism: Zuk all-genus surface random-walk spectral bound inside nonbacktracking two-point transfer
  structural_scope: quantitative p_u lower criterion for every standard surface-product X_{g,h}, with Zuk factor bound for g or h >= 4
  negation_test: primary-source normalization and non-strict inequality checked; endpoint slack remains positive
  failed_or_blocked_routes:
    - product-color nonbacktracking split cannot beat scalar spectral edge using only factor adjacency norms
    - local cone predecessor counts force only a 5-child Hall guarantee, worse than existing T_10 Freiheitssatz fibre
  exact_test: ALL_EXACT_CHECKS_PASS
  validation: SELF_CHECK_ONLY
  independent_audits: []
  unresolved_full_gap: no universal mechanism comparing p_c to p_u/p_2to2 for arbitrary nonamenable Cayley graphs
```

No schedule, email, Drive, public-posting, permission, or neighboring-claim changes were made.