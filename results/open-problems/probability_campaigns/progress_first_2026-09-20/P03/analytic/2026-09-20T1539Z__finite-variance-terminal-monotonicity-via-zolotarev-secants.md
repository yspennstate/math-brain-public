Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. GPT-6 / maximum reasoning was requested only as a preference; no authenticated runtime model-effort selector or guaranteed full-hour execution is exposed here, so I do not claim it.

# P03-A analytic proof report — finite-variance terminal monotonicity via ideal-order-2 secants

**Status:** PROVED PARTIAL / NEW MOMENT-WEAKENING THEOREM CANDIDATE. Not independently audited. The full Lyons–Pemantle–Peres conjecture remains open.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Canonical ownership was already checked on assignment and is not changed here. P03-B retains the regeneration/coupling/spine role; I consumed its current `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T1504Z__escape-spine-elasticity-band-and-terminal-child-coupling.md` only for continuity and do not duplicate its quenched descendant-skeleton work. Old D0047 history is untouched.

**Captured master immediately before this write:** `9c25ca6bc22c374a8e662395c9e05a80ebe1ed5c`.

**Inherited P03-A checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1409Z__finite-second-moment-critical-profile-and-support-free-tail-identity.md`.

That report proved, under only `E nu^2<infinity`, the `W_2` critical profile

\[
X_\delta:=\frac{B_{m-\delta}}{E B_{m-\delta}}\to W
\quad\text{in }W_2,
\]

the escape scale

\[
\frac{E B_{m-\delta}}{\delta}\to \frac{m-1}{E[\nu(\nu-1)]},
\]

and the critical speed asymptotic

\[
\ell_{m-\delta}=\frac{m-1}{2E[\nu(\nu-1)]}\delta+o(\delta),
\]

but it did **not** justify a whole terminal monotonicity interval because an `o(delta)` remainder alone does not control arbitrarily fine secants.

The present run closes exactly that missing implication. The new theorem is:

> **Finite-variance terminal theorem candidate.** Assume
> \[
> P(\nu=0)=0,\qquad m:=E\nu>1,\qquad E\nu^2<\infty.
> \]
> Then there exists a law-dependent `epsilon>0` such that the parent-bias speed is strictly decreasing on
> \[
> \boxed{m-\epsilon<\lambda<m.}
> \]
> Equivalently, in the original outward-bias variable `beta=1/lambda`, the speed is strictly increasing on a nontrivial interval immediately above the critical value `1/m`.

This removes the finite-third-moment hypothesis from the inherited `0906Z` whole-terminal-interval theorem. It is still only a terminal-neighborhood result, not the full LPP conjecture.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The intermediate obligation moves from “obtain finite-variance critical values only” to “join this finite-variance terminal interval to the strongest low/intermediate-bias intervals, or obtain a support-free global derivative inequality.”

---

## 1. Source convention and current checked frontier

At a non-root vertex with `k` children I use reciprocal **parent bias** `lambda`:

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\tag{1.1}
\]

Thus increasing `lambda` pushes toward the root. For a no-leaf supercritical Galton–Watson offspring law

\[
P(\nu=0)=0,\qquad m=E\nu>1,
\tag{1.2}
\]

the transient interval is `0<=lambda<m`, and the LPP conjecture asks that `ell_lambda` be nonincreasing on that entire interval.

The current broad later monotonicity theorem checked for this campaign remains H. Song, L. Wang and K. Xiang, *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, strict decrease holds for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.3}
\]

The historical Ben Arous–Fribergh–Sidoravicius high-outward-bias theorem, arXiv:1111.5865, is not treated as the current cutoff. Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, give differentiability / analyticity in ballistic regimes but do not provide the missing sign. Aidekon, arXiv:1111.4313, supplies the exact speed representation used below. A bounded current search on 20 September 2026 found no checked source-wide resolution and no checked published whole-terminal theorem under exactly a finite-second-moment offspring assumption. That is negative evidence only, not an external novelty certificate.

---

## 2. Inherited critical normalization

Let `B_lambda` be the quenched probability, from a child-root, of never hitting its artificial parent. If `B_1,B_2,...` are iid copies, then

\[
B_\lambda\stackrel d=\frac{\sum_{i=1}^{\nu}B_i}{\lambda+\sum_{i=1}^{\nu}B_i}.
\tag{2.1}
\]

Write

\[
\delta:=m-\lambda,
\qquad e_\delta:=E B_{m-\delta},
\qquad r_\delta:=\frac{e_\delta}{\delta},
\tag{2.2}
\]

\[
X_\delta:=\frac{B_{m-\delta}}{e_\delta},
\qquad
Y_\delta:=\sum_{i=1}^{\nu}X_{\delta,i}.
\tag{2.3}
\]

Put

\[
a:=m-1,
\qquad f_2:=E[\nu(\nu-1)].
\tag{2.4}
\]

The inherited `1409Z` theorem gives, under `E nu^2<infinity`,

\[
X_\delta\to W\quad\text{in }W_2,
\tag{2.5}
\]

where `W` is the mean-one finite-variance Galton–Watson smoothing fixed point

\[
W\stackrel d=\frac1m\sum_{i=1}^{\nu}W_i,
\tag{2.6}
\]

and

\[
r_\delta\to r_0:=\frac{a}{f_2}>0.
\tag{2.7}
\]

Also

\[
E W^2=v_*:=\frac{f_2}{m a}.
\tag{2.8}
\]

After shrinking a terminal scale `delta_0>0`, throughout `0<delta<=delta_0` we may and do assume

\[
\frac{r_0}{2}\le r_\delta\le 2r_0,
\qquad
m-\delta\ge c_0>\sqrt m,
\qquad
0<\delta_0<\frac a2.
\tag{2.9}
\]

The middle condition is possible because `m>1`.

The normalized recursion is exactly

\[
\boxed{
X_\delta\stackrel d=
F_\delta(Y_\delta),
\qquad
F_\delta(y):=\frac{y}{c_\delta+e_\delta y},
\qquad
c_\delta:=m-\delta.
}
\tag{2.10}
\]

The exact scalar companion identity is

\[
\boxed{
\frac1{r_\delta}
=E\Psi_\delta(Y_\delta),
\qquad
\Psi_\delta(y):=\frac{y^2}{c_\delta+e_\delta y}.
}
\tag{2.11}
\]

---

## 3. The right metric: an ideal order-two seminorm

For probability laws with the same finite first moment and finite second moments, define

\[
\zeta_2(U,V)
:=
\sup_f |Ef(U)-Ef(V)|,
\tag{3.1}
\]

where the supremum is over `C^1` functions whose derivative is 1-Lipschitz:

\[
|f'(x)-f'(y)|\le |x-y|.
\tag{3.2}
\]

Because `EU=EV`, affine terms cancel. We may therefore normalize every test function by

\[
f(0)=f'(0)=0,
\tag{3.3}
\]

which gives for `x>=0`

\[
|f'(x)|\le x,
\qquad
|f(x)|\le \frac{x^2}{2}.
\tag{3.4}
\]

I use only the following two elementary “ideal metric” properties, proved directly here.

### Lemma 3.1 — independent sums

If `(U_i)` and `(V_i)` are iid families with `EU_i=EV_i`, then for each deterministic `n`,

\[
\boxed{
\zeta_2\left(\sum_{i=1}^nU_i,\sum_{i=1}^nV_i\right)
\le n\,\zeta_2(U_1,V_1).
}
\tag{3.5}
\]

Indeed replace the summands one at a time. Conditional on the other summands, the test function in the replaced coordinate still has derivative Lipschitz constant at most one. The possible affine renormalization cancels because the replaced variables have the same mean.

Conditioning on the common offspring number therefore gives

\[
\boxed{
\zeta_2(Y_\delta,Y_\eta)
\le m\,\zeta_2(X_\delta,X_\eta).
}
\tag{3.6}
\]

### Lemma 3.2 — exact fractional-linear composition bound

Let

\[
F_{c,e}(y)=\frac{y}{c+ey},\qquad c>0,\ e\ge0.
\]

Then for every admissible `f`, the derivative of `f\circ F_{c,e}` is `c^{-2}`-Lipschitz. Hence, whenever `U,V` have the same mean,

\[
\boxed{
|E f(F_{c,e}(U))-E f(F_{c,e}(V))|
\le c^{-2}\zeta_2(U,V).
}
\tag{3.7}
\]

Proof. We have

\[
F'_{c,e}(y)=\frac{c}{(c+ey)^2},
\qquad
F''_{c,e}(y)=-\frac{2ce}{(c+ey)^3}.
\tag{3.8}
\]

At points where `f''` exists, `|f''|<=1`; also `|f'(F)|<=F`. Therefore

\[
|(f\circ F)''|
\le (F')^2+F|F''|
=\frac{c(c+2ey)}{(c+ey)^4}.
\tag{3.9}
\]

Writing `t=ey/c>=0`,

\[
\frac{c(c+2ey)}{(c+ey)^4}
=\frac{1+2t}{c^2(1+t)^4}
\le \frac1{c^2}.
\tag{3.10}
\]

Thus `(f\circ F)'` is `c^{-2}`-Lipschitz. `square`

The critical law-change coefficient is consequently

\[
\rho_0:=\frac{m}{m^2}=\frac1m<1.
\tag{3.11}
\]

This strict factor is the structural reason the finite-variance argument below succeeds. The earlier `W_{3/2}` route paid a moment inequality constant; the present ideal-order-two route does not.

---

## 4. Uniform-integrability moduli replace every third moment

The family `Y_delta^2`, `0<delta<=delta_0`, is uniformly integrable. One way to see this is to use the inherited `W_2` convergence of `X_delta` and the common-offspring coupling:

\[
E|Y_\delta-Y_0|^2
=m W_2(\mathcal L(X_\delta),\mathcal L(W))^2\to0,
\tag{4.1}
\]

where `Y_0=sum_{i=1}^nu W_i`.

For `t>0` define the monotone envelope

\[
\omega(t):=
\sup_{0<s\le C t}
\sup_{0<\theta\le\delta_0}
E\left[Y_\theta^2\min\{sY_\theta,1\}\right],
\tag{4.2}
\]

where `C` is any fixed constant larger than the harmless comparison constants used below. Uniform integrability gives

\[
\boxed{\omega(t)\downarrow0\quad(t\downarrow0).}
\tag{4.3}
\]

Indeed, for any `K`, on `Y<=K` the integrand is at most `CtK Y^2`, while on `Y>K` it is at most `Y^2`; first choose `K` by uniform integrability and then `t`.

Two elementary saturation bounds will be used repeatedly. Uniformly for `c>=c_0` and `e>0`,

\[
e\,\frac{y^3}{(c+ey)^3}
\le \frac{1}{c_0^2}y^2\min\left\{\frac{ey}{c_0},1\right\},
\tag{4.4}
\]

and

\[
e\,\frac{y^3}{(c+ey)^2}
\le \frac{1}{c_0}y^2\min\left\{\frac{ey}{c_0},1\right\}.
\tag{4.5}
\]

Thus the apparent cubic terms in parameter derivatives cost only a vanishing finite-variance modulus after multiplication by the small escape scale `e`.

---

## 5. Scaled secant regularity of the normalized escape law

Fix

\[
0<\eta<\delta\le\delta_0,
\qquad h:=\delta-\eta,
\tag{5.1}
\]

and set

\[
d:=\zeta_2(X_\delta,X_\eta),
\qquad \Delta r:=r_\delta-r_\eta,
\qquad \Delta e:=e_\delta-e_\eta.
\tag{5.2}
\]

Because of (2.9),

\[
|\Delta e|
=|\delta r_\delta-\eta r_\eta|
\le 2r_0 h+\eta|\Delta r|,
\tag{5.3}
\]

and

\[
\min(e_\delta,e_\eta)\ge \frac{r_0}{2}\eta.
\tag{5.4}
\]

### Lemma 5.1 — law equation

There is a law-dependent constant `C` such that

\[
\boxed{
d
\le \rho d
+C h
+C\omega(\eta)\left(\frac h\eta+|\Delta r|\right),}
\tag{5.5}
\]

where

\[
\rho:=\frac{m}{c_0^2}<1.
\tag{5.6}
\]

Proof. For a normalized `zeta_2` test function, split

\[
Ef(F_\delta(Y_\delta))-Ef(F_\eta(Y_\eta))
\]

into the law-change term at fixed `(c_delta,e_delta)` and the parameter-change term at fixed law `Y_eta`.

The law-change term is at most

\[
c_\delta^{-2}\zeta_2(Y_\delta,Y_\eta)
\le \rho d
\]

by Lemmas 3.1–3.2.

For the parameter term, `|f'(x)|<=x`, hence for nonnegative `u,v`,

\[
|f(u)-f(v)|\le\frac{u+v}{2}|u-v|.
\tag{5.7}
\]

Changing `c` costs `C h E Y_eta^2`. Changing `e` costs at most

\[
C|\Delta e|E\frac{Y_\eta^3}{(c_0+e_*Y_\eta)^3},
\qquad e_*:=\min(e_\delta,e_\eta).
\tag{5.8}
\]

By (4.4), (5.4), and the definition of `omega`, this is

\[
C\omega(\eta)\frac{|\Delta e|}{e_*}
\le C\omega(\eta)\left(\frac h\eta+|\Delta r|\right).
\]

This proves (5.5). `square`

### Lemma 5.2 — scalar companion equation

After perhaps enlarging `C`,

\[
\boxed{
|\Delta r|
\le C d+C h
+C\omega(\eta)\left(\frac h\eta+|\Delta r|\right).}
\tag{5.9}
\]

Proof. Use (2.11). The function

\[
\Psi_{c,e}(y)=\frac{y^2}{c+ey}
\]

has

\[
\Psi''_{c,e}(y)=\frac{2c^2}{(c+ey)^3},
\tag{5.10}
\]

so its derivative is `2/c_0`-Lipschitz. Hence changing `Y_delta` to `Y_eta` costs at most `C d` by (3.6).

Changing `c` costs `C h E Y_eta^2`. Changing `e` costs

\[
|\Delta e|E\frac{Y_\eta^3}{(c_0+e_*Y_\eta)^2},
\]

which is bounded by

\[
C\omega(\eta)\frac{|\Delta e|}{e_*}
\]

using (4.5). Since `r_delta` stays bounded above and away from zero, differences of `1/r` and of `r` are equivalent up to a constant. Apply (5.3)–(5.4). `square`

### Proposition 5.3 — the scaled secant estimate

There is a deterministic modulus `epsilon(t)->0` such that for all

\[
0<\eta<\delta\le\delta_0,
\]

\[
\boxed{
\frac{\eta}{\delta-\eta}
\left[
\zeta_2(X_\delta,X_\eta)+|r_\delta-r_\eta|
\right]
\le \epsilon(\delta_0).
}
\tag{5.11}
\]

More explicitly, one may take

\[
\epsilon(\delta_0)=C[\delta_0+\omega(\delta_0)].
\tag{5.12}
\]

Proof. Shrink `delta_0` until the coefficient of `|Delta r|` in (5.9) is absorbable and the additional `O(omega(delta_0))d` produced after substitution leaves the strict contraction `rho<1` intact. Then (5.5)–(5.9) give

\[
d+|\Delta r|
\le C h\left(1+\frac{\omega(\eta)}{\eta}\right).
\tag{5.13}
\]

Multiply by `eta/h` and use the monotone envelope of `omega`. `square`

A useful immediate corollary is a genuine asymptotic secant derivative for the mean escape scale:

\[
\frac{e_\delta-e_\eta}{\delta-\eta}
=r_\delta+\eta\frac{r_\delta-r_\eta}{\delta-\eta}.
\tag{5.14}
\]

Hence

\[
\boxed{
\sup_{0<\eta<\delta\le\delta_0}
\left|
\frac{e_\delta-e_\eta}{\delta-\eta}-r_0
\right|
\longrightarrow0
\quad(\delta_0\downarrow0).
}
\tag{5.15}
\]

This is stronger than the inherited value asymptotic `e_delta/delta->r_0`; it controls arbitrarily fine terminal secants.

---

## 6. A cancellation identity for the Aidekon branch weights

Because `delta_0<a/2`, the terminal region satisfies `lambda=m-delta>1`. Aidekon’s exact speed representation can therefore be written in the effective-degree form

\[
\boxed{
\ell_{m-\delta}
=\frac{M_\delta-(m-\delta)}{M_\delta+(m-\delta)}.
}
\tag{6.1}
\]

Let

\[
D_{n,\delta}:=a-\delta+e_\delta\sum_{i=0}^{n}X_{\delta,i},
\qquad
h_n(\delta):=E\frac{X_{\delta,0}}{D_{n,\delta}}.
\tag{6.2}
\]

Since Aidekon’s original weight is `c_n=e_delta h_n`, the factor `e_delta` cancels from the effective offspring mean:

\[
M_\delta=
\frac{E[\nu h_\nu(\delta)]}{E[h_\nu(\delta)]}.
\tag{6.3}
\]

The key identity is obtained without differentiating the law `X_delta`. Since `E X_delta=1`,

\[
\begin{aligned}
h_n(\delta)-\frac1a
&=E\left[
X_{\delta,0}
\left(
\frac1{D_{n,\delta}}-\frac1a
\right)
\right]\\
&=\frac{\delta}{a}
E\left[
\frac{X_{\delta,0}
\left(1-r_\delta\sum_{i=0}^{n}X_{\delta,i}\right)}
{D_{n,\delta}}
\right].
\end{aligned}
\tag{6.4}
\]

By exchangeability of the `n+1` normalized escape variables, if

\[
S_{n+1,\delta}:=\sum_{i=0}^{n}X_{\delta,i},
\]

then

\[
\boxed{
h_n(\delta)=\frac1a+\delta F_n(\delta),}
\tag{6.5}
\]

with

\[
\boxed{
F_n(\delta)
=\frac{1}{a(n+1)}
E\left[
\frac{S_{n+1,\delta}(1-r_\delta S_{n+1,\delta})}
{a-\delta+e_\delta S_{n+1,\delta}}
\right].}
\tag{6.6}
\]

This representation is the second structural cancellation of the run: all derivatives of the normalized law disappear from the first-order branch-weight expansion.

At the critical edge, let `S_{n+1,0}=sum_{i=0}^n W_i`. Then

\[
E S_{n+1,0}=n+1,
\qquad
E S_{n+1,0}^2=(n+1)v_*+n(n+1).
\tag{6.7}
\]

Therefore

\[
\begin{aligned}
F_n(0)
&=\frac1{a^2}
\left[1-r_0(v_*+n)\right]\\
&=\boxed{\frac1{am}-\frac{n}{a f_2}}.
\end{aligned}
\tag{6.8}
\]

Here we used `r_0 v_*=1/m`.

---

## 7. Aggregate secants need only `E nu^2<infinity`

Define

\[
\bar h_\delta:=E[h_\nu(\delta)],
\tag{7.1}
\]

and the offspring-weight covariance

\[
C_\delta:=E[(\nu-m)h_\nu(\delta)].
\tag{7.2}
\]

Then

\[
M_\delta-m=\frac{C_\delta}{\bar h_\delta},
\qquad
Q_\delta:=m-M_\delta=-\frac{C_\delta}{\bar h_\delta}.
\tag{7.3}
\]

From (6.5),

\[
\boxed{
C_\delta=\delta G_\delta,
\qquad
\bar h_\delta=\frac1a+\delta H_\delta,}
\tag{7.4}
\]

where

\[
G_\delta:=E[(\nu-m)F_\nu(\delta)],
\qquad
H_\delta:=E[F_\nu(\delta)].
\tag{7.5}
\]

The next lemma is the support-free finite-variance replacement for the degreewise `O(1+j)` branch-gap estimate that forced a third moment in `0906Z`.

### Lemma 7.1 — aggregate scaled secants

There is a modulus `epsilon_1(t)->0` such that

\[
\boxed{
\sup_{0<\eta<\delta\le\delta_0}
\frac{\eta|G_\delta-G_\eta|}{\delta-\eta}
\le\epsilon_1(\delta_0),}
\tag{7.6}
\]

and similarly

\[
\boxed{
\sup_{0<\eta<\delta\le\delta_0}
\frac{\eta|H_\delta-H_\eta|}{\delta-\eta}
\le\epsilon_1(\delta_0).}
\tag{7.7}
\]

Moreover

\[
G_\delta\to G_0,
\qquad
H_\delta\to H_0
\tag{7.8}
\]

for finite constants `G_0,H_0`.

Proof. Conditional on `nu=n`, put `N=n+1` and

\[
\Phi_{b,e,r}(s):=\frac{s(1-rs)}{b+es}.
\tag{7.9}
\]

Then

\[
F_n(\delta)=\frac1{aN}E\Phi_{a-\delta,e_\delta,r_\delta}(S_{N,\delta}).
\tag{7.10}
\]

Direct differentiation gives the exact identity

\[
\boxed{
\Phi''_{b,e,r}(s)
=-\frac{2b(br+e)}{(b+es)^3}.}
\tag{7.11}
\]

Thus `Phi'` has a law-uniform Lipschitz bound on the terminal region. By Lemma 3.1,

\[
\zeta_2(S_{N,\delta},S_{N,\eta})\le N d.
\tag{7.12}
\]

The prefactor `1/N` in (7.10) cancels this random-sum factor exactly. After multiplying by `|n-m|` and averaging, the law-change part of `G_delta-G_eta` is at most `C d E|nu-m|`.

For parameter changes,

\[
\partial_b\Phi=-\frac{s(1-rs)}{(b+es)^2},
\qquad
\partial_r\Phi=-\frac{s^2}{b+es},
\tag{7.13}
\]

so after division by `N`, their conditional expectations are bounded by `C(1+n)` because

\[
\frac1N E S_{N,\theta}^2
=E X_\theta^2+N-1.
\tag{7.14}
\]

Hence the `b` and `r` changes in `G` cost at most

\[
C h+C|\Delta r|,
\tag{7.15}
\]

because

\[
E[|\nu-m|(1+\nu)]<\infty
\tag{7.16}
\]

is exactly a finite-second-moment requirement.

Finally,

\[
\partial_e\Phi
=-\frac{s^2(1-rs)}{(b+es)^2}.
\tag{7.17}
\]

Multiplying by `e`, the absolute value is dominated by

\[
C(s+s^2)
\tag{7.18}
\]

and tends pointwise to zero as `e downarrow0`. The random variables

\[
\frac{|\nu-m|}{\nu+1}
\left(S_{\nu+1,\theta}+S_{\nu+1,\theta}^2\right)
\tag{7.19}
\]

are uniformly integrable over small `theta`. To check this, first restrict to `nu<=K`, where `W_2` convergence of `X_theta` makes the finitely many fixed-sum squares uniformly integrable; for `nu>K`, conditional expectation of (7.19) is bounded by `C(1+nu^2)`, whose tail vanishes because `E nu^2<infinity`.

Consequently there is another modulus `omega_G(t)->0` such that the `e`-parameter term is at most

\[
\omega_G(\eta)
\left(\frac h\eta+|\Delta r|\right).
\tag{7.20}
\]

Combine (5.11), (7.15), and (7.20), then multiply by `eta/h`. This proves (7.6). The proof of (7.7) is the same with the factor `|nu-m|` removed and is easier.

Convergence (7.8) follows from `W_2` convergence of the fixed finite sums, the convergence `r_delta->r_0`, and the same `nu<=K` / `nu>K` finite-variance truncation. `square`

### Critical value of `G_0`

Using (6.8),

\[
\begin{aligned}
G_0
&=E\left[(\nu-m)
\left(\frac1{am}-\frac{\nu}{a f_2}\right)
\right]\\
&=-\frac{\operatorname{Var}(\nu)}{a f_2}.
\end{aligned}
\tag{7.21}
\]

The constant term vanishes because `E(nu-m)=0`.

---

## 8. The effective-degree defect has the correct derivative on **all** fine terminal secants

From (7.3)–(7.5),

\[
\boxed{
Q_\delta=\delta R_\delta,
\qquad
R_\delta:=-\frac{G_\delta}{a^{-1}+\delta H_\delta}.}
\tag{8.1}
\]

By (7.8),

\[
\boxed{
R_\delta\to
R_0:=\frac{\operatorname{Var}(\nu)}{f_2}.}
\tag{8.2}
\]

Lemmas 7.1 and the fact that `H_delta` stays bounded imply the stronger scaled-secant statement

\[
\boxed{
\sup_{0<\eta<\delta\le\delta_0}
\frac{\eta|R_\delta-R_\eta|}{\delta-\eta}
\longrightarrow0
\quad(\delta_0\downarrow0).}
\tag{8.3}
\]

Therefore

\[
\frac{Q_\delta-Q_\eta}{\delta-\eta}
=R_\delta+
\eta\frac{R_\delta-R_\eta}{\delta-\eta},
\tag{8.4}
\]

and hence

\[
\boxed{
\sup_{0<\eta<\delta\le\delta_0}
\left|
\frac{Q_\delta-Q_\eta}{\delta-\eta}
-
\frac{\operatorname{Var}(\nu)}{f_2}
\right|
\longrightarrow0
\quad(\delta_0\downarrow0).}
\tag{8.5}
\]

This is the exact finite-variance secant estimate missing from `1409Z`.

The critical slope is strictly below one:

\[
1-\frac{\operatorname{Var}(\nu)}{f_2}
=
\frac{m(m-1)}{f_2}>0,
\tag{8.6}
\]

because

\[
f_2=E\nu^2-m=\operatorname{Var}(\nu)+m^2-m.
\]

No third offspring moment appears anywhere in (8.5).

---

## 9. Strict terminal monotonicity of the speed

Write, in the `delta=m-lambda` coordinate,

\[
L_\delta:=\ell_{m-\delta}.
\tag{9.1}
\]

Since `M_delta=m-Q_delta`, (6.1) becomes

\[
\boxed{
L_\delta
=\frac{\delta-Q_\delta}{2m-\delta-Q_\delta}.}
\tag{9.2}
\]

Fix `0<eta<delta<=delta_0` and define the effective-degree secant slope

\[
s_{\delta,\eta}:=
\frac{Q_\delta-Q_\eta}{\delta-\eta}.
\tag{9.3}
\]

A direct cross multiplication gives the exact identity

\[
\boxed{
L_\delta-L_\eta
=\frac{2(\delta-\eta)
\left[m(1-s_{\delta,\eta})+\eta s_{\delta,\eta}-Q_\eta\right]}
{(2m-\delta-Q_\delta)(2m-\eta-Q_\eta)}.}
\tag{9.4}
\]

By (8.2) and (8.5), uniformly for all such pairs,

\[
s_{\delta,\eta}\to s_0:=\frac{\operatorname{Var}(\nu)}{f_2}<1,
\qquad
Q_\eta=O(\eta).
\tag{9.5}
\]

Hence the square bracket in (9.4) converges uniformly to

\[
m(1-s_0)
=\frac{m^2(m-1)}{f_2}>0.
\tag{9.6}
\]

Shrink `delta_0` once more so that the bracket is at least half of (9.6). The denominators in (9.4) are positive. Therefore

\[
\boxed{
L_\delta>L_\eta
\qquad
(0<\eta<\delta\le\delta_0).}
\tag{9.7}
\]

Returning to `lambda=m-delta`, this is exactly

\[
\boxed{
\ell_{\lambda_1}>\ell_{\lambda_2}
\qquad
(m-\delta_0\le\lambda_1<\lambda_2<m).}
\tag{9.8}
\]

Thus the parent-bias speed is strictly decreasing on the full terminal interval

\[
\boxed{m-\delta_0<\lambda<m}
\tag{9.9}
\]

under only a finite second offspring moment.

This proves the theorem candidate stated at the beginning of the report.

---

## 10. What changed mathematically

### Before this run

Under `E nu^2<infinity` the repository had only

\[
\ell_{m-\delta}
=\frac{m-1}{2f_2}\delta+o(\delta),
\]

plus fixed-ratio terminal comparisons. Whole-interval monotonicity required the stronger inherited assumption `E nu^3<infinity`.

### After this run

Under the exact finite-variance hypothesis

\[
P(\nu=0)=0,
\quad m>1,
\quad E\nu^2<\infty,
\]

there is a law-dependent terminal interval on which speed is strictly decreasing.

The decisive new mechanism is not a sharper offspring-tail moment inequality. It is the combination of:

1. the ideal-order-two contraction
   \[
   \zeta_2(F_\delta(Y_\delta),F_\delta(Y_\eta))
   \le \frac{m}{(m-\delta)^2}\zeta_2(X_\delta,X_\eta),
   \]
   whose critical factor is `1/m<1`;
2. saturation of every apparent cubic parameter derivative by the small escape scale `e_delta`, converting it to a finite-variance uniform-integrability modulus;
3. the exact normalized branch-weight identity `h_n=1/a+delta F_n`, which removes derivatives of the changing escape law at first order;
4. averaging the branch-weight secants **before** bounding the offspring degree, so the required weight is only `|nu-m|(1+nu)`, exactly second-order.

This explains retrospectively why the degreewise `g_j` Lipschitz route paid an unnecessary third moment.

---

## 11. Heavy-tailed family newly covered by the whole-interval theorem

Take for example

\[
P(\nu=1)=\frac12,
\qquad
P(\nu=n+1)=\frac{1}{2\zeta(7/2)}n^{-7/2},
\qquad n\ge1.
\tag{11.1}
\]

Then

\[
E\nu^2<\infty,
\qquad
E\nu^3=\infty,
\tag{11.2}
\]

and there is no positive exponential moment. The `1409Z` run already gave the critical linear speed slope for this example; the present theorem upgrades that value asymptotic to an actual **whole terminal monotonicity interval**. This example is outside the finite-third-moment P03-A theorem and outside the exponential-moment regime of the classical critical linear-response argument.

No explicit numerical width is claimed here; the proof is qualitative because its width depends on the uniform-integrability moduli of the law.

---

## 12. Self-checks and limitations

1. **Deterministic offspring.** If `Var(nu)=0`, then `Q_delta=0` identically and (9.2) is the regular-tree speed `(delta)/(2m-delta)` in the `delta` coordinate, strictly increasing. The proof above also has `s_0=0` and a maximal terminal margin.
2. **Strict slope margin.** The only source-level sign margin needed is (8.6), which is positive for every supercritical no-leaf law with finite second moment.
3. **No differentiation of `o(delta)`.** The proof never infers a derivative from a pointwise asymptotic. It controls all fine secants by (8.5) before using the speed formula.
4. **No hidden third moment.** The only offspring-weighted domination in Section 7 is `|nu-m|(1+nu)`, integrable exactly under `E nu^2<infinity`. Cubic-looking escape terms are always multiplied by the small `e` and handled by uniform integrability of squares.
5. **Why `lambda>1` is harmless here.** Since `m>1`, the terminal interval may be chosen with `delta_0<m-1`, hence `lambda=m-delta>1`; this is precisely the region in which the branch-weight form used above has denominators bounded away from zero.
6. **Candidate-proof status.** This is a new repository proof candidate, not an independently verified published theorem. A later audit should check especially the `zeta_2` parameter split and the aggregate uniform-integrability truncation in Lemma 7.1.
7. **Not the full conjecture.** The theorem says nothing yet about the potentially large middle interval between current low-bias certificates and the terminal neighborhood.

---

## 13. Exact remaining gap and next attack

The finite-moment obstruction at the critical edge is now removed down to the natural finite-variance level. The dominant remaining analytic problem is therefore no longer “improve the terminal moment assumption.” It is to bridge the interior.

The most promising next attack is to use the same covariance-normalized effective degree

\[
Q_\lambda=m-M(\lambda)
=-\frac{\operatorname{Cov}(\nu,h_\nu(\lambda))}{E h_\nu(\lambda)}
\tag{13.1}
\]

away from criticality, together with P03-B’s exact escape-spine elasticity representation. The target is an interior one-sided secant inequality of the form

\[
Q_{\lambda_1}-Q_{\lambda_2}
<\lambda_2-\lambda_1
\tag{13.2}
\]

in parent-bias orientation, first for a nontrivial bounded-support family but using **aggregate** branch weights rather than degreewise derivatives. The new lesson is to average over offspring before taking derivative norms; that is what reduced a third-moment cost to a second-moment cost at criticality and may also reduce the heterogeneity loss in the middle interval.

For a concrete next family, avoid duplicating current `{2,3}`, `{3,4}`, and `{1,D}` neighboring work. A useful analytic target is a genuinely three-point law such as support `{1,2,3}` with one free interior direction, where the exact two-coordinate identity from `1158Z/1308Z` is available and P03-B’s child-selection covariance bound can control the noncritical branch-selection term.

The source-level metric remains

`R_full: 1 -> 1`.
