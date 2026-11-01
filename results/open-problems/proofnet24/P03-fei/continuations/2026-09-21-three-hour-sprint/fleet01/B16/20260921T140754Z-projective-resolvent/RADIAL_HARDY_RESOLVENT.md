# B16 follow-up — the radial first-hit bank is exactly a Hardy/noise resolvent square

**Date:** 21 September 2026  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI:** **OPEN / NOT PROVED**.

This note consumes the newest fleet04/B16 first-hit two-scale handoff. That handoff reduced the aggregate centered selector energy to an internal Bernoulli-curvature bank plus the radial moment bank
\[
\mathcal K_{\rm rad}(C)
=\sum_v \operatorname{Var}_{t\sim U[0,1]}m_v(t),
\qquad
m_v(t)=\sum_{A:v\in R_A}c_A t^{q_A-1}.
\tag{0.1}
\]
It asked for a comparison of this one-dimensional signed moment bank with the inherited R16 moment/refund reservoir. The result below gives an exact factorization, not an absolute-value estimate.

## 1. Exact Hardy variance identity

For an integrable polynomial `m` on `[0,1]`, define the Hardy average
\[
(\mathsf Hm)(t)=\frac1t\int_0^t m(s)\,ds
\quad(t>0),
\]
with the continuous value at `t=0`.

### Theorem — `B16-RADIAL-HARDY-RESOLVENT`

For every real polynomial `m`,
\[
\boxed{
\operatorname{Var}_{[0,1]}m
=\int_0^1|m(t)-\mathsf Hm(t)|^2dt.
}
\tag{1.1}
\]
If `D=t d/dt` is the dilation-number operator, then on polynomials
\[
\mathsf H=(I+D)^{-1},
\]
so equivalently
\[
\boxed{
\operatorname{Var}_{[0,1]}m
=\|D(I+D)^{-1}m\|_{L^2[0,1]}^2.
}
\tag{1.2}
\]

### Proof

Put `F=Hm`. Then `tF(t)=int_0^t m(s)ds`, so
\[
m=F+tF',
\qquad
m-F=tF'.
\]
Also
\[
\int_0^1m(t)dt=F(1).
\]
Therefore
\[
\begin{aligned}
\int_0^1m^2-F(1)^2
&=\int_0^1(F+tF')^2dt-F(1)^2\\
&=\int_0^1t^2(F')^2dt
 +\left[tF(t)^2\right]_{0}^{1}-F(1)^2\\
&=\int_0^1|m-F|^2dt.
\end{aligned}
\]
This is (1.1). Since `H(t^d)=t^d/(d+1)`, one has `H=(I+D)^-1` on every polynomial, proving (1.2). `square`

Thus the exact transfer function on degree `d` is
\[
\boxed{\frac d{d+1}.}\tag{1.3}
\]
This is the **same scalar resolvent symbol** that appeared independently in the spatial projective q-flip theorem of this B16 run, where Walsh weight `r` was charged by `r/(r+1)`.

## 2. Exact signed form of the radial bank

Group the relation coefficients at a fixed first-hit site `v` by support size:
\[
a_{v,q}=\sum_{A:v\in R_A,\ q_A=q}c_A.
\tag{2.1}
\]
Then
\[
m_v(t)=\sum_q a_{v,q}t^{q-1}.
\]
No absolute values are taken in (2.1); all R32 sign cancellation among relations of the same size is retained before any square.

The Hardy identity gives
\[
\boxed{
\mathcal K_{\rm rad}(C)
=\sum_v\int_0^1
\left[
\sum_q\frac{q-1}{q}a_{v,q}t^{q-1}
\right]^2dt.
}
\tag{2.2}
\]
Expanding (2.2) recovers exactly the fleet04 pair kernel:
\[
\frac{(q-1)(r-1)}{qr(q+r-1)}
=\frac1{q+r-1}-\frac1{qr}.
\tag{2.3}
\]
Hence (2.2) is not a new upper bound on the radial bank; it is an exact signed square factorization of it.

There is also a literal interpolation formula. Since
\[
\frac d{d+1}=\int_0^1 d s^d ds,
\]
\[
\boxed{
(I-\mathsf H)m(t)
=\int_0^1(Dm)(st)\,ds.
}
\tag{2.4}
\]
So the radial bank is the square of an integrated dilation/noise derivative. This puts the newest first-hit radial obstruction directly into APPROACH 10 language.

## 3. Exact dyadic split: moment-damped half + terminal half + one bridge scalar

The old R16 bank has exponentially damped high-order moment weights, while the terminal theorem controls a signed endpoint rather than all intermediate turnover. Split `t` at `1/2`. Let
\[
V_-:=\operatorname{Var}_{t\sim U[0,1/2]}m(t),
\qquad
V_+:=\operatorname{Var}_{t\sim U[1/2,1]}m(t).
\]
The law of total variance gives
\[
\boxed{
\operatorname{Var}_{[0,1]}m
=\frac12V_-+\frac12V_++B(m)^2,
}
\tag{3.1}
\]
where direct integration yields the single signed bridge functional
\[
\boxed{
B(m)=\sum_q\frac{1-2^{1-q}}q a_q.
}
\tag{3.2}
\]
Indeed the two conditional means differ by
\[
\mu_- -\mu_+
=-2\sum_q\frac{1-2^{1-q}}q a_q.
\]

The low half has an **exact exponentially damped resolvent form**. After `t=u/2`,
\[
m(u/2)=\sum_q a_q2^{-(q-1)}u^{q-1},
\]
so Theorem (1.1) gives
\[
\boxed{
V_-
=\int_0^1
\left[
\sum_q
2^{-(q-1)}\frac{q-1}{q}a_q u^{q-1}
\right]^2du.
}
\tag{3.3}
\]
Every support size `q` therefore enters the low-radius radial bank with an exact factor `2^{-(q-1)}` **before squaring**. This is the same exponential scale on which the inherited R16 high-resolvent coefficients live. No sign has been discarded.

Equation (3.1) isolates the still-hard radial content into only two objects:

1. the near-terminal high-half variance `V_+`, where `t` is close to the terminal value one;
2. the scalar bridge `B(m)`, which differs from the Aumann--Shapley mean `sum_q a_q/q` only by the exponentially small correction `sum_q 2^{1-q}a_q/q`.

This is a sharper target than bounding the whole radial variance at once.

## 4. Synthesis with the projective spatial resolvent

The two new fleet01 results of this run now have exactly the same transfer function:

- projective displacement/Walsh degree `r`:
  \[
  \frac r{r+1};
  \]
- first-hit radial/dilation degree `d=q-1`:
  \[
  \frac d{d+1}.
  \]

Thus the signed transport route has produced the same resolvent `z/(1+z)` independently in its **spatial q-flip** and **radial moment** variables.

This suggests a concrete next compiler target rather than another generic norm estimate:

> identify the authentic R16 first-separation/moment reservoir with the low-half square (3.3), and identify the authorized terminal response plus Shapley load with `V_+ + 2 B(m)^2` after all signed R32 coefficients are inserted.

If that identification is exact or bounded by `C J(f)`, then the fleet04 two-scale decomposition plus the projective spatial theorem would pay both unresolved channels while preserving the `2 mod 4` negative credits. The all-positive triple-star obstruction from fleet04 shows why the high-half piece cannot be replaced by a generic internal-curvature estimate.

No such R16/terminal identification is claimed yet. **Full FEI remains OPEN.**

## 5. Exact self-check

`check_hardy_resolvent.py` verifies, with rational arithmetic, the Hardy variance identity, the exact dyadic total-variance split, and the low-half exponentially rescaled resolvent identity for every coefficient vector in `{-2,-1,0,1,2}^4` on degrees `2,4,6,8`: **625 exact signed polynomial cases**.

Observed output:

```text
PASS
exact_signed_polynomial_cases 625
degrees_checked [2, 4, 6, 8]
identities ['hardy_variance', 'dyadic_total_variance', 'low_half_exponential_resolvent']
```

The checker is a self-check; equations (1.1)--(3.3) are proved analytically above.
