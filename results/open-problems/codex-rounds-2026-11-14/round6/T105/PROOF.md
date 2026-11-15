# Moving adjacent counts and a larger flat-torus gap bound

Put

\[
R(c)=c^4-4c^3+4c^2+24c-40.
\]

Let \(c_0\) be the unique solution in \((\sqrt7-1,7/4)\) of

\[
R(c_0)=\frac{48}{121},\qquad
\Gamma=\frac{c_0^2+2c_0+6}{6}.
\tag{1}
\]

**Theorem.** For almost every flat two-dimensional torus, let
\(x_1<x_2<\cdots\) be the positive eigenvalues, counted once for each
global sign pair of dual-lattice vectors and unfolded to mean spacing
one. Then

\[
\limsup_{i\to\infty}(x_{i+1}-x_i)\ge\Gamma
>\frac{121289}{60000}>\frac{2021}{1000}=2.021.
\tag{2}
\]

In particular, infinitely many gaps exceed 2.021. The theorem does not
assert infinitely many gaps exceeding the exact endpoint \(\Gamma\).

The external inputs are the almost-everywhere pair correlation recorded
in Section 1.2 and the averaged triple-correlation Theorem 1 of Christoph
Aistleitner, Valentin Blomer and Maksym Radziwiłł, *Triple correlation
and long gaps in the spectrum of flat tori*, J. Eur. Math. Soc. 26
(2024), 41–74,
[published text](https://ems.press/content/serial-article-files/42560?nt=1),
[arXiv:1809.07881](https://arxiv.org/abs/1809.07881).
Theorem 1 averages over every finite parameter rectangle and is uniform
over both interval arguments in a fixed bounded interval. No pointwise
triple-correlation limit is assumed.

## 1. Finite count inequalities

For a finite increasing sequence \(x_1<\cdots<x_N\), define

\[
\begin{aligned}
P_N(I)&=\frac1N\#\{(i,j):1\le i,j\le N,\ x_j-x_i\in I\},\\
U_N(I)&=\frac1N\#\{(i,j,k):1\le i,j,k\le N,
\ i,j,k\text{ pairwise distinct},\ x_j-x_i,x_k-x_i\in I\},\\
F_N(s)&=\frac1N\#\{i<N:x_{i+1}-x_i\le s\}.
\end{aligned}
\tag{3}
\]

All intervals used in these counts lie in \((0,\infty)\).
Write \(P_N(s)=P_N((0,s])\). The last two indices in \(U_N\)
are ordered.

For every nonnegative integer \(n\),

\[
\mathbf1_{n>0}\ge n-\frac{n(n-1)}2,\qquad
\mathbf1_{n>0}\ge\frac23 n-\frac16n(n-1).
\tag{4}
\]

At \(n=0\) the residuals vanish. At positive integers they are,
respectively, \((n-1)(n-2)/2\) and \((n-2)(n-3)/6\), both
nonnegative. Apply these inequalities to the number of later levels
within distance \(s\) of each anchor and sum over anchors. This gives

\[
F_N(s)\ge P_N(s)-\frac12U_N((0,s]),\qquad
F_N(s)\ge\frac23P_N(s)-\frac16U_N((0,s]).
\tag{5}
\]

For nonnegative integers \(A,B\), with \(T=A+B\), the
adjacent-count inequality is

\[
\mathbf1_{A>0}+2\mathbf1_{T>0}
\ge2T-\frac12T(T-1)-\frac12B(B-1).
\tag{6}
\]

At \(A=B=0\) equality holds. At \(A=0,B\ge1\) the residual is
\((B-1)(B-2)\). At \(A\ge1\) the residual is

\[
\frac{(T-2)(T-3)+B(B-1)}2.
\]

These expressions are nonnegative for all the indicated integers,
including arbitrarily large counts. At anchor \(i\), use the numbers
of later levels in \((x_i,x_i+a]\) and \((x_i+a,x_i+t]\), where
\(0<a<t\). Summing (6) gives the exact finite inequality

\[
F_N(a)+2F_N(t)\ge
2P_N(t)-\frac12U_N((0,t])-\frac12U_N((a,t]).
\tag{7}
\]

There are no boundary errors in (5) or (7): all counts are truncated
at the same index \(N\). The last anchor contributes zero.

## 2. Integrating moving lengths

Let \(w>0\). For \(0\le u\le w\), put

\[
a(u)=1+u,\qquad t(u)=1+w+2u,\qquad b(u)=t(u)-a(u)=w+u.
\tag{8}
\]

Change variables separately in the two terms to obtain the identity

\[
\begin{aligned}
\int_0^w\bigl(F_N(a(u))+2F_N(t(u))\bigr)\,du
&=\int_1^{1+w}F_N(s)\,ds+
  \int_{1+w}^{1+3w}F_N(s)\,ds\\
&=\int_1^{1+3w}F_N(s)\,ds.
\end{aligned}
\tag{9}
\]

Consequently integrating (7) gives a lower bound for the integral on
the entire interval \([1,1+3w]\). There is no monotonicity loss.

To compute its Poisson benchmark, write

\[
L_2(s)=\frac{4s-s^2}{6},\qquad
K(a,t)=2t-\frac{t^2+(t-a)^2}{2}.
\]

Replacing pair counts by interval lengths and ordered triple counts
by squared lengths replaces the right side of (7) by \(K(a,t)\).
Direct expansion gives

\[
K(a,t)-L_2(a)-2L_2(t)
=\frac{2t-2t^2+3at-a^2-2a}{3}.
\tag{10}
\]

Substituting (8) in (10) gives

\[
K(a(u),t(u))-L_2(a(u))-2L_2(t(u))
=\frac{w-2w^2}{3}+\frac{1-5w}{3}u-u^2.
\tag{11}
\]

Integrating this polynomial, and using the same changes of variables
as in (9) for \(L_2\), yields the exact gain

\[
\begin{aligned}
\eta(w)
&:=\int_0^wK(a(u),t(u))\,du-
   \int_1^{1+3w}L_2(s)\,ds\\
&=\frac{w^2}{2}-\frac{11w^3}{6}.
\end{aligned}
\tag{12}
\]

This family is optimized by

\[
w=\frac2{11},\qquad d:=1+3w=\frac{17}{11},\qquad
\eta:=\eta(w)=\frac2{363}.
\tag{13}
\]

Indeed \(\eta'(w)=w(1-11w/2)\), and, independently, the exact
factorization

\[
\frac2{363}-\eta(w)=\frac{11w+1}{6}
\left(w-\frac2{11}\right)^2
\tag{14}
\]

proves maximality for every \(w\ge0\). This is only an optimality
claim for the family (8), starting at 1 with consecutive windows.

Hereafter fix (13). The two windows in (9) are
\([1,13/11]\) and \([13/11,17/11]\). Both lie below
\(\sqrt7-1\), since \((28/11)^2<7\), or equivalently
\(784<847\).

## 3. The scalar integral for an eventual gap bound

Fix

\[
2\le G\le B:=\frac{67}{32},\qquad
c=c(G)=\sqrt{6G-5}-1.
\tag{15}
\]

Then

\[
\sqrt7-1\le c\le\frac74<2,\qquad
G=\frac{c^2+2c+6}{6},\qquad
G-c=\frac{(c-2)^2+2}{6}>0.
\tag{16}
\]

In particular \(1<d<c<G\) throughout this range. Define

\[
H_G(s)=
\begin{cases}
s-s^2/2,&0\le s\le1,\\
L_2(s),&1\le s\le c,\\
1-G+s,&c\le s\le G.
\end{cases}
\tag{17}
\]

The pieces match at 1 and \(c\), by (16). Integration gives

\[
\begin{aligned}
I(G):=\int_0^G H_G(s)\,ds
&=\frac13+\left[\frac{s^2}{3}-\frac{s^3}{18}\right]_1^c
  +\left[(1-G)s+\frac{s^2}{2}\right]_c^G\\
&=G-\frac{G^2}{2}+\frac1{18}+\frac{c^2}{6}+\frac{c^3}{9}.
\end{aligned}
\tag{18}
\]

Put

\[
D(G)=I(G)-G+1
=1-\frac{G^2}{2}+\frac1{18}+\frac{c^2}{6}+\frac{c^3}{9}.
\tag{19}
\]

Assume for the moment that all but finitely many gaps of the infinite
sequence are at most \(G\), and let \(M\) bound the number of
exceptions. For \(0\le s\le G\), each nonexceptional consecutive
gap in \((s,G]\) is a pair counted by \(P_N((s,G])\). Thus

\[
F_N(s)\ge1-P_N((s,G])-\frac{M+1}{N}.
\tag{20}
\]

Also, with \(g_i=x_{i+1}-x_i\), the exact identity

\[
\begin{aligned}
\int_0^GF_N(s)\,ds
&=\frac1N\sum_{i<N}(G-g_i)_+\\
&=\frac{G(N-1)}N-\frac{x_N-x_1}{N}
  +\frac1N\sum_{i<N}(g_i-G)_+
\end{aligned}
\tag{21}
\]

holds. The last sum is eventually a fixed finite constant. For a
unit-density torus spectrum, Weyl's law gives \(x_N/N\to1\), hence

\[
\int_0^GF_N(s)\,ds\longrightarrow G-1.
\tag{22}
\]

The range (15) extends the range used in the preceding report. No
additional correlation input is required for this extension: (5),
(7) and (20) hold at every indicated length, and the matching identity
in (16) still has \(c<2\). Only these finite inequalities and the
integral (18) will be used; a pointwise asymptotic bound by \(H_G\)
is not asserted.

## 4. One nonnegative triple functional

Let \(\mu\) denote the hyperbolic parameter measure used in the
cited paper. It has a positive continuous density in the interior of
the parameter domain. The following consequence of rectangle-averaged
convergence will be used. If \(Q_N\ge0\) and

\[
\int_E Q_N\,d\mu\longrightarrow q\mu(E)
\tag{23}
\]

for every finite rectangle \(E\) contained in the interior, with
\(q\ge0\) fixed, then

\[
\liminf_N Q_N\le q\quad\text{almost everywhere}.
\tag{24}
\]

For a proof, suppose that for some \(\varepsilon>0\) the set
\(A=\{\liminf Q_N\ge q+\varepsilon\}\) has positive measure.
The density theorem gives such a rectangle \(E\) with
\(\mu(A\cap E)/\mu(E)>q/(q+\varepsilon)\). Nonnegativity and
Fatou's lemma give

\[
q\mu(E)=\liminf_N\int_E Q_N\,d\mu
\ge\int_E\liminf_N Q_N\,d\mu
\ge(q+\varepsilon)\mu(A\cap E)>q\mu(E),
\]

a contradiction. Taking the union over positive rational margins
proves (24).

Now define, for the fixed \(G\) in (15),

\[
\begin{aligned}
\mathcal P_N(G)={}&\int_0^1P_N(s)\,ds
  +\frac23\int_d^cP_N(s)\,ds\\
&+\int_c^G\bigl(1-P_N((s,G])\bigr)\,ds
  +2\int_0^w P_N(t(u))\,du,\\
Q_N(G)={}&\frac12\int_0^1 U_N((0,s])\,ds
  +\frac16\int_d^c U_N((0,s])\,ds\\
&+\frac12\int_0^w
  \bigl(U_N((0,t(u)])+U_N((a(u),t(u)])\bigr)\,du.
\end{aligned}
\tag{25}
\]

All coefficients in \(Q_N\) are nonnegative. Integrate the first
inequality of (5) on \([0,1]\), the second on \([d,c]\), and
(20) on \([c,G]\); use integrated (7) on \([1,d]\), via (9).
Adding these four inequalities gives

\[
\int_0^G F_N(s)\,ds\ge
\mathcal P_N(G)-Q_N(G)-\frac{(M+1)(G-c)}N.
\tag{26}
\]

For almost every torus, pair correlation gives \(P_N(s)\to s\),
uniformly on \([0,B]\). To obtain this from convergence at rational
lengths, intersect the countably many full-measure sets, then squeeze
the nondecreasing functions \(P_N\) on a finite rational mesh; their
limit is continuous. Also
\(P_N((s,G])=P_N(G)-P_N(s)\). It follows that

\[
\mathcal P_N(G)\longrightarrow
p_G:=\int_0^1s\,ds+\frac23\int_d^c s\,ds
+\int_c^G(1-G+s)\,ds+2\int_0^w t(u)\,du.
\tag{27}
\]

The uniformity in Theorem 1 permits integrating its averaged error
over each bounded length parameter in (25), including the varying
interval \((a(u),t(u)]\). All these intervals lie in \([0,B]\).
Tonelli's theorem applies to the nonnegative counts. Thus (23) holds
for the entire \(Q_N(G)\), with benchmark

\[
q_G=\frac12\int_0^1s^2\,ds+\frac16\int_d^c s^2\,ds
+\frac12\int_0^w\bigl(t(u)^2+b(u)^2\bigr)\,du.
\tag{28}
\]

Applying (24) once to this functional gives
\(\liminf_NQ_N(G)\le q_G\) almost everywhere. Since \(q_G\)
is finite, a subsequence realizes this bound up to \(o(1)\).
This is a subsequence for the full sum; no simultaneous bounds for
its separate terms are needed.

Subtracting (28) from (27), using (12), (17) and (18), gives

\[
\begin{aligned}
p_G-q_G
&=\int_0^1(s-s^2/2)\,ds+\int_d^c L_2(s)\,ds
  +\int_c^G(1-G+s)\,ds
  +\int_0^wK(a(u),t(u))\,du\\
&=I(G)+\eta.
\end{aligned}
\tag{29}
\]

Along that subsequence, (22), (26) and (29) imply

\[
G-1\ge I(G)+\eta,
\quad\text{or equivalently}\quad D(G)+\frac2{363}\le0.
\tag{30}
\]

Thus (30) is necessary for an eventual gap bound \(G\), for almost
every torus and each fixed \(G\) in (15).

## 5. Threshold, rational bound and quantifiers

Differentiation of (19), using \(c'=3/(c+1)\), gives

\[
D'(G)=c-G<0.
\tag{31}
\]

At \(G=2\),

\[
18D(2)=14\sqrt7-37>0,
\]

since \(14^2\cdot7=1372>1369=37^2\). Substitution of (16) in
(19) gives the polynomial identity

\[
72D(G)=40-24c-c^2(c-2)^2=-R(c).
\tag{32}
\]

In particular, at \(B=67/32\), \(c=7/4\) and

\[
R(7/4)=\frac{561}{256}>\frac{48}{121}=72\eta,
\]

where the strict comparison is \(67881>12288\).
Therefore \(D+\eta\) has exactly one zero in \((2,B)\).
Equation (32) identifies it with \(\Gamma\) in (1).
Alternatively, uniqueness of \(c_0\) follows from
\(R'(c)=24+4c(c-1)(c-2)\ge16>0\) for \(1\le c\le2\).

For an exact lower bound, compute

\[
R(167/100)=\frac{38371121}{100000000}<\frac{48}{121}.
\tag{33}
\]

Indeed the numerator is
\(27889\cdot1089+8000000=38371121\), and cross multiplication
in (33) gives \(4642905641<4800000000\).
Since \(c\mapsto(c^2+2c+6)/6\) is increasing,

\[
\Gamma>\frac{(167/100)^2+2(167/100)+6}{6}
=\frac{121289}{60000}
=\frac{2021}{1000}+\frac{29}{60000}.
\tag{34}
\]

To pass from fixed \(G\) to a statement about almost every torus,
apply (30) for \(G=2\) and all rational \(G\in(2,\Gamma)\).
Remove their countable union of null exceptional sets, along with the
pair-correlation exceptional set. For each remaining torus these
values cannot be eventual gap bounds, because \(D(G)+\eta>0\).
If its gap limsup were below \(\Gamma\), either 2 or one of these
rational values would be an eventual bound, a contradiction. This
proves (2). Its strict rational lower bound implies infinitely many
gaps exceeding 2.021.

## 6. Separate arithmetic and normalization checks

There is a direct check of (12) at the chosen width that does not use
the expansion (10). With \(t(u)=13/11+2u\), \(b(u)=2/11+u\),
and \(0\le u\le2/11\), separate integration gives

\[
2\int_0^w t(u)\,du=\frac{60}{121},\qquad
\frac12\int_0^w(t(u)^2+b(u)^2)\,du=\frac{707}{3993}.
\]

The replacement benchmark is therefore
\(1980/3993-707/3993=1273/3993\). On the other hand,

\[
\int_1^{17/11}L_2(s)\,ds
=\left[\frac{s^2}{3}-\frac{s^3}{18}\right]_1^{17/11}
=\frac{417}{1331}=\frac{1251}{3993}.
\]

Their difference is \(22/3993=2/363\). This checks both the gain
and the ordered-count factors independently of (11).

The integral (18) also has a density check. The derivatives of
\(H_G\) on its three open pieces are \(1-s\), \((2-s)/3\),
and 1. Their total mass is
\(G-c/3-c^2/6=1\) by (16), and their first moment is

\[
\frac{G^2}{2}-\frac{c^2}{6}-\frac{c^3}{9}-\frac1{18}
=1-D(G).
\]

Integration by parts recovers \(I(G)=G-1+D(G)\).
For the polynomial identity (32), expanding

\[
72D=76-(c^2+2c+6)^2+12c^2+8c^3
\]

gives \(-R(c)\) directly. In particular the new threshold has
\(R(c_0)=72(2/363)=48/121\). It exceeds the previous scalar
range endpoint: \(R(5/3)=25/81<48/121\), since
\(3025<3888\), so \(\Gamma>109/54\). The preceding report's
threshold is below \(109/54\), hence this is a strict improvement.

For normalization, write
\(q_\alpha(m,n)=\alpha_1m^2+\alpha_2mn+\alpha_3n^2\) and
\(\Delta=4\alpha_1\alpha_3-\alpha_2^2>0\). The full ellipse
\(q_\alpha\le E\) has area \(2\pi E/\sqrt\Delta\).
Identifying global sign halves the leading count, so
\(x=\pi q_\alpha/\sqrt\Delta\) has unit density, agreeing with
the cited paper. Extra coincidences of two different global sign
pairs lie on a countable union of proper parameter hyperplanes;
discarding these null sets justifies strict ordering throughout.
Hyperbolic and Lebesgue null sets agree in the domain's interior.

The result is an almost-everywhere long-gap bound. It does not prove
the spacing distribution, all higher local statistics, or this bound
for an explicit individual Diophantine torus. The optimality in (14)
concerns only the specified family of moving lengths. The correlation
theorems are external inputs, whose full proofs are not supplied here.
