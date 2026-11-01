# fleet03/B03 r53 supplement — target-example spectral wording correction

The theorem and all Fourier/Riesz constants in `REPORT.md` and `CHECKS.md` are unchanged. This supplement corrects one wording error in the strict target-valid example and its check.

For

`A_*=[[1/2,1/2,sqrt(2)],[1/2,1/2,-sqrt(2)],[sqrt(2),-sqrt(2),1]]`,

we have

`charpoly(A_*)=(lambda-1)(lambda^2-lambda-4)`

and therefore

`spec(A_*)={1,(1-sqrt(17))/2,(1+sqrt(17))/2}`.

The report sentence saying that **all three** eigenvalues have modulus strictly larger than one is too strong: one eigenvalue is exactly `1`. The correct statement is

`min_j |lambda_j(A_*)| = 1`,

so all three eigenvalues have modulus **at least one**, while the other two have modulus strictly larger than one. This is exactly sufficient for the owner's target hypothesis.

Likewise, the `CHECKS.md` line claiming that the smallest absolute eigenvalue is `(sqrt(17)-1)/2>1` should read: the two nonunit eigenvalues have absolute values `(sqrt(17)-1)/2>1` and `(sqrt(17)+1)/2>1`, while the remaining eigenvalue has absolute value `1`; hence the minimum absolute eigenvalue is `1`.

No bound, proof step, partner application, or status changes. The example remains a literal target-valid rotated instance with the nonzero `V^2` pivot retained.

`QFORM_B03_R53_SUPPLEMENT_CHECK_PASS`
