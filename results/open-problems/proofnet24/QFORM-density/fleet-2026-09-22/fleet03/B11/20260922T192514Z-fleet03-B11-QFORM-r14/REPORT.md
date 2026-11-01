# fleet03/B11 — correction-safe localized 3-block theorem for indefinite QFORM

**Run:** `20260922T192514Z-fleet03-B11-QFORM-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner-control revision:** `2026-09-22.14`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Why this run changes mechanism

The preceding B11 run attacked a heavy *null* physical pivot through a hyperbolic-square smoothing lemma and required support separation between the leakage form and the transverse pair. The live correction state now makes the broader issue sharper: an arbitrary bounded three-dimensional joint density does **not** satisfy the formerly proposed rank-three coarea bound, and bounded transverse/conditional density caps do **not** control the parabolic null-graph trace. Therefore this run changes mechanism. It works entirely in a fixed set of three **original independent coordinates**, conditions on all other original coordinates, and pays the resulting quadratic-plus-affine form by a diagonal/off-diagonal pivot dichotomy using already proved product-source estimates.

The full conjecture remains open. This note proves a corrected localized branch that does not invoke the refuted arbitrary-joint coarea lemma.

## 2. Inputs used

We use two completed supporting theorems with their exact scopes.

### Input A: nonzero scalar pivot / rank-two affine half-Riesz consequence

From

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`,

if an original-coordinate principal block has exact rank three and representation `V M V^T`, `V^T V=I_3`, and physical row `i` has leverage `c_i` and nonzero scalar pivot `a`, then the full ambient quadratic form, including arbitrary induced affine terms, obeys

`||p_Q||_infinity <= 128 [c_i |a| |det M|]^(-1/4)`.          (2.1)

For a three-coordinate block itself, `V=I_3` and `c_i=1`.

### Input B: full-matrix indefinite-pair theorem

From the proof-first full-matrix pair extension

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`,

if a symmetric matrix `C` satisfies `s_3(C)>=s>0` and contains an invertible indefinite original-coordinate `2 x 2` principal pair `B`, with

`D=|det B|`, `kappa=sigma_min(B)`,

then for independent cap-one coordinates and arbitrary affine terms,

`||p_Q||_infinity <= 3*400^(1/3) (D^2 kappa s)^(-1/6)`.       (2.2)

This theorem allows arbitrary matrix rank; here we apply it to a conditioned three-variable form.

### Assigned-partner input actually applied

The newest completed `fleet04/B11` result is

`yspennstate/math-open-problems@797dcde430e982a020d7642b54cadc281cbc9bc1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260922T191727Z-fleet04-B11-nullgraph-obstruction-r2/REPORT.md`.

For `T=2ZW+V^2` with joint density `h`, it proves the exact identity

`p_T(t) = (1/2) integral_{w!=0} h((t-v^2)/(2w),v,w) dv dw/|w|`,  (2.3)

and shows by a source-valid construction that a bounded `(V,W)` density plus a uniformly bounded conditional density of `Z|(V,W)` does not control this trace. We apply (2.3) quantitatively in Section 5.

## 3. New theorem: every uniformly nonsingular physical 3-block is paid without arbitrary-joint coarea

### Theorem 3.1 — `QFORM-LOCALIZED-3BLOCK-REPAIR-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one, and let `A` be real symmetric. Suppose there is a set `I` of three **original coordinate indices** such that the principal matrix

`C=A_{I,I}`

has all three eigenvalues of absolute value at least `s>0`, equivalently `sigma_min(C)>=s`. Then `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity <= (128*2^(1/4))/s < 153/s`.                (3.1)

The result holds for every signature of `C`, including `(+,+,-)` and `(+,-,-)`, for arbitrary outside matrix coefficients and cross couplings, and for arbitrary cap-one input laws. No moment, support, smoothness, Gaussian, log-concavity, or post-rotation independence assumption is made.

### Proof

Condition on every original coordinate outside `I`. Since the original coordinates are independent, the three remaining coordinates stay independent with their original cap-one densities. The conditional random variable is

`R(x)=x^T C x + ell^T x + gamma`,                              (3.2)

where `ell` and `gamma` depend on the conditioned coordinates. We prove a bound uniform in `ell,gamma`.

Because `C` is symmetric and `sigma_min(C)>=s`,

`|det C| >= s^3`.                                              (3.3)

We split into two exhaustive cases.

#### Case A: a large scalar pivot

Assume some diagonal entry satisfies

`|c_ii| >= s/2`.                                               (3.4)

Apply (2.1) to the exact three-coordinate block, for which `c_i=1`, `a=c_ii`, `M=C`. The arbitrary affine term `ell^T x` is within the theorem's stated scope. Using (3.3) and (3.4),

`||p_R||_infinity`
` <= 128 (|c_ii| |det C|)^(-1/4)`
` <= 128 ((s/2)s^3)^(-1/4)`
` = 128*2^(1/4)/s`                                             (3.5)

` = 152.2185107203.../s`.

#### Case B: every scalar pivot is small

Assume instead

`|c_11|,|c_22|,|c_33| < s/2`.                                 (3.6)

For each coordinate vector `e_i`, the least-singular-value assumption gives

`||C e_i||_2^2 >= s^2`.

Hence for every row/column `i`,

`sum_{j!=i} c_ij^2`
` = ||C e_i||_2^2-c_ii^2`
` > s^2-s^2/4`
` = 3s^2/4`.                                                   (3.7)

There are two off-diagonal terms in this sum, so for at least one `j!=i`,

`a:=|c_ij| >= sqrt(3/8) s = (sqrt(6)/4)s`.                    (3.8)

Consider the physical pair

`B=[[q,a0],[a0,d]]`,                                           (3.9)

where `a0=c_ij`, `q=c_ii`, `d=c_jj`. By (3.6), `|q|,|d|<s/2`. Its determinant is negative, because

`a^2-|qd| > (3/8)s^2-(1/4)s^2 = s^2/8`,                      (3.10)

so `B` is invertible and indefinite. Moreover

`D:=|det B| = a^2-qd >= a^2-|qd| > s^2/8`.                   (3.11)

To lower-bound its least singular value, write

`B=[[0,a0],[a0,0]] + diag(q,d)`.

The first matrix has both singular values equal to `a`. Weyl's perturbation inequality therefore gives

`kappa:=sigma_min(B)`
` >= a-max(|q|,|d|)`
` > (sqrt(6)/4-1/2)s`
` = ((sqrt(6)-2)/4)s`.                                        (3.12)

Now apply (2.2) to the conditional three-variable form (3.2), whose third singular value is at least `s`. Equations (3.11)-(3.12) give

`||p_R||_infinity`
` <= 3*400^(1/3) (D^2 kappa s)^(-1/6)`
` <= [3*400^(1/3)*(256/(sqrt(6)-2))^(1/6)]/s`                (3.13)

` = 63.6396743166.../s`.

Thus the worse of the two cases is (3.5), proving the uniform conditional estimate (3.1).

Finally, avoid any measurable-density-selection issue by integrating interval probabilities. For every interval `J`, almost every outside conditioning value satisfies

`P(R in J | X_{I^c}) <= (128*2^(1/4)/s)|J|`.

Averaging gives the same inequality for `Q`. Hence the law of `Q` is dominated by `(128*2^(1/4)/s)` times Lebesgue measure, so it has a density with the claimed essential-supremum bound. QED.

## 4. Why this repairs, rather than repeats, the invalid localized proof

An earlier owner brief suggested conditioning outside a physical triple and then invoking an arbitrary-joint rank-three coarea lemma. The live correction gives an explicit cone-tube density showing that such an arbitrary-joint lemma is false. Theorem 3.1 never forms an arbitrary projected three-dimensional joint density. After conditioning outside the block, the remaining variables are still the **three original independent coordinates**. If a scalar pivot is substantial, Input A pays it through a translated rank-two half-Riesz estimate; if all scalar pivots are small, spectral nonsingularity forces a quantitatively large off-diagonal coefficient, and Input B pays the resulting physical indefinite pair. The product source is retained at every step.

This is also why the argument genuinely treats indefinite signatures rather than diagonalizing `C`: diagonalization would destroy independence. All spectral information is used only through invariant inequalities such as `sigma_min(C)>=s` and `|det C|>=s^3`; the analytic estimates themselves remain in original coordinates.

## 5. Explicit application of the completed fleet04/B11 null-graph identity

Take the canonical indefinite form

`T=2ZW+V^2`,                                                   (5.1)

with `Z,V,W` independent and each density bounded by one. Its matrix

`H0=[[0,0,1],[0,1,0],[1,0,0]]`

has spectrum `{1,1,-1}`, so Theorem 3.1 applies with `s=1`. In fact Case A uses the unit `V^2` pivot and gives the sharper displayed branch value

`||p_T||_infinity <=128`.                                     (5.2)

The completed `fleet04/B11` identity (2.3) therefore yields the actual trace inequality

`sup_t integral_{w!=0} h((t-v^2)/(2w),v,w) dv dw/|w|`
` = 2||p_T||_infinity`
` <=256`,                                                       (5.3)

for the product density `h(z,v,w)=f_Z(z)f_V(v)f_W(w)`.

The partner's obstruction theorem shows simultaneously that (5.3) cannot be deduced from the two weaker assertions `||p_(V,W)||_infinity<=1` and `sup_(v,w)||p_(Z|V,W)||_infinity<=1`: it constructs a non-product joint law satisfying both caps for which the left side diverges. Thus (5.3) is not merely another coarea estimate; it records exactly where original-coordinate product provenance enters.

## 6. The rank-two logarithmic control remains mandatory

For independent `X,Y ~ Uniform[-1/2,1/2]`, the opposite-sign rank-two saddle `2XY` has

`p_{2XY}(t)=log(1/(2|t|))`, for `0<|t|<1/2`,                  (6.1)

so its density diverges logarithmically at zero. Theorem 3.1 shows one rigorous way the third direction prevents this singularity in a localized rank-three block: either it supplies a quantitatively nonzero scalar pivot which can be averaged through the rank-two half-Riesz potential, or the absence of such a pivot forces a uniformly nondegenerate physical hyperbolic pair, whose logarithmic envelope can be averaged against the third singular direction by the full-matrix pair theorem. This is a product-preserving replacement for the false statement that mere boundedness of a three-dimensional joint density removes the cone singularity.

## 7. Scope and remaining first implication

The theorem proves the entire **uniformly localized physical 3-block branch** with explicit constant `<153/s`. It does **not** show that the bare hypothesis “three eigenvalues of `A` have modulus at least one” produces a physical triple with `sigma_min(C)>=s` for universal `s`; known singleton-plus-two-bank and diffuse examples rule out such a fixed-minor reduction. Therefore the full QFORM conjecture remains **OPEN / NOT PROVED**.

The next B11 implication is now structural and exact:

**QFORM-INDEFINITE-AGGREGATE-BEFORE-INVERSION-v1.** Starting from three large spectral directions but no uniformly nonsingular physical triple, aggregate original-coordinate diagonal/off-diagonal packets before paying reciprocal determinants, and prove that either (i) a grouped physical block enters Theorem 3.1 with universal scale, or (ii) a diffuse/ridge or many-small-pair mechanism pays the same mass without selecting a single bad minor. The fleet04/B11 null-graph obstruction requires the aggregation to preserve genuine product provenance; marginal or conditional density caps alone are insufficient.

Arbitrary additional spectrum is allowed in Theorem 3.1 because conditioning only converts it into outside-dependent affine terms on the selected three coordinates; but **existence of the selected well-conditioned triple** is not automatic and is the unpaid global reduction.

## 8. Regularity

This report proves existence of an **essentially bounded density** in the stated branch. It does not establish a continuous representative. Continuity for the full target remains separate and open.

## 9. Exact numerical checks

The two branch constants are

`C_diag = 128*2^(1/4) = 152.2185107203483...`,

`C_pair = 3*400^(1/3)*(256/(sqrt(6)-2))^(1/6) = 63.6396743166345...`.

Hence `C_local=C_diag<153`. The algebraic thresholds used in Case B are exact:

`sqrt(3/8)=sqrt(6)/4`,

`3/8-1/4=1/8`,

`sqrt(6)/4-1/2=(sqrt(6)-2)/4>0`.

No numerical experiment is used as proof.
