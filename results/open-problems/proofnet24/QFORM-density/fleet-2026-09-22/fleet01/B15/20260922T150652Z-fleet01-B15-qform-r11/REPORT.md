# fleet01/B15 — exact smooth-input reduction and continuity on the reduced class

**Run:** `20260922T150652Z-fleet01-B15-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_REGULARITY_REDUCTION / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source pins

The full target remains: for every dimension `n`, independent real coordinates with densities `0<=f_i<=1` and total mass one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite `C` such that

`P(X^T A X in I) <= C |I|`

for every interval `I`. Equivalently, the output law has an essentially bounded density with norm at most `C`. Continuity of that density is a separate stronger conclusion.

Fresh brain control was read at `yspennstate/math-research-brain@c39a945842cffdeeca468cc63f0a22a777886d84`, then refreshed before publication to `0c6a36586f49ba81b805bb5d850149b8e6848c29`; the owner revision stayed `2026-09-22.5`. The live correction inbox was re-read at the refreshed commit. In particular this report does not use a law-uniform pointwise quadratic Fourier decay, independence after rotation, a projection-only shortcut, conditional-density caps after a rotated change of variables, or a local-principal-block/rank-three-cross-cut dichotomy.

The assigned partner result actually used is fleet02/B15:

`yspennstate/math-open-problems@b1d930ff0fbc625393aebcd4a59f9ba1ead465ed`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T130201Z-fleet02-B15-qform-r2/REPORT.md`.

It proves an exact Choquet representation of every admissible one-dimensional density as a probability barycenter of indicator densities `1_E` with `|E|=1`, and hence an exact product mixture of measure-one product-indicator laws. It also proves that no common continuity modulus can hold even for the fixed target matrix `I_3`; therefore continuity may not be transferred by an equicontinuity argument.

## 2. Cap-preserving smooth approximation

### Lemma 2.1 — `QFORM-CAP1-CINF-APPROX-v1`

Let `f:R-> [0,1]` be measurable with `int f=1`. Then there are `g_k in C_c^infinity(R)` such that

`0<=g_k<=1`, `int g_k=1`, and `||g_k-f||_1 ->0`.

### Proof

Choose `R` so that

`delta_R := int_{|x|>R} f(x) dx ->0`.

Put `f_R=f 1_[-R,R]`, of mass `1-delta_R`. Choose a bounded measurable set `H_R` outside `[-R,R]` with `|H_R|=delta_R` and set

`q_R=f_R+1_{H_R}`.

Then `0<=q_R<=1`, `int q_R=1`, `q_R` has bounded support, and

`||q_R-f||_1 <= 2 delta_R`.

Let `eta_epsilon` be a nonnegative compactly supported smooth probability mollifier and set

`g_{R,epsilon}=q_R*eta_epsilon`.

Convolution with a probability kernel preserves the pointwise cap: `0<=g_{R,epsilon}<=1`; it also preserves total mass and gives a smooth compactly supported function. For fixed `R`, translation continuity in `L^1` gives

`||g_{R,epsilon}-q_R||_1 ->0`

as `epsilon->0`. A diagonal choice proves the lemma. QED.

The same construction applies in particular to each measure-one indicator `1_E`.

## 3. Exact equality of the full and smooth optimal constants

For a target output law `mu`, write

`M(mu)=sup_{intervals I, |I|>0} mu(I)/|I|`.

Let

`C_full = sup M((x^T A x)_# prod_i f_i dx)`

over the full target class, and let `C_sm` be the same supremum restricted to marginals `f_i in C_c^infinity`, `0<=f_i<=1`, `int f_i=1`.

### Theorem 3.1 — `QFORM-SMOOTH-CLASS-EXACT-v1`

In the extended interval `[0,infinity]`,

`C_full = C_sm`.

Thus any finite universal constant proved for smooth compactly supported input densities automatically proves the full QFORM theorem with **exactly the same constant**.

### Proof using the assigned partner theorem

The inclusion of the smooth class into the full class gives `C_sm<=C_full`.

For the reverse inequality, apply fleet02/B15's exact Choquet theorem to each arbitrary marginal `f_i`. There are probability measures `Pi_i` on measure-one sets `E_i` such that the full product input law is the exact mixture

`prod_i f_i(x_i) dx = int [prod_i 1_{E_i}(x_i) dx] dPi(E)`,

where `Pi=Pi_1 x ... x Pi_n`. Therefore, for every interval `I`,

`mu_f(I)=int mu_E(I) dPi(E)`.

Fix one product indicator `E`. By Lemma 2.1, choose smooth cap-one probability densities `g_{i,k}` with

`||g_{i,k}-1_{E_i}||_1 ->0`.

The product densities satisfy the telescoping estimate

`|| prod_i g_{i,k} - prod_i 1_{E_i} ||_1
 <= sum_i ||g_{i,k}-1_{E_i}||_1 ->0`,

because every factor has `L^1` norm one. Pushforward by `x -> x^T A x` contracts total variation, so for every interval `I`,

`mu_E(I)=lim_k mu_{g_k}(I)`.

By definition of `C_sm`,

`mu_{g_k}(I)<=C_sm |I|`.

Hence `mu_E(I)<=C_sm|I|`, and inserting this **actual inequality** into the partner mixture gives

`mu_f(I)=int mu_E(I)dPi(E) <= C_sm |I|`.

Taking the supremum over the full target class yields `C_full<=C_sm`. QED.

### Consequence

The hard universal constant can be attacked on smooth compactly supported product inputs with no loss whatsoever. This is stronger than merely assuming an output mollification: the matrix, dimension, quadratic form and input dimension are unchanged.

## 4. Every member of the exact reduced class has a continuous output density

The pointwise oscillatory-decay correction concerns a bound uniform over *all* cap-one input laws. For one fixed smooth compactly supported input, ordinary quadratic stationary phase is valid. This gives a clean target-level regularity statement.

### Theorem 4.1 — `QFORM-SMOOTH-INPUT-C0-v1`

Let `F in C_c^infinity(R^n)` be any probability density, not necessarily a product density. Let `A` be real symmetric of rank `r>=3`. Then `Q=X^T A X`, `X~F`, has a bounded continuous density `p_Q in C_0(R)`. In particular every instance in the smooth reduced QFORM class has a continuous density.

### Proof

Choose an orthogonal matrix `O` such that

`O A O^T = diag(Lambda,0)`,

where `Lambda` is the invertible `r x r` diagonal matrix of nonzero eigenvalues. Write `Ox=(z,w)` with `z in R^r`. The rotated joint density remains smooth and compactly supported. Integrating out the null variables gives

`h(z)=int F(O^T(z,w)) dw in C_c^infinity(R^r)`,

with `int h=1`. Hence the characteristic function of `Q` is

`phi(s)=int_R^r exp(i s z^T Lambda z) h(z) dz`.

Use the Fourier convention

`hat h(xi)=int exp(-i xi dot z) h(z) dz`,

`h(z)=(2pi)^(-r) int exp(i xi dot z) hat h(xi) dxi`.

Because `h` is smooth and compactly supported, `hat h in L^1`. For `s !=0`, the exact Fresnel integral gives

`| int exp(i s z^T Lambda z + i xi dot z) dz |
 = pi^(r/2) |s|^(-r/2) |det Lambda|^(-1/2)`.

Therefore

`|phi(s)|
 <= B(h,Lambda) |s|^(-r/2)`,

where

`B(h,Lambda)=2^(-r) pi^(-r/2) |det Lambda|^(-1/2) ||hat h||_1`.

Also `|phi(s)|<=1`. Since `r>=3`, `r/2>1`, so

`int_R |phi(s)| ds < infinity`.

Fourier inversion now defines

`p_Q(t)=(2pi)^(-1) int_R exp(-ist) phi(s) ds`.

The inverse Fourier transform of an `L^1` function is bounded, uniformly continuous and vanishes at infinity. This is the density of `Q`, proving the theorem. QED.

### Scope and correction compatibility

The constant `B(h,Lambda)` depends on the individual smooth input through `||hat h||_1` and on the nonzero spectrum through `|det Lambda|`; it is **not** uniform over the QFORM class. Along the cap-preserving approximations from Lemma 2.1, smoothness norms may blow up. Thus this theorem does not resurrect the refuted law-uniform pointwise decay claim and does not prove the universal density constant.

## 5. What this changes

The central theorem may now be stated equivalently as follows:

> Find a finite universal `C` such that `||p_{X^TAX}||_infinity<=C` for every target matrix `A` and every collection of **smooth compactly supported** independent densities `f_i` satisfying `0<=f_i<=1`, `int f_i=1`.

Every output in this exact reduced class is already a bounded continuous function individually. Hence future Fourier/coarea proofs are allowed to perform pointwise inversion and smooth manipulations on the input **provided every final estimate is independent of input smoothness seminorms and support size**. That uniformity is exactly the unpaid part.

The additional claim that the original rough-input output always has a continuous representative remains open. The partner's counterexample shows that no law-uniform modulus can be used to pass this continuity through the exact approximation above.

## 6. First unpaid implication

The full conjecture is still open. The first substantive inequality is now sharply isolated:

`sup_{n,A,(f_i smooth cap-one),I} P(X^TAX in I)/|I| < infinity`,

where `A` has at least three eigenvalues of modulus at least one. Any proof may use smooth Fourier inversion instance-by-instance, but it must eliminate the dependence on `||hat h||_1`, support diameter, derivatives of `f_i`, and small nonzero eigenvalues not protected by the three-large-eigenvalue hypothesis.

A proof of individual continuity for every rough product-indicator extreme output would still upgrade the full result to a continuous representative via fleet02/B15's exact Choquet continuity transfer, but that is a separate stronger objective.

**Full QFORM status:** `OPEN_NOT_PROVED`.
