# P0282 idea before validation — sharp local criterion for an insertion-flux step to preserve log-concavity

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Source / claim: `P0282` — Chen fixed-size LIS log-concavity  
Frozen metric on entry: `N_exact = 86`  
Complete fixed-defect theorem frontier on entry: `j <= 66`

All thirty Section-B labels have already been genuinely used on P0282, so this run necessarily uses recycled labels. The present mathematical attacks are **#3 PROVE SOMETHING STRONGER**, **#20 FIND WHY THE ALGORITHM FAILS**, and **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE**. They are not represented as previously unused.

## 1. Setup from the predecessor's exact insertion flux

For the normalized fixed-size LIS law

`p_k = ell_{n,k}/n!`,

the predecessor proved the exact row transition

`q_k = alpha_k p_k + (1-alpha_{k-1}) p_{k-1}`,

where `q_k = ell_{n+1,k}/(n+1)!` and

`alpha_k = H_{n,k}/((n+1) ell_{n,k})`.

Write `a_k=alpha_k` and `c_k=1-a_k`. The first temptation is: prove `a_k` nondecreasing and hope the bidiagonal stochastic kernel preserves log-concavity. This note tests that hope exactly rather than assuming it.

## 2. Sharp interior local criterion for universal log-concavity preservation

Fix an interior index `k` and numbers `0<=a_i<=1`. Let a positive input sequence be log-concave on the four needed sites:

`p_{k-1}^2 >= p_{k-2} p_k`,  
`p_k^2 >= p_{k-1} p_{k+1}`.

Set

`q_i = a_i p_i + c_{i-1} p_{i-1}`.

Let `x=p_{k-1}>0`, `y=p_k>0`, and `r=y/x`. Log-concavity gives the exact outer bounds

`p_{k-2} <= x/r`,  
`p_{k+1} <= y r`.

Because `q_{k-1}` is increasing in `p_{k-2}` and `q_{k+1}` is increasing in `p_{k+1}`, the quantity

`q_k^2-q_{k-1}q_{k+1}`

is minimized, for fixed `x,y`, when both inequalities above are equalities, i.e. when the local four-term input is geometric. At that extremal input,

`q_k = x(a_k r+c_{k-1})`,

`q_{k-1} = x(a_{k-1}+c_{k-2}/r)`,

`q_{k+1} = x r(a_{k+1}r+c_k)`.

Hence the extremal margin is

`x^2 P_k(r)`,

where

`P_k(r) = (a_k r+c_{k-1})^2 - (a_{k-1}r+c_{k-2})(a_{k+1}r+c_k)`.

Therefore, for an interior coordinate, the bidiagonal step preserves the target log-concavity inequality for **every** positive locally log-concave input if and only if

`P_k(r) >= 0 for every r>0`.

Necessity is obtained by taking the input itself to be the local geometric progression with ratio `r`; sufficiency is the outer-variable monotonicity argument above.

Expanding,

`P_k(r)=A_k r^2+B_k r+C_k`,

with

`A_k = a_k^2-a_{k-1}a_{k+1}`,

`B_k = 2a_k(1-a_{k-1}) - a_{k-1}(1-a_k) - a_{k+1}(1-a_{k-2})`,

`C_k = (1-a_{k-1})^2-(1-a_{k-2})(1-a_k)`.

Thus the universal-preserver problem has been reduced to one exact quadratic on the positive half-line. This is method **#3 PROVE SOMETHING STRONGER (RECYCLED)**: characterize the whole local cone of log-concave inputs instead of only the Plancherel row.

## 3. Why alpha-monotonicity alone cannot be the induction theorem

Method **#20 FIND WHY THE ALGORITHM FAILS (RECYCLED)**: even a nondecreasing retention profile need not preserve log-concavity.

Take the rational monotone profile

`(a_0,a_1,a_2,a_3)=(0,1/2,2/3,3/4)`.

At the middle index its preservation polynomial is

`P(r) = (5/72) r^2 - (1/4) r - 1/12`,

which is negative for every sufficiently small positive `r`. Thus monotonicity `a_0<=a_1<=a_2<=a_3` is not sufficient even for local preservation of log-concavity.

So a proof of monotonicity of the actual LIS `alpha_{n,k}`, by itself, would not close Chen. One needs extra structure tying `alpha` to the actual incoming Plancherel curvature, or stronger shape conditions on `alpha`.

## 4. What to validate next

Method **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE (RECYCLED)** will now test, with exact RSK/hook arithmetic:

1. the sharp quadratic criterion for the actual insertion profiles `alpha_{n,k}`;
2. whether the actual profiles satisfy the stronger universal-preserver property through small `n`;
3. the first exact failure if they do not;
4. whether the source row-to-row Chen inequality nevertheless remains positive there, which would isolate the amount of incoming curvature that rescues the step.

If the universal-preserver property fails early, the next structural object should be a curvature-transfer identity, not another attempt to prove a false kernel theorem.
