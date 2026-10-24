# B19 / A092 independent review — fair-activation SMR falsifier

**Run:** `20261014T045438Z-account01-B19-activation-smr-review-a092`  
**Primary packet:** A092, counterexample referee  
**Reviewed version:** `B05-A023-ACTIVATION-SMR-v1`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **ACCEPTED AT DECLARED SCOPE**  
**Full FEI:** **OPEN**

## 1. Audited candidate, quantifiers, and GU consequence

For every genuine Boolean sign, let

\[
M(f)=G(f)-B(f)=\sum_i(K_i-\Gamma_i),\qquad
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f).
\]

The audited universal helper was

\[
L_{2,1/4}(f)=M(f)+\frac54U(f)-2I(f)\le0.\tag{SMR}
\]

The actual reduction is correct.  If `L_{c,eta}<=0` universally for fixed
`c<infinity` and `0<eta<=1`, then `G=B+M`, `B<=H`, and

\[
H\le2(I-\operatorname{Var})+2U
\]

give

\[
G\le(c+2)I+(1-\eta)U-2\operatorname{Var}.
\]

The source restriction induction then gives

\[
U\le\frac{c+2}{\eta}I,qquad
H\le\left(2+\frac{2(c+2)}{\eta}\right)I.
\]

Thus (SMR) would imply GU `(4,3/4)` and FEI constant `34`.  This is a
sufficient-helper implication only.

## 2. Independent mathematical reconstruction

I did not use the author checker.  For mask `56242`, raw integer Walsh sums
are

```text
4,-4,4,4,-4,-4,4,-4,-4,-4,4,-4,-4,4,-4,-4
```

so the four-bit core `q` is bent and every spectral mass is `1/16`.
Consequently

\[
U(q)=I(q)=2,\quad B(q)=4.
\]

An independent exact logarithmic calculation gives `G(q)=11/2`, hence

\[
M(q)=\frac32,\qquad L_{2,1/4}(q)=0.
\]

For the fair activation

\[
F=A(q),\qquad A(q)(z,x)=1\ (z=+1),\quad q(x)\ (z=-1),
\]

the mean is `m=1/4`.  The activation spectrum has the exact shape

\[
p_\varnothing=\frac{25}{64},\qquad p_{\{z\}}=\frac9{64},
\qquad p_S=\frac1{64}\quad\text{for the other 30 labels}.
\]

Direct recomputation of every upper cap and every physical restriction gives

\[
\begin{aligned}
U(F)&=1.8381083242053355\ldots,\\
I(F)&=\frac{11}{8},\\
B(F)&=3.3369990984052347\ldots,\\
G(F)&=3.8817072476492807\ldots,\\
M(F)&=0.5447081492440460\ldots.
\end{aligned}
\]

Therefore

\[
L_{2,1/4}(F)=0.0923435545007156\ldots>0.
\]

## 3. Independent exact sign certificate

`INDEPENDENT_REVIEW.py` computes Walsh coefficients as raw character sums,
not by the author's fractional FWHT.  It expresses every rational logarithm
in prime coordinates before collecting coefficients.  Clearing the common
denominator `256` gives the transparent identity

\[
\boxed{
256L_{2,1/4}(F)=
\log_2\frac{2^{1944}3^{711}}
{5^{410}13^{416}17^{136}}.
}
\]

The numerator and denominator have 3,071 and 3,048 bits respectively.
Hence the numerator is strictly larger and the residual is rigorously
positive.  For the child `q`, every prime exponent cancels exactly, proving
`L_{2,1/4}(q)=0` without floating point.

This independently accepts the B05 finite falsifier.  The author's larger
13-rational-base product is valid; the prime-factor form above is an
equivalent simplification, not a repair to the claim.

## 4. Review of the activation ledger

The all-core activation identity is also correct.  From

\[
\widehat F(S)=\frac{\mathbf1_{S=\varnothing}+\widehat q(S)}2,
\qquad
\widehat F(S\cup\{z\})=
\frac{\mathbf1_{S=\varnothing}-\widehat q(S)}2,
\]

the selector conditional entropy is

\[
B_z=\frac{1-m^2}{2}+\frac14T((1+m)^2,(1-m)^2),
\]

and each data coordinate satisfies

\[
B_i(F)=\frac12B_i(q)-\frac12T(m^2,p_i)
+\frac14T((1+m)^2,p_i)+\frac14T((1-m)^2,p_i).
\]

Restriction of a data coordinate commutes with activation, selector
restriction returns `1` and `q`, and the selector pivotal mass is
`(1-m)/2`.  Therefore the author's complete recurrence

\[
L_{c,\eta}(A(q))=\frac12L_{c,\eta}(q)+D_R(q)+(2+\eta)R(m)
-B_z-\sum_iC_i-c\frac{1-m}{2}
\]

contains each signed, terminal, and physical-input term exactly once.
No fixed-sign projection, reused-input cancellation, or disjoint terminal
factor is silently assumed in this one-step identity.

## 5. Scope and adversarial checks

The verdict is deliberately narrow:

1. `SMR_{2,1/4}` is false for a genuine five-bit Boolean function.
2. The witness forces `c>=2.067158948727793...` within the same
   `eta=1/4` helper family.
3. It does **not** falsify GU `(4,3/4)`: the same witness has

   \[
   4I(F)+\frac34U(F)-G(F)
   =2.996873995504721\ldots>0.
   \]

4. It is not an FEI counterexample and gives no unbounded `H/I` family.
5. It does not challenge B05's separately accepted fresh/disjoint tower
   endpoints or B12's corrected coefficient-four/fixed-sign no-go results.

The failure occurs with one fresh fair selector and no reused coordinates,
so overlap or rare-limit bookkeeping cannot rescue the sharp helper.
Conversely, one finite failure supplies no universal replacement constant.

## 6. Dependency consequence and next action

`B01-A003-SMR-2-ONE-QUARTER-v1` must be marked **REFUTED**, and any claim
using it as a premise is blocked until repaired.  The general reduction
`SMR_{c,eta} => GU(c+2,1-eta)` remains valid.

The next mathematical action is to freeze a replacement reserve in the exact
activation recurrence—larger `c`, a terminal reserve, or another signed
credit—and prove single-use propagation for changing cores.  Mask `56242`
and its tensor equality relatives must be mandatory controls.  A finite
optimized value of `c` is not a universal proof.

No mathematical repair was required, so this review remains independent.
No second end-to-end GU review exists.  Full FEI remains open.

