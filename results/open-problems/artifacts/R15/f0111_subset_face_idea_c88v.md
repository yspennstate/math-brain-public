# R15 F0111 idea — lift the pair-face obstruction to every coordinate face

Date: 2026-09-19 UTC.

Status: analytic idea recorded before any checker. SELF_CHECK_ONLY / NOT CLAIMED. This is retained-screen work only; it does not reopen Burdzy--Scheutzow I0076 or promote Talagrand F0111 to READY.

## New route

The preceding R15 run obtained a necessary global certificate inequality by restricting the `k=2` hazard to a two-coordinate equal ray. Instead of differentiating the Hessian-null curve again, localize the same global argument to an arbitrary coordinate subset `J`, `|J|=m>=2`.

For

`F_n(t)=sum_i t_i-log(sum_i exp(t_i)-(n-1))`,

put `t=s 1_J`. Then all inactive coordinates cancel exactly and

`f_m(s):=F_n(s 1_J)=m s-log(m exp(s)-(m-1))`.

The candidate lower envelope is

`f_m(s) >= N_m s^2/(1+c_m s)`,

where

`N_m=binom(m,2)`, `c_m=(2m-1)/3`.

This is designed to be tangent through cubic order at the origin and recovers the previous pair bound when `m=2`.

## Proof plan

Differentiate. One has

`f_m'(s)=m(m-1)(1-exp(-s))/(m-(m-1)exp(-s))`.

For `q_m(s)=N_m s^2/(1+c_m s)`, after cancellation the inequality `f_m'>=q_m'` is equivalent to

`2(1+c_m s)^2(1-exp(-s)) >= s(2+c_m s)(m-(m-1)exp(-s))`.

Write the difference as `A_m(s)+B_m(s)exp(-s)`. With `c_m=(2m-1)/3`,

`A_m(s)=2 + 2(m-2)s/3 + (m-2)(2m-1)s^2/9`,

whose coefficients are nonnegative. After multiplying by `exp(s)`, the polynomial `B_m` cancels exactly the coefficients of degrees 0,1,2 in `A_m(s)exp(s)`. Every coefficient from degree 3 onward is then positive:

`2/k! + [2(m-2)/3]/(k-1)! + [(m-2)(2m-1)/9]/(k-2)! > 0` for `k>=3`.

Hence the derivative gap is nonnegative on `s>=0`; both functions vanish at zero, giving the envelope.

The constant should also be sharp within rational envelopes of the form `N_m s^2/(1+d s)`, because

`f_m(s)=N_m s^2-N_m c_m s^3+O(s^4)`;

a lower envelope near zero therefore requires `d>=c_m`.

## Certificate consequence

For a nonnegative quadratic global majorant

`P(t)=sum_i A_i t_i+sum_{i<j}B_ij t_i t_j >= F_n(t)`,

write

`A_J=sum_{i in J}A_i`, `B_J=sum_{i<j in J}B_ij`.

Restriction to `s 1_J` gives

`A_J+B_J s >= N_m s/(1+c_m s)`.

Optimizing over `s>=0` should yield the necessary face inequality

`A_J >= [3/(2m-1)] (sqrt(N_m)-sqrt(B_J))_+^2`.

For block-symmetric coefficients `A_i=alpha`, `B_ij=beta` on `J`, this becomes

`alpha >= [3(m-1)/(2(2m-1))](1-sqrt(beta))^2`,

which strengthens the pair coefficient `1/2` toward `3/4` as `m` grows.

A further exact-contact corollary should follow from summing the gradient equations and using `q_*:=min_{i in J}q_i`:

`A_J <= m-x_J-2q_*B_J`, where `x_J=sum_{i in J}r_i`.

Optimizing compatibility with the face inequality gives the base-only necessary condition

`m-x_J >= 3m(m-1)q_*/[3+2(2m-1)q_*]`.

## Why this route is useful

The preceding exact `n=4` null candidate passed all local derivative tests but failed a two-coordinate global face test. The proposed theorem gives a hierarchy of genuinely global obstructions on every coordinate face, so the next question is whether a Hessian-null candidate can satisfy all of them simultaneously. No numerical path sample is relevant to this analytic statement.