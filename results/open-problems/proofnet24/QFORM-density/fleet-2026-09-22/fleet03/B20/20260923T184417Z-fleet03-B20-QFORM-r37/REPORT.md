SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-23T18:44:17Z.
attacking: QFORM-TRIANGLE-COMMONPLANE-HEAVY-OR-3FAN-v1 — in the fresh absolute rank-two common-K-plane triangle survivor, convert the common plane into either one literal physical K-coordinate carrying two fixed arms or one three-way partition of K in which all six physical arms remain uniformly rank two; on the same diffuse branch apply fleet04/B20's completed three-bank mass theorem to an actual common-plane direction.

# fleet03/B20 r37 — common-plane heavy-anchor or three-fan compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T184417Z-fleet03-B20-QFORM-r37`.
Role: proof closure and keeper / synthesis.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Status: **NEW TARGET-LEVEL STRUCTURAL COMPILER + ACTUAL FLEET04/B20 APPLICATION / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

## 1. Scope and fresh source graph

The target remains the unrestricted original-coordinate problem: independent real `X_i` with probability densities at most one and a real symmetric `A` with at least three eigenvalues of absolute value at least one. No Gaussianity, log-concavity, moment, support, iid, spectral-coordinate-independence, arbitrary-joint coarea, pointwise quadratic-phase decay, uniformly good physical minor, or deletion of a small random quadratic tail is used.

The immediate source is fleet03/B20 r36, pinned at

`yspennstate/math-open-problems@1fe3d344529b743f64cb37b42a7a12b6a86a9414`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T180245Z-fleet03-B20-QFORM-r36/REPORT.md`.

Its still-unpaid common-plane chamber has three disjoint ORIGINAL-coordinate banks `D_1,D_2,K`. Write

`N_r=A[D_r,K]`, `r=1,2`.

There is one two-dimensional orthogonal projection `Q_*=VV^T` on the physical `K` coefficient space, with `V^T V=I_2`, and

`L_r=N_r Q_*`, `E_r=N_r(I-Q_*)`.

Let `U_r` be an orthonormal basis for the two-dimensional left range of `L_r`, and put

`B_r=U_r^T N_r V`.

The r36 inequalities give

`s_2(B_r) >= beta := 0.01651671529470044`,                       (1.1)

`|det B_r| >= d_0 := 0.0011039951248231808`,                    (1.2)

and, with

`epsilon := 0.0023595307563857772`,                              (1.3)

`||E_1||_F^2+||E_2||_F^2 < epsilon^2`.                           (1.4)

Hence each `||E_r||_op<epsilon`.

The designated partner used at an actual inequality is fleet04/B20 r11, pinned at

`yspennstate/math-open-problems@1fe3d344529b743f64cb37b42a7a12b6a86a9414`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T181642Z-fleet04-B20-QFORM-r11/REPORT.md`.

Its Theorem 2.1 says that for a unit coefficient vector `h`, weights `w_k=h_k^2`, and `eta=max_k w_k<1/3`, a random three-coloring has

`E[W_1W_2W_3]=(1/27)(1-3 sum w_k^2+2 sum w_k^3)
             >=(1-3 eta)/27`,                                   (1.5)

where `W_b` is the squared mass in color `b`. It also records that the normalized scalar projection from each resulting ORIGINAL-coordinate bank has density at most `sqrt(e)` and the three projections are genuinely independent.

## 2. Common-plane leverage

For each physical coordinate `k in K`, define its leverage in the common plane by

`ell_k := ||V^T e_k||_2^2`.                                      (2.1)

Since `V^T V=I_2`,

`0<=ell_k<=1`, `sum_(k in K) ell_k=2`.                           (2.2)

The new split uses the fixed threshold

`eta_0=1/16`.                                                     (2.3)

### Theorem 2.1 — `QFORM-TRIANGLE-COMMONPLANE-HEAVY-OR-3FAN-v1`

Under (1.1)-(1.4), at least one of the following holds.

**A. Common physical two-arm anchor.** There is one ORIGINAL coordinate `k in K` such that simultaneously for `r=1,2`,

`||N_r e_k||_2 > a_H`,                                           (2.4)

where

`a_H := beta/4-epsilon
     =0.0017696480672893325...`.                                 (2.5)

Thus one literal `K` coordinate carries squared cross energy greater than

`a_H^2=3.13165428206087e-6`                                     (2.6)

into each of the two disjoint banks `D_1,D_2`.

**B. Three-fan diffuse packet.** There is one partition into three disjoint ORIGINAL-coordinate banks

`K=K_1 disjoint_union K_2 disjoint_union K_3`                    (2.7)

such that, with

`G_b:=V^T P_(K_b)V`,                                              (2.8)

one has for every `b=1,2,3`

`G_b >= (1/12) I_2`.                                             (2.9)

For every `r=1,2` and every `b=1,2,3`, the literal physical cross block from `D_r` to `K_b` then satisfies

`s_2(A[D_r,K_b]) > a_D`,                                         (2.10)

where

`a_D := beta/sqrt(12)-epsilon
     =0.002408434254376076...`,                                  (2.11)

and consequently

`s_1(A[D_r,K_b])s_2(A[D_r,K_b])
 > a_D^2
 =5.800555557652045e-6`.                                        (2.12)

Moreover the same partition can be chosen so that for any preselected unit `a in R^2`, writing `h=Va` and

`W_b=sum_(k in K_b) h_k^2=a^T G_b a`,                            (2.13)

one also has

`W_1W_2W_3 >= 1/100`.                                           (2.14)

For `H_b=sum_(k in K_b) h_k X_k`, the three `H_b` are therefore independent and their genuine joint density obeys

`||p_(H_1,H_2,H_3)||_infinity
 <= e^(3/2)/sqrt(W_1W_2W_3)
 <= 10 e^(3/2)
 <44.817`.                                                       (2.15)

No post-rotation independence is asserted: the independence in (2.15) comes only from the disjoint ORIGINAL source banks.

## 3. Proof: heavy leverage gives one common physical anchor

Suppose first that `ell_k>=1/16` for some `k`. Let

`q_k=V^T e_k`, so `||q_k||=sqrt(ell_k)>=1/4`.                    (3.1)

The projected `U_r` component of the actual physical column is

`U_r^T N_r e_k
 =B_r q_k + U_r^T E_r e_k`.                                     (3.2)

By (1.1),

`||B_r q_k||_2 >= beta ||q_k||_2 >= beta/4`,                    (3.3)

while (1.4) gives

`||U_r^T E_r e_k||_2 <=||E_r||_op<epsilon`.                     (3.4)

Therefore

`||N_r e_k||_2
 >=||U_r^T N_r e_k||_2
 >beta/4-epsilon=a_H`,                                          (3.5)

simultaneously for `r=1,2`. This proves Alternative A. Notice that the off-plane tail is retained and explicitly paid against the main column; it is not deleted from the random quadratic form.

## 4. Proof: diffuse common plane admits one three-way matrix-balanced physical partition

Assume now

`ell_k<1/16` for every `k in K`.                                 (4.1)

Color the coordinates of `K` independently and uniformly with three colors. For a fixed color `b`, set

`Y_k=1_{color(k)=b} q_k q_k^T`, `q_k=V^T e_k`.                   (4.2)

Then

`0<=Y_k<=(1/16)I_2`,

and

`E sum_k Y_k=(1/3)sum_k q_kq_k^T=(1/3)I_2`.                    (4.3)

Use the standard lower-tail matrix Chernoff inequality: for independent positive semidefinite `2 x 2` matrices bounded by `R I`, if `mu=lambda_min(E sum Y_k)`, then

`P{lambda_min(sum Y_k)<=(1-delta)mu}
 <=2 [e^(-delta)/(1-delta)^(1-delta)]^(mu/R)`.                  (4.4)

Here `R=1/16`, `mu=1/3`, and choose `delta=3/4`. Thus for one color

`P{lambda_min(G_b)<1/12}
 <=2 [e^(-3/4)/(1/4)^(1/4)]^(16/3).                             (4.5)

By the union bound over the three colors,

`P{some b has lambda_min(G_b)<1/12}
 <=6 [e^(-3/4)/(1/4)^(1/4)]^(16/3)
 =0.697782346546711... <1`.                                    (4.6)

Hence a matrix-balanced three-coloring exists. The next section shows that one can impose the partner scalar-product condition simultaneously, not on a different partition.

## 5. Actual fleet04/B20 application and simultaneous source-provenance gate

Fix any unit vector `a in R^2`; for later use one may take a weakest right singular direction of `B_1`. Put

`h=Va`, `w_k=h_k^2`.                                             (5.1)

Then `sum w_k=1` and, by (4.1),

`eta=max_k w_k <= max_k ell_k <1/16`.                           (5.2)

Apply fleet04/B20 r11 Theorem 2.1 to these exact weights. For the same random three-coloring used in Section 4,

`E[W_1W_2W_3] >(1-3/16)/27=13/432`.                            (5.3)

Also `W_1+W_2+W_3=1`, hence always

`0<=W_1W_2W_3<=1/27`.                                          (5.4)

Let `E_s` be the event `W_1W_2W_3>=1/100`. From (5.3)-(5.4),

`13/432
 < E[W_1W_2W_3]
 <= (1/100)P(E_s^c)+(1/27)P(E_s)`,                              (5.5)

so

`P(E_s) > (13/432-1/100)/(1/27-1/100)
        =217/292
        =0.7431506849...`.                                      (5.6)

Let `E_m` be the matrix-balanced event (2.9). Equation (4.6) gives

`P(E_m)>1-0.6977823466=0.3022176534...`.                        (5.7)

Therefore

`P(E_m intersect E_s)
 >=P(E_m)+P(E_s)-1
 >0.0453683383...>0`.                                           (5.8)

So one deterministic ORIGINAL-coordinate partition satisfies both (2.9) and (2.14).

For that partition, fleet04/B20's source-projection conclusion applies to the three disjoint banks: `Y_b=H_b/sqrt(W_b)` have density at most `sqrt(e)` and are mutually independent. Rescaling gives (2.15). This is an equation-level use of the designated partner result in the live r36 common-plane geometry.

## 6. All six physical arms remain uniformly rank two on that same partition

Fix the partition supplied by (5.8). For each `r,b`, project the physical block `N_r[:,K_b]` onto the left range `U_r`:

`U_r^T N_r P_(K_b)
 = B_r V^T P_(K_b)+U_r^T E_r P_(K_b)`.                          (6.1)

The main term has Gram matrix

`B_r G_b B_r^T`.                                                (6.2)

By (1.1) and (2.9),

`s_2(B_r V^T P_(K_b))
 >=s_2(B_r) sqrt(lambda_min(G_b))
 >=beta/sqrt(12).`                                              (6.3)

The retained tail obeys

`||U_r^T E_r P_(K_b)||_op<=||E_r||_op<epsilon`.                 (6.4)

Weyl's singular-value inequality therefore gives

`s_2(U_r^T N_r P_(K_b))
 > beta/sqrt(12)-epsilon
 =a_D`.                                                         (6.5)

Left orthogonal projection cannot increase singular values, so the actual physical block has

`s_2(N_r[:,K_b])>=s_2(U_r^T N_r P_(K_b))>a_D`,                 (6.6)

which proves (2.10). Since `s_1>=s_2`, (2.12) follows.

Thus the previous one-common-plane label has been converted into product-source geometry: either a single literal K coordinate sends two fixed arms into the two disjoint leaf banks, or K itself splits into three independent physical banks and every one of the six resulting arms is a quantitatively rank-two ORIGINAL-coordinate cross block.

## 7. What this pays and what remains

This theorem does not claim that a bounded joint projection density controls the curved pushforward. It supplies the missing product provenance needed for a receiver: three independent K source banks, a genuine scalar three-bank cap (2.15), and six fixed rank-two physical arms (2.12), all on one partition and with the r36 off-plane tails retained exactly.

The first unpaid implication in this chamber is now

`QFORM-TRIANGLE-3FAN-OR-COMMON-K-ANCHOR-PAYMENT-v1`:

* heavy branch: pay one physical K coordinate with two cross-arm norms `>a_H`, together with the retained D1-D2 edge and arbitrary same-bank phases;
* diffuse branch: use the same three K banks from (2.7), each carrying rank-two arms of singular product `>5.8005e-6`, together with the independent scalar certificate (2.15), to invoke or prove a product-safe grouped receiver while retaining all same-bank quadratic blocks, outside couplings, signs, affine terms, fragmented/unbounded cap-one laws and extra spectrum.

The completed arbitrary-rank projected-crossing theorem remains available whenever one of these physical fan cuts has a nonzero projected crossing volume with acceptable row marginals. The aligned endpoint, where those projected volumes collapse into the already exposed fan directions, remains the analytic debt.

## 8. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report proves a new quantitative structural implication in the current full-target graph; it is not a full solution. Full-target continuity remains open. No new continuity conclusion is claimed for the structural survivor; continuity remains only on previously completed paid branches whose source theorems explicitly provide it.

Repository transport and native learned-memory ingestion are distinct. This run remains `WITHOUT_VERIFIED_BRAIN`: authenticated repository reads/writes were used, but no native learned-memory receiver ingestion was exposed or verified.
