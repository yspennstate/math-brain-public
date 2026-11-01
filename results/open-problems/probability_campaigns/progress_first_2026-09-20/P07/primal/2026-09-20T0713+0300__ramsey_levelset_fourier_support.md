Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime does not expose authenticated completed-run model/effort telemetry, so I do not claim otherwise.

# P07-A — a random-Cayley Ramsey barrier forces source-scale positive witnesses to be Fourier-dense

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `da9965ccf624d8f0530dd38ce47063abedfb54ee`  
**Previous own report:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0603+0300__reciprocal_dispersion_support_entropy.md`, blob `4b41c2dbe09cf54cc43635fda9b52c52c3ef5045`.  
**Complementary checkpoint read:** P07-B `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0610+0300__projected_hinge_directional_margin.md`, blob `0becacf6c58d389eb6ecee6c98b48824fe1d8d95`. P07-B continues to own projected-hinge / Fourier-dual exceptional-frequency control; the argument below is primal positive-definite geometry and does not duplicate it.  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227.  
**Exact endpoint:** for the source dense random circulant model,
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]

The checked current source still states this conjecture, and the primary paper still gives
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
Accordingly the frozen full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No arbitrary-`n` theta upper bound is improved in this run. The progress is instead a new source-valid theorem: **with high probability, every positive primal witness whose value is already on the `sqrt(n)` scale must use at least `Omega(sqrt(n log n))` nonzero conjugate Fourier pairs.** This improves the preceding deterministic `Omega(sqrt n)` support barrier by a `sqrt(log n)` factor and rules out the entire Fejer-scale sparse-support mechanism simultaneously, not witness by witness.

The archived SRG69 line remains **OPEN / PARTIAL** under its historical root and is untouched.

## 1. Source normalization and the positive-definite coefficient sequence

Let `n` be odd. In the source frequency-domain primal LP, write `h=ny`, so
\[
h(j)\ge0,\qquad \frac1n\sum_j h(j)=1,
\]
and define the unnormalized-characteristic Fourier coefficients
\[
c_k:=\frac1n\sum_{j\in\mathbb Z_n}h(j)e^{-2\pi i kj/n}.
\tag{1.1}
\]
Then `c_0=1`, and source feasibility says
\[
c_k=0\qquad(k\in E),
\tag{1.2}
\]
where `E` is the random symmetric edge-difference set. Because source primal vectors satisfy `h(j)=h(-j)`, every `c_k` is real and `c_k=c_{-k}`. Fourier inversion at zero gives
\[
\boxed{h(0)=\sum_{k\in\mathbb Z_n}c_k.}
\tag{1.3}
\]
The source objective is `h(0)=theta(G_E)` for an optimizer.

Most importantly, `c` is positive definite. Indeed for arbitrary complex numbers `a_1,...,a_m` and frequencies `q_1,...,q_m`,
\[
\sum_{u,v}a_u\overline{a_v}c_{q_u-q_v}
=
\frac1n\sum_jh(j)\left|\sum_u a_u e^{-2\pi i q_uj/n}\right|^2\ge0.
\tag{1.4}
\]
Also `|c_k|<=1` from the `2x2` principal minors (equivalently because `c_k` is a characteristic function of the probability measure `h/n`).

Let
\[
A:=(\mathbb Z_n\setminus\{0\})\setminus E.
\tag{1.5}
\]
Thus every nonzero Fourier coefficient of a feasible witness lies in `A`. Since each inverse pair is independently in `E` with probability `1/2`, `A` has exactly the same law as the generating set of the uniform random undirected Cayley graph on `Z_n`.

This identifies the source positive witness with a normalized positive-definite function whose nonzero support must live inside a random Cayley connection set. The positive-definite/Turan language is classical; the level-set argument below is the new use of it in this track. External novelty is **UNVERIFIED**.

---

# 2. Deterministic level-set lemma: large Fourier coefficients cannot contain an independent `r`-set

Let `H_A=Cay(Z_n,A)`. Fix any source-feasible `h`, and let `s(h)` be the number of nonzero conjugate Fourier pairs of `c`, so there are exactly `2s(h)` nonzero coefficients away from `0` because `n` is odd.

For an integer `r>=2`, define the high-coefficient set
\[
P_r:=\{k\ne0:c_k>r^{-1/2}\}.
\tag{2.1}
\]

## Theorem P07-A.11 — positive-definite Ramsey level-set bound

If `omega(H_A)<=K`, then
\[
\boxed{|P_r|<R(K+1,r)\le {K+r-1\choose r-1}.}
\tag{2.2}
\]
Consequently, if `t=h(0)`, then
\[
\boxed{
t-1
\le \frac{2s(h)}{\sqrt r}
+\left(1-\frac1{\sqrt r}\right)(R(K+1,r)-1).
}
\tag{2.3}
\]

### Proof

Suppose, toward contradiction, that `P_r` contains an independent set
\[
\Lambda=\{q_1,\dots,q_r\}
\]
in the Cayley graph `H_A`. For `u!=v`, independence means
\[
q_u-q_v\notin A.
\]
Because every nonzero coefficient of `c` is supported inside `A`,
\[
c_{q_u-q_v}=0\qquad(u\ne v).
\tag{2.4}
\]
Apply positive definiteness (1.4) to the frequency set `{0,q_1,...,q_r}`. Its Gram matrix has the block form
\[
\begin{pmatrix}
1&a^T\\
a&I_r
\end{pmatrix}\succeq0,
\qquad
a=(c_{q_1},\ldots,c_{q_r})^T.
\tag{2.5}
\]
The Schur complement of `I_r` yields
\[
\|a\|_2^2\le1.
\tag{2.6}
\]
But every `q_i in P_r` has `c_{q_i}>1/sqrt(r)`, so `||a||_2^2>1`, contradiction. Hence
\[
\alpha(H_A[P_r])\le r-1.
\tag{2.7}
\]
The induced graph also has clique number at most `K`. By the definition of the Ramsey number, this forces
\[
|P_r|<R(K+1,r).
\]
The standard Ramsey recurrence gives
\[
R(K+1,r)\le {K+r-1\choose r-1},
\]
proving (2.2).

Finally, use Fourier inversion (1.3). Since `c_k<=1` everywhere, and every nonzero coefficient outside `P_r` is at most `1/sqrt(r)`,
\[
\begin{aligned}
t-1
&=\sum_{k\ne0}c_k\\
&\le |P_r|+\frac{2s(h)-|P_r|}{\sqrt r}\\
&=\frac{2s(h)}{\sqrt r}
+\left(1-\frac1{\sqrt r}\right)|P_r|,
\end{aligned}
\]
and (2.3) follows from (2.2). Negative coefficients only make this upper bound stronger. ∎

### Geometric interpretation

The key step is not a union bound over witnesses. It is simultaneous geometry. A set of frequencies whose pairwise differences are forbidden gives an orthonormal family in `L^2(h/n)`. The atom at the origin forces the vector of correlations with the constant frequency to have squared norm at most one. Hence coefficients above `1/sqrt(r)` cannot occupy an independent `r`-set in the random Cayley graph.

For `r=2`, this says the coefficients larger than `1/sqrt(2)` form a clique. The general `r` version is substantially stronger because it can be combined with the global Ramsey property of the random Cayley mask.

---

# 3. Random-circulant consequence: a `sqrt(n)`-height witness has `Omega(sqrt(n log n))` Fourier-pair support

Green proved that for the uniform random Cayley graph on `Z_n`,
\[
\omega(H_A)=O(\log n)
\tag{3.1}
\]
with high probability; for prime `n`, Green--Morris sharpen this to `(2+o(1))log_2 n`. The 2025 random-circulant theta paper itself cites this `O(log n)` clique bound as current input on the same dense model. The random-Cayley model matches (1.5): inverse pairs are selected independently with probability `1/2`.

Let `C_0` be an absolute constant such that the high-probability event
\[
\mathcal R_n:=\{\omega(H_A)\le C_0\log n\}
\tag{3.2}
\]
holds. Choose a fixed `delta>0` small enough that
\[
\delta\log\!\left(\frac{e(C_0+\delta)}{\delta}\right)<\frac13,
\tag{3.3}
\]
and put
\[
r=\lfloor\delta\log n\rfloor.
\tag{3.4}
\]
On `R_n`, the elementary binomial estimate gives
\[
\begin{aligned}
R(C_0\log n+1,r)
&\le {C_0\log n+r\choose r}\\
&\le\left(\frac{e(C_0\log n+r)}r\right)^r\\
&\le n^{1/3+o(1)}.
\end{aligned}
\tag{3.5}
\]
Insert this in (2.3).

## Corollary P07-A.12 — source-scale Fourier-density barrier

For every fixed `c>0`, with probability `1-o(1)` over the exact dense random circulant source mask, **simultaneously for every feasible positive primal witness** satisfying
\[
h(0)\ge c\sqrt n,
\tag{3.6}
\]
its number `s(h)` of nonzero conjugate Fourier pairs obeys
\[
\boxed{
s(h)\ge
\left(\frac{c\sqrt\delta}{2}+o(1)\right)\sqrt{n\log n}.
}
\tag{3.7}
\]
In particular,
\[
\boxed{s(h)/\sqrt n\to\infty}
\tag{3.8}
\]
uniformly over all source-scale witnesses on the high-probability event.

### Proof

On `R_n`, (2.3), (3.4), and (3.5) imply
\[
c\sqrt n-1
\le \frac{2s(h)}{\sqrt{\delta\log n}}+n^{1/3+o(1)}.
\]
Because `n^{1/3+o(1)}=o(sqrt(n))`, rearrangement gives (3.7). ∎

This is an actual source-random theorem, not a fixed-witness estimate and not a finite numerical experiment.

---

# 4. What this improves, and what it does not

The previous P07-A support lemma used only `|c_k|<=1` and gave
\[
s(h)\ge\frac{h(0)-1}{2}.
\tag{4.1}
\]
At `h(0)=Theta(sqrt n)`, that was only `Omega(sqrt n)`, and the Fejer kernel shows that deterministic positivity alone really can live at that scale.

Corollary P07-A.12 proves that the **random source mask forbids every such low-support mechanism simultaneously**: a source-feasible `Theta(sqrt n)` spike needs an extra `sqrt(log n)` factor of Fourier-pair support. Thus the Fejer family is not merely unlikely one dilation at a time; on the standard high-probability random-Cayley Ramsey event, *no* witness of that support order can attain the source scale.

This cleanly changes the remaining primal picture:

- sparse positive Fourier certificates of size `O(sqrt n)` are eliminated with high probability;
- any obstruction to the conjectured constant must come from a **Fourier-dense, individually small-coefficient positive-definite completion**;
- the unresolved regime is therefore qualitatively different from the sparse signed-kernel vectors responsible for RIP lower bounds.

The theorem does **not** yet imply `theta(G)<= (1+o(1))sqrt n`. A witness can have `Omega(sqrt(n log n))`, or even linear, Fourier support while each coefficient is small; the sum in (1.3) can still in principle be of order `sqrt n`. So `alpha_LL` honestly remains unchanged.

There is also a method barrier visible here. The proof uses only independent subsets of coefficient level sets plus a Ramsey clique bound. Pushing this mechanism alone to tiny coefficient thresholds loses too much through Ramsey numbers. The next proof must use more of the full positive-definite matrix than the fact that selected off-diagonal entries vanish.

---

# 5. Exact next attack: dense-small-coefficient positive-definite geometry

The next P07-A run should stay on the primal side and attack the regime isolated above. Three concrete routes are now better targeted than another support count:

1. **Threshold cascade from `3x3` PSD minors.** If `c_a,c_b>=u`, positivity of
   \[
   \begin{pmatrix}1&c_a&c_b\\c_a&1&c_{a-b}\\c_b&c_{a-b}&1\end{pmatrix}
   \]
   forces
   \[
   c_{a-b}\ge c_ac_b-\sqrt{(1-c_a^2)(1-c_b^2)}.
   \]
   In particular, for `u>1/sqrt(2)`, `P_u-P_u` is forced into a lower positive level set. Iterating these level-set growth constraints may control the *whole* coefficient distribution, not just support.

2. **Layer-cake objective.** Since
   \[
   h(0)-1\le\int_0^1 |\{k\ne0:c_k>u\}|\,du,
   \]
   seek a source-specific multiscale bound on positive-definite level-set sizes strong enough to integrate to `(1+o(1))sqrt n`. The new theorem supplies the high-`u` end exactly; the hard region is `u=Theta(n^{-1/2})`.

3. **Cone comparison in the dense regime.** Translate the small-coefficient completion back to the exact Householder/trimmed-simplex normal form from the earlier P07-A reports and compare only this dense positive-definite stratum with the Haar benchmark. This remains complementary to P07-B's projected-hinge dual iteration.

The most promising immediate route is (1)+(2): derive a quantitative additive-growth recursion for coefficient level sets from PSD minors and see whether random-Cayley color counting can convert that recursion into an integrable bound for the reciprocal tail formula already proved in P07-A.

---

# 6. Prior-art / source notes

- Randomstrasse101 arXiv:2603.29571, Conjecture 18 (current checked HTML dated 24 Aug 2026) still asks for `E theta=(1+o(1))sqrt(n)`.
- Bandeira et al., arXiv:2502.16227, Theorem 1 still gives `sqrt(n) <= E theta <= C sqrt(n log log n)` and explicitly notes that their RIP upper-bound route discards primal positivity.
- Green, *Counting sets with small sumset, and the clique number of random Cayley graphs*, Combinatorica 25 (2005), gives the `O(log n)` high-probability clique bound for uniform random Cayley graphs on `Z_n`; Green--Morris sharpen the prime case to `(2+o(1))log_2 n`.
- Conlon--Fox--Pham--Yepremyan, arXiv:2412.21194, independently provides the more general `O(log N log log N)` random-Cayley clique theorem and explicitly defines the same independent inverse-pair sampling model.

The positive-definite packing/Turan viewpoint is classical. I did not locate this particular **coefficient-level-set + random-Cayley Ramsey amplification** in the bounded search performed for this run; that is not a worldwide novelty certificate.

---

# 7. Ledger delta

```yaml
native_id: 6aa7b46f70a8819184095c277974c256
role: P07-A
source: Randomstrasse101 Conjecture 18 / arXiv:2502.16227
status: OPEN / PROVED PARTIAL
metric: alpha_LL
before: 1/2
after: 1/2
new_exact_results:
  - "positive-definite level-set theorem: P_r={k:c_k>1/sqrt(r)} has independence number <=r-1 inside the available Cayley graph"
  - "deterministic Ramsey bound |P_r|<R(omega+1,r) and objective inequality t-1 <= 2s/sqrt(r)+(1-1/sqrt(r))(R-1)"
  - "using the O(log n) random-cyclic-Cayley clique theorem, every feasible witness with h(0)>=c sqrt(n) has s(h)=Omega_c(sqrt(n log n)) nonzero conjugate Fourier pairs with high probability"
  - "therefore all O(sqrt n)-Fourier-support positive spike mechanisms, including Fejer-scale mechanisms, are simultaneously excluded on a high-probability source event"
remaining_gap: "control the dense-small-coefficient positive-definite regime strongly enough to make the exact reciprocal upper-tail integral o(1)"
next_attack: "PSD threshold-cascade + layer-cake level-set integration; compare dense stratum with Householder/trimmed-simplex Haar benchmark"
P07B_boundary: "do not duplicate projected-hinge / exceptional-frequency Fourier-dual descent"
SRG69: "preserved OPEN/PARTIAL; historical root untouched"
```
