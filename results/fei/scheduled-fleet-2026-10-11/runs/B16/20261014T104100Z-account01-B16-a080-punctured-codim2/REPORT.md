# B16 / A080 — tensor-prime punctured codimension-two family

Run: `20261014T104100Z-account01-B16-a080-punctured-codim2`  
Primary packet: **A080 — universal-counterexample standard**  
Stable gap: `G-GU-SIGNED-KL-DEGREE-GE3`  
Claim: `B16-A080-PUNCTURED-CODIM2-v1`  
Status: **PROVED at the stated family/obstruction scope; independent review pending. Universal GU and full FEI remain OPEN.**

## Frozen candidate and implication

The frozen pair is

\[
G(f)\le4I(f)+\frac34U(f)
\]

for every genuine Boolean function on every finite uniform cube. The reviewed high-degree reduction says it is enough to prove

\[
D_{\ge2}+\frac12V_1
\le\left(4-\frac2{\ln2}\right)I+\frac34U
+\frac2{\ln2}Q_{\ge3}
\]

for every tensor-prime, positive-residual Boolean function of degree at least three. Here

\[
Q_{\ge3}=I-M_1-W_2,
\qquad M_1=\sum_i\min\{p(\varnothing),p(\{i\})\}.
\]

If that leaf is proved, the audited restriction induction gives (U\le16I), and the source reduction gives (H\le34I).

## Family

For every (n\ge3), define

\[
f_n(x)=-1
\quad\Longleftrightarrow\quad
x_1=x_2=1\text{ and }x\ne(1,\ldots,1).
\]

This is a codimension-two negative subcube with its all-plus point punctured. With (arepsilon=2^{1-n}), its full signed spectrum is

\[
\widehat f_n(S)=
\begin{cases}
1/2+\varepsilon,&S=\varnothing,\\
-1/2+\varepsilon,&\varnothing\ne S\subseteq\{1,2\},\\
\varepsilon,&S\not\subseteq\{1,2\}.
\end{cases}
\]

Thus (deg f_n=n). A nonzero (2\times2) Fourier minor across every nontrivial variable partition proves that every (f_n) is tensor-prime; this is not a tensor-padding artifact.

## Exact (H,I,U,G) and reserve

Put (L(t)=t\log_2(1/t)), (q_+=(1/2+\varepsilon)^2), (q_-=(1/2-\varepsilon)^2), and (r=\varepsilon^2). Then

\[
H_n=L(q_+)+3L(q_-)+(2^n-4)L(r),
\qquad
I_n=1+(n-4)\varepsilon,
\]

\[
U_n=L(q_+)+L(q_-)
+q_-\log_2\frac1{1-2\varepsilon}
+n\varepsilon-(4n-4)\varepsilon^2,
\]

and, for (n\ge4),

\[
G_n=nU_n-V_{n-1}-\frac{n-2}{2}(1+U_{n-1}),
\]

where, for (e=2^{1-N}),

\[
V_N=L(e^2)+\frac12L((1-e)^2)+Ne-(2N-1)e^2.
\]

The high-degree reserve is exactly

\[
Q_{\ge3}(f_n)
=\frac14+(n-1)\varepsilon
-\left(n+\binom n2\right)\varepsilon^2.
\]

All empty, normalization, terminal, and restriction terms are present. The formula for (G) comes from actual physical restrictions: each (x_1,x_2) restriction has a constant child and a punctured-dictator child; each other restriction has an unpunctured two-bit-defect child and an (f_{n-1}) child.

## Controlled asymptotics

The exact formulas give

\[
\begin{aligned}
H_n&=2+\left(4n-8+\frac2{\ln2}\right)\varepsilon+O(n\varepsilon^2),\\
U_n&=1+\left(n+\frac1{2\ln2}\right)\varepsilon+O(n\varepsilon^2),\\
G_n&=2+\left(n-\frac1{\ln2}\right)\varepsilon+O(n^2\varepsilon^2),\\
I_n&=1+(n-4)\varepsilon.
\end{aligned}
\]

Therefore

\[
\frac{H_n}{I_n}\to2,
\qquad
\frac{U_n}{I_n}\to1,
\qquad
\frac{G_n}{I_n}\to2,
\qquad
\frac{Q_{\ge3}(f_n)}{I_n}\to\frac14.
\]

For the frozen pair,

\[
G_n-4I_n-\frac34U_n\to-\frac{11}{4}.
\]

Hence this is not a falsifier of the pair, GU, or FEI; none of (G/I,U/I,H/I) diverges.

## What changed

Before this run, the retained reserve was known to be strictly positive on every degree-at-least-three Boolean function, but the finite evidence supplied no all-dimensional boundary family. This run gives an explicit tensor-prime, full-degree family converging spectrally to the degree-two boundary.

The consequence is exact: a reserve-only tail theorem cannot use a universal coefficient larger than (1/4) in (Q_{\ge3}\ge cI). A finite low-dimensional strict margin cannot be exported unchanged. The family does **not** disprove the plausible sharp bound (Q_{\ge3}\ge I/4), and it does not control the signed quantity (D_{\ge2}+V_1/2). Those are the remaining obligations.

## Verification

`verify_punctured_codim2.py` reconstructs truth tables and exact integer Walsh transforms through (n=9), checks every coefficient, exact influence, upper-set masses, restriction children, the (G) recurrence, and a nonzero tensor-prime minor for every nontrivial partition. Logarithmic comparisons use Python `Decimal` at 100 digits only after exact rational masses are formed.

Observed output:

- 2,018 assertions;
- maximum (H,U,I,G) formula discrepancies at most (6\times10^{-99});
- all nontrivial partitions checked for (3\le n\le9);
- no random seed;
- asymptotic table through (n=80) confirms the displayed limits.

The all-dimensional result is the analytic proof in `PUNCTURED_CODIM2_FAMILY.tex`; the finite computation is validation, not extrapolation.

## Next action

Test and prove or refute the sharp Boolean reserve candidate

\[
Q_{\ge3}(f)\ge\frac14I(f)
\]

for all nonconstant genuine Boolean (f). Even if true, the named B20 consumer must still prove that the signed high-order KL excess is paid by ((2/\ln2)Q_{\ge3}); reserve size alone does not establish the GU leaf.

Model/effort metadata: `UNKNOWN`.
