# account04/B15 — a six-currency exact information-credit theorem on a two-dimensional biased prime-gate surface

**Classification:** `AUXILIARY_ONLY / NEW_SOURCE-EXACT_CREDIT_BOUND`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Current target and inherited negative-credit rule

The later owner control supersedes the old packet-only B15 wording and keeps all FEI workers on the all-gate inequality. For a pivot coordinate `j` with bias `t`, account04/B17 proved the exact source-valid restriction cocycle

\[
D_\Gamma(G)=(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)+\mathcal R_{\Gamma,j}+\mathcal C_j,
\]

with the genuine information credit

\[
\boxed{\mathcal C_j=H(B\mid S)+I(S;J)\ge0}
\]

and quadratic currency

\[
\boxed{\mathcal W_j=t(1-t)\bigl(\delta_j-(r_1-r_0)^2\bigr)\ge0.}
\]

The newest applicable account02/B15 arithmetic handoff was also consumed at its proved scope. Its old Campaign-B harmonic-deletion residual is exactly

\[
\boxed{
D_{\rm del}=\beta H_2(\rho)-\mathbb E\log_2(K!)-\mathcal K_\rho,
\qquad \mathcal K_\rho\ge0,
}
\]

with a one-time valuation reserve `R(f)<=2J(f)<=2I(f)`. It proves that an unbounded valuation fee cannot be charged independently at every live deletion step. The lesson used here is the source-valid one: the KL/information credit stays in the physical remainder until it is paid. No packet integrality and no credit-free interpolation is assumed below.

## 2. Prime gate and the two-dimensional complementary-output surface

Use the four-input composition-prime gate

\[
B_0=1\iff \neg(x_2x_3)\wedge\neg(x_3x_4)\wedge\neg(x_4x_1).
\]

Let the product biases on `(x_1,x_2,x_3,x_4)` be `(p,q,t,r)`. Restrict on `x_3`:

\[
B_{0,0}=\operatorname{NAND}(x_1,x_4),
\qquad
B_{0,1}=(1-x_2)(1-x_4).
\]

This run enlarges the previously certified one-dimensional slice by allowing the selector bias `t` to vary freely while keeping the two child outputs complementary:

\[
\boxed{
pr=\frac14,
\qquad
(1-q)(1-r)=\frac14,
\qquad
\frac14\le r\le\frac34,
\qquad
0\le t\le1.
}
\tag{2.1}
\]

Write

\[
u=2r-1\in[-1/2,1/2].
\]

Then

\[
p=\frac1{2(1+u)},
\qquad
1-q=\frac1{2(1-u)}.
\]

The two restriction output probabilities are always `3/4` and `1/4`, their physical disagreement probability is always

\[
\delta_3=\frac12,
\]

and hence the local quadratic currency is exactly

\[
\boxed{\mathcal W_3=\frac{t(1-t)}4.}
\tag{2.2}
\]

## 3. Exact branch uncertainty

On the remaining coordinates, the two restriction spectral laws overlap on exactly two supports: `emptyset` and `{x_4}`. Their masses on the empty support are both `1/4`. Their masses on `{x_4}` are

\[
A(u)=\frac{1-u}{4(1+u)},
\qquad
B(u)=\frac{1+u}{4(1-u)},
\qquad
A(u)B(u)=\frac1{16}.
\tag{3.1}
\]

Every other spectral support belongs to only one branch, so it reveals the branch label exactly. Therefore the first, KL/branch part of the information credit has the exact closed form

\[
\boxed{
H(B\mid S)
=\frac14 h_2(t)+T\,h_2(\eta),
}
\tag{3.2}
\]

where

\[
T=(1-t)A+tB,
\qquad
\eta=\frac{tB}{T}.
\tag{3.3}
\]

This identity is source-exact; no arbitrary probability-law relaxation has been introduced.

## 4. Main theorem — the branch/KL credit alone pays six local currencies

### Theorem 4.1

For every point of the full surface (2.1), including all boundary limits,

\[
\boxed{
H(B\mid S)\ge 6\,\mathcal W_3.
}
\tag{4.1}
\]

Consequently the complete information credit obeys

\[
\boxed{
\mathcal C_3=H(B\mid S)+I(S;J)
\ge 6\,\mathcal W_3.
}
\tag{4.2}
\]

Thus, throughout this genuinely biased two-dimensional family of the composition-prime gate `B0`, the exact negative branch/KL credit returns at least six units of the same Poincare-gap currency used to normalize the all-gate margin.

### Proof

The assertion is symmetric under `(t,u) -> (1-t,-u)`, so assume `0<=t<=1/2` and put

\[
x=1-2t\in[0,1],
\qquad z=t(1-t)=\frac{1-x^2}{4}.
\]

We use the elementary binary-entropy bound

\[
h_2(y)\ge4y(1-y),\qquad 0\le y\le1.
\tag{4.3}
\]

Applying (4.3) to the second term of (3.2), and using `AB=1/16`, gives

\[
T h_2(\eta)
\ge4T\eta(1-\eta)
=\frac{z}{4T}.
\tag{4.4}
\]

Because `A in [1/12,3/4]`, `B=1/(16A)`, and

\[
T=(1-t)A+\frac{t}{16A},
\]

`T` is convex as a function of `A`. Its maximum on this interval is therefore at an endpoint. For `t<=1/2` the larger endpoint is

\[
T\le \frac34-\frac{2t}{3}=\frac{5+4x}{12}.
\tag{4.5}
\]

Dividing (3.2) by `W_3=z/4`, equations (4.4)-(4.5) yield

\[
\frac{H(B\mid S)}{\mathcal W_3}
\ge \frac{h_2(t)}{z}+\frac{12}{5+4x}.
\tag{4.6}
\]

It remains to prove that the right side is at least six.

For `0<=x<=1`, set

\[
\Psi(x)=(1+x)\ln(1+x)+(1-x)\ln(1-x).
\]

The exact even-power expansion is

\[
\Psi(x)=\sum_{n\ge1}\frac{x^{2n}}{n(2n-1)},
\qquad
\Psi(1)=2\ln2.
\tag{4.7}
\]

The first two terms are `x^2+x^4/6`; since `x^{2n}<=x^6` for every `n>=3`, the remaining coefficient sum is `2 ln 2-7/6`, and hence

\[
\Psi(x)
\le x^2+\frac{x^4}{6}+\left(2\ln2-\frac76\right)x^6.
\tag{4.8}
\]

Since

\[
h_2(t)=1-\frac{\Psi(x)}{2\ln2},
\]

substituting (4.8) into (4.6) and subtracting six gives

\[
\frac{N(x)}{3\ln2\,(5+4x)},
\tag{4.9}
\]

where

\[
\begin{aligned}
N(x)={}&\ln2\,(48x^5+60x^4+48x^3+60x^2-24x+6)\\
&-(28x^5+35x^4+24x^3+30x^2).
\end{aligned}
\tag{4.10}
\]

The coefficient multiplying `ln 2` is positive on `[0,1]`, because

\[
60x^2-24x+6=60(x-1/5)^2+18/5
\]

and all its remaining terms are nonnegative. Also

\[
\ln2=2\operatorname{atanh}(1/3)
>2\left(\frac13+\frac1{81}\right)
=\frac{56}{81}>\frac{17}{25}.
\tag{4.11}
\]

Therefore

\[
N(x)>
\frac1{25}P(x),
\]

where

\[
P(x)=116x^5+145x^4+216x^3+270x^2-408x+102.
\tag{4.12}
\]

Finally, `P` is positive on `[0,1]`. One exact finite certificate is its degree-five Bernstein representation on the following rational subdivision; every displayed Bernstein coefficient is positive:

- `[0,2/5]`:
  `(102, 1734/25, 1026/25, 11514/625, 454/125, 2262/3125)`;
- `[2/5,9/20]`:
  `(2262/3125, 1126/3125, 9123/50000, 9909/50000, 332697/800000, 337773/400000)`;
- `[9/20,1/2]`:
  `(337773/400000, 203679/160000, 76497/40000, 22173/8000, 193/50, 83/16)`;
- `[1/2,1]`:
  `(83/16, 1477/80, 1113/20, 1267/10, 247, 441)`.

Because the Bernstein basis is nonnegative on each interval, `P>=0`, so (4.9) is nonnegative. This proves (4.1). Equation (4.2) follows from `I(S;J)>=0`. Boundary cases `t=0,1` have `W_3=0` and follow by continuity. QED.

## 5. What this does and does not pay

The exact local unpaid object in the all-gate restriction cocycle is

\[
\boxed{\mathcal R_{\Gamma,3}+\mathcal C_3.}
\]

Theorem 4.1 pays a uniform, source-valid part of that object:

\[
\mathcal C_3\ge6\mathcal W_3.
\]

This is a genuine two-dimensional extension of the previous `t=1/2` credit calculation. It also gives the credit in the same units as the normalized gate margin, rather than as an unscaled entropy number.

It is **not** yet a proof that `B0` satisfies the stable all-gate candidate on the entire surface (2.1): the raw term `R_{Gamma,3}` still has to be combined with the remaining mutual-information credit `I(S;J)` and the two certified child defects. At `t=1/2`, the stronger exact calculation from the preceding B15 run gives a much larger total credit and already closes that one-dimensional slice. The present theorem proves a uniform floor for every `t`, but does not claim that the floor alone pays the worst possible raw root debit.

A dense diagnostic grid, which is not part of the proof, found

\[
\min H(B\mid S)/\mathcal W_3\approx6.9491372,
\]

so the proved constant six has visible slack. The exact checker verifies only the rational Bernstein certificate and the algebraic reduction; the grid is included only as a falsification check.

## 6. Verification

`CHECKER.py` uses only the Python standard library. It reconstructs the polynomial `P` exactly over `Fraction`, verifies the four Bernstein representations coefficient-by-coefficient, verifies `56/81>17/25`, and performs a dense floating diagnostic over the physical surface. The captured output is in `CHECKER_OUTPUT.txt`.

The theorem does not depend on floating-point extrapolation.

## 7. Next missing implication

The natural next step on this same prime gate is now sharply localized: retain the full exact credit

\[
H(B\mid S)+I(S;J)
\]

and prove, or falsify at an actual interior bias, that

\[
(1-t)D_{\Gamma_*}(\operatorname{NAND}_{p,r})
+tD_{\Gamma_*}(\operatorname{AND}_{1-q,1-r})
+\mathcal R_{\Gamma_*,3}+\mathcal C_3\ge0
\]

on the complementary-output surface (2.1), where `Gamma_*` is the stable candidate. Theorem 4.1 removes the possibility that the branch/KL credit collapses relative to the local Poincare currency; any remaining obstruction must come from the raw root term after this six-currency refund, or from the exact vertical-overlap credit being too small at the same point.

No novelty or publication-priority claim is made here without a broader literature review.
