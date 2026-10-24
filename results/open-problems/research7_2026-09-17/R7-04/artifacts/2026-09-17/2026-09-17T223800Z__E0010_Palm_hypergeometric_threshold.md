# E0010 — Palm reproduction threshold and an exact fully-mixed block theorem

Target: Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 4: for the sexual-reproduction model with fixed `beta>4.5`, prove that sufficiently fast stirring gives a unique positive/nontrivial stationary phase in the source convention.

This note continues the exact ordered-coupling reduction in `research7_2026-09-17/R7-04/artifacts/2026-09-17/2026-09-17T214000Z__E0010_disagreement_reduction.md`. It does **not** close the source problem. Its purpose is to replace the previous qualitative “relative factorization” blocker by an exact one-tag reproduction threshold and to solve that threshold in the ideal fully mixed finite-block sector.

## 1. Ordered coupling and raw disagreement reproduction

Let `eta <= xi` be a stationary basic coupling, with lower positive stationary law `mu` and upper invariant law `bar_nu`. Set

\[
D_x=\xi_x-\eta_x\in\{0,1\},\qquad q_x=\mathbb E D_x.
\]

For the source birth rule write

\[
A_x(\zeta)=\frac{1}{n(n-1)}\sum_{\substack{y,z\in N_x\\y\ne z}}\zeta_y\zeta_z.
\]

The previous run proved the exact stationary equation

\[
0=\varepsilon^{-2}\sum_{w\sim_s x}(q_w-q_x)-q_x+\beta\Gamma_x,
\tag{1.1}
\]

where

\[
\Gamma_x:=\mathbb E\!\left[(1-\xi_x)(A_x(\xi)-A_x(\eta))-D_xA_x(\eta)\right].
\tag{1.2}
\]

The first term in `Gamma_x` is the rate, per factor `beta`, at which a birth creates a disagreement at a common-zero child; the second is the rate at which a lower birth kills an existing disagreement.

### Lemma 1 (raw maximal-disagreement threshold)

If a nonzero stationary ordered disagreement field exists and `Q=sup_x q_x>0`, then along a sequence `x_m` with `q_{x_m}->Q` chosen so that

\[
\varepsilon^{-2}d_s\frac{Q-q_{x_m}}{q_{x_m}}\longrightarrow0,
\]

one has

\[
\boxed{\liminf_{m\to\infty}\frac{\Gamma_{x_m}}{q_{x_m}}\ge \frac1\beta.}
\tag{1.3}
\]

#### Proof

Since every stirring neighbor satisfies `q_w<=Q`,

\[
\varepsilon^{-2}\sum_{w\sim_s x_m}(q_w-q_{x_m})
\le \varepsilon^{-2}d_s(Q-q_{x_m}).
\]

Rearranging (1.1) gives

\[
\beta\frac{\Gamma_{x_m}}{q_{x_m}}
=1-\frac{\varepsilon^{-2}\sum_{w\sim_s x_m}(q_w-q_{x_m})}{q_{x_m}}
\ge 1-\varepsilon^{-2}d_s\frac{Q-q_{x_m}}{q_{x_m}}.
\]

Take `liminf`. QED.

This threshold is simpler than the previous stable-root remainder threshold. Indeed, with

\[
s=\sqrt{1-4/\beta},\qquad \rho=\frac{1+s}{2},\qquad
\kappa_\beta=\frac{s(1+s)}2,
\]

and `g(u)=2u-3u^2`, direct algebra gives

\[
g(\rho)+\kappa_\beta=\frac1\beta.
\tag{1.4}
\]

Thus the former `R_x/q_x >= kappa_beta` obstruction and (1.3) are the same balance written before versus after subtracting the mean-field background.

## 2. B11: exact one-tag Palm dualization

For `q_y>0`, define the discrepancy Palm expectation

\[
\widehat{\mathbb E}_y[F]:=\frac{\mathbb E[D_yF]}{q_y}.
\]

The exact pair identity from the previous run is

\[
A_x(\xi)-A_x(\eta)
=\frac1{n(n-1)}\sum_{y\ne z}
\bigl(D_y\xi_z+\eta_yD_z\bigr).
\tag{2.1}
\]

Substitution into (1.2) yields the following exact adjoint/Palm formula.

### Lemma 2 (Palm reproduction identity)

Whenever `q_x>0`,

\[
\boxed{
\frac{\Gamma_x}{q_x}
=\frac1{n(n-1)}\sum_{y\ne z}
\left[
\frac{q_y}{q_x}\widehat{\mathbb E}_y[(1-\xi_x)\xi_z]
+\frac{q_z}{q_x}\widehat{\mathbb E}_z[(1-\xi_x)\eta_y]
-\widehat{\mathbb E}_x[\eta_y\eta_z]
\right].}
\tag{2.2}
\]

#### Proof

For the first summand of (2.1),

\[
\mathbb E[(1-\xi_x)D_y\xi_z]
=q_y\widehat{\mathbb E}_y[(1-\xi_x)\xi_z].
\]

For the second,

\[
\mathbb E[(1-\xi_x)\eta_yD_z]
=q_z\widehat{\mathbb E}_z[(1-\xi_x)\eta_y].
\]

Finally,

\[
\mathbb E[D_x\eta_y\eta_z]
=q_x\widehat{\mathbb E}_x[\eta_y\eta_z].
\]

Insert these three identities into (1.2) and divide by `q_x`. QED.

At approximate-maximal sites, the ratios `q_y/q_x` and `q_z/q_x` are asymptotically at most one. Therefore the remaining source obstruction is a **one-tag reproduction number**, not a full relative factorization of every local correlation.

## 3. B6/B30 solvable endpoint: exact color exchangeability

Consider a finite block of `M>=4` sites. Under the ordered coupling each site has one of three colors:

- `A`: common one, `(eta,xi)=(1,1)`;
- `C`: common zero, `(eta,xi)=(0,0)`;
- `K`: discrepancy, `(eta,xi)=(0,1)`.

Use the same letters for their counts, so `A+C+K=M`, and assume `K>0`. Suppose that, conditional on these three counts, the colors are uniformly permuted over the block. This is the exact equilibrium of the pure interchange/stirring dynamics on a finite block with reflecting boundary.

For any three distinct sites `x,y,z`, Palm conditioning on one discrepancy gives hypergeometric probabilities:

\[
\widehat{\mathbb P}_y(C_x,\xi_z=1)
=\frac{C}{M-1}\frac{A+K-1}{M-2},
\tag{3.1}
\]

\[
\widehat{\mathbb P}_z(C_x,\eta_y=1)
=\frac{C}{M-1}\frac{A}{M-2},
\tag{3.2}
\]

and

\[
\widehat{\mathbb E}_x[\eta_y\eta_z]
=\frac{A}{M-1}\frac{A-1}{M-2}.
\tag{3.3}
\]

All sites have the same discrepancy probability `K/M`, so the `q`-ratios in (2.2) are one. Hence every ordered parent pair has the same normalized reproduction bracket

\[
B_M(A,K)
:=\frac{C(2A+K-1)-A(A-1)}{(M-1)(M-2)}.
\tag{3.4}
\]

This formula is exact.

Write

\[
a=A/M,\qquad d=K/M,\qquad c=C/M=1-a-d.
\]

Define

\[
\psi(a,d):=c(2a+d)-a^2.
\tag{3.5}
\]

Expanding gives

\[
\boxed{\psi(a,d)=2a-3a^2+d(1-3a)-d^2.}
\tag{3.6}
\]

Moreover, (3.4) can be rewritten exactly as

\[
B_M(A,K)=\frac{M^2\psi(a,d)+M(a-c)}{(M-1)(M-2)}.
\tag{3.7}
\]

Since `|a-c|<=1` and `|psi(a,d)|<=1` on the simplex `a,d,c>=0`,

\[
\left|B_M(A,K)-\psi(a,d)\right|
=\frac{|M(a-c)+(3M-2)\psi(a,d)|}{(M-1)(M-2)}
\le \frac{4M-2}{(M-1)(M-2)}
\le \frac6{M-2}.
\tag{3.8}
\]

For completeness, `|psi|<=1` follows directly from
`psi=c(2a+d)-a^2`: the negative part is at least `-a^2>=-1`, while `2a+d<=2(a+d)<=2(1-c)`, so the positive term is at most `2c(1-c)<=1/2`.

## 4. Exact high-density contraction threshold

Set

\[
g(a):=2a-3a^2.
\]

If `a>=1/3`, then from (3.6)

\[
\psi(a,d)=g(a)+d(1-3a)-d^2\le g(a).
\tag{4.1}
\]

Thus, above density `1/3`, adding discrepancy mass can only *decrease* the ideal Palm reproduction number.

For the source range `beta>4.5`, define

\[
r_\beta:=\sqrt{1-3/\beta},\qquad
a_+(\beta):=\frac{1+r_\beta}{3}.
\tag{4.2}
\]

The number `a_+(beta)` is the larger solution of

\[
g(a)=1/\beta.
\tag{4.3}
\]

In particular `a_+(beta)>1/3`. If `a>=a_+(beta)+delta`, then, because `g` is exactly quadratic and

\[
g'(a_+)=-2r_\beta,
\]

we have

\[
g(a)\le g(a_++\delta)
=\frac1\beta-2r_\beta\delta-3\delta^2.
\tag{4.4}
\]

Combining (3.8), (4.1), and (4.4) proves the main restricted theorem of this run.

### Theorem 3 (exact fully-mixed block contraction)

Fix `beta>4.5` and `delta>0` with `a_+(beta)+delta<=1`. In a uniformly color-exchangeable block with `M>=4`, if the common-one density satisfies

\[
A/M\ge a_+(\beta)+\delta,
\]

then the normalized disagreement birth bracket obeys

\[
\boxed{
B_M(A,K)
\le \frac1\beta-igl(2r_\beta\delta+3\delta^2\bigr)+\frac6{M-2}.}
\tag{4.5}
\]

Consequently, if

\[
\frac6{M-2}<2r_\beta\delta+3\delta^2,
\tag{4.6}
\]

then

\[
B_M(A,K)<1/\beta.
\tag{4.7}
\]

By Lemma 1, an exactly mixed local sector satisfying this density margin cannot support an approximate-maximal stationary disagreement.

### Why this is stronger than the previous blocker

The stable positive mean-field root is

\[
\rho_+(\beta)=\frac{1+\sqrt{1-4/\beta}}2.
\]

For every `beta>4.5`, one has `a_+(beta)<rho_+(beta)`. Therefore a proof need **not** show relative factorization all the way to the exact density `rho_+`. It is enough to show that a tagged disagreement sees:

1. a lower/common-one density uniformly above `a_+(beta)` by some margin, and
2. enough color exchangeability that its Palm reproduction bracket is close to (3.4).

The disagreement density itself does not need a positive lower bound; once `a>1/3`, the exact `d`-dependence in (3.6) is favorable.

## 5. B6 failure that should not be repeated

A naive deformation argument would say: “take stirring to infinity, obtain the mean-field ODE, prove uniqueness there, then perturb back.” This route is invalid. For `beta>4`,

\[
f(u)=-u+\beta u^2(1-u)
\]

has **two** positive roots

\[
\rho_\pm=\frac{1\pm\sqrt{1-4/\beta}}2,
\]

with `rho_-` unstable and `rho_+` stable. Thus the infinite-mixing ODE itself does not have a unique positive equilibrium. What is solvable is the **high-density upper-phase, one-tag color-exchangeable sector**, for which Theorem 3 gives strict disagreement contraction.

## 6. B30: a nonempty mixing scale, and the exact gluing failure

The following is a scaling calculation, not a completed theorem about the infinite system.

Take a `d`-dimensional block of side `L`, so `M` is of order `L^d`. For nearest-neighbor stirring at rate `epsilon^{-2}`, the interchange mixing time on such a block has the natural diffusive scale

\[
t_{mix}\asymp \varepsilon^2 L^2\log M
\]

(up to dimension- and boundary-dependent constants). Graphical reaction marks occur at total block rate `O((1+beta)M)`. Hence the expected number of reactions anywhere in the block during one mixing window is

\[
O\!\left(\varepsilon^2L^{d+2}\log L\right).
\tag{6.1}
\]

Choosing

\[
L=\varepsilon^{-\alpha},\qquad 0<\alpha<\frac{2}{d+2},
\tag{6.2}
\]

makes `L->infinity`, `t_mix->0`, and the quantity in (6.1) tend to zero. Therefore there is a genuine mesoscopic window in which pure-stirring exchangeability is a plausible local zeroth-order approximation while the finite-size error in (4.5) vanishes.

But this **does not yet glue** to the source theorem. An ordinary total-variation approximation with absolute error `o(1)` is not enough: the global disagreement density can itself tend to zero with `epsilon`, and dividing an absolute error by `q_x` reintroduces the original obstruction.

The relative route must keep the discrepancy tag throughout the averaging argument.

For the source ordered-pair birth rule there is a useful exact hazard count. A tagged discrepancy dies at its own death mark at rate `1`, and a lower birth at its current site can kill it at rate at most `beta`. Across all possible child sites, ordered birth pairs in which the tag is one parent have total graphical mark rate exactly `2 beta` in the translation-symmetric `n`-neighbor model: there are `n` possible children and `2(n-1)` ordered pairs containing the tag for each child, each with rate `beta/[n(n-1)]`. Thus directly tag-involving non-stirring marks have rate at most

\[
1+3\beta,
\tag{6.3}
\]

independent of `epsilon` and of the global disagreement density.

Equation (6.3) does not control all reactions in the tag's environment, so it is not yet a Palm replacement theorem. It does show why a **tagged interchange averaging** estimate can plausibly be relative rather than lose a factor `1/q_x`.

## 7. What is now missing

The previous blocker “prove all local correlations factorize relative to `q_x` around `rho_+`” was unnecessarily strong. The exact remaining bridge is narrower:

> **Tagged high-density averaging lemma.** At approximate-maximal stationary disagreement sites, for sufficiently fast stirring, the lower/common-one Palm density is at least `a_+(beta)+delta_beta` on a mesoscopic block and the conditional color law seen from the discrepancy is close enough to uniform exchangeability that its reproduction bracket is strictly below `1/beta`, with an error bound that is relative to the tagged event and therefore independent of the size of `q_x`.

Together with Lemma 1, such a lemma would force the disagreement field to vanish and hence give source uniqueness.

This note proves the exact threshold and the fully mixed finite-block theorem. It does **not** prove the tagged high-density averaging lemma, does not show `Q_SR=0`, and therefore remains PARTIAL.