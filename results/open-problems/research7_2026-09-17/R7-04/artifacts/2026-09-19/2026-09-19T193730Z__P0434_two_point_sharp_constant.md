# P0434: exact sharp M-SERPT/Gittins ratio for every two-point service law

Date: 2026-09-19  
Worker: R7-04  
Target: P0434, Scully--Harchol-Balter--Scheller-Wolf (2020), Section 8, Conjecture 8.1.

## 1. Statement proved here

Consider the stable preemptive M/G/1 queue with unknown individual job sizes and FCFS tie-breaking among equal SOAP ranks. Let

\[
\Pr\{X=a\}=p,\qquad \Pr\{X=b\}=q:=1-p,
\qquad 0<a<b,\quad 0<p<1,
\]

and let \(\rho=\lambda \mathbb E X<1\). Write \(T_{\rm MS}\) and \(T_G\) for mean response time under M-SERPT and Gittins.

The preceding R7-04 report proved that, with \(d=b-a\),

* if \(pd\le a\), M-SERPT and Gittins are sample-path identical to FCFS, so
  \(\mathbb ET_{\rm MS}/\mathbb ET_G=1\);
* if \(pd>a\), putting \(h=a/p\) and \(c=b-h\), M-SERPT has phase priorities
  \(H_0=[0,a)\), \(L=[a,b)\), while Gittins has
  \(H_0=[0,a)\), \(L=[a,c)\), \(H_1=[c,b)\).

This note solves the entire remaining two-point optimization exactly.

### Theorem

Let

\[
Q(p)=2p^5-8p^4+10p^3-6p^2+1.
\]

There is a unique \(p_\star\in(1/2,1)\) satisfying \(Q(p_\star)=0\). Put

\[
\rho_\star=2(1-p_\star)
\]

and

\[
C_2
=
1+
\frac{(1-p_\star)^2(2p_\star-1)}
     {(p_\star^2-2p_\star+2)(2p_\star^2-2p_\star+1)}.
\]

Then

\[
\boxed{
\sup_{\substack{\text{two-point }X\\ \rho<1}}
\frac{\mathbb E T_{\rm MS}}{\mathbb E T_G}
=
C_2
=
1.0601734219127679606\ldots
}
\]

with

\[
p_\star=0.6571391408919625222\ldots,\qquad
\rho_\star=0.6857217182160749556\ldots.
\]

The supremum is approached from the supercritical side
\(p(b-a)/a\downarrow1\); it is not attained at the boundary itself because
at equality the two policies collapse to FCFS.

In particular, every two-point law has ratio strictly below \(2\).
The source paper gives a three-point family whose ratio tends to \(2\).
Therefore **support size three is minimal among finite-support sequences
capable of approaching the source lower constant \(2\)**.

This is a restricted-class theorem and does not close Conjecture 8.1.

## 2. Published tool used

The calculation uses Theorem 5.5 of Scully--Harchol-Balter--Scheller-Wolf,
*SOAP: One Clean Analysis of All Age-Based Scheduling Policies*,
POMACS 2(1), 2018. For a tagged job of size \(x\),

\[
\mathbb E[T_x]
=
\frac{\lambda\sum_{i\ge0}\mathbb E[(X_i^{\rm old}[r])^2]}
{2(1-\rho_0^{\rm old}[r])(1-\rho^{\rm new}[r])}
+
\int_0^x\frac{da}{1-\rho^{\rm new}[r^{\rm worst}_x(a)]}.
\]

The same paper works out the nonmonotone Gittins rank for the illustrative
two-point law \(\Pr(X=2)=\Pr(X=14)=1/2\); its formulas provide an
independent published spot-check of the generalized work decomposition below.

## 3. B6: derive the exact stationary response formulas

Assume \(pd>a\). Let

\[
m=\mathbb EX=a+qd,\qquad h=\frac ap,\qquad c=b-h.
\]

The exact ranks from the preceding run are

\[
r_{\rm MS}(t)=
\begin{cases}
m,&0\le t<a,\\
d,&a\le t<b,
\end{cases}
\]

and

\[
r_G(t)=
\begin{cases}
(a-t)/p,&0\le t<a,\\
b-t,&a\le t<b.
\end{cases}
\]

Because \(pd>a\), one has \(d>m>h\) and \(a<c<b\).

### 3.1 M-SERPT, short tagged job

Its worst future rank is \(m\). A new arrival starts at the same rank
\(m\), so FCFS tie-breaking gives the tagged job priority and new
\(m\)-work is zero. An old job contributes exactly its first \(a\) units
before either completing or, if long, jumping to rank \(d>m\). Hence

\[
X_0^{\rm old}[m]=a,\qquad
X_i^{\rm old}[m]=0\ (i\ge1),\qquad
\rho^{\rm new}[m]=0,\qquad
\rho_0^{\rm old}[m]=\lambda a.
\]

SOAP therefore gives

\[
\boxed{
\mathbb E[T_{\rm MS}\mid X=a]
=
a+\frac{\lambda a^2}{2(1-\lambda a)}.
}
\tag{3.1}
\]

### 3.2 M-SERPT, long tagged job

The long tagged job has worst future rank \(d\) already at age \(0\).
Every new job can receive exactly its first \(a\) units before it either
completes or reaches rank \(d\), so

\[
X^{\rm new}[d]=a.
\]

An old job is never worse than \(d\): a short job completes by age \(a\),
and a long job jumps to exactly \(d\) and then stays there. Thus

\[
X_0^{\rm old}[d]=X,\qquad X_i^{\rm old}[d]=0\ (i\ge1).
\]

Therefore

\[
\rho^{\rm new}[d]=\lambda a,\qquad
\rho_0^{\rm old}[d]=\rho.
\]

The residence integrand is constant because the tagged job's worst future
rank remains \(d\) for its entire life. Hence

\[
\boxed{
\mathbb E[T_{\rm MS}\mid X=b]
=
\frac{\lambda\mathbb E[X^2]}
{2(1-\rho)(1-\lambda a)}
+
\frac{b}{1-\lambda a}.
}
\tag{3.2}
\]

### 3.3 Gittins, short tagged job

Its worst future rank at arrival is \(h=a/p\). A new job ties it at age
zero and therefore contributes no work before the older tagged job under
FCFS tie-breaking.

An old job is original with respect to rank \(h\) through its first
\(a\) units. If it is short it completes. If it is long it jumps at age
\(a\) to rank \(d>h\), is discarded, and then returns to rank \(h\) at
age \(c=b-h\). It then contributes the terminal interval of length \(h\)
as one recycled piece. Consequently

\[
X_0^{\rm old}[h]=a,
\]

and

\[
X_1^{\rm old}[h]
=
\begin{cases}
0,&X=a,\\
h,&X=b,
\end{cases}
\]

with all higher recycled work zero. Hence

\[
\boxed{
\mathbb E[T_G\mid X=a]
=
a+
\frac{\lambda(a^2+qh^2)}
{2(1-\lambda a)}.
}
\tag{3.3}
\]

For the published SOAP example \(a=2,p=q=1/2,b=14\), this becomes
\(2+6\lambda/(1-2\lambda)\), exactly the paper's displayed Gittins
short-job formula.

### 3.4 Gittins, long tagged job

At arrival its worst future rank is \(d\), so its waiting term is exactly
the same as in (3.2):

\[
\frac{\lambda\mathbb E[X^2]}
{2(1-\rho)(1-\lambda a)}.
\]

For ages \(0\le t<c\), its worst future rank exceeds \(h\), so each new
arrival can contribute its first \(a\) units and the residence slowdown
is \(1/(1-\lambda a)\). For the final interval \([c,b)\), of length
\(h\), the tagged rank is at most the fresh rank \(h\), so new arrivals
contribute no delaying work. Therefore

\[
\boxed{
\mathbb E[T_G\mid X=b]
=
\frac{\lambda\mathbb E[X^2]}
{2(1-\rho)(1-\lambda a)}
+
\frac{c}{1-\lambda a}+h.
}
\tag{3.4}
\]

For \(a=2,p=q=1/2,b=14\), this is

\[
\frac{50\lambda}{(1-8\lambda)(1-2\lambda)}
+\frac{10}{1-2\lambda}+4,
\]

again exactly the published SOAP formula.

## 4. B11: exact tagged-job charging identity

Average (3.1)--(3.4) over the service law. The short-job difference is

\[
\mathbb E[T_{\rm MS}-T_G\mid X=a]
=
-\frac{\lambda qh^2}{2(1-\lambda a)}.
\]

The long-job difference is

\[
\mathbb E[T_{\rm MS}-T_G\mid X=b]
=
\frac{b-c}{1-\lambda a}-h
=
\frac{\lambda ah}{1-\lambda a}.
\]

Weighting by \(p,q\) and using \(h=a/p\) gives the exact cancellation

\[
\boxed{
\mathbb E T_{\rm MS}-\mathbb E T_G
=
\frac{q\lambda a^2}{2p(1-\lambda a)}.
}
\tag{4.1}
\]

Thus the whole two-point penalty of M-SERPT is a single positive
occupation charge. The gain Gittins gives long jobs by rescuing their
last \(h\) units outweighs its extra short-job delay by exactly (4.1).

This also independently proves strict optimality of Gittins over
M-SERPT throughout \(pd>a\).

## 5. B29: compactify and solve the whole parameter optimization

Scale time by \(a\), so set \(a=1\). Introduce

\[
\theta=\frac{p(b-a)}a>1,\qquad
s=p+q\theta,\qquad
m=\frac{s}{p},\qquad
\lambda=\frac{\rho p}{s}.
\]

Let

\[
R(p,\theta,\rho)
=
\frac{\mathbb E T_{\rm MS}}{\mathbb E T_G}.
\]

By (4.1),

\[
R=1+\frac{D}{\mathbb E T_G},
\qquad
D=\frac{q\rho}{2(s-p\rho)}.
\tag{5.1}
\]

Put

\[
\mathcal N
=
2p(1-\rho)(s-p\rho)\,\mathbb E T_G.
\]

Every factor is positive on
\(0<p<1,\ \theta>1,\ 0<\rho<1\), so \(\mathcal N>0\).
Substitution of (3.3)--(3.4) followed by ordinary differentiation gives

\[
\frac{\partial R}{\partial\theta}
=
\frac{-2p\rho(p-1)^2(\rho-1)}{\mathcal N^2}\,H,
\tag{5.2}
\]

where

\[
H
=
p[\rho(p+1)-2]
-(1-p)(2-\rho)\theta.
\]

The coefficient before \(H\) in (5.2) is positive. Because the
coefficient of \(\theta\) in \(H\) is negative,

\[
H
\le H\big|_{\theta=1}
=
\rho(1+p^2)-2
<0.
\]

Hence

\[
\boxed{
\frac{\partial R}{\partial\theta}<0
\quad\text{for all }0<p,\rho<1,\ \theta>1.
}
\tag{5.3}
\]

Therefore the two-point supercritical supremum is approached as
\(\theta\downarrow1\).

### 5.1 Boundary objective

Taking the one-sided limit in (5.1) gives

\[
R_1(p,\rho)=1+\delta(p,\rho),
\]

where

\[
\boxed{
\delta(p,\rho)
=
\frac{p\rho(1-p)(1-\rho)}
{(1-p\rho)\,[\,2-\rho(p^2-p+1)\,]}.
}
\tag{5.4}
\]

The second denominator is at least \(1\), because
\(p^2-p+1\le1\) and \(\rho<1\).

Moreover

\[
1-p\rho\ge1-p,\qquad 1-p\rho\ge1-\rho,
\]

so the only apparently singular corner \((p,\rho)=(1,1)\) also has
\(\delta\to0\). Thus \(\delta\) extends continuously by zero to the
boundary of the closed unit square. It is positive in the interior, so
its global maximum occurs at an interior critical point.

### 5.2 Critical equations

Direct differentiation of (5.4) gives positive denominators times the
following two numerators:

\[
F=
p^4\rho^2-2p^3\rho^2+2p^2\rho+2p\rho-4p-\rho+2,
\]

\[
G=
p^3\rho^2-2p^2\rho^2-\rho^2+4\rho-2.
\]

At an interior critical point \(F=G=0\). Their exact combination is

\[
F-pG=(p\rho-1)(2p+\rho-2).
\]

Since \(p\rho<1\),

\[
\rho=2(1-p).
\tag{5.5}
\]

Substituting (5.5) into \(G=0\) yields

\[
G(p,2(1-p))=2Q(p),
\]

with

\[
Q(p)=2p^5-8p^4+10p^3-6p^2+1.
\]

Also

\[
Q'(p)=2p(p-2)(5p^2-6p+3).
\]

The quadratic factor is strictly positive because its discriminant is
\(36-60=-24<0\). Thus \(Q'(p)<0\) on \((0,1)\). Finally,

\[
Q(1/2)=5/16>0,\qquad Q(1)=-1<0.
\]

So \(Q\) has exactly one root \(p_\star\in(1/2,1)\), and (5.5) supplies
the unique interior critical load
\(\rho_\star=2(1-p_\star)\in(0,1)\).
Because the boundary value is zero and the interior objective is
positive, this unique interior critical point is the global maximizer.

Substituting \(\rho_\star\) into (5.4) gives

\[
\delta_\star
=
\frac{(1-p_\star)^2(2p_\star-1)}
{(p_\star^2-2p_\star+2)(2p_\star^2-2p_\star+1)}.
\]

This proves the theorem.

## 6. Exact source consequence: three support points are necessary for ratio 2

A one-point law has identical policies. The theorem gives the uniform
two-point bound

\[
\frac{\mathbb E T_{\rm MS}}{\mathbb E T_G}\le C_2<2.
\]

Section 7 of the 2020 source uses three distinct support points
\(1-\delta,1,\delta^{-1}+1\) (with positive probabilities for
\(0<\delta<1\)) and proves that its ratio approaches \(2\) in a suitable
joint limit. Therefore a finite-support sequence whose ratio approaches
\(2\) needs at least three support points, and three suffice.

This pinpoints a genuine mechanism absent from two-point laws: a
near-unit mass creates one priority inversion, a second nearby atom
creates a distinct valley boundary, and a rare very long atom drives the
heavy-traffic waiting scale.

## 7. Validation and scope

A symbolic self-check verifies:

1. the exact averaged difference (4.1);
2. the factorization (5.2);
3. the boundary objective (5.4);
4. both critical-point derivative factorizations;
5. \(F-pG=(p\rho-1)(2p+\rho-2)\);
6. the reduction to \(Q\), its derivative, and the closed form for
   \(\delta_\star\).

The checker is validation of algebra, not an independent mathematical
audit.

A fresh literature search on 2026-09-19 recovered the 2020 source and
the later heavy-traffic M/G/k result where M-SERPT is a factor-2
approximation under additional conditions, but did not locate a later
paper giving this exact all-load two-point supremum or closing
Conjecture 8.1. That is negative evidence only, not a novelty
certificate.

The frozen source metric remains

\[
W_{\rm MS}=5-2=3,
\]

because this theorem is uniform only over two-point service laws. Source
status remains **OPEN / PARTIAL**.
