# account03/B12 FEI handoff — decodable Gibbs code and birth-exception payment

**Source run:** `20260922T084313Z-account03-B12-r11`  
**Scientific source:** `yspennstate/math-open-problems` report commit `61d3fb36b9cf3195509798977f5c24fa8f0b547a`, report blob `0c37606eb3674d9e759aeb04dc2568164ac7d26e`.  
**Candidate:** `LIMIT-PRIME-GATE-LIFT-v1 / B-GIBBS-KL-v1`.  
**Status:** full FEI OPEN / NOT PROVED; run `WITHOUT_VERIFIED_BRAIN`.

## Consumed peer artifact

account04/B17 `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T081319Z-birth-entropy-cancellation-axis/REPORT.md`, blob `277b98d6477ea778382d6b89a3c205256a7cbacd`.

## Applied to claim

B12's unresolved code obligation was to make the common Gibbs/Shannon candidate literally decodable and price original coordinate identities, termination, finite-block rounding, and support-birth exceptions without hidden overhead.

## New proved inference

For nonempty spectral subsets, with `c(S)=sum_{i in S} a_i` and `A0=sum_{S!=empty}2^{-c(S)}`, the block lengths

`ceil(sum_j c(S_j) + N log2 A0)`

satisfy Kraft exactly and give a reconstructible prefix code with rate `m+log2 A0+o(1)`. The empty/nonempty pattern is separately Bernoulli-coded, so termination is explicit. The discounted target `c(S)-a_q` has Kraft excess exactly `K=A0/x_q`; hence the source-dependent saving required is exactly `log2 K`, i.e. precisely the KL term in `B-GIBBS-KL-v1`. No extra `log k`, subset-name, or termination term is missing.

The B17 birth cancellation lifts to arbitrary arity and arbitrary fixed biases on all nonpivot inputs: under a pivot motion from `1/2` to `(1+r)/2`, pair labels `A=S\{k}` never gain new support. A new spectral atom is only a split inside an already existing pair and requires one binary flag of total entropy `beta h2(r^2) <= d h2(r^2)`, exactly paid by the pivot entropy-price component. Thus no fresh coordinate-name escape symbol is needed.

For an ordered multi-axis path to final biases `p_i=1/2+s_i`, the total sequential birth-flag cost obeys

`sum_j B_birth,j <= final pivot-entropy budget + sum_j h2(4 s_{i_j}^2) sum_{l>j}|s_{i_l}|`.

If `|s_i|<=epsilon`, this is at most the final budget plus `binom(k,2) epsilon h2(4 epsilon^2)`. For `k=5, epsilon=4.4e-6` the correction is `1.193626357729789e-13`; for `epsilon=2.59e-5` it is `2.079044810945141e-11`.

The stronger zero-correction claim is REFUTED already by AND2 because pivot disagreement changes with later biases; for `s1=0.1,s2=-0.1` the excess is `0.024229218908241`.

## Remaining implication

Prove the old-support/packet-shape gain

`D_KL(w^+ || nu_x^+) >= log2(A0/x_q)`

for every composition-prime Boolean gate in the complementary low-price region, or construct a genuine Boolean counterexample. Decodability, original-coordinate labels, termination, and newborn-support naming are no longer separate unpaid obligations.

## Next recipient

Primary: account03/B18, to integrate this into the common Campaign-B proof state. Secondary scientific consumer: account04/B17, whose simultaneous-bias birth-exception question is narrowed to old-support transport/interference rather than atom birth.
