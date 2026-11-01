# fleet04/B18 r6 — transverse-volume payment or rank-two cross collar

**Programme:** \`QFORM-DENSITY-3EIG-20260922\`  
**Run:** \`20260924T032058Z-fleet04-B18-QFORM-r6\`  
**Status:** \`PROVED SUPPORTING TARGET-LEVEL REDUCTION / FULL QFORM OPEN\`  
**Continuity:** not asserted.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B18, 2026-09-24T03:20:58Z.

## 1. Scope

The owner target remains open: independent real original coordinates with probability densities bounded by one, arbitrary real symmetric \(A\), and at least three eigenvalues of modulus at least one. No moment, support, iid, symmetry, smoothness, or post-rotation independence assumption is added.

This report applies the completed fleet01/B18 transverse-anchor theorem to the live two-sided-anchor obstruction and identifies the exact deterministic geometry forced when its analytic gate fails.

## 2. Source audit

The primary marginal theorem actually used by the imported receiver is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. For a product probability density \(\prod_i f_i\), with \(\|f_i\|_\infty\le1\), every \(k\)-dimensional orthogonal marginal has density cap \(2^{k/2}\). This exactly covers the arbitrary rough, non-iid product inputs here. It supplies marginal caps only; it does not create independence after rotation.

Rudelson--Vershynin, arXiv:1402.4492, supplies the corresponding linear-image small-ball input. Herry--Malicet--Poly, arXiv:2303.09488, assumes iid inputs in a smoother Gaussian-functional class and therefore does not close the present owner quantifiers.

The completed theorem consumed below is fleet01/B18's
\`QFORM-TWOSIDED-ANCHOR-TRANSVERSE-RANK2-v1\`, scientific commit
\`51558527d4343f70fd9d43eb1ef86edda4863d38\`.

The newer fleet01/B18 active-plane theorem at
\`b1d09b4c6914935add2727f8d4a705654576c188\` is also recorded below only in its exact rank-one scope.

## 3. Live physical packet

Let \(X\), \(Y\), and the scalar \(W\) be disjoint ORIGINAL-coordinate banks. Consider a retained physical packet whose coefficient matrix is

\[
A_S=
\begin{pmatrix}
0&C&r\\
C^\top&B&h\\
r^\top&h^\top&a
\end{pmatrix}.
\tag{3.1}
\]

Here \(B,h,a\) are arbitrary. Terms involving original coordinates outside \(S\) are also arbitrary: condition those coordinates, so they contribute only affine terms to the retained variables.

For \(r\ne0\), let \(P_r\) be orthogonal projection in the \(X\)-coefficient space onto \(r^\perp\); for \(r=0\), put \(P_r=I\). Write

\[
c_1\ge c_2\ge\cdots
\tag{3.2}
\]

for the singular values of \(P_rC\).

## 4. New theorem

### \`QFORM-TWOSIDED-ANCHOR-PAY-OR-RANK2-COLLAR-v1\`

For every \(\theta>0\), the packet (3.1) satisfies the exhaustive dichotomy

\[
c_1c_2\ge\theta
\quad\Longrightarrow\quad
\boxed{\|p_Q\|_\infty
\le \frac{2\sqrt{2\pi}}{\sqrt{\theta}}},
\tag{4.1}
\]

or

\[
c_1c_2<\theta
\quad\Longrightarrow\quad
\boxed{
\operatorname{dist}_{\mathrm{op}}
\bigl([C\ r],\{R:\operatorname{rank}R\le2\}\bigr)
<\sqrt{\theta}.}
\tag{4.2}
\]

The density statement is an essential-supremum statement; continuity is separate.

### Proof

If \(c_1c_2\ge\theta\), fleet01/B18's completed physical corollary applies directly to (3.1):

\[
\|p_Q\|_\infty
\le \frac{2\sqrt{2\pi}}{\sqrt{c_1c_2}}
\le \frac{2\sqrt{2\pi}}{\sqrt{\theta}}.
\tag{4.3}
\]

This is the required equation-level application. Its proof conditions only on original-coordinate banks and uses the LPP two-dimensional marginal cap before averaging. It requires neither a conditional density bound for \(W\) nor independence after rotation.

Suppose now that \(c_1c_2<\theta\). Since \(c_2\le c_1\),

\[
c_2^2\le c_1c_2<\theta,
\qquad c_2<\sqrt{\theta}.
\tag{4.4}
\]

By Eckart--Young, choose a rank-at-most-one matrix \(R_1\) such that

\[
\|P_rC-R_1\|_{\mathrm{op}}=c_2.
\tag{4.5}
\]

Let \(P_{\langle r\rangle}=I-P_r\) when \(r\ne0\), and \(P_{\langle r\rangle}=0\) when \(r=0\). Define

\[
\widetilde C=R_1+P_{\langle r\rangle}C,
\qquad
\widetilde D=[\widetilde C\ r].
\tag{4.6}
\]

The range of \(R_1\) is at most one-dimensional, while both \(P_{\langle r\rangle}C\) and the last column \(r\) lie in \(\operatorname{span}\{r\}\). Hence

\[
\operatorname{rank}\widetilde D\le2.
\tag{4.7}
\]

Moreover,

\[
\|[C\ r]-\widetilde D\|_{\mathrm{op}}
=\|P_rC-R_1\|_{\mathrm{op}}
=c_2<\sqrt{\theta}.
\tag{4.8}
\]

This proves (4.2). \(\square\)

## 5. Numerical live gate

At the natural collar scale

\[
\theta=2^{-12},
\tag{5.1}
\]

the theorem gives

\[
\boxed{\|p_Q\|_\infty
\le128\sqrt{2\pi}
=320.848419152768\ldots}
\tag{5.2}
\]

unless

\[
\boxed{
\operatorname{dist}_{\mathrm{op}}
\bigl([C\ r],\operatorname{rank}\le2\bigr)<\frac1{64}.}
\tag{5.3}
\]

Thus the entire two-sided-anchor branch outside a \(1/64\) operator-norm tube about rank-two cross carriers is paid with a dimension-free constant. This retains arbitrary \(B,h,a\), arbitrary outside affine couplings created by conditioning, every sign, and every input tail.

## 6. Exact rank-one endpoint inside the collar

The newer completed fleet01/B18 theorem
\`QFORM-ZEROSELF-RANK1-ACTIVEPLANE-CLOSURE-v1\`
applies when the whole cross block \(D=[C\ r]\) has exact rank one and all complement curvature active on its right singular direction lies in a two-dimensional source plane. If \(s=s_3(A_S)>0\), it gives

\[
\boxed{
\|p_Q\|_\infty
\le\frac{3\,2^{5/3}}{s}
=\frac{9.524406311809\ldots}{s}.}
\tag{6.1}
\]

This is not promoted beyond its exact active-plane hypothesis. Combining (5.2)--(6.1), the first genuinely unpaid local geometry is now a near-rank-two cross carrier (or an exact rank-one carrier with complement-active dimension at least three), not the full two-sided-anchor class.

## 7. What remains

The full conjecture is not proved. The deterministic tube (5.3) cannot be discarded perturbatively for arbitrary unbounded inputs. A subsequent argument must retain the small cross tail exactly and either:

1. pay the rank-two carrier by a ruled/mixed-Fresnel receiver;
2. split it into disjoint original-coordinate banks without losing same-bank curvature; or
3. show that the global three-large-eigenvalue hypothesis forces a previously paid physical pair, ridge, or recursive complement branch.

The present theorem is therefore a noncircular structural reduction, not a full solution.

## 8. Source pins

- Required Claude baseline: \`e5f71d79eff325201dd0274053d20268ce65b837\`, directory \`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.
- Completed fleet01/B18 transverse receiver: \`51558527d4343f70fd9d43eb1ef86edda4863d38\`.
- Newer fleet01/B18 exact rank-one active-plane receiver: \`b1d09b4c6914935add2727f8d4a705654576c188\`.
- Primary marginal source: arXiv:1507.07949.
- Primary linear-image source: arXiv:1402.4492.
- Narrower quadratic-form regularity source checked but not applied: arXiv:2303.09488.
