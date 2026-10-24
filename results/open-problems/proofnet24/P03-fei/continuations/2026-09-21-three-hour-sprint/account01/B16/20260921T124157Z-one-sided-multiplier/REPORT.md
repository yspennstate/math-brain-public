# B16 signed transport: one-sided Walsh-multiplier payment for q-flip activity

**Date:** 21 September 2026  
**Scope:** account01 / B16, `FEI signed transport proof`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Route:** APPROACH 10/13, signed transport/noise interpolation.  

This run changes the payment norm after the preceding account01 calculation showed that the centered raw ordered-min entropy kernel has low Walsh multipliers of order `n`. That earlier calculation correctly kills a uniform `L2`/absolute-kernel estimate. It does **not** imply that those large modes are costly in the signed upper-bound problem. The q-flip activity has nonpositive nonconstant Walsh coefficients, so large **positive** kernel multipliers are credits. Keeping this sign gives a substantially sharper theorem: for every nonnegative codimension-level kernel of the ordered-min form, the centered part has one-sided debit at most `2 Q_n/n` times cut energy, where `Q_n` is just the sum of its level charges. For the actual raw subcube entropy charges, `Q_n<12` uniformly, hence the entire centered raw baseline costs at most `24 J(f)/n` after the minimizing-character gauge.

This is a universal signed payment lemma, not a finite-case inference. It narrows the remaining B16 burden to the constant Walsh mode and to any genuinely negative modes created by the full Shapley/terminal/R16 residual. Full FEI remains open.

---

## 1. Entering identities

For a physical coordinate `i`, write

\[
\eta_i(x)=\frac{1-f(x)f(x^{\oplus i})}{2},\qquad
\alpha_i=\mathbb E\eta_i,
\qquad E_i=\alpha_i(1-\alpha_i).
\]

Identify `eta_i` with a Boolean function on `W_i=F_2^{n-1}`. The preceding account01 report proved that the q-flip frustration profile

\[
p_i(w)=\Pr_x[\eta_i(x)\ne\eta_i(x+w)]
\]

has normalized Walsh transform

\[
\widehat p_i(0)=2E_i,
\qquad
\widehat p_i(U)=-2\widehat\eta_i(U)^2\quad(U\ne0).
\tag{1.1}
\]

In particular all its nonconstant Walsh coefficients have one sign.

For any real kernel `k:W_i->R`, normalized Parseval therefore gives the exact identity

\[
\boxed{
\langle k,p_i\rangle
=2E_i\widehat k(0)
-2\sum_{U\ne0}\widehat k(U)\widehat\eta_i(U)^2.
}
\tag{1.2}
\]

When `E_i>0`, define the cut-spectral probability measure

\[
\nu_i(U)=\frac{\widehat\eta_i(U)^2}{E_i},\qquad U\ne0.
\]

For the centered kernel `k^\circ=k-\widehat k(0)`, (1.2) becomes

\[
\boxed{
\langle k^\circ,p_i\rangle
=-2E_i\,\mathbb E_{U\sim\nu_i}\widehat k(U).
}
\tag{1.3}
\]

This is the sign that the previous `L2` criterion discarded.

### Theorem 1 — `B16-ONE-SIDED-QFLIP-MULTIPLIER-PAYMENT`

For every real displacement kernel `k`,

\[
\boxed{
\langle k^\circ,p_i\rangle
\le
2E_i\sup_{U\ne0}(-\widehat k(U))_+.
}
\tag{1.4}
\]

More precisely,

\[
(\langle k^\circ,p_i\rangle)_+
\le
2E_i\,\mathbb E_{\nu_i}[(-\widehat k(U))_+].
\tag{1.5}
\]

Thus **positive nonconstant multipliers are signed credits, regardless of their size**. A dimension-free upper-bound payment only needs a lower bound on the multipliers, not an absolute or `L2` kernel bound.

#### Proof

Equation (1.3) is exact. Replace `-\widehat k(U)` by its positive part before averaging. `square`

This is the first route change of the run: the old bounded-`L2` kernel target is dead, so the correct target is a one-sided multiplier floor.

---

## 2. A whole class of ordered-min kernels has an exact multiplier floor

Let `q_2,...,q_n` be arbitrary nonnegative real charges. Define the random-order ordered-min radial kernel on `W=F_2^{n-1}` by

\[
K_n^q(w)
=
\frac1n\sum_{c=|w|+1}^n
q_c\frac{\binom{c-1}{|w|}}{\binom{n-1}{|w|}},
\qquad w\ne0,
\tag{2.1}
\]

and `K_n^q(0)=0`. As in the preceding account01 normalization put

\[
\mathcal K_n^q(w)=2^{n-1}K_n^q(w),
\qquad
\mu_n^q=\mathbb E_w\mathcal K_n^q(w),
\qquad
k_n^q=\mathcal K_n^q-\mu_n^q.
\]

For a nonzero Walsh frequency `U` of weight `r`, the same layer-counting used for the raw entropy kernel gives

\[
\boxed{
A_{n,r}^q:=\widehat{\mathcal K_n^q}(U)
=
\frac1n\sum_{c=2}^n q_c
\left[
2^{c-1}
\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}
-1
\right].
}
\tag{2.2}
\]

For completeness, the bracket follows by summing `(-1)^{U\cdot w}` over the random `(c-1)`-subset of coordinates after the pivot: the full subset sum contributes

\[
2^{c-1}\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}},
\]

and the forbidden `w=0` term subtracts `1`.

Put

\[
Q_n=\sum_{c=2}^n q_c.
\]

### Theorem 2 — `B16-ORDEREDMIN-NEGATIVE-MULTIPLIER-FLOOR`

For every `1<=r<=n-1`,

\[
\boxed{A_{n,r}^q\ge-\frac{Q_n}{n}.}
\tag{2.3}
\]

The bound is exact: at the top frequency `r=n-1`,

\[
\boxed{A_{n,n-1}^q=-\frac{Q_n}{n}.}
\tag{2.4}
\]

#### Proof

Every binomial ratio in the positive term of (2.2) is nonnegative and every `q_c` is nonnegative, giving (2.3). If `r=n-1`, then `n-1-r=0`, so `binom(0,c-1)=0` for every `c>=2`; all positive terms vanish and equality follows. `square`

Combining Theorems 1 and 2 gives the useful payment statement.

### Corollary 3 — `B16-ORDEREDMIN-CENTERED-SIGNED-PAYMENT`

For every Boolean `f` and every coordinate `i`,

\[
\boxed{
\langle k_n^q,p_i\rangle
\le \frac{2Q_n}{n}E_i.
}
\tag{2.5}
\]

Consequently

\[
\boxed{
\sum_{i=1}^n\langle k_n^q,p_i\rangle
\le \frac{2Q_n}{n}I(f).
}
\tag{2.6}
\]

After multiplying `f` by the minimizing character, `p_i` and `E_i` are unchanged while

\[
E_i=\alpha_i(1-\alpha_i)\le\min(\alpha_i,1-\alpha_i),
\]

so

\[
\boxed{
\sum_i\langle k_n^q,p_i\rangle
\le \frac{2Q_n}{n}J(f).
}
\tag{2.7}
\]

No absolute value is placed on the left: negative terms are genuine credits.

### Sharpness inside the Boolean class

The constant `2Q_n/n` cannot be improved from the multiplier information alone. Let `U=W` be the top Walsh frequency and set

\[
\eta(w)=\frac{1-\chi_U(w)}2.
\]

Then `E=1/4` and the only nonconstant Fourier mass of `eta` is at `U`. It is an actual cut field: define

\[
f(0,w)=1,\qquad f(1,w)=\chi_U(w).
\]

For the first coordinate this has disagreement indicator exactly `eta`. Since (2.4) holds,

\[
\langle k_n^q,p\rangle
=\frac{Q_n}{2n}
=\frac{2Q_n}{n}E.
\]

Thus the one-sided theorem is not merely a loose norm estimate.

---

## 3. Application to the actual raw dual-generator entropy kernel

For the ordered-min raw baseline, the level charge is the entropy `H_c` of a codimension-`c` subcube defect. Its squared Fourier distribution has one mass

\[
p_0=(1-2^{1-c})^2
\]

and `2^c-1` equal nonzero masses `2^{2-2c}`. Equivalently, with

\[
\varepsilon_c=1-p_0=2^{2-c}-2^{2-2c},
\]

\[
H_c=h_2(\varepsilon_c)+\varepsilon_c\log_2(2^c-1).
\tag{3.1}
\]

Let

\[
Q_n^{\rm raw}=\sum_{c=2}^n H_c.
\]

This sum is uniformly bounded. Indeed

\[
h_2(\varepsilon)\le \varepsilon\log_2(e/\varepsilon),
\]

and

\[
\frac34 2^{2-c}\le\varepsilon_c\le2^{2-c}.
\]

Hence

\[
H_c
\le
\varepsilon_c\left(\log_2(e/\varepsilon_c)+c\right)
<2c\,2^{2-c}=8c\,2^{-c},
\]

so

\[
\boxed{
Q_n^{\rm raw}<8\sum_{c=2}^\infty c2^{-c}=12.
}
\tag{3.2}
\]

Therefore the **entire centered raw generator-entropy kernel**, despite its `Theta(n)` positive low Walsh multipliers, satisfies

\[
\boxed{
\sum_i\langle k_n^{\rm raw},p_i\rangle
<\frac{24}{n}J(f).
}
\tag{3.3}
\]

The direct deterministic evaluation of (3.1) through `c=100` gives

\[
\sum_{c=2}^{100}H_c=8.71142009332293,
\]

so the elementary constant `24` is intentionally coarse; the exact finite theorem uses `2Q_n^{raw}`.

### What happened to the previous `A_{n,r}=Theta(n)` obstruction?

For every fixed `r`, the previous report proved

\[
A_{n,r}^{raw}=\frac{4n}{(r+1)(r+2)}+O_r(1),
\]

which indeed rules out a uniform absolute-multiplier or `L2` kernel estimate. But by (1.1), positive `A_{n,r}` multiplies a **negative** Fourier coefficient of `p_i`. It is therefore a credit in the upper-bound direction. The only dangerous part of a centered nonnegative-level kernel is its negative multiplier tail, and Theorem 2 bounds that tail by `Q_n/n` exactly.

Thus the correct conclusion is sharper than the prior diagnostic:

> centering alone does not make the raw kernel small in norm, but centering does make its **one-sided signed debit** `O(J/n)`.

This does not undo the previous obstruction; it bypasses precisely the absolute-value step that caused it.

---

## 4. The account03 parity-switch refund becomes even cheaper one-sidedly

The account03 dummy-Ward calculation proved that on the dummy-extended parity-switch diagnostic, Shapley curvature changes the active level charge from `H_c` to

\[
q_c=2^{3-c}.
\]

Here

\[
Q_n=\sum_{c=2}^n2^{3-c}=4-2^{3-n}.
\]

Therefore its centered q-flip kernel satisfies the sharp one-sided bound

\[
\boxed{
\langle k_n^{refund},p_i\rangle
\le
\frac{8-2^{4-n}}{n}E_i.
}
\tag{4.1}
\]

This agrees with the exact refunded multiplier formula from that handoff:

\[
\widetilde A_{n,r}
=\frac4{r+1}-\frac{8-2^{3-n}}n,
\]

whose minimum occurs at `r=n-1` and equals `-(4-2^{3-n})/n`. The large positive low modes are again credits, not debits.

---

## 5. What remains for the full signed compiler

The new theorem materially changes the next target. We no longer need to prove that every nonconstant multiplier of the raw or refunded ordered-min kernel is `O(1)` in absolute value. For any piece represented by a nonnegative codimension-level kernel, all nonconstant **debit** is already paid by `O(J/n)`.

The unresolved large term is the constant Walsh mode

\[
\mu_n^q=\widehat{\mathcal K_n^q}(0)
=\frac1n\sum_{c=2}^n q_c(2^{c-1}-1),
\tag{5.1}
\]

which for `q_c=H_c` is `Theta(n)`. The full Shapley/plaquette identity also carries the signed curvature refund, the terminal Shapley share, and the inherited R16/moment credits. The next account01/B16 calculation should therefore isolate the **constant displacement mode of the fully refunded kernel** and prove that it is canceled or paid by those existing ledgers. Only genuinely negative nonconstant multipliers need further control.

A particularly useful sufficient statement would be a decomposition of the full basis-averaged residual kernel

\[
R_i(w)=\mu_i+R_i^{+}(w)+R_i^{-}(w)
\]

such that the constant debit `2E_i mu_i` is canceled by the terminal/curvature ledger, while every remaining codimension-level component has nonnegative charges. Theorem 2 would then pay the entire nonconstant remainder without any absolute-value loss.

This is narrower than the previous proposed all-mode Ward identity and is directly adapted to the sign of the Boolean q-flip profile.

**Full FEI remains OPEN.**

---

## 6. Self-check

`check_one_sided_multiplier.py` performs two small checks only:

1. exact rational verification of (2.2), the floor (2.3), and sharpness for `35` `(n,r)` cases through `n=8` with a positive synthetic rational charge sequence;
2. exhaustive direct verification of the raw centered payment on all Boolean functions for `n=2,3`, `800` function-coordinate cases total.

Observed output:

```text
PASS
exact_multiplier_cases 35
exhaustive_boolean_coordinate_cases 800
worst_raw_ratio_to_sharp_bound 1.0
Q_raw_100 8.71142009332293
theorem_elementary_uniform_bound Q_raw_infty < 12
```

The finite check is a self-check, not the proof and not an FEI audit. The theorem proof is the signed Fourier calculation above.
