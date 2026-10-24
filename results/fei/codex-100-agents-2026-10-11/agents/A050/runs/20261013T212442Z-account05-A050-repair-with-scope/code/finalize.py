from pathlib import Path
import hashlib,json,datetime

R=Path(__file__).resolve().parents[1]; A=R.parents[1]; TEAM=A.parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
check=json.loads((R/'out'/'CHECK.json').read_text(encoding='utf-8'))
assert check['status']=='PASS'
report=r'''# exact target, quantifiers, hypotheses and units

A050/B10 stage 2 follows STREAM_NOTES v2: consume the sharp singleton tax on essential coordinates and state precisely what C019/C018 uses survive and what must be supplied by C024 path entropy. All entropies are bits. The physical input law is a fixed finite independent product law with interior probabilities; every node is an actual Boolean restriction under its inherited law. Physical influence I_phys is the sum of unweighted pivotal probabilities and differs from biased spectral expected set size. Full FEI remains OPEN.

The existing scalar potential is tau*(p)=h2(p)-min_t[h2(sin^2 t)+h2(sin^2(t-beta))], sin^2 beta=min(p,1-p). The actual identity for p>1/2 first swaps children. For each finite deterministic singleton physical stopping tree, write Pi for its whole stopped transcript and Y=f(X) for the actual output. At node v define c_v=H(X_i|Y,history=v) and w_v its physical reach weight. The new scoped repair is

    sum_v w_v [tau*(p_i)-c_v/2]_+ <= I(Pi;Y)/2 <= I_phys(f)/2,
    sum_v w_v tau*(p_i) <= I_phys(f)/2 + H(Pi|Y)/2.        (A)

The required extra resource is the declared output-conditional transcript bank H(Pi|Y)/2, supplied at most once. We prove the refund coefficient 1/2 is the smallest sufficient coefficient in the explicitly tested family of bounds A_T<=C I_phys+lambda H(Pi|f), with finite C and nonnegative lambda, uniformly over all product-biased Boolean functions and essential computing trees. This is not a globally weakest structural repair or proof that a spectral reference supplies the bank. That compatibility line is left explicit.

The lead's desired root-block restatement on essential coordinates is: J_A<=M_A+sum_{i in A_eff}tau*(p_i), hence L_A<=2M_A+that sum. Its singleton version and dummy contraction are reconstructed; its full block version remains CONDITIONAL on optimal product-basis uncertainty additivity. We do not promote the cited-but-unchecked block theorem to acceptance. Sequential actual singleton reveals have their own M_v, J_v and inherited biases; the valid tree statement is (A) plus the exact terminal-inclusive residual below.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor snapshot 2026-10-13 21:24 UTC; own STATUS/LEARNED and earlier A050 REPORT; B10 STREAM_NOTES v2, 2026-10-11 23:31Z; execution protocol revision 2026-10-11-execution-v2 in full. Unlike stage 1, the lead notes now exist. Followed its scoped-consumption and C024 direction. Lead notes are older than A048's stage-2 result; that newer obstruction prevents restarting the failed essential-bit scalar tax payment mechanism.

Read full lead run REPORT/CLAIMS, 20261011T230400Z-claude-B10-onebit-half-tax: Theorem 1/angular reduction and conditional Claim 2; read A046 stage-2 CLAIMS for the child-swap and exact linear-coefficient corrections. A046 does not accept the middle-region/full block chain, so no such premise is silently adopted. Our necessary upper bound tau*<=h2(p)/2 has a complete elementary proof and avoids that pending certificate. The source's rounded -0.2787p+o(p) expression is not used as an exact asymptotic coefficient.

Read A048 REPORT/CLAIMS stage 20261012T013822Z, sections 2-4: essential tax no-go, actual uncertainty defect, collapsed-mask versus physical-input scope. Read A057 REPORT stage 20261012T003930Z for its paid cap and retained inner/core entropy; A100 REPORT stage 20261011T231552Z for the distinct positive-uniform-tax no-go; A091 REPORT stage 20261011T234101Z for accepted B09 core and exact corrected-entropy/deficit ledger; A037 REPORT stage 20261011T220010Z for the common posterior-space and coherent physical spectral lift; A064 REPORT stage 20261011T224431Z for reserve signs and the minority-output candidate failure. Read A047 LEARNED and stage-2 CLAIMS for sharp real versus finite Boolean scope. Relevant canonical stream dispatch was inspected. Earlier required campaign/paper readings remain those accurately recorded in stage 1; no new external paper theorem or novelty/priority claim is used. SOURCE_MANIFEST.json pins actual inspected bytes and states inspection scope.

# complete derivation or exact first unsupported line

PROOF.md gives the complete derivation, including every boundary/conditioning convention. Its critical steps are summarized here.

**Scalar bound.** For the two bases defining the angular tax, pick each larger-probability basis vector. Their rank-one projectors sum to an operator with maximum eigenvalue at most 1+sqrt(1-r), r=min(p,1-p). If u,w are the two smaller probabilities, then u+w>=delta=1-sqrt(1-r). Binary entropy monotonicity/concavity imply h2(u)+h2(w)>=h2(delta)>=h2(r/2)>=h2(r)/2. Thus 0<=tau*(p)<=h2(p)/2 for all biases, without any interval coverage or multi-bit additivity premise. At the symmetric angle t=beta/2, tau*>=h2(p)-2h2((1-sqrt(1-p))/2), giving tau*/h2(p)->1/2 at the rare endpoint. At uniform bias tau*(1/2)=0 exactly, by h2(x)>=4x(1-x) and the complementary sin/cos identity.

**Local bank drift and terminal balance.** Let j_v=I(X_i;Y|history=v)=h2(p_i)-c_v and ell_v=h2(p_i)/2-tau*(p_i)>=0. Exactly

    tau*(p_i)-c_v/2=j_v/2-ell_v.

The nonnegative reserve R_v=H(Y|history=v)/2 has drift j_v/2. Its complete-tree release is I(Pi;Y)/2, retaining E H(Y|Pi)/2 at stopping leaves. Therefore the positive part of each net tax is paid on one conserved account; the account is not reopened at each depth. The finite transcript chain rule also gives sum w c_v=H(Pi|Y), so this proves both inequalities in (A). It applies to partial and adaptive deterministic trees and respects every zero-probability/constant endpoint.

**Root payment.** H(Y)=I(Y;X)=sum_i I(Y;X_i|X_<i). Add later coordinates to the first mutual-information argument and use input independence: each term is at most I(Y;X_i|X_-i)=H(Y|X_-i)=h2(p_i)Inf_i^phys(f). Thus H(Y)<=sum_i h2(p_i)Inf_i^phys<=I_phys. This pays only the output-information release and proves (A) without FEI. Biased spectral energy is not substituted for physical influence.

**Sharpness of the declared extra-bank coefficient.** If lambda<1/2, choose a fixed rare bias q with tau*(q)>lambda h2(q). In the essential short-circuit computing tree of the r-bit q-biased point defect,

    A_T=tau*(q)(1-q^r)/(1-q),
    H(Pi|f)=h2(q)(1-q^r)/(1-q)-h2(q^r),
    I_phys=r q^(r-1).

Then A_T-lambda H(Pi|f) tends to a positive constant while I_phys tends to zero, so no finite C works. Lambda=1/2 works by (A). The failure without a refund and the point-defect tree are existing A048 results, credited rather than presented as new FEI counterexamples; the new result is the all-tree positive-part repair and the exact minimal bank coefficient.

**Terminal-inclusive C019 substitution.** For the actual child pair define M_v=H(queried Fourier label|remaining Fourier labels), J_v=physical-child/spectral mutual information, and D_v=tau*(p_i)-(J_v-M_v)>=0. All are under the actual inherited product basis. Let M_T=sum w M_v and S_T=sum w(ell_v+D_v). Then, exactly,

    H_hat(f)=E H_hat(f_leaf)+2M_T+H(Pi|Y)/2
                                    +I(Pi;Y)/2-S_T.          (B)

Only I(Pi;Y)/2 is paid by (A). What remains is the signed complete quantity 2M_T+H(Pi|Y)/2-S_T+E H_hat(f_leaf). The sum ell+D equals h2(p_i)/2-(J_v-M_v), so the residual can be computed exactly without optimizing tau*. At physical uniform biases tau*=0 and ell=h2(1/2)/2=1/2; the matching transcript term cancels exactly. No positive logical-mask tax is smuggled into a fair physical coordinate. C018's actual erasure remains unpaid; its identity is not replaced by output entropy.

**Compatibility control.** Reconstruct A037's fair coherent lift by selecting physical b with kernel childhat_b(T)^2/(2q_T) and retaining T, the remaining root-spectral labels. Boolean child Parseval gives fair physical branches and actual child spectra, and the kernel's dependence only on T gives I(S0;Pi)=sum w J_v. On a complete computing tree attach actual Y as its transcript-measurable output. Then

    H(Pi|Y)-H(Pi|S0)=I(S0;Pi)-I(Y;Pi).

Neither conditional entropy universally dominates the other. The fair one-bit character has difference -1. The two-bit bent AND under its forward essential computing tree has difference 1-h2(1/4)>0. This demonstrates the exact side-information mismatch. The output-conditional refund is not automatically the spectral-witness refund. A common-space reference needs to supply it, with its channel/reset corrections, once.

**Essential contraction and operations.** An ignored revealed coordinate has deterministic empty spectral label and independent physical outcome, so deleting it preserves M_A,J_A and lowers any assigned nonnegative tax. Essential contraction remains valid but alone cannot pay the scalar tax (A048). The current refund even gives nonpositive net tax at an irrelevant node because c_v=h2(p_i). Adaptive tree cuts retain the remaining output reserve and the conditional-transcript suffix entropy, with no double release. On overlapping events sharing a physical control, (A) applies to the single actual tree and queries that control once; it supplies the tax component's ownership only. Independent factorwise versions may use separate independent factor outputs and banks. A common factor remains in the actual full output and terminal Fourier entropy; replacing that output or treating its entropy as paid is not authorized. Logical masks need an explicit conversion to original physical controls. Root-block sharp additivity, arbitrary reused-selector composition, all-node OI heredity and a universal spectral residual payment are not proved.

**First unsupported line:** a normalized compatible C024 reference supplies H(Pi|Y)/2 as an actual single-use refund with the correct spectral side conditioning and all channel/reset corrections, and the signed residual in (B) plus terminal Fourier entropy is bounded by the remaining exclusive influence budget. The result does not prove that line, and terminal output entropy cannot pay terminal Fourier entropy.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before any calculation. Domain: all 278 Boolean truth tables through n=3 including n=0, under four fixed product laws truncated to n; 1,112 roots and 4,448 physical trees. Policies: forward essential computing, reverse essential computing, maximum-physical-influence computing, and forward depth-one stopping. Two fixed fair compatibility controls, eight closed point-defect formulas, three scalar midpoint lower bounds k=2,8,128, and one four-variable underrefund certificate were frozen explicitly. No symmetry quotient, random sampling, dimension increase, tau* optimizer, GPU or heavy job. Estimated memory 100 MB; no >300 MB job was planned, and no memory-gated job was started. Pilot cap 60 seconds and main watchdog 120 seconds.

Commands from A050:

    python -X utf8 runs/20261013T212442Z-account05-A050-repair-with-scope/code/check.py --pilot
    python -X utf8 runs/20261013T212442Z-account05-A050-repair-with-scope/code/check.py

Pilot PASS: 32 roots, 128 trees, 1,234 exact assertions, 0.02174 seconds. Final main PASS: 1,112 roots, 4,448 trees, 2,414 distinct queried states, 64,104 exact assertions, 21.68369 seconds. out/CHECK.json holds counts and exact certificates. Direct weighted Boolean tables give physical output probabilities and influences; centered rational Fourier moments divided by exact basis norms give actual biased squared spectra. Each node's child marginal, decrement and physical influence telescope are exact; entropy identities cancel rational coefficients of prime logarithms. Leaf probability/output joints independently reconstruct transcript entropy and its conditional bank, including partial leaves. No independence of prime logarithms is presumed. The all-dimensional claims follow from PROOF.md, not the finite domain.

The two compatibility differences are exactly -1 and -1+(3/4)log2(3); the latter is strictly positive by rational outward intervals. The fixed underrefund witness uses q=1-((2^128-1)/2^128)^2, lambda=49/100, and a four-variable q-biased point defect. A symmetric-angle lower bound on tau*, not a numerical minimizer, rigorously certifies A_T-lambda H(Pi|f)>I_phys. Interval endpoints are stored after exact outward rounding to a 2^-1024 grid. The general impossibility of lambda<1/2 is analytic, not an extrapolation from that one witness.

An initial strict certificate was unresolved because dyadic range reduction of a near-one mass subtracted unrelated ln2 intervals; it supplied no PASS. Reciprocal reduction log(x)=-log(1/x) for x in [1/2,1) resolved the same frozen witness. A second execution passed its mathematical sign but hit Python's decimal integer-string cap while serializing huge fractions. Exact outward dyadic rounding compacted the output without changing any sign computation. out/INITIAL_CERTIFICATE_FAILURE.md records both events. Rational logs use 32 atanh terms and tail 2z^65/[65(1-z^2)], sign-correct endpoint multiplication and all four positive-denominator division corners. No tolerance, floating sign, precision escalation or domain change was used.

# proof dependencies and changed downstream conclusions

The new scoped repair has a self-contained proof: angular projectors/concavity, physical product independence, finite transcript chain rules, direct Boolean output fibers and the explicit midpoint tax lower bound. A096/A090's prior projector mechanism, A037's lift and A048's point-defect mechanism are credited and reconstructed at the needed interfaces. No unaccepted half-Delta certificate, block-additivity theorem, FEI bound, or arbitrary reference compatibility is assumed. Sharp real versus Boolean gaps are context only.

Changed downstream conclusion: the literal per-bit sharp tax can be consumed with exactly a half-output-conditional-history bank, after which the positive net tax is bounded universally by half physical influence. Essential contraction alone still fails. C024 consumers must declare and provide the correct side-conditioned bank; C019 consumers have the exact residual (B), not a paid 2M or terminal term. C018 at uniform physical bias receives no new erasure constant because its tax is already zero. B10's pending cap is respected by one bundled scoped repair of the existing failed payment, not a new broad FEI candidate. Original OI repair and all prior author files remain unchanged.

# one next mathematical action and independent reviewer

NEXT: on the actual priority two-core activation with one shared physical control, place the output-conditional bank and the prescribed spectral witness on one coherent lifted tree. Compute the signed bank conversion H(Pi|Y)-H(Pi|witness,required side information) and reference-reset/channel correction together, assigning each shared control once and retaining both terminal core Fourier entropies. This is the first unfunded line exposed by (A)-(B), rather than another scalar-tax constant search. A092 primary reviewer, A087 alternate; A085 should challenge side conditioning and interval robustness. Consumers A037/A039/A057/A064/A073/A091/A095 and B10/B20. No message was sent.

# actual persistence receipts or precise save blocker

All writes stay inside A050. Saved REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, PROOF.md, SCOPED_REPAIR.tex, REPAIR_APPLICATIONS.md, FROZEN_SPEC.json, SOURCE_MANIFEST.json, code/check.py, code/finalize.py, pilot/main exact outputs, failure record and out/PERSISTENCE.json. Rolling STATUS is exactly two lines; WORKLOG and LEARNED are appended with this stage. Finalizer checks protocol key sets (normalizing only the explanatory suffix on packet_ids), exact statement hashes, progress-copy identity, passed check counts and the 20 MB artifact limit, and saves readback hashes. No git, Brain write, foreign-folder mutation, shared-ledger update, message, delete or remote publication occurred. Independent review, supervisor copying, remote mirror verification and downstream mathematical use remain pending. No local save blocker remains.

Universal bridge: This stage advances C024 history transfer and its C019 consumption rule by proving that precisely half of the output-conditional transcript entropy suffices to refund the existing sharp scalar tax, after which its positive remainder costs at most half physical influence; the half-bank coefficient is necessary in the tested all-product-law bank family. The exact C019 identity retains the signed uncertainty defect, scalar slack, all conditional erasure and terminal Fourier entropy. What remains is compatibility/funding of that bank on the actual spectral-reference space and influence payment of the signed erasure/terminal residual; no universal FEI constant improves. NEXT targets their joint conversion on a shared-control two-core tree, the shortest route because another isolated tax or function-class bound cannot supply this missing common-space credit.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
statement='For every finite Boolean sign f under an independent interior product law and every finite deterministic physical singleton stopping tree, let Pi be its full transcript, Y=f(X), w_v the physical node probabilities, c_v=H(X_i|Y,history=v), and tau*(p)=h2(p)-min_t[h2(sin^2 t)+h2(sin^2(t-beta))] with sin^2 beta=min(p,1-p). Then sum_v w_v[tau*(p_i)-c_v/2]_+<=I(Pi;Y)/2<=I_phys(f)/2 and sum_v w_v tau*(p_i)<=I_phys(f)/2+H(Pi|Y)/2. In the ordered family of uniform bounds A_T<=C I_phys(f)+lambda H(Pi|f), with finite fixed C and nonnegative lambda, the smallest coefficient over all product-biased Boolean functions and essential computing trees is lambda=1/2. The exact terminal-inclusive Fourier ledger is Hhat(f)=E Hhat(f_leaf)+2 sum_v w_v M_v+H(Pi|Y)/2+I(Pi;Y)/2-sum_v w_v[h2(p_i)/2-(J_v-M_v)]. Funding the output-conditional bank on a compatible spectral reference and paying the remaining erasure/terminal residual are not established.'
claim={'claim_id':'A050-OUTPUT-CONDITIONAL-TAX-REPAIR','version':1,'exact_statement':statement,'hypotheses':['Actual Boolean sign and fixed independent interior product input law','Finite deterministic physical singleton stopping tree; inherited probabilities; no coordinate query repeated along a path','Transcript includes chosen coordinates and stopping information; choices determined by recorded history','Physical pivotal influence distinguished from biased spectral energy','Refund conditioning is on actual physical output; availability as a spectral-reference credit is an explicit unpaid hypothesis'],'statement_sha256':sha(statement.encode()),'contributors':['A050'],'proof_source':{'run_id':R.name,'files':['PROOF.md','REPORT.md','code/check.py','out/CHECK.json']},'proof_dependencies':[],'review_records':[],'status':'SCOPED_REPAIR_AUTHOR_PROVED_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'A normalized compatible reference supplies the output-conditional transcript bank once with correct spectral side conditioning/channel resets, and pays the signed erasure residual plus all terminal Fourier entropy.','next_consumers':['A092','A087','A085','A037','A039','A057','A064','A073','A091','A095','B10','B20']}
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B10','packet_id':'A050','gap_id':'G-BIASED-TAX','attempt_id':'A050-output-conditional-bank-v1','method':'Actual output-information drift, elementary half-entropy angular bound, sharp conditional transcript bank coefficient, exact terminal-inclusive spectral residual','mathematical_delta':'Universal positive net-tax payment <=I_phys/2 after half-output-conditional transcript refund; refund coefficient 1/2 sharp in tested bank family; spectral side-conditioning mismatch certified in both directions','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_BANK_REPAIR_PROVED_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':['A050-OUTPUT-CONDITIONAL-TAX-REPAIR/v1'],'source_artifacts':['REPORT.md','PROOF.md','SCOPED_REPAIR.tex','REPAIR_APPLICATIONS.md','code/check.py','out/CHECK.json'],'next_consumers':claim['next_consumers'],'next_action':'On a shared-control priority two-core activation, compute bank conversion plus reference channel/reset corrections on one coherent tree with both terminal core Fourier entropies retained.','stagnant_substantive_attempts':0,'blockers':['Output-conditional bank is not proved available under required spectral side conditioning','Sharp root-block tax remains conditional on optimal product-basis uncertainty additivity','Independent review and supervisor mirror pending'],'packet_ids':['A050']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:(R/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
(R/'SCOPED_REPAIR.tex').write_text(r'''\documentclass{article}
\usepackage{amsmath,amssymb}
\begin{document}
\section*{A050: sharp output-conditional history repair}
For the scalar angular tax $\tau(p)$, the two-basis projector estimate gives
$u+w\ge1-\sqrt{1-r}$, where $r=\min(p,1-p)$. Thus
$h_2(u)+h_2(w)\ge h_2(1-\sqrt{1-r})\ge h_2(r)/2$,
so $0\le\tau(p)\le h_2(p)/2$.
Let $Y=f(X)$ and let $\Pi$ be a finite deterministic physical transcript.
At node $v$, put $c_v=H(X_i\mid Y,v)$ and
$j_v=I(X_i;Y\mid v)=h_2(p_i)-c_v$.
Then
\[
 [\tau(p_i)-c_v/2]_+\le j_v/2,
 \quad \sum_vw_vj_v=I(\Pi;Y).
\]
Since independence and Boolean fibers give
$H(Y)\le\sum_i h_2(p_i)\operatorname{Inf}_i^{\rm phys}(f)
\le I_{\rm phys}(f)$, it follows that
\[
 \sum_v w_v[\tau(p_i)-c_v/2]_+\le I_{\rm phys}(f)/2,
 \qquad A_{\mathcal T}\le I_{\rm phys}(f)/2+H(\Pi\mid Y)/2.
\]
The coefficient $1/2$ of the declared history bank is necessary:
$\tau(q)/h_2(q)\to1/2$ as $q\to0$, while on $r$-bit $q$-biased point
defects the transcript has expected query count $(1-q^r)/(1-q)$ and
$I_{\rm phys}=rq^{r-1}\to0$.
The exact remaining Fourier bill is
\[
H_{\widehat f}=\mathbb E H_{\widehat {f_{\rm leaf}}}
+2\sum_vw_vM_v+\tfrac12H(\Pi\mid Y)+\tfrac12I(\Pi;Y)
-\sum_vw_v\bigl[\tfrac12h_2(p_i)-(J_v-M_v)\bigr].
\]
This preserves terminal Fourier entropy. Availability of the output-conditional
refund on a spectral reference and payment of the remaining signed bill are open.
\end{document}
''',encoding='utf-8')
(R/'REPAIR_APPLICATIONS.md').write_text('''The repaired resource is a half-output-conditional transcript bank, not a new FEI hypothesis about all child Fourier spectra.

| Interface / intended application | What survives | What remains |
|---|---|---|
| Actual singleton B09 uncertainty | J-M<=tau*, essential contraction valid | M and terminal entropy unpaid |
| Essential physical product trees | Positive net tax after declared refund <=I_phys/2 | Refund funding under required side conditioning |
| Adaptive/partial stopping | Same output-information account, retained terminal output entropy | Retained terminal Fourier entropy |
| Shared-control overlapping activations | One actual tree queries shared control once; tax account has no reuse | Joint spectral/reference bank conversion |
| Disjoint factor processing | Apply theorem globally, or declare separate independent factor banks | Global output conditioning is not automatically factorwise additive |
| Common unrevealed Boolean factor | Theorem applies to the full actual output | Entire common-factor Fourier entropy stays terminal |
| Collapsed logical masks | Only after declaring that logical product experiment | Convert to original physical control influence |
| Physical uniform cube / C018 | tau*(1/2)=0; no scalar tax | True conditional spectral erasure remains FEI-strength |
| Root physical blocks | Original B09 core accepted; sharp sum tau* conditional | Optimal uncertainty additivity not accepted here |
| Earlier OI child-magnitude repair | Remains proved at its stated nodewise scope | Arbitrary data restrictions may break OI |

Ordered bank family: A_T<=C I_phys+lambda H(transcript|output), C finite, lambda>=0. All lambda<1/2 fail; lambda=1/2 works with C=1/2; larger lambda work. This is the weakest coefficient in that declared family, not a globally weakest repair. The physical output bank cannot be replaced by a Fourier-set-conditional witness bank without computing their signed conversion. Neither orientation of their ordering holds universally.
''',encoding='utf-8')
paths=[TEAM/'BOARD.md',TEAM/'claude'/'B10'/'STREAM_NOTES.md',A/'STATUS.md',A/'LEARNED.md',R/'FROZEN_SPEC.json']
canonical=Path(r'~\mop_fei100\reports\fei-2026-10-11')
paths.extend(canonical/x for x in ['EXECUTION_PROTOCOL.json','STREAM_NEXT_ACTIONS.json'])
lead=TEAM/'claude'/'B10'/'runs'/'20261011T230400Z-claude-B10-onebit-half-tax'
paths.extend(lead/x for x in ['REPORT.md','CLAIMS.json'])
source_runs={'A046':'20261011T232847Z-account05-A046-current-candidate-intake','A048':'20261012T013822Z-account05-A048-tensor-stress','A057':'20261012T003930Z-account05-A057-coherent-restriction-remainder','A100':'20261011T231552Z-account05-A100-release-and-continuation-ledger','A091':'20261011T234101Z-account05-A091-composition-referee','A037':'20261011T220010Z-account05-A037-conditional-credit-ledger','A064':'20261011T224431Z-account05-A064-global-debt-potential','A047':'20261012T003641Z-account05-A047-boundary-search'}
for agent,run in source_runs.items():
    names=['CLAIMS.json'] if agent in ['A046','A047'] else ['REPORT.md']
    if agent=='A048':names.append('CLAIMS.json')
    paths.extend(TEAM/'agents'/agent/'runs'/run/x for x in names)
paths.extend(TEAM/'agents'/agent/'LEARNED.md' for agent in ['A047','A064','A037','A039'])
paths.append(A/'runs'/'20261011T230000Z-account05-A050-repair-with-scope'/'REPORT.md')
manifest=[{'path':str(p),'sha256':sha(p.read_bytes()),'scope':'Read/inspection scope specified in REPORT; byte receipt is not proof acceptance'} for p in paths if p.is_file()]
(R/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A050 stage2 proved sharp half-output-conditional transcript refund: net tax<=I_phys/2; 64,104 exact checks PASS; review pending; full FEI OPEN.\nNEXT: A092/A087 review; convert output-history bank to one spectral reference on a shared-control two-core tree with terminal Fourier entropy retained.\n',encoding='utf-8')
date='2026-10-13T21:24:42Z stage (completed local 2026-10-14 environment)'
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+date+': Read updated board/B10 lead and newer A048 no-go; changed from already advanced OI/sparse-bent case to lead-requested C024 path-bank consumption. Proved tau*<=h2(p)/2 directly, paid positive net tax after c_v/2 refund by one output reserve and I_phys/2, and proved refund coefficient 1/2 necessary. Exact terminal Fourier ledger keeps M, uncertainty defect and output/witness bank mismatch; two controls show both conditioning orders. 1112 roots, 4448 physical trees, 64104 assertions PASS, 21.684s. Initial near-one interval enclosure unresolved; reciprocal reduction fixed it. Large-fraction serialization compacted by exact outward dyadic rounding. Full FEI and bank compatibility open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+date+': For a physical product-law singleton tree, Y=f(X), c_v=H(X_i|Y,v), tau*=angular sharp tax: 0<=tau*<=h2(p)/2, sum w[tau*-c_v/2]_+<=I(transcript;Y)/2<=I_phys/2. Output reserve R_v=H(Y|v)/2 has drift half output information; terminal output reserve stays. Scalar bank coefficient 1/2 is necessary over all biased point-defect computing trees. Exact spectral residual: Hhat=E Hhatleaf+2M_tree+H(transcript|Y)/2+I(transcript;Y)/2-sum w[h2(p)/2-(J-M)]. Correct output-conditioning is not root-Fourier conditioning: fair character gives bank difference -1, fair bent AND gives 1-h2(1/4)>0. No free side-condition conversion. Near-one logs should invert before dyadic range reduction to avoid subtracting ln2 intervals. Outward dyadic rounding safely compacts huge rational endpoints.\n')
protocol=json.loads((canonical/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert sha(claim['exact_statement'].encode())==claim['statement_sha256']
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert check['roots']==1112 and check['trees']==4448 and check['assertions']==64104
assert all(p.stat().st_size<20_000_000 for p in R.rglob('*') if p.is_file())
receipts={str(p.relative_to(R)):sha(p.read_bytes()) for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json'}
rolling={p.name:sha(p.read_bytes()) for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']}
(R/'out'/'PERSISTENCE.json').write_text(json.dumps({'status':'PASS','schema_keys_checked':True,'packet_ids_annotation_normalized':True,'progress_copy_identical':True,'all_artifacts_under_20MB':True,'local_only':True,'remote_mirror':'NOT_VERIFIED','independent_review':'PENDING','run_receipts':receipts,'rolling_receipts':rolling},indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','run_files':len(receipts),'claims':1,'exact_assertions':check['assertions'],'full_fei':'OPEN'}))
