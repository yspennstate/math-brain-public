# QFORM B17: global compound-Poisson fragmentation barrier

Run: `20260923T033115Z-account03-B17-QFORM-r24`  
Account/slot: `account03/B17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `NEW_SUPPORTING_THEOREM`; full conjecture OPEN; full-target continuity OPEN; `WITHOUT_VERIFIED_BRAIN`.

## 1. Purpose and exact target

The owner target is unchanged: for every dimension, independent real inputs whose probability densities satisfy `0<=f_i<=1`, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-supremum bound for the density of `Q=X^TAX`, or give a valid counterexample. No moment, support, log-concavity, or post-rotation independence assumption is allowed.

This run tests a sharp-witness mechanism left open by earlier B17 work: **order `1/m` remote fragmented mass at distance `Theta(sqrt(m))`** in the exact fully rotated three-bank witness. Unlike the preceding `1/m^2` perturbation, this regime has order-one many remote hits per bank and therefore a nontrivial compound-Poisson limit. The question is whether such fragmentation can raise the global density peak above the known obstruction `3 sqrt(2)`.

The answer is no for this exact source-valid architecture. In fact the limiting global density is bounded by a strict factor below `3 sqrt(2)`. The proof has two pieces: a global noncentral-Gaussian quadratic density theorem, and a uniform local-limit transfer that rules out hidden finite-`m` spikes.

## 2. Completed designated-partner result used

The completed designated partner `account04/B17` proved at

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`

that, with

\[
J=\operatorname{diag}(1,1,-1),\qquad
O={1\over7}\begin{pmatrix}6&-2&-3\\-2&3&-6\\-3&-6&-2\end{pmatrix},
\]

and

\[
B=O^TJO={1\over49}\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix},
\tag{2.1}
\]

the centered-uniform three-bank form has exact nonzero spectrum `{1,1,-1}`, is genuinely rotated, and obeys

\[
p_{Q_m^{\rm partner}}(0)
=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right).
\tag{2.2}
\]

Hence every universal constant for the owner's target satisfies

\[
\boxed{C_*\ge3\sqrt2.}
\tag{2.3}
\]

The partner also supplies the weighted local Edgeworth estimate for the normalized centered-uniform bank density `g_m`, with `sigma^2=1/12`:

\[
g_m(y)=\gamma_\sigma(y)
\left[1-{1\over20m}H_4(y/\sigma)\right]
+O(m^{-2})(1+|y|)^{-8}.
\tag{2.4}
\]

I use both (2.2) and the local-limit content of (2.4) below.

## 3. New global theorem: mean shifts cannot beat the centered Gaussian cone

### Theorem 3.1

Let `G~N(h,v I_3)`, `v>0`, and

\[
S_h=G_1^2+G_2^2-G_3^2.
\]

Define

\[
C_0={1\over2\sqrt2\,v},
\qquad
\rho={\sqrt2\,\Gamma(3/4)\over2\sqrt\pi\,\Gamma(5/4)}
={4\sqrt\pi\over\Gamma(1/4)^2}.
\tag{3.1}
\]

Then `S_h` has a bounded continuous density and

\[
\boxed{
\|p_{S_h}\|_\infty
\le C_0\left[
\rho+(1-\rho)e^{-\|h\|^2/(2v)}
\right].
}
\tag{3.2}
\]

Moreover `0<rho<1`, so every nonzero deterministic mean shift has a strict global gap from the centered ceiling `C_0`.

At the density-one Gaussian variance floor `v=1/12`,

\[
C_0=3\sqrt2,
\qquad
\|p_{S_h}\|_\infty
\le3\sqrt2\left[
\rho+(1-\rho)e^{-6\|h\|^2}
\right].
\tag{3.3}
\]

### Proof

Put

\[
\alpha={h_1^2+h_2^2\over v},\qquad
\beta={h_3^2\over v}.
\]

By the standard Poisson mixture for noncentral chi-square laws,

\[
{G_1^2+G_2^2\over v}\mid K=k\sim\chi^2_{2+2k},
\qquad
{G_3^2\over v}\mid L=l\sim\chi^2_{1+2l},
\]

where

\[
K\sim\operatorname{Pois}(\alpha/2),
\qquad
L\sim\operatorname{Pois}(\beta/2)
\]

are independent. Hence `S_h` is a convex mixture of

\[
D_{k,l}=v(U_k-V_l),
\quad
U_k\sim\chi^2_{2+2k},
\quad
V_l\sim\chi^2_{1+2l}.
\tag{3.4}
\]

The weight of `(k,l)=(0,0)` is exactly

\[
w_0=e^{-(\alpha+\beta)/2}=e^{-\|h\|^2/(2v)}.
\tag{3.5}
\]

For the central component, let `D=chi^2_2-chi^2_1`. For `x>=0`, direct convolution with the exponential `chi^2_2` density gives

\[
p_D(x)={e^{-x/2}\over2\sqrt2}.
\tag{3.6}
\]

For `x=-r<0`,

\[
p_D(-r)={e^{r/2}\over2\sqrt2}\,\operatorname{erfc}(\sqrt r)
\le {1\over2\sqrt2},
\tag{3.7}
\]

using `erfc(x)<=e^{-x^2}` for `x>=0`. Therefore

\[
\|p_{D_{0,0}}\|_\infty=C_0.
\tag{3.8}
\]

Now suppose `k+l>=1`. The characteristic function of (3.4) has modulus

\[
|\phi_{k,l}(t)|
=(1+4v^2t^2)^{-3/4-(k+l)/2}
\le(1+4v^2t^2)^{-5/4}.
\tag{3.9}
\]

Fourier inversion therefore yields

\[
\begin{aligned}
\|p_{D_{k,l}}\|_\infty
&\le{1\over2\pi}
\int_{\mathbb R}(1+4v^2t^2)^{-5/4}\,dt\\
&={\Gamma(3/4)\over4\sqrt\pi\,\Gamma(5/4)\,v}
=\rho C_0.
\end{aligned}
\tag{3.10}
\]

Taking the convex mixture and using (3.5), (3.8), and (3.10) gives (3.2).

Finally, the reflection formula and `Gamma(5/4)=Gamma(1/4)/4` give

\[
\rho={4\sqrt\pi\over\Gamma(1/4)^2}.
\tag{3.11}
\]

Also

\[
\Gamma(1/4)
=\int_0^\infty t^{-3/4}e^{-t}\,dt
>\int_0^1t^{-3/4}(1-t)\,dt={16\over5},
\]

so

\[
\rho<{4\sqrt\pi\over(16/5)^2}<1.
\]

This completes the proof. `□`

### Comment on scope

The theorem is only about isotropic Gaussian inputs after a deterministic mean shift. It is not being substituted for the arbitrary-law QFORM target. Its role is to evaluate exactly the conditional limits generated by the source-valid fragmented product family below.

## 4. Exact source-valid order-1/m fragmented family

Fix constants `a>0` and `c>0`. For all sufficiently large `m` with `c/m<1` and `a sqrt(m)>1`, define the one-dimensional density

\[
\begin{aligned}
f_m(x)=&\left(1-{c\over m}\right)\mathbf 1_{[-1/2,1/2]}(x)\\
&+{c\over2m}\mathbf 1_{[a\sqrt m-1/2,a\sqrt m+1/2]}(x)\\
&+{c\over2m}\mathbf 1_{[-a\sqrt m-1/2,-a\sqrt m+1/2]}(x).
\end{aligned}
\tag{4.1}
\]

The three intervals are disjoint for large `m`. Thus

\[
0\le f_m\le1,
\qquad
\int f_m=1.
\tag{4.2}
\]

Equivalently,

\[
X_{jk}=U_{jk}+a\sqrt m\,\xi_{jk},
\tag{4.3}
\]

where `U_{jk}~Unif[-1/2,1/2]` and, independently,

\[
\Pr(\xi_{jk}=0)=1-{c\over m},
\qquad
\Pr(\xi_{jk}=\pm1)={c\over2m}.
\tag{4.4}
\]

Take `3m` mutually independent copies, grouped in three banks. Let `v_j=Oe_j`, repeat physical row `v_j/sqrt(m)` for bank `j`, and let `R_m` be the resulting `3m x 3` frame. Then

\[
R_m^TR_m=I_3,
\qquad
A_m=R_mJR_m^T
\tag{4.5}
\]

has exact nonzero spectrum

\[
\boxed{\{1,1,-1\}}
\tag{4.6}
\]

for every finite `m`. Since all entries of `B=O^TJO` in (2.1) are nonzero, the physical three-bank form is genuinely coupled.

Write

\[
Y_{mj}=m^{-1/2}\sum_{k=1}^mX_{jk}
=G_{mj}+aT_{mj},
\tag{4.7}
\]

where

\[
G_{mj}=m^{-1/2}\sum_{k=1}^mU_{jk},
\qquad
T_{mj}=\sum_{k=1}^m\xi_{jk}.
\tag{4.8}
\]

The output is exactly

\[
Q_m=Y_m^TBY_m.
\tag{4.9}
\]

As `m->infinity`, each `T_{mj}` converges in total variation to

\[
T_j=N_{j,+}-N_{j,-},
\qquad
N_{j,+},N_{j,-}\stackrel{ind}{\sim}\operatorname{Pois}(c/2),
\tag{4.10}
\]

and the three limiting `T_j` are independent. For example, applying Le Cam first to the number of nonzero marks gives total variation `O(c^2/m)`; attaching the independent fair signs is a Markov kernel and cannot increase total variation.

Meanwhile the partner's (2.4) implies

\[
\|g_m-\gamma_\sigma\|_1=O(m^{-1}),
\qquad \sigma^2={1\over12},
\tag{4.11}
\]

for the one-bank density `g_m`.

The weak limit is therefore

\[
Q_\infty=(G+aT)^TB(G+aT),
\quad
G\sim N(0,I_3/12),
\tag{4.12}
\]

with `G` independent of the Skellam vector `T`.

## 5. Uniform local-limit transfer: no hidden finite-m spike

Weak convergence alone does not control density suprema, so a separate uniform transfer is needed.

### Lemma 5.1

For the bank densities in (4.8), uniformly over every deterministic shift `h in R^3`, the density of

\[
(G_m+h)^TB(G_m+h)
\]

converges uniformly in the output variable to the density of

\[
(G+h)^TB(G+h),
\quad G\sim N(0,I_3/12).
\]

In symbols,

\[
\boxed{
\sup_{h\in\mathbb R^3}
\|p_{m,h}-p_{\infty,h}\|_\infty\to0.
}
\tag{5.1}
\]

### Proof

The one-dimensional bank characteristic function is

\[
\widehat g_m(\xi)=\operatorname{sinc}\!\left({\xi\over2\sqrt m}\right)^m.
\tag{5.2}
\]

Using

\[
|\operatorname{sinc}u|\le e^{-u^2/6}\quad(|u|\le1),
\qquad
|\operatorname{sinc}u|\le|u|^{-1}\quad(|u|\ge1),
\]

we obtain for `m>=3`

\[
\|\widehat g_m\|_1
=2\sqrt m\int_{\mathbb R}|\operatorname{sinc}u|^mdu
\le2\sqrt{6\pi}+{4\sqrt m\over m-1}.
\tag{5.3}
\]

Thus the Fourier `L^1` norm is uniformly bounded.

Let

\[
a_{m,h}(y)=\prod_{j=1}^3g_m(y_j-h_j),
\qquad
a_{\infty,h}(y)=\prod_{j=1}^3\gamma_\sigma(y_j-h_j).
\]

Translations do not change Fourier absolute values, so

\[
\sup_{m,h}\|\widehat a_{m,h}\|_1<\infty.
\tag{5.4}
\]

The exact Fresnel transform for the nonsingular quadratic phase `y^TBy`, with `|det B|=1`, gives after harmless Gaussian regularization

\[
\left|\int e^{it y^TBy}a_{m,h}(y)dy\right|
\le C|t|^{-3/2}\|\widehat a_{m,h}\|_1.
\tag{5.5}
\]

Together with the trivial bound one, this yields a uniform integrable envelope

\[
|\phi_{m,h}(t)|\le C'\min(1,|t|^{-3/2})
\tag{5.6}
\]

for every `m,h`; the same holds for the Gaussian limit. This is a statement for the present smooth bank densities and does **not** assert the refuted law-uniform pointwise van-der-Corput estimate.

From (4.11), by telescoping the three products,

\[
\sup_h\|a_{m,h}-a_{\infty,h}\|_1
\le3\|g_m-\gamma_\sigma\|_1=:\delta_m\to0.
\tag{5.7}
\]

Therefore

\[
|\phi_{m,h}(t)-\phi_{\infty,h}(t)|\le\delta_m
\tag{5.8}
\]

uniformly in `h,t`. Split the time integral at `T` and combine (5.6)-(5.8):

\[
\sup_h\int_{\mathbb R}|\phi_{m,h}-\phi_{\infty,h}|dt
\le2T\delta_m+C''T^{-1/2}.
\tag{5.9}
\]

Choosing, for example, `T=delta_m^{-2/3}` makes the right side tend to zero. Fourier inversion proves (5.1). `□`

### Consequence for the compound-Poisson mixture

Condition on `T_m=t`. Lemma 5.1 is uniform in `t`, because the shift is simply `h=at`. Replacing the finite `T_m` law by the Skellam limit in total variation then gives

\[
\boxed{
\|p_{Q_m}-p_{Q_\infty}\|_\infty\to0.
}
\tag{5.10}
\]

Indeed, the Gaussian conditional densities are uniformly bounded by `3sqrt(2)` from Theorem 3.1, so the total-variation error is uniformly controlled. In particular, the finite witness densities are bounded and continuous for `m>=3`. This continuity statement is only for this family; it is not the full-target continuity theorem.

## 6. Strict global compound-Poisson ceiling

Condition on `T=t`. Since `B=O^TJO`,

\[
Q_\infty\mid(T=t)
\stackrel d=
Z^TJZ,
\qquad
Z\sim N(aOt,I_3/12).
\tag{6.1}
\]

Orthogonality gives `||aOt||=a||t||`. Apply Theorem 3.1:

\[
\|p_{Q_\infty\mid T=t}\|_\infty
\le3\sqrt2\left[
\rho+(1-\rho)e^{-6a^2\|t\|^2}
\right].
\tag{6.2}
\]

Averaging the conditional densities cannot exceed the average of their suprema. Since the three `T_j` are iid,

\[
\boxed{
\|p_{Q_\infty}\|_\infty
\le3\sqrt2\left[
\rho+(1-\rho)q(c,a)^3
\right],
}
\tag{6.3}
\]

where

\[
q(c,a)=\mathbb E e^{-6a^2T_1^2}
=e^{-c}\left[
I_0(c)+2\sum_{k\ge1}I_k(c)e^{-6a^2k^2}
\right].
\tag{6.4}
\]

For `a,c>0`, `P(T_1!=0)>0`, hence `q(c,a)<1`. Since `rho<1`, (6.3) is strictly below `3sqrt(2)`.

Combining with (5.10) gives the finite source-valid family statement

\[
\boxed{
\limsup_{m\to\infty}\|p_{Q_m}\|_\infty
\le3\sqrt2\left[
\rho+(1-\rho)q(c,a)^3
\right]
<3\sqrt2.
}
\tag{6.5}
\]

Thus order-`1/m` remote fragmentation at distance `Theta(sqrt(m))`, in this exact fully rotated three-bank architecture, cannot produce a sharper universal lower-bound witness than `3sqrt(2)`. It actually creates a fixed global gap.

The argument immediately extends to bankwise parameters `(c_j,a_j)`: the factor `q(c,a)^3` is replaced by `prod_j q(c_j,a_j)`, and it is strictly below one if at least one bank has nontrivial remote marks.

## 7. Concrete exact diagnostic: a=c=1

The exact checker verifies `O^TO=I`, `B^2=I`, and all nine entries of `B` are nonzero. It also evaluates

\[
\rho=0.539352601188379356667935722356\ldots,
\]

\[
q(1,1)=0.466790324386610341487165379817\ldots,
\]

so

\[
\rho+(1-\rho)q(1,1)^3
=0.586205251151669786981930229939\ldots.
\]

Therefore

\[
\boxed{
\limsup_m\|p_{Q_m}\|_\infty
\le2.48705824953905342544520564348\ldots
<3\sqrt2.
}
\tag{7.1}
\]

The strict gap from the known obstruction is

\[
3\sqrt2-2.4870582495\ldots
=1.75558243758023172095986052915\ldots.
\]

These numerics are only evaluations of the proved analytic bound; no Monte Carlo or histogram inference is used.

## 8. Application of the designated partner theorem

The partner's exact source-valid family gives the rigorous lower bound (2.3):

\[
C_*\ge3\sqrt2.
\]

The present exact fragmented family gives, for `a=c=1`,

\[
\limsup_m\|p_{Q_m}^{\rm frag}\|_\infty
\le2.48705824954\ldots<3\sqrt2\le C_*.
\tag{8.1}
\]

This is the requested actual use of a completed partner result in an inequality. It shows that a seemingly more adversarial fragmented family is quantitatively **less** extremal than the partner's unfragmented diffuse rotated witness.

## 9. What this proves and what remains open

Proved here:

1. a global, explicit sup-density bound for every mean-shifted isotropic Gaussian quadratic form of signature `(2,1)`, with a strict gap for every nonzero mean;
2. an exact admissible three-bank fragmented product family whose finite matrices have nonzero spectrum exactly `{1,1,-1}`;
3. a uniform local-limit theorem strong enough to transfer global density suprema in that family;
4. a strict global ceiling below `3sqrt(2)` for every fixed positive compound-Poisson activity `c` and jump scale `a`;
5. the concrete `a=c=1` ceiling `2.487058249539...`.

Not proved:

- the full arbitrary-law, arbitrary-matrix QFORM conjecture;
- that `3sqrt(2)` is the optimal universal constant;
- any universal extremality theorem for centered intervals;
- the full-target continuity conclusion.

The next nonredundant B17 witness mechanism must leave this fixed finite-activity compound-Poisson three-bank architecture. Natural remaining stress regimes are multiscale marks, activity/scale changing jointly with `m` so there is no fixed finite-activity limit, or shared-row constructions not reducible to independent bank shifts.

## 10. Source/correction discipline

This proof does not use the refuted arbitrary-joint rank-three coarea bound, the refuted conditional positive-moment interface, post-rotation independence, a law-uniform pointwise stationary-phase bound, naive fiber-supremum integration, or Monte Carlo extremality claims. The only pointwise `|t|^{-3/2}` estimate used is a Fresnel/Fourier-`L^1` estimate for the **specific smooth normalized-uniform bank densities**, whose Fourier `L^1` norms are proved uniformly bounded in (5.3).

Repository use is not native brain ingestion. No authenticated native receiver-use event occurred in this run, so status remains `WITHOUT_VERIFIED_BRAIN`.
