# A066 / B14 — restriction-compatible heat dissipation

## exact target, quantifiers, hypotheses and units

For every Boolean sign f on a finite uniform cube, retain K(f)=integral_0^infinity J_f(t)dt=(H_nat(f)-b(f))/2, with b(f)=p_empty ln(1/p_empty). All new charges use natural logarithms; divide entropy by ln(2) for bits. B14 lead v2 requests an exact physical-block heat drop and comparison with C006 on majority and point-defected addressing, explicitly accounting for level mass.

**Outcome:** an exact positive physical-restriction ledger is proved, with its singleton channel and level charges paid uniformly by queried influence. The remaining nonempty-context conditional erasure has exactly the same optimal universal constant as C018's full erasure. Majority and point-defected addressing are computed analytically and checked exactly in frozen finite domains. No universal residual payment or full FEI proof is supplied.

## sources actually read, revisions and theorem locators

At stage start I read BOARD.md, snapshot 2026-10-11 23:29 UTC; B14 STREAM_NOTES.md v2 dated 23:25 UTC; and my STATUS.md/LEARNED.md. The lead has independently reconstructed the first-stage heat identity and envelope obstruction. A067's `REVIEW_A066.md` and its report were read: ACCEPT_AT_STATED_SCOPE with a distinct analytic reconstruction, no repair or coauthorship. A088's report also records independent acceptance of both original A066 claims; central adoption is not inferred from those local reviews.

The lead specifically directs A066 to the restriction-compatible calculation, rather than another pointwise heat envelope. A067 is assigned the padding-strip payment and C019 arithmetic leaves; this stage supplies the heat/channel/level ledger rather than repeating its U analysis. The board's other results reinforce that terminal arbitrary-core entropy and physical influence must remain visible.

The current protocol's required field sets were reloaded (`2026-10-11-execution-v2`). The first-stage A066 heat identity v1 is the explicit mathematical dependency. The recovered source `BLOCK_RESTRICTION_IDENTITY_2026-09-18.md` was read in full, especially §§1–3, equations (4), (5), (10). C006's rows and C005's singleton channel bound are independently re-derived here. The B14 lead's point-defect-neutralization claim and A067's next-action/report scope were read as guards, not premises. No threshold, percolation or unreviewed full-FEI theorem is imported. `out/SOURCE_RECEIPTS.json` records current source bytes/hashes and read scope; no full-paper audit is claimed in this stage.

## complete derivation or exact first unsupported line

The complete proofs are saved in `DERIVATION.md`. For a physical block B, residual spectral index T, and assignment y, let p_y(T)=hat(f_y)(T)^2 and q_T=E_y p_y(T)=sum_{U subset B}p_{U union T}. Define

M_T=sum_U p_{U union T}ln(q_T/p_{U union T}),
C_T=E_y p_y(T)ln(p_y(T)/q_T).

The usual C006 entropy decrement is M_B+C_B, summing all rows. Remove the empty residual row to obtain M_B^+, C_B^+, and set ell_B=sum_{nonempty U subset B}p_U ln(1/p_U). The exact new heat identity is

2[K(f)-E_y K(f_y)]=M_B^+ + C_B^+ + ell_B.

All three terms are nonnegative, so K decreases in expectation under every physical restriction. This accounts for the constant-mode boundary exactly: ell_B is the information in Fourier coefficients supported wholly inside the erased block, which become constants in the children.

For B={i}, the channel is at most 2 Inf_i(f) nats. Booleanity gives |hat(f)({i})|<=Inf_i(f), hence ell_{ {i} }<= (2/e)Inf_i(f). Both charges are paid using the same queried coordinate; in a stopping tree their cumulative cost is at most (2+2/e)[I(f)-E I(leaf)]. Terminal K and the endpoint constant-mode entropy remain explicit.

Let R_nat(f)=sum_i M_i^+(f). Then 0<=B_nat(f)-R_nat(f)<=(1+2/e)I(f). More decisively, for every arbitrary Boolean core g and m>=1, F_m=y product_j g(x^(j)) satisfies R_nat(F_m)=m B_nat(g) and I(F_m)=mI(g)+1. Therefore a universal R_nat<=A I implies universal B_nat<=A I with the same constant. The optimal uniform constants for the two erasure quantities are equal. C018 consequently gives FEI in bits with constant (A+2)/ln2. No easier universal class has been introduced by deleting the empty row.

**First unsupported line:** there is a finite universal A with R_nat(f)<=A I(f) for every Boolean f, or a specified physical stopping tree with a summably paid M_i^+ residual and separately paid terminal entropy. This run pays the channel and singleton level terms, not that retained erasure residual.

For odd majority n=2m+1, alpha=binom(2m,m)/2^(2m), singleton channel and erasure are both zero, while K(parent)-E K(child)=alpha^2 ln(1/alpha^2)/2. Its ratio to queried influence is alpha ln(1/alpha)<=1/e. Thus a channel-only heat payment is false already at Maj_3. This does not pay the entropy preserved in its children.

For padded, point-defected Addr_a, equations (9)–(11) give exact three-class spectra and all padding-block charges for every a>=1, r>=1 and 1<=b<=r. For fixed a,b with r increasing, M_B/I_B and C_B/I_B both tend to 2ln2, while the heat-drop ratio tends to 2ln2. For the full padding block b=r, with k=a+2^a and rho=4^a/2^k, the respective limits are 2(1+rho)ln2 and 2(1-rho)ln2; the heat ratio remains 2ln2. The level bill has a nonzero full-block limit 4ln2/2^k per influence. These limits are proved analytically, not inferred from samples. Refining the block into singleton queries pays its level charges but retains the M_i^+ tree debt.

## executed validation with domain, arithmetic, commands and outputs

Both specifications were written before their jobs: `FROZEN_SPEC.json` and `EMBEDDING_SPEC.json`. Commands from the A066 folder:

```text
python -X utf8 runs\20261011T233317Z-fleet05-A066-semigroup-dissipation\code\check_restrictions.py pilot
python -X utf8 runs\20261011T233317Z-fleet05-A066-semigroup-dissipation\code\check_restrictions.py full
python -X utf8 runs\20261011T233317Z-fleet05-A066-semigroup-dissipation\code\check_embedding.py
```

Pilot: PASS, 796 assertions, 0.0234 seconds. Full restriction run: PASS, 29,463 assertions, 15.4155 seconds. It checks all 1,844 Boolean function/nonempty-block pairs in dimensions 1–3; 24 majority/block-size cases for n=3,5,7,9; 20 direct point-defected addressing cases (a=1,2; padding r=1..4; all padding block sizes); and 33 closed-histogram cases (a=1,2,3; r=1,2,4,8,16,32; b=1 or r). The largest directly enumerated truth table has 1,024 entries. Histogram cases use three coefficient classes regardless of ambient dimension, not hidden truth tables or a dimension escalation.

Integer Walsh transforms and Fraction probabilities verify the actual physical children, Fourier marginals, both heat-drop identities, the influence telescope, channel upper bounds, level upper bounds and the addressing histograms. Entropy expressions are exact formal sums of logarithms of rational arguments. Signs and displayed tables use rational atanh-series intervals with 24 terms, power-of-two range reduction, and the explicit remainder 2 z^49/[49(1-z^2)]. Exported interval endpoints are rounded outward to the dyadic grid 2^-80. Midpoint floats are labeled display only; no numerical quadrature or floating sign is a certificate.

The initial full run encountered Python's integer-to-string digit limit while exporting huge exact interval denominators. `out/FULL_INITIAL_SAVE_FAILURE.md` preserves the failure. Only output serialization was repaired; the domain, log helper and inequalities were unchanged, and the full run was rerun successfully. The successful output, not the interrupted one, supplies the assertions above.

`out/EMBEDDING_CHECK.json` separately checks all 278 Boolean base functions in dimensions 0–3 with one fresh character and five selected two-copy cores, using exact formal entropy identities: PASS, 1,698 assertions in 1.5951 seconds. The all-m limit and equality of optimal constants are analytic proofs. Jobs are below the 300 MB threshold; no GPU, window, background job or shared-tree mutation was used. Each frozen job has a 60-second guard.

## proof dependencies and changed downstream conclusions

The heat identity `A066-HEAT-ENTROPY-IDENTITY` v1 is consumed with source-bound independent A067/A088 review receipts. The new claims use only that identity and the elementary physical Fourier-row calculation, convexity, Boolean derivative values, the influence telescope, and the exact addressing coefficients. C005/C006/C018 are reconstructed where needed; no unreviewed campaign theorem is an essential proof premise.

The newly specified channel-only helper is refuted by Maj_3, but no existing accepted campaign claim is marked false. A064/B06 can consume the positive heat-row stopping ledger with terminal K retained. A067 can use it to distinguish stripped level mass from nonempty-context erasure when evaluating arithmetic leaves. A070/A088/A094 should audit the empty-row cancellation, the indispensable Boolean step |hat(f)({i})|<=Inf_i, and the arbitrary-core character/tensor admission. On a non-Boolean uniform singleton spectrum R_nat=0 while the singleton level bill/influence is ln n, so the paid-level step is essential.

## one next mathematical action and independent reviewer

Bound the retained nonempty-context erasure R_nat using full signed Boolean identities, with any proposed bound first checked against F_m=y g^m for arbitrary Boolean g. Use the saved positive row telescope to locate each claimed influence payment; preserve the terminal core. A088 is the proposed independent reviewer, with A094 as challenger and A070 for the analytic scope audit. This targets the remaining universal C018 debt instead of another majority/addressing constant.

## actual persistence receipts or precise save blocker

The four protocol files, derivation, frozen specifications, code and outputs are saved only in this A066 run; STATUS.md, WORKLOG.md and LEARNED.md are updated only in the A066 workspace. `out/SCHEMA_CHECK.json` checks exact protocol field sets, report fields and PACKET_DELTA compatibility; `out/PERSISTENCE.json` records local sizes and SHA256 receipts. Supervisor copying, central registry adoption, new independent review and mirror verification are pending; none is inferred from local saves. No artifact exceeds 20 MB.

**Universal bridge:** This stage moves C018 erasure payment and its C019 stopping-tree interface by isolating and uniformly paying the singleton level charge at 2/e nats per queried influence, together with the 2-nat channel charge, and proving an exact positive telescope that retains leaf entropy. The remaining nonempty-context erasure is not hidden in a heat integral: its optimal universal constant equals C018's original constant by the arbitrary-core character/tensor admission. No universal constant has improved. NEXT attacks that exact retained residual with full Boolean structure and a mandatory arbitrary-core check, which is the shortest surviving route here to full FEI rather than another isolated class theorem.
