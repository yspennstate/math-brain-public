Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding model/effort selector, so I do not claim otherwise.

# P07-B — exact second-order Gibbs cancellation, multiscale clipping, and a positive sparse-exception patch

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured start master:** `096cd70d196edc7013da42ad1bc10e3b6a49104b`  
**Fresh pre-write master:** `8f7d1f8209955bb8a12cb8d041417bd23970680b`  
**Previous own substantive report:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1028+0300__bounded_transverse_interpolation.md`, creation commit `35ecc3e5ba83a20856e115b9ef4f2bdc3190f951`.  
**Complementary P07-A checkpoint used:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1047+0300__reciprocal_variance_orbit_influence.md`, creation commit `d5118c589f7a6e1a205a3b79909582af88ea0630`. P07-A owns the primal/orbit-sensitivity route; this report stays on Fourier-dual exceptional-coordinate control.

**Outside target:** *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18; primary partial result arXiv:2502.16227.  
**Source endpoint:** for the dense random undirected circulant model,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
**Inherited rigorous source bound:**
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
The fixed source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
Status: **OPEN / PROVED PARTIAL**. No improved arbitrary-`n` theta exponent is claimed in this report.

The assignment-time source recovery, exact Fourier LP, and old TH18 attempts were already recovered in earlier P07-B reports and are not repeated. The exact moment-polytope normalization used here is
\[
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D},
\]
where `delta_D` is the largest common negative selected cosine moment attainable by a symmetric probability on `Z_n`.

The new point is that the preceding bounded-interpolation target `TRBI` admits a much more structured decomposition than a generic `L^1/L^2` small-ball problem. The radial Gibbs law has an **exact second-order signed interpolant**: the constant and first-order Fourier pieces cancel identically in every transverse direction. Its `L^2` size is asymptotically `beta^2/sqrt(512)`, and clipping it at a constant multiple of `beta^2` leaves only a source-generated exceptional set. An exact Hahn--Banach calculation then shows that one only needs to prevent transverse cosine polynomials from concentrating their `L^1` mass on those Gibbs-tail levels. Separately, a new explicit positive probability measure repairs any *sparse* set of bad selected frequencies with **zero cross-talk** to the other selected frequencies. These two constructions isolate the remaining obstruction much more sharply than the previous global Kashin-width condition.

---

## 1. Setup and the exact transverse tight frame

Let `n` be odd,
\[
M=\{1,\dots,(n-1)/2\},\qquad D\subset M,\qquad d=|D|,
\]
and
\[
\phi_a(j)=\cos(2\pi aj/n),\qquad
\Phi(j)=(\phi_a(j))_{a\in D}.
\]
Let `q_0` be the uniform probability on `Z_n\setminus\{0\}`. The exact identities are
\[
\mathbb E_{q_0}\phi_a=-\frac1{n-1},
\tag{1.1}
\]
\[
\mathbb E_{q_0}\phi_a^2=\frac{n-2}{2(n-1)},
\qquad
\mathbb E_{q_0}\phi_a\phi_b=-\frac1{n-1}\quad(a\ne b).
\tag{1.2}
\]
Put
\[
u=d^{-1/2}{\bf1},\qquad P=I-uu^T.
\]
For `z in u^perp`, define
\[
f_z(j)=\langle z,\Phi(j)\rangle.
\]
Then
\[
\mathbb E_{q_0}f_z=0
\tag{1.3}
\]
and, exactly,
\[
\boxed{
\mathbb E_{q_0}f_z^2
=\lambda_n\|z\|_2^2,
\qquad
\lambda_n:=\frac{n}{2(n-1)}.
}
\tag{1.4}
\]

Define the transverse moment map
\[
Th:=P\,\mathbb E_{q_0}[h(J)\Phi(J)]\in u^\perp.
\tag{1.5}
\]
Its adjoint is
\[
T^*z=f_z,
\tag{1.6}
\]
and (1.4) is exactly
\[
\boxed{TT^*=\lambda_n I_{u^\perp}.}
\tag{1.7}
\]
Thus the transverse cosine system is an exact tight frame. This elementary identity will be used twice below.

---

# 2. The Gibbs residual has an exact second-order interpolant

Fix `beta>0` and use the excluded-origin Gibbs law from the earlier P07-B report:
\[
X_D(j)=\frac1{\sqrt n}\sum_{a\in D}\phi_a(j),
\tag{2.1}
\]
\[
A_D(\beta)=\mathbb E_{q_0}e^{-\beta X_D},
\qquad
R_D(j)=\frac{e^{-\beta X_D(j)}}{A_D(\beta)}.
\tag{2.2}
\]
Thus `R_D q_0` is a probability on the nonzero sites. Let
\[
m=\mathbb E_{q_0}[R_D\Phi],
\qquad
\bar m=d^{-1}{\bf1}^Tm,
\qquad
r=m-\bar m{\bf1}=Pm.
\tag{2.3}
\]
The preceding report defined the bounded interpolation cost
\[
K_D(\beta)
=\inf\{\|h\|_\infty:Th=r\}.
\tag{2.4}
\]

The first-order term in the Gibbs density is radial and therefore completely invisible to `T`.

## Theorem P07-B.13 — exact second-order cancellation

Define
\[
\boxed{
h_{\rm raw}
:=R_D-1+\beta X_D.
}
\tag{2.5}
\]
Then
\[
\boxed{Th_{\rm raw}=r.}
\tag{2.6}
\]
In particular, `h_raw` is an exact signed interpolant of the full transverse Gibbs residual, not an asymptotic one.

### Proof

First, `T1=0` because `E_{q_0}Phi` is a multiple of `1` by (1.1). Next,
\[
\mathbb E_{q_0}[X_D\Phi]
=\frac1{\sqrt n}\mathbb E_{q_0}[\Phi\Phi^T]{\bf1}.
\]
The matrix in (1.2) has constant diagonal and constant off-diagonal entries, hence its product with `1` is again a multiple of `1`; therefore
\[
TX_D=0.
\tag{2.7}
\]
Finally,
\[
TR_D=P\mathbb E_{q_0}[R_D\Phi]=Pm=r.
\]
Combining these three identities proves (2.6). `square`

So the constant and linear terms of the exponential tilt cancel **exactly** in the transverse problem. The bounded-interpolation obstruction genuinely starts at second order in `beta`.

---

# 3. The canonical interpolant is the orthogonal projection of the second-order remainder

Because of the tight-frame identity (1.7), the minimum-`L^2(q_0)` solution of `Th=r` is explicit:
\[
\boxed{
h_{\rm can}=\lambda_n^{-1}T^*r=\lambda_n^{-1}f_r.}
\tag{3.1}
\]
Moreover
\[
\Pi_{\mathcal F}:=\lambda_n^{-1}T^*T
\tag{3.2}
\]
is the orthogonal projector in `L^2(q_0)` onto
\[
\mathcal F_D:=\{f_z:z\in u^\perp\}.
\]
Since `Th_raw=r`,
\[
\boxed{
h_{\rm can}=\Pi_{\mathcal F}h_{\rm raw}.}
\tag{3.3}
\]
Therefore
\[
\boxed{
\|h_{\rm can}\|_{L^2(q_0)}
\le \|h_{\rm raw}\|_{L^2(q_0)}.
}
\tag{3.4}
\]
This is useful because `h_raw` is an explicit scalar function of the one-dimensional Fourier field `X_D`; no matrix inverse or pathwise Hessian appears.

---

# 4. Exact asymptotic size of the second-order remainder

The earlier Gibbs report proved, for every fixed real `t`,
\[
A_D(t)\xrightarrow{\mathbb P}e^{t^2/32}
\tag{4.1}
\]
with the same convergence for the first two derivatives on compact `t`-intervals. In particular,
\[
\mathbb E_{q_0}X_D^2\xrightarrow{\mathbb P}\frac1{16},
\tag{4.2}
\]
\[
\mathbb E_{q_0}[R_DX_D]
=-\frac{A_D'(\beta)}{A_D(\beta)}
\xrightarrow{\mathbb P}-\frac\beta{16},
\tag{4.3}
\]
and
\[
\mathbb E_{q_0}R_D^2
=\frac{A_D(2\beta)}{A_D(\beta)^2}
\xrightarrow{\mathbb P}e^{\beta^2/16}.
\tag{4.4}
\]
Also `E_{q_0}X_D=-d/[\sqrt n(n-1)]=o_P(1)`. Expanding the square in (2.5) therefore gives the exact limiting second moment
\[
\boxed{
\|h_{\rm raw}\|_{L^2(q_0)}^2
\xrightarrow{\mathbb P}
H_2(\beta)
:=e^{\beta^2/16}-1-\frac{\beta^2}{16}.
}
\tag{4.5}
\]
For small fixed `beta`,
\[
\boxed{
H_2(\beta)=\frac{\beta^4}{512}+O(\beta^6),
\qquad
\|h_{\rm raw}\|_2
=\frac{\beta^2}{\sqrt{512}}+O(\beta^3).
}
\tag{4.6}
\]
By (3.4), the same upper bound applies to the canonical exact interpolant.

This is a sharper statement than merely `||r||_2=O(beta^2)`: it identifies a concrete exact interpolating function whose entire `L^2` mass is second order and gives its limiting constant.

---

# 5. Multiscale clipping: the global Kashin condition is unnecessary

The previous report used the stronger sufficient condition
\[
\inf_{\|z\|_2=1,z\perp{\bf1}}\mathbb E|f_z|\ge c.
\]
The exact interpolant above shows that this is more than is needed. We can clip `h_raw` and ask for small-ball control only on its own exceptional levels.

Fix a clipping height `B>0` and put
\[
b=\operatorname{clip}(h_{\rm raw},[-B,B]),
\qquad
w=h_{\rm raw}-b.
\tag{5.1}
\]
Let
\[
C_B=\{|h_{\rm raw}|\le B\},
\qquad
E_B=C_B^c.
\tag{5.2}
\]
Then `w` is supported on `E_B` and
\[
Tb=r-Tw.
\tag{5.3}
\]
To recover the exact residual it is enough to find a correction `v`, supported on `C_B`, such that
\[
Tv=Tw.
\tag{5.4}
\]
The resulting interpolant `h=b+v` satisfies `Th=r` and
\[
\|h\|_\infty\le B+\|v\|_\infty.
\tag{5.5}
\]

## Theorem P07-B.14 — exact exceptional-set repair duality

Let `K_B^{\rm rep}` be the least `||v||_infinity` among functions supported on `C_B` and satisfying (5.4). Then
\[
\boxed{
K_B^{\rm rep}
=
\sup_{\substack{z\perp{\bf1}\\z\ne0}}
\frac{|\mathbb E_{q_0}[w f_z]|}
{\mathbb E_{q_0}[|f_z|\,1_{C_B}]},
}
\tag{5.6}
\]
with the usual convention that a direction with zero denominator and nonzero numerator gives `+infinity`.

### Proof

For a function `v` supported on `C_B`,
\[
\langle Tv,z\rangle
=\mathbb E_{q_0}[v f_z].
\]
The support function, in direction `z`, of the convex symmetric set
\[
\{Tv:\operatorname{supp}v\subset C_B,\ \|v\|_\infty\le K\}
\]
is exactly
\[
K\,\mathbb E_{q_0}[|f_z|1_{C_B}].
\]
Finite-dimensional Hahn--Banach separation gives (5.6). `square`

This is the right dependence-aware formulation: `E_B` is generated by the **same mask** as `f_z`. No independent copy of the Fourier field is introduced.

---

## 5.1 Dyadic multiscale form

Define disjoint levels
\[
E_k(B)=\{2^kB<|h_{\rm raw}|\le2^{k+1}B\},\qquad k\ge0,
\tag{5.7}
\]
and the source-generated concentration ratios
\[
\boxed{
\rho_k(D,B)
:=\sup_{\substack{z\perp{\bf1}\\z\ne0}}
\frac{\mathbb E_{q_0}[|f_z|1_{E_k(B)}]}
{\mathbb E_{q_0}[|f_z|1_{C_B}]}.
}
\tag{5.8}
\]
Since `|w|<=|h_raw|<=2^{k+1}B` on `E_k(B)`, (5.6) yields
\[
\boxed{
K_B^{\rm rep}
\le 2B\sum_{k\ge0}2^k\rho_k(D,B).
}
\tag{5.9}
\]
Hence
\[
\boxed{
K_D(\beta)
\le
B\left(1+2\sum_{k\ge0}2^k\rho_k(D,B)\right).
}
\tag{5.10}
\]
This is an exact deterministic inequality for every mask `D`.

The global Kashin width from the preceding report is therefore unnecessary. It suffices to show that transverse cosine polynomials cannot put too large a fraction of their `L^1` mass on the **specific Gibbs second-order tail levels** `E_k(B)`.

---

# 6. The exceptional dual set is genuinely small after second-order cancellation

The partition-function theorem implies that the random empirical law of `X_D(j)`, `j ne0`, converges in probability to
\[
Z\sim N(0,1/16).
\tag{6.1}
\]
For fixed `beta`, `A_D(beta)->e^{beta^2/32}`, so the empirical law of `h_raw` converges to the scalar random variable
\[
H_\beta(Z)
:=e^{-\beta Z-\beta^2/32}-1+\beta Z.
\tag{6.2}
\]
As `beta->0`,
\[
\frac{H_\beta(Z)}{\beta^2}
\longrightarrow
\frac12\left(Z^2-\frac1{16}\right)
\tag{6.3}
\]
in every fixed Gaussian `L^p`.

Therefore, for every continuity threshold `b>0`,
\[
\boxed{
\lim_{\beta\downarrow0}\lim_{n\to\infty}
q_0\{|h_{\rm raw}|>b\beta^2\}
=
\Pr\left\{\frac12\left|Z^2-\frac1{16}\right|>b\right\}.
}
\tag{6.4}
\]
For the concrete choice
\[
B=\frac{\beta^2}{8},
\tag{6.5}
\]
(6.4) becomes
\[
\boxed{
\lim_{\beta\downarrow0}\lim_{n\to\infty}
q_0(E_B)
=\Pr\{|N(0,1)|>\sqrt5\}
=2Q(\sqrt5)
\approx0.02535.
}
\tag{6.6}
\]
Thus, after exact cancellation of the constant and linear Gibbs pieces, clipping at only `beta^2/8` leaves asymptotically about `2.5%` exceptional dual sites in the small-`beta` limit.

This number is not itself a theorem about theta. Its role is structural: the missing anti-concentration estimate (5.8) only concerns a very small source-generated set, rather than all sites or all Fourier directions.

There is also a deterministic square-mass census. Since the levels in (5.7) are disjoint,
\[
\boxed{
\sum_{k\ge0}4^k q_0(E_k(B))
\le \frac{\|h_{\rm raw}\|_2^2}{B^2}.
}
\tag{6.7}
\]
For `B=b beta^2`, (4.6) makes the right side `O_b(1)` for small fixed `beta`. What remains is not tail *size* but possible adaptive concentration of `|f_z|` onto those tails.

---

# 7. Exact theorem-sized lemma that now removes the iterated-log loss

The previous missing lemma `TRBI(beta,C)` can be replaced by the following more localized statement.

## Missing lemma `SGEL(beta,b,L)` — source-generated exceptional leakage

For one sufficiently small fixed `beta>0`, with `B=b beta^2` (for example `b=1/8`), prove that for an absolute finite `L`,
\[
\boxed{
\Pr\left\{
\sum_{k\ge0}2^k\rho_k(D,B)>L
\right\}
=O(n^{-1/2}).
}
\tag{7.1}
\]

Then (5.10) gives
\[
K_D(\beta)=O(\beta^2)
\tag{7.2}
\]
on the same event. The constructive theorem from the preceding report then gives
\[
\delta_D\ge\frac{c_\beta}{\sqrt n}
\tag{7.3}
\]
for some fixed `c_beta>0`; on the exceptional event use the universal `delta_D>=1/(n-1)` fallback. Hence
\[
\boxed{\mathbb E\vartheta(G_n)=O(\sqrt n).}
\tag{7.4}
\]
So `SGEL` removes the published `sqrt(log log n)` loss.

This is strictly narrower than a global random-Fourier Kashin theorem: it only tests `L^1` concentration on the dyadic levels of the actual second-order Gibbs remainder. It is also narrower than the earlier `STCL` covariance-tube condition and does not require controlling an entire Newton/Gibbs path.

No independence between `E_k(B)` and `f_z` is assumed or permitted. The point of (7.1) is precisely to quantify their same-mask dependence.

---

# 8. A second exact construction: positive no-cross-talk repair of sparse bad selected frequencies

The Gibbs report also produced an `O(beta^2)` *fraction* of selected frequencies whose moments may fail a target threshold. There is an exact positive repair device for such frequency exceptions once their number becomes sub-square-root.

Let `B` now denote a nonempty subset of the selected **frequency indices** `D`, and write `k=|B|`. Define a probability on `Z_n` by
\[
q_B(0)=0,
\qquad
\boxed{
q_B(j)
=\frac1n\left(1-\frac1k\sum_{a\in B}\phi_a(j)\right),
\quad j\ne0.
}
\tag{8.1}
\]
Because the average of numbers in `[-1,1]` is at most `1`, `q_B(j)>=0`. Also
\[
\sum_{j\ne0}\phi_a(j)=-1,
\]
so the total mass in (8.1) is exactly one.

## Theorem P07-B.15 — sparse positive frequency patch

For every `c in M`,
\[
\boxed{
\mathbb E_{q_B}\phi_c
=
\begin{cases}
-\dfrac1{2k},&c\in B,\\[4pt]
0,&c\notin B.
\end{cases}
}
\tag{8.2}
\]
Thus `q_B` lowers all frequencies in `B` equally and has **zero Fourier cross-talk** to every other positive frequency.

### Proof

For `c in B`,
\[
\sum_{j\ne0}\phi_c(j)^2=\frac{n-2}{2},
\]
while for distinct positive representatives `a ne c`,
\[
\sum_{j\ne0}\phi_a(j)\phi_c(j)=-1.
\]
Hence
\[
\begin{aligned}
\mathbb E_{q_B}\phi_c
&=\frac1n\left[
-1-\frac1k\left(\frac{n-2}{2}-(k-1)\right)
\right]\\
&=-\frac1{2k}.
\end{aligned}
\]
If `c notin B`, every cross term in the inner sum equals `-1`, so
\[
\mathbb E_{q_B}\phi_c
=\frac1n[-1-(-1)]=0.
\]
This proves (8.2). `square`

### Sparse-exception corollary

Suppose a probability `p` has selected moments `m_a` such that, for constants `c>c'>0` and `M<infinity`,
\[
m_a\le-\frac c{\sqrt n}\quad(a\in D\setminus B),
\tag{8.3}
\]
\[
m_a\le\frac M{\sqrt n}\quad(a\in B),
\tag{8.4}
\]
and `k=|B|`. Set
\[
\boxed{
w=
\frac{2k(M+c')}{\sqrt n+2kM}.
}
\tag{8.5}
\]
If `2kc'<sqrt(n)`, then `0<w<1`. The mixture
\[
p'=(1-w)p+wq_B
\tag{8.6}
\]
has, for `a in B`,
\[
\mathbb E_{p'}\phi_a
\le
(1-w)\frac M{\sqrt n}-\frac w{2k}
=-\frac{c'}{\sqrt n},
\tag{8.7}
\]
while for `a notin B`,
\[
\mathbb E_{p'}\phi_a
=(1-w)m_a
\le-(1-w)\frac c{\sqrt n}.
\tag{8.8}
\]
In particular, if `k=o(sqrt(n))`, then `w=o(1)` and any `O(n^{-1/2})` sparse collection of bad selected moments can be repaired while losing only `o(1)` in the leading depth coefficient.

This exact patch does **not** solve the current Gibbs exceptional-frequency problem because the proven count is still `O(beta^2 n)`, not `o(sqrt(n))`. It does, however, remove the need to drive the number of bad selected frequencies literally to zero: a multiscale argument only needs to reduce the final exceptional set below the square-root scale.

---

# 9. Relation to P07-A's newest variance reduction

P07-A's current theorem shows
\[
0\le\frac{\mathbb E\vartheta(G_n)}{\sqrt n}-1
\le\frac{\mathbb E S_-(D)}{4n},
\]
where `S_-` is the squared generator-deletion energy. That is a different route and is not reproved here.

The useful interface is now clear:

* P07-B can first target `SGEL` to obtain a source-scale `O(sqrt(n))` dual certificate with no iterated-log loss.
* The exact sparse patch (8.1)--(8.8) can repair a terminal `o(sqrt(n))` set of bad selected frequencies with no cross-talk.
* P07-A can separately ask whether these explicit dual certificates imply a useful deletion-stability estimate for its orbit-energy lemma. That sensitivity step remains unproved and belongs to P07-A's route.

No claim is made here that `O(sqrt(n))` alone yields the sharp leading constant `1`; it does not.

---

# 10. What changed this run

### Proved

1. **Exact second-order Gibbs cancellation:** `h_raw=R_D-1+beta X_D` interpolates the entire transverse Gibbs residual exactly.
2. **Exact tight-frame canonical solution:** `h_can=lambda_n^{-1}f_r=Pi_F h_raw` is the minimum-`L^2` interpolant.
3. **Exact asymptotic remainder energy:**
   \[
   \|h_{raw}\|_2^2\to e^{\beta^2/16}-1-\beta^2/16
   =\beta^4/512+O(\beta^6).
   \]
4. **Exact multiscale clipping duality:** the required bounded repair is controlled only by the source-generated ratios `rho_k(D,B)` in (5.8), giving (5.10).
5. **Controlled exceptional dual coordinates:** clipping at `B=beta^2/8` leaves limiting small-`beta` density `2Q(sqrt(5))≈0.02535`.
6. **Exact positive sparse-frequency patch:** the probability `q_B` in (8.1) has moment `-1/(2|B|)` exactly on `B` and zero on every other positive frequency.
7. **Sparse repair threshold:** `o(sqrt(n))` bad selected frequencies with `O(n^{-1/2})` deficits can be repaired at `o(1)` mixture cost.

### Not proved

* `SGEL`, `TRBI`, `E theta=O(sqrt(n))`, or the sharp `(1+o(1))sqrt(n)` conjecture.
* Any independence between Fourier coordinates or between the Gibbs exceptional sets and test polynomials.
* A reduction of the currently proved `O(beta^2 n)` selected-frequency exceptional count to `o(sqrt(n))`.

The full-source metric therefore remains `alpha_LL=1/2`.

---

# 11. Next attack

The next P07-B run should attack `SGEL` directly, not return to the global Kashin theorem. The concrete target is the fixed threshold
\[
B=\beta^2/8
\]
for a small fixed `beta`, and the same-mask quantity
\[
\sum_{k\ge0}2^k
\sup_{z\perp1}
\frac{\mathbb E_{q_0}[|f_z|1_{E_k(B)}]}
{\mathbb E_{q_0}[|f_z|1_{C_B}]}.
\]
There are two genuinely different candidate attacks:

1. **Dependence-aware leave-one-frequency small-ball:** reveal one mask bit at a time and exploit the fact that membership in `E_k(B)` is a smooth second-order function of the aggregate field after the exact linear cancellation. The goal is a direct comparison of `L^1` mass on `E_k` and `C_B`, not an independence approximation.
2. **Multiscale concentration/uncertainty:** prove that any transverse `f_z` concentrating on one Gibbs-tail level forces a large Fourier-concentration operator eigenvalue on that level; then use the small empirical level density plus the random source mask to rule out such an eigenvalue along the actual levels. This is now a fixed family of source-generated sets, not an arbitrary-subset RIP statement.

If both fail, the exact sparse patch gives a separate pivot: seek a construction that reduces bad selected frequencies from `O(beta^2 n)` to `o(sqrt(n))` and then close them by (8.1), rather than demanding exact flatness at the Gibbs stage.
