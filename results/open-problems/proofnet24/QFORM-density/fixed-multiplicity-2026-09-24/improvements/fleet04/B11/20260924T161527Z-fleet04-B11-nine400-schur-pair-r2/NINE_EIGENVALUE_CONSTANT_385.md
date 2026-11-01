# Nine-eigenvalue constant sharpened from 400 to 385

## Theorem

Let \(X_1,\ldots,X_n\) be independent real random variables with probability densities bounded by \(K\). Let \(A\) be any real symmetric matrix, let \(b\in\mathbb R^n\), \(c\in\mathbb R\), and suppose
\[
 s_9(A)\ge s>0.
\]
Then \(X^TAX+b^TX+c\) has a density satisfying
\[
 \boxed{\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
 <385\,\frac{K^2}{s}.}
\]

This uses the complete proof in source commit \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\` and changes only the final numerical closure. All signs, dimensions, remaining spectrum, affine terms, and rough cap-\(K\) product laws are retained.

## Proof

Scale to \(K=s=1\). The exhaustive branches in the source proof give the following strict upper bounds:
\[
375,\quad280,\quad320,\quad383,\quad80,
\]
except for the indefinite-pair branch, whose exact bound is
\[
 C_{\mathrm{hyp}}=200+80\log10+\frac1e.
\]
It remains to bound this number without relying on floating-point arithmetic.

Set \(x=923/400\). Positivity of the exponential Taylor series gives
\[
 e^x>\sum_{j=0}^{7}\frac{x^j}{j!}
 =\frac{9195903741172641329483}{917504000000000000000}.
\]
The numerator exceeds ten times the denominator by
\[
20863741172641329483>0.
\]
Therefore \(e^{923/400}>10\), or
\[
 \log10<\frac{923}{400}.
\]
Likewise
\[
 e>1+1+\frac12+\frac16=\frac83,
\]
hence \(1/e<3/8\). It follows that
\[
 C_{\mathrm{hyp}}
 <200+80\frac{923}{400}+\frac38
 =200+\frac{923}{5}+\frac38
 =\frac{15399}{40}
 =384.975<385.
\]
Every other branch is already below 385. Rescaling restores \(K^2/s\), proving the claim.

## Scope

This sharpens the constant, not the singular-value threshold. The independently reconstructed proof still requires \(s_9(A)\ge s\). The overlap theorem in the same source does not by itself supply the missing product-preserving analytic estimate needed for \(s_8\).
