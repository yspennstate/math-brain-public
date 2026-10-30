SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T17:22:11Z.
attacking: the rank-two hub/star G_*=0 and near-zero endpoint—classify leaf curvature aligned with the hub-partner plane, then spend any transverse component through source-coordinate mixed-hub/projected-crossing smoothing before a reciprocal physical minor.

# fleet02/B09 r17 — near-zero aggregate volume forces aligned leaf curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / NEW STRUCTURAL STABILITY LEMMA / SOURCE-VALID OBSTRUCTION / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication

The first B09 debt is now

`QFORM-GSTARZERO-ALIGNED-HUBCORE-INTERPOLATION-v1`:

> In the surviving physical rank-two hub/star, after the completed `G_*>0` projected-crossing branch is paid, either (i) a whitened hub-partner row is a physical coloop and must be localized as an original coordinate, or (ii) the leaf curvature is exactly `diagonal + aligned rank-two` when `G_*=0`, and is quantitatively close to that algebraic class when `G_*` is small. Prove a product-source density estimate for the aligned class through an arbitrary nonzero hub core, or combine the aligned low-dimensional phase with the transverse residual before any perturbative deletion. A small coefficient-matrix/Frobenius norm may not be converted into a small random error because the admissible input laws have no support or moment bound.

This is narrower than the preceding `G_* scale or paid exit` debt. The theorem below identifies the exact zero variety and a quantitative near-zero normal form. An explicit target-valid family shows that the owner spectral hypothesis does **not** force `G_*` to be positive or to a universal scale even when all hub-partner physical leverages are diffuse.

## 2. Completed sources used at equations

The required pinned package was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed mixed-hub Theorem H is applied in Section 7 to an actual target-valid source-coordinate star and gives a direct linear interval bound.

The current reviewed grouped projected-crossing theorem was read at

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The latest completed designated partner result available during this run is fleet03/B09

`QFORM-LOCALIZED-HUBPAIR-PROJECTED-CROSSING-CLOSURE-v1`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T171049Z-fleet03-B09-QFORM-r37/REPORT.md`, blob `459b74538b549dc334eef21b09cb3d80257cc1d7`.

It applies `(GC)` with two literal physical hubs and one projected crossing direction, retains an arbitrary physical pair core and arbitrary leaf curvature, and in its upstream diffuse-singleton branch gives

`||p_Q||_infinity
 <= 3*2^(5/6)*(400/27)^(1/6) G_*^(-1/6)
 < 8.378 G_*^(-1/6).`                                        (2.1)

The same constant multiplies interval length and the branch has a continuous density.

I also use this slot's completed earlier theorem `QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1` only as a regression receiver at the exact zero physical-pair core. It states that two literal source hubs with zero `2x2` core and complementary coupling-row wedge `Delta>0` satisfy

`||p_Q||_infinity <= 2 sqrt(2) Delta^(-1/4)`                  (2.2)

with completely arbitrary complementary quadratic curvature. Its proof is conditional linear anti-concentration plus a two-dimensional product-projection density cap, hence directly linear in interval length.

No source used here assumes moments, bounded support, log-concavity, iid inputs, diagonalization in a product basis, or independence after rotation.

## 3. Rank-two hub/star aggregate currency

Let `H,I` be disjoint sets of original coordinates and suppose the physical cross block has rank two:

`A[H,I]=P C^T,      P^T P=I_2`,                               (3.1)

where `C` is `|I| x 2` and has rank two. Put

`D=A[I,I]`.                                                     (3.2)

No restriction is imposed on `A[H,H]`.

For each `k in I`, fleet03/B09 defines

`M_k=A[H union {k}, I\{k}]`,
`Gamma_k^2=e_3(M_k^T M_k)`,
`G_* = sum_k Gamma_k^2`.                                      (3.3)

Because `P` is an isometry on its two coefficient directions, Cauchy--Binet gives

`Gamma_k^2
 = sum_{J subset I\{k}, |J|=3}
     det([C_J^T ; D[k,J]])^2.`                                (3.4)

Thus `G_*` measures precisely the part of each physical leaf row which creates a third exterior direction beyond the two hub-partner rows.

## 4. Exact row identity

Let

`G=C^T C`, `Z=C G^(-1/2)`,                                   (4.1)

so `Z^T Z=I_2`. Write `z_k` for row `k` of `Z` and

`ell_k=||z_k||_2^2=c_k^T G^(-1)c_k`.                         (4.2)

For each `k`, let `Pi_k` be the orthogonal projection in `R^{I\{k}}` onto the row span of `C_{I\{k}}^T` and set

`e_k=D[k,I\{k}](I-Pi_k)`.                                    (4.3)

### Lemma 4.1 — exact singleton defect identity

For every `k`,

`boxed:
Gamma_k^2 = det(G)(1-ell_k)||e_k||_2^2.                        (4.4)`

### Proof

The first two rows in (3.4) are the two rows of `C_{-k}^T`. By the Gram determinant / Schur complement identity, adjoining `D[k,-k]` multiplies their two-row Gram determinant by the squared Euclidean distance of that row from their span:

`Gamma_k^2=det(C_{-k}^T C_{-k}) ||e_k||^2`.                  (4.5)

But

`C_{-k}^T C_{-k}=G-c_k c_k^T`,

and the matrix determinant lemma gives

`det(G-c_k c_k^T)=det(G)(1-c_k^T G^(-1)c_k)
                  =det(G)(1-ell_k).`                          (4.6)

Combining (4.5)-(4.6) proves (4.4). QED.

A physical row is a deletion coloop for the two-dimensional partner plane exactly when `ell_k=1`; then deleting that row drops the rank of `C` below two. Since `sum_k ell_k=tr(Z^T Z)=2`, there are at most two such rows.

## 5. New structural theorem: quantitative aligned-curvature normal form

### Theorem `QFORM-RANK2-HUBSTAR-GSTAR-ALIGNMENT-v1`

Assume the whitened leverage gap

`max_k ell_k <= 1-delta`, `delta>0`.                           (5.1)

Then there exist a diagonal matrix `Lambda`, a symmetric `2x2` matrix `R`, and a symmetric zero-diagonal matrix `T` such that

`boxed:
D = Lambda + Z R Z^T + T,`                                    (5.2)

and

`boxed:
||T||_F <= 4 [G_* /(delta det G)]^(1/2).`                     (5.3)

In particular, under the no-coloop hypothesis `max ell_k<1`,

`boxed:
G_*=0  iff  D=Lambda+Z R Z^T for some diagonal Lambda and R=R^T.`  (5.4)

Thus exact zero aggregate third-volume is not an amorphous general-curvature endpoint: away from a localized coloop it is exactly a diagonal operator plus curvature lying in the same whitened two-plane as the hub partners.

### Proof

From (4.4) and (5.1),

`sum_k ||e_k||^2 <= G_* /(delta det G).`                      (5.5)

For every row choose `a_k in R^2` such that, for `j != k`,

`D[k,j]=a_k^T z_j+e_{kj}`.                                    (5.6)

Let `B` be the `|I| x 2` matrix with rows `a_k`, and define the matrix `E` by `E_kj=e_kj` off the diagonal and `E_kk=0`. Then

`||E||_F^2=sum_k||e_k||^2`.                                   (5.7)

Symmetry of `D` gives, for all `i != j`,

`a_i^T z_j-a_j^T z_i=E_ji-E_ij`.

The diagonal vanishes identically, hence

`K:=BZ^T-ZB^T=E^T-E`,                                        (5.8)

and therefore

`||K||_F<=2||E||_F`.                                          (5.9)

Since `Z^T Z=I`, put `S=B^T Z`. Then

`KZ=B-ZS`,                                                     (5.10)
`Z^T K Z=S^T-S`.                                              (5.11)

Let `R=(S+S^T)/2`. Equations (5.9)-(5.11) imply

`||B-ZR||_F
 <=||KZ||_F + (1/2)||Z(S-S^T)||_F
 <=(3/2)||K||_F
 <=3||E||_F.`                                                  (5.12)

Choose `Lambda` so that `T=D-Lambda-ZRZ^T` has zero diagonal. Off the diagonal,

`T=(B-ZR)Z^T+E`,                                               (5.13)

so, because `||Z^T||_op=1`,

`||T||_F<=||B-ZR||_F+||E||_F<=4||E||_F`.                     (5.14)

Combine (5.5), (5.7), and (5.14) to get (5.3). If `G_*=0`, then `E=T=0`, proving the forward implication in (5.4). Conversely, if `D=Lambda+ZRZ^T`, then every off-diagonal physical row of `D` lies in the span of the two corresponding rows of `C`, so every `3x3` determinant in (3.4) vanishes and `G_*=0`. QED.

### Important scope warning

Equation (5.3) is a coefficient-matrix statement only. It is **not** legitimate under the owner hypotheses to infer that `X^T T X` is probabilistically small when `||T||_F` is small: the input coordinates may have arbitrarily large tails and no moments. Therefore the near-zero branch requires an oscillatory/product-source interpolation, not perturbative deletion. This is exactly where the next analytic work must go.

## 6. Source-valid obstruction: the owner spectral hypothesis does not force G_*

Take two literal physical hubs `a,b` and a flat Walsh leaf bank of size `m>=8`. Choose flat orthonormal vectors `u,v` and put

`s=2`,
`A[I,a]=s u`, `A[I,b]=s v`,
`D=u u^T-v v^T`.                                              (6.1)

First take zero physical hub core. On the grouped basis `{e_a,u,e_b,v}` the active coefficient matrix is the direct sum

`[[0,s],[s,1]]  direct_sum  [[0,s],[s,-1]].`                  (6.2)

Its spectrum is

`{(1+sqrt(17))/2, (1-sqrt(17))/2,
  (-1+sqrt(17))/2, (-1-sqrt(17))/2}`.                         (6.3)

The smallest absolute value is

`(sqrt(17)-1)/2 = 1.56155... >1`,                             (6.4)

so all four active eigenvalues satisfy the owner target. Yet `D` is exactly aligned with the hub-partner plane and (5.4) gives

`boxed: G_*=0.`                                                (6.5)

The whitened leverage of every leaf row is `2/m`, so this is maximally diffuse rather than a coloop construction. Physical hub-leaf coefficients are `2/sqrt(m)` and leaf coefficients are `O(1/m)`.

The obstruction survives a genuinely nonzero physical hub core. Add

`A_ab=A_ba=epsilon`, `A_aa=A_bb=0`.                            (6.6)

The perturbation from (6.2) has operator norm `|epsilon|`, so by Weyl, for `|epsilon|<=1/2`, all four active eigenvalues retain modulus at least

`(sqrt(17)-1)/2-1/2 >1.0615`.                                 (6.7)

Thus the target remains valid while `G_*=0` and the physical pair core may approach the zero stratum through arbitrary nonzero `epsilon`. This is a source-valid counterexample to the structural implication

`three large eigenvalues => G_* >= universal c`,

not a counterexample to QFORM itself.

For `epsilon=0`, this slot's earlier zero-hubpair theorem pays the family without looking at `D`: here the full coupling-row wedge is

`Delta=||2u||^2||2v||^2-<2u,2v>^2=16`,                       (6.8)

hence

`boxed: ||p_Q||_infinity <= sqrt(2).`                          (6.9)

For nonzero `epsilon`, (6.9) cannot be extended by deleting the small coefficient; arbitrary unbounded product inputs forbid such a perturbative step. This is the exact aligned-hubcore interpolation debt identified in Section 1.

There is a second diagnostic: if one tries to use pinned mixed-hub Theorem H on the aligned leaf curvature in (6.1), the augmented rows are proportional to

`(u_i,v_i,2u_i,2v_i)`.

Their Gram has rank two rather than four, so the theorem's mixed-frame determinant is zero. Thus the completed mixed-hub theorem correctly detects the absence of a genuinely transverse source-coordinate curvature direction; no hidden post-rotation independence can repair this certificate.

## 7. Required pinned mixed-hub theorem applied to an actual target inequality

Now take two literal original hubs `a,b`, a disjoint flat Walsh leaf bank `I` of size `m>=8`, and three flat orthonormal vectors `u,v,w` on that bank. Let `J` be any further disjoint coordinate bank. On the principal block `H union I`, set

`Q_0=2X_a<u,X_I>+2X_b<v,X_I>+lambda<w,X_I>^2`,                (7.1)

with `lambda !=0`. Allow **arbitrary** symmetric `A[J,J]`, arbitrary `A[I,J]`, arbitrary `A[H,J]`, and arbitrary affine terms. These are exactly the arbitrary outside/same-side blocks permitted by Theorem H after conditioning on `X_J`; they are not discarded.

The mixed rows on `I` are

`rho_i=(w_i,u_i,v_i)`.                                        (7.2)

Their Gram is `I_3`, and every physical leverage equals `3/m<=1/2`. Apply Theorem H with two hubs and one same-side Fresnel direction. Its actual characteristic-function estimate is

`|phi_Q(t)|
 <= (2|t|)^(-2)(4 pi |t lambda|)^(-1/2)(4 pi)^3
 = 8 pi^(5/2)|lambda|^(-1/2)|t|^(-5/2).`                     (7.3)

Let `K=8pi^(5/2)|lambda|^(-1/2)` and `alpha=5/2`. Integrating `min(1,K|t|^-alpha)` exactly and applying Fourier inversion gives

`boxed:
||p_Q||_infinity
 <= (5/3)2^(6/5)|lambda|^(-1/5)
 <3.829 |lambda|^(-1/5).`                                    (7.4)

Therefore

`boxed:
P{Q in L}
 <= (5/3)2^(6/5)|lambda|^(-1/5)|L|.`                         (7.5)

There is no probability squaring, so no square-root small-ball loss. The principal matrix for `lambda=1` has nonzero spectrum

`{1,-1,1,-1,1}`.                                               (7.6)

Hence it is target-valid. By Cauchy interlacing, adding arbitrary coordinates `J` and arbitrary couplings to them cannot destroy the fact that the full matrix has at least three eigenvalues >=1, because the fixed principal `H union I` block already has three positive eigenvalues equal to one. This is a real source-coordinate target inequality with a dense same-side square and arbitrary additional dense blocks retained.

## 8. Latest designated partner result applied to an actual inequality

Return to the aligned family of Section 6 and add a transverse dense square:

`D_lambda=u u^T-v v^T+lambda w w^T`,                          (8.1)

where `u,v,w` are flat orthonormal Walsh vectors and the hub-to-leaf scale remains `s=2`. The physical hub core may be arbitrary; in particular it may contain the nonzero `epsilon` from (6.6), because the partner theorem retains the whole physical pair core.

For each leaf `k`, the aligned part `u_k u_{-k}-v_k v_{-k}` lies in the span of the two hub-partner rows and contributes nothing to the third determinant. Therefore

`Gamma_k^2
 =s^4 lambda^2 w_k^2 det Gram(u_{-k},v_{-k},w_{-k})
 =16 lambda^2 m^(-1)(1-3/m).`                                (8.2)

The last equality uses

`Gram(u_{-k},v_{-k},w_{-k})=I_3-r_k r_k^T`,
`||r_k||^2=3/m`.                                               (8.3)

Hence

`boxed: G_*=16 lambda^2(1-3/m).`                              (8.4)

All singleton masses are equal, so `Gamma_k^2/G_*=1/m`. For Walsh sizes `m>=32`, this is below the partner diffuse-singleton threshold `27/512`. Applying the latest completed fleet03/B09 localized physical-pair projected-crossing closure, equation (2.1), gives the actual inequality

`boxed:
||p_Q||_infinity
 <= 3*2^(5/6)*(400/27)^(1/6)
    [16 lambda^2(1-3/m)]^(-1/6)`                              (8.5)

or numerically

`boxed:
||p_Q||_infinity
 <5.278 |lambda|^(-1/3)(1-3/m)^(-1/6).`                       (8.6)

For `m=32`, `lambda=1`, this is `<5.365`. The same coefficient multiplies `|L|`, and the partner theorem supplies continuity.

The family is target-valid uniformly as `lambda ->0`: at `epsilon=0` its four `u,v` hub blocks already have the four eigenvalues in (6.3), all of modulus greater than one, while the `w` direction merely adds eigenvalue `lambda`. Thus (8.4) can tend to zero while the owner spectral target stays safely satisfied. This concretely proves that `G_*` is a smoothing currency when present, not a quantity forced at universal scale by the spectral hypothesis.

The contrast between (7.4) and (8.6) is also informative. The specialized mixed-hub theorem sees one genuinely transverse square and pays it as `|lambda|^-1/5`; the fully general arbitrary-curvature partner theorem pays aggregate projected crossing as `|lambda|^-1/3`. At `lambda=0` neither transverse certificate survives. The new alignment theorem identifies exactly what remains there instead of pretending the limit is perturbative.

## 9. Counterexample status and regression discipline

The required pinned `COUNTEREXAMPLE_SEARCH.md` still contains no valid counterexample to the full owner conjecture, and this run found none. The constructions above are **source-valid counterexamples to intermediate structural implications only**:

- target spectral rank does not force `G_*>0`;
- diffuse physical hub-partner leverage does not force `G_*>0`;
- a small nonzero physical hub-core coefficient cannot be deleted under arbitrary unbounded input laws;
- the mixed-hub Gram can be exactly singular when all same-side curvature is aligned with the hub-partner plane.

No conclusion here relies on moments, support, log-concavity, Gaussian comparison, independence of `(u^T X,v^T X)` after rotation, or a worst conditional density supremum.

## 10. Resulting pathway

The rank-two hub/star branch now has a sharper structural split:

1. `G_*>0`: fleet03/B09's completed projected-crossing machinery provides direct `O(|L|)` control at the aggregate scale available after its compiler/localization steps.
2. `G_*=0` and some whitened leverage is one: a literal physical coloop exists; this is a localized source-coordinate endpoint, with at most two such rows.
3. `G_*=0` and no coloop: `D=Lambda+ZRZ^T` exactly. The only non-diagonal leaf curvature is aligned with the two hub-partner projections.
4. small `G_*>0` and leverage gap `delta`: the deviation from the aligned algebra has coefficient Frobenius norm at most `4[G_*/(delta det G)]^(1/2)`, but cannot be deleted probabilistically.

The next useful proof step is therefore phase-sensitive interpolation in case 3/4 through an arbitrary hub core, or a new structural routing that forces that aligned model into an already-paid physical-pair/ridge/definite/cross exit. That is strictly more specific than asking for a universal lower bound on `G_*`, which Section 6 disproves.

Full QFORM status: **OPEN**.  
Full-target continuity: **OPEN**.  
Continuity in the applied Theorem H and fleet03/B09 branches: **PROVED by their integrable characteristic-function envelopes**.  
No valid full-target counterexample was found.
