Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run model/reasoning telemetry is unavailable, so I do not claim otherwise.**

# P06 complementary P07 iteration — transverse convolution energy and the sharp first-step skew constant

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.  
Captured pre-write `master`: `63269d8d43ec0df8bf5dcd4e1eec7ef985bf2622`.  
No P07-A/P07-B canonical claim, peer report, or historical artifact is modified.

Outside source remains Bandeira–Blasiok–Dmitriev–Faure–Kireeva–Kunisky, arXiv:2502.16227. The full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

The source headline metric therefore does **not** move in this run. The square-Newton obligation ledger does move: the transverse third-cumulant constant isolated in the preceding run is computed. For every fixed source-sufficient slack `epsilon>0`, the **first covariance-regularized positive square-Newton step now has a strict contraction margin with failure probability strong enough for the eventual expectation transfer**.

The remaining gap is iteration survival: the same skew estimate has not yet been proved uniformly after the first regularized square step.

No finite SDP computation is used.

---

## 1. Inherited vanishing-tilt setup

Let `n` be odd,

\[
H=\{1,\ldots,(n-1)/2\},
\]

and let `(xi_a)_{a\in H}` be independent Bernoulli-`1/2` variables. Put

\[
D=\{a\in H:\xi_a=1\},\qquad M=|D|,
\]

\[
\phi_a(j)=\cos(2\pi aj/n),\qquad
\Phi_D(j)=(\phi_a(j))_{a\in D},
\]

and

\[
S_D(j)=\sum_{a\in D}\phi_a(j).
\]

Fix `epsilon>0` and

\[
d=(1+\epsilon)^{-1}\in(0,1),\qquad
t=-{d\over\sqrt n}{\bf1}_D.
\tag{1.1}
\]

The preceding run used the vanishing Gibbs tilt

\[
c_n=n^{-1/3},
\]

and proved on an event whose complement has probability

\[
O(n^{-7})+e^{-\Omega(n^{1/3})}
\tag{1.2}
\]

that the Gibbs law `p_n` is uniformly `1+O(delta_n)` relative to uniform measure on the nonzero time points, where

\[
\delta_n=n^{-1/3}\sqrt{\log n},
\tag{1.3}
\]

and that

\[
\Sigma_n=(1+O(\delta_n))\Sigma_*
\quad\hbox{in Loewner order},
\tag{1.4}
\]

with exact nonzero-uniform covariance

\[
\Sigma_*={n\over2(n-1)}I_M-{n\over(n-1)^2}J_M.
\tag{1.5}
\]

Its transverse eigenvalue is

\[
\lambda_\perp={n\over2(n-1)}={1\over2}+o(1),
\tag{1.6}
\]

and, on `M/n=1/4+o(1)`, its longitudinal eigenvalue is `1/4+o(1)`.

The same run proved

\[
\nu_n^2=r_n^T\Sigma_n^{-1}r_n
=d^2+O(\delta_n),
\tag{1.7}
\]

and

\[
h_n=-\Sigma_n^{-1}r_n
=-{4d\over\sqrt n}{\bf1}_D+e_n,
\qquad
\|e_n\|_2=O(\delta_n).
\tag{1.8}
\]

Thus `nu_n<1` with a fixed `epsilon`-dependent margin. What remained was the normalized third-cumulant energy

\[
\Gamma_n^2
={\tau_n^T\Sigma_n^{-1}\tau_n\over\nu_n^4},
\qquad
\tau_n=\mathbf E_{p_n}[(\Phi_D-\mu_n)g_n^2],
\tag{1.9}
\]

where

\[
g_n=h_n^T(\Phi_D-\mu_n).
\]

The target suggested by the previous reduction was `Gamma_n^2<=1+o(1)`. The calculation below gives the exact constant `1`.

---

# 2. Symmetric Rademacher mask and the convolution variable

Write

\[
\varepsilon_a=2\xi_a-1,\qquad a\in H,
\]

and extend to `Z_n` by

\[
e_0=0,\qquad e_a=e_{-a}=\varepsilon_{|a|},
\tag{2.1}
\]

where `|a|` denotes the representative in `H` of the pair `{a,-a}`.

Let

\[
A=D\cup(-D)\subset\mathbb Z_n\setminus\{0\}.
\]

For `a\in Z_n`, define the Rademacher self-convolution

\[
Q_a=(e*e)(a)=\sum_{x\in\mathbb Z_n}e_xe_{a-x}
\tag{2.2}
\]

and the selected-set convolution count

\[
N_a=(1_A*1_A)(a)
=|\{(b,c)\in A^2:b+c=a\}|.
\tag{2.3}
\]

Also put

\[
L=\sum_{x\ne0}e_x=2\sum_{r\in H}\varepsilon_r.
\tag{2.4}
\]

Since for nonzero `x`,

\[
1_A(x)={1+e_x\over2},
\]

a direct expansion, remembering that the two forbidden terms `x=0,a` are absent, gives for every nonzero `a`

\[
\boxed{
N_a={n-2\over4}+{L-e_a\over2}+{Q_a\over4}.
}
\tag{2.5}
\]

In particular, **on selected coordinates** `a\in D`, one has `e_a=1`, so every term in (2.5) except `Q_a/4` is common across `a\in D`. Therefore, writing `P_D^\perp` for Euclidean projection in `R^D` onto the orthogonal complement of `1_D`,

\[
\boxed{
P_D^\perp N={1\over4}P_D^\perp Q.
}
\tag{2.6}
\]

This is the exact cancellation that removes the common mask-density fluctuation `L` from the transverse skew.

---

# 3. Exact nonzero-uniform third-cumulant formula

Let `u_*` be uniform on

\[
J_*=\mathbb Z_n\setminus\{0\}.
\]

For `a\in D`, put

\[
X_a=\phi_a-\mathbf E_{u_*}\phi_a
=\phi_a+{1\over n-1},
\tag{3.1}
\]

and

\[
T=S_D-\mathbf E_{u_*}S_D
=S_D+{M\over n-1}.
\tag{3.2}
\]

The flat score suggested by (1.8) is

\[
\widetilde g=-{4d\over\sqrt n}T.
\tag{3.3}
\]

Define its third-cumulant vector under `u_*` by

\[
\widetilde\tau_a
=\mathbf E_{u_*}[X_a\widetilde g^2]
={16d^2\over n}\mathbf E_{u_*}[X_aT^2].
\tag{3.4}
\]

The needed mixed moments are exact. Root orthogonality over all `Z_n`, followed by deleting `j=0`, gives

\[
\mathbf E_{u_*}\phi_a=-{1\over n-1},
\qquad
\mathbf E_{u_*}S_D=-{M\over n-1},
\tag{3.5}
\]

\[
\mathbf E_{u_*}(\phi_aS_D)
={n/2-M\over n-1},
\tag{3.6}
\]

\[
\mathbf E_{u_*}S_D^2
={nM/2-M^2\over n-1},
\tag{3.7}
\]

and, since on the full cyclic group

\[
\mathbf E_{\mathbb Z_n}(\phi_aS_D^2)={N_a\over4},
\]

\[
\mathbf E_{u_*}(\phi_aS_D^2)
={nN_a/4-M^2\over n-1}.
\tag{3.8}
\]

Expanding `(phi_a+1/(n-1))(S_D+M/(n-1))^2` and simplifying yields

\[
\boxed{
\mathbf E_{u_*}[X_aT^2]
={n\over4(n-1)^3}
\left[(n-1)^2N_a+6M(n-1)-4M^2(n+1)\right].
}
\tag{3.9}
\]

Hence all terms except `N_a` are longitudinal, and by (2.6)

\[
\boxed{
P_D^\perp\widetilde\tau
={4d^2\over n-1}P_D^\perp N
={d^2\over n-1}P_D^\perp Q.
}
\tag{3.10}
\]

Thus the entire transverse square-Newton skew has become the same-mask quadratic statistic

\[
\sum_{a\in D}(Q_a-\bar Q_D)^2.
\tag{3.11}
\]

---

# 4. Exact one-coordinate energy

For fixed nonzero `a`, consider the involution

\[
x\mapsto a-x
\]

on `Z_n`. Because `n` is odd, it has one fixed point `x=a/2`. The transposition `{0,a}` contributes zero to `Q_a` because `e_0=0`. The remaining `(n-3)/2` transpositions contribute twice the product of two distinct Rademacher quotient variables. Consequently

\[
Q_a=1+2\sum_{k=1}^{(n-3)/2}\chi_{a,k},
\tag{4.1}
\]

where the `chi_{a,k}` are distinct nonconstant Walsh characters of degree two. They are pairwise orthogonal in `L^2` of the independent mask Rademachers. Therefore, for every odd `n` and every `a\ne0`,

\[
\boxed{
\mathbf E Q_a^2
=1+4{n-3\over2}
=2n-5.
}
\tag{4.2}
\]

No primality assumption is used.

The distinctness assertion in (4.1) is elementary: if two sum-`a` transpositions produced the same unordered pair of sign-classes `{\pm x,\pm(a-x)}`, a finite sign check gives either the same transposition or `a=0`; the latter is excluded.

---

# 5. A correlation-count lemma

The concentration argument uses only low-degree Walsh orthogonality.

For `r\in Z_n`, define

\[
\mathcal T_r
=\sum_{x,y\in Z_n}e_xe_ye_{x+y-r},
\tag{5.1}
\]

and

\[
\mathcal U_r
=\sum_{a,x\in Z_n}e_ae_{a-r}e_xe_{a-x}.
\tag{5.2}
\]

## Lemma 5.1

Uniformly in odd `n` and `r`,

\[
\boxed{
\mathbf E\mathcal T_r^2=O(n^2),
\qquad
\mathbf E\mathcal U_r^2=O(n^2).
}
\tag{5.3}
\]

### Proof

Every summand becomes, after the identities `e_{-x}=e_x` and `epsilon_q^2=1`, a Walsh character in the independent variables `(epsilon_q)_{q\in H}`.

For `T_r`, a generic pair `(x,y)` has parity support of size three,

\[
\{[x],[y],[x+y-r]\},
\]

where `[z]={z,-z}`. Fixing such a support leaves only finitely many possibilities for `(x,y)`: choose which support element occupies which of the three positions and choose the corresponding signs. Thus every size-three Walsh coefficient is `O(1)`.

A support can drop from size three to size one only when two quotient classes coincide. Each coincidence is one of finitely many signed affine equations such as

\[
x=\pm y,
\quad
x=\pm(x+y-r),
\quad
 y=\pm(x+y-r).
\]

Their union contains `O(n)` input pairs. For a fixed surviving singleton support, again only `O(1)` sign solutions occur. Hence the sum of squared Walsh coefficients is `O(n^2)`. Parseval on the mask cube gives the first bound.

For `U_r`, the generic parity support has size four. A fixed size-four support again admits only `O(1)` order/sign realizations. A reduction to support size two lies on a finite union of signed affine coincidence loci with `O(n)` choices for one free parameter; after fixing the surviving support the multiplicity is bounded. Complete cancellation to the empty support can contribute a coefficient of size at most `O(n)`, whose square is still `O(n^2)`. Summing squared coefficients over support sizes `4,2,0` gives `O(n^2)`. Parseval gives the second bound. `square`

The same parity-support count also gives

\[
\mathbf E Q_a^4=O(n^2)
\tag{5.4}
\]

uniformly in nonzero `a`.

---

# 6. Source-strength concentration of the selected convolution energy

Set

\[
S_Q=\sum_{a\ne0}Q_a^2,
\qquad
R_Q=\sum_{a\ne0}e_aQ_a^2.
\tag{6.1}
\]

Because `Q_{-a}=Q_a`,

\[
Y:=\sum_{a\in D}Q_a^2
={1\over4}(S_Q+R_Q).
\tag{6.2}
\]

By (4.2),

\[
\mathbf E S_Q=(n-1)(2n-5).
\tag{6.3}
\]

Moreover `R_Q` changes sign under the global mask sign flip `e\mapsto-e`, while every `Q_a` is unchanged, so

\[
\mathbf E R_Q=0.
\tag{6.4}
\]

Therefore

\[
\boxed{
\mathbf E Y={(n-1)(2n-5)\over4}
={n^2\over2}+O(n).
}
\tag{6.5}
\]

We next prove variance `O(n^3)`.

Flip one independent mask variable `epsilon_r`. With `Delta_rQ_a=Q_a^{(r)}-Q_a`, direct convolution gives, for `a\ne0`,

\[
\Delta_rQ_a
=-4\varepsilon_r(e_{a-r}+e_{a+r})
+4\bigl(1_{a=2r}+1_{a=-2r}\bigr).
\tag{6.6}
\]

Thus `|Delta_rQ_a|=O(1)` uniformly. Expanding

\[
\Delta_r S_Q
=\sum_{a\ne0}
\left(2Q_a\Delta_rQ_a+(\Delta_rQ_a)^2\right)
\tag{6.7}
\]

shows that the only nontrivial sums are, up to `O(n)` deterministic/special-index terms,

\[
\sum_aQ_ae_{a-r}=\mathcal T_r+O(n),
\qquad
\sum_aQ_ae_{a+r}=\mathcal T_{-r}+O(n).
\tag{6.8}
\]

Lemma 5.1 and (5.4) therefore imply

\[
\mathbf E(\Delta_rS_Q)^2=O(n^2).
\tag{6.9}
\]

For `R_Q`, the flip of the explicit factor `e_a` contributes only the two positions `a=plus_or_minus r`, whose squared `L^2` cost is `O(n^2)` by (5.4). The remaining leading sums are of the form

\[
\sum_a e_aQ_ae_{a-r}=\mathcal U_r
\tag{6.10}
\]

and the `r\mapsto-r` analogue, plus `O(n)` terms. Hence

\[
\mathbf E(\Delta_rR_Q)^2=O(n^2).
\tag{6.11}
\]

Efron-Stein over the `(n-1)/2` independent mask bits yields

\[
\boxed{
\operatorname{Var}(S_Q)=O(n^3),
\qquad
\operatorname{Var}(R_Q)=O(n^3),
\qquad
\operatorname{Var}(Y)=O(n^3).
}
\tag{6.12}
\]

Now let

\[
Z:=\sum_{a\in D}Q_a.
\tag{6.13}
\]

Since convolution sums multiply,

\[
\sum_{a\in Z_n}Q_a
=\left(\sum_xe_x\right)^2=L^2,
\qquad Q_0=n-1.
\tag{6.14}
\]

Also

\[
\sum_{a\ne0}e_aQ_a=\mathcal T_0.
\tag{6.15}
\]

Therefore

\[
\boxed{
Z={1\over4}\left[L^2-(n-1)+\mathcal T_0\right].
}
\tag{6.16}
\]

The fourth moment of the Rademacher sum `L` is `O(n^2)` and Lemma 5.1 gives `E T_0^2=O(n^2)`, hence

\[
\boxed{
\mathbf EZ^2=O(n^2).
}
\tag{6.17}
\]

Finally

\[
\sum_{a\in D}(Q_a-\bar Q_D)^2
=Y-{Z^2\over M}.
\tag{6.18}
\]

On `M>=n/8`, whose complement has exponentially small probability, combine (6.5), (6.12), and (6.17). For

\[
\eta_n=(\log n)^{-1/8},
\tag{6.19}
\]

Chebyshev and Markov give

\[
\Pr\left(
\left|{Y\over n^2}-{1\over2}\right|>\eta_n
\right)
=O\left({(\log n)^{1/4}\over n}\right),
\tag{6.20}
\]

and

\[
\Pr\left(
{Z^2/M\over n^2}>\eta_n
\right)
=O\left({(\log n)^{1/8}\over n}\right)+e^{-\Omega(n)}.
\tag{6.21}
\]

Thus

\[
\boxed{
{1\over n^2}
\sum_{a\in D}(Q_a-\bar Q_D)^2
={1\over2}+o(1)
}
\tag{6.22}
\]

outside an event of probability

\[
\boxed{
O\left({(\log n)^{1/4}\over n}\right)+e^{-\Omega(n)}
=o\left({1\over\sqrt{\log n}}\right).
}
\tag{6.23}
\]

This is already at the source-required failure scale.

---

# 7. The transverse constant is exactly `d^4`

By (3.10) and (6.22),

\[
\begin{aligned}
\|P_D^\perp\widetilde\tau\|_2^2
&={d^4\over(n-1)^2}
\sum_{a\in D}(Q_a-\bar Q_D)^2\\
&={d^4\over2}+o(1)
\end{aligned}
\tag{7.1}
\]

with the failure bound (6.23).

Since `Sigma_*^{-1}` acts on the transverse subspace by the scalar

\[
\lambda_\perp^{-1}={2(n-1)\over n}=2+o(1),
\tag{7.2}
\]

we obtain

\[
\boxed{
(P_D^\perp\widetilde\tau)^T
\Sigma_*^{-1}
(P_D^\perp\widetilde\tau)
=d^4+o(1).
}
\tag{7.3}
\]

So the conjectured transverse constant `1` after normalization by `nu^4` is not merely an upper bound: it is the exact leading constant.

---

# 8. The longitudinal third-cumulant energy is negligible

The flat score is longitudinal:

\[
\widetilde g
=\widetilde h^TX,
\qquad
\widetilde h=-{4d\over\sqrt n}{\bf1}_D.
\]

Hence

\[
\widetilde h^T\widetilde\tau
=\mathbf E_{u_*}\widetilde g^3.
\tag{8.1}
\]

Equivalently,

\[
{4d\over\sqrt n}
\left|{\bf1}_D^T\widetilde\tau\right|
={64d^3\over n^{3/2}}
\left|\mathbf E_{u_*}T^3\right|.
\tag{8.2}
\]

The same Walsh parity-support count as Lemma 5.1, now applied to the centered cubic cyclic moment, gives

\[
\mathbf E_D\left(\mathbf E_{u_*}T^3\right)^2=O(n^2).
\tag{8.3}
\]

Therefore

\[
\mathbf E_D\left({\bf1}_D^T\widetilde\tau\right)^2=O(1).
\tag{8.4}
\]

Since `M=Theta(n)` with exponentially high probability,

\[
\boxed{
\|P_D^\parallel\widetilde\tau\|_2^2
={{({\bf1}_D^T\widetilde\tau)^2}\over M}
=o_{\mathbb P}(1).
}
\tag{8.5}
\]

Moreover, for the same `eta_n` as in (6.19), the failure probability for the bound `||P_parallel tau_tilde||^2<=eta_n` is `O((log n)^{1/8}/n)`.

Combining (7.3), (8.5), and the bounded longitudinal inverse eigenvalue gives

\[
\boxed{
\widetilde\tau^T\Sigma_*^{-1}\widetilde\tau
=d^4+o(1)
}
\tag{8.6}
\]

with failure `o(1/sqrt(log n))`.

---

# 9. Returning from the idealized bulk law to the actual Gibbs Newton score

It remains to check that the exact constant survives the already-proved vanishing-tilt perturbation.

On the strong event inherited from the previous run:

1. the nonzero-point Gibbs density differs from `u_*` by `1+O(delta_n)` uniformly;
2. `Sigma_n=(1+O(delta_n))Sigma_*` in Loewner order;
3. `h_n=-(4d/sqrt(n))1_D+e_n` with `||e_n||_2=O(delta_n)`;
4. the origin mass is `exp[-Omega(n^{1/6})]/n`.

For the score error

\[
Y_n=e_n^T(\Phi_D-\mu_n),
\]

(1.4) gives

\[
\|Y_n\|_{L^2(p_n)}=O(\delta_n).
\tag{9.1}
\]

The deterministic bound `|Y_n|<=O(sqrt(n) delta_n)` and interpolation yield

\[
\|Y_n\|_{L^4(p_n)}
\le
\|Y_n\|_\infty^{1/2}\|Y_n\|_2^{1/2}
=O(n^{1/4}\delta_n)
=O(n^{-1/12}\sqrt{\log n})
=o(1).
\tag{9.2}
\]

Thus the actual Newton score differs in `L^4` from the flat score by `o(1)`. On the same strong event, the flat score has `L^2=O(1)` and `L^infty=O(sqrt(log n))`, hence `L^4=O((log n)^{1/4})`.

For any Euclidean unit vector `v`, covariance boundedness gives

\[
\|v^T(\Phi_D-\mu_n)\|_{L^2(p_n)}=O(1).
\]

Therefore Cauchy-Schwarz and (9.2) imply

\[
\left\|
\mathbf E_{p_n}
[(\Phi_D-\mu_n)(g_n^2-\widetilde g^2)]
\right\|_2=o(1).
\tag{9.3}
\]

The `1+O(delta_n)` density comparison changes the idealized vector by at most

\[
O(\delta_n\sqrt{\log n})=O(n^{-1/3}\log n)=o(1)
\tag{9.4}
\]

in Euclidean norm, and the mean-centering change is `O(n^{-1/3})`. Consequently

\[
\boxed{
\|\tau_n-\widetilde\tau\|_2=o(1).
}
\tag{9.5}
\]

Since `||Sigma_n^{-1}||_op=O(1)` and

\[
\|\Sigma_n^{-1}-\Sigma_*^{-1}\|_{op}=O(\delta_n),
\]

(8.6) transfers to the actual Gibbs Newton score:

\[
\boxed{
\tau_n^T\Sigma_n^{-1}\tau_n=d^4+o(1).
}
\tag{9.6}
\]

Together with `nu_n^2=d^2+o(1)`, this is the main theorem of the run.

---

# 10. Main theorem: the normalized skew constant is `1`

## Theorem 10.1 — source-strength first-step transverse-skew law

For every fixed `epsilon>0`, put `d=(1+epsilon)^(-1)` and use the vanishing Gibbs seed `c_n=n^(-1/3)`. Then there is a deterministic sequence `o(1)` such that outside an event of probability

\[
q_n
=O\left({(\log n)^{1/4}\over n}\right)
+e^{-\Omega(n^{1/3})}
=o\left({1\over\sqrt{\log n}}\right),
\tag{10.1}
\]

one has

\[
\boxed{
\nu_n^2=d^2+o(1),
\qquad
\Gamma_n^2
={\tau_n^T\Sigma_n^{-1}\tau_n\over\nu_n^4}
=1+o(1).
}
\tag{10.2}
\]

In particular

\[
\Gamma_n=1+o(1).
\tag{10.3}
\]

This computes the exact constant that the previous run left open.

---

# 11. Consequence: strict first covariance-regularized square-Newton contraction for every fixed slack

Recall the deterministic positive square-Newton quantity

\[
A_n
={\Gamma_n\nu_n\over
2(1+\sqrt{1-\nu_n^2})}.
\tag{11.1}
\]

Using Theorem 10.1,

\[
\boxed{
A_n
={d\over2(1+\sqrt{1-d^2})}+o(1).
}
\tag{11.2}
\]

For every fixed `d<1`,

\[
d<1+\sqrt{1-d^2},
\]

so

\[
\boxed{
{d\over2(1+\sqrt{1-d^2})}< {1\over2}.
}
\tag{11.3}
\]

Hence for every fixed `epsilon>0` there is `c_epsilon>0` such that, outside the source-strength failure event (10.1),

\[
\boxed{
A_n\le {1\over2}-c_\epsilon
}
\tag{11.4}
\]

for all sufficiently large `n`.

Choosing the previously proved optimal covariance-regularizing mixture

\[
\eta_n={A_n\over1-A_n}
\tag{11.5}
\]

therefore gives a strict first-step Newton-decrement contraction

\[
\widehat\nu_n
\le
2\sqrt{A_n(1-A_n)}\,\nu_n
\le q_\epsilon\nu_n,
\qquad q_\epsilon<1.
\tag{11.6}
\]

Thus the first positive square-Newton correction is now controlled at **arbitrarily small but fixed source-sufficient slack**, not only in the coarse `epsilon>0.1547...` regime supplied by the generic kurtosis shortcut.

This is the strongest mathematical change of the run.

---

# 12. What this does and does not close

## Proved in this run

1. Exact transverse reduction
   \[
   P_D^\perp\widetilde\tau={d^2\over n-1}P_D^\perp Q.
   \]

2. Exact one-coordinate convolution energy
   \[
   E Q_a^2=2n-5.
   \]

3. Same-mask selected-energy concentration
   \[
   {1\over n^2}\sum_{a\in D}(Q_a-\bar Q_D)^2
   ={1\over2}+o(1)
   \]
   with failure `o(1/sqrt(log n))`.

4. Negligible longitudinal third-cumulant energy.

5. Actual Gibbs skew constant
   \[
   \Gamma_n^2=1+o(1)
   \]
   with source-sufficient failure.

6. Therefore a strict **first** covariance-regularized square-Newton contraction for every fixed `epsilon>0`.

## Still unresolved

The full random-circulant theta problem is **not solved here**. The missing theorem is **iteration survival**:

> after applying the first positive square update and the covariance-regularizing mixture, prove that the next law still has a decrement/skew pair with a fixed contraction margin, uniformly enough to iterate to zero residual.

The first updated law is no longer near-uniform. Its leading density is a quadratic polynomial in the asymptotically Gaussian flat score, so the next covariance and third-cumulant constants should be computable by a finite Hermite/Gaussian moment recursion, but that recursion has not yet been rigorously connected back to the same-mask cyclic model.

The source headline remains

\[
\sqrt n\le\mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No source-wide improvement is claimed yet.

---

# 13. Next attack

The next run should **not** repeat the first-step convolution calculation. It should propagate the square-Newton state one step.

For fixed `epsilon>0`, let the first-step flat-score limit be `G~N(0,d^2)`. Let

\[
\alpha_*={1\over1+\sqrt{1-d^2}},
\qquad
A_*={d\over2(1+\sqrt{1-d^2})},
\qquad
\eta_*={A_*\over1-A_*}.
\]

The covariance-regularized limiting reweighting has scalar profile

\[
w_{d}(G)
=\eta_*+(1-\eta_*)
{(1+\alpha_*G)^2\over1+\alpha_*^2d^2}.
\tag{13.1}
\]

Attack the next-step decrement/skew by computing the exact Gaussian/Hermite moments under `w_d(G)gamma_d(dG)` and the transverse response of a single Fourier coordinate to this scalar reweighting. The concrete target is a deterministic recursion

\[
(\nu,\Gamma)\mapsto(\nu',\Gamma')
\]

with

\[
A'={\Gamma'\nu'\over2(1+\sqrt{1-(\nu')^2})}<1/2
\]

on the entire compact interval reached from every fixed `d<1`.

Then prove a **one-step propagation theorem** from the finite cyclic same-mask model to that Gaussian recursion with failure `o(1/sqrt(log n))`, using the same low-degree convolution/Walsh counts as in Sections 5–9. If one-step propagation works, look for an invariant compact region and geometric residual decay. That is now the shortest route to an exact positive moment certificate at every fixed slack.

A fallback, if the Gaussian recursion itself crosses `A=1/2`, is to optimize the covariance-mixing parameter away from the one-step optimum rather than returning to pointwise `max|g|` control.

---

## Obligation ledger

- Full-source P07 bound: **UNCHANGED**.
- Initial decrement margin at every fixed slack: **PROVED previous run**.
- Transverse third-cumulant reduction: **PROVED previous run / made exact here**.
- Same-mask transverse energy constant: **NEW PROVED: `1/2` before covariance inverse**.
- Normalized skew constant: **NEW PROVED: `Gamma_n^2=1+o(1)`**.
- Source-strength first square-Newton contraction for every fixed slack: **NEW PROVED**.
- Iteration survival / invariant contracting region: **OPEN**.
- Exact positive feasible distribution and source-wide theta closure: **OPEN**.
- Prime restriction for the new convolution/decrement lemmas: **NOT NEEDED; odd `n` suffices here**.
- Publication novelty: **UNVERIFIED**.

`ledger_delta`: first-step directional-skew obligation moved from OPEN to PROVED PARTIAL; the bottleneck is now second-step/iteration survival rather than the initial square-Newton step.
