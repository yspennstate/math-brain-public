SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B03, 2026-09-24T10:13:58Z.
attacking: the dependence-safe pivot plus two-bank crossing branch, using the completed account01/B03 bipartite Moyal receiver.

# A pivot-crossing determinant compiler

Programme: QFORM-DENSITY-3EIG-20260922. Status: NEW SUPPORTING THEOREM / FULL QFORM OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

## 1. Statement

Let \(A\) be a real symmetric \(n\times n\) matrix. Choose five distinct original coordinates
\[
z,\qquad X=\{x_1,x_2\},\qquad Y=\{y_1,y_2\}.
\]
Write
\[
d=A_{zz}
\]
and form the rectangular \(3\times3\) minor
\[
M=A[\{z\}\cup X,\{z\}\cup Y]
=
\begin{pmatrix}
d&A[z,Y]\\
A[X,z]&A[X,Y]
\end{pmatrix}.
\]
Assume \(d\det M\ne0\). Then for every vector of independent real random variables whose coordinate densities satisfy \(0\le f_i\le1\), the law of
\[
Q=X_{\rm all}^{T}AX_{\rm all}
\]
has an essentially bounded density and
\[
\boxed{
 \|p_Q\|_{\infty,\mathrm{ess}}
 \le 4\sqrt2\,|d\det M|^{-1/4}.
}
\tag{1.1}
\]
Equivalently, every interval \(I\) satisfies
\[
\boxed{
 \Pr(Q\in I)\le4\sqrt2\,|d\det M|^{-1/4}|I|.
}
\tag{1.2}
\]
All coordinates outside the selected five, all their mutual quadratic couplings, and all their couplings to the selected coordinates are arbitrary. No moment, support, sign, smoothness, or post-rotation independence assumption is used. This theorem asserts essential boundedness; continuity is not inferred from the square-peel argument.

## 2. Proof

Condition on all original coordinates outside \(\{z\}\cup X\cup Y\). They contribute only affine terms and a constant to the five-coordinate quadratic polynomial. The selected variables remain independent and retain their original cap-one densities.

The conditional polynomial has the form
\[
Q=dZ^2+2Z(a_X^TX+a_Y^TY+\beta)
 +X^TCX+2X^TB_0Y+Y^TDY+\ell_X^TX+\ell_Y^TY+c,
\tag{2.1}
\]
where \(C,D\) are symmetric \(2\times2\) matrices and
\[
a_X=A[X,z],\qquad a_Y=A[Y,z],\qquad B_0=A[X,Y].
\]
Since \(d\ne0\), complete the physical square:
\[
Q=d\left(Z+d^{-1}(a_X^TX+a_Y^TY+\beta)\right)^2+R(X,Y),
\tag{2.2}
\]
where the crossing matrix of the residual four-variable quadratic form is exactly
\[
B=B_0-d^{-1}a_Xa_Y^T.
\tag{2.3}
\]
The completed account01/B03 theorem QFORM-BIPARTITE-MOYAL-CS-v1, at
math-open-problems commit
\[
\texttt{6c4698000d4fd206b465a18231ba8c7a8f643f59},
\]
retains each sum/difference pair jointly and proves
\[
\sup_s\mathbb E|R-s|^{-1/2}
\le4\sqrt2\,|\det B|^{-1/4}.
\tag{2.4}
\]
This estimate is uniform in the same-side matrices \(C,D\), all affine terms, and the conditioned outside coordinates.

For a cap-one scalar density, the translated physical square satisfies the standard trace-free bound
\[
p_{d(Z+h)^2}(u)\le |d|^{-1/2}|u|^{-1/2}
\]
on its supporting half-line. Applying it conditionally in (2.2), then using (2.4), gives
\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le4\sqrt2\,|d|^{-1/2}|\det B|^{-1/4}.
\tag{2.5}
\]
No independence between the completed-square center and \(R\) is asserted or needed: one conditions on \(X,Y\) for the scalar square bound and integrates the resulting fractional potential.

Finally, the Schur determinant identity gives
\[
\det M
=d\det(B_0-d^{-1}a_Xa_Y^T)
=d\det B.
\tag{2.6}
\]
Substitution into (2.5) yields
\[
|d|^{-1/2}|\det B|^{-1/4}
=|d|^{-1/4}|\det M|^{-1/4}
=|d\det M|^{-1/4},
\]
which proves (1.1). Averaging the uniform conditional interval bound over the outside coordinates proves (1.2).

## 3. A target-valid dense ambient family

Let the selected five-coordinate principal block be
\[
A_5=
\begin{pmatrix}
1&0&0&0&0\\
0&0&0&1&0\\
0&0&0&0&1\\
0&1&0&0&0\\
0&0&1&0&0
\end{pmatrix}.
\tag{3.1}
\]
Its spectrum is
\[
\{1,1,1,-1,-1\},
\]
so it already lies in the full target. With \(z=1\), \(X=\{2,3\}\), and \(Y=\{4,5\}\),
\[
d=1,\qquad
A_5[\{1,2,3\},\{1,4,5\}]=I_3.
\]
Therefore every cap-one product law obeys
\[
\boxed{\|p_{X^TA_5X}\|_{\infty,\mathrm{ess}}\le4\sqrt2.}
\tag{3.2}
\]

More strongly, embed \(A_5\) as a principal block of an arbitrary larger symmetric matrix, with arbitrary dense couplings to all additional coordinates and arbitrary additional spectrum. Principal-submatrix interlacing gives at least three eigenvalues of the full matrix at least \(1\), so every such extension remains inside the owner's full target. Conditioning on the outside coordinates leaves the same five-coordinate quadratic block and only changes affine terms. Hence every such dense ambient extension still satisfies
\[
\boxed{\|p_{X^TAX}\|_{\infty,\mathrm{ess}}\le4\sqrt2.}
\tag{3.3}
\]

## 4. What the determinant identity buys

Before the Schur identity, the natural cost is
\[
|A_{zz}|^{-1/2}\,
\left|\det\!\left(
A[X,Y]-\frac{A[X,z]A[z,Y]}{A_{zz}}
\right)\right|^{-1/4}.
\]
Equation (2.6) turns this into one original-matrix certificate,
\[
\left|A_{zz}\det A[\{z\}\cup X,\{z\}\cup Y]\right|^{-1/4}.
\]
Thus the near-pivot loss and the two-bank crossing volume are not independent losses. One quarter-power of the pivot is canceled exactly by the growth of the Schur crossing determinant.

Define the physical pivot-crossing score
\[
\mathcal P_3(A)=
\max_{\substack{z,X,Y\ {\rm pairwise\ disjoint}\\ |X|=|Y|=2}}
\left|A_{zz}\det A[\{z\}\cup X,\{z\}\cup Y]\right|.
\tag{4.1}
\]
Whenever \(\mathcal P_3(A)>0\),
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}
\le4\sqrt2\,\mathcal P_3(A)^{-1/4}.
}
\tag{4.2}
\]
This is an actual final-matrix inequality, not a statement about a rank-three component after a canceling perturbation.

## 5. Remaining full-target gap

The unrestricted conjecture remains open. The missing deterministic implication is to force a universal lower bound for \(\mathcal P_3(A)\), or a different already-paid exit, from the sole global hypothesis \(s_3(A)\ge1\). Such a lower bound for one individual minor is not assumed here and is false without an appropriate alternative branch in diffuse configurations.

The next useful splice is therefore a dichotomy between:
1. a paid pivot-crossing certificate \(\mathcal P_3(A)\gtrsim1\);
2. the aggregate overlap-two / \(Z_2\) branch, which does not select one universally good minor;
3. a uniformly invertible physical principal block or another established hub/ridge exit.

## 6. Source pins

- Owner/control revision read from fresh math-research-brain main: 2026-09-22.15.
- Current continuation request: QFORM-CLAUDE-LATEST-20260922T225732Z.
- Completed partner theorem: account01/B03 QFORM-BIPARTITE-MOYAL-CS-v1, math-open-problems commit 6c4698000d4fd206b465a18231ba8c7a8f643f59.
- Prior account04/B03 overlap-two localization: math-open-problems commit 5f93186cf8952b2b8b0255e08a78fd8506c613e4.
- Prior account04/B03 hyperbola four-volume branch: math-open-problems commit 8147f1247043e419eb6762911c4a34fa58494d0f.

Repository publication is not native learned-memory ingestion. Unexposed model and thinking metadata remain UNKNOWN.
