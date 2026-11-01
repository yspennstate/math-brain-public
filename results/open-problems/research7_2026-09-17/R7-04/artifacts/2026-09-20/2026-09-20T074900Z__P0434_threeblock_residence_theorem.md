# P0434 — three-block residence theorem and terminal Gittins-hill alignment

Source: Ziv Scully, Mor Harchol-Balter, Alan Scheller-Wolf, *Simple Near-Optimal Scheduling for the M/G/1* (2020), Conjecture 8.1, arXiv:1907.10792, DOI 10.1145/3379477.

Status: **PROVED PARTIAL**. This does not prove Conjecture 8.1 for arbitrary service laws. It proves the residence-side inequality on the minimal finite-support topology not covered by the preceding one-record theorem and isolates the only remaining two-record waiting mismatch.

## 1. Setup

Let `X` have positive finite support, finite mean

\[
\mu=E[X],\qquad \rho=\lambda\mu<1.
\]

Assume the increasing M-SERPT envelope has exactly two strict internal record ages

\[
0<b_1<b_2.
\]

Because a discrete SERPT rank is affine decreasing between support ages, M-SERPT is constant on the three rank blocks

\[
(0,b_1],\qquad (b_1,b_2],\qquad (b_2,\infty).
\]

Put `b_0=0`, `b_3=infinity`, and for `j=1,2,3` define

\[
P_j=P(b_{j-1}<X\le b_j),\qquad
M_j=E[X1_{\{b_{j-1}<X\le b_j\}}].
\]

For `j=1,2`, let

\[
m_j=E[X\wedge b_j],\qquad
V_j=E[(X\wedge b_j)^2],\qquad
A_j=1-\lambda m_j.
\]

Set

\[
m_3=\mu,\qquad V_3=E[X^2],\qquad
A_0=1,\qquad A_3=1-\rho.
\]

The exact SOAP formulas (Propositions 4.7–4.8 of the source, with equality because M-SERPT has monotone rank) give

\[
\boxed{
Q_{MS}=\frac\lambda2\sum_{j=1}^3
\frac{P_jV_j}{A_{j-1}A_j},
}
\tag{1.1}
\]

and

\[
\boxed{
R_{MS}=\sum_{j=1}^3\frac{M_j}{A_{j-1}}.
}
\tag{1.2}
\]

Equivalently, if

\[
q_j:=\lambda M_j,
\]

then

\[
q_1+q_2+q_3=\rho.
\tag{1.3}
\]

## 2. The new theorem

### Theorem 2.1 — three-block residence inequality

Under the setup above, for every stable load,

\[
\boxed{
R_{MS}<Q_{MS}+2\mu.
}
\tag{2.1}
\]

Equivalently, the exact residence reserve

\[
\boxed{
K_3:=Q_{MS}+2\mu-R_{MS}
}
\tag{2.2}
\]

is strictly positive.

The theorem actually needs only the three-block monotone SOAP formulas (1.1)–(1.2); the M-SERPT record inequalities themselves are not used after those formulas are available.

### Proof

For each block, Cauchy-Schwarz gives

\[
M_j^2
\le
P_j E[X^2 1_{\{b_{j-1}<X\le b_j\}}]
\le P_jV_j.
\tag{2.3}
\]

Therefore, after multiplying (2.2) by `lambda`,

\[
\lambda K_3
\ge
\Phi(q_1,q_2,q_3;A_1,A_2,A_3),
\tag{2.4}
\]

where

\[
\Phi
:=
2\rho
+\frac12\sum_{j=1}^3
\frac{q_j^2}{A_{j-1}A_j}
-\sum_{j=1}^3\frac{q_j}{A_{j-1}}.
\tag{2.5}
\]

The useful point is that the service-distribution geometry has disappeared. We now have only

\[
1>A_1>A_2>A_3=1-\rho>0,
\qquad
q_1+q_2+q_3=\rho.
\]

Complete the square in each `q_j`:

\[
\frac{q_j^2}{2A_{j-1}A_j}-\frac{q_j}{A_{j-1}}
=
\frac{(q_j-A_j)^2}{2A_{j-1}A_j}
-\frac{A_j}{2A_{j-1}}.
\]

Weighted Cauchy gives

\[
\sum_{j=1}^3\frac{(q_j-A_j)^2}{A_{j-1}A_j}
\ge
\frac{\left(\rho-A_1-A_2-A_3\right)^2}
{A_1+A_1A_2+A_2A_3}.
\]

Thus, writing

\[
a=A_1,\qquad b=A_2,\qquad c=A_3=1-\rho,
\]

we obtain

\[
\Phi\ge\Psi(a,b,c),
\tag{2.6}
\]

with

\[
\boxed{
\Psi(a,b,c)=
2(1-c)
-\frac12\left(a+\frac ba+\frac cb\right)
+\frac{(1-a-b-2c)^2}{2(a+ab+bc)}.
}
\tag{2.7}
\]

It remains to prove `Psi>0` on

\[
0<c<b<a<1.
\]

Because all denominators are positive, this is equivalent to positivity of

\[
P(a,b,c):=2ab(a+ab+bc)\Psi(a,b,c).
\]

Exact expansion gives

\[
\begin{aligned}
P={}&-a^3b^2-5a^2b^2c+6a^2b^2-a^2bc+2a^2b-a^2c\\
&-4ab^2c^2+8ab^2c-3ab^2+3abc^2-4abc+ab-b^3c.
\end{aligned}
\tag{2.8}
\]

Map the ordered simplex to the unit cube by

\[
c=Z,
\qquad
b=Z+(1-Z)Y,
\qquad
a=b+(1-b)X,
\qquad 0\le X,Y,Z\le1.
\tag{2.9}
\]

The resulting polynomial has power multidegree `(3,5,5)`. Convert it exactly to the tensor Bernstein basis after degree elevation to `(5,8,8)`. There are 486 rational Bernstein coefficients. The exact certificate contains

- 422 strictly positive coefficients,
- 64 zero coefficients,
- 0 negative coefficients,
- smallest strictly positive coefficient `1/40`.

Every tensor Bernstein basis function is nonnegative on the closed cube and strictly positive in the open cube. Hence

\[
P(a,b,c)>0\qquad(0<c<b<a<1),
\]

so `Psi>0`, `Phi>0`, and finally

\[
K_3>0.
\]

This proves (2.1).  ∎

The certificate is reproduced by

`research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T074800Z__P0434_threeblock_residence_checker.py`.

Its archived output ends with `ALL_EXACT_CHECKS_PASS`.

## 3. Analytic structural lemma: the last M-SERPT record is always a Gittins hill

The preceding theorem solves the residence side. The waiting side can also be reduced structurally.

Let `b` be the last strict internal M-SERPT record of an arbitrary positive finite-support law, and let

\[
L=r_S(b)=\frac{N(b)}{S(b)},
\qquad
S(x)=P(X>x),\quad N(x)=E[(X-x)^+].
\]

By definition of the last record,

\[
r_S(c)\le L\qquad(c>b).
\]

For every Gittins stopping endpoint `c>b`,

\[
\frac{N(b)-N(c)}{S(b)-S(c)}-L
=
\frac{-\{N(c)-LS(c)\}}{S(b)-S(c)}\ge0,
\]

because `N(b)-LS(b)=0` and `N(c)-LS(c)<=0`. The terminal stopping candidate is exactly `L`, so

\[
\boxed{r_G(b)=L=r_S(b).}
\tag{3.1}
\]

Immediately before `b`, Gittins rank is at most SERPT rank and therefore below the preceding M-SERPT record level, which is strictly smaller than `L`. Hence

\[
\boxed{b\text{ is a strict Gittins hill.}}
\tag{3.2}
\]

### Consequence for the two-record topology

If M-SERPT has exactly two strict records `b_1<b_2`, then Gittins **cannot skip `b_2`**. Since every Gittins hill is an M-SERPT hill (source Lemma 5.3), there are only two possibilities:

1. Gittins uses both `b_1,b_2`; or
2. Gittins skips `b_1` and uses only `b_2`.

In case 1, the Gittins and M-SERPT hill partitions coincide. Proposition 4.7 then gives

\[
Q_G\ge Q_{MS},
\]

while Proposition 4.9 gives `R_G>=mu`. Theorem 2.1 therefore immediately yields

\[
2T_G-T_{MS}
\ge
Q_{MS}+2\mu-R_{MS}
=K_3>0.
\]

Thus every two-record finite law with aligned first record already satisfies factor two. The **only unresolved two-record topology** is the genuine skipped-first-record case.

## 4. The skipped-first topology is real

The reduction above is sharp; the first record need not be a Gittins hill.

Take

\[
X\in\{1,2,4,8\},
\qquad
P=\left(\frac1{20},\frac{11}{20},\frac14,\frac3{20}\right).
\]

At ages `0,1,2,4`, the exact SERPT ranks are

\[
\left(\frac{67}{20},\frac{47}{19},\frac72,4\right),
\]

so the strict M-SERPT records are `b_1=2` and `b_2=4`.

The exact Gittins ranks at the same ages are

\[
\left(\frac{55}{17},\frac{19}{11},\frac{16}{5},4\right).
\]

Since

\[
\frac{16}{5}<\frac{55}{17}<4,
\]

Gittins skips the first M-SERPT record and uses the last one. This is therefore an exact four-atom witness of the minimal unresolved rank mismatch, not a counterexample to Conjecture 8.1.

At the high load `rho=19/20`, the exact M-SERPT quantities are

\[
Q_{MS}=\frac{12183427}{353410},
\qquad
R_{MS}=\frac{6246811}{706820},
\]

and

\[
\boxed{
K_3=Q_{MS}+2\mu-R_{MS}
=\frac{22855737}{706820}>0.
}
\]

The distribution-free certificate from Theorem 2.1 alone gives the weaker but still exact lower bound

\[
K_3\ge\frac{25829399}{1413640}>0.
\]

## 5. Precise handoff to P01-B

P01-B's newest arbitrary-law waiting theorem writes

\[
Q_{MS}\le \underline Q_G+\mathcal E_{\rm eff},
\qquad
\mathcal E_{\rm eff}=\mathcal E_{\rm out}-\mathcal C_\tau,
\]

where the positive defect is only the outer Gittins/M-SERPT rank mismatch after retaining the central-plateau and `tau` credits.

For the present three-block topology,

\[
2T_G-T_{MS}
\ge
2\underline Q_G-Q_{MS}+2\mu-R_{MS}
=
K_3-2(Q_{MS}-\underline Q_G).
\]

Therefore the full two-record finite-law problem is reduced to

\[
\boxed{
K_3\ge2\mathcal E_{\rm eff}.
}
\tag{5.1}
\]

The new theorem proves `K_3>0` at **all** stable loads, so P01-B no longer needs to pay the separate scalar high-load term `(L(rho)-2)mu` on this minimal topology. All remaining difficulty is the single skipped-prefix waiting defect.

If Gittins skips `b_1`, its Proposition-4.7 lower surrogate has only the last hill `b_2` and is explicit:

\[
\underline Q_G
=
\frac\lambda2\left[
\frac{(P_1+P_2)V_2}{A_2}
+
\frac{P_3V_3}{A_2A_3}
\right].
\tag{5.2}
\]

Consequently the exact remaining two-record inequality can be written without any hidden Gittins optimization as

\[
\boxed{
2\underline Q_G-Q_{MS}+2\mu-R_{MS}\ge0.
}
\tag{5.3}
\]

The next finite-law attack should prove (5.3) from the record/chord conditions that force Gittins to skip `b_1`, or produce a source-valid counterexample. This is now strictly narrower than the generic three-block residence problem.

## 6. Scope warning

Theorem 2.1 is a finite/three-block statement. It is **not** asserted for arbitrary infinite-support M-SERPT rank geometries. In particular, the arbitrary-law proof should use it as a finite prefix/residence module, not silently extrapolate `R_MS<=Q_MS+2mu` to every source-admissible law.
