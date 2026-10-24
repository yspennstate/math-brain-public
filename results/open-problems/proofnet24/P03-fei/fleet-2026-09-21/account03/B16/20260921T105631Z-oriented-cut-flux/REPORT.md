# B16 FEI signed transport: oriented cut flux and a fractional resolvent bank

**Date:** 21 September 2026  
**Scope:** account03 / B16, `FEI signed transport proof`  
**Status of full FEI:** **OPEN / NOT PROVED**  
**Brain label:** **WITHOUT_VERIFIED_BRAIN**. No authenticated mathematical/cognitive-brain retrieval or receiver-context use occurred in this run.  
**Novelty:** no publication-priority claim is made.

## 0. Entering proof state and route change

This run first read the owner-required `TASKS_2026-09-21.md`, then the complete read-once `REPORT.md`, then `APPROACHES.md`. It also recovered the preceding account03 B16 T-join normal form and the newer account01 B16 signed noise-square payment.

The inherited exact compiler obligation remains, in nats and after the one legitimate minimizing-character gauge,

\[
H_{\rm nat}(f)=\kappa_2J(f)-\mathcal B_d+\mathcal Q_{d,<2}+R_d(f),
\qquad \mathcal B_d\ge0,
\]

with the R32 signed relation representation retained exactly: `0 mod 4` frustrated relations are debits, `2 mod 4` relations are genuine negative credits, the dual-code multiplicities are not collapsed, and the R16 odd moment terms remain refunds rather than errors. The terminal band is separately paid; it is not re-used below.

The previous account03 B16 run proved a sign-preserving T-join disintegration of the R32 relation sum and reduced one possible closure to a signed congestion theorem on the actual disagreement quotient. The newer account01 B16 run changed representation and proved, for

\[
g_\rho=T_\rho f,\qquad
C_U(\rho)=\widehat{g_\rho^2}(U),
\]

the dimension-free signed square bank

\[
\sum_{U\ne\varnothing}C_U(\rho)^2
\le (1-\rho^2)I(f)
\tag{0.1}
\]

and its integrated Hardy form, together with the exact Boolean tail factorization
\(C_U(\rho)=\rho^{|U|}(1-\rho^2)R_U(\rho^2)\). It also proved that an `L1` absolute-correlation lift is exponentially false.

This run does **not** repeat either route. It asks whether the noise-square bank can pay *actual oriented physical cut transport*, and whether it can carry some resolvent-size geometry without paying dimension.

The answer is partially positive:

1. there is an exact dimension-free integrated signed flux across the actual disagreement cut, paid by one copy of influence;
2. there is a continuum of fractional resolvent banks carrying up to one full coordinate derivative of the noisy square;
3. a tempting stronger coordinatewise endpoint-singular payment is false, with an explicit Boolean family and exact asymptotics.

The missing step is still the compiler representation from the R32/T-join signed debit into the new paid flux/bank. Therefore full FEI remains **OPEN**.

---

## 1. Notation

Use normalized Walsh coefficients
\[
a_S=\widehat f(S),\qquad \sum_S a_S^2=1.
\]

For a real function \(h\) on the cube define the flip derivative
\[
D_i h(x)=\frac{h(x)-h(x^{\oplus i})}{2}.
\]
Then
\[
\widehat{D_i h}(S)=1_{\{i\in S\}}\widehat h(S),
\qquad
\|D_i h\|_2^2=\sum_{S\ni i}\widehat h(S)^2.
\]

For Boolean \(f\),
\[
\|D_i f\|_2^2=\operatorname{Inf}_i(f),
\qquad
I(f)=\sum_i\operatorname{Inf}_i(f).
\tag{1.1}
\]

Let
\[
g_\rho=T_\rho f,\qquad 0\le\rho\le1,
\]
so
\[
\widehat g_\rho(S)=\rho^{|S|}a_S.
\]
Set
\[
C_U(\rho)=\widehat{g_\rho^2}(U).
\tag{1.2}
\]

For a nonnegative coordinate tax \(\lambda=(\lambda_1,\ldots,\lambda_n)\), put
\[
\Lambda(U)=\sum_{i\in U}\lambda_i,\qquad
I_\lambda(f)=\sum_i\lambda_i\operatorname{Inf}_i(f)
=\sum_S\Lambda(S)a_S^2.
\tag{1.3}
\]

---

## 2. `P03-B16-NOISE-SQUARE-GRADIENT-16` — **PROVED**

### Theorem 2.1

For every Boolean \(f\), every \(0\le\rho\le1\), and every nonnegative coordinate tax \(\lambda\),

\[
\boxed{
\sum_{U\ne\varnothing}\Lambda(U)C_U(\rho)^2
\le 4\rho^2 I_\lambda(f).
}
\tag{2.1}
\]

In particular, for \(\lambda_i=1\),

\[
\boxed{
\sum_{U\ne\varnothing}|U|C_U(\rho)^2
\le 4\rho^2I(f).
}
\tag{2.2}
\]

### Proof

Parseval and the derivative multiplier give

\[
\sum_U\Lambda(U)C_U(\rho)^2
=\sum_i\lambda_i\|D_i(g_\rho^2)\|_2^2.
\tag{2.3}
\]

Pointwise,
\[
D_i(g_\rho^2)
=(g_\rho+g_\rho^{\oplus i})D_i g_\rho.
\tag{2.4}
\]
Because \(T_\rho\) is an averaging operator applied to a \(\{-1,1\}\)-valued function,
\[
|g_\rho|\le1,
\]
hence
\[
|g_\rho+g_\rho^{\oplus i}|\le2
\]
and therefore
\[
\|D_i(g_\rho^2)\|_2^2
\le4\|D_i g_\rho\|_2^2.
\tag{2.5}
\]

The derivative commutes with noise:
\[
D_i g_\rho=T_\rho D_i f.
\]
Every Fourier coefficient of \(D_i f\) contains \(i\), so
\[
\|D_i g_\rho\|_2^2
=\sum_{S\ni i}\rho^{2|S|}a_S^2
\le\rho^2\sum_{S\ni i}a_S^2
=\rho^2\operatorname{Inf}_i(f).
\tag{2.6}
\]

Multiply (2.5) by \(\lambda_i\), sum \(i\), and use (2.6). `□`

### Why this is useful

The inherited bank (0.1) controls the **amount** of nonconstant noisy-square correlation. The new estimate controls one full derivative of that field while retaining the original coordinate directions. It is not a shell count or a Hamming-path surrogate.

---

## 3. `P03-B16-FRACTIONAL-RESOLVENT-BANK-17` — **PROVED**

### Theorem 3.1

For every \(0\le\theta\le1\),

\[
\boxed{
\int_0^1
\frac{
\sum_{U\ne\varnothing}\Lambda(U)^\theta C_U(\rho)^2
}{
(1-\rho^2)^{1-\theta}
}\,d\rho
\le
\frac{4^\theta}{2\theta+1}\,
I(f)^{1-\theta}I_\lambda(f)^\theta.
}
\tag{3.1}
\]

For the unweighted coordinate tax \(\lambda_i=1\),

\[
\boxed{
\int_0^1
\frac{
\sum_{U\ne\varnothing}|U|^\theta C_U(\rho)^2
}{
(1-\rho^2)^{1-\theta}
}\,d\rho
\le
\frac{4^\theta}{2\theta+1}I(f).
}
\tag{3.2}
\]

The midpoint \(\theta=1/2\) has constant exactly one:

\[
\boxed{
\int_0^1
\frac{\sum_{U\ne\varnothing}\sqrt{|U|}\,C_U(\rho)^2}
{\sqrt{1-\rho^2}}\,d\rho
\le I(f).
}
\tag{3.3}
\]

At \(\theta=1\),

\[
\boxed{
\int_0^1\sum_{U\ne\varnothing}|U|C_U(\rho)^2\,d\rho
\le \frac43 I(f).
}
\tag{3.4}
\]

### Proof

Let
\[
A_0(\rho)=\sum_{U\ne\varnothing}C_U(\rho)^2,
\qquad
A_{1,\lambda}(\rho)=\sum_{U\ne\varnothing}\Lambda(U)C_U(\rho)^2.
\]

The inherited signed square payment gives
\[
A_0(\rho)\le(1-\rho^2)I(f).
\tag{3.5}
\]
Theorem 2.1 gives
\[
A_{1,\lambda}(\rho)\le4\rho^2I_\lambda(f).
\tag{3.6}
\]

Hölder on the finite counting measure over \(U\) gives

\[
\sum_{U\ne\varnothing}\Lambda(U)^\theta C_U^2
=
\sum_U
(C_U^2)^{1-\theta}
(\Lambda(U)C_U^2)^\theta
\le
A_0^{1-\theta}A_{1,\lambda}^{\theta}.
\tag{3.7}
\]

Combining (3.5)--(3.7),

\[
\sum_U\Lambda(U)^\theta C_U^2
\le
4^\theta\rho^{2\theta}
(1-\rho^2)^{1-\theta}
I(f)^{1-\theta}I_\lambda(f)^\theta.
\tag{3.8}
\]

Divide by \((1-\rho^2)^{1-\theta}\), integrate, and use
\[
\int_0^1\rho^{2\theta}\,d\rho=\frac1{2\theta+1}.
\]
`□`

### Signed tail form

The account01 B16 factorization is
\[
C_U(\rho)
=
\rho^{|U|}(1-\rho^2)R_U(\rho^2),
\tag{3.9}
\]
where \(R_U\) is built from signed cumulative Boolean-convolution credits. Substitution into (3.1) gives

\[
\boxed{
\int_0^1
(1-\rho^2)^{1+\theta}
\sum_{U\ne\varnothing}
\Lambda(U)^\theta
\rho^{2|U|}
R_U(\rho^2)^2\,d\rho
\le
\frac{4^\theta}{2\theta+1}
I^{1-\theta}I_\lambda^\theta.
}
\tag{3.10}
\]

Thus the extra coordinate geometry is bought without taking absolute values of the signed moment coefficients inside \(R_U\). Negative cross-moment credits remain inside the Gram square.

This is distinct from the previously killed Fourier-`L1`/square-root comparator: (3.3) is an `L2` signed-correlation bank, not an absolute coefficient comparator.

---

## 4. `P03-B16-ORIENTED-CUT-FLUX-18` — **PROVED**

The live transport problem is physical, so now return to the actual disagreement cut.

Define the oriented cut field
\[
\zeta_i(x):=D_i f(x).
\tag{4.1}
\]
For Boolean \(f\),
\[
\zeta_i(x)=f(x)\eta_i(x),
\qquad
\eta_i(x)=\frac{1-f(x)f(x^{\oplus i})}{2}.
\tag{4.2}
\]
Thus \(\zeta_i\) is zero off the genuine disagreement edges and equals the endpoint sign on a disagreement edge.

Define the signed noisy-square flux
\[
\mathfrak F_f(\rho)
:=
\sum_{i=1}^n
\left\langle D_i f,\,
D_i(g_\rho^2)\right\rangle.
\tag{4.3}
\]

### Theorem 4.1

For every Boolean \(f\),

\[
\boxed{
|\mathfrak F_f(\rho)|
\le2\rho I(f)
\qquad(0\le\rho\le1),
}
\tag{4.4}
\]

and consequently

\[
\boxed{
\int_0^1|\mathfrak F_f(\rho)|\,d\rho
\le I(f).
}
\tag{4.5}
\]

More generally, for measurable edge multipliers \(\psi_i(\rho,x)\),

\[
\boxed{
\left|
\int_0^1
\sum_i
\mathbb E[
\psi_i(\rho,x)\,
D_i f(x)\,
D_i(g_\rho^2)(x)
]\,d\rho
\right|
\le
\sum_i
2\operatorname{Inf}_i(f)
\int_0^1
\rho\,
\|\psi_i(\rho,\cdot)\|_\infty\,d\rho.
}
\tag{4.6}
\]

In particular, if
\[
\sup_i
\int_0^1 2\rho\|\psi_i(\rho,\cdot)\|_\infty\,d\rho
\le L,
\tag{4.7}
\]
then the whole signed transport is at most \(L I(f)\).

### Proof

By Cauchy-Schwarz, (2.5), and (2.6),

\[
\begin{aligned}
\left|
\langle D_i f,D_i(g_\rho^2)\rangle
\right|
&\le
\|D_i f\|_2
\|D_i(g_\rho^2)\|_2\\
&\le
2\rho\|D_i f\|_2^2\\
&=
2\rho\operatorname{Inf}_i(f).
\end{aligned}
\tag{4.8}
\]

Sum over \(i\) to obtain (4.4), then integrate
\(\int_0^1 2\rho\,d\rho=1\) to get (4.5).

For (4.6), replace \(D_i f\) by \(\psi_iD_i f\) in the first Cauchy-Schwarz step and use
\[
\|\psi_iD_i f\|_2
\le
\|\psi_i\|_\infty
\|D_i f\|_2.
\]
`□`

### Exact physical-edge form

Orient each undirected disagreement edge \(e=\{x,x^{\oplus i}\}\) from the endpoint \(x_+\) with \(f(x_+)=+1\) to the endpoint \(x_-\) with \(f(x_-)=-1\). Counting both cube orientations in the expectation gives

\[
\boxed{
\mathfrak F_f(\rho)
=
\frac1N
\sum_{e\in\mathcal D_f}
\left[
g_\rho(x_+)^2-g_\rho(x_-)^2
\right].
}
\tag{4.9}
\]

So (4.5) is literally an **integrated signed potential-drop payment on the actual influence cut**. Agreement geometry contributes nothing. No path length, truth-table shell absolute value, or positive-part replacement appears.

The spectral form is also exact:

\[
\boxed{
\mathfrak F_f(\rho)
=
\sum_{U\ne\varnothing}
|U|\,a_U C_U(\rho).
}
\tag{4.10}
\]

The field therefore has both a physical-cut realization and a signed Fourier-noise realization.

After the one legitimate minimizing-character gauge \(h=\chi_T f\), the same theorem applies to \(h\) and the right side is exactly \(J(f)\):

\[
\int_0^1|\mathfrak F_h(\rho)|\,d\rho
\le J(f).
\tag{4.11}
\]

---

## 5. A concrete R32 compiler criterion — **CONDITIONAL**

Theorem 4.1 gives a paid sink. It does **not** yet identify the exact R32/T-join debit with that sink.

A sufficient next statement is now precise.

### Criterion 5.1

At a paid compiler prefix, suppose the still-unpaid signed quantity \(D_d\) can be decomposed, without modifying the existing R16 bank or terminal residual, as

\[
D_d
=
\int_0^1
\sum_i
\mathbb E[
\psi_{d,i}(\rho,x)\,
D_i h(x)\,
D_i((T_\rho h)^2)(x)
]\,d\rho
+
E_d,
\tag{5.1}
\]

where \(h\) is the minimizing-character gauge, the decomposition preserves the exact R32 signs/multiplicities, and

\[
\sup_i
\int_0^1
2\rho\|\psi_{d,i}(\rho,\cdot)\|_\infty\,d\rho
\le L,
\qquad
E_d\le L'J(f).
\tag{5.2}
\]

Then

\[
\boxed{
D_d\le(L+L')J(f).
}
\tag{5.3}
\]

Together with the already retained compiler and terminal payment, this yields FEI with a dimension-independent constant.

**Status:** **CONDITIONAL / OPEN.** No representation (5.1) is asserted here.

This criterion is more geometric than the previous scalar-noise dual-energy criterion: \(\psi\) may depend on the physical edge location, while \(D_i h\) forces the source to live on the genuine disagreement cut. The remaining task is to compile the normalized alternating T-join transport into bounded noisy-square potential-drop multipliers, while leaving `2 mod 4` negative credits and R16 odd moments signed.

---

## 6. The weighted `L2` dual criterion — **PROVED as a sufficient estimate**

For comparison, Theorem 3.1 yields a second bridge target. If

\[
D(f)=
\int_0^1
\sum_{U\ne\varnothing}
\Phi_U(\rho)C_U(\rho)\,d\rho,
\tag{6.1}
\]

then weighted Cauchy-Schwarz and (3.2) give, for \(0\le\theta\le1\),

\[
|D(f)|^2
\le
\frac{4^\theta}{2\theta+1}I(f)
\cdot
\int_0^1
(1-\rho^2)^{1-\theta}
\sum_{U\ne\varnothing}
|U|^{-\theta}\Phi_U(\rho)^2\,d\rho.
\tag{6.2}
\]

At \(\theta=1/2\) the bank constant is one:

\[
|D(f)|^2
\le
I(f)
\int_0^1
\sqrt{1-\rho^2}
\sum_{U\ne\varnothing}
\frac{\Phi_U(\rho)^2}{\sqrt{|U|}}\,d\rho.
\tag{6.3}
\]

Thus compared with the earlier \(\theta=0\) source norm, high spatial frequencies receive an inverse resolvent discount. This is potentially useful for the long-T-join obstruction, but the exact R32-to-\(\Phi\) map remains **OPEN**.

---

## 7. A tempting stronger local payment is false

The physical flux theorem might suggest trying to pay each coordinate separately with the endpoint factor from (0.1):

\[
\sum_{U\ni i}C_U(\rho)^2
\stackrel{?}{\le}
C(1-\rho^2)\operatorname{Inf}_i(f)
\tag{7.1}
\]

for a universal \(C\), or even the integrated critical form

\[
\int_0^1
\frac{\sum_{U\ni i}C_U(\rho)^2}{1-\rho^2}\,d\rho
\stackrel{?}{\le}
C\operatorname{Inf}_i(f).
\tag{7.2}
\]

Both are false.

### `P03-B16-PARITY-SWITCH-LOCAL-OBSTRUCTION-19` — **REFUTED**

Let \(m\ge1\), let \(y\in\{-1,1\}^m\), \(z\in\{-1,1\}\), and put

\[
\chi(y)=\prod_{j=1}^m y_j,
\qquad
A(y)=\frac{1+\chi(y)}2,
\qquad
B(y)=\frac{1-\chi(y)}2.
\]

Define the Boolean function

\[
f_m(y,z)=A(y)+zB(y).
\tag{7.3}
\]

Thus \(f_m(y,+1)=1\) and \(f_m(y,-1)=\chi(y)\). For the distinguished coordinate \(z\),

\[
\operatorname{Inf}_z(f_m)=\mathbb E B^2=\frac12.
\tag{7.4}
\]

Noise gives

\[
g_\rho(y,z)
=
\frac{1+\rho^m\chi(y)}2
+
\rho z\frac{1-\rho^m\chi(y)}2.
\tag{7.5}
\]

Therefore

\[
D_z(g_\rho^2)
=
\frac{\rho z}{2}(1-\rho^{2m}),
\tag{7.6}
\]

so Parseval gives the exact coordinate energy

\[
\boxed{
\sum_{U\ni z}C_U(\rho)^2
=
\frac{\rho^2}{4}(1-\rho^{2m})^2.
}
\tag{7.7}
\]

Choose \(\rho_m=1-1/m\). Then the ratio in (7.1) is

\[
\frac{
\sum_{U\ni z}C_U(\rho_m)^2
}{
(1-\rho_m^2)\operatorname{Inf}_z(f_m)
}
=
\frac{
\rho_m^2(1-\rho_m^{2m})^2
}{
2(1-\rho_m^2)
}
\sim
\frac{(1-e^{-2})^2}{4}\,m.
\tag{7.8}
\]

The asymptotic coefficient is

\[
\frac{(1-e^{-2})^2}{4}
=
0.1869112681\ldots
\tag{7.9}
\]

so no universal \(C\) can satisfy (7.1).

For the integrated form,

\[
\begin{aligned}
K_m
&:=
\int_0^1
\frac{\sum_{U\ni z}C_U(\rho)^2}{1-\rho^2}\,d\rho\\
&=
\frac14
\sum_{j=0}^{m-1}
\left(
\frac1{2j+3}
-
\frac1{2(j+m)+3}
\right),
\end{aligned}
\tag{7.10}
\]

hence

\[
\boxed{
\frac{K_m}{\operatorname{Inf}_z(f_m)}
=
\frac12
\sum_{j=0}^{m-1}
\left(
\frac1{2j+3}
-
\frac1{2(j+m)+3}
\right)
=
\frac14\log m+O(1).
}
\tag{7.11}
\]

So (7.2) also fails.

### Meaning of the obstruction

A single coordinate can have a cut indicator whose spatial complexity lives on a parity of all the other variables. The endpoint cancellation of the noisy square can therefore require cross-coordinate resources. A proof that taxes each physical direction only by its own \(\operatorname{Inf}_i\) at the critical endpoint singularity is impossible.

This does **not** kill Theorems 3.1 or 4.1. The fractional bank correctly pools global and taxed influence, and the oriented flux bound uses no singular \(1/(1-\rho^2)\) factor.

---

## 8. Calculation / attempted refutation

Companion code in this run checks the new identities and deliberately exercises the refuted local route.

It evaluates:

- every Boolean function through dimension three;
- deterministic random Boolean functions in dimensions four through six;
- six noise values per function;
- the gradient bank, oriented-cut physical/Fourier flux equality, flux payment, and fractional pointwise interpolation;
- the exact parity-switch obstruction for \(m=8,16,32,64,128,256\).

The executed check covered **2,376 function/noise cases**. Observed maxima in that sample were

\[
\max \frac{A_1}{4\rho^2 I}=0.13997206265625003,
\qquad
\max \frac{|\mathfrak F|}{2\rho I}=0.24749999999999994.
\]

For the refuted coordinatewise endpoint payment, at
\(\rho=1-1/m\) the exact ratios were

| \(m\) | pointwise ratio (7.8) | critical integral / \(\operatorname{Inf}_z\) |
|---:|---:|---:|
| 8 | 1.2704159162 | 0.3814070866 |
| 16 | 2.7671291985 | 0.5334197684 |
| 32 | 5.7584871050 | 0.6955511320 |
| 64 | 11.7400512633 | 0.8631223452 |
| 128 | 23.7025777027 | 1.0335157817 |
| 256 | 47.6273235090 | 1.2053468635 |

The finite calculations are falsification/sanity checks only; the all-dimensional positive and negative statements above have direct proofs.

---

## 9. What changed in the proof state

### PROVED

1. The noisy-square field has a direction-weighted gradient bank:
   \[
   \sum_U\Lambda(U)C_U^2\le4\rho^2I_\lambda.
   \]
2. Interpolating this with the inherited signed square bank yields a dimension-free fractional resolvent family (3.1), including the exact-constant midpoint (3.3).
3. The actual oriented disagreement cut carries an integrated signed noisy-square potential-drop flux costing at most one copy of influence:
   \[
   \int_0^1|\mathfrak F_f(\rho)|\,d\rho\le I(f).
   \]
4. The same payment survives bounded edge-local multipliers via (4.6).
5. After the minimizing-character gauge all these right sides become the appropriate gauged influence, in particular \(J(f)\) for the unweighted statements.

### REFUTED

A coordinatewise attempt to add the critical endpoint factor,
\[
\sum_{U\ni i}C_U^2\lesssim(1-\rho^2)\operatorname{Inf}_i,
\]
and its \(1/(1-\rho^2)\)-integrated version are false. The parity-switch family gives respectively linear and logarithmic divergence.

### OPEN / CONDITIONAL

The exact compiler bridge from the R32/T-join signed relation debit to either the oriented cut flux (5.1) or the weighted `L2` source form (6.1) is not proved. No universal FEI constant is claimed.

---

## 10. Next attack

Do **not** re-run the finite checks.

The next B16 target is to return to the **unsymmetrized alternating T-join telescope** before its `1/d_A` barycenter is collapsed. Each disagreement crossing already carries an orientation sign. Test whether, after the R32 Borel radial integral is inserted but before absolute values, the routed debit can be written as a bounded superposition of the physical potential drops

\[
D_i\big((T_\rho h)^2\big)
\]

against the oriented cut source \(D_i h\).

The exact target is a representation of form (5.1) with

\[
\sup_i\int_0^1 2\rho\|\psi_{d,i}(\rho,\cdot)\|_\infty\,d\rho=O(1),
\]

while leaving the R16 odd collision-order refunds and the `2 mod 4` R32 credits signed and keeping the terminal-band payment separate.

If the spatial multiplier must grow, pivot to the fractional source norm (6.2), where high spatial frequencies receive the inverse factor \(|U|^{-\theta}\). The parity-switch obstruction says not to demand a critical coordinatewise endpoint payment again.

**Full FEI remains OPEN / NOT PROVED.**
