SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T10:10:39Z.
attacking: stability under arbitrary signed spectral additions via square-order spectral clipping, plus a local-row residual perturbation.

# account03/B12 — square-order spectral clipping and threshold-projector reduction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T101039Z-qform-eigenvalue-r54`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY/REDUCTION THEOREMS; FULL QFORM OPEN**  
Continuity: **proved on the positive five-square-mode branch below; unrestricted continuity remains open.**  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and corrections retained

The owner target remains: independent ORIGINAL coordinates with arbitrary scalar probability densities bounded by one, an arbitrary real symmetric coefficient matrix, and only the hypothesis that at least three eigenvalues have absolute value at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, or diagonal-basis assumption is used below. No rotation of the random vector is made.

The live corrections were reread immediately before publication. In particular, this report does **not** use uniform pointwise van-der-Corput decay, arbitrary-joint coarea, post-rotation independence, a fiber-supremum argument, or the claim that a small coefficient perturbation is a small independent random quadratic error.

The new observation is entirely deterministic and acts on the square Gram matrix of a physical ORIGINAL-coordinate carrier.

## 2. Square-order monotonicity on every physical carrier

Let `P=P_H : R^m -> R^n` be the coordinate embedding of a literal ORIGINAL-coordinate set `H`, and let `A,B` be real symmetric `n x n` matrices.

### Theorem 2.1 — `QFORM-SQUARE-ORDER-PHYSICAL-CARRIER-v1`

If

`A^2 >= B^2`

in Loewner order, then for every `1 <= k <= m`,

`boxed: lambda_k((A^2)[H,H]) >= lambda_k((B^2)[H,H])`,

or equivalently

`boxed: s_k(A P) >= s_k(B P)`.

Here eigenvalues and singular values are ordered decreasingly.

### Proof

Because `P` is a coordinate isometry,

`(A P)^T(A P)=P^T A^2 P`,

and likewise for `B`. The Loewner hypothesis gives

`P^T A^2 P - P^T B^2 P = P^T(A^2-B^2)P >= 0`.

Monotonicity of each ordered eigenvalue under Loewner order gives

`lambda_k(P^T A^2 P) >= lambda_k(P^T B^2 P)`.

Taking square roots yields the singular-value statement. QED.

The point is that this comparison is about the **final coefficient matrix**. It says nothing of the form `X^T A X = X^T B X + independent noise`, and no such statement is needed.

## 3. Arbitrary signed spectral clipping is free

Write the final matrix spectrally as

`A = U diag(lambda_1,...,lambda_n) U^T`.

Choose any real numbers `mu_j` satisfying only

`|mu_j| <= |lambda_j|`,

with arbitrary signs, and define the proxy

`B = U diag(mu_1,...,mu_n) U^T`.

Then

`A^2-B^2 = U diag(lambda_j^2-mu_j^2) U^T >= 0`.

Theorem 2.1 therefore yields, on **every** ORIGINAL-coordinate carrier `H`,

`boxed: s_k(A P_H) >= s_k(B P_H)` for all `k`.

This gives a dependence-safe reduction for additional spectrum:

- unwanted eigenvalues of the final `A` may be set to zero in the proxy;
- large eigenvalues may be clipped to any smaller magnitude;
- proxy signs may be selected conveniently because only squares matter;
- every final eigenvalue omitted by the proxy may have arbitrary sign and arbitrary magnitude;
- increasing the absolute value of any eigenvalue, even after a sign flip, cannot destroy a previously established physical square-energy certificate.

This is the precise sense in which arbitrary additional smaller/larger eigenvalues of either sign can be harmless: one proves a carrier certificate for a spectrally clipped proxy and transfers that certificate to the actual final matrix by square order, not by convolution.

### Corollary 3.1 — orthogonal spectral-complement addition

If `B,E` are real symmetric and `BE=EB=0`, then

`(B+E)^2=B^2+E^2 >= B^2`.

Therefore every physical carrier singular-value lower bound for `B` survives addition of **arbitrary** spectrum in the orthogonal spectral complement. The rank, signs and magnitudes of `E` are unrestricted.

## 4. Threshold-projector reduction

For a final symmetric `A`, let

`Pi_tau = 1_{|A| >= tau}`

be the spectral projector onto eigenvectors whose eigenvalues have absolute value at least `tau`. Since

`A^2 >= tau^2 Pi_tau`,

Theorem 2.1 gives the coordinate-free-to-physical conversion

`boxed:
 s_k(A P_H)
 >= tau sqrt(lambda_k(P_H^T Pi_tau P_H)).`

This is useful because all magnitude information is now separated from one purely geometric quantity: the compression of a spectral projector to ORIGINAL coordinates. Arbitrarily many further eigenvalues above the threshold, of either sign and any magnitude, can only improve the square-order certificate. Eigenvalues below the chosen threshold are simply not used in this lower bound.

A direct structural consequence is:

- if `rank Pi_tau <= 4`, then `A` is a rank-at-most-four high-spectrum matrix plus a symmetric tail of operator norm `< tau`;
- if `rank Pi_tau >= 5` and some bounded physical set `H`, `|H|=m`, has `lambda_5(P_H^T Pi_tau P_H)>=beta`, then the final matrix has a five-square-mode carrier with scale `tau sqrt(beta)`.

This does **not** assert that the bare target hypothesis automatically supplies such an `H`; that remains a structural gap.

## 5. Arbitrary noncommuting remainder: charge only local row action

The square-order comparison can be followed by a completely arbitrary symmetric residual.

### Theorem 5.1 — `QFORM-SQUARE-ORDER-PLUS-LOCAL-TAIL-v1`

Suppose `A_spec^2 >= B^2` and

`A = A_spec + T`,

where `T=T^T` is arbitrary. Put

`epsilon_H = ||T P_H||_op`.

Then for every `k <= |H|`, rectangular Weyl gives

`boxed:
 s_k(A P_H)
 >= [s_k(B P_H)-epsilon_H]_+.`

No bound on the complement-only block of `T` is required, and `||T||_op` may be arbitrarily large if its action on the selected physical carrier is small.

Again this is only a deterministic coefficient inequality. It never treats `X^T T X` as an independent random error.

## 6. Density-level stability through the completed five-mode compiler

Use the completed account03/B12 result

- repository/commit: `yspennstate/math-open-problems@7fa8e2a00f932cb7ed6e68da9dbd07725c24d0f1`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T031535Z-qform-eigenvalue-r47/REPORT.md`;
- theorem: `QFORM-FIVE-SQUARE-MODE-E3-CORE-COMPILER-v1`.

For a literal physical carrier `H`, `m=|H|>=5`, it proves that

`lambda_5((A^2)[H,H]) >= g^2 >0`

implies

`||p_(X^T A X)||_infinity <= sqrt(24*pi*m+K3^2)/g`,

where

`K3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,

and the density has a continuous representative in `C_0(R)`.

Combining that theorem with Theorem 5.1 gives:

### Corollary 6.1 — `QFORM-SPECTRAL-CLIPPING-FIVE-MODE-DENSITY-STABILITY-v1`

Let `A=A_spec+T`, `A_spec^2>=B^2`, and let `H` have size `m>=5`. If

`g = s_5(BP_H)-||TP_H||_op >0`,

then for every independent cap-one product law,

`boxed:
 ||p_(X^T A X)||_infinity
 <= sqrt(24*pi*m+K3^2)/g,`

and the density is continuous and vanishes at infinity.

The spectral proxy `B` can be any clipping of `A_spec`; all omitted spectral modes are unrestricted in sign and magnitude.

## 7. Required account04/B12 application at an actual inequality

Apply the completed partner theorem

- `yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T002154Z-account04-B12-multihub-shear-r8/REPORT.md`;
- theorem `QFORM-MULTIHUB-ALIGNED-SPECTRAL-PACKET-STABILITY-v1`.

For a six-coordinate physical carrier, take its parameters

`m=6, p=2, ell=4`,

`s_2(Lambda)>=4`, `s_4(R)>=2`, and

`||Lambda^(-1) W^T||_op <= 1/2`.

The partner's proved multihub shear inequality gives the actual proxy-carrier bound

`s_6(BP_H)
 >= gamma(1/2)*min(4,2)
 = (sqrt(17)-1)/2
 = 1.5615528128088303...`,

where `gamma(t)=(sqrt(t^2+4)-t)/2`.

Now replace the proxy `B` by **any spectral magnitude inflation in its own eigenbasis**: every eigenvalue can change sign; every nonzero magnitude may increase arbitrarily; every zero eigenvalue may be replaced by an arbitrary signed eigenvalue of arbitrary magnitude. Call the result `A_spec`. Then

`A_spec^2 >= B^2`,

so the new square-order theorem gives

`s_5(A_spec P_H) >= s_6(BP_H) >= (sqrt(17)-1)/2`.

Finally add an arbitrary symmetric noncommuting `T` satisfying only

`||T P_H||_op <= 1/20`.

Then

`boxed:
 sqrt(lambda_5((A^2)[H,H]))
 >= (sqrt(17)-1)/2 - 1/20
 = 1.5115528128088302... .`

The five-mode compiler therefore gives

`boxed:
 ||p_(X^T A X)||_infinity
 <= 23.74227041550599... / 1.5115528128088302...
 = 15.707205341629523... < 15.708,`

and the density is continuous and belongs to `C_0(R)`.

Thus the partner's physical multihub certificate is stable under an **unbounded amount of arbitrary signed extra spectrum in the same spectral basis**, followed by a fully noncommuting dense perturbation charged only through its local physical-row action.

## 8. Explicit partner-family matrix

A literal baseline realizing the preceding partner hypotheses is useful as a control. Take `n=18`, `H={1,...,6}`, `J={7,...,18}`. Write

`B_* = [[C,X],[X^T,0]]`,

with

`C=diag(4,4,0,0,0,0)`.

In the `6 x 12` cross block `X`, put coefficient `2` at

- `(H_1,J_5)` and `(H_2,J_6)`;
- `(H_3,J_1)`, `(H_4,J_2)`, `(H_5,J_3)`, `(H_6,J_4)`;

and zero elsewhere.

Then `Lambda=4I_2`, `s_4(R)=2`, and `||Lambda^(-1)W^T||=1/2`. The six physical row vectors are actually orthogonal, with singular values

`s(B_*P_H)=(sqrt(20),sqrt(20),2,2,2,2)`.

The full spectrum is

`{-2 (x4), 2-2sqrt(2) (x2), 0 (x6), 2 (x4), 2+2sqrt(2) (x2)}`.

So the partner bound is conservative here: exact square order already gives `s_6(A_spec P_H)>=2` for every spectral magnitude inflation, leading to the stronger no-residual cap `11.871135207752994...`. The displayed `<15.708` theorem above deliberately uses only the partner's general r8 inequality and permits a noncommuting local tail.

## 9. Deterministic numerical checks

A seeded checker (`seed=20260924101039`) performed:

1. **10,000 random spectral-clipping instances.** Random symmetric matrices were generated by random orthogonal eigenbases. Proxy eigenvalue magnitudes were random fractions of final magnitudes, with arbitrary proxy signs. For random physical carriers of size at least five, every singular index was checked against

   `s_k(AP_H)>=s_k(BP_H)`.

   Violations: `0`. Minimum observed singular-value margin: `1.1289467070100268e-06`. Minimum numerical eigenvalue of `A^2-B^2`: `7.73e-16` (floating-point roundoff scale).

2. **10,000 arbitrary spectral inflations of the explicit 18-dimensional partner family.** Final signs were chosen independently and magnitudes were increased by random log-spread amounts. Violations of the exact baseline inequality `s_6(A_spec P_H)>=2`: `0`. Minimum observed final `s_6`: `2.0000157747605813`.

These computations are sanity checks only; the theorems are the analytic Loewner/min-max and Weyl arguments above.

## 10. Exact remaining implication

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

The square-order theorem removes one genuine source of difficulty: once a useful spectral proxy has a physical five-mode certificate, *all additional same-eigenbasis spectrum can be restored for free*, regardless of sign or size, and a further noncommuting remainder costs only its local physical-row norm.

What is still unpaid under the bare hypothesis `s_3(A)>=1` is structural. At threshold `tau=1`, the spectral projector can have rank exactly three, so a five-mode carrier cannot be forced from rank alone. The next useful dichotomy is:

- lower the threshold until `Pi_tau` has at least five geometrically usable physical modes and apply the threshold-projector/five-mode compiler; or
- if `rank Pi_tau<=4`, exploit the resulting rank-at-most-four high-spectrum core plus operator-norm-`<tau` tail through one of the already-paid rank-three/four, grouped-bank, projected-crossing, ridge, hub/common-plane, Schur, or Pluecker-volume mechanisms; or
- if `rank Pi_tau>=5` but no bounded physical compression retains five modes, convert that diffuse geometry into a proved ridge/projected-crossing receiver.

This report does not claim that any one of those three exits is yet forced uniformly.

No counterexample to the full conjecture was found.
