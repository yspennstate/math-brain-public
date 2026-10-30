# B16 FEI signed transport — Carleman collapse of the Shannon/Laplace bank to the Brownian threshold bank

**Date:** 21 September 2026  
**Scope:** `fleet01 / B16`, signed transport / noise interpolation, APPROACH 10/13  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** one analytic Loewner-contraction theorem and its compiler corollaries. No publication-priority claim.

## 0. Exact missing implication attacked

This run consumes the fresh cross-account interface-C report

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260921T200356Z-restriction-kernel-polarization/REPORT.md`

(blob on the inspected source snapshot: `f139911380f55a0dc715c4d00463b2e33a2ab947`), together with the current B16 source reduction

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260921T204046Z-terminal-shell-feature-projector/REPORT.md`

and its supplement `RADIAL_FINITE_DIFFERENCE.md`.

The fleet02/B18 report reduces the authentic square-first full-line compiler to two positive quadratic banks:

\[
\mathcal Q_{\mathsf S}(h)
=\frac1{\ln2}\int_0^\infty
\frac{\left|\sum_r\alpha_r(e^{-tU_r^2}-e^{-tV_r^2})\right|^2}{t^2}\,dt,
\tag{0.1}
\]
\[
\mathcal Q_{\mathsf M}(h)
=\int_0^\infty
\left|\sum_r\alpha_r
({\bf1}_{u\le V_r^2}-{\bf1}_{u\le U_r^2})\right|^2du.
\tag{0.2}
\]

Its phase bank was already proved to satisfy
\[
\mathcal Q_{\mathsf P}\le \frac2{\ln2}\mathcal Q_{\mathsf M},
\tag{0.3}
\]
but the Shannon/Laplace bank (0.1) was left as a separate open payment, intended to use terminal/R16/negative-entropy credits.

The present run proves that this separation is unnecessary:

\[
\boxed{\mathcal Q_{\mathsf S}\le \frac{\pi}{\ln2}\mathcal Q_{\mathsf M}.}
\tag{0.4}
\]

The proof is a direct factorization through the classical Carleman operator.  It is a quadratic-form / Loewner statement, so every authentic signed terminal coefficient remains inside the square.  No relation is positive-parted, no same-syndrome cancellation is lost, and no terminal/R16/negative-entropy credit is spent.

This collapses the **entire** full-line Shannon-plus-phase source to the single Brownian threshold bank.

---

## 1. Scalar kernels

For real \(x,y\), put \(X=x^2\), \(Y=y^2\).  The Shannon kernel from the consumed fleet02 report is

\[
\mathsf S(x,y)
=\frac{(X+Y)\ln(X+Y)-X\ln X-Y\ln Y}{\ln2},
\tag{1.1}
\]
with \(0\ln0=0\).

The Brownian threshold kernel is

\[
\mathsf M(x,y)=\min\{X,Y\}
=\int_0^\infty {\bf1}_{u\le X}{\bf1}_{u\le Y}\,du.
\tag{1.2}
\]

The fleet02 report already proved that both are positive semidefinite and gave

\[
(\ln2)\mathsf S(x,y)
=\int_0^\infty
\frac{(1-e^{-tX})(1-e^{-tY})}{t^2}\,dt.
\tag{1.3}
\]

The key point is to keep (1.3) as an **operator factorization**, rather than estimate its scalar diagonal.

---

## 2. PROVED — Shannon-to-Brownian Carleman Loewner contraction

### Theorem 2.1 — `P03-B16-SHANNON-CARLEMAN-CONTRACTION`

For every finite collection of real numbers \(x_a\) and real coefficients \(c_a\),

\[
\boxed{
\sum_{a,b}c_ac_b\,\mathsf S(x_a,x_b)
\le
\frac{\pi}{\ln2}
\sum_{a,b}c_ac_b\,\mathsf M(x_a,x_b).
}
\tag{2.1}
\]

Equivalently, in Loewner order,

\[
\boxed{\mathsf S\preceq \frac{\pi}{\ln2}\mathsf M.}
\tag{2.2}
\]

### Proof

Let \(X_a=x_a^2\), and define the signed threshold profile

\[
F(u)=\sum_a c_a{\bf1}_{\{u\le X_a\}},
\qquad u>0.
\tag{2.3}
\]

By (1.2),

\[
\sum_{a,b}c_ac_b\mathsf M(x_a,x_b)
=\int_0^\infty F(u)^2\,du.
\tag{2.4}
\]

Also

\[
\frac{1-e^{-tX_a}}{t}
=\int_0^{X_a}e^{-tu}\,du.
\tag{2.5}
\]

Substituting (2.5) in (1.3), summing with the coefficients \(c_a\), and using Tonelli first for simple profiles and then density gives

\[
\begin{aligned}
(\ln2)\sum_{a,b}c_ac_b\mathsf S(x_a,x_b)
&=
\int_0^\infty
\left|
\int_0^\infty e^{-tu}F(u)\,du
\right|^2dt\\
&=
\int_0^\infty\!\!\int_0^\infty
\frac{F(u)F(v)}{u+v}\,du\,dv.
\end{aligned}
\tag{2.6}
\]

Thus the quadratic form is exactly that of the Carleman operator

\[
(CF)(u)=\int_0^\infty\frac{F(v)}{u+v}\,dv.
\tag{2.7}
\]

Its \(L^2(0,\infty)\) norm is at most \(\pi\) by the elementary Schur test with weight \(w(u)=u^{-1/2}\), because

\[
\int_0^\infty\frac{v^{-1/2}}{u+v}\,dv
=
\pi u^{-1/2},
\tag{2.8}
\]
and the same identity holds after interchanging \(u,v\).  Therefore

\[
\langle F,CF\rangle
\le \pi\|F\|_2^2.
\tag{2.9}
\]

Combining (2.4), (2.6), and (2.9) proves (2.1).  \(\square\)

### Sharpness of the kernel constant

The constant \(\pi\) in the natural-log form is sharp even when all \(X_a\in[0,1]\).  Indeed the span of the functions \({\bf1}_{[0,X]}\), \(0<X\le1\), is dense in \(L^2(0,1)\).  For

\[
F_\varepsilon(u)=u^{-1/2}{\bf1}_{[\varepsilon,1]}(u),
\tag{2.10}
\]
one has \(\|F_\varepsilon\|_2^2=\log(1/\varepsilon)\).  Setting \(u=e^{-x}\), \(v=e^{-y}\) turns the normalized Carleman quadratic form into

\[
\frac1L
\int_0^L\!\!\int_0^L
\frac{dx\,dy}{2\cosh((x-y)/2)},
\qquad L=\log(1/\varepsilon),
\tag{2.11}
\]
which tends to

\[
\int_{-\infty}^{\infty}\frac{dz}{2\cosh(z/2)}=\pi.
\tag{2.12}
\]

So no smaller universal Loewner constant is available for the unrestricted scalar Shannon kernel.  The gain here is not a scalar pointwise estimate; it is the exact threshold-feature factorization.

---

## 3. Exact feature-level identity for the authentic compiler

The theorem can be read directly at the source-feature level.

For any signed coefficient family \(\beta_r\) and amplitudes \(X_r\in[0,1]\), define

\[
F_\beta(u)=\sum_r\beta_r{\bf1}_{\{u\le X_r\}}.
\tag{3.1}
\]

Then

\[
\sum_r\beta_r e^{-tX_r}
=
\sum_r\beta_r
-t\int_0^\infty e^{-tu}F_\beta(u)\,du.
\tag{3.2}
\]

Whenever \(\sum_r\beta_r=0\), as in every authentic terminal difference used here,

\[
\boxed{
\frac1t\sum_r\beta_r e^{-tX_r}
=
-\int_0^\infty e^{-tu}F_\beta(u)\,du.
}
\tag{3.3}
\]

Thus the Laplace/Shannon feature is literally the Laplace transform of the Brownian threshold feature.  The only analytic cost in passing from the threshold \(L^2(du)\) bank to the Laplace \(L^2(dt)\) bank is the Carleman norm \(\pi\).

For the compiler, take the doubled signed list
\[
(\beta,X)
=
\{(+\alpha_r,U_r^2),(-\alpha_r,V_r^2)\}_r.
\tag{3.4}
\]
Its total coefficient is zero automatically.  Equation (3.3) inserted into (0.1)-(0.2) yields exactly

\[
\boxed{
\mathcal Q_{\mathsf S}(h)
\le \frac{\pi}{\ln2}\mathcal Q_{\mathsf M}(h)
}
\tag{3.5}
\]
for every authentic syndrome twist \(h\), with the terminal signs untouched.

The same argument applies after the B16 terminal-shell projector and same-syndrome aggregation: if

\[
F_R(u)=
\sum_{\substack{A\in C_0\setminus D_d\\
f_A=-1,\ R_A=R}}
\lambda_{|A|}^{\rm th}(u),
\tag{3.6}
\]
then the radial Laplace sum is

\[
\sum_A\lambda_{|A|}^{\rm Lap}(t)
=
-t\int_0^1 e^{-tu}F_R(u)\,du,
\tag{3.7}
\]
and the Carleman estimate acts **after** the same-syndrome signed sum.  This is precisely the order of operations required by the one-point obstruction in the preceding B16 report.

---

## 4. PROVED — the complete scalar restriction kernel contracts to Brownian threshold

The consumed fleet02/B18 theorem gives

\[
\mathsf P\preceq\frac2{\ln2}\mathsf M.
\tag{4.1}
\]

Adding (2.2) and (4.1),

### Corollary 4.1 — `P03-B16-FULL-RESTRICTION-TO-BROWNIAN`

\[
\boxed{
\mathsf G=\mathsf S+\mathsf P
\preceq
\frac{\pi+2}{\ln2}\mathsf M.
}
\tag{4.2}
\]

Numerically,

\[
\frac{\pi}{\ln2}=4.532360141827\ldots,
\qquad
\frac{\pi+2}{\ln2}=7.417750223605\ldots.
\tag{4.3}
\]

This is a quadratic-form statement, not a scalar comparison.  It may therefore be inserted into the signed terminal MMD without replacing the terminal measure by total variation.

---

## 5. Compiler consequence — two open source banks collapse to one

The consumed exact polarization identity is

\[
\int_0^\infty\frac{R_h(s)^2}{s^3}\,ds
=
N^2\ln2\,[\mathcal Q_{\mathsf S}(h)+\mathcal Q_{\mathsf P}(h)].
\tag{5.1}
\]

Using (3.5) and the already-proved phase contraction,

\[
\boxed{
\int_0^\infty\frac{R_h(s)^2}{s^3}\,ds
\le
N^2(\pi+2)\,\mathcal Q_{\mathsf M}(h).
}
\tag{5.2}
\]

Hence the live-window current estimates of the same source improve to

\[
\boxed{
\int_W\frac{\mathcal E_{\rm cur}(s)}{s^3}\,ds
\le
\frac{\pi+2}{9}\,
N^2\,\mathbb E_S\mathcal Q_{\mathsf M}(g_S),
}
\tag{5.3}
\]
and

\[
\boxed{
\int_W\frac{\mathcal E_{\rm cen}(s)}{s^3}\,ds
\le
\frac{11(\pi+2)}{1152}\,
N^2\,\mathbb E_S\mathcal Q_{\mathsf M}(g_S).
}
\tag{5.4}
\]

The numerical prefactors are

\[
\frac{\pi+2}{9}=0.571288072621\ldots,
\qquad
\frac{11(\pi+2)}{1152}=0.049095068741\ldots.
\tag{5.5}
\]

Therefore the previous pair of source obligations

\[
N^2\mathbb E\mathcal Q_{\mathsf M}=O(J),
\qquad
N^2\ln2\,\mathbb E\mathcal Q_{\mathsf S}=O(J)
\tag{5.6}
\]
has become the **single** implication

\[
\boxed{
N^2\,\mathbb E_S\mathcal Q_{\mathsf M}(g_S)
\le C_M J(f).
}
\tag{5.7}
\]

No R16, negative-entropy, terminal, or valuation credit is required to dominate the Shannon bank once (5.7) is available.  Those ledgers remain untouched for other compiler terms.

This is not full FEI: (5.7) is still open.

---

## 6. Compatibility with the physical-sink handoff

The second cross-account artifact consumed is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260921T195855Z-parent-signed-pivotization/REPORT.md`

(blob `e0ad48a8bb791b0536f5ceda92e3738cc378990a`).

That report proves that **once** a positive parent-indexed physical pair measure is available with the authentic parent masses, every one-subcube parent pair pivots exactly into the signed physical derivative-curvature sink and costs at most its parent mass times \(J(g_j)\).

The present theorem does not manufacture that positive pair measure.  Its effect is different and complementary: it proves that **all** square-first logarithmic/Shannon source cost can be postponed until the same Brownian threshold bank that the physical-sink workers are already targeting.  There is now no second source geometry to match.

Thus the current exact interface-C frontier is:

\[
\boxed{
\text{authentic terminal/syndrome source}
\longrightarrow
\mathcal Q_{\mathsf M}
\longrightarrow
\text{actual parent-indexed physical pair/flag bank}
\longrightarrow
J(f).
}
\tag{6.1}
\]

Only the middle arrow remains universally unpaid on this chain.

---

## 7. Decisive self-check

`check_shannon_carleman.py` performs deterministic numerical falsification checks:

- 961 scalar feature identities;
- 36 logarithmic/random Gram matrices for \(\pi\mathsf M-(\ln2)\mathsf S\succeq0\);
- 40 independent Gram matrices for \((\pi+2)\mathsf M-(\ln2)(\mathsf S+\mathsf P)\succeq0\), using the consumed phase kernel formula;
- logarithmic approximations to the sharp Carleman ratio.

The committed output is `verification.txt`.  These computations are not used as proof; Theorem 2.1 is analytic.

---

## 8. Classification and next recipient

**PROVED HERE:** the sharp scalar-kernel Loewner contraction
\[
\mathsf S\preceq(\pi/\ln2)\mathsf M,
\]
the exact feature-factorization through the Laplace transform, the combined contraction
\[
\mathsf G\preceq((\pi+2)/\ln2)\mathsf M,
\]
and the one-bank compiler bounds (5.2)-(5.4).

**CONSUMED AND USED:** fleet02/B18's exact square-first Shannon/phase polarization and phase-to-Brownian Loewner contraction; current B16 terminal-shell/same-syndrome radial source representation; fleet03/B18's exact parent-pair-to-signed-pivot theorem.

**OPEN:** the authentic Brownian threshold bank contraction (5.7), its no-reuse integration with the actual parent/current representation, the other compiler ledgers, and full FEI.

**REFUTED/NOT REOPENED:** coefficientwise absolute/diagonal payment, postcompression codimension-blind positive parent inversion, sign-free global profile relaxations, and replacement of the terminal signed measure by total variation.

**Next recipient:** fleet03/B18 and fleet02/B16/B18.  They should now treat (5.7) as the only square-first source bank: construct the authentic Brownian-threshold-to-physical-pair/flag map while preserving the terminal energy-distance negative credits and the exact parent masses.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
