# account02/B14 proof-first addendum — arbitrary-offset graph compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
**Run:** `20260922T160911Z-b14-qform-localization-r15`  
**Status:** `PROVED SUPPORTING THEOREM / FULL QFORM OPEN`

This addendum responds to the later owner continuation `QFORM-PROOF-FIRST-20260922T161801Z`, which prioritizes full-target proof synthesis and in particular translation-uniform fractional-trace mechanisms. It strengthens the run's main graphical theorem from cycle-consistent vertex shifts to **arbitrary edge offsets**, so a shell/coarea calculation need not first prove that all singular centers arise from one set of vertex translations.

A compatible completed result from account01/B14, `yspennstate/math-open-problems@2ad67886f215eff6f3daed247871a882a6f0314b`, independently proves the three-vertex arbitrary-offset case and gives the square-root triangle constant `125`. The theorem below extends the same offset robustness to every fixed finite graph and gives the exact cluster threshold.

## 1. Theorem — arbitrary-offset graphical inverse-gap localization

Let `G=(V,E)` be a finite simple graph, `V={1,...,m}`, with edge exponents `theta_e>=0`. For `S subset V`, define

`Theta(S)=sum_{e subset S} theta_e`.

Then the following are equivalent.

1. For every `S subset V`, `|S|>=2`,

   `Theta(S)<|S|-1`.                                             (1.1)

2. There exists a finite constant `C_off(G,theta)` such that, **uniformly for every collection of real edge offsets `d_e`** and every independent real `X_i` with probability densities `0<=f_i<=1`,

   `E prod_{e={i,j} in E} |X_i-X_j-d_e|^-theta_e <= C_off(G,theta)`.   (1.2)

If (1.1) fails, no law-and-offset uniform constant exists: take all offsets zero and iid `Uniform[0,1]`, for which the corresponding moment diverges logarithmically at equality and by a power above the threshold.

Thus arbitrary edge incompatibility introduces **no new absolute-integrability debt** below the graphical cluster threshold.

## 2. Graphic-matroid proof of sufficiency

Assume `E` contains at least one positive exponent; otherwise the claim is trivial. Put

`delta=min_{S subset V, |S|>=2} (|S|-1-Theta(S))>0`.              (2.1)

Choose

`epsilon=min{1/2, delta/[2(m-1)]}`.                              (2.2)

For an edge subset `F subset E`, let `r(F)` be its graphic-matroid rank: the number of vertices incident to `F` minus the number of nontrivial connected components of `(V,F)`. Decomposing `F` into connected components with vertex sets `S_1,...,S_c`, the cluster inequalities give

`sum_{e in F} theta_e`
` <= sum_l Theta(S_l)`
` <= sum_l (|S_l|-1-delta)`
` = r(F)-c delta`
` <= r(F)-delta`.                                                (2.3)

Since `r(F)<=m-1` and `epsilon(m-1)<=delta/2`,

`sum_{e in F} theta_e <= (1-epsilon) r(F)`.                      (2.4)

Therefore the vector

`x_e=theta_e/(1-epsilon)`                                       (2.5)

lies in the graphic matroid's independent-set polytope

`P_G={x>=0: sum_{e in F}x_e<=r(F) for every F subset E}`.        (2.6)

The standard finite forest-polytope characterization gives a convex decomposition

`x=sum_r lambda_r 1_{F_r}`,                                     (2.7)

where each `F_r` is a forest, `lambda_r>=0`, and `sum_r lambda_r=1`.

Now define the offset kernel

`h_e= max{1, |X_i-X_j-d_e|^{-(1-epsilon)}}`.                     (2.8)

For every edge,

`|X_i-X_j-d_e|^{-theta_e} <= h_e^{x_e}`:                        (2.9)

when the gap has magnitude at most one this is equality, and when it exceeds one the left side is at most one.

Using (2.7),

`prod_e h_e^{x_e}`
` = prod_r (prod_{e in F_r} h_e)^{lambda_r}`.                   (2.10)

Hölder with exponents `1/lambda_r` yields

`E prod_e h_e^{x_e}`
` <= prod_r [ E prod_{e in F_r}h_e ]^{lambda_r}`.               (2.11)

It remains only to bound a forest term, where arbitrary edge offsets cause no difficulty.

## 3. Forest leaf elimination is translation-uniform

For any fixed real `a` and any cap-one probability density `f`,

`int f(x) max{1,|x-a|^{-(1-epsilon)}} dx`

` <= 1 + int_{|u|<=1}|u|^{-(1-epsilon)}du`

` = 1+2/epsilon =: L_epsilon`.                                  (3.1)

The bound is independent of `a`.

Take a forest `F_r`. Integrate a leaf variable first. Its only forest kernel depends on that variable through

`max{1,|x_leaf-x_parent-d_e|^{-(1-epsilon)}}`,

so (3.1) removes the leaf at cost at most `L_epsilon`, uniformly in the parent value and edge offset. Repeat until every forest edge is removed. Therefore

`E prod_{e in F_r}h_e <= L_epsilon^{|F_r|}`.                    (3.2)

Substitute into (2.11):

`E prod_e |X_i-X_j-d_e|^{-theta_e}`
` <= L_epsilon^{sum_r lambda_r |F_r|}`
` = L_epsilon^{sum_e x_e}`
` <= L_epsilon^{m-1}`.                                          (3.3)

Thus one explicit offset-uniform constant is

`C_off(G,theta) <= (1+2/epsilon)^{m-1}`,                         (3.4)

with `epsilon` from (2.2). This constant is crude but depends only on the finite graph and its cluster slack, never on the offsets, supports, locations, fragment counts, moments, or ambient dimension.

This proves sufficiency.

## 4. Necessity and exact critical obstruction

If some `S`, `q=|S|>=2`, has `Theta(S)>=q-1`, choose all offsets `d_e=0` and iid `X_i~Uniform[0,1]`. Near the full diagonal of the variables in `S`, one common translation is free and the remaining `q-1` relative variables carry a homogeneous singularity of degree `-Theta(S)`. On an angular cone away from partial diagonals, the radial lower bound is

`const * int_0^rho rho^{q-2-Theta(S)} d rho`.                   (4.1)

It diverges logarithmically at `Theta(S)=q-1` and by a power above it. Hence (1.1) is necessary for a bound uniform over laws and offsets.

The complete graph `K_4` with all six exponents `1/2` is again the simplest critical control:

`Theta(V)=3=4-1`,

so even arbitrary-offset technology cannot pay a six-edge square-root four-point shell by raw absolute integration; zero offsets already force logarithmic divergence.

## 5. Relation to account01/B14 and the previous theorem

Account01/B14 (`2ad67886...`) proved arbitrary offsets for the triangle by an explicit convolution/Young argument, giving constant `125` at three square-root edges. The present theorem:

- recovers that the triangle threshold is `theta_12+theta_23+theta_31<2` together with individual exponents `<1`;
- extends arbitrary offset robustness to every fixed finite graph;
- identifies the full family of collision-cluster inequalities rather than only the total exponent;
- supplies a forest-mixture proof which never requires cycle consistency of the offsets.

For cycle-consistent offsets `d_ij=tau_i-tau_j`, the run's main report already gives sharper geometry-specific constants in small graphs; the addendum's value is robustness, not constant optimization.

## 6. Full-target localization compiler with component-adaptive certificates

Combine this theorem with the completed assigned-partner account03/B14 law-level convex-mixture localization (`yspennstate/math-open-problems@871a2d4c9f1ea58d89748ab1abab05021b4408de`).

Suppose there are universal `m_0`, `delta_0>0`, and `K<infinity` such that for every compact finite-fragment extreme-product component `nu`, every target matrix `A`, every interval `I`, and every deterministic outside vector `z`, one may choose — separately for that component — an original-coordinate active set `S`, `|S|<=m_0`, a pair-gap graph `G_nu`, exponents with cluster slack at least `delta_0`, and **arbitrary edge offsets** `d_e(z)` satisfying

`P_nu{X^TAX in I | z}`
` <= K |I| E_{nu_S} prod_{e={i,j} in G_nu}`
`      |X_i-X_j-d_e(z)|^{-theta_e}.                             (6.1)

Then (3.4) gives one constant `C_0=C_0(m_0,delta_0)`, uniform over every component and every outside vector, so

`P_nu{X^TAX in I} <= K C_0 |I|`.                                (6.2)

Finite convex mixing preserves this bound and the partner's total-variation limit transfers it to the original arbitrary-support product law with the same constant.

Hence **translation compatibility of the singular centers is no longer part of the localization debt**. The remaining full-target obligation is purely the matrix/shell step: produce such a bounded-size subcritical graph certificate componentwise, or show a branch forces a critical cluster and therefore needs cancellation/operator aggregation.

This also stays compatible with `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`: the active set and graph may vary with the extreme component. Nothing here asserts the spectral hypothesis forces one fixed physical triple.

## 7. Interaction with the new curved-coarea peer result

The newly completed account01/B06 theorem (`yspennstate/math-open-problems@1bc95193312b70572b2765529ac3b6d98e3fe754`) proves a translation-uniform three-coordinate curved-coarea bound for any invertible physical `3x3` block and explicitly refutes post-hoc determinant-weight averaging in the delocalized Hadamard family. Its first unpaid step is to retain determinant/Pluecker weights inside the reciprocal-distance kernel before scalar collapse.

The theorem above gives a precise admissible endpoint for such a prebound synthesis: if that weighted curved kernel can be reorganized, before taking the scalar block bound, into a convex combination of bounded-size pair-gap graphs satisfying the cluster inequalities with uniform slack, then all arbitrary offsets created by completing squares are harmless and account03/B14 removes the outside localization. Conversely, if the reorganization produces a critical collision cluster, Section 4 shows that an absolute pair-gap majorant cannot be the missing final step even for iid uniforms.

No claim is made that account01/B06's current `1/|Cu|` kernel has already been converted to such a graph form; that is the remaining translation-uniform fractional-trace synthesis problem named by the latest owner continuation.

## 8. Source pins

- owner continuation: `QFORM-PROOF-FIRST-20260922T161801Z`, source `yspennstate/math-research-brain@10695e7784b41c0a2bf1a5e61a93cbc8cfc66564`;
- correction snapshot before this write: `yspennstate/math-research-brain@29e91087236ca7ebeaa5d6b64e42adc450cba975`;
- assigned partner applied: account03/B14 `yspennstate/math-open-problems@871a2d4c9f1ea58d89748ab1abab05021b4408de`;
- compatible arbitrary-offset triangle peer: account01/B14 `yspennstate/math-open-problems@2ad67886f215eff6f3daed247871a882a6f0314b`;
- curved-coarea synthesis peer: account01/B06 `yspennstate/math-open-problems@1bc95193312b70572b2765529ac3b6d98e3fe754`;
- main report for this run: `yspennstate/math-open-problems@cc52390bf9c5007889d0004bd994a3142225d54a`.

Full QFORM remains open. No scheduler mutation, new task, email/notification action, public release, paid call, remote workflow, permission change, or cross-account authentication is used here.
