SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-23T21:04:57Z.
attacking: QFORM-STRONG-PHYSICAL-PAIR-SCHUR-COLLAPSE-v1 — convert any well-conditioned literal physical pair in the r41 finite core into either a full density payment or a quantitative rank-two Schur collapse, while retaining arbitrary rough product laws and every outside coupling.

# fleet03/B19 r42 — strong physical-pair Schur compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **NEW TARGET-LEVEL ANALYTIC RECEIVER + NEW FINITE-CORE STRUCTURAL COMPILER / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Full-target continuity: **OPEN**. The new pair/Schur payments below establish essential boundedness; no continuity upgrade is claimed for them.

## 1. Compact conditional end-to-end position

The unrestricted target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, moments, compact support, connected support, log-concavity, iid hypothesis, diagonal-basis independence, or post-rotation independence is used.

The immediate predecessor for this slot is fleet03/B19 r41,

`yspennstate/math-open-problems@70d462947bf313c24fa3acf49114b5164c02138c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T200734Z-fleet03-B19-QFORM-r41/REPORT.md`.

Its finite-core rank-two collar has a literal physical partition `H disjoint_union L`, with

`|H|<=124`,
`C=A[H,L]`,
`s_1(C)s_2(C)>1/480`,

and after the r38 transverse payment one may choose a literal two-row cross skeleton `C_2` of rank at most two satisfying

`||C-C_2||_op <1/64`.                                             (1.1)

The r41 defect-circuit compiler pays every large physical defect circuit by `<11991`; otherwise it localizes its still-unexplained H-side self curvature. The first remaining local question was whether that self curvature can be forced into a source-valid paid structure rather than merely labelled a bad bank.

This run attacks that implication before doing any further matrix taxonomy. The new theorem below says that one well-conditioned physical 2-by-2 pair is already enough: either a second literal Schur resource pays the FULL ambient quadratic form, or the ENTIRE H-side self block is within `0.000165` of rank two. Combined with (1.1), the latter leaves a rank-at-most-six coupling carrier over `A[L,L]` at operator error below `0.015790`.

Thus, conditional on the already-proved r41 reduction, every still-unpaid finite-core state now lies in one of only two mechanisms:

1. every physical 2-by-2 principal pair in `A[H,H]` has smallest singular value `<1/64`; or
2. the H-side self block is quantitatively rank two, and together with the cross collar the full matrix is within `0.015790` of `diag(0,A[L,L])` plus a symmetric rank-at-most-six carrier.

This is not yet an end-to-end proof of QFORM: the pairwise-weak collective regime and the arbitrary-extra-spectrum interaction of the rank-six carrier remain open.

## 2. Source-complete analytic inputs

Two completed inputs are used at exact equations.

### 2.1 Physical indefinite-pair logarithmic transducer

The source is

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

If two ORIGINAL coordinates have an invertible indefinite symmetric coefficient block `B`, put

`D=|det B|`, `kappa=sigma_min(B)`.

After exact completion of that physical pair, suppose the remaining random term `R` satisfies

`sup_t P(|R-t|<rho) <= H sqrt(rho)` for every `rho>0`.             (2.1)

Then the full quadratic form has an essentially bounded density and

`||p_Q||_infinity <=4 sqrt(2H) (D kappa)^(-1/4).`                 (2.2)

The pair translations may depend arbitrarily on the remainder. No independence is asserted after diagonalizing `B`.

### 2.2 Rank-two affine half-Riesz theorem

The source is

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For two orthonormal projection coordinates, any invertible symmetric `2 x 2` quadratic coefficient `Lambda`, arbitrary affine perturbation, and independent cap-one originals,

`sup_t E |W-t|^(-1/2) <=128 |det Lambda|^(-1/4).`                 (2.3)

In particular,

`P(|W-t|<rho) <=128 |det Lambda|^(-1/4) sqrt(rho).`               (2.4)

This theorem allows both signatures.

The fresh zero-diagonal physical-triangle theorem at

`yspennstate/math-open-problems@28f12d8868c8e8521dcd63fdf6988b38fd2ca53e`

`proofnet24/QFORM-density/interactive/20260923T211600Z-offdiagonal-triangle/REPORT.md`

is also compatible with the compiler: an exact physical zero-diagonal triangle with edge minimum `m` has `||p_Q||_infinity <=(3+log 8)/m`, even with arbitrary couplings to conditioned outside originals. I use it only as a paid endpoint, not as a replacement for the nonzero-diagonal branches below.

All live corrections are retained: no arbitrary-joint coarea estimate, no pointwise law-uniform quadratic-phase decay, no conditional projection-height shortcut, no independence after rotation, no fiber-supremum argument, and no deletion of a small coefficient multiplying an unbounded random input.

## 3. Main target-level theorem

### Theorem 3.1 — `QFORM-PHYSICAL-PAIR-SCHUR-SECOND-RESOURCE-v1`

Let `X=(X_1,...,X_n)` have independent real probability densities bounded by one. Let `A=A^T` be arbitrary and allow an arbitrary affine term as well. Choose two ORIGINAL coordinates `T={i,j}` such that

`B=A[T,T]`

is invertible and indefinite. Put

`D=|det B|`, `kappa=sigma_min(B)`, `R=T^c`,                     (3.1)

and form the exact physical Schur complement

`S=A[R,R]-A[R,T] B^(-1) A[T,R].`                                (3.2)

Then the following two source-valid payments hold.

**(a) Scalar Schur resource.** If one original coordinate `k in R` satisfies

`|S_kk|>=eta>0`,                                                  (3.3)

then

`boxed:
 ||p_Q||_infinity
 <=8*2^(1/4) (D kappa eta)^(-1/4).`                              (3.4)

**(b) Second physical-pair Schur resource.** If two original coordinates `K={k,l} subset R` satisfy

`d:=|det S[K,K]|>0`,                                              (3.5)

then

`boxed:
 ||p_Q||_infinity
 <=64 (D kappa)^(-1/4) d^(-1/8).`                               (3.6)

Equivalently, because of the exact principal Schur identity

`|det A[T union K,T union K]|=D d`,                              (3.7)

(3.6) can be written

`boxed:
 ||p_Q||_infinity
 <=64 kappa^(-1/4)
       [D |det A[T union K,T union K]|]^(-1/8).}`                 (3.8)

All signs outside the requirement that the first pair is indefinite are arbitrary. Every quadratic coefficient outside `T`, every coupling to the outside variables, every extra eigenvalue, and every affine term is retained.

### Proof

Write `x=(x_T,x_R)`. Exact completion of the physical pair gives

`x^T A x + linear`
`=(x_T+m(x_R))^T B (x_T+m(x_R)) + R_S(x_R)`,                    (3.9)

where `m` is affine in the remaining ORIGINAL variables and the quadratic matrix of `R_S` is exactly `S`. Since `T` and `R` are disjoint original-coordinate banks, `X_T` is genuinely independent of `X_R`; for fixed `X_R`, the translation `m(X_R)` preserves both scalar density caps on the pair.

For (a), condition all remaining originals except `X_k`. The random remainder becomes a scalar quadratic

`q(u)=S_kk u^2+b u+c`.                                           (3.10)

Completing the scalar square reduces its interval preimage to

`{v: |v^2-y|<rho/|S_kk|}`.                                      (3.11)

For every real `y` and `eps>0`, this set has Lebesgue measure at most

`2 sqrt(2 eps)`.                                                  (3.12)

Indeed, when `y<=eps` it lies in `[-sqrt(2eps),sqrt(2eps)]`; when `y>eps`, its two components have total length

`2[sqrt(y+eps)-sqrt(y-eps)]<=2sqrt(2eps)`.                       (3.13)

The conditional scalar input density is at most one, so uniformly in all conditioning values,

`sup_t P(|R_S-t|<rho | others)
 <=2sqrt(2) |S_kk|^(-1/2) sqrt(rho).`                            (3.14)

Average the conditioning and use (3.3): (2.1) holds with

`H=2sqrt(2) eta^(-1/2)`.                                        (3.15)

Substitution into (2.2) gives exactly (3.4).

For (b), condition all remainder originals outside `K={k,l}`. The retained remainder is

`W=X_K^T S[K,K]X_K+b^T X_K+c`,                                  (3.16)

with two genuinely independent cap-one physical inputs and arbitrary affine vector `b`. The completed half-Riesz theorem (2.3) gives, uniformly in the conditioning,

`sup_t E|W-t|^(-1/2)
 <=128 d^(-1/4).`                                                (3.17)

Since

`1_{|W-t|<rho} <=sqrt(rho)|W-t|^(-1/2)`                          (3.18)

away from the null set `W=t`, (3.17) yields (2.1) with

`H=128 d^(-1/4)`.                                                (3.19)

Substitute this in (2.2):

`4 sqrt(2H)=4 sqrt(256 d^(-1/4))=64 d^(-1/8)`,                  (3.20)

which proves (3.6). Finally, (3.7) is the standard determinant identity for the principal block

`[[B,A[T,K]],[A[K,T],A[K,K]]]`,                                 (3.21)

whose Schur complement of `B` is `S[K,K]`. QED.

**Regularity.** The proof gives an essentially bounded density. The invoked pair-log theorem does not claim continuity at this level of roughness, so neither do I.

## 4. Definite physical pairs are already direct exits

For completeness, if an invertible physical `2 x 2` block `B` is definite, then after conditioning every other original coordinate and translating the two retained variables, the joint pair density is at most one. The pushforward of two-dimensional Lebesgue measure by `y -> y^T B y` has density `pi/sqrt(det B)` on its half-line. Therefore

`boxed: ||p_Q||_infinity <= pi/sqrt(det B).}`                    (4.1)

This again permits every outside coupling and arbitrary affine terms.

Thus a quantitatively well-conditioned physical pair has only two possibilities: a definite pair pays immediately, while an indefinite pair enters Theorem 3.1.

## 5. New finite-core structural compiler

Fix the live finite-core size bound

`m=|H|<=124`                                                     (5.1)

and set

`kappa_0=2^(-6)=1/64`,
`eta=2^(-20)`,
`delta=eta^2=2^(-40).`                                           (5.2)

### Theorem 5.1 — `QFORM-STRONG-PHYSICAL-PAIR-SCHUR-COLLAPSE-v1`

For the FULL ambient quadratic form, one of the following holds.

1. Every physical principal pair `B=A[{i,j},{i,j}]` with `i,j in H` satisfies

   `sigma_min(B)<1/64`.                                          (5.3)

2. The density is paid by one of the explicit bounds

   `||p_Q||_infinity<202`,                                       (5.4)

   `||p_Q||_infinity<6889`,                                      (5.5)

   or

   `||p_Q||_infinity<46341`.                                     (5.6)

3. There is a symmetric matrix `L_H` of rank at most two such that

   `boxed:
    ||A[H,H]-L_H||_op
    < [1+121sqrt(2)]2^(-20)
    <0.000165.}`                                                 (5.7)

### Proof

If (5.3) fails, choose a physical pair `T` with `kappa>=kappa_0`. Because `B` has two singular values at least `kappa`,

`D=|det B|>=kappa^2>=kappa_0^2.`                                (5.8)

If `B` is definite, (4.1) gives

`||p_Q||_infinity
 <=pi/kappa_0
 =64pi
 =201.0619298...<202`,                                           (5.9)

so (5.4) holds.

Assume `B` is indefinite. Let `S_H` be the restriction of the exact Schur complement (3.2) to the remaining core coordinates `H\T`.

If some diagonal of `S_H` has magnitude at least `eta`, (3.4), (5.8) give

`||p_Q||_infinity
 <=8*2^(1/4)(kappa_0^3 eta)^(-1/4)
 =6888.6234337...<6889`.                                        (5.10)

If some physical pair `K subset H\T` has

`|det S_H[K,K]|>=delta`,                                        (5.11)

then (3.6), (5.8) give

`||p_Q||_infinity
 <=64 (kappa_0^3)^(-1/4) delta^(-1/8)
 =46340.9500118...<46341`.                                      (5.12)

Suppose both gates fail. Then for all remaining core coordinates `k,l`,

`|(S_H)_kk|<eta`,                                                (5.13)

and

`|(S_H)_kk(S_H)_ll-(S_H)_kl^2|<delta=eta^2`.                    (5.14)

Therefore

`|(S_H)_kl|^2
 <=|(S_H)_kk(S_H)_ll|+delta
 <2 eta^2`,                                                       (5.15)

so every off-diagonal entry has magnitude `<sqrt(2)eta`. There are at most `122` remaining coordinates. The maximum absolute row sum and hence the operator norm satisfy

`||S_H||_op
 <=eta+121sqrt(2)eta
 =[1+121sqrt(2)]2^(-20)
 =0.00016414627175...`.                                          (5.16)

Write the physical core block in the `T | H\T` ordering as

`A[H,H]=[[B,F^T],[F,G]].`                                       (5.17)

Define

`L_H=[[B,F^T],[F,F B^(-1)F^T]].`                                (5.18)

Then

`L_H=[I;F B^(-1)] B [I,B^(-1)F^T]`,                            (5.19)

so `rank(L_H)<=2`, while

`A[H,H]-L_H=diag(0,S_H)`.                                       (5.20)

Equations (5.16)-(5.20) prove (5.7). QED.

The conclusion is deterministic matrix structure. It is NOT used to say that the random variable `X_H^T(A[H,H]-L_H)X_H` is small; with no moment/support assumption that inference would be invalid.

## 6. Actual splice into the r41 rank-two cross collar

Return to the r41 finite-core survivor. Its literal cross block admits

`C=C_2+Z`,
`rank(C_2)<=2`,
`||Z||_op<1/64`.                                                  (6.1)

If Theorem 5.1 pays the density, this branch is closed with one of (5.4)-(5.6). Otherwise there are two structural possibilities.

### 6.1 Pairwise-weak self bank

Every physical pair in the finite source bank obeys (5.3). This is a genuinely collective/diffuse mechanism; selecting another fixed small minor cannot be assumed to repair it.

### 6.2 Rank-two self bank

If (5.7) holds, define the full structured carrier

`A_sharp = [[L_H,C_2],[C_2^T,A[L,L]]].`                          (6.2)

Then

`A-A_sharp
 =[[A[H,H]-L_H,Z],[Z^T,0]]`,                                    (6.3)

and therefore

`boxed:
 ||A-A_sharp||_op
 <0.000164146272+1/64
 =0.015789146272<0.015790.}`                                     (6.4)

Moreover

`K:=A_sharp-diag(0,A[L,L])
 =[[L_H,C_2],[C_2^T,0]]`                                        (6.5)

has rank at most six. Indeed its image is contained in

`[Ran(L_H)+Ran(C_2)] direct_sum Ran(C_2^T)`,                     (6.6)

whose dimension is at most `2+2+2=6`. Thus

`boxed:
 A_sharp=diag(0,A[L,L])+K,
 rank(K)<=6.}`                                                    (6.7)

Since the original target has `s_3(A)>=1`, Weyl gives the deterministic spectral bookkeeping statement

`boxed: s_3(A_sharp)>0.984210853728.}`                            (6.8)

Again, (6.4) is used only for matrix/singular-value bookkeeping. No random quadratic tail is discarded.

This is a sharper successor to the r41 description `latent two directions plus an arbitrary bad self bank`: once ANY H-side physical pair is `1/64`-conditioned, the arbitrary bad self block disappears. The survivor is either paid or the complete H-side self interaction is rank two up to `1.65e-4`.

## 7. Fresh physical-triangle endpoint

The newly completed physical zero-diagonal triangle theorem can be inserted without changing any hypotheses. If three actual coordinates in the current state have exactly zero diagonal coefficients and their three mutual edge magnitudes are at least `1/64`, then, after conditioning every outside original coordinate, the theorem gives

`||p_Q||_infinity
 <=64(3+log 8)
 =325.0842586...<326.`                                           (7.1)

This endpoint is useful because it is uniform even for a highly unbalanced triangle, where one scalar Schur curvature may be very small. I do not perturb a merely small diagonal to zero.

## 8. Designated partner fleet04/B19 applied to an actual inequality

The completed designated-partner theorem is fleet04/B19 r2,

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`.

In its exact residual-diffuse exact-rank-three null-coloop normal form, with `0<D_res<=1` and `|det M|>=1`, it proves a continuous `C_0` density and

`||p_Q||_infinity <34 sqrt(log(e/D_res)).`                        (8.1)

On the concrete interval

`2^(-20)<=D_res<=1`,                                             (8.2)

this gives the actual bound

`boxed:
 ||p_Q||_infinity
 <34 sqrt(log(2^20 e))
 =131.0784605...<132.}`                                          (8.3)

No extension of (8.1) to a merely near-null row, to the r41 finite-core carrier, or to an arbitrary joint-density surrogate is made. The partner's later moving-ridge construction remains a hard correction boundary showing why original-product provenance cannot be forgotten.

## 9. Updated first missing implication

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.

Inside the r41 finite-core branch, the first essential local implication is now

`QFORM-FINITECORE-PAIRWISEWEAK-OR-RANK6-CARRIER-PAYMENT-v1`:

> Pay either (i) the source bank in which every literal physical two-coordinate principal block has `sigma_min<1/64`, or (ii) the carrier `diag(0,A[L,L])+K` with `rank(K)<=6`, `s_3>0.9842`, while retaining the actual nonzero coefficient error in the probabilistic argument. Route either alternative to an already-proved grouped/projected-crossing/rank-one-two-source theorem without replacing a small matrix error by a small random error.

This is strictly narrower than r41's `latent2 plus small-pivot/cross-near-null bad bank`: a quantitatively usable physical pair now either closes the density estimate outright or collapses the whole finite self bank to rank two.

A separate global splice remains necessary for arbitrary extra spectrum. The current theorem does not assert that `A[L,L]` itself satisfies the three-eigenvalue target, and it does not use induction at a subunit spectral threshold.

## 10. Verification

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory independently recompute all displayed thresholds and test the exact Schur determinant identity and rank-two completion on 1000 random noncommuting symmetric instances. The maximum normalized four-by-four determinant residual is `5.686173e-15`; the maximum observed third singular value of the claimed rank-two completion is `1.725895e-15`; the terminal marker is

`QFORM_B19_R42_SCHUR_PAIR_CHECK_PASS`.

The numerical checks are regression checks only. The proof is the exact calculation in Sections 3-6.

## 11. Scope / privacy / execution record

The run consumed only QFORM mathematical repository material. It did not alter task counts, schedules, enabled/paused states, email/push delivery, permissions, public release settings, or cross-account authentication. No installation or paid model/API/Codex call was made. Repository access and native learned-memory ingestion are distinct; this run remains `WITHOUT_VERIFIED_BRAIN`.

Model self-report: GPT-5.6 Sol. Configured reasoning level/counters: UNKNOWN / not exposed.
