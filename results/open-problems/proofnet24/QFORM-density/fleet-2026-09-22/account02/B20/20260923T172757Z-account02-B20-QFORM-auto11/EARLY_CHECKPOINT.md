SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-23T17:27:57Z.
attacking: strengthen the newest account03/B20 r34 aligned E2/rank-two frontier by applying its marginal-free physical E3 theorem to all three literal cuts of the surviving three-bank triangle, forcing a common 2+2+2 physical-plane carrier without deleting any coefficient tail.

# Early checkpoint — three-cut Frobenius rank-two compressor

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T172757Z-account02-B20-QFORM-auto11`.
Status: substantive calculation checkpoint; full QFORM remains open.

Newest completed designated-partner input: account03/B20 r34, `yspennstate/math-open-problems@5485a92c78229ce55057784bdc99288d2b2c1976`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T164400Z-account03-B20-QFORM-r34/REPORT.md`.

Its aligned survivor has disjoint ORIGINAL-coordinate banks `D1,D2,K`, matrices

`C=A[D1,D2]`, `N1=A[D1,K]`, `N2=A[D2,K]`,

and fixed constants

`F=||C||_F^2 > 0.05671470919622164`,
`Delta=s1(Nr)s2(Nr) > 0.0014419528160955833`, `r=1,2`.

The partner also proves the marginal-free physical E3 theorem: for every literal physical cross block `M`, with `Z3=e3(MM^T)>0`,

`||p_Q||_infinity <= K3 Z3^(-1/6)`, `K3=3*2^(4/3)*exp(1/3)<10.551`,

with arbitrary same-bank blocks, outside couplings and affine terms retained.

Define the three literal physical cuts

`M1=[C,N1] : D1 -> D2 union K`,
`M2=[C^T,N2] : D2 -> D1 union K`,
`M3=[N1^T,N2^T] : K -> D1 union D2`.

For each `r=1,2,3`, positive-semidefinite monotonicity of the row Gram matrix gives

`s1(Mr)s2(Mr) >= Delta`.

If `T_r^2=sum_{j>=3}s_j(Mr)^2`, then the `1,2,k` terms in `e3` give the exact deterministic inequality

`e3(Mr Mr^T) >= s1(Mr)^2 s2(Mr)^2 T_r^2 >= Delta^2 T_r^2`.

Therefore, for every fixed `tau>0`, if any `T_r>=tau`, the full law is paid by

`||p_Q||_infinity <= K3 (Delta*tau)^(-1/3)`.

So every state still unpaid after this universal exit satisfies simultaneously

`dist_F(Mr, rank<=2)=T_r<tau`, `r=1,2,3`.

Take concretely `tau=sqrt(F)/256=0.0009302675875070436`. Then the paid exit is

`||p_Q||_infinity <956.621`.

In the surviving branch let `P1,P2,P3` be the top-two left singular projectors of `M1,M2,M3` on `D1,D2,K`. Orthogonality of the concatenated column banks yields

`||(I-P1)C||_F^2+||(I-P1)N1||_F^2<tau^2`,
`||C(I-P2)||_F^2+||(I-P2)N2||_F^2<tau^2`,
`||N1(I-P3)||_F^2+||N2(I-P3)||_F^2<tau^2`.

Hence

`||C-P1 C P2||_F<2tau`,
`||N1-P1 N1 P3||_F<2tau`,
`||N2-P2 N2 P3||_F<2tau`.

Moreover

`||P1 C P2||_F > sqrt(F)-2tau = (127/128)sqrt(F) >0.2362879672`.

Thus the fresh r34 first gap can be sharpened source-preservingly to a genuine common `2+2+2` physical-plane triangle with all three cross tails retained but jointly Frobenius-small. This does not treat those coefficient tails as small random perturbations and does not assert independence of the projected planes.

Next step in this run: test whether the common-plane triangle plus N3 spectral/no-pivot hypotheses force one of the newest overlap-square/two-hub L4 receivers, or isolate the exact remaining curvature obstruction.
