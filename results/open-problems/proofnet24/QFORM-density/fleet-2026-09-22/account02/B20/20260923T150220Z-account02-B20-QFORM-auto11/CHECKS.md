# Checks — account02/B20 20260923T150220Z

These checks audit the new deterministic compiler only. Full QFORM remains open.

## A. Exact recurrence arithmetic

The reproduced cross-energy inequality is

`F(E)=961/4096 + (1/2)[(63/64)E-3/4096]`

`     =1919/8192 +(63/128)E`.

Its fixed point is

`(1919/8192)/(1-63/128)=1919/4160=0.4612980769230769...`.

For the designated-partner input

`E_*=1241405/2097152`,

`F(E_*)=141090307/268435456=0.5256023518741131...`.

Both are strict lower bounds in the report because the source inequalities are strict.

## B. Rank-two distance step

For a physical cut `S sqcup T`, write `M=M1+R`, where `rank(M1)=1` and `||R||op=s2(M)<1/64`. The symmetric matrix with only the `M1` off-diagonal blocks has rank at most two. Hence

`1<=s3(A)<=||A-H||op`

and

`||A-H||op <= max(||A_SS||op,||A_TT||op)+||R||op`.

Therefore the maximum same-bank norm is strictly greater than `63/64`. This uses the operator-norm Eckart--Young identity for the third singular value of a symmetric matrix; it does not replace the random form by `H`.

## C. Colouring factor

For a symmetric zero-diagonal physical block `H_C`,

`||H_C||F^2=2 sum_{i<j} H_ij^2`.

Under independent fair two-colouring, each unordered edge crosses with probability `1/2`, while `||A[P,Q]||F^2` counts each separated unordered edge once. Hence

`E ||A[P,Q]||F^2=(1/2)sum_{i<j}H_ij^2=(1/4)||H_C||F^2`.

From `||H_C||op>31/32`, this gives `>961/4096` exactly.

## D. Fixed-floor D5 payment

At `E0=1919/4160`, the current fifth-volume gate gives

`e5 >= E0^5/(64^4*120)
    =1.0375453266188383e-11...`.

The pinned physical D5 theorem gives

`5 sqrt(2e) e5^(-1/10)=146.22833508385528...<146.229`.

## E. Fixed-floor grouped-rank-three payment

If strong-top-four holds and `s3>=1/64`, then

`Delta3 > sqrt((63/256)E0)/4096
        =8.225857204253191e-5...`.

The completed receiver `3e Delta3^(-1/3)` gives

`187.50895547386716...<187.509`.

## F. Fixed-floor E2 currency

With `s2>=1/64` and `s3<1/64`,

`z0=(1/4096)[(63/64)E0-1/2048-1/4096]
   =60351/545259520
   =0.00011068307436429537...`.

At determinant-law disjointness threshold `1/256`, the half-Riesz formula is

`8 sqrt(e) z0^(-1/8)=41.1838625924215...<41.184`.

The low-disjointness cofactor floor is

`gamma0=sqrt((127/512)z0)=0.005239712846278513...`.

Thus the triangle split yields

`gamma0/2=0.0026198564231392565...`,

`16 gamma0=0.08383540554045621...`.

## G. State-dependent r38 splice

On the low-disjointness large-core branch, put `L=||bD-cr^T||F`, assume `|b|<1/32`, `||c||||r||<=L/2`. Then

`L <= |b|||D||+||c||||r||`

implies `||D||>16L`, and `b` is nonzero (otherwise `L=||c||||r||`).

Use r38 with parameter `theta=L^2`.

If its cofactor E2 gate fails,

`dist_F(C,rank1)^2 <2 L^2 b^2 <L^2/512`,

so `s1(C)^2/||C||F^2>511/512`.

Also

`dist_F(D,rank2)^2<2L^2<(1/128)||D||F^2`,

so `(s1(D)^2+s2(D)^2)/||D||F^2>127/128`.

If the gate holds and a 3-volume orientation has maximum marginal at most `2/3`, r38/D-prime gives

`9 sqrt(3e)L^(-2/3)
 <9 sqrt(3e)gamma0^(-2/3)
 =851.945970565949...<851.946`.

No statement is made that the `>2/3`-anchor alternative is itself paid.

## H. Curvature-flip arm constant

At the invariant floor,

`(1/2)[(63/64)(1919/4160)-3/4096]
 =60351/266240
 =0.22667893629807692...`.

Therefore the arm operator norm is `>sqrt(60351/266240)=0.4761081140855267...`.

A same-side continuation strictly reduces active-bank cardinality because the produced cross `A[P,Q]` has positive Frobenius norm, so `Q` is nonempty. It cannot continue at a singleton because all N3 physical diagonals have modulus `<1/64`. Therefore a first curvature flip exists after finitely many deterministic descents. No analytic constant is multiplied along that descent.

## I. Correction regression

- Random variables are never spectrally rotated.
- No projected conditional density is replaced by a worst-fiber supremum.
- No law-uniform pointwise quadratic oscillatory decay is used.
- The residual rank-one/rank-two approximation is coefficient geometry only; the actual small tail remains in `Q`.
- Half-Riesz bounds are recorded only as fractional credit, never as an `L^infinity` density conclusion.
- All cuts/anchors/colourings refer to original physical coordinate sets.
