SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-23T07:21:07Z.
attacking: spectral-threshold/footprint control of full nonseparable tails at the matrix level.

# fleet01/B12 — spectral-threshold footprint compiler for arbitrary additional eigenvalues

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Status: `PROVED_SUPPORTING_STABILITY_THEOREM / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Independent review of this new theorem: not yet recorded.

## 0. Scope and first unpaid implication

The exact full target remains open.  The result below is a matrix-level stability compiler: after a useful ORIGINAL-coordinate cross certificate has been found, it permits simultaneously

1. arbitrarily many additional small eigenvalues of either sign, charged only by their largest magnitude;
2. arbitrarily large additional eigenvalues of either sign, charged only by how much their spectral subspace actually crosses the protected original-coordinate cut; and
3. an arbitrary-rank nonseparable symmetric tail of small operator norm, charged only at the matrix-certificate level.

At no point is a small matrix treated as a small random quadratic form.  In particular, no moment or support bound on the inputs is assumed, and there is no independence claim after spectral rotation.

The first still-unpaid implication is structural: from the bare hypothesis `s_3(A)>=1`, force one of the already-paid physical-core/ridge/grouped-bank/hub/cross-volume certificates with a quantitative margin.  Known correction families rule out replacing this by one universally well-conditioned principal minor or one universally rank-three cross cut.

## 1. Source-pinned completed inputs actually used

### 1.1 Current volume-stability theorem

Source:

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`  
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For a protected ORIGINAL-coordinate cross block `M=A[I,J]`, if

`M=M0+E`, `s_3(M0)>=a>0`, `max_i (P_range(M0))_ii<=1/2`, `||E||op<=a/16`,

then the entire ambient quadratic-plus-affine form (arbitrary self blocks and outside couplings retained) has a continuous density satisfying

`||p_Q||infinity <= 24 sqrt(3) e /(5a) < 23/a`.                 (1.1)

### 1.2 Newest-Claude unrestricted fifth-volume theorem

Source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`  
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

For an ORIGINAL-coordinate cross block `M=A[I,J]`, with

`Z_5=e_5(M^T M)`,

the full ambient quadratic-plus-affine form satisfies

`||p_Q||infinity <= 5 sqrt(2e) Z_5^(-1/10)`                    (1.2)

with no volume-marginal condition.  The proof is by an integrable Fourier envelope and gives the corresponding continuous density conclusion.

### 1.3 Designated partner fleet02/B12

Source:

`yspennstate/math-open-problems@712efebad69058a36784d6459abb18b8977b7aa4`  
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T065358Z-fleet02-B12-auto11/REPORT.md`.

For a baseline cross block `M0=A0[I,J]` and an actual perturbation satisfying `||M-M0||op<=epsilon`, define

`a_j=(s_j(M0)-epsilon)_+`,                                    (1.3)

`R=sum_j a_j^2`, `C=(s_1(M0)+epsilon)^2`,                     (1.4)

`r0=max_i ||row_i(M0)||_2^2`, `c0=max_j ||col_j(M0)||_2^2`,

`rho_*=min{(sqrt(r0)+epsilon)^2,(sqrt(c0)+epsilon)^2}`.        (1.5)

Its completed theorem gives

`||p_Q||infinity <= 5 sqrt(2e)(a_1 a_2 a_3 a_4 a_5)^(-1/5)`  (1.6)

when `a_5>0`, and, when

`R>2C`, `R-2C >= (9/2)rho_*`,                                 (1.7)

it gives the continuous density estimate

`||p_Q||infinity <= (9 sqrt(3)e/2)[R(R-C)(R-2C)/6]^(-1/6)`.  (1.8)

The application in Section 5 below substitutes an explicit new spectral-footprint bound into the partner's actual `epsilon` and verifies (1.7) numerically and exactly.

## 2. Spectral-footprint lemma

Let `H=H^T` be any real symmetric matrix and let `I,J` be disjoint original-coordinate sets.  Write `P_I,P_J` for the orthogonal coordinate projections and put

`eta(H;I,J)=||P_I H P_J||op`.                                 (2.1)

Define

`chi(H;I,J) = min{`

`  ||P_I H^2 P_I||op^(1/2),`

`  ||P_J H^2 P_J||op^(1/2),`

`  [||P_I |H| P_I||op ||P_J |H| P_J||op]^(1/2) }`.           (2.2)

### Lemma 2.1

For every symmetric `H`,

`boxed: eta(H;I,J) <= chi(H;I,J).`                             (2.3)

#### Proof

Let `K=P_I H P_J`, viewed as a map from the `J` coordinate subspace to the `I` coordinate subspace.  Since `0<=P_J<=I`,

`K K^* = P_I H P_J H P_I <= P_I H^2 P_I`                     (2.4)

in the positive-semidefinite order.  Hence

`||K||op^2 <= ||P_I H^2 P_I||op`.                             (2.5)

Applying the same argument to `K^*=P_J H P_I` proves the second alternative.

For the third alternative use the polar/sign decomposition

`H=|H|^(1/2) sgn(H) |H|^(1/2)`, `||sgn(H)||op<=1`.            (2.6)

Then

`K=(P_I|H|^(1/2)) sgn(H) (|H|^(1/2)P_J)`,                    (2.7)

so submultiplicativity gives

`||K||op <= ||P_I|H|^(1/2)||op |||H|^(1/2)P_J||op`

`          = [||P_I|H|P_I||op ||P_J|H|P_J||op]^(1/2)`.       (2.8)

Taking the minimum proves (2.3).  QED.

If `H=sum_k tau_k u_k u_k^T` spectrally, then the quantities in (2.2) are explicitly

`P_I H^2 P_I=sum_k tau_k^2 (u_k)_I (u_k)_I^T`,               (2.9)

`P_I |H| P_I=sum_k |tau_k| (u_k)_I (u_k)_I^T`,               (2.10)

and likewise on `J`.  In particular the easy scalar relaxations

`eta <= min{(sum tau_k^2 ||(u_k)_I||^2)^(1/2),`

`           (sum tau_k^2 ||(u_k)_J||^2)^(1/2),`

`           [(sum |tau_k| ||(u_k)_I||^2)(sum |tau_k| ||(u_k)_J||^2)]^(1/2)}`
                                                                    (2.11)

are always valid.  The operator form (2.2) is sharper because it retains orthogonality/cancellation geometry inside the physical banks.

## 3. Main theorem: spectral-threshold footprint compiler

Let

`A=A0+S+T`,                                                    (3.1)

where `A0,S,T` are symmetric and

`||T||op<=delta`.                                              (3.2)

No probabilistic smallness of `X^T T X` is asserted.  Diagonalize only the deterministic matrix `S`:

`S=sum_k tau_k u_k u_k^T`.                                    (3.3)

For any threshold `h>=0`, split

`H_h=sum_{|tau_k|>h} tau_k u_k u_k^T`,

`L_h=sum_{|tau_k|<=h} tau_k u_k u_k^T`.                       (3.4)

Then

`||L_h||op<=h`.                                                (3.5)

For a fixed protected original-coordinate cut `I|J`, define

`chi_h=chi(H_h;I,J)`,

`epsilon_h=delta+h+chi_h`.                                    (3.6)

### Theorem 3.1 — QFORM-SPECTRAL-THRESHOLD-FOOTPRINT-COMPILER-v1

For the actual final cross block `M=A[I,J]` and baseline `M0=A0[I,J]`,

`boxed: ||M-M0||op <= epsilon_h`                               (3.7)

for every `h>=0`.  Hence every completed original-coordinate cross theorem whose perturbation hypothesis is `||M-M0||op<=epsilon` may be applied with `epsilon=epsilon_h`.  Equivalently one may optimize over thresholds and use

`epsilon_* = inf_{h>=0} [delta+h+chi_h]`.                      (3.8)

#### Proof

From (3.1) and (3.4),

`M-M0=H_h[I,J]+L_h[I,J]+T[I,J]`.                              (3.9)

Rectangular compression cannot increase operator norm.  Lemma 2.1 and (3.5) therefore give

`||M-M0||op <= chi_h+h+delta=epsilon_h`.                       (3.10)

No random-variable operation has been performed.  QED.

### Interpretation

* Every eigenvalue in the small spectral cloud `|tau_k|<=h` is paid collectively by **one number `h`**, regardless of rank or sign.
* Every eigenvalue in the large spectral cloud `|tau_k|>h` can have arbitrarily large magnitude and either sign.  It is paid only through the original-coordinate footprint `chi_h`.
* The arbitrary-rank dense tail `T` is paid once by `delta` in a deterministic certificate on the actual final matrix.

This is exactly the distinction required for unbounded product inputs: small matrix norm is used to preserve a matrix certificate, never to claim `X^T T X` is small.

## 4. Actual application to the current volume-stability theorem

Assume for the same cut that

`s_3(M0)>=a>0`, `max_i(P_range(M0))_ii<=1/2`.                  (4.1)

If for some threshold `h`

`epsilon_h<=a/16`,                                             (4.2)

then (3.7) verifies the perturbation hypothesis of the current volume-stability theorem at `c2414e...`.  Therefore

`boxed: ||p_Q||infinity <= 24 sqrt(3)e/(5a) <23/a`,           (4.3)

and the density has a continuous version vanishing at infinity.  Arbitrary within-bank quadratic curvature, outside couplings and affine terms remain allowed because they are retained in the cited theorem.

This is an equation-level use of the newest continuation theorem: (3.7)+(4.2) is inserted directly into its hypothesis.

### A literal target-class family for (4.3)

Take original banks of sizes `|I|=6`, `|J|=3`, `|K|=3`, and set

`M0=sqrt(2) [I_3; I_3]`.                                      (4.4)

Then all three singular values of `M0` equal `2`, and its range projection has all six diagonal entries `1/2`.  Let

`A0 = [[0, M0, 0],[M0^T,0,0],[0,0,2 I_3]]`.                  (4.5)

The nonzero spectrum of the first two banks is `+2,+2,+2,-2,-2,-2`, and the last bank contributes three further `+2` eigenvalues.

Let `w_j=(M0 e_j/2 + e_{J,j})/sqrt(2)` be the normalized `+2` eigenvector from the cross block and let `g_j=e_{K,j}`.  (Since `||M0 e_j||=2`, the displayed vector has unit norm.)  For arbitrary `tau_1,tau_2,tau_3 in R`, put

`alpha_j^2=1/[32(1+|tau_j|)]`,

`v_j=sqrt(1-alpha_j^2) g_j+alpha_j w_j`,                      (4.6)

and

`H=sum_{j=1}^3 tau_j v_j v_j^T`.                              (4.7)

The `v_j` are orthonormal `+2` eigenvectors of `A0`; hence (4.7) literally replaces three eigenvalues `+2` by `2+tau_j`, with no restriction on magnitude or sign.  On `I|J`, the rank-one footprint of each `v_j` has operator size `alpha_j^2/2`, and the three directions are orthogonal on both sides, so

`||H[I,J]||op <= 1/64`.                                       (4.8)

Add any symmetric small spectral cloud `L` with `||L||op<=1/64` and any symmetric dense tail `T` with `||T||op<=1/64`.  Then the compiler gives

`epsilon <= 3/64 < 2/16`.                                    (4.9)

Therefore (4.3), with `a=2`, yields the explicit continuous bound

`boxed: ||p_Q||infinity <= 12 sqrt(3)e/5 = 11.2996853668...`  (4.10)

uniformly over all three arbitrary signed `tau_j` and over all such `L,T`.  Before `L+T`, at least six eigenvalues of `A0+H` remain exactly `+/-2`; since `||L+T||op<=1/32`, Weyl gives

`s_3(A0+H+L+T)>=2-1/32=63/32>1`,                              (4.11)

so every final matrix is genuinely in the exact QFORM target class.

## 5. Actual application of the designated fleet02/B12 partner result

For any baseline cross block `M0`, define from the compiler's `epsilon_h`

`b_j=(s_j(M0)-epsilon_h)_+`,                                  (5.1)

`R_h=sum_j b_j^2`, `C_h=(s_1(M0)+epsilon_h)^2`,               (5.2)

`rho_h=min{(sqrt(r0)+epsilon_h)^2,(sqrt(c0)+epsilon_h)^2}`.   (5.3)

Because (3.7) is exactly the perturbation premise of the partner theorem, that theorem gives

`boxed: ||p_Q||infinity <= 5 sqrt(2e)(b_1...b_5)^(-1/5)`      (5.4)

when `b_5>0`, and if

`R_h>2C_h`, `R_h-2C_h >= (9/2)rho_h`,                         (5.5)

then

`boxed: ||p_Q||infinity <= (9sqrt(3)e/2)`

`       *[R_h(R_h-C_h)(R_h-2C_h)/6]^(-1/6).`                 (5.6)

The second conclusion is continuous.  Equation (5.4) is also the direct application of the newest-Claude `D_5` theorem after (3.7) and singular-value Weyl give `s_j(M)>=b_j`.

### Eight simultaneous unbounded signed eigenvalue replacements

Take 24 original coordinates in three banks `I,J,K`, each of size 8, and set

`A0 = [[0,2I_8,0],[2I_8,0,0],[0,0,2I_8]]`.                   (5.7)

Its spectrum contains `+2` with multiplicity 16 and `-2` with multiplicity 8.  Put

`w_k=(e_k+e_{8+k})/sqrt(2)`, `g_k=e_{16+k}`.                  (5.8)

Both are `+2` eigenvectors.  For **arbitrary** real `tau_1,...,tau_8`, set

`alpha_k^2=1/[20(1+|tau_k|)]`,

`v_k=sqrt(1-alpha_k^2)g_k+alpha_k w_k`,                       (5.9)

`H=sum_{k=1}^8 tau_k v_k v_k^T`.                              (5.10)

The `v_k` are orthonormal `+2` eigenvectors, so (5.10) literally replaces eight eigenvalues `+2` by `2+tau_k`.  All signs and magnitudes are unrestricted.  Moreover

`P_I |H|P_I=P_J |H|P_J`

` = diag(|tau_k| alpha_k^2/2)`,                               (5.11)

in the natural bank bases.  Lemma 2.1 therefore gives, in fact sharply here,

`chi(H;I,J)<=max_k |tau_k|/[40(1+|tau_k|)]<=1/40`.           (5.12)

Add an arbitrary symmetric small spectral cloud `L` with `||L||op<=1/80` and an arbitrary symmetric dense tail `T` with `||T||op<=1/80`.  Taking the threshold payment `h=1/80` (or simply grouping this already-small cloud into the `h` term) gives

`epsilon_h<=1/40+1/80+1/80=1/20`.                            (5.13)

For `M0=2I_8`,

`b_j=39/20`, `j=1,...,8`,                                    (5.14)

`R_h=8(39/20)^2=30.42`,

`C_h=rho_h=(41/20)^2=4.2025`.                                (5.15)

The partner gate has the strict exact margin

`R_h-2C_h-(9/2)rho_h = 2483/800 =3.10375>0`.                (5.16)

Thus the designated partner inequality (5.6) applies to the **actual final matrix** and gives

`boxed: ||p_Q||infinity <=5.602062744709504...`               (5.17)

with a continuous density, uniformly in all eight arbitrary `tau_k`, every independent cap-one product source, and every `L,T` above.

For comparison, direct newest-Claude fifth-volume payment gives

`||p_Q||infinity <= 5 sqrt(2e)/(39/20)`

`                  =5.978574311787498...`.                    (5.18)

The partner collective-energy branch is therefore strictly sharper on this family.

The eight unmodified `+2` directions and all eight `-2` directions survive (5.10).  Since `||L+T||op<=1/40`,

`s_3(A0+H+L+T)>=2-1/40=79/40>1`.                              (5.19)

Hence this is again a literal family inside the full target class, not merely an abstract matrix perturbation example.

## 6. Why this is not a forbidden perturbative shortcut

For allowed input laws, small `||T||op` does not imply small `X^T T X`.  For example, with

`T=delta e_1e_1^T`, `X_1 ~ Uniform[R,R+1]`,

we have the admissible density cap one and

`X^T T X=delta X_1^2 >=delta R^2` almost surely.              (6.1)

The present proof uses `delta,h,chi_h` only to verify singular-value/volume/cross-energy hypotheses on the actual final matrix.  Thus arbitrary unbounded supports, fragmented laws and all outside quadratic couplings are retained.

## 7. What changed and what remains

The new content is the exact bridge

`arbitrary spectral modifications -> physical cross-footprint chi_h + spectral threshold h -> completed cross certificate`.

Compared with charging `||S||op`, it makes arbitrarily large eigenvalue changes free whenever their large-eigenvalue subspace has small physical cross footprint.  Compared with truncating by rank, it allows arbitrarily many small eigenvalues at once because their entire cloud costs only its spectral radius `h`.

This does **not** prove that every matrix with `s_3(A)>=1` admits a cut for which the compiled budget and a paid baseline certificate are simultaneously quantitative.  That structural extraction remains the exact gap.  The full conjecture therefore remains OPEN.

Continuity status: Sections 4 and the collective-energy branch of Section 5 give a continuous density by their cited Fourier theorems.  Essential boundedness is proved in every stated branch.  No general continuity claim for the unrestricted full conjecture is made.

## 8. Correction boundary and provenance

Fresh current controls and the live correction inbox were re-read during this invocation before publication.  The argument uses none of the refuted interfaces: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint coarea bound, no worst conditional projection-density moment, no post-rotation independence, no universally good single minor, and no universal rank-three cross cut.

The report is a supporting theorem, not a full solution and not an independent review of its source theorems.  Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
