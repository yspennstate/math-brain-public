Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run model/reasoning telemetry is unavailable, so I do not claim otherwise.**

# P06 complementary P07 iteration — calibrated Hermite second chaos and a strict surrogate second-step margin

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.  
Captured pre-write `master`: `c17ca5c0211213e9b64eb687133349b09b349d98`.  
Previous own checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T0732+0300__transverse_convolution_gamma_constant.md`, creation commit `aed84b6c194dc0480a41969cc8aea549c429337c`, readback blob `9b1273ba276d9ebc4f2e3989bd52cd7c59215a2b`.

The outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

Thus the headline source metric does **not** move. The new result is about the missing iteration-survival mechanism after the first positive square-Newton contraction.

The preceding run proved, for every fixed source slack `epsilon>0` with `d=(1+epsilon)^{-1}`, that the vanishing-tilt seed has

\[
\nu_n^2=d^2+o(1),\qquad \Gamma_n^2=1+o(1)
\tag{0.1}
\]

with source-sufficient failure `o(1/sqrt(log n))`, and therefore the first covariance-regularized square step contracts. This run does two things:

1. it proves an **actual finite-model second-chaos calibration** forced by (0.1) and the inherited Gaussian score moments;
2. it solves the resulting **two-chaos Gaussian/Hermite surrogate exactly through the next skew test**, proving that the surrogate second step has a strict margin for every fixed `d<1`.

This is not yet a second-step theorem for the finite circulant model. The exact remaining gap is higher-chaos / off-block leakage of the *fixed* selected Fourier subspace after the first quadratic reweighting. The report derives an explicit positive leakage budget for that step.

---

## 1. Actual finite model: the second-chaos direction is canonically calibrated

Work on the good event from the preceding run and whiten the centered selected feature vector:

\[
Y_n=\Sigma_n^{-1/2}(\Phi_D-\mu_n),\qquad
\mathbf E_{p_n}Y_n=0,\qquad
\mathbf E_{p_n}Y_nY_n^T=I.
\tag{1.1}
\]

Let

\[
Z_n={g_n\over\nu_n},
\tag{1.2}
\]

so `E Z_n=0`, `E Z_n^2=1`. The preceding bulk calculation gives

\[
\mathbf E Z_n^3=o(1),\qquad
\mathbf E Z_n^4=3+o(1).
\tag{1.3}
\]

Define the coefficient vector of the square score

\[
m_n:=\mathbf E[Y_n Z_n^2].
\tag{1.4}
\]

Because `tau_n=nu_n^2 Sigma_n^{1/2}m_n`, the definition of `Gamma_n` gives the exact identity

\[
\|m_n\|_2^2=\Gamma_n^2=1+o(1).
\tag{1.5}
\]

Let `e_n` be the unit coefficient vector with `Z_n=e_n^T Y_n`. Then

\[
e_n^T m_n=\mathbf E Z_n^3=o(1).
\tag{1.6}
\]

Let

\[
\widetilde m_n=(I-e_ne_n^T)m_n,
\qquad
f_n={\widetilde m_n\over\|\widetilde m_n\|_2},
\qquad
U_n=f_n^T Y_n.
\tag{1.7}
\]

From (1.5)--(1.6), `||tilde m_n||=1+o(1)`. By whitening and `f_n perp e_n`,

\[
\mathbf E U_n=0,\qquad
\mathbf E U_n^2=1,\qquad
\mathbf E U_nZ_n=0,
\tag{1.8}
\]

and

\[
\mathbf E[U_nZ_n^2]
=f_n^Tm_n
=1+o(1).
\tag{1.9}
\]

Now set

\[
V_n:=U_n-{Z_n^2-1\over2}.
\tag{1.10}
\]

Using only (1.3), (1.8), and (1.9),

\[
\mathbf E[V_n(Z_n^2-1)]
=\mathbf E[U_nZ_n^2]-{1\over2}(\mathbf EZ_n^4-1)
=o(1),
\tag{1.11}
\]

\[
\mathbf E[V_nZ_n]
=-{1\over2}\mathbf EZ_n^3=o(1),
\tag{1.12}
\]

and

\[
\begin{aligned}
\mathbf EV_n^2
&=1+{1\over4}(\mathbf EZ_n^4-1)-\mathbf E[U_n(Z_n^2-1)]\\
&={1\over2}+o(1).
\end{aligned}
\tag{1.13}
\]

Therefore the actual finite model has the rigorous `L^2` decomposition

\[
\boxed{
U_n={Z_n^2-1\over2}+V_n,
\qquad
\|V_n\|_2^2={1\over2}+o(1),
}
\tag{1.14}
\]

with `V_n` asymptotically orthogonal to `1`, `Z_n`, and `Z_n^2-1`.

This is a new interpretation of the exact constant `Gamma_n^2 -> 1`: the selected Fourier feature space captures asymptotically **half of the Gaussian second-chaos energy**. Since `Var(Z^2-1)=2`, the captured normalized direction has variance one and regression coefficient `1/2` onto `Z^2-1`.

Crucially, (1.14) is a theorem about the finite model and does **not** assert that `V_n` is Gaussian or independent of `Z_n`.

---

# 2. The calibrated two-chaos Gaussian/Hermite surrogate

The minimal Gaussian closure consistent with every identity in Section 1 is

\[
Z,W\stackrel{\mathrm{iid}}\sim N(0,1),
\tag{2.1}
\]

\[
X_1=Z,
\qquad
X_2={Z^2-1\over2}+{W\over\sqrt2}.
\tag{2.2}
\]

Then

\[
\mathbf EX=0,\qquad \operatorname{Cov}(X)=I_2,
\tag{2.3}
\]

and for target

\[
t_d=(d,0),\qquad 0<d<1,
\tag{2.4}
\]

the base residual is `r_0=(-d,0)`, the Newton vector is `h_0=(d,0)`, and the Newton score is

\[
G=dZ,\qquad \nu_0=d.
\tag{2.5}
\]

Moreover

\[
\tau_0=\mathbf E[XG^2]=(0,d^2),
\qquad
\Gamma_0=1.
\tag{2.6}
\]

Thus (2.1)--(2.6) exactly reproduce the limiting decrement and skew constant already proved in the finite model.

The useful mixed-moment table of this closure is

\[
\begin{array}{c|rrrrrrr}
k&0&1&2&3&4&5&6\\ \hline
\mathbf EZ^k&1&0&1&0&3&0&15
\end{array}
\tag{2.7}
\]

\[
\mathbf E[X_2Z^k]=(0,0,1,0,6)\quad(k=0,1,2,3,4),
\tag{2.8}
\]

\[
\mathbf E[X_2^2Z^k]=(1,0,3,0)\quad(k=0,1,2,3),
\tag{2.9}
\]

\[
\mathbf E[X_2^3Z^k]=(1,0,10)\quad(k=0,1,2).
\tag{2.10}
\]

These numbers are **surrogate values**, not yet asserted for the finite model beyond the entries forced by Section 1.

---

# 3. Exact first regularized square update in half-angle coordinates

Put

\[
s=\sqrt{1-d^2},\qquad
\alpha={1\over1+s},
\tag{3.1}
\]

and introduce the half-angle parameter

\[
\beta=\alpha d={d\over1+\sqrt{1-d^2}}\in(0,1).
\tag{3.2}
\]

Then

\[
d={2\beta\over1+\beta^2},
\qquad
s={1-\beta^2\over1+\beta^2}.
\tag{3.3}
\]

The first-step skew parameter is simply

\[
A_0={d\over2(1+s)}={\beta\over2}.
\tag{3.4}
\]

Use the covariance-regularizing mixture chosen in the preceding report,

\[
\eta={A_0\over1-A_0}={\beta\over2-\beta}.
\tag{3.5}
\]

The updated surrogate law has density relative to `(Z,W)` Gaussian measure

\[
w_\beta(Z)
=\eta+(1-\eta){(1+\beta Z)^2\over1+\beta^2}.
\tag{3.6}
\]

It is useful that this is exactly a quadratic Hermite perturbation,

\[
\boxed{
w_\beta(Z)=1+uZ+v(Z^2-1),
}
\tag{3.7}
\]

where

\[
u={4\beta(1-\beta)\over(2-\beta)(1+\beta^2)},
\qquad
v={2\beta^2(1-\beta)\over(2-\beta)(1+\beta^2)}={\beta u\over2}.
\tag{3.8}
\]

Hence the new feature mean is exactly

\[
\mu_1=(u,v).
\tag{3.9}
\]

The residual relative to `t_d` simplifies to

\[
\boxed{
r_1=(u-d,v)=R_\beta(-1,1-\beta),
}
\tag{3.10}
\]

with

\[
R_\beta={2\beta^2\over(2-\beta)(1+\beta^2)}.
\tag{3.11}
\]

The covariance is the explicit positive-definite matrix

\[
\boxed{
C_1=
\begin{pmatrix}
1+2v-u^2 & u(1-v)\\
u(1-v) & 1+2v-v^2
\end{pmatrix}.
}
\tag{3.12}
\]

Let

\[
(a,b)^T=-C_1^{-1}r_1,
\qquad
\nu_1^2=r_1^TC_1^{-1}r_1.
\tag{3.13}
\]

Writing

\[
Y_1=Z-u,
\qquad
Y_2={Z^2-1\over2}+{W\over\sqrt2}-v,
\tag{3.14}
\]

the next Newton score is

\[
G_1=aY_1+bY_2.
\tag{3.15}
\]

Everything through this point is exact in the surrogate.

---

# 4. Exact next third-cumulant map

Define

\[
\tau_1=\mathbf E_{w_\beta}[Y G_1^2].
\tag{4.1}
\]

A direct Gaussian moment calculation gives

\[
\boxed{
\begin{aligned}
(\tau_1)_1
=2\big[&a^2u(u^2-3v)\\
&+ab\{2u^2(v-1)-2v^2+4v+1\}\\
&+b^2u(v-1)^2\big],
\end{aligned}}
\tag{4.2}
\]

and

\[
\boxed{
\begin{aligned}
(\tau_1)_2
={}&a^2\{2u^2(v-1)-2v^2+4v+1\}\\
&+4abu(v-1)^2\\
&+b^2(2v^3-6v^2+6v+1).
\end{aligned}}
\tag{4.3}
\]

Therefore

\[
\Gamma_1^2={\tau_1^TC_1^{-1}\tau_1\over\nu_1^4},
\qquad
A_1={\Gamma_1\nu_1\over2(1+\sqrt{1-\nu_1^2})}.
\tag{4.4}
\]

Equations (3.8), (3.10)--(3.13), and (4.2)--(4.4) are an explicit deterministic recursion for the calibrated two-chaos closure. No numerical optimization or finite SDP is involved.

---

# 5. New theorem: the calibrated closure survives the second skew test for every `d<1`

## Theorem 5.1 — strict surrogate second-step margin

For every `0<d<1`, equivalently every `0<beta<1`, the quantities above satisfy

\[
\boxed{\nu_1^2<1,\qquad A_1<1/2.}
\tag{5.1}
\]

Thus the covariance-regularized positive square-Newton construction admits a **second strict contraction step throughout the entire source-sufficient slack range** in the calibrated two-chaos Gaussian/Hermite closure.

### Proof

Introduce the following positive polynomials:

\[
R_7(\beta)=-5\beta^7+16\beta^6-16\beta^5+7\beta^3-4\beta^2+2\beta+4,
\tag{5.2}
\]

\[
R_9(\beta)=-5\beta^9+46\beta^8-87\beta^7+66\beta^6-43\beta^5-22\beta^4+59\beta^3-2\beta^2-12\beta+8,
\tag{5.3}
\]

\[
\begin{aligned}
R_{10}(\beta)={}&-15\beta^{10}+3\beta^9+31\beta^8-81\beta^7+77\beta^6+17\beta^5\\
&+9\beta^4+49\beta^3+2\beta^2-4\beta+8.
\end{aligned}
\tag{5.4}
\]

Straight substitution from Sections 3--4 gives

\[
\boxed{
\nu_1^2={4\beta^4R_7(\beta)\over(1+\beta^2)R_9(\beta)}
}
\tag{5.5}
\]

and

\[
\boxed{
1-\nu_1^2={(1-\beta)R_{10}(\beta)\over(1+\beta^2)R_9(\beta)}.
}
\tag{5.6}
\]

The exact algebra for the skew simplifies much more usefully if one does **not** expand `Gamma_1^2` itself. Instead,

\[
\boxed{
2-(1+\Gamma_1^2)\nu_1^2
={2(1-\beta)R_{42}(\beta)\over R_7(\beta)R_9(\beta)^4},
}
\tag{5.7}
\]

where

\[
\begin{aligned}
R_{42}(\beta)={}&-159375\beta^{42}+2615625\beta^{41}-20966875\beta^{40}+106362125\beta^{39}\\
&-370734400\beta^{38}+903045876\beta^{37}-1454540126\beta^{36}+1075519350\beta^{35}\\
&+1580227711\beta^{34}-6711532569\beta^{33}+11607803287\beta^{32}-11278588689\beta^{31}\\
&+2694095730\beta^{30}+10452915446\beta^{29}-18365096512\beta^{28}+13264890020\beta^{27}\\
&+2038994063\beta^{26}-15186962761\beta^{25}+15356389283\beta^{24}-3637222885\beta^{23}\\
&-8411057044\beta^{22}+10733548968\beta^{21}-3940131990\beta^{20}-3573528698\beta^{19}\\
&+5382292833\beta^{18}-2182503271\beta^{17}-1312174271\beta^{16}+2039904329\beta^{15}\\
&-733675326\beta^{14}-432606770\beta^{13}+567877332\beta^{12}-155529472\beta^{11}\\
&-124693824\beta^{10}+109049376\beta^9-11713856\beta^8-22487808\beta^7\\
&+11489792\beta^6+332288\beta^5-2003968\beta^4+630784\beta^3+65536\beta^2-73728\beta+16384.
\end{aligned}
\tag{5.8}
\]

The sign certificate is exact. Expressing each polynomial in the Bernstein basis on `[0,1]`, **every Bernstein coefficient is strictly positive**. The smallest coefficients are respectively

\[
\min B(R_7)=4,
\qquad
\min B(R_9)=127/28,
\qquad
\min B(R_{10})=326/45,
\tag{5.9}
\]

and, among all 43 Bernstein coefficients of `R_42`,

\[
\min B(R_{42})={14486362908917\over2764529222}>0.
\tag{5.10}
\]

Hence all four polynomials are positive on `[0,1]`. Equation (5.6) proves `nu_1^2<1` for `beta<1`; (5.7) proves

\[
\Gamma_1^2\nu_1^2<2-\nu_1^2.
\tag{5.11}
\]

Since `nu_1^2<1`,

\[
2-\nu_1^2
<
(1+\sqrt{1-\nu_1^2})^2.
\tag{5.12}
\]

Combining (5.11)--(5.12),

\[
\Gamma_1\nu_1
<1+\sqrt{1-\nu_1^2},
\]

which is exactly `A_1<1/2`. `square`

### Near-sharp asymptotics

Let

\[
\delta=1-\beta\downarrow0.
\tag{5.13}
\]

The exact rational formulas give

\[
\nu_1^2=1-6\delta+36\delta^2-224\delta^3+O(\delta^4),
\tag{5.14}
\]

\[
\Gamma_1^2=1+2\delta+17\delta^2+363\delta^3+O(\delta^4),
\tag{5.15}
\]

and

\[
A_1={1\over2}-{\sqrt6\over2}\sqrt\delta+2\delta+O(\delta^{3/2}).
\tag{5.16}
\]

Thus the second-step margin in the closure is actually of order `sqrt(delta)` near the sharp endpoint, even though the first-step mixture fraction is only

\[
1-\eta={2\delta\over1+\delta}=2\delta+O(\delta^2).
\tag{5.17}
\]

This scale separation is potentially useful for controlling finite-model leakage.

---

# 6. Exact finite-model consequence and exact remaining leakage budget

The theorem above is a theorem of the calibrated closure, not of the full finite Fourier feature space. The finite space is fixed across iterations; it does **not** resample a fresh random half-projection after each square update. Therefore one must not add another independent half of the unprojected `Z^2` energy at the next step. Such a resampling model would even give the wrong continuity limit as `eta -> 1`.

What the finite proof must show is that the same fixed selected-frequency projector does not create too much **new higher-chaos skew energy** when the score changes from `G_0` to `G_1`.

The surrogate provides an exact quantitative budget. If the finite next decrement is `x` and its in-two-chaos skew constant is `gamma_2ch`, then additional normalized skew energy `Delta>=0` is admissible provided

\[
(\gamma_{2ch}^2+\Delta)x
<
(1+\sqrt{1-x})^2.
\tag{6.1}
\]

At the exact surrogate values the allowable leakage is

\[
\boxed{
\Delta_{\rm crit}(\beta)
={2-(1+\Gamma_1^2)\nu_1^2+2\sqrt{1-\nu_1^2}\over\nu_1^2}>0.
}
\tag{6.2}
\]

Using (5.7), this is completely explicit. Near `beta=1`,

\[
2-(1+\Gamma_1^2)\nu_1^2
=10\delta-77\delta^2+115\delta^3+O(\delta^4),
\tag{6.3}
\]

and

\[
\boxed{
\Delta_{\rm crit}(\beta)
=2\sqrt6\,\sqrt\delta+10\delta+O(\delta^{3/2}).
}
\tag{6.4}
\]

Hence, near the sharp source endpoint, it would already suffice to prove that the genuinely new fixed-projector skew energy created by the first reweighting is `o(sqrt(delta))` (after `n -> infinity` for fixed `delta`). A perturbative `O(delta)` or `O(delta^2)` estimate would be much stronger than needed.

---

# 7. Why Section 1 is enough to identify the next finite proof obligation

In whitened coordinates, let

\[
\mathcal S_n=\operatorname{span}\{e_n,f_n\}.
\tag{7.1}
\]

The first mixed square update has residual in this plane up to the inherited `o(1)` longitudinal-skew error, because the exact square-update residual is a linear combination of the old residual and `tau_n`. The only way the actual next Newton score can differ materially from the two-chaos closure is therefore through:

1. covariance coupling from `S_n` into `S_n^perp`; and
2. a new component of the next `tau` in `S_n^perp`.

The covariance-regularizing mixture gives a deterministic safety floor. If `lambda=1-eta`, then

\[
p_1=(1-\lambda)p_0+\lambda q_0
\]

and consequently, for every feature score `F`,

\[
\operatorname{Var}_{p_1}(F)
\ge(1-\lambda)\operatorname{Var}_{p_0}(F).
\tag{7.2}
\]

Thus in whitened coordinates

\[
\boxed{\Sigma_1\succeq(1-\lambda)I.}
\tag{7.3}
\]

This means an off-plane covariance column of norm `L_n` alters the two-dimensional Schur complement by at most

\[
{L_n^2\over1-\lambda}.
\tag{7.4}
\]

Therefore no generic minimum-eigenvalue theorem is needed. The next finite theorem can focus entirely on source-coupled low-degree leakage norms.

A useful target is:

\[
\boxed{
L_n=O_\delta(\delta)+o_{\mathbb P}(1),
\qquad
\|P_{\mathcal S_n^\perp}\tau_{1,n}\|_{\Sigma_{1,n}^{-1}}^2
=O_\delta(\delta^2)+o_{\mathbb P}(1),
}
\tag{7.5}
\]

with failure `o(1/sqrt(log n))`. By (6.4), these estimates would be far inside the available near-sharp skew budget.

The important point is that the relevant leakage vectors are coefficients of **specific low-degree scalar polynomials in the inherited score and the convolution direction**. Their Euclidean coefficient norms can be bounded by Bessel/Parseval and then reduced to the same Walsh/additive-collision counts already used for the `Q_a` theorem. This is a source-coupled calculation, not uniform hypercontractivity over the entire Fourier subspace.

---

# 8. What is proved and what is not

## Proved in the actual finite model

From the preceding source-strength event plus algebra in Section 1:

\[
U_n={Z_n^2-1\over2}+V_n,
\quad
\|V_n\|_2^2\to{1\over2},
\quad
V_n\perp\{1,Z_n,Z_n^2-1\}\ \text{asymptotically}.
\tag{8.1}
\]

This is a genuine new finite-model structural lemma.

## Proved exactly in the calibrated Gaussian/Hermite closure

The first regularized square step has explicit updated mean, covariance, residual and third-cumulant formulas, and

\[
\nu_1^2<1,\qquad A_1<1/2
\]

for every `0<d<1`. The sign proof is algebraic and uses the positive Bernstein certificates above.

## Not proved

It is **not** yet proved that the finite circulant model's post-step Newton score has exactly the two-chaos law (2.2), nor that its higher-chaos leakage obeys (7.5). Therefore this report does not claim a second finite-model square-Newton contraction, an invariant region, exact positive moment feasibility, or an improved full-source theta bound.

---

# 9. Obligation ledger

| obligation | old state | new state |
|---|---|---|
| Full P07 source bound | `sqrt(n) <= E theta <= C sqrt(n log log n)` | unchanged |
| Initial decrement at fixed slack | `nu_0^2=d^2+o(1)` | preserved |
| Initial skew | `Gamma_0^2=1+o(1)` | preserved and reinterpreted as half second-chaos capture |
| Actual second-chaos geometry | implicit convolution theorem | **proved canonical L2 decomposition (1.14)** |
| Gaussian/Hermite iteration | not computed | **exact first reweighting and next skew map (3.7)--(4.4)** |
| Second skew test in closure | open | **proved `A_1<1/2` for every `d<1`** |
| Finite second-step survival | open | reduced to fixed-projector leakage budget (6.2), source-coupled target (7.5) |
| Exact positive feasibility | open | open |
| Expectation endpoint | open | open |

---

# 10. Next attack

Spend the next run on the fixed-projector leakage in (7.5), not on recomputing the surrogate and not on a generic operator-norm theorem.

Write the first updated covariance cross-block and `P_{S_n^perp} tau_{1,n}` explicitly in terms of the inherited symmetric mask `e`, `Q=e*e`, and the next cubic convolution generated by multiplying `Q` with the flat score. Use Bessel/Parseval to convert coefficient norms to scalar `L^2` moments, then use the same low-degree Walsh-support counting architecture as the previous `Q_a` proof. The sharp near-source target is only `o(sqrt(delta))` normalized skew leakage; an `O(delta)` bound is already enough.

If that leakage estimate is proved with failure `o(1/sqrt(log n))`, combine it with the explicit positive budget (6.2) to obtain a genuine **second finite-model covariance-regularized square-Newton contraction for every sufficiently small fixed source slack**. Then use the same expansion to seek a near-boundary invariant strip until the decrement enters a coarse regime where stronger damping can take over.

Expectation/high-probability distinctions remain unchanged: source closure ultimately requires certificate failure `o(1/sqrt(log n))` so the primary `theta<=1+4 sqrt(n log n)` fallback and its `<=2/n` failure can transfer the high-probability sharp-slack certificate to expectation.
