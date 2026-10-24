Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run model/reasoning telemetry is unavailable, so I do not claim otherwise.**

# P06 complementary P07 iteration — fixed-projector leakage and a genuine second finite-model square-Newton contraction near the sharp boundary

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.  
Captured pre-write `master`: `951d31a5a028f53568ed04cdae3fd6539394be48`.  
Previous own checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T0838+0300__gaussian_hermite_second_step.md`, creation commit `e956fedd24de8521b1ae1fb293494555d612837f`, readback blob `d2547fc411492e12af384f4b3cc1064a3d968153`.

The outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed. The new result is narrower but genuinely finite-model: the fixed selected Fourier projector does **not** destroy the second positive square-Newton step near the sharp source boundary. More precisely, after strengthening the vanishing tilt just enough to control the finite low-degree convolution dictionary, the first updated covariance has an `O(delta)` off-plane block, the actual next third-cumulant vector has `O(delta)` off-plane leakage, and the **actual finite-model second skew test** satisfies `A_{1,n}<1/2` for every sufficiently small fixed source slack.

The previous report proved this only in a calibrated two-chaos Gaussian/Hermite surrogate. This report removes that surrogate dependence for the second step.

Here and below `delta=1-beta`, where

\[
beta={d\over1+\sqrt{1-d^2}},\qquad d={1\over1+\epsilon}.
\]

The exact relation is

\[
\boxed{
\epsilon={1\over d}-1={ (1-\beta)^2\over2\beta}
={\delta^2\over2(1-\delta)}.
}
\tag{0.1}
\]

Thus `delta downarrow 0` is exactly the sharp source limit `epsilon downarrow 0`, with `delta asymp sqrt(2 epsilon)`.

---

# 1. Strengthening the vanishing seed only as much as the higher-chaos step needs

The earlier decrement/skew work used

\[
c_n=n^{-1/3}.
\]

For the present fixed-projector calculation it is useful to take instead

\[
\boxed{c_n=n^{-9/20}.}
\tag{1.1}
\]

Nothing in the first-step argument requires the exponent `1/3`. The three properties actually used are

\[
c_n\to0,\qquad c_n\sqrt n\to\infty,
\qquad c_n\sqrt{\log n}\to0.
\tag{1.2}
\]

They still hold for (1.1). Consequently:

* the singular point `j=0` has relative Gibbs weight
  \[
  \exp[-\Omega(c_n\sqrt n)]
  =\exp[-\Omega(n^{1/20})];
  \tag{1.3}
  \]
* on all nonzero time points, the Gibbs density is uniformly
  \[
  1+O(n^{-9/20}\sqrt{\log n})
  \tag{1.4}
  \]
  relative to the nonzero-uniform law;
* the covariance and inverse covariance are the same relative perturbation of the exact compound-symmetry matrix `Sigma_*`;
* the initial decrement and first skew conclusions remain
  \[
  \nu_{0,n}^2=d^2+o(1),\qquad
  \Gamma_{0,n}^2=1+o(1)
  \tag{1.5}
  \]
  with the inherited source-sufficient failure probability.

The reason for (1.1) is higher moments. If a selected cosine coefficient vector has Euclidean error `rho_n`, its trigonometric polynomial satisfies, by interpolation between `L^2` and `L^infty`,

\[
\|F\|_{L^p(u_*)}
\le C_p n^{1/2-1/p}\rho_n.
\tag{1.6}
\]

Here `rho_n=O(n^{-9/20}\sqrt{\log n})`. Therefore

\[
\boxed{
\|F\|_{L^p(u_*)}=o(1)
\quad\hbox{for every fixed }p<20.
}
\tag{1.7}
\]

In particular all `L^p` errors through `p=16`, which are enough for the finite dictionary below, vanish. The previous `n^{-1/3}` choice only gave this interpolation for `p<6` and therefore was insufficient for a clean fixed-projector Taylor expansion.

This is a strengthening of the same vanishing-tilt route, not a different source claim.

---

# 2. Whitened base state and the canonical two-plane

Work under the strengthened vanishing Gibbs law `p_n`. Write

\[
Y=\Sigma_0^{-1/2}(\Phi_D-\mu_0),
\qquad
\mathbf E Y=0,
\qquad
\mathbf E YY^T=I.
\tag{2.1}
\]

Let `r_0=mu_0-t` be the target residual and

\[
h_0=-\Sigma_0^{-1}r_0,
\qquad
g_0=h_0^T(\Phi_D-\mu_0),
\qquad
\nu_0^2=\mathbf E g_0^2.
\]

Define the unit whitened Newton direction `e` and normalized score `Z` by

\[
Z={g_0\over\nu_0}=e^TY,
\qquad \|e\|_2=1.
\tag{2.2}
\]

Because `h_0` is the exact Newton vector, the whitened residual is exactly

\[
\Sigma_0^{-1/2}r_0=-\nu_0e.
\tag{2.3}
\]

Set

\[
m_2:=\mathbf E[YZ^2].
\tag{2.4}
\]

The inherited first-step skew theorem gives

\[
\|m_2\|_2^2=\Gamma_{0,n}^2=1+o(1),
\qquad
e^Tm_2=\mathbf EZ^3=o(1).
\tag{2.5}
\]

Let

\[
f={m_2-(e^Tm_2)e\over
\|m_2-(e^Tm_2)e\|_2},
\qquad
\mathcal S=\operatorname{span}\{e,f\},
\qquad P=P_{\mathcal S},\quad P^\perp=I-P.
\tag{2.6}
\]

Put

\[
U=f^TY.
\tag{2.7}
\]

Thus `m_2 in S` **exactly**. The previous report's identity

\[
U={Z^2-1\over2}+V,
\qquad \|V\|_2^2={1\over2}+o(1)
\tag{2.8}
\]

remains available, but this report does not assume that `V` is Gaussian or independent of `Z`.

---

# 3. A finite fixed-word convolution envelope

The new higher-chaos estimates use only a finite set of scalar words and their selected Fourier projections. The needed words are generated by

\[
Z,\quad Z^2,\quad Z^3,\quad Z^4,\quad
U,\quad UZ,\quad U(Z^2-1),
\tag{3.1}
\]

and by the projections of `Z^2` and `Z^3` back to the selected feature space.

The following lemma is the technical input that replaces any uniform hypercontractivity assertion over the whole selected Fourier subspace.

## Lemma 3.1 — fixed-word collision envelope

There is an absolute constant `K<infty` such that, outside an event of probability

\[
O(n^{-1})+\exp[-\Omega(n^{1/20})],
\tag{3.2}
\]

the following quantities are all at most `K`:

\[
\mathbf E|Z|^{16},
\tag{3.3}
\]

\[
\|\mathbf E[Y(Z^3-Z)]\|_2,
\qquad
\|\mathbf E[Y(Z^4-Z^2)]\|_2,
\tag{3.4}
\]

\[
\|\mathbf E[YUZ]\|_2,
\qquad
\|\mathbf E[YU(Z^2-1)]\|_2,
\tag{3.5}
\]

and, with

\[
U_2=m_2^TY,
\qquad
A_3=\mathbf E[YZ^3],
\qquad
U_3=A_3^TY,
\tag{3.6}
\]

\[
\mathbf E[Z^2U_2^2],
\qquad
\mathbf E[Z^2U_3^2].
\tag{3.7}
\]

The same statement holds after inserting `P` or `P^perp` on any coefficient vector.

### Proof

It is enough, by (1.4)--(1.7) and the bounded condition number of the nonzero-uniform covariance, to prove the estimates for the flat nonzero-uniform model.

Extend the mask to the symmetric Rademacher sequence

\[
e_0=0,\qquad e_a=e_{-a}=\varepsilon_{|a|},
\]

and write

\[
Q=e*e,
\qquad
C=e*e*e.
\tag{3.8}
\]

The flat normalized score is, up to a harmless sign and the deleted origin,

\[
Z_*(j)=n^{-1/2}\sum_{x\ne0}e_x\omega^{jx}.
\tag{3.9}
\]

Hence the selected Fourier coefficient of `Z_*^k` is a normalized `k`-fold cyclic convolution of `e`. In particular the new cubic coefficient array is

\[
C_a=\sum_{x,y}e_xe_ye_{a-x-y}.
\tag{3.10}
\]

The correlation-count lemma in the preceding convolution report is exactly the statement

\[
\mathbf E C_a^2=O(n^2)
\tag{3.11}
\]

uniformly in `a`, because its `T_r` differs from (3.10) only by signed reindexing. Therefore the normalized selected cubic projection has aggregate squared coefficient norm `O(1)`.

The second-chaos direction has coefficients proportional to the centered selected restriction of `Q`; the inherited theorem

\[
{1\over n^2}
\sum_{a\in D}(Q_a-\bar Q_D)^2
={1\over2}+o(1)
\tag{3.12}
\]

already gives its normalization.

For the remaining words, expand every selected coefficient in independent mask Rademachers. Each coefficient is a finite sum of Walsh characters with at most eight occurrences of quotient classes `[x]={x,-x}` and with a fixed number of cyclic additive constraints. In a squared coefficient norm, a term has nonzero mask expectation only when every quotient class has even parity. For a generic tuple this pairs the two copies up to one of finitely many permutations and signs; the normalization in (3.9) leaves `O(1)` total mass. Degenerate identifications satisfy an additional signed affine relation and therefore lose at least one free cyclic parameter. Because the degree is fixed, every nonzero integer minor of the resulting finite linear systems has bounded absolute determinant, so even on composite odd `n` its kernel multiplicity is bounded by that determinant and cannot grow with `n`.

For the variance of each aggregate empirical moment, subtract the product of expectations and repeat the same expansion with two copies. The disconnected parity diagrams cancel. Every surviving connected diagram contains at least one additional independent signed affine relation, hence has one fewer free cyclic parameter. Consequently

\[
\operatorname{Var}(F_n)=O(n^{-1})
\tag{3.13}
\]

for every normalized scalar aggregate `F_n` appearing in (3.3)--(3.7). The number of parity/sign patterns is finite because the maximum degree is fixed. Chebyshev gives a common constant bound with failure `O(n^{-1})`.

This is the same Walsh/additive-collision mechanism as the proved `Q`-energy theorem; it is applied here only to the finite dictionary (3.1), not to arbitrary directions in the selected Fourier space. Finally (1.4)--(1.7) transfer the bounds from the flat model to the actual strengthened vanishing Gibbs seed. ∎

Combining (3.2) with the inherited `Q`-energy failure gives throughout the rest of this report

\[
\boxed{
q_n=O\!\left({(\log n)^{1/4}\over n}\right)
+\exp[-\Omega(n^{1/20})]
=o\!\left({1\over\sqrt{\log n}}\right).
}
\tag{3.14}
\]

---

# 4. Exact fixed-projector covariance leakage after the first regularized square step

Let

\[
\alpha={1\over1+\sqrt{1-\nu_0^2}},
\qquad
\beta_n=\alpha\nu_0.
\tag{4.1}
\]

The first positive square law has density `(1+beta_n Z)^2/(1+beta_n^2)` relative to the base law. Mix back a fraction

\[
\eta_n={A_{0,n}\over1-A_{0,n}},
\tag{4.2}
\]

where `A_{0,n}` is the inherited first skew parameter. Since `nu_0->d` and `Gamma_0->1`,

\[
\beta_n\to\beta,
\qquad
\eta_n\to\eta:={\beta\over2-\beta}.
\tag{4.3}
\]

Write `lambda_n=1-eta_n`. The mixed density relative to the base law is **exactly**

\[
w_n(Z)=1+u_nZ+v_n(Z^2-1),
\tag{4.4}
\]

with

\[
u_n={2\lambda_n\beta_n\over1+\beta_n^2},
\qquad
v_n={\lambda_n\beta_n^2\over1+\beta_n^2}.
\tag{4.5}
\]

At the deterministic limit,

\[
\boxed{
 u={4\beta(1-\beta)\over(2-\beta)(1+\beta^2)},
\qquad
 v={2\beta^2(1-\beta)\over(2-\beta)(1+\beta^2)}.
}
\tag{4.6}
\]

For `delta=1-beta`,

\[
u=2\delta+O(\delta^2),
\qquad
v=\delta+O(\delta^2),
\qquad
\eta=1-2\delta+O(\delta^2).
\tag{4.7}
\]

The new mean in the old whitened coordinates is exactly

\[
m_1=\mathbf E[w_nY]=u_ne+v_nm_2\in\mathcal S.
\tag{4.8}
\]

Let `C_1` be the covariance under the mixed law, still expressed in the old whitened coordinates. Since `m_1 in S`, the mean subtraction has no `S^perp x S` block. Directly from (4.4),

\[
\boxed{
P^\perp C_1e
=v_nP^\perp\mathbf E[Y(Z^3-Z)].
}
\tag{4.9}
\]

The potentially order-`u_n` term cancels because `E[YZ^2]=m_2 in S` exactly.

Likewise, with `U=f^TY`,

\[
\boxed{
P^\perp C_1f
=u_nP^\perp\mathbf E[YUZ]
+v_nP^\perp\mathbf E[YU(Z^2-1)].
}
\tag{4.10}
\]

Lemma 3.1 therefore yields the requested fixed-projector covariance estimate

\[
\boxed{
L_n:=\|P^\perp C_1P\|_{op}
=O_{\mathbf P}(\delta)+o_{\mathbf P}(1)
}
\tag{4.11}
\]

with the source-sufficient failure (3.14).

This is the first half of the leakage target in the previous checkpoint. No fresh-half-projection model is used; the projector is the actual fixed selected Fourier feature space.

---

# 5. A global finite-model fact: the second decrement stays below one for every fixed source slack

The covariance of a mixture satisfies the exact floor

\[
C_1\succeq\eta_n I.
\tag{5.1}
\]

The square-cancellation identity also gives the mixed residual directly. In the old whitened coordinates,

\[
r_1=-\eta_n\nu_0e
+(1-\eta_n){\alpha\nu_0^2\over2}m_2.
\tag{5.2}
\]

At the deterministic limit, the second coefficient is exactly `v` from (4.6). Since `||m_2||^2->1` and `e^Tm_2->0`, (5.1)--(5.2) imply

\[
\limsup_{n\to\infty}\nu_{1,n}^2
\le
B(\beta),
\tag{5.3}
\]

where

\[
\boxed{
B(\beta)
={4\beta^3(\beta^2-2\beta+2)
\over(2-\beta)(1+\beta^2)^2}.
}
\tag{5.4}
\]

The gap factors exactly:

\[
\boxed{
1-B(\beta)
={(1-\beta)(5\beta^4-5\beta^3+5\beta^2+\beta+2)
\over(2-\beta)(1+\beta^2)^2}>0
}
\tag{5.5}
\]

for every `0<beta<1`, because

\[
5\beta^4-5\beta^3+5\beta^2+\beta+2
=5\beta^2(\beta^2-\beta+1)+\beta+2>0.
\]

Thus:

## Theorem 5.1 — second decrement preservation

For every fixed `d<1`, the actual finite-model state after the first covariance-regularized square update satisfies

\[
\boxed{
\limsup_{n\to\infty}\nu_{1,n}^2<1
}
\tag{5.6}
\]

on the good event (3.14).

Near the sharp boundary,

\[
B(1-\delta)=1-2\delta+2\delta^2-3\delta^3+O(\delta^4).
\tag{5.7}
\]

In particular, for all sufficiently small fixed `delta`,

\[
\boxed{
\nu_{1,n}^2\le1-\delta+o(1).
}
\tag{5.8}
\]

This conclusion is **not** a surrogate statement. It uses only the exact mixture covariance floor and the already-proved finite-model first skew calibration.

A matching coarse lower bound is also available. By the variational inequality

\[
r^TC^{-1}r\ge{(r^Te)^2\over e^TCe},
\tag{5.9}
\]

the exact density (4.4), `EZ^3=o(1)`, and `EZ^4=3+o(1)` give

\[
\boxed{
\nu_{1,n}^2\ge1-C\delta+o(1)
}
\tag{5.10}
\]

for an absolute `C` and small fixed `delta`.

Hence the next decrement is still near one, but its gap from one is at least order `delta`.

---

# 6. The actual next Newton direction has only `O(delta)` off-plane mass

Block the new covariance relative to `S plus S^perp`:

\[
C_1=
\begin{pmatrix}
A&B^T\\
B&D
\end{pmatrix}.
\tag{6.1}
\]

The residual (5.2) belongs to `S` exactly. By (5.1),

\[
D\succeq\eta_nI.
\tag{6.2}
\]

The within-plane block satisfies

\[
A=I_2+O_{\mathbf P}(\delta)+o_{\mathbf P}(1)
\tag{6.3}
\]

because every entry is one of the fixed scalar moments in Lemma 3.1. By (4.11),

\[
\|B\|_{op}=O_{\mathbf P}(\delta)+o_{\mathbf P}(1).
\tag{6.4}
\]

Let the actual next Newton coefficient in old whitened coordinates be

\[
h_1=-C_1^{-1}r_1=h_{1,S}+h_{1,\perp}.
\]

The block equations give

\[
h_{1,\perp}=-D^{-1}Bh_{1,S}.
\tag{6.5}
\]

Since the Schur complement differs from `I_2` by `O(delta)+o(1)`, `||h_{1,S}||=O(1)`, and hence

\[
\boxed{
\|h_{1,\perp}\|_2
=O_{\mathbf P}(\delta)+o_{\mathbf P}(1).
}
\tag{6.6}
\]

More is true at first order. Put

\[
A_3:=\mathbf E[YZ^3].
\tag{6.7}
\]

As `delta downarrow0` after `n to infinity`, the exact Taylor expansion of the Newton equation gives

\[
\boxed{
h_1=e+\delta k+O_{\mathbf P}(\delta^2)+o_{\mathbf P}(1),
\qquad
k=-(e+3m_2+A_3).
}
\tag{6.8}
\]

Indeed the first covariance derivative is

\[
K=2\mathbf E[YY^TZ]
+\mathbf E[YY^T(Z^2-1)],
\]
so

\[
Ke=2m_2+(A_3-e),
\]
while the residual derivative is `2e+m_2`; solving `k+Ke=-(2e+m_2)` gives (6.8).

The off-plane first derivative is therefore exactly the selected cubic-convolution leakage

\[
\boxed{
P^\perp k=-P^\perp A_3.
}
\tag{6.9}
\]

In the flat mask model its Fourier coefficients are normalized restrictions of

\[
C=e*e*e,
\]
which is why the old `T_r` correlation count already had the correct scale for this step.

---

# 7. Exact first derivative of the next third-cumulant vector

Let

\[
g_1=h_1^T(Y-m_1)
\]

be the actual next Newton score, and let

\[
\tau_1=\mathbf E_{w_n}[(Y-m_1)g_1^2].
\tag{7.1}
\]

The fixed-word envelope permits a genuine coefficient-space Taylor expansion, not merely a scalar moment expansion. Put

\[
a_3=\mathbf EZ^3=o(1)
\]

and

\[
A_{42}:=\mathbf E[Y(Z^4-Z^2)].
\tag{7.2}
\]

Using

\[
w_n=1+\delta\{2Z+(Z^2-1)\}+O(\delta^2),
\]

\[
m_1=\delta(2e+m_2)+O(\delta^2),
\]

and (6.8), a direct expansion gives

\[
\boxed{
\tau_1
=m_2+\delta\Xi
+O_{\mathbf P}(\delta^2)+o_{\mathbf P}(1),
}
\tag{7.3}
\]

where

\[
\boxed{
\Xi=
2A_3+A_{42}
+2\mathbf E\big[Y Z(k^TY)\big]
-(6+2a_3)e-m_2,
}
\tag{7.4}
\]

and `k` is (6.8).

Projecting away the canonical two-plane removes the explicit longitudinal terms and `m_2`. Since

\[
k=-(e+3m_2+A_3),
\]

one obtains the explicit leakage formula

\[
\boxed{
\begin{aligned}
P^\perp\Xi={}&
2P^\perp A_3
+P^\perp A_{42}\\
&-6P^\perp\mathbf E[Y Z(m_2^TY)]
-2P^\perp\mathbf E[Y Z(A_3^TY)].
\end{aligned}
}
\tag{7.5}
\]

Every term in (7.5) is one of the fixed convolution words controlled in Lemma 3.1. Therefore

\[
\boxed{
\|P^\perp\tau_1\|_2
=O_{\mathbf P}(\delta)+o_{\mathbf P}(1).
}
\tag{7.6}

Moreover, since `||m_2||=1+o(1)`, the full vector obeys

\[
\boxed{
\|\tau_1\|_2^2
\le1+C\delta+o(1)
}
\tag{7.7}
\]

for an absolute constant `C` and all sufficiently small fixed `delta`.

Because `C_1 succeq eta_n I`, (7.7) implies

\[
\tau_1^TC_1^{-1}\tau_1
\le1+C\delta+o(1).
\tag{7.8}
\]

Combining this with the lower decrement estimate (5.10),

\[
\boxed{
\Gamma_{1,n}^2
={\tau_1^TC_1^{-1}\tau_1\over\nu_{1,n}^4}
\le1+C_1\delta+o(1)
}
\tag{7.9}
\]

for another absolute constant `C_1`.

Equations (4.11) and (7.6) are the concrete fixed-projector leakage estimates requested by the preceding checkpoint. In particular, the normalized off-plane skew energy is

\[
\boxed{
\|P^\perp\tau_1\|_{C_1^{-1}}^2
=O_{\mathbf P}(\delta^2)+o_{\mathbf P}(1),
}
\tag{7.10}
\]

because `C_1 succeq eta_n I` and `eta_n->1` as `delta downarrow0`.

---

# 8. Main new theorem: a genuine second finite-model contraction for sufficiently sharp fixed slack

Recall

\[
A_{1,n}
={\Gamma_{1,n}\nu_{1,n}
\over2(1+\sqrt{1-\nu_{1,n}^2})}.
\tag{8.1}
\]

From (5.8), for small fixed `delta`,

\[
1-\nu_{1,n}^2\ge\delta+o(1).
\tag{8.2}
\]

From (7.9),

\[
\Gamma_{1,n}\nu_{1,n}
\le1+C_2\delta+o(1).
\tag{8.3}
\]

Therefore

\[
\boxed{
A_{1,n}
\le
{1+C_2\delta+o(1)
\over2(1+\sqrt{\delta+o(1)})}.
}
\tag{8.4}
\]

Since `sqrt(delta)` dominates `delta` as `delta downarrow0`, there exists an absolute `delta_0>0` such that for every fixed

\[
0<\delta<\delta_0,
\tag{8.5}
\]

one has, for all sufficiently large `n` outside the source-sufficient failure event (3.14),

\[
\boxed{A_{1,n}<1/2.}
\tag{8.6}
\]

By (0.1), this is equivalent to the existence of `epsilon_0>0` such that for every fixed source slack

\[
0<\epsilon<\epsilon_0,
\]

the actual finite random-circulant model admits a **second covariance-regularized positive square-Newton contraction step** with failure

\[
q_n=o(1/\sqrt{\log n}).
\tag{8.7}
\]

This is strictly stronger than the previous report's surrogate theorem: the second contraction is now proved for the actual fixed selected Fourier projector, albeit only in a sufficiently sharp fixed-slack neighborhood of the source endpoint.

No finite SDP experiment is used.

---

# 9. What moved and what did not

## Fixed full-source bound

Unchanged:

\[
\sqrt n\le\mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full P07 solution is claimed.

## Intermediate obligation ledger

1. **First-step decrement and skew**  
   Preserved:
   \[
   \nu_{0,n}^2=d^2+o(1),\qquad \Gamma_{0,n}^2=1+o(1).
   \]

2. **Higher-moment seed control**  
   Before: `c_n=n^{-1/3}` only yielded a crude interpolation through moments below order six.  
   After: **PROVED PARTIAL** that `c_n=n^{-9/20}` preserves the old source-sufficient first-step estimates while giving `L^p` flat-score transfer for every fixed `p<20`.

3. **Fixed-projector covariance leakage**  
   Before: open.  
   After: **PROVED** near the source boundary:
   \[
   \|P^\perp C_1P\|_{op}=O_P(\delta)+o_P(1).
   \]
   Exact columns are (4.9)--(4.10).

4. **Second decrement**  
   Before: proved only in the Gaussian/Hermite surrogate.  
   After: **PROVED FINITE-MODEL** that for every fixed `d<1`,
   \[
   \limsup\nu_{1,n}^2\le B(\beta)<1.
   \]

5. **Actual second-step skew leakage**  
   Before: open.  
   After: **PROVED** for small fixed source slack:
   \[
   \|P^\perp\tau_1\|_{C_1^{-1}}^2
   =O_P(\delta^2)+o_P(1),
   \qquad
   \Gamma_{1,n}^2\le1+O(\delta)+o(1).
   \]

6. **Actual second contraction**  
   Before: surrogate only.  
   After: **PROVED FINITE-MODEL** for every sufficiently small fixed `epsilon>0`, with failure `o(1/sqrt(log n))`.

7. **Order restriction**  
   The collision proof above is written for odd cyclic order. Fixed-degree composite resonances are controlled by bounded integer minors in the diagram count, so no primality assumption is used. Even order still has the additional self-inverse frequency and is not removed in this report.

---

# 10. Remaining gap and next attack

The source theorem is still open because two successful positive corrections do not yet produce an exact feasible moment vector.

The new picture near the source boundary is favorable. With `delta=1-beta`, the first regularized measure change is only `O(delta)`, while the second-step safety margin generated by the decrement gap is order `sqrt(delta)`. Thus the fixed-projector leakage is one full power smaller than the available nonlinear margin.

The next attack should exploit this **square-root escape from the boundary** rather than recompute another two-dimensional surrogate.

A concrete route is:

1. Prove a one-step stability lemma for a general state satisfying
   \[
   \nu^2\le1-\rho,
   \qquad
   \Gamma^2\le1+C\rho,
   \]
   whose density relative to the strengthened vanishing seed is a fixed positive polynomial in the existing low-degree convolution dictionary.
2. Show that the covariance-regularized square update moves the density by `O(sqrt(rho))` but creates the next decrement gap at least `c sqrt(rho)`.
3. Extend Lemma 3.1 to whatever **finite** convolution degree is generated by that one step. For each fixed source slack, only finitely many degrees are needed; constants may depend on the fixed slack because the source expectation argument takes `n to infinity` before `epsilon downarrow0`.
4. Seek the recursive boundary scale
   \[
   \rho_{k+1}\gtrsim\sqrt{\rho_k}
   \]
   until the decrement enters a coarse regime bounded away from one. The number of near-boundary steps would then be only `O(log log(1/epsilon))` for each fixed `epsilon`.
5. Once in the coarse regime, use a fixed damping/regularization constant and attempt a compact invariant region with geometric residual decay.

If the square-root escape recursion can be made rigorous with the same source-sufficient failure `o(1/sqrt(log n))`, it would give exact positive moment feasibility for every fixed `epsilon>0`. The published fallback would then transfer this to

\[
\mathbf E\vartheta(G_n)\le(1+\epsilon+o(1))\sqrt n,
\]

and finally `epsilon downarrow0` would reach the source endpoint.

The obstruction is therefore no longer the first or second finite step. It is a **multi-step invariant-region theorem for a growing but finite convolution dictionary**.
