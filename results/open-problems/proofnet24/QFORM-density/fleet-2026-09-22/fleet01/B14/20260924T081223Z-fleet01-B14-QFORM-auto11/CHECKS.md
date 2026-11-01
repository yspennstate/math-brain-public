# Checks for fleet01/B14 20260924T081223Z

## Algebraic target block

For

`B_*=2I_3-11^T`,

`11^T` has eigenvalue `3` on `span{(1,1,1)}` and eigenvalue `0` on its orthogonal complement. Hence

`spec(B_*)={-1,2,2}`

and `min |eig(B_*)|=1` exactly. Numerically `6sqrt(pi)=10.634723105433096`.

## Mutual-information inequality

For a saturated marginal `f=1_E`, `|E|=1`, a positive label decomposition has joint density

`p_{X,J}(x,j)=m_j g_j(x)` on `E`,

with posterior/prior likelihood ratio `g_j(x)`. Thus

`I(X;J)=sum_j m_j int_E g_j log g_j`

and `g_j<=M_j` implies

`I(X;J)<=sum_j m_j log M_j`.

No Jensen step, moment hypothesis, support bound, or finite-label assumption is used. For a deterministic equal-`N` partition, `g_j=N 1_{E_j}`, hence equality gives `I=log N=log M`.

## TV inequality

For `g` supported on a unit-measure set `E`, `int_E g=1`, `0<=g<=M`,

`d_TV(g dx,1_E dx)=1-int_E min(g,1) dx`.

Since `min(g,1)>=g/M`,

`d_TV<=1-1/M`.

Equality holds for `g=M 1_S` with `S subset E`, `|S|=1/M`.

## No-moment stress family

With `m_j=6/(pi^2 j^2)`, `a_j=j^3`, and `h_j=1_[0,1]`,

`f=sum_j m_j h_j(. - a_j)`

is a probability density with `||f||_infinity<=m_1<1`, because the translated unit intervals are disjoint. But

`E|X| >= sum_j m_j a_j = (6/pi^2) sum_j j = infinity`.

Each conditional component has normalized density cap exactly one, so the partner cap-weighted localization theorem applies with `M=I` despite the unbounded support and divergent first moment.
