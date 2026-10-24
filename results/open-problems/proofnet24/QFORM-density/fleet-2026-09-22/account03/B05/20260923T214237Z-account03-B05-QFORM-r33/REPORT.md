SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T21:42:37Z.
attacking: QFORM-HEAVY-TOWER-PLUECKER-COMPILER-v1 — compile the r32 repeated heavy-row descent into a fixed-length original-product Pluecker trichotomy, so an arbitrarily long conditioning tower is no longer an admissible endpoint.

# account03/B05 r33 — heavy-row tower = exact Pluecker exhaustion

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea / product-preserving interval bound  
Owner control revision: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING GEOMETRIC COMPILER; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Continuity: proved only on the exact-cross branch below; not proved by the partner exact-slope branch or by the structural endpoints.

## 1. Sources actually used

1. r32 heavy-row descent (read from its immutable proof):
   `yspennstate/math-open-problems@0e5ef0d3f80bd0d28c449a6f20b8d780ca894e5d:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T204411Z-account03-B05-QFORM-r32/REPORT.md`.
2. r31 determinant-sensitive exact-cross theorem and ratio-packet crossing identity:
   `yspennstate/math-open-problems@95f94696393b5ad8b0def71fa0d93082de92bd85:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T193756Z-account03-B05-QFORM-r31/REPORT.md`.
3. Designated partner account04/B05 exact-slope theorem:
   `yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f:proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`, proving
   `||p_Q||_infinity < 51.6 (mu m_*)^(-1/3)`.
4. Current corrections were reread before publication. In particular, no arbitrary-joint coarea estimate, conditional density-cap moment, rotated-coordinate independence, pointwise van der Corput estimate, or small-random-tail deletion is used.

The new point is that the r32 tower has an exact invariant that was not used there: the determinant of the **fixed original two-frame Gram matrix**. Heavy leverage consumes this determinant geometrically. This gives a fixed-length compiler.

## 2. Fixed-frame subset determinant identity

Start with the r32 nonzero-residual ratio packet on an original-coordinate bank `G_0`. Write

`m_0 = sum_i u_i^2`,
`r_0 = (sum_i u_i t_i)/m_0`,
`e_i = t_i-r_0 u_i`,
`sigma_0^2 = sum_i e_i^2 > 0`.

Then `sum_i u_i e_i=0`, and the fixed Parseval frame is

`g_i = (u_i/sqrt(m_0), e_i/sigma_0)`,

so

`sum_i g_i g_i^T = I_2`.

For an arbitrary subset `K subseteq G_0` with

`m_K=sum_{i in K}u_i^2>0`,
`r_K=(sum_{i in K}u_i t_i)/m_K`,
`sigma_K^2=sum_{i in K}(t_i-r_Ku_i)^2`,

put

`G_K = sum_{i in K} g_i g_i^T`.

### Lemma 2.1 (`QFORM-SUBSET-GRAM-RESIDUAL-IDENTITY-v1`)

One has the exact identity

`boxed: det G_K = m_K sigma_K^2/(m_0 sigma_0^2).`

Equivalently, by Cauchy-Binet,

`boxed: det G_K = sum_{i<j, i,j in K} det(g_i,g_j)^2.`

### Proof

In the fixed coordinates `(u,e)`,

`G_K = diag(m_0^(-1/2),sigma_0^(-1))
       [[sum_K u_i^2, sum_K u_i e_i],
        [sum_K u_i e_i, sum_K e_i^2]]
       diag(m_0^(-1/2),sigma_0^(-1)).`

Hence

`det G_K = [m_K sum_K e_i^2-(sum_K u_i e_i)^2]/(m_0 sigma_0^2).`

But `r_K-r_0=(sum_Ku_ie_i)/m_K`, so the numerator is

`m_K min_a sum_K(e_i-a u_i)^2
 = m_K sum_K(t_i-r_Ku_i)^2
 = m_K sigma_K^2`.

This proves the first identity. The second is the `2 x |K|` Cauchy-Binet formula. QED.

This identity is product-coordinate geometry. It does not condition a dependent projection and does not use any law beyond the original independence/cap assumptions.

## 3. Exact heavy-row determinant consumption

Let `K` be a current descendant subset with `det G_K>0`. Normalize the current two-frame by whitening `G_K`. For a row `h in K`, its current leverage is

`q_h^(K) = g_h^T G_K^(-1) g_h`.

This is exactly the row norm squared used by r32 after re-orthogonalizing the descendant packet.

Let `K'=K\{h}`.

### Lemma 3.1 (`QFORM-PLUECKER-ROW-PEEL-IDENTITY-v1`)

One has

`boxed: det G_K' = det G_K (1-q_h^(K)).`

Moreover, if `Delta_ij=det(g_i,g_j)`, then

`boxed: det G_K-det G_K' = sum_{i in K'} Delta_hi^2 = q_h^(K) det G_K.`

### Proof

The first identity is the matrix determinant lemma applied to

`G_K' = G_K-g_hg_h^T`.

The second follows either by subtracting the Cauchy-Binet formulas of Lemma 2.1 or by the first identity. QED.

Thus every r32 **heavy** step, where `q_h^(K)>=1/2`, consumes at least one half of the remaining internal Pluecker mass:

`det G_K' <= (1/2) det G_K`.

This is strictly stronger for the tower geometry than the r32 estimate `sigma'^2 <= (5/8)sigma^2`.

## 4. Star decomposition of the entire tower

Suppose the r32 heavy alternative is iterated without the partner payment. Let

`K_0=G_0`,
`K_j=K_{j-1}\{h_j}`,
`H_j={h_1,...,h_j}`,
`D_j=det G_{K_j}`.

At every such step `q_j:=q_{h_j}^{(K_{j-1})}>=1/2`. Since `D_0=1`, Lemma 3.1 gives

`boxed: D_j = product_{ell=1}^j (1-q_ell) <= 2^(-j).`

Even more importantly, the Pluecker mass is exhausted by **disjoint stars**:

`boxed:
1-D_k
 = sum_{j=1}^k q_j D_{j-1}
 = sum_{j=1}^k sum_{i in K_j} Delta_{h_j i}^2.`

Each unordered pair occurs at most once in the last double sum, at the moment its earlier-peeled endpoint is removed. Therefore a long tower is not geometrically featureless: it converts the original unit Pluecker mass into explicit original-coordinate star mass.

For `k=6`,

`D_6 <= 1/64`.

So the “arbitrarily long heavy tower” named as the r32 obstruction can be replaced by a fixed six-step geometric endpoint.

## 5. A fixed-threshold trichotomy

For any split `G_0=H disjoint_union K`, set

`E(H)=det G_H`, `D(K)=det G_K`.

Because `G_H+G_K=I_2`, if the eigenvalues of `G_K` are `lambda_1>=lambda_2`, then

`D(K)=lambda_1 lambda_2`,
`E(H)=(1-lambda_1)(1-lambda_2)`.

Fix

`eta=1/64`.

Assume that the process remains in the r32 heavy residual alternative until the first index `k` for which

`D_k<=eta`.

Such a `k` exists with `k<=6`. Put `E_j=det G_{H_j}`. Since `G_{H_j}` increases in PSD order, `E_j` is nondecreasing.

At this first threshold crossing exactly one of the following occurs.

### A. Two-sided Pluecker mass before collapse

If

`E_{k-1} >= eta/2`,

then `D_{k-1}>eta`, hence

`boxed: sqrt(E_{k-1}D_{k-1}) >= eta/sqrt(2).`

This is already an **unconditional original-coordinate split** of the original packet. No previously peeled coordinate has to remain conditioned.

The r31 exact-cross calculation works for an arbitrary first-bank split and gives crossing volume

`Delta_YZ = mu m_0 |z_1z_2| sqrt(E_{k-1}D_{k-1}).`

Therefore, whenever the mixed residual currency is nonzero,

`boxed:
||p_Q||_infinity
 <= 6 [sqrt(2)/(eta mu m_0 |z_1z_2|)]^(1/3)
 = 6 [64 sqrt(2)/(mu m_0 |z_1z_2|)]^(1/3).`

This branch has a **continuous** density because it is an `L^1` exact-cross Fourier exit.

For the standard packet `m_0>=3/20`, the concrete chamber `mu |z_1z_2|>=1` gives

`||p_Q||_infinity < 50.71.`

No claim is made that `mu |z_1z_2|` is automatically bounded below; the previously identified escaped-curvature branches remain necessary when it collapses.

### B. Complementary rank-one two-bank endpoint

Suppose `E_{k-1}<eta/2` and, after adding `h_k`, still

`E_k<=eta`.

Then both

`D_k<=eta`, `E_k<=eta`.

Let `lambda_1>=lambda_2` be the eigenvalues of `G_{K_k}`. Since `eta<1/4`, these two determinant inequalities force

`lambda_1>=1/2`, `lambda_2<=1/2`,
`lambda_2<=2eta`, `1-lambda_1<=2eta`.

If `P` is the orthogonal rank-one projection onto the top eigendirection of `G_{K_k}`, then

`boxed: ||G_{K_k}-P||_op <= 2eta = 1/32,`

and, because `G_{H_k}=I-G_{K_k}`,

`boxed: ||G_{H_k}-(I-P)||_op <= 1/32.`

The cross Pluecker mass is

`C_k=sum_{h in H_k,i in K_k}Delta_hi^2
    =1-E_k-D_k`,

so

`boxed: C_k>=1-2eta=31/32.`

Thus the long-heavy endpoint is not an uncontrolled descendant: it is an **independent two-bank near-orthogonalization**. One original-coordinate bank carries almost one coefficient-plane direction and the other carries almost the orthogonal direction, while at least `31/32` of the total Pluecker mass is cross-bank.

The unresolved factor is now precise: the small operator tails in these two coefficient-plane directions cannot be deleted or called small random errors, because the input laws have no moment or support bound. A receiver must keep those tails inside the product integral.

### C. One literal coordinate is a genuine bi-star

The only remaining possibility is

`E_{k-1}<eta/2` but `E_k>eta`.

Adding the literal row `h_k` increases the peeled internal Pluecker mass by

`E_k-E_{k-1}
 = sum_{j<k} Delta_{h_k h_j}^2
 > eta/2.`

At the same time, because `D_{k-1}>eta`, `q_k>=1/2`, and `D_k=(1-q_k)D_{k-1}`,

`D_{k-1}-D_k
 = sum_{i in K_k}Delta_{h_k i}^2
 =q_kD_{k-1}
 >eta/2.`

Hence

`boxed:
sum_{j<k}Delta_{h_k h_j}^2>1/128,
qquad
sum_{i in K_k}Delta_{h_k i}^2>1/128.`

So a single **literal original coordinate** is Pluecker-transverse to both the already peeled bank and the still-unpeeled bank. The tower terminates at a quantitative bi-star, not at an unstructured infinite conditioning chain.

This bi-star is a geometric certificate only. A full QFORM payment still has to combine it with the scalar-pair curvature before reciprocal minor inversion; selecting one star edge and paying its reciprocal would revive a known bad interface.

## 6. Partner theorem applied to the fixed-length compiler

The designated account04/B05 theorem is not merely cited. At every stage before the six-step endpoint, r32 says that if the selected heavy row has

`u_h^2/m_j >= 1/8`,

then conditioning only the previously peeled **literal original coordinates** and applying the partner exact-slope theorem gives, uniformly in those conditioning values,

`||p_Q||_infinity < 51.6 (mu m_j/8)^(-1/3).`

If this payment has not fired earlier, r32 also gives

`m_j >= (7/8)^j m_0`.

Because the new determinant compiler stops the heavy chain by `j<=6`, the partner loss can no longer grow through an arbitrarily long tower. For the standard packet `m_0>=3/20`, any partner payment during this compiler obeys

`boxed:
||p_Q||_infinity
 <51.6 [8/(mu (7/8)^6 (3/20))]^(1/3)
 <253.69 mu^(-1/3).`

In particular this branch is `<253.69` when `mu>=1`.

This explicitly applies the completed account04/B05 result to the live compiler.

## 7. What the new theorem changes

The r32 first missing implication was an **arbitrarily long** residual-heavy tower. The exact fixed-frame determinant identity shows that this particular obstruction is not real: six consecutive leverage-`>=1/2` residual descents already consume all but `1/64` of the internal Pluecker determinant.

Hence the next obligation is finite and geometric:

`QFORM-HEAVY-PLUECKER-ENDPOINT-RECEIVER-v1`:

- pay Case A by the exact-cross theorem whenever its residual determinant currency survives (already done above);
- in Case B, retain the `<=1/32` coefficient tails in the independent near-orthogonal two-bank product decomposition rather than deleting them;
- in Case C, aggregate the two `>1/128` bi-star Pluecker packets jointly with the physical scalar pair before selecting/inverting a minor;
- if the r31 residual currencies collapse, route them to the previously isolated escaped-curvature / one-hub mechanisms rather than calling the residual a small random error.

This is materially narrower than “compile arbitrarily many peeled coordinates”: the number of heavy stages is now universally bounded by six before an explicit structural certificate appears.

## 8. Scope and integrity

- Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity remains **OPEN**.
- No Gaussianity, moments, log-concavity, bounded support, connected support, or diagonal-basis assumption is introduced.
- No independence is asserted after a rotation.
- No arbitrary-joint coarea theorem or positive conditional-density moment is used.
- No small coefficient tail is discarded as a small random variable.
- The new identities are deterministic and exact; finite computation is only a regression check.
