Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but authenticated completed-run model/reasoning telemetry is unavailable, so I do not claim otherwise.

# P07-A — adjacent-mask one-harmonic factorization and a fourth-collision criterion

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `2dcab07a1887511f981ad79670dcbaa8e8547d43`  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1047+0300__reciprocal_variance_orbit_influence.md`, creation commit `d5118c589f7a6e1a205a3b79909582af88ea0630`.  
**Complementary checkpoint consulted:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1124+0300__second_order_clipping_sparse_exception_patch.md`. P07-B owns the Fourier-dual Gibbs / exceptional-frequency / interpolation route. The present report stays on primal adjacent-mask sensitivity and optimizer self-convolution.

**Outside target:** *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18; primary partial-result paper A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source model:** odd `n`, with the `(n-1)/2` conjugate nonzero difference pairs selected independently with probability `1/2`.  
**Endpoint:**
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]
A bounded source/current check on 20 September 2026 again found the primary paper describing exact asymptotics as open and retaining the square-root scale up to the iterated-log loss. This is bounded evidence, not a worldwide novelty certificate.

The fixed full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No arbitrary-`n` improvement of the published headline bound is claimed here. Publication novelty of the new identities below is **UNVERIFIED**.

---

## 0. Preserved predecessor handoff: SRG69 is still OPEN / PARTIAL

The reassigned predecessor remains archived under

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/`

with frozen `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve its exact no-Cayley result, rooted `L/B/C` feasibility system, centered spectral transfer, endpoint/cycle filters, block-moment and Gram reductions, low-rank residual work, and star-complement handoff. Nothing in this report edits that root or represents SRG69 as solved.

---

# 1. Source-normalized primal notation

Let
\[
M=\{1,\ldots,(n-1)/2\}
\]
index conjugate difference pairs. For `D\subset M`, let `G_D` be the corresponding undirected circulant graph and put
\[
T_D:=\vartheta(G_D),\qquad X_D:=T_D/\sqrt n.
\]
Choose a cyclically averaged optimal theta primal for `G_D`, represented by an even real positive-definite function
\[
f_D:\mathbb Z_n\to\mathbb R
\]
with
\[
f_D(0)=1,\qquad f_D(\pm a)=0\quad(a\in D),
\qquad \sum_{x\in\mathbb Z_n}f_D(x)=T_D.
\tag{1.1}
\]
Write its spectral probability as
\[
\mu_D(k):=\frac{\widehat f_D(k)}n.
\tag{1.2}
\]
Then
\[
\mu_D\ge0,\qquad \sum_k\mu_D(k)=1,
\qquad \mu_D(0)=T_D/n.
\tag{1.3}
\]
For composite `n`, if the optimum is nonunique, fix any deterministic optimal selector; every identity below holds for the selected optima. On prime order, the earlier P07-A work proved uniqueness of the cyclically averaged optimum.

Adding an edge-pair only adds primal zero constraints, hence
\[
D\subset D'\implies T_D\ge T_{D'}.
\tag{1.4}
\]
Also every circulant graph is vertex transitive, so
\[
\boxed{T_DT_{D^c}=n.}
\tag{1.5}
\]

---

# 2. New exact theorem: every adjacent mask produces a one-harmonic spectral convolution

Fix `H\subset M` and `a\notin H`. Put
\[
D:=H\cup\{a\},\qquad K:=M\setminus D.
\tag{2.1}
\]
Thus `K=D^c`, while `H` and `K` partition every pair coordinate except `a`. Define
\[
u:=f_H(a),\qquad v:=f_K(a).
\tag{2.2}
\]

## Theorem P07-A.23 — adjacent-mask one-harmonic factorization

For every odd `n`,
\[
\boxed{
(\mu_H*\mu_K)(s)
=\frac{1+2uv\cos(2\pi as/n)}n
\qquad(s\in\mathbb Z_n).
}
\tag{2.3}
\]
Consequently,
\[
\boxed{
\frac{T_H}{T_D}-1
=2uv-n\sum_{j\ne0}\mu_H(j)\mu_K(-j).
}
\tag{2.4}
\]
In particular,
\[
\boxed{uv\ge0,\qquad
0\le \frac{T_H}{T_D}-1\le2uv.}
\tag{2.5}
\]

### Proof

The pointwise product `g=f_Hf_K` is positive definite because its Fourier transform is the convolution of two nonnegative spectra. For every nonzero pair `b\ne a`, exactly one of `H,K` contains `b`; hence one of `f_H(\pm b),f_K(\pm b)` is zero. Therefore
\[
g(0)=1,\qquad g(\pm a)=uv,
\qquad g(x)=0\quad(x\notin\{0,\pm a\}).
\tag{2.6}
\]
With the normalization (1.2), the spectral probability of a pointwise product is exactly the cyclic convolution of the spectral probabilities. Fourier transforming (2.6) gives (2.3).

At `s=0`,
\[
\frac{1+2uv}{n}
=\sum_j\mu_H(j)\mu_K(-j).
\]
The `j=0` term equals
\[
\frac{T_HT_K}{n^2}
=\frac{T_H}{nT_D}
\]
by `K=D^c` and (1.5). Multiplying by `n` and separating `j=0` proves (2.4). Since `T_H\ge T_D` and every spectral summand is nonnegative, (2.5) follows. ∎

### Exact convolution-defect form

Let `U_n` denote uniform measure on `Z_n`. Orthogonality of the cosine gives
\[
\boxed{
n\|\mu_H*\mu_K-U_n\|_2^2=2u^2v^2.}
\tag{2.7}
\]
Thus a one-generator sensitivity is controlled by a single additive-convolution defect of the two adjacent-mask optimizers; no all-sign Fourier RIP statement is involved.

---

# 3. Deterministic one-generator Lipschitz bound

Let
\[
\ell(a):=\frac n{\gcd(a,n)}
\]
be the additive order of `a`. Since `n` is odd, `ell(a)` is odd and at least `3`.

The left side of (2.3) is nonnegative for every `s`. The minimum of
\[
\cos(2\pi as/n)
\]
over `s` is `-cos(pi/ell(a))`. Since `uv>=0`, (2.3) therefore implies
\[
\boxed{
0\le uv\le \frac1{2\cos(\pi/\ell(a))}.}
\tag{3.1}
\]
Combining with (2.5) gives the source-independent adjacent-mask bound
\[
\boxed{
1\le\frac{T_H}{T_{H\cup\{a\}}}
\le1+\sec\!\left(\frac\pi{\ell(a)}\right)
\le3.}
\tag{3.2}
\]
For prime `p`, every nonzero `a` has order `p`, so
\[
\boxed{
\frac{T_H}{T_{H\cup\{a\}}}
\le1+\sec(\pi/p)=2+O(p^{-2}).}
\tag{3.3}
\]
This is a genuine deterministic theorem for every source mask, but it is not alone strong enough to prove the expectation asymptotic.

---

# 4. Prime equality rigidity: maximal one-bit sensitivity forces arithmetic-progressive spectral supports

Now let `n=p` be an odd prime and suppose both `H` and `K` in (2.1) are nonempty. Let
\[
A=\operatorname{supp}\mu_H,
\qquad B=\operatorname{supp}\mu_K.
\]
The earlier prime P07-A exact-support theorem gives
\[
|A|=2|H|+1,
\qquad |B|=2|K|+1,
\qquad |A|+|B|=p-1,
\tag{4.1}
\]
and both spectral measures are strictly positive on their supports.

If equality holds in (3.1), then the right side of (2.3) vanishes at exactly two frequencies and is positive at all other frequencies. Since the convolution is nonnegative,
\[
\operatorname{supp}(\mu_H*\mu_K)=A+B
\]
has size `p-2`. Cauchy-Davenport gives
\[
|A+B|\ge |A|+|B|-1=p-2,
\]
so this is equality in Cauchy-Davenport. Vosper's theorem then yields:

\[
\boxed{
uv=\frac1{2\cos(\pi/p)}
\Longrightarrow
A\text{ and }B\text{ are arithmetic progressions with a common difference.}
}
\tag{4.2}
\]

If the **theta deletion ratio itself** reaches the upper bound in (3.3), then equality must also hold in (2.5), so the nonzero overlap term in (2.4) vanishes. Hence additionally
\[
\boxed{A\cap(-B)=\{0\}.}
\tag{4.3}
\]
This is a restricted prime-order rigidity theorem, not a probability estimate. It identifies the exact additive-combinatorial structure required by a maximally sensitive generator deletion.

---

# 5. Fourth-moment control of log-theta influences

Define the one-sided log-deletion energy
\[
J_{\log}(D)
:=\sum_{a\in D}
[\log T_{D\setminus\{a\}}-\log T_D]^2.
\tag{5.1}
\]
Also define the primal fourth-mass on currently available pair coordinates
\[
\boxed{
\Lambda_4(D):=\sum_{a\notin D} f_D(a)^4.}
\tag{5.2}
\]

## Theorem P07-A.24 — fourth-moment log-influence bound

Under the exact fair source mask,
\[
\boxed{
\mathbb E J_{\log}(D)\le4\,\mathbb E\Lambda_4(D),
}
\tag{5.3}
\]
and therefore
\[
\boxed{
\operatorname{Var}(\log T_D)
\le2\,\mathbb E\Lambda_4(D).
}
\tag{5.4}
\]
Since complement symmetry makes
\[
\log(T_D/\sqrt n)\stackrel d=-\log(T_D/\sqrt n),
\]
its mean is zero, so
\[
\boxed{
\mathbb E\left[\log\frac{T_D}{\sqrt n}\right]^2
\le2\,\mathbb E\Lambda_4(D).
}
\tag{5.5}
\]

### Proof

Reindex a deletion edge by writing `D=H\cup{a}` with `a\notin H`, and use `K=M\setminus(H\cup{a})` as in Section 2. Put `r=T_H/T_D`. By (2.5),
\[
0\le\log r\le r-1\le2uv,
\]
so
\[
(\log r)^2\le4u^2v^2\le2(u^4+v^4).
\tag{5.6}
\]
Averaging over all fair `H` and all `a\notin H`, the involution
\[
(H,a)\longleftrightarrow(K,a)
\]
preserves the counting measure and swaps `u,v`. Thus the two fourth-power contributions are equal, giving (5.3).

For a function of independent fair bits, Efron-Stein gives one quarter of the total squared flip energy. The one-sided deletion energy counts each hypercube edge on exactly one endpoint, hence
\[
\operatorname{Var}(\log T_D)
\le\frac12\mathbb E J_{\log}(D),
\]
which with (5.3) proves (5.4). Equation (5.5) follows from `T_DT_{D^c}=n` and fair complement invariance. ∎

The condition `E Lambda_4=o(1)` would therefore force `T_D/sqrt(n)->1` in probability. By itself this is **not yet** the source expectation theorem because uniform integrability must still be controlled. The next section removes that gap.

---

# 6. New source-exact expectation bridge: weighted fourth collision directly controls the conjectural gap

Put
\[
X_D:=\frac{T_D}{\sqrt n},
\qquad
Z_D:=\sqrt{X_D}-\frac1{\sqrt{X_D}}.
\tag{6.1}
\]
Complementation sends `X` to `X^{-1}` and hence `Z` to `-Z`. Under the fair source law,
\[
\mathbb EZ=0
\]
and exactly
\[
\mathbb EZ^2
=\mathbb E(X+X^{-1}-2)
=2(\mathbb EX-1).
\tag{6.2}
\]

For an adjacent edge `D=H\cup{a}`, let
\[
r=T_H/T_D,\qquad x=X_D,
\qquad x'=X_{H^c}=\frac1{rx}.
\]
A direct algebraic identity gives
\[
Z_H-Z_D
=(\sqrt r-1)(\sqrt x+\sqrt{x'}).
\tag{6.3}
\]
By (2.5),
\[
\sqrt r-1
=\frac{r-1}{\sqrt r+1}
\le uv,
\]
and therefore
\[
(Z_H-Z_D)^2
\le2u^2v^2(x+x').
\tag{6.4}
\]

Applying Efron-Stein to `Z`, using (6.2), reindexing deletion edges, applying `u^2v^2<=(u^4+v^4)/2`, and again using the involution `(H,a)<->(K,a)`, yields
\[
\mathbb EX-1
\le\frac12\,2^{-|M|}
\sum_H\sum_{a\notin H}
f_H(a)^4\,[X_{H\cup\{a\}}+X_{H^c}].
\tag{6.5}
\]
Finally, adding an edge can only decrease theta and `X_{H^c}=X_H^{-1}`. Hence
\[
\boxed{
0\le
\frac{\mathbb E T_D}{\sqrt n}-1
\le
\frac12\,
\mathbb E\left[
\left(X_D+X_D^{-1}\right)\Lambda_4(D)
\right].
}
\tag{6.6}
\]
This is already an expectation-level sufficient condition with no separate uniform-integrability step.

---

# 7. Spectral self-convolution form: the remaining obstruction is weighted additive energy of the actual optimizer

Because `f_D` is even, equals `1` at zero, and vanishes on the selected edge pairs,
\[
\sum_{x\in\mathbb Z_n} f_D(x)^4
=1+2\Lambda_4(D).
\tag{7.1}
\]
By Parseval and (1.2),
\[
\sum_x f_D(x)^4
=n\|\mu_D*\mu_D\|_2^2.
\tag{7.2}
\]
Therefore
\[
\boxed{
\Lambda_4(D)
=\frac{n\|\mu_D*\mu_D\|_2^2-1}{2}
=\frac n2\|\mu_D*\mu_D-U_n\|_2^2.
}
\tag{7.3}
\]
Substitution into (6.6) gives the clean primal criterion
\[
\boxed{
0\le
\frac{\mathbb E\vartheta(G_n)}{\sqrt n}-1
\le
\frac14\,
\mathbb E\left[
\left(X_D+X_D^{-1}\right)
\left(n\|\mu_D*\mu_D\|_2^2-1\right)
\right].
}
\tag{7.4}
\]
Equivalently,
\[
\boxed{
\mathbb E\left[
\left(X_D+X_D^{-1}\right)
\,n\|\mu_D*\mu_D-U_n\|_2^2
\right]=o(1)
\Longrightarrow
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
}
\tag{7.5}
\]

This is distinct from P07-B's `CCEL`, which concerns the **second physical moment** `||f_D||_2^2` / spectral collision energy of one optimizer. The present quantity is the **fourth physical moment**, equivalently the `L^2` additive-energy defect of the optimizer's **spectral self-convolution**, and it arose from exact one-bit primal sensitivity. P07-B may use (7.4) as a handoff if its dual certificates happen to control this defect, but ownership of its Fourier-dual route is unchanged.

---

# 8. What changed, what remains, and next attack

### Proved this run

1. **All odd `n`:** exact adjacent-mask factorization (2.3); two optimal spectra on opposite sides of one missing generator convolve to a one-harmonic perturbation of Haar.
2. **All odd `n`:** exact deletion identity (2.4) and deterministic one-generator factor bound (3.2), at most `3` in general and `2+O(p^-2)` on prime order.
3. **Prime restricted theorem:** equality in the maximal product bound forces the two optimizer spectral supports to be common-difference arithmetic progressions; maximal theta sensitivity additionally forces `A cap (-B)={0}`.
4. **Exact fair source:** log-theta variance is controlled by the primal fourth mass `Lambda_4`.
5. **Exact fair source, expectation level:** the full Conjecture 18 gap is bounded directly by the weighted fourth/additive-energy defect in (7.4). No high-probability/expectation substitution is made.

### Not proved

The key missing estimate is still
\[
\mathbb E\left[
(X_D+X_D^{-1})
\,n\|\mu_D*\mu_D-U_n\|_2^2
\right]=o(1).
\tag{8.1}
\]
So the headline source metric does **not** move. The report is **PROVED PARTIAL**, not a candidate full proof.

### Next primal attack

The next P07-A run should attack (8.1), not introduce another generic reformulation. Two concrete routes are now available:

- **Adjacent-mask additive stability:** quantify how often the exact one-harmonic convolution (2.3) can have non-negligible amplitude without forcing the prime-support arithmetic structure from Section 4 approximately. This is a weighted inverse-additive problem for the *actual optimizers*, not P07-B's exceptional-frequency problem.
- **PSD level-set control of fourth mass:** combine the earlier P07-A positive-definite/Ramsey level-set argument with dyadic physical levels of `|f_D(a)|` to bound `Lambda_4`, rather than merely counting Fourier support. A successful source bound at the weighted `o(1)` scale in (8.1) closes the conjecture directly.

If both pivots fail to improve (8.1), preserve this report as the handoff and rotate according to the progress-first owner directive rather than repeating the same sensitivity reduction.
