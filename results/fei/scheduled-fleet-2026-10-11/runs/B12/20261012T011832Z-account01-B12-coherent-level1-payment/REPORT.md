# B12 / A057 — first-layer payment for the coherent alpha-log term

Run ID: `20261012T011832Z-account01-B12-coherent-level1-payment`  
Primary packet: `A057` (Coherent restriction remainder)  
Attempt: `B12-A057-ATTEMPT-01`  
Claim version: `B12-A057-LEVEL1-LOG-PAYMENT-v1`  
Stable remaining gap: `B12-A057-COHERENT-HIERARCHY`  
Full FEI: **OPEN**

## Exact prior status

The reviewed source supplied, in natural units, the complete balanced disjoint-composition identity

`D_i(F)=q D_i(h_j)+R(alpha)`,

where

`R(alpha)=q alpha^2 log(1/alpha^2)+Eraw(a)+alpha^2 Eraw(b)-[Eraw(a+alpha b)+Eraw(a-alpha b)]/2`.

It also proved `R>=0` and supplied an actual Boolean control with

`R(alpha)=(alpha^2/2)log(1/alpha^2)+(3/2)alpha^2+O(alpha^4)`

for arbitrarily small nonzero `alpha` at leaf influence one. Therefore the previous tracked value was: no pointwise finite `C` can make `R<=C q alpha^2`, and no globally summable payment for the mandatory logarithmic term had been recorded. The complete physical hierarchy remained open because a restriction biases the child.

## New result

**PROVED (`B12-A057-LEVEL1-LOG-PAYMENT-v1`).** For every genuine Boolean sign `h` (balanced or not),

`sum_i hat h({i})^2 log(1/hat h({i})^2) <= (2/e) I(h)`

in nats. The proof is elementary but targets the exact obstruction: on every physical edge,

`|hat h({i})| <= Inf_i(h)`,

and `u^2 log(1/u^2) <= (2/e)u`.

Consequently, for a balanced disjoint substitution `F=g(h_1,...,h_m)`, the complete sum of the explicit singular pieces over the first nonreusing physical layer obeys

`sum_{j,i} q_j alpha_{j,i}^2 log(1/alpha_{j,i}^2) <= (2/e) I(F)`.

In bits the coefficient is `2/(e ln 2)<1.062`. This is a genuine movement from an unpayable pointwise `O(alpha^2)` estimate to a dimension-free simultaneous physical-coordinate payment that retains the logarithm.

The result uses neither a selector increment nor an existentially chosen spectral coordinate. It applies to all physical coordinates at once, including prime Boolean children. The outer activation probability is exactly the same `q_j` appearing in `Inf_i(F)=q_j Inf_i(h_j)`.

## Exact cancellation structure

With `psi(t)=t^2 log(1/t^2)`, the full remainder is

`R(alpha)=sum_T [psi(a_T)+psi(alpha b_T)-(psi(a_T+alpha b_T)+psi(a_T-alpha b_T))/2]`.

This yields exact zero remainder when `alpha=0`, when `q=0`, or when `a_T b_T=0` coefficientwise for every `T`. The last condition is neighboring Fourier-support orthogonality; ordinary vector orthogonality alone is insufficient.

## What remains open

The run does **not** bound the remaining coherent term

`C(alpha)=Eraw(a)+alpha^2 Eraw(b)-[Eraw(a+alpha b)+Eraw(a-alpha b)]/2`

after summing coordinates. It also does not iterate the balanced identity down a restriction hierarchy, because the restricted child may be biased. Therefore:

- claim `B12-A057-LEVEL1-LOG-PAYMENT-v1`: **PROVED**, contributor proof complete;
- packet A057: **OPEN / PARTIAL_MATHEMATICAL_MOVEMENT**;
- stable gap `B12-A057-COHERENT-HIERARCHY`: **OPEN**;
- full FEI: **OPEN**.

No third complete unreviewed packet candidate was opened. This is a scoped partial theorem under the stream's two-candidate review cap.

## Mandatory controls

- The reviewed AND2/adjacent-parity family is preserved and defeats every pointwise `R<=Cq alpha^2` replacement.
- Parity-zero coefficients contribute exactly zero.
- Rare logarithms are retained explicitly and paid by physical pivotality.
- No claim is made for shared physical inputs, so `OVERLAP_PRODUCT` is not crossed.
- No raw-convolution tensor additivity is used, so `RAW_CONV_TENSOR` is not crossed.
- Addressing and fresh-selector closure are not invoked; this is not a re-proposal of the already proved selector-energy endpoint.
- Biased restriction synergy is named as the exact remaining obstruction rather than silently assuming restriction closure.

## Computation

`check_level1_payment.py` exhaustively enumerated all balanced Boolean truth tables through four variables: 2, 6, 70, and 12,870 cases. Walsh coefficients and influences were exact rationals; only logs used float64. The largest observed `L/I` was `ln 2`, below `2/e`. Command and complete output are archived in `check_level1_payment.out`. This finite audit is only a control; the all-dimension statement is proved on the page.

## Acceptance accounting

- A057-D1: partial. The complete source remainder is imported with both `Eraw(a±alpha b)` terms, and its explicit logarithmic component has a proved nonreusing first-layer payment. The remaining coherent component and hierarchy are unpaid.
- A057-D2: partial. Small-alpha, zero, orthogonality, parity-zero, restriction, shared-input, and activation controls are recorded.
- Criterion 1: met for the source identity and units.
- Criterion 2: met; the logarithmic counterexample is retained and passed.
- Criterion 3: met only at the explicitly scoped one-layer theorem alternative, not at the requested full physical hierarchy. Packet remains open because the deliverable asks for the complete coherent remainder payment, not merely its singular component.

## Review and routing

Contributor/self-check only. No independent review is observed. Suggested reviewers remain A091 and A090, with recusal required for any material repair contributor. Next consumers after review are A058, A059, A091, and A097. This report itself is not acceptance evidence.

## Concrete next action

Derive the biased-child analogue of the edge identity with the child mean carried explicitly. Freeze the candidate telescoping quantity before calculation: the unpaid coherent sum plus the binary entropy released when a physical restriction changes the child mean. Test it first on the reviewed AND2/adjacent-parity family and on a three-bit majority child, then on whole-set addressing. A successful identity must reduce to the present `(2/e)I` payment for the explicit alpha-log term without assuming equal child spectra.

## Configuration and provenance

Natural execution in the exposed Codex work runtime; no model or reasoning selector was exposed to this run, so no claim of GPT-6 or maximum reasoning is made. No worker was launched. No protected evaluation source, held reroute, live graph/store, scheduler, email, or public publication action was used. Immutable source details are in `SOURCE_PINS.md`.

## Delivery state

The complete canonical artifact set was saved and read back nonempty with exact expected Git blob identities at open-problems commit `bc346f6b454cde99acd5adda152553ba17f0d015`. The Brain mirror is recorded separately after its canonical pointer is available. No independent review or native Brain ingestion is inferred from file delivery.

