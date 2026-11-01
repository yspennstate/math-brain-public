Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — requested GPT-6 maximum is prompt-only here, and I do not claim otherwise.**

# PROB10-06 idea before code: exploit exact two-support cancellation in Aïdékon's speed derivative

## Frozen source convention

Use the parent-bias convention of He–Wang–Xiang: at a non-root vertex with `nu` children, parent weight is `lambda` and each child has weight `1`; increasing `lambda` increases drift toward the root. The reciprocal child-bias convention is `beta=1/lambda`, where increasing `beta` increases drift away from the root. The original no-leaf conjecture is that the speed `ell_lambda` is nonincreasing for `0<=lambda<m=E nu`, equivalently `v(beta)` is nondecreasing for `beta>1/m`.

Fix first the genuinely nondegenerate bounded no-leaf family

`P(nu=2)=1-p, P(nu=3)=p`, with `0<p<1`, so `m=2+p`, `m1=2`, `m2=3`.

The published all-offspring baseline for `m1=2` is strict decrease on

`0 <= lambda <= 2/(1+sqrt(1/2)) = 1.171572875...`.

## New route

Let `B` be the escape probability from a vertex to infinity before its parent, and let `U=-dB/dlambda`. For `1<=lambda<2`, published Lemmas 2.3–2.4 give

`1-lambda/2 <= B <= 1-lambda/3`,

`0 < U <= B/(2-lambda)`.

For `k=2,3`, let `B_0,...,B_k` be iid copies of `B`, put

`S_k=sum_i B_i`, `D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.

Since `B_i+(1-lambda)B_i' = B_i+(lambda-1)U_i`, these are exactly the quantities appearing in the derivative criterion (2.8).

Set

`A=(1-p)*2*c_2+p*3*c_3`, `C=(1-p)*c_2+p*c_3`,

`H1=(1-p)*h_2+p*h_3`, `Hnu=(1-p)*2*h_2+p*3*h_3`.

Then the entire environment-measure correction in (2.8) collapses algebraically:

`A*H1-C*Hnu = p(1-p)*(c_3*h_2-c_2*h_3)`.

This is the key new mechanism: for a two-point offspring law the difficult measure-change term is a single cross-difference, rather than four unrelated expectations.

For the `k=2` branch,

`D_2 >= lambda-1+3(1-lambda/2)=2-lambda/2`,

and `B_i+(lambda-1)U_i <= B_i/(2-lambda)`, hence

`h_2 <= c_2/Q`, `Q=(2-lambda)*(2-lambda/2)`.

For the `k=3` branch,

`D_3 <= lambda-1+4(1-lambda/3)=3-lambda/3`,

and `B_i+(lambda-1)U_i >= B_i`, hence

`h_3 >= c_3/V`, `V=3-lambda/3`.

Therefore, writing `x=(1-p)c_2`, `y=p c_3`, `C=x+y`, and using `xy<=C^2/4`,

`A*H1-C*Hnu <= (C^2/4)*(1/Q-1/V)`.

Also `2C<=A<=3C`. From the symmetrized speed formula,

`ell=(A-lambda*C)/(A+lambda*C)`,

and because `c_k'=-h_k`,

`-ell' = 2*lambda*[(A*C/lambda)-(A*H1-C*Hnu)]/(A+lambda*C)^2`.

Thus for every `0<p<1` and `1<=lambda<2`,

`-ell' >= [4-(lambda/2)*(1/Q-1/V)]/(3+lambda)^2`.

In particular strict monotonicity holds whenever

`F(lambda):=2/lambda-(1/4)*(1/Q-1/V)>0`.

For `d=2`, the first zero of `F` in `(1,2)` is the first root of

`P(lambda)=-5 lambda^3+104 lambda^2-490 lambda+576`,

numerically `theta_2 = 1.8110191398...`.

A robust closed certified region is `1<=lambda<=9/5`. On that interval,

`Q>=11/50`, `1/V>=3/8`, `lambda/2<=9/10`, `(3+lambda)^2<=576/25`,

so

`-ell' >= 1085/101376 > 0`.

This gives a quantitatively certified bridge beyond the published all-offspring `m1=2` endpoint. It is only a finitely-supported subclass result and does not settle the full source conjecture.

## Extension template

The same cancellation works for any adjacent two-point support `nu in {d,d+1}`, `d>=2`. With

`delta_d=d-lambda/d`,

`Q_d=(d-lambda)*delta_d/(d-1)`,

`V_d=d+1-lambda/(d+1)`,

one obtains for `1<=lambda<d`

`-ell' >= [2d-(lambda/2)*(1/Q_d-1/V_d)]/(d+1+lambda)^2`

whenever the numerator is positive. This is an explicit sufficient monotonicity region for every nondegenerate adjacent two-point offspring law. Novelty is NOT claimed pending a broader prior-art check.

## Truncation route to certify the recursion itself

For `p<=1/4` and `1<=lambda<=9/5`, the finite-depth escape recursion has an explicit expected contraction. For a node of degree `k`, the sum of child Lipschitz constants is bounded by

`L_2 <= 9/10`, `L_3 <= 60/49`.

Averaging gives

`rho <= (3/4)*(9/10)+(1/4)*(60/49)=1923/1960 < 1`.

Hence if `B_n` is the level-n escape approximation,

`E|B_n-B| <= rho^n`.

Using the differentiated recursion, the published bound `U_n,U<=1/(2-lambda)<=5`, and the uniform denominator lower bound, a direct Lipschitz estimate gives the conservative derivative truncation bound

`E|U_n-U| <= 5*rho^n + 21*n*rho^(n-1)`.

This provides an explicit finite-depth error certificate on a nontrivial rectangle instead of assuming a numerical derivative sign.

## Third route tried and obstruction

The Ben Arous–Fribergh–Sidoravicius common super-regeneration coupling is built after fixing child-bias `beta>1`; their one-dimensional regeneration event has positive drift proportional to `beta-1`. The new parent-bias interval `lambda>1` corresponds to `beta=1/lambda<1`, so that exact common-super-regeneration construction does not cross the remaining interval without a genuinely different regeneration reference process. This route is therefore not silently reused as if it covered the new range.
