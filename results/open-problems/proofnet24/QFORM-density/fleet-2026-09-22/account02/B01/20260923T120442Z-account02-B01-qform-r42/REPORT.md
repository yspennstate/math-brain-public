SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T12:04:42Z.
attacking: the high-leverage destructive-overlap survivor by testing global exterior three-volume before Schur elimination, then identifying what overlap-dominated spectral volume looks like on an exact strict-N3 hub model.

# account02/B01 r42 — exterior three-volume routing before Schur

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T120442Z-account02-B01-qform-r42`  
Classification: **NEW STRUCTURAL DICHOTOMY + SOURCE-VALID PAID BRANCH + ROUTING REFINEMENT / FULL QFORM OPEN**

The exact owner target remains: for every symmetric real `A` with at least three eigenvalues of modulus at least one and every product law with independent one-dimensional densities bounded by one, prove one universal essential-supremum bound for `X^T A X`, or give a valid counterexample. No moments, support regularity, post-rotation independence, Gaussianity or log-concavity are used here.

The phase-aligned fragmented-density construction still refutes every positive-power law-uniform pointwise scalar quadratic-phase decay estimate. Every Fourier estimate used below is a joint decoupled / Fresnel--Brascamp--Lieb estimate from the required source, never that false scalar premise.

## 1. Source boundary and previous unpaid implication

Fresh owner control observed revision `2026-09-22.15`, QFORM-only. The required pinned Claude/Fourier source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The compatible current blobs read in this run are

- `RESULTS.md = 62e20ee976ddeb3f42d3ee5befd6ed49edc917a5`,
- `FOURIER_ROUTE_REPORT.md = 9da148eed6cd43b1046a6f91d0f9329e12921cb4`,
- `COUNTEREXAMPLE_SEARCH.md = ee721b237e206f31298b1871979faaab37a1bac2`.

The two source results used at equations below are:

1. **Theorem D / D'.** For an ORIGINAL-coordinate cross block `M=A[I,J]`, `Z=e_3(M^T M)`, volume-sampling row marginals `alpha_i`, and `max alpha_i<=h<3/4`,

   `||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)`.

   The self blocks, outside couplings and affine terms are arbitrary. For `h<=1/2` this reduces to the sharper Theorem D constant `6 sqrt(e) Z^(-1/6)`.

2. **Theorem H.** A physical hub contributes a full `|t|^-1` factor and a source-disjoint diffuse rank-one square contributes `|t|^-1/2`; the augmented frame may be handled by Brascamp--Lieb when its row leverages are at most one half.

The previous account02/B01 r41 report proved that a strong natural rank-two bicore can be annihilated exactly by a legitimate physical-pair Schur complement. Its first unpaid implication was to test/pay a product-preserving pre-Schur packet before insisting on Schur survival. The present run attacks exactly that point.

## 2. Exact exterior-energy identity

For any real symmetric `n x n` matrix `A`, define for `r=0,1,2,3`

`W_r(A) = sum det(A[I,J])^2`,                                      (2.1)

where the sum is over ordered coordinate triples `|I|=|J|=3` with `|I intersect J|=r`.

### Lemma 2.1 (exterior overlap decomposition)

`W_0(A)+W_1(A)+W_2(A)+W_3(A) = e_3(A^2)`

`                                  = sum_{i<j<k} lambda_i(A)^2 lambda_j(A)^2 lambda_k(A)^2.`  (2.2)

**Proof.** Fix a triple `I`. Cauchy--Binet and symmetry give

`det((A^2)[I,I]) = sum_{|J|=3} det(A[I,J]) det(A[J,I])`
`                = sum_{|J|=3} det(A[I,J])^2.`                    (2.3)

Sum (2.3) over `I`. The left side is `e_3(A^2)`; splitting the right side according to `|I intersect J|` gives (2.2). QED.

Under the owner spectral hypothesis, at least one product of three squared eigenvalues is at least one, so

`boxed: W_0+W_1+W_2+W_3 >= 1.`                                    (2.4)

This identity is deterministic and uses the physical coordinate basis only.

## 3. Disjoint exterior volume produces a real cross cut

Let `S` be a random coordinate subset obtained by independent fair coin flips, and put

`Z_3(S)=e_3(A[S,S^c]^T A[S,S^c])`
`      =sum_{I subset S,J subset S^c, |I|=|J|=3} det(A[I,J])^2.`    (3.1)

For each fixed ordered disjoint pair `(I,J)`, the event `I subset S, J subset S^c` has probability `2^-6`. Therefore

`E_S Z_3(S) = W_0(A)/64.`                                          (3.2)

Consequently

`boxed: max_S Z_3(S) >= W_0(A)/64.`                                (3.3)

This is the missing conversion from a basis-free exterior spectral currency to an actual ORIGINAL-coordinate cross packet on which Theorem D can operate.

### Corollary 3.1 (a paid universal branch)

Assume `W_0(A)>=1/4`. Choose a cut `S` with

`Z=Z_3(S)>=1/256.`                                                  (3.4)

Let `alpha` be the three-volume row marginals of `M=A[S,S^c]` and `beta` its column marginals. Reversing the cut transposes `M`, so the source's one-sided marginal condition may be tested on whichever orientation is lighter.

If

`min(max_i alpha_i, max_j beta_j) <= 2/3`,                         (3.5)

then D' with `h=2/3` yields

`||p_Q||_infinity`
` <= 6 sqrt(e) (4/3)^(-1/2) (1/3)^(-1) (256)^(1/6)`
` = 9 sqrt(3e) 2^(4/3)`
` < 64.763.`                                                        (3.6)

All other blocks of `A` are untouched and arbitrary.

Thus **every full-target matrix** is now routed to one of three states:

- **D'-paid disjoint-volume branch:** (3.6);
- **strong two-sided volume-coloop branch:** `W_0>=1/4`, some cut has `Z>=1/256`, and both row and column volume-marginal maxima exceed `2/3`;
- **overlap-dominated branch:** `W_0<1/4`, whence by (2.4)

  `boxed: W_1+W_2+W_3 > 3/4.`                                      (3.7)

This does not finish QFORM, but it replaces the vague pre-Schur routing debt by a concrete exterior-overlap dichotomy with one entire branch paid at a universal constant.

## 4. The r41 Schur-cancellation family actually contains hidden disjoint volume

The previous r41 family, after conditioning its two physical pair coordinates, has leaf block

`L = [[0,              sigma U V^T],
      [sigma V U^T,    0          ]],`                              (4.1)

where `U,V` are `m x 2` matrices with orthonormal columns. The natural bank cut `I|J` has rank two, hence `Z_3=0`; r41 correctly recorded that fact. But it does **not** imply that every interleaved physical cut has zero three-volume.

Write row vectors `u_i`, `v_j` and leverages

`ell_i=||u_i||^2`, `m_j=||v_j||^2.`                                (4.2)

A nonzero disjoint `3 x 3` minor of (4.1) must use either two `I` rows plus one `J` row against one `I` column plus two `J` columns, or the reverse orientation. For the first orientation its determinant is, up to sign,

`sigma^3 det(U[S,:]) det(V[T,:]) <u_i,v_j>`,                        (4.3)

where `|S|=|T|=2`, `i notin S`, `j notin T`.

For a two-column orthonormal frame,

`sum_{S: |S|=2, i notin S} det(U[S,:])^2 = 1-ell_i`,               (4.4)

because all squared `2 x 2` minors sum to one and the volume-sampling marginal of row `i` is exactly `ell_i`. The analogous identity holds for `V`. Summing (4.3)^2 and including the reverse orientation gives the exact formula

`boxed: W_0(L)`
` = 2 sigma^6 sum_{i,j}(1-ell_i)(1-m_j)<u_i,v_j>^2.`                (4.5)

Since

`sum_{i,j}<u_i,v_j>^2 = tr[(U^T U)(V^T V)] = 2`,                  (4.6)

we get

`W_0(L) >= 4 sigma^6(1-max_i ell_i)(1-max_j m_j).`                 (4.7)

For the flat r41 frames, `ell_i=m_j=2/m`, so in fact

`boxed: W_0(L)=4 sigma^6(1-2/m)^2.`                                (4.8)

In particular, for `m>=4` and `sigma>=1`, the r41 conditional leaf block has `W_0>=1` even though its **natural** bank cut has rank only two.

This is a proof-map refinement: exact Schur cancellation remains valid, but a proof must search interleaved physical cuts rather than treating failure of the natural bank cut as global failure of volume currency.

## 5. Explicit Walsh interleaving pays the destructive-overlap family by Theorem D

Specialise (4.1) to `U=V` equal to the constant Walsh column and one balanced sign Walsh column, and take `m` divisible by four. Each bank splits into sign classes `I+`, `I-`, `J+`, `J-` of size `m/2`.

Split **each** of those four sign classes evenly between a cut `S` and its complement `T`. After row/column permutation, the leaf cross block `M=L[S,T]` is the orthogonal direct sum of four rank-one constant rectangles. Each rectangle has its unique singular value

`(2 sigma/m)*(m/4)=sigma/2.`                                       (5.1)

Hence `M` has four nonzero singular values, all `sigma/2`, and

`Z=e_3(M^T M)=4 (sigma^2/4)^3 = sigma^6/16.`                       (5.2)

Every active row belongs to exactly one rectangle. Under three-volume sampling, its rectangle is selected with probability `3/4`, then the row is selected uniformly among `m/4` rows. Therefore every row marginal is

`alpha_i=(3/4)*(4/m)=3/m.`                                         (5.3)

For `m>=8`, `alpha_i<=1/2`, so the original Theorem D—not even D'—applies after conditioning the two physical pair coordinates. All pair-to-leaf terms become affine and are allowed. Thus

`boxed: ||p_Q||_infinity`
` <= 6 sqrt(e) (sigma^6/16)^(-1/6)`
` = 6*2^(2/3)*sqrt(e)/sigma`
` < 15.704/sigma.`                                                  (5.4)

The characteristic-function envelope supplied by Theorem D is integrable, so this scoped family has a continuous `C_0` density. The earlier r41 Fresnel bound `8/sigma` is numerically stronger, but (5.4) is structurally new: it shows that **interleaving the same original coordinates recovers volume currency before Schur completion**.

The exact r41 physical-pair Schur cancellation and target spectrum are unchanged; the new point is solely that its natural-cut `Z_3=0` is not a global volume obstruction.

## 6. A strict-N3 overlap model with `W_0=0` is paid by Theorem H

The complementary endpoint is not empty. Let `a,z` be flat unit vectors on two disjoint size-`m` coordinate banks `Y,Z`, let `X_0` be one further independent original coordinate, and set

`Q_m = 2 X_0 (a^T Y) + (z^T Z)^2.`                                 (6.1)

The coefficient matrix is the direct sum of a rank-two star and a rank-one square. Its nonzero eigenvalues are exactly

`{-1,1,1}`.                                                        (6.2)

Its largest physical diagonal is `1/m`, and the only nonzero physical `2 x 2` principal determinants are hub--`Y` determinants of magnitude `1/m`. Therefore for every fixed no-pivot threshold `tau>0`, `m>1/tau` places (6.1) in strict N3.

For **every** physical coordinate cut, the star contributes cross rank at most one (the unique hub lies on only one side) and the square contributes cross rank at most one. Hence every cross block has rank at most two and

`boxed: W_0(Q_m)=0.`                                                (6.3)

So the disjoint-volume branch cannot be made exhaustive.

Nevertheless Theorem H applies directly. Take hub set `H={0}` and leaf set `I=Y union Z`. The leaf quadratic block is the rank-one square `zz^T`; the hub slope is `a` on `Y`. In augmented coordinates `(square direction, hub slope)`, the rows are

`(0,a_i)` on `Y`, `(z_j,0)` on `Z`,                                (6.4)

so the augmented Gram is exactly `I_2` and every leverage is `1/m<=1/2`. With `|H|=1`, `r=1`, `lambda=1`, Theorem H gives

`|phi_Q(t)| <= (2|t|)^(-1)(4 pi |t|)^(-1/2)(4 pi)^2`
`            = 4 pi^(3/2) |t|^(-3/2).`                             (6.5)

Integrating `min(1,4 pi^(3/2)|t|^-3/2)` yields

`boxed: ||p_(Q_m)||_infinity <= 3*2^(4/3) < 7.560.`                 (6.6)

This is an actual inequality from the required newest averaged-frequency source on a genuine strict-N3 family with **no rank-three cross cut at all**.

## 7. Exact overlap profile of the hub-square model

The same family explains what the overlap branch can encode. Use the orthonormal range frame

`R=[e_0,a,z]`                                                        (7.1)

and the range coefficient matrix

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`, `det M_0=-1`.                    (7.2)

For a coordinate triple `T`, `det R_T` is nonzero exactly when `T` contains the hub, one `Y` coordinate and one `Z` coordinate. All `m^2` such triples have squared determinant `1/m^2`. Thus the rank-three Pluecker measure is uniform on those triples.

For two independent such triples, the hub is always shared; the `Y` coordinate coincides with probability `1/m`, independently of the `Z` coincidence. Therefore the exterior classes are exactly

`W_0 = 0,`
`W_1 = (1-1/m)^2,`
`W_2 = 2(m-1)/m^2,`
`W_3 = 1/m^2.`                                                      (7.3)

They sum to `e_3(A^2)=1`. In particular

`W_1 -> 1` as `m->infinity`.                                       (7.4)

So a large `W_1` is compatible with strict N3 and with a uniformly bounded density; in this model it is exactly the signature of **one common physical hub plus two diffuse product directions**. The remaining structural task is not to eliminate overlap, but to extract such a hub/grouped packet from general overlap energy or route elsewhere.

## 8. Newest designated partner applied to the same overlap endpoint

The newest completed designated-partner result read before this report is account03/B01

`QFORM-RANK1-BILINEAR-PLUS-SQUARE-LP-v1`,

canonical mathematics `yspennstate/math-open-problems@ffbc3b5d921d1c8c391fe1ea3d8c1264697e8813`. It proves at `p=3`, on disjoint ORIGINAL banks,

`||p_Q||_infinity <= 12 kappa^(-2/3) rho^(-1/3)`,                  (8.1)

for a one-sided rank-one bilinear packet of strength `kappa` plus a source-disjoint grouped square of strength `rho`.

Apply it to (6.1) with its bilinear conditioned-side bank equal to the singleton `{X_0}`, receiver bank `Y`, and square bank `Z`. Then

`kappa=1`, `rho=1`,                                                 (8.2)

so independently of Theorem H,

`boxed: ||p_(Q_m)||_infinity <=12.`                                 (8.3)

The partner theorem also supplies a continuous `C_0` representative. Thus the exact `W_1`-dominated strict-N3 endpoint is paid by both a joint averaged-frequency hub mechanism (6.6) and the newest distribution-domain partner receiver (8.3).

## 9. What changed

The previous r41 unpaid phrase `QFORM-N3-PRESCHUR-OR-SCHUR-ROUTING-v1` is sharpened.

First, **global disjoint exterior volume can be tested before any Schur step**. If it carries at least one quarter of the total spectral three-volume and one orientation is not a volume coloop, D' pays with the explicit universal constant `<64.763`.

Second, the r41 destructive-Schur Walsh family is not a global counterexample to volume routing: its natural cut has `Z_3=0`, but an interleaved cut has `Z_3=sigma^6/16` and is paid by Theorem D.

Third, the complement `W_0=0` is real even in strict N3, but its canonical one-overlap hub model is already paid by Theorem H and by the newest account03/B01 theorem.

The first unpaid implication is therefore

**`QFORM-EXTERIOR-OVERLAP-TO-HUB-ROUTING-v1`.** Starting from the full-target identity (2.4), handle either

1. the strong two-sided three-volume-coloop endpoint (`Z_3>=1/256`, both row/column volume marginals `>2/3`), or
2. the overlap-dominated endpoint `W_1+W_2+W_3>3/4`,

by quantitatively extracting a product-preserving one-/two-hub or bounded-dimensional packet, or routing to an already-paid ridge/pair/grouped-square/exact-null/Schur branch. The hub-square model proves that `W_1`-dominance itself is not pathological; the issue is structural extraction without rotating away independence.

No claim is made that a heavy overlap class automatically has a common coordinate hub. That implication remains unproved and should not be assumed.

## 10. Finite regression

`check_r42.py` is auxiliary verification only. At `m=8`, it checks:

- the Walsh interleaved leaf cross block has four singular values `1/2`, `Z_3=1/16`, and every row/column volume marginal `3/8`;
- the D bound constant at `sigma=1` is `15.703091277070`;
- the hub-square model has nonzero spectrum `{-1,1,1}` and exterior profile `(W_0,W_1,W_2,W_3)=(0,49/64,14/64,1/64)`;
- the Theorem H constant is `7.559526299369`;
- output ends `STATUS=PASS`.

These checks are not used as proof substitutes.

## 11. Status

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The new result is a source-valid structural reduction and two concrete target-family payments. No two independent end-to-end reviews are claimed.
