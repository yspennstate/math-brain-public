Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. STRUCTURAL-SCOPE METRIC MOVED: the preceding R20 theorem covered one non-split central surface extension and a bounded arbitrary-generator perturbative range; this run proves a strict bond-percolation nonuniqueness phase for every standard iterated central amalgam of at least two closed-surface central extensions. The smallest new graph `(g_1,g_2)=(2,2)` moves UNMEASURED -> certified `p_u-p_c>1/1500`. Parent Benjamini–Schramm remains OPEN/PARTIAL.**

# PROB10-09 — central amalgams of surface extensions: an infinite new fixed-generator family

## 0. Frozen source, continuity, ownership, and runtime honesty

The owner-frozen source remains exactly

\[
 p_c(G)<p_u(G)
\]

for iid **BOND** percolation on every locally finite Cayley graph `G=Cay(Gamma,S)` of every finitely generated nonamenable group. No planar site-percolation variant is substituted. A restricted family remains **PARTIAL**.

The native scheduler exposes no authenticated model/effort selector or guaranteed run length. The model visible to this run is GPT-5.6 Sol; reasoning effort is not authenticated by scheduler telemetry and is therefore reported **UNVERIFIED**. No schedule, enablement, notification, email, Drive, or public-posting setting was changed.

The required pre-refocus R20 handoff already exists and was re-read rather than duplicated:

- `runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`, blob `6e1b9e54cbc01461d32b523854c3bd82e50bfd04`.

It preserves the actual predecessor R20 state: Paley/I0100 `p_max=1213` with its full exact covered-prime set, KNSV restricted diagnostics, and BMO `n_all=9`, together with their artifacts and historical ownership. None of those tracks is edited here.

Controlling evidence consumed before the new proof:

- `operations/PROB10_2026-09-20.md`;
- current `POSTED.md`;
- source alias `D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)`, still catalogued as a HARD famous problem rather than a closed claim;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`;
- immediate R20 predecessor `runs/prob10_2026-09-20/PROB10-09/2026-09-20T06-59-30Z_arbitrary_generator_augmentation_robustness_7b3e91.md`;
- newest neighboring lane located before research: `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T09-50-00+0300__t09-free-subgroup-augmentation-tail.md`.

The neighboring NM13-11 lane is currently proving subgroup/nonbacktracking transfers on Rattaggi/product-of-trees graphs and arbitrary free-generator augmentations. The present run stays in R20's already delimited **central-extension Fourier/magnetic lane** and changes the ambient group by central amalgamation. It does not overwrite or rebrand the neighboring claim.

The June archive's normalized-kernel escape, BK finite-volume/boundary dichotomy, killed-SAW, boundary-energy, global SAW-operator, quotient/fibre-shell, and earlier nonbacktracking bridge attempts are treated as consumed history, not as new work.

## 1. Current-source and prior-art check — 20 September 2026

The owner-specified and current sources were rechecked before making any unresolved-status statement.

1. **Hutchcroft, arXiv:1804.10191 / GOFA 2019** proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs. The groups below contain `Z^2` because the common infinite central element commutes with an infinite-order surface lift, so this theorem does not directly cover them.

2. **Hutchcroft--Pan, arXiv:2409.12283** explicitly states that the converse-to-Burton--Keane / Benjamini--Schramm nonuniqueness conjecture remains open in general. Their new amenable-`wq`-normal application assumes an amenable subgroup of exponential growth. The common central subgroup used below is `Z`, of linear growth.

3. **Terlov--Timar, arXiv:2502.02560** concerns weighted amenability and the heavy-cluster threshold `p_h`; it proves a relaxed weighted/nonunimodular result and does not state the fixed standard-Cayley theorem below.

4. **Choi--Seo, arXiv:2508.08932** proves a nonuniqueness phase for every Cayley graph of every acylindrically hyperbolic group. The groups below have infinite centre; a non-elementary acylindrically hyperbolic group has finite centre, so this class is not covered by that theorem.

5. **Juschenko--Nagnibeda, arXiv:1206.2183** proves existence of a favorable generating set when a group has an infinite normal subgroup with nonamenable quotient. The groups below satisfy that algebraic pattern, but the theorem proved here concerns one explicit frozen natural generating set and a quantitative certificate, not merely existence of some generating set.

6. **Martineau--Severo, arXiv:1803.09686** gives strict monotonicity of `p_c` under suitable covering/quotient maps. This is useful context for one failed route below, but by itself it does not supply the needed lower bound on `p_u` for the present infinite-fibre central extensions.

7. A paper submitted 10 September 2026, arXiv:2609.11845, still refers to the classical Benjamini--Schramm nonamenability/nonuniqueness statement as a conjectural general principle. No all-Cayley resolution was found in the bounded current search.

8. Dated searches for `central extension surface group percolation p_c p_u`, `surface group central extension Cayley percolation`, `amalgamated surface groups percolation p_c p_u`, and `infinite center Cayley p_c p_u` did not locate a source stating the theorem below. This is **negative bounded-search evidence only**, not a worldwide novelty or priority certificate.

The spectral input is the same rigorous surface-group bound already used in the predecessor track: for the standard `4g`-regular Cayley graph of the closed orientable surface group `Gamma_g`, Żuk's estimate gives

\[
 \|M_g\|\le g^{-1/2},
\]

hence its unnormalized adjacency operator satisfies

\[
 \|A_{\Gamma_g}\|\le 4\sqrt g.
\tag{1.1}
\]

## 2. Metrics: source level and mechanism/scope kept separate

### Parent source metric

Before: `OPEN/PARTIAL`.

After: `OPEN/PARTIAL`.

No universal implication for arbitrary nonamenable groups or arbitrary Cayley generating sets is claimed.

### Structural-scope metric

Before this run, R20 had proved the standard non-split central surface-extension family

\[
E_{g,e},\qquad g\ge2,\ e\ne0,
\]

and then a bounded perturbative result under small arbitrary symmetric generator augmentation.

After this run, the proof covers **every iterated central amalgam of at least two such factors**, with all standard generators retained:

\[
\boxed{
\mathcal E_{\mathbf g,\mathbf e}
=E_{g_1,e_1}*_{\langle z\rangle}E_{g_2,e_2}*_{\langle z\rangle}\cdots*_{\langle z\rangle}E_{g_r,e_r},
\quad r\ge2,\quad g_i\ge2,\quad e_i\ne0.
}
\tag{2.1}
\]

This is an infinite multi-parameter family of new fixed standard Cayley graphs, not a finite enumeration.

### Auxiliary frozen quantitative metric

Freeze the smallest new member `r=2`, `g_1=g_2=2`, with arbitrary nonzero `e_1,e_2`. Before: `UNMEASURED` in this R20 lane. After:

\[
\boxed{p_u-p_c>\frac1{1500}=0.000666666666\ldots .}
\tag{2.2}
\]

The older frozen `X_{3,4}` gap `>0.03480012` and the one-factor central-extension certificates remain unchanged and are not overwritten by changing graph families.

## 3. Idea-before-code and three materially different methods

The new mathematical idea was written before any new checker:

- `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T07-52-00Z_central_surface_amalgam_idea.md`, creation commit `8bab3f87360e722e626b9f21996cd401fba9c30f`.

### Method A — strict quotient/cover monotonicity: useful but insufficient

Killing the common centre gives a free product of surface groups. On the horizontal-edge subgraph, the central extension is an infinite cyclic cover of that quotient Cayley graph, so strict `p_c` monotonicity under coverings points in the correct direction. But the full standard graph also contains central edges, and the covering theorem does not by itself provide the required lower bound on `p_u` for the infinite-fibre extension. This route therefore does **not** close the fixed graph on its own.

### Method B — subgroup comparison alone: gives `p_c`, not `p_u`

A large subgroup `F_k x Z` survives inside every central amalgam. It gives a strong percolating subgraph and hence an upper bound on `p_c`. However graph/subgroup inclusion has no monotonicity that would transfer the needed uniqueness-side lower bound in the required direction. The subgroup geometry alone is therefore incomplete.

### Method C — central Fourier norm + free-by-central percolation witness: SUCCESS

Use the `F_k x Z` subgroup for the critical side, but separately Fourier-transform along the common infinite centre for the operator side. Each surface factor becomes a magnetic surface adjacency operator and is diamagnetically dominated by the ordinary surface adjacency. The triangle inequality across free-product factors then gives a uniform adjacency norm. The nonbacktracking polynomial transfer converts this norm into a strict `p_{2->2}` lower bound. A coarse but exact global inequality shows the operator threshold beats the critical witness for **every** `r>=2`, `g_i>=2`.

The negation test was the smallest possible case `(g_1,g_2)=(2,2)`, where the margin is narrow. It still survives with an exact rational gap `1/1500`; hence the general argument is not hiding a large-genus-only assumption.

## 4. The new group family and its standard Cayley graphs

For each `i=1,...,r`, let

\[
E_{g_i,e_i}
=\left\langle
 a_{i,1},b_{i,1},\ldots,a_{i,g_i},b_{i,g_i},z_i
\;\middle|\;
 z_i\text{ central},\quad
 \prod_{j=1}^{g_i}[a_{i,j},b_{i,j}]=z_i^{e_i}
\right\rangle,
\tag{4.1}
\]

with `g_i>=2` and `e_i!=0`. As in the preceding R20 theorem, `z_i` has infinite order and

\[
1\to\langle z_i\rangle\cong\mathbb Z
\to E_{g_i,e_i}\to\Gamma_{g_i}\to1,
\tag{4.2}
\]

where `Gamma_{g_i}` is the closed orientable surface group of genus `g_i`.

Identify all the cyclic subgroups `\langle z_i\rangle` by `z_i=z` and form the iterated amalgamated free product (2.1). The normal-form theorem for free products with amalgamation implies that every factor embeds and the common subgroup `\langle z\rangle` remains infinite cyclic. Because `z` is central in every factor, it is central in the whole amalgam.

Equivalently,

\[
\mathcal E_{\mathbf g,\mathbf e}
=\left\langle z, a_{i,j},b_{i,j}
\;\middle|\;
 z\text{ central},\quad
 \prod_{j=1}^{g_i}[a_{i,j},b_{i,j}]=z^{e_i}\ (1\le i\le r)
\right\rangle.
\tag{4.3}
\]

Killing `z` gives

\[
\mathcal Q_{\mathbf g}
:=\mathcal E_{\mathbf g,\mathbf e}/\langle z\rangle
\cong
\Gamma_{g_1}*\Gamma_{g_2}*\cdots*\Gamma_{g_r}.
\tag{4.4}
\]

Indeed the quotient of each amalgam factor is its surface group, and the amalgamated subgroup becomes trivial. Conversely, if a reduced amalgam normal form maps trivially to the free product (4.4), each surviving factor syllable must lie in the common central subgroup, so the original element lies in `\langle z\rangle`. Thus the kernel of (4.4) is exactly `\langle z\rangle`.

Let

\[
S_{\mathbf g,\mathbf e}
=
\{a_{i,j}^{\pm1},b_{i,j}^{\pm1}:1\le i\le r,1\le j\le g_i\}
\cup\{z^{\pm1}\},
\tag{4.5}
\]

and define

\[
X_{\mathbf g,\mathbf e}
=\operatorname{Cay}(\mathcal E_{\mathbf g,\mathbf e},S_{\mathbf g,\mathbf e}).
\tag{4.6}
\]

Put

\[
G:=\sum_{i=1}^r g_i,
\qquad
H:=\sum_{i=1}^r\sqrt{g_i}.
\tag{4.7}
\]

Then `X` is `D=4G+2` regular. The quotient (4.4) is nonamenable, so `\mathcal E_{\mathbf g,\mathbf e}` is nonamenable. Hence every graph (4.6) is an admissible instance of the frozen parent conjecture.

These groups have infinite centre and contain `Z^2`, so they are neither Gromov hyperbolic nor non-elementary acylindrically hyperbolic. They are also not Cartesian products in the frozen `e_i!=0` presentation.

## 5. Exact free-by-central subgroup

Define

\[
k:=\sum_{i=1}^r(2g_i-1)=2G-r.
\tag{5.1}
\]

For each surface factor `Gamma_{g_i}`, omit (for definiteness) `b_{i,g_i}` and let `U_i` be the subgroup generated by

\[
a_{i,1},b_{i,1},\ldots,a_{i,g_i-1},b_{i,g_i-1},a_{i,g_i}.
\]

By Magnus Freiheitssatz applied to the standard one-relator surface presentation,

\[
U_i\cong F_{2g_i-1}.
\tag{5.2}
\]

Inside the free product (4.4), the union of these `U_i` generates their free product, therefore

\[
\langle U_1,\ldots,U_r\rangle
\cong
F_{2g_1-1}*\cdots*F_{2g_r-1}
\cong F_k.
\tag{5.3}
\]

Take the corresponding standard lifts in `\mathcal E_{\mathbf g,\mathbf e}` and adjoin `z`. There is a natural surjection

\[
F_k\times\mathbb Z\longrightarrow \widetilde H.
\]

If a word `w z^n` maps to the identity, its projection to (4.4) gives `w=1` in the free group (5.3). Since the selected quotient generators are freely independent, `w` reduces using only inverse cancellation, and the identical cancellations occur among the chosen lifts. Hence the lifted `w` is already the identity, so `z^n=1`. Since `z` has infinite order, `n=0`. Therefore

\[
\boxed{\widetilde H\cong F_k\times\mathbb Z.}
\tag{5.4}
\]

Using only the corresponding edges from (4.5),

\[
\boxed{T_{2k}\square\mathbb Z\subseteq X_{\mathbf g,\mathbf e}.}
\tag{5.5}
\]

This inclusion is the complete critical-side geometric input.

## 6. Strict critical-side estimate from the full `Z` fibre

Root the `T_{2k}` factor in (5.5). Every non-root tree vertex has

\[
b:=2k-1
\tag{6.1}
\]

forward children.

At an activated tree vertex, expose the entire open cluster of the seed in its vertical `Z` fibre. If `N` is its size then

\[
N=1+L_-+L_+,
\]

where `L_-` and `L_+` are independent geometric variables

\[
\mathbb P(L=m)=(1-p)p^m,\qquad m\ge0.
\]

For any fixed forward child fibre, conditional on `N`, there are `N` fresh horizontal candidate edges and therefore the activation probability is

\[
1-(1-p)^N.
\]

Different forward child fibres use disjoint horizontal edges, and once a child is activated we choose the first open crossing by a deterministic ordering before revealing that child's vertical cluster. Since distinct tree fibres are disjoint and every fibre has a unique parent in the oriented tree, this defines an honest Galton--Watson process whose mean offspring is

\[
\mu(p)=b\left(1-\mathbb E[(1-p)^N]\right).
\tag{6.2}
\]

Put `s=1-p`. Since

\[
\mathbb E[s^L]=\frac{1-p}{1-ps}=\frac{s}{1-ps},
\]

we obtain

\[
\mathbb E[s^N]
=s\left(\frac{s}{1-ps}\right)^2
=\frac{s^3}{(1-ps)^2}.
\tag{6.3}
\]

Evaluate at

\[
p_0=\frac1{b+1}=\frac1{2k}.
\tag{6.4}
\]

Then `s=b/(b+1)` and

\[
\mathbb E[s^N]
=\frac{b^3(b+1)}{(b^2+b+1)^2}.
\]

The inequality `\mu(p_0)>1` is equivalent to

\[
(b-1)(b^2+b+1)^2>b^4(b+1),
\]

and the exact difference is

\[
\boxed{b^3-b^2-b-1.}
\tag{6.5}
\]

In the present family `r>=2`, `g_i>=2`, so `G>=4`, `k=2G-r>=6`, and therefore `b>=11`. The polynomial in (6.5) is already `1198>0` at `b=11` and is increasing for `b>=1`. Thus `\mu(p_0)>1` for every graph in the family.

Since `\mu(p)` is continuous, it remains `>1` for some `p<p_0`. Consequently the retained Galton--Watson process survives at some parameter strictly below `p_0`, giving

\[
\boxed{
 p_c(X_{\mathbf g,\mathbf e})<\frac1{2k}
 =\frac1{4G-2r}.
}
\tag{6.6}
\]

This is a strict bound, not a non-strict subgraph estimate.

## 7. Central Fourier / diamagnetic adjacency bound

Because `z` is central and infinite, choose a set-theoretic section of (4.4) and identify

\[
\ell^2(\mathcal E_{\mathbf g,\mathbf e})
\cong
\ell^2(\mathcal Q_{\mathbf g})\otimes\ell^2(\mathbb Z).
\]

Fourier transform in the `Z` coordinate gives a direct integral over `theta in [0,2pi)`. Let `A_i(theta)` denote the contribution of the `4g_i` horizontal generators from factor `i`.

Right multiplication by a factor-`i` generator preserves each right coset of `Gamma_{g_i}` in the free product (4.4). On every such coset, `A_i(theta)` is a magnetic surface-group adjacency operator: the central cocycle contributes only unit-modulus phases. Pointwise,

\[
|A_i(\theta)f|\le A_{\Gamma_{g_i}}|f|.
\]

Therefore by (1.1)

\[
\|A_i(\theta)\|\le 4\sqrt{g_i}.
\tag{7.1}
\]

The two central edges contribute the scalar `2 cos(theta)`. Hence for the full adjacency operator `A_X`, uniformly in `theta`,

\[
\boxed{
\|A_X\|\le R:=4H+2.
}
\tag{7.2}
\]

No Euler-class parameter enters the bound.

## 8. Nonbacktracking transfer recalled with proof

Let `Y` be an infinite `D`-regular graph with adjacency operator norm at most `R`, and write

\[
Q=D-1.
\]

Let `B_n(x,y)` be the number of length-`n` nonbacktracking walks from `x` to `y`. The standard recurrence is

\[
B_0=I,\qquad B_1=A,
\]

with the degree correction at `n=2`, and for `n>=3`

\[
B_n=A B_{n-1}-Q B_{n-2}.
\tag{8.1}
\]

Thus `B_n` is a polynomial in `A`. By the spectral theorem, the exponential growth of `\|B_n\|` is controlled by the scalar recurrence

\[
u_n=\lambda u_{n-1}-Q u_{n-2},\qquad |\lambda|\le R.
\]

Its characteristic roots give the uniform growth exponent

\[
\beta_D(R)=
\begin{cases}
\sqrt Q,&R\le2\sqrt Q,\\[2mm]
\dfrac{R+\sqrt{R^2-4Q}}2,&R>2\sqrt Q.
\end{cases}
\tag{8.2}
\]

(up to a harmless polynomial factor at the repeated-root boundary).

Every open connection contains a self-avoiding, hence nonbacktracking, open path. The union bound therefore gives entrywise

\[
T_p(x,y)=\mathbb P_p(x\leftrightarrow y)
\le \sum_{n\ge0}p^nB_n(x,y).
\tag{8.3}
\]

All kernels in (8.3) are nonnegative, so matrix domination implies the same `l^2` operator domination. Whenever `p\beta_D(R)<1`, the right-hand operator series converges absolutely. Hence

\[
\boxed{p_{2\to2}(Y)\ge \beta_D(R)^{-1}.}
\tag{8.4}
\]

The standard two-point-threshold comparison gives

\[
p_{2\to2}(Y)\le p_u(Y).
\tag{8.5}
\]

For our graph, `D=4G+2` and

\[
Q=4G+1.
\tag{8.6}
\]

## 9. Uniform spectral inequality for every number of factors

Recall

\[
x:=2k=4G-2r.
\tag{9.1}
\]

We prove

\[
\boxed{\beta_D(R)<x.}
\tag{9.2}
\]

Since every `g_i>=2`,

\[
\sqrt{g_i}\le \frac{g_i}{\sqrt2},
\]

so

\[
H\le \frac{G}{\sqrt2}
\quad\Longrightarrow\quad
R\le R_0:=2\sqrt2\,G+2.
\tag{9.3}
\]

Also `r<=G/2`, hence

\[
x=4G-2r\ge3G.
\tag{9.4}
\]

First, `x^2>Q` because `x>=3G` and `9G^2>4G+1`. Thus if `R<=2\sqrt Q`, equation (8.2) gives `\beta_D(R)=\sqrt Q<x` immediately.

Assume now `R>2\sqrt Q`. Let

\[
P(t)=t^2-Rt+Q.
\]

The number `\beta_D(R)` is the larger root of `P`. We show that `x` lies strictly to its right.

By (9.3)--(9.4), for `G>=4`,

\[
x\ge3G>\sqrt2\,G+1\ge \frac R2.
\tag{9.5}
\]

Moreover, since `R<=R_0` and the polynomial `t^2-R_0t+Q` is increasing for `t>=R_0/2`,

\[
\begin{aligned}
P(x)
&\ge x^2-R_0x+Q\\
&\ge (3G)^2-R_0(3G)+4G+1\\
&=(9-6\sqrt2)G^2-2G+1.
\end{aligned}
\tag{9.6}
\]

Now

\[
9-6\sqrt2>\frac12.
\tag{9.7}
\]

Indeed (9.7) is equivalent to `17/2>6sqrt(2)`; both sides are positive, and squaring reduces this to the exact integer inequality

\[
289>288.
\]

Therefore

\[
P(x)>\frac12G^2-2G+1.
\tag{9.8}
\]

The right-hand side is increasing for `G>=4` and equals `1` at `G=4`. Hence `P(x)>0`. Together with (9.5), this places `x` strictly to the right of the larger root, proving (9.2).

Combining (8.4), (8.5), and (9.2),

\[
\boxed{
 p_u(X_{\mathbf g,\mathbf e})
 \ge p_{2\to2}(X_{\mathbf g,\mathbf e})
 \ge \beta_D(R)^{-1}
 >\frac1{2k}.
}
\tag{9.9}
\]

Finally (6.6) and (9.9) give the family theorem

\[
\boxed{
 p_c(X_{\mathbf g,\mathbf e})<p_u(X_{\mathbf g,\mathbf e})
\qquad
(r\ge2,\ g_i\ge2,\ e_i\ne0).
}
\tag{9.10}
\]

This is a complete proof for the stated restricted family, subject to the cited standard inputs (Freiheitssatz, Żuk's surface spectral bound, and the standard `p_{2->2}<=p_u` comparison). It is not a proof of the universal Benjamini--Schramm conjecture.

## 10. Smallest new graph: exact rational gap `1/1500`

Take

\[
r=2,\qquad g_1=g_2=2.
\]

Then

\[
G=4,\qquad H=2\sqrt2,\qquad k=6,
\]

so (6.6) gives

\[
\boxed{p_c<\frac1{12}.}
\tag{10.1}
\]

Here `D=18`, `Q=17`, and

\[
R\le 8\sqrt2+2.
\]

Set

\[
z=\frac{250}{21}.
\]

The exact rational bound

\[
\sqrt2<\frac{99}{70}
\tag{10.2}
\]

holds because

\[
\left(\frac{99}{70}\right)^2-2=\frac1{4900}>0.
\]

Also

\[
z^2-17=\frac{55003}{441}>0.
\tag{10.3}
\]

Finally

\[
 z+\frac{17}{z}
 =\frac{69997}{5250},
\]

while by (10.2)

\[
2+8\sqrt2<\frac{466}{35}=\frac{69900}{5250}.
\]

Thus

\[
 z+\frac{17}{z}-R>\frac{97}{5250}>0.
\tag{10.4}
\]

Equations (10.3)--(10.4) imply `z>\beta_{18}(R)`. Hence

\[
\boxed{p_u>\frac{21}{250}=0.084.}
\tag{10.5}
\]

Combining (10.1) and (10.5),

\[
\boxed{
 p_u-p_c>
 \frac{21}{250}-\frac1{12}
 =\frac1{1500}
 =0.000666666666\ldots .
}
\tag{10.6}
\]

This quantitative certificate is uniform in the two nonzero Euler classes `e_1,e_2`.

## 11. Executed checker and what it does / does not certify

After the idea note was committed, the exact checker

- `artifacts/prob10_2026-09-20/PROB10-09/central_surface_amalgam_exact.py`

was executed, and its actual output was archived at

- `artifacts/prob10_2026-09-20/PROB10-09/central_surface_amalgam_exact.out`.

The run ended

`ALL_EXACT_CHECKS_PASS`.

The exact assertions include:

- `(99/70)^2-2 = 1/4900`;
- `z^2-17 = 55003/441` for `z=250/21`;
- the spectral-root margin `97/5250`;
- the quantitative gap `21/250-1/12=1/1500`;
- the minimal full-fibre branching numerator `b^3-b^2-b-1=1198` at `b=11`;
- the exact global radical margin `289-288=1` establishing `9-6sqrt(2)>1/2`;
- the coarse general polynomial floor equal to `1` at `G=4`.

The output also contains a floating-point sweep over representative tuples only as a diagnostic; it is explicitly **not** used as proof evidence.

The checker validates the finite algebraic core. The group-theoretic and operator arguments are the written proof above and remain a **self-check**, not an independent audit.

## 12. What changed, what failed, and what remains open

### Source-level before / after

`OPEN/PARTIAL -> OPEN/PARTIAL`.

The universal Cayley-graph statement is untouched.

### Structural mechanism delta

The central Fourier/nonbacktracking mechanism is no longer limited to one surface quotient. It now survives a free product of arbitrarily many surface quotients while the common central fibre remains one-dimensional. The proof scales because the critical witness gains free rank

\[
k=\sum_i(2g_i-1)
\]

while the operator cost grows only as

\[
4\sum_i\sqrt{g_i}+2.
\]

The exact inequality in Section 9 shows this separation is already positive in the smallest two-factor case.

### Failed routes / precise obstructions

1. **Covering monotonicity alone:** supplies critical-side information but no infinite-fibre `p_u` lower bound strong enough to conclude the frozen statement.
2. **Subgroup inclusion alone:** gives the `F_k x Z` percolating subgraph and thus `p_c`, but there is no corresponding uniqueness-threshold monotonicity in the needed direction.
3. **Treating this as a known product theorem:** invalid. The nonzero Euler classes produce a non-split central amalgam, not a Cartesian graph product; Peres's product theorem is therefore not a substitute for the fixed standard graph proved here.

### Unresolved full gap

A proof of the parent conjecture still needs a mechanism that survives **arbitrary** nonamenable groups and **arbitrary** finite generating sets. Even within groups having infinite centre, this report does not prove every Cayley graph: it proves the explicit standard central-amalgam generating set. The previous perturbative augmentation theorem handles a controlled neighborhood of a one-factor standard set, but there is no all-generating-set transfer here.

No source closure is claimed. No independent other-track audit has been recorded for this theorem.

## 13. Structured ledger delta

```yaml
ledger_delta:
  task: PROB10-09
  source: Benjamini-Schramm nonamenability/nonuniqueness conjecture, iid bond percolation on Cayley graphs
  source_status_before: OPEN/PARTIAL
  source_status_after: OPEN/PARTIAL
  structural_metric_before: standard one-factor non-split central surface extensions plus bounded perturbative generator augmentation
  structural_metric_after: all standard iterated central amalgams E_{g1,e1} *_Z ... *_Z E_{gr,er}, r>=2, gi>=2, ei!=0
  frozen_auxiliary_family: r=2, g1=g2=2, arbitrary nonzero e1,e2
  auxiliary_metric_before: UNMEASURED
  auxiliary_metric_after: p_u-p_c > 1/1500
  methods:
    - quotient/cover strict-p_c route: INSUFFICIENT for p_u
    - subgroup-only F_k x Z route: INSUFFICIENT for p_u
    - central Fourier + diamagnetic + nonbacktracking + full-Z-fibre branching: SUCCESS on restricted family
  exact_checker: artifacts/prob10_2026-09-20/PROB10-09/central_surface_amalgam_exact.py
  exact_output: artifacts/prob10_2026-09-20/PROB10-09/central_surface_amalgam_exact.out
  checker_verdict: ALL_EXACT_CHECKS_PASS
  validation: SELF_CHECK_ONLY
  remaining_obligation: arbitrary Cayley generating sets of arbitrary finitely generated nonamenable groups
  r20_handoff: runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md
  prior_percolation_history:
    - probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md
    - probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md
  neighboring_owner_lane: proofnet24/NM13-11/progress-percolation/
```

No shared root, canonical claim, neighboring-track file, schedule, email, Drive, or public-posting state was edited by this run.
