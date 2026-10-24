SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-23T20:42:51Z.
attacking: QFORM-ZEROPIVOT-NEARRANK1-NONZERO-TAIL-L1-v1 — retain the genuinely nonzero transverse tail on the heavy zero-pivot overlap-one slice and either obtain a Fourier-L1 bridge uniform through rank one or route it to a paid physical E3/D5 mechanism without deleting the tail.

# Early checkpoint — physical compound escape from the zero-pivot near-rank-one slice

Programme: `QFORM-DENSITY-3EIG-20260922`. Full unrestricted QFORM remains OPEN. Target-wide universal unweighted Fourier-L1 remains OPEN / not refuted.

## Source pins used before this checkpoint

- Required base Fourier package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.
- Reviewed q-dependent sharp-HY refinement: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
- Immediate account02/B02 predecessor: `yspennstate/math-open-problems@aeaba9e3351623ead11450857c2d014b43664aef`, exact rank-one shared-hub tensor theorem.
- Designated partner account03/B02 newest handoff/report consumed: `yspennstate/math-open-problems@c5cc2edeeee6426fcbbf73eb00fbd68a176d28cb`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T201213Z-account03-B02-qform-r38/REPORT.md`.
- Fresh small-leakage correction source: `yspennstate/math-open-problems@2ac0c66b922e3742161e9e914ae2190afa1f978e`, `proofnet24/QFORM-density/interactive/20260923T203400Z-negative-target-projection-fake/REPORT.md`.

No scalar pointwise Fresnel decay, no deletion of a nonzero tail, no arbitrary conditional density cap, and no post-rotation independence are used below.

## 1. Exact append-one-row/column compound identities

Fix a physical shared hub `i` with `A_ii=0`, and an ORIGINAL residual cut `K=L disjoint_union R`. Write

`c=A[L,i]`, `r=A[i,R]`, `N=A[L,R]`,

`u=||c||^2`, `w=||r||^2`,

`P_c=I-cc^T/u`, `P_r=I-rr^T/w`,

`C=P_c N P_r`, `F=||C||_F^2`, `T=u w F`,

when `u,w,F>0`. Put `b=min(u,w)/F` and `M=max(u,w)`.

There are two literal physical cross blocks

`M_R=A[{i} union L,R]=[r^T;N]`,

`M_L=A[L,{i} union R]=[c,N]`.

For every integer `k>=1`, Cauchy-Binet / exterior algebra gives the exact identities

`E_k(M_R)=E_k(N)+w E_(k-1)(N P_r)`,

`E_k(M_L)=E_k(N)+u E_(k-1)(P_c N)`.                 (1.1)

Indeed every k-minor either avoids the appended row/column or contains it; wedging with `r` (respectively `c`) kills the component parallel to that vector. Since an orthogonal projection is a contraction on every exterior power,

`max{E_3(M_R),E_3(M_L)} >= M E_2(C)`,              (1.2)

`max{E_5(M_R),E_5(M_L)} >= M E_4(C)`.              (1.3)

These are physical ORIGINAL-coordinate blocks; the projections occur only inside a deterministic lower bound for their exterior volumes.

## 2. Sharp near-rank-one E2 lower bound

Let the squared singular values of `C` be `x_1>=x_2>=...`, and let

`rho=F/x_1`.

On the actual near-rank-one range `1<rho<=2`, the tail has total mass

`F-x_1=F(rho-1)/rho <=x_1`.

Therefore

`E_2(C)=x_1(F-x_1)+E_2(x_2,x_3,...)`

`       >=F^2 (rho-1)/rho^2`.                       (2.1)

The constant is sharp from stable rank alone: equality occurs for a rank-two `C` with squared singular values `1` and `rho-1` after scaling.

Because `min(u,w)=bF` and `T=u w F=b M F^2`, (1.2)-(2.1) give the live physical third-volume certificate

`boxed: max{E_3(M_R),E_3(M_L)}
        >=[(rho-1)/(rho^2 b)] T,   1<rho<=2.`         (2.2)

## 3. Reviewed sharp-HY D' applied to the live physical block

The completed marginal-free physical-E3 theorem (reviewed sharp-HY D' plus the heavy-row promotion) gives

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,

`C_3=10.345083232147514...`, with `phi_Q in L1`.

Applying it to whichever of `M_R,M_L` realizes (2.2) gives the new near-rank-one escape

`boxed: ||p_Q||_infinity
 <=C_3 [b rho^2/((rho-1)T)]^(1/6),   1<rho<=2,`       (3.1)

and the corresponding unweighted Fourier-L1 bound is at most `2 pi` times the right side.

For the partner overlap-one cut, `T>=Delta_i/16`, hence

`boxed: ||p_Q||_infinity
 <=C_3 [16 b rho^2/(rho-1)]^(1/6) Delta_i^(-1/6).`    (3.2)

The previous one-hub projected-E2 theorem gives

`C_h [32 rho b/(rho-1)]^(1/6) Delta_i^(-1/6)`,

with `C_h=3*2^(7/6)e^(1/3)`. Since `C_3=C_h(16/9)^(1/6)`, (3.2) is strictly smaller on the genuinely near-rank-one interval

`1<rho<9/8`,

and the two coefficients agree exactly at `rho=9/8`. Thus D' is not merely retained: it is the best currently certified Fourier-L1 exit in the closest positive-tail collar.

## 4. D5 applied to the same physical blocks

The reviewed sharp-HY fifth-volume exit is

`||p_Q||_infinity <=(5e/sqrt(2)) E_5(M)^(-1/10)`.

Equation (1.3) therefore gives the actual complementary inequality

`boxed: ||p_Q||_infinity
 <=(5e/sqrt(2)) [M E_4(C)]^(-1/10)`                 (4.1)

whenever `E_4(C)>0`. Comparing (4.1) with the E3 branch using the same block, D5 is smaller whenever

`M E_4(C) >0.4788009378679107 [M E_2(C)]^(5/3)`.     (4.2)

Thus higher transverse exterior volume is paid without selecting a singleton minor.

## 5. A sharp obstruction: the known positive-tail currencies must degenerate

Take orthogonal star directions and a transverse rank-two model with squared singular values `(1,delta)`, `delta>0`, and choose

`u=w=F=1+delta`.

Then `rho=1+delta`, `b=1`, `T=(1+delta)^3`. The natural physical blocks have three squared singular values `(1+delta,1,delta)`, so

`E_3(M_R)=E_3(M_L)=delta(1+delta)`,                 (5.1)

and (2.2) is an equality. They have rank three, hence

`E_5(M_R)=E_5(M_L)=0`.                               (5.2)

Therefore the best currently available D'/E3 certificate blows up exactly like `delta^(-1/6)` as `delta downarrow0`, while D5 is literally unavailable. At `delta=0`, however, the preceding exact-rank-one shared-hub tensor theorem gives a finite bound proportional to `T^(-1/6)` (and genuine Fourier L1). This proves a real discontinuity of the present certificate family, not of QFORM itself.

The fresh dependent-light construction at `2ac0c66...` independently rules out the tempting repair “collapse the two light banks to one arbitrary 3D law and use only its 1D/2D/3D projection caps”: even for `Q_epsilon=2HL+V^2+2 epsilon LP`, all those caps can hold uniformly while the output density is essentially unbounded. That source is explicitly NOT an original-product counterexample. Its correct implication here is that the next bridge must retain the two-bank/original-product factorization (or exploit tied same-bank curvature), not merely low-dimensional projection heights.

## 6. Newest designated-partner implication consumed

Account03/B02 r38 proves the exact local cubic

`det(P_L^2+tG_L)=d_L+v_L t+u_L t^2+z_L t^3`

and hence `v_L^2>=3d_Lu_L`, `u_L^2>=3v_Lz_L`. In particular, on the target-scale branch `V_1>1/4`, `V_2<=1/4`, it gives the actual aggregate obstruction

`sum_{L: d_L<1/4} u_L >1/6`.                                    (6.1)

This is now the complementary global route: if the zero-pivot near-rank-one slice cannot be paid uniformly, the overlap-one mass is not allowed to be replaced by one guessed minor; (6.1) keeps an absolute amount of compound mass on a low-principal-determinant collar for a grouped product-preserving receiver.

## 7. Next mechanism

The first unpaid implication is sharpened to `QFORM-ZEROPIVOT-NEARRANK1-PRODUCT-BRIDGE-v1`: close the `rho downarrow1` gap while retaining the two original light banks (or the exact product characteristic-function factorization) and the actual same-bank quadratic phases. A lemma stated only in terms of the aggregate 3D light density and its projection caps is now known false. The direct D'/E3, D5, projected-E2, and punctured projection-cap mechanisms all have explicit positive-tail degeneracies; the next attempt must change mechanism rather than repeat them.
