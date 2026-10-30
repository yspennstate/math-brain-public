# B14 FEI — parity-line adaptive restrictions without geometry loss

Status: PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.
Execution: WITHOUT_VERIFIED_BRAIN. No novelty or publication-priority claim.

This run attacks interface A with a non-coordinate physical restriction. It consumes fleet02/B17 `20260921T224419Z-affine-parity-straightening/REPORT.md` and fleet04/B18 `20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`.

## Main proved lemma

Let `f:{0,1}^n->{-1,1}` have spectral sample `X`, with `p_S=hat f(S)^2`. For a partition `Pi={C_1,...,C_m}` of the coordinates, impose within every block `C` all relative-parity constraints `x_v xor x_root = z_v`, with `z` uniform. This is an affine physical restriction of codimension `n-m`, leaving one free root bit per block. If `f_z` is the resulting Boolean child, then

`E_z I(f_z) = sum_{C in Pi} Pr(|X intersect C| is odd)`.

Hence the exact influence drift is

`D_Pi = I(f)-E_z I(f_z) = sum_C E[ |X intersect C| - (|X intersect C| mod 2) ] >= 0`.

Proof: use the invertible forest coordinates `y_root=x_root`, `y_v=x_v xor x_parent(v)`. In the dual map, the surviving root character of block `C` is the parity of `|S intersect C|`. Averaging branch Fourier squares over all fixed edge parities kills cross terms inside each dual fibre, so the child marginal at the root is exactly that parity probability. Summing root marginals proves the identity.

Thus these non-coordinate restrictions have no ordinary-influence geometry loss, and their drifts telescope on any adaptive tree.

### Pair case and the peer mixed-curvature law

For `C={i,j}`, write `q_ij=Pr(i,j in X)`. Then

`D_{ij}=2 q_ij`.

The fleet04/B18 theorem gives `4 q_ij = p_ij + 4 o_ij`, where `p_ij` is pivotality-support disagreement and `o_ij` opposite-sign overlap. Therefore

`D_{ij}=p_ij/2+2o_ij`.

So the genuine signed mixed-curvature bank has an exact realizable interpretation: half of it is the ordinary-influence drift of a parity-line merge.

## Application to the newest affine-parity peer result

Consume fleet02/B17's completed result: if the pivotality event `eta_i` is within symmetric-difference error `e<1/2` of an affine parity halfspace on a nonempty control set `F`, `r=|F|`, then for every `k in F`,

`p_ik >= 1-2e`.

Combine this with `4q_ik=p_ik+4o_ik` to get `q_ik >= (1-2e)/4`.

Now take ONE parity-line block `C={i} union F`. Pointwise, if `i in X` and `m=|X intersect F|`, then

`|X intersect C|-(|X intersect C| mod 2) >= m`.

Consequently

`D_C >= sum_{k in F} q_ik >= r(1-2e)/4`.

The block has codimension `r`. Revealing its `r` affine parity constraints sequentially in forest coordinates and using the universal one-coordinate restriction cap `Delta H<=2` at every intermediate Boolean child gives

`Delta_C H <= 2r`.

Therefore the direct non-coordinate block obeys

`Delta_C H / D_C <= 8/(1-2e)`.

In particular, the fleet02/B17 near-parity threshold `e<=1/34` gives the explicit paid step

`Delta_C H <= (17/2) D_C = 8.5 D_C`.

For exact affine parity (`e=0`) the constant is at most `8`.

This removes the peer report's affine-coordinate inflation ledger on this sector: rather than straighten an approximate parity and later amortize the accumulated change in `J`, contract the pivot and all parity controls in one original-coordinate affine line. The actual influence drift is nonnegative and telescopes exactly, so there is no cumulative geometry debt. This does NOT handle cores far from every affine parity halfspace.

## Attempted refutation and finite evidence

A stronger pair-only selector is false at the current lower-bound scale. A five-variable Boolean function, normalized by `f(00000)=+1`, is negative on every input of Hamming weight at least 3 and on the five weight-2 sets forming the cycle

`{0,2},{2,1},{1,4},{4,3},{3,0}`.

Its spectral square multiset is exactly `16 x (1/256), 10 x (9/256), 6 x (25/256)`, with `I=25/16` and numerical entropy `H=4.164563755484309` bits. For every one of its ten pairs, direct parity merge gives

`D=3/16`, `Delta H=1.2402229725414227`, `Delta H/D=6.614522520220921`.

Thus a universal single-pair parity selector with constant at most `6.614522520220921` is REFUTED; in particular it cannot by itself close at the currently recorded unrestricted lower-bound scale `6.521845710923046575`.

But the non-coordinate partition strategy survives this witness. Exhausting all 52 set partitions, the best partition is the single five-coordinate block: `E H(child)=0`, `E I(child)=11/16`, drift `7/8`, ratio

`4.75950143483921`.

Exhaustive sign-normalized finite checks gave maxima of the best pair-selector ratio `4.0, 4.867668746754797, 4.867668746754797` for `n=2,3,4`, while allowing arbitrary partition-line restrictions gave `4.0, 4.433834373377398, 4.557890505417236`. These are finite checks, not a universal theorem.

## Full contraction and the remaining universal implication

Putting all coordinates in one block gives children on one bit, hence zero child spectral entropy. If

`o(f)=Pr(|X| is odd)`, then

`D_all=I(f)-o(f)`

and the selector ratio is exactly

`H(f)/(I(f)-o(f))`.

The quantity `I-o` is already present elsewhere in the current FEI project, including the fleet02 interactive quadratic-phase composition theorem; no novelty is claimed for it. The new point here is its exact physical realization as the drift of a geometry-preserving parity-line restriction, and the partition interpolation between pair merges and full contraction.

A bound `H<=C(I-o)` would immediately prove FEI but is OPEN and is not asserted. The current Numaro seed itself has reconstructed `I=261/128`; direct current-run Walsh evaluation gives odd spectral mass `o=163/256=0.63671875`, `H≈6.776605309005978`, hence full-contraction ratio `≈4.83234250447223`. The known composition amplification still forces any universal constant for this stronger target to be at least the current FEI lower bound asymptotically.

## Claim ledger

PROVED: partition parity-line influence-drift identity and nonnegativity; pair drift `2q_ij`; application of the peer mixed-curvature identity; near-affine-parity star block payment `Delta H <= [8/(1-2e)]D`.

REFUTED: single-pair parity selector with constant `<=6.614522520220921`.

OPEN: a dimension-independent selector over arbitrary partitions/adaptive parity-line blocks; a universal bound for `H/(I-o)`; treatment of cores far from every affine parity row.

Full FEI remains OPEN / NOT PROVED.

## Joint handoff

consumed_peer_artifact: `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260921T224419Z-affine-parity-straightening/REPORT.md` (plus fleet04/B18 mixed-curvature identity).
applied_to_claim: replace repeated affine straightening plus an unpaid inflation ledger on the near-affine-parity sector by one geometry-preserving physical parity-line block with directly paid entropy decrement.
remaining_implication: prove that every high-ratio centered critical core either contains an affine-parity-approximable pivotality row with error bounded away from `1/2`, or admits another partition-line block with `Delta H=O(D)`, or else close the far-from-parity terminal sector by a different mechanism.
next_recipient: fleet01/B14 and fleet01/B18 (adaptive selector / interface-A integration), with fleet02/B17 for comparison to its affine-amortization gap.
