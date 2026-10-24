from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]; HOME=ROOT.parent.parent
BASE=HOME.parent.parent
SOURCE=BASE/'agents'/'A050'/'runs'/'20261013T212442Z-account05-A050-repair-with-scope'
def dump(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
claim=json.loads((SOURCE/'CLAIMS.json').read_text(encoding='utf-8-sig'))[0]
digest=hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
canonical_digest=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert digest==claim['statement_sha256']
claim['review_records'].append({'reviewer':'A046','decision':'INDEPENDENTLY_ACCEPTED_AT_EXACT_STATED_SCOPE','statement_sha256':digest,'source_run':ROOT.name,'proof':'REPORT.md sections 1,3; distinct direct probability-table and coherent-joint implementation code/check.py','validation':'out/CHECK.json: 22694 exact assertions PASS','conflict':'No substantive repair supplied; original statement and hypotheses unchanged','scope':'Refund and coefficient optimality accepted; universal compatible-reference funding remains explicitly unproved'})
claim['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_REVIEW_RECORD'
dump(ROOT/'CLAIMS.json',[claim])
report=r'''# exact target, quantifiers, hypotheses and units

A046/B10 stage 3 independently reviews **A050-OUTPUT-CONDITIONAL-TAX-REPAIR v1**, statement SHA256 c675ec8f6765d38276e2e143c666d2c290adc03c6d427880e378b8951946ab50. The unchanged scoped claim is accepted by this review; shared-registry adoption is not observed. Full FEI remains OPEN.

Freeze the live reserve R_v=H(Y|history=v)/2 on a finite deterministic physical singleton stopping tree for an actual Boolean sign f under any independent interior product law. Each path queries a physical coordinate at most once; its inherited bias is p_i. Pi includes query identities, outcomes and deterministic stopping; Y=f(X). Write w_v for reach probability, c_v=H(X_i|Y,v), j_v=I(X_i;Y|v), and tau*(p)=h2(p)-min_t[h2(sin^2 t)+h2(sin^2(t-beta))], sin^2 beta=min(p,1-p), with the physical children swapped for p>1/2. All entropy is bits. I_phys is unweighted pivotal influence, not biased spectral expected set size.

The exact claim is sum_v w_v[tau*(p_i)-c_v/2]_+ <= I(Pi;Y)/2 <= I_phys(f)/2, and sum_v w_v tau*(p_i) <= I_phys/2+H(Pi|Y)/2. Over all such functions and essential computing trees, the smallest lambda allowing A_T<=C I_phys+lambda H(Pi|f) for fixed finite C is 1/2. No compatible spectral-reference refund or full FEI theorem is claimed.

# sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 read in full; its exact field contract is used. BOARD.md read at stage start and refreshed at supervisor snapshot 2026-10-13 21:55 UTC; B10 lead STREAM_NOTES v2 (2026-10-11 23:31Z) and own rolling status/prior reports read. The lead's A046 scalar-review direction is stale: stage 2 already completed its reduction, boundary lemmas and faithful replay. Its rounded asymptotic coefficient and child orientation corrections remain those previously recorded. This stage therefore resumes the explicit saved A050/A064 audit obligation and consumes a new dependency rather than repeating the scalar census. A098's allocation retires duplicate singleton review and directs future A046 work toward localized odd-face payment; it is a dispatch proposal, not observed external adoption.

Read original A050 stage-2 REPORT.md, CLAIMS.json and PROOF.md, sections 1-7, run 20261013T212442Z-account05-A050-repair-with-scope. A064 REPORT.md sections on terminal-corrected reserves, exact drift signs and the first unsupported universal root bound; A098 CHECKPOINT_ALLOCATION.json keeper/dispatch and review-cap guards; own stage-1 exact logarithm helper and stage-2 PROGRESS. Earlier campaign, paper and registry readings are retained as recorded in prior runs; no new external theorem, novelty claim, or paper dependency is used here. SOURCE_MANIFEST.json hashes inspected original bytes and distinguishes refreshed context from mathematical premises.

# complete derivation or exact first unsupported line

**Independent reconstruction of the scalar prerequisite.** Put r=min(p,1-p). In the two real bases separated by beta, let u,w be the smaller probabilities. The two selected larger-probability basis vectors have overlap at most sqrt(1-r). Their projector sum has maximal eigenvalue 1+overlap, hence u+w>=delta=1-sqrt(1-r). Here delta<1/2, u,w<=1/2. If either probability exceeds delta, monotonicity gives h(u)+h(w)>=h(delta). Otherwise concavity on the segment u+w=delta gives the same inequality. Since delta>=r/2, h(delta)>=h(r/2)>=h(r)/2. Thus 0<=tau*<=h(p)/2, with no finite-p numerical minimizer or multi-bit uncertainty premise.

The symmetric trial t=beta/2 gives tau*>=h(p)-2h((1-sqrt(1-p))/2). Since the latter argument is p/4+O(p^2), tau*/h(p)->1/2 as p->0. At p=1/2, tau*=0: the positive-coefficient power series for h((1+z)/2) gives h(x)>=4x(1-x), and the two rotated bounds sum to one, attained at a basis vector.

**Reserve and root payment.** Let ell_v=h(p_i)/2-tau*(p_i)>=0. Independence of unrevealed inputs gives j_v=h(p_i)-c_v and exactly tau*-c_v/2=j_v/2-ell_v. The positive part is at most j_v/2. The physical conditional-output reserve has drift R_v-E R_child=j_v/2. Finite tree summation releases exactly I(Pi;Y)/2 and leaves E H(Y|Pi)/2 at stopping leaves; it never releases that terminal account twice. The transcript chain rule gives H(Pi|Y)=sum w_v c_v, proving the refund statement before any influence comparison.

For a fixed full physical order, H(Y)=sum_i I(Y;X_i|X_<i). Adding X_>i to the first argument and using product independence bounds each term by I(Y;X_i|X_-i)=H(Y|X_-i)=h(p_i)Inf_i^phys. Therefore H(Y)<=sum h(p_i)Inf_i^phys<=I_phys. This proves the root payment for adaptive or partially stopped trees too; H(Y|Pi) remains visible.

**Optimality, with exact quantifiers.** For lambda<1/2, the rare-endpoint limit chooses a fixed q with tau*(q)>lambda h(q). Take f_r=1-2 product_i X_i under q-biased inputs, with its essential short-circuit tree. Then A_T=tau*(q)(1-q^r)/(1-q), H(Pi|f_r)=h(q)(1-q^r)/(1-q)-h(q^r), and I_phys=r q^(r-1). Thus A_T-lambda H(Pi|f_r) tends to a positive constant but influence tends to zero. No finite C works. The previously proved refund gives lambda=1/2,C=1/2. This is optimality in that declared scalar bank family; it does not compare all structural repairs or supply a spectral bank. The underlying point-defect falsifier is credited to A048/A050, not a new FEI disproof.

**Terminal spectral ledger.** Direct actual squared-coefficient algebra gives the entropy decrement M_v+J_v. Set S_T=sum_v w_v[h(p_i)/2-(J_v-M_v)], M_T=sum w_v M_v. It is nonnegative by the scalar prerequisite and the one-bit angular reduction. The physical transcript chain rule and finite entropy telescope give exactly

    Hhat(f)=E Hhat(f_leaf)+2M_T+H(Pi|Y)/2+I(Pi;Y)/2-S_T.

Only the output-information term has been paid. The rest includes signed spectral erasure/uncertainty and all terminal Fourier entropy. At fair physical coordinates tau*=0, sum w h(p_i)/2=H(Pi)/2, so the output/transcript substitution cancels that same account exactly and leaves the original fair spectral ledger. A rare logical event does not turn a fair physical bit into a biased physical query.

**Independent compatibility test.** For fair full computing orders form the joint root Fourier set/transcript law directly, not by assuming an information-chain identity: for retained label T choose branch b with probability childhat_b(T)^2/[2q_T]. Multiplication of these kernels along each path gives the exact rational joint. Its physical transcript marginal is uniform and its child spectral law is correct. The kernel depends only on current retained root labels; conditional on them and history it is independent of earlier discarded labels. Hence I(S0;Pi)=sum w_v J_v. Because Y is determined by a full computing transcript,

    H(Pi|Y)-H(Pi|S0)=I(S0;Pi)-H(Y).

For f=(-1)^X this difference is -1. For f=(-1)^(X1 X2) it is -1+(3/4)log2(3), rigorously in (0.188721875540867,0.188721875540868). Both directions of universal conditional-entropy domination fail already on actual fair Boolean functions. These are reconstructions of A050's existing controls, not fresh obstruction claims. An essential short-circuit tree or the full tree gives the same difference in the second witness; the added dummy outcome contributes equally to both conditional entropies.

**Honest first unsupported line:** a normalized common-space spectral reference supplies H(Pi|Y)/2 once, including the signed side-information correction, and pays 2M_T-S_T plus terminal Fourier entropy from one original physical influence account. The present review does not establish it. The accepted local reserve alone cannot make this inference.

**Obsolete repairs rejected before computation.** Unchanged tax-free J<=M, any universal O(p) tax, raw restriction loss and fixed Renyi order below one are retired as in the prior A046 ledger. Essential contraction removes dummy tax but cannot repair the A048 essential point-defect tax-payment failure. Restarting H(Y)/2 at each node would reuse credit; exchanging H(Pi|Y) and H(Pi|S0) fails the two witnesses above. Dropping terminal entropy fails on an unrevealed arbitrary factor. The A064 CI-H candidate has the wrong reserve sign: its requested one-step payment reduces to the already false universal local D<=Cd. No numerical adjustment of those unchanged mechanisms was searched.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the first pilot; that larger all-adaptive-three-bit pilot did not finish within the wall-clock budget and was externally stopped, producing no certificate. Its proposed count contained an arithmetic error. FROZEN_SPEC_V3B.json corrects the count, reduces the domain and freezes the changed helper before the successful run; the first pilot is not cited as a PASS. No other process was stopped. A runtime guard and per-function cache clearing were added. Estimated memory 80 MB; no job expected above 300 MB, so no heavy-job memory gate was required.

Command: python -X utf8 runs\20261013T215251Z-account05-A046-current-candidate-intake\code\check.py. Result: 22,694 exact assertions PASS in 11.8950754 seconds. There are 7,466 tree/function/bias cases: n=0 two; n=1 twenty-four; n=2 1,296; n=3 6,144. Through two bits every raw function, every deterministic fresh-coordinate stopping policy (including adaptive and partial trees), and biases {1/4,1/2,3/4}^n are covered. At n=3 all 256 functions, six coordinate orders and four truncation depths are covered; equivalent labelled order/depth cases are deliberately counted repeatedly. Separately 294 direct full coherent joints cover every raw function through three bits, all orders through two bits and order (0,1,2) at three bits. No symmetry reduction or dimension escalation.

Each case checks physical conditional entropy by direct joint outcome/output tables, the stopped output-information telescope, the spectral telescope and the exact terminal-inclusive A050 ledger. Spectra are computed with Fraction arithmetic from centered product-basis moments. Entropy equalities compare formal rational prime-log vectors; vector equality is a sufficient exact certificate, with no assumption of independence of logarithms. The two compatibility signs use the previously checked rational 24-term atanh helper with four-corner interval division. No floating point establishes a sign or extrapolates a finite domain to the universal theorem. CHECK.json contains rational witness endpoints; universal acceptance rests on the analytic reconstruction above.

# proof dependencies and changed downstream conclusions

The sole reviewed claim is unchanged A050-OUTPUT-CONDITIONAL-TAX-REPAIR v1, including its explicit unpaid compatibility line. The proof is reconstructed without importing a pending block-uncertainty theorem or finite-p half-tax interval certificate. A050 supplies the claim and endpoint/control direction; A048 supplies the earlier essential-tax no-go. Our prior corrected singleton reduction supplies orientation conventions, also explained here. A037's coherent lift is reconstructed directly for compatibility control, not adopted as a universal credit payment.

CLAIMS.json preserves the exact A050 statement, hypotheses, contributors and hash, adding an A046 independent acceptance record with no substantive repair. This consumes the review queue rather than opening another broad candidate. Changed downstream conclusion: A050/A064 may use the half-output-bank theorem at its stated scope without waiting for this review; they still may not infer a spectral refund, erase terminal entropy, pay a biased spectral budget with physical influence, or sum shared-coordinate budgets. Independent acceptance is local evidence, not a mutation of the shared registry or proof of supervisor adoption.

# one next mathematical action and independent reviewer

Next: on the first three-event overlapping-control exposure failure already identified by A023/A040/A089, freeze its history-measurable physical tree and test the localized K=4 odd-face bill together with the accepted output-bank ledger. Charge each shared physical coordinate once, retain the signed difference I(S0;Pi)-I(Y;Pi) and all terminal spectral entropy, and identify the first unpaid node. This follows the A098 localized-credit allocation and avoids another singleton search or already-paid two-event census. A087 should independently challenge this acceptance and tree/terminal signs; A092 should challenge the scalar-bank coefficient and scope. Saved handoff metadata is not external messaging.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved in the assigned stage directory with code/check.py, code/finalize.py, both frozen specs, CHECK.json, source manifest, schema check and hash receipts. Rolling STATUS.md has exactly STATE/NEXT lines; WORKLOG.md is appended and LEARNED.md records durable scope. All mutations are inside A046. No git, brain mutation or external message occurred. Independent external challenge, supervisor copies and mirror verification are unobserved. SHA256 receipts certify local bytes only; they do not establish downstream use.

# Universal bridge

This stage advances C024 history transfer and C019 stopping-tree payment by independently accepting the unchanged sharp half-output-conditional refund on every finite physical singleton tree, with its complete stopped output reserve and terminal Fourier ledger; 22,694 exact assertions independently validate the interfaces. It also pins the already-known bidirectional side-information mismatch with rational certificates, so neither spectral nor output conditioning is treated as free credit. The universal normalized reference, signed erasure payment and terminal admission remain open. NEXT combines the accepted refund with localized odd-face credit at the first existing shared-control exposure failure, because that is the unresolved ownership/conditioning interface needed by arbitrary physical restriction trees, rather than another isolated class entropy bound.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B10','packet_id':'A046','gap_id':'G-C024-OUTPUT-SPECTRAL-REFUND','attempt_id':'A046-stage3-review-1','method':'Independent all-dimensional proof reconstruction plus exact direct physical and coherent joint probability tables','mathematical_delta':'Unchanged A050 v1 independently accepted at stated scoped refund/optimality; 22694 exact assertions PASS; terminal and bidirectional spectral-conditioning gaps retained','deliverable_status':'COMPLETE_LOCAL_INDEPENDENT_REVIEW','mathematical_status':'SCOPED_OUTPUT_REFUND_ACCEPTED; UNIVERSAL_REFERENCE_AND_FULL_FEI_OPEN','claim_versions_used':['A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 (reviewed unchanged)','A046-CORRECTED-ONEBIT-REDUCTION-REVIEW@1 (orientation context)','A048 sharp-tax no-go (source credited; proof reconstructed)'],'claims_created_or_changed':['A050-OUTPUT-CONDITIONAL-TAX-REPAIR@1 (independent review record only)'],'source_artifacts':['REPORT.md','CLAIMS.json','code/check.py','out/CHECK.json','out/FROZEN_SPEC.json','out/FROZEN_SPEC_V3B.json','out/SOURCE_MANIFEST.json'],'next_consumers':['A050','A064','A037','A039','A040','A089','A087','A092','B10','B20'],'next_action':'Test localized K=4 odd-face payment at the existing three-event exposure failure with one physical influence account, accepted output refund, signed side-information correction and retained terminal Fourier entropy','stagnant_substantive_attempts':0,'blockers':['Universal compatible-reference bank funding remains unproved','Signed erasure and terminal admission remain unpaid','External review challenge, registry adoption and mirror receipts unobserved'],'packet_ids':['A046']}
dump(ROOT/'PROGRESS.json',progress); dump(ROOT/'PACKET_DELTA.json',progress)
sources=[BASE/'BOARD.md',BASE/'claude'/'B10'/'STREAM_NOTES.md',SOURCE/'REPORT.md',SOURCE/'PROOF.md',SOURCE/'CLAIMS.json',BASE/'agents'/'A064'/'runs'/'20261011T224431Z-account05-A064-global-debt-potential'/'REPORT.md',BASE/'agents'/'A098'/'runs'/'20261012T024601Z-account05-A098-resource-reallocation'/'CHECKPOINT_ALLOCATION.json',Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
dump(ROOT/'out'/'SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources])
(HOME/'STATUS.md').write_text('STATE: A046 stage 3 complete: unchanged A050 v1 half-output refund independently accepted; 22,694 exact assertions PASS; signed spectral-conditioning and terminal gaps retained; FEI OPEN.\nNEXT: Test localized K=4 odd-face payment at the existing three-event exposure failure with one physical influence account, signed output/spectral correction and terminal entropy; A087/A092 challenge review.\n',encoding='utf-8')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write('\n2026-10-13 stage 3 (run '+ROOT.name+'): consumed A050 v1 after retiring duplicate scalar review. Independently reconstructed all-tree refund and minimal coefficient; direct rational probability-table audit PASS (22,694 assertions). Initial larger pilot stopped without certificate; reduced frozen job finished 11.895s. Accepted original hash without repair, preserving spectral-reference and terminal gaps. No universal FEI claim.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8') as f: f.write('\nStage 3 durable: A050-OUTPUT-CONDITIONAL-TAX-REPAIR v1 independently accepted unchanged by A046. The conserved physical reserve is H(Y|v)/2; its release is I(Pi;Y)/2, with terminal output entropy retained. Refund coefficient 1/2 is sharp only in the declared A_T<=C I_phys+lambda H(Pi|Y) family. Spectral compatibility is additional: H(Pi|Y)-H(Pi|S0)=I(S0;Pi)-I(Y;Pi); fair character gives -1 and AND gives -1+(3/4)log2(3)>0. Neither conditioning universally dominates. Fair physical tau is zero; a logical rare-event bias is not a physical query bias. Terminal Fourier entropy remains separate. Retire scalar replay; next localized odd-face shared-coordinate ownership.\n')
protocol=json.loads(sources[-1].read_text(encoding='utf-8-sig'))
pf=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(pf)
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (ROOT/'PACKET_DELTA.json').read_bytes()==(ROOT/'PROGRESS.json').read_bytes()
assert len((HOME/'STATUS.md').read_text().splitlines())==2
for title in protocol['required_per_run']['report_fields']: assert '# '+title in report
assert report.strip().split('\n\n')[-2]=='# Universal bridge'
dump(ROOT/'out'/'SCHEMA_CHECK.json',{'status':'PASS','claim_hash':digest,'fields_exact':True,'packet_delta_identical':True,'status_two_lines':True,'universal_bridge_last':True})
receipts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
dump(ROOT/'out'/'PERSISTENCE_RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','accepted_claim_hash':digest,'saved_files':len(receipts)+1,'full_fei':'OPEN'}))
if __name__=='__main__': pass
