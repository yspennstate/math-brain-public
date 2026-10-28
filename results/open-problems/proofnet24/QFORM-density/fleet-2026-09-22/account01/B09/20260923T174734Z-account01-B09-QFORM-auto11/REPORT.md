SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T17:47:34Z.
attacking: fixed-pair anchored fourth volume via the arbitrary-rank projected-crossing theorem and an ORIGINAL-coordinate hub-concentration cascade.

# account01/B09 — fixed physical pair: aggregate fourth volume pays arbitrary leaf curvature

## Status

**ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN.**

This run proves `QFORM-FIXEDPAIR-AGGREGATE-FOURVOLUME-v1`. A fixed literal physical pair whose anchored disjoint physical 4-volume is positive already gives a continuous bounded density with a direct linear interval estimate. The theorem retains the entire physical pair core and all same-side curvature. It uses the new arbitrary-rank projected-crossing estimate at two exact equations and closes its row-marginal failures by promoting actual ORIGINAL coordinates, never spectral coordinates.

The unrestricted owner target remains **OPEN / not proved / not disproved**. Full-target continuity also remains open.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source-pinned premises

### 1.1 Current programme state


The live corrections used here include: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no arbitrary-joint rank-three coarea cap; no worst conditional projection-density moment; no deletion of a small nonzero quadratic coefficient as a small random error; and no assumption that the three-large-eigenvalue hypothesis forces one uniformly good physical minor.

### 1.2 New arbitrary-rank projected crossing theorem

The owner-provided, independently checked source is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

I use two specializations of its grouped-hub theorem. If there are `k` literal hub coordinates, a literal light split `I disjoint J`, hub-to-`J` matrix `M_J` with singular-value product `S`, and projected crossing

`C=A[I,J](I-Pi_row(M_J))`,

put `Z_ell=e_ell(CC^T)`. If the canonical `ell`-volume row marginals are at most `1/2`, `d=k+ell>2`, and the hubs are exactly the `k` ORIGINAL coordinates (joint density cap one), then

`||p_Q||_infinity
 <= d/(d-2) 2^((k+3ell)/(2d)) exp(ell/(2d))
    S^(-1/d) Z_ell^(-1/(2d))`,                                    (1.1)

with the exponential factor omitted for `ell=1`. Arbitrary internal hub functions, same-side light curvature, diagonals, affine terms and outside terms are retained. Its Fourier envelope is integrable, hence the density is continuous and the same coefficient multiplies interval length.

The same source's exact-rank crossing theorem says that a physical rank-`r>2` cross block with singular-value product `s_1...s_r`, one side consisting of exactly `r` ORIGINAL coordinates, satisfies

`||p_Q||_infinity
 <= r/(r-2) (2^(r/2)/(s_1...s_r))^(1/r)`.                         (1.2)

For `r=4` this is `2 sqrt(2)(s_1s_2s_3s_4)^(-1/4)`, again with continuity.

### 1.3 Designated partner account02/B09

The completed partner report is

`yspennstate/math-open-problems@c27ff5b752bf25d2933cbdfac5a870b0dcf71181`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T154445Z-account02-B09-QFORM-r15/REPORT.md`,

with its same-run `CORRECTION.md`. Its theorem `QFORM-TWOHUB-MIXEDFRAME-UNIFORMCORE-v1` gives, for two literal hubs and a leaf block

`D + sum_{q=1}^r lambda_q v_q v_q^T`,

mixed row frame `rho_i=((v_q)_i,A_ia,A_ib)`, Gram `G>0`, and normalized row leverages at most `1/2`,

`||p_Q||_infinity
 <= C_r [det(G) product_q |lambda_q|]^(-1/(r+4)),
 C_r=4(r+4)/(r+2) 2^(-4/(r+4)).`                                  (1.3)

The density is continuous. I apply (1.3) to an actual target-valid family in Section 7.

## 2. Fixed-pair anchored fourth-volume currency

Fix two distinct literal ORIGINAL coordinates

`H={a,b}`

and put `L=H^c`. For an unordered two-set `S subset L` and a four-set `T subset L\S`, define the genuine disjoint physical minor

`m(S,T)=det A[H union S,T]`.

Define

`boxed:
 U_H := sum_{S subset L, |S|=2}
        sum_{T subset L\S, |T|=4} m(S,T)^2.`                       (2.1)

This is the fixed-pair anchored disjoint physical fourth volume. Under `A -> sA`, `U_H -> |s|^8 U_H`, so `U_H^(-1/8)` has exactly the scaling of a one-dimensional density.

The theorem below concerns `U_H>0`. It makes no assertion at `U_H=0`.

## 3. Exact pair-to-projected-two-volume identity

Take any literal partition

`L=I disjoint_union J`.

Write

`M=A[H,J]`,
`Delta=det(M M^T)`,
`Pi=orthogonal projection onto row(M)`,
`C=A[I,J](I-Pi)`.                                                   (3.1)

For each two-set `S subset I`, let `C_S` be the corresponding two rows.

### Lemma 3.1

If `M` has row rank two, then

`boxed:
 Delta det(C_S C_S^T)
 =sum_{T subset J, |T|=4} det A[H union S,T]^2.`                    (3.2)

Consequently

`boxed:
 W(I,J):=Delta e_2(CC^T)
 =sum_{S subset I, |S|=2}
   sum_{T subset J, |T|=4} det A[H union S,T]^2.`                   (3.3)

If the right side is positive, rank two of `M` is automatic.

#### Proof

Form the `4 x |J|` row matrix

`R_S=[M; A[S,J]]`.

Subtracting from the last two rows their orthogonal projections onto `row(M)` does not change the row-volume. The Gram determinant factors orthogonally:

`det(R_S R_S^T)=det(MM^T) det(C_S C_S^T).`                          (3.4)

Cauchy--Binet gives

`det(R_S R_S^T)
 =sum_{|T|=4} det(R_S[:,T])^2
 =sum_{|T|=4} det A[H union S,T]^2.`                                (3.5)

This proves (3.2), and summing over `S` gives (3.3). If `M` had rank at most one, `R_S` would have rank at most three for every `S`, making the right side zero. QED.

## 4. Random literal split and first marginal gate

Put each coordinate of `L` independently into `J` with probability `p` and into `I` with probability `1-p`. Each term of (2.1) appears in (3.3) exactly when its two row labels lie in `I` and its four column labels lie in `J`. Since all six labels are distinct,

`E W(I,J)=(1-p)^2 p^4 U_H.`                                        (4.1)

The maximum occurs at `p=2/3`, with

`boxed: c_0=(1/3)^2(2/3)^4=16/729.`                                (4.2)

Hence some literal split has

`W>=c_0 U_H.`                                                       (4.3)

For every leaf `i in L`, define its one-row anchored share

`U_i := sum_{j in L\{i}}
       sum_{T subset L\{i,j}, |T|=4}
       det A[H union {i,j},T]^2.`                                  (4.4)

Every row-pair term is counted twice, so `sum_i U_i=2U_H`.

### Case A: diffuse pair-anchored fourth volume

Assume

`U_i <= (c_0/2) U_H = (8/729)U_H` for every `i`.                   (4.5)

Choose a split satisfying (4.3). For `i in I`, its selected projected two-volume share is

`w_i := Delta sum_{j in I\{i}} det(C_{i,j}C_{i,j}^T).`             (4.6)

By (3.2), `w_i` is a sub-sum of `U_i`, so

`w_i<=U_i<=c_0U_H/2<=W/2.`                                        (4.7)

Therefore every canonical `ell=2` volume row marginal is at most `1/2`.

Apply (1.1) with `k=2`, `ell=2`, `d=4`. Since `S=s_1(M)s_2(M)=sqrt(Delta)` and `Z_2=e_2(CC^T)`,

`S^2 Z_2=W`.

Thus

`||p_Q||_infinity
 <=4 e^(1/4) W^(-1/8)
 <=4 e^(1/4)(729/16)^(1/8) U_H^(-1/8).`                            (4.8)

The exact normalized constant is

`C_A=2 sqrt(2) e^(1/4) 3^(3/4)
    =8.2786506268... .`                                            (4.9)

This branch has a continuous density and direct linear interval bound.

## 5. First concentration: promote one literal leaf to a third hub

Otherwise choose a literal leaf `i` with

`U_i>(8/729)U_H.`                                                   (5.1)

Promote **that same ORIGINAL coordinate** to the three-hub set

`H_i=H union {i}`.

For each remaining literal leaf `j`, define

`U_{ij}:=
 sum_{T subset L\{i,j}, |T|=4}
 det A[H union {i,j},T]^2.`                                        (5.2)

Then

`sum_{j != i} U_{ij}=U_i.`                                         (5.3)

Partition `L\{i}=I disjoint_union J`, putting a coordinate into `J` with probability `p`. Let

`M_3=A[H_i,J]`,
`Delta_3=det(M_3M_3^T)`,
`C_3=A[I,J](I-Pi_row(M_3)).`                                      (5.4)

The same Gram-Schur/Cauchy--Binet argument, now with three hub rows and one leaf row, gives

`boxed:
 Delta_3 ||(C_3)_j||^2
 =sum_{T subset J, |T|=4}
   det A[H_i union {j},T]^2.`                                     (5.5)

Hence

`W_3:=Delta_3 e_1(C_3C_3^T)`                                      (5.6)

has expectation

`E W_3=(1-p)p^4 U_i.`                                              (5.7)

This is maximized at `p=4/5`, with

`boxed: c_1=(1/5)(4/5)^4=256/3125.`                               (5.8)

Therefore some literal split satisfies

`W_3>=c_1 U_i.`                                                     (5.9)

### Case B: diffuse after one promotion

If

`U_{ij}<=(c_1/2)U_i=(128/3125)U_i` for every `j`,                 (5.10)

then every selected `ell=1` row marginal is at most `1/2`, by exactly the same sub-sum argument as (4.7). Apply (1.1) with `k=3`, `ell=1`, `d=4`; the `ell=1` exponential factor is absent. Since `S_3^2 Z_1=W_3`,

`||p_Q||_infinity
 <=2^(7/4) W_3^(-1/8)
 <=2^(7/4)c_1^(-1/8)(8/729)^(-1/8)U_H^(-1/8).`                    (5.11)

Thus

`C_B=2^(3/8)3^(3/4)5^(5/8)
    =8.0832021885... .`                                            (5.12)

Again the density is continuous and the interval estimate is linear.

## 6. Second concentration: four literal hubs close the chain

If (5.10) fails, choose a literal `j` such that

`U_{ij}>(128/3125)U_i
       >(128/3125)(8/729)U_H.`                                    (6.1)

Promote `j` as well and set

`H_4=H union {i,j}`.

Let

`B=A[H_4,L\{i,j}]`                                                (6.2)

be the literal four-row physical cross block. Cauchy--Binet is exact:

`boxed:
 det(BB^T)
 =sum_{T subset L\{i,j}, |T|=4}
   det A[H_4,T]^2
 =U_{ij}.`                                                         (6.3)

Thus `B` has rank four and, if its singular values are `s_1,...,s_4`,

`s_1s_2s_3s_4=sqrt(U_{ij}).`                                       (6.4)

Apply the exact rank-four crossing theorem (1.2), with the four-hub side consisting of exactly four independent ORIGINAL coordinates. The hub projection density cap is one; the opposite rank-four projection has the standard product-projection cap `2^(4/2)=4`. Therefore

`||p_Q||_infinity
 <=2 sqrt(2) U_{ij}^(-1/8)`                                       (6.5)

and hence, using (6.1),

`||p_Q||_infinity
 <2 sqrt(2)[(8/729)(128/3125)]^(-1/8) U_H^(-1/8).`                 (6.6)

The normalized constant is

`C_C=2^(1/4)3^(3/4)5^(5/8)
    =7.4123290889... .`                                            (6.7)

The rank-four Fourier envelope is integrable, so this branch also has a continuous density.

## 7. Main theorem

### Theorem `QFORM-FIXEDPAIR-AGGREGATE-FOURVOLUME-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities at most one. Let

`Q=X^TAX+b^TX+c`

for any real symmetric `A`, arbitrary affine terms, and fix any two literal ORIGINAL coordinates `H={a,b}`. Define `U_H` by (2.1).

If `U_H>0`, then `Q` has a **continuous density** and

`boxed:
 ||p_Q||_infinity
 <= C_4 U_H^(-1/8),
 C_4=2 sqrt(2)e^(1/4)3^(3/4)
 <8.279.`                                                          (7.1)

Consequently, for every interval `B`,

`boxed:
 P{Q in B}<8.279 U_H^(-1/8)|B|.`                                  (7.2)

The estimate is uniform in the entire physical `2x2` hub core, all same-side leaf curvature, all signs, all additional spectrum and all affine terms. There is no square-root small-ball conversion and no rotation of the random variables.

#### Proof

Cases A, B and C above are exhaustive. Their constants are respectively

`8.2786506268...`, `8.0832021885...`, `7.4123290889...`,

so the Case-A constant dominates. QED.

### What this adds beyond the preceding fixed-pair three-volume theorem

The previous B09 theorem paid the fixed-pair anchored physical **third** volume with exponent `-1/6`. The present theorem spends a genuinely different higher exterior currency: two extra physical leaf rows against four disjoint physical columns, with exponent `-1/8`. It is useful when a pair's third-volume certificate is quantitatively poor but a four-dimensional transverse crossing packet is not. The entire same-side curvature remains inside the projected-crossing receiver.

This does **not** prove that the bare condition `sigma_3(A)>=1` forces one pair with `U_H` bounded below by a universal constant. That remains an upstream structural obligation.

## 8. Required actual application of account02/B09 r15

Take disjoint original-coordinate banks `S,T` with

`|S|=|T|=m=2^k>=8`.

Choose two flat orthonormal Walsh vectors `u_1,u_2` on `S` and four flat orthonormal Walsh vectors `c_1,c_2,q_1,q_2` on `T`. Let `a,b` be two additional literal physical coordinates and define

`Q_m =
 2X_a <c_1,X_T>
 +2X_b <c_2,X_T>
 +2<u_1,X_S><q_1,X_T>
 +2<u_2,X_S><q_2,X_T>.`                                           (8.1)

### 8.1 Exact target spectrum

Across the literal bipartition `(a,b,S) | T`, the cross block maps the four orthonormal right vectors

`c_1,c_2,q_1,q_2`

to the four orthonormal left vectors

`e_a,e_b,u_1,u_2`.

Hence its four nonzero singular values are all one, and the symmetric coefficient matrix of (8.1) has nonzero spectrum

`{+1,+1,+1,+1,-1,-1,-1,-1}.`                                      (8.2)

Thus (8.1) satisfies the owner's three-large-eigenvalue hypothesis.

### 8.2 The new anchored-four-volume theorem applies

Fix `H={a,b}`. Restrict the row-pair sum in `U_H` to pairs `{i,j} subset S` and the column sets to `T`. Cauchy--Binet gives

`sum_{|T_0|=4} det A[H union {i,j},T_0]^2
 =(u_{1i}u_{2j}-u_{2i}u_{1j})^2.`                                 (8.3)

Summing over `i<j` and using Cauchy--Binet again for the orthonormal pair `(u_1,u_2)` gives exactly one. Therefore

`U_H>=1.`                                                          (8.4)

The new theorem gives the direct uniform bound

`||p_{Q_m}||_infinity<8.279.`                                      (8.5)

### 8.3 Designated partner r15 gives a sharper actual inequality on the same family

The leaf block on `S union T` has four orthonormal eigenvectors

`v_1=(u_1,q_1)/sqrt(2), lambda_1=+1`,
`v_2=(u_1,-q_1)/sqrt(2), lambda_2=-1`,
`v_3=(u_2,q_2)/sqrt(2), lambda_3=+1`,
`v_4=(u_2,-q_2)/sqrt(2), lambda_4=-1`.                              (8.6)

Together with the two hub-star columns `c_1,c_2`, these six mixed-frame columns are orthonormal. Hence partner r15 has

`G=I_6`, `det G=1`, `product |lambda_q|=1`.                         (8.7)

For a physical row in `S`, the normalized leverage is

`u_{1i}^2+u_{2i}^2=2/m`;                                          (8.8)

for a physical row in `T`, it is

`q_{1j}^2+q_{2j}^2+c_{1j}^2+c_{2j}^2=4/m<=1/2`.                  (8.9)

Thus every hypothesis of the designated partner theorem is met. Applying (1.3) with `r=4` gives the actual inequality

`boxed:
 ||p_{Q_m}||_infinity
 <=4*(8/6)*2^(-1/2)
 =8 sqrt(2)/3
 =3.7712361663... .`                                              (8.10)

The density is continuous and

`P{Q_m in B}<3.772 |B|`                                           (8.11)

for every interval `B`. This is an equation-level use of the designated account02/B09 result, not a citation-only dependency.

## 9. First unpaid B09 implication after this run

The new analytic payment means that a fixed physical pair is finished whenever either its anchored third volume or its anchored fourth volume is quantitatively nondegenerate. The first unpaid implication is now

`QFORM-FIXEDPAIR-LOW-V3V4-OR-PAID-EXIT-v1`:

> starting from the bare three-large-eigenvalue hypothesis, either force a literal physical pair whose anchored third- or fourth-volume currency is bounded below at a universal normalized scale, or show that simultaneous degeneration of those pair-anchored currencies forces an already-paid grouped-coordinate, ridge/diffuse, finite-core, definite/singular-pair, or diagonal-plus-low-rank carrier branch.

The next useful calculation should be deterministic: characterize simultaneous small anchored `3`- and `4`-volume through the physical pair's quotient row space, without treating a small operator residual as a small random quadratic error.

No valid counterexample to the full conjecture is produced here.

## 10. Integrity

Only private authorized mathematical repositories and source-pinned QFORM artifacts were used. No public release, email, notification change, scheduler mutation, new task, cross-account authentication, paid model/API/Codex call, installation work or unrelated data was used. The changed-file scope contains only this run's pure mathematical report/check/handoff/status artifacts. Repository synchronization is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
