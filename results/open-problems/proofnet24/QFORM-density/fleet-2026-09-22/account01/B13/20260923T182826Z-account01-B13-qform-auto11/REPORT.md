SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T18:28:26Z.
attacking: combine the designated partner's unconditional D5 exterior-volume estimate with a sharp target-level first-volume lower bound and the corrected robust skeleton, then feed the stronger residual into a diffuse-vs-heavy bounded-rank carrier split.

# account01/B13 — rho^{-5/4} exterior bootstrap and diffuse-carrier rank-four collapse

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` acknowledged. Execution status: **WITHOUT_VERIFIED_BRAIN**.

Status: **PROVED SUPPORTING TARGET-LEVEL THEOREMS / FULL QFORM OPEN / CONTINUITY OPEN**. Nothing below deletes a small coefficient tail on arbitrary rough product supports, and nothing below claims the universal theorem has been closed.

## 1. Sources and scopes actually used

### 1.1 Designated partner account02/B13

Latest completed handoff/report:

- `yspennstate/math-open-problems@4db7e9f914c201c3162b6213dd63b577755b8a36`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/account02-B13-20260923T1811Z/REPORT.md`
- skeleton-correction reconciliation: `yspennstate/math-open-problems@9a272828dbb4008db19bf92034bdfdc583909d7b`, same run path `POSTREFRESH_ADDENDUM.md`.

Two completed inequalities from that source are used below.

**D5 cross-block receiver.** For every disjoint original-coordinate cut `I,J`, with `M=A[I,J]`, arbitrary same-side curvature, outside terms and affine terms retained,

`||p_Q||_infinity <= C5 e_5(M^T M)^(-1/10)`,

`C5 = 5 sqrt(2e) = 11.6582199079856...`.                           (1.1)

Hence an actual slab ratio `rho=P{Q in J0}/|J0|` obeys

`e_5(M^T M) <= (C5/rho)^10`                                       (1.2)

for every physical cut.

**Localized physical-triple receiver.** If one original-coordinate principal `3 x 3` block has all three eigenvalue moduli at least `c>0`, then the full ambient quadratic form has

`||p_Q||_infinity <= 6 sqrt(pi)/c`,                               (1.3)

with arbitrary outside coefficients and affine terms retained.

### 1.2 Corrected robust exterior skeleton

The current correction, source-pinned at

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`,

changes an earlier volume-sampled *identity* to an upper bound, but preserves the robust corollary used here:

if

`V_{r+1}(A) <= kappa V_r(A)`,                                     (1.4)

where

`V_r(A)=sum det A[S,T]^2`

over ordered disjoint physical `r`-sets `S,T`, then

`A=D+R+E`, `D` diagonal, `R` symmetric, `rank R<=4r`, `E` symmetric zero-diagonal, and

`||E||_F <= 3(r+1) sqrt(kappa)`.                                  (1.5)

The account02/B13 post-refresh addendum explicitly checks that (1.5) survives the correction. No random variable is rotated.

### 1.3 Extremal-product scope

The exact B13 barycentric purification already proved in

`yspennstate/math-open-problems@82a83d6da64145ee7aed98a87f4f1dd03d209d98:proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T102930Z-account01-B13-qform-auto20/REPORT.md`

states that every cap-one mass-one marginal is a probability barycenter of indicators `1_E`, `|E|=1`; tensoring gives the same statement for product laws and every nonnegative measurable kernel. Thus for the slab kernel there is no loss in passing from arbitrary cap-one product densities to arbitrary measurable unit-measure product indicators. Bounded finite unions of intervals give arbitrary strict approximations, but there is no single-interval, centered-uniform, bounded-diameter or bounded-fragment reduction.

For completeness, the one-dimensional barycentric construction partitions the line into unit intervals `I_m`, writes `alpha_m=int_{I_m} f`, applies metrizable Choquet to the weak-* compact convex set `{0<=g<=1, int g=alpha_m}`, whose extreme points are exactly indicators of subsets of `I_m` of measure `alpha_m`, and takes the countable product of these representing measures. The sampled union has total measure `sum alpha_m=1` deterministically. Tensoring over coordinates and Tonelli gives the product identity.

## 2. A sharp target-level lower bound on the first exterior volume

Write

`D0=diag(A)`, `O=A-D0`, `V1=V_1(A)=||O||_F^2`, and put

`c0=6 sqrt(pi)=10.6347231054331...`.                              (2.1)

### Lemma 2.1 — `QFORM-V1-SPECTRAL-FLOOR-v1`

Under the exact target hypothesis `s_3(A)>=1`, every actual slab ratio `rho>c0` satisfies

`boxed: sqrt(V1) >= (1-c0/rho)/2`,                                (2.2)

hence

`boxed: V1 >= (1/4)(1-c0/rho)^2.`                                 (2.3)

#### Proof

Set `v=sqrt(V1)`. If `v>=1/2`, (2.2) is immediate because its right side is below `1/2`.

Assume `v<1/2`. Then `||O||_op<=||O||_F=v`. Weyl gives

`s_3(D0) >= s_3(A)-v >=1-v`.                                      (2.4)

Since `D0` is diagonal, there are three original coordinates `K` whose diagonal entries have modulus at least `1-v`. On that physical principal block,

`sigma_min(A[K,K]) >= 1-v-||O[K,K]||_op >=1-2v`.                  (2.5)

Apply the completed localized physical-triple theorem (1.3), conditioning only on the original coordinates outside `K`:

`rho <= 6 sqrt(pi)/(1-2v)=c0/(1-2v)`.                             (2.6)

Rearranging gives `v >= (1-c0/rho)/2`, proving (2.2)-(2.3). QED.

This improves the weaker high-ratio lower bound `V1>=rho^-2`: as `rho->infinity`, it forces `V1>=1/4-o(1)`.

## 3. General exterior-decay bootstrap

### Lemma 3.1 — `QFORM-EXTERIOR-DECAY-BOOTSTRAP-v1`

Fix an integer `m>=2`. Assume `V1>0`, and suppose

`V_m <= B rho^(-2m)`.                                              (3.1)

Assume the robust skeleton implication (1.4)-(1.5) for `r=1,...,m-1`. Then either some exterior volume vanishes and one obtains an exact decomposition with `E=0`, or there exists `r in {1,...,m-1}` such that

`A=D+R+E`, `rank R<=4r<=4(m-1)`, `E_ii=0`, and

`boxed:
 ||E||_F <= 3 (m!)^(1/(m-1)) (B/V1)^(1/(2(m-1))) rho^(-m/(m-1)).`  (3.2)

#### Proof

If some `V_j=0` for `2<=j<=m`, let `j` be the first such index. Then `V_{j-1}>0` and (1.4)-(1.5) with `kappa=0` gives `E=0`.

Otherwise put

`q_r=V_{r+1}/V_r`, `r=1,...,m-1`.                                (3.3)

Then

`prod_{r=1}^{m-1} q_r = V_m/V1 <= (B/V1) rho^(-2m)`.              (3.4)

Let `a_r=3(r+1)`. If every `a_r sqrt(q_r)` exceeded a number `K rho^{-m/(m-1)}`, multiplication would give

`prod q_r > K^{2(m-1)} rho^{-2m}/prod a_r^2`.                    (3.5)

But

`prod_{r=1}^{m-1} a_r = 3^{m-1} m!`.                             (3.6)

Choosing

`K=3 (m!)^(1/(m-1)) (B/V1)^(1/(2(m-1)))`                         (3.7)

contradicts (3.4). Therefore some `r` obeys `a_r sqrt(q_r)<=K rho^{-m/(m-1)}`. The robust skeleton (1.5) gives (3.2). QED.

The exponent `m/(m-1)` is the key point: once `V1` has a target-level positive floor rather than decaying like `rho^-2`, the fifth-volume theorem yields a residual smaller than the density scale `rho^-1`.

## 4. Actual application of account02/B13 D5: an O(rho^{-5/4}) Frobenius twist

A fair Bernoulli physical cut gives, by Cauchy--Binet,

`E_cut e_5(A[I,J]^T A[I,J]) = 4^-5 V_5(A)`.                       (4.1)

Applying the partner inequality (1.2) for every cut and averaging yields

`boxed: V_5(A) <= 4^5 C5^10 rho^-10.`                             (4.2)

This is the designated-partner result applied at an actual global inequality.

Feed (4.2) and Lemma 2.1 into Lemma 3.1 with `m=5`, `B=4^5 C5^10`. Define

`K5 = 3 * 120^(1/4) * (4^6 C5^10)^(1/8)`
`   = 604.9951089367705...`.                                      (4.3)

### Theorem 4.1 — `QFORM-D5-RHO54-RANK16-SKELETON-v1`

For every target-class matrix and every actual slab ratio

`rho>6 sqrt(pi)`,                                                  (4.4)

there is a physical-coordinate decomposition

`boxed: A=D+R+E,   rank R<=16,   E_ii=0,}`                        (4.5)

such that either `E=0` or

`boxed:
 ||E||_F <= K5 (1-6 sqrt(pi)/rho)^(-1/4) rho^(-5/4).}`            (4.6)

In particular, for `rho>=12 sqrt(pi)=21.2694462108662...`,

`boxed: ||E||_F <= 719.464488089454 rho^(-5/4).}`                 (4.7)

#### Proof

From (2.3),

`1/V1 <= 4(1-c0/rho)^(-2)`.                                      (4.8)

Substitute (4.2) and (4.8) into the `m=5` form of (3.2):

`||E||_F
 <=3*120^(1/4)*[4^5 C5^10 * 4(1-c0/rho)^(-2)]^(1/8) rho^(-5/4)`
` =K5(1-c0/rho)^(-1/4)rho^(-5/4)`.                               (4.9)

If `rho>=2c0`, the parenthetical factor is at most `2^(1/4)`, and `K5*2^(1/4)=719.464488089454...`. QED.

### Comparison with the current partner endpoint

The latest account02/B13 theorem gave, unconditionally,

`A=D+R+E`, `rank R<=16`, `||E||_F<=508.738219/rho`.               (4.10)

The new conclusion (4.6) is asymptotically stronger in the exact rough-law chamber:

`rho ||E||_F = O(rho^-1/4) ->0`.                                  (4.11)

This is a genuine strengthening, not a perturbative deletion claim. The partner's separated-support construction still shows that coefficient-small quadratic twists can remain order one as random variables when supports move with the small coefficient.

## 5. Counterexample normal form after exact extremal-product purification

Suppose the unrestricted theorem were false. The exact barycentric product reduction lets every strict bad slab be witnessed with the same `A,J` by arbitrary measurable unit-measure product indicators; the finite-mixture approximation lets one choose bounded finite-union unit sets with an arbitrarily small loss in ratio.

Therefore any hypothetical sequence with slab ratios `rho_n->infinity` can be chosen with bounded finite-union unit-product indicator marginals and matrices satisfying

`A_n=D_n+R_n+E_n`, `rank R_n<=16`,                                (5.1)

`||E_n||_F <= (604.996+o(1)) rho_n^(-5/4)`,                       (5.2)

and independently

`V_5(A_n) <= 4^5 C5^10 rho_n^-10`.                               (5.3)

Thus

`boxed: rho_n * dist_F(A_n, {diagonal + rank<=16}) ->0.}`         (5.4)

This is strictly stronger than the preceding `O(rho^-1)` counterexample normal form. It does not assume any support diameter, moment, interval structure, or bounded fragment count.

## 6. Secondary consequence: diffuse bounded-rank carrier collapses to rank four

The stronger tail can be combined with the same partner D5 estimate to isolate a finite-hub obstruction inside the rank-sixteen carrier.

Take a decomposition (4.5)-(4.6), put `eps=||E||_F`, and spectrally factor the nonzero part of `R` as

`R=U Lambda U^T`, `U^T U=I_m`, `m<=16`.                           (6.1)

Let the physical row leverages be

`ell_i=||U_{i,:}||_2^2`.                                          (6.2)

### Lemma 6.1 — `QFORM-DIFFUSE-CARRIER-RANK4-COLLAPSE-v1`

If `m<=4`, nothing is needed. If `m>=5` and

`max_i ell_i <=1/2048`,                                           (6.3)

then there are a diagonal `D'`, a symmetric rank-at-most-four matrix `R4`, and a symmetric zero-diagonal `F` such that

`A=D'+R4+F`                                                        (6.4)

and

`boxed: ||F||_op <= 8 C5/rho + 9 eps.`                            (6.5)

For `rho>=12 sqrt(pi)`, this gives the explicit estimate

`||F||_op <= 93.265759263885 rho^-1
             +6475.18039280509 rho^-5/4.`                          (6.6)

Consequently, every remaining carrier of rank at least five either contains a physical coordinate of leverage `>1/2048`, or it collapses to rank four plus the retained operator-small twist (6.5).

#### Proof

For every physical cut `I,J`, (1.2) implies

`s_5(A[I,J]) <= C5/rho`,                                          (6.7)

because `e_5(M^T M)>=s_5(M)^10`. Since diagonal matrices have zero cross block,

`A[I,J]=R[I,J]+E[I,J]`,

and Weyl gives

`s_5(R[I,J]) <= C5/rho+eps`.                                      (6.8)

It remains to choose one balanced physical cut for the spectral frame `U`. Label each coordinate independently red with probability `1/2` and put

`G_I=U_I^T U_I`.                                                   (6.9)

For a fixed unit vector `v in R^m`,

`v^T(G_I-I/2)v = sum_i (xi_i-1/2)(u_i.v)^2`.                     (6.10)

Writing `a_i=(u_i.v)^2`, one has `sum a_i=1`, `max a_i<=1/2048`, hence `sum a_i^2<=1/2048`. Hoeffding therefore yields

`P{|v^T(G_I-I/2)v|>=1/8} <=2 exp(-64)`.                          (6.11)

A `1/4`-net of `S^{m-1}`, `m<=16`, has at most `9^16` points. The union bound is

`2*9^16*exp(-64)<5.95e-13<1`.                                    (6.12)

For some deterministic original-coordinate cut, the standard net argument gives

`||G_I-I/2||_op<=1/4`,                                            (6.13)

so both

`G_I>=I/4`, `G_J=I-G_I>=I/4`.                                    (6.14)

Write

`U_I=Q_I G_I^{1/2}`, `U_J=Q_J G_J^{1/2}`,                        (6.15)

where `Q_I,Q_J` have orthonormal columns. Thus the nonzero singular values of `R[I,J]` are those of

`G_I^{1/2} Lambda G_J^{1/2}`.                                    (6.16)

Using (6.14),

`s_5(R[I,J]) >= (1/4)s_5(Lambda)`.                               (6.17)

Combine (6.8) and (6.17):

`s_5(Lambda) <=4(C5/rho+eps)`.                                   (6.18)

Let `R4` retain the four largest absolute eigenvalues of `R`, and put `T=R-R4`. Then

`||T||_op<=4(C5/rho+eps)`.                                        (6.19)

Move `diag(T)` into the diagonal matrix and retain the off-diagonal part in the residual:

`D'=D+diag(T)`, `F=E+T-diag(T)`.                                  (6.20)

Since `||diag(T)||_op<=||T||_op`,

`||F||_op <=eps+2||T||_op
          <=8C5/rho+9eps`,                                        (6.21)

which is (6.5). QED.

This lemma uses a random partition only as a deterministic existence device; no rotated random variables or post-rotation independence are invoked.

## 7. Exact remaining gap

The full conjecture is still **OPEN**. The first unpaid rough-law implication is now sharper than the partner's `O(rho^-1)` endpoint:

`QFORM-DIAG-RANK16-RHO54-TWIST-GLUE-v1`:

> Starting from a genuine high-ratio product witness and
> `A=D+R+E`, `rank R<=16`, `||E||_F=O(rho^-5/4)`, prove a universal contradiction while retaining `E` inside the product-preserving estimate; or construct a genuine counterexample sequence.

The diffuse carrier subbranch is further reduced to rank four plus (6.5); otherwise one has a physical heavy-leverage coordinate in the bounded-rank carrier. The hard point remains the same in kind: arbitrary fragmented/unbounded product laws can amplify coefficient-small twists, so neither Frobenius nor operator smallness alone permits probabilistic deletion.

A next viable mechanism is to combine the physical heavy-leverage branch with the existing hub/pair receivers, while in the diffuse branch applying the checked projected-crossing/grouped-hub machinery directly to the retained twist rather than replacing it by zero.

## 8. Scope / integrity

No moments, support-radius bounds, log-concavity, identical laws, interval extremality, spectral-coordinate independence, pointwise quadratic oscillatory decay, arbitrary-joint coarea, or perturbative deletion are used. All partitions act on original physical coordinates. Continuity is not inferred. Full QFORM remains OPEN.
