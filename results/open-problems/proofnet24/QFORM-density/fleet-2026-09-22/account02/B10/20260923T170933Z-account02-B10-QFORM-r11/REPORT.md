SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T17:09:33.027127Z.
attacking: QFORM-TWOSHEET-NEARNULL-NEARCOLOOP-JOINT-SMOOTHING-v1; test whether the newest one-original-hub projected-crossing compiler can itself bridge the true near-coloop collar, while retaining original-coordinate product provenance.

# account02/B10 r11 — a sharp near-coloop barrier for leaf-only one-hub crossing, and a uniformly safe true-collar family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: rank-three coupled case; complementary constructions/source-valid counterexamples  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_STRUCTURAL_OBSTRUCTION / TARGET-VALID SAFE FAMILY / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains OPEN: arbitrary independent original-coordinate laws with densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and no moments, support bounds, log-concavity, diagonal-basis reduction, or post-rotation independence. Essential boundedness is the target; continuity is separate.

## 1. Fresh source boundary and first unpaid implication


`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its ruled one-sheet theorem is used at an actual inequality in Section 4 below. The current continuation `c4c23b784395630c094ba299a50712209921d1ae` and the newer projected-crossing record `829192412f2a2d84e72b4bed91115fc5fab68401` were also read. They do not claim the full theorem.

The latest completed designated partner result used here is account03/B10 r24,

`QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1`,

at `yspennstate/math-open-problems@97a77b266879a93eb43ad36555ffdec1d981ebe0`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T114517Z-account03-B10-QFORM-r24/REPORT.md`.

It proves for an exact-null ORIGINAL hub `u_0=sqrt(h)r`, with every complementary transverse leverage at most `1/2`,

`||p_Q||_infinity <= 3*2^(4/3) (h |det M|)^(-1/3)`,                 (1.1)

and a continuous `C_0` density, while preserving the original product amplitude under the null shear. The later account03/B10 r25 checkpoint contains a useful nonzero-near-null square-root small-ball estimate but is not promoted here to a completed partner theorem.

The newest completed analytic compiler relevant to the prior B10 gap is account01/B03

`QFORM-ONE-HUB-ROW-MARGINAL-FREE-2VOLUME-v1`,

at `yspennstate/math-open-problems@97a77b266879a93eb43ad36555ffdec1d981ebe0`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T165124Z-account01-B03-QFORM-r29/REPORT.md`.

For a physical hub `h`, leaf split `I disjoint J`, and

`V_3 = ||A_{h,J}||^2 sum_{i<k in I}|A_{i,J}(I-P_{A_{h,J}}) wedge A_{k,J}(I-P_{A_{h,J}})|^2`,

it gives

`||p_Q||_infinity <= C_* V_3^(-1/6)`,
`C_*=3*2^(7/6) exp(1/3)<9.400`,                                  (1.2)

with no volume-row-marginal hypothesis.

The first unpaid implication at the start of this run was therefore precise: can a better original leaf partition keep `V_3` uniformly positive in the true near-coloop collar, or must the proof change topology and group another source with the hub?

The answer is the latter. The barrier is exact and independent of the near-null scalar pivot.

## 2. New theorem — the leaf-only one-hub currency necessarily loses the coloop defect

Write an exact-rank-three form as

`A=R M R^T`, `R^T R=I_3`, `D=|det M|>0`.

Let one ORIGINAL physical spectral row be

`u_0=sqrt(h) r`, `||r||=1`, `0<h<1`,

and put `rho=1-h`. For every leaf row write

`u_j=t_j r+p_j`, `p_j perpendicular r`.

Parseval gives for the entire leaf bank

`sum_j u_j u_j^T = I_3-h rr^T`,                                  (2.1)

so in the splitting `Rr direct_sum r^perp` its Gram eigenvalues are exactly `(rho,1,1)`.

For disjoint leaf banks `I,J` define

`S_I=sum_{i in I} p_i p_i^T`,
`G_J=sum_{j in J} u_j u_j^T`.

The exact B10 factorization already proved for the account01/B03 packet is

`V_3(h;I,J)=h D^2 det(S_I) det(G_J)`.                             (2.2)

### Theorem 2.1 — `QFORM-NEARCOLOOP-ONEHUB-CURRENCY-BARRIER-v1`

For every such exact-rank-three frame and every disjoint leaf split `I,J`,

`boxed: V_3(h;I,J) <= h D^2 (1-h) = h D^2 rho.`                  (2.3)

Consequently, when `D` stays bounded and `h -> 1`, no choice of leaf-only physical partition can make the one-original-hub projected-crossing currency uniformly positive.

#### Proof

Because `S_I` is a transverse sub-Gram of the full leaf frame,

`0 <= S_I <= I_2`.

Hence both eigenvalues of `S_I` are at most one and

`det S_I<=1`.                                                     (2.4)

Likewise

`0 <= G_J <= I_3-h rr^T`.                                       (2.5)

For positive semidefinite matrices, Loewner order implies coordinatewise ordered eigenvalues by the min-max principle, hence determinant monotonicity. The right side of (2.5) has eigenvalues `(rho,1,1)`, so

`det G_J <= rho`.                                                 (2.6)

Insert (2.4)-(2.6) into (2.2). QED.

This is not a failure of the account01/B03 theorem. It identifies a structural limit of that theorem's **one original hub plus leaf-only full-rank column bank** topology. In particular, recursively removing its row-marginal gate does not remove the near-coloop determinant loss: the loss is already present in the full leaf Gram before any marginal estimate.

## 3. A target-valid true-collar family where the barrier is sharp but QFORM is uniformly safe

The preceding upper bound could still be irrelevant if every family saturating it were itself dangerous. The following exact target family shows the opposite: every leaf-only one-hub packet vanishes like `rho`, while a product-preserving collinear-bank compression gives a uniform all-level density bound.

Fix an even integer `m>=128`. Work in an orthonormal spectral basis `(e,v,u)`. Put

`eps=1/m`, `s=sqrt(1-eps^2)`,

`Lambda_m=[[-eps,0,s],[0,1,0],[s,0,eps]]`.                       (3.1)

Then `Lambda_m^2=I_3`, hence

`spec(Lambda_m)={-1,1,1}`, `D=1`.                                (3.2)

Set

`rho=1/m`, `c=1-rho`,
`rho_M=1/(2m)`,
`eta=1-1/(4m)`.                                                   (3.3)

Use the physical hub

`r_0=sqrt(c)e`.                                                    (3.4)

Take `m` genuinely mixed rows, half with sign `+` and half with sign `-`,

`r_j^M = (1/(sqrt(2)m)) e + sigma_j sqrt(eta/m) v`,
`sum_j sigma_j=0`.                                                (3.5)

Add three disjoint pure banks, each with `m` rows,

`r_j^L = (1/(sqrt(2)m))e`,
`r_j^V = (1/(2m))v`,
`r_j^U = (1/sqrt(m))u`.                                          (3.6)

The mixed cross Gram vanishes because `sum sigma_j=0`. The total masses are

`e: c + 1/(2m) + 1/(2m) = 1`,
`v: eta + 1/(4m) = 1`,
`u: 1`.                                                           (3.7)

Therefore `R_m^T R_m=I_3`, and

`A_m=R_m Lambda_m R_m^T`                                         (3.8)

is an exact target matrix with nonzero spectrum exactly `{-1,1,1}`.

### 3.1 It is in the genuine sharpened near-coloop survivor

The hub leverage and Rayleigh coefficient are

`c>63/64`, `rho<1/64`,
`alpha=e^T Lambda_m e=-1/m`.                                     (3.9)

The mixed bank has

`rho_M=1/(2m)`,
`H_M=eta vv^T`.                                                   (3.10)

The completed account03/B10 near-coloop excision gate would require

`(1-rho_M)|alpha| <= (1/2) min(1-rho_M,1-eta)`.

Here `1-eta=1/(4m)` while

`(1-rho_M)|alpha|=(1-1/(2m))/m > 1/(8m)=(1-eta)/2`.             (3.11)

Thus the gate genuinely fails. Also every complementary transverse row is light: the mixed transverse leverage is `eta/m<1/128`, the pure-u leverage is `1/m`, and the others are smaller.

The physical local certificates collapse as well. Since `Lambda_m` is orthogonal, `|x^T Lambda_m x|<=||x||^2`; every nonhub row has squared norm at most `(eta+1/(2m))/m<2/m`. Therefore scalar pivots are `O(m^-1)`, hub-leaf principal-pair determinants are `O(m^-1)`, leaf-leaf pair determinants are `O(m^-2)`, and every principal triple is `O(m^-2)` by Hadamard. No fixed physical local certificate explains the bound below.

### 3.2 Every leaf-only one-hub projected-crossing packet vanishes

The full leaf Gram is exactly

`G_leaf=diag(rho,1,1)`                                            (3.12)

in `(e,v,u)`. Therefore Theorem 2.1 gives, for **every** disjoint leaf split `I,J`,

`boxed: V_3(0;I,J) <= c rho < 1/m.`                              (3.13)

So the newest row-marginal-free one-hub compiler cannot yield a uniform constant on this family from any leaf partition.

The loss has the correct order, not merely an upper-bound artifact. For example put in `I` all positive mixed rows and half of the pure-u rows; put in `J` all pure-longitudinal rows, all negative mixed rows, and the other half of the pure-u rows (adding the pure-v rows to `J` only helps). Then

`det S_I = (eta/2)(1/2)=eta/4`.                                  (3.14)

In `J`, the pure-longitudinal bank contributes `(rho/2)ee^T`; the negative mixed bank contributes one rank-one vector with aggregate squared `e` component `rho/4` and `v` component `eta/2`; the retained pure-u half contributes `(1/2)uu^T`. Dropping the positive pure-v contribution, the `(e,v)` determinant is already `(rho/2)(eta/2)=rho eta/4`, hence

`det G_J >= rho eta/8`.                                          (3.15)

Thus for this explicit split

`V_3 >= c rho eta^2/32`.                                         (3.16)

Equations (3.13) and (3.16) show that the best one-hub packet is genuinely `Theta(rho)`. Its direct compiler therefore has an intrinsic `rho^(-1/6)` scale on this family even though the actual target remains uniformly bounded by the next paragraph.

### 3.3 Uniform all-level payment by a different product topology

The positive-sign half of the mixed rows is an EXACT collinear ORIGINAL-coordinate bank. Compress that bank to its scalar normalized product projection; likewise compress the pure-u bank. Keep the physical hub scalar itself. These are three mutually independent functions of disjoint original-coordinate banks, each with density at most `sqrt(2)`.

Their aggregate spectral rows are

`tilde r_0=sqrt(c)e`,
`tilde r_+=sqrt(1/(4m))e + sqrt(eta/2)v`,
`tilde r_U=u`.                                                     (3.17)

Hence

`w=det(tilde r_0,tilde r_+,tilde r_U)^2=c eta/2`.                (3.18)

Apply the previously completed B10 theorem `QFORM-COLLINEAR-PRODUCT-BANK-COMPRESSION-v1`, whose source physical-triple constant is

`C_3=16 sqrt(30) 2^(1/4)=104.216889989...`.

It gives

`||p_{X^T A_m X}||_infinity <=2 C_3 (c eta/2)^(-1/3)`.           (3.19)

For `m>=128`, `c eta/2 >= (127/128)(511/512)/2`, so

`boxed: ||p_{X^T A_m X}||_infinity <263.470.`                    (3.20)

This is uniform in `m` and in every admissible original cap-one product law. The family is therefore a counterexample to the hoped **structural implication** “a uniformly safe true near-coloop state must have a uniformly positive leaf-only one-hub projected-crossing packet”, not a counterexample to QFORM.

The distinction is exact: the winning proof topology groups a transverse collinear product bank with the hub certificate before reciprocal payment; the losing topology insists that a leaf-only column bank itself carry three-dimensional Gram determinant.

## 4. Required ruled-side theorem and designated partner applied at actual inequalities

The required `e5f71d.../COUNTEREXAMPLE_SEARCH.md` ruled theorem applies directly to every `A_m` above. Its signature is `(2,1)` and there is no induced linear term, hence on the majority/one-sheet side

`boxed: ess sup_{t>=0} p_{X^T A_m X}(t) <= pi sqrt(2)<4.443.`     (4.1)

Thus only the minority/two-sheet side is relevant to the near-coloop mechanism. Equation (3.20) pays that side too, by a different source-preserving bank compression.

For an actual inequality-level use of the latest completed designated partner result, keep the same physical frame `R_m` but replace `Lambda_m` by its exact-null endpoint

`Lambda_0=[[0,0,1],[0,1,0],[1,0,0]]`,                            (4.2)

which still has spectrum `{-1,1,1}` and determinant magnitude one. The physical hub is now exactly null, has leverage `c`, and every complementary transverse leverage is at most `1/m<1/2`. Account03/B10 r24 therefore yields

`||p_Q||_infinity <=3*2^(4/3)c^(-1/3)`.                          (4.3)

For `m>=128`,

`boxed: ||p_Q||_infinity <7.580`,                                (4.4)

and the partner theorem also supplies a continuous `C_0` density on this exact-null companion. No continuity in the nonzero parameter `eps=1/m` is inferred from (4.4).

## 5. Consequence for the exact-rank-three proof map

The new barrier (2.3) settles a structural question left open by the previous B10 run: **no amount of better leaf partitioning inside the one-original-hub projected-crossing theorem can by itself bridge `h -> 1` when `|det M|` is O(1)**. The full leaf bank has only `rho=1-h` longitudinal Gram mass, so every such packet loses that factor before any analytic estimate is applied.

The explicit family shows simultaneously that this determinant loss is a proof-interface loss, not evidence of a density blow-up: its leaf-only packet is `Theta(rho)` while a disjoint collinear-bank product compression has constant Pluecker volume and yields (3.20).

Therefore the first unpaid implication is sharpened to

`QFORM-NEARCOLOOP-GROUPED-HUB-OR-VECTORBANK-RECEIVER-v1`:

> In the true exact-rank-three near-null/near-coloop survivor, replace the impossible uniformly positive leaf-only one-hub currency by a source-preserving grouped-hub or vector-bank receiver whose determinant currency is the constant hub-incident transverse Pluecker packet, while retaining same-bank longitudinal/transverse contamination. The receiver must remain valid for genuinely non-collinear mixed banks and cannot condition on a rotated projection, take a worst conditional-profile supremum, or treat the `O(sqrt(rho))` longitudinal component as a small random perturbation.

The collinear-bank boundary is paid by (3.20); the exact-null boundary is paid by the designated partner (4.4); the majority-sign side is paid by the required ruled theorem (4.1). What remains is the genuinely non-collinear punctured collar on the minority/two-sheet side.

Full exact-rank-three QFORM: OPEN.  
Full owner conjecture: OPEN.  
Global continuity: OPEN.
