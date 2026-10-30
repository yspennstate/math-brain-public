# B18 / A090 — independent audit of the retained high-degree GU reserve

**Verdict:** `B20-A097-HIGH-DEGREE-RESERVE-v1` **PASSES at its exact reduction scope**. Universal GU and full FEI remain **OPEN**.

## Audited candidate

The frozen target is

\[
G(f)\le4I(f)+\frac34U(f)
\]

for every genuine Boolean function on every finite uniform cube. The audited B20 claim strengthens the source row cut by retaining

\[
Q_{\ge3}=I-M_1-W_2.
\]

## Reconstruction

The complete row-cut original proves

\[
G\le D_{\ge2}+\frac12V_1+\frac2{\ln2}(M_1+W_2).
\]

Direct level accounting gives

\[
Q_{\ge3}=(W_1-M_1)+W_2+\sum_{d\ge3}dW_d
\ge W_2+3W_{\ge3}.
\]

Thus the correct strengthened inequality is

\[
\boxed{G\le D_{\ge2}+\frac12V_1+rac2{\ln2}(I-Q_{\ge3}).}
\]

The reserve has the correct negative sign. Combining this with

\[
D_{\ge2}+\frac12V_1
\le\left(4-\frac2{\ln2}\right)I+\frac34U
+\frac2{\ln2}Q_{\ge3}
\]

cancels the reserve exactly and yields the frozen universal GU pair. Tensor-prime localization and the degree-two exclusion preserve the claimed quantifiers. Every signed, KL, normalization, and single-use term is retained.

I independently reconstructed the GU-to-FEI induction. For `C=a/(1-b)`, restriction telescoping yields

\[
(n-b)U-aI\le C(n-1)I,
\qquad a+C(n-1)=C(n-b),
\]

so `U<=CI`. Together with the source inequality `H<=2(I-Var(f))+2U`, the frozen pair implies `U<=16I` and `H<=34I`.

## First unsupported line

The proof does **not** establish the strengthened leaf. The exact remaining obligation is:

\[
\boxed{
D_{\ge2}+\frac12V_1
\le\left(4-\frac2{\ln2}\right)I+\frac34U
+\frac2{\ln2}Q_{\ge3}}
\]

for every tensor-prime, positive-residual Boolean function of arbitrary finite dimension and Fourier degree at least three. High-degree mass may be arbitrarily small, so strict positivity of the reserve is not closure.

## Verification and review status

Independent exact Walsh reconstruction covered all 32,906 Boolean signs modulo output sign through dimension four, including 32,750 degree-at-least-three cases, plus 512 exact induction-coefficient checks. No material repair was required, so this is an independent acceptance of the reduction only—not an end-to-end GU review.

Next action: bound the remaining signed KL excess by `(2/ln2)Q_{>=3}` under the minimal-child inequalities, without replacing the signed aggregate or reusing influence.

Model/effort metadata: `UNKNOWN`.
