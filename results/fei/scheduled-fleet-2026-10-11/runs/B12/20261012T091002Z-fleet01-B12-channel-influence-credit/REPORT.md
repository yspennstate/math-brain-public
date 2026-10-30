# B12 / A057 — aggregate channel influence and collision credit

Run ID: `20261012T091002Z-fleet01-B12-channel-influence-credit`  
Primary packet: **A057 — Coherent restriction remainder**  
Attempt: `B12-A057-ATTEMPT-09`  
Stable gap: `B12-A057-COHERENT-HIERARCHY-v9`  
Status: **SUBSTANTIVE MATHEMATICAL MOVEMENT; FULL FEI OPEN**

## Outcome first

The preceding block theorem exposed `2^|B|-1` selector-frequency channels.
This run proves that their number causes **no influence loss**.  If

`C^alpha_gamma=h_alpha b_(gamma xor alpha)`, `alpha!=0`,

then, pointwise over the unqueried variables,

`sum_alpha I_B(C^alpha)=V_h I_B(b)+p_b I_B(h)-2 Overlap_B`.

The final term is an exact nonnegative collision refund.  Consequently,

`sum_alpha I_B(C^alpha) <= I_B(b)+I_B(h)`.

Summing over every node of any adaptive nonreusing physical hierarchy gives

`sum_v w_v sum_alpha I_{B_v}(C_v^alpha) <= I(b)+I(h)`.

There is no block-size, depth, bias, address-count, or `2^|B|` factor.  This
is the requested low-energy collision credit at the exact physical-hierarchy
level.

The sharp limitation is equally important.  Paying the channel entropy
decrements separately by their aggregate channel influence is already full
FEI.  For an arbitrary Boolean `k`, add a fresh bit `x` and take

`h=x`, `g_+=xk`, `g_-=-xk`.

The unique selector channel is exactly `k`; its block entropy decrement is
`H_nat(k)` and its block influence is `I(k)`.  Therefore the tempting
standalone channel inequality is not an easier bridge.  Future progress must
retain cancellation with the signed remainder/source/terminal reserve.

## Frozen objective and prior status

The previous run proved the exact arbitrary-block identity and found that
sequential and simultaneous ledgers differ by an order-dependent signed
reassociation transfer.  It left an apparent exponential family of
selector-frequency channels and proposed an aggregate KL or terminal-reserve
mechanism.

Previous tracked value: exact block algebra, but no quantitative aggregate
budget for the channels.

Bounded objective: aggregate all selector-frequency channels before applying
entropy estimates, preserve collision refunds, and determine whether a
standalone channel entropy/influence payment is genuinely simpler than FEI.

## Exact local theorem — PROVED

For a block `B`, partially Fourier-expand `h` and `b` in the block variables.
For unqueried physical state `y`, define

- `V_h=sum_{alpha!=0} h_alpha^2`;
- `J_h=sum_{alpha!=0}|alpha|h_alpha^2`;
- `p_b=sum_beta b_beta^2`;
- `J_b=sum_beta|beta|b_beta^2`;
- `Overlap=sum_{alpha!=0,beta}|alpha intersect beta|h_alpha^2b_beta^2`.

Then

`sum_alpha ||C^alpha||_2^2 = E_y[V_h p_b] <= ||b||_2^2`,

and

`sum_alpha I_B(C^alpha)=E_y[V_h J_b+p_b J_h-2 Overlap]`.

The proof is a direct use of the exact symmetric-difference identity

`|beta xor alpha|=|beta|+|alpha|-2|beta intersect alpha|`.

Because `h` is Boolean and `b` is `{0,+-1}`-valued, `V_h<=1` and `p_b<=1`.
This yields the uniform bound by `I_B(b)+I_B(h)`.

## Adaptive hierarchy theorem — PROVED

Let node `v` query a fresh physical block `B_v` and have actual reach weight
`w_v`.  Apply the exact local theorem to the restricted functions `b_v,h_v`.
For any real `f`, nonreuse implies

`sum_v w_v I_{B_v}(f_v) <= I(f)`.

This follows in physical derivative form: for each coordinate, the events
that reach nodes querying it select disjoint portions of its derivative
energy.  Applying this once to `b` and once to `h` proves the depth-uniform
channel-influence budget.

This is an actual adaptive physical hierarchy statement, not a frozen-source
or independent-block estimate.

## Exact parity-zero control

For

```text
g+ = (-1,-1, 1, 1)
g- = ( 1, 1,-1,-1)
h  = (-1,-1, 1, 1)
```

we have `b=h` equal to one character and `F` constant.  The gross channel
influence is `2`, the overlap refund is `2`, and the actual selector-channel
influence is zero.  Thus the refund exactly captures parity-zero erasure;
discarding it loses the complete cancellation.

## Universality obstruction — PROVED

For arbitrary Boolean `k(z)`, introduce fresh `x` and set

`h=x`, `g_+=xk`, `g_-=-xk`.

Then `a=0`, `b=xk`, `F=k`, and the unique nonzero selector channel is

`C^{\{x\}}=x(xk)=k`.

For the full block, its entropy decrement and influence are exactly
`H_nat(k)` and `I(k)`.  Hence a universal estimate

`sum_alpha D_B(C^alpha) <= C sum_alpha I_B(C^alpha)`

specializes to full FEI itself.  The special channel family is universal,
despite its composition notation.  This retires the plan to finish A057 by
bounding each channel, or even their unsigned aggregate, independently of
the signed remainder.

## Verification

Command:

```bash
python3 check_channel_influence_credit.py
```

All arithmetic is exact rational Walsh arithmetic.  The checker verifies:

- all `4096` genuine Boolean triples on two bits;
- `3260` triples with a strict overlap refund;
- `12` complete parity-erasure cases;
- `8192` hierarchy/order checks, with zero budget violations;
- the exact displayed parity witness;
- the universality construction for all `278` Boolean functions through
  three variables.

There is no random search and no seed.  Enumeration checks the formulas;
the all-dimension statements are proved analytically.

## Movement and remaining obstruction

The exponential channel-count concern is removed at the influence level.
The remaining obstruction is not combinatorial multiplicity but signed
entropy conversion:

> Control the combined quantity
> `sum_alpha X_{B,alpha}+R_B^sh` (and, where necessary, the source channel)
> by the exact activated collision-credit budget, without isolating the
> universal channel class.

The next bounded attempt should use the scalar entropy interference
associator

`Phi(sum_j c_j)-sum_j Phi(c_j)`

inside each block-frequency fiber.  Keep the overlap refund paired with the
signed associator and test whether the combined charge has a one-sided bound;
do not apply absolute values or FEI separately to `C^alpha`.  The new
B01/A003 KL-by-JS falsifier was also checked: coefficient-one payment of an
asymmetry KL term by ordinary restriction JS fails on a four-bit Boolean
witness and all its tensor powers.  Therefore the combined B12 associator
must retain its signed alignment term and be tested on that witness family;
it cannot be replaced by unsigned restriction JS.

## Controls and acceptance

- **Parity-zero erasure:** exact and fully refunded.
- **Activation weights:** retained as `p_b(y)` and actual node weights `w_v`.
- **Shared-variable interference:** coefficients shift by symmetric
  difference; no false product tensor rule is used.
- **Rare restrictions/addressing/depth:** the hierarchy theorem is exact and
  has no depth or address-count factor.
- **Near tensors and prime gates:** the theorem is exact for every Boolean
  pair/selector; no finite-case extrapolation is used.
- **A057-D1:** **ADVANCED** by a dimension-free aggregate influence budget.
- **A057-D2:** exact parity, activation, collision and hierarchy controls.
- **Packet complete:** **NO**; combined signed entropy payment remains open.
- **Independent review:** **PENDING**.
- **Full FEI:** **OPEN**.

## Source and execution status

The exact predecessor package is the immutable block-reassociation run
recorded in `SOURCE_PINS.md`.  No intervening canonical correction was
present at research start; the only Brain change then was inbox relay
metadata.  Before delivery, the relevant B01/A003 KL-by-JS falsifier was read
from its original proof package and incorporated as a guard on the next
associator attempt.

Observed model metadata: `gpt-5` family Codex agent; no explicit scheduler
effort selector was exposed.  Natural execution and exact local verification
are recorded.  Independent review and native Brain ingestion were not
observed.
