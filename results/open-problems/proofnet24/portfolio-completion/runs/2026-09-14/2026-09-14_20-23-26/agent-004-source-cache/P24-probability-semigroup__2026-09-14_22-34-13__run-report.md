# ProofNet24 P24 — Probability Semigroup

**Run timestamp:** 2026-09-14 22:34:13 Asia/Jerusalem  
**Scope:** product-space noise semigroups, Hoeffding/ANOVA concentration, Efron–Stein influence, P14 fixed-apex null-projector correlation; cross-checks against P11 Xi and P13 weak-tail RMT; **NO number theory**.

# Exact target selected this run

The latest P14 report has isolated the arbitrary-finite-variance bulk problem as a scale-local ANOVA theorem.

Let

\[
n=m-1,
\]

and let

\[
\Pi=\Pi(X_1,\ldots,X_n)
\]

be the rank-one orthogonal projector onto the null line of an \(n\times m\) iid-row matrix.

Its Hilbert-valued Hoeffding decomposition is

\[
\Pi=\sum_{S\subset[n]}\Pi_S,
\]

with level energies

\[
W_s
=
\sum_{|S|=s}E\|\Pi_S\|_F^2,
\qquad
W_s\ge0,
\qquad
\sum_{s=0}^{n}W_s=1.
\]

The fixed-apex \(D\)-stratified quadratic purity is

\[
R_D
=
\sum_{s=0}^{m-D}
\frac{\binom{m-D}{s}}
{\binom{m-1}{s}}
W_s.
\]

P14's sharp finite-variance bulk target is

\[
\boxed{
R_D\le \frac{C_\xi}{D},
\qquad
3\le D\le m.
}
\tag{T1}
\]

The singular high-correlation edge is already separately controlled at order \(C_\xi/D\), so (T1) is the live bulk obstruction.

The associated Bernoulli row-resampling semigroup is

\[
\boxed{
N_m(\theta)
=
E\,\operatorname{tr}(\Pi\Pi^\theta)
=
\sum_{s=0}^{n}\theta^sW_s,
\qquad
0\le\theta\le1.
}
\tag{T2}
\]

The Gaussian comparison curve is

\[
G_m(\theta)
=
\frac{1-\theta^m}{m(1-\theta)}.
\]

The latest P14 theorem `P14-HOEFFDING-BANDPASS-05` shows that the dyadic reveal block

\[
R_q-R_{2q}
\]

is a positive band-pass filter concentrated on Hoeffding degrees

\[
s\asymp m/q.
\]

This run asks the probability/semigroup question suggested by that result:

> Can the scale-local P14 shell theorem be reformulated as a standard concentration quantity—namely the Efron–Stein/Dirichlet energy of a **noise-smoothed null projector**?

The answer is yes.

---

# Main new theorem

## `P24-SMOOTH-INFLUENCE-CRITERION-06` — PROVED

For

\[
0<\theta<1,
\]

let \(T_\rho\) be the product row-resampling noise operator, so that on a Hoeffding component

\[
T_\rho\Pi_S=\rho^{|S|}\Pi_S.
\]

Define the smoothed projector

\[
\boxed{
F_\theta
=
T_{\sqrt\theta}\Pi.
}
\tag{S0}
\]

Define its total row Efron–Stein influence

\[
\boxed{
\mathcal I_m(\theta)
=
\sum_{i=1}^{n}
E\left\|
F_\theta
-
E[F_\theta\mid X_{-i}]
\right\|_F^2.
}
\tag{S1}
\]

Equivalently, if \(X^{(i)}\) is obtained by replacing only row \(X_i\) by an independent copy,

\[
\boxed{
\mathcal I_m(\theta)
=
\frac12
\sum_{i=1}^{n}
E\|
F_\theta(X)-F_\theta(X^{(i)})
\|_F^2.
}
\tag{S2}
\]

Then

\[
\boxed{
\mathcal I_m(\theta)
=
\sum_{s=1}^{n}
s\theta^sW_s
=
\theta N_m'(\theta).
}
\tag{S3}
\]

Define the normalized semigroup Dirichlet energy

\[
\boxed{
\mathscr D_m(\theta)
=
(1-\theta)N_m'(\theta)
=
\frac{1-\theta}{\theta}\,
\mathcal I_m(\theta).
}
\tag{S4}
\]

For every integer \(q\ge2\) with \(q<m\), put

\[
\boxed{
\eta_q
=
1-\frac{q}{4(m-1)}.
}
\tag{S5}
\]

Then:

### Direct block domination

For every \(q\ge2\),

\[
\boxed{
R_q-R_{\min(2q,m)}
\le
8\,
\mathscr D_m(\eta_q).
}
\tag{S6}
\]

### Sharp theorem criterion

Up to universal changes in constants, the sharp P14 theorem

\[
R_D\lesssim_\xi D^{-1}
\quad
(1\le D\le m)
\]

is equivalent to:

1. the zero-shared-row anchor
   \[
   \boxed{
   R_m=W_0\lesssim_\xi m^{-1};
   }
   \tag{S7}
   \]

2. for dyadic integers
   \[
   2\le q<m,
   \]
   the smoothed influence estimate
   \[
   \boxed{
   \mathscr D_m(\eta_q)
   \lesssim_\xi
   q^{-1}.
   }
   \tag{S8}
   \]

Equivalently, because

\[
1-\eta_q=\frac{q}{4(m-1)},
\]

condition (S8) is

\[
\boxed{
\mathcal I_m(\eta_q)
\lesssim_\xi
\frac{m}{q^2}.
}
\tag{S9}
\]

Therefore the remaining P14 geometry can be stated entirely as:

\[
\boxed{
\text{prove Gaussian-scale Efron--Stein influence for the row-noise-smoothed null projector at }O(\log m)\text{ dyadic scales}.
}
\]

This is a concentration theorem, not a global angular-universality theorem.

---

# 1. Research state read this run

## 1.1 Latest P24

Full prior report:

`2026-09-14_21-33-50__run-report.md`

Library file id:

`file_000000008cbc8230af4289f7c1be8575`.

Its principal P14 results were:

### `P24-DYADIC-BLOCK-CRITERION-05`

For dyadic \(q\), with

\[
q^+=\min(2q,m),
\]

define

\[
\mathcal B_m(q)
=
R_q-R_{q^+}.
\]

Then sharp purity is equivalent, up to universal constants, to

\[
R_m=O(m^{-1})
\]

plus

\[
\mathcal B_m(q)=O(q^{-1})
\]

on the dyadic \(q\)'s.

### `P24-DYADIC-NOISE-CHECKPOINT-05`

It is enough to establish the sharp row-noise comparison at the \(O(\log m)\) effective-dimension checkpoints

\[
1+(m-1)(1-\theta)=2^k.
\]

### `P24-XI-CYL-MIX-RATE-05`

For Gaussian cylinder characters of the exact Xi scaling skew flow, correlations decay as

\[
O(e^{-h/4})
\]

at logarithmic scale separation \(h\).

The prior report explicitly left the dyadic P14 block geometry as the highest-value probability target.

## 1.2 Latest P14

Full latest report:

`P14_probability_correlation_2026-09-14_22-20-39.md`

Library file id:

`file_0000000069f8824697602ef8931c40e9`.

The exact fixed-apex conditioning is:

1. take two overlapping \((m-1)\)-row sets \(S,T\);
2. condition on the actual shared rows
   \[
   A=S\cap T;
   \]
3. work in
   \[
   E_A=\operatorname{span}(A)^\perp,
   \qquad
   \dim E_A=D;
   \]
4. the two private original-row blocks are then independent;
5. the coordinates of a projected residual row
   \[
   Q_A^\top X
   \]
   are generally dependent and are never replaced by iid coordinates.

The newest P14 theorem is:

### `P14-HOEFFDING-BANDPASS-05`

For

\[
2q\le m,
\]

\[
R_q-R_{2q}
=
\sum_s b_{m,q}(s)W_s,
\]

where, with

\[
x=\frac{sq}{m-1},
\]

\[
0\le b_{m,q}(s)
\le
\min\{x,e^{-x/2}\}.
\]

On

\[
\frac1{16}
\le
x
<
\frac18,
\]

\[
b_{m,q}(s)\ge\frac1{32}.
\]

Hence the block probes Hoeffding degrees

\[
s\asymp m/q.
\]

Its corollary `P14-DYADIC-ANOVA-LOCALIZATION-05` says the sharp theorem is equivalent to Gaussian-scale energy in those logarithmic degree bands, plus \(W_0=O(1/m)\).

This run independently audits the band-pass lemma below.

## 1.3 Latest P11

The newest P11 report is

`P11_Xi_diffusion_paths_2026-09-14_2214.md`.

Its \(p=\infty\) endpoint problem has advanced beyond the previous P24 state.

P11 now proves the sharp continuum law

\[
\limsup_{q\downarrow0}
\frac{
|\Xi_{\beta q}-\Xi_0|
}{
q^{1/4}\sqrt{2\log\log(1/q)}
}
=
\varphi(B_1)^{-1/2}
\sigma_T\lambda^{1/4}
\sqrt{
\frac{4(\sqrt2-1)}{\sqrt\pi}
}
\quad\text{a.s.}
\]

Thus the old P24 Xi continuum-limsup target is no longer the highest-value unresolved probability problem.

The live P11 finite-\(p\) target is instead log removal from the shrinking-strip theorem:

\[
\boxed{
p\sqrt{q_p}\to\infty
\stackrel{?}{\Longrightarrow}
\text{shrinking-strip path CLT}.
}
\]

The currently proved sufficient condition remains

\[
\frac{\log(ep/q_p)}
{p\sqrt{q_p}}
\to0.
\]

The exact empirical objects are

\[
\widehat b_p(x,\tau)
=
\frac1p
\sum_{i=1}^p
w(Y_i;x,\tau),
\]

\[
\widehat n_p(x,\tau)
=
\frac1p
\sum_{i=1}^p
w(Y_i;x,\tau)
\{Y_i-m_\infty(x,\tau)\},
\]

and

\[
m_p-m_\infty
=
\frac{\widehat n_p}{\widehat b_p}.
\]

The logarithm in the current proof comes from uniform raw empirical-process control over the entire shrinking \((x,\tau)\)-strip.  The integrated linear influence process itself already has an endpoint \(L^2\) functional CLT.

The conceptual parallel with the new P24 theorem is important:

\[
\boxed{
\text{smooth/integrate first, then estimate influence at the scale actually used by the target}.
}
\]

No new P11 log-removal theorem is claimed in this run.

## 1.4 RMT cross-check: P13

Read in full:

`P13_fourth_moment_RMT_2026-09-14_22-04-16.md`

Library file id:

`file_000000005a1481f6adcdf1cca4cc241f`.

Its new theorem `P13-BALANCED-TAIL-MAIN-10` replaces the previous bounded-critical-tail condition by a signed mesoscopic tail-drift assumption.

Its symmetric triangular-array corollary requires only:

\[
E\xi_m^2=1,
\qquad
\|f_{\xi_m}\|_\infty\le K,
\]

with no higher moment.

The most relevant methodological result is the sequential-reservoir repair:

- a one-row useful event may lose a power of \(\log m\);
- one need not pay that loss at every predetermined stage;
- scan a linear reservoir and charge the loss only at successful scales.

For P14 this reinforces the same conclusion reached by the semigroup analysis:

\[
\boxed{
\text{do not multiply the same finite-variance defect through every intermediate residual dimension}.
}
\]

---

# 2. Product row-noise semigroup

Let

\[
X=(X_1,\ldots,X_n)
\]

be the iid row vector.

For

\[
0\le\rho\le1,
\]

let \(X^\rho\) be obtained by independently, for every \(i\),

- retaining \(X_i\) with probability \(\rho\);
- otherwise replacing it by an independent copy.

The product noise operator is

\[
T_\rho f(X)
=
E[f(X^\rho)\mid X].
\]

For the Hoeffding decomposition

\[
f=\sum_{S\subset[n]}f_S,
\]

one has the exact eigenvalue identity

\[
\boxed{
T_\rho f_S
=
\rho^{|S|}f_S.
}
\tag{2.1}
\]

For the null projector,

\[
F_\theta
=
T_{\sqrt\theta}\Pi
=
\sum_S
\theta^{|S|/2}\Pi_S.
\tag{2.2}
\]

Because the Hoeffding components are orthogonal in the Hilbert space

\[
L^2(\Omega;\operatorname{Sym}_m),
\]

\[
\boxed{
E\|F_\theta\|_F^2
=
\sum_s\theta^sW_s
=
N_m(\theta).
}
\tag{2.3}
\]

Thus P14's row-noise correlation curve is literally the squared \(L^2\)-norm of the noise-smoothed projector.

This is the discrete-product analogue of the Hermite/Ornstein–Uhlenbeck identity

\[
\|P_tf\|_2^2
=
\sum_{k\ge0}
e^{-2kt}\|f_k\|_2^2.
\]

The degree \(s\) in P14 plays the same spectral role as Hermite degree \(k\).

---

# 3. Exact Efron–Stein representation

Fix one row \(i\).

Since conditional expectation onto all rows except \(i\) removes exactly the Hoeffding components containing \(i\),

\[
E[F_\theta\mid X_{-i}]
=
\sum_{S:\,i\notin S}
\theta^{|S|/2}\Pi_S.
\]

Therefore

\[
F_\theta
-
E[F_\theta\mid X_{-i}]
=
\sum_{S:\,i\in S}
\theta^{|S|/2}\Pi_S.
\]

Orthogonality gives

\[
E\left\|
F_\theta-E[F_\theta\mid X_{-i}]
\right\|_F^2
=
\sum_{S:\,i\in S}
\theta^{|S|}
E\|\Pi_S\|_F^2.
\]

Summing \(i\),

\[
\begin{aligned}
\mathcal I_m(\theta)
&=
\sum_{i=1}^n
E\left\|
F_\theta-E[F_\theta\mid X_{-i}]
\right\|_F^2
\\
&=
\sum_S
|S|\theta^{|S|}
E\|\Pi_S\|_F^2
\\
&=
\sum_{s=1}^n
s\theta^sW_s.
\end{aligned}
\]

Since

\[
N_m'(\theta)
=
\sum_{s=1}^n
s\theta^{s-1}W_s,
\]

\[
\boxed{
\mathcal I_m(\theta)
=
\theta N_m'(\theta).
}
\]

This is (S3).

---

# 4. Exchangeable-pair form

Let \(X^{(i)}\) replace only row \(i\) by an independent copy.

Condition on \(X_{-i}\).

The two random matrices

\[
F_\theta(X),
\qquad
F_\theta(X^{(i)})
\]

are conditionally iid.

Hence

\[
\begin{aligned}
E[
\|F_\theta(X)-F_\theta(X^{(i)})\|_F^2
\mid X_{-i}
]
&=
2
E\left[
\left\|
F_\theta
-
E[F_\theta\mid X_{-i}]
\right\|_F^2
\mid X_{-i}
\right].
\end{aligned}
\]

Averaging and summing gives

\[
\boxed{
\mathcal I_m(\theta)
=
\frac12
\sum_{i=1}^n
E\|
F_\theta(X)-F_\theta(X^{(i)})
\|_F^2.
}
\]

Thus the P14 target has been converted to a canonical exchangeable-pair energy of a **smoothed** projector.

There is no inverse-singular-gap derivative in this identity.

---

# 5. Generator form

Let the product-space number operator \(\mathcal L\) be defined spectrally by

\[
\mathcal L\Pi_S
=
|S|\Pi_S.
\]

Then

\[
\boxed{
\mathcal I_m(\theta)
=
\|
\mathcal L^{1/2}
T_{\sqrt\theta}\Pi
\|_2^2.
}
\tag{5.1}
\]

The normalized Dirichlet form is

\[
\boxed{
\mathscr D_m(\theta)
=
\frac{1-\theta}{\theta}
\|
\mathcal L^{1/2}
T_{\sqrt\theta}\Pi
\|_2^2.
}
\tag{5.2}
\]

This normalization is the one that has Gaussian size

\[
1/q
\]

when

\[
1-\theta\asymp q/m.
\]

It is the precise discrete-product counterpart of measuring an OU-smoothed function by

\[
t\,\|\mathcal L^{1/2}P_tf\|_2^2.
\]

---

# 6. Proof of direct block domination

We prove (S6).

Fix

\[
q\ge2.
\]

First suppose

\[
2q\le m.
\]

Set

\[
n=m-1,
\qquad
\delta
=
1-\eta_q
=
\frac{q}{4n}.
\]

Because \(2q\le m\),

\[
\delta\le\frac16.
\]

P14 gives

\[
R_q-R_{2q}
=
\sum_s b_{m,q}(s)W_s,
\]

with

\[
x=\frac{sq}{n}
\]

and

\[
b_{m,q}(s)
\le
\min\{x,e^{-x/2}\}.
\tag{6.1}
\]

The corresponding Dirichlet coefficient is

\[
d_q(s)
=
\delta s(1-\delta)^{s-1}.
\]

Since

\[
\delta s=\frac x4,
\]

and

\[
\log(1-\delta)
\ge
-\frac{\delta}{1-\delta},
\]

\[
\begin{aligned}
d_q(s)
&=
\frac x4
(1-\delta)^{s-1}
\\
&\ge
\frac x4
(1-\delta)^s
\\
&\ge
\frac x4
\exp\left(
-\frac{\delta s}{1-\delta}
\right)
\\
&\ge
\frac x4
e^{-3x/10}.
\end{aligned}
\tag{6.2}
\]

If

\[
0<x\le1,
\]

then

\[
b_{m,q}(s)\le x
\le
4e^{3/10}d_q(s)
<
6d_q(s).
\]

If

\[
x\ge1,
\]

then

\[
\frac{b_{m,q}(s)}{d_q(s)}
\le
\frac4x
e^{-x/2+3x/10}
=
\frac4x e^{-x/5}
<
4.
\]

Thus

\[
\boxed{
b_{m,q}(s)
\le
6d_q(s)
}
\tag{6.3}
\]

for all \(s\).

Therefore

\[
R_q-R_{2q}
\le
6
\sum_s
\delta s\eta_q^{s-1}W_s
=
6\mathscr D_m(\eta_q).
\tag{6.4}
\]

Now suppose

\[
m/2<q<m.
\]

Then

\[
R_q-R_{\min(2q,m)}
=
R_q-R_m.
\]

For \(s\ge1\), the spectral coefficient is

\[
c_{m,q}(s)
=
\frac{\binom{m-q}{s}}
{\binom{m-1}{s}}.
\]

It has the hypergeometric meaning that a uniformly random \(s\)-subset avoids a fixed set of \(q-1\) coordinates.

Hence

\[
c_{m,q}(s)
\le
\exp\left(
-\frac{(q-1)s}{n}
\right)
\le
e^{-x/2},
\tag{6.5}
\]

again with

\[
x=sq/n.
\]

Here

\[
x\ge q/n>1/2.
\]

Also

\[
\delta=\frac q{4n}\le\frac14.
\]

Thus

\[
d_q(s)
\ge
\frac x4e^{-x/3}.
\]

Therefore

\[
\frac{c_{m,q}(s)}{d_q(s)}
\le
\frac4x e^{-x/6}
<8
\qquad
(x>1/2).
\]

So

\[
R_q-R_m
\le
8\mathscr D_m(\eta_q).
\]

Combining the two cases proves

\[
\boxed{
R_q-R_{\min(2q,m)}
\le
8\mathscr D_m(\eta_q).
}
\]

QED.

---

# 7. Why the quarter-noise checkpoint is natural

The choice

\[
1-\eta_q
=
\frac{q}{4(m-1)}
\]

is not cosmetic.

The dyadic block coefficient has two regimes:

\[
b_{m,q}(s)
\lesssim
\min\left\{
\frac{sq}{m},
e^{-c\,sq/m}
\right\}.
\]

A Dirichlet coefficient at noise scale

\[
1-\eta
\asymp q/m
\]

has the form

\[
(1-\eta)s\eta^{s-1}
\asymp
\frac{sq}{m}
\exp\left(
-c'
\frac{sq}{m}
\right).
\]

To dominate the block coefficient for large degrees one needs

\[
c'<1/2.
\]

The factor \(1/4\) in the noise level provides exactly this slack.

Thus the semigroup smoothing is calibrated to the *whole dyadic shell*, not merely to its central ANOVA band.

---

# 8. Sharp purity implies the smoothed-influence bound

Assume

\[
\boxed{
R_D\le\frac C D
\quad
(1\le D\le m).
}
\tag{8.1}
\]

The already-proved P14 Hardy/noise equivalence yields

\[
\boxed{
N_m(u)
\le
C_1 C\,G_m(u)
}
\tag{8.2}
\]

for a universal constant \(C_1\).

We now bound the derivative without differentiating (8.2).

Let

\[
0<\theta<1,
\qquad
\delta=1-\theta.
\]

For every \(s\ge1\),

\[
\delta s\theta^{s/2}
\le
(-\log\theta)
s
e^{-(-\log\theta)s/2}.
\]

Put

\[
z=\frac12(-\log\theta)s.
\]

Then

\[
\delta s\theta^{s/2}
\le
2ze^{-z}
\le
\frac2e.
\]

Therefore

\[
\begin{aligned}
\mathcal I_m(\theta)
&=
\sum_s
s\theta^sW_s
\\
&=
\sum_s
\theta^{s/2}
\left[
s\theta^{s/2}
\right]W_s
\\
&\le
\frac{2}{e\delta}
\sum_s
\theta^{s/2}W_s
\\
&=
\frac{2}{e\delta}
N_m(\sqrt\theta).
\end{aligned}
\tag{8.3}
\]

Using (8.2),

\[
\mathcal I_m(\theta)
\le
\frac{2C_1C}{e\delta}
G_m(\sqrt\theta).
\]

The explicit Gaussian curve satisfies

\[
G_m(u)
\le
\frac1{m(1-u)}.
\]

Since

\[
1-\sqrt\theta
=
\frac{\delta}{1+\sqrt\theta}
\ge
\frac\delta2,
\]

\[
\boxed{
\mathcal I_m(\theta)
\le
\frac{4C_1C}
{e\,m\delta^2}.
}
\tag{8.4}
\]

Consequently,

\[
\begin{aligned}
\mathscr D_m(\theta)
&=
\frac{\delta}{\theta}
\mathcal I_m(\theta)
\\
&\le
\frac{4C_1C}
{e\,m\,\theta\,\delta}.
\end{aligned}
\tag{8.5}
\]

At

\[
\theta=\eta_q
=
1-\frac{q}{4n},
\]

with \(q<m\),

\[
\eta_q\ge3/4
\]

and

\[
m\delta
=
\frac{mq}{4(m-1)}
\asymp q.
\]

Therefore

\[
\boxed{
\mathscr D_m(\eta_q)
\le
\frac{C_2C}{q}.
}
\tag{8.6}
\]

Equivalently,

\[
\boxed{
\mathcal I_m(\eta_q)
\le
C_3 C\,
\frac{m}{q^2}.
}
\tag{8.7}
\]

Thus the smoothed-influence theorem is **necessary** at exactly the Gaussian scale.

---

# 9. Smoothed influence implies sharp purity

Assume the anchor

\[
R_m\le C_0/m
\]

and, for every dyadic integer

\[
2\le q<m,
\]

\[
\mathscr D_m(\eta_q)
\le
C_1/q.
\]

By the direct block domination,

\[
R_q-R_{\min(2q,m)}
\le
8C_1/q.
\]

Therefore the already-proved `P24-DYADIC-BLOCK-CRITERION-05` gives

\[
\boxed{
R_D
\le
\frac{
C(C_0+C_1)
}{D}
}
\]

for every \(D\).

This proves sufficiency.

Together with Section 8, it proves the equivalence in `P24-SMOOTH-INFLUENCE-CRITERION-06`.

---

# 10. Equivalent scale-local band statement

There is a second useful formulation at P14's natural checkpoint

\[
\theta_q
=
1-\frac{q-1}{m-1}.
\]

For

\[
2\le q\le m/2,
\]

define

\[
\mathscr D_m(\theta_q)
=
(1-\theta_q)N_m'(\theta_q).
\]

If

\[
s\in I_q
=
\left\{
s:
\frac1{16}
\le
\frac{sq}{m-1}
<
\frac18
\right\},
\]

then

\[
y
=
s(1-\theta_q)
=
\frac{s(q-1)}{m-1}
\]

satisfies

\[
\frac1{32}
\le y\le\frac18.
\]

Bernoulli's inequality gives

\[
\theta_q^{s-1}
\ge
1-(s-1)(1-\theta_q)
\ge
1-y
\ge
\frac78.
\]

Hence each degree in \(I_q\) has normalized Dirichlet weight at least

\[
\frac7{256}.
\]

Therefore:

## `P24-DIRICHLET-BAND-06` — PROVED

\[
\boxed{
\sum_{s\in I_q}W_s
\le
\frac{256}{7}
\mathscr D_m(\theta_q).
}
\tag{10.1}
\]

Thus the latest P14 band theorem can be attacked directly by proving

\[
\boxed{
\mathscr D_m(\theta_q)
\lesssim_\xi
q^{-1}.
}
\tag{10.2}
\]

The quarter-noise checkpoint \(\eta_q\) is stronger in one sense: it dominates the **entire reveal block**, including both central and high-degree tails.

The natural checkpoint \(\theta_q\) is sharper for localization to the central ANOVA band.

Both are now exact semigroup bridges.

---

# 11. Gaussian calibration

For Gaussian original rows, P14 has

\[
W_s^{\rm G}
=
\frac1m,
\qquad
0\le s\le m-1.
\]

Hence

\[
N_m^{\rm G}(\theta)
=
\frac1m
\sum_{s=0}^{m-1}\theta^s
=
G_m(\theta).
\]

The smoothed influence is exactly

\[
\boxed{
\mathcal I_m^{\rm G}(\theta)
=
\frac1m
\sum_{s=1}^{m-1}
s\theta^s.
}
\tag{11.1}
\]

Using the finite geometric derivative,

\[
\boxed{
\mathcal I_m^{\rm G}(\theta)
=
\frac{
\theta
\left[
1-m\theta^{m-1}
+(m-1)\theta^m
\right]
}{
m(1-\theta)^2
}.
}
\tag{11.2}
\]

At a semigroup time satisfying

\[
1-\theta\asymp q/m,
\]

this is

\[
\boxed{
\mathcal I_m^{\rm G}(\theta)
\asymp
\frac{m}{q^2}.
}
\tag{11.3}
\]

Correspondingly,

\[
\boxed{
\mathscr D_m^{\rm G}(\theta)
\asymp
\frac1q.
}
\tag{11.4}
\]

This confirms that (S8)--(S9) are not merely sufficient estimates; they are the exact Gaussian orders.

A direct finite-\(m\) computation also reproduces

\[
R_q^{\rm G}-R_{2q}^{\rm G}
=
\frac1{2q}
\]

whenever \(2q\le m\).

---

# 12. Counterexample check: raw influence is the wrong target

One might try to prove a dimension-free one-row stability theorem for the **unsmoothed** projector.

That target is false even in the Gaussian benchmark.

At

\[
\theta=1,
\]

\[
\mathcal I_m^{\rm G}(1)
=
\frac1m
\sum_{s=1}^{m-1}s
=
\frac{m-1}{2}.
\]

Thus

\[
\boxed{
\mathcal I_m(1)=O(1)
}
\]

cannot hold in general.

The correct statement is scale dependent:

\[
\boxed{
\mathcal I_m(\theta)
\asymp
\frac{m}{q^2}
\qquad
\text{when }
1-\theta\asymp q/m.
}
\]

This is another reason uniform one-row influence estimates failed in the earlier P14 program.

Noise smoothing is not optional.

---

# 13. Counterexample check: generic product-space inequalities still do not solve P14

The abstract P14 counterexample spectrum

\[
W_0=\frac1m,
\qquad
W_1=1-\frac1m,
\qquad
W_s=0
\quad(s\ge2)
\]

satisfies every formal product-space property:

- nonnegative Hoeffding spectrum;
- total mass one;
- complete reveal monotonicity;
- legitimate row-noise polynomial.

For it,

\[
\mathcal I_m(\theta)
=
\theta
\left(
1-\frac1m
\right).
\]

At a scale

\[
q\gg\sqrt m,
\]

the desired bound

\[
\mathcal I_m(\eta_q)
\lesssim
\frac{m}{q^2}
\]

fails.

Therefore:

\[
\boxed{
\text{Efron--Stein, hypercontractivity or semigroup positivity alone cannot prove the new criterion.}
}
\]

The null-projector geometry must enter.

The advantage of the new theorem is that it identifies **where** that geometry must enter: a smoothed row influence, rather than a singular derivative of the raw projector.

---

# 14. Why smoothing may help the geometry

The raw null projector has severe one-row sensitivity near a small residual singular gap.

The semigroup-smoothed object

\[
F_{\eta_q}=T_{\sqrt{\eta_q}}\Pi
\]

averages the projector over independent row replacements before one measures row influence.

The target

\[
\frac12
\sum_i
E\|
F_{\eta_q}(X)-F_{\eta_q}(X^{(i)})
\|_F^2
\lesssim
\frac{m}{q^2}
\]

has three potentially useful features.

### 14.1 No matrix derivative

No derivative of a singular vector or projector appears.

The comparison is between bounded rank-one projectors after probabilistic smoothing.

### 14.2 The smoothing scale matches the residual dimension

At

\[
1-\eta_q\asymp q/m,
\]

the noise operator refreshes approximately \(q\) rows.

That is exactly the scale of the residual block in P14.

### 14.3 Heavy tails can be charged at one scale

A large-coordinate shell need only be controlled when the semigroup refresh count is comparable to the shell's active-row count.

This is the same scale-local accounting principle that succeeds in the latest P13 sequential-reservoir proof.

---

# 15. A useful exchangeable-pair target

The new theorem suggests the following geometric statement as the next actual probability lemma.

Let

\[
\widetilde\Pi_q
=
T_{\sqrt{\eta_q}}\Pi.
\]

For \(X^{(i)}\) obtained by resampling one original row, prove

\[
\boxed{
\sum_{i=1}^{m-1}
E\|
\widetilde\Pi_q(X)
-
\widetilde\Pi_q(X^{(i)})
\|_F^2
\le
C_\xi
\frac{m}{q^2}.
}
\tag{15.1}
\]

This is exactly twice the \(\mathcal I_m\) target.

By row exchangeability it is equivalent to

\[
\boxed{
E\|
\widetilde\Pi_q(X)
-
\widetilde\Pi_q(X^{(1)})
\|_F^2
\le
\frac{C_\xi}{q^2}.
}
\tag{15.2}
\]

This is strikingly cleaner than the original pair theorem.

It asks for an \(O(q^{-2})\) one-row influence **after \(q\)-scale noise smoothing**.

The raw one-row influence need not be small.

---

# 16. Conditioning structure for a future proof

The correct proof order must preserve P14's overlap dependence.

For one resampled row \(i\):

1. expose all original rows other than the random refresh set and row \(i\);
2. expose the Bernoulli refresh set used by \(T_{\sqrt{\eta_q}}\);
3. condition on the actual shared span;
4. only then use the genuinely fresh original rows;
5. compare the two smoothed rank-one projectors.

Projected residual coordinates remain dependent.

The only independent objects are the private **original rows** after conditioning.

This is the same dependence discipline used successfully by P12/P13 and P21.

---

# 17. Relation to the P14 cofactor-volume 2-design

P14 already has an exact spherical 2-design after endogenous cofactor-volume size bias.

That theorem was previously difficult to use because de-biasing to the ordinary null-line law required controlling a singular reciprocal volume.

The new smoothed-influence target suggests a softer use.

Instead of de-biasing one raw null line, one can try to prove the Efron–Stein difference after averaging over the semigroup refresh set.

The refreshed block supplies approximately \(q\) independent chances to regularize the cofactor-volume denominator.

A promising target is a block good event on which the refreshed cofactor sum has a lower bound at its natural \(q\)-scale, while the bad event is absorbed by the already-proved bounded-density singular-edge theorem.

This route avoids asking for a global inverse determinant moment.

No such lower-tail theorem is proved in this run.

---

# 18. Relation to P13 finite-variance shell charging

P13's newest theorem uses the mesoscopic cutoff

\[
4\sqrt{m/\log\log m}
\]

and accepts a logarithmic one-row loss.

The proof succeeds because it scans fresh rows sequentially and charges the loss only upon a successful stage.

For P14, the exact analogue should be:

- decompose \(\xi^2\) into dyadic magnitude shells;
- associate a shell with the noise-refresh scale \(q\) at which it contributes \(O(1)\) active rows;
- bound its contribution to the smoothed one-row influence;
- sum disjoint shell energies using only
  \[
  E\xi^2<\infty.
  \]

The new semigroup criterion gives the exact norm in which this must be carried out.

The old proof charged a cumulative tail modulus at every intermediate \(D\), producing

\[
\Lambda_\xi(D)=D^{o(1)}.
\]

The new target offers a way to charge each shell once.

---

# 19. Relation to P11

The latest P11 has now solved the \(p=\infty\) sharp endpoint continuum LIL.

Its remaining finite-\(p\) issue is the logarithm in

\[
\frac{\log(ep/q_p)}
{p\sqrt{q_p}}
\to0.
\]

The current P11 proof obtains this logarithm by controlling raw denominator/score fields uniformly over a two-parameter shrinking strip before integrating the path equation.

The P24/P14 theorem suggests a general semigroup lesson:

\[
\boxed{
\text{measure the smoothed/integrated functional's influence, not the raw field's worst-case coordinate fluctuation.}
}
\]

For P11 the analogous object would be a self-normalized, path-integrated empirical influence or a martingale variance along the Brownian path tube.

This is a plausible route to the conjectured condition

\[
p\sqrt{q_p}\to\infty.
\]

However, no log-removal theorem is claimed here.

The denominator is nonlinear and can still fail to self-average at

\[
q\asymp p^{-2}.
\]

---

# 20. Independent peer audit

## AUDIT_FOR=P14 — `P14-HOEFFDING-BANDPASS-05`

**Source report:**  
`P14_probability_correlation_2026-09-14_22-20-39.md`

**Library file id:**  
`file_0000000069f8824697602ef8931c40e9`

**Claim ID:**  
`P14-HOEFFDING-BANDPASS-05`

**Audit ID:**  
`P24-AUDIT-P14-BANDPASS-06`

### Claim

For

\[
n=m-1,
\qquad
2q\le m,
\]

define

\[
b_{m,q}(s)
=
\frac{
\binom{m-q}{s}
-
\binom{m-2q}{s}
}{
\binom{m-1}{s}
}.
\]

Put

\[
x=\frac{sq}{n}.
\]

P14 claims

\[
0\le b_{m,q}(s)
\le
\min\{x,e^{-x/2}\},
\]

and, if

\[
0<x\le1/8,
\]

\[
b_{m,q}(s)\ge x/2.
\]

### Audit

Choose disjoint deterministic sets

\[
F,J\subset[n]
\]

with

\[
|F|=q-1,
\qquad
|J|=q.
\]

Let \(K\) be a uniformly random \(s\)-subset of \([n]\).

Then

\[
\boxed{
b_{m,q}(s)
=
P\{
K\cap F=\varnothing,
K\cap J\ne\varnothing
\}.
}
\tag{20.1}
\]

Indeed,

\[
P\{K\cap F=\varnothing\}
=
\frac{\binom{m-q}{s}}
{\binom{m-1}{s}},
\]

while avoiding both \(F\) and \(J\) gives

\[
\frac{\binom{m-2q}{s}}
{\binom{m-1}{s}}.
\]

The first upper bound is

\[
b_{m,q}(s)
\le
P\{K\cap J\ne\varnothing\}
\le
\frac{sq}{n}
=x.
\]

The second is

\[
\begin{aligned}
b_{m,q}(s)
&\le
P\{K\cap F=\varnothing\}
\\
&\le
\left(
1-\frac{q-1}{n}
\right)^s
\\
&\le
\exp\left(
-\frac{(q-1)s}{n}
\right)
\\
&\le
e^{-x/2},
\end{aligned}
\]

because \(q\ge2\).

For the lower bound, use the sufficient event:

> \(K\) contains exactly one point of \(F\cup J\), and this point belongs to \(J\).

Its probability is

\[
\frac{
q\binom{n-2q+1}{s-1}
}{
\binom ns
}
=
x
\frac{
\binom{n-2q+1}{s-1}
}{
\binom{n-1}{s-1}
}.
\]

The ratio is the probability that a uniformly random \((s-1)\)-subset avoids \(2q-2\) forbidden points.

By the union bound,

\[
\frac{
\binom{n-2q+1}{s-1}
}{
\binom{n-1}{s-1}
}
\ge
1-
\frac{(s-1)(2q-2)}{n-1}.
\]

Since

\[
\frac{n}{n-1}\le2,
\]

the deficit is at most

\[
4\frac{sq}{n}
=
4x.
\]

If

\[
x\le1/8,
\]

the ratio is at least \(1/2\).

Thus

\[
b_{m,q}(s)\ge x/2.
\]

Every step checks.

### Verdict

\[
\boxed{
\texttt{P14-HOEFFDING-BANDPASS-05: PROVED / PASS.}
}
\]

The audit is purely combinatorial and introduces no independence assumption about projected residual coordinates.

---

# 21. Route comparison

## Route A — smoothed Efron–Stein / exchangeable pairs

**PROMOTED TO PRIMARY.**

The exact target is now

\[
\boxed{
\mathcal I_m(\eta_q)
\le
C_\xi\frac{m}{q^2}.
}
\]

Advantages:

- standard concentration functional;
- no projector derivative;
- exact match to Gaussian scale;
- only \(O(\log m)\) dyadic \(q\)'s;
- compatible with block conditioning and heavy-tail shell charging.

The geometric difficulty remains nontrivial.

## Route B — direct dyadic reveal block

Still exact:

\[
R_q-R_{\min(2q,m)}
\le
C_\xi/q.
\]

The new theorem proves that Route A is a sufficient and, globally, equivalent replacement.

Route A may be easier because row resampling is built into the quantity itself.

## Route C — cofactor-volume de-biasing

Still the strongest structural geometry.

The new suggestion is to apply it **after semigroup smoothing**, where approximately \(q\) refreshed rows regularize the endogenous volume weight.

## Route D — finite-variance shell charging

Still highly promising.

The semigroup time tells each magnitude shell which residual scale it should be charged to.

The target is no longer a cumulative product of one-step anisotropy errors.

## Route E — generic product Poincaré/Efron–Stein

Insufficient by itself.

The abstract \(W_0/W_1\) counterexample satisfies the formal product-semigroup structure but violates the desired influence scale.

Null-projector geometry must enter.

## Route F — Stein/Lindeberg

Still risky on the raw projector.

It becomes somewhat more plausible after noise smoothing, because the target is a bounded difference of smoothed projectors rather than a derivative involving inverse singular gaps.

No Lindeberg theorem is proved here.

## Route G — transportation / log-Sobolev

Unavailable under arbitrary finite variance and bounded density alone in the needed dimension-free form.

Even if available, a generic functional inequality would not exclude the abstract low-degree spectrum counterexample.

## Route H — P11 pathwise martingale concentration

Potentially useful for P11 log removal but not needed for the theorem proved here.

The lesson transferred from P14 is to control integrated/smoothed influence at the physical scale rather than a raw supremum over an oversized parameter net.

---

# 22. Endpoint and dependence bookkeeping

## P14 residual dimension

The semigroup criterion concerns the quadratic bulk quantity \(R_D\).

It does not replace the separately proved singular near-parallel estimate for

\[
(1-\rho^2)^{-1/2}.
\]

The full fixed-apex theorem still requires both.

## \(D=1,2\)

The singular kernel has a genuine low-dimensional divergence at \(D=2\) even in the Haar benchmark.

The new semigroup theorem is about quadratic purity and does not erase that endpoint distinction.

## Projected-coordinate dependence

No projected residual coordinate is treated as independent.

The semigroup operates on the original iid **row variables**.

## Finite variance

No moment above two is introduced by the new deterministic semigroup reduction.

Any future proof of the smoothed influence estimate must preserve this if it is to solve the target P14 theorem.

## Mode of conclusion

`P24-SMOOTH-INFLUENCE-CRITERION-06` is a deterministic equivalence/reduction for the ANOVA spectrum of the actual null-projector functional.

It is not an asymptotic convergence-in-probability statement.

---

# 23. Failed-route graveyard

1. **Raw one-row influence of the null projector is \(O(1)\).**  
   False even for Gaussian rows:
   \[
   \mathcal I_m^{\rm G}(1)\sim m/2.
   \]

2. **A generic Efron–Stein inequality proves the sharp P14 theorem.**  
   False. The abstract low-degree spectrum is a counterexample.

3. **Noise smoothing can be at an arbitrary unrelated scale.**  
   False for the direct block domination argument. The smoothing refresh count must be comparable to \(q\).

4. **The natural checkpoint \(\theta_q\) controls the entire dyadic block pointwise in degree.**  
   False at very high degrees: its Dirichlet coefficient decays faster than the block coefficient.  
   It does control the central ANOVA band.

5. **The quarter-noise checkpoint \(\eta_q\) is merely a constant-choice artifact.**  
   False conceptually. It supplies enough exponential slack to dominate the high-degree block tail.

6. **Semigroup positivity alone forces the desired Dirichlet scale.**  
   False by the \(W_0/W_1\) abstract spectrum.

7. **Projected residual coordinates can be independently resampled.**  
   Invalid. Only original rows are iid.

8. **P11's solved \(p=\infty\) endpoint theorem removes the finite-\(p\) shrinking-strip log.**  
   False. The finite empirical denominator remains a separate issue.

9. **P13's sequential-reservoir theorem directly proves P14.**  
   False. It supplies a scale-accounting principle, not a null-projector energy estimate.

---

# 24. Updated P24 ledger

## PROVED — inherited

- `P24-HYPERPLANE-SMOOTHING`.
- `P24-P14-QUAD` under stronger moments.
- `P24-UI-FV`.
- `P24-ENERGY-FV`.
- `P24-STEP-LOSS-FV`.
- `P24-MIDEDGE-FV`.
- `P24/P14-EDGE-FV`.
- `P24-P14-FULL-FV-SUBPOWER`.
- `P24-XI-MULTITANGENT-FDD`.
- `P24-XI-TANGENT-L2LOC`.
- `P24-XI-LAMPERTI-CORE`.
- `P24-XI-LAMPERTI-NONERGODIC` for the unnormalized tangent.
- `P24-XI-PROFILE-TRUNC-03`.
- `P24-XI-PROFILE-NEARID-03`.
- `P24-XI-PROFILE-REL-LIP-03`.
- `P24-XI-KERNEL-UNIFORM-03`.
- `P24-XI-LINEAR-WINDOW-03`.
- `P24-XI-LOGMOD-TWOSIDED-03`.
- `P24-REVEAL-BERNSTEIN-04`.
- `P24-NOISE-LOCAL-MOD-04`.
- `P24-NOISE-SUBPOWER-LOCAL-04`.
- `P24-DYADIC-BLOCK-CRITERION-05`.
- `P24-DYADIC-NOISE-CHECKPOINT-05`.
- `P24-XI-CYL-MIX-RATE-05`.
- `P24-AUDIT-P11-LAMPERTI-MIXING-05`.

## PROVED — new this run

- **`P24-SMOOTH-INFLUENCE-CRITERION-06`**:
  P14 sharp quadratic purity is equivalent, up to constants, to the anchor
  \[
  R_m=O_\xi(m^{-1})
  \]
  plus Gaussian-scale Efron–Stein influence of the row-noise-smoothed null projector
  \[
  \mathcal I_m(\eta_q)
  =
  O_\xi(m/q^2)
  \]
  on dyadic \(q\).

- **`P24-BLOCK-FROM-DIRICHLET-06`**:
  \[
  R_q-R_{\min(2q,m)}
  \le
  8(1-\eta_q)N_m'(\eta_q).
  \]

- **`P24-DIRICHLET-BAND-06`**:
  at the natural checkpoint
  \[
  \theta_q=1-(q-1)/(m-1),
  \]
  \[
  \sum_{s\in I_q}W_s
  \le
  \frac{256}{7}
  (1-\theta_q)N_m'(\theta_q).
  \]

- **exact exchangeable-pair identity**:
  \[
  \theta N_m'(\theta)
  =
  \frac12
  \sum_i
  E\|
  T_{\sqrt\theta}\Pi(X)
  -
  T_{\sqrt\theta}\Pi(X^{(i)})
  \|_F^2.
  \]

- **`P24-AUDIT-P14-BANDPASS-06`**:
  `P14-HOEFFDING-BANDPASS-05` independently PASSes.

## CONDITIONAL / protocol-open

- P14's sharp finite-variance theorem
  \[
  R_D\le C_\xi/D
  \]
  remains OPEN.

- The full singular-kernel P14 theorem still needs the sharp bulk theorem plus the already-proved singular edge.

- The new semigroup criterion itself requires OTHER-worker audit before formal ProofNet portfolio closure.

- P11's finite-\(p\) log-removal theorem remains OPEN.

- P04/P20 hard-edge adaptive-delocalization remains OPEN.

## DISPROVED / REJECTED

- raw projector influence is uniformly small;
- generic Efron–Stein alone proves P14;
- semigroup positivity alone proves the sharp Dirichlet scale;
- every \(D\)-stratum or every noise level must be controlled separately;
- projected residual coordinates may be treated as iid;
- a raw one-step angular debt must be multiplied across every scale;
- the natural P14 checkpoint alone pointwise-dominates the entire dyadic block;
- P11's \(p=\infty\) endpoint solution automatically resolves finite-\(p\) denominator self-averaging.

## OPEN

1. **`P24/P14-SMOOTHED-ROW-INFLUENCE-07`**
   \[
   \boxed{
   \sum_{i=1}^{m-1}
   E\|
   T_{\sqrt{\eta_q}}\Pi(X)
   -
   T_{\sqrt{\eta_q}}\Pi(X^{(i)})
   \|_F^2
   \le
   C_\xi\frac{m}{q^2}
   }
   \]
   for every dyadic \(q\).

2. Anchor:
   \[
   R_m\le C_\xi/m.
   \]

3. Semigroup-smoothed cofactor-volume de-biasing.

4. A finite-variance magnitude-shell proof that charges each shell to only \(O(1)\) matching \(q\)-scales.

5. P11 no-log shrinking strip:
   \[
   p\sqrt{q_p}\to\infty.
   \]

6. P04/P20 adaptive hard-edge operator delocalization.

7. Required independent audits.

---

# 25. Exact dependency graph

The original P14 geometry is

\[
\boxed{
\text{overlapping original row sets}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{condition on the actual shared row span}
}
\]

\[
\Downarrow
\]

\[
\boxed{
\text{two independent private residual null lines given the shared span}
}
\]

with dependent projected coordinates.

At the ANOVA level,

\[
\boxed{
\Pi=\sum_S\Pi_S,
\qquad
W_s=\sum_{|S|=s}E\|\Pi_S\|_F^2.
}
\]

The row-noise semigroup gives

\[
\boxed{
N_m(\theta)
=
\|T_{\sqrt\theta}\Pi\|_2^2
=
\sum_s\theta^sW_s.
}
\]

This run differentiates only the **spectral polynomial**, not the projector:

\[
\boxed{
\theta N_m'(\theta)
=
\mathcal I_m(\theta)
=
\text{total Efron--Stein influence of }T_{\sqrt\theta}\Pi.
}
\]

At

\[
1-\eta_q
=
\frac{q}{4(m-1)},
\]

\[
\boxed{
R_q-R_{\min(2q,m)}
\le
8
\frac{1-\eta_q}{\eta_q}
\mathcal I_m(\eta_q).
}
\]

Therefore

\[
\boxed{
\mathcal I_m(\eta_q)
\lesssim
m/q^2
}
\]

at dyadic scales, together with

\[
R_m\lesssim1/m,
\]

implies

\[
R_D\lesssim1/D.
\]

Then P14's already-proved singular edge yields

\[
E[(1-\rho^2)^{-1/2}\mid D]
\le
1+C_\xi/D.
\]

This is now the sharpest exact semigroup reduction of the P14 finite-variance problem.

---

# 26. Highest-value next attack

The next theorem should no longer be phrased as a global angular-correlation statement.

It should be:

## `P24/P14-SMOOTHED-ROW-INFLUENCE-07`

For one fixed centered variance-one bounded-density real law with finite variance, prove

\[
\boxed{
E\|
T_{\sqrt{\eta_q}}\Pi(X)
-
T_{\sqrt{\eta_q}}\Pi(X^{(1)})
\|_F^2
\le
\frac{C_\xi}{q^2}
}
\tag{NEXT}
\]

uniformly for dyadic

\[
2\le q<m,
\]

where

\[
\eta_q
=
1-\frac{q}{4(m-1)}.
\]

By row exchangeability, this is exactly the total influence theorem needed by `P24-SMOOTH-INFLUENCE-CRITERION-06`.

The preferred proof architecture is:

1. sample the semigroup refresh sets for the two smoothed projectors;
2. condition on their common untouched original rows;
3. work in the resulting residual subspace;
4. use P14's exact cofactor-volume spherical 2-design on the refreshed/private block;
5. prove a \(q\)-scale lower-tail bound for the **block** cofactor sum rather than an inverse determinant moment;
6. split \(\xi^2\) into dyadic magnitude shells;
7. charge a shell only when its active-row count is comparable to \(q\);
8. use the already-proved singular-edge theorem for the exceptional near-rank-deficient block;
9. sum shell energies using only finite variance.

A successful proof of (NEXT), plus the separate anchor

\[
R_m=O_\xi(m^{-1}),
\]

would close P14's quadratic finite-variance theorem.

---

# Bottom line

The latest P14 report converted its remaining finite-variance problem into a logarithmic ANOVA-shell theorem.

This run converts that shell theorem again, now into a standard probability/concentration object.

Let

\[
F_q
=
T_{\sqrt{\eta_q}}\Pi,
\qquad
1-\eta_q=\frac{q}{4(m-1)}.
\]

Then the total row Efron–Stein influence is

\[
\boxed{
\frac12
\sum_i
E\|
F_q(X)-F_q(X^{(i)})
\|_F^2
=
\sum_s s\eta_q^sW_s.
}
\]

The exact Gaussian scale is

\[
\boxed{
m/q^2.
}
\]

And the dyadic P14 block satisfies

\[
\boxed{
R_q-R_{\min(2q,m)}
\le
8(1-\eta_q)N_m'(\eta_q).
}
\]

Therefore the sharp P14 bulk theorem is equivalent, up to constants, to the anchor

\[
R_m=O_\xi(m^{-1})
\]

plus the smoothed influence bound

\[
\boxed{
\mathcal I_m(\eta_q)
=
O_\xi(m/q^2)
}
\]

on only \(O(\log m)\) dyadic scales.

This is the new high-value probability lemma.

It preserves all original row dependence, introduces no moment above two, and moves the unresolved geometry into an exchangeable-pair/Efron–Stein quantity on a noise-smoothed projector—precisely the setting where block conditioning, cofactor-volume geometry and finite-variance shell charging have the best chance to succeed.

