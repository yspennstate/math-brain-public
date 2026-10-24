Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run model/effort telemetry, so I do not claim otherwise.

# P07-A — unique prime optimizer, positive cosine bases, and a centered additive-discrepancy target

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `3a93df2d3954c4d004e5b036e1bbce7068a6c2d4`  
**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0803+0300__prime_optimal_complementary_circuits.md`  
**Complementary checkpoint used once:** P07-B `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0832+0300__reciprocal_convolution_collision_energy.md` plus its equation-(4.11) erratum. P07-B owns collision-energy / exceptional-frequency / dual descent. This report imports only its exact already-shared identity `q*r=1` in Section 5 and develops a different primal structural consequence.

**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper *The Lovasz number of random circulant graphs*, arXiv:2502.16227. For the source dense random undirected circulant model, with the independent Bernoulli choices made on conjugate nonzero difference pairs, the endpoint is
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The checked primary source still gives
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}
\]
and states the sharp asymptotic as open. The source model/parity and Fourier normalizations below are kept explicit. This run does **not** improve the arbitrary-`n` published upper bound, so the fixed full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**.

The substantive progress is prime-order and structural: (i) the cyclically averaged optimal primal is actually unique; (ii) theta has an exact maximum-over-positive-cosine-bases formula, giving an explicit feasible-certificate construction for every candidate basis; (iii) the optimizer is equivalently a positive probability measure whose cosine transform takes one exact negative flat level on every random edge row; and (iv) the distance from the sharp constant is exactly a centered weighted additive-cut discrepancy. The last quantity is antisymmetric under complementation, so it is automatically centered in the fair source ensemble. This gives a concrete concentration target rather than another all-sign RIP estimate.

---

## 0. Concise predecessor preservation: SRG69 remains OPEN / PARTIAL

The reassigned predecessor is not erased and is not called solved. Preserve

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/runs/2026-09-19/2026-09-19T22-46-00Z__report.md`

with blob `fcf42c57f30ced2e5407f70dbee6481ae1bb8278`, frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Its no-Cayley result, rooted `L/B/C` equivalence, centered spectral transfer, endpoint filters, cycle transfer, block-moment/Gram reductions and residual/star-complement route remain historical results. This report does not modify that root.

---

# 1. Prime pair normalization and inherited exact support theorem

Let `p` be an odd prime and write
\[
P=\{1,\dots,(p-1)/2\}
\]
for representatives of conjugate nonzero frequency pairs. Let `E^+\subset P` be the selected edge-difference pairs, put
\[
e=|E^+|,
\]
and let `A^+=P\setminus E^+`. The full symmetric edge set is `E=\pm E^+`, so `|E|=2e`.

For a cyclically averaged theta-primal solution write `C=Circ(c)` and use the **unnormalized** DFT
\[
h=Fc.
\]
Then
\[
h_j\ge0,\qquad h_j=h_{-j},\qquad h_0=\vartheta(G)=:t,
\qquad \sum_{j\in\mathbb Z_p}h_j=p,
\]
and the edge-zero constraints are
\[
t+2\sum_{j\in P}h_j\cos(2\pi rj/p)=0
\qquad(r\in E^+).
\tag{1.1}
\]

The preceding P07-A report proved, using optimal complementarity plus prime Fourier uncertainty, that **every** optimal cyclic primal has nontrivial spectral support `H=\pm H^+` with
\[
|H^+|=e,
\tag{1.2}
\]
all supported `h_j` strictly positive, while the complement optimizer has the complementary nontrivial support `K=\mathbb Z_p^\times\setminus H`.

---

# 2. New theorem: the prime cyclically averaged optimizer is unique

## Theorem P07-A.16 — uniqueness of the optimal cyclic primal

For every odd prime `p` and every circulant graph `G=Cay(Z_p,E)`, the cyclically averaged optimal theta-primal matrix is unique. The same holds for the complement.

### Proof

Suppose `h^(1)` and `h^(2)` are two optimal spectra in the cyclic primal normalization. Their average is again feasible and optimal because the feasible set is convex and the objective `h_0` is linear.

By the inherited exact-support theorem, every optimum has exactly `2e` nonzero nontrivial frequencies, in `e` conjugate pairs. If `h^(1)` and `h^(2)` had different nontrivial supports, nonnegativity would make the support of their average the union of the two supports, strictly larger than `2e`, contradicting the exact-support theorem applied to the average. Hence every optimum has the same support `H`.

On that fixed support, the edge-zero equations form the rectangular Fourier system
\[
F_{E,\{0\}\cup H}h=0.
\]
It has `2e` rows and `2e+1` columns. Chebotarev nonsingularity of every square Fourier minor at prime order implies full row rank, hence a one-dimensional kernel. Finally `sum h_j=p` fixes the scale. Thus the optimum is unique. ∎

### Consequence

The optimal support map `E^+ -> H^+` is a well-defined deterministic object at prime order. It is equivariant under multiplication by units (with the corresponding inverse multiplier on frequency indices, according to the fixed DFT convention), but **this does not make `H^+` uniform among `e`-subsets**. No such stronger claim is used.

---

# 3. Exact positive-cosine-basis formula: a source-specific feasible-certificate construction

For row-pair set `E^+` and any `e`-subset `J\subset P`, define the real square cosine matrix
\[
C_{E,J}=\bigl(\cos(2\pi rj/p)\bigr)_{r\in E^+,\,j\in J}.
\tag{3.1}
\]

## Lemma P07-A.17 — every such cosine minor is nonsingular

For prime `p`, `C_{E,J}` is nonsingular for every `E^+,J` with `|E^+|=|J|`.

### Proof

If `C_{E,J}z=0` for nonzero real `z`, create a symmetric vector `u` on the full column set `\pm J` by `u_j=u_{-j}=z_j/2`. For every `r\in E^+`,
\[
\sum_{j\in\pm J}u_j\omega^{rj}
=\sum_{j\in J}z_j\cos(2\pi rj/p)=0,
\]
and the same holds at `-r`. Hence the square Fourier minor with rows `\pm E^+` and columns `\pm J` has a nonzero kernel vector, contradicting Chebotarev. ∎

For such `J`, put
\[
x^{(J)}:=-C_{E,J}^{-1}\mathbf1.
\tag{3.2}
\]
Call `J` a **positive basis** when `x^(J)>0` coordinatewise.

## Theorem P07-A.18 — exact maximum over positive bases

Assume `0<e<(p-1)/2`. Then
\[
\boxed{
\vartheta(G)
=
\max_{\substack{J\subset P,\ |J|=e\\ x^{(J)}>0}}
\frac{p}{1+\mathbf1^Tx^{(J)}}.
}
\tag{3.3}
\]
Moreover the maximizing basis is unique and equals the optimal spectral pair support `H^+`.

### Proof: every positive basis gives an exact feasible certificate

Fix a positive basis `J` and set
\[
t_J=\frac p{1+\mathbf1^Tx^{(J)}}.
\]
Define a nonnegative symmetric spectrum by
\[
h_0=t_J,
\qquad h_j=h_{-j}=\frac{t_J}{2}x_j^{(J)}\quad(j\in J),
\qquad h_k=0\quad(k\notin\{0\}\cup\pm J).
\tag{3.4}
\]
Its total mass is exactly `p`, so the inverse DFT has diagonal coefficient `c_0=1`. For every edge row `r\in E^+`, (3.2) gives
\[
h_0+2\sum_{j\in J}h_j\cos(2\pi rj/p)
=t_J\bigl(1+(C_{E,J}x^{(J)})_r\bigr)=0.
\]
Thus the inverse-circulant matrix is PSD, has diagonal one, and vanishes on all edge differences: it is a valid theta-primal certificate with objective `t_J`. Therefore the right side of (3.3) is at most `theta(G)`.

Conversely, the inherited exact-support theorem says the optimal spectrum is supported on exactly one `e`-pair set `H^+`. Divide its edge equations (1.1) by `t` and define
\[
x_j=\frac{2h_j}{t}>0.
\]
Then
\[
C_{E,H}x=-\mathbf1,
\]
so `x=x^(H)`. The trace identity `sum h=p` gives
\[
p=t(1+\mathbf1^Tx),
\]
which is precisely the corresponding value in (3.3). Hence equality holds. Uniqueness of the maximizing basis follows from Theorem P07-A.16. ∎

### Bordered-minor form

For every positive basis,
\[
1+\mathbf1^Tx^{(J)}
=1-\mathbf1^TC_{E,J}^{-1}\mathbf1
=\frac{
\det\begin{pmatrix}1&\mathbf1^T\\ \mathbf1&C_{E,J}\end{pmatrix}
}{\det C_{E,J}}.
\tag{3.5}
\]
Thus the prime source problem is exactly a positivity-selected bordered-minor extreme-value problem for a random row subset of the deterministic cosine system.

The generic inverse-minor / projected-simplex mechanism itself is not claimed novel: related machinery occurs elsewhere in this repository. The new source-specific content here is the combination with the prime exact-support theorem, which makes (3.3) an exact formula and gives uniqueness of its maximizer.

---

# 4. Flat-negative-level reformulation of a supercritical optimizer

For the unique maximizing support `H^+`, write
\[
x=-C_{E,H}^{-1}\mathbf1>0,
\qquad
S=\mathbf1^Tx=\frac pt-1=\frac{p-t}{t},
\]
and normalize
\[
w_j=\frac{x_j}{S},\qquad \sum_{j\in H^+}w_j=1.
\tag{4.1}
\]
Then every selected edge row satisfies the exact identity
\[
\boxed{
\sum_{j\in H^+}w_j\cos(2\pi rj/p)
=-\rho_t,
\qquad
\rho_t:=\frac{t}{p-t},
\qquad r\in E^+.
}
\tag{4.2}
\]

So a large theta value is not merely the existence of some positive Fourier vector. It is the existence of an **endogenous probability measure on exactly `e` frequency pairs whose cosine transform takes one identical negative value on every one of the `e` random edge rows**.

At the conjectural scale `t=c sqrt(p)` with fixed `c>0`,
\[
\rho_t=\frac{c}{\sqrt p-c}
=\frac c{\sqrt p}+O(p^{-1}).
\tag{4.3}
\]
Hence excluding `theta(G)>(1+epsilon)sqrt(p)` is equivalent, on prime order, to excluding a positive-basis measure with flat negative level exceeding `(1+epsilon+o(1))/sqrt(p)`.

This is a primal probabilistic-geometry target and is distinct from P07-B's exceptional-frequency / collision-energy analysis.

---

# 5. A centered weighted additive-cut discrepancy exactly measures the sharp-constant error

This section uses one already-shared P07-B identity and then returns to a structural primal target.

Let `D` now denote the complement optimizer, let `s=theta(bar G)=p/t`, and normalize the two optimal spectra by
\[
q=h/t,\qquad r=g/s.
\]
P07-B proved
\[
q*r=\mathbf1,
\qquad q_0=r_0=1,
\qquad q_jr_j=0\ (j\ne0).
\tag{5.1}
\]
Let `H,K` be their disjoint nontrivial full spectral supports, and define
\[
a=q\mathbf1_H,
\qquad b=r\mathbf1_K.
\]
Then
\[
\sum_H a=s-1,
\qquad
\sum_K b=t-1.
\tag{5.2}
\]
For `d\ne0`, expanding `(delta_0+a)*(delta_0+b)=1` gives
\[
(a*b)(d)=1-a_d-b_d.
\tag{5.3}
\]
Put
\[
m=|H|=|E|,
\qquad
\alpha=\frac{m}{p-1},
\]
and define the **weighted additive cut discrepancy**
\[
\boxed{
\mathfrak D
:=
\sum_{x\in H}\sum_{y\in K}
q_xr_y\left(\mathbf1_H(x+y)-\alpha\right).
}
\tag{5.4}
\]

## Theorem P07-A.19 — exact discrepancy identity

For every prime-order circulant graph,
\[
\boxed{
\mathfrak D
=\alpha(t-1)-(1-\alpha)(s-1),
\qquad s=\frac pt.
}
\tag{5.5}
\]
Equivalently, with
\[
\Delta:=\mathfrak D+2\alpha-1,
\]
`theta(G)=t` is recovered exactly from
\[
\boxed{
\alpha t^2-\Delta t-(1-\alpha)p=0,
}
\tag{5.6}
\]
so
\[
\boxed{
t=
\frac{\Delta+\sqrt{\Delta^2+4\alpha(1-\alpha)p}}{2\alpha}.
}
\tag{5.7}
\]

### Proof

Summing (5.3) over `d\in H` gives
\[
\sum_{d\in H}(a*b)(d)
=m-\sum_Ha=m-(s-1).
\]
The total cross mass is `(s-1)(t-1)`. Therefore (5.4) equals
\[
m-(s-1)-\alpha(s-1)(t-1).
\]
Use `m=alpha(p-1)` and `st=p` to simplify this to (5.5). Rearranging (5.5) gives (5.6), and the positive quadratic root is (5.7). ∎

### Exactly balanced masks

If `alpha=1/2` (possible in the prime source when the pair count is exactly balanced), then
\[
\boxed{
\mathfrak D=\frac12\left(t-\frac pt\right),
\qquad
t=\mathfrak D+\sqrt{p+\mathfrak D^2}.
}
\tag{5.8}
\]
Thus the sharp constant is equivalent to the weighted additive cut being pseudorandom at scale `o(sqrt(p))`.

### Complement antisymmetry and centering

Complementation swaps
\[
(E,H,q,t,\alpha)\leftrightarrow(A,K,r,s,1-\alpha).
\]
Equation (5.5) therefore gives
\[
\boxed{\mathfrak D(\bar G)=-\mathfrak D(G).}
\tag{5.9}
\]
The fair random-circulant source law is invariant under complementation, hence
\[
\boxed{\mathbb E\,\mathfrak D=0}
\tag{5.10}
\]
for every prime `p` (no independence between the optimizer and the mask is asserted).

This centering is the main reason (5.4) is a potentially useful quantity: an upper-tail problem for theta has become concentration of a canonical mean-zero additive discrepancy of the **unique** optimizer.

---

# 6. Exact variance target sufficient for the prime sharp constant

Let the source pair count be `e~Bin((p-1)/2,1/2)`, so
\[
\alpha=\frac{e}{(p-1)/2}
=\frac12+O_P(p^{-1/2}).
\tag{6.1}
\]
Define the zero-discrepancy baseline
\[
t_0(\alpha)=\sqrt{\frac{1-\alpha}{\alpha}p}.
\tag{6.2}
\]
From (5.6), the increasing function
\[
F_\alpha(t)=\alpha t-(1-\alpha)p/t
\]
has derivative at least `alpha`. On the event `alpha in [1/4,3/4]`,
\[
|t-t_0(\alpha)|
\le4|\Delta|
\le4|\mathfrak D|+4|2\alpha-1|.
\tag{6.3}
\]
Also on this event
\[
|t_0(\alpha)-\sqrt p|
\le C\sqrt p\,|\alpha-1/2|
\tag{6.4}
\]
for an absolute constant `C`. The complement pair-count tail outside `[1/4,3/4]` is exponentially small, while `1<=t<=p`.

Therefore
\[
\boxed{
\mathbb E|\mathfrak D|=o(\sqrt p)
\quad\Longrightarrow\quad
\mathbb E\vartheta(G_p)=(1+o(1))\sqrt p.
}
\tag{6.5}
\]
In particular the stronger, clean second-moment target
\[
\boxed{
\mathbb E\mathfrak D^2=o(p)
}
\tag{6.6}
\]
is sufficient for the sharp expectation asymptotic on prime orders.

For exactly balanced masks, complementation preserves the conditioning class and makes `mathfrak D` conditionally symmetric. Then (5.8) yields the sharper identity
\[
\mathbb E[t\mid\alpha=1/2]
=
\mathbb E\bigl[\sqrt{p+\mathfrak D^2}\mid\alpha=1/2\bigr],
\tag{6.7}
\]
and hence
\[
0\le
\mathbb E[t\mid\alpha=1/2]-\sqrt p
\le
\frac{\mathbb E[\mathfrak D^2\mid\alpha=1/2]}{2\sqrt p}.
\tag{6.8}
\]

Similarly, an `O(sqrt(p))` first-moment bound for `|mathfrak D|` would already imply `E theta(G_p)=O(sqrt(p))` on prime orders and remove the iterated-log loss there.

These are **reductions**, not proved concentration bounds. The source metric therefore does not move.

---

# 7. What this run does and does not resolve

**Proved partial:**

1. Prime cyclically averaged theta optimizer is unique.
2. Exact positive-cosine-basis formula (3.3), with an explicit PSD feasible certificate for every positive basis.
3. Exact flat-negative-level probability-measure formulation (4.2).
4. Exact additive-discrepancy identity (5.5)-(5.7), complement antisymmetry, and source centering.
5. `E mathfrak D^2=o(p)` is a precise prime-order sufficient condition for the sharp expectation constant.

**Not proved:**

- no arbitrary-`n` improvement of `C sqrt(n log log n)`;
- no concentration estimate for `mathfrak D` yet;
- no claim that the optimizer support is uniformly random, independent of `E`, or Haar-like;
- no extension of Chebotarev/full-spark steps from prime to general odd composite `n`;
- no worldwide novelty claim for generic inverse-minor or projected-simplex mechanisms.

A quick deterministic Parseval/Cauchy attack on the flat-level measure only reproduces coarse energy constraints and does not force `rho_t<=(1+o(1))/sqrt(p)`. The missing ingredient is genuinely **positivity-selected random-basis geometry** or **concentration of the endogenous weighted additive cut**.

---

# 8. Next concrete P07-A attack

Stay primal/structural and do not duplicate P07-B's exceptional-frequency work.

1. Condition on the edge-pair count `e`. Use uniqueness/equivariance to study the positive-basis selector `H^+(E)` as a canonical random basis of the row-subsampled cosine system. The first target is a variance estimate for the centered quantity `mathfrak D`, not a generic RIP theorem.
2. Try an exchange/Efron-Stein argument under one pair swap in the fixed-size slice. The useful statement would be a source-valid bound on the **change of the unique positive basis certificate** under a row swap; if this change is `O(1)` in the right averaged norm, (6.6) becomes plausible.
3. In parallel, use (3.5) to seek anti-concentration for the bordered-minor ratio **conditioned on positivity**. Volume-sampling averages from the earlier P07-A work give the correct `p^{-1/2}` coordinate scale but do not control the positivity selection; the new uniqueness theorem tells us exactly which selected basis must be controlled.
4. Keep the all-odd-`n` endpoint visible: any prime proof must later replace Chebotarev by a decomposition handling composite Fourier minors rather than being reported as full-source closure.

No checker was manufactured in this run because the new claims are theorem-sized identities with written proofs, and no finite numerical experiment is being promoted to an arbitrary-size theorem.