# B12 / A057 — exact fixed-activation Doob bridge

**Run:** `20261013T121918Z-account01-B12-fixed-activation-doob`  
**Primary packet:** A057 (Coherent restriction remainder)  
**Attempt:** `A057-FIXED-ACTIVATION-DOOB-18`  
**Stable gap:** `B12-A057-COHERENT-HIERARCHY-v18`  
**Status:** fixed-activation bridge and arbitrary-source selector payment PROVED by contributor; full FEI OPEN.

## Previous exact status

The alpha-log envelope was paid on every adaptive nonreusing physical tree, but the complete biased remainder

`R_mu(alpha)=sum_T b_T^2[K(a_T/b_T+mu,alpha)-K(mu,alpha)]`

was not. A later cylinder family refuted any bound for repeatedly charging a static positive associator, and the previous run repaired that auxiliary charge by replacing it with an event-local Doob decrement. The missing bridge was to identify whether the genuine `R_mu(alpha)` itself is event-local and to isolate what remains when activation changes.

## New mathematical movement

### 1. Exact fixed-activation Doob identity — PROVED

For a fixed disjoint outer pair `a,b`, `a±b` Boolean, put `q=||b||_2^2` and

`J_{a,b}(g)=Eraw(a+g b)-q Eraw(g)`.

At every queried physical coordinate of a Boolean child `g`, the exact biased remainder is

`R_mu(alpha)=J(g)-[J(g_+)+J(g_-)]/2`.

This is an exact identity, not an estimate. It follows by subtracting the two physical split decrements in the proved kernel identity. Therefore `R_mu(alpha)` already vanishes on unchanged dummy cylinders and its weighted sum telescopes on every complete adaptive restriction tree:

`sum_v w_v R_v = J(h)-Pr[h=1] Eraw(a+b)-Pr[h=-1] Eraw(a-b)`.

The identity is simultaneous over all values of `mu/alpha` and every coherent collision ratio. In the fixed-activation regime, the planned near/separated coefficient split is unnecessary.

### 2. Arbitrary Boolean source at the one-bit selector interface — PROVED

Take a fresh selector bit `x`, an arbitrary Boolean indicator `s`, `h=2s-1`, and

`a=(1+x)/2`, `b=(1-x)/2`, `F=a+h b`, `p=E s`.

Both terminal branches have zero entropy (`a+b=1`, `a-b=x`). Direct Fourier calculation reduces the entire hierarchy sum to the scalar endpoint law

`sum_v w_v R_v = Q(p)`

with

`Q(p)=psi(p)+psi(1-p)-psi(2p-1)/2+4p(1-p) ln 2`.

It obeys

`Q(p) <= 8 p ln 2`.

If `d=((1-x)/2)s` is the activated source, then `I(d)=I(s)/2+p/4`, so

`sum_v w_v R_v <= 32 ln 2 I(d)` in nats, equivalently constant `32` in bits.

This pays the **complete** biased coherent remainder—not just the alpha-log envelope—for an arbitrary genuine Boolean source and an arbitrary adaptive complete physical tree, uniformly in dimension, bias, depth, address count, and collision gap. The source may be an addressing function, a rare indicator, a near tensor, or a prime Boolean gate.

## Why this matters

The previous event-local theorem was restricted to a three-parallel-coset associator. The new bridge acts directly on the exact `R_mu(alpha)` and the selector corollary allows every Boolean source. It shows that changing bias and near-collision behavior are not themselves the universal obstruction when the activation pair is fixed. The surviving term is now sharply localized: if `(a_v,b_v)` changes between nodes, telescoping acquires the inter-node drift of `J_{a_v,b_v}(h_v)`.

The public fresh-selector composition endpoint remains established and is not being re-proposed as open. The new contribution is the exact identification and payment of the campaign's biased coherent remainder across the physical hierarchy in this fixed-activation subcase.

## Verification

`check_selector_doob.py` used no randomness and checked:

- all 65,814 Boolean truth tables through four variables;
- 262,948 local kernel-remainder/Doob-decrement identities;
- 1,646 complete ordered-tree telescopes, including every query order through three variables and selected four-variable controls;
- the exact scalar selector formula for every truth table through four variables;
- the analytic envelope on a deterministic grid of 999,999 interior values of `p`.

Maximum residuals were `4.927e-16` locally and `4.441e-16` for complete trees. The largest dense-grid ratio `Q/(8p ln2)` was `0.609040133972938`. These computations corroborate the all-dimensional proof in `FIXED_ACTIVATION_DOOB_BRIDGE.tex`; they are not finite-to-infinite evidence.

## Mandatory controls

- **Dummy cylinders:** local remainder is exactly zero because it is a Doob decrement.
- **Parity-zero erasure:** `alpha=0` is handled by the exact identity; no division by `alpha` occurs.
- **Rare restrictions:** exact reach weights telescope, and `Q(p)=O(p)`.
- **Whole-set addressing/adaptivity:** the proof permits any query coordinate selected from the entire previous transcript.
- **Near tensors and prime gates:** the source `s` is arbitrary.
- **Changing bias/collision gaps:** no fixed-bias Taylor estimate is used.
- **Shared variables:** no overlapping-input claim is made.
- **Activation equivalence:** the conclusion is stated only for one fixed outer pair.

## Exact remaining universal gap

Stable gap `B12-A057-COHERENT-HIERARCHY-v18` is now:

> Control the inter-node activation drift created when `(a_v,b_v)` changes coherently with the restricted physical state, or prove that a canonical global representation keeps one fixed defect potential. The payment must use one source-influence/terminal-reserve budget and survive overlap and activation equivalence.

Equivalently, add and subtract the child potentials in the variable-activation sum. The fixed-pair Doob pieces telescope by the present theorem; only mismatch terms

`J_{a_v,b_v}(h_child)-J_{a_child,b_child}(h_child)`

remain. Those mismatch terms, not the `mu=O(alpha)` transition by itself, are the next unpaid object.

## Acceptance and review

- A057 exact complete-remainder formula: **advanced to a full adaptive-tree theorem for fixed activation**.
- Uniform bias/collision transition: **paid for the arbitrary-source selector interface**.
- General changing activation/overlap: **OPEN**.
- Independent review: **not yet observed**; route to A091, with A090 as the second suggested reviewer.
- Full FEI: **OPEN**. No full proof or counterfamily is claimed.

## Next concrete action

Freeze a two-state activation-change model and write its exact mismatch term coefficientwise. Test whether the mismatch is a signed relative-entropy/Bregman divergence plus the already paid alpha-log envelope. First controls: an unchanged dummy cylinder (must give zero), the balanced AND2/parity splice, the fixed-bias `Z_{1/2}=1/4` collision family, and one reused-selector overlap witness.

## Configuration and delivery

Contributor proof and deterministic self-check only. No independent acceptance, native ingestion, merge, deployment, scheduler edit, new worker, protected source, held reroute, public release, email, or paid resource was used. The exposed runtime did not provide model or reasoning-effort telemetry, so no such claim is made. Delivery/readback is recorded separately and does not imply mathematical review.

