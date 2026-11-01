# B17 FEI campaign-A adversary — vanishing-mass source hijack and the coefficient-4 barrier

**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** PARTIAL. One exact adversarial theorem and one materially different replacement mechanism are proved on an admissible Boolean family. Full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**New route:** `A-MASS-AWARE-SOURCE-PROMOTION`.

## 0. Exact live candidates attacked

The fleet01/B14 candidate used here is
`20260921T231020Z-proxy-gauge-activation-drop/REPORT.md`, whose live missing raw-reveal arrow is of the form

`B_B <= C1 [ J(f) - E J(f_B) ] + C2 D(f) - already-counted nonnegative credits`,

for the **actual** fleet04/B13 proxy-gauge/source-frontier block. Here `D(f)=sum_i j_i Delta_i` is the current positive depth-defect bank.

The fleet04/B14 candidate used here is
`20260921T232918Z-residual-boundary-cover/REPORT.md`, with the proved crossing estimate

`c_j(A) >= p_j - R_j(A)/2`,  where  `R_j(A)=sum_{i notin A union {j}} Inf_i(eta_j)`.

The fleet04/B14 report still leaves the high-Shannon-rate boundary-cover exception open.

## 1. Cross-account results consumed

I use the fleet04/B13 source-frontier/proxy-gauge theorem at its exact scope: in the simultaneous low-defect, physical-near-subcube sector, reciprocal proxy incidences contract to a DAG; the one-shot block preserves one representative of every DAG source and hits every non-source component.

I apply fleet04/B14's residual-boundary crossing formula exactly to the adversarial family below, both for the bad graph-source survivor and for the downstream replacement survivor.

I also apply fleet02/B14 `20260921T230653Z-asymmetric-shortcircuit-ledger/REPORT.md` only at its proved scope: an exact-subcube pivotality event has zero support error, and its first-mismatch physical tree determines that event with a proved folded-drift denominator on its own `r q` scale. That theorem does not itself upper-bound the corrected entropy cost, and I do not claim otherwise.

## 2. Asymmetric slab-plus-outlier family

Fix integers `r>=3`, `k>=1`. Split the coordinates as

- gates `z=(z_1,...,z_r)`;
- tails `y=(y_1,...,y_k)`.

Set `q=2^{-r}`, `delta=2^{-k}`, `eps=q delta`. Let `Q={z=0^r}` be the full `k`-dimensional slab and let the single outlier be `v=(e_1,0^k)`. Define the Boolean function

`f_{r,k}=-1` on `Q union {v}` and `+1` elsewhere.

This is a sparse, biased, genuinely asymmetric perturbation of the codimension-`r` one-point/subcube defect.

Direct edge counting gives the centered/folded influences

`j_{z1}=2q(1-delta)`,

`j_{zi}=2q(1+delta)` for `2<=i<=r`,

`j_{ya}=2q delta` for every tail coordinate.

Thus

`J(f_{r,k}) = 2q [ r + (r+k-2) delta ]`.

## 3. Exact row-defect formulas

The natural physical proxies are unique once the allowed relative error is small.

For every tail `y_a`, its pivotality row is exactly the single quotient-cube point
`z=e_1, y_{!=a}=0`. Hence it is an exact coordinate subcube and

`Delta_{y_a}=0`.

For `z_1`, the pivotality support is the slab `z_2=...=z_r=0` with the point `y=0` deleted. The relative proxy error is

`e_-/j_- = delta/(1-delta)`

and exact boundary counting gives

`Delta_- = k delta/[2(1-delta)] + (1/2) log2(1-delta)`.

For every `z_i`, `i>=2`, the pivotality support is the slab `z_{-i}=0` plus one isolated outlier point. The relative proxy error is

`e_+/j_+ = delta/(1+delta)`

and

`Delta_+ = (k-2) delta/[2(1+delta)] + (1/2) log2(1+delta)`.

The checker derives the underlying rational `j_i,d_i` directly from truth tables on small parameter pairs and verifies these formulas.

Consequently, for fixed `r`,

`Delta_-, Delta_+, e_-/j_-, e_+/j_+ -> 0` as `k->infinity`.

Therefore, for any fixed positive stability threshold used by the current fleet04/B13 theorem, every row lies in its robust sector once `k` is sufficiently large. The exact current defect bank is

`D(f_{r,k}) = j_- Delta_- + (r-1) j_+ Delta_+`,

so

`D(f_{r,k})/J(f_{r,k}) -> 0` for fixed `r` and `k->infinity`.

## 4. PROVED: the current graph-only source frontier is hijacked by a vanishing-mass source

The proxy incidence graph has exactly two reciprocal components.

The tail rows form a clique `Y`. For any tail row, its exact point proxy fixes every other coordinate, so its closed trigger signature is the whole active coordinate set.

The gate rows form a clique `Z`. Every gate proxy fixes the other `r-1` gates and no tail coordinate, so its closed trigger signature is exactly the gate set.

Hence there is a quotient edge `Y -> Z`, and no edge `Z -> Y`. Thus `Y` is the unique DAG source even though its folded mass

`J_Y = 2 k q delta`

satisfies `J_Y/J_Z -> 0`.

The exact fleet04/B13 source-frontier rule must therefore preserve one tail representative, say `y_*`. Its trigger set is every other coordinate. The actual one-shot reveal block is forced to be

`B = all coordinates except y_*`.

The downstream gate representative is hit automatically. After revealing `B`, every child is either constant or a one-bit character in `y_*`; both have folded influence zero. Therefore

`J(f_{r,k}) - E J((f_{r,k})_{B=b}) = J(f_{r,k})`.

This is the authentic current source-frontier block, not a prescribed-coordinate surrogate.

## 5. Exact Fourier entropy and the coefficient-4 barrier

The Fourier spectrum has a closed form. For nonempty spectral atoms there are only three squared coefficient magnitudes:

`4(q+eps)^2`, `4(q-eps)^2`, and `4 eps^2`.

Writing `phi(t)=t log2(1/t)`, the exact spectral entropy is

`H(f_{r,k}) = phi((1-2q-2eps)^2)`

`  + (2^{r-1}-1) phi(4(q+eps)^2)`

`  + 2^{r-1} phi(4(q-eps)^2)`

`  + 2^r(2^k-1) phi(4 eps^2)`.

For the spectral sample `X`, `Pr(y_* in X)=Inf_{y_*}(f)=2 eps`. Because `B` is exactly the complement of `y_*`, the raw source-frontier Shannon cost is

`B_B = H(X_B | X_{y_*}) = H(f_{r,k}) - h_2(2 eps)`.

For fixed `r`, as `k->infinity`, this tends to the codimension-`r` subcube-defect value. If

`H_r = phi((1-2q)^2) + (2^r-1) phi(4q^2)`,

then

`B_B/J -> H_r/(2 r q)`.

Finally `H_r/(2 r q) -> 4` as `r->infinity`.

### Theorem — actual source-frontier drift coefficient must be at least 4

For every `C1<4` and every finite `C2`, there are admissible Boolean members `f_{r,k}` in the arbitrarily-low-defect current robust sector such that, on the **actual** source-frontier block,

`B_B > C1 [J - E J_child] + C2 D`.

The proof is the two-step limit above: first choose `r` so the zero-defect limiting rate exceeds `C1` by a fixed margin, then choose `k` so `B_B/J` stays in that margin while `D/J` is arbitrarily small. Since the contemplated crossing/information terms are nonnegative rebates subtracted from the right side, they cannot rescue `C1<4` without adding a genuinely new positive bank of order `J`.

**REFUTED:** any attempt to close the current raw source-frontier cost inequality with drift coefficient strictly below `4` plus only a fixed multiple of the present depth-defect bank.

**NOT REFUTED:** coefficient `4` or larger, the folded-cooling compiler, or FEI.

Targeted diagnostics at `(r,k)=(32,40)` give

`B_B/J = 3.9651684390255424`,

`D/J = 1.7923878931813145e-11`.

## 6. Applying fleet04/B14: the forced source survivor has boundary-cover rate tending 4

For the forced source survivor `y_*`, the pivotality event is the single point in the other `r+k-1` coordinates. Put `p_*=j_{y_*}=2 eps`. For every other coordinate `i`,

`Inf_i(eta_{y_*}) = 2 p_*`.

Therefore if a candidate block `A` omits even one coordinate from `B`, then

`R_{y_*}(A) >= 2 p_* > 2(1-gamma)p_*`

for every fixed `gamma>0`. The proved fleet04/B14 crossing criterion forces `A=B` for every positive crossing fraction on this source survivor.

Its Shannon rate is

`B_B/I_B = [H(f_{r,k})-h_2(2eps)]/[J(f_{r,k})-2eps] -> 4`.

Thus a survivor-specific strengthening with universal boundary-cover rate `L<4` is **REFUTED**.

This does **not** establish fleet04/B14's full exception `(every candidate survivor has high rate)`, because a different survivor remains available.

## 7. Materially different replacement executed: promote the high-mass downstream gate

The obstruction is graph-theoretic source status ignoring mass. The vanishing-mass tail source forces the current one-shot block to reveal essentially all high-mass gate structure.

On the same Boolean function, choose the downstream gate survivor `z_1` instead and reveal only its physical proxy block

`A_G={z_2,...,z_r}`.

Its pivotality event is

`eta_{z1}=1_{ z_2=...=z_r=0, y != 0 }`.

The only residual mixed boundary after revealing `A_G` comes from the tails:

`R_{z1}(A_G)=4 k q delta`,

while `p_{z1}=2q(1-delta)`. Applying fleet04/B14 gives

`c_{z1}(A_G)/p_{z1} >= 1 - k delta/(1-delta) -> 1`.

The Fourier atoms can be regrouped by the outside variables `(X_{z1},X_y)` to compute the block Shannon rate exactly; the checker records the formula. The asymptotic result is

`B_{A_G}/I_{A_G} -> 3`

as first `k->infinity` and then `r->infinity`.

At `(r,k)=(32,40)` the diagnostic values are

`B_{A_G}/I_{A_G}=3.0465385486997065`,

`c_{z1}(A_G)/p_{z1} >= 0.9999999999636202`.

So the same admissible witness that forces the graph-source block toward coefficient `4` admits a different, physically realizable high-mass block with rate tending `3` and nearly perfect crossing.

The fleet02/B14 first-mismatch theorem applies exactly to the tiny tail-source event because that event is an exact codimension-`r+k-1` subcube. It gives a real physical determination tree with zero support error and a proved folded-drift denominator on the `O((r+k)p_*)` scale, which is `o(J)` here. The missing universal step is still an upper corrected-entropy payment for that separate determination; the peer report also leaves that step open.

## 8. Replacement obligation

The current source-frontier theorem is excellent for residual influence contraction, but this adversary shows that **graph sources need not be the correct Shannon-payment anchors**.

A new selector should be mass aware: if a source component has negligible folded mass compared with the downstream mass its trigger would force into the reveal, determine that source in a separate nonreusing branch and promote a downstream high-mass component. On this family that changes the rate from `4` to `3` while preserving crossing.

The universal missing theorem is now precise: prove that such discarded-source determinations have a dimension-independent aggregate corrected-entropy payment and do not reuse folded drift, activation, or crossing credits.

A conservative alternative is to accept the barrier and prove the sharp-form candidate

`B_B <= 4 [J - E J_child] + C D`

for the actual source-frontier block. The present family shows that coefficient `4` would be sharp for this architecture. This report does not prove that universal inequality.

Either a mass-aware source-promotion telescope or a universal coefficient-4 source-frontier bound would be a real finite-constant step toward FEI. Neither is complete here, so full FEI remains **OPEN**.

## 9. Verification

The targeted checker is `check_asymmetric_source_frontier.py`. It is not an exhaustive FEI search. It first builds exact Boolean truth tables for `(r,k)=(3,4),(4,4),(4,5)` and verifies the rational `j_i,d_i` formulas for one `z_1`, one `z_i` with `i>1`, and one tail coordinate. It then evaluates only the proved closed forms at larger parameters.

Checker SHA-256: `716d8cffcd84820b1daf432769d81dadce930e169658f352e089efe71d563511`.

Output SHA-256: `1b2c374a415520faf6b726354348539c9679991d995cb4acdaae1b43aafb5940`.

No finite computation is treated as a proof of FEI or of a universal selector theorem.

## 10. Handoff

`candidate_version`: fleet01/B14 `20260921T231020Z-proxy-gauge-activation-drop`, raw source-frontier reveal-cost target (5.1), plus fleet04/B14 `20260921T232918Z-residual-boundary-cover`.

`consumed_peer_artifact`: fleet04/B14 `20260921T232918Z-residual-boundary-cover/REPORT.md`, applied to both survivors; fleet02/B14 `20260921T230653Z-asymmetric-shortcircuit-ledger/REPORT.md`, applied to the exact tiny-source pivotality event.

`applied_to_claim`: the authentic current source-frontier block and survivor-specific boundary-cover rate on the asymmetric slab-plus-outlier Boolean family.

`new_refutation`: drift coefficient `<4` plus any fixed current-defect correction cannot pay the actual source-frontier raw Shannon cost; source-survivor boundary-cover rate `<4` also fails.

`replacement_obligation`: prove a mass-aware source-promotion telescope, or accept and prove the sharp coefficient-4 source-frontier inequality.

`remaining_implication`: dimension-independent aggregate corrected-entropy payment for discarded low-mass source components without reusing folded drift/activation/crossing banks.

`next_recipient`: fleet01/B14 for selector redesign; fleet01/B18 for folded-cooling integration; fleet04/B14 for survivor-adaptive boundary cover.

`full_FEI`: **OPEN / NOT PROVED**.
