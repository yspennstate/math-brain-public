# Parameterized reused-activation cone obstruction

All logarithms are base two.  Put

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),
\qquad M=G-B.
\]

The universal signed-mismatch refund `SMR(c,eta)` is the assertion
`L_{c,eta}(f)<=0` for every genuine Boolean sign.  For `0<eta<=1`, it
would imply GU with `(a,b)=(c+2,1-eta)` and then

\[
H(f)\le \left(2+\frac{2(c+2)}{\eta}\right)I(f).
\]

This note proves a parameterized obstruction to one proposed way of proving
SMR.  It does not refute GU.

## 1. The Boolean pair

Let `q` be the four-bit Boolean sign whose `+1` truth-table positions are
encoded by the least-significant-bit-first mask `10049`.  Let `x=3`
(zero-based), let `r=chi_x q`, and let `F=A(r)` be fair activation: one
fresh selector branch is `r` and the other is the constant `1`.

Direct rational Walsh arithmetic gives

\[
 I(q)=2,\qquad U(q)=2,\qquad M(q)=\frac78.
\]

Consequently

\[
L_{c,\eta}(q)\le0
\quad\Longleftrightarrow\quad
c\ge c_q(\eta):=\frac{23}{16}+\eta. \tag{1}
\]

For the five-bit Boolean sign `F`, the same calculation gives

\[
I(F)=\frac{11}{8},
\]

\[
U(F)=\frac{31}{8}\log 2-\frac{9}{64}\log 3
     -\frac{25}{32}\log 5, \tag{2}
\]

and

\[
M(F)=\frac{83}{16}\log 2+\frac{189}{64}\log 3
     -\frac58\log 5-\frac{13}{8}\log 13
     -\frac{17}{32}\log 17. \tag{3}
\]

Thus

\[
L_{c,\eta}(F)\le0
\quad\Longleftrightarrow\quad
c\ge c_F(\eta):=\alpha_F+\beta_F\eta, \tag{4}
\]

where

\[
\begin{aligned}
\alpha_F={}&\frac{145}{22}\log2+\frac{45}{22}\log3
-\frac{45}{44}\log5-\frac{13}{11}\log13-\frac{17}{44}\log17,\\
\beta_F={}&\frac{31}{11}\log2-\frac9{88}\log3-\frac{25}{44}\log5.
\end{aligned}
\]

Numerically,

\[
c_F(\eta)=1.505684707963186+1.336806053967517\eta. \tag{5}
\]

## 2. Exact positivity of the entire wedge

Subtracting (1) from (4) gives

\[
c_F(\eta)-c_q(\eta)=D_0+D_1\eta, \tag{6}
\]

with

\[
176D_0=\log\frac{2^{907}3^{360}}
 {5^{180}13^{208}17^{68}},
\qquad
88D_1=\log\frac{2^{160}}{3^9 5^{50}}. \tag{7}
\]

Both signs are exact.  In the first comparison the numerator has 1,478
bits and the denominator 1,466 bits; in the second they have 161 and 131
bits.  Hence `D_0>0` and `D_1>0`, so

\[
\boxed{c_q(\eta)<c_F(\eta)\quad\text{for every }\eta\ge0.} \tag{8}
\]

Therefore, for every `eta>=0` and every

\[
\boxed{c_q(\eta)\le c<c_F(\eta),} \tag{9}
\]

the child is paid, `L(q)<=0`, but the activated output is unpaid,
`L(F)>0`.  This refutes the reused-coordinate zero-cone implication on a
nonempty parameter interval for every GU-relevant `0<eta<=1`.

Independently of cone induction, the same `F` proves the necessary lower
bound

\[
\boxed{c\ge c_F(\eta)} \tag{10}
\]

for any universal `SMR(c,eta)` theorem.  This is a lower bound on the
sufficient signed-mismatch route, not a lower bound on all possible GU
constants.

At `eta=1/4`, (1) and (5) give

\[
c_q=1.6875,\qquad c_F=1.839886221455066\ldots.
\]

Thus the previously certified point `c=7/4` lies strictly inside the
wedge.  The earlier candidate `c=2, eta=1/4` lies outside this obstruction
and remains open.

## 3. Verification and scope

`CHECK_WEDGE.py` reconstructs the spectra from the truth tables, stores all
entropy terms as rational prime exponents, and compares the integer products
in (7).  Command:

```text
python3 CHECK_WEDGE.py
```

The all-parameter statement follows analytically from the affine formula
(6); the finite checker supplies the exact coefficients and sign
certificates.  This package extends the B19 one-point witness.  It does not
prove an admissible GU pair, does not refute GU or FEI, and needs fresh
independent review before registry acceptance.
