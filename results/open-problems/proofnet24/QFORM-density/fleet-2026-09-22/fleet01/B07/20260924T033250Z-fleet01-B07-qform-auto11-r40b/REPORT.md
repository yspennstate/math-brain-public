SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-24T03:32:50Z.
attacking: the exact-singular low-pivot h=2 operator-star survivor — preserve the whole bordered-minor law, balance its physical coordinates before selecting anything, and force a third original-coordinate resource from s_3(A)>=1.

# fleet01/B07 r40b — exact-singular determinant-star balance and third-resource router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection  
Status: `NEW STRUCTURAL THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
Continuity: not proved by the new structural theorem; full-target continuity remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary


The incoming B07 theorem is fleet01/B07 r39,

`yspennstate/math-open-problems@ce8f5fb778ae6f29b4b99ee9574360f71f584c68`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/20260924T020937Z-fleet01-B07-qform-auto11-r39/REPORT.md`.

Its low-pivot h=2 branch supplies one literal physical pair `H={i,j}`. Put

`B=A[H,H]`, `delta=det B`, `O=H^c`,

`D_H(r,c)=det A[(H,r),(H,c)]`, `r,c in O`.

After the already-paid principal-triple exit has failed, r39 gives

`m_H:=max(|A_ii|,|A_jj|,|A_ij|)<1/64`,

`max_r |D_H(r,r)|<1/96`,

`||D_H||_op >= 7/96`.                                      (1.1)

It also proved the exact Sylvester identity

`D_H=delta A[O,O]-A[O,H] adj(B) A[H,O]`.                  (1.2)

The present run treats the exact singular face `delta=0` and, crucially, uses the global owner hypothesis `s_3(A)>=1` before any reciprocal pair selection.

The newest completed designated partner actually consumed is fleet02/B07,

`yspennstate/math-open-problems@ec29bb4321feffe020e5cb0185d148f2f6de847e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260924T013622Z-fleet02-B07-qform-auto11/REPORT.md`.

Its theorem `QFORM-E2-BOUNDED-SUPPORT-BALANCE-v1` states

`E2(K) <= (rank(K)-1) s_2(K)^2 ||K||_F^2`,                  (1.3)

and if a `p x q` physical block has entries bounded by `L`, then

`s_2(K) >= [E2(K)/((rank(K)-1)pqL^2)]^(1/2)`.              (1.4)

Its companion stress correctly warns that a diffuse aggregate E2 packet need not have a dimension-free balanced second singular value or bounded physical core.

## 2. Exact singular pair: the complete bordered-minor law is rank one and diffuse

Assume now `delta=0`. Since (1.1) says `D_H` is nonzero, `B` cannot be the zero matrix. Thus there are a signed nonzero eigenvalue `tau`, a unit vector `ell in R^2`, and a unit kernel vector `k perpendicular ell` such that

`B=tau ell ell^T`, `adj(B)=tau k k^T`.                         (2.1)

Let

`U=A[O,H]`, `q=Uk`, `s=||q||_2`, `L=||D_H||_op`.              (2.2)

Equation (1.2) becomes the exact physical-coordinate identity

`boxed: D_H = -tau q q^T.`                                      (2.3)

Consequently

`boxed: |tau| s^2 = L >= 7/96.`                                 (2.4)

Moreover `|tau|=|tr B|<1/32`, because both physical diagonal entries of `B` have modulus `<1/64`.

The failed principal-triple exit in (1.1) now has a useful meaning. From (2.3),

`|tau| q_r^2=|D_H(r,r)|<1/96`,

and after division by (2.4),

`boxed: max_r q_r^2/s^2 < 1/7.`                                (2.5)

Thus the exact-singular bordered-minor direction is quantitatively diffuse in the ORIGINAL residual coordinates. No rotated random coordinate has been introduced.

### 2.1 Dimension-free physical two-bank selection

Set `p_r=q_r^2/s^2`. Since `sum p_r=1` and `max p_r<1/7`, a greedy accumulation gives a literal physical subset `R subset O` with

`3/7 <= sum_(r in R) p_r < 4/7`.                                (2.6)

For `S=O\R`, both banks therefore contain at least `3/7` of the q-energy. From (2.3),

`D_H[R,S]=-tau q_R q_S^T`,

hence

`boxed:
 ||D_H[R,S]||_op
 =|tau| ||q_R||_2 ||q_S||_2
 >= (sqrt(12)/7)L
 >= sqrt(3)/48.
}`                                                               (2.7)

This is the desired determinant-weighted coordinate localization: the whole h=2 star is balanced first, and only then is a physical cut selected. There is no tiny-minor pigeonhole and no inverse of `B`.

The complete off-diagonal fixed-pair overlap-two currency also obeys

`Omega_(2,H)
 =sum_(r!=c) D_H(r,c)^2
 =tau^2[(sum_r q_r^2)^2-sum_r q_r^4]`.                           (2.8)

By (2.5), `sum p_r^2<1/7`; therefore

`boxed: Omega_(2,H) > (6/7)L^2 >= 7/1536.`                       (2.9)

So the exact-singular survivor contains a constant complete overlap-two packet even when every individual physical bordered minor is small.

## 3. Existing exact-pair receiver applied, and its precise remaining loss

A newer completed theorem from fleet02/B09,

`yspennstate/math-open-problems@9c6683c03c8b0dbd635314109854871448343055`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260924T021301Z-fleet02-B09-QFORM-r16/REPORT.md`,

proves for an exact nonzero rank-one physical pair with arbitrary pair-to-leaf cross rank and arbitrary same-leaf curvature that

`||p_Q||_infinity <= 2^(5/2) (|tau| s)^(-1/2)`.                  (3.1)

Using (2.4), this gives the actual scoped inequality

`boxed:
 ||p_Q||_infinity
 <= 2^(5/2) (7|tau|/96)^(-1/4)
 < 10.886 |tau|^(-1/4).
}`                                                               (3.2)

Equivalently (2.9) and that theorem's overlap form give

`||p_Q||_infinity < 11.098 |tau|^(-1/4)`.                        (3.3)

Thus all exact-singular pairs with a fixed lower bound on `|tau|` are already paid, with completely arbitrary outside curvature. The only quantitative exact-singular collar left by this receiver is `|tau| ->0`; fleet02/B09 also gives a target-valid near-singular example showing that one cannot simply perturb its half-Riesz proof through `det B !=0`.

## 4. Main new theorem: the third owner-scale resource cannot disappear with tau

The small-`|tau|` collar is not allowed to become a two-direction problem, because the original matrix still satisfies `s_3(A)>=1`. The following lemma forces a third physical resource before any analytic conditioning.

Write the original-coordinate block decomposition

`A = [[B,U^T],[U,C]]`, `C=A[O,O]`.                                (4.1)

Let `U_1` be a best rank-one approximation to the `|O| x 2` matrix `U`, and define

`T=[[0,U_1^T],[U_1,0]]`.                                         (4.2)

Then `rank T<=2`. Since `s_3(A)>=1`, Eckart--Young gives

`1 <= ||A-T||_op`.                                                (4.3)

But if `E=U-U_1`, then

`A-T=[[B,E^T],[E,C]]`,

and therefore

`||A-T||_op
 <= max(||B||_op,||C||_op)+||E||_op
 = max(|tau|,||C||_op)+s_2(U)`.                                  (4.4)

Combining (4.3)-(4.4),

`boxed: max(|tau|,||C||_op)+s_2(U) >=1.`                          (4.5)

Since `|tau|<1/32`, at least one of

`boxed: s_2(U)>31/64`                                             (4.6)

or

`boxed: ||C||_op>31/64`                                           (4.7)

must hold. This uses the THIRD large singular direction of the original A directly; it does not delete the exact-singular pair or rotate the independent inputs.

### 4.1 Cross-E2 branch

Because `U` has only two columns, (4.6) implies

`boxed:
 E2(U)=s_1(U)^2 s_2(U)^2 >= s_2(U)^4
 > (31/64)^4
 =923521/16777216
 >0.0550.
}`                                                               (4.8)

Thus one branch regenerates a macroscopic complete physical E2 packet between the actual pair H and the residual coordinates.

### 4.2 Outside-curvature branch: physical square or disjoint cross operator

Assume (4.7). If some original residual coordinate satisfies

`|C_rr|>=31/128`,                                                 (4.9)

then we have a constant physical square outside H.

Otherwise put `M=C-diag(C)`. Then

`||M||_op >= ||C||_op-||diag(C)||_op >31/128`.                    (4.10)

For a random sign diagonal `D=diag(epsilon_r)`, let

`N=(M-DMD)/2`.                                                     (4.11)

For the cut `O=R union S` determined by the signs, `N` has only the two cross blocks and

`||N||_op=||C[R,S]||_op`.                                        (4.12)

If `x` is a unit top singular/eigenvector of the symmetric `M`, then conditioning on `epsilon_i` gives the exact identity

`E |(Nx)_i|^2
 =1/4 (Mx)_i^2 +1/4 sum_j M_ij^2 x_j^2`.                         (4.13)

Summing,

`E||Nx||_2^2 >=1/4||M||_op^2`.                                   (4.14)

Hence some literal original-coordinate cut satisfies

`boxed:
 ||C[R,S]||_op >=(1/2)||M||_op >31/256.
}`                                                               (4.15)

This is another dimension-free coordinate selection statement. It extracts an actual disjoint residual crossing, not an abstract spectral direction.

### 4.3 Simultaneous q-balance and outside crossing

The same cut can be chosen to retain a definite amount of the exact-singular determinant-star currency. Let

`P_R=sum_(r in R) q_r^2/s^2`.

For the random cut, `E P_R=1/2` and, using (2.5),

`Var(P_R)=1/4 sum_r p_r^2 <1/28`.                                 (4.16)

Chebyshev gives

`P{|P_R-1/2|>=2/5}<25/112`.                                      (4.17)

On the bad event `||Nx||^2<=||M||^2`. Combining (4.14) and (4.17),

`E[||Nx||^2 1_{1/10<P_R<9/10}]
 > (1/4-25/112)||M||^2
 =3/112 ||M||^2`.                                                  (4.18)

Therefore one cut has simultaneously

`boxed: 1/10<P_R<9/10`,                                          (4.19)

and

`boxed:
 ||C[R,S]||_op
 >=sqrt(3/112)||M||_op
 > (31/128)sqrt(3/112)
 = (31/512)sqrt(3/7)
 >0.0396.
}`                                                               (4.20)

On that same cut the bordered-minor cross satisfies

`boxed:
 ||D_H[R,S]||_op
 =L sqrt(P_R(1-P_R))
 > L/10
 >=7/960.
}`                                                               (4.21)

So in the outside-cross branch, a single original-coordinate partition simultaneously exposes the third residual crossing and a nontrivial fraction of the exact-singular determinant-star packet. This is the strongest selection statement of the run.

## 5. Designated partner fleet02/B07 applied to an actual inequality

The cross-E2 branch (4.8) is still aggregate; the designated partner theorem tells exactly what happens if that packet is physically concentrated.

Let `R_0 subset O` have cardinality `m`, suppose

`E2(U[R_0,H]) >= (1/2) E2(U)`,                                   (5.1)

and suppose the actual original-coordinate entries on this row core obey

`max_(r in R_0,h in H)|U_rh| <= L_0`.                             (5.2)

Apply fleet02/B07's completed theorem (1.4) with `p=m`, `q=2`, `rank<=2`. From (4.8),

`sqrt(E2(U[R_0,H]))
 > (31/64)^2/sqrt(2)`.                                            (5.3)

Therefore the actual physical subblock satisfies

`boxed:
 s_2(U[R_0,H])
 > (31/64)^2/(2 sqrt(m) L_0)
 = 961/(8192 sqrt(m) L_0).
}`                                                               (5.4)

This is an equation-level application of the current designated partner result. It cleanly separates the bounded-support case from the genuine diffuse-support case: if a bounded physical row core carries half of the new E2 currency, it contains two quantitative singular directions at the explicit scale (5.4); otherwise the determinant packet itself is support-diffuse, exactly the regime the partner stress says must be handled without a bounded-core pigeonhole.

## 6. Supporting theorem recorded

The result of Sections 2--5 is recorded as

`QFORM-EXACTSINGULAR-H2-THIRDRESOURCE-ROUTER-v1`:

> In the r39 exact-singular low-pivot h=2 survivor, the full bordered-minor law is `D_H=-tau q q^T` with `|tau|s^2>=7/96` and coordinate leverage `<1/7`. It admits a dimension-free physical two-bank determinant cut. Moreover the owner hypothesis `s_3(A)>=1` forces either a macroscopic physical pair-to-residual E2 packet `E2(U)>(31/64)^4`, or residual operator curvature `||C||>31/64`. The latter yields either a physical square `>=31/128` or a disjoint physical residual crossing; in the crossing case one can choose the same partition so that the bordered-minor star remains quantitatively present.

Every statement is in original coordinates. No individual tiny principal minor is inverted.

## 7. What remains

This is not a full solution. The sharpened exact-singular debt is now:

`QFORM-TAU-SMALL-THIRDRESOURCE-RECEIVER-v1` — jointly spend the small-`|tau|` exact rank-one pair, its diffuse q-star, and one of the forced third resources from Section 4. The existing exact-pair half-Riesz receiver has the explicit `|tau|^{-1/4}` loss (3.2), so a valid uniform proof must use the third resource BEFORE the worst-slice half-Riesz step.

The near-singular `delta!=0 ->0` branch and the r39 anchored-E4 branch remain separate. Fleet02/B09's target-valid near-singular example rules out treating the small determinant as a perturbative random error.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains OPEN.
