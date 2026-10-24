SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T10:55:51Z.
attacking: partner r33's bounded 191-coordinate high-leverage star hub: pay any star mass trapped inside the hub by a universal physical pair/pivot bound, leaving only genuinely heavy-to-light aggregate curvature.

# account02/B06 — bounded-hub internal payment and the robust-light rank-one obstruction

**Run:** `b06-20260923T105551Z-182f201f81de`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration / complementary constructions and source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository transport occurred, but no verified native learned-memory retrieval plus receiver use was established.  
**Continuity:** not claimed by the new results; all positive density conclusions below are essential-supremum statements unless an imported theorem explicitly says otherwise.

## 0. Fresh control and source-valid inputs

Fresh control was resolved from `yspennstate/math-research-brain` main during the run. OWNER CONTROL remained revision `2026-09-22.15`, QFORM remained the sole research target, and no account02/B06 pause or stop was present. A same-hour B06 login record from a preceding incomplete invocation already existed, so it was preserved rather than overwritten; this run created its own start record only.

The exact target remains: for arbitrary independent real original-coordinate inputs with densities bounded by one and real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or produce a valid target counterexample. No moment, support, log-concavity, identical-law, diagonal-basis, Gaussian, or post-rotation-independence hypothesis may be inserted.

The live correction boundary is retained: arbitrary-joint rank-three coarea is false; a positive moment of worst conditional projection-density caps is false; law-uniform pointwise quadratic-phase decay is unavailable; rotation does not preserve product independence; a fiber supremum may destroy an integrable transverse singularity; determinant mass need not yield one good physical minor before a bounded-cardinality reduction; and a small quadratic tail cannot simply be deleted.

The mathematical inputs actually used are:

1. **Designated partner account03/B06 r33**, canonical mathematics `yspennstate/math-open-problems@6e33b73460eb417643369a043ebfe903f78e1bd2`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T102206Z-account03-B06-qform-r33/REPORT.md`. Its theorem `QFORM-RANK3-LIGHT-DIFFUSE-OR-191-STAR-HUB-v1` is the starting point of Section 1 below.

2. **Exact-rank-three physical-pivot theorem**, cited and applied in partner r33: for an exact-rank-three original-coordinate matrix `B=U Lambda U^T`, physical leverage `ell_i=||u_i||^2`, nonzero pivot `a_i=B_ii`,

   `||p||_inf <= 128 [ell_i |a_i| |det Lambda|]^(-1/4)`.

3. **Completed pair-log theorem**, `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`: if an exact-rank-three original-coordinate principal block has nonzero eigenvalue magnitudes at least `s`, and a physical `2 x 2` principal pair `P` is invertible indefinite, with `D=|det P|` and `kappa=sigma_min(P)`, then the full ambient form satisfies

   `||p||_inf <= 8 sqrt(5) (D kappa s)^(-1/4)`.

4. **Required newest-Claude package**, pinned at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` were read. Section 4 applies its completed mixed-Fresnel Theorem MF to a genuine target obstruction.

5. **Own immediate durable predecessor**, `yspennstate/math-open-problems@2fdec7c0b085cb5acf5a09847b293b5bcb296b80`, which proved the weighted max-reciprocal receiver for shared zero-anchor coefficients and isolated arbitrary-background near-collinearity. A still later incomplete same-slot checkpoint at `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T103249Z-15bb5d1acfac/EARLY_CHECKPOINT.md` established a determinant-only ruled-side estimate; it is preserved and not claimed as completed by this run.

The early checkpoint for the present run was committed before the full argument.

## 1. Partner r33's first unpaid branch

Let

`B=U Lambda U^T`, `U^T U=I_3`, `s=s_3(B)>0`,

be the exact-rank-three original-coordinate matrix in partner r33. With

`H={i: ell_i:=||u_i||^2>1/64}`, `L=H^c`,

partner r33 proves `|H|<=191` and gives an exhaustive trichotomy. Two branches are already paid:

- if the light Gram remains quantitatively spanning, `||p||_inf<53/s`;
- if some heavy scalar pivot obeys `|B_ii|>=s/(8sqrt(2))`, `||p||_inf<664/s`.

The only unpaid branch therefore satisfies, for every `i in H`,

`|B_ii| < c0 s`,
`||B[H_i^c,{i}]||_2 > c0 s`,

where

`c0=1/(8sqrt(2))`.                                                 (1.1)

Partner r33 asks to aggregate the complete star before reciprocal payment. The first issue is whether the star can be trapped almost entirely inside the finite hub. It cannot remain unpaid there.

## 2. Main theorem: internal hub concentration is already payable

### Theorem 2.1 — `QFORM-191-STAR-HUB-INTERNAL-PAYMENT-v1`

Assume the partner-r33 star-hub branch (1.1). Define, for `i in H`,

`rho_i^2 = sum_{j in H, j!=i} B_ij^2`,
`tau_i^2 = sum_{l in L} B_il^2`.                                   (2.1)

Put

`beta = sqrt(3)/(16 sqrt(380)) = 0.00555327072899...`,
`delta = beta/sqrt(2) = 0.00392675539023...`,
`gamma = 1/(16sqrt(2)) = 0.0441941738242...`.                      (2.2)

Then at least one of the following holds:

1. the full quadratic form has

   `||p||_inf < 1447/s`;                                            (2.3)

2. every heavy row carries a genuinely heavy-to-light aggregate packet,

   `boxed: tau_i >= gamma s = s/(16sqrt(2))  for every i in H.`     (2.4)

No individual light edge is selected in (2.4).

### Proof

Suppose (2.4) fails for some heavy `i`. Then `tau_i< c0 s/2`. By (1.1),

`rho_i^2 = ||B[H_i^c,{i}]||_2^2 - tau_i^2
          > c0^2 s^2 - (c0^2/4)s^2
          = (3/4)c0^2 s^2`,

so

`rho_i > (sqrt(3)/2)c0 s`.                                         (2.5)

If `|H|=1`, then `rho_i=0`, contradiction. Hence `2<=|H|<=191`, so there are at most 190 internal neighbours. By averaging the squared internal star mass, some `j in H`, `j!=i`, satisfies

`|B_ij| >= rho_i/sqrt(|H|-1)
         > [sqrt(3)c0/(2sqrt(190))] s
         = beta s`.                                                 (2.6)

Now split according to the two physical diagonals.

#### Pivot subcase

If `|B_ii|>=delta s` or `|B_jj|>=delta s`, the relevant coordinate is heavy, hence its leverage is `>1/64`. Also `|det Lambda|>=s^3`. The completed exact-rank-three pivot theorem gives

`||p||_inf
 < 128 [(1/64)(delta s)s^3]^(-1/4)
 = 128(64/delta)^(1/4) s^(-1)
 = 1446.26042011.../s`.                                            (2.7)

#### Pair subcase

Assume instead

`|B_ii|<delta s`, `|B_jj|<delta s`.                                (2.8)

The physical principal pair

`P=[[B_ii,B_ij],[B_ij,B_jj]]`

is indefinite, because by (2.6), (2.8), and `delta=beta/sqrt(2)`,

`det P = B_ii B_jj-B_ij^2
       < delta^2 s^2-beta^2 s^2
       = -(beta^2/2)s^2 <0`.                                       (2.9)

Quantitatively,

`D:=|det P| >= (beta^2-delta^2)s^2=(beta^2/2)s^2`.                 (2.10)

Compare `P` with the off-diagonal matrix `P0=[[0,B_ij],[B_ij,0]]`. Since

`||P-P0||op=max(|B_ii|,|B_jj|)<delta s`,

Weyl's singular-value perturbation inequality gives

`kappa:=sigma_min(P)
 >= |B_ij|-delta s
 >= (beta-delta)s
 = beta(1-1/sqrt(2))s`.                                            (2.11)

Apply the completed pair-log theorem:

`||p||_inf
 <= 8sqrt(5)(D kappa s)^(-1/4)
 <= 8sqrt(5)[(beta^2/2) beta(1-1/sqrt(2))]^{-1/4}s^(-1)
 = 1421.48906795.../s`.                                            (2.12)

Thus failure of (2.4) always implies (2.3). QED.

### What this accomplishes

Partner r33 deliberately refused to pick a single edge before aggregation, because a diffuse star can have every edge tiny. The present argument respects that correction. It first uses the complete star norm, then only after partner r33 has compressed the dangerous set to at most 191 physical coordinates does it use finite-cardinality averaging. The loss `sqrt(190)` is therefore universal, not dimension-dependent.

Equivalently, a genuinely unpaid r33 survivor must satisfy simultaneously

`|B_ii|<delta s` for all `i in H`,
`|B_ij|<beta s` for all distinct `i,j in H`,
`||B_{i,L}||_2 >= gamma s` for all `i in H`.                        (2.13)

The first two statements follow because any violation is paid by exactly the pivot/pair argument above. Thus the remaining curvature is forced out of the finite hub and into the product light bank.

## 3. A second deterministic compiler: row area or common light direction

The robust light packet in (2.13) still need not be two-dimensional. Let

`C=B_{H,L}`

be the heavy-to-light cross block, with row vectors `c_i`. Since `rank(B)=3`, `rank(C)<=3`. In an unpaid survivor,

`||c_i||>=gamma s` for every `i in H`.                              (3.1)

The following exact split makes the next analytic debt explicit.

### Proposition 3.1 — `QFORM-191-ROBUST-LIGHT-ROW-AREA-OR-COMMON-DIRECTION-v1`

Let `m=|H|<=191` and set `eta=1/128`. Then either:

**(T) transverse row-area branch.** `sigma_2(C)>=eta s`, and there exist distinct `i,j in H` such that

`Delta_ij := sqrt(||c_i||^2||c_j||^2-(c_i.c_j)^2)
 >= [gamma eta/sqrt(binomial(191,2))] s^2
 = 2.56316499669...e-6 s^2`;                                      (3.2)

or

**(R1) common-direction branch.** There is a rank-one matrix `C1=alpha r^T`, `||r||=1`, such that

`||C-C1||_F < gamma s/4`,                                          (3.3)

and in particular every heavy row has

`|alpha_i| > 3gamma s/4`.                                          (3.4)

### Proof

If `sigma_2(C)>=eta s`, then `sigma_1(C)>=max_i||c_i||>=gamma s`. Cauchy--Binet for row areas gives

`sum_{i<j} Delta_ij^2
 = e_2(CC^T)
 = sum_{p<q} sigma_p(C)^2 sigma_q(C)^2
 >= sigma_1(C)^2 sigma_2(C)^2
 >= gamma^2 eta^2 s^4`.                                            (3.5)

There are at most `binomial(191,2)` pairs, proving (3.2).

If `sigma_2(C)<eta s`, take the best rank-one SVD approximation `C1`. Since `sigma_3<=sigma_2`,

`||C-C1||_F
 = sqrt(sigma_2^2+sigma_3^2)
 < sqrt(2) eta s
 = s/(64sqrt(2))
 = gamma s/4`.                                                      (3.6)

Each row error is bounded by the Frobenius error. Combining with (3.1) gives

`|alpha_i|=||(C1)_{i,.}||
 >= ||c_i||-||(C-C1)_{i,.}||
 > gamma s-gamma s/4=3gamma s/4`.                                  (3.7)

QED.

This proposition does not claim a density bound in branch (T): the heavy pair can have small nonzero quadratic coefficients, and the full light block remains arbitrary. It identifies the exact currency available without making the invalid leap from row area to post-rotation independence.

## 4. Source-valid obstruction: robust light stars need not yield transverse heavy rows

The natural strengthening of Proposition 3.1 — that robust star rows in a three-large-eigenvalue target must force a universal row angle — is false.

### Construction — `QFORM-ROBUST-HUB-NO-ROW-AREA-v1`

Take two heavy original coordinates `X_1,X_2` and `N` light coordinates `Z_1,...,Z_N`, all independent with density caps one. Let `N>=128` be even and define orthonormal diffuse vectors

`u=(1,...,1)/sqrt(N)`,
`v=(1,...,1,-1,...,-1)/sqrt(N)`                                    (4.1)

with `N/2` plus signs and `N/2` minus signs in `v`. Put

`alpha=(1/sqrt(2),1/sqrt(2))`,
`S=alpha_1 X_1+alpha_2 X_2`,
`U=u.Z`, `V=v.Z`,

and

`Q_N = 2 S U + V^2`.                                                (4.2)

In the orthonormal grouped basis `(S,U,V)`, the quadratic matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,                                      (4.3)

so the nonzero spectrum is exactly

`{-1,1,1}`.                                                        (4.4)

Thus this is a genuine exact target for every `N`.

The range projection on each heavy physical coordinate has leverage `1/2>1/64`, while every light coordinate has leverage

`u_l^2+v_l^2=2/N<=1/64`.                                            (4.5)

Hence partner r33 has exactly the two-coordinate heavy hub `H={1,2}`. Both heavy diagonals and their mutual edge are zero, while each heavy-to-light star norm is

`||c_i||=1/sqrt(2)`.                                                (4.6)

But

`C=alpha u^T`                                                       (4.7)

has rank one exactly, so every heavy coefficient row is collinear and every row-area determinant in (3.2) vanishes. This refutes any deterministic inference

`robust heavy-to-light row norms => quantitative row transversality`.

It is not a QFORM counterexample.

## 5. Required newest-Claude result applied to the obstruction

The same family is paid uniformly by the completed newest-Claude mixed-Fresnel theorem; this shows what a valid product-preserving repair looks like in the pure rank-one endpoint.

Because `X_1,X_2` are independent with density caps one, the sum

`Y=X_1+X_2`

has density cap at most one by convolution. It is independent of the light product bank `Z`. Since `S=Y/sqrt(2)`, (4.2) becomes

`Q_N = sqrt(2) Y U + V^2
     = 2Y (u/sqrt(2)).Z + (v.Z)^2`.                                (5.1)

This is an exact regrouping of independent sources; no rotation of the original product law is asserted.

Apply Theorem MF from the pinned `FOURIER_ROUTE_REPORT.md` with one heavy scalar `H={Y}`, leaf bank `L=Z`, one Fresnel direction `S_leaf=v`, eigenvalue `lambda=1`, and hub coupling vector

`C_leaf=u/sqrt(2)`.                                                 (5.2)

The mixed feature Gram is

`Gamma = [[||u/sqrt(2)||^2, (u/sqrt(2)).v],
          [(u/sqrt(2)).v, ||v||^2]]
        = diag(1/2,1)`,                                             (5.3)

so `det Gamma=1/2`. At each light coordinate `l`, the normalized feature leverage is

`(u_l/sqrt(2),v_l) Gamma^{-1} (u_l/sqrt(2),v_l)^T
 = u_l^2+v_l^2
 = 2/N <=1/2`.                                                      (5.4)

Theorem MF therefore gives

`|phi_Q(t)|
 <= (4pi)^(3/2) 2^(-1) |t|^(-3/2) det(Gamma)^(-1/2)
 = (4pi)^(3/2)/sqrt(2) |t|^(-3/2)`.                                (5.5)

Integrating `min(1,B|t|^(-3/2))` gives

`boxed:
 ||p_QN||_inf <= 12 * 2^(-1/3)
               = 9.52440631181... .`                               (5.6)

This is uniform in `N` and in all cap-one original input laws.

For comparison, with a single physical heavy scalar rather than the two-variable sum, the same calculation has `Gamma=I_2` and gives the familiar newest-Claude constant `12*2^(-2/3)=7.55952629937...`.

Thus the rank-one robust-star endpoint is structurally real, but in the clean case where all heavy dependence enters through one grouped sum, the correct payment is to aggregate that independent heavy bank first and then use the diffuse third direction in a mixed-Fresnel integral. Selecting an individual star edge would lose the dimension-free geometry.

## 6. Consequence for the partner r33 programme

Splicing Theorem 2.1 into partner r33 gives the following sharpened exhaustive statement for its exact-rank-three matrix `B`:

- conditioned diffuse light frame: `||p||_inf<53/s`;
- heavy scalar pivot: `||p||_inf<664/s`;
- internally concentrated heavy star: `||p||_inf<1447/s`;
- otherwise a hub `H` of at most 191 original coordinates satisfies (2.13), so **every** heavy row sends at least `s/(16sqrt(2))` of Euclidean star mass into the genuine product light bank.

Inside the last branch, Proposition 3.1 gives a second exhaustive split:

- quantitative transverse row-area currency (3.2); or
- a rank-one common light direction capturing all heavy-to-light rows to Frobenius error `<gamma s/4`, with every heavy coefficient along that direction still of size `>3gamma s/4`.

The construction in Section 4 proves the rank-one branch cannot be removed by deterministic spectral reasoning, even for an exact target with eigenvalues `{-1,1,1}` and with all light physical coefficients tending to zero.

## 7. First unpaid implication

The next B06 debt is

`QFORM-191-ROBUST-LIGHT-TRANSVERSE-OR-GROUPED-RANK1-RECEIVER-v1`:

> Starting from (2.13), retain the full heavy-heavy block and the full light quadratic block. In the transverse row-area branch, turn the pair of shared light coefficient forms into a weighted curved-fiber payment without assuming the two heavy diagonals/cross-entry vanish. In the near-rank-one branch, aggregate the common light direction before reciprocal payment and use the third large spectral direction to control the residual heavy quadratic dependence; the pure grouped family (4.2) is paid by newest-Claude Theorem MF, but arbitrary heavy-heavy curvature and arbitrary light background curvature remain.

A valid continuation may route either branch into an already-paid exact physical pair, mixed-Fresnel frame, aggregate volume/ridge exit, or a new joint negative-moment receiver. It may not infer a uniformly good individual light edge, a uniformly positive row angle, or independence after rotating the heavy bank.

## 8. Status

The full QFORM conjecture is **OPEN**. No target counterexample was found. The source-valid counterexample in Section 4 refutes only an intermediate deterministic transversality claim. The main positive advance is that the entire internally-concentrated half of partner r33's 191-star-hub debt is now paid with an explicit scale-correct bound, so every genuinely unpaid star must carry universal aggregate curvature into the original-coordinate light product bank.

Independent review of the new theorem and constants has not yet been performed.
