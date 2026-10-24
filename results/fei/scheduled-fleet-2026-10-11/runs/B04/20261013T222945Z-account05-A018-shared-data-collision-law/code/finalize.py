"""Persist stage metadata, source-bound reviews, and local readback receipts."""
from pathlib import Path
import json, hashlib, datetime

RUN = Path(__file__).resolve().parents[1]
OWN = RUN.parents[1]
BASE = OWN.parents[1]
PROTO = Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
A016 = BASE/'agents/A016/runs/20261013T214508Z-account05-A016-addressing-benchmark'
LEAD = BASE/'claude/B04/runs/20261011T224500Z-claude-B04-sharp-selector-debt'
OLD = OWN/'runs/20261012T010436Z-account05-A018-shared-data-collision-law'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, obj): p.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n', encoding='utf8')
def plain(st): return hashlib.sha256(st.encode('utf8')).hexdigest()
def canonical(c): return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',', ':')).encode('utf8')).hexdigest()

protocol = read(PROTO)
outputs = {name:read(RUN/'out'/name) for name in ('PRODUCT_PILOT.json','PRODUCT_CHECK.json','SPINE_REVIEW.json','ROW_IDENTITY_CHECK.json')}
total = sum(x['checks'] for x in outputs.values())
assert total == 394537
assert all(x['status']=='PASS' for x in outputs.values())
report = (RUN/'REPORT.md').read_text(encoding='utf8')
report = report.replace('157 assertion groups', '204 assertion groups').replace('2.820 seconds',f"{outputs['SPINE_REVIEW.json']['elapsed_seconds']:.3f} seconds")
report = report.replace('394,490 checks', '394,537 checks')
(RUN/'REPORT.md').write_text(report, encoding='utf8')

source = read(A016/'CLAIMS.json')[0]
assert source['statement_sha256']==plain(source['exact_statement'])
review = {'reviewer':'A018/account05','reviewed_at':NOW,'verdict':'HOLDS_AT_STATED_SCOPE',
 'source_claim':'A016-CONNECTED-SPINE-FACTOR-REPAIR-CONTROL@1',
 'source_claims_path':str(A016/'CLAIMS.json'),'source_claims_sha256':sha(A016/'CLAIMS.json'),
 'statement_sha256':source['statement_sha256'],'hash_recipe':'SHA256(exact_statement UTF-8)',
 'scope':'Entire all-a>=1, even-m>=4 statement; fixed selector-first failure, finest sign factor removal, paid separator-first control, and normalized complete reference.',
 'reconstruction':'Independent analytic reconstruction in REPORT.md Section 1; own actual truth tables, GF(2) ANF components, physical edges, Walsh derivatives, and normalized reference. No A016 checker imported.',
 'proof_artifact':str(RUN/'REPORT.md'),'exact_certificate':str(RUN/'out/SPINE_REVIEW.json'),
 'checks':204,'substantive_repair':False,'remaining_gap':'Universal adaptive C019 and full FEI; no general bad-tree payment inferred.'}
save(RUN/'out/REVIEW_RECORDS.json',[review])
source['review_records'].append(review)
source['status']='INDEPENDENT_A018_HOLDS_AT_STATED_SCOPE; SUPERVISOR_ADOPTION_PENDING'

statement = ('For every r>=1 and Boolean signs f_j(z,y_j)=g_{j,z}(y_j) sharing exactly one uniform physical bit z with mutually disjoint private blocks, set F=product_j f_j. In bits, let P_jb be each branch squared spectrum, R_j=(P_j0+P_j1)/2, R=(product_j P_j0+product_j P_j1)/2, B_j=H(S_z^j|S_yj^j), B_*=H(S_z^F|S_y^F), M_j=H(R_j)-average_b H(g_jb), M_*=H(R)-average_b sum_j H(g_jb), and TC=KL(R||product_j R_j). Then H(F)-sum_j H(f_j)=B_*-sum_j B_j-TC, M_*=sum_j M_j-TC, 0<=TC<=sum_j M_j, and H(F)<=sum_j H(f_j)+1. For any normalized complete module references Q_j with finite cross-entropy, let q_j(T)=sum_A Q_j(A,T), tau_j=Q_j/q_j, and k_j=E_Rj KL(nu_j||tau_j), with actual selector conditional laws nu_j. The normalized reference Q_*(A,Tvec)=nu_*(A|Tvec) product_j q_j(T_j), using any fixed conditional on zero true rows, satisfies CE_*=sum_j CE_j+B_*-sum_j B_j-sum_j k_j and CE_*-H(F)=TC+sum_j KL(R_j||q_j). If d_j=Inf_z(f_j), then d_*=Inf_z(F)=[1-product_j(1-2d_j)]/2, I(F)=sum_j average_b I(g_jb)+d_*, and sum_j I(f_j)-I(F)=sum_j d_j-d_*=2 E floor(N_flip/2)>=0. These are exact interfaces, not an influence bound for TC or a universal FEI proof.')
new = {'claim_id':'A018-SHARED-SEPARATOR-TC-REFERENCE','version':1,'exact_statement':statement,
 'hypotheses':['r>=1; all input bits independent fair bits','each f_j is a Boolean sign; all modules share z and have disjoint private blocks','entropy, cross-entropy, and KL use bits; influence is physical edge disagreement','each Q_j is a normalized complete spectral reference and has finite cross-entropy on f_j','zero true rows receive arbitrary fixed selector conditionals; no positive true row may be excluded'],
 'statement_sha256':plain(statement),'contributors':['A018/account05'],
 'proof_source':{'path':str(RUN/'REPORT.md'),'locators':['Sections 2-4; Section 5 for the separate unproved strengthening'],'code':str(RUN/'code/check_row_identity.py'),'exact_certificates':[str(RUN/'out/ROW_IDENTITY_CHECK.json')]},
 'proof_dependencies':[],'review_records':[], 'status':'AUTHOR_PROVED_EXACT_INTERFACE_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['B04 lead','A019','A020','A086','A090','A091','A095','A097','B20']}
save(RUN/'CLAIMS.json',[source,new])

corrections=[]
for c in read(LEAD/'CLAIMS.json')['claims']:
 if c['claim_id'] not in ('B04-SEL-LOG-SHARP','B04-BENT-SPLICE-SHARP','B04-NODE-BOUNDARY'): continue
 assert canonical(c)==c['statement_sha256']
 corrections.append({'claim':f"{c['claim_id']}@{c['version']}",'announced_original_sha256':c['statement_sha256'],'recomputed_canonical_statement_and_hypotheses_sha256':canonical(c),'plain_statement_utf8_sha256':plain(c['exact_statement']),'original_hash_valid':True,'mathematical_verdict':'HOLDS_UNCHANGED','correction':'Previous A018 metadata warning compared different hash recipes; no lead source hash needed repair.'})
assert len(corrections)==3
save(RUN/'out/HASH_CONVENTION_CORRECTION.json',{'recorded_at':NOW,'source':str(LEAD/'CLAIMS.json'),'source_sha256':sha(LEAD/'CLAIMS.json'),'source_recipe_code':str(LEAD/'code/write_records.py'),'canonical_recipe':'SHA256(UTF8(json.dumps({statement: exact_statement, hypotheses: hypotheses}, sort_keys=True, separators=(comma,colon))))','affected_prior_artifacts':[str(OLD/'CLAIMS.json'),str(OLD/'out/REVIEW_RECORDS.json'),str(OLD/'REPORT.md')],'previous_runs_modified':False,'metadata_diagnosis_retracted':True,'mathematical_acceptances_retracted':False,'records':corrections})

paths = [(PROTO,'Protocol complete field definitions'),(BASE/'BOARD.md','Stage-start board and relevant follow-up entries'),(BASE/'claude/B04/STREAM_NOTES.md','B04 v2 direction'),(A016/'REPORT.md','Sections 1-6 full proof reconstruction'),(A016/'CLAIMS.json','Exact claim and hash'),(A016/'code/persist.py','Plain-statement hash recipe'),(BASE/'agents/A017/runs/20261013T220934Z-account05-A017-recursive-addressing/REPORT.md','Stage3 shared-spine phase obstruction'),(BASE/'agents/A019/LEARNED.md','Disjoint rare translations'),(BASE/'agents/A020/LEARNED.md','n5 finite discount scope guard'),(BASE/'agents/A086/LEARNED.md','Disjoint-child reference transfer guard'),(BASE/'agents/A095/LEARNED.md','Common-spine costs and metadata correction'),(BASE/'agents/A097/LEARNED.md','Compatible reference and nonreuse guard'),(LEAD/'CLAIMS.json','Three original canonical digests'),(LEAD/'code/write_records.py','Canonical digest recipe'),(OLD/'REPORT.md','Prior independent review'),(OLD/'code/check_lead.py','Imported rational-log arithmetic definitions; main not executed')]
save(RUN/'out/SOURCE_RECEIPTS.json',{'recorded_at':NOW,'note':'Hashes bind available source bytes at stage close, not a claimed immutable stage-start BOARD snapshot. External sources read-only; no mirror/adoption receipt.','sources':[{'path':str(p),'sha256':sha(p),'read_scope':scope} for p,scope in paths]})

next_action='Prove or refute the zero-mean scalar paired-row entropy inequality; then insert its exact correction against the repeated-selector loss L and one exclusive deficit reserve on a two-separator fixture, retaining terminal CE.'
progress = {'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B04','packet_id':'A018','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A018-stage3-shared-separator-tc-owned-influence',
 'method':'Independent analytic source reconstruction; exact physical edges, GF(2) ANF, rational Walsh spectra, integer prime-log identities and outward rational logarithm certificates.',
 'mathematical_delta':'A016 connected-spine factor-removal obstruction and paid separator/reference control independently HOLDS. Proved exact shared-product entropy correction B_*-sum B_j-TC, conditional-product reference debt TC+sum marginal KL, and repeated physical selector loss L. Exhausted 65536 ordered two-private-bit module pairs; no entropy-subadditivity violation. 394537 checks total. Corrected prior hash-recipe diagnosis without changing mathematical verdicts.',
 'deliverable_status':'COMPLETE_LOCAL_READBACK_VERIFIED','mathematical_status':'EXACT_INTERFACE_AUTHOR_PROVED_PENDING_REVIEW; A016_INDEPENDENT_HOLDS; UNIVERSAL_FEI_OPEN',
 'claim_versions_used':['A016-CONNECTED-SPINE-FACTOR-REPAIR-CONTROL@1 (reviewed, not a premise of new interface)','A018-COLLISION-BLOCK-INTERFACE@1 (previous identity context)','B04-SEL-LOG-SHARP@1 (metadata-only correction)','B04-BENT-SPLICE-SHARP@1 (metadata-only correction)','B04-NODE-BOUNDARY@1 (metadata-only correction)'],
 'claims_created_or_changed':['A018-SHARED-SEPARATOR-TC-REFERENCE@1: new exact interface pending independent review','A016-CONNECTED-SPINE-FACTOR-REPAIR-CONTROL@1: unchanged statement and hash; append independent A018 HOLDS review','Three B04 v1 hash warnings: retract previous metadata diagnosis; original canonical digests verified'],
 'source_artifacts':['REPORT.md','CLAIMS.json','code/check_product.py','code/check_spine.py','code/check_row_identity.py','code/finalize.py','out/FROZEN_SPEC.json','out/IDENTITY_SPEC.json','out/PRODUCT_PILOT.json','out/PRODUCT_CHECK.json','out/SPINE_REVIEW.json','out/ROW_IDENTITY_CHECK.json','out/REVIEW_RECORDS.json','out/HASH_CONVENTION_CORRECTION.json','out/SOURCE_RECEIPTS.json','out/PERSISTENCE_RECEIPTS.json'],
 'next_consumers':['B04 lead','A016','A019','A020','A081','A086','A090','A091','A095','A097','B20'],
 'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal scalar entropy strengthening unproved outside certified finite domain','No exclusive influence payment for shared-selector loss and residual data/reference debt','Independent review, supervisor adoption and mirror verification pending'],'packet_ids':['A018']}
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)

(OWN/'STATUS.md').write_text('STATE: A018 stage 3: A016 connected-spine control independently HOLDS; exact shared-separator TC/reference interface proved pending review; 394537 checks PASS; full FEI OPEN.\nNEXT: Prove/refute scalar paired-row entropy inequality, then pay shared-selector loss L with an exclusive reserve on a two-separator fixture; retain terminal CE.\n',encoding='utf8')
with (OWN/'WORKLOG.md').open('a',encoding='utf8') as f:
 f.write(f'\n## {NOW} — stage 3 ({RUN.name})\nRead current BOARD/B04 notes and consumed A016 new connected-spine dependency. Independent all-parameter analytic reconstruction HOLDS; own truth/ANF/edge/derivative/reference implementation passed five fixed fixtures. Exhausted 256 pilot and 65536 full module pairs, then checked new row/reference quantities on the same domain; 394537 checks PASS in bounded low-memory jobs. Proved exact TC/reference debt and shared-coordinate influence loss interfaces. No universal entropy-subadditivity proof or physical reserve supplied. Source-bound correction retracts stage2 hash warning: lead used canonical statement+hypotheses JSON, while A018 compared plain statement hashes; mathematical verdicts unchanged and prior runs untouched. Saved four protocol files and receipts; new interface requires independent review. NEXT: {next_action}\n')
learned=(OWN/'LEARNED.md').read_text(encoding='utf8')
learned=learned.replace('Statement text is unchanged; review records preserve announced source hashes and recomputed UTF-8 hashes (which differ), and local statement hashes use the latter.', 'Statement text is unchanged. CORRECTION (stage3): the previous mismatch diagnosis compared different hash recipes; the lead canonical statement+hypotheses JSON hashes are valid. Stage2 local plain-statement hashes do not replace the original source digests; mathematical acceptance is unchanged.')
learned+='''
## Stage 3: shared-separator exact debt and review

A016-CONNECTED-SPINE-FACTOR-REPAIR-CONTROL@1 independently HOLDS without repair, for all a>=1 and even m>=4. The connected ANF prevents a naive factor-removal rescue of its fixed bad-selector-first rule, but querying the paid common separator first gives a normalized complete root reference CE<=8I/3. This refutes that rule/repair, not adaptive C019 or FEI.

For products of arbitrary Boolean modules with exactly one common physical bit z and disjoint private blocks, the joint data marginal is R=(product P_j0+product P_j1)/2. TC=KL(R||product R_j)>=0. Exact entropy correction is H(F)-sum H(f_j)=B_*-sum B_j-TC; posterior costs obey M_*=sum M_j-TC>=0. In particular TC<=sum M_j and H(F)<=sum H(f_j)+1. These elementary identities do not imply a universal influence payment.

For finite-cost normalized complete module references with marginal q_j and selector conditional tau_j, lift Q_*=actual_nu_* product q_j. It is normalized even with zero true rows filled arbitrarily. CE_*=sum CE_j+B_*-sum B_j-sum E_Rj KL(nu_j||tau_j), and residual debt is exactly TC+sum KL(R_j||q_j). Retain B_* explicitly; conditional credits cannot be reused and an exact true-spectrum reference is not a free FEI proof.

If d_j=Inf_z(f_j), the actual product has d_*=(1-product(1-2d_j))/2. Its influence is sum average private branch influence+d_*. Independent module budgets overcount by L=sum d_j-d_*=2 E floor(N_flip/2)>=0. Paying dependence by sum d_j alone is not an exclusive physical reserve.

Finite certificates: 256 ordered k1 module pairs and all 65536 ordered k2 pairs satisfy H(shared product)<=sum module H; no inconclusive signs. Exact TC/B/reference identities on all k2 pairs, four explicit reference fixtures, and five independent A016 fixtures give 394537 checks total. Prime-log identities and outward rational atanh intervals are proof arithmetic; runtime/peak estimates are not theorem evidence. No automatic parameter escalation.

First unsupported all-dimensional line: B_*<=B_1+B_2+TC. Reduce to independent zero-mean posterior biases U_j and e(u)=h2((1+sqrt(1-u^2))/2): E[(1+U1U2)e((U1+U2)/(1+U1U2))]<=E e(U1)+E e(U2)+E[(1+U1U2)log2(1+U1U2)]. Zero weighted rows are ignored. A real-law counterexample still needs Boolean realization. Even a proof leaves loss L and terminal CE payment open. Next analyze this scalar inequality before a two-separator insertion with an owned reserve.

Metadata correction: stage2's B04 lead hash warning was wrong. Lead write_records.py hashes compact sorted JSON containing both exact statement and hypotheses; all three original digests match. Stage2 used plain statement UTF-8. Preserve original runs, supersede the mismatch diagnosis through stage3 HASH_CONVENTION_CORRECTION.json, and leave all three mathematical HOLDS verdicts intact.
'''
(OWN/'LEARNED.md').write_text(learned,encoding='utf8')

# Independent readback of required schemas, digests, files, and final paragraph.
claim_fields=set(protocol['required_per_run']['claim_fields'])
progress_fields={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
claims=read(RUN/'CLAIMS.json')
assert all(set(c)==claim_fields and c['statement_sha256']==plain(c['exact_statement']) for c in claims)
assert set(read(RUN/'PROGRESS.json'))==progress_fields
assert read(RUN/'PACKET_DELTA.json')==read(RUN/'PROGRESS.json')
assert read(RUN/'PROGRESS.json')['packet_ids']==['A018']
assert len((OWN/'STATUS.md').read_text(encoding='utf8').splitlines())==2
report=(RUN/'REPORT.md').read_text(encoding='utf8')
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.rsplit('## ',1)[-1].startswith('Universal bridge\n\n')
files=[p for p in RUN.rglob('*') if p.is_file()]
for p in files:
 assert p.stat().st_size<20*1024*1024
 if p.suffix=='.json':read(p)
save(RUN/'out/PERSISTENCE_RECEIPTS.json',{'status':'PASS','checked_at':NOW,'checks_total':total,'claim_field_sets':'PASS','progress_field_set':'PASS','declared_plain_hashes':'PASS','original_lead_canonical_hashes':'PASS','packet_delta_equal':'PASS','status_two_lines':'PASS','required_report_fields':'PASS','final_universal_bridge':'PASS','json_readback':'PASS','per_file_under_20MB':'PASS','independent_review':'A016 HOLDS; new interface pending','supervisor_adoption':'NOT_VERIFIED','mirror_verification':'NOT_VERIFIED','files':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],'rolling_files':[{'path':str(OWN/n),'sha256':sha(OWN/n)} for n in ('STATUS.md','WORKLOG.md','LEARNED.md')]})
print(json.dumps({'status':'PASS','checks_total':total,'claims':len(claims),'run':str(RUN),'independent_review':'A016 HOLDS; new interface pending','full_fei':'OPEN'}))
