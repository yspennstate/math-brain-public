Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding model selector is exposed.**

# Immutable correction to the iteration step in `2026-09-19T142300Z__H0008_conductance_truncation_and_small_escape_tail.md`

The theorem

\[
P_i(0<B\le x)\le C e^{-c/x}
\]

is unchanged, but the threshold wording between equations (6.10) and (6.14) in the first artifact was too loose: because

\[
T(x)=\frac{x}{1-x}>x,
\]

one cannot choose a positive `x_0` for which `T(x)<=x_0` holds for every `x<=x_0`. The correct iteration uses two nested thresholds.

Let `y_0>0` be small enough that the Taylor estimate is valid and

\[
C_3f(y)\le\kappa_1-\kappa
\qquad(0<y\le y_0).
\]

Set

\[
x_1:=T^{-1}(y_0)=\frac{y_0}{1+y_0}.
\]

Then for every `0<x<=x_1`,

\[
f(x)\le\kappa_1 f(T(x)).
\tag{C.1}
\]

For such `x`, define

\[
k:=\left\lfloor\frac1x-\frac1{x_1}\right\rfloor+1.
\tag{C.2}
\]

Since

\[
\frac1{T^r(x)}=\frac1x-r,
\]

for every `0<=r<=k-1` we have `T^r(x)<=x_1`, so (C.1) is valid at every one of the `k` iteration steps. Moreover

\[
\frac1{T^k(x)}
=\frac1x-k
\ge \frac1{x_1}-1
=\frac1{y_0},
\]

hence

\[
T^k(x)\le y_0.
\]

Therefore

\[
\begin{aligned}
f(x)
&\le \kappa_1^k f(T^k(x))\\
&\le \big(\sup_{0<y\le y_0}f(y)\big)\kappa_1^k\\
&\le C\exp\!\left(-\frac{-\log\kappa_1}{x}\right),
\end{aligned}
\]

up to an `x`-independent multiplicative factor coming from `1/x_1`. This is the claimed `Ce^{-c/x}` bound.

All subsequent consequences in the first artifact, including finiteness of every negative conductance moment, use only the corrected bound and remain valid. No source-level closure claim is added by this correction.