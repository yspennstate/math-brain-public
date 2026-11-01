SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-23T22:16:37Z.
attacking: Schur-gauge signed-spectrum stability: exact pivot-graph perturbations that change arbitrary signed eigenvalues while preserving the physical Schur remainder, plus a quantitative local-tail bound.

# fleet01/B12 — Schur-gauge signed-spectrum stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260923T221637Z-fleet01-B12-QFORM-auto11b`  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **not claimed** for the scalar-Schur/half-Riesz branch used here; the conclusion below is essential boundedness.

## 1. Scope and first missing implication

The target remains the unrestricted statement for independent original coordinates with scalar densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one. No Gaussianity, moments, compact support, connected support, log-concavity, iid hypothesis, post-rotation independence, or independent-convolution treatment of an added quadratic remainder is used.

The previous fleet01/B12 run controlled arbitrary signed additions through a carrier-relative gain. This run changes mechanism. It exploits an **exact Schur-gauge identity**: a large signed packet lying on the graph of a physical pivot block can be arbitrarily large and can cross signs while leaving the entire conditional Schur remainder exactly unchanged. A subsequent non-gauge perturbation is paid only through the few literal physical blocks that can change the Schur crossing used by the scalar receiver.

This attacks the first missing implication early: identify a nontrivial class of additional positive/negative eigenvalues which is exactly free even though it penetrates the pivot and cross blocks, rather than living only in a spectator complement.

## 2. Exact block Schur-gauge identity

Let an ORIGINAL-coordinate split be `x=(u,y)` with `u in R^k`, and write

`A0 = [[C,B],[B^T,D]]`,                                            (2.1)

where `C=C^T` is invertible. Put

`Q=C^{-1}B`,                                                       (2.2)
`S=D-B^T C^{-1}B`,                                                 (2.3)
`R=[[I_k,Q],[0,I]]`.                                               (2.4)

Then the exact congruence is

`A0 = R^T diag(C,S) R`.                                            (2.5)

Equivalently,

`x^T A0 x=(u+Qy)^T C (u+Qy)+y^T S y`.                             (2.6)

Now let `K=K^T` be completely arbitrary: no sign, rank, or norm restriction. Define

`G=[I_k;Q^T]`                                                       (2.7)

and the **Schur-gauge packet**

`E_K=G K G^T`.                                                     (2.8)

Then

`A_K:=A0+E_K=R^T diag(C+K,S)R`,                                   (2.9)

hence

`boxed: x^T A_K x=(u+Qy)^T(C+K)(u+Qy)+y^T S y.`                   (2.10)

If `C+K` is invertible, its Schur complement is therefore exactly

`boxed: Schur_u(A_K)=S=Schur_u(A0).`                              (2.11)

The identity (2.10) remains true even when `C+K` is singular. Thus crossing a local eigenvalue through zero does not corrupt the remainder; it only removes the corresponding local smoothing resource.

### Spectral content of the added packet

`G` has full column rank. The nonzero inertia of `E_K=GKG^T` equals the inertia of `K`: indeed, with `H=G^TG>0`, the nonzero part of `E_K` is unitarily equivalent to the symmetric matrix `H^{1/2} K H^{1/2}`, which is congruent to `K`. Therefore the gauge packet may contain any prescribed number up to `k` of positive and negative directions, with arbitrarily large magnitudes after scaling `K`.

So the theorem genuinely absorbs arbitrarily large **signed** added spectrum, not merely a PSD update. The only change is inside the translated local quadratic block `C+K`; the entire Schur remainder is exactly fixed.

### Product-law safety

Equation (2.10) does **not** assert that the sheared variables `(u+Qy,y)` are independent. Instead, condition on the original coordinates `y`. The original coordinates in `u` remain independent with the same scalar density caps, and `Qy` is then only a deterministic translation. Thus every translation-uniform local receiver may be applied without rotating or shearing the random product law globally.

## 3. Scalar version and exact gauge line

For `k=1`, write the baseline as

`A0 = [[a, a q^T],[a q, S+a q q^T]]`,                              (3.1)

where `a!=0` and `q` is a column vector on the remaining original coordinates. Put

`g=(1,q)^T`.                                                       (3.2)

For every `tau in R`,

`A_tau=A0+tau g g^T
      =[[a_tau,a_tau q^T],[a_tau q,S+a_tau q q^T]]`,              (3.3)

where

`a_tau=a+tau`.                                                     (3.4)

The added rank-one packet has the single nonzero eigenvalue

`tau ||g||^2=tau(1+||q||^2)`,                                     (3.5)

so it can be positive or negative and arbitrarily large. Whenever `a_tau!=0`, the final scalar Schur complement is **exactly `S`**.

The exceptional value `a_tau=0` is a genuine smoothing cancellation, not a proof artifact: at that value the pivot coordinate disappears completely from (3.3). Therefore no magnitude-free theorem based on this scalar pivot can be uniform through that cancellation without another smoothing mechanism.

## 4. Local perturbation theorem around the gauge orbit

The exact gauge identity becomes useful for arbitrary additions because only the distance to the gauge orbit needs to be paid.

Split the remaining original coordinates further as `K union J`. Write

`q=(q_K,q_J)`                                                      (4.1)

and add an arbitrary symmetric perturbation `F`, written in the physical blocks

`F = [[t, z_K^T, z_J^T],
      [z_K, F_KK, W_KJ],
      [z_J, W_KJ^T, F_JJ]].`                                      (4.2)

The same-bank blocks `F_KK` and `F_JJ` may be completely arbitrary. They never enter the scalar-Schur **cross block** from `K` to `J`.

Let

`A=A_tau+F`,                                                       (4.3)
`a_tilde=a_tau+t`.                                                 (4.4)

Assume `a_tilde!=0`. Define

`r_K=z_K-t q_K`, `r_J=z_J-t q_J`.                                 (4.5)

A direct expansion of the final scalar Schur complement gives the exact cross-block identity

`boxed:
Schur_i(A)[K,J]-S[K,J]
 = W_KJ+t q_K q_J^T-q_K z_J^T-z_K q_J^T
   -(r_K r_J^T)/(a_tau+t).`                                       (4.6)

This is the central new stability identity.

Suppose only

`|t|<=d0`, `||z_K||<=dK`, `||z_J||<=dJ`, `||W_KJ||op<=dX`,        (4.7)

with

`a_*:=|a_tau|-d0>0`.                                               (4.8)

Then (4.6) implies

`boxed:
||Schur_i(A)[K,J]-S[K,J]||op <= eps_loc`,                         (4.9)

where

`eps_loc
 = dX+d0||q_K||||q_J||+||q_K||dJ+dK||q_J||
   +((dK+d0||q_K||)(dJ+d0||q_J||))/a_* .`                         (4.10)

Consequently, for every singular index `j`,

`boxed:
s_j(Schur_i(A)[K,J]) >= s_j(S[K,J])-eps_loc.`                    (4.11)

No bound at all is imposed on `F_KK` or `F_JJ`. In particular, arbitrarily many additional same-bank eigenvalues of either sign and arbitrary magnitude are invisible to this cross certificate.

### Global-op-norm corollary

If simply `||F||op<=delta<|a_tau|`, then all four quantities in (4.7) are at most `delta`. Writing `rho_K=||q_K||`, `rho_J=||q_J||`,

`boxed:
eps_loc <= delta(1+rho_K)(1+rho_J)
                 |a_tau|/(|a_tau|-delta).`                        (4.12)

Thus an arbitrary-rank small signed spectral tail is paid only by one operator-norm threshold, while the arbitrarily large gauge packet is free except for the resulting pivot magnitude.

## 5. Proof of the local identity

The gauge matrix before `F` is

`A_tau=[[a_tau,a_tau q^T],[a_tau q,S+a_tau qq^T]].`               (5.1)

After `F`, the pivot is `a_tau+t`, the pivot-to-rest vector is `a_tau q+z`, and the rest block is `S+a_tau qq^T+W`. Therefore

`Schur_i(A)-S
 =W+a_tau qq^T-(a_tau q+z)(a_tau q+z)^T/(a_tau+t).`               (5.2)

Since

`a_tau q+z=(a_tau+t)q+(z-tq)`,                                    (5.3)

we get

`Schur_i(A)-S
 =W+tqq^T-qz^T-zq^T-(z-tq)(z-tq)^T/(a_tau+t).`                   (5.4)

Taking the `K x J` physical block gives (4.6). The triangle inequality, the bounds

`||r_K||<=dK+d0||q_K||`,
`||r_J||<=dJ+d0||q_J||`,
`|a_tau+t|>=a_*`,                                                  (5.5)

and singular-value Weyl give (4.9)-(4.11). Under `||F||op<=delta`, every compression and off-diagonal block in (4.7) has norm at most `delta`; the first four terms factor as

`delta(1+rho_K)(1+rho_J)`,                                        (5.6)

and the last contributes

`delta^2(1+rho_K)(1+rho_J)/( |a_tau|-delta)`,                     (5.7)

which is (4.12).

## 6. Application of the designated partner result to an actual inequality

The newest completed designated partner `fleet02/B12` result is

`QFORM-RANKONE-SELF-CARRIER-RETENTION-v1`,

canonical source

`yspennstate/math-open-problems@894dfe1e6cc4817c2b3e0bbe46036e4839f10dbf`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T215456Z-fleet02-B12-QFORM-auto11b/REPORT.md`.

At its exact rank-one self endpoint, for an original-coordinate carrier `H` of size `m>=3` and scalar pivot `i in H`, its theorem gives

`boxed: s_2(B#)>=g`,                                               (6.1)

where `B#` is the actual scalar-Schur cross block from `K=H\{i}` to `J=H^c` and `g^2<=lambda_3(C^2+BB^T)` is the physical square-energy carrier gate.

Apply the partner theorem first to a baseline `A0` satisfying that exact endpoint. Put

`Delta0:=g`.                                                       (6.2)

Now add the arbitrary signed Schur-gauge packet `tau gg^T`. By Section 3 the complete scalar Schur remainder, hence `B#`, is unchanged exactly. Add the local tail `F`. By (4.11),

`boxed: s_2(B#_final)>=g-eps_loc.`                                (6.3)

This is the requested actual application of the designated partner result: the partner supplies the nontrivial lower bound `g` on the baseline physical Schur crossing, and the new theorem transports that exact inequality through an unbounded signed spectral packet plus a non-gauge tail.

The scalar-square/rank-two-cross receiver used in the partner proof then gives, whenever `g>eps_loc`,

`boxed:
||p_(X^TAX)||_(infinity,ess)
 <= 2^(11/4) binom(m-1,2)^(1/8)
    /sqrt( a_* (g-eps_loc) ).`                                    (6.4)

This conclusion is dependence-safe: all conditioning and square completion are in original coordinates. No `X^TEX` term is declared small or independent.

## 7. Exact target-class stress family

Use the partner's exact `m=3` stress carrier. Let

`H={1,2,3}`,                                                       (7.1)

`C0=diag(2,0,0)`,                                                  (7.2)

and on two active complement coordinates let

`B0=[[2,0],[0,2],[2,0]]`.                                         (7.3)

The entire complementary symmetric block `D` is arbitrary; it may have any dimension, signs, mixing and eigenvalue magnitudes. Choose pivot `i=1`. Then

`a=2`,                                                             (7.4)
`q_K=0`,                                                           (7.5)
`q_J=(1,0,0,...)`,                                                 (7.6)

so `rho_K=0`, `rho_J=1`.

The baseline three-column carrier has

`g0=s_3(A0[:,H])=sqrt(6-sqrt(20))
   =1.2360679774997896... .`                                      (7.7)

The designated partner exact-rank-one theorem therefore yields

`boxed: s_2(B#)>=g0.`                                              (7.8)

Now set

`gvec=e_1+e_4`                                                     (7.9)

(where coordinate 4 is the first active complement coordinate), and add

`tau gvec gvec^T`, `tau in R`.                                    (7.10)

Its single nonzero eigenvalue is exactly `2 tau`, hence has arbitrary sign and unbounded magnitude. The new pivot is

`a_tau=2+tau`.                                                     (7.11)

Take any further full symmetric dense tail `T` with

`||T||op<=delta:=1/100`.                                           (7.12)

For every `tau` satisfying

`|2+tau|>=2`                                                       (7.13)

(that is, in particular, every `tau>=0` and every `tau<=-4`), the local Schur error obeys

`eps_loc
 <=2 delta |a_tau|/(|a_tau|-delta)
 <=0.020100502512562814... .`                                     (7.14)

Hence the transported partner crossing is

`s_2(B#_final)
 >=g0-eps_loc
 >=1.2159674749872267... .`                                       (7.15)

The final pivot has

`|a_tilde|>=|a_tau|-delta>=1.99`.                                 (7.16)

Since `m=3`, `binom(m-1,2)=1`, and (6.4) gives the explicit full-law bound

`boxed:
||p_Q||_(infinity,ess)
 <= 2^(11/4)/sqrt(1.99*(g0-0.020100502512562814...))
 <=4.324590307685186 .`                                           (7.17)

Thus the same universal constant works simultaneously through an arbitrary complementary spectrum, an unbounded positive or negative rank-one packet that penetrates the pivot and cross block, and a genuinely dense full-rank signed tail of norm `0.01`.

### Verification of the owner's exact three-large-eigenvalue hypothesis

Before the dense tail, the three-column carrier singular values are determined by one orthogonal column of norm `2` and the two-column Gram matrix

`[[2 a_tau^2, 2 a_tau],
  [2 a_tau,     4    ]]`.                                         (7.18)

Its smaller eigenvalue is

`lambda_-(a_tau)=a_tau^2+2-sqrt(a_tau^4+4)`.                      (7.19)

This is increasing in `|a_tau|`; at `|a_tau|=2`,

`sqrt(lambda_-)=sqrt(6-sqrt(20))=g0`.                             (7.20)

Therefore under (7.13),

`s_3(A_tau)>=s_3(A_tau[:,H])>=g0`.                                (7.21)

After the dense tail,

`boxed: s_3(A)>=g0-0.01=1.2260679774997896...>1.`                 (7.22)

So every matrix in this family is literally inside the owner's target class. The arbitrary complementary block `D` cannot hurt (7.21), since restriction to the carrier columns is a contraction on the right and hence `s_3(A)>=s_3(A[:,H])`.

## 8. Why the mechanism is different from earlier B12 stability results

This is not an operator-norm perturbation theorem for the large packet. The gauge addition `tau gg^T` may have norm tending to infinity. It is also not a low-rank reserve argument, a Gram-defect estimate, a polar-positive cone, a commuting eigenvalue replacement, or a carrier-square perturbation. The large packet is free because of an **exact conditional Schur invariance**.

The useful quantity for a general perturbation `E` is therefore its distance to the physical Schur-gauge subspace

`G_i(A0)={tau gg^T: tau in R}`                                    (8.1)

in the scalar case, or

`G_H(A0)={G K G^T: K=K^T}`                                       (8.2)

for a `k`-coordinate pivot. A huge component in this subspace is harmless to the remainder. Only the non-gauge residue needs to be paid, and Section 4 shows that even this payment can be localized to the literal blocks entering the selected Schur crossing.

## 9. Sharp limitation and remaining full-target gap

The exact identity does not make all arbitrary spectral additions free. If the gauge update drives `C+K` through a loss of the local smoothing modes, the corresponding local receiver can fail. In the scalar case `a_tau=0` deletes the pivot coordinate from the completed-square term exactly. A different branch must then supply the missing smoothing.

The full target is therefore still open. Starting only from `s_3(A)>=1`, we have not proved that one can always find an original-coordinate scalar or block pivot for which the large hostile spectral part is close to a Schur-gauge subspace while the surviving Schur crossing satisfies the partner/rank-two receiver; nor have we proved that failure of every such gauge approximation forces one of the already-paid D5, projected-crossing, ridge, physical-pair, grouped-bank/hub, half-Riesz, or Schur alternatives.

A concrete successor implication is:

> prove a product-preserving dichotomy saying that a three-large-eigenvalue matrix either has a quantitatively nondegenerate scalar/block Schur-gauge approximation on some physical pivot, or its non-gauge residue necessarily creates a paid crossing/ridge certificate.

That is a structural implication; this report does not claim it.

## 10. Finite algebra sanity check

A private finite check sampled 10,000 random scalar baselines, arbitrary signed gauge parameters, and random dense symmetric tails. Whenever `|a_tau|>delta`, the observed operator norm of the Schur-remainder change was below the global specialization

`delta(1+||q||)^2 |a_tau|/(|a_tau|-delta)`

in every trial. This is only a check of the algebra/numerics, not evidence for the probability theorem.

## 11. Status

- New theorem: `QFORM-SCHUR-GAUGE-SIGNED-SPECTRUM-STABILITY-v1` — **proved supporting theorem**.
- Designated partner actually applied: fleet02/B12 `QFORM-RANKONE-SELF-CARRIER-RETENTION-v1` at commit `894dfe1e6cc4817c2b3e0bbe46036e4839f10dbf`.
- Concrete target-class consequence: essential density bound `<4.325` for the family in Section 7, uniformly in an unbounded signed gauge eigenvalue and arbitrary complementary spectrum, plus a dense `0.01` tail.
- Continuity: not established by this branch.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Execution context: `WITHOUT_VERIFIED_BRAIN`.
