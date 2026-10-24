Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** No authenticated runtime metadata establishes GPT-6 or a maximum-effort setting.

# P26 / LIVE20 T08 — radial-clock Green transfer and exact-distance-four halves of non-Ramanujan Cayley bigraphs

**Parent status:** `PARTIAL / OPEN` for Salez Problem 2.3 before this run; `PARTIAL / OPEN` after this run.

**Restricted theorem status:** `CANDIDATE_FULL` for Theorems A–B below, pending later independent review.

**Publication novelty:** `UNVERIFIED`. Bounded searches on 20 September 2026 for combinations of `distance-4 bigraph cutoff random walk Cayley`, `halved graph cutoff random walk biregular`, and `distance four Cayley bigraph cutoff` found standard halved/distance-graph terminology but no matching continuous-time cutoff theorem for the arithmetic exact-distance-four class below. This is negative evidence only, not a worldwide priority certificate.

Repository/branch: `yspennstate/math-open-problems` / `master`.
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.
Run root: `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/`.

## 0. Compact handoff and C28 split

The controlling LIVE20 instruction has replaced P26's old audit-first role by T08 research. The newest own report before this run was

`2026-09-20_10-10-50__biregular-halved-green-transfer.md`.

That report established a Green-shell criterion and applied it to the ordinary left half of a left-transitive `(K+1,k+1)` bigraph. Its concrete arithmetic application was the 18-regular left half of the non-Ramanujan Eisenstein `(9,3)` Cayley bigraphs of Evra--Feigon--Maurischat--Parzanchevski (EFMP). The key reusable input is their Sarnak--Xue NBRW estimate, which gives exponentially small shell chi-square after the entropic radius even though the source bigraph is not fully Ramanujan.

The newest relevant historical-C28 successor report read this run is

`proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md`.

NM13-01 now owns a complementary route: reversal-augmented oriented-edge graphs plus a direct attack on arbitrary transitivity through the root-stabilizer quotient. Its exact identity says the point-start likelihood ratio is the quotient density `f_t=nu_t/barpi`, eliminating the earlier artificial stabilizer-rank/orbit-size varentropy penalty. Its remaining target is a direct `L^1` Green/log-likelihood or Dirichlet control of `log f_t` from degree and spectral gap. P26 therefore does **not** duplicate arc/Hodge or stabilizer-quotient work here. This run stays on shell-Green transfer and asks how far one can change the radial clock while keeping the same information front.

## 1. Exact source statement and current primary boundary

Justin Salez, `arXiv:2508.21055`, Section 1.1 uses independent mean-one exponential waiting times. If `T` is the discrete transition matrix, then

\[
P_t=e^{-t}\sum_{j\ge0}\frac{t^jT^j}{j!}=e^{t(T-I)}.
\tag{1.1}
\]

This is the convention used throughout this report. No lazification or hidden time rescaling is introduced.

Salez defines expanders as graph sequences with diverging size, uniformly bounded degree and spectral gaps bounded away from zero, and Problem 2.3 is literally:

> Prove that all vertex-transitive expanders exhibit cutoff.

The current primary boundary was refreshed on 20 September 2026.

* Dylan J. Altschuler, `arXiv:2609.14945`, submitted 14 September 2026, proves cutoff with an explicit Gaussian profile for every fixed-degree fixed-constant **long-range expander** sequence. The same paper proves the strict hierarchy
  \[
  \text{Ramanujan}\Longrightarrow\text{long-range expansion}\Longrightarrow\text{spectral expansion},
  \]
  with neither converse. Thus long-range expansion is genuinely stronger than Salez's source hypothesis.
* Francesco Pedrotti and Justin Salez, `arXiv:2607.05345`, submitted 6 July 2026, prove a universal window bound in terms of their non-equilibrium Poincare constant `gamma_*`. The checked theorem does not derive the needed `gamma_*` estimate from vertex transitivity plus the ordinary spectral gap alone.
* Shai Evra, Brooke Feigon, Kathrin Maurischat and Ori Parzanchevski, `arXiv:2312.06507`, current revision checked 20 September 2026, construct arithmetic `(p^3+1,p+1)` Cayley bigraphs. Their Eisenstein family is adj-Ramanujan but genuinely non-Ramanujan, satisfies a Sarnak--Xue density hypothesis, has logarithmic girth, and has bounded-window NBRW cutoff. Theorem 8.2 records these properties explicitly.

The `POSTED.md` exclusion of Salez Problem 2.4 / the Abelian-Cayley product-condition manuscript remains untouched. This run concerns Problem 2.3 only.

## 2. Parent before/after and what counts as movement

### Parent problem before

Salez Problem 2.3 was `OPEN / PARTIAL`. P26 had proved source-valid cutoff for several explicit spectral-but-not-long-range classes, most recently the ordinary left halves of suitable Sarnak--Xue biregular bigraphs.

### Parent problem after

Salez Problem 2.3 remains `OPEN / PARTIAL`; this report does **not** claim the general conjecture.

The proved subclass is nevertheless strictly enlarged: the ordinary rate-one continuous-time SRW on the **exact bigraph-distance-four graph on the left side** of a suitable left-transitive Sarnak--Xue bigraph has a Gaussian cutoff profile. For the concrete non-Ramanujan Eisenstein `(9,3)` Cayley bigraph family this produces a new sequence of **288-regular vertex-transitive Cayley spectral expanders** with cutoff, while the output sequence provably fails every fixed long-range-expansion constant.

This is not the previous 18-regular half-square again: all distance-two edges are removed, and one output transition is a uniformly chosen nonbacktracking four-edge geodesic in the biregular ancestor.

### Mechanism-level movement

The substantive mechanism gain is **radial-clock invariance of the Green front** in a form strong enough to change the local walk, not merely decorate the same output graph. The EFMP shell information is a property of the projected nonbacktracking endpoint laws `nu_r`; once those shell laws have passed the Green threshold, any transitive isotropic walk whose lift is a different ballistic radial clock over the same shells inherits the same TV front, with center/profile determined only by its new radial drift and variance.

The exact-distance-four operation below is the first P26 application of this principle in which the radial process has five interior increments `{-2,-1,0,1,2}` rather than the preceding skip-free `{-1,0,1}` clock.

## 3. Quantitative Green-shell / radial-clock transfer

Let `V_n` be transitive with uniform law `pi_n`. Suppose a rate-one continuous-time chain `S_t` started from `x` admits an exact shell representation

\[
\delta_x S_t=\sum_{r\ge0}\Pr(R_t=r)\nu_{n,r}^x.
\tag{3.1}
\]

Assume there is an entropic radius `ell_n` and functions `G_n(h),B_n(h)` such that for every relevant `h>=0`,

\[
\sup_x\sup_{r\ge \ell_n+h}
\chi^2(\nu_{n,r}^x\Vert\pi_n)\le G_n(h),
\tag{3.2}
\]

and there are sets `A_{n,x}(a)` containing the supports of all shells `nu_{n,r}^x`, `r<=a`, with

\[
\sup_x\pi_n(A_{n,x}(\ell_n-h))\le B_n(h).
\tag{3.3}
\]

Then for every `t,h`,

\[
\boxed{
 d_n(t)
 \le
 \Pr(R_t<\ell_n+h)+\frac12\sqrt{G_n(h)}
}
\tag{3.4}
\]

and

\[
\boxed{
 d_n(t)
 \ge
 \Pr(R_t\le\ell_n-h)-B_n(h).
}
\tag{3.5}
\]

Here `d_n(t)` is the worst-start TV distance, which equals the point-start value by transitivity.

**Proof.** Split the mixture (3.1) at `ell_n+h`. Convexity of TV bounds every early shell by one, while for every late shell

\[
\|\nu_{n,r}^x-\pi_n\|_{TV}
\le\frac12\sqrt{\chi^2(\nu_{n,r}^x\Vert\pi_n)}
\le\frac12\sqrt{G_n(h)}.
\]

This proves (3.4). For (3.5), test TV against the set `A_{n,x}(ell_n-h)`. Under the walk it has mass at least `Pr(R_t<=ell_n-h)`, while stationarity gives at most `B_n(h)`. `QED`

This immediately yields a quantitative window criterion. If

\[
G_n(h)\le C_1e^{-c_1h},
\qquad
B_n(h)\le C_2e^{-c_2h},
\tag{3.6}
\]

then fixed TV accuracy costs only `h=O(log(1/epsilon))` radial layers. Therefore any radial front of width `w_n->infinity` transfers with no asymptotic widening. More generally, it is enough to have a cleanup shift `h_n=o(w_n)` for which both errors tend to zero.

This is the exact quantitative form needed below.

## 4. Exact distance four on the left side of a biregular bigraph

Fix integers `K>=k>=2`. Let

\[
X=(L\sqcup R,E)
\]

be connected, `(K+1,k+1)`-biregular, left-transitive, and of girth greater than eight. Define `Y^{[4]}(X)` on `L` by

\[
x\sim_{Y^{[4]}}y
\quad\Longleftrightarrow\quad
\operatorname{dist}_X(x,y)=4.
\tag{4.1}
\]

Every left automorphism of `X` preserves this relation, so left transitivity of `X` implies vertex transitivity of `Y^{[4]}`. For a Cayley bigraph, the left regular group acts simply transitively, hence `Y^{[4]}` is a Cayley graph.

A length-four geodesic from a left vertex has

\[
(K+1)\,k\,K\,k
\]

choices. Girth `>8` prevents two such geodesics from having the same endpoint. Therefore

\[
\boxed{D_2=K(K+1)k^2}
\tag{4.2}
\]

is the output degree.

### 4.1 Exact spectral polynomial

Let `M` be the `|L| x |R|` incidence matrix and put

\[
B=MM^T.
\]

Let `A_1` be adjacency of the ordinary left half (bigraph distance two), and `A_2` adjacency of `Y^{[4]}`. Girth `>4` gives

\[
B=(K+1)I+A_1.
\tag{4.3}
\]

Now count two-step walks in `A_1`. On the diagonal there are `(K+1)k` choices. If two left vertices are at bigraph distance two, their only common `A_1` neighbors are the `k-1` other left vertices in their common right fiber; an additional common neighbor would produce a six-cycle. If they are at bigraph distance four, there is exactly one intermediate left vertex; two would produce an eight-cycle. Hence

\[
A_1^2=(K+1)kI+(k-1)A_1+A_2.
\tag{4.4}
\]

Substituting (4.3) gives the exact distance-four polynomial

\[
\boxed{
A_2=B^2-(2K+k+1)B+K(K+1)I.
}
\tag{4.5}
\]

Thus the normalized output kernel is

\[
\boxed{
Q_2=q_2(B),
\qquad
q_2(x)=
\frac{x^2-(2K+k+1)x+K(K+1)}{K(K+1)k^2}.
}
\tag{4.6}
\]

The Perron eigenvalue of `B` is

\[
b_0=(K+1)(k+1),
\]

and `q_2(b_0)=1`, as it must.

More usefully,

\[
\boxed{
1-q_2(x)
=
\frac{(b_0-x)(x+K(k-1))}{K(K+1)k^2}.
}
\tag{4.7}
\]

The other root of `q_2(x)=1` is `-K(k-1)<0`.

For an adj-Ramanujan bigraph, every nontrivial eigenvalue `x` of `B=MM^T` is either zero or lies in

\[
I_{K,k}:=
[(\sqrt K-\sqrt k)^2,(\sqrt K+\sqrt k)^2].
\tag{4.8}
\]

The upper endpoint is strictly below `b_0`, since

\[
b_0-(\sqrt K+\sqrt k)^2=(\sqrt{Kk}-1)^2>0.
\tag{4.9}
\]

Therefore (4.7) gives a fixed positive output spectral gap. An explicit general lower bound is

\[
\boxed{
\operatorname{gap}(Y^{[4]})
\ge
\min\left\{
1-\frac1{k^2},
\frac{(k-1)(\sqrt{Kk}-1)^2}{(K+1)k^2}
\right\}>0.
}
\tag{4.10}
\]

The point is structural: this second spherical half remains a spectral expander even though it contains **none** of the original distance-two half edges.

## 5. Same Green shells, different radial clock

Let `T_{K+1,k+1}` be the universal biregular tree rooted at a left vertex `o`. Form its exact-distance-four left graph by (4.1), and lift rate-one continuous-time SRW on `Y^{[4]}` to this cover. Let

\[
R_t=\frac12\operatorname{dist}_{T}(o,Z_t)
\]

be the left half-radius.

The stabilizer of `o` in the biregular-tree automorphism group acts transitively on every left sphere. The lifted kernel is isotropic, so conditional on `R_t=r`, the lifted endpoint is uniform on the left sphere of bigraph radius `2r`. Projecting to `X` gives exactly the endpoint distribution `nu_r^x` of a uniformly chosen nonbacktracking path of length `2r` from the starting left vertex.

Hence, in Salez's exact continuous-time convention,

\[
\boxed{
\delta_x e^{t(Q_2-I)}
=
\sum_{r\ge0}\Pr(R_t=r)\nu_r^x.
}
\tag{5.1}
\]

This is the key radial-clock transfer: the shell laws are **identical** to those used in the previous half-square theorem, while the radial dynamics are new.

### 5.1 Interior radial law

For `r>=2`, classify a four-edge geodesic from the current left vertex by how long it initially follows the unique route toward the root. The exact multiplicities are

\[
\begin{array}{c|ccccc}
\Delta R&-2&-1&0&1&2\\ \hline
\#&1&k-1&(K-1)k&(k-1)Kk&K^2k^2.
\end{array}
\tag{5.2}
\]

The total is `D_2`. Therefore the interior drift and compound-Poisson raw second-moment rate are

\[
\boxed{
 v_2
 =\frac{(Kk-1)(2Kk+k+1)}{K(K+1)k^2}>0,
}
\tag{5.3}
\]

and

\[
\boxed{
 M_{2,2}
 =
 \frac{4K^2k^2+Kk(k-1)+(k-1)+4}{K(K+1)k^2}.
}
\tag{5.4}
\]

The boundary consists only of radii `0,1`. Because the interior increment has positive mean, for some small `theta>0`, `E[e^{-theta Delta R}]<1`. The usual exponential-supermartingale argument gives an exponentially decaying probability of returning to the boundary from high radius. In particular the number of boundary visits has a geometric tail. Couple all interior jumps to an iid increment sequence and alter only jumps made while the chain is in the finite boundary region. Only a tight, in fact geometrically-tailed, number of bounded increments are altered. Thus the boundary changes `R_t` by `O_P(1)` relative to the compound-Poisson iid sum.

Since the event clock has rate one,

\[
\boxed{
\frac{R_t-v_2t}{\sqrt{M_{2,2}t}}
\Longrightarrow N(0,1).
}
\tag{5.5}
\]

No discrete-time conversion is being made here: the `M_{2,2}` rather than the centered one-step variance is exactly the variance rate for a rate-one compound-Poisson sum.

## 6. EFMP Sarnak--Xue density supplies the Green front unchanged

Let `N=|E(X)|`. For an initial directed `L->R` edge `e`, write `p_e^{2r}` for the EFMP NBRW law after `2r` directed-edge transitions and `u` for uniform measure on the `L->R` orientation class.

Theorem 4.17 and its proof in EFMP give, for the left-transitive adj-Ramanujan Sarnak--Xue families under their logarithmic-girth hypothesis,

\[
\chi^2(p_e^{2r}\Vert u)
\le
(K+1)\left[
\mathcal E_X k^{-2r}+m^2N(Kk)^{-r}
\right],
\tag{6.1}
\]

with the sharp Sarnak--Xue exponent

\[
\delta=\frac{2}{1+\log_kK}=2\log_{Kk}k.
\tag{6.2}
\]

At

\[
L_N=\lceil\log_{Kk}N\rceil,
\]

one has `k^{2L_N}` of order `N^delta`. Hence for `r=L_N+h`, after the harmless bounded arithmetic-progression adjustment used in the source proof,

\[
\boxed{
\chi^2(p_e^{2r}\Vert u)
\le
C_{K,k,m}
\left(k^{-2h}+(Kk)^{-h}\right).
}
\tag{6.3}
\]

Choose the first edge from a left start uniformly and project the final directed edge to its left tail. This produces exactly `nu_r^x`. Mixture convexity and chi-square data processing give

\[
\boxed{
\sup_x\chi^2(\nu_r^x\Vert u_L)
\le
C_{K,k,m}
\left(k^{-2h}+(Kk)^{-h}\right),
\qquad r\ge L_N+h.
}
\tag{6.4}
\]

Because `N=(K+1)|L|`, the left-vertex entropic radius is

\[
\ell_n=\log_{Kk}|L|+O(1).
\tag{6.5}
\]

Thus the Green front is unchanged by replacing the half-square radial clock with the exact-distance-four clock.

For the lower bound, the union of left shells through radius `a` has size at most

\[
1+(K+1)k\sum_{j=0}^{a-1}(Kk)^j
\le C_{K,k}(Kk)^a.
\tag{6.6}
\]

Therefore, with `n=|L|`,

\[
\pi_L(A_x(\ell_n-h))\le C_{K,k}(Kk)^{-h}.
\tag{6.7}
\]

Substituting (6.4) and (6.7) into (3.4)–(3.5) gives the completely explicit finite-accuracy sandwich

\[
\boxed{
\Pr(R_t\le\ell_n-h)-C_0(Kk)^{-h}
\le d_n(t)
\le
\Pr(R_t<\ell_n+h)
+rac12\sqrt{C_1\left(k^{-2h}+(Kk)^{-h}\right)}.
}
\tag{6.8}
\]

Thus fixed accuracy requires only `h=O(log(1/epsilon))` shell layers.

## 7. The general exact-distance-four cutoff theorem

Combining Sections 3–6 gives the promised transfer theorem.

> **Theorem A — second spherical half Green transfer.**
> Fix `K>=k>=2`. Let `(X_n)` be a connected left-transitive `(K+1,k+1)`-biregular family satisfying the EFMP adj-Ramanujan, Sarnak--Xue density and logarithmic-girth hypotheses, with `|L_n|->infinity`. For all sufficiently large `n`, let `Y_n^{[4]}` be the graph on `L_n` joining pairs at exact `X_n`-distance four. Then `(Y_n^{[4]})` is a fixed-degree vertex-transitive spectral-expander sequence. Its rate-one continuous-time SRW has the Gaussian TV profile
> \[
> \boxed{
> d_n\left(
> \frac{\ell_n}{v_2}+z\sqrt{\ell_n}
> \right)
> \longrightarrow
> \Phi\left(-\frac{z}{\tau_2}\right),
> }
> \tag{7.1}
> \]
> where
> \[
> \ell_n=\log_{Kk}|L_n|+O(1),
> \qquad
> \tau_2^2=\frac{M_{2,2}}{v_2^3},
> \tag{7.2}
> \]
> with `v_2,M_{2,2}` from (5.3)–(5.4). In particular,
> \[
> \boxed{
> t_{mix}(\epsilon)
> =\frac{1}{v_2}\log_{Kk}|L_n|
> +O_{K,k,m,\epsilon}(\sqrt{\log |L_n|}).
> }
> \tag{7.3}
> \]

**Proof.** The spectral expansion is Section 4. The exact shell decomposition is (5.1). Choose any `h_n->infinity` with `h_n=o(sqrt(ell_n))`; (6.4) and (6.7) make the error terms in (6.8) vanish. At times `t=ell_n/v_2+z sqrt(ell_n)`, the CLT (5.5) gives

\[
\Pr(R_t<\ell_n+o(\sqrt{\ell_n}))
\to
\Phi(-z/\tau_2).
\]

The upper and lower bounds in (6.8) squeeze TV to the same limit. `QED`

## 8. The outputs are spectral but not long-range

The output degree is

\[
D_2=K(K+1)k^2,
\]

so the regular-tree branching benchmark is `D_2-1`. One output step moves the bigraph half-radius by at most two. Therefore an output radius-`r` ball lies inside a left bigraph ball of half-radius `2r`, and

\[
|B_{Y^{[4]}}(x,r)|
\le C_{K,k}(Kk)^{2r}.
\tag{8.1}
\]

But

\[
(Kk)^2=K^2k^2
< K(K+1)k^2-1=D_2-1,
\tag{8.2}
\]

because `Kk^2>1`. Let

\[
r_n=\left\lfloor\frac12\log_{D_2-1}|L_n|\right\rfloor.
\]

This is an unsaturated radius for the LRE singleton test, while

\[
\frac{|B_{Y^{[4]}}(x,r_n)|}{(D_2-1)^{r_n}}
\le
C_{K,k}
\left(\frac{(Kk)^2}{D_2-1}\right)^{r_n}
\to0.
\tag{8.3}
\]

Hence no fixed positive long-range-expansion constant can hold for the outputs. Theorem A therefore produces source-valid T08 examples strictly outside Altschuler's output hypothesis.

## 9. Concrete new class: exact-distance-four graphs of the non-Ramanujan Eisenstein bigraphs

Take the EFMP Eisenstein family `X_E^{p,q}` with `p=2` and admissible primes `q`. Their Theorem 8.2 gives a `(p^3+1,p+1)=(9,3)` Cayley bigraph, hence

\[
K=8,\qquad k=2.
\]

The source family is left-transitive, adj-Ramanujan, **non-Ramanujan**, satisfies Sarnak--Xue density, and has girth tending to infinity. The exact-distance-four left graph

\[
Z_q:=Y^{[4]}(X_E^{2,q})
\tag{9.1}
\]

is therefore a Cayley graph on the left finite group.

Its degree is

\[
\boxed{D_2=8\cdot9\cdot4=288.}
\tag{9.2}
\]

The squared-singular-value Ramanujan bulk is `[2,18]`, with possible zero modes. Equation (4.6) becomes

\[
q_2(x)=\frac{x^2-19x+72}{288}.
\tag{9.3}
\]

This polynomial is convex. On the bulk its maximum is at an endpoint:

\[
q_2(2)=\frac{19}{144},
\qquad
q_2(18)=\frac{3}{16},
\]

while

\[
q_2(0)=\frac14.
\]

Therefore every nonconstant output eigenvalue is at most `1/4`, and

\[
\boxed{\operatorname{gap}(Z_q)\ge\frac34.}
\tag{9.4}
\]

The five interior radial multiplicities are

\[
\boxed{
\{-2:1,\;-1:1,\;0:14,\;+1:16,\;+2:256\}.
}
\tag{9.5}
\]

Hence

\[
\boxed{
 v_2=\frac{175}{96},
 \qquad
 M_{2,2}=\frac{1045}{288},
 \qquad
 \tau_2^2=\frac{642048}{1071875}.
}
\tag{9.6}
\]

Writing `n_q=|V(Z_q)|`, Theorem A gives

\[
\boxed{
T_q=\frac{96}{175}\log_{16}n_q+O(1)
}
\tag{9.7}
\]

and the full rate-one continuous-time TV profile

\[
\boxed{
 d_{TV}^{Z_q}\left(
 T_q+z\sqrt{\log_{16}n_q}
 \right)
 \longrightarrow
 \Phi\left(
 -z\sqrt{\frac{1071875}{642048}}
 \right).
}
\tag{9.8}
\]

The output branching mismatch is concrete:

\[
256=(Kk)^2<287=D_2-1.
\tag{9.9}
\]

Thus `(Z_q)` is a genuinely new project class of 288-regular vertex-transitive Cayley **spectral expanders with cutoff that are not long-range expanders**. The ancestor bigraph itself is deliberately non-Ramanujan; the Green information is supplied by Sarnak--Xue density rather than a full Ramanujan spectrum.

## 10. Why this is more than another checker or constant

The parent conjecture does not move to solved, but two mathematical mechanisms move.

1. **Radial clock can be changed while preserving the information front.** The same nonbacktracking shell laws that mixed the ordinary half-square also mix a walk whose local transition is exact distance four and whose radial process has five increments. The source Green estimate and the output radial CLT decouple cleanly.
2. **The spectral-expansion step survives removal of every ordinary-half edge.** The incidence-square identity (4.5) gives a new normalized polynomial with a uniform gap on the adj-Ramanujan singular-value support. This is not a perturbative use of the preceding 18-regular graph.

These are mechanism-level advances with a proved application, rather than an auxiliary constant without transfer.

## 11. Exact executed sanity check

The checker created and executed in this run is

`2026-09-20_10-59-32__biregular_distance4_green_exact.py`.

Its archived output is

`2026-09-20_10-59-32__biregular_distance4_green_exact.out`.

It verifies with exact rational/integer arithmetic:

* `D_2=K(K+1)k^2` and the five radial multiplicities on a parameter grid;
* the drift factorization
  \[
  v_2=\frac{(Kk-1)(2Kk+k+1)}{D_2};
  \]
* the two roots of `q_2(x)=1`, namely the Perron value `(K+1)(k+1)` and the negative value `-K(k-1)`;
* the strict tree-growth mismatch `(Kk)^2<D_2-1`;
* for `(K,k)=(8,2)`, degree `288`, radial counts `{-2:1,-1:1,0:14,1:16,2:256}`, `v=175/96`, `M2=1045/288`, `tau^2=642048/1071875`;
* spectral images `q_2(0)=1/4`, `q_2(2)=19/144`, `q_2(18)=3/16`, giving gap at least `3/4`; and
* the center coefficient `96/175`.

The archived output ends

`P26_T08_BIGRAPH_DISTANCE4_GREEN_EXACT_PASS`.

Creation commits:

* checker: `64059749efdc40ba74b08401caa3aa205d3d4934`;
* output: `f0a73e75d10a6e700cf496db435c0dcee9b54e1f`.

These checks certify algebra and constants only; the asymptotic transfer proof is written above.

## 12. Residual obstruction and next attack

The remaining source obstruction is not local radial geometry. The source Green front in this report still comes from an arithmetic Sarnak--Xue density theorem on an ancestor bigraph. Arbitrary bounded-degree vertex-transitive spectral expanders need not expose such an ancestor or a near-Ramanujan bulk.

The next P26 attack is a **weighted exceptional-density Green criterion**. Instead of counting exceptional NBRW modes or assuming a sharp SX exponent, weight each exceptional mode by its actual radial amplification at the entropic radius and seek a bound of the form

\[
\log\left(
1+\sum_{j\in E_n}W_j(\ell_n)
\right)=o(\sqrt{\log n}).
\tag{12.1}
\]

This is strictly weaker than requiring few exceptional modes and is designed to tolerate polynomially many moderately subcritical outliers. P26 will pursue this shell-spectral route. NM13-01/C28 remains complementary on the direct arbitrary-transitivity quotient-likelihood route `f_t=nu_t/barpi`.

No historical or peer report was modified, no public posting was made, and no schedule/access setting was changed.

## 13. ledger_delta

```json
{
  "slot": "P26",
  "parent": "T08",
  "source": "Salez arXiv:2508.21055 Problem 2.3",
  "source_status_before": "PARTIAL / OPEN",
  "source_status_after": "PARTIAL / OPEN",
  "source_level_gain": "rate-one continuous-time Gaussian-profile cutoff for exact bigraph-distance-four left graphs of left-transitive adj-Ramanujan Sarnak-Xue bigraph families; concrete 288-regular Cayley non-LRE class from the non-Ramanujan Eisenstein p=2 family",
  "mechanism_gain": "quantitative radial-clock Green-shell transfer with explicit finite-accuracy sandwich; exact incidence polynomial for second spherical halves; five-increment compound-Poisson radial CLT",
  "new_class": "Z_q = exact-distance-four graph on the left side of EFMP X_E^{2,q}; degree 288; spectral gap >= 3/4; not fixed-constant LRE; cutoff center (96/175) log_16 n with O(sqrt(log n)) Gaussian window",
  "c28_coordination": "NM13-01 owns reversal-arc/Hodge and direct stabilizer-quotient likelihood control; P26 owns shell-Green/spectral-density radial-clock transfer",
  "checker_result": "P26_T08_BIGRAPH_DISTANCE4_GREEN_EXACT_PASS",
  "restricted_status": "CANDIDATE_FULL_PENDING_LATER_INDEPENDENT_REVIEW",
  "publication_novelty": "UNVERIFIED",
  "remaining_obstruction": "derive a weighted exceptional NBRW Green-density bound from arbitrary vertex transitivity plus ordinary spectral expansion, without an arithmetic/SX ancestor",
  "next_attack": "weighted exceptional-density shell Green criterion with mode-by-mode radial amplification",
  "runtime_model": "GPT-5.6 Sol",
  "runtime_reasoning": "UNVERIFIED"
}
```

End of complete P26 substantive T08 report.
