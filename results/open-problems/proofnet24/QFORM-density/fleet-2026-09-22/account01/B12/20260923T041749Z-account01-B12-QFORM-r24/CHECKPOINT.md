SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T04:17:49Z.
attacking: principal-compression elimination of all genuinely additional large eigenvalues, using a resolvent-trace obstruction in the four-large survivor case.

# Early substantive checkpoint

Status: WORKED_PARTIAL_DERIVATION / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN.

## Goal of this mechanism

Change mechanism after the preceding stability/cross-bank runs. Instead of controlling an added spectral remainder directly, condition on ORIGINAL coordinates and remove coordinates while keeping three eigenvalues above one fixed subunit threshold. The intended payoff is a reduction of every >=4-large-eigenvalue matrix to either an exactly-three-large principal compression or a uniformly bounded-dimensional principal compression. This would isolate the genuinely unpaid theorem to the exactly-three-large core and eliminate arbitrary additional large eigenvalues without rotating the independent inputs.

## Key resolvent-trace lemma

For a real symmetric m x m matrix B and a number t in (0,1) such that +/-t is not an eigenvalue of B, define

p = #{lambda(B)>t},   q = #{lambda(B)<-t},   N_t(B)=p+q.

Assume N_t(B)=4 and that for every physical coordinate i, the principal compression B^{(i)} obtained by deleting coordinate i satisfies N_t(B^{(i)})<=2.

Cauchy interlacing gives

p(B^{(i)}) >= p-1,   q(B^{(i)}) >= q-1.

Hence p,q are both nonzero and, for every i,

p(B^{(i)})=p-1,   q(B^{(i)})=q-1.

Apply inertia additivity to C_+=B-tI. Writing C_+ in the i | i^c block form, the Schur scalar s_i has sign + because the positive inertia drops by exactly one on passing to the compression. Since s_i^{-1}=[(B-tI)^{-1}]_{ii},

[(B-tI)^{-1}]_{ii}>0.

Likewise for C_-=B+tI, the negative inertia drops by exactly one, so

[(B+tI)^{-1}]_{ii}<0.

Therefore every diagonal entry of

(B-tI)^{-1}-(B+tI)^{-1}=2t(B^2-t^2 I)^{-1}

is positive, and hence

tr (B^2-t^2 I)^{-1} > 0.                                      (1)

If, in addition, the four t-large eigenvalues of B all have absolute value >=1, while every other eigenvalue has absolute value <t, then

tr (B^2-t^2 I)^{-1}
 = sum_j 1/(lambda_j^2-t^2)
 <= 4/(1-t^2) - (m-4)/t^2.                                    (2)

Combining (1)-(2) yields

m-4 < 4t^2/(1-t^2), equivalently m < 4/(1-t^2).                (3)

Thus a four-large survivor for which *every* physical-coordinate deletion destroys at least two t-large directions is automatically bounded-dimensional.

## Compression algorithm suggested by the lemma

Choose t in (2/3,7/10) avoiding the absolute eigenvalues of every principal submatrix of the starting A. Such a t exists because there are finitely many principal submatrices and finitely many eigenvalues.

Start with A having at least four eigenvalues of modulus >=1, hence N_t(A)>=4.

* If N_t>=5, Cauchy interlacing shows that deleting any one physical coordinate leaves N_t>=3. Delete one coordinate.
* If N_t=4 and some physical deletion leaves N_t>=3, make that deletion.
* If N_t=4 and every deletion leaves N_t<=2, apply the lemma. Because t<7/10,

  4t^2/(1-t^2) < 196/51 <4,

  so m-4<4 and therefore m<=7.
* The procedure terminates because dimension strictly decreases. Its other terminal state is N_t=3.

Hence every matrix with at least four eigenvalues |lambda|>=1 has a principal compression B, obtained only by deleting ORIGINAL coordinates, such that either

(a) N_t(B)=3, or
(b) dim B<=7 and N_t(B)>=3,

and throughout the deletion chain the retained compression has at least three eigenvalues of modulus >t.

Conditioning on all deleted original coordinates keeps the remaining variables independent with the same density cap and merely creates an arbitrary affine term in the surviving variables.

## Expected end-to-end consequence

The current Claude finite-dimensional theorem gives, in case (b), for arbitrary affine terms,

||p||_infinity <= 2 sqrt(6 pi * 7)/t < 3 sqrt(42 pi).

In case (a), after scaling by 1/t, the surviving matrix has exactly three eigenvalues of modulus >1 and all remaining eigenvalues of modulus <1. Therefore any universal theorem for that exact-three spectral core, once affine terms are handled, automatically extends to every >=4-large-eigenvalue matrix with only the one-time scale loss 1/t<3/2. There is no loss per deleted coordinate.

The remaining work in this run is to make the affine closure precise via epsilon-I regularization/completion of squares, check the exact constants, apply the designated account02/B12 result at an actual inequality, and publish a complete reduction theorem with all threshold/equality cases explicit.
