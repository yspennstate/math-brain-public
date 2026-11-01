# A027 stage6: sharp signed low-bias core admission

Full FEI remains OPEN. The signed activation correction is nonpositive on a sharp bias band, so safe core splits need no controller refund or additive core surcharge. A first proper core query is guaranteed safe when the parent bias is at most half the band width. The complete core and terminal payments remain explicit.

## exact target, quantifiers, hypotheses and units

For every Boolean core u and independent controller a, set p=Pr(a=-1)<=1/2, d=Pr(u=-1), F=1+((1-a)/2)(u-1). Entropy is in bits; influence counts actual physical input edges. The exact activation remainder R(p,d) is convex for 0<=d<=d_star=(1-1/sqrt(2))/2. Every actual core-only restriction tree with terminal core biases in this band obeys Pi_H(F)-p Pi_H(u)<=0. For parent d<=d_star/2, any first core coordinate has both child biases in the band; when m>=2 this is a proper block. Neither full core entropy nor arbitrary child entropy is thereby paid.

For point controls and an interleaved physical tree, impose this same child-bias condition at every active core query. Using the actual original-input projected tree U gives Pi_H(F;T)<=p Pi_H(u;U)+C0 Q_control. A supplied proper projected payment K and actual terminal allowance L yield H(F)<=max(K,C0,L)I(F), C0<6. This removes the previous additive kappa=4+12/ln(2) core surcharge in the safe band. The theorem does not produce K or L.

## sources actually read, revisions and theorem locators

Read current BOARD (opening10:35UTC snapshot), full B06 STREAM_NOTESv2, own STATUS, and full execution protocol2026-10-11-execution-v2. Read own arbitrary-controller R proof, projected interleaving proof, and prior signed-admission/unsigned-renewal result. Consulted scoped passages of A028 stage5 REPORT/DERIVATION for its signed-owner direction; its latest theorem is not independently accepted here or used as a new mathematical premise. SOURCE_READS records paths, hashes and exact scope.

The exact R identity is prior A027 version2; projected actual input weights and endpoint ledger are prior version3. A028 one-bit scalar bound at version2 was previously independently reconstructed in A027 stage3; it is retained at that existing scope. No new external source, paper claim or literature-priority assertion is made. Stream lead direction remains unchanged: prove a useful proper split, keep complete terminals and identify the universal unsupported line.

## complete derivation or exact first unsupported line

DERIVATION.md proves R_dd=(16p/ln(2))D, where D=ln(1-2d)-(1-p)ln(2d)-p ln(1-2pd)+p ln(p). Its p derivative is increasing in p and strictly negative at p=1/2 throughout d<=d_star; the proof uses d_star<1/6 and ln(2)>=2/3. Therefore D(p,d)>=D(1/2,d)=(1/2)ln((1-2d)^2/(4d(1-d)))>=0 on the band. All reciprocal-ln(2) differentiation constants cancel, including the constant -4V folded into ln(2d). Continuity closes d=0 and p=0. This is an analytic all-dimensional proof, not extrapolation from finite cases.

Bias martingale plus Jensen makes the exact endpoint correction nonpositive. The controller Hplus term cancels linearly but remains in the complete actual leaf entropies. The refund is ONE signed endpoint quantity, never a renewed positive future-control reserve. The first-query guarantee follows from child d_i<=2d. In the interleaved point setting every live core node has p_v<=1/2; exhausted controls give zero correction. Control nodes pay their own physical influence once. Summation and the exact terminal influence partition prove the conditional max(K,C0,L) allowance.

Sharpness is also proved: at p=1/2, R_dd<0 for d_star<d<1/2. Any extension of the initial band contains dyadic nested shared-core siblings giving a positive Jensen correction. The fixed actual six-bit witness has child negative probabilities3/16 and1/4; both children are nonconstant, the selector leaves four physical core coordinates, and the independent control is a dictator. Its exact signed correction is

    2 -(49/512)log2(7) -(675/256)log2(5)
      +(315/256)log2(3) +(169/256)log2(13)
      >2503282859835519/1152921504606846976 >0.

This refutes only the wider quarter-bias nonpositive-surcharge helper. It is not a failure of FEI, of the actual core ledger, or of the sharp safe band.

First unsupported universal line: for EVERY Boolean core select a proper projected tree with independently paid core decrement K and complete actual terminal allowance L, and pay any first band exit from one unused certified signed child surplus without renewing the controller bank. The safe first-query theorem supplies none of these core or terminal certificates. Rare activations still carry their encoded core difficulty.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC was saved before computations. The copied exact helper is pinned by sha256 a4e7bc617754627eefeeff73263ab12a8628fb660e16118aaa1c0e5dd3698217. The first family has all nine labeled3-bit child tables with zero or one negative input, all81 ordered sibling pairs, and16 actual controllers: counts1,3,11 on0,1,2 controller bits with p<=1/2, plus the3-bit point controller. No symmetry quotient; maximum dimension7. Two additional fixed cases reach dimension8: near-boundary nested sizes8,9 on64 shared core inputs, and the quarter-band witness sizes3,4 on16 inputs. Forty-five rational scalar curvature grid checks verify the differentiation formula and strict positive signs; p=1/3 and2/5 grid parameters are continuous scalar checks, not claimed Boolean truth-table cases.

From A027 run `python -X utf8 runs/20261014T104101Z-fleet05-A027-block-selection/code/check.py --pilot`, then the same command without --pilot. Pilot passed594 assertions over81 cases in0.041s. Full passed9,666 assertions over1,296 exhaustive cases plus two fixed certificates in0.682s. Integer Walsh transforms, Fraction edge counts and exact prime-log vectors verify actual entropy cancellation, queried influence, retained terminal influence and exact curvature algebra. Rational24-term atanh enclosures with explicit tail certify all signs. The near-boundary fixed witness is strictly negative, the beyond-band witness strictly positive.

Run `python -X utf8 runs/20261014T104101Z-fleet05-A027-block-selection/code/trees.py`. All33 five-bit core signs (constant+1 or one labeled negative input), r1,2,3 point controls, and four frozen query orders give396 actual proper physical trees, maximum dimension8. Failed controls terminate at actual constant leaves. Each policy queries only two of five core coordinates on the projected tree. The orders test core-only, control between the two cores, control before them, and complete controls before them. Passed4,356 assertions in0.450s, including local child-band eligibility, actual signed corrections, own control-node price6, complete physical influence partition, and total zero-core-surcharge transfer with actual terminal entropy retained.

Each job cap60s, estimated160MB; peak RAM unmeasured. No >300MB job expected or started, so memok gate was not triggered. No GPU, dimension escalation, background job or floating sign evidence. All pilots and jobs passed without assertion/runtime failures. These finite checks validate the analytic proof and named witnesses; they do not certify arbitrary K,L or constitute a full-cube exhaustion.

## proof dependencies and changed downstream conclusions

Version5 extends the SAME A027 partial-core candidate. All version4 and earlier components, hypotheses and refutations remain; the safe-band clause adds a signed sufficient split condition and removes surcharge only under its explicit band hypothesis. No new broad candidate is opened at the stream pending-review cap. Existing core/controller identities and control payment are consumed rather than claimed as new.

A023/A025/A028/A029/A030/A064/A078 can omit the core activation debit at eligible low-bias nodes and retain a single nonnegative endpoint refund. They must still certify the core decrement and complete child entropies. The beyond-band witness prevents extrapolating this sign to biases<=1/4 or arbitrary cores. Earlier unsigned-renewal refutation remains intact. No independent acceptance, shared-index adoption or supervisor mirror is asserted.

## one next mathematical action and independent reviewer

At the first core query whose child bias exits the sharp safe band, price the ACTUAL positive signed remainder R(parent)-average R(children) from one unused certified child surplus. Carry that single endpoint balance through the next proper split, retaining both terminal entropies and the same controller owner. Start with the saved nonconstant/nonconstant six-bit witness; do not renew unsigned rp epsilon. A087 should reconstruct the scalar curvature and actual prime-log sibling certificate independently; A094 should challenge sharpness, exhausted-control handling, and complete terminal bookkeeping. These are local source-bound handoffs, not tool-sent messages or review receipts.

## actual persistence receipts or precise save blocker

All four protocol files, exact derivation, frozen spec, code and three checked outputs are saved only in A027. STATUS is two lines; WORKLOG and LEARNED append this stage. out/PERSISTENCE_RECEIPT.json checks exact progress/claim schemas, statement sha256s, required report fields, identical PACKET_DELTA, file sizes and actual file hashes. Local persistence verified; supervisor copying, remote mirrors, independent acceptance and downstream use remain unobserved.

## Universal bridge

This stage moves C019 signed proper-core admission and C024 actual history transfer by proving a sharp zero-surcharge bias band: d<=d_star/2 guarantees any first proper core split qualifies, and band-preserving interleavings replace the prior max(K+kappa,C0,L) allowance by max(K,C0,L). The exact signed correction is now a conserved nonpositive endpoint contribution there, avoiding the previously refuted positive-bank renewal. Universal paid core decrement K, complete terminal L, and unused child funding at the first band exit remain open. NEXT prices that first positive signed exit on the saved two-nonconstant-child witness with one inherited surplus and complete terminals. It attacks the remaining universal selection/payment boundary directly rather than another isolated Boolean class or a relabeled FEI-equivalent existence condition.
