# account01/B15 — fixed-multiplicity full audit, auto11 r14

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and materials read

Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.

`manuscript.tex` was read in full, source lines 1--790. The fetched blob is `183ccd294763214e6a707e8d4749ff9a8cf7006d`, agreeing with the declared SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69` in `SOURCE_MANIFEST.json`.

I also read in full `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. The current checker output records PASS on its finite suite. I read the checker and its recorded output but did not independently execute Python in this invocation, so **execution of verify.py in this invocation is UNCHECKED**. The older finite-test counts in historical `AUDIT.md` are likewise **UNCHECKED historical evidence**, because the current manifest explicitly says the new checker is a different suite.

## Fatal defects first

**None found in the mathematical proof of the pinned 17-direction theorem.**

One nonfatal notation/presentation gap remains in the main proof: the expression `||A/B||>=1` in lines 726--749 uses notation `A/B` that is not defined elsewhere. The preceding sentence identifies the intended object as the Schur complement of the chosen principal pair, and Lemma `lem:schur` proves that this Schur complement has at least fifteen eigenvalues of modulus at least one. Replacing `||A/B||` by `||S||`, where `S` denotes that Schur complement, closes the notation issue with no mathematical change.

I do **not** regard the product-projection entropy line as a mathematical gap. Although factors with `b_i=0` are dropped from the product, the proof explicitly permits adding the zero left contribution `-b_i log b_i=0` for such indices before summing `1-b_i`; over all original coordinates `sum_i(1-b_i)=d` is exact. At worst this sentence can be made more explicit.

## End-to-end source ledger

| Source lines | Object | Verdict | Reason |
|---|---|---|---|
| 1--46 | Preamble, abstract, conventions | PASS | Quantifiers and claimed scope agree with the proof; no hidden support, moment, smoothness, identical-law, or rotation-independence assumption. |
| 47--57 | Main theorem | PASS | Precise target is `s_17(A)>=s`, arbitrary affine terms, independent cap-`K` laws, essential density `<=10^4 K^2/s`. |
| 59--61 | 33-direction corollary | PASS | `s_17>=s_33`. |
| 62--90 | Architecture and normalization | PASS | `eta=1/100`, `kappa=80^-2`, and the 9/17 roles are consistent downstream. |
| 91--120 | Fourier identities / Gaussian regularization | PASS | With `hat f(t)=int e^{itx}f(x)dx`, Plancherel has factor `2pi`, inversion `1/(2pi)`, and `g_eps` transforms to `e^{-eps t^2}`. The Gaussian identity coefficient is exactly `1/(2 sqrt(pi v))`. Approximate-identity and dominated-convergence steps are valid. |
| 122--130 | Power envelope | PASS | Envelope integral is `2ap/(p-1)` and inversion gives `ap/[pi(p-1)]`. |
| 132--160 | Negative half moments / Riesz | PASS | Gamma representation and Gaussian inversion give exactly `1/sqrt(2pi) int |t|^-1/2 |phi(t)|dt`; the `3/4` envelope gives weighted integral `12 sqrt(u)`. Tonelli is legitimate with extended nonnegative values. |
| 161--181 | Singular values and rank perturbation | PASS | Approximation-number proof works for nonsymmetric matrices and is used in the correct direction. |
| 183--207 | Schur spectral count | PASS | Invertible case follows from inverse principal compression. The singular limiting argument is valid: if `q=N_A(t)-k`, then `s_q(S_eps)>=t-|eps|`; ordered eigenvalue-modulus continuity yields `s_q(S)>=t`. |
| 209--217 | Strict diagonal dominance | PASS | Standard row argument, valid without symmetry. |
| 221--255 | Geometric rank-one BL | PASS | Heat-flow derivative has correct nonnegative sign from the Parseval-frame contraction; boundary/integration-by-parts, large-time Gaussian limit, Fatou, and monotone truncation close the rough-input proof. |
| 258--282 | Product projections | PASS | Orthogonal change is only in a deterministic marginal integral. BL scaling is correct and gives `e^{d/2}`. No independence of rotated coordinates is asserted. |
| 284--301 | Integrated scalar Fourier powers | PASS | `m=floor(p/2)>=p/4`; `|hat f|^{2m}` is integrable via `|hat f|<=1` and Plancherel; inversion plus the literal-coordinate projection estimate gives the stated constant. |
| 302--324 | Cross-form setup and decoupling | PASS | Independent copies are of literal original-coordinate banks; pure phases are removed only after Cauchy--Schwarz/modulus. Jensen gives the fourth-power form. |
| 326--373 | Regularized crossing determinant | PASS | Frame vectors, `c_j,d_i`, trace identity, BL Jacobians, scalar Fourier exponent `2/d_i`, cancellation at `alpha=(2pi e)^2`, and fourth-root determinant exponent `-1/8` all check. |
| 374--400 | Crossing volumes and envelopes | PASS | Cauchy--Binet expansion is correct. Order five gives exponent `5/4>1`, hence `L^1` Fourier inversion and bounded continuous density. Order three gives exponent `3/4`, which is *not* integrable by itself but becomes integrable after the Riesz weight `|t|^-1/2`, since the tail exponent is `5/4`. The manuscript keeps these conclusions separate. |
| 404--414 | Scalar square profile | PASS | Two inverse branches and the interval preimage length are correct. |
| 415--422 | Conditional square domination | PASS | Correctly a measure/test-function domination; no false independence claim between square and Schur remainder. |
| 423--434 | Definite pair | PASS | Two-dimensional change of variables gives `pi M/sqrt(|det B|)`; rotated independence is not used. |
| 437--482 | Hyperbolic pair | PASS | Hyperbola parametrization and Jacobian `1/(2sqrt D)` are correct. Tail choice uses a physical coordinate; cap/mass rearrangement and the middle interval produce the logarithmic envelope. Critical level is handled only a.e./through nonnegative test functions. |
| 485--525 | Quarter-power concentration | PASS | Diagonal branch is direct. The sign partition produces a literal cross block with norm at least `L/4`; the determinant theorem gives the `|t|^-1/4` envelope. Gaussian smoothing constants check, and layer cake gives `4+4 log16`; no atom remains. |
| 528--535 | Pivot/volume definition | PASS | Ordered disjoint-minor convention is used consistently. |
| 536--544 | No-pivot entry bounds | PASS | `|a_ij|^2<eta^2+eta<1/49` at the selected parameters. |
| 545--564 | Volume-sampled interpolation | PASS | Bordered determinant identity is exact on nonsingular seeds; singular seeds justify an inequality, not equality. Nonsymmetric interpolation and seed row/column identities are correct. |
| 566--580 | Completion | PASS | `D` vanishes on the seed, `E` is off-diagonal on `LxL`, `R_LL=P_LL`, restricted rank `<=r`, global rank `<=3r`; no symmetry of the auxiliary matrices is needed. |
| 582--619 | Spectral-to-volume proposition | PASS | Bad volume gives a bad successive ratio. Rank subtraction forces `r+1` large diagonal entries in `L`; exact diagonal-dominance slack is `371/400-23/28=297/2800>0`, contradicting restricted rank `r`. |
| 621--630 | Random cut | PASS | Every ordered disjoint `(S,T)` survives with probability `4^-k`. |
| 632--645 | No-pivot analytic consequences | PASS | Order three pays full half potential `<200`; order five pays density `<2400`. This is the key threshold separation. |
| 646--674 | Truncated potential / singular kernels | PASS | `J(d)` near/far split and the centered-interval logarithmic rearrangement are valid with safe constants. |
| 676--714 | Pivot truncated half potential | PASS | Scalar, definite-pair, indefinite-pair alternatives are exhaustive; all conditionally obtained bounds are uniform in induced affine terms and averaged by Tonelli. |
| 716--724 | Nine-direction half-potential | PASS | Pivot/no-pivot split is complete; adding the outside-unit tail costs at most one. |
| 726--749 | Main theorem proof | PASS with nonfatal notation GAP | No-pivot, scalar, definite and indefinite branches close; scaling is correct. `A/B` should be renamed to the already-described Schur complement. No proof implication depends on the notation. |
| 750--778 | Threshold accounting | PASS | Correctly distinguishes order-three half-potential from order-five density and records the precise dependencies. |
| 779--785 | Regularity/independence remark | PASS | Only no-pivot is claimed continuous; pivot branches are essential-`L^infinity` measure domination. No spectral independence or uniform rough quadratic-phase decay is claimed. |
| 786--790 | Acknowledgment / bibliography | PASS | No mathematical dependency is hidden here. |

**No mathematical line remains UNCHECKED in this audit. No mathematical statement is marked FALSE.** The only UNCHECKED items are this invocation's non-execution of `verify.py` and historical finite-test counts that the current manifest says are not reproduced by the new suite.

## B15 analytic reconstruction: the two Fourier thresholds

The exact distinction can be summarized without any appeal to regularity folklore. If a crossing volume of order `k` gives

`|phi_Q(t)| <= min(1,(u/|t|)^(k/4))`,

then:

- `k=3`: exponent `3/4<1`, so direct Fourier inversion does **not** give a bounded density. But the Riesz representation inserts `|t|^-1/2`, and `3/4+1/2=5/4>1`, yielding a uniform negative-half-potential bound.
- `k=4`: exponent `1` is the exact absolute-inversion endpoint; it can yield strong `L^2`/weak regularity but not a bounded density by absolute inversion alone.
- `k=5`: exponent `5/4>1`, so `phi_Q in L^1`, yielding a canonical `C_0` density and the essential height bound.

Thus the manuscript's global theorem is correctly only an essential `L^infinity` statement. Continuity in the pivot branches is not proved by the manuscript and is not needed for the theorem.

## Threshold status after reading current improvements

The pinned 17-direction theorem is sound in this audit. A separate complete replacement proof currently on `master` lowers the same arbitrary-law theorem to **nine directions**, with no weakening of the original hypotheses. I read that replacement and the independent full-review artifacts; I do not self-award release/validation status here. Multiplicity eight remains an analytic GAP in the current overlap/masked-collar receiver, and the unrestricted three-direction problem remains OPEN.

This audit does not modify the pinned manuscript.
