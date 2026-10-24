# account04/B09 MOC4 report — open-gap genericization and exact fractional-linear covariance

Run: `20260922T071523Z-b09-moc4-r36`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / not proved / not disproved**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target and fresh control

For every pair of complex normal `4 x 4` matrices with spectra `a=(a_1,...,a_4)` and `b=(b_1,...,b_4)`, the target is

`det(A+B) in conv{ product_i (a_i+b_{sigma(i)}) : sigma in S_4 }`.

After diagonalizing the relative position, for a unitary `U` and a unit support direction `eta`, write

`h_{a,b,eta}(U)=Re(conj(eta) det(D_a+U D_b U*))`,

`M_{a,b,eta}=max_{sigma in S_4} Re(conj(eta) product_i(a_i+b_{sigma(i)}))`.

MOC4 fails exactly if some tuple `(a,b,eta,U)` has `h_{a,b,eta}(U)>M_{a,b,eta}`.

The final pre-write control snapshot was `b773c5f909385239a37928d6f86cbb693d785075`, OWNER CONTROL revision `2026-09-22.2`. The later owner allocation keeps B09 on MOC4 and supersedes installation/benchmark work. Required control blobs at this snapshot were: AGENTS `94387098453b9f4a9b10179183f6f6ec780fd987`, scheduled-task README `3d4a9372c87802ab734141a3374d04c8823372e3`, fleet `e647d5d2479749f80ce7bb4862bee0f28513c7d9`, roles `ed17ecc94f76720c0345b3e32249b791b20ec611`, PROTOCOL `83a9268bf5287ca203e4be69a79e25382397bca7`. The connector supplied decoded UTF-8 content and Git blob identifiers, but not a raw-byte materialization suitable for independently certifying the requested SHA-256 of the full README and extracted OWNER MESSAGE; those SHA-256 fields therefore remain unavailable rather than fabricated.

## 2. Exact peer results consumed

### Campaign lead

Consumed account03/B07 run `20260922T060726Z-account03-B07-MOC4-r11`, report `proofnet24/collective-MOC4/account03/B07/20260922T060726Z-account03-B07-MOC4-r11/REPORT.md`, theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`.

For each complementary-pair Spin(4) gate at a true-unitary global support maximizer, its mixed-Hessian quantities satisfy `T>=|C|`. Equality `T=|C|` produces a genuine coordinate `SU(2)` factor whose pair orbit is support-flat, hence an equal-support zero-entry representative.

Also consumed the newer account02/B09 sharpening `MOC4-SPIN4-SATURATION-EXCLUSION-v1` from run `20260922T064517Z-account02-B09-MOC4-r17`: a positive-gap global maximizer cannot have `T=|C|` at all, because a flat coordinate pair orbit contains a transposition endpoint and the pair-specific endpoint roof makes any such tie MOC4-safe. Thus every positive-gap global maximizer satisfies the strict inequalities `T>|C|` at all relevant left/right Spin(4) gates.

### Named assigned OTHER-account partner

Consumed account01/B07 run `20260922T060626Z-account01-B07-MOC4-r11`, report `proofnet24/collective-MOC4/account01/B07/20260922T060626Z-account01-B07-MOC4-r11/REPORT.md`, theorem `MOC4-SPECTRAL-CONDITIONED-FLAT-RIGIDITY-v1`.

In the real `Lambda^2 SU(4) ~= SO(6)` block model, for each block row `alpha`, let `L_alpha` be the `3 x 3` conditioning matrix whose rows are `(1,1,1)` and the two relevant coefficient-difference vectors. If `sigma_alpha=sigma_min(L_alpha)>0`, the partner proves at a true-unitary global support maximizer

`sum_beta (R_{alpha beta}^2-D_{alpha beta}^2)
 <= (4/sigma_alpha^2)(Q_{alpha gamma}+Q_{alpha delta})`,

where `Q_{alpha gamma}=T_{alpha gamma}^2-C_{alpha gamma}^2>=0`.

The partner further proves the exact determinant factorization

`|det L_alpha| = |eta|^2 * (spectral area of a) * (spectral area of b)`,

with, for example,

`p_1-p_2=(a_2-a_3)(a_1-a_4)`,
`p_1-p_3=(a_2-a_4)(a_1-a_3)`,

so `sigma_alpha=0` in the simple-spectrum case precisely on a real-cross-ratio (generalized-circle/line) spectral locus. Its previous proof architecture therefore left this spectral locus as an exceptional branch because the quantitative bound degenerates there.

The new theorem below removes that exceptional spectral branch from the target-level proof architecture: if any counterexample exists, a counterexample exists with both spectra away from every such locus. Consequently the partner's estimate may be used pointwise on the only counterexample regime that needs to be excluded; no uniform estimate as `sigma_alpha -> 0` is required to recover repeated, singular, or real-cross-ratio spectra.

## 3. New theorem: `MOC4-OPEN-GAP-GENERICIZATION-v1`

Define `G` to be the set of spectral pairs `(a,b) in C^4 x C^4` satisfying all of the following:

1. all `a_i` are pairwise distinct and all `b_j` are pairwise distinct;
2. no `a_i` and no `b_j` is zero;
3. for every relabelling needed by the three complementary-pair decompositions, the two denominator-free cross-ratio area polynomials are nonzero; equivalently, in the partner's notation, every row and column conditioning matrix `L_alpha` has nonzero determinant.

**Theorem.** If MOC4 fails for some complex spectra, then it fails for some `(a',b') in G`, with the **same unitary** as a witness to a strict support separation. Equivalently, it suffices to prove MOC4 for the dense generic set `G`; validity on `G` implies the theorem for all spectra, including repeated eigenvalues, zero eigenvalues, and real-cross-ratio spectra.

### Proof

Assume failure. By finite-dimensional convex separation, there are spectra `(a,b)`, a unitary `U`, and a unit support direction `eta` such that

`gamma := h_{a,b,eta}(U)-M_{a,b,eta} > 0`.

For fixed `U,eta`, the determinant term `h_{a,b,eta}(U)` is a polynomial in the real and imaginary parts of the spectral entries (after taking a real part), hence continuous. Each of the 24 endpoint support values

`H_sigma(a,b,eta)=Re(conj(eta) product_i(a_i+b_{sigma(i)}))`

is continuous, and therefore their finite maximum `M_{a,b,eta}` is continuous. Hence

`F(a,b):=h_{a,b,eta}(U)-M_{a,b,eta}`

is continuous. Since `F(a,b)=gamma>0`, there is an open neighborhood `N` of `(a,b)` on which `F>gamma/2>0`.

The complement of `G` is a finite union of proper real-algebraic sets:

- the collision sets `a_i=a_j` and `b_i=b_j`;
- the zero-coordinate sets `a_i=0` and `b_j=0`;
- the real-cross-ratio area loci. In a representative labelling the latter is the zero set of

`Im( (a_2-a_3)(a_1-a_4) * conj((a_2-a_4)(a_1-a_3)) )`,

and similarly for `b`, with finitely many relabellings. These polynomials are not identically zero, so each zero set has empty interior. A finite union of them has empty interior. Therefore every nonempty open set, in particular `N`, contains a point `(a',b') in G`.

At that point the same unitary `U` still satisfies

`h_{a',b',eta}(U) > M_{a',b',eta}`,

so `(a',b')` is another MOC4 counterexample. Compactness of `U(4)` then supplies a global support maximizer with at least the same positive gap. This proves the theorem.

### Consequence for the assigned partner theorem

At the generic counterexample obtained above, every account01/B07 conditioning matrix has `sigma_alpha>0`, so `MOC4-SPECTRAL-CONDITIONED-FLAT-RIGIDITY-v1` applies without any limiting denominator. Thus the partner's strict-margin estimate is a legitimate ingredient in a target-level contradiction proof. If that generic contradiction is proved, the theorem above automatically recovers every excluded spectral limit by contradiction: an exceptional counterexample would perturb to a generic one. No estimate uniform in `1/sigma_alpha` is needed.

This directly pays the limit-case portion of B09's integration assignment. It does **not** remove the genuinely geometric zero-entry unitary branch; a generic spectrum can still have a maximizing unitary with a zero matrix entry.

## 4. Exact structural companion: `MOC4-DUAL-MOBIUS-COVARIANCE-v1`

The partner's exceptional cross-ratio locus also has an exact normal-form interpretation.

Let complex scalars `alpha,beta,gamma,delta` satisfy `alpha*delta-beta*gamma != 0`. Let denominators below be nonzero and define

`a_i = (alpha*x_i+beta)/(gamma*x_i+delta)`,

`b'_j = (beta+delta*b_j)/(alpha+gamma*b_j)`.

Then for **every** unitary `U`,

`det(D_a+U D_b U*)
 = C det(D_x+U D_{b'} U*)`,

where

`C = product_j(alpha+gamma*b_j) / product_i(gamma*x_i+delta)`.

Moreover, for every permutation `sigma`,

`product_i(a_i+b_{sigma(i)})
 = C product_i(x_i+b'_{sigma(i)})`.

Hence the entire MOC4 range and all 24 endpoint products transform by the same nonzero scalar. Convex-hull containment is exactly invariant under this dual fractional-linear transformation.

### Proof

Set `B_U=U D_b U*`. Since

`D_a (gamma D_x+delta I)=alpha D_x+beta I`,

we have

`(D_a+B_U)(gamma D_x+delta I)
 = (alpha I+gamma B_U)D_x + (beta I+delta B_U)`.

Taking determinants and factoring the first operator gives

`det(D_a+B_U) product_i(gamma*x_i+delta)
 = det(alpha I+gamma B_U)
   det(D_x+(alpha I+gamma B_U)^(-1)(beta I+delta B_U))`.

Because both factors in the last rational expression are functions of the same normal matrix `B_U`, functional calculus gives

`(alpha I+gamma B_U)^(-1)(beta I+delta B_U)=U D_{b'} U*`,

and `det(alpha I+gamma B_U)=product_j(alpha+gamma*b_j)`. This proves the determinant identity.

The endpoint identity follows termwise from

`a_i+b_j = ((alpha+gamma*b_j)/(gamma*x_i+delta)) (x_i+b'_j)`.

The same scalar `C` therefore multiplies every endpoint and every true-unitary determinant value. QED.

If a simple spectrum has real cross ratio, classical fractional-linear geometry permits a transformation sending its four points to a generalized real line. The theorem above shows that this normalization must simultaneously transform the other spectrum by the dual rule; it is a useful exact normal form but **not** by itself a proof of the one-Hermitian MOC4 subproblem. The genericization theorem is what makes a separate solution of this exceptional locus unnecessary for full MOC4.

## 5. Exact arithmetic verification used

A standard exact-rational check was performed with the Hadamard orthogonal matrix `U=H_4/2`,

`x=(0,1,2,3)`, `b=(1,2,4,5)`,
`(alpha,beta,gamma,delta)=(2,1,1,3)`.

It gives

`a=(1/3,3/4,1,7/6)`,
`b'=(4/3,7/4,13/6,16/7)`,
`C=7/5`,

`det(D_a+U D_b U^T)=13429/96`,
`det(D_x+U D_{b'} U^T)=67145/672`,

and `(7/5)*(67145/672)=13429/96`. All 24 permutation endpoint identities also matched exactly. The captured output is `verification.txt` in this run directory. The algebraic proof above does not depend on the example.

The exact check used rational Gaussian elimination and the following core computation (all arithmetic `Fraction`):

```python
a = [(alpha*z+beta)/(gamma*z+delta) for z in x]
bp = [(beta+delta*z)/(alpha+gamma*z) for z in b]
C = prod(alpha+gamma*z for z in b) / prod(gamma*z+delta for z in x)
B = U @ diag(b) @ U.T
Bp = U @ diag(bp) @ U.T
assert det(diag(a)+B) == C*det(diag(x)+Bp)
for sigma in permutations(range(4)):
    assert prod(a[i]+b[sigma[i]] for i in range(4)) == \
           C*prod(x[i]+bp[sigma[i]] for i in range(4))
```

No floating-point tolerance is involved.

## 6. Compact conditional end-to-end argument after this run

Assume MOC4 fails.

1. `MOC4-OPEN-GAP-GENERICIZATION-v1` supplies a counterexample with simple nonzero spectra, all cross-ratio conditioning determinants nonzero, and a positive support gap.
2. Choose a true-unitary global support maximizer for that support functional.
3. By account02/B09 `MOC4-SPIN4-SATURATION-EXCLUSION-v1`, every left/right mixed-conformal Spin(4) gate at this maximizer is strict: `T>|C|`.
4. By the assigned partner account01/B07 `MOC4-SPECTRAL-CONDITIONED-FLAT-RIGIDITY-v1`, every block-row/column nonconformality is quantitatively controlled by the adjacent strict `Q=T^2-C^2` margins, with finite pointwise constants because every `sigma_alpha>0`.
5. The target-level contradiction is therefore reduced to the **genuine unitary geometry**, not a spectral limit: exclude a positive-gap generic maximizer on (a) the zero-entry strict-pair branch, using the exact residual `U(2)`/quaternion reserve, and (b) the no-zero strict interior branch, using the full same-unitary `P/R/D`, subgroup-roof, Cartan, stationarity and mixed-Hessian constraints.

If those two generic geometric implications are proved, full MOC4 follows immediately by step 1, including every repeated and singular spectrum. No additional spectral-boundary theorem is then required.

## 7. First remaining essential implication

The first boundary obligation remains the source-valid strict zero-face statement isolated by account02/B09, now with spectral exceptional cases removed:

**`MOC4-GENERIC-ZERO-FACE-STRICT-RESERVE-v1`.** For generic spectra as in `G` and arbitrary support direction, there is no genuine global maximizer `U_*` with a zero entry and positive gap `gamma` satisfying all strict coordinate-pair gaps and the exact residual quaternion-fiber/Haar-reserve identities.

In parallel, the no-zero branch requires a strict-interior payment theorem combining the partner's finite-`sigma_alpha` nonconformality bounds with the lead's full mixed-Hessian and subgroup constraints. Neither implication is proved here, so there is no full-proof candidate and no truth promotion.

## 8. Verdict and integrity

**ESSENTIAL_STEP_APPLIED.** The spectral limit/real-cross-ratio exceptional branch is eliminated from the target-level proof by a strict-gap density argument, and the named assigned OTHER-account theorem is thereby integrated without requiring uniform conditioning. The dual fractional-linear covariance supplies an exact structural normal form and an independent algebraic cross-check.

Full MOC4 remains open because the generic strict zero-face and generic strict no-zero unitary-orbit contradictions remain unpaid.

Scoped privacy/provenance review: this report contains only the owner-authorized MOC4 target, exact peer theorem statements from the private mathematical coordination repository, and harmless exact rational calculations. It contains no benchmark gold or keys, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive material, paid-model/API output, remote-workflow output, or public release action.
