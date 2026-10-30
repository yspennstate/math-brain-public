# MOC4 fleet04/B07 — explicit mixed-Schur SVD payment and spinor alignment

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T071214Z-fleet04-B07-MOC4-r14`  
**Role:** representation-theoretic / exterior-algebra mixed-minor constraint  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and current source chain

The target is the exact `n=4` Marcus–de Oliveira statement: for every pair of complex normal
`4 x 4` matrices with spectra `a_i,b_i`,
\[
\det(A+B)\in\operatorname{conv}\{\prod_i(a_i+b_{\sigma(i)}):\sigma\in S_4\},
\]
including singular and repeated-spectrum cases.

The latest complete campaign-lead report available at the scientific snapshot is fleet03/B07
`20260922T064004Z-fleet03-B07-MOC4-r12`,
`MOC4-KERNEL-QUARTIC-RESERVE-v1`, report blob
`ec11bc9937109dc0059b8e2ab78a485a9f646e3e`.
It reduces the surviving mixed-Schur boundary to an exact Lyapunov–Schmidt condition
\[
q+3\langle \ell^\#,(-H)^+\ell^\#\rangle\le0
\]
and explicitly asks for the cubic covector and reserve to be substituted using the special MOC4
Spin(4) structure rather than generic orbit geometry.

The named assigned OTHER-account result applied here is fleet01/B08
`20260922T060423Z-fleet01-B08-MOC4-r11`,
`MOC4-PR-JOINT-LIFT-FACET-v1`, report blob
`5a93eb14d686499625085947cf3fcc4612597863`.
Its strict dense true-unitary witness proves that an unconditional positive common `S_4` law
reproducing the same unitary's degree-one and complementary degree-two data does not exist in
general. Consequently the argument below does **not** introduce such a lift; all quantities are
computed on one genuine Spin(4) orbit through the same unitary.

I also use fleet03/B20
`20260922T064515Z-fleet03-B20-MOC4-r12`,
`MOC4-SPIN4-BIAFFINE-ORBIT-v1` and
`MOC4-SPIN4-GLOBAL-TRUST-REGION-GATE-v1`, report blob
`69574583d7e7ade0aa97b0a03f79a9a7b2d216b9`.
For every complementary Spin(4) product orbit the genuine determinant support is exactly
bi-affine on `S^2 x S^2`. This supplies the canonical coordinates used below.

## 2. Compact conditional proof chain

Suppose MOC4 fails. Support separation and compactness give a true-unitary global maximizer
with positive gap over all 24 permutation endpoints. Existing strict-root results eliminate
scalar Spin(4) saturation. For each complementary pair Hessian, therefore, either

1. it is negative definite; or
2. it lies on the genuine mixed-Schur boundary.

The lead's current first boundary gap is case 2. The theorem below computes its entire
Lyapunov–Schmidt reserve in closed SVD form and turns it into a quantitative same-orbit
alignment constraint. Thus a proof of MOC4 may now attack the mixed-Schur branch by inserting
the structured spectral/exterior-minor identities into one explicit inequality rather than
carrying an unspecified cubic polynomial and pseudoinverse. If all pair blocks are negative
definite, the separate NDI branch of the lead remains.

## 3. Exact Spin(4) pole form

Fix one genuine complementary Spin(4) product orbit. By fleet03/B20, after rotating Bloch
coordinates so the current unitary is the north pole `e=(0,0,1)`,
\[
f(n,m)=c+p\cdot n+q\cdot m+n^T Zm,\qquad n,m\in S^2.
\]
At a stationary point write
\[
Z=\begin{pmatrix}M&r\\ s^T&z\end{pmatrix},\qquad
p=(-r,A-z),\qquad q=(-s,B-z),
\]
where `M` is `2 x 2`, `r,s in R^2`, and on the surviving strict branch
\[
A>0,\qquad B>0.
\]
The tangent Hessian is
\[
H=\begin{pmatrix}-A I_2&M\\ M^T&-B I_2\end{pmatrix}\preceq0.
\]
The mixed-Schur boundary is
\[
\sigma_1(M)=\sqrt{AB}.
\]
Choose singular bases
\[
Mv_i=\sigma_i u_i,\qquad M^Tu_i=\sigma_i v_i,\qquad
\sigma_1=\sqrt{AB}\ge\sigma_2\ge0,
\]
and set
\[
r_i=u_i\cdot r,\qquad s_i=v_i\cdot s.
\]
Finally define the simultaneous-antipode half-drop
\[
\delta:=A+B-2z
=\frac{f(e,e)-f(-e,-e)}2\ge0.
\]

All of these are source-bound true-unitary quantities. In particular
\[
2A=f(e,e)-f(-e,e),\qquad 2B=f(e,e)-f(e,-e),
\]
and for each singular direction
\[
4r_i=f(-u_i,-e)-f(u_i,-e),\qquad
4s_i=f(-e,-v_i)-f(-e,v_i).
\]

## 4. New theorem — `MOC4-MIXED-SCHUR-SVD-PAYMENT-v1`

Assume the mixed-Schur boundary and local maximality at `(e,e)`.

### Simple top singular value: `sigma_2 < sqrt(AB)`

Then the cubic kernel condition is
\[
\boxed{\sqrt A\,r_1+\sqrt B\,s_1=0.}\tag{C}
\]

Moreover
\[
\boxed{
\delta\ge
\frac{r_1^2}{B}
+
\frac{A r_2^2+2\sigma_2 r_2s_2+B s_2^2}{AB-\sigma_2^2}.
}\tag{P1}
\]

Equivalently,
\[
\boxed{
\delta\ge \frac{r_1^2}{B}
+\frac{(\sqrt A\,r_2+\sqrt B\,s_2)^2}
       {2\sqrt{AB}(\sqrt{AB}-\sigma_2)}
+\frac{(\sqrt A\,r_2-\sqrt B\,s_2)^2}
       {2\sqrt{AB}(\sqrt{AB}+\sigma_2)}.
}\tag{P2}
\]

This is the lead's abstract Lyapunov–Schmidt reserve with every term explicitly evaluated in
the exact Spin(4) representation.

### Proof

Use the tangent chart
\[
n=(x,\sqrt{1-\|x\|^2}),\qquad
m=(y,\sqrt{1-\|y\|^2}).
\]
Stationarity gives the expansion
\[
\begin{aligned}
f-f(e,e)
={}&-\frac A2\|x\|^2-\frac B2\|y\|^2+x^TMy\\
&-\frac12(r\cdot x)\|y\|^2-\frac12(s\cdot y)\|x\|^2\\
&-\frac A8\|x\|^4-\frac B8\|y\|^4+\frac z4\|x\|^2\|y\|^2+O(5).
\end{aligned}\tag{1}
\]

The negative Hessian has kernel vector
\[
\zeta=(\sqrt B\,u_1,\sqrt A\,v_1).
\]
The cubic derivative along that kernel is
\[
D^3f(0)[\zeta,\zeta,\zeta]
=-3\sqrt{AB}\,(\sqrt A\,r_1+\sqrt B\,s_1),
\]
so local maximality gives `(C)`.

Let
\[
\ell(Y)=D^3f(0)[\zeta,\zeta,Y].
\]
In the singular bases and after `(C)`,
\[
\ell=(A r_1,\,-A r_2,\,-\sqrt{AB}r_1,\,-B s_2).
\]
The top singular mode of `-H` has nonzero eigenvalue `A+B`; its pseudoinverse contribution is
\[
A r_1^2.
\]
The second mode is the positive-definite block
\[
\begin{pmatrix}A&-\sigma_2\\-\sigma_2&B\end{pmatrix},
\]
whose inverse gives contribution
\[
\frac{AB(A r_2^2+2\sigma_2r_2s_2+B s_2^2)}{AB-\sigma_2^2}.
\]
Hence
\[
R:=\langle\ell^\#,(-H)^+\ell^\#\rangle
=A r_1^2+
\frac{AB(A r_2^2+2\sigma_2r_2s_2+B s_2^2)}
     {AB-\sigma_2^2}.\tag{2}
\]

The fourth derivative along the kernel is
\[
q=D^4f(0)[\zeta,\zeta,\zeta,\zeta]
=3AB(2z-A-B)=-3AB\delta.\tag{3}
\]
The lead's exact local-max reserve `q+3R<=0` therefore becomes
\[
R\le AB\delta,
\]
which after division by `AB` is `(P1)`. Diagonalizing the numerator in the second singular
mode gives `(P2)`. `QED`

## 5. Polar-alignment collar

Let `Q` be the orthogonal polar factor carrying `v_i` to `u_i`. From `(C)` and `(P2)`,
\[
\boxed{
\|\sqrt A\,r+\sqrt B\,Q s\|^2
\le
2\sqrt{AB}\,(\sqrt{AB}-\sigma_2)\,\delta.
}\tag{PA}
\]

Thus a mixed-Schur candidate with a nearly double top singular value is forced into a
quantitatively narrow spinor-alignment collar. In particular, fixed nonzero misalignment
forces a definite lower bound on the second singular-value gap.

The payment is strictly stronger than the separate antipodal shadows
\[
\|r\|^2\le B\delta,\qquad \|s\|^2\le A\delta.
\]
Indeed `(P1)` may also be written
\[
\delta-\frac{\|r\|^2}{B}
\ge
\frac{(B s_2+\sigma_2r_2)^2}
     {B(AB-\sigma_2^2)},\tag{4}
\]
and symmetrically
\[
\delta-\frac{\|s\|^2}{A}
\ge
\frac{(A r_2+\sigma_2s_2)^2}
     {A(AB-\sigma_2^2)}.\tag{5}
\]

These are genuine common-unitary constraints; they are not properties of arbitrary
bistochastic or independently chosen compound-minor arrays.

## 6. Double mixed-Schur singularity

If
\[
\sigma_2=\sigma_1=\sqrt{AB},
\]
the Hessian kernel is two-dimensional. Vanishing of the cubic on every kernel direction gives
the vector identity
\[
\boxed{\sqrt A\,r+\sqrt B\,Q s=0.}\tag{6}
\]
Applying the same kernel-reserve lemma to an arbitrary kernel vector
`(sqrt(B)t,sqrt(A)Qt)` gives
\[
\boxed{\|r\|^2\le B\delta,\qquad \|s\|^2\le A\delta.}\tag{7}
\]
The proof uses the reflection identity
\[
\|2(r\cdot t)t-\|t\|^2r\|^2=\|t\|^4\|r\|^2.
\]
Thus the apparent pole in `(P2)` has the correct rigid limit: the numerator in the
`(sqrt(AB)-sigma_2)^{-1}` channel must vanish exactly.

## 7. Exact top-two-circle factorization

There is also a useful nonlocal check. Restrict the genuine Spin(4) product orbit to the two
great circles generated by the top singular vectors:
\[
n=(\sin\theta\,u_1,\cos\theta),\qquad
m=(\sin\phi\,v_1,\cos\phi).
\]
Put
\[
x=\tan(\theta/2),\qquad y=\tan(\phi/2).
\]
Under the cubic gate `(C)`, exact algebra gives
\[
\boxed{
(f(n,m)-f(e,e))(1+x^2)(1+y^2)
=
-2\left[
\left(\sqrt A\,x-\sqrt B\,y-\frac{r_1}{\sqrt B}xy\right)^2
+
\left(\delta-\frac{r_1^2}{B}\right)x^2y^2
\right].
}\tag{8}
\]
Hence `(e,e)` is globally maximal on this entire genuine two-circle suborbit if and only if
\[
r_1^2/B\le\delta.
\]
The extra second-mode term in `(P1)` is therefore precisely the additional payment obtained by
allowing the optimal order-two transverse correction away from that top-mode suborbit.

This separates two mechanisms cleanly: generic Spin(4) geometry can have a quartically or
higher-order strict mixed-Schur maximum, as the lead's calibration already shows, but an actual
MOC4 candidate must additionally obey the explicit transverse SVD payment `(P1)` in every
mixed-Schur pair block.

## 8. Exact verification

`verify_mixed_schur_svd_payment.py` symbolically checks:

- the mixed-Schur Hessian kernel;
- the cubic gate and cubic covector;
- the exact pseudoinverse reserve `(2)`;
- the quartic derivative `(3)`;
- equivalence of the lead reserve to `(P1)` and `(P2)`;
- the polar-alignment consequence `(PA)`;
- the exact two-circle factorization `(8)`;
- the lead's calibration `f=x_3+y_3-(1/2)x.y`, for which the reserve is noncontradictory.

`VERIFY_OUTPUT.txt` records the exact PASS output. The code is verification of the algebra; the
proof is the derivation above.

## 9. Updated first missing implication

The lead's `MOC4-MIXED-SCHUR-LS-RESIDUAL-v1` is now reduced on every simple mixed-Schur block
to the explicit source-bound inequality `(P1)`, and on the double-singular block to `(6)-(7)`.

The next representation-theoretic target is:

> **`MOC4-SIX-SPIN4-SVD-RESERVE-EXCLUSION-v1` (OPEN).**  
> For structured MOC4 spectral coefficients at a positive-gap true-unitary support maximizer,
> combine the six left/right global Spin(4) trust-region gates, the same-unitary `P/R/D`
> identities and the exterior-spinor constraints with `(P1)`/`(PA)` to exclude every
> mixed-Schur block. If no block is mixed-Schur singular, the lead's negative-definite-interior
> branch remains and must be closed separately.

This is narrower than an unsupported positivity representation and directly preserves the
fleet01/B08 no-go.

## 10. Verdict

`ESSENTIAL_STEP_APPLIED`.

The lead's abstract mixed-Schur cubic/quartic reserve has been explicitly evaluated in the
exact Spin(4) representation and converted into a quantitative singular-gap/spinor-alignment
constraint on one genuine unitary orbit. No full MOC4 proof is claimed.
