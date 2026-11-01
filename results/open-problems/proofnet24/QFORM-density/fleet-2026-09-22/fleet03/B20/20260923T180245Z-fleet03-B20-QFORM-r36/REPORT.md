SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-23T18:02:45Z.
attacking: QFORM-TRIANGLE-COMBINED-R2-TUBE-v1 — in the fresh three-bank triangle survivor, use the whole literal K-to-(D1 union D2) cross block to either pay fifth/third volume or force both rank-two legs onto one common K-plane with an explicit absolute Frobenius tail.

# fleet03/B20 r36 — combined-leg rank-two tube compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T180245Z-fleet03-B20-QFORM-r36`.
Role: proof closure and keeper / SYNTHESIS.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Status: **NEW TARGET-LEVEL STRUCTURAL COMPILER + ACTUAL PARTNER PAYMENT / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

I acknowledge owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. The unrestricted target remains the exact cap-one independent-coordinate problem. No Gaussianity, log-concavity, moments, compact/connected support, spectral-coordinate independence, arbitrary-joint coarea, pointwise quadratic-phase decay, uniformly good physical minor, conditional-density cap substitution, or deletion of a small matrix tail is used.

## 1. Fresh source graph


The immediate fresh assembly input is fleet03/B19:

`yspennstate/math-open-problems@afbdba9c6b0624552a6725568d3eb883b999d1e1`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T170040Z-fleet03-B19-qform-r37/REPORT.md`.

Its predecessor quantitative triangle packet gives disjoint ORIGINAL-coordinate banks `D_1,D_2,K` and

`C=A[D_1,D_2]`, `N_1=A[D_1,K]`, `N_2=A[D_2,K]`,

with the fixed constants

`F=0.4537176735697731005/8
  =0.05671470919622164...`,                                      (1.1)

`Delta=0.0014419528160955833...`,                                (1.2)

`sigma_*^2=0.000356312664981148...`,                             (1.3)

such that, for `r=1,2`,

`s_1(N_r)s_2(N_r)>=Delta`,                                       (1.4)

`s_2(N_r)^2>=sigma_*^2`.                                         (1.5)

Writing `P_r` for the top-two left singular projection of `N_r`, its aligned survivor also has

`||P_1 C P_2||_F >= (3/4)||C||_F`,                              (1.6)

and `||C||_F^2>=F`.                                               (1.7)

The newest B19 report then forms the literal physical cross block

`M_K=[N_1^T,N_2^T]`,                                             (1.8)

with rows on the ORIGINAL bank `K` and columns on the disjoint ORIGINAL bank `D_1 union D_2`, and

`Z_K=e_3(M_KM_K^T)`.                                             (1.9)

It proves a D3 payment/anchor/common-plane trichotomy at

`Z_0=1.1575863166387214e-11`.                                    (1.10)

The designated fleet04/B20 theorem actually applied in this run is

`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T142031Z-fleet04-B20-QFORM-r10/REPORT.md`.

For any literal ORIGINAL-coordinate cross block `M`, if

`E=||M||_F^2`, `S_4=sum_(j<=4)s_j(M)^2`,                         (1.11)

and `S_4<=(1-delta)E`, then its fifth-volume compiler gives

`e_5(M^TM)>=delta^4 E^5/120`,                                    (1.12)

and the ambient density bound

`||p_Q||_infinity <=5 sqrt(2e) e_5(M^TM)^(-1/10)`.               (1.13)

This theorem retains arbitrary same-bank blocks, outside couplings, affine terms, signs and additional spectrum. I use it only on the literal block (1.8).

## 2. First payment: the combined two-leg block already has fixed energy

Let the singular values of `M_K` be

`mu_1>=mu_2>=...>=0`.                                             (2.1)

Since

`||N_r||_F^2>=s_1(N_r)^2+s_2(N_r)^2
             >=2s_1(N_r)s_2(N_r)>=2Delta`,                       (2.2)

we get

`boxed: E_K:=||M_K||_F^2
       =||N_1||_F^2+||N_2||_F^2
       >=4Delta
       =0.005767811264382333... .}`                              (2.3)

Apply fleet04/B20 r10 with `delta=1/64`. If

`sum_(j<=4)mu_j^2 <=(63/64)E_K`,                                 (2.4)

then

`e_5(M_K^TM_K)
 >=(1/64)^4(4Delta)^5/120`,                                      (2.5)

and (1.13) gives the explicit full-law payment

`boxed: ||p_Q||_infinity <1307.727.}`                             (2.6)

This is the required equation-level application of the designated partner theorem. I record (2.6) as an essentially bounded-density payment; I do not add a continuity conclusion here beyond the source theorem actually checked.

Hence any state surviving this new partner exit has

`sum_(j<=4)mu_j^2 >(63/64)E_K`.                                  (2.7)

## 3. New key theorem: low combined third volume forces an absolute rank-two tube

### Theorem 3.1 — `QFORM-TRIANGLE-COMBINED-R2-TUBE-v1`

Under (1.4)-(1.5), define `M_K` and `Z_K` by (1.8)-(1.9). Then

`boxed: sum_(j>=3)mu_j^2 <= Z_K/Delta^2.}`                        (3.1)

Consequently, on the B19 low-third-volume survivor `Z_K<Z_0`,

`boxed: sum_(j>=3)mu_j^2
       < Z_0/Delta^2
       =sigma_*^2/64
       =5.567385390330438e-6,}`                                  (3.2)

and therefore there is one two-dimensional subspace `Q_*` of the physical `K` coefficient space for which

`boxed: ||(I-Q_*)M_K||_F
       <sigma_*/8
       =0.0023595307563857772... .}`                             (3.3)

#### Proof

The combined Gram matrix is

`M_KM_K^T=N_1^TN_1+N_2^TN_2 >= N_r^TN_r`                        (3.4)

in positive-semidefinite order for either `r`. Hence eigenvalue monotonicity gives

`mu_1mu_2>=s_1(N_r)s_2(N_r)>=Delta`.                             (3.5)

Now

`Z_K=e_3(M_KM_K^T)
    =sum_(i<j<k)mu_i^2mu_j^2mu_k^2
    >=mu_1^2mu_2^2 sum_(k>=3)mu_k^2
    >=Delta^2 sum_(k>=3)mu_k^2`,                                 (3.6)

which proves (3.1). Substituting the live B19 threshold

`Z_0=Delta^2 sigma_*^2/64`                                       (3.7)

gives (3.2). Let `Q_*` be the top-two left singular projection of `M_K`; then (3.3) is exactly the square root of (3.2). QED.

This is stronger than merely saying the two K-side top singular planes are close: the entire physical combined block has a dimension-free absolute Frobenius tail below `0.00236` after one common K-plane is chosen.

## 4. Both legs remain quantitatively invertible on that single common K-plane

Put

`L_r=N_r Q_*`, `E_r=N_r(I-Q_*)`, `r=1,2`.                        (4.1)

Equation (3.3) gives the simultaneous tail budget

`boxed: ||E_1||_F^2+||E_2||_F^2<sigma_*^2/64.}`                  (4.2)

In particular

`||E_r||_op<sigma_*/8`.                                          (4.3)

Weyl's singular-value perturbation inequality and (1.5) imply, for `j=1,2`,

`s_j(L_r)>=s_j(N_r)-sigma_*/8
          >=(7/8)s_j(N_r)`.                                      (4.4)

Therefore each compressed physical leg has exact rank two and

`boxed: s_2(L_r) >=7sigma_*/8
       =0.01651671529470044... ,}`                               (4.5)

`boxed: s_1(L_r)s_2(L_r)
       >=(49/64)Delta
       =0.0011039951248231808... .}`                             (4.6)

No tail is discarded from the random quadratic form; (4.2) is a deterministic structural certificate only.

## 5. Transfer the self edge to the new common-plane legs

Let `\widetilde P_r` be the orthogonal projection onto the two-dimensional left range of `L_r`.

### Lemma 5.1 — subspace transfer

`boxed: ||P_r-\widetilde P_r||_op<1/8.}`                          (5.1)

Proof. Let `U_r Sigma_r V_r^T` denote the top-two SVD block of `N_r`; thus `P_r=U_rU_r^T`. Because `(I-\widetilde P_r)L_r=0`,

`(I-\widetilde P_r)U_r Sigma_r
 =(I-\widetilde P_r)N_rV_r
 =(I-\widetilde P_r)E_rV_r`.                                     (5.2)

Hence

`||(I-\widetilde P_r)U_r||_op
 <=||E_r||_op/s_2(N_r)<1/8`.                                     (5.3)

Both projections have rank two, so their operator-norm distance is the maximal sine of their principal angles and equals the left side of (5.3). QED.

Using (1.6), (5.1), and the identity

`\widetilde P_1 C\widetilde P_2-P_1CP_2
 =(\widetilde P_1-P_1)CP_2
  +\widetilde P_1C(\widetilde P_2-P_2)`,                          (5.4)

we get

`||\widetilde P_1 C\widetilde P_2||_F
 >=||P_1CP_2||_F
   -||P_1-\widetilde P_1||_op||C||_F
   -||P_2-\widetilde P_2||_op||C||_F
 >(3/4-1/8-1/8)||C||_F
 =(1/2)||C||_F`.                                                  (5.5)

Thus the actual self edge in the exact common-plane skeleton obeys

`boxed: ||\widetilde P_1 C\widetilde P_2||_F^2
       >F/4
       =0.01417867729905541... ,}`                               (5.6)

or equivalently

`boxed: ||\widetilde P_1 C\widetilde P_2||_F
       >0.11907425120090158... .}`                               (5.7)

The self edge is not asserted invertible; rank one remains possible. What has been proved is that both K legs are uniformly invertible in the same two-dimensional K-plane while a nontrivial in-plane D1-D2 edge survives.

## 6. Updated exhaustive local compiler

For the fresh robust three-bank triangle packet, the combined literal block `M_K=[N_1^T,N_2^T]` now routes as follows.

1. If its top-four energy is not concentrated, fleet04/B20 r10 pays the full density by (2.6): `<1307.727`.
2. If `Z_K>=Z_0`, the already-completed B19 D3 theorem either pays the full law continuously by `<657.718` under its row-volume marginal gate, or produces a literal physical K-row third-volume anchor carrying more than `Z_0/2=5.787931583193607e-12`.
3. If `Z_K<Z_0`, Sections 3-5 force one exact common two-dimensional K-plane `Q_*`, two exact rank-two main legs with (4.5)-(4.6), a self-edge with (5.6)-(5.7), and a retained combined off-plane tail obeying (4.2).

Thus the formerly qualitative/common-principal-angle survivor is now an **absolute rank-two physical combined-leg tube** around one quantitative `2+2+2` main cycle.

## 7. First remaining implication

The first unpaid implication in this chamber is now

`QFORM-TRIANGLE-ABS-RANK2-WITH-ARBITRARY-SAMEBANK-PAYMENT-v1`:

pay the exact grouped `2+2+2` main cycle with

`det-size(N-leg) >=0.0011039951248231808`,
`s_2(N-leg)>=0.01651671529470044`,
`self-edge Frobenius >0.11907425120090158`,                       (7.1)

while retaining simultaneously

`||E_1||_F^2+||E_2||_F^2<5.567385390330438e-6`                   (7.2)

and **arbitrary same-bank quadratic phases, outside couplings, signs, affine terms, fragmented/unbounded cap-one input laws and extra spectrum**.

A small coefficient tail is not a small random quadratic error without moment assumptions, so (7.2) may not be dropped perturbatively. The newest projected-crossing theorem can pay a transverse projected remainder when its actual volume and row-marginal gates fire, but the aligned/small-projected-crossing endpoint remains the analytic debt.

## 8. Status

This report proves a quantitatively stated supporting implication in the current full-target graph and applies the designated partner at an actual original-coordinate inequality. It is **not** a full solution.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The full-target continuous-density conclusion also remains **OPEN**. Continuity is inherited only on the already completed D3-paid branch explicitly cited above; no continuity conclusion is claimed for the new structural survivor, and the partner D5 payment is recorded here only at the bounded-density level actually needed.

Repository transport and native learned-memory ingestion remain separate. This run is `WITHOUT_VERIFIED_BRAIN` because authenticated repository reads/writes occurred but no native learned-memory receiver use was exposed or verified.
