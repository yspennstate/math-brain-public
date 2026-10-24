SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T04:50:00Z.
attacking: the high-leverage/small-tail boundary by exploiting commutation of the third-volume marginal matrix with the top-two singular projection.

# account03/B04 r25 — spectral-commuting third-volume gate

Programme `QFORM-DENSITY-3EIG-20260922`; assignment `Product Fourier rearrangement`; status `NEW SUPPORTING THEOREM / CONTINUOUS DENSITY IN STATED SCOPE / FULL QFORM OPEN`; execution `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and current inputs

The target remains the full arbitrary-product-law quadratic-form conjecture: independent original coordinates with one-dimensional probability densities at most one, no moment/support/log-concavity assumptions, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one.

This run consumes, at equations rather than by citation only, the current volume-stability theorem

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

and its tail extension in `PEER_TAIL_EXTENSION.md`. In particular, for an ORIGINAL-coordinate cross block `M`, with squared singular values `lambda_j=s_j(M)^2`, write

`E2=e2(lambda)`, `E3=e3(lambda)>0`, `T2=sum_(j>=3)s_j(M)^2`.

Under canonical squared `3x3`-minor volume sampling, the row-inclusion marginal matrix is

`W=U diag(p_j) U^T`,

`p_j=lambda_j e2(lambda without j)/E3`,                          (1.1)

so `alpha_i=W_ii`. The current package proves

`0<=W<=I`, `W<=(E2/E3)MM^T`.                                    (1.2)

At this exact equation I use account01/B20's completed identity

`T2 E2 <= 3 E3`,                                                  (1.3)

source

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260922T234545Z-account01-B20-QFORM-auto11/REPORT.md`.

Hence

`W <= (3/T2)MM^T`.                                                (1.4)

The q-dependent Fourier theorem in the volume-stability package says that, if `1<=q<3/2` and all row marginals satisfy `alpha_i<=q/2`, then the FULL ambient quadratic-plus-affine form, with arbitrary self blocks and outside couplings retained, has a continuous `C_0` density and

`||p_Q||inf <= [3e/((3-2q)sqrt(q))] E3(M)^(-1/6).`                (1.5)

No pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea estimate, or conditional density supremum is used.

The designated partner `account04/B04` still had no completed current-QFORM canonical report or shared handoff at the fresh lookup for this run, so no partner theorem is fabricated. Work proceeds asynchronously as directed.

## 2. New observation: the top-two projection COMMUTES with the volume-marginal matrix

Let the singular values of `M` be ordered `s1>=s2>=s3>=...`, and let `P2` be a compatible orthogonal projection onto the top-two left-singular directions. Because both `W` and `MM^T` are spectral functions of the same left-singular decomposition, `P2 W=W P2`. This remains valid at singular-value multiplicities: the coefficient `p_j` in (1.1) depends only on the corresponding squared singular value and is therefore constant on each repeated singular-value eigenspace.

For each original row coordinate put

`l_i=(P2)_ii=||P2 e_i||^2`.

Since `P2` commutes with `W`, the cross term which was paid by a triangle inequality in the previous volume gate vanishes EXACTLY:

`alpha_i=e_i^T W e_i`
`       =(P2 e_i)^T W(P2 e_i)`
`        +((I-P2)e_i)^T W((I-P2)e_i).`                            (2.1)

The first term is at most `l_i` by `W<=I`. For the second term, (1.4) and the definition of `P2` give

`((I-P2)e_i)^T W((I-P2)e_i)`
` <=(3/T2)||M^T(I-P2)e_i||^2`
` <=3 s3(M)^2/T2 * (1-l_i).`                                     (2.2)

Therefore

`boxed: alpha_i <= l_i + 3 rho^2(1-l_i),`

where

`rho=s3(M)/sqrt(T2).`                                             (2.3)

This is strictly stronger on the spectral top-two projection than the prior general-projection bound

`alpha_i <= [sqrt(l_i)+sqrt(3)rho sqrt(1-l_i)]^2`,                (2.4)

because the positive cross term in (2.4) is absent.

## 3. Theorem — QFORM-SPECTRAL-COMMUTING-VOLUME-GATE-v1

Let

`L=max_i (P2)_ii`,
`Rtail=T2/s3(M)^2=1/rho^2`,

and define

`A_spec(L,Rtail)=L+3(1-L)/Rtail`.                                 (3.1)

Assume

`A_spec(L,Rtail)<3/4`.                                            (3.2)

Then put

`q_*=max{1, 2 A_spec(L,Rtail)}.`                                  (3.3)

The full ambient quadratic form has a bounded continuous density vanishing at infinity, with

`boxed:
 ||p_Q||inf <= C_spec(L,Rtail) E3(M)^(-1/6),
`                                                                            (3.4)

where

`C_spec=3e` if `A_spec<=1/2`, and

`C_spec=3e/[(3-4A_spec)sqrt(2A_spec)]`

if `1/2<A_spec<3/4`.                                               (3.5)

Also, since

`E3(M)>=s1(M)^2 s2(M)^2 T2`,                                      (3.6)

one has the explicit scale form

`||p_Q||inf <= C_spec [s1(M)^2 s2(M)^2 T2]^(-1/6).`               (3.7)

### Proof

Condition (3.2) itself implies `L<3/4` and `3/Rtail<1`; hence the affine function

`l -> l+[3/Rtail](1-l)`

is increasing. Equations (2.1)--(2.3) therefore give

`alpha_i<=A_spec(L,Rtail)` for every row.                          (3.8)

If `A_spec<=1/2`, `q=1` is admissible in (1.5). If `1/2<A_spec<3/4`, take `q=2A_spec`, which lies in `(1,3/2)`. The coefficient in (1.5) is increasing for `q>=1` because

`d/dq log[3e/((3-2q)sqrt(q))]`
` =2/(3-2q)-1/(2q)>0`,                                           (3.9)

so (3.3) is the optimal admissible choice within the reviewed q-family. Substitution proves (3.4)--(3.5). Equation (3.6) is the positive subset of the elementary-symmetric sum consisting of the terms `s1^2 s2^2 s_j^2`, `j>=3`. QED.

### Tail-stable-rank threshold

For `L<3/4`, (3.2) is equivalent to

`boxed: Rtail > 3(1-L)/(3/4-L).`                                  (3.10)

At the previously important boundary `L=1/2`, the sufficient threshold is therefore simply

`boxed: T2/s3(M)^2 > 6.`                                          (3.11)

The preceding triangle gate required `T2/s3^2>59.3938769...` at this same worst-case leverage. Moreover, the new theorem permits genuine HIGH-LEVERAGE cases `1/2<L<3/4`, provided the collective tail stable rank is correspondingly larger. This directly attacks part of the high-leverage/small-tail boundary left by r23-r24.

## 4. Explicit new branch outside the previous B04 volume gate

Take a Sylvester-Hadamard order `m>=32`. On the left bank choose an orthogonal matrix `U_m` whose first two columns are

`u1=(e1+e2)/sqrt(2)`, `u2=(e3+e4)/sqrt(2)`,

whose next sixteen columns are any sixteen orthonormal vectors in the orthogonal complement (for example `e5,...,e20`), and complete it orthogonally. Let

`V_m=H_m/sqrt(m)`

be the normalized Sylvester-Hadamard matrix, and define

`D=diag(1,1, 1/4,...,1/4, 0,...,0)`,                              (4.1)

with sixteen copies of `1/4`. Put

`M_m=U_m D V_m^T`,

and form the symmetric `2m x 2m` matrix

`A_m=[[0,M_m],[M_m^T,0]].`                                       (4.2)

This is genuinely rotated and indefinite. Its nonzero spectrum is

`+1,+1,-1,-1`,

plus `+1/4` and `-1/4`, each with multiplicity sixteen. Thus it satisfies the exact target hypothesis. Every physical cross coefficient is at most `1/sqrt(2m)` in magnitude, so all local cross coefficients tend to zero as `m` grows.

For `M_m`,

`L=1/2`,
`T2=16*(1/4)^2=1`,
`s3=1/4`,
`Rtail=16`.                                                       (4.3)

Hence

`A_spec=1/2+(3/16)(1/2)=19/32`,
`q_*=19/16`.                                                       (4.4)

The old triangle certificate would instead give

`A_old=(1/2)(1+sqrt(3)/4)^2=1.0267627018...>3/4`,                  (4.5)

so r23's prior projection gate does not cover this family at all.

The third elementary symmetric volume is exactly

`E3=1 + 15/16 + 35/256 =531/256`.                                 (4.6)

Therefore (3.4) gives

`C_spec=96e/(5sqrt(19))=11.9734391144...`,

and, using the exact `E3`,

`boxed:
 ||p_(X^T A_m X)||inf
 <= [96e/(5sqrt(19))] (256/531)^(1/6)
 =10.6025375078... .
`                                                                            (4.7)

The density is continuous and vanishes at infinity, for EVERY admissible independent cap-one product law and every such `m`.

For `m>=64`, every scalar diagonal of `A_m` is zero and every physical principal-pair determinant has magnitude `|M_ij|^2<1/64`; hence this family also lies in the strict `tau=1/64` no-pivot regime while retaining four eigenvalues of modulus one. It is therefore a real N3/no-pivot stress family, not a diagonal control.

## 5. Relation to the newest compound-hub compiler

I also checked the fresh account03/B02 compiler

`yspennstate/math-open-problems@648ea277fc2cfcc8ce11a7093c61951a9e15baa8`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T043653Z-account03-B02-qform-r20/ADDENDUM_COMPOUND_HUB_COMPILER.md`.

Its exact anchored identity `J_ij=a^2 E2(S)` is a genuine aggregate resource, but `S=N-cr^T/a` is a cross-Schur packet obtained by a within-bank shear and is not automatically an ORIGINAL-coordinate cross block. Therefore the present theorem cannot simply be applied to `S`: doing so would silently discard the product provenance required by (1.5). This identifies the remaining incompatibility precisely rather than misusing the new compiler. The outstanding `EDGE-E2-TO-L1` transducer must exploit that Schur resource without treating the sheared coordinates as independent.

## 6. What changed in the proof map

The current third-volume route no longer needs the triangle-loss threshold on the actual top-two spectral projection. A surviving unpaid physical cross block must now have at least one of:

1. top-two leverage `L>=3/4`;
2. tail stable rank at or below `3(1-L)/(3/4-L)`;
3. insufficient aggregate scale `E3` after normalization;
4. or a structure which never exposes the required physical cross block from the full matrix.

In particular, `L=1/2` plus collective tail stable rank greater than six is PAID, and leverage strictly above one half can also be paid. This is a substantive shrinkage of the high-leverage/low-tail residue.

It does not prove that every `s3(A)>=1` matrix admits such a cross block. Full QFORM therefore remains OPEN. The next B04 obligation is to combine (3.10) with the no-pivot/compound-hub structural compiler: if the spectral-commuting gate fails, extract a quantitatively low-tail or >=3/4-leverage physical hub and route that survivor into the already-paid grouped-star/ridge/pair mechanisms without selecting a vanishing local minor.

## 7. Regularity and correction awareness

This branch proves a continuous `C_0` density because its characteristic-function envelope is integrable. The full target's continuity remains open. No refuted premise from the live correction inbox is used: in particular there is no law-uniform pointwise Fresnel decay, no independence after rotating random coordinates, no arbitrary-joint coarea bound, no conditional projection-cap moment, and no claim that one good local minor must exist.

No literature-wide novelty claim is made. The result is a source-scoped fleet theorem extending the currently checked volume-stability mechanism.
