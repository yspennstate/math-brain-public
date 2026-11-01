Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-FAMILY METRIC MOVED: certified `X_{3,4}` gap `>0.02441444290890310... -> >2649449/100000000 = 0.02649449`; parent Benjamini–Schramm source remains OPEN/PARTIAL. Auxiliary mechanism progress: the finite-depth tree-fibre witness is replaced by an exact full-tree pgf criterion certifiable by a rational fixed-point supersolution.**

# PROB10-09 — exact infinite-tree fibre activation sharpens the frozen `X_{3,4}` nonuniqueness certificate

## 0. Frozen source, continuity, ownership and current status

The owner-frozen parent is unchanged:

\[
\forall G=\operatorname{Cay}(\Gamma,S),\qquad
\Gamma\text{ finitely generated and nonamenable},\qquad
p_c(G)<p_u(G)
\]

for iid **bond** percolation. This run does not substitute any planar site-percolation statement. The universal source remains **OPEN / PARTIAL**.

The required R20 predecessor handoff already exists and remains controlling for the refocus:

`runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`, blob `6e1b9e54cbc01461d32b523854c3bd82e50bfd04`.

It preserves the frozen Paley/KNSV/BMO predecessor ownership and artifacts and records that R20 no longer researches them while assigned to PROB10-09.

The immediate PROB10-09 predecessor is

`runs/prob10_2026-09-20/PROB10-09/2026-09-20T01-58-30Z_nagnibeda_spectral_upgrade_x22_closure_6d8c42.md`, blob `a86291abef734345b855996fd8410ac0cfa283b3`.

That report proved a self-checked quantitative certificate for every standard surface-product graph `X_{g,h}`, `g,h>=2`, and for the frozen graph

\[
X_{3,4}=\operatorname{Cay}(\Gamma_3\times\Gamma_4,
(S_3\times\{1\})\cup(\{1\}\times S_4))
\]

it established

\[
p_u(X_{3,4})-p_c(X_{3,4})
>0.0244144429089031045\ldots .
\]

The June archive was retained rather than restarted. In particular the current work depends on and preserves

- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`, blob `ee8bde8735e84ff75d3a625fed61e9bafbefd64f`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`, blob `d94127841f3b335a32b7936b86d8dee7a6b8d093`;
- the June nonbacktracking/product/fibre attempts summarized there, including the nonbacktracking polynomial transfer and the product-tree stress tests;
- current `operations/PROB10_2026-09-20.md`;
- current `POSTED.md`, which does not list the frozen universal Benjamini–Schramm source as closed or posted.

### Neighbor ownership / nonduplication

The newest related neighboring route read before this attack is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T05-50-00+0300__t09-triangle-fibre-degree9-sl-n-gap.md`.

NM13-11 is working the distinct **free-core/complement / higher-rank-lattice** lane, including `SL_n(Z)` applications and a triangle-fibre subgroup construction. This report does not edit, absorb or duplicate that claim. R20 stays on its already-delimited **standard surface-product quantitative / full-tree fibre / nonbacktracking** lane.

Repository search also recovered the old intake alias `D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)` as a HARD famous source alias. No current canonical claim was found assigning R20's exact quantitative surface-product subroute to another worker.

## 1. Current primary-source check

A bounded current check on 20 September 2026 retained these source distinctions.

1. Hutchcroft, arXiv:1804.10191 / GOFA 2019, proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs. This is a major known special case, not the universal Cayley theorem.
2. Hutchcroft–Pan, arXiv:2409.12283, studies uniqueness-threshold behavior using subgroup relativization, including new `p_u` results for groups with certain `wq`-normal subgroups. It does not state the universal fixed-Cayley-graph theorem.
3. Terlov–Timár, arXiv:2502.02560, concerns weighted amenability / nonunimodular variants and does not settle the frozen source.
4. The 2026 planar-site papers concern a different Benjamini–Schramm planar-site conjecture and are not substitutions for this bond-percolation Cayley problem.
5. Peres (2000), *Percolation on nonamenable products at the uniqueness threshold*, already supplies qualitative product nonuniqueness results. Therefore the standard surface-product family below is **not claimed as a new qualitative family**. The tracked contribution here is the explicit quantitative certificate and the exact full-tree fibre mechanism.

A fresh bounded search did not locate a 2026 primary source announcing a proof of the universal nonamenable Cayley-graph bond-percolation conjecture. This is negative search evidence, not a worldwide novelty certificate.

## 2. Idea before code and three genuinely different routes

The idea was written before code at

`artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T03-20-00Z_tree_fibre_fixed_point_idea.md`.

Three routes were compared.

### Route 1 — exact infinite-tree fibre pgf by rational supersolution: SUCCESSFUL

The predecessor used a radius-two truncation of the vertical tree cluster to upper-bound `p_c`. That leaves substantial probability mass unused. The new route writes the **exact** Galton–Watson pgf for the full subcritical vertical tree cluster and avoids solving its high-degree fixed-point equation by producing one rational supersolution. This moved the frozen metric.

### Route 2 — reverse the product orientation: NOT COMPETITIVE

The embedded comparison is `T_10 square T_14`. One may instead use `T_14` vertically and orient `T_10`. Direct fixed-point exploration shows that the reverse orientation requires a larger activation probability than the `T_10`-vertical / thirteen-forward-child orientation used below. This was used only to reject the route; no source theorem is claimed from the exploratory decimal comparison.

### Route 3 — sharpen the `p_u` side via a genus-four surface spectral theorem: NO NEW INPUT FOUND

The prior run imported Nagnibeda's sharp rigorous Markov spectral-radius bounds for genera 2 and 3, as quoted in Bartholdi, arXiv:math/0112108, Theorem 1.3. The same theorem explicitly records sharp values only for genera 2 and 3. A bounded current search did not recover a comparably sharp rigorous genus-four upper bound. I therefore do not invent one; the genus-four factor keeps the elementary Freiheitssatz bound. The metric move comes from the `p_c` side instead.

The neighboring free-core/complement route was deliberately excluded because it is already active under NM13-11.

## 3. Full-tree fibre activation lemma

This is the main new mechanism in the run.

Let `T_d` be the `d`-regular tree and let `p<1/(d-1)`. Put

\[
s=1-p.
\]

Consider a rooted branch of `T_d`, so every nonroot vertex has `d-1` forward neighbors. If `H` denotes the pgf of the size of the open branch cluster, evaluated at `s`, the Galton–Watson recursion gives

\[
H=s(1-p+pH)^{d-1}.
\tag{3.1}
\]

Define

\[
F(x):=s(1-p+px)^{d-1}.
\]

For `0<=x<=1`,

\[
0\le F'(x)
=s p(d-1)(1-p+px)^{d-2}
\le s p(d-1)<1.
\tag{3.2}
\]

Thus `F` is a strict contraction on `[0,1]`; it has a unique fixed point `h_*` there, and `F(x)-x` is strictly decreasing.

The root of `T_d` has `d` incident branches, so the pgf of the full root cluster `C(o)` is

\[
\mathbb E_p[s^{|C(o)|}]
=s(1-p+p h_*)^d.
\tag{3.3}
\]

Now place this vertical tree in `T_d\square T_{q+1}` and orient the second tree away from a root. Given a realized vertical open cluster `C(o)`, the probability that no open horizontal edge goes from `C(o)` into one specified forward fibre is `s^{|C(o)|}`. Therefore the exact forward-fibre activation probability is

\[
\phi_d(p)
=1-\mathbb E_p[s^{|C(o)|}]
=1-s(1-p+p h_*)^d.
\tag{3.4}
\]

Different forward fibres use disjoint horizontal edges and fresh vertical clusters. The standard fibre exploration therefore dominates/realizes the one-type Galton–Watson comparison with mean

\[
q\phi_d(p).
\]

Hence

\[
q\phi_d(p)>1
\quad\Longrightarrow\quad
p_c(T_d\square T_{q+1})<p.
\tag{3.5}
\]

The strict `<p` follows because the inequalities below have positive slack and all displayed expressions vary continuously with `p`, so the same supercritical comparison holds for some `p'<p` sufficiently close to `p`.

### Rational supersolution certificate

The key exact simplification is this. If a rational `u in [0,1]` satisfies

\[
F(u)\le u,
\tag{3.6}
\]

then strict monotonicity of `F(x)-x` implies

\[
u\ge h_*.
\]

Since the right side of (3.4) decreases as `h_*` increases,

\[
\phi_d(p)
\ge 1-s(1-p+pu)^d.
\tag{3.7}
\]

Therefore the two exact rational checks

\[
F(u)<u,
\qquad
q\left[1-s(1-p+pu)^d\right]>1
\tag{3.8}
\]

are a full infinite-tree certificate. No numerical fixed-point solve and no finite-radius truncation enters the proof.

## 4. Apply the lemma to the frozen graph `X_{3,4}`

For the standard genus-`g` surface group

\[
\Gamma_g=
\langle a_1,b_1,\ldots,a_g,b_g\mid
[a_1,b_1]\cdots[a_g,b_g]=1\rangle,
\]

Magnus Freiheitssatz gives a free subgroup of rank `2g-1` by omitting one standard generator. Therefore the standard Cayley graph of `Gamma_3` contains `T_10`, and that of `Gamma_4` contains `T_14`. Hence

\[
T_{10}\square T_{14}\subseteq X_{3,4}.
\tag{4.1}
\]

Use `T_10` vertically and orient `T_14`; thus

\[
d=10,\qquad q=13.
\]

Set exactly

\[
p_0=\frac{4540551}{100000000}=0.04540551,
\qquad
s_0=1-p_0,
\tag{4.2}
\]

and choose the rational supersolution

\[
u=\frac{9261812689}{10000000000}=0.9261812689.
\tag{4.3}
\]

The executed exact checker gives

\[
s_0p_0(d-1)
=\frac{3900946469547591}{10^{16}}<1,
\tag{4.4}
\]

and

\[
u-F(u)>0,
\qquad
u-F(u)=2.768190633360405751\times10^{-11}\ldots,
\tag{4.5}
\]

with the complete exact rational numerator/denominator archived in the output file. It also gives

\[
13\left[1-s_0(1-p_0+p_0u)^{10}\right]-1
>0,
\tag{4.6}
\]

with exact positive rational value and decimal margin

\[
9.623590018794654934\times10^{-8}\ldots .
\]

By (3.6)--(3.8),

\[
13\phi_{10}(p_0)>1.
\]

Using (4.1) and monotonicity of `p_c` under adding edges,

\[
\boxed{
 p_c(X_{3,4})<\frac{4540551}{100000000}.
}
\tag{4.7}

This replaces the predecessor's `p_c<19/400=0.0475` by a much sharper exact full-tree certificate.

## 5. A clean fully rational `p_u` floor

The previous spectral input is retained. Nagnibeda's rigorous genus-three Markov bound gives

\[
\|A_3\|<\frac{1659}{250}.
\]

For genus four, deleting one standard generator gives a free rank-seven subgroup, so

\[
\|A_4\|\le2+2\sqrt{13}.
\]

Thus for the degree-28 product graph

\[
\|A_{3,4}\|
<R_{34}:=\frac{2159}{250}+2\sqrt{13}.
\tag{5.1}
\]

The nonbacktracking recurrence has `Q=D-1=27`. If `beta` is the corresponding larger characteristic root, the already-established transfer gives

\[
p_{2\to2}(X_{3,4})\ge\beta^{-1}
\quad\text{and}\quad
p_{2\to2}(X_{3,4})\le p_u(X_{3,4}).
\tag{5.2}
\]

For this run take

\[
z_0=\frac{10000}{719}.
\]

Use the elementary exact bounds

\[
\frac{18}{5}<\sqrt{13}<\frac{1803}{500},
\]

verified by

\[
13-\left(\frac{18}{5}\right)^2=\frac1{25}>0,
\qquad
\left(\frac{1803}{500}\right)^2-13=\frac{809}{250000}>0.
\]

Hence

\[
R_{34}<\frac{2159}{250}+2\frac{1803}{500}
=\frac{1981}{125}=:\overline R.
\tag{5.3}
\]

The checker verifies exactly

\[
z_0^2-27=\frac{86042053}{516961}>0
\tag{5.4}
\]

and

\[
z_0^2-\overline R z_0+27
=\frac{10827}{516961}>0.
\tag{5.5}
\]

Also the relevant discriminant is positive (the archived lower comparison gives `R_lower^2-108=8923681/62500>0`). Since `z_0>sqrt(27)` and the monic quadratic is positive at `z_0`, (5.5) places `z_0` strictly above its larger positive root. Monotonicity in the adjacency-norm parameter then gives

\[
\beta<z_0=\frac{10000}{719}.
\]

Therefore

\[
\boxed{
 p_u(X_{3,4})\ge p_{2\to2}(X_{3,4})
 >\frac{719}{10000}=0.0719.
}
\tag{5.6}

## 6. Frozen metric movement

Combining (4.7) and (5.6),

\[
\boxed{
 p_u(X_{3,4})-p_c(X_{3,4})
 >\frac{719}{10000}-\frac{4540551}{100000000}
 =\frac{2649449}{100000000}
 =0.02649449.
}
\tag{6.1}

The predecessor metric was

\[
>0.0244144429089031045\ldots,
\]

so the certified lower bound increases by more than

\[
0.00208004709.
\]

This is a real source-valid quantitative movement for the frozen graph, not merely a new checker for the same number.

The exact radical-valued predecessor lower bound on `p_u` is slightly stronger than the clean rational floor `719/10000`; the latter is used here so that the entire new certificate (6.1) is rational and independently re-executable.

## 7. Executed exact test

The checker was executed locally before persistence and its exact output archived unchanged:

- `artifacts/prob10_2026-09-20/PROB10-09/tree_fibre_fixedpoint_exact.py`;
- `artifacts/prob10_2026-09-20/PROB10-09/tree_fibre_fixedpoint_exact.out`.

The output ends

`ALL_EXACT_CHECKS_PASS`.

It verifies the contraction inequality, rational fixed-point supersolution, forward-fibre activation, rational square-root bounds, nonbacktracking root comparison, and the exact gap `2649449/100000000`.

This is a **self-check**, not an independent audit.

## 8. Source-level and auxiliary deltas kept separate

### Source-level parent

Before: **OPEN / PARTIAL**.

After: **OPEN / PARTIAL**.

The universal statement for every Cayley graph of every finitely generated nonamenable group is not proved or refuted.

### Frozen-family metric

Before:

\[
\delta_{34}:=p_u(X_{3,4})-p_c(X_{3,4})
>0.0244144429089031045\ldots .
\]

After:

\[
\boxed{\delta_{34}>2649449/100000000=0.02649449.}
\]

### Auxiliary mechanism delta

Before: `p_c` used a finite-radius cluster truncation.

After: full subcritical tree-cluster activation is reduced to the one-variable exact criterion

\[
F(u)\le u,
\qquad
q[1-s(1-p+pu)^d]>1,
\]

with rational `p,u`. This is a reusable structural certificate for any embedded `T_d square T_{q+1}` comparison. It remains only a sufficient criterion and does not solve the universal conjecture.

## 9. Remaining full gap

The source-level obstruction is still that a general nonamenable Cayley graph need not expose a quantitatively useful embedded product/free-fibre geometry, and no general argument has converted nonamenability alone into

\[
p_c(G)<p_{2\to2}(G)
\]

or directly into `p_c(G)<p_u(G)`.

The June finite-set-escape program records the corresponding general obstruction from the operator side: one needs a genuinely universal control of trapped two-point mass / boundary energy, not merely another restatement of the desired `L^2` inequality.

Thus this run is **PARTIAL**, with a stronger fixed-family quantitative theorem and a reusable exact fibre criterion, but no universal closure.

## 10. Delivery / continuity receipt fields

- parent: `PROB10-09 / Benjamini-Schramm nonuniqueness phase`;
- exact model convention: iid bond percolation, Cayley graph, nonamenable finitely generated group;
- predecessor handoff: `runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`;
- immediate predecessor: `runs/prob10_2026-09-20/PROB10-09/2026-09-20T01-58-30Z_nagnibeda_spectral_upgrade_x22_closure_6d8c42.md`;
- neighboring nonoverlap: NM13-11 higher-rank/free-core lane, newest read `2026-09-20T05-50-00+0300__t09-triangle-fibre-degree9-sl-n-gap.md`;
- source metric before: `delta_34 > 0.0244144429089031045...`;
- source metric after: `delta_34 > 2649449/100000000 = 0.02649449`;
- auxiliary delta: exact full-tree fibre pgf supersolution criterion;
- status: `OPEN / PARTIAL`;
- validation: exact self-check PASS; independent validation still absent;
- schedule/email/Drive/public-posting actions: none.
