# P0434 — three-point rank classification and exact factor-two theorem for the source extremal family

Target: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1*, Proc. ACM Meas. Anal. Comput. Syst. 4(1), Article 11 (2020), DOI 10.1145/3379477, Section 8, Conjecture 8.1. The source conjectures that the all-load worst-case mean-response ratio of M-SERPT to optimal Gittins is exactly 2. Its Section 7 gives a three-point family whose ratio tends to 2.

This note does **not** close Conjecture 8.1. It proves two source-relevant restricted results: (i) every three-point law has an explicit finite rank geometry, with at most eight Gittins combinatorial rank types; and (ii) for the exact three-point family used by the source to establish the lower bound 2, the M-SERPT/Gittins ratio is strictly below 2 at every finite stable parameter value in the source regime, for every load, and tends to 2 from below along the source scaling. The second statement is proved by exact SOAP algebra plus an exact Bernstein-basis positivity certificate.

## 1. Generic three-point Gittins and M-SERPT ranks

Let

\[
\Pr\{X=a\}=p,\qquad \Pr\{X=b\}=q,\qquad \Pr\{X=c\}=r,
\]

where

\[
0<a<b<c,\qquad p,q,r>0,\qquad p+q+r=1.
\]

Write

\[
d_1=b-a,\qquad d_2=c-b,
\]

and

\[
m=\mathbb EX=a+(q+r)d_1+r d_2.
\]

For a discrete distribution the Gittins rank at age \(u\) is

\[
r_G(u)=\inf_{v>u}
\frac{\int_u^v \bar F(t)\,dt}
{\bar F(u)-\bar F(v)}.
\tag{1.1}
\]

Between consecutive support points the tail \(\bar F\) is constant. Once an atom has been crossed, moving the stopping point farther inside the next constant-tail interval increases the numerator while leaving the denominator fixed. Therefore an optimizer in (1.1) can be taken at the next one of the remaining support points. This gives the following exact formulas.

For \(0\le u<a\), put \(x=a-u\). The three possible stopping ages \(a,b,c\) give

\[
A_1(u)=\frac{a-u}{p},
\tag{1.2}
\]

\[
A_2(u)=
\frac{(a-u)+(q+r)(b-a)}{p+q},
\tag{1.3}
\]

and

\[
A_3(u)=m-u.
\tag{1.4}
\]

Hence

\[
\boxed{
 r_G(u)=\min\{A_1(u),A_2(u),A_3(u)\},\qquad 0\le u<a.
}
\tag{1.5}
\]

For \(a\le u<b\), stopping at \(b\) or \(c\) gives

\[
B_1(u)=\frac{(q+r)(b-u)}{q},
\tag{1.6}
\]

and

\[
B_2(u)=
(b-u)+\frac{r(c-b)}{q+r},
\tag{1.7}
\]

so

\[
\boxed{
 r_G(u)=\min\{B_1(u),B_2(u)\},\qquad a\le u<b.
}
\tag{1.8}
\]

Finally, once age \(b\) has been reached the job is known to have size \(c\), and

\[
\boxed{r_G(u)=c-u,\qquad b\le u<c.}
\tag{1.9}
\]

These formulas give a finite classification without any numerical optimization. On \([0,a)\), the slopes of \(A_1,A_2,A_3\) are respectively

\[
-\frac1p< -\frac1{p+q}<-1.
\]

Thus, as age increases, the lower envelope can only move in the order

\[
A_3\longrightarrow A_2\longrightarrow A_1,
\]

with either or both of the first two phases omitted. Since \(A_1(u)\to0\) as \(u\uparrow a\), the final phase is always \(A_1\). There are therefore at most four lower-envelope types on \([0,a)\): \(A_1\) only, \(A_2\to A_1\), \(A_3\to A_1\), or \(A_3\to A_2\to A_1\). On \([a,b)\), \(B_1\) has steeper negative slope than \(B_2\) and \(B_1(u)\to0\) as \(u\uparrow b\), so there are at most two types: \(B_1\) only or \(B_2\to B_1\). Consequently a three-point service law has at most eight Gittins combinatorial rank types.

The possible switch distances are explicit. With \(x=a-u\),

\[
A_1=A_2
\iff
x=\frac{p(q+r)d_1}{q},
\tag{1.10}
\]

\[
A_2=A_3
\iff
x=(p+q)d_2-(q+r)d_1,
\tag{1.11}
\]

and

\[
A_1=A_3
\iff
x=\frac{p((q+r)d_1+r d_2)}{q+r}.
\tag{1.12}
\]

On the second interval, writing \(y=b-u\),

\[
B_1=B_2
\iff
 y=\frac{q d_2}{q+r}.
\tag{1.13}
\]

The SERPT rank is even simpler. It is

\[
r_S(u)=
\begin{cases}
 m-u,&0\le u<a,\\[3pt]
 (b-u)+\dfrac{r d_2}{q+r},&a\le u<b,\\[7pt]
 c-u,&b\le u<c.
\end{cases}
\tag{1.14}
\]

Each displayed piece is decreasing. Since M-SERPT is the increasing envelope of SERPT, its rank is therefore exactly a three-level feedback rank:

\[
\boxed{
 r_{MS}(u)=
 \begin{cases}
 M_0,&0\le u<a,\\
 M_1,&a\le u<b,\\
 M_2,&b\le u<c,
 \end{cases}
}
\tag{1.15}
\]

where

\[
M_0=m,
\qquad
M_1=\max\left\{m,d_1+\frac{r d_2}{q+r}\right\},
\qquad
M_2=\max\{M_1,d_2\}.
\tag{1.16}
\]

This is stronger than merely classifying the source's example: it reduces **every** three-point M-SERPT/Gittins comparison to finitely many rank geometries.

## 2. Specialization to the source lower-bound family

Section 7 of the source takes, for small \(\delta>0\),

\[
X_\delta=
\begin{cases}
1-\delta,&\text{with probability }1-\delta,\\
1,&\text{with probability }\delta-\delta^2,\\
1+\delta^{-1},&\text{with probability }\delta^2.
\end{cases}
\tag{2.1}
\]

We work on the whole explicit range

\[
0<\delta\le\frac12.
\tag{2.2}
\]

The elementary moments needed below are

\[
\mathbb EX_\delta=1+\delta^2,
\tag{2.3}
\]

\[
\mu_1:=\mathbb E\min\{X_\delta,1\}=1-\delta+\delta^2,
\tag{2.4}
\]

\[
\nu_1:=\mathbb E\min\{X_\delta,1\}^2
=1-2\delta+3\delta^2-\delta^3,
\tag{2.5}
\]

and

\[
\nu_\infty:=\mathbb EX_\delta^2
=2+3\delta^2-\delta^3.
\tag{2.6}
\]

The generic formulas above collapse sharply. For M-SERPT,

\[
M_0=1+\delta^2,
\qquad
M_1=1+\delta,
\qquad
M_2=\delta^{-1}.
\tag{2.7}
\]

The inequalities in (2.7) are strict on \((0,1/2]\), so M-SERPT has exactly the three levels separated at ages \(1-\delta\) and \(1\).

For Gittins, the first two candidate lines cross exactly at age

\[
1-2\delta.
\tag{2.8}
\]

The third candidate is never minimal on the first interval, and the first candidate on the second interval is always minimal. Hence

\[
r_G(u)=
\begin{cases}
\dfrac{1-\delta+\delta^2-u}{1-\delta^2},
&0\le u<1-2\delta,\\[8pt]
\dfrac{1-\delta-u}{1-\delta},
&1-2\delta\le u<1-\delta,\\[8pt]
\dfrac{1-u}{1-\delta},
&1-\delta\le u<1,\\[8pt]
1+\delta^{-1}-u,
&1\le u<1+\delta^{-1}.
\end{cases}
\tag{2.9}
\]

In particular the fresh-job rank is

\[
\boxed{
 r_0=r_G(0)=\frac{1-\delta+\delta^2}{1-\delta^2}.
}
\tag{2.10}
\]

At age \(1-\delta\), the rank jumps to \(\delta/(1-\delta)\), and

\[
r_0-\frac{\delta}{1-\delta}
=\frac{1-2\delta}{1-\delta^2}\ge0.
\tag{2.11}
\]

Thus this jump does not create a new worst rank. At age \(1\), by contrast, the rank jumps to \(1/\delta>r_0\). This recovers the source's statement that Gittins has the hill age at 1 but not the extra M-SERPT hill age at \(1-\delta\).

## 3. Exact SOAP work decomposition

Let the load be

\[
\rho=1-\varepsilon,\qquad 0<\varepsilon<1,
\tag{3.1}
\]

so

\[
\lambda=\frac{1-\varepsilon}{1+\delta^2}.
\tag{3.2}
\]

Define the positive load complements

\[
A=1-\lambda(1-\delta),
\qquad
B=1-\lambda(1-\delta+\delta^2),
\qquad
C=1-\lambda(1+\delta^2)=\varepsilon.
\tag{3.3}
\]

The source's M-SERPT hill/valley formula is exact for this discrete rank geometry. For the three possible job sizes,

\[
\boxed{
T_{MS}(1-\delta)
=(1-\delta)+\frac{\lambda(1-\delta)^2}{2A},
}
\tag{3.4}
\]

\[
\boxed{
T_{MS}(1)
=\frac1A+\frac{\lambda\nu_1}{2AB},
}
\tag{3.5}
\]

and

\[
\boxed{
T_{MS}(1+\delta^{-1})
=\frac{1+\delta^{-1}}B
+\frac{\lambda\nu_\infty}{2BC}.
}
\tag{3.6}
\]

For Gittins, the exact rank path (2.9) gives a compact r-work accounting identity which is the main simplification of this run.

For a tagged short or medium job, the worst future rank is \(r_0\). A new job begins at rank \(r_0\), so its new \(r_0\)-work is zero. An old job contributes its original work until age 1, namely \(\min\{X,1\}\). A long old job is discarded when its rank jumps to \(1/\delta\) at age 1, and is recycled exactly when its deterministic terminal rank falls back to \(r_0\), at age \(1+\delta^{-1}-r_0\). Its sole recycled block therefore has deterministic length \(r_0\). Thus

\[
X^{old}_0[r_0]=\min\{X,1\},
\qquad
X^{old}_1[r_0]=r_0\,\mathbf 1_{\{X=1+\delta^{-1}\}},
\tag{3.7}
\]

and no higher recycled block occurs. The exact common waiting term for short and medium jobs is consequently

\[
\boxed{
W_0=\frac{\lambda(\nu_1+\delta^2r_0^2)}{2B}.
}
\tag{3.8}
\]

Their new-work load is zero throughout residence, so

\[
\boxed{
T_G(1-\delta)=1-\delta+W_0,
\qquad
T_G(1)=1+W_0.
}
\tag{3.9}
\]

For a tagged long job, the worst future rank is \(1/\delta\). At that threshold a new job contributes exactly \(\min\{X,1\}\), an old job contributes its whole size \(X\), and there is no recycled old block. Hence the waiting term is

\[
\boxed{
W_\infty=\frac{\lambda\nu_\infty}{2BC}.
}
\tag{3.10}
\]

For residence, the tagged long job's worst future rank stays above \(r_0\) until its age reaches \(1+\delta^{-1}-r_0\). During that part, every new arrival can contribute \(\min\{X,1\}\), giving slowdown factor \(1/B\). During the terminal interval of length \(r_0\), the tagged job's worst future rank is no worse than the fresh-job rank, so new work is zero. Therefore

\[
\boxed{
R_G(1+\delta^{-1})
=\frac{1+\delta^{-1}-r_0}{B}+r_0,
}
\tag{3.11}
\]

and

\[
\boxed{
T_G(1+\delta^{-1})
=W_\infty+rac{1+\delta^{-1}-r_0}{B}+r_0.
}
\tag{3.12}
\]

Equations (3.4)--(3.12) are exact for every \(0<\delta\le1/2\) and every stable load, not an asymptotic replacement of the Section 7 approximations.

Let

\[
E_{MS}=(1-\delta)T_{MS}(1-\delta)
+(\delta-\delta^2)T_{MS}(1)
+\delta^2T_{MS}(1+\delta^{-1}),
\tag{3.13}
\]

and define \(E_G\) analogously from (3.9) and (3.12).

## 4. Exact factor-two theorem for the source family

We now prove that the source family approaches 2 but never crosses it at finite parameters in the whole regime (2.2).

**Theorem.** For every

\[
0<\delta\le\frac12,
\qquad
0<\varepsilon<1,
\]

with \(\lambda\) given by (3.2),

\[
\boxed{
\frac{E_{MS}}{E_G}<2.
}
\tag{4.1}
\]

**Proof.** Substituting (3.4)--(3.12), bringing terms to a common denominator, and simplifying exactly gives

\[
2E_G-E_{MS}
=\frac{P(\delta,\varepsilon)}
{2\varepsilon(1-\delta^2)
[\delta^2+\delta+\varepsilon(1-\delta)]
[\delta+\varepsilon(1-\delta+\delta^2)]},
\tag{4.2}
\]

where

\[
\begin{aligned}
P(\delta,\varepsilon)={}&
\delta^9-2\delta^8-4\delta^7+\delta^5+2\delta^4+2\delta^3\\
&+\varepsilon\bigl(-2\delta^9-3\delta^8+17\delta^7-16\delta^6-10\delta^5
+9\delta^4-7\delta^3+8\delta^2\bigr)\\
&+\varepsilon^2\bigl(\delta^9+5\delta^8-18\delta^7+12\delta^6+23\delta^5
-28\delta^4+12\delta^3-6\delta^2+2\delta+1\bigr)\\
&+\varepsilon^3\bigl(-2\delta^8+5\delta^7-14\delta^5+17\delta^4-7\delta^3
+2\delta^2-2\delta+1\bigr).
\end{aligned}
\tag{4.3}
\]

Every denominator factor in (4.2) is strictly positive on the stated domain. It remains to prove \(P>0\).

Put

\[
u=2\delta\in(0,1].
\]

Expand \(P(u/2,\varepsilon)\) in the tensor-product Bernstein basis of bidegree \((9,3)\):

\[
P(u/2,\varepsilon)
=
\sum_{i=0}^9\sum_{j=0}^3
b_{ij}\binom9i u^i(1-u)^{9-i}
\binom3j\varepsilon^j(1-\varepsilon)^{3-j}.
\tag{4.4}
\]

Exact rational conversion gives the coefficient table below, with rows \(i=0,\ldots,9\) and columns \(j=0,\ldots,3\):

\[
\begin{array}{c|cccc}
0&0&0&1/3&2\\
1&0&0&10/27&2\\
2&0&1/54&31/72&73/36\\
3&1/336&37/672&65/126&25/12\\
4&13/1008&25/224&949/1512&13/6\\
5&47/1344&2323/12096&4639/6048&41/18\\
6&17/224&101/336&3767/4032&3247/1344\\
7&55/384&6077/13824&3895/3456&165/64\\
8&31/128&4187/6912&9241/6912&3175/1152\\
9&189/512&401/512&395/256&375/128
\end{array}
\tag{4.5}
\]

Every Bernstein coefficient is nonnegative. On \(0<u\le1\), \(0<\varepsilon<1\), at least one positive coefficient multiplies a positive basis term, so the sum is strictly positive. Hence \(P(\delta,\varepsilon)>0\), proving (4.1). □

The exact symbolic checker archived with this note verifies (4.2), converts (4.3) to the Bernstein basis by rational arithmetic, checks every coefficient in (4.5), and ends with `ALL_EXACT_CHECKS_PASS`.

## 5. Exact approach to two from below

The source chooses

\[
\varepsilon=\delta^{3/2}
\]

and sends \(\delta\downarrow0\). Put \(\delta=t^2\), so \(\varepsilon=t^3\). Expanding the **exact** ratio obtained above gives

\[
\boxed{
\frac{E_{MS}}{E_G}
=2-3t+t^2+8t^3-11t^4-9t^5+O(t^6).
}
\tag{5.1}
\]

Equivalently,

\[
\boxed{
\frac{E_{MS}}{E_G}
=2-3\sqrt\delta+\delta+8\delta^{3/2}-11\delta^2-9\delta^{5/2}+O(\delta^3).
}
\tag{5.2}
\]

Thus the source construction reaches the lower-bound constant 2 **from below**, and the leading finite-parameter deficit is exactly \(3\sqrt\delta\) along the advertised scaling.

## 6. What this does and does not establish

The generic rank classification removes continuous Gittins optimization from the three-point problem: only finitely many affine-envelope geometries remain. The source's own apparent extremal family is now solved exactly at all loads in its full small-\(\delta\) regime, and it cannot hide a finite-parameter ratio above 2. Its approach to 2 is quantitatively controlled by (5.2).

This does **not** prove that every three-point distribution has ratio at most 2, and it does not improve the source-wide universal interval \([2,5]\). The next mathematically meaningful step is therefore to use the eight-type classification to derive one exact response-time formula per genuinely feasible type and seek a type-independent charging inequality for \(2E_G-E_{MS}\), rather than searching continuous rank functions blindly.

## 7. Current literature boundary

A bounded 2026-09-19 search recovered the original 2020 all-load M/G/1 paper and the later Scully--Grosof--Harchol-Balter M/G/k result proving a factor-2 statement only in a heavy-traffic regime under additional tail assumptions. It did not recover a later source explicitly proving or refuting Conjecture 8.1, nor a later exact treatment of the source's three-point family matching (4.1)--(5.2). This is negative search evidence only, not a novelty certificate or a proof of worldwide openness.
