SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T02:47:57Z.
attacking: high-E4 carrier failure -> cross-E3 or literal low-rank product-Fourier receiver with explicit constants.

# fleet03/B04 r47 — higher-compound downshift into the marginal-free E3 Fourier receiver

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement.
Status: **NEW SUPPORTING THEOREM / E4-AND-HIGHER-COMPOUND ROUTED TO E3 / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target is not proved here. The result below is a deterministic compound-volume reduction followed by an already-proved product-Fourier receiver. It never rotates the random variables, assumes no moments or regularity of the input laws beyond independent one-dimensional densities bounded by one, and does not invoke law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, or a worst-fiber supremum.

## 1. Fresh sources and exact scope


The product-Fourier input is fleet03/B04 r42,

`QFORM-CROSS-E3-OPTIMAL-THRESHOLD-v1`,

at

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T215155Z-fleet03-B04-QFORM-auto11-r42/REPORT.md`.

For every literal original-coordinate cross block `M=A[I,J]` with `I cap J=emptyset` and

`E3(M):=e_3(MM^T)>0`,

that theorem gives the full ambient quadratic-plus-affine form the continuous `C_0` density bound

`||p_Q||_infinity <= C_* E3(M)^(-1/6)`,                         (1.1)

where

`C_*=8.453021225528176874704918...`.                             (1.2)

Arbitrary same-bank quadratic terms, outside couplings, signs and affine terms are retained.

The designated partner input is fleet04/B04 r2,

`QFORM-HIGH-CARRIER-ANCHORED-DOWNSHIFT-v1`,

at

`yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260924T001353Z-fleet04-B04-QFORM-r2/REPORT.md`.

It works on a literal block with `E4(M)>0`, and in its live branch produces a physical fourth-volume carrier with `rho_i>1/25`, followed by an anchored-entropy-or-double-anchor dichotomy.

## 2. Rank-free Maclaurin downshift

Let `x_1,...,x_r` be the positive eigenvalues of `MM^T`; thus `r=rank(M)`. For `k<=r` write

`E_k(M)=e_k(x_1,...,x_r)`.

### Lemma 2.1 — normalized elementary means

For `3<=m<=r`,

`E3(M) >= binom(r,3) [ E_m(M)/binom(r,m) ]^(3/m)`.              (2.1)

Proof. The polynomial `prod_j(1+x_j t)` has only real nonpositive zeros. Newton's inequalities imply log-concavity of

`a_k=E_k(M)/binom(r,k)`.

Since `a_0=1`, the successive ratios `a_k/a_(k-1)` decrease, hence the geometric means
`a_k^(1/k)` decrease. Therefore `a_3^(1/3)>=a_m^(1/m)`, which is (2.1). QED.

The rank dependence in (2.1) can be removed sharply. Define

`c_m=(m!)^(3/m)/6`.                                              (2.2)

Then

`binom(r,3)/binom(r,m)^(3/m)
 = c_m * (r)_3/(r)_m^(3/m)`,                                    (2.3)

where `(r)_k=r(r-1)...(r-k+1)`. The three factors in `(r)_3` are the three largest factors of `(r)_m`, so their geometric mean is at least the geometric mean of all `m` factors:

`(r)_3^(1/3) >= (r)_m^(1/m)`.                                   (2.4)

Consequently

`boxed: E3(M) >= c_m E_m(M)^(3/m),  c_m=(m!)^(3/m)/6.`           (2.5)

The constant `c_m` is rank-uniform and sharp: if all `r` nonzero singular values of `M` are equal, then the ratio in (2.3) tends to one as `r->infinity`.

For `m=4`,

`c_4=24^(3/4)/6=(32/3)^(1/4)=1.8072040072196895...`.             (2.6)

Equivalently,

`boxed: E3(M) >= (32/3)^(1/4) E4(M)^(3/4).`                    (2.7)

This is the first essential implication attempted in this run: a target-scale fourth-compound packet on any literal cross block cannot coexist with arbitrarily tiny third-compound currency on that same block.

## 3. New product-Fourier theorem — `QFORM-HIGHER-COMPOUND-DOWNSHIFT-v1`

Let `m>=3`. Suppose a literal original-coordinate cross block `M=A[I,J]`, `I cap J=emptyset`, satisfies `E_m(M)>0`. Then the full ambient target form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= C_* c_m^(-1/6) E_m(M)^(-1/(2m)),
 c_m=(m!)^(3/m)/6.`                                              (3.1)

Proof. Equation (2.5) gives

`E3(M)^(-1/6)
 <= c_m^(-1/6) E_m(M)^(-1/(2m))`.                               (3.2)

Apply the marginal-free product-Fourier theorem (1.1) to the same literal block. Its characteristic-function envelope is in `L^1`, so the density is continuous and `C_0`. No new probabilistic assumption is introduced. QED.

For `m=4` this becomes

`boxed:
 ||p_Q||_infinity
 <= C_4down E4(M)^(-1/8),`                                      (3.3)

with

`C_4down
 = C_* (32/3)^(-1/24)
 = 7.659094523616393... <7.660.`                                 (3.4)

Thus every positive fourth-volume certificate on a physical cross block is already an `E3` Fourier certificate. A carrier analysis is unnecessary for generic boundedness once `E4(M)` itself is available, although carrier-sensitive theorems can still give sharper constants on special matrices.

For reference, the first few rank-free coefficients are

`m=3: 8.4530212255...`
`m=4: 7.6590945236...`
`m=5: 7.0596912826...`
`m=6: 6.5855612478...`.

## 4. Designated partner application

Apply fleet04/B04 r2 to its live literal cross block. Its branch hypothesis includes

`E4(M)>0`,                                                       (4.1)

and in the high-carrier state

`rho_i=H_i/E4(M)>1/25`.                                         (4.2)

The new theorem does not need to split on the partner's anchored-face marginal `beta_*`: directly from the same `E4(M)`,

`boxed:
 ||p_Q||_infinity
 <=7.659094523616393... E4(M)^(-1/8).`                           (4.3)

This is an actual equation-level use of the completed designated-partner state. It simultaneously pays both of its `beta_*<=2/3` and `beta_*>2/3` subbranches, preserves arbitrary same-bank curvature and extra spectrum through the r42 receiver, and proves a continuous `C_0` density.

For comparison, the previous generic high-carrier assembly from this slot had constants `8.5844318...` on the diffuse anchored branch and `13.4999079...` on the pair branch. Equation (4.3) is smaller than both and removes both the row-norm and carrier-marginal case splits at the generic `E4` level.

This does not invalidate the partner theorem: its anchored currency can outperform (4.3) on particular matrices, and its structural information remains useful when only an anchored packet, rather than a global lower bound on `E4`, is known.

## 5. A disjoint higher-compound global bridge

For a symmetric matrix `A`, define the disjoint physical `m`-compound mass

`D_m^disj(A)
 = sum_{|S|=|T|=m, S cap T=emptyset} det A[S,T]^2`.              (5.1)

Color every original coordinate independently into banks `I,J` with probability one half and set `M=A[I,J]`. A fixed ordered disjoint pair `(S,T)` is captured as `S subset I`, `T subset J` with probability `2^(-2m)`. Therefore

`E E_m(A[I,J])=2^(-2m) D_m^disj(A)`.                            (5.2)

Some literal cut satisfies

`E_m(M)>=4^(-m)D_m^disj(A)`.                                    (5.3)

Combining (3.1) and (5.3),

`boxed:
 ||p_Q||_infinity
 <=2 C_* c_m^(-1/6) [D_m^disj(A)]^(-1/(2m)).`                   (5.4)

The density is continuous `C_0`. For `m=4`, the front coefficient is

`15.318189047232786...`.                                        (5.5)

This is only a receiver: the bare three-large-eigenvalue hypothesis does not by itself force target-scale `D_m^disj` for `m>=4`.

## 6. Genuinely rotated indefinite stress test

Take the `64x64` Sylvester Hadamard matrix `H_64` and set

`M_*=H_64/8`.                                                    (6.1)

Every coefficient of `M_*` is `+/-1/8`, while

`M_* M_*^T=I_64`.                                                (6.2)

Define the symmetric `128x128` matrix

`A_*=[[0,M_*],[M_*^T,0]]`.                                      (6.3)

This is dense across the original two banks and non-diagonal in the independent coordinates. Since every singular value of `M_*` equals one,

`spec(A_*)={+1 (multiplicity 64), -1 (multiplicity 64)}`.        (6.4)

Thus it is genuinely rotated and indefinite and satisfies the owner target very strongly.

Here

`E3(M_*)=binom(64,3)=41664`,                                    (6.5)

`E4(M_*)=binom(64,4)=635376`.                                   (6.6)

Using only the new fourth-compound downshift gives, for every admissible independent cap-one product input,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=1.441446667917172... .`                                      (6.7)

The density is continuous and vanishes at infinity. The direct `E3` value gives the slightly stronger `1.4356606569073866...`; their closeness reflects the asymptotic sharpness of the rank-free Maclaurin constant. For comparison, the generic exact-rank-64 crossing estimate with all singular values one has coefficient

`2*64/(64-2)=2.0645161290...`,                                  (6.8)

so the compound product-Fourier route is quantitatively stronger on this dense test.

No Monte Carlo evidence is used. The committed deterministic checker verifies Hadamard orthogonality, the exact compound values, the rank-free constants, and the numerical bounds.

## 7. Scope and next obligation

This run closes the previously named B04 implication `QFORM-E4-CARRIER-OR-E3-COLLISION-ROUTING-v1` whenever the relevant literal block has `E4>0`: higher compound currency automatically downshifts to the already-paid `E3` collision receiver.

**Full QFORM remains OPEN**, and full-target continuity remains OPEN separately. The unresolved structural step is earlier:

`QFORM-THREE-SPECTRAL-DIRECTIONS-TO-DISJOINT-E3-OR-OVERLAP-RECEIVER-v1`:

from the bare hypothesis that `A` has three eigenvalues of modulus at least one, force a target-scale literal cross `E3` / disjoint third-compound packet, or pay the overlap classes `C1,C2,C3` through product-preserving hub/star/ridge/square-bank receivers. Higher `E4/E5/...` certificates should no longer be treated as separate density endpoints, because (3.1) routes them to `E3`.

No scheduler state, task identity, email/push notification, repository visibility, paid model/API call, remote workflow, or cross-account authentication is changed by this report. Model self-report: `GPT-5.6 Sol`; configured reasoning effort and provider thinking counters were not exposed.
