# MOC4 account01/B08 — chain-cube face propagation and a low-frequency payment no-go

Run: `20260922T040837Z-b08-moc4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Target: complex-normal `4 x 4` Marcus–de Oliveira inclusion  
Outcome: **ESSENTIAL_STEP_APPLIED**; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact team state consumed

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{v_\sigma:=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

This run uses four exact completed team inputs.

1. **Campaign lead account03/B07**, `MOC4-V4-PAIR-GAP-CEILING-v1`, report blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`. For any true-unitary support violation of gap `gamma`, the V4 roof and all six pair roofs give
   \[
   0<\gamma\le\frac{3d-\Delta-G/2}{4}.
   \]
   Its exact low-frequency relaxation witness shows that group-algebra roofs alone do not close the residual reserve; genuine same-unitary/spectral compatibility is still required.

2. **Named assigned partner account02/B09**, run `20260922T034112Z-account02-B09-MOC4-r14`, theorem `MOC4-ZERO-FIBER-HAAR-LIFT-v1`, report blob `20a1ea240bb65b81b880cad265e4db5f225d2a8a`. On a true zero-entry face, fixing the first row/column leaves a `U(2)` fiber. Haar averaging that residual fiber has one exact positive permutation law simultaneously reproducing every compound-minor marginal. The support on the fiber is a quaternion quadratic form `q^T H q`, and a hypothetical support violation of gap `gamma` pays exact curvature at least `8 gamma`. I use this to keep the zero-entry branch separate: the present calculation is not allowed to replace the partner's true-unitary fiber by an arbitrary compound array.

3. **account03/B08**, run `20260922T031831Z-a03-b08-moc4-r11`, theorem `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`, report blob `cd4264eb161c05fd44ff188490e4e0354295213c`. For
   \[
   U_0=R_{12}(c_1,s_1)R_{23}(c_2,s_2)R_{34}(c_3,s_3)
   \]
   and a closing `SU(2)` gate on columns `1,4`, the determinant image is the exact filled ellipse
   \[
   D=c^2D_0+s^2D_1+2cs\,\Re\zeta\,K,
   \]
   with
   \[
   K=c_1s_1s_2s_3(v_{4123}-v_{1423}).
   \]
   For a support functional `L`, writing `M=max_sigma L(v_sigma)`, `delta_j=M-L(D_j)`, and `C=L(K)`, the entire closing orbit is safe iff
   \[
   C^2\le\delta_0\delta_1. \tag{1}
   \]

4. **account02/B08**, `MOC4-CIRCLE-FACE-REDUCTION-v1`, report blob `5e52a9d9463e30108d1de0c5269d693dfd4e4ef3`. Its theorem `MOC-COMMON-CIRCLE-v1` proves MOC in every dimension whenever the signed spectra
   \[
   \{-a_1,\dots,-a_4,b_1,\dots,b_4\}
   \]
   lie on one generalized circle, by an exact Möbius reduction to the Hermitian theorem.

The present mechanism is deliberately different from the preceding common-positive-lift/facet-separator attempts: it works in the **spectral product geometry of an exposed support face**.

## 2. A sharp low-frequency warning: compound-event structure alone does not prove (1)

Use the exact chain parameters

\[
(c_1,s_1)=(3/5,4/5),\qquad
(c_2,s_2)=(c_3,s_3)=(7/25,24/25).
\]

Put `x=9/25`, `y=16/25`, `u=49/625`, `q=(1-u)^2`, and

\[
\alpha=c_1s_1s_2s_3.
\]

The two forest-Givens endpoints have the exact positive permutation lifts

\[
\begin{aligned}
p_0=&\{1234:xu^2,\ 1243:xu(1-u),\ 1324:x(1-u)u,\ 1423:xq,\\
&2134:yu^2,\ 2143:yu(1-u),\ 3124:y(1-u)u,\ 4123:yq\},
\end{aligned}
\]

and

\[
\begin{aligned}
p_1=&\{1423:yq,\ 2413:yu(1-u),\ 2431:yu^2,\ 3421:y(1-u)u,\\
&4123:xq,\ 4213:xu(1-u),\ 4231:xu^2,\ 4321:x(1-u)u\}.
\end{aligned}
\]

Now define on `S_4` the nonnegative deficit

\[
\begin{aligned}
d(\sigma)=1&-1_{\sigma(1)=2}+1_{\sigma(1)=3}
-1_{\sigma(2)=2}-1_{\sigma(3)=2}\\
&-1_{\sigma(\{1,2\})=\{1,3\}}
+1_{\sigma(\{1,3\})=\{1,2\}}. \tag{2}
\end{aligned}
\]

It takes only the values `0,1,2`, with thirteen zeros. Because (2) is an explicit linear combination of one-point and two-subset compound events, it lies in the exact exterior-power low-frequency space `[4] + [31] + [22]`. Equivalently, if `A` denotes the central adjacency operator obtained by summing the six transpositions on `S_4`, then the exact verifier checks

\[
A(A-2I)(A-6I)d=0. \tag{3}
\]

Thus (2) obeys the same **linear** representation-theoretic frequency restriction as a determinant support array; it is not an arbitrary 24-vector.

Nevertheless, for the chain above,

\[
\delta_0=\sum_\sigma p_0(\sigma)d(\sigma)
=\frac{2985984}{9765625},
\]

\[
\delta_1=\sum_\sigma p_1(\sigma)d(\sigma)
=\frac{6211584}{9765625},
\]

and, because `d(4123)=0`, `d(1423)=1`, the formal chord payment has

\[
C^2=\alpha^2(d(1423)-d(4123))^2
=\frac{47775744}{244140625}.
\]

Exact arithmetic gives

\[
\boxed{\delta_0\delta_1-C^2
=-\frac{114709561344}{95367431640625}<0} \tag{4}
\]

and

\[
\frac{C^2}{\delta_0\delta_1}=\frac{390625}{388224}>1. \tag{5}
\]

Therefore the tempting statement

> every nonnegative deficit in the compound-event / `[4]+[31]+[22]` span automatically satisfies the one-cycle payment

is **false**. This is a relaxation counterexample only, not a MOC4 counterexample. In particular, the lead's low-frequency identities and arbitrary same-cardinality compound marginals cannot by themselves prove the one-cycle theorem. The nonlinear fact that the 24 values come from the *same two spectra* is essential.

## 3. New theorem: the exact bad face propagates to the solved common-circle locus

The relaxation witness (2) has a highly structured zero face. The following theorem explains why that exact bad face cannot survive generically as a genuine spectral obstruction.

Write

\[
x_i=-a_i,\qquad y_j=b_j,\qquad z_{ij}=y_j-x_i=a_i+b_j,
\]

so

\[
v_\sigma=\prod_i z_{i,\sigma(i)}.
\]

### Theorem — `MOC4-CHAIN-CUBE-FACE-PROPAGATION-v1`

Assume the `x_i` are pairwise distinct, the `y_j` are pairwise distinct, and every `z_{ij}` is nonzero. Let `L(w)=Re(eta w)` with `eta !=0`. Suppose the following eleven spectral vertices all have one common support value `M`:

\[
\boxed{1234,1243,2134,2143,1324,3124,2431,4231,2341,4123,4321.} \tag{6}
\]

Then all eight signed spectral points

\[
x_1,x_2,x_3,x_4,y_1,y_2,y_3,y_4
\]

lie on one generalized circle. Consequently, by account02/B08 `MOC-COMMON-CIRCLE-v1`, the MOC inclusion holds for the corresponding normal pair for every relative unitary.

### Proof

For two permutations differing only by swapping the assignments in rows `i,j`, with columns `r,s`, the product difference factors as

\[
v_\sigma-v_{(ij)\sigma}
=(x_i-x_j)(y_r-y_s)\prod_{k\ne i,j}z_{k,\sigma(k)}. \tag{7}
\]

Every edge used below joins two vertices in (6), so its endpoints have equal `L`-value. Hence every nonzero edge difference lies in the one-real-dimensional kernel of `L`; the ratio of any two such edge differences is real. The generic assumptions make all displayed factors nonzero.

First compare the two tied `34`-swap edges:

\[
\frac{v_{1234}-v_{1243}}{v_{2134}-v_{2143}}
=\frac{z_{11}z_{22}}{z_{12}z_{21}}\in\mathbb R. \tag{8}
\]

The right side is a cross ratio, so `x_1,x_2,y_1,y_2` lie on one generalized circle; call it `C`.

Next compare the tied edges `1234--1324` and `2134--3124`:

\[
\frac{v_{1234}-v_{1324}}{v_{2134}-v_{3124}}
=\frac{(x_2-x_3)z_{11}}{(x_1-x_3)z_{21}}\in\mathbb R. \tag{9}
\]

This is the cross-ratio criterion for `x_1,x_2,x_3,y_1`, so `x_3` lies on `C`.

Similarly, using `2134--2431` and `1234--4231`,

\[
\frac{v_{2134}-v_{2431}}{v_{1234}-v_{4231}}
=\frac{(x_2-x_4)z_{12}}{(x_1-x_4)z_{22}}\in\mathbb R. \tag{10}
\]

Thus `x_1,x_2,x_4,y_2` are concyclic. Since `x_1,x_2,y_2` already lie on `C`, uniqueness of the generalized circle through three distinct points gives `x_4 in C`.

Now compare `2143--2341` with `4123--4321`:

\[
\frac{v_{2143}-v_{2341}}{v_{4123}-v_{4321}}
=\frac{z_{12}z_{34}}{z_{14}z_{32}}\in\mathbb R. \tag{11}
\]

Hence `x_1,x_3,y_2,y_4` are concyclic. The first three are already on `C`, so `y_4 in C`.

Finally compare `2143--4123` with `2341--4321`:

\[
\frac{v_{2143}-v_{4123}}{v_{2341}-v_{4321}}
=\frac{z_{21}z_{43}}{z_{23}z_{41}}\in\mathbb R. \tag{12}
\]

Thus `x_2,x_4,y_1,y_3` are concyclic. Again the first three lie on `C`, so `y_3 in C`. Therefore all eight signed spectral points lie on `C`. `QED`

The exact bad deficit (2) vanishes on every vertex in (6). Thus if it were realized by a **generic** genuine spectral support face, Theorem (6)-(12) would force the pair onto the already-solved common-circle locus. This identifies precisely what the abstract low-frequency witness was missing: nonlinear cross-ratio compatibility of the same spectra.

## 4. Why this is useful rather than merely another no-go

The conclusion is stronger than observing that (2) is not known to be spectral. It exhibits an explicit mechanism by which the spectral manifold rejects the bad direction:

- the low-frequency relaxation can make eleven chain-cube vertices simultaneously support-tight while separating `1423`;
- a genuine spectral product array cannot do this generically without forcing five exact real cross-ratios;
- those five cross-ratios put the entire signed spectrum on one generalized circle;
- the common-circle theorem then closes the *full* normal-matrix problem, not just the chain orbit.

Thus exact face degeneracy is not the dangerous regime. A genuine counterexample to the one-cycle payment, if one exists, must live in a **transverse, strictly non-common-circle perturbation** where at least one of the eleven deficits in (6) is positive, or in one of the explicitly lower-dimensional repeated/cross-sum strata where the generic ratio proof must be replaced by the boundary machinery.

This also explains the repeated numerical observation from the one-cycle search that payment ratios approach one near cross-sum/common-circle degeneracies rather than producing a robust interior reversal; that observation is heuristic only and is not used in the theorem.

## 5. Compact conditional end-to-end argument

A source-valid full proof would now have the following form.

1. Reduce singular/repeated/common-reducing boundary cases through the established boundary results; common generalized-circle signed spectra are solved exactly by the Möbius/Hermitian reduction.
2. If a maximizing true unitary develops a zero entry, apply the **assigned partner account02/B09 `MOC4-ZERO-FIBER-HAAR-LIFT-v1`**. Its exact Haar common lift and quaternion Hessian payment reduce that branch to the remaining matrix inequality `M I-H >=0`; no arbitrary bistochastic replacement is used.
3. On the generic nonzero one-cycle branch, use account03/B08's exact ellipse formula. The only scalar obstruction is (1).
4. Do **not** try to prove (1) from nonnegative deficits plus low-frequency/compound identities alone: (2)-(5) are an exact counterexample to that relaxation.
5. Use the spectral product structure. The present theorem closes the exact eleven-tie face by forcing the common-circle locus. What remains is the transverse strict-face case.
6. Prove the quantitative transverse version below. Then the one-cycle mechanism is closed. Combine it with the lead's V4/pair-gap ceiling and partner zero-face payment to continue toward the strict-interior residual `MOC4-RESIDUAL-PR-RESERVE-v1`.

## 6. First essential missing implication

The first missing implication after this run is now narrower than `C^2<=delta_0 delta_1` for an arbitrary low-frequency deficit.

> **`MOC4-CHAIN-CUBE-TRANSVERSE-COLLAR-v1` (OPEN).** For a genuine spectral support facet in the generic simple/nonzero-sum branch, quantify the five cross-ratio deviations in (8)-(12) in terms of the eleven support deficits in (6), and prove that this transverse departure from the common-circle locus supplies enough positive payment to force
> \[
> C^2\le\delta_0\delta_1.
> \]
> Equivalently, exhibit actual spectra/support data with strict reverse inequality; by `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1` that would be a genuine true-unitary MOC4 counterexample.

The exact tie theorem proves the zero-deficit endpoint of this proposed collar. The next useful calculation is therefore a **stability estimate for cross-ratio phases**, not another arbitrary common-permutation lift or another low-frequency transport cut.

## 7. Verification and non-claims

`verify_chain_face.py` uses only standard-library exact `Fraction`/integer arithmetic. It checks:

- the explicit compound-event formula (2), its values, and the eleven required ties;
- the exact low-frequency annihilator (3);
- both endpoint probability laws;
- the exact values of `delta_0`, `delta_1`, `C^2`;
- the strict relaxation failure (4)-(5).

The cross-ratio theorem is algebraic and proved above; it does not depend on floating-point search.

**Honest status:** `ESSENTIAL_STEP_APPLIED`; the spectral-independent payment relaxation is refuted, the exact bad face is generically propagated into a solved common-circle locus, and full MOC4 remains open. No target counterexample is claimed.

No benchmark material, held-out key, credential, machine-local path, unrelated private data, email, Drive, public posting, paid/remote model/API/Codex, workflow invocation, scheduler mutation, or permission change was used.
