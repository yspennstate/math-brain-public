SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T15:00:32Z.
attacking: compile the r32 residual anchored-E2 packet into a double-anchor third-volume packet or explicit one-sided strip packets, then spend the double-anchor branch by D5/pair integrated-Fourier interpolation and apply fleet04/B02's L2 theorem to a new hybrid inequality.

# fleet03/B02 r33 — residual H2 packet compiler and double-anchor Fourier payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control refreshed before publication:** revision `2026-09-22.15`, QFORM only  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`; authenticated GitHub repository reads/writes occurred, but no native learned-memory ingestion/receiver was verified  
**Full QFORM target:** **OPEN**  
**Target-wide universal unweighted Fourier L1 criterion:** **OPEN / not refuted**  
**Continuity:** proved on the new high-stable-rank double-anchor Fourier branch below; not proved on the remaining strip alternatives and not proved for the full target.

## 1. Exact live branch and source-pinned inputs

The preceding fleet03/B02 r32 theorem is at

`yspennstate/math-open-problems@3cc1145d1fb015deed33085d536db7156d918225`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T142846Z-fleet03-B02-qform-r32/REPORT.md`.

It works with an ORIGINAL-coordinate physical cross block

`B=[[a,r^T],[c,N]]`, `a!=0`,                                      (1.1)

and its scalar cross-Schur residual

`S=N-c r^T/a`,                                                    (1.2)

with heavy anchored third-volume

`J=a^2 E2(S)`.                                                    (1.3)

On the live r30 heavy branch, `J>Z/3`, where `Z=E3(B)`.

The r32 theorem says either a genuine two-star/transverse packet is already large, or `a^2E2(N)>=J/4`; on the latter branch its weighted mixed-(3+2) Fourier theorem gives a continuous-density L1 exit or one of

`G3^(x,i;y,j)(B)>J/8`                                            (1.4)

or

`H2^(i,j)(N)>E2(N)/8>=J/(32a^2)`.                               (1.5)

The only purpose of this run is to pay more of these remaining physical packets without selecting a reciprocal tiny minor.

The newest Claude Fourier source actually applied is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

Its proved D5 theorem gives, for any ORIGINAL-coordinate physical cross block `M`, with `E5(M)>0`,

`||p_Q||inf <=5 sqrt(2e) E5(M)^(-1/10)`,                        (1.6)

with all same-bank phases and outside couplings retained.

The sharper determinant-cancelling receiver used below is source-pinned at fleet02/B02:

`yspennstate/math-open-problems@4029b9b55694ce709e43c62d2729e89108fbdede`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T141147Z-fleet02-B02-QFORM-auto11/REPORT.md`.

For an invertible physical `2x2` anchor `P`, with `D=|det P|`, Schur cross residual `T`, packet `G=D^2||T||_F^2`, and `rho=sr(T)>2`, it proves

`||p_Q||inf <=9 e^(5/9)2^(-5/18)c3(rho)^(-1/18)G^(-1/6)`,       (1.7)

where

`c3(rho)=(rho-2)/rho^3` for `2<rho<=3`, and `c3(rho)=1/27` for `rho>=3`.  (1.8)

In particular `rho>=5/2` gives `c3>=4/125` and coefficient `<15.665527`. Its proof genuinely yields `phi_Q in L1`.

The designated fleet04/B02 partner theorem is source-pinned at

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.

When the full physical form has a nonsingular zero-diagonal principal triple `H0`, it proves

`int_R |phi_Q(t)|^2 dt <=6 pi 2^(2/3)|det H0|^(-1/3)`.          (1.9)

No post-rotation independence, arbitrary-joint coarea estimate, conditional projection-height bound, law-uniform scalar quadratic stationary phase, or small-random-tail deletion is used anywhere below.

## 2. Main new algebraic theorem — `QFORM-H2-TO-H3-OR-STRIPS-v1`

Assume the r32 residual packet (1.5). Reorder the selected residual row/column first and split the original anchor vectors accordingly:

`N=[[b,rho^T],[gamma,M]]`,                                      (2.1)

`r=(u,r0)`, `c=(v,c0)`.                                        (2.2)

Thus the full anchored cross block, with the selected residual row/column second, is

`B = [[a, u, r0^T],
      [v, b, rho^T],
      [c0, gamma, M]]`.                                         (2.3)

Define the residual anchored-two-volume kernel

`K=bM-gamma rho^T`.                                             (2.4)

By the exact physical-minor identity,

`H2^(i,j)(N)=||K||_F^2`.                                       (2.5)

Define the physical double-anchor block and its bordering banks

`P=[[a,u],[v,b]]`,
`R=[[r0^T],[rho^T]]`,
`C=[c0,gamma]`,                                                 (2.6)

and define

`L=det(P)M-C adj(P)R`.                                          (2.7)

Then `||L||_F^2` is exactly the physical third-volume incident to both selected rows and both selected columns:

`G3^(x,i;y,j)(B)=||L||_F^2`.                                   (2.8)

### The exact three-packet identity

A direct expansion of (2.7) gives

`boxed:
 aK
 = L + u(vM-c0 rho^T) + (b c0-v gamma)r0^T.
`                                                                    (2.9)

Indeed

`C adj(P)R
 =[c0,gamma] [[b,-u],[-v,a]] [[r0^T],[rho^T]]`

`=(b c0-v gamma)r0^T+(-u c0+a gamma)rho^T`,                    (2.10)

so

`L=(ab-uv)M-(b c0-v gamma)r0^T+(u c0-a gamma)rho^T`,           (2.11)

and adding the two stated correction packets leaves

`abM-a gamma rho^T=aK`.                                        (2.12)

Taking Frobenius norms in (2.9), at least one of the following three packets satisfies

`boxed: G3:=||L||_F^2 >= a^2||K||_F^2/9`,                       (2.13)

`boxed: U:=u^2||vM-c0 rho^T||_F^2 >= a^2||K||_F^2/9`,           (2.14)

or

`boxed: V:=||b c0-v gamma||_2^2 ||r0||_2^2
               >=a^2||K||_F^2/9`.                              (2.15)

Otherwise each of the three Frobenius norms on the right of (2.9) would be strictly less than `|a|||K||_F/3`, contradicting (2.9).

Using the r32 H2 lower bound (1.5),

`a^2||K||_F^2 > J/32`,                                         (2.16)

so one of (2.13)-(2.15) satisfies

`boxed: max{G3,U,V}>J/288`.                                    (2.17)

On the live r30 heavy branch `J>Z/3`,

`boxed: max{G3,U,V}>Z/864`.                                    (2.18)

This is the principal new reduction of the run.

### Why U and V are genuine physical strip packets

No Schur-probabilistic interpretation is needed. For each residual row `p` and residual column `q`,

`(vM-c0 rho^T)_{pq}=v M_pq-c0_p rho_q`                         (2.19)

is the determinant of the physical `2x2` cross minor on row pair `{i,p}` and column pair `{y,q}`. Therefore U is the squared physical edge `u=B[x,j]` times the aggregate squared-minor mass of an actual one-sided strip.

Similarly

`(b c0-v gamma)_p=b c0_p-v gamma_p`                             (2.20)

is, up to the irrelevant determinant sign convention, the physical `2x2` minor on row pair `{i,p}` and column pair `{y,j}`. Hence V is another literal one-sided minor strip times the untouched original-coordinate star `||r0||^2`.

Thus the former r32 H2 alternative is no longer a separate diffuse `E2` obstruction: it is compiled into a known double-anchor packet or one of two explicit original-coordinate strip products.

## 3. Integrated-Fourier payment of the new G3 alternative

Assume the G3 alternative in (2.17). First suppose the physical `2x2` block P in (2.6) is invertible. Put

`D=|det P|`,
`T=M-CP^(-1)R`.                                                 (3.1)

The exact block-determinant identity gives

`G3=D^2||T||_F^2`.                                              (3.2)

Let `rho_T=sr(T)`. If `rho_T>2`, the stable-rank exterior-volume inequality used in fleet02/B02 gives

`E3(T)>=c3(rho_T)||T||_F^6`.                                   (3.3)

Every physical `5x5` minor using the two anchored rows and columns equals `det(P)` times the corresponding residual `3x3` minor, hence

`E5(B)>=D^2 E3(T)
       >=c3(rho_T) G3^3/D^4`.                                  (3.4)

### Newest-Claude input applied at an actual equation

Applying the newest Claude D5 theorem (1.6) to (3.4) gives the valid direct bound

`boxed:
 ||p_Q||inf
 <=5 sqrt(2e)c3(rho_T)^(-1/10)
   D^(2/5)G3^(-3/10).
`                                                                    (3.5)

This equation is a direct application of the owner-required newest Claude result. It is not yet determinant-free and is therefore not by itself the final receiver.

### Determinant cancellation with the physical-pair endpoint

The physical-pair Plancherel estimate from fleet02/B02 is

`|phi_Q(t)|<=pi D^(-1/2)|t|^(-1)`.                              (3.6)

The sharp D5 tail underlying (3.5) is

`|phi_Q(t)|
 <=e^(5/4)2^(-5/8)pi^(5/4)c3(rho_T)^(-1/8)
   D^(1/2)G3^(-3/8)|t|^(-5/4)`.                                (3.7)

Taking the geometric mean of (3.6) and (3.7) cancels D exactly and yields

`|phi_Q(t)|
 <=min{1,
 e^(5/8)2^(-5/16)pi^(9/8)c3(rho_T)^(-1/16)
 G3^(-3/16)|t|^(-9/8)}.                                       (3.8)

Since `9/8>1`, this proves `phi_Q in L1`. Exact inversion gives

`boxed:
 ||p_Q||inf
 <=9e^(5/9)2^(-5/18)c3(rho_T)^(-1/18)G3^(-1/6).
`                                                                    (3.9)

For `rho_T>=5/2`, `c3>=4/125`, so

`boxed: ||p_Q||inf<15.665526724 G3^(-1/6).`                     (3.10)

Combining (2.18) with (3.10),

`boxed:
 ||p_Q||inf<48.346379735 Z^(-1/6).
`                                                                    (3.11)

The law has a continuous density vanishing at infinity on this branch.

If P has rank one, the fleet02/B02 scalar-anchor D6 receiver applies whenever the resulting scalar Schur residual has stable rank at least five. Its bound `<38.541905463 G3^(-1/6)` therefore gives, from (2.18),

`boxed:
 ||p_Q||inf<118.946629122 Z^(-1/6),
`                                                                    (3.12)

again with `phi_Q in L1`. The low-stable-rank rank-one-anchor collar remains an explicit separate obligation.

## 4. Designated fleet04/B02 theorem applied to a new hybrid inequality

Now assume the invertible-P branch above, `rho_T>2`, and additionally that the ambient physical form has a nonsingular zero-diagonal principal triple `H0`, so the designated partner estimate (1.9) applies.

Write

`c=c3(rho_T)`, `G=G3`,

`K0=e^(5/8)2^(-5/16)pi^(9/8)c^(-1/16)G^(-3/16)`.               (4.1)

Equation (3.8) supplies the high-frequency tail

`|phi_Q(t)|<=K0 |t|^(-9/8)`.                                   (4.2)

The partner supplies

`L:=int |phi_Q|^2
 <=6pi 2^(2/3)|det H0|^(-1/3)`.                               (4.3)

For every `T0>0`, Cauchy-Schwarz on `[-T0,T0]` and (4.2) outside give

`||phi_Q||_1
 <=sqrt(2L T0)+16K0 T0^(-1/8)`.                               (4.4)

Set `A0=sqrt(2L)`. The optimizer satisfies

`T0^(5/8)=4K0/A0`.                                             (4.5)

At this value the second term is four times the first, so

`||phi_Q||_1
 <=5 A0^(1/5)(4K0)^(4/5)`.                                   (4.6)

Using Fourier inversion and substituting (4.1)-(4.3), all powers of pi cancel and we obtain the genuinely new partner-hybrid inequality

`boxed:
 ||p_Q||inf
 <=C04 |det H0|^(-1/30)c3(rho_T)^(-1/20)G3^(-3/20),
`                                                                    (4.7)

where

`C04=5*2^(37/60)*3^(1/10)*sqrt(e)
   =14.107970236...`.                                           (4.8)

For `rho_T>=5/2`,

`boxed:
 ||p_Q||inf
 <=16.757415412 |det H0|^(-1/30)G3^(-3/20).
`                                                                    (4.9)

On the new packet size `G3>Z/864`, this becomes

`boxed:
 ||p_Q||inf
 <46.204481095 |det H0|^(-1/30) Z^(-3/20).
`                                                                    (4.10)

This is an equation-level use of the designated fleet04/B02 theorem. Continuity on this overlap does not rely on the partner's L2 estimate: it already follows from the L1 estimate (3.8).

## 5. What this run closes and what remains

The r32 H2 packet no longer needs to be carried as a distinct aggregate residual-E2 case. It is now exhaustively compiled by (2.17) into:

1. a double-anchor third-volume packet `G3>J/288`, which is paid whenever its invertible cross-Schur residual has stable rank at least `5/2`, and also in the stated high-stable-rank rank-one-anchor branch;
2. the literal one-sided strip packet `U>J/288`;
3. the literal one-sided strip/star packet `V>J/288`.

The r32 H3 branch was already stronger (`G3>J/8`) and therefore inherits every G3 payment above with better constants. The old r32 two-star/transverse alternative remains separate and unchanged.

The **first unpaid B02 implication** is now

`QFORM-STRIP-OR-LOWRANK-DOUBLEANCHOR-RECEIVER-v1`:

- pay U or V by a product-preserving grouped-strip / mixed-Fresnel receiver while retaining arbitrary same-bank curvature; and
- pay the low-stable-rank collar of the G3 double-anchor branch without deleting its small singular directions or selecting a reciprocal tiny minor.

The full three-large-eigenvalue theorem is not established by this run, and the stronger target-wide `int|phi_Q|` criterion is neither proved nor refuted.

## 6. Correction boundary

The proof uses only original-coordinate physical blocks and exact determinant identities. Algebraic Schur complements are used only to express determinant families; their coordinates are never declared independent. No arbitrary-joint coarea lemma, worst conditional projection density, uniform single-direction van der Corput bound, fixed-good-minor inference, small matrix-tail deletion, or post-rotation product structure is used.

In particular, (2.9) is an identity in coefficients, not a probabilistic coordinate transform. The Fourier bounds (1.6), (3.6), and the partner estimate (1.9) are all established original-coordinate product-source estimates in their cited scopes.

## 7. Computation check

A deterministic seeded regression on 1000 random dense block matrices checked (2.9). The maximum relative Frobenius discrepancy was

`1.7642082675161952e-15`.

The constants recomputed independently are

`5sqrt(2e)=11.658219907985622`,
`C_highrank=15.665526723732583`,
`C_highrank*864^(1/6)=48.34637973497758`,
`38.541905462520745*864^(1/6)=118.94662912149158`,
`C04=14.107970235994491`,
`C04*(4/125)^(-1/20)=16.757415411794742`,
`16.757415411794742*864^(3/20)=46.20448109470123`.

The finite regression is only corroboration; the proof is the exact symbolic expansion (2.10)-(2.12) and the cited Fourier theorems.

## 8. Status

**New result:** `QFORM-H2-TO-H3-OR-STRIPS-v1`, plus the high-stable-rank double-anchor L1 payment and the fleet04/B02 L2/L1 hybrid (4.7).  
**Full target:** OPEN.  
**Target-wide universal unweighted Fourier L1:** OPEN / not refuted.  
**Continuity:** proved on the new paid G3 branches; full-target continuity OPEN.  
**Next:** `QFORM-STRIP-OR-LOWRANK-DOUBLEANCHOR-RECEIVER-v1`.
