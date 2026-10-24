# B12 / A057 — uniform kernel envelope and fixed-source hierarchy payment

Run ID: `20261012T032618Z-account01-B12-uniform-kernel-envelope`  
Primary packet: `A057` (Coherent restriction remainder)  
Attempt: `B12-A057-ATTEMPT-03`  
Main claim versions: `B12-A057-SCALAR-KERNEL-ENVELOPE-v1`, `B12-A057-NEAR-SEPARATED-SPLIT-v1`, `B12-A057-FIXED-SOURCE-COMPLETE-PAYMENT-v1`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v3`  
Full FEI: **OPEN**

## Frozen objective and previous value

The current B12 owner target asks for a payment of the complete biased coherent remainder

`R_mu(alpha)=sum_{b_T!=0} b_T^2[K(a_T/b_T+mu,alpha)-K(mu,alpha)]`

through an actual adaptive physical hierarchy, uniformly as `mu/alpha` and coherent collision ratios vary. The prescribed move was to split

`|a_T+mu b_T| <= c |alpha b_T|`

from its complement and retain a signed near-collision refund.

Before this run, the exact biased identity and the dimension-free adaptive estimate

`sum_v w_v alpha_v^2 ln(1/alpha_v^2) <= (2/e) I(h)`

were proved. The rest of `R_mu` had no uniform transition bound. Fixed nonzero-bias Taylor expansions were known to fail uniformly when `mu=O(alpha)` or when a collision gap was `O(alpha b_T)`.

## New mathematical movement

### 1. Scalar transition envelope — PROVED

The exact homogeneity

`K(lambda x,lambda y)=lambda^2 K(x,y)`

reduces the two-parameter transition to the one-variable even kernel `k(r)=K(r,1)`. For every real `r`, this run proves

`2 ln(1+|r|)-1 <= k(r) <= 2 ln(1+|r|)+3`,

and proves that `k` is nonnegative and increasing on `[0,infinity)`. Hence, for all real `r,s`,

`k(r)-k(s) <= 4+2 ln(1+|r-s|)`.

The proof is analytic. It writes `k` as a centered second difference of `x^2 ln x`, uses a triangular-kernel integral away from zero, and treats the compact transition interval by monotonicity. No fixed-bias expansion and no separation parameter occur.

### 2. Owner-requested near/separated split — PROVED

Put `beta=|alpha|`,

`r_T=(a_T+mu b_T)/(beta b_T)`, `s=mu/beta`.

For the near set `N_c={T:|a_T+mu b_T|<=c beta |b_T|}`, the exact signed bound is

`R_N <= beta^2 sum_{T in N_c} b_T^2 [k(c)-k(|mu|/beta)]`.

Thus the whole near region is nonpositive whenever `|mu|>=c beta`; the fixed-bias collision refund is retained rather than discarded.

For every separated coefficient—and in fact for every nonzero `b_T`—the uniform bound is

`k(r_T)-k(s) <= 4+2 ln(1+|a_T|/(beta|b_T|))`.

This bound is uniform in `mu/alpha`, the collision gap and `c`.

### 3. Complete one-node remainder envelope — PROVED

Define the reverse collision reserve

`M(a,b)=2 sum_{b_T!=0} b_T^2 ln_+(|a_T|/|b_T|)`.

Because `a+b` and `a-b` are Boolean, `|a_T|,|b_T|<=1`, and therefore

`0<=M(a,b)<=E_raw(b)`.

The complete biased remainder obeys

`R_mu(alpha) <= q psi(alpha)+(4+2 ln 2)q alpha^2+M(a,b)alpha^2`,

where `q=sum b_T^2` and `psi(alpha)=alpha^2 ln(1/alpha^2)`. This is a uniform all-node statement, not an asymptotic expansion.

### 4. Depth-free complete payment for a new class — PROVED

Hold one genuine Boolean outer pair `a±b` fixed and run any adaptive nonreusing physical restriction tree inside an arbitrary disjoint Boolean child `h`. Then

`sum_v w_v R_{mu_v}(alpha_v)`

`<= [M(a,b)+(4+2 ln 2+2/e)q] I(h)`.

The numerical part of the constant outside the reserve is

`4+2 ln 2+2/e = 6.122053243462775...` nats.

Consequently, every all-dimensional family of outer Boolean pairs satisfying `M(a,b)<=Lq` has a complete coherent-remainder constant

`L+4+2 ln 2+2/e`,

independent of child dimension, depth, bias, address count, collision separation and adaptive query order. This strictly extends the previous result: the previous theorem paid only the explicit alpha-log envelope, while this theorem pays the entire `R_mu` for the fixed-source class.

## Why the result matters and what it does not prove

The simultaneous near-balance/near-collision transition is no longer the obstruction for a fixed outer pair. Its exact cost is reduced to one static reverse collision reserve `M(a,b)`. This covers arbitrary Boolean children, rare-switch chains, unbounded-depth adaptive addressing, and actual prime outer gates whenever `M/q` is uniformly bounded.

The theorem does **not** prove full FEI. In the universal hierarchy the outer witness `(a_v,b_v)` can itself change coherently with the restricted variables. Applying the fixed-source estimate separately at every node would recharge the reserve. The precise remaining quantity is

`sum_v w_v alpha_v^2 M(a_v,b_v)`.

It must be paid once by source influence or a terminal reserve, or canceled by a sharper use of the negative near-region term. The normalized reserve `M/q` is not proved universally bounded; arbitrary-spectrum activation embeddings explain why such a bound cannot be assumed.

## Mandatory controls

- **Balanced AND/parity and alpha-log**: the envelope retains one full `q psi(alpha)` term and treats `alpha=0` exactly.
- **Fixed `mu=1/2` collision refund**: the signed near bound remains negative; the genuine `Z_{1/2}=1/4` family was checked through `n=16`.
- **`mu` proportional to `alpha`**: exact homogeneity handles this regime without a nonuniform Taylor constant.
- **Rare-switch chains and whole-set addressing**: the hierarchy theorem uses exact node weights and physical-coordinate pivotal-event packing, not a depth sum.
- **Actual prime Boolean gates**: every ordered pair of Boolean two-variable branches was tested against every Boolean child/coordinate through three variables.
- **Near tensors and shared variables**: no raw convolution tensor law or overlapping-input closure is asserted. The proved theorem is for a disjoint child block and a fixed outer pair.

## Verification

`check_uniform_kernel.py` is deterministic and used no random seed. It checked:

1. `1,121` 70-digit scalar mesh points over magnitudes through `10^15`, including both envelope inequalities and monotonicity.
2. `15,876` deterministic cross-scale scalar pairs for the difference inequality.
3. `205,824` genuine Boolean splice cases: every ordered pair of Boolean branches on two variables and every Boolean child/coordinate through three variables.
4. The genuine fixed-bias collision-refund family for `n=4,...,16`.

All checks passed. The minimum finite Boolean slack was zero because of equality/zero cases. These are numerical controls; the all-real scalar lemma and all-dimensional hierarchy theorem are proved in `UNIFORM_KERNEL_PAYMENT.tex`.

## Acceptance and status

- A057-D1: **SUBSTANTIALLY ADVANCED**. The complete fixed-source coherent remainder is now summed over an arbitrary adaptive nonreusing physical hierarchy. The changing-source reserve remains unpaid.
- A057-D2: **MET for the frozen transition target**. Balanced, biased, exact collision, `mu=O(alpha)`, near-collision, parity, rare-chain, addressing and prime-gate regimes are retained.
- Complete source remainder and consistent nats: **MET**.
- Mandatory logarithmic obstruction: **MET**; no `O(alpha^2)` replacement was made.
- Nonreusing hierarchy: **MET for the new fixed-source/M-bounded class**.
- Packet A057: **OPEN**, because an arbitrary changing outer witness is not covered.
- Full FEI: **OPEN**.

## Failed or insufficient mechanisms

- Fixed-bias Taylor expansion was replaced by exact scale reduction; it was not uniform in the live transition.
- Dropping the near-region sign loses the collision refund and is too coarse for the changing-witness problem.
- Bounding `M(a,b)` by `E_raw(b)` is valid but not a universal influence payment; normalized derivative entropy can encode arbitrary hard spectra.
- Reapplying the fixed-source theorem nodewise when `(a_v,b_v)` changes would spend the same source/terminal reserve multiple times.

## Next concrete action

Use `M(a_v,b_v)` as a martingale reverse-collision potential. Attempt a one-use telescope for

`sum_v w_v alpha_v^2 M(a_v,b_v)`

against the source gate's physical influence plus terminal derivative entropy, retaining the signed refund

`alpha_v^2 sum_{near} b_{v,T}^2[k(c)-k(|mu_v|/|alpha_v|)]`.

If that telescope fails, construct a genuine Boolean changing-witness family that certifies the failure of this exact reserve payment; do not infer an FEI counterexample from failure of the helper.

## Review, delivery and configuration

This is a contributor proof with deterministic self-check. No independent A090/A091 reconstruction is observed; review remains pending. The result is routed to A058, A059, A091, A097 and B20 as a partial A057 advance, not as a third complete unreviewed packet candidate.

The runtime identifies the assistant as Codex based on GPT-5 but exposes no model selector or reasoning-effort telemetry. No claim of GPT-6, maximum effort, or an hour of execution is made. No worker, scheduler edit, public release, email, paid resource, protected evaluation source, held reroute, live-store mutation, native ingestion, merge or deployment was used.

