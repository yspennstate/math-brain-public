SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T03:30:02Z.
attacking: arbitrary same-bank nonlinear phase with a one-sided hyperbolic hub-slope entanglement, using conditional averaged-frequency L^r gluing.

# account03/B01 — one-sided entangled hyperbolic smoothing with arbitrary same-bank phase

Run: `20260924T033002Z-account03-B01-qform-auto11-r42`.

Status: **NEW SUPPORTING THEOREM / AVERAGED-FREQUENCY PAYMENT / FULL QFORM OPEN**.

The full conjecture is not claimed. All variables below are literal original-coordinate groups, so no independence after a spectral rotation is used. No Gaussian, moment, support, log-concavity, connected-support, smoothness, or compact-support assumption is introduced.

## 1. Why this is the next interface

The preceding account03/B01 run proved a joint mixed-norm theorem that tolerates a random two-dimensional shift of both hub slopes by the same variables that create a hyperbolic smoothing edge. Its remaining restriction was that the base same-bank phase had to be affine in the base two-dimensional slope. The current target is to remove that restriction in a nontrivial entangled chamber.

The mechanism below is different: condition on the *one* smoothing variable that also shifts the hubs. After conditioning, the arbitrary nonlinear same-bank phase survives untouched, while the other smoothing variable becomes a source-disjoint one-dimensional residual. The completed account04/B01 L^r compiler can therefore be applied fiberwise. The singular coefficient created by conditioning is then integrable against every cap-one law because the resulting fractional exponent is strictly below one.

This is an averaged-frequency argument. It does not resurrect a pointwise stationary-phase estimate.

## 2. Completed partner input

Use the completed account04/B01 theorem from

`yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

Let

\[
Q_0=H^T C H+2H^T(BY+d)+R(Y),
\]

where `H=(H_1,H_2)` are two independent cap-one original coordinates, `Y` is a disjoint product bank, `B` has row rank two, and `R(Y)` is arbitrary measurable. Put

\[
P=\|p_{BY+d}\|_2.
\]

For an independent scalar residual `Z` with density in `L^r`, `1<r\le2`, define

\[
\alpha=\frac{r-1}{r},\qquad
\theta=\frac{r}{2r-1}.
\]

The partner theorem gives a continuous `C_0` density and

\[
\|p_{Q_0+Z}\|_\infty
\le A_r\,[B_r P\|p_Z\|_r]^\theta,
\tag{2.1}
\]

where

\[
A_r=\frac{1+\alpha}{\pi\alpha},
\qquad
B_r=\frac{\alpha\pi}{2}
\left(\frac2{r-1}\right)^{1/r}(2\pi)^\alpha.
\tag{2.2}
\]

The same source records

\[
P\le \sqrt2\,\det(BB^T)^{-1/4}.
\tag{2.3}
\]

At `r=2`, (2.1) is exactly

\[
\|p_{Q_0+Z}\|_\infty
\le3\,2^{-2/3}(P\|p_Z\|_2)^{2/3}.
\tag{2.4}
\]

## 3. A cap-one fractional-pole lemma

### Lemma 3.1

If `U` is any real random variable with density `f_U` satisfying `0\le f_U\le1`, and `0<\eta<1`, then for every `u_0\in\mathbb R`,

\[
\boxed{
\mathbb E|U-u_0|^{-\eta}
\le \frac{2^\eta}{1-\eta}.
}
\tag{3.1}
\]

Consequently, for `c\ne0` and every `\gamma\in\mathbb R`,

\[
\boxed{
\mathbb E|2cU+\gamma|^{-\eta}
\le \frac{|c|^{-\eta}}{1-\eta}.
}
\tag{3.2}
\]

### Proof

The kernel `x\mapsto |x-u_0|^{-\eta}` is radially decreasing about `u_0`. Under the constraints `0\le f\le1` and `\int f=1`, the bathtub/rearrangement principle says the integral is maximized by the indicator of the length-one interval centered at `u_0`. Hence

\[
\int |x-u_0|^{-\eta}f(x)\,dx
\le 2\int_0^{1/2}x^{-\eta}\,dx
=\frac{2^\eta}{1-\eta}.
\]

For (3.2), write `|2cU+\gamma|^{-\eta}=|2c|^{-\eta}|U+\gamma/(2c)|^{-\eta}` and use (3.1):

\[
|2c|^{-\eta}\frac{2^\eta}{1-\eta}
=\frac{|c|^{-\eta}}{1-\eta}.
\]

No moment or support information is used. `\square`

## 4. Main theorem: arbitrary nonlinear base phase plus one-sided hub entanglement

### Theorem `QFORM-TWO-HUB-ONE-SIDED-ENTANGLED-LR-v1`

Let

- `H=(H_1,H_2)` be two independent original coordinates with density caps one;
- `Y` be a disjoint bank of independent cap-one original coordinates;
- `U,V` be two further independent cap-one original coordinates, source-disjoint from `(H,Y)` and from each other;
- `B` be a real `2 x m` matrix of row rank two;
- `a\in\mathbb R^2`, `d\in\mathbb R^2`, `c\ne0`, and `\beta,\gamma,\delta\in\mathbb R`;
- `C` be any real symmetric `2x2` matrix;
- `R(Y)` be **arbitrary measurable**, with no affine, quadratic, moment, support, or regularity restriction.

Consider

\[
\boxed{
Q=H^TCH+2H^T(BY+d+aU)+R(Y)
  +2cUV+\beta U+\gamma V+\delta.
}
\tag{4.1}
\]

For `1<r\le2`, let

\[
\alpha=\frac{r-1}{r},\qquad
\theta=\frac{r}{2r-1},\qquad
\eta=\alpha\theta=\frac{r-1}{2r-1}.
\tag{4.2}
\]

Then `0<\eta<1`, the law of `Q` has a continuous `C_0` density, and

\[
\boxed{
\|p_Q\|_\infty
\le
C_{\rm one}(r)\,P^\theta |c|^{-\eta},
}
\tag{4.3}
\]

where

\[
P=\|p_{BY+d}\|_2,
\qquad
C_{\rm one}(r)
=\frac{A_r B_r^\theta}{1-\eta}.
\tag{4.4}
\]

Using (2.3), with `D=\det(BB^T)`,

\[
\boxed{
\|p_Q\|_\infty
\le
C_{\rm ent,1}(r)\,
D^{-\,r/[4(2r-1)]}
|c|^{-(r-1)/(2r-1)},
}
\tag{4.5}
\]

where

\[
C_{\rm ent,1}(r)=2^{\theta/2}C_{\rm one}(r).
\tag{4.6}
\]

The vector `a` is arbitrary and does not appear in the bound.

### Proof

Condition on the literal original coordinate `U=u`. For almost every `u`, the coefficient

\[
\kappa(u)=2cu+\gamma
\tag{4.7}
\]

is nonzero. Since `U` has a density, the unique possible zero of `\kappa` has probability zero.

At fixed `u`, rewrite (4.1) as

\[
Q_u=
H^TCH+2H^T(BY+d+au)+[R(Y)+\beta u+\delta]
+\kappa(u)V.
\tag{4.8}
\]

The first three terms have exactly the account04/B01 critical two-hub form. Crucially:

1. translation of the two-dimensional slope by `au` does not change the `L^2` norm of its density, so
   \[
   \|p_{BY+d+au}\|_2=P;
   \tag{4.9}
   \]
2. `R(Y)+\beta u+\delta` remains an arbitrary same-bank measurable phase, which the partner theorem already permits;
3. the residual `\kappa(u)V` is independent of `(H,Y)`.

If `f_V\le1`, then for `1<r\le2`,

\[
\|f_V\|_r^r=\int f_V^r\le\int f_V=1,
\qquad
\|f_V\|_r\le1.
\tag{4.10}
\]

The density of `\kappa(u)V` is a scaled copy of `f_V`, hence

\[
\|p_{\kappa(u)V}\|_r
=|\kappa(u)|^{1/r-1}\|f_V\|_r
\le |\kappa(u)|^{-\alpha}.
\tag{4.11}
\]

Apply the completed account04/B01 theorem (2.1) conditionally. For almost every `u`, `Q_u` has a continuous `C_0` density satisfying

\[
\|p_{Q|U=u}\|_\infty
\le A_r B_r^\theta P^\theta
|2cu+\gamma|^{-\alpha\theta}.
\tag{4.12}
\]

By (4.2), the pole exponent is exactly

\[
\eta=\alpha\theta=\frac{r-1}{2r-1}<1.
\tag{4.13}
\]

Average (4.12) against `f_U(u)du` and use Lemma 3.1:

\[
\begin{aligned}
\|p_Q\|_\infty
&\le
A_rB_r^\theta P^\theta
\mathbb E|2cU+\gamma|^{-\eta}\\
&\le
\frac{A_rB_r^\theta}{1-\eta}
P^\theta |c|^{-\eta}.
\end{aligned}
\tag{4.14}
\]

This is (4.3). Inserting `P\le\sqrt2D^{-1/4}` gives (4.5), because

\[
\frac\theta4=\frac{r}{4(2r-1)}.
\tag{4.15}
\]

For continuity, choose a measurable version of the conditional densities `p_u(x)`. Equation (4.12) is dominated after multiplication by `f_U(u)` by the integrable function

\[
A_rB_r^\theta P^\theta
f_U(u)|2cu+\gamma|^{-\eta}.
\]

For almost every `u`, `p_u` is continuous and tends to zero as `|x|\to\infty`. Thus dominated convergence applied to

\[
p_Q(x)=\int p_u(x)f_U(u)\,du
\tag{4.16}
\]

shows both continuity and vanishing at infinity. `\square`

## 5. Sharp simplification at r=2

Set `r=2`. Then

\[
\alpha=\frac12,
\qquad
\theta=\frac23,
\qquad
\eta=\frac13.
\]

Using the exact partner formula (2.4), conditionally on `U=u`,

\[
\|p_{Q|U=u}\|_\infty
\le
3\,2^{-2/3}P^{2/3}|2cu+\gamma|^{-1/3}.
\]

Lemma 3.1 gives

\[
\mathbb E|2cU+\gamma|^{-1/3}
\le\frac32|c|^{-1/3}.
\]

Therefore

\[
\boxed{
\|p_Q\|_\infty
\le
\frac92\,2^{-2/3}P^{2/3}|c|^{-1/3}.
}
\tag{5.1}
\]

Using `P\le\sqrt2D^{-1/4}`,

\[
\boxed{
\|p_Q\|_\infty
\le
\frac9{2\,2^{1/3}}
D^{-1/6}|c|^{-1/3}
<3.572\,D^{-1/6}|c|^{-1/3}.
}
\tag{5.2}
\]

Numerically,

\[
\frac9{2\,2^{1/3}}=3.571652366928448\ldots.
\]

The new cost relative to the source-disjoint/both-shift affine-base theorem is only the integrable pole-average factor. In exchange, the base phase `R(Y)` is now completely arbitrary.

## 6. Scale cancellation survives arbitrary R(Y)

Suppose

\[
BB^T=k^2I_2,
\qquad
c=k^{-q},
\qquad q\ge2.
\tag{6.1}
\]

Then `D=k^4`. In (4.5), the total power of `k` is

\[
-\frac{r}{2r-1}
+q\frac{r-1}{2r-1}.
\tag{6.2}
\]

Choose

\[
r=\frac q{q-1}.
\tag{6.3}
\]

Then `q(r-1)=r`, so (6.2) is exactly zero. Thus the one-sided entangled packet remains uniformly bounded in `k` for every fixed `q\ge2`, while `R(Y)` remains arbitrary measurable.

The checked determinant-form constants are approximately

\[
C_{\rm ent,1}(2)=3.5716523669,
\]
\[
C_{\rm ent,1}(3/2)=4.2910051237,
\]
\[
C_{\rm ent,1}(4/3)=5.2591647443.
\]

These correspond to `q=2,3,4` respectively.

## 7. Averaged-frequency form

Account04/B01 also proved the exact signed-Fejer interface. For a law `\mu` with characteristic function `\phi`, define

\[
D_T\mu(y)=\frac1{2\pi}
\int_{-T}^T\left(1-\frac{|t|}{T}\right)
\Re(e^{-ity}\phi(t))\,dt.
\tag{7.1}
\]

It is a positive Fejer convolution and

\[
\|p\|_\infty=\sup_{T>0,y\in\mathbb R}D_T\mu(y)
\]

whenever the law has a bounded density. Hence Theorem 4 immediately gives the explicit averaged-frequency replacement

\[
\boxed{
\sup_{T>0,y}D_T\operatorname{law}(Q)(y)
\le
C_{\rm ent,1}(r)
D^{-r/[4(2r-1)]}|c|^{-(r-1)/(2r-1)}.
}
\tag{7.2}
\]

At `r=2`,

\[
\boxed{
\sup_{T>0,y}D_T\operatorname{law}(Q)(y)
\le
\frac9{2\,2^{1/3}}D^{-1/6}|c|^{-1/3}.
}
\tag{7.3}
\]

This is stronger than merely controlling one frequency window, while making no assertion that `|\phi_Q|` itself has a universal pointwise power envelope.

## 8. Target-valid nonlinear-phase stress matrix

Order the six original coordinates as

\[
(H_1,H_2,Y_1,Y_2,U,V).
\]

Take

\[
B=I_2,\quad a=(1,0)^T,\quad c=1,\quad R(Y)=Y_1^2,
\]

and all other displayed scalar coefficients zero. Then

\[
Q=2H_1Y_1+2H_2Y_2+2H_1U+Y_1^2+2UV,
\]

with symmetric matrix

\[
A=\begin{pmatrix}
0&0&1&0&1&0\\
0&0&0&1&0&0\\
1&0&1&0&0&0\\
0&1&0&0&0&0\\
1&0&0&0&0&1\\
0&0&0&0&1&0
\end{pmatrix}.
\tag{8.1}
\]

Its characteristic polynomial factors exactly as

\[
\chi_A(x)=(x-1)^2(x+1)(x^3-3x-1).
\tag{8.2}
\]

The numerical spectrum is

\[
-1.5320888862,
-1,
-0.3472963553,
1,
1,
1.8793852416.
\]

Thus five eigenvalues have modulus at least one, so this is genuinely inside the owner's target. Here `D=1` and `c=1`, and (5.2) gives, for **every** admissible independent cap-one input law,

\[
\boxed{
\|p_{X^TAX}\|_\infty<3.572,
}
\tag{8.3}
\]

with a continuous `C_0` density. The example has a genuinely nonlinear base phase `Y_1^2` and a smoothing variable `U` that simultaneously shifts a hub slope and participates in the hyperbolic edge `2UV`.

## 9. The pointwise phase-alignment obstruction is preserved

Fix any prescribed frequency `s\ne0` and any `0<\varepsilon<\pi/2`. The set

\[
E_{s,\varepsilon}
=\{x:\operatorname{dist}(sx^2,2\pi\mathbb Z)\le\varepsilon\}
\]

has infinite Lebesgue measure. Choose a finite union of measurable components inside it having total measure one, and use its indicator as a probability density `f\le1`. Then

\[
\Re\,\mathbb E e^{isX^2}\ge\cos\varepsilon.
\tag{9.1}
\]

Therefore no uniform positive-power pointwise decay of the scalar quadratic transform can hold over the allowed class. The theorem above avoids this obstruction by first conditioning to create an `L^r` residual, using an averaged-frequency compiler, and only then integrating the resulting fractional pole.

## 10. Exact remaining interface

The one-sided entanglement is now paid even with completely arbitrary `R(Y)`. What remains from the preceding two-graph obstruction is the genuinely **two-sided** case

\[
2H^T(aU+bV)
\]

with both `a` and `b` nonzero while the same `U,V` also form the hyperbolic edge and `R(Y)` is arbitrary nonlinear. Conditioning on either `U` or `V` then leaves the other variable simultaneously in a hub slope and in the scalar smoothing term, so the partner theorem no longer factorizes directly.

The next B01 implication is therefore

`QFORM-TWO-HUB-TWO-SIDED-ENTANGLED-NONLINEAR-PHASE-v1`:

prove a joint mixed-frequency inequality for

\[
H^TCH+2H^T(BY+d+aU+bV)+R(Y)+2cUV+\text{affine},
\]

with arbitrary measurable `R(Y)`, or route the remaining matrix states to an already-paid product-preserving branch. This is narrower than the preceding run's obstruction because one-sided direct hub-edge entanglement is no longer unpaid.

## 11. Scope and integrity

- Full QFORM theorem: **OPEN**.
- Continuity: **PROVED in Theorem 4's scope**; open globally.
- No pointwise law-uniform quadratic-phase decay is asserted.
- No post-rotation independence is used.
- No arbitrary-joint coarea or conditional-density-cap inheritance is used.
- No moment, compact-support, or log-concavity condition is used.
- The designated account04/B01 result is applied at equation (4.12), then account04/B01's signed-Fejer theorem is applied at (7.2).
- Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN` absent separate receiver evidence.
