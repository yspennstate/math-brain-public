SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-24T03:11:12Z.

# account02/B02 auto11 — carrier-aligned physical-hub reduction

Programme `QFORM-DENSITY-3EIG-20260922`. Role: Integrated Fourier estimate. Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**. Continuity is proved only on the Fourier-L1 branches below.

Exact owner target unchanged: independent ORIGINAL real coordinates with densities <=1; arbitrary real symmetric A; at least three eigenvalues |lambda|>=1. No moments, support, log-concavity, iid, diagonal-basis/post-rotation independence, conditional projection cap, arbitrary-joint coarea, or deletion of a nonzero tail.

## Sources actually used

Fresh owner control before publication remained revision `2026-09-22.15`, QFORM-only; live corrections reread. Required pinned base: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`. On any literal physical cross block B, the reviewed sharp-HY machinery supplies

`D': ||p_Q||inf <= C3 E3(B)^(-1/6), C3=10.345083232147514...`,

with `phi_Q in L1`, and independently

`D5: ||p_Q||inf <= C5 E5(B)^(-1/10), C5=5e/sqrt(2)=9.61057757039779...`,

also with `phi_Q in L1`. D5 improves D' whenever `E5(B)>=0.478800937867911 E3(B)^(5/3)`.

Newest completed designated partner: account03/B02 r45, canonical math `yspennstate/math-open-problems@969923934518c728e4611e670ab6244ceea30215`, report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T030004Z-account03-B02-qform-r45/REPORT.md`. Its live full partition `L union R=[n]`, `N=A[L,R]`, has squared singular values `x1>=x2>=...` with

`x1*x2 > kappa :=247/576`.                                       (1)

After its physical-E3 / fixed-V1 / diffuse-spectral-window exits, its low-transverse survivor contains an actual coordinate i with

`|A_ii|>1/512 OR ||A[i,i^c]||_2>1/512`.                           (2)

The present theorem attacks the off-diagonal alternative in (2).

## Punctured internal-curvature lift

Write coefficient SVD only: `N=sum_j sqrt(x_j)u_j v_j^T`; no random variable is rotated. For `i in L`, put

`ell_i=u1(i)^2+u2(i)^2`,
`b_i=A[L\{i},i]`,
`d_i=dist(b_i,span(u1|_(L\{i}),u2|_(L\{i})))`.

Set

`W_i=sum_(I subset L\{i}, |I|=3) sum_(J subset R, |J|=2) det([N[I,J],b_i[I]])^2`.

Exterior Cauchy--Binet, retaining only the top singular pair, gives

`boxed: W_i >= x1*x2(1-ell_i)d_i^2.`                              (3)

Indeed the punctured two-vector volume is `x1*x2 det(I_2-r_i r_i^T)=x1*x2(1-ell_i)`, `r_i=(u1(i),u2(i))`, and wedging with `b_i` contributes `d_i^2`.

Fair-Bernoulli split the physical coordinates of L. Each determinant in W_i becomes a literal disjoint physical 3x3 cross minor when its three rows land on one side and i on the other, probability 1/16. Hence some deterministic ORIGINAL-coordinate cut B_i obeys

`boxed: E3(B_i)>=W_i/16.`                                        (4)

## New theorem `QFORM-R45-PHYSICAL-HUB-CARRIER-ALIGNMENT-v1`

For `i in L` define

`q_i=||N[i,:](I-P_V2)||_2`, where `V2=span(v1,v2)`,

and take `a0=1/512`, `delta=1/1024`. Assume (1) and `||A[i,i^c]||_2>a0`. Then at least one holds:

(A) `q_i>=delta`. Since

`E3(N)>=x1*x2 sum_(j>=3)x_j >=x1*x2 q_i^2`,                       (5)

we have

`E3(N)>kappa delta^2=247/603979776=4.08954090542e-7`.

Therefore

`boxed: ||p_Q||inf<120.075637,  integral|phi_Q|<754.457479.`       (6)

(B) `ell_i<=3/4` and `d_i>=delta`. By (3)-(4), some literal physical cut satisfies

`E3(B_i)>kappa delta^2/64=6.38990766472e-9`,                      (7)

hence

`boxed: ||p_Q||inf<240.151273,  integral|phi_Q|<1508.91407.`       (8)

(C) `ell_i>3/4` (a top-two near-coloop).

(D) None of (A)-(C). Define the carrier-aligned part

`g_i^2=||P_span(u1^(-i),u2^(-i))b_i||_2^2+||N[i,:]P_V2||_2^2`.

The two residual pieces are orthogonal and lie on disjoint physical banks, so

`||A[i,i^c]||_2^2=g_i^2+d_i^2+q_i^2`.

Thus, using `d_i,q_i<delta`,

`g_i^2>a0^2-2delta^2=a0^2/2`, and therefore

`boxed: g_i>1/(512 sqrt(2))=0.001381067932... .`                  (9)

The symmetric theorem holds for `i in R`.

Finally `sum_(i in L)ell_i=2`, so there are at most two L-side near-coloops with `ell_i>3/4`; likewise at most two on R. Thus the entire r45 off-diagonal physical-hub branch is reduced to a genuine Fourier-L1 payment, a fixed carrier-aligned hub (9), or at most four exceptional near-coloops total.

The D5 refinement remains live on both actual blocks N and B_i: whenever their E5 is positive one may replace the displayed D' payment by `min{C3 E3^(-1/6),C5 E5^(-1/10)}`; no E3=>E5 implication is claimed.

## Equation-level partner application and remaining edge

Apply r45's literal alternative (2). Its physical-E3 and diffuse spectral-window branches are already paid. If `|A_ii|>1/512`, retain a fixed physical diagonal pivot. If instead the off-diagonal row exceeds `1/512`, the theorem above gives (6), (8), at most four near-coloops, or a carrier-aligned row hub `>1/(512sqrt(2))`.

Hence the live unpaid list is now:

1. r45's fixed overlap-one V1 grouped-pivot packet;
2. a physical diagonal `|A_ii|>1/512`;
3. a carrier-aligned off-diagonal hub `g_i>1/(512sqrt(2))`;
4. at most four top-two near-coloop coordinates.

Everything else in this fork is paid by genuine unweighted Fourier L1. This respects the current `QFORM-MIXED-PLUCKER-ABSOLUTE-TTSTAR-BARRIER-v1`: the proof first manufactures a literal physical cross block and only then invokes D'/D5; it never feeds abstract mixed exterior mass into the refuted absolute kernel.

First unpaid implication: `QFORM-FIXEDSCALE-DIAGONAL-OR-CARRIERALIGNED-HUB-L1-v1`. A next receiver should couple the robust rank-two crossing to the fixed physical square/carrier-aligned hub or the fixed V1 grouped pivot, rather than trying again to force transverse E3 mass.

Full QFORM: **OPEN**. Full-target continuity: **OPEN**. Target-wide universal unweighted Fourier L1: **OPEN / not refuted**. No exact-target counterexample found.
