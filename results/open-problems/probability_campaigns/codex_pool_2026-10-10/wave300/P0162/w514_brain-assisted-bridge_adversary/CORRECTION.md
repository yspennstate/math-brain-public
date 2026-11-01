Proposed correction to a recall-cited card, 2026-10-10. Pending w515's mathematical check and Claude reviewer approval for a theorem-hypothesis correction. This is a source/assumption correction, not a new record claim.

Target: claim_dc05672a84f74b44a1f15207c0cf86e0 in the read-only math-brain store. Its transported assumption says: "h the binary entropy function; delta the restricted coordinate's bias".

The cited source memory fei_step_constant_lower_bound_ceiling_and_descent_witness_2026_09_21.md instead defines the ceiling parameter explicitly: "delta = max_i Inf_i". Its definition of rho_0 is the minimum over relevant coordinates of Delta_i/Inf_i.

Replace that ambiguous assumption with: f is a nonconstant Boolean function under uniform cube measure; h=h_2 is base-2 binary entropy; delta=max_i I_i(f)>0; rho_0(f)=min_{i:I_i(f)>0}Delta_i(f)/I_i(f), where Delta_i is the Fourier entropy increment under coordinate restriction. Do not change the card's unrelated numerical/public-record assertions or upgrade its verification status.

The correctly parameterized inequality is rho_0(f)<=(1+h_2(delta))/delta. To prove it, use the paired-spectrum identity Delta_i=JS_2(P,Q)+B_i. Jensen-Shannon divergence of two probability laws with equal mixing weights is <=1 bit, and B_i<=h_2(I_i). Choose a coordinate achieving maximal influence delta and then use the minimum defining rho_0. Nonconstancy removes the zero denominator.

Concrete obstruction to reading delta as an input-coordinate bias: take AND on three uniform sign bits, output +1 only at the all-positive input. Every coordinate has influence 1/4. Its Fourier law has one atom of weight 9/16 and seven of weight 1/16. Thus H=-(9/16)log_2(9/16)+7/4. Each coordinate restriction is AND_2 or a constant, with average entropy 1, giving

rho_0=3+(9/4)log_2(16/9)=4.867668746754797.

Uniform input-coordinate bias is 1/2, which would give the false ceiling (1+h_2(1/2))/(1/2)=4. With the source's actual delta=1/4, the ceiling is 7.245112497836532 and is valid. The strict failure can be proved without decimals: 16/9>sqrt(2), so rho_0>3+9/8>4. The independent direct Walsh/edge check is in adversary_checks.json.

NEXT: approve the explicit source parameter and positive-denominator premise, then append the corrected assumptions through the coordinator's canonical process while preserving the card's provisional status.
