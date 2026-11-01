SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T15:09:44Z.
attacking: QFORM-SECONDANCHOR-CRITICAL-STABLERANK-RECEIVER-v1 by combining a physical-anchor Plancherel endpoint with the reviewed degree-4 sharp-Hausdorff--Young volume estimate; apply fleet03/B02 r32's heavy-anchor descent to a live inequality.

# Early substantive checkpoint: degree-4 anchor interpolation

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Source used: reviewed sharp-HY calculation at `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. Its degree-k calculation gives, for a physical cross block M and k-volume row marginals <=q/2,

`|phi_Q(t)| <= min(1, e^(k/(2q)) q^(-k/(4q)) pi^(k/(2q)) E_k(M)^(-1/(4q)) |t|^(-k/(2q)))`,

with arbitrary same-bank phases/outside couplings retained. For k=4 this is integrable for q<2, but after a Schur determinant identity its density bound can carry a bad positive power of the physical anchor. The calculation below cancels that power against an independent original-coordinate Plancherel endpoint.

## Invertible 2x2 anchor

Let a physical cross block B contain an invertible 2x2 anchor P. Write `D=|det P|`, let S be the actual algebraic cross-Schur residual, and set

`F^2=||S||_F^2`, `G=D^2 F^2`.

The already-proved original-coordinate pair Plancherel estimate is

`|phi_Q(t)| <= pi D^(-1/2)|t|^(-1)`.

If `rho=sr(S)=F^2/||S||op^2>1`, then

`E2(S)=1/2(F^4-sum s_j^4) >= c2(rho) F^4`,
`c2(rho)=(rho-1)/(2rho)`.

Every 4x4 minor containing the fixed 2x2 anchor equals `det(P)` times the corresponding 2x2 minor of S, hence

`E4(B)>=D^2 E2(S)>=c2(rho) G^2/D^2`.

Assume the 4-volume row marginals of B obey `alpha_i^(4)<=q/2` for some `1<=q<2`. Inserting the preceding E4 bound into the k=4 sharp-HY envelope and taking the geometric mean with weights `1/(q+1)` on the pair-Plancherel bound and `q/(q+1)` on the k=4 bound cancels D exactly. The result is

`|phi_Q(t)| <= min(1, K G^(-1/(2(q+1))) |t|^(-3/(q+1)))`,

`K=e^(2/(q+1)) q^(-1/(q+1)) pi^(3/(q+1)) c2(rho)^(-1/(4(q+1)))`.

Since q<2, the exponent `3/(q+1)>1`. Fourier inversion gives

`||p_Q||inf <= [3 e^(2/3)/((2-q) q^(1/3))] c2(rho)^(-1/12) G^(-1/6)`.

At q=3/2, the only new gate is `max alpha_i^(4)<=3/4`. If `rho>=3/2`, then `c2>=1/6`, so

`||p_Q||inf <=11.853041 G^(-1/6)`.

On the live second-anchor packet `G>Z/24`, this is `<20.130983 Z^(-1/6)`. Thus the previous D5 payment threshold `sr(S)>=5/2` drops to `sr(S)>=3/2` whenever the fourth-volume marginals are at most 3/4.

## Rank-one 2x2 anchor / scalar pivot

On the rank-one second-anchor branch choose a genuinely nonzero scalar physical cross pivot p, let S1 be its actual scalar cross-Schur residual, and put

`H=p^2 E2(S1)`.

The original-coordinate scalar Plancherel endpoint is

`|phi_Q(t)| <= sqrt(pi)|p|^(-1/2)|t|^(-1/2)`.

If `rho1=sr(S1)>2`, the established cap-packing bound is

`E3(S1)>=c3(rho1)||S1||_F^6`,

where `c3(rho)=(rho-2)/rho^3` for `2<rho<=3` and `c3(rho)>=1/27` for `rho>=3`. Since `E2(S1)<=||S1||_F^4/2`,

`E4(B)>=p^2E3(S1)>=c3(rho1)2^(3/2)H^(3/2)|p|^(-1)`.

Assume again `alpha_i^(4)<=q/2`, now with `1<=q<7/4`. Interpolating the scalar Plancherel endpoint with the k=4 sharp-HY envelope using weights `1/(2q+1)` and `2q/(2q+1)` cancels p and gives time exponent

`a=9/[2(2q+1)]>1`.

Fourier inversion gives

`||p_Q||inf <= [9 e^(8/9) q^(-4/9)/(7-4q)] 2^(-1/6)c3(rho1)^(-1/9) H^(-1/6)`.

At q=3/2 and `rho1>=5/2`, `c3>=4/125`, hence

`||p_Q||inf <=23.874927 H^(-1/6)`.

On the live packet `H>Z/24`, this is `<40.548730 Z^(-1/6)`. This lowers the previous scalar D6 stable-rank threshold from 5 to 5/2 under the fourth-volume marginal gate.

## Exact failure classification of the new gate

If the q=3/2 fourth-volume gate fails, there is an original row i with `alpha_i^(4)>3/4`. By the definition of volume marginals,

`E4(B with row i deleted)=(1-alpha_i^(4))E4(B)<E4(B)/4`.

Thus failure is not an unspecified analytic obstruction: it creates a physical fourth-volume near-coloop. The same statement holds on the column side after transposition.

## Designated partner application already available this run

Fresh `fleet03/B02` r32 proves that on the live D' heavy-third-volume branch `J>Z/3`, writing `B=[[a,r^T],[c,N]]`, either

`||c||^2||r||^2||P_(c^perp)NP_(r^perp)||_F^2 > Z/12`,

or the mixed-(3+2) Fourier exit pays, or a deeper double-anchor third-volume packet is `>Z/24`, or an anchored residual second-volume packet is `>Z/(96a^2)`.

This is an actual inequality-level use of the designated partner result. The present degree-4 receiver is intended for the ensuing double-anchor/scalar-anchor packets, not as a claim that every partner packet automatically satisfies its fourth-volume marginal gate.

Remaining check before final report: verify constants and interpolation exponents independently, then refresh corrections/control. The full QFORM target and the target-wide unweighted Fourier-L1 criterion remain OPEN.
