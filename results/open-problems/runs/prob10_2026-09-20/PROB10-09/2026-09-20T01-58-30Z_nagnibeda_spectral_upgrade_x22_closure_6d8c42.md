Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-FAMILY METRIC MOVED: `delta_surf > 0.01716108096716552... -> delta_surf > 0.02441444290890310...`; parent Benjamini–Schramm source remains OPEN/PARTIAL. Auxiliary quantitative scope expands from all standard surface products except `X_{2,2}` to every `X_{g,h}`, `g,h>=2`.**

# PROB10-09 — surface-group spectral-radius input closes the missing `(2,2)` product certificate and improves the frozen gap

## 0. Frozen source, continuity, ownership, and source status

The parent target is unchanged:

\[
\forall G=\operatorname{Cay}(\Gamma,S),\qquad
\Gamma\text{ finitely generated and nonamenable},\qquad
p_c(G)<p_u(G)
\]

for iid **bond** percolation. No planar site-percolation statement is substituted. The universal source remains **OPEN / PARTIAL** after this run.

The required predecessor handoff already exists at

`runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`.

The immediate R20/PROB10-09 predecessor is

`runs/prob10_2026-09-20/PROB10-09/2026-09-20T00-59-30Z_surface_product_family_gap_improvement_7e3b91.md`, blob `1930c96e01a18cde88f7813e72ca0230267121fd`.

It proved, self-checked, a quantitative `p_c<p_{2->2}<=p_u` certificate for every standard product of two closed-surface-group Cayley graphs except `(g,h)=(2,2)`, and for the frozen graph `X_{3,4}` established

\[
p_u(X_{3,4})-p_c(X_{3,4})>0.01716108096716552\ldots .
\]

The June archive was retained rather than restarted. Consumed files include

- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`, blob `ee8bde8735e84ff75d3a625fed61e9bafbefd64f`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`, blob `d94127841f3b335a32b7936b86d8dee7a6b8d093`;
- the relevant June nonbacktracking/fiber attempts identified in the preceding two PROB10-09 reports, including rounds 011, 018, 040, 042, 053, 054 and 055.

I also read current `operations/PROB10_2026-09-20.md` (blob `6f0fcee836d93371d43b84af1a55150fedc80779`), `POSTED.md` (blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`), the current canonical-claim directory, and current `operations/PROGRESS20_2026-09-20.md` (blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`). No canonical claim was found that assigns the standard surface-product quantitative route to another owner. The neighboring T09 worker NM13-11 owns a distinct free-core/complement / `SL_3(Z)` route; its newest report is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T03-51-00+0300__t09-f5-plus4-sl3-gap.md`, blob `44c2ae0c528b23247e1925cc129f80a5c5209a20`.

That report is not edited or duplicated here.

### Current primary-source check

A bounded 20 September 2026 check retained the following distinctions.

- Hutchcroft, arXiv:1804.10191 / GOFA 2019, proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs, not the general Cayley target.
- Hutchcroft–Pan, arXiv:2409.12283, gives subgroup-relativization results, not the universal fixed-Cayley-graph theorem.
- Terlov–Timár, arXiv:2502.02560, concerns weighted/nonunimodular variants.
- Choi–Seo, arXiv:2508.08932, covers Cayley graphs of acylindrically hyperbolic groups; this is a known class and is not claimed as fleet progress here.
- Yuval Peres, *Percolation on nonamenable products at the uniqueness threshold*, Ann. IHP 36 (2000), 395–406, already gives qualitative product results broad enough that the standard surface-product family below is **not claimed as a new qualitative family**.

No located primary source in this bounded search announced a resolution of the frozen universal Cayley-graph conjecture. This is negative search evidence, not a worldwide novelty certificate.

## 1. Idea before code and three routes compared

The idea was recorded before the checker at

`artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T01-48-30Z_nagnibeda_spectral_upgrade_idea.md`.

Three materially different approaches were compared.

1. **Import a sharper random-walk spectral bound into the nonbacktracking certificate — developed and successful.** The previous run bounded each surface-factor adjacency operator by deleting one generator and applying Freiheitssatz. This run instead uses classical rigorous surface-group Markov spectral-radius bounds due to Nagnibeda, quoted explicitly as Theorem 1.3 in Bartholdi, arXiv:math/0112108. This attacks the `p_{2->2}` side rather than spending another run sharpening only `p_c`.

2. **Improve only the tree-fiber `p_c` witness — rejected as the decisive route for `(2,2)`.** The preceding run already diagnosed the true one-sided `T_6 square T_6` fiber threshold at about `0.102686`, while the old coarse nonbacktracking lower threshold was only about `0.0858`. Thus arbitrarily deep witnesses inside that same old comparison cannot bridge the old operator gap. The new spectral input changes the side that was actually blocking.

3. **Use the free-core/complement subgroup criterion on the standard `(2,2)` generating set — compared but not pursued.** NM13-11 owns this route. Moreover its current cardinality/operator sufficient condition is poorly matched to the standard degree-16 product generating set: a free rank-three core has forward parameter `q=5`, while the complementary standard generators are too numerous for the current free-core/complement inequality. This is both an ownership collision and a quantitative mismatch, so the present run stays on the factor-spectral route.

A fourth source-level comparison was Peres's 2000 product theorem: it confirms that qualitative product nonuniqueness is old, but it does not supply the explicit quantitative `p_u-p_c` certificate tracked here.

## 2. External spectral input, conservatively rationalized

For the standard surface group

\[
\Gamma_g=\langle a_1,b_1,\ldots,a_g,b_g\mid
[a_1,b_1]\cdots[a_g,b_g]=1\rangle
\]

with its standard symmetric generating set of size `4g`, let `M_g=A_g/(4g)` be simple random walk's Markov operator.

Bartholdi, arXiv:math/0112108, Theorem 1.3, records Nagnibeda's rigorous upper bounds

\[
\|M_2\|\le0.662816,
\qquad
\|M_3\|\le0.552792.
\tag{2.1}
\]

To avoid using a printed decimal at equality in any delicate way, deliberately weaken (2.1) to the larger exact rationals

\[
\|M_2\|<\frac{663}{1000},
\qquad
\|M_3\|<\frac{553}{1000}.
\tag{2.2}
\]

Hence

\[
\boxed{\|A_2\|<\frac{663}{125}=5.304,}
\qquad
\boxed{\|A_3\|<\frac{1659}{250}=6.636.}
\tag{2.3}
\]

For a Cartesian product `X_{g,h}`, its adjacency operator is

\[
A_{g,h}=A_g\otimes I+I\otimes A_h,
\]

so

\[
\|A_{g,h}\|\le\|A_g\|+\|A_h\|.
\tag{2.4}
\]

This is the only new external theorem imported in the proof below. The percolation transfer and finite cluster witnesses were already established in the June archive and the two predecessor PROB10-09 reports.

## 3. Recalled nonbacktracking transfer

For a `D`-regular transitive graph with adjacency norm at most `R`, put `Q=D-1` and

\[
\beta(D,R)=
\begin{cases}
\sqrt Q,&R\le2\sqrt Q,\\[1mm]
\dfrac{R+\sqrt{R^2-4Q}}2,&R>2\sqrt Q.
\end{cases}
\]

The nonbacktracking-polynomial argument gives

\[
 p_{2\to2}(G)\ge\beta(D,R)^{-1},
\tag{3.1}
\]

and transitivity plus uniqueness/FKG gives

\[
 p_{2\to2}(G)\le p_u(G).
\tag{3.2}
\]

For completeness, (3.1) comes from the recurrence for nonbacktracking endpoint kernels `N_n=P_n(A)`. Their `l^2` growth rate is at most `beta(D,R)`. If `p beta<1`, then `sum_n p^nN_n` is a bounded positive `l^2` operator and dominates the connectivity kernel because each connection has a self-avoiding, hence nonbacktracking, witness. This proves `p<p_{2->2}`. Equation (3.2) follows because above `p_u` the connectivity kernel is bounded below by the positive constant `theta(p)^2` and therefore cannot be `l^2` bounded on an infinite transitive graph.

## 4. Exact finite-depth `p_c` witness

As in the preceding report, if `T_d square T_{q+1}` is oriented in the second factor and `C(o)` is the vertical open cluster, then

\[
q\,\varphi_d(p)>1,
\qquad
\varphi_d(p)=\mathbf E_p[1-(1-p)^{|C(o)|}],
\]

implies `p_c(T_d square T_{q+1})<p`.

The radius-two exact lower witness is

\[
\Phi_d^{(2)}(p)
=1-(1-p)\left[(1-p)+p(1-p)(1-p^2)^{d-1}\right]^d
\le\varphi_d(p).
\tag{4.1}
\]

For rational `p`, (4.1) is an exact rational certificate.

## 5. New quantitative theorem for the missing `X_{2,2}`

Let

\[
X_{2,2}=\operatorname{Cay}(\Gamma_2\times\Gamma_2,
(S_2\times\{1\})\cup(\{1\}\times S_2)).
\]

This graph is `D=16` regular.

### 5.1 Upper bound on `p_c`

Magnus Freiheitssatz gives a standard `F_3` subgroup inside each genus-two surface group by omitting one standard generator. On Cayley graphs this yields

\[
T_6\square T_6\subseteq X_{2,2}.
\]

Orient one `T_6` factor, so `q=5` forward fibers, and take `d=6` vertically. At

\[
p_0=\frac{11}{100},
\]

the executed exact checker gives

\[
5\Phi_6^{(2)}(p_0)-1
=
\frac{131820329999890696337608308508976546633036851200544171887567684152276012853965669871756897261182117013763605458896297393515556551871184610744831}
{20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}
>0.
\]

Therefore

\[
 p_c(X_{2,2})\le p_c(T_6\square T_6)<\frac{11}{100}.
\tag{5.1}
\]

### 5.2 Lower bound on `p_{2->2}`

From (2.3) and (2.4),

\[
\|A_{2,2}\|<R_{22}:=2\cdot\frac{663}{125}=\frac{1326}{125}.
\]

Here `Q=D-1=15`. Let

\[
P(z)=z^2-R_{22}z+15,
\qquad
z_0=\frac{100}{11}.
\]

The exact checker gives

\[
P(z_0)=\frac{731}{605}>0,
\qquad
z_0^2-15=\frac{8185}{121}>0,
\]

and also `R_{22}^2-60=820776/15625>0`, so `P` has two positive real roots `r_-<r_+` with product `15`, where

\[
r_+=\beta(16,R_{22}).
\]

Since `P(z_0)>0`, `z_0` lies outside `[r_-,r_+]`. It cannot lie below `r_-`, because then `z_0^2<r_-r_+=15`, contradicting `z_0^2>15`. Hence

\[
z_0>r_+=\beta(16,R_{22}),
\]

so

\[
\frac{11}{100}<\beta(16,R_{22})^{-1}\le p_{2\to2}(X_{2,2})\le p_u(X_{2,2}).
\tag{5.2}
\]

Combining (5.1)--(5.2) proves

\[
\boxed{p_c(X_{2,2})<p_{2\to2}(X_{2,2})\le p_u(X_{2,2}).}
\]

More quantitatively,

\[
\boxed{
 p_u(X_{2,2})-p_c(X_{2,2})
 >\beta(16,1326/125)^{-1}-\frac{11}{100}
 =0.002008830183441238\ldots .}
\tag{5.3}
\]

This fills the sole missing pair from the preceding quantitative standard-surface-product theorem. Therefore, combining this run with the immediately preceding report gives a self-checked quantitative `p_c<p_{2->2}<=p_u` certificate for **every** standard product `X_{g,h}` with `g,h>=2`.

This is an auxiliary theorem-scope expansion, not a new qualitative source-class claim: Peres 2000 already covers the product phenomenon qualitatively.

## 6. Frozen graph `X_{3,4}`: improved certified gap

The fixed metric remains the certified lower bound for

\[
X_{3,4}=\operatorname{Cay}(\Gamma_3\times\Gamma_4,S_3\cup S_4).
\]

The preceding report's exact radius-two certificate remains valid:

\[
13\Phi_{10}^{(2)}(19/400)-1>0,
\]

hence

\[
p_c(X_{3,4})<\frac{19}{400}.
\tag{6.1}
\]

For genus 3, (2.3) gives `||A_3||<1659/250`. For genus 4 I retain the earlier conservative Freiheitssatz bound

\[
\|A_4\|\le2+2\sqrt{13}.
\]

Thus

\[
R_{34}:=\frac{2159}{250}+2\sqrt{13}
\tag{6.2}
\]

is a valid upper bound for the adjacency norm of `X_{3,4}`. The graph has `D=28`, `Q=27`.

Set `z=400/19`. To compare `z` with `R_{34}` exactly, write

\[
y=z-\frac{2159}{250}=\frac{58979}{4750}>0.
\]

The checker gives

\[
y^2-52=\frac{2305272441}{22562500}>0.
\]

Hence `y>2sqrt(13)` and therefore

\[
z>R_{34}.
\]

Since `R_{34}>2sqrt(27)`, the relevant root is

\[
\beta_{34}
=\frac{R_{34}+\sqrt{R_{34}^2-108}}2
<R_{34}<z.
\]

Consequently

\[
\frac{19}{400}<\beta_{34}^{-1}\le p_{2\to2}(X_{3,4})\le p_u(X_{3,4}),
\]

and (6.1) yields the improved frozen-family certificate

\[
\boxed{
 p_u(X_{3,4})-p_c(X_{3,4})
 >\beta_{34}^{-1}-\frac{19}{400}
 =0.0244144429089031045\ldots .}
\tag{6.3}
\]

The previous certified bound was `0.01716108096716552...`; therefore the fixed metric improves by more than

\[
0.00725336194173758.
\]

No numerical SDP or unverified simulation enters this proof.

## 7. Exact checker and negation tests

The new code and archived executed output are

- `artifacts/prob10_2026-09-20/PROB10-09/nagnibeda_surface_product_upgrade_exact.py`;
- `artifacts/prob10_2026-09-20/PROB10-09/nagnibeda_surface_product_upgrade_exact.out`.

The output ends `ALL_EXACT_CHECKS_PASS` and checks exactly:

1. the conservative rational relaxations of the quoted Nagnibeda bounds;
2. the radius-two `X_{2,2}` branching margin at `11/100`;
3. the `X_{2,2}` quadratic root comparison;
4. the prior `X_{3,4}` radius-two branching margin at `19/400`;
5. the exact radical comparison `400/19>2159/250+2sqrt(13)`.

Displayed decimal gap values are informational only. The sign decisions are exact integer/rational arithmetic plus the explicitly squared positive-side radical comparison.

The main negation test was the old `(2,2)` obstruction: sharpening finite depth alone cannot fix the old scalar comparison because even the full one-sided tree-fiber recursion crosses near `0.102686`, above the old coarse nonbacktracking threshold near `0.0858`. The new spectral input raises the certified nonbacktracking threshold above `0.11`, so the exact finite radius-two witness is enough. This identifies why the previous route failed and why the current change of method succeeds.

## 8. Before/after accounting

### Source-level parent

- **Before:** Benjamini--Schramm Cayley-graph bond conjecture OPEN / PARTIAL.
- **After:** OPEN / PARTIAL.
- **Universal source metric movement:** none. No statement here covers every Cayley graph of every finitely generated nonamenable group.

### Frozen-family metric

- Frozen graph: standard `X_{3,4}`.
- Before: `p_u-p_c > 0.01716108096716552...`.
- After: `p_u-p_c > 0.0244144429089031045...`.
- Certified improvement: `>0.00725336194173758` in the recorded lower bound.

### Auxiliary structural scope

- Before: quantitative `p_c<p_{2->2}<=p_u` for every standard surface product `X_{g,h}`, `g,h>=2`, except `(2,2)`.
- After: the same quantitative conclusion for **all** standard `X_{g,h}`, `g,h>=2`; new missing-pair certificate (5.3) has gap `>0.002008830183441238...`.
- Prior-art qualification: qualitative nonuniqueness for this product class is old (Peres 2000). External novelty of these exact numerical bounds / this certificate combination is **UNVERIFIED**.

## 9. Remaining full gap and next mathematically distinct attack

The parent conjecture still requires a mechanism that does not depend on having a convenient embedded free core/product structure plus an independently strong adjacency-norm estimate. The current result says something more specific than merely naming `p_c<p_{2->2}`: it shows exactly how a factorwise spectral-radius estimate can be combined with a finite exact cluster witness to certify a strict threshold interval.

The next nonduplicating route should leave Cartesian products. A natural candidate is an **anisotropic/color-sensitive nonbacktracking bound** that retains separate generator blocks instead of collapsing them to the scalar total adjacency norm `R`. If one can prove a block Hashimoto growth bound in terms of the individual block operator norms, it could apply to Cayley generating sets with a large nonamenable block plus structured complement and may overlap neither the current product certificate nor NM13-11's cardinality-based free-core/complement criterion. No such general theorem is claimed here.

## 10. Validation status

All new finite/algebraic claims above have an executed exact self-check. The literature theorem input is explicitly identified and conservatively weakened. **No independent other-track audit was performed in this run.** Accordingly the restricted theorems are self-checked candidate mathematics, not independently validated source closure, and the parent conjecture remains OPEN/PARTIAL.

```yaml
ledger_delta:
  worker: R20
  assignment: PROB10-09
  parent_source: "Benjamini--Schramm nonuniqueness phase for iid bond percolation on Cayley graphs of finitely generated nonamenable groups"
  parent_status_before: PARTIAL
  parent_status_after: PARTIAL
  source_metric_movement: none
  frozen_family: "standard X_{3,4}=Cay(Gamma_3 x Gamma_4)"
  metric: "certified lower bound on p_u-p_c"
  metric_before: "> 0.01716108096716552"
  metric_after: "> 0.0244144429089031045"
  metric_delta_lower_bound: "> 0.00725336194173758"
  auxiliary_scope_before: "all standard X_{g,h}, g,h>=2, except (2,2)"
  auxiliary_scope_after: "all standard X_{g,h}, g,h>=2"
  new_X22_gap: "> 0.002008830183441238"
  mechanism: "Nagnibeda surface-group spectral-radius upper bounds + nonbacktracking polynomial transfer + exact radius-two fiber branching"
  runtime_model: "GPT-5.6 Sol"
  reasoning_level: UNVERIFIED
  independent_audits: []
  exact_checker: "artifacts/prob10_2026-09-20/PROB10-09/nagnibeda_surface_product_upgrade_exact.py"
  exact_output: "artifacts/prob10_2026-09-20/PROB10-09/nagnibeda_surface_product_upgrade_exact.out"
  checker_status: ALL_EXACT_CHECKS_PASS
  remaining_obligation: "extend a strict threshold mechanism beyond product/free-core families toward arbitrary nonamenable Cayley graphs"
```
