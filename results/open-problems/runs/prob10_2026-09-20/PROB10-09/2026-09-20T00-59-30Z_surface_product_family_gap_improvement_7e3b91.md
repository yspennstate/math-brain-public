Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-FAMILY METRIC MOVED: `delta_surf > 0.01286825228190655... -> delta_surf > 0.01716108096716552...`; parent Benjamini–Schramm source remains OPEN/PARTIAL. Auxiliary theorem scope expands from one standard surface-product Cayley graph to every `Gamma_g x Gamma_h` standard product with `g,h>=2` except `(2,2)`.**

# PROB10-09 — depth-two branching sharpens the frozen gap and yields an all-but-one standard surface-product theorem

## 0. Frozen source, continuity, ownership, and a prior-art correction

The source target remains exactly the iid **bond**-percolation Cayley-graph conjecture

\[
\forall G=\operatorname{Cay}(\Gamma,S),\quad
\Gamma\text{ finitely generated nonamenable},\qquad p_c(G)<p_u(G).
\]

No planar site-percolation substitute is used. The full source remains **OPEN / PARTIAL** in this run.

The controlling assignment is `operations/PROB10_2026-09-20.md`. The required R20 predecessor handoff already exists at

`runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`

and preserves the actual predecessor Paley/KNSV/BMO states and artifacts. I did not overwrite any predecessor claim.

The immediate PROB10-09 predecessor is

`runs/prob10_2026-09-20/PROB10-09/2026-09-19T23-58-00Z_surface_product_strict_gap_4c91e2.md`.

It proved for the standard genus-3-by-genus-4 surface-product Cayley graph `G_{3,4}` the self-checked bound

\[
p_u-p_c>
\frac1{5+\sqrt{13}+\sqrt{11+10\sqrt{13}}}-\frac{13}{251}
=0.01286825228190655\ldots.
\]

The June proof history was recovered from
`probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/`, including `research/open_status.md` and the relevant nonbacktracking / fiber-branching / fixed-endpoint attempts, notably rounds 011, 018, 040, 042, 053, 054 and 055. In particular, I retain the exact nonbacktracking polynomial bound and the fiber-cluster branching lemma, while not using the old unproved finite-state charging bridge.

There is also a current neighboring T09 route under `operations/PROGRESS20_2026-09-20.md`: NM11 is assigned the subgroup/nonbacktracking direction, and its newest report

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T02-52-26+0300__t09-subgroup-nonbacktracking-sl3z-gap.md`

proves a candidate quantitative theorem for a specific Cayley graph of `SL_3(Z)`. I do **not** duplicate, edit, or claim that `SL_3(Z)` route. The present route is delimited to the standard surface-product family and a sharper finite-depth fiber comparison.

### Important prior-art correction

A current source check located Yuval Peres, *Percolation on nonamenable products at the uniqueness threshold*, Ann. Inst. H. Poincare Probab. Statist. 36 (2000), 395–406. Its Theorem 1.1 states that if `X,Y` are infinite locally finite connected quasi-transitive graphs and `Aut(X)` is nonamenable, then at `p_u` iid bond percolation on `X x Y` is not in the unique-infinite-cluster phase. The standard surface-product graphs studied here are Cartesian products, so the preceding report's suggestion that this family was wholly outside known product results was too strong.

That correction does **not** invalidate the explicit inequalities proved below. It means that they are to be read as **quantitative self-contained certificates / mechanism progress, with external novelty UNVERIFIED**, not as a claimed first qualitative treatment of nonamenable products. A bounded search did not establish whether these exact numerical lower bounds have appeared before. No novelty or publication-priority claim is made.

Current source navigation checked this run also includes:

- Hutchcroft, arXiv:1804.10191, the nonamenable Gromov-hyperbolic quasi-transitive theorem;
- Hutchcroft–Pan, arXiv:2409.12283, subgroup relativization at the uniqueness threshold;
- Hutchcroft–Pan, arXiv:2412.15895, tree-times-amenable and lamplighter `p_{2->2}=p_u` results already recognized in June round 042;
- Terlov–Timar, arXiv:2502.02560, weighted/nonunimodular theory;
- Choi–Seo, arXiv:2508.08932, every Cayley graph of every acylindrically hyperbolic group.

No located current source announced the universal Cayley-graph conjecture in the frozen scope as solved.

## 1. Idea before code and the three routes compared

The idea was written before the checker at

`artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T00-55-00Z_surface_product_family_depth2_idea.md`.

Three materially different routes were compared.

1. **Finite-depth fiber-cluster branching (developed, successful).** Replace the preceding radius-one witness by a radius-two exact cluster witness. This improves the frozen `G_{3,4}` `p_c` comparison point from `13/251` to `19/400` and closes the low-genus pair `(2,3)` within the same nonbacktracking comparison.

2. **Parameter-monotone family proof (developed, successful).** Instead of checking genera one at a time, prove monotone lower envelopes in `x=sqrt(4h-3)` that cover all `g>=3,h>=4` and all `g=2,h>=5`. Together with three exact exceptional pairs, this proves a quantitative criterion for every standard surface-product graph except `(2,2)`.

3. **Subgroup/nonbacktracking on a nonproduct group (not duplicated).** The current NM11 worker already took this direction and obtained the `SL_3(Z)` candidate. Ownership therefore rules it out as this run's route. I instead used it as a negation/collision test on the scope of my theorem. Peres's 2000 product theorem was also checked as a prior-art stress test; it forces the correction above and prevents treating the product family as a clean novelty witness.

The `(2,2)` case was additionally tested against the **full** one-sided tree-fiber cluster recursion at the current nonbacktracking comparison point. Numerically its offspring mean is about `0.746338<1`; this is recorded only as a diagnostic, **not** as an exact impossibility theorem.

## 2. Setup for all standard surface-product Cayley graphs

For `g>=2`, write

\[
\Gamma_g=\langle a_1,b_1,\ldots,a_g,b_g\mid
[a_1,b_1]\cdots[a_g,b_g]=1\rangle
\]

and let `S_g` be the standard symmetric generating set. For `g,h>=2`, set

\[
X_{g,h}:=\operatorname{Cay}(\Gamma_g\times\Gamma_h,
(S_g\times\{1\})\cup(\{1\}\times S_h)).
\]

This is the Cartesian product of the two standard surface-group Cayley graphs. It is

\[
D=4(g+h)
\]

regular and is a Cayley graph of a finitely generated nonamenable group.

By symmetry assume `2<=g<=h`, and put

\[
a=4g-3,\qquad b=4h-3,\qquad u=\sqrt a,\qquad x=\sqrt b.
\]

Magnus Freiheitssatz applied to the standard one-relator surface presentation says that omitting one of the `2g` generators leaves a free subgroup `F_{2g-1}`. Hence the standard Cayley graph of `Gamma_g` contains, using those generator edges, a copy of the `(4g-2)`-regular tree `T_{a+1}`. Similarly the second factor contains `T_{b+1}`. Therefore

\[
T_{a+1}\square T_{b+1}\subseteq X_{g,h}.
\tag{2.1}
\]

For the full factor adjacency operator, split off the omitted generator. On every free-subgroup coset the retained adjacency is `T_{a+1}`, of norm `2 sqrt(a)`, and the omitted generator plus its inverse contributes operator norm at most `2`. Therefore

\[
\|A_{\Gamma_g}\|_{2\to2}\le2\sqrt a+2,
\]

and similarly for `h`. The Cartesian-product adjacency then obeys

\[
\boxed{\|A_{X_{g,h}}\|_{2\to2}\le R_{g,h}:=4+2\sqrt a+2\sqrt b.}
\tag{2.2}
\]

For a `D`-regular graph define

\[
\beta(D,R)=
\begin{cases}
\sqrt{D-1},&R\le2\sqrt{D-1},\\[1mm]
\dfrac{R+\sqrt{R^2-4(D-1)}}2,&R>2\sqrt{D-1}.
\end{cases}
\]

The June nonbacktracking polynomial recurrence, reproduced in the preceding PROB10-09 report, gives

\[
p_{2\to2}(X_{g,h})\ge \frac1{\beta(D,R_{g,h})}.
\tag{2.3}
\]

Here in fact the second branch always applies: since `D-1=a+b+5`,

\[
R_{g,h}^2-4(D-1)
=4(4u+4x+2ux-1)>0.
\]

Consequently

\[
\beta(D,R_{g,h})<R_{g,h}.
\tag{2.4}
\]

Finally the standard transitive-percolation inequality gives

\[
p_{2\to2}\le p_u.
\tag{2.5}
\]

Thus it remains only to place a rigorous `p_c` upper bound below the quantity in (2.3).

## 3. Exact finite-depth cluster witnesses

Orient the `T_{b+1}` factor in (2.1) away from a root, so every non-root fiber has

\[
q=b
\]

forward child fibers. Use `T_d` with `d=a+1` as the vertical fiber. If `C(o)` is the vertical open cluster, define

\[
\varphi_d(p)=\mathbb E_p\left[1-(1-p)^{|C(o)|}\right].
\]

The fiber-cluster exploration is a Galton–Watson process whose mean offspring is `q varphi_d(p)`: conditional on the vertical cluster, each child fiber is reached iff at least one of the corresponding horizontal edges out of that cluster is open. Therefore

\[
q\varphi_d(p)>1\quad\Longrightarrow\quad
p_c(T_d\square T_{q+1})<p,
\tag{3.1}
\]

where strictness follows because the finite lower witnesses below are continuous polynomials and remain supercritical at some `p'<p`.

### Radius one

Using only the root and its `d` vertical neighbors gives

\[
L_d(p):=1-(1-p)(1-p^2)^d\le\varphi_d(p).
\tag{3.2}
\]

Indeed failure means that the root horizontal edge is closed and, independently for each vertical neighbor, not both the vertical edge and that neighbor's horizontal edge are open.

### Radius two

Let `s=1-p`. In one root branch, radius-two failure occurs if either the first vertical edge is closed, or it is open, the depth-one horizontal edge is closed, and each of the `d-1` depth-two directions either has its vertical edge closed or has that edge open and its terminal horizontal edge closed. Hence

\[
B_d^{(2)}(p)
=s+p\,s(1-p^2)^{d-1}.
\]

Including the root horizontal edge and all `d` first branches, the no-activation probability is

\[
Q_d^{(2)}(p)=s\,[B_d^{(2)}(p)]^d.
\]

Therefore

\[
\boxed{
\Phi_d^{(2)}(p)
:=1-(1-p)\left[(1-p)+p(1-p)(1-p^2)^{d-1}\right]^d
\le\varphi_d(p).
}
\tag{3.3}
\]

This is an exact finite polynomial/rational witness when `p` is rational.

## 4. New theorem: all standard surface products except `(2,2)`

**Theorem 4.1.** Let `g,h>=2`, and let `X_{g,h}` be the standard Cartesian Cayley graph above. If `(g,h)!=(2,2)`, then

\[
\boxed{p_c(X_{g,h})<p_{2\to2}(X_{g,h})\le p_u(X_{g,h}).}
\]

More precisely, after swapping `g,h` if necessary so that `g<=h`, the following explicit bounds hold.

### (i) `(g,h)=(2,3)`

Here `d=6`, `q=9`, `D=20`, and

\[
R=10+2\sqrt5,
\qquad
\beta=5+\sqrt5+\sqrt{11+10\sqrt5}.
\]

The exact checker verifies

\[
9\Phi_6^{(2)}(73/1000)-1>0.
\]

Thus by (3.1),

\[
p_c(X_{2,3})<\frac{73}{1000}.
\]

To compare with the nonbacktracking threshold, write `s=sqrt(5)`. The inequality

\[
73\left(5+s+\sqrt{11+10s}\right)<1000
\]

has positive right side after isolating the last radical. Squaring reduces it to

\[
146000\sqrt5<371251.
\]

This is exact because

\[
5\cdot146000^2=106580000000
<137827305001=371251^2.
\]

Therefore

\[
\boxed{
 p_u(X_{2,3})-p_c(X_{2,3})
 >\frac1{5+\sqrt5+\sqrt{11+10\sqrt5}}-\frac{73}{1000}
 =0.00385249999023046\ldots .}
\tag{4.1}
\]

### (ii) `(g,h)=(2,4)`

Here `d=6`, `q=13`, `D=24`, and

\[
R=4+2\sqrt5+2\sqrt{13}.
\]

The exact radius-one check gives

\[
13L_6(1/16)-1
=\frac{429506134774077}{4503599627370496}>0,
\]

so `p_c<1/16`. Moreover

\[
\sqrt5+\sqrt{13}<6
\]

because after one positive-side square this reduces to `sqrt(65)<9`, i.e. `65<81`. Hence `R<16`; by (2.4), `beta<R<16`, so

\[
\boxed{
 p_u(X_{2,4})-p_c(X_{2,4})
 >\beta(24,R)^{-1}-\frac1{16}
 =0.00869601377312389\ldots .}
\tag{4.2}
\]

### (iii) `(g,h)=(3,3)`

Here `d=10`, `q=9`, `D=24`, `R=16`, and

\[
\beta(24,16)=8+\sqrt{41}.
\]

The exact radius-one check gives

\[
9L_{10}(137/2000)-1>0,
\]

so `p_c<137/2000`. Also

\[
137(8+\sqrt{41})<2000
\]

is equivalent to `137sqrt(41)<904`, certified by

\[
137^2\cdot41=769529<817216=904^2.
\]

Therefore

\[
\boxed{
 p_u(X_{3,3})-p_c(X_{3,3})
 >\frac1{8+\sqrt{41}}-\frac{137}{2000}
 =0.000929380981180491\ldots .}
\tag{4.3}
\]

### (iv) Generic regime `g>=3,h>=4`

Set `x=sqrt(b)=sqrt(4h-3)`. Since `g<=h`, `u<=x`, and therefore

\[
R=4+2u+2x\le4+4x.
\]

Put

\[
p_x:=\frac1{4(1+x)}.
\]

Then

\[
p_x\le\frac1R<\frac1{\beta(D,R)}.
\tag{4.4}
\]

Here `d=a+1>=10` and `q=b=x^2`, so it suffices to show `x^2 L_{10}(p_x)>1`. Since

\[
L_{10}(p)=p+(1-p)\left[1-(1-p^2)^{10}\right]
\]

and

\[
1-(1-z)^{10}\ge10z(1-z)^9\ge10z(1-9z),
\]

we obtain, whenever `p<=1/18`,

\[
x^2L_{10}(p)
\ge x^2p+\frac{17}{18}\,10x^2p^2(1-9p^2).
\tag{4.5}
\]

For `h>=4`,

\[
x\ge\sqrt{13}>\frac{18}{5},
\]

while at `x=18/5` we have `p_x=5/92<1/18`. Each of
`x^2p_x`, `x^2p_x^2`, and `1-9p_x^2` is positive and increasing in `x`; hence the right side of (4.5) is increasing. At the rational comparison point `x=18/5` the exact checker gives

\[
\frac{94587903}{89549120}
=1+\frac{5038783}{89549120}>1.
\]

Thus `x^2 L_{10}(p_x)>1` throughout this regime. Equations (3.1) and (4.4) yield

\[
\boxed{
 p_u(X_{g,h})-p_c(X_{g,h})
 >\frac1{\beta(D,R)}-\frac1{4(1+\sqrt{4h-3})}>0
}
\tag{4.6}
\]

for all `3<=g<=h` with `h>=4`.

### (v) Generic regime `g=2,h>=5`

Again set `x=sqrt(4h-3)` and `p_x=1/[4(1+x)]`. Now `d=6` and `q=x^2`. Since `h>=5`,

\[
x\ge\sqrt{17}>\frac{41}{10},
\qquad
p_x\le\frac5{102}<\frac1{20}.
\]

Using

\[
1-(1-z)^6\ge6z(1-z)^5\ge6z(1-5z)
\]

gives

\[
x^2L_6(p_x)
\ge x^2p_x+\frac{19}{20}\,6x^2p_x^2(1-5p_x^2).
\tag{4.7}
\]

The factors on the right are again positive and increasing in `x`. At `x=41/10` the exact value is

\[
\frac{1517561413}{1443242880}
=1+\frac{74318533}{1443242880}>1.
\]

Thus (3.1) and (4.4) give the same quantitative conclusion (4.6) for every `g=2,h>=5`.

The cases (i)–(v), plus symmetry in `g,h`, cover every pair `g,h>=2` except `(2,2)`. This proves Theorem 4.1. `square`

## 5. Frozen `G_{3,4}` metric improvement

For the preceding frozen graph, `d=10`, `q=13`. The new radius-two witness gives the exact strict inequality

\[
13\Phi_{10}^{(2)}(19/400)-1>0.
\]

Its exact numerator/denominator are archived in the checker output; numerically the positive margin is

\[
0.004079785862769334\ldots.
\]

Therefore

\[
p_c(G_{3,4})<\frac{19}{400}.
\]

The preceding nonbacktracking lower bound remains

\[
p_u(G_{3,4})\ge p_{2\to2}(G_{3,4})
\ge\frac1{\beta_*},
\quad
\beta_*=5+\sqrt{13}+\sqrt{11+10\sqrt{13}}.
\]

The old exact radical certificate `beta_*<50/3` immediately gives

\[
\frac{19}{400}\beta_*<\frac{19}{400}\frac{50}{3}=\frac{19}{24}<1.
\]

Hence the frozen quantitative metric improves to

\[
\boxed{
\delta_{\rm surf}
:=\text{certified lower bound on }p_u(G_{3,4})-p_c(G_{3,4})
>
\frac1{\beta_*}-\frac{19}{400}
=0.017161080967165520\ldots .}
\tag{5.1}
\]

The numerical lower-bound constant increased by exactly

\[
\frac{13}{251}-\frac{19}{400}
=\frac{431}{100400}
=0.004292828685258964\ldots.
\tag{5.2}
\]

This is genuine movement of the frozen family metric, not a repeated checker.

## 6. The remaining `(2,2)` obstruction

For `X_{2,2}`, the current norm bound gives

\[
D=16,\qquad R=4+4\sqrt5,
\]

and the nonbacktracking comparison point is

\[
p_{\rm NB}=\beta(16,R)^{-1}\approx0.08578129994717.
\]

I tested the **full**, not truncated, one-sided vertical `T_6` cluster recursion. If `H` is the probability that a forward `T_6` branch contains no horizontal child edge, then at fixed `p`

\[
H=(1-p)\bigl[(1-p)+pH\bigr]^5,
\]

and

\[
\varphi_6(p)=1-(1-p)\bigl[(1-p)+pH\bigr]^6.
\]

Numerically at `p=p_NB`,

\[
5\varphi_6(p_{\rm NB})\approx0.74633817160493<1.
\]

This says that the present **one-sided fiber Galton–Watson mechanism** appears quantitatively incapable of closing `(2,2)` at the available NB threshold, even when the entire vertical cluster is used. It is **not** an exact impossibility theorem: the fixed point and comparison were evaluated numerically, and a different multi-child/backscattering or sharper operator route may work. No exact obstruction label is claimed in this run.

The natural next mathematical question inside PROB10-09 is therefore not another larger finite radius for `(3,4)`; it is either (a) a multi-child exploration that captures correlations between several forward fibers for `(2,2)`, or (b) a nonproduct construction outside the current known product/acylindrically-hyperbolic/relative-normal scopes that is not already owned by NM11.

## 7. Executed checks

The executed exact checker and its actual output are

- `artifacts/prob10_2026-09-20/PROB10-09/surface_product_family_exact.py`,
- `artifacts/prob10_2026-09-20/PROB10-09/surface_product_family_exact.out`.

The checker verifies with `fractions.Fraction` / integer inequalities:

- `13 Phi_10^(2)(19/400)>1`;
- `9 Phi_6^(2)(73/1000)>1`;
- `13 L_6(1/16)>1`;
- `9 L_10(137/2000)>1`;
- the sign-safe radical comparison for `(2,3)`;
- the sign-safe radical comparison for `(3,3)`;
- `R_{2,4}<16`;
- the generic `g>=3,h>=4` monotone base margin `5038783/89549120>0`;
- the generic `g=2,h>=5` monotone base margin `74318533/1443242880>0`;
- the exact frozen-gap improvement `431/100400>0`.

The output ends

`VERDICT=PASS_EXACT_ARITHMETIC_CORE`

and

`STATUS=SELF_CHECK_ONLY_PARTIAL_FOR_BENJAMINI_SCHRAMM`.

The `(2,2)` full-tree value in the same output is explicitly labeled `NUMERICAL_DIAGNOSTIC_ONLY` and is not used in any theorem.

No independent other-track audit is claimed. The theorem is a self-checked candidate restricted result; the universal source cannot be called closed without a source-level proof and independent validation.

## 8. Metrics and residual source gap

### Parent source metric

Before this run: universal Cayley-graph Benjamini–Schramm target **OPEN / PARTIAL**.

After this run: universal Cayley-graph Benjamini–Schramm target **OPEN / PARTIAL**. There is no universal source-level closure movement.

### Frozen family quantitative metric

Before:

\[
\delta_{\rm surf}>
\frac1{\beta_*}-\frac{13}{251}
=0.01286825228190655\ldots.
\]

After:

\[
\delta_{\rm surf}>
\frac1{\beta_*}-\frac{19}{400}
=0.01716108096716552\ldots.
\]

Exact improvement of the certified constant: `431/100400`.

### Auxiliary theorem-scope delta

Before: one explicit standard surface-product pair `(3,4)` had a self-contained quantitative certificate.

After: every standard surface-product `X_{g,h}` with `g,h>=2` except `(2,2)` has a proved explicit positive `p_u-p_c` lower bound under the formulas above. This is **auxiliary PARTIAL scope**, and Peres (2000) means it must not be advertised as an uncovered qualitative product class without a much stronger prior-art analysis.

### Full unresolved obligation

Still missing is a mechanism that handles an **arbitrary** finite generating set of an arbitrary finitely generated nonamenable group. Nothing above proves that every such Cayley graph contains a free subgroup with favorable generator bookkeeping, admits a product-fiber decomposition, or satisfies a universal NB comparison. The full conjecture therefore remains open here.

## ledger_delta

```yaml
ledger_delta:
  worker: R20
  assignment: PROB10-09
  source: "Benjamini--Schramm nonuniqueness conjecture for iid bond percolation on every locally finite Cayley graph of every finitely generated nonamenable group"
  parent_status_before: OPEN_PARTIAL
  parent_status_after: OPEN_PARTIAL
  frozen_family:
    graph: "G_{3,4}=standard Cartesian Cayley graph of Gamma_3 x Gamma_4"
    metric: delta_surf_certified_lower_bound_on_pu_minus_pc
    before_exact: "1/(5+sqrt(13)+sqrt(11+10sqrt(13))) - 13/251"
    before_decimal: "0.01286825228190655..."
    after_exact: "1/(5+sqrt(13)+sqrt(11+10sqrt(13))) - 19/400"
    after_decimal: "0.01716108096716552..."
    improvement_exact: "431/100400"
  auxiliary_delta:
    theorem_scope: "all standard surface products Gamma_g x Gamma_h, g,h>=2, except (2,2), with explicit positive quantitative gap formulas"
    new_mechanism: "radius-two exact fiber-cluster branching plus parameter-monotone genus envelopes"
    unresolved_family_corner: "(2,2); full one-sided cluster recursion at current NB point is below mean 1 numerically only"
  ownership_boundary:
    predecessor_handoff: "runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md"
    companion_not_overwritten: "proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T02-52-26+0300__t09-subgroup-nonbacktracking-sl3z-gap.md"
  methods:
    - "finite-depth fiber-cluster branching (successful)"
    - "parameter-monotone surface-product family proof (successful)"
    - "nonproduct subgroup/NB route checked but not duplicated because NM11 owns it; Peres product theorem used as prior-art negation test"
  prior_art_correction:
    source: "Yuval Peres, Percolation on nonamenable products at the uniqueness threshold, 2000"
    effect: "standard surface products are within a known direct-product uniqueness-threshold theorem; quantitative certificate remains valid, novelty unverified"
  evidence:
    - "operations/PROB10_2026-09-20.md"
    - "operations/PROGRESS20_2026-09-20.md"
    - "POSTED.md"
    - "probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md"
    - "probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/notes/round_011.md"
    - "probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/notes/round_018.md"
    - "probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/notes/round_040.md"
    - "probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/notes/round_042.md"
    - "probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/notes/round_053.md"
    - "probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/notes/round_054.md"
    - "probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/notes/round_055.md"
    - "artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T00-55-00Z_surface_product_family_depth2_idea.md"
    - "artifacts/prob10_2026-09-20/PROB10-09/surface_product_family_exact.py"
    - "artifacts/prob10_2026-09-20/PROB10-09/surface_product_family_exact.out"
  audits:
    self_check: PASS_EXACT_ARITHMETIC_CORE
    independent_other_track_audits: NONE_THIS_RUN
  remaining_obligation: "universal pc<pu for every locally finite Cayley graph of every finitely generated nonamenable group"
  runtime:
    requested: "GPT-6 maximum"
    actual_model: "GPT-5.6 Sol"
    reasoning_level: UNVERIFIED
```
