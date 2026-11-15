# An adjacent-interval obstruction to the scalar gap extremizer

Let

\[
L_m(s)=\frac{2ms-s^2}{m(m+1)},\qquad
L(s)=L_{\lfloor s\rfloor+1}(s),\quad L(0)=0.
\]

Define

\[
R(c)=c^4-4c^3+4c^2+24c-40.
\]

Let \(c_*\) be its root in \((\sqrt7-1,5/3)\), and put

\[
G_*=\frac{c_*^2+2c_*+6}{6}.
\tag{1}
\]

The scalar extremizer considered here is

\[
F_*(s)=
\begin{cases}
s-s^2/2,&0\le s\le1,\\
(4s-s^2)/6,&1\le s\le c_*,\\
1-G_*+s,&c_*\le s\le G_*,\\
1,&s\ge G_*.
\end{cases}
\tag{2}
\]

Consider a nondecreasing, 1-Lipschitz function \(F:[0,\infty)\to[0,1]\) with

\[
F(0)=0,\qquad F(s)=1\ (s\ge G),\qquad
\int_0^\infty(1-F(s))\,ds=1.
\tag{3}
\]

Retain the scalar lower bounds \(F(s)\ge L(s)\) for all \(s\ge0\).
These bounds follow if, separately for each \(s\), there is a nonnegative
integer-valued variable with mean \(s\), second factorial moment \(s^2\),
and positivity probability \(F(s)\).

**Theorem.** The function \(F_*\) cannot satisfy the adjacent-interval
requirements in the preceding report. More precisely, there are no
nonnegative integer-valued \(A,B\) such that

\[
\begin{gathered}
\mathbb EA=1,\qquad \mathbb EB=1/4,\\
\mathbb E[A(A-1)]=1,\qquad
\mathbb E[B(B-1)]=1/16,\qquad \mathbb E[AB]=1/4,\\
\mathbb P(A>0)=F_*(1),\qquad
\mathbb P(A+B>0)=F_*(5/4).
\end{gathered}
\tag{4}
\]

Moreover, if \(F\) satisfies (3), the scalar bounds, and (4) with \(F\)
in place of \(F_*\), then necessarily

\[
\boxed{G\ge G_*+\frac1{1944}.}
\tag{5}
\]

Only one adjacent pair is imposed in this theorem. The conclusion therefore
also applies to the relaxation requiring such a joint law for every pair
of adjacent intervals. The bound (5) is necessary; its optimality and the
existence of a feasible law with a finite support endpoint are not asserted.

## 1. A two-interval inequality

For nonnegative integers \(A,B\), write \(T=A+B\). The pointwise inequality

\[
\mathbf1_{A>0}+2\mathbf1_{T>0}
\ge 2T-\frac{T(T-1)}2-\frac{B(B-1)}2
\tag{6}
\]

holds without any probabilistic assumptions.

If \(A=0,B=0\), both sides vanish. If \(A=0,B\ge1\), the left side
is 2 and the right side is \(3B-B^2\). Their difference is
\((B-1)(B-2)\ge0\), since \(B\) is an integer.

If \(A\ge1\), then \(T\ge1\) and the left side is 3. Its difference
from the right side is

\[
\frac{(T-2)(T-3)+B(B-1)}2\ge0.
\]

Both products are nonnegative on the specified integer domains. This proves
(6), including unbounded counts.

Suppose, more generally, that \(a,b>0\), \(t=a+b\), and

\[
\mathbb EA=a,\quad \mathbb EB=b,\quad
\mathbb E[A(A-1)]=a^2,\quad
\mathbb E[B(B-1)]=b^2,\quad \mathbb E[AB]=ab.
\tag{7}
\]

Then

\[
\mathbb ET=t,\qquad
\mathbb E[T(T-1)]=a^2+2ab+b^2=t^2.
\]

If the positivity probabilities are \(F(a)\) and \(F(t)\), taking
expectations in (6) gives

\[
\boxed{F(a)+2F(t)\ge 2t-\frac{t^2}2-\frac{b^2}2.}
\tag{8}
\]

All expectations in this calculation are finite by (7).

## 2. Exact rejection of the extremizer

Since \(G_*>2\), relation (1) gives
\(c_*>\sqrt7-1>5/4\). The last inequality follows from
\(7>81/16\). Hence (2) gives

\[
F_*(1)=\frac12,\qquad
F_*(5/4)=\frac{4(5/4)-(5/4)^2}{6}=\frac{55}{96}.
\]

At \(a=1,b=1/4,t=5/4\), the two sides of (8) would be

\[
F_*(1)+2F_*(5/4)=\frac{79}{48},\qquad
2t-\frac{t^2}2-\frac{b^2}2=\frac{27}{16}=\frac{81}{48}.
\tag{9}
\]

Their difference is \(1/24>0\), proving incompatibility.

There is a second proof using the equality support of a scalar moment
bound. For every positive integer \(n\),

\[
1-\frac{4n-n(n-1)}6=\frac{(n-2)(n-3)}6\ge0.
\tag{10}
\]

At \(n=0\), the corresponding difference between the positivity indicator
and the quadratic polynomial is zero. Under (4), \(T=A+B\) has the
moments at \(t=5/4\), and its positivity probability is exactly
\((4t-t^2)/6\). The expectation of the nonnegative residual in (10)
is therefore zero. It follows that \(T\in\{0,2,3\}\) almost surely.

Because \(A\le T\),

\[
\mathbb P(A=0,T>0)=F_*(t)-F_*(a)=\frac7{96}.
\]

On this event \(B=T\ge2\). But then

\[
\frac7{96}\le\mathbb E\frac{B(B-1)}2
=\frac1{32}=\frac3{96},
\]

a contradiction with the same margin \(1/24\).

## 3. The scalar envelope and its endpoint

The scalar lower bound can be checked directly. For \(m\ge1\),

\[
q_m(n)=\frac{2mn-n(n-1)}{m(m+1)}
\le\mathbf1_{n>0}\qquad(n\in\mathbb Z_{\ge0}),
\]

because at positive integers the residual is
\((n-m)(n-m-1)/(m(m+1))\), and at zero it vanishes.
For \(m-1\le s\le m\), the law on \(\{0,m,m+1\}\) with

\[
p_m=\frac{s(m-s)}m,\qquad
p_{m+1}=\frac{s(s-m+1)}{m+1},\qquad
p_0=1-L_m(s)
\]

attains the bound. Indeed, the probabilities are nonnegative,
\(p_0=((m-s)^2+m)/(m(m+1))\), and direct substitution gives
mean \(s\) and second factorial moment \(s^2\). Thus \(L(s)\) is
the exact scalar minimum, with no compatibility across \(s\) imposed.

Put \(B_0=109/54\). For \(2\le G\le B_0\), set

\[
c=c(G)=\sqrt{6G-5}-1,
\qquad G=\frac{c^2+2c+6}{6}.
\tag{11}
\]

The endpoint and Lipschitz condition imply \(F(s)\ge1-G+s\) on
\([0,G]\). Consequently \(F\ge H_G\), where

\[
H_G(s)=
\begin{cases}
s-s^2/2,&0\le s\le1,\\
(4s-s^2)/6,&1\le s\le c,\\
1-G+s,&c\le s\le G.
\end{cases}
\tag{12}
\]

Here is a direct check of the envelope. On \([0,1]\), the endpoint line
is nonpositive and \(L(s)=s-s^2/2\). On \([1,2]\), the difference
between \(L(s)=(4s-s^2)/6\) and that line is
\((6G-6-2s-s^2)/6\), decreasing to zero exactly at \(c\).
On \([2,G]\), \(L(s)=(6s-s^2)/12\le3/4\), whereas the line is
at least \(3-G\ge53/54\). Thus (12) is precisely
\(\max(L(s),1-G+s)\) on this interval. Its derivatives are
\(1-s,(2-s)/3,1\); its pieces meet continuously. It is nondecreasing
and 1-Lipschitz.

Integration gives

\[
\begin{aligned}
I(G):=\int_0^G H_G(s)\,ds
&=\frac13+
\left[\frac{s^2}3-\frac{s^3}{18}\right]_1^c+
\left[(1-G)s+\frac{s^2}2\right]_c^G\\
&=G-\frac{G^2}2+\frac1{18}+\frac{c^2}6+\frac{c^3}9.
\end{aligned}
\tag{13}
\]

Define \(D(G)=I(G)-G+1\). Differentiating (13), with
\(c'=3/(c+1)\), gives

\[
D'(G)=c-G<0,\qquad
G-c=\frac{(c-2)^2+2}{6}.
\tag{14}
\]

The endpoint signs are

\[
18D(2)=14\sqrt7-37>0,\qquad
D(B_0)=-\frac{25}{5832}<0.
\]

The first sign follows on squaring from \(1372>1369\). Substitution
of (11) in (13) gives

\[
72D(G)=40-24c-c^2(c-2)^2=-R(c).
\tag{15}
\]

Thus \(D\) has exactly one zero in \((2,B_0)\), which is the value
\(G_*\) in (1). This also verifies existence and uniqueness of the
root used there. Equivalently, substitution of \(c=\sqrt{6G-5}-1\)
gives

\[
18D(G)=35-18G-9G^2+(12G-10)\sqrt{6G-5}.
\]

By (3), \(\int_0^G F=G-1\). Since \(F\ge H_G\), necessarily
\(D(G)\le0\), so \(G\ge G_*\) when \(2\le G\le B_0\).
If \(G<2\), the same function would satisfy the support condition with
endpoint 2, contradicting \(D(2)>0\). This proves the scalar necessary
bound for every endpoint below \(B_0\).

## 4. A positive separation from the scalar endpoint

Assume first \(G_*\le G\le B_0\). On \([0,G]\), let
\(\delta=F-H_G\ge0\). For \(x<y\), both increments
\(F(y)-F(x)\) and \(H_G(y)-H_G(x)\) lie in \([0,y-x]\).
Their difference therefore lies in \([-(y-x),y-x]\). In particular,
\(\delta\) is 1-Lipschitz.

For all these \(G\), \(c(G)>5/4\), so

\[
H_G(1)=\frac12,\qquad H_G(5/4)=\frac{55}{96}.
\]

Subtracting (9) from (8) gives

\[
\delta(1)+2\delta(5/4)\ge\frac1{24}.
\tag{16}
\]

At least one of the two values is at least \(h=1/72\). At that point
\(x_0\in\{1,5/4\}\), the Lipschitz property implies

\[
\delta(s)\ge\max\{h-|s-x_0|,0\}.
\]

The whole triangle is inside \([0,G]\), since \(G\ge2\) and
\(x_0\in\{1,5/4\}\). Its integral is
\(2\int_0^h(h-u)\,du=h^2\). Therefore

\[
-D(G)=\int_0^G\delta(s)\,ds\ge\frac1{5184}.
\tag{17}
\]

On \([2,B_0]\) one has \(3/2<c(G)\le5/3<2\): the lower bound
follows from \(\sqrt7>5/2\), and the upper bound follows by substituting
\(B_0\) in (11). Hence (14) gives

\[
G-c(G)\le\frac{(1/2)^2+2}{6}=\frac38.
\]

Using \(D(G_*)=0\) and integrating (14),

\[
-D(G)=\int_{G_*}^{G}(u-c(u))\,du
\le\frac38(G-G_*).
\tag{18}
\]

Combining (17) and (18) proves
\(G-G_*\ge8/(3\cdot5184)=1/1944\).

For completeness, endpoints \(G>B_0\) satisfy the same bound. The
derivative

\[
R'(c)=24+4c(c-1)(c-2)\ge16\qquad(1\le c\le2)
\]

is positive, since \(|c(c-1)(c-2)|\le2\) there. Direct exact evaluation
gives

\[
R(83/50)=\frac{990921}{6250000}>0.
\]

Thus \(c_*<83/50\), and by (1),

\[
G_*<\frac{10063}{5000},\qquad
B_0-\frac{10063}{5000}=\frac{799}{135000}>\frac1{1944}.
\]

The last comparison is equivalent to
\(799\cdot1944=1553256>135000\). Therefore \(G>B_0\) also implies
(5), completing the proof.

## 5. Finite counts and moment errors

The certificate does not require exact limiting moments to be useful.
Suppose the five moments in (7), in their displayed order, have errors
\(e_A,e_B,e_{AA},e_{BB},e_{AB}\). Taking expectations in (6) gives

\[
F(a)+2F(t)\ge
2t-\frac{t^2}2-\frac{b^2}2
+2e_A+2e_B-\frac{e_{AA}}2-e_{BB}-e_{AB}.
\tag{19}
\]

If every error has absolute value at most \(\varepsilon\), the right
side loses at most \(13\varepsilon/2\). Thus the two exact positivity
probabilities in (9) are still impossible whenever
\(\varepsilon<1/156\). If those probabilities also have absolute errors
at most \(\varepsilon\), the left side can increase by at most
\(3\varepsilon\), so impossibility still holds for
\(\varepsilon<1/228\). Both thresholds come from the exact margin
\(1/24\); they are sufficient bounds, without an optimality assertion.

For a finite increasing sequence \(x_1<\cdots<x_N\), let \(T_{r,N}\)
count ordered distinct indices, normalized by \(N\), with the last
\(r-1\) differences from the first index in the specified intervals.
Put

\[
F_N(s)=\frac1N\#\{i<N:x_{i+1}-x_i\le s\}.
\]

Apply (6) at each anchor \(i\), with \(A_i\) counting later points in
\((x_i,x_i+a]\) and \(B_i\) those in \((x_i+a,x_i+t]\), truncating
both at index \(N\). Summation gives the exact inequality

\[
\begin{aligned}
F_N(a)+2F_N(t)\ge{}&2T_{2,N}((0,t])\\
&-\frac12T_{3,N}((0,t],(0,t])\\
&-\frac12T_{3,N}((a,t],(a,t]).
\end{aligned}
\tag{20}
\]

The factors \(1/2\) occur because each factorial moment counts ordered
pairs. There is no boundary error: all counts and gap indicators use the
same truncated sequence. This establishes the certificate before any
passage to a limiting count law.

The theorem concerns a joint moment relaxation. It does not establish
pointwise triple correlation or an improved gap bound for flat tori.
The averaged triple-correlation theorem of Christoph Aistleitner,
Valentin Blomer and Maksym Radziwiłł, *Triple correlation and long gaps
in the spectrum of flat tori*, [arXiv:1809.07881](https://arxiv.org/abs/1809.07881),
has different quantifiers. The relation between that averaging statement
and inequalities such as (20) requires a separate argument.
