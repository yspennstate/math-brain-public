# fleet01/B15 — exact generic-matrix reduction after full target continuity

**Run:** `20260922T160350Z-fleet01-B15-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_GENERIC-CLASS_REDUCTION / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source dependencies

The full target is unchanged: for every dimension `n`, every independent real coordinates with densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove one finite universal `C` such that

`P(X^T A X in I) <= C |I|`

for every interval `I`, equivalently `||p_{X^TAX}||_infinity<=C`.

Fresh controls and corrections were read from `yspennstate/math-research-brain` at coherent source commit `1f2dc7684a305ea574bb81d6f0d991cc0dbf085c`, then refreshed immediately before publication at `9f6b5b5888a78296b602605434a363864cf6f5ac`; owner revision remained `2026-09-22.5`. This argument uses none of the refuted uniform pointwise Fourier decay, rotated-independence, fiber-supremum, conditional-cap, or local-principal-block/cross-rank dichotomies.

Two proved dependencies are used.

1. **Own preceding exact smooth-input reduction:**
   `yspennstate/math-open-problems@5e161df12dcfebf0d13eb7efeaef5c478bf09455`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T150652Z-fleet01-B15-qform-r11/REPORT.md`.
   It proves that every admissible marginal can be approximated in `L1` by compactly supported `C^infinity` probability densities still bounded by one, and that the optimal universal interval-density constant is unchanged by restricting to such smooth marginals.

2. **Assigned partner fleet02/B15 continuity theorem:**
   `yspennstate/math-open-problems@4b2e6a36bcffeb767998c43d27cee1d8f5eaa07e`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T150242Z-fleet02-B15-qform-r3/REPORT.md`.
   It proves that for every fixed real symmetric `A` of rank at least three and every independent cap-one product law, `X^TAX` has a bounded continuous density. Its height bound may depend on `A`; thus it does not prove the universal constant.

The present result removes all matrix degeneracies from the universal constant problem **with no loss in the constant**, and uses the partner theorem to turn interval domination into an everywhere pointwise density inequality for the original rough target law.

## 2. Fully generic target matrices form a dense target subclass

Call a real symmetric `n x n` matrix **fully generic** when

1. its spectrum is simple;
2. every nonempty principal minor is nonzero.

The second condition includes `det A !=0`; hence every principal submatrix is nonsingular.

### Lemma 2.1 — density of full genericity

Fully generic symmetric matrices are dense in the space `Sym_n(R)`.

### Proof

Let

`P(M) = Disc(chi_M) * product_{emptyset != S subset {1,...,n}} det M_{S,S}`,

where `Disc(chi_M)` is the discriminant of the characteristic polynomial. This is a polynomial in the independent entries of `M`. It is not identically zero: for a diagonal matrix

`D=diag(d_1,...,d_n)`

with distinct nonzero `d_i`, every principal minor is a nonzero product of a subset of the `d_i`, and the discriminant is nonzero. Therefore the zero set `{P=0}` has empty interior. Its complement is exactly the fully generic set, hence is dense. QED.

### Lemma 2.2 — target-preserving generic approximation

Let `A` satisfy the QFORM spectral hypothesis: at least three eigenvalues have modulus at least one. Then there exists a sequence of fully generic symmetric matrices `A_k -> A` such that each `A_k` has at least the same three protected eigenvalues with modulus **strictly greater than one**.

### Proof

Take `epsilon_k downarrow0` and put

`B_k=(1+2 epsilon_k)A`.

By Lemma 2.1 choose a fully generic `A_k` with

`||A_k-B_k||_op < epsilon_k`.

Hence `A_k->A`. If an ordered eigenvalue of `A` satisfies `lambda_i(A)>=1`, then Weyl's inequality gives

`lambda_i(A_k) >= (1+2 epsilon_k)lambda_i(A)-epsilon_k >= 1+epsilon_k`.

If `lambda_i(A)<=-1`, then

`lambda_i(A_k) <= (1+2 epsilon_k)lambda_i(A)+epsilon_k <= -(1+epsilon_k)`.

Thus every originally protected positive/negative eigenvalue remains protected with strict margin. QED.

This approximation is purely in the matrix. The original independent physical coordinates and their product law are never rotated or altered.

## 3. Exact equality of the full constant and the smooth fully-generic constant

By the partner theorem, every target instance has a distinguished continuous density. For a target pair `(A,f)` define

`H(A,f)=sup_{t in R} p_{A,f}(t)`.

Let

`C_full = sup H(A,f)`

over the entire QFORM target class.

Let `C_gen` be the same supremum restricted simultaneously to

- `f_i in C_c^infinity(R)`, `0<=f_i<=1`, `int f_i=1`;
- fully generic symmetric `A`;
- at least three eigenvalues of `A` have modulus strictly greater than one.

Both constants are allowed to be `+infinity`.

### Theorem 3.1 — `QFORM-GENERIC-CLASS-EXACT-v1`

`C_full = C_gen`.

In particular, to prove the full conjecture with a constant `C`, it is enough to prove the pointwise inequality

`p_{X^TAX}(t) <= C`

only for compactly supported smooth cap-one product densities and fully generic target matrices with strict spectral margin. The same `C` then holds for every original rough target instance.

### Proof

The inequality `C_gen<=C_full` is immediate.

Assume first that `C_gen<infinity`; otherwise the reverse inequality is vacuous. Fix smooth compactly supported cap-one marginals and an arbitrary target matrix `A`, possibly singular, with repeated eigenvalues and singular principal blocks. Choose the target-preserving fully generic approximation `A_k` from Lemma 2.2 and use the same random vector `X`. Then

`Q_k=X^T A_k X -> X^T A X=Q`

almost surely, because the dimension is fixed and `A_k->A`. Hence the laws `mu_k` converge weakly to `mu`.

For every bounded open interval `I`, Portmanteau gives

`mu(I) <= liminf_k mu_k(I)`.

By the definition of `C_gen`, every `mu_k` has continuous density bounded pointwise by `C_gen`, so

`mu_k(I) <= C_gen |I|`.

Therefore

`mu(I) <= C_gen |I|`.                                              (3.1)

Thus every smooth-input target law, including degenerate matrices, is dominated by `C_gen dx`.

Now let the original marginals be arbitrary measurable cap-one densities. Apply the cap-preserving approximation theorem from the preceding fleet01/B15 report: choose smooth compactly supported `g_{i,m}` with

`||g_{i,m}-f_i||_1 ->0`.

For the product densities,

`|| product_i g_{i,m} - product_i f_i ||_1
 <= sum_i ||g_{i,m}-f_i||_1 ->0`.

Pushforward under `x -> x^T A x` contracts total variation. Hence for every interval `I`,

`mu_f(I)=lim_m mu_{g_m}(I) <= C_gen |I|`,                      (3.2)

where (3.1) was applied to each smooth input law.

At this point one already has the required `L^infinity` domination in the essential-supremum sense. The assigned partner result supplies the stronger regularity and is applied to the inequality itself: since the original rough target output has a **continuous** density `p_f`, for every `t`

`p_f(t)
 = lim_{h downarrow0} mu_f((t-h,t+h))/(2h)
 <= C_gen`                                                     (3.3)

by (3.2). Therefore `H(A,f)<=C_gen` for every full target instance. Taking the supremum gives `C_full<=C_gen`, completing the equality. QED.

## 4. Consequences for future proof architecture

The full universal constant problem may henceforth be attacked under all of the following simultaneous assumptions, with **zero loss in the final constant**:

1. every input density is `C_c^infinity`, bounded by one and normalized;
2. the matrix is invertible with simple spectrum;
3. every nonempty physical principal minor is nonsingular;
4. the three protected eigenvalues lie strictly outside `[-1,1]`.

A successful proof on that dense regular class automatically passes first to degenerate matrices by weak convergence and then to arbitrary rough marginals by total variation, while fleet02/B15 continuity upgrades the final essential bound to the everywhere pointwise inequality (3.3).

This eliminates repeated eigenvalues, zero eigenvalues, singular principal blocks and input roughness as *logical* obstacles to the universal constant. It does **not** make any reciprocal minor uniformly bounded: a fully generic approximation can have arbitrarily small principal singular values. Thus the corrected singleton-plus-two-banks obstruction and the refuted local principal-block/cross-rank dichotomy remain relevant quantitatively.

## 5. First unpaid implication

The full conjecture remains open. After this exact reduction the first quantitative task can be stated on the regular class:

`sup_{n,A,f,t} p_{X^TAX}(t) < infinity`,

where `f_i` are smooth compactly supported cap-one densities and `A` is fully generic with at least three eigenvalues of modulus strictly larger than one.

Any proposed proof may freely use classical pointwise/coarea manipulations on each individual member of this regular class, but the final estimate must remain independent of smoothness seminorms, support diameters, tiny unprotected eigenvalues and the smallest principal minors. The recent ridge-window theorem controls a large diffuse spectral-window subcase; the remaining obstruction is the heavy-coordinate/nonseparable aggregate passage, not regularity.

**Full QFORM status:** `OPEN_NOT_PROVED`.
