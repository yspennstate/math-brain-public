Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; GPT-6 / maximum reasoning was requested in prompt text, but no authenticated runtime model/effort telemetry or binding selector is exposed.

# F0003 — exact Fourier–Hafnian representation, flat-spectrum no-go, and multiplicative-charge/Kloosterman decomposition

Date: 2026-09-18 UTC.  
Slot: `R7-07 Hard Problem New Methods`, native ID `6aabe8413f60819197825dd81ca138ae`.  
Outside target: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797 (2020; Probability Surveys 2021), Section 5 immediately after Theorem 5.2.  
Frozen source metric:

\[
a_3:=\sup\{a\ge0:\Pr(A_{n,3}\text{ singular})\le n^{-a+o(1)}\}.
\]

Cumulative proved value before this artifact: **`a_3 >= 1/4`**.  
Value after this artifact: **`a_3 >= 1/4` — NO SOURCE-METRIC MOVEMENT.**

This is the first ordinary research run in the final recovery cycle after STUCK2. The mandated method triple is **B1 CHANGE THE CATEGORY / B11 DUALIZE / B30 ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME**. The point of the run is to validate the Fourier–Hafnian route exactly, identify what it genuinely buys, and kill the false version of the route before another large saddle calculation is built.

The main new positive result is an exact multiplicative-character decomposition of the hyperbolic Fourier kernel. Projective scaling, which is exactly the `(p-1)` normalization in the modular singularity first moment, breaks the `p^2`-state Fourier kernel into `p-1` charge sectors of dimension only `p+O(1)`. On generic hyperbola orbits, the matrix entries become normalized twisted Kloosterman sums and therefore have square-root cancellation `O(p^{-1/2})`. The main new negative result is equally sharp: the full kernel is unitary after scaling and has **no spectral gap at all**, and an edge-diagonalizing Fourier gauge leaves local cubic tensors with exactly preserved Frobenius norm. Hence no operator-norm-only argument can produce the missing `p^3/n` gain.

---

## 1. The exact one-prime blocker inherited from STUCK2

Let `A=A_{n,3}` be the adjacency matrix of a uniform simple cubic graph, and let `p>3` be prime. For a matrix over `F_p`,

\[
L_p(A):=\frac{|\ker(A\bmod p)|-1}{p-1}
\]

is exactly the number of projective nonzero kernel vectors. Real singularity implies `L_p(A)>=1` for every prime `p`, so

\[
\Pr(A\text{ singular over }\mathbb R)\le \mathbb E L_p(A).
\tag{1.1}
\]

The cumulative low-alphabet analysis has already shown that support-two modular rows are exponentially negligible at growing `p`, and that **all** exactly-three-residue rows satisfy

\[
\frac1{p-1}\mathbb E S_p^{(3)}(A)
=
\frac{8}{9n}+o(n^{-1}),
\tag{1.2}
\]

with false twins giving the entire first-order term. Thus the final-recovery blocker is the support-at-least-four mass

\[
\mathcal M_{\ge4}(n,p)
:=
\frac1{p-1}\mathbb E S_p^{(\ge4)}(A).
\tag{1.3}
\]

A theorem

\[
\mathcal M_{\ge4}(n,p)\le n^{-1/3+o(1)}
\quad\text{for one }p=n^{1/3-o(1)}
\tag{1.4}
\]

would imply `a_3>=1/3`. Nothing below proves (1.4). The purpose of the present run is to put (1.3) into an exact collective transform and determine whether that transform really contains a contraction mechanism unavailable to the previous rowwise approach.

---

# 2. B1 — change category: from modular null rows to an exact Fourier–Hafnian/Wick tensor

Work first in the cubic configuration model. There are `3n` labelled half-edges, grouped into three half-edges at each vertex, and a uniform perfect matching `M` of the half-edges. Let `A_M` be the resulting multigraph adjacency matrix, with the standard convention that a loop contributes `2` to the corresponding diagonal entry. The number of half-edge matchings is

\[
(3n-1)!!.
\]

Fix a prime `p`, write

\[
e_p(x):=\exp(2\pi i x/p),
\]

and put

\[
G:=\mathbb F_p^2.
\]

For `z=(t,y)` and `w=(t',y')` in `G`, define the symmetric hyperbolic bilinear form

\[
B(z,w):=ty'+t'y
\tag{2.1}
\]

and its Fourier kernel

\[
K(z,w):=e_p(B(z,w)).
\tag{2.2}
\]

## 2.1 Exact phase identity, including loops

For a half-edge `h`, let `v(h)` be its incident vertex. For fixed `t,y in F_p^n`, every matched pair `{h,h'}` contributes

\[
t_{v(h)}y_{v(h')}+t_{v(h')}y_{v(h)}.
\]

Summing over matched pairs gives exactly

\[
\boxed{
 t^T A_M y
 =
 \sum_{\{h,h'\}\in M}
 B\bigl((t_{v(h)},y_{v(h)}),(t_{v(h')},y_{v(h')})\bigr).
}
\tag{2.3}
\]

If `h,h'` are two half-edges of the same vertex `i`, the contribution in (2.3) is `2t_i y_i`, exactly matching the adjacency convention for a loop. Thus no loop correction is hidden in the transform.

Fourier inversion gives

\[
\mathbf 1_{\{A_My=0\}}
=
 p^{-n}\sum_{t\in\mathbb F_p^n}e_p(t^TA_My).
\tag{2.4}
\]

## 2.2 Exact fixed-row Hafnian formula

For fixed `t,y`, form the `3n x 3n` symmetric matrix indexed by half-edges,

\[
\mathcal K^{(t,y)}_{h,h'}
:=
K\bigl((t_{v(h)},y_{v(h)}),(t_{v(h')},y_{v(h')})\bigr)
\qquad(h\ne h').
\tag{2.5}
\]

The diagonal is irrelevant to the Hafnian. By definition of the Hafnian as the sum over perfect matchings of the index set,

\[
\operatorname{Haf}(\mathcal K^{(t,y)})
=
\sum_M e_p(t^TA_My).
\tag{2.6}
\]

Averaging (2.4) over the uniform configuration pairing therefore yields the exact identity

\[
\boxed{
\Pr_{\rm conf}(A_My=0)
=
\frac{p^{-n}}{(3n-1)!!}
\sum_{t\in\mathbb F_p^n}
\operatorname{Haf}(\mathcal K^{(t,y)}).
}
\tag{2.7}
\]

This validates the STUCK2 Fourier–Hafnian candidate with the graph model and normalization explicit.

## 2.3 Aggregate Wick form

Let `Z_z`, `z in G`, be formal commuting Gaussian variables under the Wick functional with covariance

\[
\mathcal W_K(Z_zZ_w)=K(z,w),
\]

and higher even moments given by Wick pairing. Define the cubic form

\[
P(Z):=\sum_{z\in G}Z_z^3.
\tag{2.8}
\]

Choosing a state `z_i=(t_i,y_i)` for each of the `n` vertices and then Wick-pairing the resulting `3n` half-edge variables is exactly the sum over `(t,y)` and configuration matchings. Hence

\[
\boxed{
\mathbb E_{\rm conf}|\ker(A_M\bmod p)|
=
\frac{p^{-n}}{(3n-1)!!}
\mathcal W_K\!\left[P(Z)^n\right].
}
\tag{2.9}
\]

No positivity of the formal covariance is asserted or needed. Equation (2.9) is an algebraic Wick identity.

This is the promised category change: the growing-modulus first moment is a single cubic Gaussian/Feynman tensor contraction rather than a sum of separately approximated row coefficients.

---

# 3. B11 — dualize: the hyperbolic Fourier kernel is exactly flat-spectrum

Put

\[
U:=p^{-1}K
\]

as an operator on `l^2(G)`. Let `R` be reflection,

\[
(Rf)(z)=f(-z).
\]

## 3.1 Exact operator algebra

For `z,u in G`, nondegeneracy of `B` gives

\[
(K^2)_{z,u}
=
\sum_{w\in G}e_p(B(z,w)+B(w,u))
=
\sum_{w\in G}e_p(B(w,z+u))
=
p^2\mathbf1_{\{u=-z\}}.
\]

Therefore

\[
\boxed{K^2=p^2R,\qquad U^2=R,\qquad U^4=I.}
\tag{3.1}
\]

Similarly,

\[
KK^*=p^2I,
\tag{3.2}
\]

so `U` is symmetric and unitary.

For odd `p`,

\[
\operatorname{tr}U
=
\frac1p\sum_{a,b\in\mathbb F_p}e_p(2ab)=1,
\tag{3.3}
\]

\[
\operatorname{tr}U^2=\operatorname{tr}R=1,
\tag{3.4}
\]

and

\[
\operatorname{tr}U^3
=
\frac1p\sum_{a,b}e_p(-2ab)=1.
\tag{3.5}
\]

Since the eigenvalues lie in `{1,-1,i,-i}`, these traces determine their multiplicities uniquely:

\[
\boxed{
\begin{aligned}
 m_{1}&=\frac{p^2+3}{4},\\
 m_{-1}&=\frac{p^2-1}{4},\\
 m_{i}=m_{-i}&=\frac{p^2-1}{4}.
\end{aligned}}
\tag{3.6}
\]

### Flat-spectrum no-go

There is **no decaying eigenmode** to exploit: every eigenvalue of `U` has modulus one, and each of the four eigenspaces has dimension `Theta(p^2)`. Consequently, diagonalizing `K` and then bounding mode-by-mode in operator norm cannot by itself produce any `p^{-c}` gain. The hoped-for `p^3/n` mechanism must come from the cubic vertex tensor and cancellation between many modes, not from an edge spectral gap.

This is the first rigorous failure result of the STUCK2 route.

---

# 4. The cubic copy tensor is Fourier-dual to an exact zero-sum tensor

Let

\[
D(x_1,x_2,x_3):=\mathbf1_{\{x_1=x_2=x_3\}}
\qquad(x_j\in G)
\tag{4.1}
\]

be the degree-three copy tensor at a graph vertex. A direct character-orthogonality computation gives

\[
\begin{aligned}
(U^{\otimes3}D)(w_1,w_2,w_3)
&=
\sum_{z\in G}U_{w_1,z}U_{w_2,z}U_{w_3,z}\\
&=
p^{-3}\sum_{z\in G}e_p(B(w_1+w_2+w_3,z))\\
&=
p^{-1}\mathbf1_{\{w_1+w_2+w_3=0\}}.
\end{aligned}
\]

Thus

\[
\boxed{
U^{\otimes3}D
=
p^{-1}Z_0,
\qquad
Z_0(w_1,w_2,w_3)=\mathbf1_{\{w_1+w_2+w_3=0\}}.
}
\tag{4.2}
\]

This is an exact spin/flow duality: equality of the three incident states Fourier-transforms into additive charge conservation.

It does **not** provide local norm decay. Indeed

\[
\|D\|_F^2=|G|=p^2,
\]

while there are `|G|^2=p^4` zero-sum triples, so

\[
\|p^{-1}Z_0\|_F^2=p^{-2}p^4=p^2.
\tag{4.3}
\]

The local norm is exactly preserved, as it must be under the unitary transform.

---

# 5. A source-matched hidden symmetry: projective scaling commutes with the Fourier kernel

The normalized modular first moment divides by `p-1` because nonzero null vectors are counted projectively. The Fourier kernel has **exactly the same symmetry**.

For `lambda in F_p^*`, define

\[
g_\lambda(t,y):=(\lambda^{-1}t,\lambda y).
\tag{5.1}
\]

Then

\[
B(g_\lambda z,g_\lambda w)=B(z,w),
\]

so

\[
K(g_\lambda z,g_\lambda w)=K(z,w).
\tag{5.2}
\]

The action on a Fourier pair `(t,y)` is precisely the projective rescaling `y -> lambda y` accompanied by the contragredient rescaling `t -> lambda^{-1}t`. On every nonzero `y`, this action is free. Thus the symmetry is not cosmetic: it is the Fourier-side realization of the `(p-1)` quotient in `L_p(A)`.

The orbits of `F_p^*` on `G=F_p^2` are

\[
O_0=\{(0,0)\},
\quad
O_t=\{(t,0):t\ne0\},
\quad
O_y=\{(0,y):y\ne0\},
\tag{5.3}
\]

and, for each `r in F_p^*`,

\[
O_r=\{(t,y):ty=r\}.
\tag{5.4}
\]

Hence the invariant subspace has dimension only

\[
1+1+1+(p-1)=p+2,
\tag{5.5}
\]

rather than `p^2`.

More generally, because `F_p^*` is abelian, `l^2(G)` splits into multiplicative-character sectors. The trivial sector has dimension `p+2`; every nontrivial character sector has dimension `p+1`, and

\[
(p+2)+(p-2)(p+1)=p^2.
\tag{5.6}
\]

This decomposition is exact and commutes with `U`.

---

# 6. Hyperbola blocks are twisted Kloosterman transforms

This is the main positive B11 result.

Fix a multiplicative character `eta` of `F_p^*`. On a hyperbola orbit `O_r`, parameterize

\[
(t,y)=(a,r/a),\qquad a\in\mathbb F_p^*.
\]

Use the normalized character vector

\[
e_{r,\eta}(a,r/a)
=(p-1)^{-1/2}\eta(a).
\tag{6.1}
\]

Replacing `eta` by its inverse only changes the sector convention. For `r,s !=0`, direct substitution gives

\[
\begin{aligned}
\langle e_{s,\eta},Ue_{r,\eta}\rangle
&=
\frac1{p(p-1)}
\sum_{a,c\ne0}
\overline{\eta(a)}\eta(c)
 e_p\!\left(\frac{ar}{c}+\frac{cs}{a}\right)\\
&=
\frac1p\sum_{x\ne0}\eta(x)e_p\!\left(sx+\frac r x\right).
\end{aligned}
\tag{6.2}
\]

Thus each generic character block is a normalized twisted Kloosterman transform:

\[
\boxed{
Q^{(\eta)}_{s,r}
=
\frac1p\operatorname{Kl}_{\eta}(s,r),
\qquad
\operatorname{Kl}_{\eta}(s,r)
:=\sum_{x\ne0}\eta(x)e_p(sx+r/x).
}
\tag{6.3}
\]

For `rs !=0`, the classical Weil bound for these one-variable Kloosterman/Salié-type sums gives

\[
\boxed{|Q^{(\eta)}_{s,r}|\le 2p^{-1/2}.}
\tag{6.4}
\]

For the trivial character this is the usual Kloosterman bound. Axis-to-hyperbola entries are normalized Gauss sums for nontrivial `eta` and have size `p^{-1/2}`; in the trivial sector they are exactly `-1/p`. The origin/axis part of the trivial sector is exceptional: for the two nonzero axes,

\[
Q_{tt}=Q_{yy}=\frac{p-1}{p},
\qquad
Q_{ty}=Q_{yt}=-\frac1p,
\tag{6.5}
\]

and

\[
Q_{0,t}=Q_{0,y}=Q_{0,r}=\frac{\sqrt{p-1}}p.
\tag{6.6}
\]

So the projective quotient produces a very concrete dichotomy:

- a small axis/origin block containing almost-nondecaying trivial-sector directions;
- generic hyperbola/character blocks whose **matrix entries** exhibit square-root cancellation `O(p^{-1/2})`.

This does not contradict the flat spectrum (3.6): each character block is still part of a unitary operator, so its operator norm can be one even though its coordinate entries are small. The new information is delocalization, not spectral contraction.

---

# 7. Multiplicative charge is conserved at cubic vertices

Because the copy tensor `D` is invariant under applying `g_lambda` simultaneously to its three legs, its coefficient in multiplicative-character sectors vanishes unless the three characters multiply to the trivial character. In an oriented tensor-network convention, the two ends of an edge carry inverse characters. Therefore the Fourier–Hafnian tensor network admits an exact **multiplicative-charge flow decomposition**:

\[
\boxed{
\eta_1\eta_2\eta_3=1
\quad\text{at every cubic vertex.}
}
\tag{7.1}
\]

Equivalently, after choosing an orientation and writing characters additively in the cyclic dual group of `F_p^*`, the sector labels form a finite-group flow on the graph.

This is the structural gain that the raw `p^2` Fourier diagonalization misses. It gives a source-aligned route for using (6.4): nontrivial charge edges carry Kloosterman-delocalized orbit kernels, while low-complexity exceptional contributions are forced into the trivial/axis sectors or into structured charge flows.

The remaining difficulty is that the cycle-space of a connected cubic graph has dimension

\[
|E|-|V|+1=\frac n2+1,
\]

so there are exponentially many charge flows. Entrywise `p^{-1/2}` gains cannot simply be multiplied and then summed naively; doing so may return the entire gain. A successful argument needs a multilinear contraction or an inverse theorem showing that flows which saturate the unitary norm are themselves structurally exceptional.

This is a much sharper statement of the STUCK2 missing ingredient than “control all support >=4 rows.”

---

# 8. B30 — edge-diagonalizing gauge and the exact gluing failure

There is another exact way to expose where the undirected dependence lives.

Orient every graph edge. For an edge directed from a tail vertex to a head vertex, absorb the unitary `U` into the head half-edge. Since the edge tensor is `K=pU`, that edge becomes `p` times an identity contraction. If a vertex has indegree `k`, its local tensor becomes

\[
T_k=(U^{\otimes k}\otimes I^{\otimes(3-k)})D
\tag{8.1}
\]

up to a permutation of the legs.

The four tensors are explicit:

\[
T_0(x_1,x_2,x_3)=\mathbf1_{\{x_1=x_2=x_3\}},
\tag{8.2}
\]

\[
T_1(w,x_2,x_3)
=p^{-1}e_p(B(w,x_2))\mathbf1_{\{x_2=x_3\}},
\tag{8.3}
\]

\[
T_2(w_1,w_2,x)
=p^{-2}e_p(B(w_1+w_2,x)),
\tag{8.4}
\]

and

\[
T_3(w_1,w_2,w_3)
=p^{-1}\mathbf1_{\{w_1+w_2+w_3=0\}}.
\tag{8.5}
\]

Every edge is now an identity wire, but the price is the mixture of these four vertex tensors.

## 8.1 Exact local-norm no-go

A direct count gives

\[
\boxed{\|T_k\|_F=p\quad\text{for }k=0,1,2,3.}
\tag{8.6}
\]

For example, `T_1` has `p^4` nonzero entries of modulus `p^{-1}`, while `T_2` has `p^6` entries of modulus `p^{-2}`. Thus the apparent small factors in (8.3)-(8.4) are exactly compensated by support size. The gauge produces no local Frobenius-norm contraction whatsoever.

Consequently any proof that takes absolute values vertex-by-vertex, or uses only the operator norm of `U` plus local Frobenius norms, is incapable of seeing the desired growing-modulus decay. The proof must preserve phase cancellation across many vertices.

## 8.2 Pure copy/zero-sum gluing is equivalent to bipartiteness

The mixed tensors `T_1,T_2` disappear exactly when every vertex has indegree `0` or `3`. Such an orientation exists iff the graph is bipartite:

- if every vertex is a source or sink, every edge joins a source to a sink, hence the graph is bipartite;
- if the graph is bipartite, orient every edge from one part to the other.

Therefore

\[
\boxed{
\text{the Fourier gauge reduces the entire cubic network to only copy and zero-sum vertices}
\iff G\text{ is bipartite}.}
\tag{8.7}
\]

The favorable gluing case is exponentially rare in the cubic configuration model. For a fixed balanced bipartition, all `3n/2` half-edges on one side must be matched across. The probability is

\[
\frac{(3n/2)!}{(3n-1)!!}
=
\frac{2^{3n/2}}{\binom{3n}{3n/2}}
=
(1+o(1))\sqrt{\frac{3\pi n}{2}}\,2^{-3n/2}.
\tag{8.8}
\]

Union-bounding over the `\frac12\binom n{n/2}` unordered balanced vertex bipartitions gives

\[
\boxed{
\Pr_{\rm conf}(G\text{ bipartite})
\le
\left(\frac{\sqrt3}{2}+o(1)\right)2^{-n/2}.
}
\tag{8.9}
\]

Conditioning on simplicity changes this by only a fixed multiplicative factor for cubic configurations, so bipartiteness is also exponentially rare in the source model.

Thus the “turn all edges into deltas, then solve a clean flow model” idea does not fail because of a loose estimate. It fails for a precise graph-theoretic reason: random cubic graphs are overwhelmingly non-bipartite, forcing mixed Fourier tensors.

---

# 9. What the near-equidistributed one-prime problem has become

The exact transform has now separated three distinct phenomena.

### 9.1 Baseline projective symmetry

The action (5.1) is exactly the projective scaling of nonzero null vectors. It removes a genuine factor `p-1`; it is not an invented quotient.

### 9.2 Generic orbit modes have square-root cancellation

After multiplicative-character decomposition, generic hyperbola-to-hyperbola entries are `p^{-1}` times a twisted Kloosterman sum and hence are `O(p^{-1/2})`. This is the first collective Fourier representation in the R7-07 line where a square-root finite-field cancellation is visible **before** a rowwise local CLT.

### 9.3 The obstruction is now a charge-flow contraction, not a missing eigenvalue bound

Because every character block belongs to a unitary operator and the cubic tensor conserves charge, the missing estimate can be stated cleanly:

> At one prime `p=n^{1/3-o(1)}`, bound the charge-conserving cubic tensor network after removing the already-classified low-alphabet/axis contributions, gaining enough from Kloosterman-delocalized generic sectors that the total normalized support-`>=4` mass is `n^{-1/3+o(1)}` or smaller.

A sufficient intermediate theorem would be an `l^2 -> l^infinity` or entropy-sensitive multilinear contraction showing that a nontrivial charge flow which avoids the axis block cannot saturate unitary norm on more than a structurally exceptional set of vertices. No such theorem is proved here.

The old idea “diagonalize `K` and multiply spectral gaps” is now rigorously dead; the replacement object is the **multiplicative-charge/Kloosterman network**.

---

# 10. Fixed-prime literature bridge: the desired first moment is already the correct limit in a neighboring symmetric model

A fresh 2026-09-18 check of Nguyen--Wood, *Cokernels of adjacency matrices of random r-regular graphs*, arXiv:1806.10068, and Mészáros, *The distribution of sandpile groups of random regular graphs*, arXiv:1806.03736, gives a useful calibration.

Nguyen--Wood Theorem 1.5 treats the symmetric multigraph obtained as the union of `r` independent uniform perfect matchings. Their proof uses Mészáros's fixed-finite-group mixing theorem. For a fixed odd prime `p` with `p` not dividing `r`, the first surjection moment to `V=F_p` tends

\[
|\wedge^2F_p|=1.
\]

For `r=3`, this says in that neighboring symmetric model

\[
\boxed{
\mathbb E\bigl(|\ker(C_n\bmod p)|-1\bigr)\to1
\qquad(p\text{ fixed},\ p\ne3).
}
\tag{10.1}
\]

Equivalently,

\[
\mathbb E L_p(C_n)\sim\frac1{p-1}
\quad\text{for each fixed }p.
\tag{10.2}
\]

That is exactly the scale one would want at a growing `p`: if an analogous estimate were uniform to `p=n^{1/3-o(1)}`, it would give the cubic `n^{-1/3+o(1)}` modular bound immediately.

But the fixed-group theorem is **not** such a uniform result. Nguyen--Wood explicitly note in the moment argument that the little-`o` constant may depend on `|V|`; Mészáros's approximate-independence lemma likewise has constants depending on `V`, and his proof uses a phase-separation constant `1-cos(pi/|V|)`. Therefore replacing fixed `p` by `p(n)` is not licensed by the published theorem.

There is also a model-transfer issue: the union-of-three-independent-perfect-matchings model weights a simple cubic graph by its number of ordered 1-factorizations. It is not literally the uniform simple cubic source distribution. Bare contiguity, even if available, would not by itself transfer an unbounded moment such as `|ker|-1` at the polynomial precision needed here.

So (10.1) is a strong nearest solved analogue, not a hidden solution.

---

# 11. Dated source/current-status check — 2026-09-18

The original source remains Van Vu, arXiv:2005.02797, submitted 6 May 2020. The canonical repository intake records the precise locator as Section 5, open question after Theorem 5.2, PDF page 8: for a uniform simple fixed-`d` regular graph, Huang's polynomial upper bound is compared with the `n^{-d+2}` lower mechanism, and the sharp exponent is asked for.

Current neighboring work checked in this run:

1. Hoi H. Nguyen and Amanda Pan, *A note on the singularity probability of random directed d-regular graphs*, arXiv:2308.06461 / European Journal of Combinatorics 2024. Their `n^{-1/3+o(1)}` theorem is for the **directed** model and uses modular reduction plus an inverse characteristic-function/Kneser mechanism. It does not settle Vu's undirected sharp exponent.
2. Hoi H. Nguyen and Melanie Matchett Wood, *Cokernels of adjacency matrices of random r-regular graphs*, arXiv:1806.10068, Theorem 1.5 and its moment proof. This supplies the fixed-prime symmetric matching-union analogue described above, not growing-`p` uniformity for the source model.
3. Andras Mészáros, *The distribution of sandpile groups of random regular graphs*, arXiv:1806.03736, current arXiv v4 dated 28 January 2020. Its fixed-group mixing proof explicitly permits constants depending on the finite group and therefore cannot simply be evaluated at `|V|=p(n)`.

A bounded fresh search found no later source-matching theorem proving the exponent `d-2` for the uniform simple undirected fixed-degree model. That is negative evidence only; worldwide openness and novelty remain **UNVERIFIED**.

---

# 12. Metric, failure map, and next attack

The frozen source metric does not move:

\[
\boxed{a_3\ge1/4\quad\longrightarrow\quad a_3\ge1/4.}
\]

The run nevertheless changes the mathematical map in four rigorous ways:

1. the configuration-model Fourier–Hafnian/Wick identity is now exact, including loops and normalization;
2. the normalized hyperbolic Fourier kernel is exactly unitary with spectrum `{1,-1,i,-i}` and no spectral gap, killing a false spectral-decay route;
3. projective scaling decomposes the `p^2` Fourier state space into multiplicative-charge sectors of size only `p+O(1)`, with generic blocks given by twisted Kloosterman transforms and entrywise `O(p^{-1/2})` cancellation;
4. the cubic tensor enforces exact multiplicative-charge conservation, while an edge-diagonalizing gauge has a pure copy/zero-sum form iff the graph is bipartite, an exponentially rare source configuration.

The final recovery route should therefore continue only if it exploits **charge-flow cancellation**, not raw edge spectra or local tensor norms.

The next nonrepeating method triple is:

- **B4 — PROVE SOMETHING WEAKER, COMPLETELY:** first seek a quantitative growing-`p` first-surjection-moment theorem in the easier symmetric model that is the union of three independent perfect matchings, where the fixed-`p` limit is already known exactly.
- **B6 — DEFORM TO A POINT YOU CAN SOLVE:** if such a theorem can be obtained, build an explicit switching/interpolation from the edge-colored three-matching model toward the ordinary cubic configuration model and track the projective kernel moment rather than invoking bare contiguity.
- **B26 — HUNT THE SPORADIC CASE:** in the charge decomposition, isolate the trivial and quadratic-character/Salié sectors and determine whether they are the only sectors capable of saturating the unitary norm; generic characters should then be attacked with the uniform Weil/Deligne cancellation already visible in (6.4).

If these ordinary runs reach the next three-run no-movement trigger, no third HARD stuck recovery is authorized: the protocol then requires immutable handoff/rotation.
