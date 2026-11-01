# fleet02/B13 r23 early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains open.

Substantive calculation obtained before the longer argument:

Let `Q(x)=x^T A x+b^T x+c`, let `d=A_ii!=0`, and let `S=A_{-i,-i}-A_{-i,i}A_{i,-i}/d` be the ORIGINAL-coordinate scalar Schur complement. For disjoint `I,J` in the remaining coordinates, put `M=S[I,J]`. Suppose a probability law `mu` on nonzero physical `2x2` minors of `M` has row inclusion marginals at most `h<3/4`, `h>=1/2`, and entropy-determinant currency

`K2(mu)=exp(H(mu)+E_mu log det(M[P,T])^2)`.

The designated partner fleet03/B13 r23 proves

`||p_R||_3 <= A(h) K2(mu)^(-1/6)`,
`A(h)=[6 sqrt(e/(2h))/(3-4h)]^(2/3)`,

for the Schur remainder `R`, retaining arbitrary same-bank curvature, outside couplings and affine terms. Combining this with fleet02/B13's proved `L3 -> H_{1/2}` inequality

`sup_s E|R-s|^(-1/2) <= 4(4/3)^(3/4)||p_R||_3^(3/4)`

and the pinned Claude/Fourier one-coordinate completion theorem gives

`||p_Q||_inf <= C(h)|d|^(-1/2)K2(mu)^(-1/8)`,

where

`C(h)=4(4/3)^(3/4)[6 sqrt(e/(2h))/(3-4h)]^(1/2)`.

For each minor, the bordered determinant identity is

`det A[{i} union P,{i} union T]=d det M[P,T]`.

Hence the original-matrix anchored entropy currency

`K3_i(mu)=exp(H(mu)+E_mu log det A[{i} union P,{i} union T]^2)=d^2 K2(mu)`

and therefore

`||p_Q||_inf <= C(h)(|d|^2 K3_i(mu))^(-1/8)`.

At `h=2/3`, `C(h)=25.1616567012...`. This is a new lower-order anchored certificate: it uses physical bordered `3x3` minors rather than the previous bordered `4x4` currency.

Second exact calculation, for the concentrated branch. If a pre-Schur cross block is `N` and a scalar pivot removes a rank-one term, write

`N=S+x y^T`.

Then, with `E2(T)=sum_{|P|=|T|=2}det(T[P,T])^2`, exterior algebra gives the exact identity

`|| wedge^2 N-wedge^2 S ||_F^2 = ||x||^2 ||y||^2 ||P_{x^perp} S P_{y^perp}||_F^2`.

Indeed orthogonal row/column changes reduce to `x=||x||e_1`, `y=||y||e_1`, where only minors containing row 1 and column 1 change and their differences are `||x||||y|| S_{kl}`. Consequently

`sqrt(E2(N)) <= sqrt(E2(S)) + ||x||||y|| ||P_{x^perp}SP_{y^perp}||_F`.

Thus loss of aggregate pair-volume under scalar Schur descent is not free: if `E2(S)<=theta E2(N)`, the transverse star term is at least `(1-sqrt(theta))^2 E2(N)` after squaring.

Sources actually used: partner fleet03/B13 r23 `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T034405Z-fleet03-B13-qform-r23/REPORT.md`; pinned Claude/Fourier package `e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`; prior fleet02/B13 r22/r23 anchored-volume work. No attained global bathtub optimizer, support bound, fragment-count bound, or post-rotation independence is used.
