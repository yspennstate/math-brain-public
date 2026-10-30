# fleet03/B13 r26 early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T130022Z-fleet03-B13-qform-r26`  
Status: supporting lemma proved; full QFORM still open.

## Tail-insensitive slab-core transfer

Let `mu` be any probability law on `R^n`, let `Q,Q0` be real random variables on the same space, and let `J` be an interval of length `L>0`. Put `m=P(Q in J)>0` and `rho=m/L`.

Fix a finite coordinate bank `I`. Suppose that for some `0<=eta<1` there are measurable coordinate cores `K_i`, centers `c_i`, and radii `r_i>=0` such that

`P(Q in J and exists i in I with X_i notin K_i) <= eta m`,

and `|x-c_i|<=r_i` on `K_i`. Suppose, after rewriting both polynomials around the same center `c`, that

`Q-Q0 = y_I^T E y_I`,  `y_i=X_i-c_i`,

with `||E||_F<=beta`. Then on the core event,

`|Q-Q0| <= beta sum_i r_i^2 =: Delta`.

Therefore

`P(Q0 in J^{+Delta}) >= (1-eta)m`,

where `J^{+Delta}` is the interval with both endpoints enlarged by `Delta`. If `Q0` has a density cap `M0`, uniformly in the affine terms produced by the chosen center, then

`rho <= [M0/(1-eta)] [1+2 beta (sum_i r_i^2)/L]`.          (1)

The same argument with `||E||_max<=gamma` gives

`rho <= [M0/(1-eta)] [1+2 gamma (sum_i r_i)^2/L]`.          (2)

The proof is the single event inclusion

`{Q in J} intersect (cap_i {X_i in K_i}) subset {Q0 in J^{+Delta}}`.

No moment bound, support diameter bound, or independence is used in this transfer itself. In the QFORM applications `Q0` will be chosen from a source theorem whose density estimate is uniform in arbitrary affine terms, so choosing the core centers after seeing the slab does not invalidate the analytic input.

## Why this repairs the previous radius interface

The r25 essential-radius currencies `R2=sum rad(E_i)^2` and `R1=sum rad(E_i)` are valid upper bounds, but they are not coercive. For any bounded finite-union unit set `E`, any `epsilon>0`, and any large `R`, remove an interval piece of length `epsilon` from `E` and replace it by a translate at distance `R`. The resulting unit set `E_R` has total-variation distance at most `epsilon` from `E`, while `rad(E_R)->infinity`. Consequently every bounded event probability, including a QFORM slab event, changes by at most `epsilon`, even though the essential-radius currency diverges. Thus a lower bound on ambient essential radius alone cannot close the proof.

The slab-conditioned core estimate (1) is immune to this poisoning: a remote fragment that carries only an `epsilon` fraction of the actual slab mass may be discarded into the `eta` term. Any surviving large core radius must be used by a positive fraction of the concentrated slab event itself.

## Apply the newest three-volume theorem at the actual slab inequality

Use `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. For an original-coordinate cross block `M` with `Z=e3(M^T M)>0` and row volume marginals `alpha_i<=q/2`, `1<=q<3/2`, the exact model has a continuous density cap

`Mvol = 3e/[(3-2q)sqrt(q)] Z^(-1/6)`,

uniformly in arbitrary self terms, outside couplings, and affine terms. Substituting `M0=Mvol` in (1) yields

`rho <= [3e/((3-2q)sqrt(q))(1-eta)] Z^(-1/6)
        * [1+2 beta R2_core/L]`,                              (3)

for every slab-conditioned core with `R2_core=sum r_i^2`.

Equivalently every bad slab with ratio `rho` obeys

`R2_core >= [L/(2 beta)] * ((1-eta)rho/Mvol - 1)_+`          (4)

whenever `beta>0`. At `q=4/3`, `Mvol=(9sqrt(3)e/2)Z^(-1/6)=21.186910... Z^(-1/6)`.

This is a genuine application of the newest volume theorem, not a copied citation: it converts its exact-model density bound into a robust geometric obstruction for the slab-conditioned mass of an extremal witness.

## Designated partner use

The fleet04/B13 theorem at `math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1` reduces the supremum of the bounded slab functional over arbitrary cap-one product laws to bounded finite-union unit-product indicators without assuming an attained infinite-line bathtub maximizer. Hence a violation by rough marginals can be transferred, with arbitrarily small loss, to a compact finite-union product witness before applying the slab-core argument above. No single interval, bounded diameter, or fixed fragment count is assumed.

## Next implication

Replace the noncoercive r25 ambient-radius alternative by the slab-conditioned core currency. The remaining task is to show that if a bad slab genuinely uses widely separated core pieces at positive conditional mass, then translation between those pieces forces an algebraic near-invariance/low-rank relation in the corresponding original-coordinate row of `A`; otherwise (3) pays the slab. This is the next geometric step.

Changed-file privacy review: this checkpoint contains only private mathematical statements/source pins and no credentials, personal data, tokens, or unrelated material. No automated repository scanner was available through the current connector, so this is a manual changed-file-only check.
