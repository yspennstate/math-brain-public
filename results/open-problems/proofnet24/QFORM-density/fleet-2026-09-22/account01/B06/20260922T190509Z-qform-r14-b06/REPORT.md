# account01/B06 — zero-Schur fractional trace and determinant-zero pair endpoint

**Run:** `20260922T190509Z-qform-r14-b06`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh control used before publication:** `yspennstate/math-research-brain@bc641207682ca86ebe9b5bac4bccce2d78c053b8`, OWNER CONTROL revision `2026-09-22.13`  
**Assignment:** curved fiber integration / geometry  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / NEAR-ZERO_EXTENSION_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction gate

The sole target remains: for independent real coordinates with densities `0<=f_i<=1` and a real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential bound on the density of `X^T A X`, or give a valid target counterexample. No moment, support, Gaussian, log-concave, post-rotation-independence, or diagonal-basis assumption is introduced.

The live correction inbox was checked through brain commit `bc641207682ca86ebe9b5bac4bccce2d78c053b8`. In particular, this report does **not** use the refuted arbitrary-joint rank-three coarea bound, the refuted positive conditional-density moment, unrestricted fiber suprema, a fixed good physical minor, or pointwise law-uniform Fresnel decay. The revision-.13 OWNER MESSAGE repeats some older coarea claims; the source-backed corrections in `CURRENT_RESEARCH.md` and `CORRECTION_INBOX.json` override those mathematical claims as premises. The full target remains open.

Named partner actually consumed and applied: account02/B06 run `b06-20260922T155426Z-9fd56fa68a65`, canonical report `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. I use its proved `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` in dimension one:

`||p_{sum_j c_j X_j}||_infinity <= sqrt(e) / ||c||_2`                                  (1.1)

for every nonzero coefficient vector `c` and independent cap-one coordinates. This is the product-preserving input below.

## 2. Compact conditional end-to-end route

A presently viable physical-coordinate route is:

1. choose a quantitatively usable scalar pivot and complete its square;
2. control the resulting Schur remainder by a translation-uniform fractional trace;
3. feed that half-Riesz trace into the outer square kernel to obtain an `L^infinity` density bound;
4. combine this branch with the already proved diffuse/ridge/grouped branches.

The first missing implication in the zero/near-isotropic pivot regime was whether a Schur row with zero quadratic coefficient can be paid without selecting a second invertible physical minor. The theorem below answers the **exact-zero** case in arbitrary dimension and arbitrary matrix rank. The subsequent counterexample shows why replacing exact zero by merely small diagonal is not legitimate.

## 3. Exact-zero affine half-Riesz theorem

### Theorem A — `QFORM-ZERO-DIAGONAL-AFFINE-HALF-RIESZ-v1`

Let `X=(X_1,...,X_m)` have independent probability densities bounded by one. Let `S=S^T` be any real symmetric `m x m` matrix, let `b in R^m`, `c in R`, and choose an index `i` such that

`S_ii=0`,

`beta_i := (sum_{j != i} S_ij^2)^(1/2) > 0`.

Then, for every real `t`,

`E | X^T S X + b^T X + c - t |^(-1/2)
    <= C0 beta_i^(-1/2)`,                                             (3.1)

where

`C0 = 4 sqrt(2) e^(1/4) < 7.264`.                                    (3.2)

No rank assumption on `S` is used, and the affine vector is arbitrary.

### Proof

Write `X=(X_i,Z)` and

`W(Z)=2 sum_{j != i} S_ij X_j + b_i`,

`H(Z)=Z^T S_{-i,-i} Z + b_{-i}^T Z + c - t`.

Because `S_ii=0`,

`X^T S X+b^T X+c-t = W(Z) X_i + H(Z)`.                               (3.3)

For fixed `w != 0` and arbitrary `h`, the one-dimensional bathtub/rearrangement principle gives

`int f_i(x) |w x+h|^(-1/2) dx
 <= int_{-1/2}^{1/2} |w x|^(-1/2) dx
 = 2 sqrt(2) |w|^(-1/2)`.                                            (3.4)

The exceptional event `W=0` has probability zero once we know that `W` has a density. Put

`U=sum_{j != i} S_ij X_j`.

The partner theorem (1.1), with coefficient Euclidean norm `beta_i`, gives

`||p_U||_infinity <= sqrt(e)/beta_i`.

After scaling and translation,

`||p_W||_infinity <= M := sqrt(e)/(2 beta_i)`.                        (3.5)

Among all probability densities bounded by `M`, the negative half moment is maximized by filling the interval nearest the origin. Hence

`E |W|^(-1/2)
 <= M int_{-1/(2M)}^{1/(2M)} |w|^(-1/2) dw
 = 2 sqrt(2M)`.                                                       (3.6)

Averaging (3.4) and using (3.6) yields

`E|...|^(-1/2)
 <= 2 sqrt(2) * 2 sqrt(2M)
 = 8 sqrt(M)
 = 4 sqrt(2) e^(1/4) beta_i^(-1/2)`,                                (3.7)

which is (3.1). `QED`

A direct small-ball corollary is

`P(|X^T S X+b^T X+c-t| <= rho)
 <= C0 beta_i^(-1/2) rho^(1/2)`.                                    (3.8)

This is a translation-uniform fractional-trace estimate. Crucially, the arbitrary quadratic remainder `H(Z)` is never conditioned away; only the original independent coordinate `X_i` and the product-law linear form `W` are used.

## 4. Density closure after one outer scalar pivot

### Corollary B — `QFORM-OUTER-PIVOT-ZERO-SCHUR-v1`

Let

`Q(X_k,Z)=a X_k^2+2 X_k v^T Z+Z^T C Z + l_k X_k+l^T Z+c`,

with `a != 0` and all physical coordinates independent with densities at most one. Complete the square in the original coordinate `X_k` and set

`S=C-vv^T/a`,

with the corresponding affine remainder `tilde l, tilde c`. If some residual physical coordinate `i` obeys

`S_ii=0`,

`beta_i=(sum_{j != i,k}S_ij^2)^(1/2)>0`,

then `Q` has an essentially bounded density and

`||p_Q||_infinity
 <= C0 |a|^(-1/2) beta_i^(-1/2)`.                                    (4.1)

### Proof

For fixed `Z`, the conditional density of the shifted square

`a (X_k + a^(-1)(v^T Z+l_k/2))^2`

at displacement `u` is at most `|a|^(-1/2)|u|^(-1/2)` on its supported side: the two roots each contribute at most `1/(2 sqrt(|a u|))`. Therefore

`p_Q(t)
 <= |a|^(-1/2) E | Z^T S Z + tilde l^T Z+tilde c-t |^(-1/2)`.

Apply Theorem A. `QED`

This is an arbitrary-rank ambient theorem. It closes a genuine class that the invertible-pair certificate does not cover: the secondary Schur diagonal may vanish exactly.

## 5. Exact rank-three determinant-zero identity

Now assume the exact-rank-three representation

`A=R Lambda R^T`, `R^T R=I_3`, `det Lambda !=0`.

Let rows of `R` be `r_j`. Choose a physical pivot `k` with

`a=A_kk !=0`.

For `i != k`, define the physical two-by-two determinant

`d_ki = A_kk A_ii-A_ki^2`,

and the full three-frame pair area

`Delta_ki = ||r_k wedge r_i||^2
          = ||r_k||^2 ||r_i||^2-<r_k,r_i>^2`.                         (5.1)

### Corollary C — `QFORM-RANK3-ZERO-MINOR-ENDPOINT-v1`

If `d_ki=0` and `Delta_ki>0`, then

`||p_{X^T A X}||_infinity
 <= C0 [ |a| |det Lambda| Delta_ki ]^(-1/4)`.                         (5.2)

### Proof

After pivoting on `k`, the Schur complement is

`S=A_{-k,-k}-A_{-k,k}A_{k,-k}/a`.

Schur's determinant identity gives

`S_ii=d_ki/a=0`.                                                      (5.3)

For every `j` distinct from `i,k`,

`det S_{ {i,j} } = det A_{ {k,i,j} }/a`.                             (5.4)

Because `S_ii=0`, the left side equals `-S_ij^2`, hence

`S_ij^2 = |det A_{ {k,i,j} }|/|a|`.                                  (5.5)

Exact rank three gives

`det A_{ {k,i,j} } = det(Lambda) det(R_{ {k,i,j} })^2`.              (5.6)

Summing (5.5) over `j` and using `sum_j r_j r_j^T=I_3`,

`beta_i^2
 = |det Lambda|/|a| * sum_j det(R_{ {k,i,j} })^2
 = |det Lambda|/|a| * ||r_k wedge r_i||^2
 = |det Lambda| Delta_ki/|a|`.                                       (5.7)

Insert (5.7) into (4.1), obtaining (5.2). `QED`

For the same-sign two-plane used by the partner, its Pluecker weight `w_ki` is one coordinate-square of `r_k wedge r_i`, so

`Delta_ki >= w_ki`.                                                   (5.8)

Therefore, on the partner's exact support-disjoint Hadamard phenomenon where `w_ki>0` but `d_ki=0`, the pair is **not analytically useless**: it satisfies the finite endpoint estimate

`||p_Q||_infinity <= C0 [|a| |det Lambda| w_ki]^(-1/4)`.             (5.9)

This does not by itself give a dimension-free bound after selecting one tiny pair; the diffuse Hadamard family is paid by the separate aggregate branch. The point is that the determinant-zero endpoint is now controlled rather than singular.

## 6. Exact-zero is essential for this half-Riesz mechanism

The tempting extension “replace `S_ii=0` by `|S_ii|` small while keeping only `beta_i`” is false.

### Counterexample — `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`

For `0<epsilon<=1`, let

`S_epsilon = [[epsilon,1],[1,epsilon^(-1)]]
            = v_epsilon v_epsilon^T`,

`v_epsilon=(sqrt(epsilon),epsilon^(-1/2))`.

Then `(S_epsilon)_11=epsilon ->0` while the first-row off-diagonal norm is identically one. For independent `X_1,X_2 ~ Uniform[-1/2,1/2]`,

`X^T S_epsilon X
 = (sqrt(epsilon) X_1+epsilon^(-1/2)X_2)^2
 =: L_epsilon^2`.                                                     (6.1)

The density of `L_epsilon` is strictly positive on a neighborhood of zero (indeed it has a central plateau when `epsilon<1`). Hence

`E |X^T S_epsilon X|^(-1/2)
 = E |L_epsilon|^(-1)
 = infinity`.                                                         (6.2)

Thus no finite bound for the half-Riesz potential can depend only on the cross-row norm and an upper bound `|S_ii|<=delta`, even as `delta->0`. This is a counterexample to that **intermediate extension**, not to the three-large-eigenvalue QFORM conjecture: `S_epsilon` has rank one.

Consequently the exact zero-Schur endpoint and the genuinely near-zero branch require different mechanisms. The latter must retain an additional independent/grouped smoother or a discriminant small-ball estimate; continuity in the pivot coefficient cannot be assumed at the level of the half-Riesz norm.

## 7. What changed and what remains

**New proved supporting claims**

- `QFORM-ZERO-DIAGONAL-AFFINE-HALF-RIESZ-v1`, arbitrary rank and arbitrary affine perturbation, constant `4 sqrt(2)e^(1/4)`.
- `QFORM-OUTER-PIVOT-ZERO-SCHUR-v1`, an arbitrary-rank density closure branch.
- `QFORM-RANK3-ZERO-MINOR-ENDPOINT-v1`, with the exact identity `beta_i^2=|det Lambda| Delta_ki/|a|`.

**New refuted interface**

- `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`: exact zero cannot be replaced by merely small diagonal while retaining only the cross-row norm.

**First unpaid implication**

`QFORM-HIGH-ROW-NEAR-ISOTROPIC-DISCRIMINANT-v1`: in the high-leverage/product-provenance branch, treat a genuinely small but nonzero physical pivot by keeping the discriminant/remainder coupling before the half-Riesz singularity is taken. A viable proof must use a second independent/grouped smoothing resource or a translation-uniform small-ball estimate for the completed-square remainder; the rank-one counterexample above rules out a continuity argument from the exact-zero lemma alone.

Arbitrary additional spectral components outside the exact-rank-three/supporting branches remain a separate full-target debt. No full theorem and no full continuity conclusion are claimed.

## 8. Verification note

The exact identity (5.7) was also checked numerically on the `n=4` Hadamard frame with `Lambda=diag(1,1,-1)`: for every tested determinant-zero pair, `Delta_ki=1/2`, `a=1/4`, and both sides of (5.7) equal `2`. This is only a consistency check; the proof above is analytic.

Privacy/provenance review: this report contains only authorized mathematics, source pins, run labels and nonsecret constants; no credentials, scheduler identifiers, machine paths, signed URLs, unrelated private data, public release, paid compute, or permission change.
