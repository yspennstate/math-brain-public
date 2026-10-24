# Signed-mismatch refund: exact reduction and local obstruction

All logarithms are base two.  Let `S` have the spectral law
`P(S=A)=p_A=fhat(A)^2`.  Put

\[
B_i=H(1_{i\in S}\mid S\setminus\{i\}),\qquad
B=\sum_iB_i,
\]

and use the source identity

\[
\Delta_iU=B_i-\Gamma_i+K_i.
\]

Thus, with `M=sum_i(K_i-Gamma_i)`,

\[
G=B+M. \tag{1}
\]

## The reduction

The dual total-correlation inequality gives

\[
B\le H(S)=H(f). \tag{2}
\]

The reviewed upper-set bridge, with its retained terminal term, is

\[
H(f)\le2\bigl(I(f)-\operatorname{Var}(f)\bigr)+2U(f). \tag{3}
\]

Assume, for fixed `0<eta<=1` and finite `c`, that

\[
M(f)+(1+\eta)U(f)\le cI(f) \tag{4}
\]

for every genuine Boolean `f`.  Combining (1)--(4),

\[
\begin{aligned}
G
&\le 2(I-\operatorname{Var})+2U+cI-(1+\eta)U\\
&=(c+2)I+(1-\eta)U-2\operatorname{Var}\\
&\le(c+2)I+(1-\eta)U.
\end{aligned}
\]

This is GU' with `a=c+2` and `b=1-eta<1`.  Constants have
`I=U=G=B=M=0` and need no division.  For nonconstants, the reviewed
restriction induction gives

\[
U\le\frac{c+2}{\eta}I,
\]

and then (3) gives

\[
H\le\left(2+\frac{2(c+2)}{\eta}\right)I.
\]

At `(c,eta)=(2,1/4)` these constants are `(a,b)=(4,3/4)` and `C=34`.

## Exact tensor behavior

For disjoint products, the spectral subset law is the product of the two
factor laws.  Consequently `U`, `G`, and `I` are additive.  Conditional
entropies from the first block are unaffected by conditioning on the
independent second block, and conversely, so `B` is additive.  Equation (1)
then makes `M` additive.  Hence the residual

\[
\mathcal R_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f)
\]

is additive under every disjoint tensor product.

For the displayed four-bit vector in `REPORT.md`, direct Walsh arithmetic
gives a flat spectral law, `H=B=4`, `U=I=2`, and `G=11/2`.  Therefore
`M=3/2` and

\[
\mathcal R_{2,1/4}=3/2+(5/4)2-2(2)=0.
\]

Thus `c=2` cannot be reduced at fixed `eta=1/4`, even before taking tensor
powers.

## Why the coordinate proof fails

For `I>0`, define

\[
u_i^*=\sum_{S\ni i}\frac{p_S}{|S|}
\log_2\frac{\pi(S)}{p_S}
+\frac{\operatorname{Inf}_i}{I}
p_\varnothing\log_2\frac1{p_\varnothing}. \tag{5}
\]

The first sum contains only nonempty `S`.  Hence

\[
\sum_i u_i^*=U. \tag{6}
\]

Summing the coordinate inequality

\[
\Delta_iU-B_i+\frac54u_i^*\le2\operatorname{Inf}_i \tag{7}
\]

would prove `(SMR)_{2,1/4}`.  The five-bit mask and coordinate in
`REPORT.md` violate (7).  `CERTIFY_SIGNED_MISMATCH.py` uses exact integer
Walsh coefficients.  Every entropy is represented as a rational linear
combination of `log_2(m)` for positive integers `m`; clearing coefficient
denominators converts the sign of (7)'s residual into one exact comparison
of two integers.  The positive product is strictly larger.  Therefore (7)
is rigorously false, while the aggregate inequality remains open.

