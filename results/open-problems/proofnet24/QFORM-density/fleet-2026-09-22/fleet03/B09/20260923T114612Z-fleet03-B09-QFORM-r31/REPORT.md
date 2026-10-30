SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T11:46:12Z.
attacking: quantitative stability of the rank-two no-augmentation hub/star geometry, using aggregate third exterior volume rather than a worst physical minor.

# fleet03/B09 r31 — quantitative stability of the rank-two no-augmentation geometry

## Status

This run proves a new deterministic structural theorem, `QFORM-RANK2-NOAUGMENT-AGGREGATE-STABILITY-v1`. It quantitatively identifies the correct dimension-free defect from the exact r30 statement `A_II = C M C^T + diagonal`: the relevant quantity is the **sum of squared third exterior volumes over all singleton augmentations**, not the largest singleton third volume.

It also gives a target-valid strict-N3 family showing that `max_k Gamma_k -> 0` alone does **not** imply closeness to the exact diagonal-plus-slope-span model. On that family the aggregate defect stays order one while every individual augmentation tends to rank two. The same family is uniformly paid by the earlier grouped two-slope/one-Fresnel Pluecker theorem, illustrating why aggregate-before-minor smoothing is essential.

The full QFORM conjecture remains OPEN. The new theorem is deterministic matrix structure; by itself it does not permit treating a small dense quadratic residual as a small random error on arbitrary unbounded product inputs. Continuity is proved only in the explicitly invoked Fourier branches, not by the stability theorem itself.

Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources actually consumed


Current corrections consumed include the false law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, fiber-sup dimension loss, the failure of a universally good single cross minor, and the failure of one-heavy-row absorption.

Relevant predecessor results:

1. **r30 grouped cross-rank smoothing**, fleet03/B09: for any original-coordinate cross block of rank `r>2`,
   `||p_Q||_inf <= e r/(r-2) Delta_r(B)^(-1/r)`, with arbitrary same-side curvature and continuous density.
   Canonical predecessor: `yspennstate/math-open-problems@0257b7a08990f303da16797bcbad0d3e6a1e6538`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T104947Z-fleet03-B09-QFORM-r30/REPORT.md`.

2. **Grouped two-slope/one-Fresnel Pluecker smoothing**, fleet03/B09 r23:
   `||p_Q||_inf <= (5e/3)[|lambda| delta^2 pdet(CC^T) rho]^(-1/5)`.
   Canonical predecessor: `yspennstate/math-open-problems@0ca2df8a2cfb2702f2498ee6924f3a7cee63166a`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T034845Z-fleet03-B09-QFORM-r23/REPORT.md`.

3. **Newest volume-stability theorem** from the required Claude continuation, canonical package `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, path `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. For a cross matrix with third-volume `E3` and row volume marginals `alpha_i <= q/2`, `1<=q<3/2`,
   `||p_Q||_inf <= 3e/[(3-2q)sqrt(q)] E3^(-1/6)`.

4. **Designated partner fleet04/B09** `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`, canonical mathematics `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B09/20260923T101659Z-fleet04-B09-dense-self-cross-fourier-r1/REPORT.md`. For a literal invertible physical `3x3` cross block `K`,
   `||p_Q||_inf <= 3 |det K|^(-1/3)`.

## 2. Setup: rank-two hub/slopes and singleton augmentation volumes

Let `C in R^{N x 2}` have full column rank. Write its rows as `c_k^T`, and put

`G = C^T C`, `Delta = sqrt(det G) > 0`,

`ell_k = c_k^T G^(-1) c_k`.

Thus `ell_k` is the leverage of physical leaf coordinate `k` in the two-dimensional slope space. Assume

`q := max_k ell_k < 1`.

Let `D=D^T in R^{N x N}` be the arbitrary within-leaf quadratic block. For each `k`, delete coordinate `k` and define

`d_k = (D_{k j})_{j != k} in R^{N-1}`,

`delta_k = dist(d_k, range(C_{-k}))`.

If a physical hub bank has cross block `P C^T` with `P^T P=I_2`, then moving leaf `k` to the hub side produces the augmented physical cross matrix

`M_k = [ P C_{-k}^T ; d_k^T ]`.

Its rank is at most three. Define

`Gamma_k = Delta_3(M_k) = product of the three nonzero singular values`,

with `Gamma_k=0` when the rank is at most two.

The quantity `Gamma_k` is independent of the particular orthonormal realization `P`: `M_k^T M_k = C_{-k} C_{-k}^T + d_k d_k^T`.

## 3. Exact singleton exterior-volume identity

### Lemma 3.1

For every `k`,

`Gamma_k^2 = det(C_{-k}^T C_{-k}) delta_k^2`

and therefore

`boxed: Gamma_k^2 = Delta^2 (1-ell_k) delta_k^2.`

### Proof

Replace `M_k` by the singular-value-equivalent `3 x (N-1)` matrix

`R_k = [ C_{-k}^T ; d_k^T ]`.

Let `B=C_{-k}^T`. Since `ell_k<1`, `B` has row rank two. The squared product of the three singular values is

`det(R_k R_k^T)`.

Taking the Schur complement of `B B^T` gives

`det(R_k R_k^T)
 = det(B B^T) [ ||d_k||^2 - d_k^T B^T (B B^T)^(-1) B d_k ]
 = det(C_{-k}^T C_{-k}) delta_k^2.`

Also

`C_{-k}^T C_{-k} = G - c_k c_k^T`.

The matrix determinant lemma yields

`det(G-c_k c_k^T)=det(G)(1-c_k^T G^(-1)c_k)=Delta^2(1-ell_k)`.

This proves the identity. QED.

## 4. New theorem — aggregate stability of the exact no-augmentation model

Define the distance to the exact r30 model

`E(C,D) = inf_{S=S^T, Lambda diagonal} || D - C S C^T - Lambda ||_F`.

### Theorem `QFORM-RANK2-NOAUGMENT-AGGREGATE-STABILITY-v1`

Under the setup above,

`boxed:
  [sum_k Gamma_k^2]^(1/2) / Delta
  <= E(C,D)
  <= sqrt(2)/sqrt(1-q) * [sum_k Gamma_k^2]^(1/2) / Delta.
`

Thus, under a no-coloop leverage gate `q<1`, the aggregate squared singleton third-volume is quantitatively equivalent, up to a dimension-free factor, to Frobenius distance from `C Sym_2 C^T + diagonal`.

In particular, the exact condition `Gamma_k=0` for every `k` recovers the r30 algebraic conclusion `D=C S C^T+Lambda`.

### Proof: lower bound

Fix arbitrary symmetric `S` and diagonal `Lambda`. For row `k`, the off-diagonal row of `C S C^T` is

`(c_k^T S c_j)_{j!=k} = C_{-k} (S c_k)`,

which lies in `range(C_{-k})`. Therefore

`delta_k <= || (D-C S C^T-Lambda)_{k,-k} ||_2`.

Summing over `k`,

`sum_k delta_k^2 <= ||D-C S C^T-Lambda||_F^2`.

Since `1-ell_k <=1`, Lemma 3.1 gives

`sum_k Gamma_k^2
 = Delta^2 sum_k (1-ell_k) delta_k^2
 <= Delta^2 ||D-C S C^T-Lambda||_F^2`.

Take the infimum. QED for the lower bound.

### Proof: upper bound

The model family is invariant under right whitening. Put

`C0 = C G^(-1/2)`.

Then `C0^T C0=I_2`, the spans `range(C_{-k})` are unchanged, and

`{C S C^T:S=S^T} = {C0 T C0^T:T=T^T}`.

So it suffices to prove the construction when `C^T C=I_2`.

For each `k`, choose the least-squares coefficient `m_k in R^2` such that

`d_k = C_{-k} m_k + e_k`,

`C_{-k}^T e_k=0`, `||e_k||_2=delta_k`.

Let `U in R^{N x 2}` have row `m_k^T`. Form `E in R^{N x N}` by

`E_{kk}=0`, `E_{kj}=(e_k)_j` for `j!=k`.

Then

`||E||_F^2 = sum_k delta_k^2`.

Choose a diagonal matrix `Lambda0` so that the diagonal matches. Then exactly

`D = U C^T + E + Lambda0`.                                    (4.1)

Decompose

`U = C A + Z`, `A=C^T U`, `C^T Z=0`,

and write `A=S+K` with `S=S^T`, `K=-K^T`. Define

`T = U C^T - C S C^T = Z C^T + C K C^T`.

Because `D`, `C S C^T`, and `Lambda0` are symmetric, (4.1) implies

`skew(T) = -skew(E)`.                                           (4.2)

The orthogonality `C^T Z=0` gives the exact norm identities

`||sym(T)||_F^2 = (1/2)||Z||_F^2`,

`||skew(T)||_F^2 = (1/2)||Z||_F^2 + ||K||_F^2`.

Hence

`||sym(T)||_F <= ||skew(T)||_F = ||skew(E)||_F`.                (4.3)

Now the final residual is symmetric:

`D-C S C^T-Lambda0 = E+T = sym(E)+sym(T)`.

Therefore, by (4.3),

`||D-C S C^T-Lambda0||_F
 <= ||sym(E)||_F + ||skew(E)||_F
 <= sqrt(2) ||E||_F
 = sqrt(2) [sum_k delta_k^2]^(1/2).`                             (4.4)

Finally Lemma 3.1 and `1-ell_k >=1-q` give

`sum_k delta_k^2
 <= [Delta^2(1-q)]^(-1) sum_k Gamma_k^2`.

Insert this into (4.4). QED.

## 5. The correct quantitative parameter is aggregate volume, not max singleton volume

A tempting stability statement would be: if every singleton augmentation has very small `Gamma_k`, then the leaf block must be uniformly close to `C Sym_2 C^T+diagonal`. That is false dimension-freely. The theorem above shows exactly why: the correct parameter is `(sum Gamma_k^2)^(1/2)`.

The following target-valid family makes this sharp.

Let `N=2^m` and take three orthonormal Walsh columns `c^(1),c^(2),u in R^N`, each entry equal to `+/- N^(-1/2)`. Put

`C=[c^(1),c^(2)]`,

and on two hub coordinates plus the `N` leaves define

`A_N = [[0_2, C^T], [C, u u^T]].`                               (5.1)

### 5.1 Exact target spectrum

On the two hub/C pairs, (5.1) is two copies of `[[0,1],[1,0]]`; on `u` it is `+1`; it vanishes on the remaining orthogonal leaf directions. Hence its nonzero spectrum is exactly

`{-1,-1,1,1,1}`.

Thus it satisfies the original target for every `N`.

For `N>=256`, it also lies in strict `N3(1/128)`:

- hub diagonals are zero;
- leaf diagonals are `1/N < 1/128`;
- every hub/leaf principal `2x2` determinant has magnitude `1/N <1/128`;
- every leaf/leaf principal determinant is zero because `u u^T` has rank one.

### 5.2 Every singleton rank-three augmentation degenerates

Here `ell_k=2/N`. A direct least-squares computation gives

`delta_k^2 = (1/N) (N-3)/(N-2)`

and therefore

`boxed: Gamma_k^2=(N-3)/N^2.`                                  (5.2)

Consequently

`max_k Gamma_k = sqrt(N-3)/N ->0`,

but

`boxed: sum_k Gamma_k^2=(N-3)/N ->1.`                           (5.3)

The lower half of the new theorem therefore gives

`E(C,u u^T) >= sqrt((N-3)/N) ->1`.

So the matrices stay a fixed Frobenius distance from every `C S C^T + diagonal`, even though **every single physical leaf augmentation becomes arbitrarily close to rank two**.

This rules out a dimension-free proof based on `max_k Gamma_k` alone.

## 6. The same diffuse survivor is nevertheless uniformly paid by grouped Pluecker smoothing

The active three-frame `[u,C]` is orthonormal and every row leverage equals `3/N`. The r23 disjoint-basis theorem gives

`rho >= 1-sum_i ell_i^2 = 1-9/N`.

For (5.1), `lambda=1`, `delta=1`, and `pdet(CC^T)=1`. Therefore

`boxed:
 ||p_{X^T A_N X}||_inf
 <= (5e/3)(1-9/N)^(-1/5),
`

with a continuous density and the same coefficient multiplying every interval length.

At `N=256`,

`||p||_inf < 4.563015`.

Thus the order-one aggregate stability defect is not an obstruction to QFORM: it is exactly the diffuse transverse-curvature regime that determinant-distributed Fresnel smoothing can pay. What fails is only the attempt to route through one strong singleton augmentation.

## 7. Required newest-volume result applied at an actual implication

For any singleton augmented cut `M_k`, rank is at most three and

`E3(M_k) = Gamma_k^2`.

Whenever its third-volume row marginals satisfy `alpha_i<=1/2`, the newest volume theorem with `q=1` gives the concrete branch

`boxed: ||p_Q||_inf <= 3e Gamma_k^(-1/3).`                       (7.1)

This is a continuous-density `O(|L|)` exit. It agrees with the rank-three grouped Fourier scale from r30. Therefore, after the present stability reduction, a diffuse rank-three singleton is already paid; the difficult region is where all singleton volumes vanish quantitatively and the curvature must be aggregated across coordinates, as in Section 6.

## 8. Designated partner fleet04/B09 applied at an actual inequality

In the Walsh family (5.1), choose a physical left bank consisting of the two hubs and one leaf `k`, and any three leaves on the right. The corresponding literal physical `3x3` cross determinant is

`|u_k det([C_J,u_J])|`.

For the Walsh sign rows, the largest `3x3` determinant of `[C,u]` is `4/N^(3/2)`, so

`max |det K| = 4/N^2`.

Applying the completed designated-partner theorem gives the actual inequality

`boxed:
 ||p_Q||_inf <= 3(4/N^2)^(-1/3)
              = 3 N^(2/3) / 4^(1/3).`                           (8.1)

At `N=256`, this is

`||p_Q||_inf <= 76.195251`.

The inequality is correct but deteriorates with dimension, while the grouped Pluecker payment in Section 6 stays below `4.564`. This is a concrete quantitative demonstration that the physical-minor endpoint is useful locally but cannot replace aggregate-before-minor smoothing in the diffuse hub/star survivor.

For comparison, applying the grouped rank-three singleton theorem to (5.2) gives

`||p_Q||_inf <= 3e Gamma_k^(-1/3)`,

which equals `20.589335` at `N=256` and grows like `N^(1/6)`. Again, one singleton is the wrong scale.

## 9. What changed in the proof map

The exact r30 statement

`all Gamma_k=0  =>  D=C S C^T+diagonal`

now has a dimension-free quantitative replacement, but only in the **aggregate** norm:

`distance to exact model  ~  (sum Gamma_k^2)^(1/2)/Delta`.

This creates a genuine fork for the remaining rank-two hub/star geometry:

1. If the aggregate defect is small, the leaf block is matrix-close in Frobenius/operator norm to the exact diagonal-plus-slope-span model. This is a deterministic structural fact only; because inputs may be unbounded, the residual may not be discarded as a small random quadratic perturbation.
2. If the defect is concentrated in a quantitative singleton rank-three augmentation, r30 / the newest-volume theorem / the fleet04 physical-minor endpoint pay the corresponding cross branch.
3. If the aggregate defect is order one but spread over many vanishing singleton augmentations, Section 5 shows this can happen in the exact target; the r23 Pluecker/Fresnel theorem pays the rank-one transverse prototype uniformly. The general dense aggregate-curvature version remains open.

The next precise B09 debt is therefore

`QFORM-RANK2-AGGREGATE-CURVATURE-DECOMPOSITION-v1`:

> Given rank-two hub slopes `C` and arbitrary symmetric leaf block `D`, convert an order-one aggregate stability defect into either (a) a determinant-distributed transverse low-rank curvature packet paid by existing Pluecker smoothing, (b) a genuine rank-at-least-three cross/volume certificate at universal scale, or (c) a finite-core/high-leverage endpoint already paid elsewhere, while retaining the residual phase exactly and without treating small matrix norm as a small random error.

Full QFORM remains OPEN. Full-target continuity remains OPEN.

## 10. Computation bundle

`CHECK.py` verifies:

- the two-sided stability inequality on 100 deterministic random test instances;
- the exact Walsh-family spectrum and strict-N3 pair determinants at `N=256`;
- `Gamma_k^2=(N-3)/N^2` and total aggregate defect `(N-3)/N`;
- the r23 bound `4.563014343315869`;
- the partner physical-minor bound `76.195250494473555`;
- the singleton grouped-rank-three bound `20.589334288025853`.

Finite checks support the algebra but are not proof certificates.

## 11. Integrity

No Gaussianity, moments, compact support, connected support, log-concavity, identical laws, post-rotation independence, pointwise van-der-Corput decay, arbitrary-joint coarea bound, worst-fiber supremum, or Monte Carlo extremality claim is used.

No schedule, notification, email, task identity, credential, permission, public release, paid model/API/Codex call, or cross-account state was changed.
