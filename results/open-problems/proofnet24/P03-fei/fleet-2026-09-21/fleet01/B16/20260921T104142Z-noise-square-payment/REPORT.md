# B16 FEI signed transport/noise interpolation: a dimension-free signed square bank and an exponential absolute-value obstruction

**Date:** 21 September 2026  
**Status of full FEI:** **OPEN / NOT PROVED**.  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical/cognitive-brain retrieval was available or used in this derivation.  
**Route:** APPROACH 10/13, noise-semigroup / Boolean-correlation payment, continuing the fleet01 B16 folded T-join note and the fleet03 B16 signed T-join disintegration.  
**Source state:** the required 21 September read-once continuation was read on `master` at `89e9e942cbcaed3b044a3d9147eb5b2ae2e33dbe`; immediately before delivery, `master` had advanced to `43d76b549303e4ce9c275bd90be2600788cbf4b4`. No novelty-priority claim is made.

The preceding fleet01/B16 run proved that a frustrated weight-four affine relation can require `(n-1)/2` genuine disagreement crossings even after the exact coordinate fold, so short T-joins are impossible. It also proved that the normalized `1/d` routing is the barycenter of exact alternating signed telescopes. The fleet03/B16 run independently put the full R32 relation sum into a sign-preserving T-join congestion normal form. This run changes representation: rather than trying to bound the absolute congestion of individual relations, it looks for a **dimension-free signed Hilbert payment already forced by Booleanity**.

The result is a clean semigroup inequality of total cost `I(f)` (or `J(f)` after the legitimate minimizing-character gauge), an exact tail-sum factorization which exposes the cancellation being paid, and a Boolean family proving that the corresponding `L1`/absolute-correlation estimate is exponentially false at the natural noise scale. Thus the new bank is genuinely signed: taking absolute values before payment destroys the correct scale.

---

## 1. Signed noisy-square correlations

Use normalized Walsh coefficients

\[
a_S=\widehat f(S),\qquad \sum_S a_S^2=1,
\]

and let `T_rho` be the ordinary cube noise operator,

\[
g_\rho=T_\rho f,\qquad
\widehat g_\rho(S)=\rho^{|S|}a_S,\qquad 0\le \rho\le 1.
\]

For each Fourier displacement `U`, define the signed convolution correlation

\[
C_U(\rho)
:=\widehat{g_\rho^2}(U)
=\sum_S a_Sa_{S\triangle U}\,
  \rho^{|S|+|S\triangle U|}.
\tag{1.1}
\]

For `U != emptyset`, Booleanity gives the terminal cancellation

\[
C_U(1)=\widehat{f^2}(U)=0.
\tag{1.2}
\]

This is precisely the kind of cancellation that disappears if one replaces the signed sums by absolute values.

Put

\[
Z(\rho):=C_\emptyset(\rho)
=\|T_\rho f\|_2^2
=\sum_S a_S^2\rho^{2|S|}.
\tag{1.3}
\]

---

## 2. `B16-NOISE-SQUARE-SIGNED-PAYMENT-03` — PROVED

### Theorem

For every Boolean `f:{-1,1}^n->{-1,1}` and every `0<=rho<1`,

\[
\boxed{
\sum_{U\ne\emptyset} C_U(\rho)^2
\le Z(\rho)(1-Z(\rho))
\le 1-Z(\rho)
\le (1-\rho^2)I(f).
}
\tag{2.1}
\]

Consequently,

\[
\boxed{
\int_0^1
\frac{\sum_{U\ne\emptyset}C_U(\rho)^2}
     {1-\rho^2}\,d\rho
\le I(f).
}
\tag{2.2}
\]

After multiplying `f` by a minimizing character, Fourier entropy is unchanged and the resulting influence is exactly the repository's `J(f)`. Therefore the gauged version is

\[
\boxed{
\int_0^1
\frac{\sum_{U\ne\emptyset}C^{\,\mathrm{gauge}}_U(\rho)^2}
     {1-\rho^2}\,d\rho
\le J(f).
}
\tag{2.3}
\]

### Proof

Parseval applied to `g_rho^2` gives

\[
\sum_U C_U(\rho)^2
=\|g_\rho^2\|_2^2
=\mathbb E\,g_\rho^4.
\tag{2.4}
\]

The constant Fourier coefficient of `g_rho^2` is `Z(rho)`, so

\[
\sum_{U\ne\emptyset}C_U(\rho)^2
=\mathbb E g_\rho^4-Z(\rho)^2.
\tag{2.5}
\]

Because `f` is Boolean and `T_rho` is an averaging operator,

\[
|g_\rho(x)|\le1
\]

pointwise. Hence `g_rho^4<=g_rho^2`, and therefore

\[
\mathbb E g_\rho^4-Z^2
\le Z-Z^2
=Z(1-Z)
\le1-Z.
\tag{2.6}
\]

Finally,

\[
1-Z(\rho)
=\sum_S a_S^2(1-\rho^{2|S|})
\le(1-\rho^2)\sum_S |S|a_S^2
=(1-\rho^2)I(f),
\tag{2.7}
\]

using `1-x^k<=k(1-x)` for `0<=x<=1`. This proves (2.1). Divide by `1-rho^2` and integrate over `[0,1)` to obtain (2.2). The character-gauged statement follows by applying the same theorem to the gauged Boolean function. `□`

### Interpretation

Equation (2.2) is a literal dimension-free payment inequality. It pays the entire continuum of nonconstant signed noisy-square correlations with one copy of influence. It is not a terminal endpoint estimate and not a finite-shell check. The cancellation `C_U(1)=0` is used before squaring, so opposite-sign terms inside each Boolean convolution constraint remain available.

This does **not** itself close R32. The missing compiler step is to represent the remaining signed R32/T-join debit as a bounded dual functional of the fields `C_U(rho)` without discarding the existing terminal and moment refunds.

---

## 3. Exact parity-frustration tail factorization

The previous theorem has a useful algebraic form that makes the signed cancellation explicit.

For fixed `U != emptyset`, use

\[
|S|+|S\triangle U|
=|U|+2|S\setminus U|.
\tag{3.1}
\]

Define

\[
q_{U,k}
:=
\sum_{S:\,|S\setminus U|=k}
a_Sa_{S\triangle U},
\qquad 0\le k\le n-|U|.
\tag{3.2}
\]

Then

\[
C_U(\rho)
=\rho^{|U|}\sum_k q_{U,k}\rho^{2k}.
\tag{3.3}
\]

Booleanity at `rho=1` says

\[
\sum_kq_{U,k}=0.
\tag{3.4}
\]

Let the signed prefix/tail credits be

\[
B_{U,j}:=\sum_{k=0}^j q_{U,k},
\qquad 0\le j<n-|U|.
\tag{3.5}
\]

Since the full sum is zero, the elementary polynomial identity

\[
\sum_kq_{U,k}x^k
=(1-x)\sum_jB_{U,j}x^j
\tag{3.6}
\]

holds exactly. Therefore

\[
C_U(\rho)
=\rho^{|U|}(1-\rho^2)
  \sum_j B_{U,j}\rho^{2j}.
\tag{3.7}
\]

This is the noise-semigroup analogue of keeping the signed R16/R32 refunds rather than positive-parting them: the terminal cancellation has been converted into a literal factor `1-rho^2`.

---

## 4. `B16-HARDY-TAIL-CREDIT-BANK-04` — PROVED

Substituting (3.7) into (2.2) gives the exact dimension-free quadratic bank

\[
\boxed{
\sum_{U\ne\emptyset}
\int_0^1
\rho^{2|U|}(1-\rho^2)
\left(\sum_jB_{U,j}\rho^{2j}\right)^2\,d\rho
\le I(f).
}
\tag{4.1}
\]

Expanding the square gives a completely explicit signed moment kernel:

\[
\boxed{
\sum_{U\ne\emptyset}
\sum_{j,\ell}
\frac{2B_{U,j}B_{U,\ell}}
{\bigl(2(|U|+j+\ell)+1\bigr)
 \bigl(2(|U|+j+\ell)+3\bigr)}
\le I(f).
}
\tag{4.2}
\]

Indeed,

\[
\int_0^1\rho^{2m}(1-\rho^2)\,d\rho
=
\frac1{2m+1}-\frac1{2m+3}
=
\frac2{(2m+1)(2m+3)}.
\tag{4.3}
\]

The quadratic form in (4.2) is positive semidefinite because it is the Gram form in (4.1), but its individual cross terms retain signs. This is the useful feature: it is a **global signed moment-credit bank** whose total cost is dimension-free.

After the minimizing-character gauge, the right side is `J(f)`.

---

## 5. Why an `L1` lift is impossible: a folded Boolean obstruction

A tempting next step would be to strengthen (2.1) to

\[
\sum_{U\ne\emptyset}|C_U(\rho)|
\stackrel{?}{\le}
C(1-\rho^2)I(f)
\tag{5.1}
\]

with a universal `C`, and then pay relation congestion by triangle inequality. This is false by an exponential factor even for a coordinate-folded Boolean function.

### `B16-ONEPOINT-L1-NOISE-OBSTRUCTION-05` — PROVED

Let `N=2^n` and

\[
f_n(x)=
\begin{cases}
-1,&x=0,\\
+1,&x\ne0.
\end{cases}
\tag{5.2}
\]

Then

\[
\widehat f_n(\emptyset)=1-\frac2N,
\qquad
\widehat f_n(S)=-\frac2N \quad(S\ne\emptyset),
\tag{5.3}
\]

and each coordinate influence is `2/N`. Thus

\[
I(f_n)=J(f_n)=\frac{2n}{N},
\tag{5.4}
\]

for `n>=3`, and the function is already in the folded gauge.

For `U != emptyset` with `r=|U|`, direct factorization of (1.1) gives

\[
\boxed{
C_U(\rho)
=
\frac4N\rho^r
\left[
\left(\frac{1+\rho^2}{2}\right)^{n-r}-1
\right].
}
\tag{5.5}
\]

In particular these correlations are nonpositive for `0<rho<1`; their large absolute mass is a signed refund, not a positive debit.

Writing

\[
a=\frac{1+\rho^2}{2},
\]

the exact `L1` norm is

\[
\boxed{
L_1(n,\rho)
:=
\sum_{U\ne\emptyset}|C_U(\rho)|
=
\frac4N
\left[
(1+\rho)^n-1-(a+\rho)^n+a^n
\right].
}
\tag{5.6}
\]

Choose the natural boundary scale

\[
\rho_n=1-\frac1n.
\tag{5.7}
\]

Then

\[
\frac{(1+\rho_n)^n}{N}\to e^{-1/2},
\qquad
\frac{(a_n+\rho_n)^n}{N}\to e^{-1},
\tag{5.8}
\]

while the remaining two terms in (5.6), after division by `N`, vanish. Therefore

\[
\boxed{
L_1(n,\rho_n)
\longrightarrow
4(e^{-1/2}-e^{-1})
=
0.9546048741\ldots
}
\tag{5.9}
\]

but

\[
(1-\rho_n^2)I(f_n)
=
\left(\frac2n-\frac1{n^2}\right)\frac{2n}{N}
=
\frac{4-2/n}{N}.
\tag{5.10}
\]

Hence

\[
\boxed{
\frac{L_1(n,\rho_n)}
{(1-\rho_n^2)I(f_n)}
\sim
(e^{-1/2}-e^{-1})\,2^n.
}
\tag{5.11}
\]

So (5.1) fails exponentially.

This is a rigorous reason not to turn the new signed semigroup bank into an absolute-correlation/total-variation estimate. It does not refute every possible positive-part argument; it specifically shows that the cancellations inside the Boolean correlation field are of exponentially larger `L1` size than the available influence budget.

---

## 6. The `L2` bank has the correct scale on the same obstruction

For the same one-point defect, (5.5) gives

\[
\sum_{U\ne\emptyset}C_U(\rho)^2
=
\frac{16}{N^2}
\left[
(1+\rho^2)^n-1
-2\bigl((a+\rho^2)^n-a^n\bigr)
+\bigl((a^2+\rho^2)^n-a^{2n}\bigr)
\right].
\tag{6.1}
\]

At `rho_n=1-1/n`,

\[
\sum_{U\ne\emptyset}C_U(\rho_n)^2
\sim
\frac{16}{N}
\left(e^{-1/2}-e^{-1}\right)^2,
\tag{6.2}
\]

whereas the right side of (2.1) is asymptotic to `4/N`. Thus

\[
\boxed{
\frac{\sum_{U\ne\emptyset}C_U(\rho_n)^2}
{(1-\rho_n^2)I(f_n)}
\longrightarrow
4\left(e^{-1/2}-e^{-1}\right)^2
=
0.2278176164\ldots
}
\tag{6.3}
\]

The signed `L2` bank is therefore on the correct `1/N` scale even on a family where `L1` explodes relative to influence. This is evidence for the **representation**, not a proof of FEI.

---

## 7. A concrete compiler criterion for the unresolved R32/T-join debit

The new bank suggests a sharper target than the previous per-edge absolute congestion bound.

Suppose an unresolved signed quantity `D(f)` can be represented in the gauged coordinates as

\[
D(f)
=
\int_0^1
\sum_{U\ne\emptyset}
\Phi_U(\rho)C_U(\rho)\,d\rho.
\tag{7.1}
\]

Weighted Cauchy-Schwarz and (2.3) give

\[
|D(f)|
\le
J(f)^{1/2}
\left[
\int_0^1
(1-\rho^2)
\sum_{U\ne\emptyset}\Phi_U(\rho)^2\,d\rho
\right]^{1/2}.
\tag{7.2}
\]

Therefore the following **dual-energy condition** is sufficient for linear payment:

\[
\boxed{
\int_0^1
(1-\rho^2)
\sum_{U\ne\emptyset}\Phi_U(\rho)^2\,d\rho
\le L^2J(f)
\quad\Longrightarrow\quad
|D(f)|\le LJ(f).
}
\tag{7.3}
\]

This makes clear why a deterministic `Phi` of bounded norm is not enough: it would only give a `sqrt(J)` bound. The compiler must obtain the second `sqrt(J)` from the actual disagreement geometry.

There is a natural source for exactly that factor. For each physical coordinate define the disagreement indicator

\[
\eta_i(x)
=
\frac{1-f(x)f(x^{\oplus i})}{2}
\in\{0,1\}.
\tag{7.4}
\]

Then

\[
\|\eta_i\|_2^2=\operatorname{Inf}_i(f),
\qquad
\boxed{
\sum_i\sum_U\widehat\eta_i(U)^2
=
I(f)
}
\tag{7.5}
\]

by Parseval. In the folded minimizing-character gauge this total is `J(f)`.

Thus a concrete next theorem would be an operator representation of the R32 normalized T-join field in the form

\[
\Phi=M(\widehat\eta),
\tag{7.6}
\]

where `M` maps the cut-indicator Fourier field into the weighted space of (7.3) with universal operator norm. The earlier `1/d_A` T-join barycenter supplies a sign-preserving way of producing the physical cut source; (2.2)/(4.2) supplies the signed Boolean-correlation sink. Proving the bounded operator bridge between them would give a genuine dimension-free payment without taking absolute values across relation orders.

This is the next nonoverlapping target. It is **not proved here**.

---

## 8. Computation performed for this run

Companion code:

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B16/20260921T104142Z-noise-square-payment/check.py`

The exact locally executed bytes had SHA-256

`b6a171148df14d9eb02f6873acf50e0af192708646149fde3e7f2994a0d28937`.

Execution returned `PASS` and checked:

- the exact rational Hardy-tail bank (4.2) for **all 276 Boolean functions through n=3**;
- the pointwise chain
  `sum C_U^2 <= Z(1-Z) <= (1-rho^2)I`
  in **3,096 function/noise cases**, exhaustive through `n=3` and deterministic random functions for `n=4,5,6`;
- the one-point closed forms at `n=8,12,16,20,30,40`.

Observed maxima/limits:

- maximum exact Hardy-bank / influence ratio through `n=3`: `0.1126984126984127`;
- maximum tested pointwise `L2` / `((1-rho^2)I)` ratio: `0.2298116683959961`;
- predicted one-point `L1` limit: `0.9546048741647644`;
- predicted one-point `L2`-ratio limit: `0.2278176164447814`;
- at `n=40`, the one-point `L1`/budget ratio was about `2.661699654266e11`, while the `L2`/budget ratio was `0.2408567657`.

These computations are checks of the formulas only. The all-dimensional statements above have direct proofs and do not depend on finite enumeration.

---

## 9. What changed in the FEI proof state

**PROVED this run:**

1. a dimension-free signed noise-square payment of total cost `I`, and cost `J` after the legitimate gauge;
2. an exact Hardy/tail-credit factorization of the Boolean cancellation into a positive semigroup Gram form with signed cross-moment terms;
3. an explicit folded Boolean family showing that the corresponding absolute-correlation `L1` estimate fails exponentially;
4. an exact dual-energy criterion identifying what the next compiler bridge must supply.

**Not proved:**

- the operator bridge from the normalized R32/T-join debit to the new `C_U(rho)` bank;
- any universal bound on the old per-edge signed congestion;
- full FEI.

The full conjecture therefore remains **OPEN**.

**Next run on this route:** express the normalized T-join edge source through the Fourier transforms of the actual cut indicators `eta_i`, and test whether the R32 Borel kernel induces a multiplier/operator `M` with the weighted norm in (7.3). If that operator norm grows with dimension on an explicit Boolean family, record the obstruction and pivot; if it stays bounded, prove the multiplier bound while preserving terminal-band and R16 moment credits.
