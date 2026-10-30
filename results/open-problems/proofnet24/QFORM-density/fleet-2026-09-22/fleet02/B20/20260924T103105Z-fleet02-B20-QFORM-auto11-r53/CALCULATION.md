# Early calculation — large-diagonal balance from the all-sign pair-free gate

Programme `QFORM-DENSITY-3EIG-20260922`; fleet02/B20 r53.

Let the newest compatible fleet03/B20 pair thresholds be

`D0=9.530157744638501e-7 < 2^-20`,
`kappa0=6.075614261408114e-5 < 2^-14`.

Assume the full-law definite-pair and indefinite-pair exits have both failed. Put `a=2^-6` and
`H={i: |A_ii|>=a}`.

For an opposite-sign pair `A_ii=x>0`, `A_jj=-y<0`, `x,y>=a`, its determinant magnitude is at least `xy>=2^-12>D0`. Its smaller singular value equals

`(sqrt((x+y)^2+4A_ij^2)-|x-y|)/2 >= min(x,y)>=2^-6>kappa0`.

Hence such a pair would be terminal. Therefore all diagonals on `H` have one sign.

For a same-sign pair write, after the common sign is removed,

`B=diag(sqrt(x),sqrt(y)) [[1,r],[r,1]] diag(sqrt(x),sqrt(y))`,
`r=A_ij/sqrt(xy)`.

If `|r|<1`, definite-pair failure gives `xy(1-r^2)<D0`, hence `1-|r|<D0/(xy)<2^-8`. If `|r|>1` and `xy(r^2-1)<D0`, the same estimate gives `|r|-1<2^-8`. If instead `xy(r^2-1)>=D0`, indefinite-pair failure gives `s_min(B)<kappa0`, while

`s_min(B)>=min(x,y)(|r|-1)`,

so `|r|-1<kappa0/a<2^-8`. Thus every pair in `H` obeys

`1-2^-8 < |A_ij|/sqrt(|A_ii A_jj|) < 1+2^-8`.  (E1)

For a triple in `H`, normalize its common diagonal sign so the diagonal is one. If the product of its three normalized off-diagonal signs is negative, then with `eps=2^-8`

`|det C| >= gamma := 2(1-eps)^3+3(1-eps)^2-1 = 33162367/8388608`,

while `||C||op <= 3+2eps =385/128`. Therefore

`s_min(C)>=gamma/(3+2eps)^2 =676783/1548800`,

and the actual physical `3x3` principal block has

`s_min >= c0 := 2^-6 * 676783/1548800 =676783/99123200 >0.00682769`.

The localized three-dimensional bound in pinned `COUNTEREXAMPLE_SEARCH.md` then gives the full ambient law

`||p_Q||_infinity <= 6 sqrt(pi)/c0 <1558`.

Consequently every unpaid state has no frustrated triangle on `H`. Choosing one vertex as root yields signs `sigma_i` for which every normalized heavy-heavy edge becomes positive. Thus, after an original-coordinate sign switch only,

`| A_ij - s sigma_i sigma_j sqrt(|A_ii A_jj|) | < 2^-8 sqrt(|A_ii A_jj|)`

for every distinct `i,j in H`, with the common diagonal sign `s`. This is an entrywise multiplicative rank-one tube; no operator-small random perturbation is asserted.
