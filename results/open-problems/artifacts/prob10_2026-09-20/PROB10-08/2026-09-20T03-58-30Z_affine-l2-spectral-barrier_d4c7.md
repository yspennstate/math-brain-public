Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but the runtime exposes no authenticated applied-effort telemetry establishing GPT-6/maximum, so this artifact does not claim it.

# PROB10-08 artifact — exact two-scale spectrum, continuous-time L2 cutoff, and why L2 cannot prove the TV conjecture on the affine stress test

Status: **PROVED auxiliary theorem / source remains OPEN / no TV cutoff claim / independent audit pending / worldwide novelty UNVERIFIED**.

This artifact concerns Justin Salez, arXiv:2508.21055v1, Problem 2.3, under the source's rate-one continuous-time SRW convention. It does **not** concern the posted Abelian Cayley/product-condition target.

## 1. Inputs and nonduplication

The current PROB10 contract, posting exclusions, canonical I0112 claim, R16 handoff, and newest PROB10-08/P26 reports were read before this iteration. In particular, this iteration does not restart the historical product-varentropy, synchronous-tensor, moving-weight/local-Poincare, Hecke/information-curvature, tree-subcommutation, finite-fiber, line-graph, graph-square, distance-shell, or long-range-expansion weakening routes.

The immediate predecessor established a source-admissible affine stress-test family and showed that Sarnak-Xue A=1 and near-uniform NBRW collision cannot follow from transitivity plus a spectral gap. Here the route is different: use a spectral fact in the **original Haiman--Schildkraut--Zhang--Zhao construction that the predecessor did not exploit**, namely that the lifted 16-regular subgroup graph has its entire nontrivial spectrum in the exact interval `[-4 sqrt(7),4 sqrt(7)]`, not merely below 12. This turns the affine construction into a two-scale spectral model and lets us locate its continuous-time L2 mixing sharply.

Primary sources checked:

- Salez, arXiv:2508.21055v1, Problem 2.3.
- Altschuler, arXiv:2609.14945v1, submitted 14 September 2026. The current arXiv record is still v1; no correction/erratum was found in a bounded fresh search. Its proof uses LRE to force near-maximal NBRW endpoint **Shannon entropy**, not L2 mixing.
- Haiman--Schildkraut--Zhang--Zhao, arXiv:2109.13131v3 / BLMS 54 (2022), especially Theorem 2.1 and the proof of Theorem 1.4. Their lift from the 8-regular LPS graph replaces each base eigenvalue `lambda` by `2 lambda`, with the remaining lifted eigenvalues equal to zero. Thus every nontrivial eigenvalue of the 16-regular subgroup adjacency operator has absolute value at most `4 sqrt(7)`.

A bounded current search for the exact Haiman affine family together with cutoff/L2 mixing found the multiplicity paper itself but no source matching the theorem below. This is negative search evidence only, not a priority or novelty certificate.

## 2. Frozen affine family

Let `q` range through the infinite odd LPS subfamily used in the predecessor. Put

`Pi_q = SL(2,q)`, `V_q = F_q^2`, `Gamma_q = Pi_q semidirect V_q`.

Let `S subset Pi_q` be the full preimage of the 8-element LPS generating set on `PSL(2,q)`, so `|S|=16`. Let `e != 0` and take the pure translation `t=(I,e)`. Define

`G_q = Cay(Gamma_q, S union {t,t^{-1}})`.

Then `G_q` is connected, 18-regular and vertex-transitive. Write

`N_q = |Gamma_q| = q^3(q^2-1)`,

`m_q = q^2-1`.

The predecessor proved a uniform one-sided gap for this same family. We sharpen the full nontrivial spectral description below.

Let `A_S` denote convolution by `S`, `B=R_t+R_{t^{-1}}`, and `A=A_S+B` the adjacency operator of `G_q`.

## 3. The exact lifted subgroup bound

The LPS base graph is 8-regular Ramanujan, so every nontrivial base adjacency eigenvalue has absolute value at most `2 sqrt(7)`. Haiman et al.'s lift replaces each base vertex by a pair and each base edge by `K_{2,2}`. Their proof records that the lifted spectrum consists exactly of twice the base spectrum, together with zeros. Hence

`||A_S|| <= 4 sqrt(7)`

on every nontrivial `Pi_q`-isotypic component.

Set

`beta := 2 + 4 sqrt(7)`,

`gamma_bulk := 1-beta/18 = (16-4 sqrt(7))/18 > 0`.

The inequality `4 sqrt(7)<11` follows after squaring from `112<121`, so in particular `beta<13`.

## 4. The slow irreducible block and exact multiplicity

As in Haiman et al.,

`Ind_{Pi_q}^{Gamma_q}(1) = 1 direct-sum phi_q`,

where `phi_q` is irreducible of dimension `m_q=q^2-1`. These are exactly the irreducibles of `Gamma_q` whose restriction to `Pi_q` contains a trivial vector.

Realize `1 direct-sum phi_q` on functions on `V_q`. In `phi_q`, the `Pi_q`-fixed line is generated (for the probability inner product on `V_q`) by

`u(0)=sqrt(m_q)`,

`u(x)=-1/sqrt(m_q)` for `x != 0`.

Then `A_S u=16u`. On `u^perp` inside `phi_q`, the exact lifted LPS bound gives

`lambda_max(A_S|_{u^perp}) <= 4 sqrt(7)`.

For the pure translation, the predecessor computed exactly

`<u,Bu> = -2/m_q`,

`||Bu||^2 = 2(q^2-2)/(q^2-1) < 2`.

Therefore the off-axis component `h=P_{u^perp}Bu` satisfies `||h||<sqrt(2)`.

Let `mu_q` be the top eigenvalue of `A` on `phi_q`. Rayleigh at `u` gives

`mu_q >= 16 - 2/m_q`.                                           (4.1)

For an upper bound, decompose a unit vector as `a u+w`, `w perpendicular u`. On `u^perp`,

`lambda_max(A_S+B) <= 4 sqrt(7)+2=beta`.

The cross term has magnitude at most `sqrt(2)|a| ||w||`. Hence

`mu_q <= mu_bar`,                                                (4.2)

where

`mu_bar := lambda_max([[16,sqrt(2)],[sqrt(2),beta]])`

` = (16+beta + sqrt((16-beta)^2+8))/2`

` = 9+2 sqrt(7) + (1/2)sqrt((14-4 sqrt(7))^2+8)`.

Numerically `mu_bar = 16.509376... <18`, but positivity of the resulting gap is already exact from the displayed expression.

Now let `rho` be any irreducible representation other than `1` and `phi_q`. By Frobenius reciprocity and the two-double-coset decomposition above, `rho|_{Pi_q}` contains no trivial representation. Thus

`||A_{S,rho}|| <= 4 sqrt(7)`

and therefore

`lambda_max(A_rho) <= beta`.                                    (4.3)

Within `phi_q`, min-max similarly gives

`lambda_2(A|_{phi_q}) <= beta`.                                 (4.4)

For all large `q`, (4.1) gives `mu_q>beta`. Consequently `mu_q` is simple inside `phi_q`, is strictly larger than every other nontrivial block eigenvalue, and is the unique second adjacency eigenvalue at the irreducible-block level.

Because the regular representation contains exactly `dim(phi_q)=m_q` copies of `phi_q`, the second adjacency eigenvalue `mu_q` of `G_q` has **exact multiplicity**

`m_q=q^2-1`,                                                    (4.5)

not merely multiplicity at least `q^2-1`.

This exact-multiplicity conclusion is the first new ingredient of the present iteration.

## 5. Continuous-time spectral decomposition

Normalize adjacency by degree:

`P_q=A/18`,

and use Salez's rate-one semigroup

`H_t = exp(t(P_q-I))`.

Define the slow decay rate

`delta_q := 1-mu_q/18`.

From (4.1)--(4.2),

`delta_- <= delta_q <= (1+1/m_q)/9`,                             (5.1)

where

`delta_- := 1-mu_bar/18 >0`.

Every other nontrivial eigenvalue has decay rate at least `gamma_bulk`.

Since `G_q` is vertex-transitive, the diagonal of each spectral projector is constant. Thus the chi-square distance from a point is independent of the starting vertex and satisfies the exact trace identity

`chi_q^2(t)`

` := sum_y (H_t(x,y)-1/N_q)^2/(1/N_q)`

` = sum_{i=2}^{N_q} exp(-2(1-lambda_i(P_q))t)`.                  (5.2)

Using (4.3)--(4.5),

`m_q exp(-2 delta_q t)`

` <= chi_q^2(t)`

` <= m_q exp(-2 delta_q t) + (N_q-m_q-1)exp(-2 gamma_bulk t)`.   (5.3)

## 6. New theorem: the affine family has an O(1)-window L2 cutoff

Set

`t_q^(2) := (log m_q)/(2 delta_q)`.                              (6.1)

At this time the slow block contributes exactly one to (5.3). The bulk contribution obeys

`N_q exp(-2 gamma_bulk t_q^(2))`

` = N_q m_q^(-gamma_bulk/delta_q)`.

By (5.1),

`gamma_bulk/delta_q`

` >= (8-2 sqrt(7))/(1+1/m_q)`.                                  (6.2)

Since `N_q=q^3 m_q`, `m_q=q^2-1`,

`log [N_q m_q^(-gamma_bulk/delta_q)] / log q`

` <= 5 - 2(8-2 sqrt(7)) + o(1)`

` = 4 sqrt(7)-11+o(1) <0`.                                     (6.3)

Therefore the bulk term tends to zero.

More generally, for every fixed real `s`, (5.3) gives

`chi_q^2(t_q^(2)+s) = exp(-2 delta_q s) + o(1)`,                 (6.4)

where the `o(1)` is uniform for `s` in any fixed compact interval. No convergence of `delta_q` is assumed.

Let

`d_{2,q}(t):=sqrt(chi_q^2(t))`

and define `t_{2,q}(epsilon)` by `d_{2,q}(t)<=epsilon`. Because `delta_q` is uniformly bounded above and below away from zero by (5.1), (6.4) implies, for every fixed `epsilon in (0,infinity)`,

`t_{2,q}(epsilon) = t_q^(2)+O_epsilon(1)`.                       (6.5)

In particular,

`[t_{2,q}(epsilon)-t_{2,q}(1/epsilon)]/t_q^(2) = O(1/log N_q)`

for any fixed `epsilon<1` (with the obvious ordering of the two thresholds), and the continuous-time walk has **L2 cutoff with an O(1) window**.

This is an auxiliary mixing theorem, not a TV-cutoff theorem.

## 7. The important consequence: L2 is polynomially wrong at the tree/Ramanujan TV scale

For degree 18, Altschuler's Ramanujan/LRE cutoff center would be

`T_q := (18/16) log_17 N_q = (9/8) log_17 N_q`.                  (7.1)

The point is not to assert that this is the actual TV center of the affine family; it is the fastest tree/radial benchmark and the center in Altschuler's theorem.

Using only the slow block and the upper bound on `delta_q` from (5.1),

`chi_q^2(T_q)`

` >= m_q exp[-2 ((1+1/m_q)/9) T_q]`

` = N_q^(2/5 - 1/(4 log 17) + o(1))`.                           (7.2)

The exponent is positive. Numerically it is about `0.31176`, and exact positivity follows already from `log 17>5/8`.

Hence

`chi_q^2(T_q) -> infinity` polynomially.                         (7.3)

Moreover, from `delta_q<=(1+o(1))/9`,

`t_q^(2) >= (9/2+o(1)) log m_q`,

and therefore

`liminf t_q^(2)/T_q >= (8/5) log 17 = 4.533...`.                 (7.4)

Thus the **actual continuous-time SRW** on this source-admissible transitive expander has an L2 transition at least a factor 4.53 later than the degree-18 tree benchmark, even though Salez's conjecture predicts a sharp TV transition somewhere on the `Theta(log N)` scale.

This makes the previous NBRW-collision obstruction substantially sharper: not only the NBRW endpoint but the true heat kernel itself remains polynomially far from uniform in chi-square at the fastest possible TV scale. Therefore a proof of Salez 2.3 cannot rely on converting ordinary spectral/L2 mixing into TV mixing uniformly over the source class. A genuinely `L log L` / Shannon / typical-mass mechanism is necessary for families of this kind.

No TV lower bound follows from (7.3). A distribution can have very large chi-square distance because of a tiny exceptional set while still having small total variation. This distinction is essential here.

## 8. Second approach: try to rescue the Feynman--Kac route by a quiet-gap regeneration — REFUTED

The predecessor derived the exact semidirect decomposition. Translation events form an independent Poisson process of rate `1/9`; subgroup `S`-moves occur at rate `8/9` and do not change the additive coordinate. A tempting regeneration argument is:

1. wait for a long interval with no translation;
2. use that interval to mix the subgroup direction `M e`;
3. let the next translation add an almost-uniform vector and nearly refresh the additive coordinate.

This cannot be the logarithmic-scale mechanism.

Fix `C<infinity` and observe the walk until time `C log q`. There are `O(log q)` translation gaps with probability tending to one. Since each gap has exponential tail `exp(-u/9)`, for any fixed `K>9`,

`P(max translation-free gap > K log log q) -> 0`.                (8.1)

Condition on such a gap and on its starting subgroup state. During a gap of length `K log log q`, the number of `S`-moves is Poisson with mean `(8K/9)log log q`; uniformly over all `O(log q)` gaps it is `O(log log q)` with probability tending to one if the implicit constant is chosen large enough. Starting from a fixed subgroup state, after `r=O(log log q)` `S`-moves the vector `M e` can lie in at most `16^r=(log q)^{O(1)}` locations. The stationary orbit has `q^2-1` locations. Therefore the conditional law of `M e` at the end of every such quiet gap has TV distance `1-o(1)` from uniform.

So with high probability **no translation-free interval available before any `C log q` time is long enough even in support size to create a fresh uniform direction**. This refutes the single-quiet-gap regeneration scheme, independently of spectral estimates.

It does not refute multi-translation entropy accumulation.

## 9. Third approach: keep all translations and use the epoch resolvent — structurally clean, quantitatively still L2-like

At translation epochs, the subgroup state has evolved through a geometric number of `S`-moves. Let `P_S=A_S/16` be the subgroup walk. The transition operator between consecutive translation epochs on the subgroup coordinate is exactly

`R = sum_{k>=0} (1/9)(8/9)^k P_S^k`

`  = (9I-8P_S)^(-1)`.                                           (9.1)

On mean-zero functions, the exact lifted LPS spectrum gives

`||R|| <= r_0 := 1/(9-2 sqrt(7)) = 0.26965...`.                  (9.2)

For a nontrivial additive character, sign averaging at a translation multiplies by

`C_xi(M)=Re chi_xi(M e)`.

Under uniform `M`,

`E C_xi = -1/(q^2-1)`,

`E C_xi^2 = (q^2-2)/(2(q^2-1)) <1/2`                            (9.3)

for odd `q`. Splitting `L2(Pi_q)` into constants and mean-zero functions, the operator `R M_{C_xi}` is dominated by the 2-by-2 norm matrix

`[[1/m_q, 1/sqrt(2)], [r_0/sqrt(2), r_0]]`.                     (9.4)

Its Frobenius norm tends to

`sqrt(1/2 + (3/2)r_0^2) = 0.780... <1`,

so for all sufficiently large `q` one gets a uniform contraction below, say, `0.8` per translation epoch.

This is a genuine exact structural gain over conditioning on the entire subgroup path: the correlated directions have a strongly contracting epoch operator. But using (9.4) through Parseval still pays for `q^2` additive characters (and a point-mass `L2` prefactor on the subgroup), so it only gives a much later `Theta(log q)`-epoch/L2 bound. It does not approach the `Theta(log q)` **physical-time** TV scale, where there are only `Theta(log q)` translation epochs with a small coefficient.

The conclusion is precise: the affine route now has a useful reduced operator, but any successful proof must use its **Shannon/typical-mass behavior**, not its L2 norm.

## 10. Information accounting: what the Feynman--Kac conditioning throws away

There is also a simple entropy-budget warning. At the degree-18 tree benchmark `T_q=(9/8)log_17 N_q`, the expected number of translation events is `T_q/9=Theta(log q)`. If one exposes the entire ordered sequence of `S`-generators and asks the remaining event-type/sign randomness to generate the additive `F_q^2` coordinate, the residual per-jump entropy is at most

`h(1/9)+(1/9)log 2 = 0.425848...` nats.

Since `T_q = 1.985378... log q+o(log q)`, that residual entropy is only

`0.84547... log q+o(log q)`,

whereas a uniform additive coordinate requires `2 log q+o(log q)` nats. Therefore any entropy proof that **conditions away the subgroup bridge randomness** is quantitatively incapable of producing the missing additive entropy near the fastest scale. The bridge randomness of the subgroup path must itself be harvested by the additive coordinate.

This explains why the predecessor's conditional Feynman--Kac identity is a useful analytic representation but not, by itself, an entropy proof.

## 11. Three approaches compared

1. **Exact two-scale spectrum / L2.** Successful as a complete auxiliary theorem. It gives exact second-eigenvalue multiplicity, an O(1)-window continuous-time L2 cutoff, and a polynomial chi-square obstruction at the tree/Ramanujan TV scale.
2. **Single quiet-gap regeneration.** Refuted on every `C log q` physical-time horizon: the longest available translation-free gap is only `O(log log q)`, far too short even by support size to refresh the direction.
3. **Multi-translation epoch/Feynman--Kac.** The exact epoch resolvent has a uniform mean-zero contraction `<=1/(9-2sqrt(7))`, and the character transfer operator has norm `<0.8` for large `q`. This is retained as a structurally different next route, but ordinary L2/Parseval use is quantitatively too slow. A Shannon or bridge-entropy estimate is the missing ingredient.

## 12. Source-level accounting

**Before:** Salez Problem 2.3 OPEN. Historical R16 source metric `W_exp=1/2 provisional`; the previous run made no TV graph-class/window improvement, but proved an obstruction to Sarnak-Xue/NBRW-collision methods.

**After:** Salez Problem 2.3 remains **OPEN**. No new total-variation cutoff graph class is proved in this iteration, so the source metric does **not move** and `W_exp` remains `1/2 provisional`.

**Auxiliary mechanism progress proved here:**

- the Haiman affine family has a unique slow irreducible block whose second adjacency eigenvalue has exact multiplicity `q^2-1`;
- every other nontrivial adjacency eigenvalue is at most `2+4sqrt(7)`;
- its rate-one continuous-time SRW has L2 cutoff with O(1) window at `(log(q^2-1))/(2 delta_q)`;
- its chi-square distance diverges polynomially at the degree-18 tree/Ramanujan time, so uniform L2-to-TV conversion is provably unavailable on the source class;
- a single-quiet-gap Feynman--Kac regeneration is impossible on logarithmic physical time;
- the exact translation-epoch resolvent isolates the remaining Shannon/bridge-entropy problem.

This is deliberately labeled an obstruction/mechanism run, not a source advance.

## 13. Checks actually run

No finite mixing plot was used. No asymptotic statement is inferred from numerics.

A local symbolic/numerical sanity check evaluated only the constants in the exact formulas:

- `beta=2+4sqrt(7)=12.583005...`;
- `gamma_bulk=(16-4sqrt(7))/18=0.300944...`;
- `mu_bar=16.509376...`;
- `delta_-=1-mu_bar/18=0.0828124...`;
- `4sqrt(7)-11=-0.416994...`;
- `(8/5)log 17=4.53314...`.

The proof does not depend on floating-point certification: the signs used above reduce to elementary exact inequalities such as `4sqrt(7)<11`.

## 14. Remaining full-scope gap

The main target is now sharper. A general solution of Salez 2.3 must tolerate source-admissible families whose heat kernel is polynomially far from uniform in chi-square at the relevant TV scale. On the affine family, the concrete missing statement is an `L log L` estimate that extracts the roughly `2 log q` additive-coordinate entropy from the **bridge randomness of the subgroup walk** while retaining the endpoint subgroup entropy. Equivalently, one needs a Shannon/typical-mass estimate for the multi-translation transfer operator that does not pay its L2 norm or the number of characters.

Any next iteration that merely sharpens the L2 constants, repeats the quiet-gap idea, or conditions on the whole subgroup path should be treated as exhausted unless it supplies that missing bridge-entropy mechanism.

## 15. History links

- `operations/claims/I0112.md`
- `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`
- `runs/R16/2026-09-16T18-48-00Z_i0112-product-varentropy.md`
- `runs/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff.md`
- `runs/R16/2026-09-16T20-45-00Z_i0112-window-floor-gauge-obstruction.md`
- `runs/R16/2026-09-16T21-42-29Z_i0112-Hecke-information-curvature-obstruction.md`
- `runs/R16/2026-09-16T23-44-54Z_i0112-stuck-recovery-2-tree-subcommutation-obstruction.md`
- `runs/prob10_2026-09-20/PROB10-08/2026-09-20T03-00-00Z_affine-sx-green-obstruction_9c21.md`
- newest neighboring same-parent report read: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_05-56-17__distance-set-shell-profile-transfer.md`.
