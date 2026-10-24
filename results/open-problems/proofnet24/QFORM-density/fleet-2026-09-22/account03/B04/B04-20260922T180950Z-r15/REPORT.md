SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B04, 2026-09-22T18:09:50Z.
attacking: the scalar-Q_rest conditioning reduction introduced by owner control revision 2026-09-22.11; testing whether sup_b ||p_{Q3|Q_rest=b}||_infinity can be bounded while preserving the original product law.

# QFORM B04 r15 — scalar spectral conditioning is not a uniform gate

## Status

Outcome: **EXPLICIT COUNTEREXAMPLE TO AN INTERMEDIATE PROOF GATE + EXPLICIT POSITIVE BOUND FOR THE SAME ROTATED INDEFINITE FORM.**

This report does **not** prove or refute the full QFORM conjecture. It refutes the new intermediate claim that, after fixing three large spectral directions and writing `Q=S+R`, one can hope for a universal bound

\[
\sup_b\|p_{S\mid R=b}\|_\infty<\infty.
\]

The failure already occurs for four independent cap-one uniforms and a fixed 4x4 symmetric matrix with four distinct eigenvalues. In fact every possible choice of three spectral directions versus the remaining one has an unbounded scalar-conditioned density supremum. At the same time the *unconditional* quadratic form has the explicit law-uniform density bound `2 pi / sqrt(3)`. Thus the obstruction is solely the use of an unweighted conditional supremum; it is not a counterexample to QFORM.

The run also consumes the fresh correction `QFORM-COAREA-AND-CONDITIONAL-MOMENT-CORRECTIONS-v1` from `yspennstate/math-research-brain@938e59f2caed677576b8bb3cd87ee1ffe81ee572`, which already invalidates the unrestricted `K ||rho||_infinity^(2/3)` coarea lemma for arbitrary joint densities and a positive-moment vector-conditioning interface. No such false lemma is used below.

The designated partner `account04/B04` had no completed QFORM handoff/report visible at the two fresh partner checks in this run, so no partner result is fabricated or attributed.

## 1. Exact target instance

Let `X_1,...,X_4` be independent `Uniform[-1/2,1/2]`, so every input density is exactly one on its support. Put

\[
H=\frac12\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},\qquad Y=HX.
\]

`H` is orthogonal and symmetric. Let

\[
D=\operatorname{diag}(1,2,-3,4),\qquad A=H^T D H.
\]

Explicitly,

\[
A=\begin{pmatrix}
1&1/2&-2&3/2\\
1/2&1&3/2&-2\\
-2&3/2&1&1/2\\
3/2&-2&1/2&1
\end{pmatrix}.
\]

Hence `A` is genuinely rotated and indefinite, with distinct eigenvalues

\[
\{1,2,-3,4\}.
\]

All four eigenvalues have modulus at least one, so this is inside the exact QFORM hypothesis. The quadratic form is

\[
Q=X^TAX=Y_1^2+2Y_2^2-3Y_3^2+4Y_4^2.
\]

Because the eigenvalues are distinct, the spectral axes are fixed up to signs; there is no repeated-eigenvalue freedom hiding the construction.

## 2. Edge slices of a Hadamard spectral coordinate

The same calculation works for any row of `H`. Start with row 4 and set

\[
t=1-\varepsilon,\qquad 0<\varepsilon<\frac12.
\]

The point

\[
c=(1/2,-1/2,-1/2,1/2)
\]

is the unique cube corner with `Y_4=1`. Define nonnegative deficits

\[
u_1=\frac12-X_1,\quad
u_2=X_2+\frac12,\quad
u_3=X_3+\frac12,\quad
u_4=\frac12-X_4.
\]

Then

\[
Y_4=1-\frac{u_1+u_2+u_3+u_4}{2}.
\]

Consequently the slice `Y_4=1-epsilon` is exactly

\[
u_i\ge0,\qquad u_1+u_2+u_3+u_4=2\varepsilon.
\]

For the other three Hadamard coordinates one obtains

\[
\begin{aligned}
Y_1&=(-u_1+u_2+u_3-u_4)/2,\\
Y_2&=(-u_1+u_2-u_3+u_4)/2,\\
Y_3&=(-u_1-u_2+u_3+u_4)/2.
\end{aligned}
\]

Therefore, on this slice,

\[
|Y_1|,|Y_2|,|Y_3|\le \frac{u_1+u_2+u_3+u_4}{2}=\varepsilon.
\tag{2.1}
\]

The marginal density of `Y_4` can also be computed exactly. The four deficits are independent `Uniform[0,1]`; for `z in [0,1]`, the Irwin-Hall density of `Z=u_1+...+u_4` is `z^3/6`. Since `Y_4=1-Z/2`,

\[
p_{Y_4}(1-\varepsilon)=2\,p_Z(2\varepsilon)=\frac83\varepsilon^3.
\tag{2.2}
\]

Because the joint density of `Y=HX` is the indicator of the rotated unit-volume cube, the conditional density of `(Y_1,Y_2,Y_3)` given `Y_4=t` is constant on its tetrahedral slice and has exact essential supremum

\[
\|\rho_{123\mid Y_4=t}\|_\infty
=\frac1{p_{Y_4}(t)}
=\frac{3}{8\varepsilon^3}.
\tag{2.3}
\]

The same formula holds at `-t` by central symmetry.

## 3. The scalar-conditioned quadratic density blows up

Write

\[
S=Y_1^2+2Y_2^2-3Y_3^2,\qquad R=4Y_4^2.
\]

Set

\[
b_\varepsilon=4(1-\varepsilon)^2.
\]

Conditioning on `R=b_epsilon` mixes the two slices `Y_4=+t` and `Y_4=-t`. The map `X -> -X` interchanges these slices and sends `(Y_1,Y_2,Y_3)` to its negative. Since `S` is even, the conditional law of `S` on the two slices is identical. Hence

\[
\mathcal L(S\mid R=b_\varepsilon)=\mathcal L(S\mid Y_4=1-\varepsilon).
\tag{3.1}
\]

By (2.1),

\[
|S|\le |Y_1|^2+2|Y_2|^2+3|Y_3|^2\le6\varepsilon^2.
\tag{3.2}
\]

Thus the conditional law is supported in an interval of length at most `12 epsilon^2`.

This conditional law is absolutely continuous. Indeed, on the three-dimensional tetrahedral slice the conditional measure has a bounded Lebesgue density, while

\[
\nabla S=(2Y_1,4Y_2,-6Y_3)
\]

vanishes only at the single point `0`, a conditional-measure-null set. The coarea theorem therefore gives an absolutely continuous one-dimensional pushforward (no quantitative unrestricted coarea estimate is invoked).

Any probability density supported on an interval of length `L` has essential supremum at least `1/L`. Therefore

\[
\boxed{
\|p_{S\mid R=b_\varepsilon}\|_\infty\ge\frac1{12\varepsilon^2}.
}
\tag{3.3}
\]

Letting `epsilon -> 0` gives

\[
\boxed{
\sup_b\|p_{S\mid R=b}\|_\infty=\infty.
}
\tag{3.4}
\]

This directly falsifies the scalar-conditioning supremum gate proposed in owner revision `2026-09-22.11`.

## 4. There is no escape by choosing a different spectral triple

The preceding argument is not special to leaving out eigenvector 4. Every row of the normalized Hadamard matrix has entries `+/-1/2`. For each `k`, the cube corner having signs matching row `k` satisfies

\[
Y_k=1,\qquad Y_j=0\quad(j\ne k).
\]

Write, for any `k`,

\[
R_k=\lambda_kY_k^2,\qquad
S_k=\sum_{j\ne k}\lambda_jY_j^2,
\]

where `(lambda_1,lambda_2,lambda_3,lambda_4)=(1,2,-3,4)`. On the slice `Y_k=1-epsilon`, the same deficit-simplex argument gives `|Y_j|<=epsilon` for every `j!=k`. Hence

\[
|S_k|\le \varepsilon^2\sum_{j\ne k}|\lambda_j|.
\]

The conditional law given

\[
R_k=\lambda_k(1-\varepsilon)^2
\]

is absolutely continuous and supported on an interval of length at most

\[
2\varepsilon^2\sum_{j\ne k}|\lambda_j|\le18\varepsilon^2.
\]

Consequently

\[
\boxed{
\|p_{S_k\mid R_k=\lambda_k(1-\varepsilon)^2}\|_\infty
\ge\frac{1}{2\varepsilon^2\sum_{j\ne k}|\lambda_j|}
\ge\frac1{18\varepsilon^2}.
}
\tag{4.1}
\]

Thus **every** `3+1` spectral split for this fixed distinct-spectrum matrix has an unbounded scalar-conditioned quadratic density supremum. A proof cannot repair the gate merely by selecting a different three of the four large eigendirections.

For completeness, the conditional three-dimensional projection density itself also diverges. If `b=lambda_k(1-epsilon)^2`, the two sign slices have equal weight and overlap at the origin, so

\[
\boxed{
\|\rho_{Y_{-k}\mid R_k=b}\|_\infty=\frac{3}{8\varepsilon^3}.
}
\tag{4.2}
\]

This is an exact product-source calculation, not an arbitrary dependent joint-density shell.

## 5. The same full quadratic form nevertheless has a uniform density bound

The construction is **not** a counterexample to QFORM. In fact, the full law admits a simple explicit cap for *every* choice of independent input densities bounded by one, not merely for the uniform witness used above.

Condition on `(X_3,X_4)`. As a quadratic polynomial in `(X_1,X_2)`, the Hessian block is

\[
B=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix},
\qquad \det B=\frac34,
\]

which is positive definite. The remaining coordinates contribute only an affine term and a constant. Completing the square gives

\[
Q=(z-z_0)^T B(z-z_0)+c
\]

for `z=(X_1,X_2)` with `z_0,c` depending on the conditioned variables.

Let `I` be any interval of length `h`. Since the product density of `(X_1,X_2)` is at most one,

\[
\Pr(Q\in I\mid X_3,X_4)
\le \operatorname{Leb}_2\{z:(z-z_0)^TB(z-z_0)+c\in I\}.
\]

The area of the ellipse sublevel set `{z:z^TBz<=s}` is `pi s_+ / sqrt(det B)`. Therefore every shell of quadratic-value thickness `h` has area at most

\[
\frac{\pi h}{\sqrt{\det B}}=\frac{2\pi}{\sqrt3}h.
\]

Averaging over `(X_3,X_4)` yields the target-scale small-ball estimate

\[
\Pr(Q\in I)\le\frac{2\pi}{\sqrt3}|I|.
\]

Hence the full law has an essentially bounded density satisfying

\[
\boxed{
\|p_Q\|_\infty\le\frac{2\pi}{\sqrt3}=3.627598728\ldots
}
\tag{5.1}
\]

for every independent cap-one input law. This is a genuinely rotated indefinite matrix with four distinct large eigenvalues. The argument proves absolute continuity plus the essential-supremum bound. A continuous representative is **not** established here.

This is a direct product-space/bathtub estimate: after conditioning, cap-one product density is dominated by planar Lebesgue measure of the optimal quadratic shell. No pointwise oscillatory decay is used.

## 6. What exactly failed, and the corrected interface

The algebraic mixture identity is valid:

\[
p_Q(q)=\int p_{S\mid R=b}(q-b)\,d\mu_R(b).
\]

Therefore

\[
\|p_Q\|_\infty
\le \int \|p_{S\mid R=b}\|_\infty\,d\mu_R(b).
\tag{6.1}
\]

Replacing the right side by the stronger quantity `sup_b ||p_{S|R=b}||_infinity` is what fails.

The edge geometry explains why an averaged quantity can still survive. In the witness above,

* slice probability density near `Y_k=1-epsilon` is of order `epsilon^3` by (2.2);
* conditional quadratic density necessarily scales at least as `epsilon^{-2}` by (4.1).

Thus the bad edge conditional cap is multiplied by a vanishing scalar-conditioning weight. The model power balance is `epsilon^3 * epsilon^{-2} = epsilon`, which is integrable. This identifies a more plausible replacement obligation: control a **weighted mixed norm** such as

\[
\int \|p_{S\mid R=b}\|_\infty\,d\mu_R(b)
\]

(or a sharper product-Fourier/rearrangement surrogate), rather than a uniform conditional supremum. Whether this weighted quantity is universally bounded under the full QFORM hypotheses remains open and must be tested against the existing conditional-moment falsifiers.

## 7. Source/correction accounting

Fresh control observed in this run:

* brain owner-control commit before operational writes: `eb93d5ba9d2e5fa40d55d15696832f556b715e9d`;
* OWNER CONTROL revision: `2026-09-22.11`;
* target remains `QFORM-DENSITY-THREE-LARGE-EIGENVALUES`;
* fresh correction commit additionally consumed: `938e59f2caed677576b8bb3cd87ee1ffe81ee572`, event `QFORM-COAREA-AND-CONDITIONAL-MOMENT-CORRECTIONS-v1`.

No Gaussian, log-concavity, moment, compact-support assumption beyond the *specific counterexample law* itself, eigen-coordinate independence assumption, or pointwise Fourier-decay assertion enters any target-level conclusion. The positive bound (5.1) is law-uniform over all independent cap-one coordinate densities for the displayed fixed matrix.

## 8. Next unpaid implication

**QFORM-B04-SCALAR-WEIGHTED-MIXED-NORM-v1.** Replace the false `sup_b` gate by a product-preserving weighted conditional norm. The first concrete target is to prove or refute, under a decomposition into three selected large spectral directions plus the rest,

\[
\int \|p_{Q_3\mid Q_{\rm rest}=b}\|_\infty\,d\mu_{Q_{\rm rest}}(b)\le C
\]

with a universal `C`, or to find the correct weaker Lorentz/rearrangement quantity that still implies the full small-ball estimate. Any proof must keep original-coordinate product provenance and survive the fresh vector-conditioning and arbitrary-joint-coarea counterexamples.

Full QFORM status: **OPEN**.
Continuous-density status for the full target: **OPEN**.
Native learned-memory status: **WITHOUT_VERIFIED_BRAIN**.
