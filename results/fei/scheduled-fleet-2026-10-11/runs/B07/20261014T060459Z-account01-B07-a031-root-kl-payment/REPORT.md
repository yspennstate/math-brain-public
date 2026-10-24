# B07 / A031 — universal payment of the root signed-KL rows

**Status:** PROVED exact reduction; independent review pending. Universal GU and full FEI remain OPEN.

## Frozen target

The preceding A031 identity writes

\[
\Delta_iU=B_i-\Gamma_i+K_i,
\qquad
K_i=\sum_A m_{i,A}D_2\!\left(
\frac{1+\alpha_{i,A}}2\middle\|\frac{1+\beta_{i,A}}2\right).
\]

Here `beta` is formed from the signed upper correlation before any absolute
value is taken.  The stable gap is `G-GU-SIGNED-KL`: pay a nonzero part of
`sum_i K_i` using genuine Boolean convolution, uniformly in dimension,
arity, reuse, bias, and correlation gap.

## New payment

Split `K_i=K_i^(0)+K_i^(+)`, where the first term is the row `A=emptyset`
and the second sums over nonempty `A`.  Booleanity gives

\[
C_{i,\varnothing}=\sum_A\widehat f(A)\widehat f(A\triangle\{i\})/2=0,
\]

so `beta_(i,emptyset)=0`.  If

\[
a=\widehat f(\varnothing),\qquad b=\widehat f(\{i\}),
\qquad m=a^2+b^2,
\]

then

\[
K_i^{(0)}=m\left[1-h_2\!\left(\frac{1+2ab/m}{2}\right)\right].
\]

The scalar inequality

\[
1-h_2\!\left(\frac{1+x}{2}\right)\le x^2,
\qquad |x|\le1,
\]

therefore yields

\[
K_i^{(0)}\le \frac{4a^2b^2}{a^2+b^2}\le4b^2.
\]

Summing gives the dimension-free Boolean-specific payment

\[
\boxed{\sum_iK_i^{(0)}\le4\sum_i\widehat f(\{i\})^2\le4I(f).}
\]

The entropy inequality is proved from the convergent even series

\[
1-h_2\!\left(\frac{1+x}{2}\right)
=\frac1{\ln2}\sum_{k\ge1}\frac{x^{2k}}{2k(2k-1)}
\le x^2,
\]

because the positive coefficients sum to `ln 2` at `x=1`.

## Exact GU implication

Substituting the payment into the signed local identity gives

\[
G(f)\le4I(f)+\sum_i(B_i-\Gamma_i)+\sum_iK_i^{(+)}.
\]

Consequently, for any `a>=4` and `0<=b<1`, the strictly smaller inequality

\[
\boxed{
\sum_iK_i^{(+)}
\le(a-4)I+bU+\sum_i(\Gamma_i-B_i)
}
\]

on tensor-prime Boolean functions is sufficient for universal GU with the
pair `(a,b)`.  The source-reviewed reduction would then give

\[
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\]

This is a genuine hypothesis removal: the empty upper-set KL row no longer
belongs to the unpaid aggregate.  It uses the signed Boolean normalization
`C_emptyset=0`; it is false as a derivation for arbitrary spectral laws.

## Higher convolution compatibility

For distinct `i,j`, group Fourier coefficients on each two-face as
`a_A,b_A,c_A,d_A` according to the presence of `i,j`.  The three Boolean
convolution identities at shifts `{i}`, `{j}`, and `{i,j}` give

\[
\sum_A(a_Ab_A+c_Ad_A)=0,
\quad
\sum_A(a_Ac_A+b_Ad_A)=0,
\quad
\sum_A(a_Ad_A+b_Ac_A)=0.
\]

Thus the fair-root normalization survives either physical restriction,
with the mixed signed term retained.  This identifies the next target:
transport the root payment through a stopping tree without charging the
same singleton/doubleton mass repeatedly, or prove an analogous payment for
the nonempty rows `A!=emptyset`.

## Verification and sharpness information

`verify_root_kl_payment.py` checks the exact local quantities on all 65,812
Boolean truth tables through dimension four, all two-face convolution
identities, and point defects through dimension 24.  The point-defect ratio

\[
\frac{\sum_iK_i^{(0)}}{\sum_i\widehat f(\{i\})^2}
\]

approaches `2/ln 2`, so a coefficient below `2/ln 2` is impossible for this
particular scalar payment.  The proved coefficient four is uniform but is
not claimed optimal.

No finite check is used as an all-dimensional bridge.  The proof is the
series inequality plus Boolean convolution.

## Remaining gap

The nonempty-row KL aggregate `sum_i K_i^(+)` is still universal and can
contain vanishing correlation gaps.  No pair `(a,b)` is proved.  This result
does not prove GU or FEI, and failure of a sharper root coefficient would
not disprove either conjecture.

