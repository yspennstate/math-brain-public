# Signed extension of the scalar-bank obstruction

This addendum strengthens the main report from the positive rank-three projection to the genuinely indefinite signature `(2,1)` endpoint. It uses the same original-coordinate frame and no new probabilistic assumption.

Let `R_n` be the trigonometric Parseval frame from `REPORT.md`, and set

`Lambda=diag(1,1,-1)`,
`A_n=R_n Lambda R_n^T`.                                         (1)

Then the nonzero spectrum of `A_n` is exactly `{1,1,-1}`. Thus this is an exact owner-target family with the difficult indefinite sign pattern.

## 1. Full-spark scalar-sufficiency obstruction survives arbitrary invertible spectral signs

More generally, let `Lambda` be any invertible `3 x 3` matrix and `A=R_n Lambda R_n^T`. For every coordinate set `S`,

`A[S,:] R_n Lambda^(-1)=R_n[S,:]`.                              (2)

Since also `rank A[S,:]<=rank R_n[S,:]`, (2) gives the exact identity

`rank A[S,:]=rank R_n[S,:]`.                                   (3)

The scalar-sufficiency lemma from the main report therefore implies again:

> if the conditional quadratic dependence on a physical bank `S` can be represented exactly through one scalar linear aggregate while all outside original coordinates merely create an affine coefficient, then `|S|=1`.

So the leakage-free scalar-bank obstruction is not an artifact of positive semidefiniteness.

## 2. Every clean three-singleton core degenerates

For a physical triple `I`,

`B_I=A_n[I,I]=R_n[I,:] Lambda R_n[I,:]^T`.                      (4)

Because every row has squared norm `3/n`,

`||R_n[I,:]||_F^2=9/n`.                                       (5)

Hence

`||B_I||_op <= ||R_n[I,:]||_op^2 ||Lambda||_op <=9/n`,         (6)

and therefore

`boxed(sigma_min(B_I)<=9/n.)`                                  (7)

For the chosen `Lambda=diag(1,1,-1)`, every triple is actually nonsingular by full spark and

`|det B_I|=det(R_n[I,:])^2 <=(3/n)^3=27/n^3`.                  (8)

As in the main report, arbitrary nonzero rescaling of singleton aggregates is exactly canceled by density normalization (for cap-attaining inputs such as `Uniform[0,1]`), so the density-normalized core has the same singular values as `B_I` up to sign congruence. Thus no absolute normalized core threshold can be obtained by a clean three-scalar reduction on this indefinite family.

## 3. The same indefinite family is uniformly paid by aggregate diffuse curvature

The spectral projection of `A_n` onto `|lambda|>=1/64` is still

`P_H=R_n R_n^T`,                                               (9)

with

`max_i(P_H)_ii=3/n`.                                          (10)

For every `n>=96`, the completed ridge-window theorem therefore gives, for **every** allowed independent cap-one input law,

`boxed(||p_(X^T A_n X)||_infinity <=288 sqrt(3e)/13<64),`      (11)

and the density is continuous and vanishes at infinity.

Thus the clean scalar-core degeneration occurs in a signature `(2,1)` target family even while the correct aggregate theorem remains uniformly dimension-free.

## 4. Signed leakage identity

Let `U` have orthonormal columns, complete it by `W`, and write

`M=U^T A_n U`, `E=U^T A_n W`, `G=U^T P_H U`.                  (12)

Because `A_n^2=P_H`, the top-left block of `A_n^2` gives

`boxed(E E^T=G-M^2.)`                                         (13)

For the positive projection endpoint `A_n=P_H`, `G=M` and (13) reduces to `EE^T=M-M^2`. Equation (13) is the correct signed conservation law: a compressed indefinite core cannot be studied independently of its residual leakage and the active spectral leverage `G`.

## 5. Consequence for B05

The first unpaid implication can be sharpened to a signed form:

`QFORM-SIGNED-COMPRESSED-CORE-LEAKAGE-COAREA-v1`:

jointly spend the triple `(M,G,E)` satisfying `EE^T=G-M^2` in the signed rank-three endpoint, and its original-coordinate analogue for arbitrary extra spectrum, without conditioning on dependent within-bank residual linear combinations.

This remains a supporting structural advance, not a proof of full QFORM. Full QFORM and the full continuity conclusion remain open.
