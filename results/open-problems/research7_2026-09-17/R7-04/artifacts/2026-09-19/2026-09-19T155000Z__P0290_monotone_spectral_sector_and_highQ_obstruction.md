# P0290: monotone spectral reduction and the exact high-Q obstruction

Target: Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), 213--215, DOI `10.1007/s11134-022-09824-0`, Problem 2 on journal p. 214.

Status of this artifact: **PARTIAL / OPEN**. It neither proves nor refutes Leskelä Problem 2. It identifies a new source-relevant spectral restriction supplied by 2026 monotone-matrix literature, proves an exact high-quality-factor mechanism by which the recovered light-traffic coefficient can reverse for finite stationary Markov chains, and shows precisely why that construction is outside the source class. The point is to isolate what double stochastic monotonicity still has to forbid.

Recovered predecessor: `research7_2026-09-17/R7-04/artifacts/2026-09-19/2026-09-19T145600Z__P0290_reflection_family_endpoint_compactification.md` @ creation commit `26874a61c2d057212d918144761e1452a111615f`. That orphan artifact executed B3/B5/B20 after the last immutable run report. It proved all-scale second-order safety near both endpoints `a=0,1` of the exact four-state reflection family and reduced the remaining family sign problem to a compact two-variable rectangle. The present note does not repeat that work.

## 1. Recovered light-traffic operator

For a stationary finite-state hidden chain with generator `Q`, stationary law `pi`, and centered real observable `g`, put

\[
C_g(t)=\langle g,e^{tQ}g\rangle_\pi,
\qquad
J_g(c)=\int_0^1(1-u)C_g(cu)\,du.
\]

The prior P0290 work established

\[
\Phi(z)=\frac{e^z-1-z}{z^2},
\qquad
\Psi(z)=\Phi'(z)=\frac{(z-2)e^z+z+2}{z^3},
\]

with removable values at zero, and

\[
J_g'(c)=\left\langle g,\frac12\left(Q\Psi(cQ)+[Q\Psi(cQ)]^\dagger\right)g\right\rangle_\pi.
\tag{1.1}
\]

For a normal generator and an eigenmode with eigenvalue `lambda`, the sign is therefore governed by

\[
\operatorname{Re}[\lambda\Psi(c\lambda)].
\tag{1.2}
\]

It is useful to absorb the scale into

\[
G(z):=z\Psi(z)=\frac{(z-2)e^z+z+2}{z^2}.
\tag{1.3}
\]

Then the sign in (1.2) is the sign of `Re G(c lambda)`.

The source-level frozen metric remains

`Delta_Ross := sup (w(c2)-w(c1))/(1+w(c1)+w(c2))`

over the full source class. Nothing below produces a positive source-admissible value of this metric.

---

# B21 -- who else has this shape? A 2026 monotone-spectrum theorem gives a CTMC sector bound

## 2. New relevant prior art

A fresh 2026-09-19 literature check found a directly relevant paper that had not appeared in the earlier P0290 reports:

Brando Vagenende, Brecht Verbeken and Marie-Anne Guerry, *Eigenvalue regions and realising monotone stochastic matrices*, Electronic Journal of Linear Algebra **42** (2026), 387--398, published 14 May 2026, DOI `10.13001/ela.2026.10159`; arXiv:2502.01314v2 (18 Dec 2025).

Primary pages:
- `https://journals.uwyo.edu/index.php/ela/article/view/10159`
- `https://arxiv.org/abs/2502.01314`

Their Theorem 5.2 proves that for `n>=4` every eigenvalue of an `n x n` monotone stochastic matrix belongs to the Karpelevich eigenvalue region `Theta_{n-1}` for `(n-1) x (n-1)` stochastic matrices. Their paper also states that every eigenvalue of a `3 x 3` monotone stochastic matrix is real (they cite earlier monotone-matrix work for that fact).

This corrects the novelty boundary of the earlier R7-04 three-state calculation: the fact that three-state monotone chains have real spectrum is **prior art**, not a new R7-04 theorem. The earlier R7-04 proof remains a useful source-native derivation, and its additional positive-definite two-exponential covariance argument is logically separate.

## 3. Corollary for continuous-time monotone generators

**Theorem 3.1 (monotone-generator sector reduction).** Let `Q` be the generator of a stochastically monotone continuous-time Markov chain on a totally ordered `n`-state space, `n>=4`. For every nonzero eigenvalue

\[
\lambda=-\alpha+i\beta
\qquad(\alpha>0),
\]

one has

\[
\boxed{
|\beta|\le \cot\!\left(\frac{\pi}{n-1}\right)\alpha.
}
\tag{3.1}
\]

In particular the same bound holds for every source-admissible P0290 hidden chain, since double stochastic monotonicity includes forward stochastic monotonicity.

### Proof

For every `t>0`, the transition matrix

\[
P_t=e^{tQ}
\]

is an `n x n` monotone stochastic matrix. Therefore `e^{t\lambda}` is a nontrivial eigenvalue of `P_t`. By Vagenende--Verbeken--Guerry Theorem 5.2,

\[
e^{t\lambda}\in\Theta_{n-1}.
\]

Equivalently, for each `t` there exists some `(n-1) x (n-1)` stochastic matrix `S_t` having `e^{t\lambda}` as an eigenvalue. Hence

\[
A_t:=S_t-I
\]

is an `(n-1)`-state continuous-time Markov generator: its off-diagonal entries are nonnegative and its row sums are zero. Its corresponding eigenvalue is

\[
\nu_t=e^{t\lambda}-1.
\]

The classical Dmitriev--Dynkin/Karpelevich sector theorem for an `m`-state Markov generator says

\[
|\operatorname{Im}\nu|
\le \cot(\pi/m)\,[-\operatorname{Re}\nu]
\tag{3.2}
\]

for every nonzero eigenvalue `nu`; equality is attained by the directed `m`-cycle up to scale. Applying (3.2) with `m=n-1` gives

\[
|\operatorname{Im}(e^{t\lambda}-1)|
\le \cot\!\left(\frac\pi{n-1}\right)
\bigl(1-\operatorname{Re}e^{t\lambda}\bigr).
\]

Divide by `t` and send `t downarrow 0`. Since

\[
\frac{e^{t\lambda}-1}{t}\longrightarrow\lambda,
\]

we obtain (3.1). `square`

### Meaning

This is a clean source-relevant restriction on any oscillatory counterexample route. A general `n`-state generator may approach the sharp sector ratio `cot(pi/n)`; a monotone `n`-state chain is forced into the smaller `(n-1)`-state stochastic sector. Double monotonicity may impose still more restrictions, but (3.1) is the first current published spectral result found in this campaign that directly constrains the P0290 search.

---

# B7 -- take the limit: an exact high-Q reversal exists for finite stationary Markov chains

The previous P0290 searches found nonmonotone covariances but no increase of `J_g(c)`. The next theorem shows that this is not a universal Markov phenomenon: sufficiently weakly damped rotational modes really do reverse `J`.

## 4. A fixed point where the scalar filter has the wrong sign

Let

\[
y=\frac{5\pi}{2},\qquad z_0=iy.
\]

Since `e^{iy}=i`, equation (1.3) gives exactly

\[
G(iy)
=
\frac{(iy-2)i+iy+2}{(iy)^2}
=
\frac{(y-2)(1-i)}{y^2}.
\]

Therefore

\[
\boxed{
\operatorname{Re}G\!\left(\frac{5\pi i}{2}\right)
=\frac{y-2}{y^2}>0.
}
\tag{4.1}
\]

So any normal eigenmode whose rescaled eigenvalue gets sufficiently close to `5 pi i/2` makes the triangular time-average coefficient increase.

We can make the neighborhood explicit.

**Lemma 4.1.** If `0<=x<=1/20` and `y=5 pi/2`, then

\[
\boxed{\operatorname{Re}G(-x+iy)>0.}
\tag{4.2}
\]

### Proof

Write

\[
N(z)=(z-2)e^z+z+2,
\qquad G(z)=N(z)/z^2,
\]

so

\[
N'(z)=(z-1)e^z+1,
\qquad
G'(z)=\frac{N'(z)}{z^2}-\frac{2N(z)}{z^3}.
\]

On the horizontal segment from `iy` to `-x+iy`, with `x<=1/20`, the elementary bounds `3<pi<22/7` imply

\[
7<|z|<8,
\qquad |e^z|\le e^{1/20}<2.
\]

Hence

\[
|N'(z)|<19,
\qquad |N(z)|<30,
\]

and therefore

\[
|G'(z)|
<\frac{19}{49}+\frac{60}{343}
=\frac{193}{343}.
\tag{4.3}
\]

Because `(s-2)/s^2` is decreasing for `s>4` and `y<55/7`, (4.1) gives

\[
\operatorname{Re}G(iy)
>\frac{287}{3025}.
\tag{4.4}
\]

The mean-value bound along the horizontal segment now yields

\[
\operatorname{Re}G(-x+iy)
>\frac{287}{3025}-\frac1{20}\frac{193}{343}>0,
\]

where the final inequality is an exact rational comparison. `square`

## 5. Explicit directed-cycle family

For `n>=3`, let `P_n` be the cyclic shift on `Z/nZ` and let

\[
Q_n=P_n-I.
\tag{5.1}
\]

This is an irreducible continuous-time Markov generator with uniform stationary law and is normal in `L^2(pi)`. Let

\[
\theta_n=\frac{2\pi}{n},
\qquad
\lambda_n=e^{i\theta_n}-1=-\alpha_n+i\beta_n,
\]

where

\[
\alpha_n=1-\cos\theta_n,
\qquad
\beta_n=\sin\theta_n>0.
\]

Take the real Fourier observable

\[
g_n(j)=\cos(2\pi j/n).
\]

Its stationary covariance is

\[
C_n(t)=\frac12 e^{-\alpha_nt}\cos(\beta_nt).
\tag{5.2}
\]

Choose

\[
c_n=\frac{5\pi}{2\beta_n}.
\tag{5.3}
\]

Then

\[
c_n\lambda_n=-x_n+\frac{5\pi i}{2},
\qquad
x_n=\frac{5\pi}{2}\frac{1-\cos\theta_n}{\sin\theta_n}
=\frac{5\pi}{2}\tan\!\left(\frac\pi n\right).
\tag{5.4}
\]

For `n>=1000`, `pi/n<1/100`, and the elementary estimate `tan t<=2t` on `[0,1/100]`, together with `pi<22/7`, gives

\[
x_n
<\frac{55}{7}\frac{44}{7n}
=\frac{2420}{49n}
\le\frac{2420}{49000}
<\frac1{20}.
\tag{5.5}
\]

Lemma 4.1 therefore applies.

**Theorem 5.1 (finite Markov time-average reversal).** For every `n>=1000`, the irreducible stationary finite-state CTMC (5.1) and the real observable `g_n` above satisfy

\[
\boxed{J_{g_n}'(c_n)>0.}
\tag{5.6}
\]

### Proof

From (5.2),

\[
J_{g_n}(c)=\frac12\operatorname{Re}\Phi(c\lambda_n),
\]

hence

\[
J_{g_n}'(c)
=\frac12\operatorname{Re}[\lambda_n\Psi(c\lambda_n)]
=\frac1{2c}\operatorname{Re}G(c\lambda_n).
\]

Equations (5.4)--(5.5) and Lemma 4.1 give positivity at `c=c_n`. `square`

Since the earlier double-counting identity gives

\[
J_g(c)=\frac12\operatorname{Var}\left(\frac1c\int_0^c g(X_t)\,dt\right),
\]

Theorem 5.1 also says that the variance of the time average of a stationary finite-state Markov observable can locally **increase** when the averaging window becomes longer.

---

# B23 -- do what the source hypothesis is designed to prevent

## 6. Why the construction is not a P0290 counterexample

The directed cycle is not stochastically monotone in any source-compatible linear order with its natural cyclic orientation. In the order `0<1<...<n-1`, compare states `n-2<n-1` and the lower set

\[
D=\{0,1,\ldots,n-3\}.
\]

Neither compared state belongs to `D`, but

\[
Q_n(n-2,D)=0,
\qquad
Q_n(n-1,D)=1,
\]

violating the generator lower-set inequality required for stochastic monotonicity. Hence Theorem 5.1 is **not** a source-valid witness and does not move `Delta_Ross`.

It nevertheless closes an important logical escape route. One cannot prove the second-order P0290 statement from stationarity, finite-state Markovity, positive definiteness of covariance, or uniform stationarity alone. A genuine proof must use the order structure; a genuine counterexample must somehow preserve both forward and reverse stochastic monotonicity while retaining enough rotational/nonnormal interference to cross the filter sign.

## 7. The exact spectral bottleneck now exposed

For a normal mode `lambda=-alpha+i beta`, write its quality ratio

\[
q=|\beta|/\alpha.
\]

Theorem 5.1 works because directed cycles have

\[
q_n=\cot(\pi/n)\to\infty.
\]

By Theorem 3.1, an `n`-state source-admissible hidden chain can have no eigenvalue with

\[
q>\cot\!\left(\frac\pi{n-1}\right).
\tag{7.1}
\]

Thus the next source attack should no longer be a blind search over images `f`. It should work directly with the **simultaneous dominance constraints for `Q` and its stationary reversal `Q*`**, asking whether those constraints force a stronger sector/numerical-range bound than (7.1), or whether they permit a high-Q mode that can be coupled to a deterministic image. This is a structurally new route compared with the exhausted four-state reflection-family search.

The 2026 Vagenende--Verbeken--Guerry theorem constrains the spectrum of forward-monotone transition matrices but does not impose the time-reversal monotonicity required by Leskelä. That extra condition is exactly the remaining opportunity.

---

## 8. Literature/status check, 2026-09-19

Leskelä source: `https://math.aalto.fi/~lleskela/paper039.html` and arXiv:2204.11856. The source is the 2022 Queueing Systems note containing Problem 2.

The newly found spectral paper was published 14 May 2026: `https://journals.uwyo.edu/index.php/ela/article/view/10159`, with arXiv v2 dated 18 Dec 2025. It establishes the monotone stochastic-matrix eigenvalue reduction used in Theorem 3.1; that machinery is prior art and is not claimed as new.

A bounded current search did not locate a later source-specific solution of Leskelä Problem 2. That is negative evidence only and is **not** treated as proof of current openness or novelty.

## 9. Outcome

- New source-relevant theorem: every `n`-state monotone CTMC eigenvalue obeys the strengthened `(n-1)`-state sector bound (3.1), by combining continuous-time monotonicity with the 2026 monotone stochastic-matrix reduction.
- Prior-art correction: the real-spectrum phenomenon for three-state monotone chains is known in the monotone-matrix literature.
- New exact obstruction theorem: finite stationary Markov chains can have `J_g'(c)>0`; the directed-cycle construction proves this for every `n>=1000` with a fully explicit observation time and observable.
- Therefore positive-definite covariance and generic Markov structure cannot prove P0290; double monotonicity must do genuine work.
- No source-admissible workload witness was produced, so `Delta_Ross` remains `UNKNOWN/UNMEASURED`.
