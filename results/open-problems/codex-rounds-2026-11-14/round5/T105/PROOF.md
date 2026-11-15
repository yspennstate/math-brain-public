# A stronger long-gap consequence of averaged triple correlation

Let

\[
c(G)=\sqrt{6G-5}-1,\qquad B_0=\frac{109}{54},
\]

and, for \(2\le G\le B_0\), put

\[
D(G)=1-\frac{G^2}{2}+\frac1{18}
       +\frac{c(G)^2}{6}+\frac{c(G)^3}{9}.
\tag{1}
\]

Set

\[
w=\frac1{32},\qquad \eta=\frac{131}{196608}.
\tag{2}
\]

There is a unique \(G_\dagger\in(2,B_0)\) with

\[
D(G_\dagger)+\eta=0.
\tag{3}
\]

**Theorem.** For almost every flat two-dimensional torus, let
\(x_1<x_2<\cdots\) be its positive eigenvalues after identifying the
vectors \(v\) and \(-v\), unfolded to mean spacing one. Then

\[
\limsup_{i\to\infty}(x_{i+1}-x_i)\ge G_\dagger.
\tag{4}
\]

In particular there are infinitely many gaps larger than
\(251/125=2.008\). If \(G_*\) denotes the zero of \(D\), the constant
in the preceding scalar calculation, then

\[
G_\dagger\ge G_*+\frac{131}{73728}.
\tag{5}
\]

The correlation input is Theorem 1 and the almost-everywhere pair
correlation statement recorded in Section 1.2 of Christoph Aistleitner,
Valentin Blomer and Maksym Radziwiłł, *Triple correlation and long gaps in
the spectrum of flat tori*,
[published text, DOI 10.4171/JEMS/1356](https://ems.press/content/serial-article-files/31432),
[arXiv:1809.07881](https://arxiv.org/abs/1809.07881).
Their Theorem 1 gives convergence of averaged triple counts over every
finite parameter rectangle, uniformly over intervals in a fixed bounded
interval. The proof below uses that averaged statement and does not
assume pointwise triple convergence.

## 1. Counts and finite inequalities

For \(x_1<\cdots<x_N\) and an interval \(I\subset(0,\infty)\), define

\[
\begin{split}
P_N(I)&=\frac1N\#\{(i,j):1\le i,j\le N,
               \ x_j-x_i\in I\},\\
U_N(I)&=\frac1N\#\{(i,j,k):1\le i,j,k\le N,
             \ i,j,k\text{ pairwise distinct},
             \ x_j-x_i,x_k-x_i\in I\}.
\end{split}
\tag{6}
\]

The last two indices in \(U_N\) are ordered. Abbreviate
\(P_N(s)=P_N((0,s])\), and put

\[
F_N(s)=\frac1N\#\{i<N:x_{i+1}-x_i\le s\}.
\tag{7}
\]

At anchor \(i\), let \(C_i(s)\) count the later points at distance at
most \(s\), truncated at \(N\). For every nonnegative integer \(n\),

\[
\mathbf1_{n>0}\ge n-\frac{n(n-1)}2,
\qquad
\mathbf1_{n>0}\ge\frac23 n-\frac16 n(n-1).
\tag{8}
\]

At positive integers the respective residuals are
\((n-1)(n-2)/2\) and \((n-2)(n-3)/6\); at zero they vanish.
Since \(C_i(s)>0\) precisely when the next gap exists and is at most
\(s\), summation gives the exact inequalities

\[
\begin{split}
F_N(s)&\ge P_N(s)-\frac12U_N((0,s]),\\
F_N(s)&\ge\frac23P_N(s)-\frac16U_N((0,s]).
\end{split}
\tag{9}
\]

For nonnegative integers \(A,B\) and \(T=A+B\), one also has

\[
\mathbf1_{A>0}+2\mathbf1_{T>0}
\ge 2T-\frac12T(T-1)-\frac12B(B-1).
\tag{10}
\]

At \(A=B=0\) the residual is zero. At \(A=0,B\ge1\) it is
\((B-1)(B-2)\). At \(A\ge1\) it is
\(((T-2)(T-3)+B(B-1))/2\). These are nonnegative for all the indicated
integers.

Fix

\[
a=1,\qquad t=\frac54,\qquad b=t-a=\frac14.
\tag{11}
\]

Use at each anchor the two counts in \((0,a]\) and \((a,t]\).
Summing (10) gives

\[
F_N(a)+2F_N(t)
\ge 2P_N(t)-\frac12U_N((0,t])-\frac12U_N((a,t]).
\tag{12}
\]

There is no end-of-sequence correction in (9) or (12), since every
count uses the same truncation at \(N\).

## 2. One subsequence for a nonnegative sum

Let \(\mu\) be the hyperbolic measure on the torus parameter domain
used in the cited paper. On its interior it has a positive continuous
density with respect to Lebesgue measure. Suppose measurable functions
\(Q_N\ge0\) satisfy, for every finite rectangle \(R\) of finite
\(\mu\)-measure,

\[
\int_R Q_N\,d\mu\longrightarrow q\mu(R),\qquad q\ge0.
\tag{13}
\]

Then

\[
\liminf_{N\to\infty}Q_N(\alpha)\le q
\quad\text{for almost every }\alpha.
\tag{14}
\]

To prove this, suppose \(\liminf Q_N>q\) on a set of positive measure.
For some \(\varepsilon>0\), the set

\[
E=\{\alpha:\liminf_NQ_N(\alpha)\ge q+\varepsilon\}
\]

has positive measure. By the density theorem there is a finite
rectangle \(R\), contained in the interior, with

\[
\frac{\mu(E\cap R)}{\mu(R)}>\frac{q}{q+\varepsilon}.
\]

Fatou's lemma and nonnegativity give

\[
q\mu(R)=\liminf_N\int_R Q_N\,d\mu
\ge\int_R\liminf_NQ_N\,d\mu
\ge(q+\varepsilon)\mu(E\cap R)>q\mu(R),
\]

a contradiction. This proves (14).

In particular the lemma applies to any fixed finite nonnegative sum
of triple counts and integrals of triple counts with finite
nonnegative measures and bounded interval parameters. Indeed, the
uniformity in Theorem 1 permits integration of the averaged error;
Tonelli's theorem applies since the counts are nonnegative. The
benchmark \(q\) is obtained by replacing each \(U_N(I)\) by
\(|I|^2\). The lemma is applied to the entire sum. No simultaneous
subsequence bounds for its separate terms are required.

## 3. Eventual gap bounds and the scalar integral

Assume temporarily that for some fixed \(G\in[2,B_0]\) all but
finitely many gaps are at most \(G\). Let \(M\) bound the number of
exceptional gaps. For \(0\le s\le G\), every nonexceptional gap
larger than \(s\) contributes a pair in \((s,G]\), so

\[
F_N(s)\ge1-P_N((s,G])-\frac{M+1}{N}.
\tag{15}
\]

Also, writing \(g_i=x_{i+1}-x_i\), one has exactly

\[
\int_0^G F_N(s)\,ds
=\frac1N\sum_{i<N}(G-g_i)_+
=\frac{G(N-1)}N-\frac{x_N-x_1}{N}
  +\frac1N\sum_{i<N}(g_i-G)_+.
\tag{16}
\]

The last sum is eventually a fixed finite constant. Thus the Weyl
asymptotic \(x_N/N\to1\) implies

\[
\int_0^G F_N(s)\,ds\longrightarrow G-1.
\tag{17}
\]

For comparison define, with \(c=c(G)\),

\[
H_G(s)=
\begin{cases}
s-s^2/2,&0\le s\le1,\\
(4s-s^2)/6,&1\le s\le c,\\
1-G+s,&c\le s\le G.
\end{cases}
\tag{18}
\]

Its pieces agree because

\[
G=\frac{c^2+2c+6}{6}.
\tag{19}
\]

Direct integration gives

\[
\begin{split}
I(G):=\int_0^G H_G(s)\,ds
&=\frac13+
 \left[\frac{s^2}{3}-\frac{s^3}{18}\right]_1^c
 +\left[(1-G)s+\frac{s^2}{2}\right]_c^G\\
&=G-\frac{G^2}{2}+\frac1{18}+\frac{c^2}{6}+\frac{c^3}{9}.
\end{split}
\tag{20}
\]

Consequently \(D(G)=I(G)-G+1\), agreeing with (1).
The argument below uses the finite inequalities (9), (12), (15).
It does not assert the pointwise inequality \(F_N\ge H_G+o(1)\).

## 4. Replacing two windows

Let

\[
W_1=[1,1+w],\qquad W_2=[t,t+2w],\qquad W=W_1\cup W_2,
\qquad V_G=[1,c(G)]\setminus W.
\tag{21}
\]

These windows are disjoint and lie in \([1,c(G)]\) for every
\(G\in[2,B_0]\). Indeed \(1+w=33/32<5/4\), and
\(t+2w=21/16<\sqrt7-1\le c(G)\); the second strict inequality
follows from \(37^2<7\cdot16^2\).

Monotonicity of \(F_N\) gives

\[
\int_W F_N(s)\,ds\ge wF_N(1)+2wF_N(t).
\tag{22}
\]

Apply the first inequality in (9) on \([0,1]\), the second on
\(V_G\), (15) on \([c,G]\), and \(w\) times (12) on the two
windows. Define

\[
\begin{split}
\mathcal P_N(G)={}&\int_0^1 P_N(s)\,ds
 +\frac23\int_{V_G}P_N(s)\,ds\\
&+\int_c^G\bigl(1-P_N((s,G])\bigr)\,ds+2wP_N(t),\\
Q_N(G)={}&\frac12\int_0^1U_N((0,s])\,ds
 +\frac16\int_{V_G}U_N((0,s])\,ds\\
&+\frac w2\bigl(U_N((0,t])+U_N((1,t])\bigr).
\end{split}
\tag{23}
\]

The resulting finite inequality is

\[
\int_0^G F_N(s)\,ds
\ge \mathcal P_N(G)-Q_N(G)-\frac{(M+1)(G-c)}N.
\tag{24}
\]

All coefficients in \(Q_N\) are nonnegative.

For almost every torus, Poisson pair correlation gives \(P_N(s)\to s\),
uniformly for \(s\in[0,B_0]\). To see the uniformity, take a finite
rational mesh and squeeze the nondecreasing functions \(P_N\) between
their mesh values; the limiting function \(s\) is continuous. Since
\(P_N((s,G])=P_N(G)-P_N(s)\), it follows that

\[
\mathcal P_N(G)\longrightarrow p_G
:=\int_0^1s\,ds+\frac23\int_{V_G}s\,ds
  +\int_c^G(1-G+s)\,ds+2wt.
\tag{25}
\]

The averaged triple theorem and Section 2 give

\[
\liminf_N Q_N(G)\le q_G
:=\frac12\int_0^1s^2\,ds+\frac16\int_{V_G}s^2\,ds
  +\frac w2(t^2+b^2)
\tag{26}
\]

for almost every torus. Thus (24) holds along a subsequence on which
its right side is at least \(p_G-q_G-o(1)\).

The scalar contribution omitted from the windows is particularly
simple. Put \(L_2(s)=(4s-s^2)/6\). Then

\[
L_2(1)=\frac12,\quad L_2(t)=\frac{55}{96},\quad
2t-\frac{t^2+b^2}{2}=\frac{27}{16}.
\tag{27}
\]

For any \(u\) and \(\ell\ge0\), exact integration of the quadratic
gives

\[
\int_u^{u+\ell}L_2(s)\,ds
=\ell L_2(u)+\frac{2-u}{6}\ell^2-\frac{\ell^3}{18}.
\tag{28}
\]

Use \((u,\ell)=(1,w)\) and \((t,2w)\). It follows that

\[
\int_W H_G(s)\,ds
=w\left(\frac12+2\frac{55}{96}\right)
  +\frac23w^2-\frac12w^3
=\frac{79}{48}w+\frac23w^2-\frac12w^3.
\tag{29}
\]

Combining (20), (25)--(29),

\[
\begin{split}
p_G-q_G
&=I(G)-\int_WH_G(s)\,ds+w\frac{27}{16}\\
&=I(G)+\frac{w}{24}-\frac23w^2+\frac12w^3
=I(G)+\eta.
\end{split}
\tag{30}
\]

Here

\[
\frac{w}{24}-\frac23w^2+\frac12w^3
=\frac1{768}-\frac1{1536}+\frac1{65536}
=\frac{131}{196608}.
\tag{31}
\]

Equations (17), (24), and (30) prove the necessary condition

\[
D(G)+\eta\le0
\tag{32}
\]

for an eventual gap bound \(G\), for almost every torus and each
fixed \(G\in[2,B_0]\).

## 5. The threshold and its quantifiers

Differentiating (20) and using \(c'=3/(c+1)\), or differentiating
the integrals at their matching endpoint, gives

\[
D'(G)=c(G)-G<0,\qquad
G-c(G)=\frac{(c(G)-2)^2+2}{6}.
\tag{33}
\]

At the endpoints,

\[
18D(2)=14\sqrt7-37>0,\qquad D(B_0)=-\frac{25}{5832}.
\tag{34}
\]

The first sign follows from \(14^2\cdot7=1372>1369=37^2\).
Also \(\eta<25/5832\), since
\(131\cdot5832=763992<4915200=25\cdot196608\).
Thus \(D+\eta\) is strictly decreasing and has exactly one zero
\(G_\dagger\in(2,B_0)\). Since \(D(G_*)=0\) and \(\eta>0\),
this zero is larger than \(G_*\).

Apply the preceding argument for \(G=2\) and for every rational
\(G\in(2,G_\dagger)\), and discard the countable union of their
null exceptional sets. For every remaining torus no such \(G\)
can be an eventual bound, by (32). If its gap limsup were less than
\(G_\dagger\), either 2 or one of those rational numbers would be
an eventual bound. This proves (4). The assertion is a limsup bound;
at the exact endpoint it means infinitely many gaps larger than
\(G_\dagger-\varepsilon\) for every \(\varepsilon>0\).

On \([2,B_0]\), one has \(3/2<c(G)\le5/3\), and (33) implies
\(G-c(G)\le3/8\). Consequently

\[
\eta=-D(G_\dagger)
=\int_{G_*}^{G_\dagger}(u-c(u))\,du
\le\frac38(G_\dagger-G_*).
\]

This proves (5), since \((8/3)\eta=131/73728\).

## 6. An independent exact check of the constant

Substitute (19) in (1). With

\[
R(c)=c^4-4c^3+4c^2+24c-40=c^2(c-2)^2+24c-40,
\]

one obtains

\[
72D(G)=-R(c(G)).
\tag{35}
\]

Thus the new constant can equivalently be specified by

\[
R(c_\dagger)=\frac{393}{8192},\qquad
G_\dagger=\frac{c_\dagger^2+2c_\dagger+6}{6}.
\tag{36}
\]

Indeed \(72\eta=393/8192\). Equivalently its square-root equation is

\[
35-18G-9G^2+(12G-10)\sqrt{6G-5}
+\frac{393}{32768}=0.
\tag{37}
\]

The identity \(R'(c)=24+4c(c-1)(c-2)\ge16\) on \([1,2]\)
provides an independent uniqueness check. Exact rational evaluations
give

\[
R(331/200)=\frac{73619921}{1600000000}
 <\frac{393}{8192}
 <\frac{77745}{1048576}=R(53/32).
\tag{38}
\]

For the first strict comparison the cross products are
\(603094392832<628800000000\). For the second, the middle value is
\(50304/1048576<77745/1048576\). Both comparison points belong to
\((\sqrt7-1,5/3)\). Since (19) is increasing in \(c\), (38) gives

\[
\frac{481961}{240000}<G_\dagger<\frac{12345}{6144}.
\tag{39}
\]

The lower endpoint exceeds \(251/125\) by \(41/240000\). This
proves the stated strict improvement past 2.008 without relying on
a numerical root finder.

The window gain has a separate integration check. With
\(J(s)=s^2/3-s^3/18\), compute

\[
[J(1+w)-J(1)]+[J(t+2w)-J(t)]
=\frac{79}{48}w+\frac23w^2-\frac12w^3.
\]

This agrees with the Taylor integration (28). The baseline integral
can likewise be checked without integrating the CDF: the density of
\(H_G\) is \(1-s\), \((2-s)/3\), and 1 on its three pieces.
Its mass is \(G-c/3-c^2/6=1\), and its first moment is

\[
\frac{G^2}{2}-\frac{c^2}{6}-\frac{c^3}{9}-\frac1{18}=1-D(G).
\]

Both identities use (19) and recover (20) by integration by parts.

At the chosen rational width the two window integrals separately are
\(9311/589824\) and \(21400/589824\). Their sum is
\(10237/196608\). The replacement has value
\(w(27/16)=27/512=10368/196608\), again giving the difference
\(131/196608\). Separating its two moment terms gives the same
replacement: the pair part is \(2wt=5/64\), and the triple part is
\(w(t^2+b^2)/2=13/512\), whose difference is \(27/512\).

## 7. Scope

For completeness, if
\(q_\alpha(m,n)=\alpha_1m^2+\alpha_2mn+\alpha_3n^2\) and
\(\Delta=4\alpha_1\alpha_3-\alpha_2^2>0\), the unfolded levels
are \(\pi q_\alpha(m,n)/\sqrt\Delta\), with one representative
of each global sign pair. The full ellipse \(q_\alpha\le E\) has
area \(2\pi E/\sqrt\Delta\); halving it verifies unit density
after this rescaling. Outside a countable union of parameter
hyperplanes distinct sign pairs have distinct levels. Thus the
strict ordering used in (6) holds almost everywhere. Hyperbolic and
Lebesgue null sets agree on the interior of the parameter domain.

The result uses only the cited averaged triple theorem, the known
almost-everywhere pair correlation, Weyl asymptotics, and the finite
inequalities proved above. It does not give convergence of triple
correlation for an individual torus, an explicit Diophantine class
for (4), or the nearest-neighbour spacing distribution. The width
\(w=1/32\) is a convenient rational choice; optimality of the new
constant is not asserted.
