# B16 FEI signed transport — central Hardy frequency localization

**Date:** 21 September 2026  
**Scope:** `account01 / B16`, FEI signed transport/noise interpolation (APPROACH 10/13)  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** a new exact Hardy-resolved source identity, two dimension-free payment criteria (one sharp), and a rigorous localization of the inherited raw ordered-min low-mode obstruction. No publication-priority claim.

## 0. Entering state and why this is a new step

This run follows the current owner order `FEI-SEVEN-TASKS-2026-09-21`; it does not audit or rerun the settled read-once certificate.

The compatible signed-transport chain entering this run contains three exact pieces.

1. For a physical coordinate `i`, with cut
   \[
   \eta_i(x)=\frac{1-f(x)f(x^{\oplus i})}{2},\qquad
   a_i(U)=\widehat{\eta_i}(U)^2,\qquad
   E_i=\sum_{U\ne0}a_i(U)=\alpha_i(1-\alpha_i),
   \]
   the central Bernoulli prefix/suffix antisymmetry is
   \[
   \delta_i(t)=-4\sum_{\substack{U\ne0\\ |U|\ {\rm odd}}}a_i(U)t^{|U|},
   \qquad 0\le t\le\frac12.
   \]
   The preceding account01 report proved
   \[
   \int_0^{1/2}t\left(\frac12-t\right)\delta_i(t)^2dt
   \le \frac{E_i^2}{40},
   \]
   and after the minimizing-character fold the aggregate source square is at most `J/270`.

2. The account04 central Hardy/Ward identity writes the actual low radial bank using the one-dimensional operator
   \[
   (\mathcal R A)(t):=\frac1t\int_0^t sA(s)\,ds:
   \qquad
   \mathcal L_-=\frac{N^2}{1024}\sum_v\int_0^{1/2}(\mathcal R A_v(t))^2dt.
   \]
   The previous estimate bounded this by a weighted derivative square. That is safe, but it discards some of the exact degree damping in `R`.

3. The inherited raw random-order ordered-min entropy displacement multiplier is
   \[
   A^{\rm raw}_{n,r}
   =\frac1n\sum_{c=2}^nH_c
   \left[
      2^{c-1}
      \frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}
      -1
   \right].
   \]
   At every fixed low `r` it grows like `4n/((r+1)(r+2))`, so a bounded-multiplier argument is impossible before the Shapley/plaquette/terminal/R16 refunds are inserted.

The new point is that the *exact Hardy resolvent* tolerates exponentially more growth at high Fourier degree than the previous bounded-multiplier criterion. Therefore the refund calculation does not need uniform control of the entire odd spectrum. The real universal obligation can be localized to the low odd modes.

---

## 1. Exact Hardy-resolved physical-cut source

Fix a physical coordinate `i`. Let `kappa_U` be arbitrary real coefficients indexed by the nonzero odd cut frequencies. Define the signed central source
\[
A_i^\kappa(t)
:=-4\sum_{\substack{U\ne0\\ |U|\ {\rm odd}}}
a_i(U)\kappa_U t^{|U|}.
\tag{1.1}
\]
No sign is removed inside the sum.

### Theorem 1.1 — `B16-CENTRAL-HARDY-GRAM-IDENTITY`

Put `r=|U|`, `s=|V|`. Then
\[
\boxed{
(\mathcal R A_i^\kappa)(t)
=
-4\sum_{\substack{U\ne0\\ |U|\ {\rm odd}}}
a_i(U)\frac{\kappa_U}{|U|+2}t^{|U|+1}.
}
\tag{1.2}
\]
Consequently
\[
\boxed{
\begin{aligned}
\mathcal Q_i(\kappa)
&:=\int_0^{1/2}(\mathcal R A_i^\kappa(t))^2dt\\
&=
16\sum_{\substack{U,V\ne0\\ |U|,|V|\ {\rm odd}}}
a_i(U)a_i(V)\kappa_U\kappa_V
\frac{2^{-(r+s+3)}}
{(r+2)(s+2)(r+s+3)}.
\end{aligned}
}
\tag{1.3}
\]

#### Proof

Integrating one monomial gives
\[
\frac1t\int_0^t s\,s^r ds=\frac{t^{r+1}}{r+2},
\]
which proves (1.2). Expanding the square and using
\[
\int_0^{1/2}t^{r+s+2}dt
=\frac{2^{-(r+s+3)}}{r+s+3}
\]
gives (1.3). `square`

This is the exact central-band Hilbert/Gram form seen by the low Hardy bank. Its kernel is positive because it is literally the Gram matrix of the monomials
\[
4\,t^{r+1}/(r+2)
\]
in `L2([0,1/2])`.

---

## 2. A sharp bounded-multiplier payment: `E_i^2/90`

The exact Hardy resolvent improves the preceding derivative-square estimate even before using any compiler structure.

### Theorem 2.1 — `B16-CENTRAL-HARDY-BOUNDED-PAYMENT`

If
\[
|\kappa_U|\le M
\qquad\text{for every nonzero odd }U,
\tag{2.1}
\]
then
\[
\boxed{
\mathcal Q_i(\kappa)\le\frac{M^2}{90}E_i^2.
}
\tag{2.2}
\]
The constant `1/90` is sharp over Boolean cuts and multipliers satisfying (2.1).

#### Proof

For odd `r,s>=1`, the absolute coefficient in (1.3) is
\[
K_{r,s}
=
16\frac{2^{-(r+s+3)}}
{(r+2)(s+2)(r+s+3)}.
\]
Every factor decreases when either `r` or `s` increases. Hence
\[
K_{r,s}\le K_{1,1}
=\frac1{90}.
\]
Using `a_i(U)>=0` and (2.1),
\[
\mathcal Q_i(\kappa)
\le\frac{M^2}{90}\left(\sum_{U\ne0}a_i(U)\right)^2
=\frac{M^2}{90}E_i^2.
\]
For the one-bit affine cut,
\[
\eta(x)=\frac{1-\chi_{\{1\}}(x)}2,
\]
all nonconstant cut energy is at `r=1`; choosing `kappa=M` gives equality. `square`

After the minimizing-character gauge, write
\[
\beta_i=\min\{\alpha_i,1-\alpha_i\},\qquad
J(f)=\sum_i\beta_i.
\]
Since
\[
E_i=\beta_i(1-\beta_i),\qquad
E_i^2\le\frac4{27}\beta_i,
\tag{2.3}
\]
Theorem 2.1 yields the aggregate payment
\[
\boxed{
\sum_i\mathcal Q_i(\kappa)
\le \frac{2M^2}{1215}J(f).
}
\tag{2.4}
\]

For `M=1`, `2/1215=0.00164609...`, whereas applying the preceding weighted-Hardy inequality to the `J/270` central square gives `1/540=0.00185185...`. The improvement is modest numerically but conceptually important: the exact resolvent exposes the true degree denominator.

---

## 3. The important new relaxation: exponential high-degree tolerance

A uniform multiplier bound is still much stronger than the low Hardy bank actually needs.

Define the Hardy-adapted multiplier norm
\[
\boxed{
\|\kappa\|_{\rm H}
:=
\sup_{\substack{U\ne0\\|U|\ {\rm odd}}}
\frac{|\kappa_U|}
{(|U|+2)2^{|U|-1}}.
}
\tag{3.1}
\]

### Theorem 3.1 — `B16-CENTRAL-HARDY-EXPONENTIAL-TOLERANCE`

For every Boolean cut and every odd multiplier field,
\[
\boxed{
\mathcal Q_i(\kappa)
\le \frac{\|\kappa\|_{\rm H}^2}{10}E_i^2.
}
\tag{3.2}
\]
The scalar constant `1/10` is sharp for the norm (3.1). Consequently
\[
\boxed{
\sum_i\mathcal Q_i(\kappa)
\le\frac{2}{135}\|\kappa\|_{\rm H}^2J(f).
}
\tag{3.3}
\]

#### Proof

Let `M=||kappa||_H`. From (1.2),
\[
\begin{aligned}
|(\mathcal R A_i^\kappa)(t)|
&\le
4M\sum_{U\ {\rm odd}}a_i(U)
2^{|U|-1}t^{|U|+1}\\
&=
4M t^2\sum_{U\ {\rm odd}}a_i(U)(2t)^{|U|-1}.
\end{aligned}
\]
On the central band `0<=t<=1/2` and for every odd `|U|>=1`,
\[
(2t)^{|U|-1}\le1.
\]
Therefore
\[
|(\mathcal R A_i^\kappa)(t)|
\le4M E_i t^2.
\]
Squaring and integrating,
\[
\mathcal Q_i(\kappa)
\le16M^2E_i^2\int_0^{1/2}t^4dt
=\frac{M^2}{10}E_i^2.
\]
The aggregate estimate follows from (2.3).

Sharpness of `1/10` in this norm again occurs on the one-bit affine cut: at `r=1`, the denominator in (3.1) is `3`, so taking `kappa=3M` makes every displayed inequality an equality. `square`

### Interpretation

The low Hardy channel therefore permits
\[
|\kappa_U|=O\!\left((|U|+2)2^{|U|-1}\right)
\tag{3.4}
\]
with a dimension-independent payment.

This is the main reduction of the run. The preceding central-Radon compiler criterion asked for an `O(1)` odd multiplier envelope. For the *low radial Hardy bank*, that is unnecessarily strong by an exponential factor in Fourier degree.

The only modes for which (3.4) gives little slack are the genuinely low odd modes, especially `r=1,3,5,...`. This is exactly where the inherited raw ordered-min kernel has its ambient-dimensional obstruction.

---

## 4. Rigorous localization of the inherited raw ordered-min obstruction

This section applies the new Hardy norm only to the already-computed **raw entropy displacement multiplier**. It does **not** identify that raw multiplier with the fully refunded compiler multiplier, and it does not spend terminal/R16 credits separately.

For a codimension-`c` affine-subcube defect of density `q=2^{-c}`, the squared Fourier law has empty mass `(1-2q)^2` and equal nonzero masses `4q^2`. Let its spectral entropy in bits be `H_c`. With
\[
\varepsilon=4q(1-q),
\]
\[
H_c=h_2(\varepsilon)+\varepsilon\log_2(2^c-1).
\]
The elementary entropy bound
\[
h_2(x)\le x\log_2(e/x)
\]
gives, for every `c>=2`,
\[
\boxed{
H_c<8c\,2^{-c}.
}
\tag{4.1}
\]
Hence
\[
\boxed{
H_c2^{c-1}<4c,
\qquad
\sum_{c=2}^{\infty}H_c<12.
}
\tag{4.2}
\]

Now use the inherited exact raw multiplier
\[
A^{\rm raw}_{n,r}
=
\frac1n\sum_{c=2}^nH_c
\left[
2^{c-1}
\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}
-1
\right].
\tag{4.3}
\]

### Lemma 4.1 — exact avoidance sum

For `0<=r<=n-1`,
\[
\boxed{
\sum_{c=2}^n
c\,
\frac{\binom{n-1-r}{c-1}}
{\binom{n-1}{c-1}}
=
\frac{(n-1-r)(n+r+2)}
{(r+1)(r+2)}.
}
\tag{4.4}
\]

#### Proof

Put `N=n-1`, `k=c-1` and use
\[
\frac{\binom{N-r}{k}}{\binom Nk}
=
\frac{\binom{N-k}{r}}{\binom Nr}.
\]
After setting `j=N-k`, the numerator becomes
\[
\sum_{j=r}^{N-1}(N-j+1)\binom jr.
\]
Use the hockey-stick identity and
\[
j\binom jr
=
r\binom jr+(r+1)\binom j{r+1}.
\]
Straight simplification gives (4.4). `square`

Combining (4.2)--(4.4) yields a global, not merely fixed-`r`, bound.

### Theorem 4.2 — `B16-RAW-MULTIPLIER-GLOBAL-BOUND`

For every `n>=2` and `0<=r<=n-1`,
\[
\boxed{
|A^{\rm raw}_{n,r}|
\le
\frac{4(n+1)}{(r+1)(r+2)}
+\frac{12}{n}.
}
\tag{4.5}
\]

Indeed the positive part is at most
\[
\frac4n
\frac{(n-1-r)(n+r+2)}{(r+1)(r+2)}
\le
\frac{4(n+1)}{(r+1)(r+2)},
\]
and the constant negative part has absolute value `<12/n`.

### Corollary 4.3 — only a low logarithmic band can carry the raw Hardy obstruction

Fix an odd `R>=1`. For every odd `r>=R`,
\[
\boxed{
\frac{|A^{\rm raw}_{n,r}|}
{(r+2)2^{r-1}}
\le
M_{n,R}
:=
\frac{4(n+1)}
{(R+1)(R+2)^2\,2^{R-1}}
+
\frac{12}
{n(R+2)\,2^{R-1}}.
}
\tag{4.6}
\]

In particular, if `R` is the smallest odd integer with
\[
2^{R-1}\ge n,
\tag{4.7}
\]
then
\[
M_{n,R}=O(R^{-3})+O(n^{-2}R^{-1}).
\tag{4.8}
\]
Since `R=log_2 n+O(1)`, the raw high-frequency tail is not the source of the dimension blow-up in the exact central Hardy norm. The ambient-dimensional obstruction is concentrated below an `O(log n)` odd-frequency band.

This is compatible with, and sharpens the interpretation of, the inherited fixed-low-mode asymptotic
\[
A^{\rm raw}_{n,r}
=\frac{4n}{(r+1)(r+2)}+O_r(1).
\]
For `r=1`, the Hardy norm denominator is only `3`, so the raw singleton multiplier still blows up linearly. The refunds **must** cancel the low modes. But there is no need to demand an `O(1)` bound on the entire high-frequency spectrum: the exact Hardy/central-band geometry already pays multipliers growing almost like `2^r` times a polynomial factor.

---

## 5. Structured-family consequence from the newest monomial handoff

The newest compatible account02/B16 result computes the Shapley-curvature-refunded entropy multiplier for every codimension-`k` monomial defect
\[
f_A(x)=(-1)^{\prod_{j\in A}x_j}.
\]
For a physical pivot `p in A`, every genuine cut frequency satisfies `U subset A\setminus{p}` and
\[
\mathcal M_{n,k,p}(U)=\frac{H_k}{k}(-1)^{|U|}.
\]
Thus on the central odd sector,
\[
|\mathcal M_{n,k,p}(U)|=\frac{H_k}{k}\le1.
\]
Applying Theorem 2.1 gives the new exact-Hardy consequence
\[
\boxed{
\mathcal Q_p(\mathcal M)
\le
\frac1{90}E_p^2,
}
\tag{5.1}
\]
uniformly in the number of appended dummy coordinates.

So the low-Hardy entropy-curvature component is dimension-free on the entire monomial-defect family, not only on the former two-variable parity-switch diagnostic. This does **not** include or double-spend the separately retained terminal/R16/KL ledgers; it is a structured-family closure of the refunded entropy component only.

---

## 6. What remains for full FEI

**Full FEI remains OPEN.**

The useful compiler target is now strictly weaker than the one at the start of the run.

It is no longer necessary to prove
\[
|\kappa_U|=O(1)
\quad\text{for every odd Fourier mode.}
\]
For the low radial Hardy channel it is enough to prove
\[
\boxed{
|\kappa_U|
\le
M(|U|+2)2^{|U|-1}
}
\tag{6.1}
\]
for the **fully refunded** central source multiplier, with `M` dimension-free. Even this pointwise condition is only sufficient; the exact Gram form (1.3) permits additional signed cancellation.

The inherited raw entropy kernel already satisfies the needed scale automatically above an `O(log n)` band. Therefore the next account01/B16 calculation should focus on the finitely many low odd displacement-Walsh modes
\[
r=1,3,\ldots,R_n,
\qquad
2^{R_n-1}\asymp n,
\]
of the **fully combined** Shapley curvature + terminal + retained R16/moment kernel. The first mandatory identity remains the singleton cancellation on the dummy-extended parity-switch family; after that, one should seek a fixed-`r` cancellation formula and only then use Theorem 3.1 to dispose of the high-degree tail.

This avoids the previous over-strong demand of uniform all-frequency multiplier control and preserves every signed credit and terminal ledger.

---

## 7. New checker

`check_central_hardy_localization.py` checks only the new algebra in this report. It does not rerun the read-once certificate or any settled FEI sweep.

It verifies with exact rational arithmetic:

- the avoidance-sum identity (4.4) for every `2<=n<=30` and every admissible `r`;
- the exact Hardy Gram formula (1.3) on 100 deterministic rational synthetic odd-level sources;
- the sharp coefficient maxima
  \[
  \max_{r,s\ {\rm odd}\ge1}K_{r,s}=1/90,
  \]
  and, after the Hardy norm scaling,
  \[
  \max K_{r,s}(r+2)(s+2)2^{r-1}2^{s-1}=1/10
  \]
  over all odd `r,s<=31`, with the maxima at `(1,1)`.

The analytic proofs above establish the results; the checker is falsification evidence.

---

## 8. Before / after

**Before:** the central source theorem required a uniformly bounded odd compiler multiplier, while the inherited raw ordered-min kernel had `Theta(n)` fixed low modes. It was unclear whether all frequencies had to be canceled by refunds.

**After:** the exact low-Hardy Gram identity shows that high Fourier degree has an automatic `1/(r+2)` resolvent and `2^{-r}` central-band damping. A fully refunded multiplier may grow as `O((r+2)2^{r-1})` and still be paid dimension-free. The inherited raw entropy multiplier is rigorously within this scale above an `O(log n)` odd band. Thus the universal cancellation problem has been localized to the low odd modes; full FEI is still open.
