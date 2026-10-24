SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T23:30:49Z.
attacking: aggregate principal-versus-overlap compound energy after one scalar pivot; seek a dimension-free averaged-frequency payment without selecting a single physical star.

# account03/B01 — scalar-pivot compound-operator closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `account03-B01-20260923T233049Z-auto11`  
Assignment: oscillatory replacement / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING TARGET-LEVEL THEOREM / HIGH-DIAGONAL BRANCH PAID / FULL QFORM OPEN**

## 1. Exact scope and correction boundary

Let `X_1,...,X_n` be independent real random variables whose probability densities satisfy `0<=f_i<=1`, and let `A` be real symmetric with `s_3(A)>=1`. No moment, support, Gaussian, log-concavity, connected-support, iid, spectral-coordinate independence, or post-rotation product assumption is used.

Fresh owner control was resolved on `yspennstate/math-research-brain/main`; immediately before publication it was commit `1e5b27aef796a45fad7fe5e2ba648f3b462e4626`. OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, with no pause for account03/B01. The live correction boundary was refreshed: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint coarea is not a valid replacement for product provenance; small matrix tails cannot be discarded without moment/support assumptions; rotations generally destroy independence; and the corrected account04/B01 random-coloring corollary is not used here.

The full conjecture remains open. This report proves a dimension-free closure of the three second-compound channels after **one literal original-coordinate scalar pivot**. It closes the principal-versus-overlap aggregate gap left by the preceding B01 run and gives a universal payment whenever that pivot has a quantitative lower bound.

## 2. Source-pinned inputs actually used

### 2.1 Designated partner account04/B01 — exact overlap-star identity

Canonical source:

`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260923T131003Z-account04-B01-singular-star-routing-r2/REPORT.md`.

Choose a literal original coordinate `i` with `a=A_ii!=0` and form the exact scalar Schur complement `H` on `K=[n]\{i}`. For a second literal coordinate `j in K`, account04/B01 proves the exact identity

`W_2({i,j})/a^2
 = sum_(k!=l; k,l!=j) det H[{j,k},{j,l}]^2.`                    (2.1)

Only this identity is used. In particular, the subsequently corrected individual-bank statement in that report is not used.

### 2.2 Determinant-free single-star receiver

Earlier account03/B01 source:

`yspennstate/math-open-problems@26f7f13da915bad3b848ea49a91320c01c81cb1c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T203127Z-auto11/REPORT.md`.

For the same first pivot `a` and any second coordinate `j`, if `W_2({i,j})>0`, then the full ambient form has an essentially bounded density with the uniform estimate

`||p_Q||_infinity
 <= K_W |a|^(-1/4) W_2({i,j})^(-1/8),`                          (2.2)

where it is safe to take

`K_W=77.02149767209895.`                                        (2.3)

This includes both nonzero and exactly singular second Schur pivots; the singular endpoint actually has a substantially smaller constant. The theorem retains arbitrary dense/high-rank remaining curvature and affine terms.

### 2.3 Scalar-Schur aggregate-E2 receiver

Canonical source:

`yspennstate/math-open-problems@2cb64b71f8aafa0892547dffebcf6af647ea7c64`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T102108Z-account03-B08-qform-diffuse-r32/REPORT.md`.

If the exact scalar Schur matrix contains a literal original-coordinate cross block `N` with

`Delta_2=E_2(N)=sum_(|R|=|C|=2) det N[R,C]^2>0`,

then

`||p_Q||_infinity
 < C_E2 |a|^(-1/2) Delta_2^(-1/8),`                             (2.4)

with

`C_E2=2 sqrt(10) 7^(9/10)=36.44334493792993... .`               (2.5)

The source retains arbitrary same-bank curvature and all other residual couplings.

### 2.4 Orientation-free rank-two affine half-Riesz theorem

Canonical source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For any invertible symmetric `2x2` matrix `B`, any two original independent coordinates, and any affine term induced by conditioning all other coordinates,

`sup_t E |Z^T B Z + linear(Z)-t|^(-1/2)
 <=128 |det B|^(-1/4).`                                        (2.6)

### 2.5 Designated partner signed-Fejer equivalence

Canonical source:

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For a probability law `mu`,

`D_T mu(y)=(1/(2pi)) int_(-T)^T (1-|t|/T)
 Re(e^(-ity) phi_mu(t)) dt`,                                    (2.7)

and

`||p_mu||_infinity=sup_(T>0,y)D_T mu(y)`                        (2.8)

in the bounded-density sense. This is the averaged-frequency interface used below; no absolute Fourier-`L1` assertion is made.

## 3. One scalar pivot and the second compound

Choose one ORIGINAL coordinate `i` with

`a=A_ii!=0`,                                                     (3.1)

and let

`H=A[K,K]-a^(-1)A[K,i]A[i,K]`, `K=[n]\{i}`.                    (3.2)

Completing only this literal coordinate gives

`Q=a(X_i+h(X_K))^2+R(X_K)`,                                     (3.3)

where the residual quadratic matrix is exactly `H` and all affine terms are retained.

The rank-one decomposition

`A=diag(0,H)+a (1,A[K,i]/a)^T(1,A[K,i]/a)`                       (3.4)

implies rank-one singular-value interlacing

`s_(k+1)(A)<=s_k(H).`                                            (3.5)

Since `s_3(A)>=1`,

`s_2(H)>=1`, hence `s_1(H)s_2(H)>=1`.                            (3.6)

Index the exterior square by unordered two-subsets `alpha={j,k}` of `K`, each written in increasing order. Set

`C=wedge^2 H`, so `C_(alpha,beta)=det H[alpha,beta]`.             (3.7)

Because `H` is symmetric, `C` is symmetric, and

`||C||_op=s_1(H)s_2(H)>=1`.                                     (3.8)

Split `C` exactly into

`C=P+O+D`,                                                       (3.9)

where `P` is the diagonal part (`alpha=beta`), `O` contains entries with `|alpha intersect beta|=1`, and `D` contains entries with `alpha intersect beta=empty`.

Define

`p_* = ||P||_op = max_(|alpha|=2)|det H[alpha,alpha]|`,          (3.10)

`D_2 = ||D||_F^2
    = sum_(alpha intersect beta=empty) det H[alpha,beta]^2.`     (3.11)

For each coordinate `j in K`, let `O^(j)` contain exactly those overlap-one entries whose unique shared coordinate is `j`. Thus

`O=sum_(j in K) O^(j)`                                          (3.12)

with no double counting. Put

`S_j=||O^(j)||_F^2
   =sum_(k!=l;k,l!=j)det H[{j,k},{j,l}]^2`,                     (3.13)

`S_*=max_j S_j.`                                                 (3.14)

By the designated account04/B01 identity (2.1),

`boxed: W_2({i,j})=a^2 S_j.`                                    (3.15)

This is the required equation-level application of the partner result.

## 4. New dimension-free overlap-star operator bound

### Lemma 4.1 — `QFORM-COMPOUND-STAR-OPERATOR-v1`

With the notation above,

`boxed: ||O||_op <=2 sqrt(S_*).`                                (4.1)

#### Proof

Let `E_j` be the subspace of the pair-index space spanned by two-subsets containing `j`, and let `Pi_j` denote its orthogonal projection. Since `O^(j)` is supported on `E_j x E_j`, for every vector `x`,

`|<x,O x>|
 <=sum_j |<Pi_j x,O^(j)Pi_j x>|`
`<=sum_j ||O^(j)||_op ||Pi_j x||^2`
`<=sqrt(S_*) sum_j ||Pi_j x||^2.`                               (4.2)

Every unordered two-subset contains exactly two coordinates. Therefore

`sum_j ||Pi_j x||^2=2||x||^2.`                                  (4.3)

Taking the supremum over unit vectors proves (4.1). QED.

This is the key aggregation step: even if the total overlap-one Frobenius mass is spread over arbitrarily many physical stars, its **operator effect** cannot exceed twice the largest star Frobenius norm. There is no factor depending on `n`.

Since `||D||_op<=||D||_F=sqrt(D_2)`, (3.8)-(4.1) imply the deterministic closure

`boxed:
1 <= p_* + 2 sqrt(S_*) + sqrt(D_2).`                             (4.4)

## 5. Three paid branches

Use the simple thresholds

`sqrt(D_2)=1/40`, `p_*=31/40`.                                  (5.1)

### Branch A: disjoint second-compound energy

If

`D_2>=1/1600`,                                                   (5.2)

randomly two-color the coordinates of `K`. A fixed ordered disjoint pair of two-subsets lands with its row pair in the first bank and its column pair in the second with probability `1/16`; hence some literal original-coordinate cut has

`Delta_2>=D_2/16.`                                               (5.3)

Applying (2.4),

`||p_Q||_infinity
 < C_E2 sqrt(2)|a|^(-1/2)D_2^(-1/8)`
`<=129.612900 |a|^(-1/2).`                                      (5.4)

### Branch B: one principal physical pair in the residual

Suppose (5.2) fails but

`p_*>=31/40.`                                                    (5.5)

Choose `alpha={j,k}` attaining `p_*`. Condition on all residual coordinates except `X_j,X_k`. The conditional residual is a quadratic-plus-linear form in these two independent original coordinates with physical quadratic block `H[alpha,alpha]`, whose determinant has magnitude `p_*`. By (2.6), uniformly in the conditioning and target level,

`H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <=128 p_*^(-1/4).`                                              (5.6)

Conditioning the outer coordinate `X_i` in (3.3) gives the elementary translated-square density envelope

`||p_Q||_infinity <= |a|^(-1/2)H_(1/2)(R).`                     (5.7)

Therefore

`||p_Q||_infinity
 <=128(40/31)^(1/4)|a|^(-1/2)`
`<136.422042 |a|^(-1/2).`                                       (5.8)

### Branch C: overlap-star energy

Assume both (5.2) and (5.5) fail. Then (4.4) gives

`2 sqrt(S_*)
 >1-1/40-31/40=1/5`,                                            (5.9)

so

`boxed: S_*>1/100.`                                              (5.10)

Choose `j` attaining `S_*`. The designated partner identity (3.15) gives the actual physical-star inequality

`W_2({i,j})>a^2/100.`                                            (5.11)

Now apply the determinant-free account03/B01 receiver (2.2):

`||p_Q||_infinity
 <=K_W |a|^(-1/4)W_2({i,j})^(-1/8)`
`<K_W 100^(1/8)|a|^(-1/2)`
`<136.965744 |a|^(-1/2).`                                       (5.12)

No division by the second physical-pair determinant occurs.

## 6. Main theorem and high-diagonal corollary

### Theorem 6.1 — `QFORM-SCALARPIVOT-COMPOUND-OPERATOR-CLOSURE-v1`

Under the exact target assumptions, if `s_3(A)>=1` and one literal physical diagonal coefficient satisfies `a=A_ii!=0`, then `Q=X^TAX` has an essentially bounded density and

`boxed:
||p_Q||_infinity <137 |a|^(-1/2).`                              (6.1)

The estimate is dimension-free, sign-free, permits arbitrary additional spectrum and arbitrary dense residual curvature, and uses only original-coordinate conditioning/completion. It does **not** assert that `|a|` is universally bounded below.

Consequently, the entire high-physical-diagonal chamber

`max_i |A_ii|>=1/64`                                             (6.2)

is paid by

`boxed: ||p_Q||_infinity <1096.`                                 (6.3)

This closes the principal-versus-overlap aggregate obstruction left by the preceding B01 second-compound decomposition.

### Homogeneity

If `A` is replaced by `lambda A`, then `a` is multiplied by `lambda`, while the normalized premise `s_3(A)>=1` is not scale-invariant. More generally, retaining the actual spectral scale `L=s_3(A)>0` and applying the theorem to `A/L` gives

`||p_(X^TAX)||_infinity
 <137 (L |A_ii|)^(-1/2).`                                       (6.4)

This scales as `|lambda|^-1`, as required.

## 7. Averaged-frequency consequence and preserved pointwise counterexample

By the designated account04/B01 signed-Fejer equivalence (2.8), every branch above gives the exact averaged-frequency replacement

`boxed:
sup_(T>0,y) D_T law(Q)(y)
 <137 |a|^(-1/2).`                                              (7.1)

In particular, (6.2) implies

`sup_(T,y)D_T law(Q)(y)<1096.`                                  (7.2)

No absolute Fourier-`L1` estimate is asserted.

The phase-aligned obstruction is preserved explicitly. Given any fixed nonzero frequency `s` and any `eta>0`, the set

`E_(s,eta)={x:dist(sx^2,2pi Z)<=eta}`                            (7.3)

has infinite Lebesgue measure. Choose a finite union of measurable fragments inside it of total measure one and let its indicator be the input density. Then

`Re E exp(i s X^2)>=cos(eta).`                                  (7.4)

Thus no positive law-uniform pointwise quadratic-phase power decay can hold. The theorem above succeeds instead by converting spectral rank into a second-compound operator inequality and then into density/signed-Fejer estimates.

## 8. Target-valid overlap-star stress family

Let `m>=2` and let `H_m` be the `(m+1)x(m+1)` normalized star matrix, with center `0`, leaves `1,...,m`,

`(H_m)_(0k)=(H_m)_(k0)=m^(-1/2)`,                               (8.1)

and every other entry zero. Its nonzero eigenvalues are exactly `1,-1`. Set

`A_m=[1] direct_sum H_m.`                                       (8.2)

Then

`spec_nonzero(A_m)={1,1,-1}`,                                   (8.3)

so it is an exact target-valid family. Use the singleton `[1]` as the first scalar pivot `a=1`; its Schur residual is exactly `H_m`.

For this residual,

`p_*=1/m ->0`,                                                   (8.4)

`D_2=0`,                                                         (8.5)

but the center star has

`S_0=sum_(k!=l)(1/m^2)=(m-1)/m.`                                (8.6)

Hence, by the designated partner identity,

`W_2({i,0})=(m-1)/m.`                                           (8.7)

The physical pair `{i,0}` has exact second Schur pivot `delta=0`, so the sharper exact-singular receiver from the earlier B01 theorem gives

`||p_Q||_infinity
 <=4 sqrt(2)e^(1/4)[(m-1)/m]^(-1/8)`
`<=7.920952.`                                                    (8.8)

Thus there are target-valid matrices for which the residual principal-pair currency tends to zero and the disjoint compound currency vanishes identically, while a high-cardinality overlap star remains dimension-free and the partner-fed branch pays the full form uniformly.

## 9. What remains

This run does **not** solve the unrestricted conjecture because (6.1) deteriorates when every physical diagonal is tiny. The next B01 implication is now cleanly upstream:

`QFORM-SMALLDIAG-AGGREGATE-CROSS-OR-GROUPED-SQUARE-v1`:

> Under `s_3(A)>=1` and `max_i |A_ii|<1/64`, obtain a universal density/signed-Fejer payment by aggregating zero/small-diagonal hyperbolic cross structure before any reciprocal scalar pivot, or route it into an already-paid grouped-square/ridge/cross-volume branch.

The all-small-diagonal branch cannot be handled by simply choosing the largest nonzero diagonal and applying (6.1), since that would lose the desired universal constant. It needs a genuinely aggregate, pivot-free mechanism.

**Continuity:** The present proof establishes absolute continuity and an essentially bounded density in the stated branches. It does not prove continuity of the full density.

**Brain status:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval and writeback are genuine, but no authenticated native learned-memory receiver ingestion was established.
