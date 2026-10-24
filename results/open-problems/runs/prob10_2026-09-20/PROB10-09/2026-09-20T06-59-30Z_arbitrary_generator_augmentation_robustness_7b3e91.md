Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. STRUCTURAL-SCOPE METRIC MOVED: the previous central-extension theorem covered only the standard generating set; this run proves a strict bond-percolation nonuniqueness phase after adding an arbitrary symmetric set of extra generators throughout an explicit perturbative range. In particular every `E_{g,e}`, `g>=3`, `e!=0`, remains certified after any `m<=2g-4` arbitrary added generators (with the usual symmetry/distinctness conditions). The concrete new `g=3,m=2` family moves UNMEASURED -> certified `p_u-p_c > 0.007313379602737586...`. Parent Benjamini–Schramm remains OPEN/PARTIAL.**

# PROB10-09 — robustness of the central-surface certificate under arbitrary generator augmentation

## 0. Frozen source, continuity, ownership, and delivery boundaries

The owner-frozen target remains exactly

\[
 p_c(G)<p_u(G)
\]

for iid **BOND** percolation on every locally finite Cayley graph `G=Cay(Gamma,S)` of every finitely generated nonamenable group. This report does not replace that target by a planar site-percolation statement. The universal source problem remains **OPEN/PARTIAL**.

The required predecessor handoff was already made and was re-read rather than duplicated:

- `runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`.

It preserves R20's pre-refocus Paley/KNSV/BMO state, artifacts, and ownership. This run changes none of those files.

Controlling repository evidence re-read before research:

- `operations/PROB10_2026-09-20.md`;
- current `POSTED.md`;
- current canonical `D0061` / Benjamini--Schramm claim history and aliases;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`, blob `d94127841f3b335a32b7936b86d8dee7a6b8d093`;
- immediate PROB10-09 predecessor `runs/prob10_2026-09-20/PROB10-09/2026-09-20T05-59-30Z_central_surface_extension_family_gap_4a8f21.md`;
- newest neighboring lane read this run, `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T08-50-00+0300__t09-rattaggi-horizontal-free-k8-gap.md`.

The neighboring NM13-11 lane is currently using Rattaggi/free-core/complement geometry. The present theorem stays inside R20's explicitly complementary **central-surface Fourier/nonbacktracking lane** and does not overwrite that claim.

The June archive's mass-transport/pivotal, relative-denseness, boundary-energy, second-moment/fixed-endpoint, embedded-tree escape, quotient/iid-lift, fibre-shell, and earlier nonbacktracking bridge attempts are consumed evidence; none is relabelled as new.

## 1. Current-source / prior-art check — 20 September 2026

The bounded source check used the owner-specified sources plus current references.

- Hutchcroft, `arXiv:1804.10191`, proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs. The central extensions below contain `Z^2`, hence are not in that hyperbolic class.
- Hutchcroft--Pan, `arXiv:2409.12283`, develops subgroup relativization and, among other results, proves nonuniqueness at `p_u` for groups with an amenable `wq`-normal subgroup of exponential growth. The central subgroup below is `Z`, of linear growth; this does not supply the fixed-generator theorem proved here.
- Terlov--Timar, `arXiv:2502.02560`, concerns weighted amenability/nonunimodular thresholds. It does not state the present fixed Cayley-graph result.
- Choi--Seo, `arXiv:2508.08932`, proves the nonuniqueness phase for **every Cayley graph of every acylindrically hyperbolic group**. The groups below have infinite centre and are not acylindrically hyperbolic.
- Juschenko--Nagnibeda, `arXiv:1206.2183`, proves existence of a favorable generating set when a group contains an infinite normal subgroup with nonamenable quotient. That existential result is important prior art, but it does not give the explicit statement below for **every arbitrary small augmentation of one frozen natural generating set**.
- The 10 September 2026 paper `arXiv:2609.11845` still discusses the Benjamini--Schramm nonamenability/nonuniqueness question as a conjectural general principle in its surrounding weighted-threshold framework; no source-level all-Cayley resolution was located in this bounded check.
- The 7 September 2026 paper `arXiv:2609.07768` mentions a recently solved *different* Benjamini--Schramm percolation conjecture about homogeneous weighted/isoperimetric percolation and gives `p_c` consequences; its abstract has no `p_u` statement. It is not a resolution of the owner-frozen uniqueness-gap target.

Dated web queries included the three owner-specified arXiv identifiers, `"surface group" "central extension" percolation Cayley graph p_c p_u`, `"central extension" "p_c" "p_u"`, `"infinite center" Cayley percolation p_c p_u`, and current-2026 searches for an all-Cayley `p_c<p_u` theorem. No source specifically stating the theorem below was found. This is **negative bounded-search evidence only**, not a worldwide novelty or priority certificate.

The spectral input reused from the preceding report is Żuk's rigorous surface-group random-walk estimate in the standard `4g`-generator normalization,

\[
\|M_g\|\le g^{-1/2},
\]

hence for the standard surface adjacency operator

\[
\|A_{\Gamma_g}\|\le 4\sqrt g.
\tag{1.1}
\]

## 2. Metric before/after — source and auxiliary deltas kept separate

### Parent source metric

Before: `OPEN/PARTIAL`.

After: `OPEN/PARTIAL`.

No universal all-Cayley implication is claimed.

### Structural-scope metric

Before this run, the proved central-extension family was

\[
E_{g,e}=\langle a_1,b_1,\ldots,a_g,b_g,z\mid z\text{ central},\ \prod_{i=1}^g[a_i,b_i]=z^e\rangle,
\qquad g\ge2,\ e\ne0,
\]

with only the frozen standard symmetric generating set

\[
S_0=\{a_i^{\pm1},b_i^{\pm1}:1\le i\le g\}\cup\{z^{\pm1}\}.
\]

After this run, for every `g>=3`, `e!=0`, the proof covers **every** symmetric finite augmentation

\[
S=S_0\sqcup T,\qquad T=T^{-1},\qquad |T|=m,
\tag{2.1}
\]

with no loops, repetitions, or collisions with `S_0`, whenever the explicit operator-margin criterion in Theorem 7.1 holds. In particular it covers the simple uniform range

\[
\boxed{m\le 2g-4.}
\tag{2.2}
\]

Since these are arbitrary added group elements, this is not merely a central-slant reparametrization of the old Cayley graph.

### Auxiliary new frozen family

Freeze `g=3`, any `e!=0`, and any arbitrary additional inverse pair `T={c,c^{-1}}` disjoint from `S_0`. Before: `UNMEASURED`. After:

\[
\boxed{
 p_u-p_c>
 \frac{1}{2+2\sqrt3+\sqrt{1+8\sqrt3}}-\frac1{10}
 =0.00731337960273758675438427444\ldots .
}
\tag{2.3}
\]

The preceding `X_{3,4}` and `C_{2,1}` numerical certificates are retained unchanged; (2.3) is a separate auxiliary metric on genuinely augmented Cayley graphs.

## 3. Idea-before-code and three genuinely different methods

The research idea was committed **before** writing the checker:

- `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T06-52-00Z_arbitrary_pair_augmentation_idea.md`, commit `51c2e88d54f3fb3a09e26d3d0ba48f2f0d3c23e0`.

### Method A — central slants / presentation deformation: rejected as fake progress

First I tested the tempting route of replacing horizontal generators by `a_i z^{r_i}` or `b_i z^{s_i}`. For many such choices the change is induced by a group automorphism preserving the central relation, so the resulting Cayley graph is isomorphic to the old one. That would enlarge notation without enlarging the graph class. I did not count it as progress.

### Method B — arbitrary generator augmentation + operator robustness: SUCCESS

Keep the old embedded `F_{2g-1} x Z` percolation witness, which survives any added edges, but charge every new generator exactly once in the adjacency norm. This gives a quantitative robustness radius for the `p_c<p_{2->2}` mechanism and proves Theorem 7.1 below.

### Method C — two-dimensional central fibre: not promoted

I also tested replacing the one-dimensional central fibre by a `Z^2` fibre and trying to gain a stronger critical-side witness. Small-radius reliability calculations suggest this may eventually help, but the first useful crossing appears only after a larger finite cluster computation. Numerical/Monte-Carlo evidence would not be an exact certificate and therefore is not promoted. This remains a genuinely different future route, not a theorem in this report.

The negation test for Method B is also informative: adding arbitrarily many generators cannot be certified by the same crude triangle-norm argument because each added generator increases the operator bound while the embedded-subgraph `p_c` witness is fixed. Thus the proof itself predicts a finite perturbative scope rather than silently extrapolating to the universal conjecture.

## 4. The family and its persistent free-by-central subgraph

Fix `g>=3` and `e!=0`. Let

\[
G=\operatorname{Cay}(E_{g,e},S_0\sqcup T)
\]

with `T` as in (2.1).

The predecessor report proved, by Magnus Freiheitssatz in the surface quotient, that

\[
H_g=\langle a_1,b_1,\ldots,a_{g-1},b_{g-1},a_g,z\rangle
\cong F_{2g-1}\times\mathbb Z.
\tag{4.1}
\]

Using only generator edges already present in `S_0`, every augmented graph therefore contains

\[
T_{4g-2}\square\mathbb Z.
\tag{4.2}
\]

Adding `T` cannot destroy this subgraph. This observation will make the `p_c` side completely uniform in the arbitrary augmentation.

## 5. A strict exact critical-side bound using the full Z-fibre

Set

\[
b=4g-3.
\]

Orient the `T_{4g-2}` factor of (4.2) away from a root, retaining `b` forward children at each non-root tree vertex.

At an activated tree vertex, expose the entire open cluster of the seed in its vertical `Z` fibre. Let `N` be its size. In one-dimensional bond percolation,

\[
N=1+L_-+L_+,
\]

where `L_-,L_+` are independent and

\[
\mathbb P(L=r)=(1-p)p^r,\qquad r\ge0.
\]

For any fixed forward child direction, there are `N` horizontal bonds from the exposed parent fibre cluster to that child fibre. Conditional on `N`, the probability that at least one is open is

\[
\phi(p)=1-(1-p)^N
\]

at the random-cluster level. Averaging gives

\[
\phi(p)=1-\mathbb E[(1-p)^N].
\]

Writing `s=1-p`,

\[
\mathbb E[s^L]=\frac{1-p}{1-ps}=\frac{s}{1-ps},
\]

so

\[
\mathbb E[s^N]
=s\left(\frac{s}{1-ps}\right)^2
=\frac{s^3}{(1-ps)^2},
\]

and hence

\[
\boxed{
\phi(p)=1-\frac{(1-p)^3}{\bigl(1-p(1-p)\bigr)^2}.
}
\tag{5.1}
\]

Different forward child fibres use disjoint fresh horizontal edges and disjoint vertical fibres. Choosing, on each successful child direction, the first successful horizontal endpoint before revealing that child's vertical bonds therefore embeds an ordinary Galton--Watson process with mean offspring

\[
\mu(p)=b\phi(p).
\tag{5.2}
\]

Now put

\[
p_0=\frac1{b+1}=\frac1{4g-2}.
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

whose exact difference is

\[
\boxed{b^3-b^2-b-1>0.}
\tag{5.3}
\]

For `g>=3`, `b>=9`, so (5.3) is immediate. Since `\mu(p)` is continuous, `\mu(p)>1` already for some `p<p_0`. Therefore

\[
\boxed{
 p_c(G)<\frac1{4g-2}.
}
\tag{5.4}
\]

This is strict, not merely `<=`: supercriticality at `p_0` has positive slack and persists on a left-neighborhood of `p_0`.

## 6. Operator side under arbitrary added generators

Let `A_0` be the adjacency operator for the standard central-extension graph `Cay(E_{g,e},S_0)`.

Fourier transform in the central `Z` coordinate decomposes the horizontal part into magnetic surface-group adjacency operators. Each magnetic coefficient has unit modulus, so pointwise

\[
|A_{\theta}^{\rm hor}f|\le A_{\Gamma_g}|f|.
\]

Consequently (1.1) gives

\[
\|A_{\theta}^{\rm hor}\|\le4\sqrt g.
\]

The two central edges contribute the scalar `2 cos(theta)`, so uniformly in the Fourier parameter

\[
\boxed{
\|A_0\|\le4\sqrt g+2.
}
\tag{6.1}
\]

Now add an arbitrary symmetric set `T` of `m` new generators. Every right-translation operator has norm one, hence by the triangle inequality

\[
\left\|\sum_{t\in T}R_t\right\|\le m.
\]

Therefore the adjacency operator `A` of the augmented graph satisfies

\[
\boxed{
\|A\|\le R:=4\sqrt g+2+m.
}
\tag{6.2}
\]

The graph is

\[
D=4g+2+m
\]

regular, and write

\[
Q=D-1=4g+1+m.
\tag{6.3}
\]

### Lemma 6.1 — nonbacktracking transfer

Let `X` be an infinite `D`-regular graph with self-adjoint adjacency operator `A_X` satisfying `||A_X||<=R`, and put `Q=D-1`. Define

\[
\beta_D(R)=
\begin{cases}
\sqrt Q,&R\le2\sqrt Q,\\[2mm]
\dfrac{R+\sqrt{R^2-4Q}}2,&R>2\sqrt Q.
\end{cases}
\tag{6.4}
\]

Then

\[
 p_{2\to2}(X)\ge \frac1{\beta_D(R)}.
\tag{6.5}
\]

**Proof.** Let `B_n(x,y)` count nonbacktracking walks of length `n`. Apart from the standard `n=2` initial correction, the vertex nonbacktracking matrices satisfy

\[
B_n=A_XB_{n-1}-QB_{n-2}.
\]

By functional calculus for the self-adjoint `A_X`, the exponential growth rate of `||B_n||_{2->2}` is at most the largest modulus of a root of

\[
r^2-\lambda r+Q=0,\qquad |\lambda|\le R,
\]

which is exactly `\beta_D(R)`. Thus for every `p<1/\beta_D(R)`,

\[
\sum_{n\ge0}p^n\|B_n\|_{2\to2}<\infty.
\]

Every open connection contains a self-avoiding path, and every self-avoiding path is nonbacktracking. A union bound gives the entrywise domination

\[
\tau_p(x,y)=\mathbb P_p(x\leftrightarrow y)
\le\sum_{n\ge0}p^n B_n(x,y).
\]

The right-hand side is a bounded positive-kernel operator on `l^2`, proving (6.5). ∎

Finally,

\[
p_{2\to2}\le p_u.
\tag{6.6}
\]

For completeness, if `p>p_u`, there is a unique infinite cluster and its vertex-density `theta(p)` is positive. By FKG,

\[
\tau_p(x,y)\ge\mathbb P(x\leftrightarrow\infty,\ y\leftrightarrow\infty)
\ge\theta(p)^2,
\]

because two vertices in the unique infinite cluster are connected. A kernel bounded below by a positive constant is not bounded on `l^2` of an infinite graph. Hence every `p>p_u` lies above `p_{2->2}`, proving (6.6).

For our augmented graph, (6.2)--(6.4) therefore give

\[
\boxed{
 p_u(G)\ge p_{2\to2}(G)\ge\frac1{\beta_D(R)}.
}
\tag{6.7}
\]

## 7. Main new theorem: explicit robustness radius

Put

\[
z=4g-2,
\qquad
Q=4g+1+m,
\qquad
R=4\sqrt g+2+m.
\]

Since `R>2sqrt(Q)` in the present parameter range, `\beta_D(R)` is the larger positive root of

\[
r+\frac Qr=R.
\]

On `(sqrt(Q),infinity)` the map `r -> r+Q/r` is strictly increasing. Thus, whenever `z^2>Q`,

\[
\beta_D(R)<z
\quad\Longleftrightarrow\quad
R<z+\frac Qz.
\tag{7.1}
\]

Substituting `R,Q,z`, the latter is exactly

\[
\boxed{
 m(4g-3)
 <16g^2-16g^{3/2}-20g+8\sqrt g+9.
}
\tag{7.2}
\]

**Theorem 7.1 (arbitrary-generator robustness).**
Let `g>=3`, `e!=0`, and let `T=T^{-1}` be any finite symmetric set of `m` elements disjoint from `S_0`, with no loops or repeated generators. If

\[
4g+1+m<(4g-2)^2
\tag{7.3}
\]

and (7.2) holds, then iid bond percolation on

\[
G=\operatorname{Cay}(E_{g,e},S_0\sqcup T)
\]

has a strict nonuniqueness phase. More quantitatively,

\[
\boxed{
 p_u(G)-p_c(G)
 >\frac1{\beta_D(4\sqrt g+2+m)}-\frac1{4g-2}>0.
}
\tag{7.4}
\]

**Proof.** Equation (5.4) gives `p_c<1/z`. Conditions (7.2)--(7.3), via (7.1), give `\beta_D(R)<z`; hence (6.7) gives `p_u>=1/\beta_D(R)>1/z`. Combining yields (7.4). ∎

### Clean parameter-free corollary

A convenient uniform subset of the exact criterion is

\[
\boxed{m\le2g-4.}
\tag{7.5}
\]

Indeed the left side of (7.1) worsens monotonically as `m` increases, so take `m=2g-4`. Then

\[
z+\frac Qz-R
=2g-4\sqrt g+\frac{6g-3}{4g-2}.
\tag{7.6}
\]

For `g>=4`, `2g>=4sqrt(g)` and the final rational term is strictly positive. For `g=3`, (7.6) is

\[
\frac{15}{2}-4\sqrt3>0,
\]

since `225>192`. Condition (7.3) is then immediate. Therefore every arbitrary symmetric augmentation by at most `2g-4` generators is certified.

The exact inequality (7.2) often allows more. For example its maximal even `m` values begin `2,4,8,10,14,18,...` for `g=3,4,5,6,7,8,...`; these values are diagnostic consequences of the exact criterion, not a replacement for the symbolic proof.

## 8. Concrete new `g=3`, one-pair certificate

Take `g=3` and any extra inverse pair `T={c,c^{-1}}`, so `m=2`. Then

\[
D=16,\qquad Q=15,\qquad R=4\sqrt3+4.
\]

The nonbacktracking root is

\[
\beta
=\frac{4\sqrt3+4+\sqrt{(4\sqrt3+4)^2-60}}2
=2+2\sqrt3+\sqrt{1+8\sqrt3}.
\]

The exact comparison `\beta<10` follows from

\[
4\sqrt3+4<10+\frac{15}{10}=\frac{23}{2},
\]

which reduces to `4sqrt(3)<15/2`; squaring positive sides gives

\[
192<225.
\]

On the critical side, `b=9` and the exact slack in (5.3) is

\[
9^3-9^2-9-1=638>0.
\]

Hence

\[
p_c<\frac1{10}
<\frac1{2+2\sqrt3+\sqrt{1+8\sqrt3}}
\le p_{2\to2}\le p_u,
\]

and therefore the gap (2.3) follows.

## 9. Executed validation

The finite arithmetic checker was written only after the idea artifact:

- code: `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T06-53-00Z_arbitrary_pair_augmentation_check.py`, commit `2e550b3b389d94ec178dccd7bfd038eceb1aac1a`;
- output: `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T06-53-00Z_arbitrary_pair_augmentation_check.out`.

Executed output ends

`ALL_EXACT_CHECKS_PASS`.

It verifies the concrete exact `g=3,m=2` squared inequality, the positive critical-side polynomial slack, the clean `m<=2g-4` algebraic reduction, and high-precision diagnostics for the auxiliary gap. The infinite-family proof is written on the page above and is not delegated to numerical enumeration.

This is a **self-check only**, not an independent audit. Therefore even this restricted theorem is not labeled source-closed under the fleet closure standard.

## 10. What moved, what did not, and the unresolved universal gap

### Source metric delta

`Benjamini--Schramm all nonamenable Cayley graphs, bond percolation`:

`OPEN/PARTIAL -> OPEN/PARTIAL`.

### Structural metric delta

`standard central extensions, standard S_0 only`

`->`

`standard non-split central extensions with every arbitrary symmetric augmentation satisfying (7.2)--(7.3), in particular every |T|<=2g-4 for g>=3`.

### Auxiliary metric delta

`g=3, arbitrary one-extra-pair family`: `UNMEASURED -> p_u-p_c > 0.00731337960273758675438427444...`.

### Remaining full obligation

The proof still depends on two special pieces of structure absent from a general Cayley graph:

1. a large explicit free-by-central subgraph giving the fibre branching witness for `p_c`; and
2. a quotient/magnetic decomposition giving a controlled adjacency norm under perturbation.

The universal conjecture requires a mechanism replacing both ingredients for arbitrary finite generating sets of arbitrary finitely generated nonamenable groups. Merely renaming this missing mechanism `p_c<p_{2->2}` would not be progress; no such claim is made.

A mathematically concrete next question inside this same conjecture is whether the exact full-fibre threshold `q_g`, defined by `(4g-3) phi(q_g)=1` with `phi` from (5.1), can replace the convenient `1/(4g-2)` cutoff and enlarge the arbitrary-augmentation radius beyond (7.2), or whether a two-dimensional central-fibre exact computation gives a qualitatively stronger robust family.

## 11. Delivery / ownership receipt content

This report writes only to the authorized PROB10-09 run/artifact paths. It does not edit shared roots, NM13-11, R20's former targets, schedules, email, Drive, or public repositories. The R20 handoff and the June percolation history are linked above. No force push was used.
