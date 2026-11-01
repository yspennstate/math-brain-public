# Independent reconstruction and adversarial extension

All logarithms are base two. This audit did not import or execute the B05
checker.

## 1. Equivalence claim

For an existing physical coordinate \(x\), multiplication by its character
\(\chi_x\) is an involution on the set of Boolean functions on the same
cube. Hence for every Boolean \(r\), choosing \(q=\chi_xr\) gives

\[
A(\chi_xq)=A(r).
\]

Restricting the fresh activation selector to its nonconstant branch recovers
\(r\). Therefore the arbitrary-core restriction closure of the reused
construction is the universal Boolean class. The producer's scope statement
is exact.

## 2. Signed slice identities

Let \(r=\chi_xq\) and \(W_x(q)=U(r)-U(q)\). Fourier multiplication toggles
membership of \(x\):

\[
\widehat r(S)=\widehat q(S\triangle\{x\}).
\]

For \(B_i\), this either swaps the two masses in every \(i=x\) pair or
permutes the pairs for \(i\ne x\). Since the binary entropy functional is
symmetric,

\[
B(r)=B(q).
\]

The degree of every Fourier set changes by \(+1\) when it omits \(x\) and
by \(-1\) when it contains \(x\). Thus

\[
I(r)-I(q)=1-2\operatorname{Inf}_x(q).
\]

For \(j\ne x\), restriction commutes with multiplication by \(\chi_x\).
For \(j=x\), the corresponding restrictions differ only by output signs,
which preserve \(U\). Direct subtraction of all restriction increments gives
the producer's \(\mathcal D_xW\) formula and hence

\[
L_{c,\eta}(\chi_xq)-L_{c,\eta}(q)
=\mathcal D_xW(q)+(1+\eta)W_x(q)
-c(1-2\operatorname{Inf}_x(q)).
\]

Substitution into the independently accepted exact activation recurrence
proves equation (8) of the reviewed proof. No normalization or terminal term
is missing.

## 3. Half-contraction falsifier

For \(q=\chi_x\), one has \(\chi_xq=1\), so
\(A(\chi_xq)=1\), while \(L_{c,\eta}(q)=-c\). Therefore the claimed
residual is exactly \(c/2>0\) for every \(c>0\). The producer correctly
labels this as a failure of the transfer template, not of GU or FEI.

## 4. New adversarial finding: cone preservation also fails at the inherited pair

The producer suggested next testing

\[
L_{7/4,1/4}(q)\le0
\quad\Longrightarrow\quad
L_{7/4,1/4}(A(\chi_xq))\le0. \tag{C}
\]

Take the four-bit truth-table mask `10049`, where bit \(s\) is one exactly
when the function value at input index \(s\) is \(+1\), and take coordinate
\(x=3\) in zero-based indexing. Exact Walsh arithmetic gives

\[
L_{7/4,1/4}(q)=-\frac18.
\]

For \(F=A(\chi_xq)\), collecting every entropy logarithm into prime powers
gives

\[
256L_{7/4,1/4}(F)
=\log_2\frac{2^{1952}3^{711}}
{5^{410}13^{416}17^{136}}. \tag{1}
\]

The numerator in (1) has 3,079 bits and the denominator 3,048 bits; direct
integer comparison proves the quotient is greater than one. Hence

\[
L_{7/4,1/4}(F)=0.123593554500714\ldots>0.
\]

Thus (C) is rigorously refuted. This does not refute cone preservation for a
larger \(c\), a different terminal reserve, the universal GU inequality, or
FEI. It shows that simply weakening half-contraction to zero-cone preservation
does not repair the reused-coordinate step at the proper-class constants.

## 5. Review conclusion

`B05-A023-REUSED-CHARACTER-EQUIVALENCE-v1` is accepted without repair at its
declared scope. The new cone witness is a separate B19 contribution and
requires an uninvolved A085/A090 review before adoption.
