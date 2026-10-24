# QFORM-S5-FULL-HALF-POTENTIAL-v1

Run: `20260924T144935Z-account01-B20-fixedmult-auto11-r14`  
Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
New dependency: the rough-law-safe marginal-free `E_2` half-potential receiver from the multiplicity-nine compiler.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K`. Let `A=A^T`, `b`, `c` be arbitrary. If

\[
s_5(A)\ge s>0,
\]

then, for `Q=X^TAX+b^TX+c`,

\[
\boxed{
\sup_{a\in\mathbb R}\mathbb E|Q-a|^{-1/2}
<488\,{K\over\sqrt s}.
}
\]

No support, moment, smoothness, iid, sign, exact-rank, leverage, diagonal-basis, or post-rotation-independence hypothesis is added. This is a full negative-half-potential theorem, not by itself a bounded-density theorem.

## Proof

Normalize first to `K=s=1`. Keep the manuscript constants

\[
\eta={1\over100},\qquad \kappa={1\over80^2}={1\over6400}.
\]

### Case 1: an `eta`-pivot exists

The sharpened pivot half-potential argument in the multiplicity-nine replacement requires only two unit-scale spectral directions. Since `s_5(A)>=1`, that hypothesis is automatic. Its three physical pivot alternatives give:

- scalar pivot: truncated half-potential
  \[
  10\,[8+2\sqrt2\{4+4\log(40/3)\}]
  =486.192361433\ldots<487;
  \]
- definite pair: `<40 pi<126`;
- indefinite pair: `<433`.

Outside `|Q-a|<=1`, the kernel is at most one. Hence in all pivot alternatives

\[
\sup_a\mathbb E|Q-a|^{-1/2}<488.
\tag{1}
\]

### Case 2: no `eta`-pivot exists

Apply the pinned spectral-to-volume proposition with `k=2`. Its required spectral multiplicity is

\[
4k-3=5,
\]

so `s_5(A)>=1` gives

\[
V_2(A)\ge\kappa^2.
\tag{2}
\]

The fair original-coordinate cut lemma gives a literal cross block `M` satisfying

\[
E_2(M)=e_2(MM^T)\ge4^{-2}V_2(A)
\ge {\kappa^2\over16}.
\tag{3}
\]

The rough-law-safe marginal-free `E_2` receiver from the grouped product-Fourier compiler states

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le C_2 E_2(M)^{-1/8},
\qquad
C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots .
\tag{4}
\]

It retains arbitrary same-bank quadratic terms, affine terms, outside coordinates and all nonzero coefficient tails. Inserting (3),

\[
E_2(M)^{-1/8}
\le (16\kappa^{-2})^{1/8}
=\sqrt2\,\kappa^{-1/4}
=\sqrt{160}.
\]

Therefore

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le C_2\sqrt{160}
=152.99191115498\ldots<153<488.
\tag{5}
\]

Together (1) and (5) prove the normalized theorem.

### Scaling

Put `Y=KX` and

\[
\widetilde Q
=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]

Then every coordinate of `Y` has density cap one, `s_5(A/s)>=1`, and

\[
Q={s\over K^2}\widetilde Q.
\]

Consequently, for every `a`,

\[
\mathbb E|Q-a|^{-1/2}
={K\over\sqrt s}
\mathbb E\left|\widetilde Q-{K^2a\over s}\right|^{-1/2}
<488\,{K\over\sqrt s}.
\]

This proves the theorem.

## Threshold accounting consequence

This isolates the current multiplicity-nine density bottleneck. The scalar-pivot branch of the density theorem needs only one additional direction above this theorem, namely `s_6` before a scalar Schur loss; the no-pivot density branch is what forces `s_9`, because the present order-three spectral-to-volume mechanism requires `4*3-3=9` directions. Thus any `9 -> 8` improvement must genuinely improve the no-pivot endpoint (or replace it), rather than further sharpening scalar-pivot half-potentials.

## Status

**PROVED supporting theorem, conditional only on the already written grouped `E_2` receiver used in the complete multiplicity-nine replacement.** It does not prove multiplicity eight and does not solve the unrestricted three-eigenvalue conjecture.
