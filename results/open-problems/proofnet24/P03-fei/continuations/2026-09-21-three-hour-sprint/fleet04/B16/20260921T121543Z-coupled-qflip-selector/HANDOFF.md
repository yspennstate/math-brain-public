# B16 coupled-selector handoff

Status: **PARTIAL / PROVED SELECTOR IDENTITIES / FULL FEI OPEN**. Execution context: **WITHOUT_VERIFIED_BRAIN**.

## Proved this run

1. **Coupled dummy Ward.** Appending one dummy coordinate splits every active ordered-min q-flip into two clone generators whose product is the old generator extended trivially. If the two clones are kept adjacent and clone blocks are put in a uniform random order, the block marginal is exactly the old Shapley entropy marginal; dummy translation symmetry splits it equally between the two clones.
2. **Signed block-parity selector.** For one signed frustrated parity monomial of coefficient `c`, a contiguous-block selector gives zero total marginal to any block with even relation occupancy and gives `c/q_odd` to each block with odd occupancy, where `q_odd` is the odd number of odd-occupancy blocks. Signs and relation multiplicities are preserved exactly.
3. **Ordinary-Shapley refinement defect.** The difference between ordinary fine-player Shapley orbit aggregates and coarse Shapley is an exact Harsanyi-dividend transport. For a fine dividend touching `s` clone pairs with `r` doubled pairs, the coefficient vector has squared norm `r(s-r)/(s(s+r)^2) <= 1/(8s)`. Only order >=3 mixed dividends contribute, hence the defect is purely higher signed plaquette curvature.
4. **Killed shortcut.** Ordinary Shapley is not universally orbit-invariant. The genuine Boolean truth vector `(1,-1,1,-1,1,-1,-1,-1)` has coarse q-flip Shapley shares `(1, 1.2169171866886992...)`; after one dummy coordinate the ordinary fine orbit aggregates are `(1.4547869923250596..., 0.7621301943636398...)`.

The run also consumed the newer compatible fleet02/B16 result that the basiswise pointwise `L_v=O(n)` route is false by an exponential singleton-syndrome family and that transitive random-basis orbit averaging gives the correct signed scale. Do **not** revive that pointwise lemma.

## Exact checker/readback

Primary checker: `check_coupled_selector_exact_v2.py`  
Git blob: `fb58a3db297407fc5fd3a04a55bd75a166a4963f`  
SHA-256: `25921bcafcc0b94d065c958bdbd1a12d0b5a95a61ca1845c21dc0ef67b9ecde0`

Primary output: `verification_v2.json`  
Git blob: `feeb96b1db47f8b22483fc34dc4e7e278daa184c`  
SHA-256: `05436a48e4011720e985aef81f5dc838c31a0a3990541d430cb4294363585f53`

Executed scope: `python -m py_compile`; 24 generic exact rational paired games; 168 exact signed parity games; explicit Boolean counterexample. Both primary files were read back with Git blobs identical to the locally executed bytes.

Report Git blob: `3d1f42314ad5b69a81bd4d8c07b5a77726daeaac`.

## Next mathematical target

Use physically meaningful translation/invariance blocks, apply the signed block-parity allocation relation by relation, and map the remaining mixed higher-curvature defect to the original-coordinate cut-Radon frequencies. The selector mismatch already supplies an exact `1/sqrt{s}` coefficient scale; the next decisive calculation is whether that combines with the proved midpoint fractional noisy-square `sqrt{|U|}` bank to give a dimension-free operator bound after retaining R16/moment refunds and the terminal ledger.
