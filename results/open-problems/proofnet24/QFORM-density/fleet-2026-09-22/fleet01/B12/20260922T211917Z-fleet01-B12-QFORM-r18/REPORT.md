SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-22T21:19:17Z.
attacking: additional-eigenvalue control by affine closure, principal-compression induction, and arbitrary ambient completion of the fleet02/B12 rank-one boundary family.

# QFORM additional-eigenvalue control: affine-hereditary reduction

Status: **PROVED_SUPPORTING_THEOREM; FULL TARGET OPEN.**

Control source at start: `yspennstate/math-research-brain@9bcab90c6a6c42bf73e8e4cb60bc3ecdb006ddb2`, owner-control revision `2026-09-22.15`, programme `QFORM-DENSITY-3EIG-20260922`. Fresh corrections consumed before publication include the no-independence-after-rotation rule, the false arbitrary-joint coarea gate, the false normalized conditional-fiber gate, the false local-cross-rank-three dichotomy, and the fixed-Schur-pivot failure mechanisms. No such premise is used below.

The target is: for independent real coordinates with densities at most one and symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal `L^infinity` density bound. The arguments here preserve original-coordinate independence and prove only supporting reductions, not the full target.

## 1. Affine closure of any lower-dimensional full theorem

### Lemma 1 (affine closure at fixed spectral threshold)
Fix `L>0` and dimension `d`. Assume the following pure-quadratic statement with constant `C`:

> for every symmetric `d x d` matrix `M` with at least three eigenvalues satisfying `|lambda|>=L`, and every independent cap-one input `X`, the law of `X^T M X` is dominated by `C/L` times Lebesgue measure.

Then for every vector `b` and scalar `c`, the affine quadratic

`Z = X^T M X + b^T X + c`

also satisfies

`P(Z in I) <= (C/L)|I|`

for every interval `I`. Hence `Z` has a density with essential supremum at most `C/L`.

### Proof
For `eta>0`, put `s=1+eta`. Choose a sequence `eps_m ->0` such that

`|eps_m| < eta L/2`

and `M_m=sM+eps_m I` is invertible. This is possible because only finitely many values of `eps` make `sM+eps I` singular.

Every target eigenvalue `lambda` of `M` with `|lambda|>=L` obeys

`|s lambda + eps_m| >= (1+eta)L-eta L/2 > L`,

so `M_m` still has at least three `L`-large eigenvalues. Since `M_m` is invertible,

`x^T M_m x+b^T x+c = (x+h_m)^T M_m (x+h_m)+c_m`,

where `h_m=(1/2)M_m^{-1}b`. Translation preserves independence and the coordinate density cap, so by hypothesis each regularized affine law is dominated by `(C/L) dx`.

As `m->infinity`, the random variables converge almost surely to

`s X^T M X+b^T X+c`.

A weak limit of probability measures each dominated by `(C/L) dx` is again dominated by `(C/L) dx`: for every open interval `J`, Portmanteau gives

`mu(J) <= liminf_m mu_m(J) <= (C/L)|J|`,

and open-set decomposition plus outer regularity gives the domination for all Borel sets. Thus the `s`-scaled affine quadratic has the same density cap. Finally let `eta downarrow0`; the same weak-limit argument gives the claim for `M` itself. QED.

This lemma is important because conditioning on an original coordinate produces an affine quadratic form, not a pure one.

## 2. Principal-compression induction: all sufficiently many extra large eigenvalues are free

For a symmetric matrix `A`, define

`p_L(A)=#{lambda_j(A)>=L}`,
`q_L(A)=#{lambda_j(A)<=-L}`.

### Theorem 2 (hereditary reduction of extra large eigenvalues)
Assume the full pure-quadratic QFORM theorem with constant `C` is already known in every dimension `< n` at threshold `L`. Let `A` be an `n x n` symmetric matrix. If

`(p_L(A)-1)_+ + (q_L(A)-1)_+ >=3`,

then for every independent cap-one input `X`,

`||p_{X^T A X}||_infinity <= C/L`.

In particular, the condition holds whenever either

1. `p_L(A)+q_L(A)>=5`, or
2. `p_L(A)>=4`, or
3. `q_L(A)>=4`.

### Proof
Delete any original coordinate `i` and write the corresponding principal compression as `B=A_{\hat i,\hat i}`. Cauchy interlacing separately above `+L` and below `-L` gives

`p_L(B)>=p_L(A)-1`,
`q_L(B)>=q_L(A)-1`.

Hence the displayed hypothesis implies that `B` has at least three eigenvalues of modulus at least `L`.

Condition on the deleted original coordinate `X_i=x`. The remaining coordinates stay independent and retain their cap-one densities, while

`X^T A X = Y^T B Y + ell_x^T Y + c_x`

for `Y=X_{\hat i}` and deterministic `ell_x,c_x` depending on `x`. By the induction hypothesis in dimension `n-1` and Lemma 1, every conditional law obeys

`P(X^TAX in I | X_i=x) <= (C/L)|I|`

for every interval `I`, uniformly in `x`. Integrating over `X_i` gives the same inequality unconditionally. QED.

### Consequence: only seven spectral signatures are irreducible by this mechanism
For the threshold `L=1`, an induction proof of the full conjecture never needs a genuinely new argument for matrices with five or more large eigenvalues, nor for four or more large eigenvalues of one sign. After Theorem 2, the only spectral-count patterns not automatically inherited from lower dimension are

`(p,q) in {(3,0),(2,1),(1,2),(0,3),(3,1),(2,2),(1,3)}`.

Thus arbitrary additional large eigenvalues are reduced to at most **one extra large direction beyond the required three**, and arbitrary sub-threshold eigenvalues of either sign are already allowed throughout. This is an exact original-coordinate reduction; no eigenbasis independence is asserted.

Regularity note: the argument proves essential boundedness. Even if the lower-dimensional theorem supplies continuous densities, weak-limit affine closure as used here does not by itself prove continuity, so continuity remains separate.

## 3. Direct consumption of fleet02/B12: ambient-completion theorem for its rank-one boundary family

Named partner dependency consumed:

with canonical mathematics at
`yspennstate/math-open-problems@5295a978b9e3336cc823f0e631bde093c30a8a4d:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T1953Z-fleet02-B12-qform-r16/REPORT.md`.

That completed partner result proves the following for

`D_tau = 2 sigma I_4 + (tau-2 sigma) vv^T`,
`sigma in {+1,-1}`, `v=(sqrt(q),sqrt(1-q),0,0)`, `0<q<1`, `tau in R`:

`||p_{Y^T D_tau Y}||_infinity <= C_*/2`,

for every four-dimensional independent cap-one source, where

`C_*=24.183038289961516...`.

The partner proof uses a certificate switch through the physical three-coordinate block and remains uniform across the genuine Schur-pivot Möbius pole.

### Proposition 3 (affine and arbitrary ambient completion of the partner family)
For every `b in R^4` and `c in R`,

`||p_{Y^T D_tau Y+b^T Y+c}||_infinity <= C_*/2 = 12.091519144980758...`.

Consequently, let `A` be **any** larger symmetric matrix having `D_tau` as a physical `4 x 4` principal block. All entries outside that block and all cross couplings to it may be arbitrary; equivalently, all additional eigenvalues created by the ambient completion may be smaller or larger, of either sign, and of arbitrary multiplicity and magnitude. Then

`||p_{X^T A X}||_infinity <= C_*/2`.

### Proof
If `tau !=0`, `D_tau` is invertible and direct completion of the square proves the affine version immediately from the partner theorem: translation preserves independent cap-one coordinates.

If `tau=0`, regularize by `D_0+eps I`. For small `eps`, write

`D_0+eps I = s_eps [2 sigma I_4 + (tau_eps-2 sigma)vv^T]`

with `s_eps=1+eps/(2 sigma)` and `tau_eps=eps/s_eps`. The partner theorem plus scaling gives density cap `C_*/(2|s_eps|)` for every affine tilt after completing the square; this tends to `C_*/2`. Weak convergence as `eps->0` gives the same domination for `D_0`.

For an arbitrary ambient completion, condition on every coordinate outside the four-coordinate block. The conditional form in the four retained original coordinates is exactly

`Y^T D_tau Y+b(z)^T Y+c(z)`.

The affine bound above is uniform in the outside value `z`; integrating the interval small-ball inequality over `z` yields the ambient bound. No restriction is placed on the outside quadratic matrix or cross-coupling matrix. QED.

This is a direct, nonperturbative additional-eigenvalue theorem: once the partner boundary packet occurs as a physical block, an arbitrary spectral cloud elsewhere is free. It does not rely on convolution after a spectral rotation.

## 4. Relation to the full target

Theorem 2 removes all cases with at least five `1`-large eigenvalues (and all one-sign counts at least four) from the list of genuinely new induction steps. Proposition 3 pays a nontrivial family on the remaining four-large boundary, including arbitrary smaller/larger/opposite-sign fourth eigenvalue `tau` and arbitrary ambient completion.

The unpaid implication is now concentrated in the seven irreducible signatures above, especially the mixed four-large patterns `(3,1),(2,2),(1,3)` and the exact three-large patterns. One still needs a product-preserving structural mechanism (ridge/grouped-bank/physical-block/cross-packet) that treats those signatures uniformly. The present reduction does **not** prove that such a packet always exists and therefore does not solve the full conjecture.

## 5. Why this avoids the live corrections

- No rotation of the independent coordinates is performed.
- No pointwise van-der-Corput decay is used.
- No arbitrary-joint coarea lemma is used.
- No normalized conditional-fiber supremum is used.
- No fixed physical pivot is inverted in Theorem 2 or Proposition 3.
- Conditioning is only on original independent coordinates and is paid using an affine theorem with a uniform interval-density bound.

Classification: `PROVED_SUPPORTING_THEOREM_FULL_TARGET_OPEN`.
