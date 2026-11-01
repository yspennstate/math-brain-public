SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T04:52:00Z.
attacking: balanced weak-direction routing by identifying the exact two-physical-row component of ridge volume sampling and transferring it to the already-proved E2 half-Riesz smoother.

# fleet01/B04 auto12 — ridge volume decomposes exactly into E1/E2/E3 physical-volume laws

Programme: `QFORM-DENSITY-3EIG-20260922`. Fresh prepublication owner control: revision `2026-09-22.15`, QFORM only.  
Outcome: `ESSENTIAL_STEP_APPLIED / NEW_STRUCTURAL_IDENTITY_AND_TRANSFER / FULL_TARGET_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is **not proved** here. The new result below is a product-coordinate structural transfer: in a three-column physical cross block, the regularized ridge leverage is exactly a mixture of the canonical one-, two-, and three-volume row marginals. This turns the newest fleet02/B04 virtual-volume identity into an explicit criterion under which a genuine original scalar square plus aggregate rank-two cross volume yields a universal density bound even when the ridge effective dimension is below two. The resulting density conclusion is an essential-supremum statement; continuity is not proved by this splice.

No Gaussianity, moments, compact support, connected support, log-concavity, independence after a spectral rotation, arbitrary-joint coarea bound, worst conditional projection-density cap, fixed good minor, or law-uniform pointwise quadratic-phase decay is used.

## 1. Source boundary and mechanism change

The early checkpoint of this run started to rederive a weighted E2 half-Riesz theorem. A source-match search then located the already-completed fleet01/B04 theorem `QFORM-SQUARE-ENTROPY-E2-HALFRIESZ-v1` in

`yspennstate/math-open-problems@e6cb03b671784bc5ea61a293144b6c3731b942a5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T024533Z-fleet01-B04-QFORM-auto12/REPORT.md`.

That report already proves, for a scalar-square representation

`Q = a (Z+d(Y))^2 + R(Y)`, `a != 0`,

and a residual cross block `M`, the optimized two-volume estimate

`||p_Q||_infinity
 <= [8 e^(1/4) q^(-1/4)/(2-q)]
    |a|^(-1/2) Z_(2,eff)(q;M)^(-1/8)`,       `1<=q<2`,            (1.1)

with exact entropy/diagonal-scaling optimization and arbitrary same-bank curvature retained. Hence I stopped the duplicate derivation and changed mechanism immediately, as required by the source-matching rule.

The new designated-partner source is fleet02/B04 run

`yspennstate/math-open-problems@36263ba314738468f934a5b3245130b6754e940f`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T043800Z-fleet02-B04-qform-auto11/REPORT.md`.

Its Section 8 proves the virtual-volume identity for a three-column matrix `M`: augment `M` by `gamma I_3`; then the three-row volume-sampling mass splits into the four homogeneous terms

`E_3 + gamma^2 E_2 + gamma^4 E_1 + gamma^6`,                     (1.2)

and the ordinary ridge leverage is the physical-row inclusion probability in that augmented three-volume law. This report applies that completed partner identity at an actual inequality, not merely as a citation.

## 2. Canonical volume laws

Let `M` be an `m x 3` real matrix and put

`C=M^T M`,
`E_r=e_r(C)` for `r=1,2,3`.

For every `r` with `E_r>0`, define the canonical `r`-volume law on pairs `(S,T)`, `|S|=|T|=r`, by

`P_r(S,T)=det(M[S,T])^2/E_r`.                                   (2.1)

Its physical-row inclusion marginals are

`alpha_i^(r)=P_r(i in S)`.                                      (2.2)

Thus `sum_i alpha_i^(r)=r`. In particular,

`alpha_i^(1)=||m_i||_2^2/E_1`,                                  (2.3)

where `m_i` is physical row `i`; and when `rank M=3`, `alpha_i^(3)` is the ordinary row leverage of the range projection `M C^(-1) M^T`.

For `gamma>0` define

`D_gamma=det(C+gamma^2 I_3)
       =E_3+gamma^2 E_2+gamma^4 E_1+gamma^6`,                    (2.4)

`K_gamma=M(C+gamma^2 I_3)^(-1)M^T`,
`ell_i(gamma)=(K_gamma)_(ii)`.                                  (2.5)

Define four scalar masses

`m_3=E_3/D_gamma`,
`m_2=gamma^2 E_2/D_gamma`,
`m_1=gamma^4 E_1/D_gamma`,
`m_0=gamma^6/D_gamma`.                                          (2.6)

They sum to one.

## 3. Exact virtual-volume row decomposition

### Theorem 3.1 — `QFORM-RIDGE-VOLUME-MIXTURE-v1`

For every physical row `i`,

`boxed:
 ell_i(gamma)
 =m_3 alpha_i^(3)+m_2 alpha_i^(2)+m_1 alpha_i^(1),
`                                                                  (3.1)

with any term omitted when its `E_r` vanishes.

Consequently, whenever `E_2>0`,

`boxed:
 alpha_i^(2) <= ell_i(gamma)/m_2(gamma).
`                                                                  (3.2)

More precisely,

`boxed:
 ell_i(gamma)/m_2(gamma)
 = alpha_i^(2)
   + [E_3/(gamma^2 E_2)] alpha_i^(3)
   + [gamma^2 E_1/E_2] alpha_i^(1).
`                                                                  (3.3)

#### Proof

Form the augmented `(m+3) x 3` matrix

`M_tilde_gamma = [ M ; gamma I_3 ]`.

By Cauchy--Binet its total squared three-volume is exactly `D_gamma`. The newest fleet02/B04 identity already records that the total masses of augmented three-row bases containing respectively `3,2,1,0` physical rows are `m_3,m_2,m_1,m_0` in (2.6).

Condition on the event that exactly `r` rows are physical. Fix a physical row set `S`, `|S|=r`. The remaining `3-r` virtual coordinate rows select the complementary set of `r` columns `T`; the squared augmented determinant is

`gamma^(2(3-r)) det(M[S,T])^2`.                                  (3.4)

After summing over the virtual choices and normalizing by the total `gamma^(2(3-r))E_r`, the conditional law of `(S,T)` is exactly the canonical `r`-volume law (2.1). Therefore the conditional probability that physical row `i` is selected is `alpha_i^(r)`.

On the other hand, fleet02/B04's partner identity identifies the unconditional physical-row inclusion probability in this same augmented three-volume process with the ridge leverage `ell_i(gamma)`. The law of total probability gives (3.1). Dividing by `m_2>0` gives (3.3), and positivity of the other two terms gives (3.2). QED.

This is an exact structural identity, not an asymptotic or a numerical observation.

## 4. Balanced weak-direction scale

Assume `E_1,E_2,E_3>0` and define the dimensionless weak-direction parameter

`rho = sqrt(E_1 E_3)/E_2`.                                      (4.1)

Choose the balanced ridge scale

`gamma_*^2 = sqrt(E_3/E_1)`.                                    (4.2)

Then the two contamination coefficients in (3.3) are equal, and

`boxed:
 ell_i(gamma_*)/m_2(gamma_*)
 =alpha_i^(2)+rho[alpha_i^(1)+alpha_i^(3)].
`                                                                  (4.3)

Hence

`boxed:
 alpha_i^(2)
 <=ell_i(gamma_*)/m_2(gamma_*)
 <=alpha_i^(2)+2rho.
`                                                                  (4.4)

So in the small-third-volume regime `rho<<1`, ridge leverage divided by the two-physical-row ridge mass is a quantitative proxy for the actual canonical E2 row marginal. This explains algebraically why the one-scale ridge and E2/square mechanisms become close in a weak-third-direction limit while still having different integrability thresholds.

For reference, Newton's inequality gives `E_2^2>=3 E_1 E_3`, hence `0<=rho<=1/sqrt(3)`; no smallness is automatic from rank three alone.

## 5. Partner-to-density transfer

### Theorem 5.1 — `QFORM-SQUARE-RIDGE-M2-TRANSFER-v1`

Let one original coordinate `Z` be independent of all remaining original coordinates `Y`, each coordinate having a probability density bounded by one, and suppose

`Q=a(Z+d(Y))^2+R(Y)`, `a!=0`.                                   (5.1)

Choose disjoint original-coordinate banks inside `Y` such that the residual cross block `M` has exactly three columns and `E_2=e_2(M^T M)>0`. For some `gamma>0`, let `m_2(gamma)` and `ell_*(gamma)=max_i ell_i(gamma)` be as in (2.5)-(2.6), and define

`q_gamma=max{1, 2 ell_*(gamma)/m_2(gamma)}.`                     (5.2)

If

`q_gamma<2`,                                                     (5.3)

then the law of `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= [8 e^(1/4) q_gamma^(-1/4)/(2-q_gamma)]
    |a|^(-1/2) E_2^(-1/8).
`                                                                  (5.4)

Equivalently, using the partner's virtual-volume identity `m_2 D_gamma=gamma^2 E_2`,

`boxed:
 ||p_Q||_infinity
 <= [8 e^(1/4) q_gamma^(-1/4)/(2-q_gamma)]
    |a|^(-1/2) gamma^(1/4)
    [m_2(gamma)D_gamma]^(-1/8).
`                                                                  (5.5)

#### Proof

Under the canonical two-volume law `w=P_2`, Theorem 3.1 gives

`max_i alpha_i^(2) <= ell_*/m_2 <= q_gamma/2`.                  (5.6)

Thus the exact marginal gate of the already-proved `QFORM-SQUARE-ENTROPY-E2-HALFRIESZ-v1` is satisfied with this `q_gamma`. For the canonical law its KL cost is zero and its optimized determinant currency is exactly `E_2`. Substitution into (1.1) gives (5.4). Identity (5.5) is just `E_2=m_2D_gamma/gamma^2`. QED.

The important point is that Theorem 5.1 does **not** require the ridge effective dimension `theta=tr K_gamma` to exceed two. It only asks that the two-physical-row component of the virtual three-volume law be sufficiently diffuse relative to total physical-row inclusion. Therefore a scalar square can close some matrices on which the pure ridge density theorem is below its integrability threshold.

## 6. Exact comparison with pure ridge effective dimension

The same virtual-volume process gives

`theta(gamma)=tr K_gamma=3m_3+2m_2+m_1`.                         (6.1)

Pure q=1 ridge smoothing requires `theta>2` in the completed ridge theorem. By contrast, Theorem 5.1 may apply when `theta<2` if `m_2` dominates the individual row leverages. This is not merely logical: the partner's newest balanced weak family is an explicit example.

The difference can be read directly from the decomposition. A mass configuration concentrated on `m_2` has expected number of physical rows close to two and therefore sits near or below the pure-ridge critical exponent, but conditional on that component it contains exactly the two physical directions needed by the E2 half-Riesz theorem; the genuine independent scalar square supplies the missing half derivative.

## 7. Apply the designated partner result to an actual inequality

Use fleet02/B04's newest family

`M_epsilon=U diag(2,2,epsilon)V^T`, `0<epsilon<=1`,               (7.1)

where `U` has two weak rows `(0,0,1/sqrt(2))`, four rows `(1/2,0,0)`, four rows `(0,1/2,0)`, and `V` is its displayed dense rational orthogonal `3x3` matrix. All thirty physical entries are nonzero and the singular values are exactly `(2,2,epsilon)`.

Embed it in the target-valid indefinite quadratic form

`Q_epsilon=Z^2+2 X^T M_epsilon Y`.                              (7.2)

Its symmetric coefficient matrix has spectrum

`{1,+2,+2,+epsilon,-2,-2,-epsilon,0,...,0}`,                    (7.3)

so at least five eigenvalues have modulus at least one for every `0<epsilon<=1`.

At the fixed ridge scale `gamma=1/2`, fleet02/B04's virtual-volume identity gives

`D=(1+4/gamma^2)^2(1+epsilon^2/gamma^2)` up to the common `gamma^6` normalization, equivalently from (2.4)

`D_(1/2)=289(1+4epsilon^2)/64`,                                 (7.4)

and the exactly-two-physical mass is

`m_2
 = [gamma^2(16+8epsilon^2)]/D_(1/2)
 = 128(2+epsilon^2)/[289(1+4epsilon^2)].`                       (7.5)

The ridge leverage is

`ell_* = max{4/17, 2epsilon^2/(1+4epsilon^2)}.`                 (7.6)

For

`epsilon^2 <=64/257`                                            (7.7)

one checks directly from (7.5)-(7.6) that `ell_*/m_2<=1/2`; hence `q_gamma=1`. Theorem 5.1 and

`E_2=16+8epsilon^2`                                              (7.8)

give the explicit all-input-law estimate

`boxed:
 ||p_(Q_epsilon)||_infinity
 <=8 e^(1/4)(16+8epsilon^2)^(-1/8)
 <=4 sqrt(2)e^(1/4)
 =7.263544634846275... .
`                                                                  (7.9)

In particular, as `epsilon->0`, the partner report's pure one-scale ridge certificate at its optimized scale grows logarithmically, while the transfer (7.9) stays bounded. At the partner's illustrative `epsilon=10^(-6)`, its pure-ridge certificate is `34.3217841164...`, whereas (7.9) is `7.263544634845820...`.

This is an equation-level application of the designated partner's **new** virtual-volume result: (7.5)-(7.6) certify the E2 marginal gate through the conditional two-physical component. It is distinct from simply reusing the older E2 theorem or selecting two large singular values.

For larger `epsilon`, the direct canonical E2 marginals of this particular balanced family are already small enough to use the earlier theorem, so failure of the fixed-scale transfer is not a density obstruction; it only marks when `gamma=1/2` ceases to be a good virtual-volume witness.

## 8. A useful exact diagnostic for the remaining near-star case

Define

`r_2(M)=inf_(gamma>0) ell_*(gamma)/m_2(gamma)`                    (8.1)

when `E_2>0`. Theorem 3.1 gives the rigorous one-sided comparison

`alpha_*^(2):=max_i alpha_i^(2) <= r_2(M)`.                      (8.2)

At the balanced scale (4.2),

`r_2(M) <= alpha_*^(2)+2rho`.                                   (8.3)

Thus

`boxed:
 alpha_*^(2) <= r_2(M) <= alpha_*^(2)+2 sqrt(E_1E_3)/E_2.
`                                                                  (8.4)

This separates two obstructions which were previously mixed together:

1. **support/near-star concentration:** `alpha_*^(2)` is close to one, so every balanced two-volume law necessarily concentrates on one physical row;
2. **spectral third-direction contamination:** `rho` is not small, so the virtual ridge process cannot isolate the two-physical component sharply.

When the third singular direction is genuinely weak, `rho` is small and the two diagnostics agree. Therefore a low-total-tail/high-ridge survivor with `r_2` close to one is quantitatively forced toward the same near-star geometry identified by the previous B04 fractional-matching classification; it is not an independent mystery of regularization.

No claim is made that (8.4) alone closes that near-star branch.

## 9. What changed and what remains

Paid in this run:

- exact row-by-row decomposition of ridge leverage into canonical E1/E2/E3 physical-volume marginals;
- a balanced-scale identity with explicit error `2 sqrt(E_1E_3)/E_2`;
- a direct ridge-to-E2/square density transfer with all constants explicit;
- a branch that can remain uniformly bounded even when `tr K_gamma<2`, so it strictly crosses the pure-ridge integrability threshold;
- a direct application of fleet02/B04's newest virtual-volume theorem to its genuinely rotated indefinite balanced weak-direction family.

Not paid:

- a universal scalar pivot `|a|` from the bare three-large-eigenvalue hypothesis;
- the quantitative near-star/zero-pivot branch when every useful scalar diagonal is tiny and canonical two-volume mass concentrates on one row;
- a proof that `|a|^4 E_2` or its entropy-flattened version is universally bounded below;
- full QFORM or full-target continuity.

The first remaining implication on this route is now

`QFORM-RIDGE-E2-NEARSTAR-TO-HUB-v1`:

> Starting from a full-target/N3 survivor for which a scalar pivot exists but every square-plus-E2 certificate fails, use (8.4) to convert the failure into a quantitative original-coordinate near-star statement, then retain the nonzero same-bank curvature and route that near-star to an already-paid mixed-hub/grouped-bank theorem. The zero-pivot endpoint must be handled separately and cannot be obtained by treating a small matrix coefficient as a small random perturbation.

This is narrower than the former generic `QFORM-NEARSTAR-E2-OR-ZEROPIVOT-ROUTING-v1`: weak-third-direction regularization versus physical E2 concentration is now separated exactly.

## 10. Regularity and review status

Theorem 5.1 supplies an **essentially bounded density** by the previously proved conditional square-kernel/Fubini argument. This report does **not** prove continuity in that general scope. The full target remains `OPEN`, and the full-target continuous-density statement remains `OPEN`.

No independent end-to-end review of `QFORM-RIDGE-VOLUME-MIXTURE-v1` / `QFORM-SQUARE-RIDGE-M2-TRANSFER-v1` has yet been recorded. The algebraic mixture identity is exact, but it is a supporting theorem rather than a full candidate proof.

Final status: `FULL_TARGET_OPEN / CONTINUITY_FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.
