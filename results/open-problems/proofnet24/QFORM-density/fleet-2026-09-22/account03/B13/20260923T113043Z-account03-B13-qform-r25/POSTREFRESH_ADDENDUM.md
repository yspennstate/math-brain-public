# account03/B13 r25 post-refresh addendum — slab-scale transfer for aggregate and Nystrom tails

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T113043Z-account03-B13-qform-r25`  
Status: **NEW SUPPORTING GEOMETRIC COMPILERS / FULL QFORM OPEN / FULL CONTINUITY OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

This addendum consumes two results that landed after the main r25 report and applies them to the actual extremal-product slab inequality. It does **not** treat a small matrix norm as a uniformly small random perturbation. Every comparison is made only on the bounded finite-union product witness furnished by the completed no-attainment purification theorem, after removing translations by centering the actual support sets.

## 1. Immutable inputs used

### 1.1 Designated partner account04/B13: purification without attainment

Source:

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

For every bounded measurable product kernel, and in particular for

`K(x)=1_{x^T A x in J}`,

the supremum over independent cap-one mass-one marginal densities equals the supremum over products of indicators `1_{E_i}` with `|E_i|=1`, with every `E_i` allowed to be a bounded finite union of intervals. There is no optimizer assertion and no single-interval, bounded-diameter, or fixed-fragment-count reduction.

### 1.2 account03/B09 aggregate stability

Source:

`yspennstate/math-open-problems@dc7d419453536317f88f75407b6060c50a37b1be`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T114612Z-account03-B09-QFORM-r31/REPORT.md`.

Let `C in R^{m x 2}` have full column rank, put

`Delta=sqrt(det(C^T C))`,

`ell_k=c_k^T(C^T C)^(-1)c_k`, `q=max_k ell_k<1`,

and let `D=D^T` be an arbitrary leaf block. For the singleton augmentation volumes `Gamma_k` defined in that report, put

`Gamma=(sum_k Gamma_k^2)^(1/2)`.

Then there exist `S=S^T in R^{2x2}` and diagonal `Lambda` such that

`D_0=C S C^T+Lambda`

and

`||D-D_0||_F <= beta`,

`beta := sqrt(2) Gamma/[Delta sqrt(1-q)]`.                    (1.1)

The theorem is deterministic matrix structure. Its source explicitly warns that (1.1) alone is not a small-random-error statement for arbitrary unbounded input laws.

### 1.3 account01/B13 two-hub Nystrom rigidity

Source:

`yspennstate/math-open-problems@ac5acc0621d0b45e2942a259747399d983e24c14`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T113036Z-account01-B13-qform-auto22/REPORT.md`.

For a physical two-hub block

`H_0=[[a,h],[h,g]]`, `a!=0`, `det H_0!=0`,

with two-hub/leaf cross matrix `B`, leaf block `D`, and exact pair Schur/Nystrom remainder

`T_0=D-B^T H_0^(-1)B`,

an actual slab ratio `rho` forces

`||T_0||_max <= eta(rho)`,

`eta(rho):= C_N/[rho^4 |a det H_0|]`,                            (1.2)

where

`C_N=sqrt(128^8+32^8)=268437503.9921875...`.

Again the source correctly states that max-norm smallness cannot be discarded on arbitrary translated or fragmented laws.

## 2. Centered product-set notation

Let every marginal be `1_{E_i}`, where `|E_i|=1` and `E_i` is bounded. Define

`rad(E_i)=inf_c ess sup_{x in E_i}|x-c|`.

Choose a minimizing center `c_i` and put `y_i=x_i-c_i`; then

`|y_i|<=r_i:=rad(E_i)` a.e. on `E_i`.

For a leaf bank `I`, define the two support currencies

`R_2(I,E)=sum_{i in I} r_i^2`,

`R_1(I,E)=sum_{i in I} r_i`.                                      (2.1)

These are translation invariant. They are deliberately **not** claimed to be universally bounded: separated fragments can make them arbitrarily large.

The following elementary observation is the mechanism behind both new compilers. In centered coordinates, write the full quadratic-affine polynomial as

`Q(y,z)=y^T D y + L(y,z)+R(z)`,                                  (2.2)

where `z` denotes all other original coordinates and `L` contains every cross term and every affine term produced by the translations. If `D_0` is another leaf quadratic block, define

`Q_0(y,z)=y^T D_0 y + L(y,z)+R(z)`.                              (2.3)

Thus **only the centered quadratic block is replaced**; the original translation-induced affine and constant terms are retained exactly.

If `E=D-D_0`, then on the actual product support

`|Q-Q_0|=|y^T E y|`.                                             (2.4)

No statement about the size of `Q-Q_0` is made away from that witness.

## 3. Frobenius-tail slab transfer

### Theorem 3.1 — `QFORM-EXTREME-FROBENIUS-TAIL-SLAB-TRANSFER-v1`

Under (2.2)-(2.4), suppose `||E||_F<=beta`. For every interval `J` of length `L>0`, put

`delta_F := beta R_2(I,E)`.                                      (3.1)

Then

`boxed:
 P_E{Q in J}
 <= P_E{Q_0 in J^{+delta_F}},
`                                                                  (3.2)

where `J^{+delta_F}` is the interval obtained by enlarging both endpoints by `delta_F`, and hence has length `L+2 delta_F`.

Consequently, if the centered exact-model polynomial `Q_0` has a density cap `M_0` uniformly in its retained affine terms, then the slab ratio

`rho_E=P_E{Q in J}/L`

obeys

`boxed:
 rho_E <= M_0 [1+2 beta R_2(I,E)/L].
`                                                                  (3.3)

Conversely, with no density assumption on `Q_0`, the enlarged interval itself has ratio at least

`boxed:
 P_E{Q_0 in J^{+delta_F}}/(L+2delta_F)
 >= rho_E/[1+2 beta R_2(I,E)/L].
`                                                                  (3.4)

#### Proof

By Cauchy-Schwarz for the Frobenius inner product,

`|y^T E y|=|<E,yy^T>_F|
 <=||E||_F ||yy^T||_F
 =||E||_F ||y||_2^2
 <= beta sum_i r_i^2
 =delta_F.`                                                       (3.5)

Thus `Q in J` implies `Q_0 in J^{+delta_F}`, proving (3.2). If `Q_0` has density cap `M_0`, the right side is at most `M_0(L+2delta_F)`, which gives (3.3). Dividing (3.2) in the opposite direction by the enlarged interval length gives (3.4). QED.

This is the precise safe replacement for the forbidden heuristic "small matrix norm means small random quadratic perturbation." It is valid only after purification to an actual bounded witness and explicitly pays its centered support radius.

## 4. Apply the aggregate-stability theorem at the slab inequality

Insert (1.1) into Theorem 3.1. There is an exact slope-span-plus-diagonal block

`D_0=C S C^T+Lambda`

for which

`delta_agg
 <= [sqrt(2) Gamma/(Delta sqrt(1-q))] R_2(I,E).`            (4.1)

Hence the exact model inherits the concrete slab ratio

`boxed:
 rho_0
 >= rho_E /
 [1 + (2 sqrt(2) Gamma R_2(I,E))/(L Delta sqrt(1-q))].
`                                                                  (4.2)

In particular, if

`Gamma R_2(I,E)
 <= L Delta sqrt(1-q)/(2 sqrt(2)),`                               (4.3)

then the exact model has an interval with ratio at least `rho_E/2`.

More generally, if an existing analytic theorem pays the exact model with cap `M_0`, then every extreme witness satisfies

`boxed:
 rho_E
 <= M_0
 [1 + (2 sqrt(2) Gamma R_2(I,E))/(L Delta sqrt(1-q))].
`                                                                  (4.4)

Therefore every witness with `rho_E>M_0` must obey the quantitative spread/defect lower bound

`boxed:
 Gamma
 >= [L Delta sqrt(1-q)/(2 sqrt(2) R_2(I,E))]
       (rho_E/M_0-1).
`                                                                  (4.5)

This is a genuine equation-level application of the new aggregate-stability theorem. It converts its previously non-probabilistic Frobenius approximation into a valid geometric small-ball compiler without adding moments or a global support assumption.

Notice what (4.5) does **not** say: it does not force `Gamma` itself to be large uniformly, because the extremal witness may have enormous separated support radii. Instead it identifies the exact missing currency: a bad witness must pay either the exact-model concentration or the slab-scale weighted aggregate defect `Gamma R_2/L`.

## 5. Nystrom max-norm tail: exact skeleton inheritance

The same centering repairs the max-norm tail in the account01/B13 rigidity theorem.

### Theorem 5.1 — `QFORM-EXTREME-NYSTROM-TAIL-SLAB-TRANSFER-v1`

Use the two-hub setup of (1.2), and let the actual extreme-product slab ratio be `rho_E`. On its leaf bank, put

`R_1=sum_j r_j`.

Define the centered **exact Nystrom skeleton** `Q_N` by replacing only the centered leaf quadratic block `D` by

`D_N=B^T H_0^(-1)B`,

while retaining all original cross, outside, translation-induced affine, and constant terms.

Then

`boxed:
 P_E{Q_N in J^{+delta_N}}
 >= rho_E L,
`                                                                  (5.1)

with

`delta_N
 <= [C_N R_1^2]/[rho_E^4 |a det H_0|].`                          (5.2)

Consequently the exact Nystrom skeleton has an interval with ratio at least

`boxed:
 rho_N
 >= rho_E /
 [1 + 2 C_N R_1^2/(L rho_E^4 |a det H_0|)].
`                                                                  (5.3)

In particular, if

`R_1^2
 <= L rho_E^4 |a det H_0|/(2 C_N),`                            (5.4)

then `rho_N>=rho_E/2`.

#### Proof

Here `E=T_0` and `||E||_max<=eta(rho_E)` by (1.2). On the centered support,

`|y^T T_0 y|
 <= sum_{j,k}|(T_0)_{jk}| r_j r_k
 <= eta(rho_E) (sum_j r_j)^2`,                                   (5.5)

which is (5.2). The same interval inclusion as in Theorem 3.1 gives (5.1)-(5.3). QED.

### Corollary 5.2 — conditional payment of the Nystrom skeleton

Suppose a source-valid theorem gives the centered exact Nystrom skeleton a density cap `M_N`, uniformly in all affine terms retained above. Then

`rho_E
 <= M_N [1+2 C_N R_1^2/(L rho_E^4 |a det H_0|)].`              (5.6)

Equivalently,

`boxed:
 R_1^2
 >= [L rho_E^4 |a det H_0|/(2 C_N)]
      (rho_E/M_N-1)_+.
`                                                                  (5.7)

If `rho_E>=2M_N`, this simplifies to the strong fifth-power spread requirement

`boxed:
 R_1^2
 >= L |a det H_0| rho_E^5/(4 M_N C_N).
`                                                                  (5.8)

No claim is made here that every exact Nystrom skeleton is already paid; (5.6)-(5.8) are a compiler for whichever grouped-bank/ridge/third-curvature theorem supplies such an `M_N` in a specific branch.

## 6. Designated-partner transfer back to arbitrary cap-one laws

Fix the original `A,J` and arbitrary independent cap-one densities, and write

`rho_f=P_f{X^TAX in J}/L`.

By the designated account04/B13 no-attainment purification theorem, for every `epsilon>0` there is a bounded finite-union product indicator witness with

`rho_E >= rho_f-epsilon`.                                        (6.1)

Apply Theorems 3.1 and 5.1 to that **actual** compact witness. Thus:

* the aggregate-stability residual can be replaced safely at slab scale only after paying its actual `R_2(I,E)`;
* the Nystrom max-norm tail can be replaced safely at slab scale only after paying its actual `R_1(I,E)^2`;
* no global support radius, moment, interval extremality, or finite fragment count is inferred from purification.

Therefore, if QFORM is false, one may choose arbitrarily large-ratio bounded finite-union product witnesses for which every attempted small-tail simplification has an explicit alternative: either the corresponding exact low-rank/diagonal skeleton itself inherits comparably large concentration, or the witness develops quantitatively large translation-invariant support-spread currency at the tested slab scale.

This is the precise extremal-product interface needed by the newest rank-two aggregate and Nystrom rigidity results.

## 7. Joint normal form after r25 + this addendum

Any strict bad witness obtained by purification can now be required to satisfy simultaneously:

1. the r25 robust leaf-curvature graph constraint: every slab-scale independent transverse triple has `|det(b_j,b_k)| ||b_l|| <=216 sqrt(2)/rho_E^3`;
2. the previous local-principal compiler: every physical `3x3` principal block has `sigma_min <=128*2^(1/4)/rho_E`;
3. if a no-coloop rank-two slope chamber is used, either its exact `C S C^T+diagonal` model inherits a comparable bad interval or the weighted aggregate defect `Gamma R_2/L` is large by (4.2)-(4.5);
4. if an invertible two-hub Nystrom chamber is used, either its exact Nystrom skeleton inherits a comparable bad interval or the centered support spread obeys (5.7), with the fifth-power form (5.8) whenever the skeleton is independently paid.

The full conjecture is still **OPEN**. The addendum closes a proof-interface gap, not the remaining grouped-bank/third-curvature analytic branch. Full continuity also remains **OPEN**; interval comparison alone does not transfer a continuous representative.

## 8. Next B13 implication

`QFORM-EXTREME-SKELETON-OR-SPREAD-CLOSURE-v1`:

> In the strict no-pivot survivor, combine the exact-skeleton inheritance above with one of the completed grouped-bank/ridge payments. If the skeleton is unpaid, preserve that exact low-rank structure and locate the third large spectral direction without rotating the independent coordinates. If it is paid, use (4.5) or (5.8) to exploit the forced slab-scale support-spread currency rather than trying to bound support diameter uniformly.

The crucial point is that separated fragments are no longer an untracked obstruction: their only role in these transfers is through the explicit centered currencies `R_2` and `R_1^2`.