Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime does not expose authenticated completed-run model/effort telemetry, so I do not claim otherwise.

# P07-A — prime optimal complementarity forces full available support and paired positive Fourier circuits

**Native role:** `P07-A`, task `6aa7b46f70a8819184095c277974c256`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-write master:** `0832e1c1d0b2617b6645f5addfc506afb0985cf7`  
**Previous own report:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0713+0300__ramsey_levelset_fourier_support.md`, blob `cb7358eb124ebd064dff81da8f181cc6991fe702`.  
**Complementary checkpoint read:** P07-B `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0725+0300__static_moreau_cone_projection.md`, blob `3623ec148eeed786cc94541a41f8a530dccbbe8e`. P07-B owns the Moreau / Fourier-dual exceptional-frequency route; this report stays on the primal optimal-certificate geometry.  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227.  
**Exact endpoint:** for the source dense random circulant model,
\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]

The current checked Randomstrasse source still states Conjecture 18 and records the partial bound
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
The primary arXiv record likewise still describes exact asymptotics as open. These are bounded current-source checks, not a worldwide novelty certificate.

Accordingly the frozen full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No arbitrary-`n` theta upper bound is improved in this run. The new progress is an exact prime-order theorem about **every optimal primal solution**, not merely an extreme solution: optimality for a graph and its complement, together with prime Fourier uncertainty, forces exact ranks, exact physical support, disjoint nontrivial spectral supports, and a pair of complementary strictly-positive Fourier circuits.

This materially strengthens the previous support picture. On prime order, the actual optimizer cannot have `O(sqrt(n))` or even `O(sqrt(n log n))` Fourier-pair support: it uses **every available nonedge pair**, hence linear support in the source random model. The remaining problem is therefore magnitude/sign geometry of a dense optimal circuit, not support entropy.

---

## 0. Concise preservation handoff: SRG69 is still OPEN / PARTIAL

The reassigned predecessor is preserved, not erased and not called solved. Its latest stagnant checkpoint remains

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-13/rotations/SHPECTOROV-ZHAO-2026-SRG69/runs/2026-09-19/2026-09-19T22-46-00Z__report.md`

with blob `fcf42c57f30ced2e5407f70dbee6481ae1bb8278` and frozen metric `R_SRG69=1`, status **OPEN / PARTIAL**. Preserve there the exact no-Cayley theorem, rooted `L/B/C` equivalence, centered spectral transfer, endpoint filters, cycle transfer, block-moment/Gram reductions and low-rank residual route. This P07-A report does not modify that historical root.

---

# 1. Exact prime-order normalization

Let `p` be an odd prime and let `G=Cay(Z_p,E)` be any undirected circulant graph, so
\[
E=-E\subset \mathbb Z_p^\times.
\]
Write
\[
A:=\mathbb Z_p^\times\setminus E,
\]
so `A=-A` is the set of nonedge differences.

Average any theta optimizer over cyclic shifts. In the source time-domain normalization, an optimal primal solution for `G` is a real symmetric circulant PSD matrix
\[
C=\operatorname{Circ}(c),
\]
with
\[
c_0=1,\qquad c_e=0\ (e\in E),
\qquad \sum_{a\in\mathbb Z_p}c_a=t:=\vartheta(G).
\tag{1.1}
\]
Thus
\[
\operatorname{supp}(c)\subseteq\{0\}\cup A.
\tag{1.2}
\]
Let
\[
h:=Fc
\]
for the unnormalized DFT `F_{jk}=omega^{jk}` (the sign convention is immaterial here). Since `C` is PSD, its circulant eigenvalues obey
\[
h_j\ge0.
\tag{1.3}
\]
The trivial eigenvalue is
\[
h_0=\sum_a c_a=t,
\tag{1.4}
\]
and
\[
\sum_jh_j=p c_0=p.
\tag{1.5}
\]
Hence
\[
\operatorname{rank}C=|\operatorname{supp}h|.
\tag{1.6}
\]

Choose likewise an optimal circulant primal solution
\[
D=\operatorname{Circ}(d)
\]
for the complement `bar G`, with
\[
d_0=1,\qquad d_a=0\ (a\in A),
\qquad \sum_ed_e=s:=\vartheta(\bar G),
\tag{1.7}
\]
and eigenvalues
\[
g:=Fd\ge0,\qquad g_0=s,\qquad \sum_jg_j=p.
\tag{1.8}
\]
Because a circulant graph is vertex transitive, Lovasz's identity gives
\[
\boxed{ts=p.}
\tag{1.9}
\]
Randomness is not used anywhere in the structural theorem below.

---

# 2. New theorem: every optimal prime pair satisfies `CD=J` and has complementary spectral support

## Theorem P07-A.13 — optimal complementary-support theorem

With the normalization above, **every** optimal circulant pair `C,D` satisfies
\[
\boxed{C\circ D=I,\qquad CD=J.}
\tag{2.1}
\]
Equivalently, in the physical first-row vectors and Fourier eigenvalues,
\[
\boxed{c\odot d=\delta_0,\qquad c*d=\mathbf1,}
\tag{2.2}
\]
where convolution is cyclic with the normalization consistent with `F`, and
\[
\boxed{h_jg_j=0\quad(j\ne0).}
\tag{2.3}
\]
Thus the nontrivial spectral supports of optimal solutions for `G` and `bar G` are disjoint.

### Proof

For `i\ne j`, the difference `i-j` belongs either to `E` or to `A`.

- If `i-j in E`, then `C_{ij}=0` by primal feasibility for `G`.
- If `i-j in A`, then this is an edge difference of `bar G`, so `D_{ij}=0`.

Both matrices have diagonal entries one. Therefore their entrywise product is exactly
\[
C\circ D=I.
\tag{2.4}
\]
Taking the Frobenius inner product,
\[
\langle C,D\rangle_F=p.
\tag{2.5}
\]
Because `C,D` are real symmetric circulants, the same unitary Fourier basis diagonalizes both, and therefore
\[
\langle C,D\rangle_F
=\operatorname{tr}(CD)
=\sum_{j=0}^{p-1}h_jg_j.
\tag{2.6}
\]
The `j=0` summand is, by (1.4), (1.8), and (1.9),
\[
h_0g_0=ts=p.
\tag{2.7}
\]
All summands in (2.6) are nonnegative by PSD. Since their total is already exhausted by (2.7),
\[
h_jg_j=0\qquad(j\ne0).
\tag{2.8}
\]
The eigenvalues of `CD` are therefore `p` on the constant Fourier mode and zero on every nontrivial mode. These are exactly the eigenvalues of `J`, so
\[
CD=J.
\tag{2.9}
\]
The first-row identities (2.2) are the physical-domain forms of (2.4) and (2.9). ∎

### Why this is more than the usual product identity

The scalar identity `theta(G)theta(bar G)=p` is classical for vertex-transitive graphs. Here the primal support constraints plus nonnegativity upgrade equality of the scalar objectives to **matrix complementary slackness at every nontrivial Fourier mode**. This is the point that makes prime uncertainty exact below.

---

# 3. Prime uncertainty forces exact rank and full physical support

For a nonzero function `f:Z_p->C`, Tao's prime cyclic uncertainty principle (equivalent here to Chebotarev nonsingularity of Fourier minors) gives
\[
|\operatorname{supp}f|+|\operatorname{supp}\widehat f|\ge p+1.
\tag{3.1}
\]
Apply it first to `c`. From (1.2),
\[
|\operatorname{supp}c|\le |A|+1.
\]
Thus
\[
\operatorname{rank}C=|\operatorname{supp}h|
\ge p+1-|\operatorname{supp}c|
\ge p-|A|=|E|+1.
\tag{3.2}
\]
Similarly,
\[
\operatorname{rank}D\ge |A|+1.
\tag{3.3}
\]

But (2.3) says that the two nontrivial spectral supports are disjoint, while both contain the trivial frequency zero. Hence
\[
\operatorname{rank}C+\operatorname{rank}D\le p+1.
\tag{3.4}
\]
The lower bounds sum to
\[
(|E|+1)+(|A|+1)=p+1.
\tag{3.5}
\]
Therefore equality holds everywhere in (3.2)--(3.5).

## Corollary P07-A.14 — exact ranks and exact supports

For every odd prime `p` and every circulant graph on `Z_p`, every optimal circulant primal pair satisfies
\[
\boxed{\operatorname{rank}C=|E|+1,\qquad
\operatorname{rank}D=|A|+1.}
\tag{3.6}
\]
Moreover
\[
\boxed{\operatorname{supp}c=\{0\}\cup A,
\qquad
\operatorname{supp}d=\{0\}\cup E.}
\tag{3.7}
\]
So **every permitted off-diagonal physical coefficient of an optimal solution is nonzero**.

If
\[
H:=\operatorname{supp}h\setminus\{0\},
\qquad
K:=\operatorname{supp}g\setminus\{0\},
\]
then
\[
\boxed{|H|=|E|,\quad |K|=|A|,\quad
H\sqcup K=\mathbb Z_p^\times.}
\tag{3.8}
\]
Because `h,g>=0`, every coordinate in their supports is in fact strictly positive.

This is stronger than the earlier P07-A extreme-point statement. No choice of a sparse optimal extreme point is being made: **all optimal circulant solutions have the same exact rank and full allowed physical support** on prime order.

---

# 4. Every optimum is a pair of complementary strictly-positive Fourier circuits

The edge zero constraints for `C` say
\[
c_e=\frac1p\sum_{j\in\{0\}\cup H}h_j\omega^{-ej}=0
\qquad(e\in E).
\tag{4.1}
\]
Equivalently,
\[
F_{E,\{0\}\cup H}h_{\{0\}\cup H}=0.
\tag{4.2}
\]
This matrix has `|E|` rows and `|E|+1` columns. Every square Fourier minor of prime order is nonsingular, so it has full row rank `|E|`; its kernel is one-dimensional. Since every supported eigenvalue is positive,
\[
\boxed{h_{\{0\}\cup H}>0}
\tag{4.3}
\]
is the unique positive circuit on this support, up to scaling. The trace normalization fixes that scale by
\[
\sum_{j\in\{0\}\cup H}h_j=p,
\tag{4.4}
\]
and the theta objective is the distinguished circuit coordinate
\[
\boxed{\vartheta(G)=h_0.}
\tag{4.5}
\]

The complement simultaneously gives
\[
F_{A,\{0\}\cup K}g_{\{0\}\cup K}=0,
\qquad
g_{\{0\}\cup K}>0,
\qquad
\sum g_j=p,
\qquad
\vartheta(\bar G)=g_0,
\tag{4.6}
\]
where `K=Z_p^times\H`.

## Corollary P07-A.15 — bi-positive complementary-circuit reduction

For prime order, an optimal theta solution determines a partition
\[
\mathbb Z_p^\times=H\sqcup K,
\qquad |H|=|E|,\quad |K|=|A|,
\tag{4.7}
\]
such that **both** rectangular Fourier systems
\[
F_{E,\{0\}\cup H}h=0,
\qquad
F_{A,\{0\}\cup K}g=0
\tag{4.8}
\]
have strictly positive one-dimensional kernel vectors. Conversely, any candidate optimal support must pass this simultaneous positivity test; one-sided circuit positivity is not enough.

This is the most useful form for the next attack. Cramer's rule writes every circuit coordinate as a signed Fourier minor. Jacobi complementary-minor identities then relate the two systems because `E/A` and `H/K` are complementary partitions. The source random problem can therefore be attacked through the probability that a random row partition admits a **matched pair of positive complementary cofactor vectors** with an anomalously large distinguished-coordinate ratio.

External novelty of this exact packaging is **UNVERIFIED**. The ingredients (vertex-transitive theta product, prime Fourier uncertainty, Chebotarev minors) are classical; the value here is their source-specific combination and the simultaneous positivity consequence.

---

# 5. Random-source consequence: optimal prime witnesses have linear Fourier-pair support

Return to the exact dense random circulant source model at prime `p`. There are
\[
m=(p-1)/2
\]
conjugate difference pairs, independently declared edges with probability `1/2`.

The time-domain theta vector `c` is the Fourier-coefficient sequence of the nonnegative frequency-domain witness used in the preceding P07-A reports. Corollary P07-A.14 says that for an **optimizer**, its nonzero conjugate Fourier-pair count is exactly the number of available nonedge pairs:
\[
\boxed{s_{\mathrm{opt}}=|A|/2.}
\tag{5.1}
\]
Thus
\[
s_{\mathrm{opt}}\sim \operatorname{Bin}\left((p-1)/2,1/2\right),
\tag{5.2}
\]
and hence, with high probability,
\[
\boxed{s_{\mathrm{opt}}=p/4+O(\!\sqrt{p\log p})}
\tag{5.3}
\]
(for example by Hoeffding; the weaker `p/4+O_p(sqrt p)` also follows immediately).

This is a qualitative upgrade over the previous Ramsey theorem, which uniformly forced only
\[
\Omega(\sqrt{p\log p})
\]
support for arbitrary source-scale feasible witnesses. At the true optimum on prime order, **support sparsity disappears completely**: all available Fourier pairs are used.

Therefore the iterated-log loss cannot be removed by another support lower bound for prime optimizers. The remaining sharp-constant question is about the **magnitude distribution and simultaneous sign/cofactor geometry** of the dense bi-positive circuit.

---

# 6. Centered orthogonal decomposition and a useful spectral-spread identity

Set
\[
\widetilde C:=C-\frac tpJ,
\qquad
\widetilde D:=D-\frac spJ.
\tag{6.1}
\]
These matrices are PSD on `1^perp`, and (2.1) gives
\[
\boxed{\widetilde C\widetilde D=0.}
\tag{6.2}
\]
Their ranges form orthogonal complementary subspaces of `1^perp` of dimensions `|E|` and `|A|`.

The physical zeros become fixed centered entries:
\[
\widetilde c_e=-\frac tp\quad(e\in E),
\qquad
\widetilde d_a=-\frac sp=-\frac1t\quad(a\in A).
\tag{6.3}
\]
Thus the sharp theta value is equivalently the magnitude of a constant negative level forced on one random half of the coordinates of a PSD circulant matrix whose nontrivial spectral range is complementary to that of the complement optimizer.

There is also an exact spectral-spread decomposition. Since the nontrivial eigenvalues of `C` are the `|E|` positive numbers `{h_j:j in H}` with sum `p-t`,
\[
\sum_{k\in\mathbb Z_p}c_k^2
=\frac1p\sum_jh_j^2
=\frac{t^2}{p}
 +\frac{(p-t)^2}{p|E|}
 +\frac1p\sum_{j\in H}\left(h_j-\frac{p-t}{|E|}\right)^2.
\tag{6.4}
\]
The last term is a nonnegative **spectral-spread excess**. Equation (6.4) is not yet an upper bound on `t`, but it isolates a concrete obstruction: at source density `|E|~p/2`, the conjectured value `t~sqrt p` is compatible with a bounded frame potential only if the nontrivial positive circuit spectrum does not develop excessive variance. The bi-positive condition (4.8), rather than support size, is the new candidate mechanism for controlling this spread.

---

# 7. Secondary new concentration comparison on prime orders: a transitive sharp-threshold amplifier

This route is independent of the complementary-circuit proof and may help convert a biased-model estimate into the fair-model tail needed for the expectation.

Let each conjugate pair be **available / nonedge** independently with probability `q`; denote the resulting graph by `G_{p,q}`. For fixed `t`, define
\[
\Phi_{p,t}(q):=\Pr\{\vartheta(G_{p,q})\ge t\}.
\tag{7.1}
\]

The event is monotone increasing in the nonedge bits: making another pair available removes theta-primal zero constraints, so theta cannot decrease. Moreover the multiplicative group
\[
\mathbb Z_p^\times/\{\pm1\}
\]
acts transitively on the `m=(p-1)/2` pair coordinates, and multiplication by a unit is a graph isomorphism. Therefore the event is a symmetric monotone subset of `{0,1}^m`.

Friedgut--Kalai's sharp-threshold theorem applies directly. For every fixed `epsilon in (0,1/2)` there is an absolute `C` such that
\[
\boxed{
\Phi_{p,t}(q)>\epsilon
\Longrightarrow
\Phi_{p,t}\left(q+\frac{C\log(1/(2\epsilon))}{\log m}\right)>1-\epsilon,
}
\tag{7.2}
\]
whenever the shifted parameter is at most one.

Hence, by contrapositive, to prove a small upper tail at the fair mask it is enough to prove that the same upper-tail event is **not almost certain** after increasing the available/nonedge density by only `O(1/log p)`.

Complementation gives the exact biased relation
\[
\boxed{
\Pr_q\{\vartheta(G)>t\}
+\Pr_{1-q}\{\vartheta(G)\ge p/t\}=1,
}
\tag{7.3}
\]
because `bar G_{p,q}` has law `G_{p,1-q}` and `theta(G)theta(bar G)=p` deterministically. At `q=1/2`, this recovers the reciprocal symmetry around `sqrt p` from the earlier P07-A report.

This does **not** prove the conjecture by itself: (7.2) supplies threshold width, not threshold location. It does, however, reduce fair-tail control to a small biased comparison, a potentially easier target for the bi-positive circuit geometry because the row/column partition sizes acquire a deterministic drift.

---

# 8. What moved and what did not

### New proved partial results

1. For every prime-order circulant graph and every optimal primal pair for it and its complement,
   \[
   C\circ D=I,\qquad CD=J.
   \]
2. Prime uncertainty plus the preceding identity forces exact ranks
   \[
   \operatorname{rank}C=|E|+1,\qquad \operatorname{rank}D=|A|+1,
   \]
   and exact full physical supports.
3. The nontrivial spectral supports partition all nonzero frequencies, and the two optimizers are uniquely determined on their supports by **strictly positive complementary Fourier circuits**.
4. In the exact random source model on prime order, the optimizer uses exactly every available conjugate pair, so its support is linear (`~p/4` pairs w.h.p.). This supersedes support-counting as the main optimal-witness bottleneck.
5. Prime-order theta upper-tail events are transitive monotone Boolean events, so the Friedgut--Kalai sharp-threshold theorem gives the exact `O(1/log p)` biased-mask amplifier (7.2).

### Full-source quantity

Still
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No arbitrary-`n` asymptotic upper bound is claimed. Prime-only structure is **PROVED PARTIAL**, not a proof of Conjecture 18.

### Failed / retired route from this run

The preceding support-entropy route is no longer the right next move for optimal prime witnesses. Corollary P07-A.14 shows that optimal support is already deterministically maximal inside the allowed set. Another Ramsey support bound cannot touch the remaining sharp constant. The missing information is the **relative sizes of the positive circuit coordinates**, especially the distinguished zero-frequency coordinate.

---

# 9. Next attack

The next P07-A iteration should stay primal and use the stronger object just exposed.

### Attack A — matched Jacobi/cofactor positivity

For a candidate partition `H sqcup K=Z_p^times`, use Cramer's rule on
\[
F_{E,\{0\}\cup H}h=0,
\qquad
F_{A,\{0\}\cup K}g=0
\]
to write `h_0` and `g_0` as bordered Fourier-minor ratios. Use Jacobi complementary-minor identities to place the two ratios in one formula, then exploit the requirement that **all cofactors in both complementary circuit vectors have the same sign/phase after the real-even reduction**. The target is an anti-concentration or deterministic inequality that rules out `h_0>(1+epsilon)sqrt p` except on a sufficiently small family of partitions.

### Attack B — spectral-spread control from bi-positivity

Use (6.4) for both `C` and `D`, together with `CD=J`, full physical support and the fixed levels (6.3), to seek a two-sided bound on the sum of the two spectral-spread excesses. A bound `o(p)` at fair density would force both nontrivial spectra toward flatness and directly constrain `t` versus `p/t`.

### Attack C — locate the threshold in a slightly biased model

At `q=1/2+O(1/log p)`, use the exact rank formulas (`rank C=|E|+1`) and bi-positive circuit dimensions to seek a one-sided probability bounded away from one for `theta>(1+epsilon)sqrt p`. Friedgut--Kalai then amplifies this to a small fair-model tail. This is a genuine primal concentration comparison and remains distinct from P07-B's Moreau residual / exceptional-frequency work.

The most promising immediate route is **Attack A** because it simultaneously uses every new equality from this run and directly targets the distinguished circuit coordinate that equals theta.

---

# 10. Source and prior-art notes checked this run

- Randomstrasse101 current HTML for arXiv:2603.29571v1 (dated 24 Aug 2026 in the current rendering), Entry 9, Conjecture 18, still states `E theta(G)=(1+o(1))sqrt(n)` and cites the `O(sqrt(n log log n))` partial result.
- arXiv:2502.16227 still describes exact random-circulant theta asymptotics as open and the known bound as square-root scale up to a `log log` factor.
- Terence Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, supplies the exact prime support inequality `|supp f|+|supp fhat|>=p+1`; equivalently one may invoke Chebotarev nonsingularity of prime Fourier minors.
- Friedgut--Kalai, *Every monotone graph property has a sharp threshold*, Proc. AMS 124 (1996), gives the symmetric-monotone threshold theorem used in (7.2). Here symmetry is verified on the **conjugate-pair mask coordinates**, not asserted from the theorem abstract alone.
- No claim of external novelty is made for the classical ingredients. The paired optimal-circuit formulation and its use for this source target are candidate new track-level deductions pending later independent review.

No code/checker was created because the new claims are algebraic theorems with complete proofs above; adding a numerical theta value would not improve the arbitrary-size source target.
