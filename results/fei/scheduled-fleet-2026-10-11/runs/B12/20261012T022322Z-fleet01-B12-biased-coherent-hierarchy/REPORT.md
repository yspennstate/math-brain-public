# B12 / A057 — biased coherent identity and adaptive hierarchy payment

Run ID: `20261012T022322Z-fleet01-B12-biased-coherent-hierarchy`  
Primary packet: `A057` (Coherent restriction remainder)  
Attempt: `B12-A057-ATTEMPT-02`  
Main claim versions: `B12-A057-ADAPTIVE-LOG-PAYMENT-v2`, `B12-A057-BIASED-REMAINDER-v1`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v2`  
Full FEI: **OPEN**

## Previous exact status

The reviewed source established the complete coherent remainder only for a balanced child. The preceding B12 run proved

`sum_i alpha_i^2 ln(1/alpha_i^2) <= (2/e) I(h)`

and hence paid the explicit singular term across one balanced disjoint layer. It did not iterate through physical restrictions because a restriction biases the child. The tracked hierarchy value was therefore one layer, with the biased mean correction and complete coherent interference unpaid.

## New mathematical movement

### 1. Adaptive nonreusing hierarchy payment — PROVED

Let a deterministic restriction tree for an arbitrary Boolean sign `h` query a fresh physical coordinate `i(v)` at each internal node `v`. Let `w_v` be the exact uniform probability of reaching the node and let `alpha_v` be the singleton coefficient of the restricted function in the queried coordinate. Then

`sum_v w_v alpha_v^2 ln(1/alpha_v^2) <= (2/e) I(h)`.

The proof is dimension-free and depth-free. The local inequality follows from `|alpha_v|<=Inf_{i(v)}(h_v)`. For each original coordinate `i`, the node cylinders that query `i` are disjoint, and

`w_v Inf_i(h_v)=Pr(reach v and i is globally pivotal)`.

Their sum is at most `Inf_i(h)`. Summing physical coordinates proves the theorem. This covers adaptive addressing trees, rare restrictions, arbitrary prime gates, and unbounded depth without paying once per level.

For a fixed outer pair on a disjoint child block, multiplication by `q=||b||_2^2` gives the exact composition payment `(2/e) q I(h)`. This advances the prior one-layer value to a complete adaptive restriction-tree value for the alpha-log envelope.

### 2. Exact biased-child coherent identity — PROVED

For `F=a+h b`, write `h=r+x_i s`, `mu=E h`, `alpha=hat h({i})`, and `q=||b||_2^2`. With

`K(x,y)=psi(x)+psi(y)-[psi(x+y)+psi(x-y)]/2`,

the exact physical split is

`D_i(F)=q D_i(h)+R_mu(alpha)`,

where

`R_mu(alpha)=Eraw(a+mu b)+Eraw(alpha b)-[Eraw(a+(mu+alpha)b)+Eraw(a+(mu-alpha)b)]/2-q K(mu,alpha)`.

The final scalar correction is precisely what is lost if a biased restriction is silently treated as balanced. At `mu=0`, the identity reduces to the complete reviewed remainder, including the explicit `q alpha^2 ln(1/alpha^2)` term and both coherent spectra.

Coefficientwise, for `t_T=a_T/b_T`,

`R_mu(alpha)=sum_{b_T != 0} b_T^2 [K(t_T+mu,alpha)-K(mu,alpha)]`.

No equality of child spectra is assumed.

### 3. Fixed-bias collision law — PROVED

Define

`Z_mu=sum_{b_T != 0, a_T+mu b_T=0} b_T^2`.

For fixed finite outer coefficient arrays and fixed `0<|mu|<1`,

`R_mu(alpha)/[alpha^2 ln(1/alpha^2)] -> -Z_mu`.

At exact balance the limit is instead `q-Z_0`. Hence fixed nonzero bias cancels every positive leading rare logarithm, while exact coherent collisions produce a negative logarithmic refund. The original balanced obstruction is preserved.

The result is nonuniform in the live hierarchy parameters. If `mu=c alpha`, then `K(mu,alpha)=alpha^2 K(c,1)`, so the positive alpha-log term can return. Near-collision gaps that shrink with `alpha` create the analogous transition. This identifies the exact remaining two-parameter obstruction rather than declaring biased restrictions harmless.

## Genuine Boolean controls

An explicit four-input Boolean outer gate has collision energy `Z_{1/2}=1/4`. Genuine Boolean children with

`E h_n=1/2`, `hat h_n({1})=-2^{2-n}`

give

`R_{1/2}(alpha_n)/[alpha_n^2 ln(1/alpha_n^2)] -> -1/4`.

The archived values through `n=14` approach the predicted refund. This is a control for the sign and collision coefficient, not an FEI counterexample.

The adaptive theorem directly survives whole-set addressing because the queried coordinate may depend on previous answers. It also preserves parity-zero erasure, exact rare-node probabilities, near tensors, and actual prime Boolean gates. No shared-input composition theorem or raw-convolution tensor law is asserted.

## Verification

`check_biased_hierarchy.py` performed three deterministic checks with no random seed:

1. `205,824` actual Boolean splice cases: all Boolean children through three variables, every physical coordinate, and every ordered pair of Boolean branches on two variables. The maximum biased split-identity residual was `4.9961e-16`; the maximum kernel-rewrite residual was `3.0532e-16`.
2. Every Boolean truth table through four variables (`65,812` functions total). Dynamic programming maximized the weighted alpha-log cost over all full adaptive nonreusing query trees. The largest observed ratio was `0.5545177444479562`, below `2/e=0.7357588823428847`.
3. The genuine biased-collision family through `n=14`, confirming approach toward the proved `-1/4` logarithmic coefficient.

These are numerical development controls. The universal statements are proved analytically in the TeX artifacts.

## Acceptance and status

- A057-D1: **PARTIAL**. The exact balanced source remainder is retained; the exact biased extension and a full adaptive sum for the singular envelope are proved. A uniform bound for the complete coherent interference is still missing.
- A057-D2: **SUBSTANTIALLY ADVANCED**. Balanced, biased, zero, collision, rare-event, adaptive-tree, addressing, overlap, tensor, and prime-gate regimes are recorded.
- Complete source remainder and consistent nats: **MET**.
- Mandatory logarithmic counterexample retained: **MET**.
- Nonreusing sum across an actual adaptive physical hierarchy: **MET for the alpha-log envelope**.
- Complete packet criterion: **NOT MET**, because the entire `R_mu(alpha)` sum with changing coherent activation remains unpaid.

The run adds proved components to A057 but is not routed as a third complete unreviewed packet candidate. The two existing complete B12 candidates remain A058-v2 and A060-v2.

## Exact remaining obstruction

Stable gap `B12-A057-COHERENT-HIERARCHY-v2` is:

> Prove a dimension-free upper bound for the weighted sum of the complete `R_mu(alpha)` over a physical hierarchy when `mu/alpha` and `(a_T+mu b_T)/(alpha b_T)` may vary with the node, and when the activation witness may change coherently with the same restricted variables.

The adaptive alpha-log envelope is now paid. The unpaid term is the uniform transition between separated coefficients, near collisions, and near-balanced nodes.

## Failed or insufficient mechanisms

- Reapplying the balanced formula after restriction is invalid; the exact `-qK(mu,alpha)` mean correction is necessary.
- Fixed-bias Taylor expansion is not uniform when `mu=O(alpha)`.
- A collision refund at fixed coefficients does not by itself pay changing near-collision coefficients along a hierarchy.
- Paying a constant per depth level is unnecessary for the alpha-log term and would introduce a false depth factor.

## Next concrete action

Partition every coefficient at a node into the near-collision region

`|a_T+mu b_T| <= c |alpha b_T|`

and its separated complement. Derive a signed exact bound on the near region from the kernel formula, and a uniform second-order Taylor bound on the separated region. Then sum the resulting `alpha^2 ln(1/alpha^2)` envelope with the adaptive pivotal-event theorem proved here. Test the frozen inequality on the balanced AND2/parity control, the `Z_{1/2}=1/4` refund family, majority3, and whole-set addressing before any hierarchy claim.

## Review, delivery, and configuration

Contributor proof and deterministic self-check only. No independent A090/A091 reconstruction is observed; any material repair contributor must recuse. Full FEI remains open.

The exposed runtime supplied no model selector or reasoning-effort telemetry, so no GPT-6 or maximum-reasoning claim is made. No worker, scheduler change, protected evaluation source, held reroute, public publication, live-store mutation, native ingestion, merge, deployment, email, or paid resource was used.

The complete canonical artifact set was saved and read back nonempty with exact expected Git blob identities at open-problems commit `95e438b0915a65d55223af9fe671b423bf42b66d`; `PROGRESS.json` and `PACKET_DELTA.json` were byte-identical. Brain mirroring and its readback are recorded separately after the canonical pointer is available. File delivery does not imply review or native ingestion.

