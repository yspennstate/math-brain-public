# A square-function bound from restricted transfer between diffusion scales

Let \(M\geq3\), let \(B=(I+\mathrm{adjacency})/5\) on
\(\mathbb T_M=(\mathbb Z/M\mathbb Z)^2\), and put
\[
P_{xy}=M^{-2},\qquad Q=I-P,\qquad A=I-B,\qquad
G_u=(I-uB)^{-1},\qquad H_u=G_uQ.
\tag{1}
\]
The order on symmetric matrices is denoted by \(\preceq\). All vector
norms and operator norms are Euclidean. On the nonconstant Fourier mode
\(k\), these matrices have eigenvalues determined by
\[
b_k=\frac{1+2\cos(2\pi k_1/M)+2\cos(2\pi k_2/M)}5,
\quad a_k=1-b_k,
\quad g_u(k)=1-ub_k=1-u+ua_k.
\tag{2}
\]
In particular, \(-3/5\leq b_k\leq1\), \(0<a_k\leq8/5\) on
\(Q\), and \(g_u(k)>0\) for \(u<1\).

Define the dyadic spectral projections
\[
\Pi_j=\mathbf1_{(2^{-j},\,2^{1-j}]}(A)Q,\qquad j=0,1,\ldots.
\tag{3}
\]
They are mutually orthogonal and sum to \(Q\); only finitely many are
nonzero for fixed \(M\). Their intervals specify the boundary convention
at every dyadic eigenvalue.

## The bound

Let \(E(u)=QE(u)Q\) be a measurable real symmetric contraction for
\(0\leq u\leq t<1\). Suppose that, for an integer \(h\geq0\),
\[
\Pi_iE(u)\Pi_j=0\qquad\text{if }|i-j|>h
\tag{4}
\]
for almost every \(u\). There is no condition on its temporal variation.
Then
\[
0\preceq K_t:=\int_0^t u^2E(u)A|B|G_u^2E(u)\,du
\preceq 2(2h+1)t^2Q.
\tag{5}
\]
Here \(|B|\) has eigenvalues \(|b_k|\).

For \(\delta\geq0\), \(W\geq1\), set
\[
D(u)=\frac{\delta u}{W^2}A^{1/2}G_uE(u)G_uA^{1/2},
\quad U_{u,t}=(I-uB)G_t,
\quad
\mathcal J_t[D]=W^2\int_0^t U_{u,t}D(u)BD(u)U_{u,t}\,du.
\tag{6}
\]
Thus \(D\) satisfies the pointwise envelope
\[
-\frac{\delta u}{W^2}AG_u^2Q\preceq D(u)
\preceq\frac{\delta u}{W^2}AG_u^2Q.
\tag{7}
\]
Under (4),
\[
-\frac{2(2h+1)\delta^2t}{W^2}H_t
\preceq\mathcal J_t[D]
\preceq\frac{2(2h+1)\delta^2t}{W^2}H_t.
\tag{8}
\]
In particular,
\[
|\mathcal J_t[D]_{xy}|
\leq\frac{2(2h+1)\delta^2t}{W^2}r_M(t),
\qquad r_M(t)=(H_t)_{00}.
\tag{9}
\]
The return estimate established in round 3 gives
\[
\sup_{0\leq t<1}r_M(t)\leq C(1+\log M),
\qquad
r_M(t)=\frac5{4\pi}\log\frac1{1-t+M^{-2}}+O(1)
\quad(t\geq1/2).
\tag{10}
\]
Thus fixed \(h\) suffices for a single return-kernel logarithm, regardless
of temporal oscillations.

The linear order in \(h\) in (5), and the order
\((h+1)\log M\) in the uniform entry bound, are necessary in general.
Specifically, for integers \(1\leq q\leq R\), there is a continuous
piecewise linear contraction path on
\[
M=8^{R+2},\qquad t=1-M^{-4},\qquad h=6q+6,
\tag{11}
\]
satisfying (4) and
\[
\mathcal J_t[D]_{00}
\geq\frac{\delta^2\log8}{1440000W^2}\,qR.
\tag{12}
\]
For a real unit Fourier eigenvector \(e\), the same path satisfies
\[
\langle e,K_te\rangle\geq\frac q{20000},\qquad
\frac{\langle e,\mathcal J_t[D]e\rangle}
     {\langle e,H_te\rangle}
\geq\frac{\delta^2q}{30000W^2}.
\tag{13}
\]
The constants are not asserted to be optimal. The claims of sharpness
refer to orders of growth.

## Proof of the square-function estimate

On the band \(\Pi_i\), put \(\lambda_i=2^{-i}\). If
\(\lambda_i<a\leq2\lambda_i\), then \(|1-a|\leq1\), and
\[
\frac{u^2a|1-a|}{(1-u+ua)^2}
\leq q_i(u):=\frac{2u^2\lambda_i}{(1-u+u\lambda_i)^2}.
\tag{14}
\]
This includes negative eigenvalues of \(B\). Since
\[
\frac{d}{du}\frac{u}{1-u+u\lambda}
=\frac1{(1-u+u\lambda)^2},
\]
we have, for every \(0<\lambda\leq1\),
\[
\int_0^t\frac{2u^2\lambda}{(1-u+u\lambda)^2}\,du
\leq\frac{2\lambda t^3}{1-t+t\lambda}
\leq2t^2.
\tag{15}
\]
No division by \(1-\lambda\) is involved. The case \(\lambda=1\)
and the case \(t=0\) are included.

Let \(v=Qv\) and
\[
R_i=\sum_{\substack{j\geq0\\|i-j|\leq h}}\Pi_j.
\]
By (4), \(\Pi_iE(u)v=\Pi_iE(u)R_iv\). Contractivity therefore gives
\[
\|\Pi_iE(u)v\|^2\leq\|R_iv\|^2.
\tag{16}
\]
Diagonalizing only the deterministic positive matrix
\(u^2A|B|G_u^2\), and then applying (14)–(16), gives
\[
\begin{split}
\langle v,K_tv\rangle
&\leq\sum_i\int_0^t q_i(u)\|\Pi_iE(u)v\|^2du\\
&\leq2t^2\sum_i\|R_iv\|^2\\
&=2t^2\sum_j
  \#\{i\geq0:\ |i-j|\leq h\}\,\|\Pi_jv\|^2\\
&\leq2(2h+1)t^2\|v\|^2.
\end{split}
\tag{17}
\]
Only finitely many summands are nonzero; an index of \(R_i\) need only
range within \(h\) of a nonzero spectral band.
The integral exists because \(t<1\) and the integrand is bounded and
measurable. Positivity of the integrand proves the other side of (5).

For clarity, the multiplicity \(2h+1\) can also be checked by grouping
the indices \(i\) into residue classes modulo \(2h+1\). Within one
class the integer intervals \([i-h,i+h]\) are disjoint, so the
corresponding \(R_i\) have orthogonal ranges and
\(\sum_i\|R_iv\|^2\leq\|v\|^2\) in that class. Summing the
\(2h+1\) classes reproduces (17), including truncated intervals near
index zero.

## Passage to the quadratic drift

Let \(C_t=A^{1/2}G_tQ\). The deterministic functions of \(B\)
commute with one another, but no such commutation with \(E(u)\) is used.
Cancellation of \((I-uB)G_u\) in (6) gives the exact identity
\[
\mathcal J_t[D]
=\frac{\delta^2}{W^2}C_t
 \left[\int_0^t u^2E(u)ABG_u^2E(u)du\right]C_t.
\tag{18}
\]
The bracket is between \(-K_t\) and \(K_t\). For \(t>0\),
\[
tC_t^2=tAG_t^2Q\preceq H_t,
\tag{19}
\]
because \(ta_k\leq g_t(k)\) at every nonzero mode. Combining (5),
(18), and (19) proves (8). For \(t=0\) the drift is zero.

If \(-cH_t\preceq J\preceq cH_t\) and \(J=QJQ\), then on
\(Q\) one can write \(J=cH_t^{1/2}TH_t^{1/2}\), with \(T\) a
symmetric contraction (the case \(c=0\) is immediate). Hence
\[
|J_{xy}|\leq c\sqrt{(H_t)_{xx}(H_t)_{yy}}=c r_M(t).
\]
Translation invariance is used for \(H_t\), not for \(J\).
This proves (9).

## A version with decaying transfer instead of exact zeros

Suppose, in place of (4), that there is a nonnegative sequence
\((c_m)_{m\in\mathbb Z}\) such that
\[
\sup_{0\leq u\leq t}\|\Pi_iE(u)\Pi_j\|\leq c_{i-j},
\qquad S:=\sum_{m\in\mathbb Z}c_m<\infty.
\tag{20}
\]
An essential supremum suffices. Then
\[
K_t\preceq2S^2t^2Q,
\qquad
-\frac{2S^2\delta^2t}{W^2}H_t
\preceq\mathcal J_t[D]
\preceq\frac{2S^2\delta^2t}{W^2}H_t.
\tag{21}
\]
Indeed, writing \(v_j=\Pi_jv\), the triangle inequality and weighted
Cauchy–Schwarz give
\[
\|\Pi_iE(u)v\|^2
\leq\left(\sum_j c_{i-j}\|v_j\|\right)^2
\leq S\sum_j c_{i-j}\|v_j\|^2.
\tag{22}
\]
Multiply by \(q_i(u)\), integrate using (15), and sum over \(i\).
Since \(\sum_i c_{i-j}\leq S\), the result is
\(\langle v,K_tv\rangle\leq2S^2t^2\|v\|^2\). The remaining
argument is (18)–(19). For example,
\(c_m=C_0\rho^{|m|}\), \(0<\rho<1\), gives
\(S=C_0(1+\rho)/(1-\rho)\), independent of \(M\).
The sharper linear estimate (5) uses contractivity in addition to the
finite range and does not follow by substituting indicator weights into
(21).

## Continuous examples showing the dependence on the number of scales

Fix \(1\leq q\leq R\) and the parameters in (11). Put
\[
n_r=8^r,\quad s_r=n_r^2/M^2,\quad m_r=8^{\max(r-q,0)},
\quad
\mathcal K_{r,q}=\{k\in\{1,\ldots,n_r\}^2:
                         \max(k_1,k_2)>m_r\}.
\tag{23}
\]
For \(k\in\mathcal K_{r,q}\), pair \(k\) with
\(j_r(k)=(k_1+3n_r,k_2)\). Use the real cosine eigenvectors
\[
e_k(x)=\frac{\sqrt2}{M}\cos(2\pi k\cdot x/M).
\tag{24}
\]
All frequencies used are in the positive quadrant, with first coordinate
at most \(4n_r\leq M/16\), and second coordinate at most
\(n_r\leq M/64\). They are nonzero and no two distinct ones are
negatives modulo \(M\). The identities for products of cosines and
the vanishing of nonconstant exponential sums therefore prove that
these vectors are centered, orthonormal, and have \(e_k(0)^2=2/M^2\).
If a frequency is reused at another scale, it denotes the same vector.
The input and output sets at a fixed \(r\) are disjoint; the map
\(k\mapsto j_r(k)\) is injective.

Let \(T_{r,q}\) interchange each pair \(e_k,e_{j_r(k)}\), and
vanish on the orthogonal complement. It is a real symmetric centered
contraction of norm one. Let \(\chi_r\), in the variable \(v=1-u\),
vanish outside \([s_r,2s_r]\), equal one on
\([5s_r/4,7s_r/4]\), and be linear on the two remaining pieces.
Set
\[
E(u)=\sum_{r=1}^R\chi_r(u)T_{r,q}.
\tag{25}
\]
Since \(s_{r+1}=64s_r\), at most one term is nonzero. Thus (25)
is a continuous piecewise linear symmetric contraction. It vanishes
near zero and near \(t\). Its total variation in operator norm is
\(2R\), since every excursion goes from zero to a norm-one matrix
and back, with a zero interval before the next excursion.

### Verification of the scale restriction

For these frequencies, the elementary bounds on sine give
\[
\frac{16}{5}\frac{|k|^2}{M^2}
\leq a_k\leq\frac{4\pi^2}{5}\frac{|k|^2}{M^2}
<8\frac{|k|^2}{M^2}.
\tag{26}
\]
Indeed \(a_k=(4/5)\sum_{\alpha=1}^2\sin^2(\pi k_\alpha/M)\),
and \(2x/\pi\leq\sin x\leq x\) on \([0,\pi/2]\).
The strict numerical bound uses \(\pi^2<10\).

For \(j=j_r(k)\), \(9n_r^2\leq|j|^2\leq17n_r^2\), so
\[
28s_r\leq a_j\leq136s_r.
\tag{27}
\]
Also \(a_j>a_k\), because sine squared is strictly increasing in
the first coordinate in the range under consideration. Since
\(\max(k_1,k_2)>m_r\) and \(n_r/m_r=8^{\min(r,q)}\),
\[
1<\frac{a_j}{a_k}
<\frac{136\cdot5}{16}\left(\frac{n_r}{m_r}\right)^2
\leq\frac{85}{2}\,64^q
<64^{q+1}.
\tag{28}
\]
If two positive eigenvalues in the intervals (3) have band indices
separated by \(d\), their ratio, larger divided by smaller, exceeds
\(2^{d-1}\). Therefore (28) implies \(d<6q+7\), hence
\(d\leq6q+6\). The only nonzero matrix elements of \(T_{r,q}\)
join these pairs. This proves (4) with \(h=6q+6\), including every
dyadic boundary case.

### Time integral for one pair

As \(s_r\leq1/4096\), (27) gives \(a_j\leq136/4096<1/16\).
The output satisfies \(a_k\leq16s_r<1/16\) as well. Thus all
used modes have \(b>1/2\). On the support of \(\chi_r\),
\(u\geq1/2\) and
\[
g_u(j)=v+ua_j\leq138s_r.
\]
Consequently, on its plateau,
\[
\frac{u^2a_jb_j}{g_u(j)^2}
\geq\frac{28}{8\cdot138^2s_r}
\geq\frac1{10000s_r}.
\tag{29}
\]
The last comparison follows from
\(28\cdot10000>8\cdot138^2=152352\).
The plateau has length \(s_r/2\), whence
\[
\int_0^t\chi_r(u)^2\frac{u^2a_jb_j}{g_u(j)^2}\,du
\geq\frac1{20000}.
\tag{30}
\]
The integration interval contains the full support: if \(\mu=M^{-4}\),
then \(\mu<s_1=64/M^2\), and \(2s_R<1\).

Every nonzero eigenvalue of \(A\) satisfies
\[
a_k\geq a_*:=\frac45\sin^2(\pi/M)\geq\frac{16}{5M^2}.
\]
Thus \(\mu/a_k\leq5/(16M^2)<1/2\). At \(t=1-\mu\),
\[
g_t(k)\leq a_k+\mu\leq\frac32a_k,
\qquad \frac{a_k}{g_t(k)^2}\geq\frac4{9a_k},
\qquad \frac{a_k}{g_t(k)}\geq\frac23.
\tag{31}
\]

### Diagonal and operator lower bounds

In a real eigenbasis extending (24), the matrix
\(T_{r,q}ABG_u^2T_{r,q}\) is diagonal: it exchanges the two
diagonal coefficients on every pair. All retained coefficients are
positive. The disjoint time supports in (25) prevent cross terms
between different \(r\), even where a frequency is reused.
The bracket in (18) is therefore diagonal and positive semidefinite
in this fixed basis. Keeping only the output modes, (30)–(31) give
\[
\mathcal J_t[D]_{00}
\geq\frac{\delta^2}{W^2}\frac1{20000}\frac49\frac2{M^2}
       \sum_{r=1}^R\sum_{k\in\mathcal K_{r,q}}\frac1{a_k}.
\tag{32}
\]
For \(l=m_r+1,\ldots,n_r\), the shell
\(\max(k_1,k_2)=l\) has \(2l-1\geq l\) points, all with
\(|k|^2\leq2l^2\). Applying (26),
\[
\begin{split}
\sum_{k\in\mathcal K_{r,q}}\frac1{a_k}
&\geq\frac{M^2}{16}\sum_{l=m_r+1}^{n_r}\frac1l\\
&\geq\frac{M^2}{16}\log\frac{n_r+1}{m_r+1}\\
&\geq\frac{M^2}{16}
   \bigl(\min(r,q)\log8-\log2\bigr)\\
&\geq\frac{M^2\log8}{32}\min(r,q).
\end{split}
\tag{33}
\]
Here \(m_r\geq1\), so \(m_r+1\leq2m_r\); also
\(\min(r,q)\geq1\) and \(\log2=(\log8)/3\). Inserting
(33) into (32) yields
\[
\mathcal J_t[D]_{00}
\geq\frac{\delta^2\log8}{720000W^2}
         \sum_{r=1}^R\min(r,q).
\tag{34}
\]
The exact sum is
\[
\sum_{r=1}^R\min(r,q)
=qR-\frac{q(q-1)}2\geq\frac{qR}{2},
\tag{35}
\]
which proves (12).

For (13), take \(e=e_{(2,1)}\). When \(1\leq r\leq q\),
\(m_r=1\), so this mode is retained in every one of those \(q\)
swaps. Formula (30) gives a coefficient at least \(1/20000\)
in \(K_t\), since \(|b_j|=b_j\) there. The same lower bound
holds in the signed bracket of (18). All other contributions are
nonnegative. This proves the first part of (13). Dividing its drift
coefficient by the \(H_t\) coefficient, and using (31), gives
\[
\frac{\langle e,\mathcal J_t[D]e\rangle}
     {\langle e,H_te\rangle}
\geq\frac{\delta^2}{W^2}\frac q{20000}
                            \frac{a_{(2,1)}}{g_t((2,1))}
\geq\frac{\delta^2q}{30000W^2}.
\]
Since \(h=6q+6\) and \(\log M=(R+2)\log8\), (12)–(13)
establish the asserted sharp orders for this family of parameters.

## Independent checks and limits

The scalar integral constant in (15) has a second verification. Set
\(z=u/(1-u+u\lambda)\); then
\(dz=du/(1-u+u\lambda)^2\), and
\[
\int_0^t q_i(u)du
=2\lambda\int_0^{t/(1-t+t\lambda)}u(z)^2dz
\leq\frac{2\lambda t^3}{1-t+t\lambda}\leq2t^2.
\]
This check does not use a formula dividing by an eigenvalue of \(B\).

The normalization in (18) also follows by setting
\(Y_u=(I-uB)D(u)(I-uB)\). Direct multiplication gives
\[
\mathcal J_t[D]=W^2G_t\left[\int_0^tY_uBG_u^2Y_u\,du\right]G_t,
\qquad
Y_u=\frac{\delta u}{W^2}A^{1/2}E(u)A^{1/2}.
\]
Substitution gives (18), with the external \(W^2\) canceling two
factors \(W^{-2}\) to leave \(W^{-2}\).
On a single pair, multiplying
\(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\)
on both sides of \(\operatorname{diag}(f_k,f_j)\) gives
\(\operatorname{diag}(f_j,f_k)\). Thus the input coefficient used
in (29)–(32) is indeed the one at \(j\).

The harmonic lower bound in (33) can instead be checked using disjoint
rows \(k_2=l\), \(1\leq k_1\leq l\), for
\(m_r<l\leq n_r\). These \(l\) retained points each have
\(|k|^2\leq2l^2\), giving the same \(1/(2l)\) contribution
before multiplying by \(M^2/8\). The constant in (34) is separately
checked by
\((1/20000)(4/9)(2/32)=1/720000\).
The coefficient \(1/1440000\) in (12) is the further factor one
half in (35). Counting the sum in (35) by layers,
\(\sum_{s=1}^q(R-s+1)\), gives the same exact value.

The upper bounds include zero and negative eigenvalues of \(B\), while
the examples use only positive ones. The constant mode is removed
throughout. The examples have strictly positive mass \(M^{-4}\),
continuous paths, and \(D(0)=0\). For fixed \(q\), their total
variation grows as \(2R\) although their spectral range \(h=6q+6\)
stays fixed. Thus (5) supplies a uniform bound where the earlier
variation estimate grows with volume. It also applies to arbitrary
measurable paths satisfying (4) or (20), including those of infinite
variation.

The source of the deterministic quadratic term and two-coordinate
propagator is equations (2.31)–(2.38) of Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices:
Exponential Lower Bounds*,
[arXiv:2609.24426v4](https://arxiv.org/html/2609.24426v4).
Their Ward identities (3.21)–(3.22) constrain resolvent row and column
sums. No implication from those identities or entrywise positivity
to (4) or (20) is proved here. In particular, the examples are not
claimed to be realizable resolvent errors or to satisfy all constraints
of the full two-loop observable.

Neither the normalized envelope (7) nor the spectral transfer assumptions
have been established for the actual random error. Symmetry and exact
centering are also hypotheses of the deterministic result. This proves
a conditional replacement for temporal bounded variation, not a new
delocalization threshold, localization length, or local-statistics theorem.
