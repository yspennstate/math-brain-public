# Diffuse spectral-window deletion compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet01/B08` — diffuse eigenvector case  
Run: `20260923T144019Z-fleet01-B08-qform-r30`  
Status: **PROVED SUPPORTING STRUCTURAL/ANALYTIC ROUTER / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted bounded-density conjecture remains OPEN. The unrestricted continuous-density conclusion also remains open. This report gives a full-spectrum, original-coordinate router that joins the completed one-scale diffuse payment to a one- or two-coordinate localized core. It does not use a probabilistic small-matrix perturbation, spectral-coordinate independence, moments, support regularity, or a fiber supremum.

## 1. Source-pinned inputs actually used

### 1.1 One-scale ridge / spectral-window theorem

Canonical source:

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For a symmetric matrix with three eigenvalues of modulus at least `M`, if the spectral projection onto **all** eigenspaces with `|lambda|>=M/64` has diagonal at most `1/32`, the full ambient quadratic form has a continuous `C_0` density with

`||p||_infinity <= C_R/M`,

`C_R = 288 sqrt(3e)/13 = 63.2640518777... <64`.                 (1.1)

The proof is by an original-coordinate ridge cross block and permits arbitrary outside coordinates/couplings and coordinate-separable terms. Thus the same constructed child cross block can be used inside a larger ambient form after conditioning or without deleting the outside coordinate probabilistically.

### 1.2 New volume-stability / collective-tail source required by the current continuation

Canonical source:

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`.

For an original-coordinate cross block `M`, put

`T2=sum_(nu>=3) s_nu(M)^2`.

If the top-two left singular projection has diagonal at most `1/2` and

`T2/s_3(M)^2 >=225`,

then

`||p_Q||_infinity <= (9 sqrt(3)e/2)
 [s_1(M)^2 s_2(M)^2 T2]^(-1/6)`,                              (1.2)

with a continuous density. All same-bank curvature, outside couplings and affine terms remain arbitrary. This is used below as the already-paid collective-tail entrance to the designated partner's `k=1` branch; the new work here treats what remains after that diffuse exit.

### 1.3 Designated partner fleet02/B08

Canonical source:

`yspennstate/math-open-problems@41ee49f6e9c3383e4c3a322bdc52779768a17eb7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T130941Z-fleet02-B08-qform-diffuse-r27/REPORT.md`.

On the inherited selected-three `mu<=1/48` `k=1` gate it has

`beta=(3/16)sqrt(3/5)=0.145236875482...`,

`s_2(B)>=beta L`.                                                (1.3)

Its high-top-two-leverage branch produces an ORIGINAL physical row `i` of the cross block with

`g=B^T e_i`,

`||g||>beta L/sqrt(2)
      =(3/16)sqrt(3/10)L
      =0.102697979532...L`.                                    (1.4)

The same partner report applies (1.2) before entering this high-row branch; in particular, under the explicit collective-tail/marginal hypotheses its equation-level substitution gives the continuous exit `<584/L`. The work below consumes the surviving high-row resource (1.4) at the same physical coordinate.

## 2. Exact rank-loss lemma under physical deletion

### Lemma 2.1 — `QFORM-PHYSICAL-DELETION-SPECTRAL-CONSERVATION-v1`

Let `A=A^T`, let `U in R^{n x r}` have orthonormal columns, and suppose

`A U=U Lambda`,

`min_j |Lambda_jj|>=a>0`.

Let `H` be a physical coordinate set, `|H|=h<r`, let `T=H^c`, and put

`C=A[T,T]`,

`delta_H=||U_H^T U_H||op`.

Then

`boxed: s_(r-h)(C) >= a sqrt(1-delta_H).`                       (2.1)

#### Proof

Restrict the eigen-equation to the `T` rows:

`C U_T = U_T Lambda - A[T,H] U_H`.                              (2.2)

The second term has rank at most `h`. Since

`U_T^T U_T=I-U_H^T U_H`,                                       (2.3)

we have

`s_r(U_T Lambda)
 >=s_r(U_T)s_r(Lambda)
 >=a sqrt(1-delta_H)`.                                         (2.4)

For a rank-`h` perturbation, singular-value interlacing gives

`s_(r-h)(C U_T)>=s_r(U_T Lambda)`.                              (2.5)

Finally `||U_T||op<=1`, so

`s_(r-h)(C U_T)<=s_(r-h)(C)||U_T||op<=s_(r-h)(C)`.              (2.6)

Combining (2.4)-(2.6) proves (2.1). QED.

This is a statement about the literal principal child of the full matrix. No complementary spectral part is subtracted.

## 3. Two-level diffuse-window router

Fix three genuine eigenvectors `R in R^{n x 3}` satisfying

`R^T R=I_3`,

`A R=R Lambda_3`,

`min_j |(Lambda_3)_jj|>=L`,                                    (3.1)

and suppose their physical leverage is diffuse:

`max_i ||R_i||_2^2 <= 1/48`.                                   (3.2)

Let

`P0 = 1_{|A|>=L/64}`                                           (3.3)

be the spectral projection onto **all** eigenvalues at the one-scale window, including every complementary high spectral direction.

Put

`L1=L/(64 sqrt(3))=0.00902109795609...L`.                      (3.4)

### Theorem 3.1 — `QFORM-DIFFUSE-WINDOW-TWOLEVEL-ROUTER-v1`

At least one of the following alternatives holds.

**(D) Paid diffuse window.** The full ambient form has a continuous `C_0` density and

`||p_Q||_infinity <= C_R/L <64/L`.                              (3.5)

**(C3) Three-direction principal child.** There is an ORIGINAL coordinate `i` such that

`1/32 < (P0)_ii <=2/3`,                                        (3.6)

and for `C=A[-i,-i]`,

`boxed: s_3(C)>=L1.`                                           (3.7)

For this branch let

`P1=1_{|C|>=L1/64}`.                                           (3.8)

Then either the full original form already has a continuous `C_0` density with

`boxed: ||p_Q||_infinity
 <= C_R/L1
 = (55296 sqrt(e)/13)/L
 =7012.89933728.../L <7013/L,}`                                (3.9)

or there is a second ORIGINAL coordinate `j != i` with

`(P1)_jj>1/32`                                                  (3.10)

and the literal child row satisfies

`boxed:
 max{|C_jj|, ||C[j,(-i,-j)]||_2}
 > L1/512
 = L/(32768 sqrt(3))
 =1.76193319e-5 L.}`                                           (3.11)

Thus failure of both diffuse payments creates a genuine two-level physical core `(i,j)`; no favorable spectral-coordinate rotation is used.

**(H) Ultra-high spectral-window coordinate.** There is an ORIGINAL coordinate `i` such that

`(P0)_ii>2/3`,                                                  (3.12)

and simultaneously

`boxed:
 max{|A_ii|, ||A[i,-i]||_2} > L/(64 sqrt(3)),}`                (3.13)

`boxed:
 s_2(A[-i,-i]) >= sqrt(47/48)L
 =0.989528507253...L.}`                                        (3.14)

#### Proof

If `max_i(P0)_ii<=1/32`, apply the source theorem (1.1) at scale `L`; this is (D).

Assume the gate fails and choose `i` with `(P0)_ii>1/32`. The rank of `P0` is at least four. Indeed the selected three-dimensional range in (3.1) is contained in `Ran P0`; if `rank P0=3`, then `P0=RR^T`, contradicting `(P0)_ii>1/32` and (3.2).

Let `r=rank P0`, choose an orthonormal eigenframe `U` for `Ran P0`, and note that every corresponding eigenvalue has modulus at least `L/64`. Apply Lemma 2.1 with `H={i}`.

If `(P0)_ii<=2/3`, then

`s_(r-1)(A[-i,-i])
 >=(L/64)sqrt(1-(P0)_ii)
 >=L/(64 sqrt(3))=L1`.                                         (3.15)

Since `r>=4`, `r-1>=3`, hence `s_3(C)>=s_(r-1)(C)>=L1`, proving (3.7).

Now run the spectral-window construction (1.1) on the literal child matrix `C` at scale `L1`. If `max_j(P1)_jj<=1/32`, the proof constructs a ridge-admissible cross block entirely inside the child coordinates. The general ridge theorem is an ambient statement allowing arbitrary outside coordinates/couplings and affine terms, so the same child cross block pays the **original** full form `A`, with coordinate `i` treated as outside. This gives (3.9); no recursive use of the unproved QFORM conjecture occurs.

If the child window gate fails, choose `j` with `(P1)_jj>1/32`. Spectral energy in the child gives

`||C e_j||_2^2
 >=(L1/64)^2 (P1)_jj
 >(L1/64)^2/32`.                                                (3.16)

Because

`||C e_j||_2^2=|C_jj|^2+||C[j,(-i,-j)]||_2^2`,                  (3.17)

one of the two displayed terms is greater than `||C e_j||/sqrt(2)`, yielding

`max{|C_jj|,||C[j,(-i,-j)]||_2}>L1/512`.                       (3.18)

This is (3.11).

It remains to treat `(P0)_ii>2/3`. The same spectral-energy identity in the full matrix gives

`||A e_i||_2^2
 >=(L/64)^2(P0)_ii
 >(L/64)^2(2/3)`.                                              (3.19)

Writing `A e_i=(A_ii,A[-i,i])` and taking the larger of its scalar and off-diagonal pieces gives

`max{|A_ii|,||A[i,-i]||_2}
 > (L/64)sqrt((2/3)/2)
 =L/(64 sqrt(3))`,                                             (3.20)

which is (3.13).

Finally apply Lemma 2.1 to the selected three eigenvectors `R`. By (3.2), deletion of **any** physical coordinate satisfies

`s_2(A[-i,-i])
 >=L sqrt(1-||R_i||^2)
 >=sqrt(47/48)L`,                                              (3.21)

proving (3.14). QED.

### What Theorem 3.1 changes

The failure of the one-scale diffuse theorem is no longer merely the phrase “high spectral leverage.” It is now routed, without deleting the spectral remainder, into one of two explicit objects:

1. a child with three actual absolute eigenvalues at scale `L/(64sqrt3)` which itself either creates a valid ambient ridge payment `<7013/L` or a second physical high-window coordinate; or
2. one ultra-high physical spectral-window coordinate carrying a scalar/star of scale `L/(64sqrt3)` while its principal child retains two almost-`L` singular directions.

The second-level density payment is a genuine estimate for the original form, not an induction hypothesis.

## 4. Actual application of designated partner fleet02/B08

Enter the partner's `k=1` high-top-two-leverage branch (1.4), and let its physical row be `i`. Since the cross row `g` is a subvector of the full off-diagonal row,

`boxed:
 ||A[i,-i]||_2
 >=||g||_2
 >(3/16)sqrt(3/10)L
 =0.102697979532...L.}`                                       (4.1)

Independently, Lemma 2.1 on the selected-three frame gives at the **same** coordinate

`boxed:
 s_2(A[-i,-i])>=sqrt(47/48)L.`                                 (4.2)

Now combine this literal partner row with Theorem 3.1.

If the global one-scale window is diffuse, the entire partner survivor is already paid by (3.5). Suppose it is not. Then `rank P0>=4`. Evaluate the high-window deletion lemma at the partner's **same** physical row `i`:

* If `(P0)_ii<=2/3`, then

  `boxed: s_3(A[-i,-i])>=L1=L/(64sqrt3).}`                     (4.3)

  Thus the partner row carries the strong star (4.1) while its principal child has three genuine directions. If the child window (3.8) is diffuse, the entire original form is paid by

  `boxed: ||p_Q||_infinity<7013/L}`                            (4.4)

  with a continuous `C_0` density. If not, the same star (4.1) is accompanied by a second original coordinate `j` obeying (3.10)-(3.11).

* If `(P0)_ii>2/3`, then the remaining state is a genuinely localized high-window coloop-type state, with the simultaneous quantitative resources

  `(P0)_ii>2/3`,

  `||A[i,-i]||_2>0.102697979532...L`,

  `s_2(A[-i,-i])>=0.989528507253...L`.                         (4.5)

This is a strict strengthening of the bare partner “heavy row”: unless the same row is ultra-heavy in the **entire** one-scale spectral window, it automatically leaves a three-direction child, and that child either pays the original form by an existing ambient ridge theorem or creates a second localized physical coordinate.

The newest collective-tail source is also applied at the entrance: in the partner `k=1` state, if `T2>=gamma^2L^2` with `gamma=beta/64`, top-two projection diagonal at most `1/2`, and `T2/s_3(B)^2>=225`, then from (1.2) and `s_1,s_2>=beta L`,

`||p_Q||_infinity
 <=(9sqrt(3)e/2)[beta^4 gamma^2 L^6]^(-1/6)
 =(18sqrt(3)e/beta)L^(-1)
 =(480e/sqrt(5))L^(-1)
 =583.513243.../L <584/L`.                                    (4.6)

So (4.1)-(4.5) concern an actual survivor after the current diffuse volume exit, rather than a branch already paid by the newest tail theorem.

## 5. First unpaid implication

The first remaining B08 interface is now

`QFORM-STRONG-STAR-CHILD3-OR-HIGHWINDOW-COLOOP-RECEIVER-v1`:

> Pay either (a) a physical coordinate with star `>0.102697L` whose deletion leaves three directions at scale `L/(64sqrt3)` but whose child spectral window has a `>1/32` physical leverage coordinate, or (b) the same strong star with two almost-`L` child directions and full-window leverage `>2/3`, while retaining arbitrary same-bank curvature, all unused couplings, arbitrary complementary spectrum and conditioning-generated affine terms.

The full-matrix physical-pair theorem can pay a genuine fixed indefinite principal pair, but an `ell^2` star alone does not supply such a pair dimension-free; therefore this report does not silently convert (4.5) into a density theorem. Likewise the second heavy coordinate in (3.11) is a structural core, not by itself a completed analytic receiver.

## 6. Continuity bookkeeping

Continuity and `C_0` are proved only on alternatives (D), the second-level diffuse child payment (3.9), and the collective-tail payment (4.6), because those branches come from an integrable characteristic-function envelope. No continuity claim is made for the remaining structural branches.

## 7. Verification

A deterministic checker (`checks.py`, `check_results.json`) verifies the displayed constants and tests Lemma 2.1 on 2000 finite symmetric-matrix instances generated from exact orthogonal spectral decompositions. No numerical test is used as proof.

Independent end-to-end review status: **not performed for this new router**. The full conjecture still requires two independent end-to-end reviews after a complete candidate exists.
