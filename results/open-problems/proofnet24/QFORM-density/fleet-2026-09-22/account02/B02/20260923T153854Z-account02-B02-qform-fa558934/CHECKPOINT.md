SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T15:38:54Z.
attacking: finish the degree-4 physical-anchor interpolation and apply fresh account03/B02 r33 to the low-stable-rank / strip collar with all original-coordinate product provenance retained.

# Early substantive checkpoint — D4 anchor interpolation

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. Target-wide universal unweighted `int |phi_Q|` remains OPEN / not refuted.

Sources actually used at equations:

* newest-Claude source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `FOURIER_ROUTE_REPORT.md` D'/D5/general D_k;
* reviewed q-dependent sharp-Hausdorff--Young continuation `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`;
* prior account02/B02 original-coordinate physical-anchor Plancherel endpoints `yspennstate/math-open-problems@4029b9b55694ce709e43c62d2729e89108fbdede`;
* fresh designated partner account03/B02 r33 `QFORM-H2-TO-H3-OR-STRIPS-v1`, canonical mathematics `yspennstate/math-open-problems@604b3273a6db312558088b7ed2a9d9735c546e7a`.

The reviewed degree-k sharp-HY calculation gives for a physical cross block `B`, if its k-volume row marginals obey `alpha_i^(k)<=q/2`,

`|phi_Q(t)| <= min(1, e^(k/(2q)) q^(-k/(4q)) pi^(k/(2q)) E_k(B)^(-1/(4q)) |t|^(-k/(2q)))`              (0.1)

for `q>=1`; its density conclusion needs `k>2q`. All same-bank phases, outside couplings and affine terms remain arbitrary.

## 1. Invertible physical 2x2 anchor: `QFORM-ANCHOR-D4-GEOMEAN-L1-v1`

Let a physical cross block contain an invertible physical `2x2` anchor `P`, put

`D=|det P|`, `S=M-CP^(-1)R`, `F^2=||S||_F^2`, `G=D^2 F^2`.

The original-coordinate pair-Plancherel endpoint is

`|phi_Q(t)| <= pi D^(-1/2)|t|^(-1)`.                              (1.1)

Let `rho=sr(S)=F^2/||S||op^2>1`. If `x_j=s_j(S)^2`, then `sum x_j=F^2` and `max x_j=F^2/rho`; hence

`E2(S)=1/2[(sum x_j)^2-sum x_j^2]
        >=(rho-1)/(2rho) F^4 =:c2(rho)F^4`.                       (1.2)

Every `4x4` minor using the fixed anchor equals `det(P)` times a `2x2` minor of `S`, so

`E4(B)>=D^2E2(S)>=c2(rho)G^2/D^2`.                               (1.3)

Assume the fourth-volume row marginals of the FULL physical block `B` obey `alpha_i^(4)<=q/2` for some `1<=q<2`. Substituting (1.3) into (0.1) at `k=4`, and taking the geometric mean with weights `1/(q+1)` on (1.1) and `q/(q+1)` on the D4 tail, cancels `D` exactly:

`|phi_Q(t)| <= min{1,
 K4(q,rho) G^(-1/[2(q+1)]) |t|^(-3/(q+1))}`,                    (1.4)

`K4=e^(2/(q+1)) q^(-1/(q+1)) pi^(3/(q+1))
    c2(rho)^(-1/[4(q+1)]).`                                      (1.5)

Since `q<2`, `3/(q+1)>1`. Exact integration of `min(1,A|t|^-a)` therefore gives

`boxed:
 ||p_Q||inf <= [3 e^(2/3)/((2-q)q^(1/3))]
                c2(rho)^(-1/12) G^(-1/6).
`                                                                    (1.6)

This is a genuine unweighted Fourier-L1 estimate, so the branch has a continuous C0 density.

At the clean choice `q=3/2`, if `rho>=3/2` then `c2(rho)>=1/6`, hence

`boxed: ||p_Q||inf <11.853041 G^(-1/6).`                          (1.7)

## 2. Rank-one second anchor / scalar pivot

If the physical `2x2` anchor has rank one, choose a genuinely nonzero physical scalar pivot `p`; let `S1` be its actual scalar cross-Schur residual and put

`H=p^2 E2(S1)`.

The scalar physical Plancherel endpoint is

`|phi_Q(t)|<=sqrt(pi)|p|^(-1/2)|t|^(-1/2)`.                      (2.1)

For `rho1=sr(S1)>2`, cap packing gives

`E3(S1)>=c3(rho1)||S1||_F^6`,                                   (2.2)

where `c3(rho)=(rho-2)/rho^3` for `2<rho<=3`, and `c3(rho)>=1/27` for `rho>=3`. Also `E2(S1)<=||S1||_F^4/2`, so

`E4(B)>=p^2E3(S1)
       >=c3(rho1)2^(3/2)H^(3/2)|p|^(-1)`.                       (2.3)

Assume `alpha_i^(4)<=q/2` with `1<=q<7/4`. Interpolating (2.1) with the D4 tail using weights `1/(2q+1)` and `2q/(2q+1)` cancels `p` and yields time exponent

`a=9/[2(2q+1)]>1`.                                                (2.4)

Exact inversion gives

`boxed:
 ||p_Q||inf <= [9 e^(8/9)q^(-4/9)/(7-4q)]
                2^(-1/6)c3(rho1)^(-1/9)H^(-1/6).
`                                                                    (2.5)

At `q=3/2`, `rho1>=5/2` implies `c3>=4/125`, hence

`boxed: ||p_Q||inf <23.874927 H^(-1/6).`                          (2.6)

Again `phi_Q in L1` and the density is continuous C0.

## 3. Two-sided failure of the new D4 gate is a physical fourth-volume star

Because the sharp-HY decoupling is one-sided, either orientation may be used. If at `q=3/2` neither orientation is admissible, there are a physical row `i` and physical column `j` with fourth-volume inclusion probabilities

`alpha_i^(4)>3/4`, `beta_j^(4)>3/4`.

Under the normalized squared `4x4`-minor law, inclusion-exclusion gives

`P(i in S and j in T)>=alpha_i+beta_j-1>1/2`.

Therefore the joint incident fourth-volume packet obeys

`boxed:
 J4(i,j):=sum_(S contains i,T contains j,|S|=|T|=4) det B[S,T]^2
 > E4(B)/2.
`                                                                    (3.1)

Thus D4 gate failure is not an unspecified analytic obstruction: it creates a physical fourth-volume near-coloop/star. In one orientation alone, `alpha_i>3/4` equivalently gives

`E4(B with row i deleted)<E4(B)/4`.                                (3.2)

No conclusion about the single coefficient `B_ij` is drawn.

## 4. Fresh designated-partner application

Fresh account03/B02 r33 proves on its residual H2 branch the exact identity

`aK=L+u(vM-c0 rho^T)+(bc0-v gamma)r0^T`,                         (4.1)

and consequently, on the live heavy-third-volume branch `J>Z/3`,

`max{G3,U,V}>Z/864`,                                             (4.2)

where `G3=||L||_F^2` is genuine physical double-anchor incident third-volume and `U,V` are literal one-sided original-coordinate 2x2-minor strip products.

On the `G3` alternative with invertible second anchor, `G3=D^2||S||_F^2`; hence (1.7) gives the actual new inequality

`boxed:
 max alpha^(4)<=3/4, sr(S)>=3/2, G3>Z/864
 => ||p_Q||inf <36.580423 Z^(-1/6).
`                                                                    (4.3)

This lowers the previous determinant-cancelling D5 stable-rank threshold `5/2` to `3/2` on the D4-admissible part of the partner packet.

If the second anchor has rank one, the scalar Schur packet satisfies `H>=G3`; hence (2.6) gives

`boxed:
 max alpha^(4)<=3/4, sr(S1)>=5/2, G3>Z/864
 => ||p_Q||inf <73.681933 Z^(-1/6).
`                                                                    (4.4)

This lowers the previous D6 threshold `5` to `5/2` on the same D4-admissible part.

If the D4 gate fails in both orientations, (3.1) supplies the next physical fourth-volume star instead of losing the branch. The remaining partner alternatives `U,V` still require a grouped-strip / mixed-hub receiver; this checkpoint does not pretend they are paid by (1.6).

The exact-target conjecture remains open. No target-valid counterexample to the universal unweighted Fourier-L1 criterion is produced here.
