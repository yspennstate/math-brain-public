# Independent reconstruction

## GU implication

Assume `M+(1+eta)U<=cI`.  Since `G=B+M`, `B<=H`, and
`H<=2(I-Var)+2U`,

\[
G\le(c+2)I+(1-\eta)U-2\operatorname{Var}.
\]

Set `a=c+2`, `b=1-eta`, and `K=a/(1-b)`.  For a nonconstant `n`-bit
Boolean function, induction on `n` and

\[
\sum_i\mathbb E I(f|x_i)=(n-1)I(f)
\]

give

\[
nU=G+\sum_i\mathbb E U(f|x_i)
\le aI+bU+K(n-1)I.
\]

Using `a=K(1-b)` yields `(n-b)U<=(n-b)KI`; constants are separate.
Thus `U<=KI`, followed by `H<=2I+2U`.

## Witness

Raw Walsh sums for mask `56242` all have absolute value four, so its spectral
law is uniform on the 16 labels.  This gives `U=I=2` and `B=4` immediately.
The independently collected prime-log expression for its residual is empty,
so `G=11/2` and `L_{2,1/4}=0` exactly.

Activation produces masses `25/64`, `9/64`, and thirty copies of `1/64`.
Computing the upper caps of this law and the upper caps of all ten physical
restrictions gives

\[
256L_{2,1/4}(A(q))=
1944\log_2 2+711\log_2 3-410\log_2 5
-416\log_2 13-136\log_2 17.
\]

Equivalently,

\[
2^{1944}3^{711}>5^{410}13^{416}17^{136},
\]

because the two integers have bit lengths 3,071 and 3,048.  This certifies
the strict sign.

