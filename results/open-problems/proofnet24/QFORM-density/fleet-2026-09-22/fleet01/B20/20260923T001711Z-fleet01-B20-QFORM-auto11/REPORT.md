# fleet01/B20 QFORM auto11 — anchored-compound degree descent and compulsory spike×dust reserve

Run: `20260923T001711Z-fleet01-B20-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: proof closure and keeper  
Classification: **ESSENTIAL_STEP_APPLIED / NESTED-ANCHOR-DEGREE-DROP / SPIKE-CARRIES-DUST / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction boundary

The target is the full arbitrary-product statement: independent real coordinates with densities bounded by one, and a real symmetric matrix with at least three eigenvalues of modulus at least one. No Gaussian, iid, moment, support, log-concavity, post-rotation independence, uniform pointwise quadratic oscillatory decay, arbitrary-joint coarea bound, or conditional projected-density cap is introduced here. Continuity is tracked separately and is not claimed by the new structural lemmas below.

Fresh owner control was QFORM-only, revision `2026-09-22.15`, at the source checks used for this report. The full conjecture remains OPEN.

## 2. Newest designated-partner result actually consumed

The newest completed fleet02/B20 result available to this run is

`yspennstate/math-open-problems@34a57f18778ea4be069a3f39a953801296d01864`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T000049Z-fleet02-B20-QFORM-auto11/REPORT.md`.

Inside the sufficient no-pivot class `N3(1/128)`, that report reduces the live O0 residual to physical packets. Its P2 residual has an actual original-coordinate cross block `D` satisfying

`E_2(D)>1/48`, `E_5(D)<1/1024`.                                      (2.1)

It pays the `E_5(D)>=1/1024` branch by the reviewed fifth-volume theorem, and for

`E_3(D)<epsilon`, `epsilon:=2^-18`,                                  (2.2)

it proves the fork

`lambda_1 lambda_2>1/96`                                              (2.3)

or a large leading squared singular value `lambda_1>9.481344...`. It also supplies a target-valid Hadamard spike/dust family showing that (2.1)-(2.2) do **not** force a dimension-free lower bound on `sigma_1 sigma_2`.

The substantial-`E_3` concentrated branch from the same proof chain instead produces a nested physical row/column anchor with anchored third-minor mass

`mu > 1/786432 = 1/(3*2^18)`.                                        (2.4)

The two new results below pay the first structural implication in both surviving directions: nested anchoring now decreases exterior degree exactly, and the spike branch is shown to carry a fixed scale-invariant amount of non-leading dust.

## 3. Exact anchored-compound degree-descent identity

### Theorem `QFORM-ANCHORED-COMPOUND-DEGREE-DROP-v1`

Let

`B = [[b, r^T],[c,D]]`                                                (3.1)

be any real matrix after **physical permutations only**. For integer `k>=1`, let `T_k` be the matrix of all `(k+1)x(k+1)` minors of `B` that contain the distinguished first row and first column, indexed by `k` residual rows and `k` residual columns. In exterior-algebra notation,

`T_k = b Lambda^k(D) - (c wedge) Lambda^(k-1)(D) iota_r`,             (3.2)

up to the harmless fixed sign convention in the wedge bases. Moreover the star term has the exact Hilbert-Schmidt norm

`|| (c wedge) Lambda^(k-1)(D) iota_r ||_HS`
` = ||c||_2 ||r||_2 ||Lambda^(k-1)(P_(c perp) D P_(r perp))||_HS`
` = ||c||_2 ||r||_2 sqrt(E_(k-1)(P_(c perp) D P_(r perp))).`          (3.3)

Consequently the total anchored `(k+1)`-minor mass

`Z_anchor^(k+1):=||T_k||_HS^2`                                       (3.4)

obeys the source-coordinate inequality

`sqrt(Z_anchor^(k+1))`
` <= |b| sqrt(E_k(D))`
`    + ||c||_2 ||r||_2 sqrt(E_(k-1)(P_(c perp) D P_(r perp))).`       (3.5)

In particular, if `Z_anchor^(k+1)>mu`, then at least one of the two terms on the right of (3.5) exceeds `sqrt(mu)/2`.

### Proof

For residual row set `I` and column set `J`, both of size `k`, Laplace expansion of the physical minor

`det B[{0} union I,{0} union J]`

along the distinguished row/column is precisely the matrix coefficient of (3.2). Thus (3.2) is an identity of deterministic exterior-power maps; it makes no probabilistic rotation.

For (3.3), if either `c` or `r` is zero the claim is immediate. Otherwise choose orthonormal bases with first domain vector `e_1=r/||r||` and first range vector `f_1=c/||c||`. Interior multiplication `iota_r` vanishes on wedge basis vectors not containing `e_1`, and maps

`e_1 wedge e_I -> ||r|| e_I`

isometrically up to `||r||`. Wedge multiplication by `c` kills exactly the component containing `f_1` and maps a wedge in `c^perp` to `f_1 wedge (...)` isometrically up to `||c||`. Therefore the surviving middle map is exactly

`Lambda^(k-1)(P_(c perp) D P_(r perp))`,

which proves the first equality in (3.3). The second is Cauchy-Binet: the squared Hilbert-Schmidt norm of `Lambda^(k-1)(M)` is the elementary symmetric singular-value sum `E_(k-1)(M)`. Triangle inequality gives (3.5). QED.

This recovers the completed partner deshearing identity at `k=2`, but the degree-`k` formulation is the new point: repeated physical anchoring is now forced to **lower exterior degree** in its star term rather than reproducing an unstructured packet at the same degree.

## 4. Actual application to the concentrated nested `E_3` packet

Apply the newest fleet02/B20 chain's physical nested anchor (2.4). Write its residual matrix, after physical permutations only, as

`D = [[d,s^T],[t,E]]`.                                                (4.1)

Set `k=2` in (3.5). Since

`sqrt(mu)>1/(512 sqrt(3))`,                                           (4.2)

one obtains the explicit dichotomy

`boxed: |d| sqrt(E_2(E)) > 1/(1024 sqrt(3))`                          (4.3)

or

`boxed: ||t|| ||s|| ||P_(t perp) E P_(s perp)||_F`
`       > 1/(1024 sqrt(3)).`                                         (4.4)

Thus the substantial-`E_3` concentrated survivor cannot cycle indefinitely as another undifferentiated third-volume packet. Its first nested anchor descends to either a physical edge times **second compound mass**, or a two-star packet times **transverse first-compound mass**.

Inside `N3(1/128)`, `|d|<1/8`; hence (4.3) further gives the actual inequality

`boxed: E_2(E)>1/49152.`                                              (4.5)

This is not yet a density payment; it is a source-valid, monotone-complexity handoff for the next smoothing step. Importantly, the projections in (4.4) are used only to measure a deterministic norm. No projected random coordinates are declared independent.

A physical two-colouring can also be applied **after** (4.4): independently split the residual row and column index sets into two colours. Each squared star-term coefficient whose two residual row/column indices are distinct is retained in an ordered cross-colour class with probability `1/4`. Hence some disjoint physical four-bank restriction captures at least one quarter of the transverse star Hilbert-Schmidt mass. This is an optional provenance-preserving refinement; no single large coefficient is inferred.

## 5. The fleet02 spike is not naked: a fixed spike×dust reserve

The newest partner's route counterexample correctly kills a robust-second-singular-direction shortcut. The following strengthening shows what remains universally true.

### Theorem `QFORM-R-SMALL-E3-SPIKE-CARRIES-DUST-v1`

Let the squared singular values of a real matrix `D` be

`lambda_1=a >= lambda_2 >= lambda_3 >= ... >=0`,

and assume the exact fleet02/B20 P2 low-third-volume inequalities

`E_2(D)>1/48`, `E_3(D)<2^-18`.                                       (5.1)

Put

`S=sum_(j>=2) lambda_j`, `T=sum_(j>=3) lambda_j`.                     (5.2)

Then

`boxed: a S > 1/50.`                                                  (5.3)

Consequently either the partner's two-direction packet holds,

`a lambda_2>1/96`,                                                    (5.4)

or the complementary spike/dust state satisfies the stronger quantitative reserve

`boxed: a T > 23/2400.`                                              (5.5)

In the latter state one also has

`boxed: lambda_2 < 75/188416 <0.000399,`                             (5.6)

`boxed: T < 9/16384,`                                                 (5.7)

and therefore

`boxed: a >11776/675 =17.4459259... .}`                              (5.8)

Equivalently,

`boxed: sigma_1(D) dist_F(D,{rank<=2}) > sqrt(23/2400)`               (5.9)

while

`sigma_2(D)<sqrt(75/188416)<0.019952` and `sigma_1(D)>4.17683`.       (5.10)

If `D` is a physical subblock of `N3(1/128)`, whose entry cap is

`eta=sqrt(129)/128`,                                                   (5.11)

then (5.8) and `a<=||D||_F^2<eta^2 mn` imply

`boxed: mn>=2216.`                                                     (5.12)

Thus the high-dimensional obstruction isolated by fleet02/B20 is quantitatively a **spike coupled to nonzero collective dust**, not an isolated rank-one spike. The fleet02 Hadamard family is compatible with (5.5): it has a vanishing second singular direction but spends the reserve through many weak tail directions.

### Proof of (5.3)

Let

`e_2^tail := e_2(lambda_2,lambda_3,...)`.

Then

`E_2 = aS + e_2^tail`,
`E_3 = a e_2^tail + e_3(lambda_2,lambda_3,...)`.                      (5.13)

Assume for contradiction `aS<=1/50`. Since `E_2>1/48`,

`e_2^tail > 1/48-1/50 =1/1200`.                                      (5.14)

From `E_3>=a e_2^tail` and `E_3<2^-18`,

`a < 1200/2^18 =75/16384`.                                           (5.15)

Also `e_2^tail<=S^2/2`, hence

`S>sqrt(1/600)`.                                                       (5.16)

For the tail sequence, every term is at most `a`; therefore

`3 e_3(lambda_2,lambda_3,...)
 = sum_(j<k, j,k>=2) lambda_j lambda_k (S-lambda_j-lambda_k)
 >= (S-2a)e_2^tail.`                                                  (5.17)

The exact bounds (5.15)-(5.16) give `S-2a>1/32`. Combining with (5.14),

`e_3(lambda_2,lambda_3,...) > 1/(3*32*1200)=1/115200 >2^-18`,         (5.18)

contradicting (5.1). Thus (5.3) holds.

If (5.4) fails, subtracting `a lambda_2<=1/96` from (5.3) gives

`aT > 1/50-1/96 =23/2400`,                                           (5.19)

which is (5.5). The triple terms containing indices `1,2,j>=3` give

`E_3 >= a lambda_2 T`; using (5.5) yields

`lambda_2 < 2^-18 /(23/2400)=75/188416`,                             (5.20)

which is (5.6). The previously proved exact inequality

`3E_3 >= E_2 T`                                                       (5.21)

and (5.1) give (5.7). Dividing (5.5) by (5.7) gives

`a > (23/2400)*(16384/9)=11776/675`,                                 (5.22)

proving (5.8). Equations (5.9)-(5.12) are immediate. QED.

## 6. What this pays and what it does not

This run does **not** prove the full QFORM theorem and does not claim a counterexample to it. It proves the first missing universal implications in the two newest fleet02/B20 residual mechanisms:

1. concentrated nested third-volume anchoring has an exact one-step complexity descent `E_3 -> E_2 or transverse E_1`, so that recursion cannot simply reproduce the same third-compound debt; and
2. the low-`E_3` spike branch necessarily carries a dimension-free scale-invariant spike×dust reserve (5.5)/(5.9), sharpening the partner's large-spike alternative and increasing the no-pivot physical bank floor from `mn>=1205` to `mn>=2216` on the non-two-direction branch.

The first unpaid analytic implication is now narrower: spend either

- the degree-dropped packet (4.3) or (4.4), or
- the genuine spike×dust reserve `aT>23/2400`

through a product-preserving grouped random-slope/fractional-potential estimate while retaining arbitrary same-side and ambient couplings. The spike/dust family shows that deleting the dust or replacing it by one uniformly large second singular direction is invalid.

## 7. Source/provenance discipline

Newest designated partner applied at actual inequalities: fleet02/B20 auto11, canonical commit `34a57f18778ea4be069a3f39a953801296d01864`. Its inputs (2.1)-(2.4), no-pivot entry cap, and target-valid spike/dust obstruction are preserved as stated.

Prior structural dependency for (5.21): fleet01/B20 prior run, canonical `yspennstate/math-open-problems@87249e62ca7c0ac965eb617d35c356f9e06296f2`, which proved `3E_3>=E_2 T` for `T=sum_(r>=3)lambda_r` and explicitly kept the result algebraic rather than probabilistically rotating the source.

No correction-gated forbidden route is used. Exterior/singular coordinates appear only in deterministic norm identities; all probability-facing coordinates remain the original physical product coordinates.

## 8. Status

`ESSENTIAL_STEP_APPLIED`  
`QFORM-ANCHORED-COMPOUND-DEGREE-DROP-v1`: proved here; not independently reviewed.  
`QFORM-R-SMALL-E3-SPIKE-CARRIES-DUST-v1`: proved here; not independently reviewed.  
Full QFORM target: **OPEN / NOT PROVED / NOT DISPROVED**.  
Global continuity: **OPEN**.
