import copy,datetime,hashlib,json
from pathlib import Path
RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];TEAM=AGENT.parents[1]
SRC=TEAM/'agents/A028/runs/20261014T051435Z-fleet05-A028-stopping-tree-payment'
A23=TEAM/'agents/A023/runs/20261014T051414Z-fleet05-A023-amortized-rarity-budget'
OLD=AGENT/'runs/20261014T025327Z-fleet05-A029-child-deficit-transport'
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
pr=json.loads(PROTOCOL.read_text(encoding='utf-8'));a=json.loads((RUN/'out/compression.json').read_text());b=json.loads((RUN/'out/bank.json').read_text())
assert a['status']==b['status']=='PASS'
assert a['core_width_cases']==36864 and b['roots']==8256 and b['queries']==471744
total=a['assertions']+b['assertions']
source=json.loads((SRC/'CLAIMS.json').read_text());c=copy.deepcopy(source[0])
assert c['version']==5 and c['statement_sha256']=='66a08477db58867a640a8dc7202d62a73c1f8d766491eaf3a2cd26e896317b7d'
c['review_records'].append({'reviewer':'fleet05/A029','verdict':'HOLDS_MIXED_BANK_AND_RELEASE_ONLY_GUARD_CLAUSES_ONLY','source':str(RUN/'REVIEW_A028.md'),'scope':'DERIVATION sections4 and7, binary arbitrary mixed-history bank, data owner/release bound, exact AND2 guard','excluded':'Controller entropy/reference clauses, old versions and whole bundled acceptance','repair_supplied':False,'validation':{'roots':b['roots'],'histories':b['histories'],'queries':b['queries'],'assertions':b['assertions']}})
c['status']='INDEPENDENT_SCOPED_BANK_ACCEPTANCE_OTHER_CLAUSES_PENDING'
dump(RUN/'CLAIMS.json',[c])
used=[{'claim_id':c['claim_id'],'version':5,'statement_sha256':c['statement_sha256'],'scope':'BANK_AND_EXACT_GUARD_ONLY','status':'INDEPENDENTLY_RECONSTRUCTED'},
 {'claim_id':'A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER','version':3,'scope':'Whole-point-block only','status':'PREVIOUS_A029_A025_SCOPED_ACCEPTANCE'},
 {'artifact':'A029 stage4 DERIVATION.md','review_source':str(A23/'REVIEW_A029.md'),'status':'A023_INDEPENDENT_ACCEPTANCE_OF_NESTED_ALGEBRA_CONSUMED'},
 {'claim_id':'B06-R2','version':'STREAM_NOTES v2,2026-10-11 23:26Z','status':'BASELINE_NOT_REPROVED'}]
nextaction='At one non-flat three-label mixed query, compare the actual signed entropy/reference residual with released FIXED-price R_star, actual query influence and unused certified child deficits; keep both terminal bills. A023/A028/A087/A094 review conversion and finite-label conservation.'
p={'protocol_revision':pr['revision'],'run_id':RUN.name,'stream':'B06','packet_id':'A029','gap_id':'G-R-MISMATCH','attempt_id':'A029-child-deficit-transport-05','method':'Finish reviewed nested application by sharp Boolean three-pivot cut compression; independently review A028 bank and carry finite-label pivot-variance bank through all mixed histories','mathematical_delta':f'Sharp all-dimensional R_data<=[(2-a-b)/(1-ab)]R_star with distinct nonconstant equality witness; signed three-core sufficient condition retains future-control debit. Arbitrary finite-label R_star supermartingale and sharp data release<=2d(1-d). A028 scoped HOLDS. {total} exact assertions PASS. No new broad universal candidate.','deliverable_status':'COMPLETE_LOCAL_SAVED','mathematical_status':'SCOPED_DEPENDENCY_ACCEPTED_PRIOR_APPLICATION_FINISHED_LOCAL_ENTROPY_PAYMENT_AND_FEI_OPEN','claim_versions_used':used,'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':5,'change':'LOCAL_SCOPED_REVIEW_ONLY_SOURCE_UNCHANGED'}],'source_artifacts':['REPORT.md','DERIVATION.md','REVIEW_A028.md','SPEC.json','VERIFY_SPEC.json','code/compression.py','code/bank.py','out/compression.json','out/sharp_witness.json','out/bank.json','out/guard.json','out/PILOT_CORRECTION.json'],'next_consumers':['A023','A025','A027','A028','A030','A064','A087','A094','B06 lead','B20'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['Released boundary bank does not by itself pay entropy drift; non-flat mixed residual still needs unused certified child surplus','General terminal FEI admission remains open','External review of checked consequences, remote copying and downstream use unverified'],'packet_ids':['A029']}
dump(RUN/'PROGRESS.json',p);dump(RUN/'PACKET_DELTA.json',p)
report=f'''# exact target, quantifiers, hypotheses and units

A029/B06 stage5, run {RUN.name}. Complete the existing three-core owned-reserve application while consuming useful independent review and a new conserved-bank dependency. Entropy bits, Boolean signs, uniform physical cube. Fresh point blocks a=2^-r,b=2^-s,r,s>=1, arbitrary three shared-data cores; original terminal weights(1-a,a(1-b),ab). All actual child deficits remain signed. Second target: arbitrary finite-valued physical controller L on fresh independent controls, arbitrary finite list of Boolean cores on one shared data cube, and ANY adaptive mixed physical stopped tree.

This is verification/completion of the prior application and independent source-bound A028 review, not another broad FEI candidate while older claims await review. The stale B06 lead gain NEXT was refuted in stage3 at its unrestricted scope; no further gain search is undertaken. Protocol dispatch consumes the newer reviewed dependency. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read BOARD.md supervisor2026-10-14 05:52UTC in two parts, B06 STREAM_NOTES.md unchanged v2, own STATUS.md and complete protocol revision {pr['revision']}. Read A023 stage5 REPORT.md and REVIEW_A029.md, A028 LEARNED.md and current full DERIVATION.md/CLAIMS.json. Source locators: A028 DERIVATION sections4 and7; A023 REVIEW_A029 actual accepted nested-algebra scope. A028 source run {SRC.name}; A023 source run {A23.name}.

The board points to A023's finite10648-case stronger symmetric payment, A025's nested owner no-go and A028's carried binary bank. We consume their exact scope: A023 independently accepts our stage4 nested algebra without repair, but does not certify arbitrary-dimensional multiplier1 payment; A028 bank conservation is separate from entropy drift. One initially guessed A028 run locator did not exist; listing runs resolved the actual path before using it. This was access-only and is not a substantive failure.

No fresh paper, web or brain premise. Earlier campaign reads remain inherited. Current-source SHA256 receipts and a local board snapshot are saved; all source folders and indices remain read-only.

# complete derivation or exact first unsupported line

Full proofs are DERIVATION.md and REVIEW_A028.md. Sharp data compression for every core dimension/triple is R_data<=kappa R_star, kappa=(2-a-b)/(1-ab), 4/3<=kappa<2. The complete Boolean per-edge partition has only three nonzero exceptional-label patterns. Their ratios are1,(1-a+b)/(1-a+ab),kappa; the last dominates since the cross-multiplied difference is(1-a)^2(1-2b)>=0. The actual distinct nonconstant equality witness is g0=x,g1=-x,g2=xy. This certifies a sufficient RESERVE conversion factor, not the optimum entropy constant.

The original future-control reserve is retained. With I_C=I_A+aI_B and original pi weights, for every real K,

    D_K(f)>=sum pi_j D_K(gj)+(K-11/2)I_C-kappa R_star-2a(1-a)I_B.

This is an explicit sufficient condition for child slack to compensate a difficult block: its right side must be nonnegative. No child is clipped. Supplied terminal rates Cj yield max(11/2+2(1-a),max_j[Cj+2kappa(1-pi_j)])I(f). The price mark is fixed at the root and not reissued. This closes an all-dimensional two-level priced-bank application; it does not claim A023's multiplier1 finite entropy payment extends universally or that repeated depth has a fixed conversion factor.

For finite-label control pi and restricted actual cores, the root symmetric bank is R=2sum_{{j<k}}pi_j pi_k I(gj gk). Let r_j(i,x) be a core data-edge pivotal indicator and q_i=sum pi_j r_j. EXACTLY R=2sum_i E q_i(1-q_i). Controller-query release is(1/2)sum_i E(q_i^0-q_i^1)^2>=0. Data-query release is2sum_{{j<k}}pi_j pi_k Inf_i(gj gk)=2E q_i(1-q_i)<=2d_i(1-d_i)<=2d_i. Thus Rroot=sum physical_reach*release+E terminalR for every adaptive mixed stopped tree, with no renewed mark and both actual siblings retained. Any fixed root multiplier contracts by the same identity. Arbitrarily changing the multiplier is not licensed.

A028@5's binary bank and exact release-only guard independently HOLDS; entropy/reference clauses and full bundled claim excluded from acceptance. The AND2 guard attains the new data-release cap at d=1/2, release1/2; its entropy residual is2, leaving a3/2 gap. A local additional data price must be at least3 in that residual rule. A conserved bank is not itself an entropy bound.

FIRST UNSUPPORTED LINE: pay the actual signed entropy/reference residual at a non-flat mixed query from the fixed-price bank release, actual queried influence, and one unused inherited child surplus, retaining both full terminal/reference debts. The new sharp conversion and conservation do not remove that line. The old constant-failure chain's repeated sufficient reserve still has unbounded root-bank ratio; its grouping repair was already proved in stage4 and is not repeated.

# executed validation with domain, arithmetic, commands and outputs

SPEC.json/VERIFY_SPEC.json frozen before their respective jobs. Exact arithmetic only; no floating mathematical decisions, random sampling, GPU, automatic dimension growth or persistent process. Memory estimates25MB and100MB; no>300MB expected job, so memok gate not applicable. Compression max60seconds, observed{a['seconds']:.6f}; mixed-bank max180seconds, observed{b['seconds']:.6f}. Jobs ran sequentially. All pilots under60seconds.

Commands `python -X utf8 runs\\{RUN.name}\\code\\compression.py --pilot`, then without --pilot; same for `code\\bank.py`. Compression PASS all36864 ordered two-bit-core/width cases (16^3 masks times r,s1..3),72 pivot patterns and144 exact sharp-witness pairs at r,s1..12, {a['assertions']} assertions. Integer Boolean product edges and Fraction cut ratios; all-dimensional proof uses the complete edge-pattern partition. Outputs out/compression.json and out/sharp_witness.json saved immediately.

Bank PASS {b['roots']} roots: all81 ternary label maps on two controls times all4^3 one-bit core triples (5184), plus six canonical surjective maps times all8^3 declared two-bit core triples (3072). Canonical maps choose the paired controller vertices; core-position permutations cover all label relabelings. The selected mask list is0,1,3,5,6,10,12,15; no claim of exhausting all two-bit core triples for this bank job. Every ternary restriction and every remaining physical query checked: {b['histories']} histories, {b['queries']} sibling queries, {b['stopped_trees']} stopped-controller trees, {b['assertions']} assertions. Maximum physical dimension4. Direct pair-product Boolean boundaries are compared with separately enumerated pivot variance; actual conditional label counts give exact Fraction probabilities. Arbitrary history probabilities are not replaced by spectral labels. out/bank_checkpoint.json flushed after each dimension; out/bank.json and exact guard saved immediately.

One pilot failed in the guard-only check because I compared squared INTEGER Walsh numerator to1 rather than4 for a4-entry truth table. All bank identities had already passed. Corrected before the full run, with out/PILOT_CORRECTION.json preserving the first failed assertion19603, scope and normalization. Corrected pilot19605 checks passed. This is an A029 implementation correction, not a source repair. Neither domain nor mathematical target was weakened. Total full-run assertions {total}; all PASS. No test repeated after both full jobs passed.

# proof dependencies and changed downstream conclusions

Consume A023's independent review of A029 stage4 nested influence/owner/signed-condition algebra at its explicit scope. Use the previously A029/A025 accepted A023@3 whole-point-block clause for the root entropy price. Independently reconstruct A028@5 binary bank/conservation and guard clauses; original statement hash preserved in CLAIMS.json local review copy, source unchanged. Existing B06-R2 telescoping is a baseline, not reclaimed as new.

The sharp conversion and finite-label extension finish the existing application; no new broad universal candidate is opened. General formulas are proved analytically and checked exactly; separate external review of these consequences remains pending. A023's finite symmetric entropy theorem is contextual reported evidence, not independently accepted here or used as a proof premise. The two-bit finite payment census is not rerun. No circular FEI certificate or free terminal refund is introduced.

A023/A025/A027/A028/A064 can price the first two-level data surcharge with one root kappa R_star and carry that fixed bank through later mixed histories. They must retain the future-control debit and may not infer entropy payment from conservation. The sharper data-release cap2d(1-d) is attained by the existing guard. Arbitrary core/terminal admission and a depth-independent signed payment remain OPEN.

# one next mathematical action and independent reviewer

{nextaction} This targets the unpriced residual after a real mixed query, not another larger finite gain census. A028/A087 should independently reconstruct the finite-label variance identity and query releases; A023/A025/A094 should reconstruct the three-pivot sharp factor and signed child condition. Saved source-bound handoffs only, no messages sent and no observed external adoption.

# actual persistence receipts or precise save blocker

Saved four protocol files, DERIVATION.md, REVIEW_A028.md, both frozen specs, code and exact outputs/correction record. Schema keys, byte-identical PROGRESS/PACKET_DELTA, report fields/final bridge and file sizes<20MB checked. SOURCE_RECEIPTS.json and ARTIFACT_RECEIPTS.json give current hashes. STATUS.md two lines, dated WORKLOG append and durable LEARNED append updated inside A029 only. No local persistence blocker. Remote copying, new application acceptance and downstream use unverified.

**Universal bridge:** This stage moves C019 stopping payment and C024 history transfer by completing a sharp all-dimensional two-level child-deficit application with one priced symmetric root reserve and by proving that this finite-label reserve conserves through every physical mixed history. The conversion factor is exactly(2-a-b)/(1-ab)<2, attained by three distinct nonconstant cores; data release has the sharp cap2d(1-d). Both signed child deficits and the future-control debit survive, and the exact release-only guard prevents treating conservation as payment. What remains is a noncircular unused terminal certificate that funds the actual non-flat mixed-query residual, plus a universal depth-independent payment. NEXT is the shortest route toward full FEI because the root bank can now be carried without reset, leaving one concrete signed residual to price rather than another isolated class or repeated tree identity.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(AGENT/'STATUS.md').write_text(f'STATE: A029 stage5 saved: sharp two-block kappa<2 with distinct-core equality; finite-label R_star contracts through arbitrary mixed histories; A028 bank scoped HOLDS; {total} exact checks PASS; FEI OPEN.\nNEXT: A023/A028/A087/A094 review; pay one non-flat three-label mixed-query signed residual from fixed bank release, actual query influence and unused child surplus; retain both terminal debts.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Stage5 {RUN.name}: consumed A023 independent review of stage4. Sharp three-edge-pattern kappa compression proved with x,-x,xy equality; finite-label mixed R_star bank proved and data release sharp2d(1-d). Independently reviewed only A028@5 bank/guard; no repair. Compression36864 cases73973 checks PASS2.08s; bank8256 roots388800 histories471744 queries1770627 checks PASS48.61s. Pilot guard numerator normalization corrected before full run; record saved. Full FEI and actual non-flat mixed residual payment OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
2026-10-14 stage5: A023 stage5 independently accepts our stage4 nested owner/signed algebra only. Sharp all-dimensional two-point-block DATA reserve conversion: Rdata<=kappa Rstar,kappa=(2-a-b)/(1-ab) in[4/3,2),a,b<=1/2. Per-edge pivotal cut patterns give ratios1,(1-a+b)/(1-a+ab),kappa; their cross difference(1-a)^2(1-2b)>=0. Equality with DISTINCT NONCONSTANT g0=x,g1=-x,g2=xy (masks10,5,9). Signed sufficient D_Kroot>=sum piD_K+(K-11/2)I_C-kappaRstar-2a(1-a)I_B keeps future controls and all negative children. Any finite label map on fresh controls and shared Boolean cores has R=2sum pi_jpi_k I(gj gk)=2sum_iE q_i(1-q_i),q_i weighted core pivot indicators. Under controller query release=1/2sum_iE(q0-q1)^2; data query release=2E q_i(1-q_i)<=2d_i(1-d_i)<=2d_i. All mixed stopped histories conserve ONE fixed-price bank; updating multiplier or source needs a priced term. A028@5 bank/guard scoped independently HOLDS; controller entropy/reference and whole bundle excluded. AND2 source guard attains new data-release cap but entropy residual exceeds release by3/2, necessary extra local data price>=3. Therefore bank conservation still does not pay a non-flat mixed entropy/reference residual. Compression73973 and bank1770627 exact checks PASS. Pilot guard had Walsh numerator-square1-versus4 error, corrected before full run without source repair. No universal FEI result.
''')
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B06/STREAM_NOTES.md',A23/'REPORT.md',A23/'REVIEW_A029.md',SRC/'DERIVATION.md',SRC/'CLAIMS.json',TEAM/'agents/A028/LEARNED.md',OLD/'DERIVATION.md']
dump(RUN/'SOURCE_RECEIPTS.json',{'saved_at':now,'sources':[{'path':str(z),'sha256':sha(z),'bytes':z.stat().st_size} for z in sources]})
(RUN/'out/BOARD_snapshot.md').write_bytes((TEAM/'BOARD.md').read_bytes())
assert set(c)==set(pr['required_per_run']['claim_fields'])
assert set(p)=={v.split(' (')[0] for v in pr['required_per_run']['progress_fields']}
for field in pr['required_per_run']['report_fields']:assert '# '+field in report
assert report.splitlines()[-1].startswith('**Universal bridge:**')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
files=[z for z in RUN.rglob('*') if z.is_file() and z.name!='ARTIFACT_RECEIPTS.json'];assert all(z.stat().st_size<20*1024*1024 for z in files)
dump(RUN/'ARTIFACT_RECEIPTS.json',{'saved_at':now,'protocol_keys_exact':True,'progress_delta_byte_identical':True,'all_under20MB':True,'receipts':[{'path':str(z.relative_to(RUN)),'sha256':sha(z),'bytes':z.stat().st_size} for z in files]})
print(json.dumps({'status':'PASS','run':str(RUN),'total_assertions':total,'schema_keys_exact':True,'rolling_current':True,'review_scope':'A028 BANK/GUARD ONLY','full_FEI':'OPEN'}))
