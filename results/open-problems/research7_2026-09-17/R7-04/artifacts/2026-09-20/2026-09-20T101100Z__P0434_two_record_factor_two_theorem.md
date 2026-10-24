Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum is the owner's requested preference, not authenticated runtime telemetry here.

# P0434 / P01-A — factor two for every finite-support law with at most two strict internal M-SERPT records

**Status relative to Scully–Harchol-Balter–Scheller-Wolf (2020), Conjecture 8.1:** **PROVED PARTIAL**. This note does not prove the arbitrary-service-law conjecture. It closes the minimal unresolved two-record finite-support topology left by the preceding R7-04 report.

Outside source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Section 8, Conjecture 8.1, arXiv:1907.10792, DOI 10.1145/3379477. The source target is

\[
E[T_{MS}]\le 2E[T_G]
\]

for every source-admissible service law at every stable load. The full-source interval in the project remains `[2,5]`.

## 1. Inherited reduction

The preceding R7-04 theorem proved the following facts for positive finite-support laws.

1. If the M-SERPT increasing envelope has at most one strict internal record jump, then the factor-two inequality holds at every stable load.
2. If it has exactly two strict internal record ages
   \[
   0<b_1<b_2,
   \]
   then the last record `b_2` is always a Gittins hill.
3. Hence Gittins either uses both `b_1,b_2`, in which case the hill partitions align and factor two is already proved, or it skips `b_1` but necessarily uses `b_2`.

Only the skipped-first topology remained.

Put `b_0=0`, `b_3=infinity` and define the three M-SERPT blocks

\[
P_j=P(b_{j-1}<X\le b_j),\qquad
M_j=E[X1_{\{b_{j-1}<X\le b_j\}}],
\]
\[
m_j=E[X\wedge b_j],\qquad
V_j=E[(X\wedge b_j)^2],\qquad
A_j=1-\lambda m_j.
\]

Write

\[
p=P_1,\qquad q=P_2,\qquad r=P_3,
\qquad s=p+q,\qquad t=q+r,
\]

and

\[
a=A_1,\qquad b=A_2,\qquad c=A_3=1-\rho,
\qquad \rho=\lambda E[X].
\]

Thus `p,q,r>0`, `p+q+r=1`, and

\[
1>a>b>c>0.
\]

The exact M-SERPT SOAP quantities are

\[
Q_{MS}=\frac\lambda2\left(
\frac{pV_1}{a}+\frac{qV_2}{ab}+\frac{rV_3}{bc}
\right),
\tag{1.1}
\]

\[
R_{MS}=M_1+\frac{M_2}{a}+\frac{M_3}{b}.
\tag{1.2}
\]

In the skipped-first Gittins topology, the Gittins hill partition has only the final internal hill `b_2`, so Proposition 4.7 gives the explicit waiting lower surrogate

\[
\underline Q_G
=\frac\lambda2\left(
\frac{sV_2}{b}+\frac{rV_3}{bc}
\right).
\tag{1.3}
\]

Because `Q_G>=\underline Q_G` and `R_G>=E[X]`, it is enough to prove

\[
\boxed{
H:=2\underline Q_G-Q_{MS}+2E[X]-R_{MS}\ge0.
}
\tag{1.4}
\]

This note proves `(1.4)` for the entire skipped-first topology.

## 2. Exact topology coordinates

Set

\[
x:=1-a=\lambda m_1,
\qquad
y:=1-b=\lambda m_2.
\]

The fresh SERPT rank is `E[X]=rho/lambda`. At the two M-SERPT record ages the ranks can be written

\[
r_S(b_1)=E[X]+\frac{f}{\lambda t},
\qquad f:=p\rho-x,
\tag{2.1}
\]

and

\[
r_S(b_2)=E[X]+\frac{e}{\lambda r},
\qquad e:=s\rho-y.
\tag{2.2}
\]

Because `b_1` is a strict first record,

\[
0<f<p\rho.
\tag{2.3}
\]

If Gittins skips `b_1` and its next hill is `b_2`, then `b_1` lies inside the Gittins valley `(0,b_2]`. The endpoint chord condition is

\[
\frac{m_2-m_1}{q}\le \frac{m_2}{s}.
\]

Equivalently,

\[
\boxed{
d:=sx-py=pe-sf\ge0.
}
\tag{2.4}
\]

Also `m_2>m_1`, so

\[
e<q\rho+f.
\tag{2.5}
\]

The skipped condition automatically implies the strict order of the two M-SERPT records. Indeed

\[
\frac ef\ge\frac sp>\frac rt,
\tag{2.6}
\]

because

\[
st-pr=q>0.
\]

Thus there is no additional hidden record-order constraint.

The whole parameter domain has the following exact cube parametrization. Let

\[
P,Q,R,F\in(0,1),\qquad E\in[0,1),
\]

and put

\[
p=P,\qquad q=(1-P)Q,\qquad r=(1-P)(1-Q),\qquad \rho=R,
\tag{2.7}
\]

\[
f=PRF,
\tag{2.8}
\]

\[
e=R\left[(P+(1-P)Q)F+(1-P)Q(1-F)E\right].
\tag{2.9}
\]

Then

\[
\boxed{
a=1-PR(1-F),}
\tag{2.10}
\]

\[
\boxed{
b=1-R(1-F)\left[P+(1-P)Q(1-E)\right].}
\tag{2.11}
\]

Moreover

\[
a-b=R(1-P)Q(1-F)(1-E)>0,
\tag{2.12}
\]

and

\[
\boxed{
d=P(1-P)Q R(1-F)E\ge0.}
\tag{2.13}
\]

Conversely, `(2.3)--(2.5)` recover `F` and `E` by affine normalization, so this parametrizes the complete skipped-first topology, including its Gittins-chord tie face `E=0`.

## 3. Exact waiting rearrangement

From `(1.1)` and `(1.3)`, direct algebra gives

\[
2\underline Q_G-Q_{MS}
=\frac\lambda2\left[
\frac{kV_2}{ab}
+\frac{p(V_2-V_1)}a
+\frac{rV_3}{bc}
\right],
\tag{3.1}
\]

where

\[
\boxed{
k:=sa-d=2sa-q-pb.}
\tag{3.2}
\]

The coefficient `k` is strictly positive throughout the topology. Since `y>x`,

\[
d=sx-py=qx-p(y-x)<qx.
\]

Also `x<p\rho<p`, so

\[
\begin{aligned}
k&=s(1-x)-d\\
&>s-x(s+q)\\
&>s-p(s+q)\\
&=pr+q(q+r)>0.
\end{aligned}
\tag{3.3}
\]

Since `V_2>=V_1`, `(3.1)` yields

\[
2\underline Q_G-Q_{MS}
\ge\frac\lambda2\left[
\frac{kV_2}{ab}+\frac{rV_3}{bc}
\right].
\tag{3.4}
\]

The entire remaining proof is an exact lower bound for the right-hand side plus the residence term.

## 4. Blockwise Cauchy reduction

Let

\[
q_j:=\lambda M_j,
\qquad q_1+q_2+q_3=\rho,
\]

and put

\[
u:=q_1+q_2,\qquad q_3=\rho-u.
\]

Blockwise Cauchy gives

\[
\lambda^2V_3
\ge \frac{q_1^2}{p}+\frac{q_2^2}{q}+\frac{q_3^2}{r}.
\tag{4.1}
\]

For the truncated second moment at `b_2`, note that

\[
y=\lambda m_2=q_1+q_2+r\lambda b_2.
\]

Hence

\[
\lambda^2V_2
\ge
\frac{q_1^2}{p}+\frac{q_2^2}{q}+\frac{(y-u)^2}{r}.
\tag{4.2}
\]

Multiplying `(1.4)` by `lambda`, using `(3.4)`, `(4.1)`, and `(4.2)`, gives

\[
\lambda H\ge B(q_1,q_2),
\tag{4.3}
\]

where

\[
\begin{aligned}
B(q_1,q_2)
={}&2\rho-q_1-\frac{q_2}{a}-\frac{\rho-u}{b}\\
&+\frac{k}{2ab}
\left(
\frac{q_1^2}{p}+\frac{q_2^2}{q}+\frac{(y-u)^2}{r}
\right)\\
&+\frac{r}{2bc}
\left(
\frac{q_1^2}{p}+\frac{q_2^2}{q}+\frac{(\rho-u)^2}{r}
\right).
\end{aligned}
\tag{4.4}
\]

We may minimize over all real `q_1,q_2`, a larger domain than the physically feasible block moments.

Define

\[
H_0:=ck+ar>0.
\tag{4.5}
\]

At fixed `u=q_1+q_2`, completing the square in `q_1` gives the exact lower envelope

\[
\begin{aligned}
B_*(u)
={}&2\rho-\frac ua-\frac{\rho-u}{b}
+\frac{k(y-u)^2}{2abr}
+\frac{(\rho-u)^2}{2bc}\\
&+\frac{H_0u^2}{2abc s}
+\frac{p(1-a)u}{as}
-\frac{pq(1-a)^2bc}{2asH_0}.
\end{aligned}
\tag{4.6}
\]

The coefficient of `u^2` simplifies exactly to

\[
\boxed{
A_2=\frac{H_0}{2abcrs}>0.
}
\tag{4.7}
\]

Thus it remains only to show that the discriminant of the quadratic `(4.6)` is nonpositive.

## 5. The discriminant polynomial

Write

\[
B_*(u)=A_2u^2+B_1u+C_0,
\qquad
\Delta=B_1^2-4A_2C_0.
\]

Exact simplification gives

\[
\boxed{
\Delta=-\frac{\mathcal P(p,q,a,b,c)}{a^2b^2c^2sr},
}
\tag{5.1}
\]

where `mathcal P` is a polynomial. Since the denominator is positive, it is enough to prove `mathcal P>=0` on the skipped-first domain.

Substitute the cube coordinates `(2.7)--(2.11)` and call the resulting polynomial

\[
\widehat{\mathcal P}(P,Q,R,F,E).
\]

It has multidegree

\[
(6,4,6,4,4)
\]

and 1475 nonzero power-basis monomials.

The exact tensor Bernstein expansion over `[0,1]^5` has 6125 coefficients:

- 4397 are positive;
- 1727 are zero;
- exactly one is negative;
- the smallest positive coefficient is `1/1350`;
- the unique negative coefficient is `-1/300` at multi-index
  \[
  (4,4,3,0,4).
  \]

The unique negative coefficient belongs to the Bernstein slice `Q=1,F=0,E=1`. Splitting off that whole slice gives the exact identity

\[
\widehat{\mathcal P}
=Q^4(1-F)^4E^4 G(P,R)+\mathcal R(P,Q,R,F,E),
\tag{5.2}
\]

where every Bernstein coefficient of `mathcal R` is nonnegative. The two-variable face factors as

\[
\boxed{G(P,R)=R(1-R)J(P,R),}
\tag{5.3}
\]

with

\[
\begin{aligned}
J(P,R)={}&P^5R^4-2P^5R^3-8P^4R^4+14P^4R^3-2P^4R^2+P^4R\\
&+8P^3R^4-3P^3R^3-16P^3R^2+P^3R\\
&-14P^2R^3+20P^2R^2+4P^2R\\
&+7PR^2-12PR-R+2.
\end{aligned}
\tag{5.4}
\]

So only `J>=0` on the unit square remains.

## 6. Exact positivity certificate for the exceptional face

The degree of `J` is `(5,4)`. Subdivide `[0,1]^2` into the exact `32 x 32` dyadic grid. On 1022 of the 1024 cells, all 30 local Bernstein coefficients are strictly positive. Across those cells there are 30,660 positive coefficients, no zeros, and the smallest coefficient is

\[
\frac1{1048576}.
\]

Only the cells `(30,31)` and `(31,31)` have a negative local coefficient. They are both contained in the corner

\[
U:=1-P\le\frac1{16},
\qquad
V:=1-R\le\frac1{16}.
\]

In these coordinates, exact expansion gives

\[
\begin{aligned}
J(1-U,1-V)={}&-U^5V^4+2U^5V^3-2U^5V+U^5\\
&-3U^4V^4+8U^4V^3-8U^4V^2+3U^4V\\
&+14U^3V^4-23U^3V^3+9U^3V^2\\
&-14U^2V^4+15U^2V^3-U^2V^2\\
&+3UV^4-3UV^3+V^4+V^3.
\end{aligned}
\tag{6.1}
\]

Let `delta=1/16`. Keep only the positive monomials `U^5+V^3` and dominate the eight negative monomials as follows:

\[
U^5V^4\le\delta^4U^5,
\qquad
2U^5V\le2\delta U^5,
\]

\[
3U^4V^4\le3\delta^5V^3,
\]

and, by weighted AM-GM,

\[
8U^4V^2
\le \frac{32\delta}{5}U^5+rac{8\delta^3}{5}V^3.
\]

Also

\[
23U^3V^3\le23\delta^3V^3,
\qquad
14U^2V^4\le14\delta^3V^3.
\]

Young's inequality with conjugate exponents `5/2` and `5/3` gives

\[
U^2V^2\le\frac25U^5+\frac35V^{10/3}.
\]

Since `delta<(2/5)^3`,

\[
V^{10/3}\le\frac25V^3,
\]

so

\[
U^2V^2\le\frac25U^5+\frac6{25}V^3.
\]

Finally

\[
3UV^3\le3\delta V^3.
\]

Therefore

\[
J(1-U,1-V)
\ge(1-A)U^5+(1-B)V^3,
\tag{6.2}
\]

where exactly

\[
A=\frac{303109}{327680}<1,
\qquad
B=\frac{11453771}{26214400}<1.
\tag{6.3}
\]

Thus `J>=0` on the two remaining cells as well. Combining with the dyadic Bernstein certificate proves

\[
J(P,R)\ge0
\quad (0\le P,R\le1).
\tag{6.4}
\]

Equations `(5.2)--(5.3)` now yield

\[
\widehat{\mathcal P}\ge0
\quad\text{on }[0,1]^5.
\tag{6.5}
\]

Inside the nondegenerate topology, the nonnegative Bernstein remainder in `(5.2)` has positive terms and every Bernstein basis factor is positive, so `widehat{mathcal P}>0`. Hence

\[
\Delta<0.
\]

By `(4.7)`,

\[
B_*(u)>0
\]

for every real `u`. Therefore `(4.3)` proves

\[
\boxed{H>0}
\tag{6.6}
\]

throughout the strict skipped-first topology; the non-strict chord-tie face is covered by the same weak inequalities.

## 7. Factor-two consequence

Using `Q_G>=underline Q_G` and `R_G>=E[X]`,

\[
\begin{aligned}
2E[T_G]-E[T_{MS}]
&=2(Q_G+R_G)-(Q_{MS}+R_{MS})\\
&\ge 2\underline Q_G-Q_{MS}+2E[X]-R_{MS}\\
&=H\\
&\ge0.
\end{aligned}
\]

Thus the skipped-first topology satisfies the conjectured factor-two inequality at every stable load.

Combining this with the inherited aligned-two-record theorem and the inherited zero/one-record theorem gives:

> **Two-record finite-law theorem.** Every positive finite-support service law whose M-SERPT increasing envelope has at most two strict internal record jumps satisfies
> \[
> \boxed{E[T_{MS}]\le2E[T_G]}
> \]
> at every stable load.

Consequently, any finite-support counterexample to Conjecture 8.1 must have **at least three strict internal M-SERPT record jumps**. Because the final M-SERPT record is always shared with Gittins, every remaining finite obstruction is necessarily a longer **prefix rank-mismatch chain**.

This is still not the arbitrary-law theorem.

## 8. Exact self-check

Checker:

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T101000Z__P0434_two_record_skip_checker.py`

Archived executed output:

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T101000Z__P0434_two_record_skip_checker.out`

The exact run verifies the cube identities, polynomial multidegree, 6125-coefficient five-dimensional Bernstein table, exceptional-face factorization, all 1024 dyadic face cells plus the analytic corner bound, and the previous skipped-first witness. It ends with

`ALL_EXACT_CHECKS_PASS`.

For the inherited exact witness

\[
X\in\{1,2,4,8\},\qquad
P=(1/20,11/20,1/4,3/20),\qquad \rho=19/20,
\]

the newly proved target is

\[
2\underline Q_G-Q_{MS}+2E[X]-R_{MS}
=\frac{60274143}{1767050}>0.
\]

The checker is a self-check, not an independent publication audit.

## 9. Structural handoff to P01-B

The paired general-law worker has rewritten each remaining Gittins-valley waiting defect as a Stieltjes rectangle

\[
h(v)\,\Delta(1/A)_V\,
\frac{\Delta r_S}{r_S(u)}.
\]

The present theorem supplies the exact finite-chain base case for that program: **one skipped internal M-SERPT record is always fully payable by the exact residence/waiting slack, uniformly over masses, support geometry, and load.** The obstruction cannot appear until a prefix contains at least two strict record mismatches.

The next finite-law target should therefore be the four-block topology with three strict internal M-SERPT records. The useful objective is not another atom-specific family: derive the four-block analogue of `(4.4)` and determine whether two successive skipped-prefix rectangles admit an Abel/summation-by-parts charge against the same blockwise Cauchy slack. A successful induction on the number of strict record jumps would connect directly to P01-B's support-independent prefix-rectangle problem.
