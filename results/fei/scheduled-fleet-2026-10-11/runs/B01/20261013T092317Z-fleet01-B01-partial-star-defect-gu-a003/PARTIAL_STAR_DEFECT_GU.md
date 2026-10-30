# Partial-star point-defect GU' theorem

All variables are in \(\{0,1\}\), and \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\).
For \(R\subseteq[n]\), \(1\le |R|\le n\), put
\[
d_n(x)=1-2\mathbf 1_{\{x=0\}},\qquad
F_{n,R}(z,x)=(-1)^{z\sum_{j\in R}x_j}d_n(x).
\]
Write \(p_A=\widehat f(A)^2\), \(\pi(A)=\sum_{B\supseteq A}p_B\),
\[
U(f)=\sum_Ap_A\log_2\frac{\pi(A)}{p_A},\qquad
G(f)=\sum_i\left(U(f)-\mathbb E_bU(f\mid x_i=b)\right).
\]

## Theorem

Let \(\mathcal C_{\rm ps}\) be the smallest class containing every
\(F_{n,R}\), every parity-shifted point defect \(\chi_Rd_n\), every affine-
quadratic phase, arbitrary products of these blocks on disjoint variable
sets, and all physical restrictions and global signs. Then
\[
                         G(f)\le14I(f)                 \tag{1}
\]
for every \(f\in\mathcal C_{\rm ps}\). Consequently
\[
 U(f)\le14I(f),\qquad H(f)\le30I(f).                  \tag{2}
\]
The constants are independent of \(n\), \(|R|\), the number of inactive
defect variables, the rank of disjoint quadratic factors, and total
dimension.

This strictly extends the earlier full-star class \(R=[n]\): it allows an
unbounded number \(n-|R|\) of zero columns in the quadratic star. Those
coordinates retain exponentially small influence, so the earlier estimate
\(G\le (n+1)U\) cannot pay them. The proof below pairs their Fourier fibers
and retains the rare-event logarithmic refund.

## 1. Exact spectrum and influences

Put \(t=|R|\), \(\delta=2^{-n}\), \(e=4\delta^2\), and
\(a=(1/2-2\delta)^2\). Averaging first over \(z\) gives
\[
 \widehat F_{n,R}(0,S)=\tfrac12(\widehat d_n(S)+\widehat d_n(S\triangle R)),
 \quad
 \widehat F_{n,R}(1,S)=\tfrac12(\widehat d_n(S)-\widehat d_n(S\triangle R)).
\]
Thus the nonzero squared coefficients are located as follows:
\[
p_z=p_{z\cup R}=\tfrac14,\qquad p_\varnothing=p_R=a,
\qquad p_S=e\quad(S\ne\varnothing,R),                 \tag{3}
\]
and all remaining coefficients vanish. In particular the multiset is the
same as for the full star. Hence
\[
 U(F_{n,R})\le H(F_{n,R})\le4.                         \tag{4}
\]
Indeed, the two quarter-atoms contribute 1 to entropy, the two \(a\)-atoms
at most 1, and the dust at most
\((2^n-2)e(2n-2)\le 8(n-1)2^{-n}\le2\).

Physical-input accounting from (3) gives
\[
 \operatorname{Inf}_z=\tfrac12,
 \quad \operatorname{Inf}_{x_j}=\tfrac12\ (j\in R),
 \quad \operatorname{Inf}_{x_j}=2\delta\ (j\notin R). \tag{5}
\]
The last value is the rare point-defect edge; it is the case that requires a
non-crude estimate.

## 2. Inactive-coordinate fiber payment

Fix \(y\notin R\), and put \(k=n-t\ge1\). The two restrictions are
\(F_{n-1,R}\) and the pure star phase
\(q_R(z,x)=(-1)^{z\sum_{j\in R}x_j}\). The latter has four quarter-atoms at
\(\varnothing,R,z,z\cup R\), and \(U(q_R)=1\).

Let \(a'=(1/2-4\delta)^2\). Pair the parent Fourier sets \(C\) and
\(C\cup\{y\}\) over each child set \(C\subseteq[n]\setminus\{y\}\).
The two sets involving \(z\) cancel exactly between parent and children.
For \(C\not\subseteq R\), the paired contribution to
\(\Delta_yU\) is exactly \(e\). There are \(2^{n-1}-2^t\) such pairs, so
their total is at most \(2\delta\).

For \(\varnothing\ne C\subsetneq R\), set
\(h=n-|C|-1\),
\[
P=\tfrac12-2\delta+2^{h+1}e,
\qquad P'=\tfrac12-4\delta+2^{h+2}e=2P-\tfrac12.
\]
The paired contribution equals
\[
 e\left[h+4+\log_2\frac{Pe}{(P')^2}\right].          \tag{6}
\]
For \(n\ge4\), \(P\le1/2\), \(P'\ge1/4\), and
\(e2^h\le\delta\). Therefore \(e2^hP\le(P')^2\), so the bracket in
(6) is at most 4. All such pairs together cost at most
\(4e2^t\le8\delta\).

It remains to bound the special pairs \(C=\varnothing,R\). With
\(\phi(x)=x\log_2(1/x)\) and \(g(x,P)=x\log_2(P/x)\), their contributions are
\[
T_0=\phi(a)+e(n-1)-\tfrac12\phi(a')-\tfrac14,          \tag{7}
\]
\[
T_R=g(a,P_R)+e(k-1)-\tfrac12g(a',P'_R)-\tfrac18,       \tag{8}
\]
where \(P_R=1/2-2\delta+2^ke\) and
\(P'_R=1/2-4\delta+2^{k+1}e\).

For \(n\ge4\), \(a,a'\in[1/16,1/4]\) and
\(P_R,P'_R\in[1/4,1/2]\). On these intervals
\(|\phi'|<2.6\), \(|\partial_xg|<1.6\), and
\(|\partial_Pg|<1.45\). Also
\[
|a-\tfrac14|\le2\delta,
\quad |a'-\tfrac14|\le4\delta,
\quad |P_R-\tfrac12|\le2\delta,
\quad |P'_R-\tfrac12|\le4\delta,
\]
and \(e(n-1)<0.75\delta\). Since \(\phi\) is increasing on this interval,
rewriting (7) as
\(\tfrac12(\phi(a)-\phi(a'))+\tfrac12\phi(a)-1/4+e(n-1)\)
gives \(T_0<4\delta\). Centering (8) at
\(g(1/4,1/2)=1/4\) gives \(T_R<13\delta\).

Combining all pairs,
\[
 \Delta_yU< (2+8+4+13)\delta=27\delta
 <14(2\delta)=14\operatorname{Inf}_y(F_{n,R}).        \tag{9}
\]
For \(n\le3\), the same inequality follows directly from
\(\Delta_yU\le U\le H\), the support-size bound, and
\(\operatorname{Inf}_y=2^{1-n}\). Thus every inactive coordinate is paid
uniformly. For \(z\) and the active data coordinates, (4)--(5) give
\(\Delta_iU\le4=8\operatorname{Inf}_i\). Therefore
\[
                         G(F_{n,R})\le14I(F_{n,R}).     \tag{10}
\]

## 3. All parity-shifted defect boundaries

The restriction \(z=1\) is \(g_{n,R}=\chi_Rd_n\), now with arbitrary
\(R\), not only \(R=[n]\). Its spectrum has one mass
\(A=(1-2\delta)^2\) at \(R\) and dust mass \(e\) everywhere else. Hence
\(H(g_{n,R})<3\). Active coordinates have influence \(1-2\delta\), so their
loss is at most six times influence.

For an inactive coordinate, pair Fourier sets as above. Generic pairs again
cost exactly \(e\), totaling at most \(2\delta\). Proper subsets of \(R\)
have the analogue of (6), now with
\[
P=1-4\delta+2^{h+1}e,
\qquad P'=1-8\delta+2^{h+2}e=2P-1.
\]
For \(n\ge4\), their bracket is at most 4 and their total at most
\(8\delta\). The special big-atom pair contributes at most
\[
A\log_2(P_R/A)+e(k-1)
\le \frac{P_R-A}{\ln2}+e(k-1)<7\delta,                \tag{11}
\]
because the omitted child term is nonnegative and
\(P_R-A=(2^k-1)e\le4\delta\). Thus an inactive boundary loss is less than
\(17\delta<9(2\delta)\). The cases \(n\le3\) follow from
\(\Delta_iU\le H\le n\). Consequently
\[
                         G(\chi_Rd_n)\le9I(\chi_Rd_n). \tag{12}
\]

## 4. Closure, tensors, and FEI consequence

Restrictions preserve the stated class:

- \(z=0\) gives \(d_n\), and \(z=1\) gives \(\chi_Rd_n\);
- an active \(x_j=0\) gives \(F_{n-1,R\setminus\{j\}}\), while
  \(x_j=1\) kills the defect and gives an affine-quadratic phase;
- an inactive \(x_j=0\) gives \(F_{n-1,R}\), while \(x_j=1\) gives a pure
  star phase;
- restrictions of \(\chi_Rd_n\) remain parity-shifted defects or affine
  characters, and restrictions of affine-quadratic phases remain such.

The source theorem `B01_ALL_QUADRATIC_GU_v1` gives \(G(q)\le3I(q)\).
For disjoint products, \(U,G,I\) are exactly additive because both Fourier
probabilities and upper-set masses factor. Equations (10)--(12) therefore
prove (1) on the whole class.

Finally, restriction induction is noncircular. If all proper restrictions
satisfy \(U\le14I\), then for a function on \(m\) relevant coordinates,
\[
mU(f)\le\sum_i\mathbb E U(f\mid x_i)+14I(f)
       \le14(m-1)I(f)+14I(f)=14mI(f).
\]
This proves \(U\le14I\); combining it with the accepted identity
\(H\le2I+2U\) proves (2).

The result is a proper-class theorem, not universal GU' and not full FEI.
It pays arbitrarily many rare inactive coordinates for one quadratic centre.
The next unpaid step is two or more overlapping centres, where the same dust
fibers can acquire incompatible upper-set caps and the pairing used in (6)
need not remain single-use.
