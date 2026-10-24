# QFORM research handoff — all-sign scalar pivot theorem

2026-09-23T19:22Z. FULL UNRESTRICTED CONJECTURE OPEN.

New explicit corollary of the assembled manuscript, math commit 6fc6115304e63909de896dab1c3a9cb7ff4938af:
https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T192150Z-all-sign-scalar-pivot/REPORT.md

If symmetric A has s3(A)>=sigma>0 and SOME original physical diagonal a=A_ii!=0, then independent cap-one product laws and arbitrary affine terms yield
  ||p_{X^TAX+b^TX+c}||infinity <= C_*/sqrt(|a| sigma),
  C_* = 1+44*10^7.5 =1.391402171...e9.
All ranks and all signatures are included. This broadens the earlier one-minority-sign extension, at a much larger constant.

Proof: scalar Schur complement S=D-vv^T/a obeys s2(S)>=s3(A) because A=rank-one matrix +(0⊕S). The assembled lower_levels.tex Theorem lower:two gives truncated half-Riesz H<=1e6 for all s2>=1 matrices without a c*=1e-15 physical pivot. Assembled structure.tex Lemma pivot-half gives H<=44 c*^-1/2 when a c* pivot exists (diagonal OR principal pair). Thus full half-potential <=C_* for every s2>=1 matrix; scale by sigma. Conditional scalar square in original Xi contributes |a|^-1/2 |y-R|^-1/2. No rotated independence, supports, moments, or sign assumptions.

Source audit: lower:two comparable/dominant spectral branches and their numerical constants were checked in the math report. Do not treat this as a full proof. The no-small-pivot branch, notably a true zero-curvature hub a=0 with diffuse leaves, remains open; its discriminant has rank one and the scalar square path loses the transverse regularization. Keep all dense leakage terms in the actual polynomial.

This is a scoped source synthesis. Existing mixed-sign minority-pivot note at interactive/20260923T185647Z-minority-pivot-all-rank retains a substantially better constant 674.401/sqrt(delta) when the Schur remainder is semidefinite.
