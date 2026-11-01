SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-24T06:55:22.857152Z.
attacking: the rank-one plus four-diagonal rough survivor; replace absolute support radius by a translation-invariant product-diameter obstruction while retaining the separable and entangled tails.

# fleet02/B13 r11 — translation-invariant diameter escape for the rank-one/four-diagonal rough survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T065522Z-fleet02-B13-qform-r11`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING OBSTRUCTION / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No moment, compact-support assumption on the original laws, log-concavity, connected support, diagonal-basis reduction, post-rotation independence, common support diameter, fixed fragment count, attained global bathtub optimizer, or law-uniform deletion of a coefficient-small quadratic term is used.

## 1. First unpaid implication

The first unpaid implication is now

`QFORM-DIAMETER-BANK-TO-ROUGH-RECEIVER-v1`:

> In the latest partner fleet03/B13 rank-one-plus-four-diagonal normal form, convert the forced translation-invariant spread of the original coordinate product sets into an affine-uniform density payment while keeping both the O(rho^-1) separable diagonal tail and the retained secondary carrier inside the actual phase. Otherwise construct a genuine bounded-finite-union product-indicator counterexample sequence satisfying the spread lower bounds proved below.

This is narrower than the previous `QFORM-REMOTE-SUPPORT-RANK1-4DIAG-RECEIVER-v1`: remote translation alone has now been removed as a possible mechanism.

## 2. Fresh source state and compatible completed inputs


The latest completed designated-partner result at refresh is fleet03/B13 r45:

- `yspennstate/math-open-problems@a1ccc98be0cd4752de1b2b29e4c46f8193854757`,
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260924T063322Z-fleet03-B13-qform-r45/REPORT.md`.

Its proved multi-square theorem applies to the exact diffuse rank-two chamber

\[
A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad \max_i\|u_i\|^2\le1/3,
\]
with arbitrary cap-one product laws and arbitrary deterministic affine terms. For two selected physical diagonal coefficients bounded below, it gives

\[
\|p_Q\|_\infty\le C\bigl(1+|\det\Lambda|^{-3/7}\bigr),
\]
up to the stated fixed diagonal-scale factor. Applied to a high-density survivor, r45 obtains the physical normal form

\[
\boxed{
A=D_C+\lambda_1 vv^T+E_{\rm sep}+E_{\rm ent},\qquad |C|\le4,
}
\tag{2.1}
\]
with

\[
\|E_{\rm sep}\|_{op}\le {C_D\over\rho},\qquad
C_D=2\sqrt{30\pi}=19.41625912555699\ldots,
\tag{2.2}
\]

\[
\|E_{\rm ent}\|_{op}=O(\rho^{-7/6})=o(\rho^{-1}).
\tag{2.3}
\]
Here `E_sep` is the retained diagonal tail and `E_ent` is the retained secondary carrier. r45 also supplies a physical-star/ultra-collapse alternative; none of those coefficient-small terms is discarded probabilistically.

The prior fleet02/B13 grouping theorem at

- `yspennstate/math-open-problems@2af615c6d649e207191127733fc6dd180db14944`

proves that a matrix supported by at most `m` latent one-dimensional direction classes plus a diagonal supported on finitely many named physical coordinates can be grouped into finitely many **independent original-coordinate variables**, after which the fixed-dimensional QFORM theorem applies. In particular, if

\[
M=D_C+\lambda vv^T,\qquad |C|\le4,
\tag{2.4}
\]

and `s_3(M)>=1`, every affine M-form has density at most

\[
250e\,5(8+\log5).
\]
By coefficient scaling, if instead `s_3(M)>=1/2`, every affine M-form has density at most

\[
\boxed{
C_M:=500e\,5(8+\log5)
=65302.90114768759\ldots .
}
\tag{2.5}
\]
The affine uniformity is essential below.

Finally the owner-pinned source

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`

contains the completed unconditional fifth-volume theorem D5. It will be applied in Section 7.

## 3. Optimizer-free finite-union interface

The partner line includes the completed no-attainment extremal-product transfer: a strict slab violation for arbitrary cap-one marginals can be transferred, with arbitrarily small ratio loss, to a finite convex-mixture component in which every marginal is an indicator of a bounded finite union of intervals of total measure one. The product error is controlled by the usual telescoping inequality

\[
\left\|\prod_i f_i-\prod_i g_i\right\|_1
\le \sum_i\|f_i-g_i\|_1.
\tag{3.1}
\]

No common support diameter or uniform fragment count is produced or needed. Therefore it is legitimate, for a strict counterexample-sequence argument, to work with a **single bounded finite-union witness at a time** and derive a lower bound on how its support geometry must deteriorate. The bounds below do not assert an attained global optimizer.

## 4. New theorem: translation-invariant product-diameter escape

### Theorem 4.1 — `QFORM-TRANSLATION-INVARIANT-DIAMETER-ESCAPE-v1`

Let `X_i` be independent and uniform on bounded measurable sets `E_i` of Lebesgue measure one. Let

\[
A=M+F
\tag{4.1}
\]

be symmetric. Assume there is a constant `C_M` such that for **every** deterministic affine vector `b` and scalar `c`, the random variable

\[
X^TMX+b^TX+c
\]

has density bounded by `C_M`; equivalently the same statement holds after arbitrary translations of the individual product factors.

For each coordinate define

\[
a_i=\operatorname*{ess\,inf}E_i,\qquad
b_i=\operatorname*{ess\,sup}E_i,
\]

\[
m_i={a_i+b_i\over2},\qquad
h_i={b_i-a_i\over2},\qquad
H^2=\sum_i h_i^2.
\tag{4.2}
\]

Let `J` be an interval and

\[
\rho={\Pr\{X^TAX\in J\}\over |J|}.
\tag{4.3}
\]

Then with

\[
\delta:=\sup_{|y_i|\le h_i}|y^TFy|
\tag{4.4}
\]

one has

\[
\boxed{
\rho\le C_M\left(1+{2\delta\over |J|}\right).
}
\tag{4.5}
\]

Consequently

\[
\delta\le\|F\|_{op}H^2,
\tag{4.6}
\]

and whenever `rho>=2 C_M`,

\[
\boxed{
H^2\ge {\rho |J|\over4C_M\|F\|_{op}}.
}
\tag{4.7}
\]

If in addition

\[
\|F\|_{op}\le {C_F\over\rho},
\]

then

\[
\boxed{
H^2\ge {\rho^2|J|\over4C_MC_F}.
}
\tag{4.8}
\]

Equivalently, writing `diam(E_i)=2h_i`,

\[
\boxed{
\sum_i\operatorname{diam}(E_i)^2
\ge {\rho^2|J|\over C_MC_F}.
}
\tag{4.9}
\]

### Proof

Write

\[
X=m+Y.
\]

Then the coordinates of `Y` remain independent cap-one variables, each uniform on the translated set `E_i-m_i`, and

\[
|Y_i|\le h_i\quad\text{a.s.}
\tag{4.10}
\]

Expand the **actual** form:

\[
X^TAX
=Y^TAY+2(Am)^TY+m^TAm.
\]

Using `A=M+F`, regroup it as

\[
X^TAX
=\underbrace{Y^TMY+2(Am)^TY+m^TAm}_{Q_0(Y)}
+Y^TFY.
\tag{4.11}
\]

The possibly enormous translation `m` occurs only in the deterministic affine term of `Q_0`. By hypothesis, `Q_0` has density at most `C_M`, uniformly in this affine term. On the support (4.10),

\[
|Y^TFY|\le\delta.
\]

Therefore

\[
\{X^TAX\in J\}
\subseteq
\{Q_0(Y)\in J+[-\delta,\delta]\},
\]

and hence

\[
\Pr\{X^TAX\in J\}
\le C_M(|J|+2\delta).
\]

Divide by `|J|` to obtain (4.5). Also

\[
|y^TFy|\le\|F\|_{op}\|y\|_2^2
\le\|F\|_{op}H^2,
\]

which proves (4.6). If `rho>=2C_M`, equation (4.5) implies

\[
{\rho\over2}\le {2C_M\delta\over|J|},
\]

so

\[
\delta\ge {\rho|J|\over4C_M}.
\]

Combine with (4.6) to obtain (4.7), then substitute `||F||op<=C_F/rho` to obtain (4.8) and multiply by four to obtain (4.9). `QED`

### Why this matters

The previous absolute-radius obstruction could be saturated simply by translating a compact unit-measure factor to distance `R`. Theorem 4.1 proves that this is a false mechanism once the paid core is affine-uniform: **translations are exactly absorbed**, and only genuine within-coordinate support spread/fragmentation can activate the retained rough coefficient tail.

This is especially relevant because arbitrary cap-one laws may be supported on fragments separated by arbitrarily large gaps; the theorem preserves that possibility rather than suppressing it.

## 5. Application to the latest partner r45 normal form

Let

\[
M=D_C+\lambda_1vv^T,\qquad
F=E_{\rm sep}+E_{\rm ent}
\tag{5.1}
\]

in the partner normal form (2.1). Since the target has `s_3(A)>=1`, Weyl gives

\[
s_3(M)\ge1-\|F\|_{op}.
\tag{5.2}
\]

By (2.2)-(2.3), `||F||op=o(1)` along any putative sequence `rho->infinity`; hence for all sufficiently large `rho`,

\[
s_3(M)\ge1/2.
\tag{5.3}
\]

The finite-direction grouping theorem therefore pays every affine `M`-form with the explicit `C_M` in (2.5).

Write the retained secondary carrier as

\[
E_{\rm ent}=\lambda_2ww^T,\qquad \|w\|_2=1.
\tag{5.4}
\]

For the centered support widths (4.2), define

\[
H_{\rm tail}^2:=\sum_{i\notin C}h_i^2,
\qquad
W_w:=\sum_i |w_i|h_i.
\tag{5.5}
\]

The diagonal tail is supported away from the four retained diagonal centers, so

\[
|Y^TE_{\rm sep}Y|
\le {C_D\over\rho}H_{\rm tail}^2.
\tag{5.6}
\]

Also

\[
|Y^TE_{\rm ent}Y|
=|\lambda_2|(w^TY)^2
\le |\lambda_2|W_w^2.
\tag{5.7}
\]

Thus Theorem 4.1 gives, for every sufficiently large witness with `rho>=2C_M`,

\[
\boxed{
C_DH_{\rm tail}^2+\rho|\lambda_2|W_w^2
\ge {\rho^2|J|\over4C_M}.
}
\tag{5.8}
\]

Therefore at least one of the following occurs:

\[
\boxed{
H_{\rm tail}^2
\ge {\rho^2|J|\over8C_MC_D},
}
\tag{5.9}
\]

or

\[
\boxed{
W_w^2
\ge {\rho|J|\over8C_M|\lambda_2|}.
}
\tag{5.10}
\]

The first denominator is explicit:

\[
8C_MC_D
=10143504.402673082\ldots .
\tag{5.11}
\]

Partner r45 proves the universal estimate

\[
|\lambda_2|\le K_{\rm ent}\rho^{-7/6}
\tag{5.12}
\]

for some universal finite `K_ent` in its high-density branch. Substitution in (5.10) yields the new product-geometric obstruction

\[
\boxed{
W_w^2
\ge {\rho^{13/6}|J|\over8C_MK_{\rm ent}}.
}
\tag{5.13}
\]

Thus a diverging counterexample sequence in the partner chamber must develop either quadratic aggregate diameter in the distributed diagonal bank at scale at least `rho^2 |J|`, or projective support width along the secondary carrier at scale at least `rho^(13/6)|J|`. Neither can be produced merely by translating the entire coordinate supports.

A stronger exponent is available if one also imports the previously completed fleet02/B13 lower-bound bootstrap `math-open-problems@21a48883fa1152dac179f3f6ebe1725785793520`, which combines the physical three-coordinate theorem with the two-square receiver to obtain `|lambda_2|=O(rho^-7/3)`. Then (5.10) improves to

\[
W_w^2\gtrsim \rho^{10/3}|J|.
\tag{5.14}
\]

Equation (5.13), however, already follows from the designated partner alone and is the source-minimal statement of the new theorem.

## 6. Why this does not assume a bounded-support extremizer

The finite-union reduction is used in exactly the permitted direction. Given a strict arbitrary-density violation, approximate the marginals in `L^1` by finite convex mixtures of bounded finite-union unit-measure indicators. Expanding the product mixture and using (3.1), one component still has almost the same slab ratio. Theorem 4.1 then gives a **lower bound on that component's widths**.

As the target ratio grows, the widths in (5.9) or (5.13) are allowed — indeed forced — to diverge. There is no common diameter bound, no compactness assertion, no centered interval conclusion, and no assumed attainment of a bathtub optimum.

## 7. Required pinned Fourier result applied to a real obstruction

Let `B=A[I,J]` be any disjoint original-coordinate physical cross block. The completed D5 theorem in the pinned source says

\[
\|p_Q\|_\infty
\le5\sqrt{2e}\,e_5(B^TB)^{-1/10}.
\tag{7.1}
\]

Therefore every slab witness of ratio `rho` necessarily satisfies

\[
\boxed{
 e_5(B^TB)
\le\left({5\sqrt{2e}\over\rho}\right)^{10}
}
\tag{7.2}
\]

for **every** physical cut, and since

\[
e_5(B^TB)\ge s_5(B)^{10},
\]

also

\[
\boxed{
 s_5(B)\le {5\sqrt{2e}\over\rho}
 = {11.6582199079856\ldots\over\rho}.
}
\tag{7.3}
\]

This is an unconditional physical-coordinate obstruction with no marginal gate. Combining (7.2) with the new diameter theorem shows what any genuine counterexample sequence must do simultaneously:

1. lose fifth physical cross-volume on **every** original-coordinate cut at rate `rho^-10`, while
2. in the partner rank-one/four-diagonal endpoint, create diverging translation-invariant support width in the diagonal tail or along the retained secondary carrier.

The numerical searches in `COUNTEREXAMPLE_SEARCH.md` report no growing family, but those observations are not used in this proof.

## 8. Remaining gap

The new theorem does not yet convert large translation-invariant width into smoothing. Arbitrary unit-measure sets can have tiny total measure spread over extremely remote fragments, and the tail can interact coherently with that geometry. A valid next receiver must exploit product structure before taking absolute values, or else construct a genuine finite-union counterexample sequence satisfying (5.8) and (7.2) simultaneously.

The first unpaid implication is therefore exactly `QFORM-DIAMETER-BANK-TO-ROUGH-RECEIVER-v1`. A successful proof must retain the rough tail in the phase; a statement that `||F||op=o(1)` is not enough under the target's unbounded-support laws.
