# account01/B06 — isotropic triple determinant bank and transverse-heavy dichotomy

**Run:** `20260922T140612Z-qform-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Outcome:** `ESSENTIAL_STEP_APPLIED / RANK3_DOUBLE_HEAVY_BRANCH_CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/use occurred, but native learned-memory ingestion was not verified.

## 0. Exact target and correction discipline

The full target is unchanged: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal finite constant, or give a valid counterexample. The additional requested continuous-density conclusion is tracked separately.

Fresh control before publication remained `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`; no later stop was present. This report respects all live corrections, in particular: no law-uniform pointwise one-dimensional Fresnel decay; no unrestricted spectral-fiber supremum; no independence after spectral rotation; no generic conditional-cap substitute for independence; no X-ray-only two-sheet closure; no uniformly good local principal-block/cross-rank dichotomy; and no fiberwise indefinite trace-mass closure.

### Source-pinned dependencies actually used

1. **Named partner account02/B06**: `QFORM-SAMESIGN-DETERMINANT-MASS-v1`, canonical report
   `yspennstate/math-open-problems@6902eb62f21a7c833ca27dcca69f34d50e711a7d:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`.
   It proves the Pluecker determinant-mass identity for a two-frame and records the rank-three Cauchy--Binet analogue.

2. **account01/B10**: `QFORM-ZERO-DIAGONAL-TRIPLE-v1`, canonical report
   `yspennstate/math-open-problems@3be6045911d80a0881d7a1c3631871643f52434c:proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260922T131954Z-account01-B10-QFORM-r12/REPORT.md`.
   If a physical principal `3x3` block `B=A[S,S]` is invertible and has one zero diagonal entry, then, with arbitrary outside couplings,
   `||p_Q||_infinity <= 3*2^(2/3)|det B|^(-1/3)`.

3. **Previous account01/B06 weighted projection theorem**:
   `yspennstate/math-open-problems@0b523077616e4d1a2c959ddca036cfd895067460:proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260922T130334Z-qform-r11/REPORT.md`.
   Its sharp Hausdorff--Young input is used in Section 4 below.

4. For frontier comparison only, not as a premise of the new determinant calculation: **account03/B06** `QFORM-HEAVY-ISOTROPIC-TRANSVERSE-WIENER-v1`,
   `yspennstate/math-open-problems@aa64434a2d628bd7848f154dbc872008338911a2:proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T132210Z-account03-B06-qform-curved-r12/REPORT.md`.

## 1. Compact conditional end-to-end argument and first missing implication

The present calculation concerns the exact rank-three heavy-isotropic state, a live hard branch of the team proof. Write

`A=U Lambda U^T`, `U^T U=I_3`,

with all three eigenvalues of the real symmetric invertible `Lambda` satisfying `|lambda|>=1`, hence

`|det Lambda|>=1`.

Assume there is a physical row `u_i` which is leverage-heavy and isotropic for the quadratic form:

`u_i=sqrt(c)e`,  `c>1/2`,  `e^T Lambda e=0`.

For `j!=i`, decompose

`u_j=s_j e+w_j`,   `w_j in e^perp ~= R^2`.

Account03/B06 already handles the branch in which every transverse leverage `d_j=||w_j||^2` is at most `1/2`, obtaining useful `3/4` characteristic-function decay and a half-Riesz bank but not yet a full `L^infinity` bound. Thus a first unresolved branch is that some `d_j>1/2`.

The new calculation below splits that transverse-heavy branch sharply:

- if a second heavy direction appears inside the one-dimensional perpendicular complement of `w_j`, then a single physical triple has determinant `>1/8`, and the account01/B10 zero-diagonal theorem gives a universal density bound immediately;
- otherwise the entire perpendicular determinant bank is diffuse and admits a dimension-free **modulation-stable one-dimensional Wiener/Fresnel payment**. The only remaining debt is to splice that paid one-dimensional bank into the full heavy-isotropic formula without discarding the leakage/product provenance.

This is a target-relevant structural reduction, not a proof of the full conjecture.

## 2. Exact isotropic triple determinant bank

### Theorem 2.1 — `QFORM-ISOTROPIC-TRIPLE-DETERMINANT-BANK-v1`

Under the rank-three heavy-isotropic setup above, for every residual pair `j<k`, define

`D_jk = |det A[{i,j,k},{i,j,k}]|`.

Then

`D_jk = c |det Lambda| det(w_j,w_k)^2`,                              (2.1)

and the complete determinant bank satisfies

`sum_{j<k, j,k != i} D_jk = c |det Lambda|`,                         (2.2)

while each residual-row marginal is

`sum_{k != i,j} D_jk = c |det Lambda| ||w_j||^2`.                    (2.3)

#### Proof

Because `U^T U=I_3` and `u_i=sqrt(c)e`, deleting row `i` gives

`sum_{j!=i} u_j u_j^T = I_3-c ee^T`.

Projecting to `e^perp` yields the Parseval identity

`sum_{j!=i} w_j w_j^T = I_2`.                                       (2.4)

For a physical triple `S={i,j,k}`, rank three gives the exact Cauchy--Binet factorization

`det A_S = det(U_S Lambda U_S^T) = det Lambda * det(U_S)^2`.         (2.5)

Using the row decomposition and expanding the determinant along the first row,

`det(U_{i j k}) = sqrt(c) det(w_j,w_k)`.                              (2.6)

Taking absolute values in (2.5) proves (2.1).

Now apply the partner account02/B06 determinant-mass/Cauchy--Binet identity to the two-dimensional Parseval frame `(w_j)`: from (2.4),

`sum_{j<k} det(w_j,w_k)^2 = det(I_2)=1`.                              (2.7)

Multiplying by `c|det Lambda|` proves (2.2).

For the marginal, the same Pluecker calculation used in the previous account01/B06 report gives

`sum_{k!=j} det(w_j,w_k)^2 = ||w_j||^2`;                             (2.8)

indeed, if `w_j=(a,b)` and `sum_k w_k w_k^T=I_2`, expanding
`sum_k (a w_{k,2}-b w_{k,1})^2` gives `a^2+b^2`. Multiplying by `c|det Lambda|` proves (2.3). QED.

### Interpretation

The isotropic physical pivot does not merely belong to some nonsingular triple. It carries an exact **probability bank** of triple determinant mass: after normalization by `c|det Lambda|`, the triple weights sum to one, and the incidence mass at residual row `j` is exactly its transverse leverage `d_j`.

This is the rank-three physical-triple lift of the named partner's determinant-mass theorem.

## 3. A universal closure when the determinant bank is heavy twice

Assume now that some residual row `j` is transverse-heavy:

`d_j=||w_j||^2>1/2`.

Rotate only the abstract transverse basis `e^perp` (this is a change of coordinates in the spectral bookkeeping, not a rotation of the independent physical variables) so that

`w_j=sqrt(d_j) f`.

For every other residual row write

`w_k=y_k f+z_k g`.

Taking the `g,g` entry of (2.4) gives

`sum_{k != i,j} z_k^2=1`.                                            (3.1)

Moreover

`det(w_j,w_k)^2=d_j z_k^2`,                                          (3.2)

so (2.1) becomes

`D_jk=c|det Lambda| d_j z_k^2`.                                      (3.3)

### Theorem 3.1 — `QFORM-TRANSVERSE-DOUBLE-HEAVY-CLOSE-v1`

If there exists `k` with

`z_k^2>1/2`,                                                          (3.4)

then the full quadratic form `Q=X^TAX` has an essentially bounded density with the universal estimate

`||p_Q||_infinity < 6*2^(2/3)`.                                      (3.5)

No restriction is imposed on the other coordinates or outside couplings. Continuity is not asserted by this theorem.

#### Proof

By (3.3), the owner normalization and `c,d_j,z_k^2>1/2` give

`D_jk = c|det Lambda|d_j z_k^2 > 1/8`.                               (3.6)

Since `A_ii=e^T Lambda e * c =0`, the physical principal triple

`S={i,j,k}`

has one zero diagonal entry. Equation (3.6) makes it invertible. Apply the source-pinned account01/B10 theorem:

`||p_Q||_infinity <=3*2^(2/3)D_jk^(-1/3)
                  <3*2^(2/3)*(8)^(1/3)
                  =6*2^(2/3)`.                                       (3.7)

The B10 theorem already permits arbitrary coupling from this triple to all remaining physical coordinates, so nothing else needs to be conditioned away. QED.

### Consequence for the heavy-isotropic frontier

The account03/B06 residual condition `d_j>1/2` is no longer one undifferentiated hard branch. If the normalized determinant incidence bank at that row has an atom larger than `1/2`, the rank-three target is closed with a universal constant by Theorem 3.1.

## 4. Diffuse perpendicular bank: uniform modulated Wiener payment

The complementary case to (3.4) is

`z_k^2<=1/2` for every `k`, while `sum_k z_k^2=1`.                    (4.1)

This admits an exact product-structure payment before any curved trace is taken.

### Lemma 4.1 — `QFORM-MODULATED-1D-WIENER-BANK-v1`

Let `X_k` be independent with densities `f_k<=1`. Let real coefficients `z_k` satisfy

`sum_k z_k^2=1`,  `z_k^2<=1/2`,                                     (4.2)

and let `a_k` be arbitrary real modulation shifts. Then

`W(eta)=prod_k hat f_k(a_k+z_k eta)`

satisfies

`int_R |W(eta)| d eta <=2 pi sqrt(e)`.                               (4.3)

Equivalently, the complex pushforward measure

`nu(A)=E[ exp(i sum_k a_k X_k) 1_{sum_k z_kX_k in A} ]`

has a bounded continuous density `h` with

`||hat h||_1<=2pi sqrt(e)`, `||h||_infinity<=sqrt(e)`.                (4.4)

For every `tau!=0`, `t!=0`, and real `beta`, its quadratic trace obeys

`|int h(z) exp(i t tau z^2+i beta z) dz|
 <=sqrt(pi e) |tau t|^(-1/2)`.                                       (4.5)

#### Proof

Put `q_k=1/z_k^2` and omit zero coefficients. By (4.2), `q_k>=2`. The sharp Hausdorff--Young estimate proved in the previous account01/B06 report states, with `d=z_k^2`,

`int |hat f_k(theta)|^(1/d) dtheta
 <=2pi sqrt(d) (1-d)^(-(1-d)/(2d)).`                                 (4.6)

Translation of Fourier frequency does not change this integral. Apply Holder in `eta` with exponents `q_k`; these are admissible because

`sum_k 1/q_k=sum_k z_k^2=1`.

After the change of variables `theta=a_k+z_k eta`, the factor `|z_k|^(-1)` cancels the `sqrt(d)=|z_k|` in (4.6). Therefore

`int |W(eta)|deta
 <=2pi prod_k (1-z_k^2)^(-(1-z_k^2)/2).`                              (4.7)

Using `-(1-d)log(1-d)<=d` and `sum d=1`,

`prod_k (1-z_k^2)^(-(1-z_k^2)/2) <=e^(1/2)`,                         (4.8)

which proves (4.3). Fourier inversion gives (4.4).

For (4.5), use the Fourier transform of the chirp:

`| Fourier_z[ exp(i t tau z^2+i beta z) ](eta) |
 =sqrt(pi/|t tau|)`.

Parseval/Fourier inversion in one dimension and (4.4) give

`|int h(z)e^{it tau z^2+i beta z}dz|
 <=(2pi)^(-1)||hat h||_1 sqrt(pi/|t tau|)
 <=sqrt(pi e)|t tau|^(-1/2)`. QED.

### Why this survives the live corrections

This is not the refuted statement that every one-dimensional density bounded by one has pointwise Fresnel decay. The input to (4.5) is a **specific complex pushforward of the original product law**, and (4.3) is obtained before taking the curved trace by a dimension-free product Holder/Hausdorff--Young aggregation. The arbitrary shifts `a_k` make the estimate stable under coordinatewise linear modulation.

Nor does it select one large physical minor: in the complementary branch every atom `z_k^2` is at most `1/2`, and the entire determinant incidence bank is paid simultaneously.

## 5. Exact remaining implication

Combining Sections 3 and 4 produces the following rigorous dichotomy for a transverse-heavy row in the heavy-isotropic rank-three state.

Let `j` satisfy `d_j>1/2`, and normalize its incident determinant bank by (3.3). Then either

1. **double-heavy atom:** some `z_k^2>1/2`; the full rank-three quadratic is already universally bounded by Theorem 3.1; or
2. **perpendicular diffuse bank:** all `z_k^2<=1/2`; the remaining one-dimensional determinant bank has the uniform modulated Wiener/Fresnel payment (4.3)--(4.5).

Thus the next exact unpaid implication is narrower than the previous generic transverse-heavy problem:

### `QFORM-TRANSVERSE-HEAVY-DIFFUSE-BANK-SPLICE-v1` — OPEN

Starting from the full heavy-isotropic identity

`Q=2B(sqrt(c)X_i+T)Y+rY^2+2sYZ+tau Z^2`

(or an equivalent basis after aligning the heavy transverse row), insert the product-origin estimate (4.5) **before or jointly with** the remaining leakage integration, and obtain one further integrable payment without replacing the leakage by a conditional-density cap or assuming independence after rotation.

The difficulty is precise: after aligning the transverse-heavy row, the leakage and transverse coordinates may be carried by the same original residual variables. Lemma 4.1 tolerates arbitrary fixed coordinatewise Fourier shifts, but this run does not prove that the full moving modulation generated by the remaining bilinear terms can always be represented by such fixed shifts at the point where the final curved integral is taken. That interface must be derived, not assumed.

A successful splice yielding an `L^1` characteristic-function majorant or a direct `O(epsilon)` small-ball estimate would close this residual rank-three branch. The full arbitrary-matrix target would still require the team's reduction from general matrices/additional eigendirections to these paid rank-three/full-spectrum branches.

## 6. Status and regularity

**PROVED in this run:**

- `QFORM-ISOTROPIC-TRIPLE-DETERMINANT-BANK-v1`, exact total and marginal determinant identities (2.1)--(2.3), explicitly applying the named account02/B06 determinant-mass theorem;
- `QFORM-TRANSVERSE-DOUBLE-HEAVY-CLOSE-v1`, universal essential-density bound `<6*2^(2/3)` in the double-heavy rank-three branch;
- `QFORM-MODULATED-1D-WIENER-BANK-v1`, the dimension-free modulation-stable product Wiener/Fresnel estimate in the complementary perpendicular-diffuse determinant bank.

**NOT PROVED:**

- the splice in Section 5;
- the full rank-three theorem in all heavy-isotropic cases;
- the full arbitrary symmetric-matrix three-large-eigenvalue conjecture;
- a continuous representative for the new double-heavy branch (the source theorem invoked there guarantees an essentially bounded density; this report does not add continuity).

No numerical experiment is used as proof, and no source-matching literature theorem is claimed.
