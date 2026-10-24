# Independent audit of the changing-overlap counterfamily

All logarithms are base two.  This audit reconstructs the Boolean Fourier
calculation directly and does not import or execute the producer checker.

## 1. Reviewed statement

For

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
\psi_k(t)=q(t)+t\log_2k,
\]

the reviewed fixed-block potential is

\[
\widetilde\Lambda_X(f)=
\psi_{|X|}(E_X^f(\varnothing))+
\sum_{i\notin X}q(E_X^f(\{i\})),
\qquad
E_X^f(S)=\sum_{A\subseteq X}\widehat f(S\cup A)^2. \tag{1}
\]

B05 claims that no finite (C) can pay the swap
(X=\{y,x\}\) to (Y=\{y,z\}\) using only
(C(\operatorname{Inf}_x+\operatorname{Inf}_z)).

## 2. Independent spectral reconstruction

Let (m=2r+1), let (M_m) be odd majority, and put

\[
f_m=\frac{x+xy+zM_m-yzM_m}{2}. \tag{2}
\]

The four summands in (2) have disjoint Fourier supports.  Since (M_m) is
balanced, the (X)-empty orbit contains exactly the coefficients of (x)
and (xy), while every (X)-private singleton orbit vanishes.  Hence

\[
E_X^{f_m}(\varnothing)=\frac12,qquad
\widetilde\Lambda_X(f_m)=\psi_2(1/2). \tag{3}
\]

For (Y), the empty orbit vanishes.  The (x)-singleton orbit contains the
coefficients of (x) and (xy), so it has energy (1/2).  For each
majority coordinate (u_j), the coefficients of (zu_j) and (yzu_j)
have opposite signs and equal square (a_m^2/4), where

\[
a_m=\widehat M_m(\{u_j\})
=\frac{\binom{2r}{r}}{4^r}. \tag{4}
\]

Therefore

\[
\widetilde\Lambda_Y(f_m)=q(1/2)+m q(a_m^2/2), \tag{5}
\]

and subtracting (3) proves exactly

\[
\widetilde\Lambda_Y(f_m)-\widetilde\Lambda_X(f_m)
=m q(a_m^2/2)-\frac12. \tag{6}
\]

The central-binomial asymptotic (a_m^2\sim2/(\pi m)) gives

\[
m q(a_m^2/2)-\frac12
=\frac1\pi\log_2m+O(1). \tag{7}
\]

Thus the producer's divergence and leading constant are correct.

## 3. Pivotal accounting and strengthening

From (2) and Parseval,

\[
\operatorname{Inf}_x(f_m)=\frac12,qquad
\operatorname{Inf}_z(f_m)=\frac12. \tag{8}
\]

This proves the reviewed no-go.  The same calculation gives

\[
\operatorname{Inf}_y(f_m)
=\frac14+\frac14\sum_T\widehat M_m(T)^2
=\frac12. \tag{9}
\]

Consequently the stronger candidate

\[
\boxed{
\widetilde\Lambda_Y(f)
\le\widetilde\Lambda_X(f)
+C\sum_{v\in X\cup Y}\operatorname{Inf}_v(f)} \tag{10}
\]

also fails for every finite (C): the charge in (10) is always (3C/2)
on (f_m), while (7) diverges.  This strengthening rules out a fee using
all local coordinates of the two overlap blocks, not merely the symmetric
difference.

The full influence is

\[
I(f_m)=\frac32+\frac12 I(M_m)
=\frac32+\frac m2 a_m=\Theta(\sqrt m). \tag{11}
\]

Thus the counterfamily does not refute a global (CI(f)) payment.  It
pinpoints the missing reserve as private-core or whole-slice credit.

## 4. GU scope

The actual signed-mismatch reduction was re-read.  A universal estimate

\[
M(f)+(1+\eta)U(f)\le cI(f),\qquad0<\eta\le1,
\]

would imply

\[
G(f)\le(c+2)I(f)+(1-\eta)U(f)
\]

and (H(f)\le[2+2(c+2)/\eta]I(f)).  The orbit potential is only one
candidate mechanism for establishing that estimate.  Failure of (10) does
not refute the signed estimate, GU, or FEI.

## 5. Review conclusion

`B05-A023-CHANGING-OVERLAP-SWAP-NOGO-v1` is accepted without mathematical
repair at its declared scope.  The source report and proof have several
dropped inline TeX delimiters/backslashes; this is a typesetting issue only.
The stronger union-block no-go (10) is a B19 contribution and needs a fresh
A085/A090 review.
