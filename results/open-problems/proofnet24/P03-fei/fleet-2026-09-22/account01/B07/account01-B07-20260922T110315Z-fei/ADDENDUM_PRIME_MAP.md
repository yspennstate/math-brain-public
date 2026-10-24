# Addendum — complete common-bias arity-three composition-prime zero-KL map

**Outcome refinement:** `ESSENTIAL_STEP_APPLIED / PRIME_RIGIDITY_REFUTED_ON_EXPLICIT_ALGEBRAIC_BIASES`  
**Full FEI:** **OPEN / NOT PROVED**.

After the main report was committed, I pushed the same exact toric calculation one step further using the project’s exact cofactor criterion for composition-primality. This supersedes the main report’s statement that the exceptional arity-three slice is still wholly open.

## 1. A closed-form composition-prime zero-KL gate

Let

\[
f(x_1,x_2,x_3)=
\begin{cases}
+1,&x_1+x_2+x_3\le1,\\
-1,&x_1+x_2+x_3\ge2.
\end{cases}
\tag{1.1}
\]

This is truth-table mask `23` in the report’s lexicographic convention. At common input bias `p`, direct exact biased-Fourier calculation gives, for every singleton `i`, pair `ij`, and the triple,

\[
\widehat f(i)^2=16p^3(1-p)^3,
\tag{1.2}
\]
\[
\widehat f(ij)^2=4p^2(1-p)^2(2p-1)^2,
\tag{1.3}
\]
\[
\widehat f(123)^2=16p^3(1-p)^3.
\tag{1.4}
\]

The first two three-variable toric equations hold by symmetry. The third is equivalent, in the interior, to equality of (1.2) and (1.3):

\[
16p^3(1-p)^3=4p^2(1-p)^2(2p-1)^2,
\]

hence

\[
4p(1-p)=(2p-1)^2
\iff
\boxed{8p^2-8p+1=0.}
\tag{1.5}
\]

Therefore at the two exact biases

\[
\boxed{p_\pm=\frac12\pm\frac{\sqrt2}{4}}
\tag{1.6}
\]

all seven nonempty squared Fourier coefficients are equal and strictly positive. Thus the normalized nonempty spectral law is exactly the uniform law on the seven nonempty subsets of `[3]`:

\[
w_S=\frac17\qquad(S\ne\varnothing).
\tag{1.7}
\]

Its occurrence marginals are

\[
r_1=r_2=r_3=\frac47,
\]

and its occurrence I-projection is precisely independent `Bernoulli(1/2)^3` conditioned on nonemptiness. Hence

\[
\boxed{K_{\rm occ}(f;p_\pm)=0.}
\tag{1.8}
\]

This is an analytic equality, not a numerical near-zero statement.

The gate is also **composition-prime** under the project’s exact cofactor criterion. For any proper two-coordinate block, the four cofactors on the remaining bit include exactly the three distinct one-bit functions

\[
(+,+),\qquad (+,-),\qquad (-,-).
\]

Thus every proper block has three distinct cofactors, so no decomposition `f=H(g(x_A),x_{A^c})` is possible. This directly applies the cofactor theorem used throughout the FEI fleet (account01/B13, commit `d99ffba1e2cb9dc61f7a6d77f8ba961239694ea3`).

Consequently the unrestricted conjectural statement “every essential composition-prime biased gate has positive `K_occ`” is false already at arity three. The failure occurs on an explicit algebraic bias locus. It does **not** refute FEI and does not invalidate generic rigidity away from that locus.

## 2. Exact complete prime map for common-bias arity three

The second certificate exhausts all 218 essential three-input truth tables, applies the three toric equations from the main report, and then applies the exact cofactor criterion. For every nonbalanced irreducible exceptional factor it also verifies that none of the seven squared Fourier coefficients vanishes at its algebraic roots. Hence the toric equations are sufficient there, not merely necessary.

The resulting common-bias composition-prime zero-KL map is:

| bias polynomial | composition-prime truth-table masks |
|---|---|
| `2p-1` | none |
| `8p^2-8p+1` | `23, 232` |
| `2p^2-1` | `61, 91, 103, 152, 164, 194` |
| `2p^2-4p+1` | `25, 37, 67, 188, 218, 230` |
| `18p^2-24p+7` | `22, 233` |
| `2p^2-6p+3` | `62, 94, 118, 137, 161, 193` |
| `18p^2-12p+1` | `104, 151` |
| `2p^2+2p-1` | `110, 122, 124, 131, 133, 145` |

For `p=1/2`, every zero-KL conditional-product law must satisfy the same toric binomials (possibly on their boundary). The exact enumeration finds 42 essential toric candidates and **none is composition-prime**, so there is no essential composition-prime three-input zero-KL gate at the balanced point. This is compatible with the separate balanced character-times-bent equality theorem.

For every `p in (0,1)` outside the eleven-point exceptional set in the main report, the main theorem already shows that only one-point defects and parity/complements occur, all decomposable. Thus the table above is the complete set of common-bias locations at which an essential composition-prime arity-three zero-KL gate can occur.

## 3. Exact certificates

The full prime-map certificate is

`verify_arity3_prime_map.py`, creation commit `1bcca3b356b5d9fa8a9e3a78eaf484902f7d156f`,

with archived PASS output in `verify_arity3_prime_map.out`, creation commit `bdf9a6bdf4d58ba4a028a28e5bbfcd9949de5103`.

The short analytic witness checker is

`verify_exceptional_prime.py`, creation commit `86a2cf06841e5d1baeedb522890761e319123b9f`,

with archived PASS output in `verify_exceptional_prime.out`, creation commit `54fd73f17eeb9a8df129ed81af357ee403eda686`.

Both were executed in this invocation with exact symbolic arithmetic. They are author-side exact certificates, not independent reviews.

## 4. Revised next implication

The arity-three **prime** equality problem is no longer open in the common-bias slice. The next useful equality target is therefore genuinely higher-dimensional or non-common-bias:

> **`B-ZEROKL-PRIME-RIGIDITY-v2` (revised).** Classify the intersection of the full conditional-product toric ideal with the exact biased Boolean multiplication variety for essential composition-prime gates of arity at least four, while allowing explicit algebraic exceptional bias loci analogous to (1.5).

A quantitative Path-B theorem must also allow `K_occ` to vanish on these prime exceptional loci. Consequently any universal lower bound of the form “composition-prime implies `K_occ >= epsilon`” is impossible without a distance-to-exception term or an additional source currency.
