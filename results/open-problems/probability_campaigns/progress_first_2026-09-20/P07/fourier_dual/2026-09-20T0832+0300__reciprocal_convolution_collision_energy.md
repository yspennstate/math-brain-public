Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding selector, so I do not claim otherwise.

# P07-B — reciprocal convolution, a critical collision-energy target, and a supercritical spectral-dispersion certificate

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured start master:** `5147efc28f27cc5fd46ab16525c4c702ffbdea93`  
**Fresh pre-write master:** `c2e7130fc60e384cf3d828f85b13a22b861f113c`  
**Previous own report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T0725+0300__static_moreau_cone_projection.md`, creation commit `b853587bd507193ad92fe4a090910a3926019b87`.  
**Complementary P07-A checkpoint used:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0803+0300__prime_optimal_complementary_circuits.md`.  
**Outside target:** Randomstrasse101, arXiv:2603.29571, Conjecture 18; primary partial-result paper arXiv:2502.16227.  
**Exact source endpoint:** for the dense random circulant model,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
**Inherited rigorous source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
Hence the frozen full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No improvement of the published exponent is claimed in this report.

The assignment-time source recovery, exact Fourier LP, old TH18 attempts, and current-status check were already done in earlier P07-B reports. This run does not repeat them. It takes P07-A's new exact complementary-optimum theorem as an input, verifies the consequences needed here directly, and derives a genuinely dual magnitude obstruction rather than duplicating P07-A's support/circuit work.

The main result is a new normalization in which the two complementary optimal spectra are nonnegative factors of the constant function under cyclic convolution. This immediately caps every optimal spectral coordinate by its DC coordinate. Combining that factorization with Parseval identifies an exact collision-energy quantity whose expectation at the critical value would prove Conjecture 18. On prime order, the P07-A exact-rank theorem then yields a new two-sided dispersion identity: any optimizer with theta above `c sqrt(p)` must have a fixed positive amount of spectral weight variance. Thus a supercritical theta value cannot be produced by an almost-flat positive Fourier circuit.

No numerical experiment is used below.

---

## 1. Setup and the complementary optimal pair

Let `n` be odd and let
\[
G=\operatorname{Cay}(\mathbb Z_n,E)
\]
be an undirected circulant graph. Let
\[
A=(\mathbb Z_n\setminus\{0\})\setminus E
\]
be the nonedge-difference set. Average optimal theta matrices over cyclic shifts. We may therefore choose real symmetric circulant optimal primal matrices
\[
C=\operatorname{Circ}(c),\qquad D=\operatorname{Circ}(d)
\]
for `G` and `bar G`, respectively, normalized by
\[
c_0=d_0=1,
\]
with
\[
c_e=0\quad(e\in E),\qquad d_a=0\quad(a\in A).
\]
Write
\[
t:=\vartheta(G)=\sum_x c_x,
\qquad
s:=\vartheta(\bar G)=\sum_x d_x.
\]
Since circulant graphs are vertex transitive,
\[
\boxed{ts=n.}
\tag{1.1}
\]
Let `F` be the nonunitary DFT and put
\[
h:=Fc,\qquad g:=Fd.
\]
Positive semidefiniteness is exactly
\[
h_j\ge0,\qquad g_j\ge0.
\]
Moreover
\[
h_0=t,\quad g_0=s,\qquad \sum_j h_j=\sum_j g_j=n.
\tag{1.2}
\]

P07-A proved the complementary matrix identities. I record the short argument because the normalization below depends on every factor.

For every off-diagonal difference, either `C` is forced to vanish there or `D` is forced to vanish there, while both diagonals are one. Hence
\[
C\circ D=I.
\tag{1.3}
\]
Therefore
\[
\langle C,D\rangle_F=n.
\]
The two circulants diagonalize in the same Fourier basis, so
\[
\sum_j h_jg_j=n.
\]
But the zero-frequency term alone equals
\[
h_0g_0=ts=n,
\]
and every summand is nonnegative. Thus
\[
\boxed{h_jg_j=0\quad(j\ne0),}
\tag{1.4}
\]
and consequently
\[
CD=J.
\tag{1.5}
\]
In first-row language,
\[
\boxed{c\odot d=\delta_0,\qquad c*d=\mathbf1,}
\tag{1.6}
\]
where `*` is unnormalized cyclic convolution.

The identities (1.3)--(1.6) use only circulant vertex transitivity, not primal support exactness or prime-order uncertainty. Thus they remain valid for arbitrary source-admissible odd `n`.

---

# 2. New theorem: normalized optimal spectra factor the constant function

Define
\[
q:=\frac ht,\qquad r:=\frac gs.
\tag{2.1}
\]
Then
\[
q,r\ge0,\qquad q_0=r_0=1,
\tag{2.2}
\]
and by (1.2),
\[
\sum_jq_j=s,\qquad \sum_jr_j=t.
\tag{2.3}
\]

Taking the DFT of the pointwise identity `c odot d=delta_0` in (1.6) gives
\[
\frac1n(h*g)=\mathbf1.
\]
Since `ts=n`, division by `ts` yields the following exact factorization.

## Theorem P07-B.10 — reciprocal spectral convolution

Every optimal complementary circulant pair satisfies
\[
\boxed{q*r=\mathbf1.}
\tag{2.4}
\]
Together with (1.4),
\[
\boxed{q_jr_j=0\quad(j\ne0).}
\tag{2.5}
\]
In particular,
\[
\boxed{0\le q_j\le1,\qquad0\le r_j\le1\quad\text{for all }j.}
\tag{2.6}
\]
Equivalently,
\[
\boxed{0\le h_j\le t,\qquad0\le g_j\le s.}
\tag{2.7}
\]

### Proof of the cap

For `j\ne0`, the nonnegative convolution sum in (2.4) contains the two terms
\[
q_jr_0=q_j,\qquad q_0r_j=r_j.
\]
Therefore
\[
1=(q*r)_j\ge q_j+r_j.
\]
This proves both bounds for nonzero `j`; at zero they are equalities by (2.2). ∎

There is also a probability-measure form which may be useful for dependence-aware small-ball arguments. Define
\[
\mu_j:=\frac{h_j}{n},\qquad \nu_j:=\frac{g_j}{n}.
\]
Then `mu` and `nu` are probability measures and
\[
\boxed{\mu*\nu=\operatorname{Unif}(\mathbb Z_n),}
\tag{2.8}
\]
with
\[
\mu_0=\frac tn=\frac1s,\qquad
\nu_0=\frac sn=\frac1t.
\tag{2.9}
\]
Thus the complementary optimal spectra form an exact positive convolution factorization of Haar measure. This is not an independence assertion: both factors are highly endogenous functions of the same graph.

### Immediate collision-energy cap

Parseval gives
\[
\|c\|_2^2=\frac1n\sum_jh_j^2.
\]
Using `h_j<=t` and `sum h_j=n`,
\[
\boxed{\|c\|_2^2\le t.}
\tag{2.10}
\]
The analogous bound `||d||_2^2<=s` also holds. This is much too weak by itself at `t~sqrt(n)`, but it identifies the right normalized second moment.

---

# 3. An all-`n` collision-energy lemma sufficient for the full conjecture

Let
\[
a:=|A|
\]
be the number of nonzero allowed physical differences for the primal optimizer of `G`, and define the optimal physical collision energy
\[
\mathcal E(G):=\|c\|_2^2=\frac1n\sum_jh_j^2.
\tag{3.1}
\]
Since `c_0=1` and `c_e=0` on `E`,
\[
t-1=\sum_{x\in A}c_x.
\]
Cauchy--Schwarz gives the deterministic inequality
\[
\boxed{(t-1)^2\le a\bigl(\mathcal E(G)-1\bigr).}
\tag{3.2}
\]
This remains true if additional allowed coefficients happen to vanish and does not require prime order.

Taking expectation over the exact source model and using Jensen,
\[
\boxed{
\mathbb E\vartheta(G_n)
\le
1+\sqrt{\mathbb E\left[a(G_n)\bigl(\mathcal E(G_n)-1\bigr)\right]}.
}
\tag{3.3}
\]

This yields a new source-exact sufficient lemma.

## Missing Critical Collision-Energy Lemma `CCEL`

Prove
\[
\boxed{
\mathbb E\left[a(G_n)\left(\frac1n\sum_jh_j^2-1\right)\right]
\le(1+o(1))n,
}
\tag{3.4}
\]
where `h` is the spectrum of an optimal cyclically averaged primal theta matrix.

Then (3.3) gives
\[
\mathbb E\vartheta(G_n)\le(1+o(1))\sqrt n,
\]
and the known lower bound proves Conjecture 18.

The weaker estimate
\[
\boxed{
\mathbb E\left[a(G_n)(\mathcal E(G_n)-1)\right]=O(n)
}
\tag{3.5}
\]
is already sufficient for
\[
\mathbb E\vartheta(G_n)=O(\sqrt n),
\]
so (3.5) removes the published iterated-log loss.

This is a useful replacement for the preceding report's static Moreau target because it asks for one second moment of the **actual optimal spectrum**, rather than an `L^infty` or cone-distance bound uniform over many generated exceptional sets. It is still nontrivial: the universal cap (2.10) only gives `E(G)<=t`, which is far from the critical `O(1)` collision-energy scale.

For the dense fair source, `a=(1/2+o_P(1))n`. Thus the sharp heuristic content of (3.4) is
\[
\mathcal E(G_n)\lesssim3,
\]
but (3.4), not an informal pointwise `3`, is the expectation statement actually sufficient for the all-`n` source theorem.

---

# 4. Prime-order exact identity: supercritical theta forces spectral dispersion

Now specialize to odd prime order `p`. This is a restricted theorem, not a full-source closure. Put
\[
m:=|E|,\qquad a:=|A|=p-1-m.
\]
P07-A's prime optimal-support theorem gives, for every optimal pair,
\[
\operatorname{supp}h=\{0\}\cup H,\qquad |H|=m,
\tag{4.1}
\]
and all `q_j`, `j in H`, are strictly positive. Recall
\[
s=\frac pt,\qquad \sum_{j\in H}q_j=s-1.
\]
Define the spectral dispersion
\[
V_q:=\sum_{j\in H}\left(q_j-\frac{s-1}{m}\right)^2
\tag{4.2}
\]
and the physical dispersion
\[
W_c:=\sum_{x\in A}\left(c_x-\frac{t-1}{a}\right)^2.
\tag{4.3}
\]
Both are nonnegative.

Expanding the physical side gives
\[
\mathcal E(G)
=1+\frac{(t-1)^2}{a}+W_c.
\tag{4.4}
\]
On the Fourier side, Parseval and `h=tq` give
\[
\begin{aligned}
\mathcal E(G)
&=\frac{t^2}{p}\left(1+\sum_{j\in H}q_j^2\right)\\
&=\frac{t^2}{p}
+\frac{(p-t)^2}{pm}
+\frac{t^2}{p}V_q.
\end{aligned}
\tag{4.5}
\]
Equating (4.4) and (4.5) proves the exact identity
\[
\boxed{
\frac{t^2}{p}V_q-W_c
=
1+\frac{(t-1)^2}{a}
-\frac{t^2}{p}
-\frac{(p-t)^2}{pm}.
}
\tag{4.6}
\]
This is the key new dual magnitude relation.

### Exactly balanced masks

If
\[
m=a=\frac{p-1}{2},
\]
then the right side of (4.6) simplifies **exactly** to
\[
\frac{t^2}{p}-1.
\]
Hence
\[
\boxed{
\frac{t^2}{p}V_q-W_c=\frac{t^2}{p}-1.
}
\tag{4.7}
\]
Since `W_c>=0`, every supercritical optimizer obeys
\[
\boxed{
V_q\ge1-\frac p{t^2}.
}
\tag{4.8}
\]
In particular, if
\[
t\ge c\sqrt p,\qquad c>1,
\]
then
\[
\boxed{V_q\ge1-c^{-2}.}
\tag{4.9}
\]

Thus an optimizer above the conjectural constant cannot have its positive nonzero spectral weights nearly flat. The obstruction is not merely a large exceptional coordinate: it carries a fixed amount of aggregate spectral variance.

### Source-typical near balance

For the fair source mask,
\[
\frac mp\to\frac12,\qquad \frac ap\to\frac12
\]
in probability. From the explicit right side of (4.6), uniformly on any event with `m/p=1/2+o(1)`, `a/p=1/2+o(1)` and `t>=c sqrt(p)` for fixed `c>1`, one obtains
\[
\boxed{
V_q\ge1-c^{-2}-o(1).
}
\tag{4.10}
\]
One convenient way to see the uniformity is to multiply the right side of (4.6) by `p/t^2`:
\[
\frac p{t^2}
\left[
1+\frac{(t-1)^2}{a}-\frac{t^2}{p}-\frac{(p-t)^2}{pm}
\right]
=
-1+\frac pa\left(1-\frac1t\right)^2+rac p{t^2}
-\frac1m\left(\frac pt-1\right)^2.
\tag{4.11}
\]
For `m,a=(1/2+o(1))p` and `t>=c sqrt(p)`, this is bounded below by `1-c^{-2}-o(1)`. Since `W_c>=0`, (4.10) follows.

This is a rigorous restricted source consequence along prime orders: **a fixed supercritical factor forces fixed spectral dispersion**. It complements P07-A's support theorem. P07-A showed the optimizer is Fourier-dense; (4.10) says that if its value is too large, those dense positive weights must additionally be quantitatively nonuniform.

---

# 5. A dependence-aware next lemma that would improve the source bound

The prime-order reduction suggests a sharper exceptional-frequency target than bounding the maximum coordinate.

## Missing Optimal-Circuit Flattening Lemma `OCFL(c)`

For every fixed `c>1`, prove on the fair prime-order source model that
\[
\boxed{
\Pr\left\{V_q\ge1-c^{-2}-o(1)\right\}
}
\tag{5.1}
\]
is small enough, uniformly in `c`, to make P07-A's exact reciprocal upper-tail integral
\[
\int_1^{\sqrt p}(1-c^{-2})
\Pr\{\vartheta(G_p)>c\sqrt p\}\,dc
\tag{5.2}
\]
tend to zero.

By (4.10), such a bound controls the theta upper tail. A quantitative `OCFL` sufficient to make (5.2) `o(1)` proves the sharp prime-order asymptotic. An all-odd-`n` analogue, or the all-`n` collision-energy estimate `CCEL`, would address the full source endpoint.

The dependence warning is essential. `q` is the positive one-dimensional Fourier circuit selected **after seeing the same random edge mask**, and its support is itself endogenous. It is invalid to replace the coordinates of `q` by independent samples. The right object for a small-ball argument is the coupled complementary system
\[
q*r=\mathbf1,\qquad q,r\ge0,\qquad q_0=r_0=1,\qquad q_jr_j=0\ (j\ne0),
\tag{5.3}
\]
together with the two source Fourier circuit equations from P07-A. The next attack should exploit those exact equations via leave-one-mask-bit or complementary-minor identities, not an iid surrogate for the Fourier coordinates.

A weaker but already source-useful target is (3.5): show directly that the expected optimal collision energy is `O(1)` after multiplication by the actual nonedge count. That alone removes `sqrt(log log n)`.

---

# 6. New local tightening lemma and why black-box concentration is not enough

I also tested whether one can turn the spectral cap into a direct bounded-difference proof. The following deterministic one-bit estimate is useful, but its scale shows that this route alone does not prove the conjecture.

Let `b` be a currently allowed nonedge conjugate pair, and let `G^{+b}` be the circulant graph obtained by adding `+-b` as an edge pair. Let `c` be the optimal first row for `G` and write `u=c_b=c_{-b}`. Define
\[
\widetilde c
:=c-u(e_b+e_{-b})+2|u|e_0.
\tag{6.1}
\]
Then the new pair coefficient is zero and all old edge zeros are preserved. In Fourier space,
\[
F\widetilde c
=h-2u\cos(2\pi bj/n)+2|u|\mathbf1
\ge h\ge0
\tag{6.2}
\]
coordinatewise. Thus after division by `1+2|u|`, this is a feasible primal point for `G^{+b}`. Its objective gives
\[
\vartheta(G^{+b})
\ge
\frac{t-2u+2|u|}{1+2|u|}
\ge
\frac{t}{1+2|u|}.
\tag{6.3}
\]
Since adding an edge can only decrease theta,
\[
\boxed{
0\le\log\vartheta(G)-\log\vartheta(G^{+b})
\le\log(1+2|c_b|)\le2|c_b|.
}
\tag{6.4}
\]
Summing over all currently absent conjugate pairs gives
\[
\boxed{
\sum_{b\in A/\{+-\}}
\bigl(\log\vartheta(G)-\log\vartheta(G^{+b})\bigr)^2
\le2\bigl(\mathcal E(G)-1\bigr).
}
\tag{6.5}
\]
Indeed `E(G)-1=2 sum_b c_b^2` for a real-even first row.

This identifies collision energy as a genuine mask-sensitivity budget, not merely an algebraic reformulation. But even at the conjectural critical energy `E(G) approximately 3`, (6.5) yields only an `O(1)` total squared log-sensitivity. A black-box Efron--Stein argument would therefore give at best constant-order logarithmic fluctuations; it does not force the reciprocal dispersion to vanish. The next proof needs the Fourier/circuit dependence encoded in (5.3), or a stronger multiscale cancellation, rather than generic bounded differences.

---

# 7. Relation to the preceding Moreau target

The previous P07-B report reduced the dual feasibility problem to the static positive-cone residual
\[
d_D(\tau)
=\max_{p\in\mathcal F_D}
\frac{(p_0-1/n-\tau)_+}{\|p\|_2}
\]
and proved deterministic transversality of any surviving obstruction. That reduction remains correct.

The present report changes the immediate attack because P07-A subsequently supplied exact complementary optimal circuits. Rather than bounding every positive-cone witness, we can now condition on the **actual optimal pair** and exploit identities that are unavailable for an arbitrary feasible witness. The hierarchy is:

1. `SPCP` from the preceding report is a sufficient cone-uniform route.
2. `CCEL` in (3.4) is a weaker optimal-witness second-moment route, sufficient for the full expectation conjecture.
3. On prime order, supercriticality implies the fixed spectral-dispersion event (4.10), reducing the upper tail to an endogenous optimal-circuit flattening problem.

This is a real narrowing of the missing theorem, not a claim that it has been proved.

---

# 8. What changed, what failed, and next attack

**Headline source metric:**
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No source-level exponent movement is claimed.

**New proved partial results:**

1. Exact reciprocal spectral convolution `q*r=1` for every complementary optimal circulant pair, with the pointwise cap `0<=q_j,r_j<=1`.
2. Exact all-`n` collision-energy inequality
   \[
   (\vartheta(G)-1)^2\le |A|(\mathcal E(G)-1),
   \]
   giving the sufficient expectation lemma `CCEL`.
3. On prime order, exact physical-versus-spectral dispersion identity (4.6); for balanced masks it collapses to (4.7), so `theta>=c sqrt(p)` forces `V_q>=1-c^{-2}`.
4. Exact one-bit tightening bound (6.4) and aggregate forward sensitivity budget (6.5).

**Failed/insufficient route learned:** the one-bit sensitivity estimate does not by itself give vanishing fluctuations. Generic bounded differences can at best see the total collision-energy budget and misses the complementary-circuit cancellation needed for the sharp constant.

**Next concrete attack:** use the P07-A cofactor/Jacobi representation of the positive circuit together with the exact complementary convolution system (5.3). The immediate goal is a dependence-aware estimate on
\[
V_q=\sum_{j\in H}\left(q_j-\frac{s-1}{|H|}\right)^2
\]
for the actual source-generated positive circuit. A successful first milestone is any bound implying
\[
\mathbb E\left[|A|(\mathcal E(G)-1)\right]=O(n),
\]
which already removes the iterated-log loss. The sharp milestone is `(1+o(1))n`, which proves Conjecture 18 by (3.3).

**P07-A handoff:** the useful new dual consequence of P07-A's circuit theorem is (2.4)--(2.7) plus the supercritical dispersion certificate (4.6)--(4.10). P07-A need not duplicate the collision-energy proof; its complementary-minor work can feed an estimate on `V_q`.

External novelty of this packaging is **UNVERIFIED**. The result is recorded as **PROVED PARTIAL**, not a candidate full proof.
