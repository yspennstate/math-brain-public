SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T08:21:41Z.
attacking: `QFORM-PAIRPIVOT-GLOBALNULL-TRANSITION-COMPILER-v1`; make the singular/near-singular three-hub transition stable without dividing by the three-hub determinant, and route the exact global-null face by conditioning on one ORIGINAL coordinate rather than rotating the product law.

# account03/B06 r55 — pair-pivot transition compiler and product-preserving global-null deletion

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.  
Fresh startup control: `yspennstate/math-research-brain@467587cfffec5397ce23d38f2f686437ccde3fc7`, OWNER CONTROL revision `2026-09-22.15`.  
Immediate B06 input: `QFORM-HUBSINGULAR-DIFFUSE-PAIRLOG-COMPILER-v1`, `yspennstate/math-open-problems@8bdce354a7ab12c52133f56532d8c7589cc94e98`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T075625Z-account03-B06-qform-r54/REPORT.md`.  
Analytic input actually applied: account03/B19 `QFORM-INDEFINITE-PAIR-ARBITRARY-HUB-v1`, source `yspennstate/math-open-problems@68a56e5fdbdc5b2812c544824e4ca584ec014263`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T030233Z-account03-B19-QFORM-r23/REPORT.md`.  
Pair-log input: `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.  
Designated partner actually applied in Section 8: account04/B06 `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`, source `yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`.  
Execution label: `WITHOUT_VERIFIED_BRAIN`; authenticated repository transport is not native learned-memory ingestion.

The full QFORM conjecture remains OPEN. This run does **not** prove the universal theorem. It supplies an exact, determinant-free transition compiler for a literal indefinite physical pair plus a third physical coordinate. The only zero-currency endpoint is an actual global null vector supported on those three original coordinates; that endpoint can be deleted by conditioning on one original coordinate while preserving the product structure and retaining three spectral directions at a universal scale.

## 1. Compact conditional end-to-end argument

Take three literal ORIGINAL coordinates, with the first two forming an invertible pair, and put all remaining original coordinates into a bank `Y`. Write the quadratic matrix as

\[
 A=
 \begin{pmatrix}
 P&r&M\\
 r^T&a&h^T\\
 M^T&h&C
 \end{pmatrix},
 \qquad P=P^T\in\mathbb R^{2\times2},\quad \det P\ne0.
 \tag{1.1}
\]

Set

\[
 q_H=\binom{-P^{-1}r}{1}\in\mathbb R^3,
 \qquad
 s:=a-r^TP^{-1}r,
 \qquad
 m:=h-M^TP^{-1}r.
 \tag{1.2}
\]

Completing only the literal physical pair gives, with `U` the pair and `X` the third physical coordinate,

\[
\begin{aligned}
Q={}&(U+P^{-1}(rX+MY))^TP(U+P^{-1}(rX+MY))\\
&+sX^2+2Xm^TY+Y^T(C-M^TP^{-1}M)Y.
\end{aligned}
\tag{1.3}
\]

Arbitrary affine terms merely add an affine coefficient to `X`, an affine term in `Y`, and a translation to the completed pair. All analytic receivers used below allow those terms. Thus the complete nonzero tail is retained.

If `P` is definite, conditioning on every coordinate outside this literal pair gives immediately

\[
 \|p_Q\|_\infty\le \pi/\sqrt{|\det P|}.
 \tag{1.4}
\]

The hard signature is therefore the invertible **indefinite** pair. In that case (1.3) has an exact trichotomy:

1. `m != 0`: the completed account03/B19 random-slope/pair theorem pays the full scalar output, uniformly in the value of `s`;
2. `m=0`, `s != 0`: the third literal scalar square gives a half-power small-ball estimate, which the pair-log theorem converts into a full scalar density bound;
3. `m=0`, `s=0`: `q=(q_H,0)` is an **exact global null vector of A**. No small denominator is paid; Section 5 deletes one original coordinate product-preservingly.

This is the first essential missing implication from r54. It is stable through the exact singular face and never divides by `det` of the three-hub block.

## 2. Exact algebra: the pair-pivot currencies are the global-null residual

Embed

\[
 q=(q_H,0_Y)=(-P^{-1}r,1,0_Y)^T.
\]

A direct block multiplication gives

\[
 \boxed{
 A q=(0,0,s,m)^T.
 }
 \tag{2.1}
\]

Here the first two entries are the pair coordinates, the next entry is the third physical coordinate, and the final vector is on the tail bank. Hence

\[
 \boxed{s=0\ \hbox{and}\ m=0\quad\Longleftrightarrow\quad q\in\ker A.}
 \tag{2.2}
\]

This identity is stronger than merely saying that a three-by-three Schur determinant is small. It identifies exactly which physical/tail quantities must vanish for the pair completion to become globally degenerate.

Also, if `F=A[H,H]` is the literal three-hub block, then

\[
 \det F=\det(P)\,s.
 \tag{2.3}
\]

Thus `s` is the exact three-hub determinant currency divided by the **fixed pair** determinant, while `m` is the complete post-pair cross row to every remaining original coordinate.

## 3. Nonzero star: existing random-slope theorem closes the transition uniformly in `s`

Assume now that `P` is indefinite and `m != 0`. The residual in (1.3) has the exact account03/B19 form

\[
 R=sX^2+2X(m^TY+\beta)+S(Y),
 \tag{3.1}
\]

where `S` contains all same-bank quadratic and affine curvature and `s` is arbitrary, including zero and arbitrarily small nonzero values.

The completed theorem `QFORM-INDEFINITE-PAIR-ARBITRARY-HUB-v1` applies with

\[
 D=|\det P|,
 \qquad \kappa=\sigma_{\min}(P).
\]

It gives the full ambient essential-density bound

\[
 \boxed{
 \|p_Q\|_\infty
 <12.714\,D^{-1/3}\kappa^{-1/6}\|m\|_2^{-1/6}.
 }
 \tag{3.2}
\]

The source theorem proves this by paying the random derivative before taking a reciprocal slope; it does **not** delete `sX^2` as a perturbation. Therefore (3.2) is genuinely uniform through `s=0` as long as `m` remains nonzero.

This directly improves the r53/r54 singular-hub transition: no heavy/diffuse split of the star is needed at this stage, and no reciprocal three-hub determinant appears.

## 4. Zero star but nonzero Schur square: an elementary half-power payment

Assume `m=0` and `s!=0`. Conditional on the tail bank `Y`, the residual scalar variable is

\[
 R=sX^2+\beta X+\gamma(Y).
\]

The following elementary estimate is translation-uniform.

### Lemma 4.1

If `X` has density at most one and `s!=0`, then for every `beta,c,t` and every `rho>0`,

\[
 \boxed{
 \Pr\{|sX^2+\beta X+c-t|<\rho\}
 \le 2\sqrt2\,|s|^{-1/2}\rho^{1/2}.
 }
 \tag{4.1}
\]

**Proof.** Complete the scalar square. Up to translation of `X` and output, the inverse image is

\[
 \{x:\ |x^2-u|<\rho/|s|\}.
\]

For `delta=rho/|s|`, its total Lebesgue length is at most `2 sqrt(2 delta)`: if `u<=delta`, it lies in `|x|<sqrt(2delta)`; if `u>delta`, its length is

\[
2(\sqrt{u+\delta}-\sqrt{u-\delta})\le2\sqrt{2\delta}.
\]

The density cap one proves (4.1). QED.

Averaging in `Y` preserves (4.1), so the pair-log theorem's half-power small-ball receiver applies with

\[
 H=2\sqrt2\,|s|^{-1/2}.
\]

Its bound `4 sqrt(2H)(D kappa)^(-1/4)` yields

\[
 \boxed{
 \|p_Q\|_\infty
 \le 2^{13/4}\,[D\kappa |s|]^{-1/4}
 =9.5136569200\ldots [D\kappa |s|]^{-1/4}.
 }
 \tag{4.2}
\]

Again every tail quadratic coefficient remains present in `gamma(Y)`; it is never maximized over a spectral fiber.

## 5. `QFORM-GLOBALNULL-PHYSICAL-DELETION-v1`

The only endpoint not paid by Sections 3--4 is `s=m=0`, where (2.2) gives a global null vector supported on the three literal hubs. The correct operation is **not** to rotate into a null eigenbasis. It is to condition on one ORIGINAL coordinate.

### Theorem 5.1

Let `A=A^T` and let `u` be a unit vector satisfying `Au=0`. Fix an original coordinate `i` with `alpha:=|u_i|>0`, and write

\[
 A=\begin{pmatrix}a&b^T\\ b&C\end{pmatrix},
 \qquad
 u=\binom{u_i}{u_R},
 \qquad
 z=u_R/u_i.
 \tag{5.1}
\]

Then

\[
 b=-Cz,
 \qquad
 a=z^TCz,
 \tag{5.2}
\]

and therefore the exact polynomial identity

\[
 \boxed{
 x^TAx=(x_R-zx_i)^TC(x_R-zx_i).
 }
 \tag{5.3}
\]

Conditional on the ORIGINAL coordinate `X_i=t`, the variables

\[
 Y_j=X_j-z_jt\qquad(j\ne i)
 \tag{5.4}
\]

remain independent and each has a probability density bounded by one. Hence the conditional quadratic form is exactly `Y^T C Y`, with no induced affine remainder.

Moreover, if `s_k(.)` denotes the decreasing singular values, then for every `k<=n-1`,

\[
 \boxed{
 s_k(C)\ge \alpha^2 s_k(A).
 }
 \tag{5.5}
\]

In particular, if `A` has at least three eigenvalues of modulus at least one and `u` is supported on at most three original coordinates, choose `i` with maximal `|u_i|`. Then

\[
 \alpha^2\ge1/3,
 \qquad
 \boxed{s_3(C)\ge1/3.}
 \tag{5.6}
\]

### Proof of the spectral inequality

Let `U` be an `n x (n-1)` matrix with orthonormal columns spanning `u^perp`, and write

\[
 A=UA_0U^T.
\]

The nonzero singular values of `A_0` are those of `A`. Let `E` embed the coordinate hyperplane `x_i=0`, and put

\[
 T=U^TE.
\]

Then

\[
 C=T^TA_0T.
 \tag{5.7}
\]

Since `UU^T=I-uu^T`,

\[
 T^TT=E^T(I-uu^T)E=I-u_Ru_R^T.
 \tag{5.8}
\]

The eigenvalues of (5.8) are `1` with multiplicity `n-2` and `alpha^2` once. Thus

\[
 \sigma_{\min}(T)=\alpha.
\]

For square invertible `T`, the standard singular-value product inequality gives

\[
 s_k(T^TA_0T)\ge\sigma_{\min}(T)^2s_k(A_0)
 =\alpha^2s_k(A),
\]

proving (5.5). QED.

This is the product-preserving replacement for spectral null-coordinate deletion. A general orthogonal deletion would destroy independence; (5.3)--(5.4) do not.

## 6. Quantitative near-null deletion without a reciprocal hub determinant

The exact-null identity also has a robust spectral companion. It is useful when both pair-pivot currencies are small but nonzero.

### Theorem 6.1 — `QFORM-APPROXNULL-PRINCIPAL-RETENTION-v1`

Let `A=A^T`, let `u` be a unit vector, and choose an original coordinate `i` with

\[
 \alpha=|u_i|\ge1/\sqrt3.
\]

Let `C=A[i^c,i^c]`, put `epsilon=\|Au\|_2`, and assume `s_3(A)>=1`. Then

\[
 \boxed{
 s_3(C)
 \ge (2-\sqrt3)-\frac{3+\sqrt{21}}2\,\epsilon.
 }
 \tag{6.1}
\]

Consequently, with

\[
 \epsilon_*:=\frac{2-\sqrt3}{3+\sqrt{21}}
 =0.0353374899520\ldots,
 \tag{6.2}
\]

`epsilon<=epsilon_*` implies

\[
 \boxed{
 s_3(C)\ge\frac{2-\sqrt3}{2}
 =0.133974596216\ldots .
 }
 \tag{6.3}
\]

### Proof

Let `E` again embed the coordinate hyperplane excluding `i`, and form the square matrix

\[
 L=[u/\alpha,\ E].
\]

Its Gram matrix is

\[
 L^TL=
 \begin{pmatrix}
 \alpha^{-2}&(u_R/\alpha)^T\\
 u_R/\alpha&I
 \end{pmatrix}.
\]

Besides `n-2` eigenvalues equal to one, the remaining two have product one and trace `1+alpha^{-2}<=4`. Therefore

\[
 \sigma_{\min}(L)^2\ge2-\sqrt3=:c_0.
 \tag{6.4}
\]

Put `B=L^TAL`. Then

\[
 s_3(B)\ge c_0s_3(A)\ge c_0.
 \tag{6.5}
\]

In block form,

\[
 B=
 \begin{pmatrix}
 \beta&q^T\\q&C
 \end{pmatrix},
 \qquad
 \beta=\frac{u^TAu}{\alpha^2},
 \qquad
 q=\frac{E^TAu}{\alpha}.
 \tag{6.6}
\]

Let `B_0=diag(0,C)`. The rank-two arrow difference `R=B-B_0` has exact operator norm

\[
 \|R\|_{op}
 =\frac{|\beta|+\sqrt{\beta^2+4\|q\|_2^2}}2.
 \tag{6.7}
\]

Since `alpha^2>=1/3`,

\[
 |\beta|\le3\epsilon,
 \qquad
 \|q\|_2\le\sqrt3\epsilon,
\]

and hence

\[
 \|R\|_{op}\le\frac{3+\sqrt{21}}2\epsilon=:c_1\epsilon.
 \tag{6.8}
\]

Weyl's singular-value inequality gives

\[
 s_3(C)=s_3(B_0)\ge s_3(B)-\|R\|_{op}\ge c_0-c_1\epsilon,
\]

which is (6.1). QED.

## 7. Applying the robust deletion to the live pair-pivot collar

Normalize the pair-pivot vector from Section 2:

\[
 v=\frac{q}{\|q\|_2}.
\]

It is supported on exactly the selected three physical coordinates, so some hub coordinate satisfies

\[
 |v_i|\ge1/\sqrt3.
\]

Equation (2.1) gives the exact residual norm

\[
 \boxed{
 \|Av\|_2
 =\frac{\sqrt{s^2+\|m\|_2^2}}{\|q\|_2}.
 }
 \tag{7.1}
\]

Since `||q||>=1`, if

\[
 |s|\le\tau,
 \qquad
 \|m\|_2\le\tau,
 \qquad
 \tau\le\tau_*:=\frac{2-\sqrt3}{\sqrt2(3+\sqrt{21})}
 =0.0249873787752\ldots,
 \tag{7.2}
\]

then `||Av||<=epsilon_*`, and Theorem 6.1 gives a literal principal child `C_i=A[i^c,i^c]` with

\[
 \boxed{s_3(C_i)\ge0.133974596216\ldots .}
 \tag{7.3}
\]

Thus the near-singular transition has an exhaustive determinant-free local compiler:

- a quantitative post-pair star `m` is paid by (3.2);
- a quantitative Schur square `s` is paid by (4.2);
- simultaneous smallness of both produces a literal product-preserving near-null principal child with three retained spectral directions (7.3);
- exact vanishing of both produces the stronger exact product deletion (5.3) and scale `1/3` in (5.6).

This is a structural advance, not the full theorem: the remaining global proof must prevent repeated near-null principal-child reductions from accumulating scale loss, or route the child immediately into one of the completed affine-stable product receivers.

## 8. Actual designated-partner application

The freshest completed designated partner result is account04/B06 `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`, source

`yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260924T001014Z-account04-B06-QFORM-r3/REPORT.md`.

Apply it to an actual exact-global-null child from Section 5. By (5.6), that child retains three spectral directions at scale at least `1/3`. On the partner theorem's tangential curved-frame subbranch, take a retained curved coefficient satisfying

\[
 |\lambda_*|\ge1/3,
 \qquad
 \max_j(w_j^2+v_j^2)\le1/2,
\]

and a shared statistic of the proved form

\[
 B_{sh}=\alpha L+\gamma V+B_R
\]

with `B_R` on a disjoint original-coordinate bank. At the actual off-fold radius `r=1/64`, the partner theorem gives

\[
 \boxed{
 \|g_{1/64}\|_\infty
 \le\frac4{|\lambda_*|(1/64)}
 \le768.
 }
 \tag{8.1}
\]

Conditioning on the deleted ORIGINAL coordinate merely translates the remaining independent coordinates as in (5.4), so the leverage condition and density caps are unchanged and (8.1) is uniform in the conditioning value. Averaging the conditional subprobability kernels therefore preserves the same `L^infinity` bound `<=768` in this exact partner scope. The partner theorem supplies a continuous `C_0` two-output density before that averaging; I do **not** promote continuity of the averaged scalar law, nor do I apply (8.1) through a genuinely normal shared innovation outside the theorem's scope.

## 9. Relation to r53/r54 and the exact singular hub

On the r53/r54 exact rank-two singular hub face, choose the same complementary indefinite pair `P` and normalize its hub null vector `v` so the third component is nonzero. Then

\[
 s=0,
 \qquad
 m=Z^TBq_H
 =-Z^TD_Hq_H.
\]

If `v` is unit and `q_H=v/v_i`, the r53 bank vector `omega=Z^TD_Hv` gives

\[
 \boxed{m=-\omega/v_i.}
 \tag{9.1}
\]

(up to the harmless convention whether the residual cross term is written `2Xm^TY` or `Xg^TY` with `g=2m`). Therefore

\[
 \omega\ne0\Longleftrightarrow m\ne0,
\]

and Section 3 gives a single transition-stable proof route for the entire `omega!=0` face. When `omega=0`, Section 5 applies exactly: the hub null vector is a global null vector and can be deleted product-preservingly. This removes the r54 discontinuity between the diffuse/heavy `omega!=0` analysis and the exact `omega=0` endpoint at the structural level.

## 10. Status, limitations, and next precise debt

This run proves:

- `QFORM-PAIRPIVOT-GLOBALNULL-TRANSITION-COMPILER-v1` — exact pair-completion trichotomy (paid star / paid Schur square / genuine global null);
- `QFORM-GLOBALNULL-PHYSICAL-DELETION-v1` — exact original-coordinate deletion with product preservation and spectral retention `s_k(C)>=alpha^2 s_k(A)`;
- `QFORM-APPROXNULL-PRINCIPAL-RETENTION-v1` — dimension-free quantitative near-null principal retention (6.1).

The main full-scalar paid branches establish absolute continuity and an essential `L^infinity` bound. Continuity is not proved by Sections 3--4. The partner subbranch has its own two-output `C_0` regularity at the exact scope of the partner theorem. Global continuity remains open.

The next exact B06 debt is

`QFORM-NEARNULL-CHILD-NOSCALELOSS-OR-DIRECT-CURVED-ROUTING-v1`:

> starting from the literal principal child in (7.3), aggregate its retained three-direction spectral mass with the original product structure before another near-null deletion is allowed. Either route it immediately to a completed curved/pair/cross receiver, or prove a one-shot weighted deletion principle whose spectral cost cannot accumulate with dimension.

No Gaussianity, log-concavity, moments, compact support, connected support, or post-rotation independence was used. No unrestricted fiber maximum was taken. The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**; the full continuous-density conclusion remains **OPEN**.
