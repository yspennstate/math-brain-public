Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# P06 complementary P07 iteration — translated target comparator, actual Galerkin fourth moment, and an essentially exact fixed-c decrement

Status: **P06 SOURCE KNOWN / preserve `U_ER^cert=1`. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1400+0300__quadratic_neutral_comparator_kurtosis_target.md`, creation commit `9badf58464c21e25e947c6d1c0049dc2b256165e`, readback blob `8dc75ea2037deb18f2991b8cddbff6e838718479`, together with the immutable exact-centering correction `2026-09-20T1418+0300__quadratic-comparator-centering-correction.md`, commit `927849de7bba2069ceef551705cb46a35ff47f9c`, blob `34d778c554c79428d31524ad8547ea9a7072eef0`.

Outside P07 source: Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed in this report.

## New result in one sentence

The previous quadratic-neutral comparator gave only the upper bound `nu^2<=0.450370865+o_P(1)`.  The present run introduces an **exact translated-comparator squeeze around the finite Hermite/convolution Galerkin Newton score**.  At the same fixed Gibbs point

\[
a_*=0.430159709001947\ldots,\qquad c_*=4a_*=1.72063883600779\ldots,
\]

the actual finite-model full Newton decrement is now pinned down to

\[
\boxed{
\nu_{c_*}^2\ \xrightarrow{\mathbf P}\ 0.439112404044659\ldots .
}
\tag{0.1}
\]

This is a genuine finite-model statement, not a surrogate constant.  Moreover the actual degree-eight fixed-projector Galerkin score satisfies

\[
\boxed{
\nu_8^2=0.439112403505520+o_{\mathbf P}(1),
\qquad
K_8=5.545641356+o_{\mathbf P}(1),
}
\tag{0.2}
\]

and the **full** Newton score decomposes orthogonally as

\[
g_N=g_8+e_8,
\qquad
\boxed{
\mathbf E_{p_{c_*}}e_8^2
\le1.416502656\times10^{-9}+o_{\mathbf P}(1).
}
\tag{0.3}
\]

Thus the fourth-moment problem has been reduced to controlling the `L^4` effect of an `L^2` tail of size only `3.764e-5`.  This does **not** by itself prove the full-score kurtosis bound, because an arbitrary orthogonal projection need not be `L^4`-contractive.  That remaining distinction is kept explicit below.

The exact decrement value slightly relaxes the sufficient full-score kurtosis target from `7.733048049` to

\[
\boxed{K<7.96572484+o(1).}
\tag{0.4}
\]

---

## 1. Fixed-c Hilbert-space setup

Work, as in the inherited line, on odd cyclic order and the nonzero support

\[
\Omega_n=\mathbb Z_n\setminus\{0\},
\]

with `u_*` uniform on `Omega_n`.  Let `F_{*,D}` be the centered selected-frequency feature span in `L^2(u_*)`, and let

\[
\Pi_{*,D}:L^2(u_*)\to F_{*,D}
\]

be its orthogonal projection.

At `c=4a`, write the positive Gibbs law as

\[
p_{D,a}=f_{D,a}u_*,
\qquad
f_{D,a}(j)=\frac{e^{-aZ_D(j)}}{M_D(-4a)},
\qquad
Z_D=\frac{4S_D}{\sqrt n}.
\tag{1.1}
\]

Let `L_D u_*` denote the exact signed target law from the earlier comparator construction, normalized by

\[
\mathbf E_*L_D=1,
\qquad
\mathbf E_*[L_D\Phi_D]=t_D,
\tag{1.2}
\]

where here the target is the exact sharp target

\[
t_D=-n^{-1/2}\mathbf 1_D.
\]

Set

\[
y_D:=\frac{L_D}{f_{D,a}}-1.
\tag{1.3}
\]

If `F_{p,D}` is the centered feature-linear span in `L^2(p_{D,a})`, the actual Newton score is the orthogonal projection

\[
g_N=P_{F_{p,D}}y_D,
\qquad
\nu^2=\|g_N\|_{L^2(p)}^2.
\tag{1.4}
\]

This is just the normal-equation form of

\[
g_N=-r^T\Sigma^{-1}(\Phi_D-\mu_D).
\]

The crucial point for this run is that the target density is not unique: adding to `L_D` any `u_*`-function orthogonal to constants and all selected features preserves the target moments.  We use that freedom to build a comparator around a restricted Newton score rather than around the original affine density `1-Z_D`.

---

## 2. Exact translated-comparator squeeze lemma

Let `K\subset F_{p,D}` be any finite-dimensional subspace obtained from a coefficient subspace of the selected features.  Denote by

\[
g_K=P_Ky_D
\tag{2.1}
\]

the restricted Newton score and by

\[
\nu_K^2=\|g_K\|_p^2
\tag{2.2}
\]

its restricted decrement.

Regard the same coefficient functions before `p`-centering as a subspace `K_*\subset F_{*,D}`.  Define the density mismatch

\[
D_K:=f_{D,a}(1+g_K)-L_D.
\tag{2.3}
\]

Because `g_K` has `p`-mean zero and `L_D` is normalized,

\[
\mathbf E_*D_K=0.
\tag{2.4}
\]

For every `v\in K_*`, the restricted normal equations give

\[
\mathbf E_*[D_Kv]
=\mathbf E_p[(1+g_K)v]-\mathbf E_*[L_Dv]
=0.
\tag{2.5}
\]

Now project the remaining mismatch onto the **full** selected feature space under the base law:

\[
q_K:=\Pi_{*,D}D_K.
\tag{2.6}
\]

By (2.5),

\[
q_K\perp_{u_*}K_*.
\tag{2.7}
\]

Define the translated signed comparator

\[
\boxed{
\widehat L_K:=f_{D,a}(1+g_K)-q_K.
}
\tag{2.8}
\]

Then

\[
\widehat L_K-L_D
=(I-\Pi_{*,D})D_K.
\]

The right side is orthogonal to constants and to every selected feature, so **exactly**

\[
\mathbf E_*\widehat L_K=1,
\qquad
\mathbf E_*[\widehat L_K\Phi_D]=t_D.
\tag{2.9}
\]

Thus `\widehat L_Ku_*` is another exact signed target law.

Its score relative to `p` is

\[
\widehat y_K:=\frac{\widehat L_K}{f_{D,a}}-1
=g_K-\frac{q_K}{f_{D,a}}.
\tag{2.10}
\]

The cross term vanishes **exactly**:

\[
\left\langle g_K,{q_K\over f_{D,a}}\right\rangle_p
=\langle g_K,q_K\rangle_{u_*}=0,
\tag{2.11}
\]

because the nonconstant part of `g_K` lies in `K_*`, while `q_K` is base-orthogonal to `K_*` and has zero base mean.

Therefore

\[
\boxed{
\|\widehat y_K\|_p^2
=\nu_K^2+\epsilon_K,
\qquad
\epsilon_K:=\mathbf E_*\frac{q_K^2}{f_{D,a}}.
}
\tag{2.12}
\]

Since the full Newton score is the feature projection of **every** exact target score, including `\widehat y_K`,

\[
\nu^2\le\nu_K^2+\epsilon_K.
\tag{2.13}
\]

On the other hand, `K\subset F_{p,D}` gives

\[
\nu^2\ge\nu_K^2.
\tag{2.14}
\]

Moreover the projection of the full Newton score onto `K` is exactly `g_K`, hence Pythagoras gives

\[
\boxed{
\|g_N-g_K\|_p^2
=\nu^2-\nu_K^2
\le\epsilon_K.
}
\tag{2.15}
\]

### Lemma 2.1 — translated-comparator Galerkin squeeze

Equations (2.12)--(2.15) are deterministic and require only positivity of the seed `p`, not positivity of the signed target comparator.  They are the main structural advance of this iteration.

The old quadratic-neutral comparator bounded the full decrement by the total weighted norm of a hand-built target density.  Lemma 2.1 instead centers the comparator on the **restricted Newton solution itself** and charges only the residual target mismatch left outside the chosen Galerkin subspace.

---

## 3. Degree-R fixed-projector Hermite/convolution subspace

Use the same actual fixed selected projector as in the preceding reports; no independent half-projection is resampled.

Write

\[
e_k(z)=\frac{H_k(z)}{\sqrt{k!}}.
\]

For `k>=2`, let the selected fixed-projector direction be the normalized projection of the centered `k`th Hermite chaos; in the calibrated reference bookkeeping this is

\[
U_1=Z,
\qquad
U_k=\frac{e_k(Z)}{\sqrt2}+\frac{W_k}{\sqrt2},\quad k\ge2,
\tag{3.1}
\]

where the `W_k` merely encode the orthogonal half of each same-mask projected chaos.  In the finite cyclic model the `U_{k,D}` are the corresponding explicit convolution words obtained by applying `\Pi_{*,D}` to `H_k(Z_D)` and normalizing.  The earlier fixed-degree Walsh/additive-collision theorem, with exponential insertions, transports every fixed joint moment needed below from the finite model to (3.1), with failure `o(1/sqrt(log n))`.

Let

\[
K_R=\operatorname{span}\{U_{1,D},\ldots,U_{R,D}\}
\]

after `p`-centering.  The restricted covariance and residual converge to the deterministic reference system

\[
C_R=T_RT_R^T+N_R,
\tag{3.2}
\]

where

\[
(T_R)_{11}=1,
\]

\[
(T_R)_{kj}
={\binom{k}{j}(-a)^{k-j}\sqrt{j!}\over\sqrt{2k!}},
\qquad
2\le k\le R,\ 1\le j\le k,
\tag{3.3}
\]

and

\[
N_R=\operatorname{diag}(0,1/2,\ldots,1/2).
\tag{3.4}
\]

The sharp-target residual is

\[
r_1=1-a,
\qquad
r_k={(-a)^k\over\sqrt{2k!}},\quad k\ge2.
\tag{3.5}
\]

Thus, with

\[
h_R=C_R^{-1}r_R,
\tag{3.6}
\]

the restricted decrement is

\[
\nu_R^2=r_R^TC_R^{-1}r_R.
\tag{3.7}
\]

For `R=8` and `a=a_*`,

\[
\boxed{
\nu_8^2=0.43911240350551994\ldots .
}
\tag{3.8}
\]

The reference coefficient vector is

\[
\begin{aligned}
h_1&= 0.715432100514094,\\
h_2&= 0.341415100117758,\\
h_3&= 0.003497408915030,\\
h_4&=-0.015538655342461,\\
h_5&=-0.000030668854966,\\
h_6&= 0.001277788598227,\\
h_7&=-0.000014994329950,\\
h_8&=-0.000133406350513.
\end{aligned}
\tag{3.9}
\]

Because the fourth moment of the degree-eight score is a fixed polynomial/exponential insertion involving only a finite convolution dictionary, the same collision transport gives an **actual finite-model Galerkin theorem**:

\[
\boxed{
\mathbf E_{p_{D,a_*}}g_{8,D}^2
=0.439112403505520+o_{\mathbf P}(1),
}
\tag{3.10}
\]

\[
\boxed{
\mathbf E_{p_{D,a_*}}g_{8,D}^4
=1.06930891872+o_{\mathbf P}(1),
}
\tag{3.11}
\]

and therefore

\[
\boxed{
K_{8,D}
=5.545641356+o_{\mathbf P}(1).
}
\tag{3.12}
\]

This promotes the **degree-eight restricted score** constant from a benchmark to an actual finite-model theorem.  It does not yet identify the fourth moment of the unrestricted Newton score.

---

## 4. Exact reference form of the translated mismatch

In the reference model the base-law directions `U_k` are orthonormal.  For `k>R`, the coefficient of the projected mismatch `q_R` in direction `U_k` is simply the residual left by the restricted normal equations:

\[
\boxed{
\rho_k^{(R)}
=r_k-C_{k,1:R}h_R.
}
\tag{4.1}
\]

For `R=8`, the first terms are

\[
\begin{array}{c|r}
k&\rho_k^{(8)}\\ \hline
9&-1.11636971968\times10^{-5}\\
10& 3.29741987283\times10^{-5}\\
11&-2.13188122273\times10^{-5}\\
12& 9.04918814847\times10^{-6}\\
13&-3.00338578544\times10^{-6}\\
14& 8.37550272537\times10^{-7}\\
15&-2.04121253018\times10^{-7}\\
16& 4.45699808739\times10^{-8}\\
17&-8.87024461667\times10^{-9}\\
18& 1.62944704374\times10^{-9}.
\end{array}
\tag{4.2}
\]

For `k>R` there is an explicit factorial tail.  Indeed (3.2)--(3.5) give

\[
\rho_k^{(R)}
={(-a)^k\over\sqrt{2k!}}P_R(k),
\tag{4.3}
\]

where `P_R` is a polynomial of degree at most `R`; explicitly

\[
P_R(k)
=1-{h_1k\over -a}
-\sum_{j=2}^R
{h_j\over\sqrt{2j!}}
\sum_{s=1}^j
\binom{k}{s}\binom{j}{s}s!(-a)^{j-2s}.
\tag{4.4}
\]

So the translated mismatch is factorially small in chaos degree.

---

## 5. Weighted norm of the translated mismatch

Set

\[
w_a(Z)=f_a(Z)^{-1}=e^{aZ+a^2/2}
\]

in the reference model.  For `k,l>=2`, define

\[
G^+_{k\ell}(a)
={1\over\sqrt{k!\ell!}}
\sum_{s=0}^{\min(k,\ell)}
\binom{k}{s}\binom{\ell}{s}s!a^{k+\ell-2s}.
\tag{5.1}
\]

Then the weighted Gram matrix of the base directions is

\[
A^+_{k\ell}
=\mathbf E[w_aU_kU_\ell]
={e^{a^2}\over2}
\bigl(G^+_{k\ell}(a)+\delta_{k\ell}\bigr),
\qquad k,\ell\ge2,
\tag{5.2}
\]

with the analogous obvious first-row formula

\[
A^+_{1\ell}
={e^{a^2}\over\sqrt2}G^+_{1\ell}(a)
\quad (\ell\ge2),
\qquad
A^+_{11}=e^{a^2}(1+a^2).
\tag{5.3}
\]

Hence the translated-comparator remainder in Lemma 2.1 has deterministic reference value

\[
\boxed{
\epsilon_R^{\rm ref}
=\sum_{k,\ell>R}
\rho_k^{(R)}A^+_{k\ell}\rho_\ell^{(R)}.
}
\tag{5.4}
\]

The series is absolutely convergent.  Equation (4.3), Stirling, and the translated-Hermite norm bound from (5.1) give a factorial majorant; in particular the tail after a fixed truncation is bounded by a convergent series of the form

\[
C_R\sum_{k>K}{k^{2R}(|a|+1)^{2k}\over k!}.
\tag{5.5}
\]

For `R=8`, direct evaluation of the exact finite sum through degree 24 together with (5.5) gives

\[
\boxed{
\epsilon_8^{\rm ref}
=1.41650265516424\times10^{-9}.
}
\tag{5.6}
\]

For orientation, the partial values are

\[
\begin{array}{c|c}
K&\sum_{9\le k,\ell\le K}\rho_kA^+_{k\ell}\rho_\ell\\ \hline
12&1.43897605756\times10^{-9}\\
16&1.41650295563\times10^{-9}\\
20&1.41650265516\times10^{-9}\\
24&1.41650265516\times10^{-9}.
\end{array}
\tag{5.7}
\]

The apparent nonmonotonicity is harmless: (5.4) is a quadratic form with cross terms, not a sum of nonnegative coordinate contributions.

---

## 6. Transport of the translated mismatch to the actual finite cyclic model

It remains to justify that (5.4) is not merely a Gaussian bookkeeping number.

For fixed `R`, the actual finite-model object

\[
q_{R,D}=\Pi_{*,D}\bigl(f_{D,a}(1+g_{R,D})-L_D\bigr)
\tag{6.1}
\]

is a source-coupled selected-frequency Fourier projection of an analytic function of `Z_D` times a finite list of the existing convolution words.

To evaluate

\[
\epsilon_{R,D}
=\mathbf E_*\frac{q_{R,D}^2}{f_{D,a}},
\tag{6.2}
\]

truncate each fixed exponential at degree `M`.  For fixed `R,M`, (6.2) is a finite linear combination of exactly the Walsh/additive-collision words already controlled in the inherited fixed-degree theorem.  Disconnected pairings give (5.1)--(5.4), while every connected two-copy diagram loses a free cyclic parameter.  Thus, for fixed `R,M`, the normalized error has variance `O_{R,M}(1/n)`.

The inherited fixed-parameter subgaussian exponential-moment estimate then lets `M` tend to infinity after the finite-model limit.  Because `a=a_*` is fixed and (4.3) is factorial, the truncation is uniform in the weighted quadratic quantity (6.2).  Choosing a fixed sufficiently large `M` first and then the standard `n^{-1/4}` concentration tolerance yields failure `o(1/sqrt(log n))`.

Therefore, for every fixed `R`,

\[
\boxed{
\epsilon_{R,D}
\xrightarrow{\mathbf P}
\epsilon_R^{\rm ref},
}
\tag{6.3}
\]

with source-sufficient failure.

For `R=8`, Lemma 2.1 and (5.6) give the **actual full-score decomposition**

\[
\boxed{
\|g_N-g_{8,D}\|_{L^2(p)}^2
\le1.416502656\times10^{-9}+o_{\mathbf P}(1).
}
\tag{6.4}
\]

This is much stronger than the previous comparator gap

\[
0.450370865-0.439112404\approx1.13\times10^{-2}.
\]

The translated comparator removes essentially all of that artificial gap.

---

## 7. The actual fixed-c decrement is now identified asymptotically

For every fixed `R`, Lemma 2.1 gives

\[
\nu_R^2+o_{\mathbf P}(1)
\le\nu^2
\le\nu_R^2+\epsilon_R^{\rm ref}+o_{\mathbf P}(1).
\tag{7.1}
\]

The deterministic reference values satisfy

\[
\begin{array}{c|c|c}
R&\nu_R^2&\epsilon_R^{\rm ref}\\ \hline
4&0.439109803833425&5.045603361\times10^{-6}\\
6&0.439112373267131&6.977401257\times10^{-8}\\
8&0.439112403505520&1.416502655\times10^{-9}\\
10&0.439112404031960&3.841824440\times10^{-11}\\
12&0.439112404044280&1.312312180\times10^{-12}\\
16&0.439112404044658&2.628730863\times10^{-15}.
\end{array}
\tag{7.2}
\]

Both sequences converge, and the common limit is

\[
\boxed{
\nu_\infty^2
=0.439112404044659\ldots .
}
\tag{7.3}
\]

Given any fixed tolerance `delta>0`, choose `R` so that both `|nu_R^2-nu_infty^2|<delta/3` and `epsilon_R^{ref}<delta/3`, then choose `n` large enough for the fixed-`R` collision errors to be below `delta/3`.  This proves the promised actual finite-model limit

\[
\boxed{
\nu_{D,c_*}^2\xrightarrow{\mathbf P}
0.439112404044659\ldots .
}
\tag{7.4}
\]

Equivalently,

\[
\boxed{
\nu_{D,c_*}\xrightarrow{\mathbf P}
0.662655569693\ldots .
}
\tag{7.5}
\]

This replaces the earlier one-sided bound `nu<=0.671096763+o_P(1)` by an asymptotically exact source-coupled decrement constant.

---

## 8. Updated scalar kurtosis threshold

The inherited deterministic inequality remains

\[
\Gamma^2\le K-1,
\qquad
K={\mathbf E g_N^4\over(\mathbf E g_N^2)^2}.
\tag{8.1}
\]

With the actual decrement limit (7.5),

\[
\beta_*
={\nu_\infty\over1+\sqrt{1-\nu_\infty^2}}
=0.378893227408\ldots .
\tag{8.2}
\]

The positive square-Newton contraction criterion `A=Gamma beta/2<1/2` is therefore implied by

\[
\boxed{
K<1+\beta_*^{-2}
=7.965724841\ldots .
}
\tag{8.3}
\]

So the remaining scalar target has relaxed slightly from `7.733048049` to `7.965724841`.

For comparison, the **actual degree-eight Galerkin** fourth moment from (3.11) is

\[
K_8=5.545641356+o_{\mathbf P}(1).
\tag{8.4}
\]

The corresponding fourth-moment budget is

\[
\mathbf E g_8^4
=1.06930891872+o(1),
\]

whereas the sufficient full-score threshold at the limiting decrement is

\[
7.965724841\,(0.439112404044659)^2
=1.53594870118\ldots .
\tag{8.5}
\]

Thus there is an absolute fourth-moment budget of about

\[
0.46664
\]

between the actual degree-eight Galerkin value and the sufficient full-score threshold.

---

## 9. What this does and does not prove about the full kurtosis

Equation (6.4) is deliberately not overinterpreted.

We know

\[
g_N=g_8+e_8,
\qquad
\langle g_8,e_8\rangle_p=0,
\qquad
\|e_8\|_2\le3.764\times10^{-5}+o_{\mathbf P}(1).
\tag{9.1}
\]

But `L^2` smallness alone does not imply `L^4` smallness for an arbitrary function on a growing finite space.  Therefore this report does **not** claim

\[
K_N\to5.545638\ldots
\]

and does not yet claim an absolute coarse-entry contraction.

What has changed is the nature of the remaining obligation.  The full fourth-moment theorem no longer needs to identify the whole Newton inverse from scratch.  It only needs a source-coupled `L^4` tail estimate for the Galerkin remainder.

A quantitatively sufficient statement is, for example,

\[
\boxed{
\|e_8\|_{L^4(p)}<0.088
}
\tag{9.2}
\]

outside source-sufficient failure.  Indeed Minkowski with the degree-eight value then places the full fourth moment below (8.5).  The actual reference remainder is vastly smaller than this target, but that reference fact is not promoted here without the finite same-mask tail argument.

The correct next proof object is the translated mismatch `q_{8,D}` from (6.1), not a generic vector in the selected Fourier space.  The remainder satisfies

\[
e_8=-P_{F_{p,D}}\left({q_{8,D}\over f_{D,a_*}}\right),
\tag{9.3}
\]

and `q_{8,D}` is generated by the same mask through the explicit analytic/convolution tail in (4.1)--(4.4).  Thus the next run should estimate the fourth moment of this **specific source-coupled projected tail**, using its factorial chaos coefficients and the existing connected-diagram bounds.  A uniform `2->4` theorem for the whole selected subspace is unnecessary and would be much harder.

---

## 10. Failed route avoided in this run

The tempting inequality

\[
\|P_F z\|_4\le\|z\|_4
\]

is false for a general orthogonal projection, so the tiny weighted comparator tail cannot simply be declared an `L^4` bound.  Likewise, using `p_{\min}` or a worst-case Fourier `L^2->L^\infty` estimate would reintroduce a growing `n` factor and throw away the source-coupled structure.

The translated-comparator squeeze is useful precisely because it isolates the remaining tail as the fixed analytic same-mask object (9.3), where collision methods can still exploit equivariance and factorial chaos decay.

---

## 11. Intermediate-obligation ledger

- **Full-source P07 metric:** unchanged, `sqrt(n) <= E theta <= C sqrt(n log log n)`.
- **P06 source status:** KNOWN in later literature; `U_ER^cert=1` preserved; no rescreening.
- **New deterministic theorem:** exact translated-comparator Galerkin squeeze, equations (2.12)--(2.15).
- **New actual finite-model theorem:** degree-eight fixed-projector Galerkin score has `nu_8^2=0.439112403505520+o_P(1)` and `K_8=5.545641356+o_P(1)`.
- **New actual full-score theorem:** `nu_{c_*}^2 ->_P 0.439112404044659...`.
- **New score decomposition:** `E_p[(g_N-g_8)^2] <= 1.416502656e-9+o_P(1)`.
- **Updated sufficient scalar target:** full-score `K<7.965724841` implies `A<1/2`.
- **Remaining bridge:** prove an `L^4` bound for the specific translated same-mask tail `e_8`, e.g. `||e_8||_4<0.088`; then invoke `Gamma^2<=K-1` and the inherited superlinear coarse tail.
- **Parity:** odd cyclic order only; even-order self-inverse frequency remains untreated.

## 12. Next attack

Spend the next useful iteration on the source-coupled fourth moment of

\[
e_8=-P_{F_p}(q_8/f).
\]

Expand `q_8/f` in the canonical Hermite/convolution tail beginning at degree nine.  Use the exact coefficients (4.1)--(4.4), pairing terms for the `L^4` main contribution and connected diagrams for the error.  The target is only `||e_8||_4<0.088`, not a sharp identification of every higher-chaos coefficient.  If direct projection of the infinite tail is awkward, take `R=12` or `R=16`, for which the translated `L^2` remainders are respectively about `1.15e-6` and `5.13e-8`, and prove an `L^2->L^4` estimate only on that **single canonical tail family**.  Do not replace it by a worst-case bound over the whole selected Fourier subspace.
