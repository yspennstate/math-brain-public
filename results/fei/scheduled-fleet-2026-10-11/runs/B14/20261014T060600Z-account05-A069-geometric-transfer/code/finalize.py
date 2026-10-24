from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1];ROOT=A.parents[1]
P=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
review=ROOT/'agents/A070/runs/20261014T034205Z-account05-A070-analytic-route-referee'
flagreview=ROOT/'agents/A088/runs/20261014T053751Z-account05-A088-booleanity-referee'
leadsrc=ROOT/'agents/A067/runs/20261014T044841Z-account05-A067-hypercontractive-refinement'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
protocol=json.loads(P.read_text(encoding='utf-8-sig'))
res=json.loads((R/'out/CHECK.json').read_text());hist=json.loads((R/'out/HISTORY.json').read_text())
assert res['status']==hist['status']=='PASS' and res['cases']==6403 and hist['cases']==256
assert res['elapsed_seconds']<55 and hist['elapsed_seconds']<55
accepted=json.loads((review/'CLAIMS.json').read_text())[0]
flag=json.loads((flagreview/'CLAIMS.json').read_text())[0]
assert accepted['claim_id']=='A069-SOURCE-BLIND-SHARED-EDGE-TRANSFER' and accepted['review_records']
assert flag['claim_id']=='A067-BOOLEAN-FLAG-FOUR-BRANCH-FINAL-REFERENCE' and flag['review_records']
dep={'claim_id':flag['claim_id'],'version':1,'statement_sha256':flag['statement_sha256'],'scope':'ONLY universal Boolean h2(control-tail mass)<=2I; proof reproduced in DERIVATION Section4','acceptance':'Independent A088 full-scope acceptance without repair','source':str(flagreview/'CLAIMS.json')}
statement=('On disjoint uniform coordinates c,u,Z,Y with |Z|=m>=1 and |Y|>=1, let four arbitrary Boolean Y cores define G(c,u,Y), q1=1-2*1{c=c*,u=u*}, q2=1-2*1{c=c*,Z=z*}, g=q1G and q=q1q2, so F=gq=q2G. For any single positive normalized common core reference R_Y and B=average_cu C_R(h_cu), a complete normalized product final reference Q has H(F)<=C_Q(F)<=B+2I_Y(F)+4I_{c,u}(F)+(4+log2(20/7))I_Z(F). R_Y is retained unchanged, B is the actual final terminal average, and source/final core marginals coincide. If each C_R(h_cu)<=K I(h_cu), H(F)<=max(K+2,4+log2(20/7))I(F), with 4+log2(20/7)<28/5. The output-only q2=1 case is included. After any one actual core query i, carry R_Y by frequency marginalization to the SAME reference Rprime for all actual child cores and update only actual child flag priors: the complete reference decrement equals sum_T P_F(S_Y=T)log2(Rprime(T minus i)/R_Y(T)) plus h2(alpha)-average h2(alpha_child). For every K the signed ledger is K I(F)-C_Q(F)=average_child[K I(child)-C_Qchild(child)]+K Inf_i(F)-Delta C_Q. No positivity of its final signed term, universal paid core references or same-constant induction is asserted.')
hyp=['Finite uniform cubes, actual Boolean signs; entropy/reference costs bits and ordinary physical influences.',
 'Source cancellation normal form g=q1G with G independent of the remaining private Z; arbitrary four unequal Y cores.',
 'ONE common positive normalized R_Y supplied before the Fourier sample, retained across all actual source/final core terminals; separate entropy bounds cannot substitute.',
 'Five fixed control cells cover all nonempty subsets, including unoccupied cells; weights1/4,1/4,1/16,7/20,7/80; only final empty/nonempty prior depends on alpha.',
 'Zero/one tail endpoints use normalized supported laws and zero-mass continuity, not deletion of a positive output row.',
 'Paid common-reference core inequalities are additional hypotheses; constants remain included in the retained-B statement.',
 'Core query carries the same marginal reference to both actual children and preserves signed query budget; no independently available or renewed child reserve is assumed.']
claim={'claim_id':'A069-EXPOSED-CANCELLATION-COMMON-REFERENCE-HISTORY','version':1,'exact_statement':statement,'hypotheses':hyp,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['account05/A069; Boolean global flag lemma credited to A067 and independent A088 review'],
 'proof_source':{'path':str(R/'DERIVATION.md'),'sha256':sha(R/'DERIVATION.md'),'locators':'Sections1-6, equations(1)-(11)'},
 'proof_dependencies':[dep],'review_records':[],'status':'NARROW_SCOPED_TRANSFER_AUTHOR_PROVED_EXACT_CHECKS_PASS_PENDING_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':None,'next_consumers':['A070','A088','A094','A067','A096','B14','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields']);save(R/'CLAIMS.json',[claim])
nxt='At an actual Y query price signed K*Inf_i minus complete reference decrement from one unused SAME-core-reference child surplus; retain both terminals and five-cell law, first on nonfactorizing Maj3/literal branches, without renewing the global flag reserve.'
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B14','packet_id':'A069','gap_id':'G-A069-STABLE-ENCODING','attempt_id':'A069-stage5-exposed-cancellation-final-reference',
 'method':'Exact cancellation normal form; five uniform spectral cells with normalized nonuniform label weights; inherited common core reference and one actual query history; integer Walsh/rational and exact prime-log certificates',
 'mathematical_delta':'C020 final exposed-event reference preserves complete terminal B, pays2I_Y+4I_cu+(4+log2(20/7))I_Z (<5.6 control coefficient). C024 exact common-reference physical core-query decrement and signed ledger. Universal unused child surplus remains open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT; NEW_REVIEW_AND_EXTERNAL_COPIES_PENDING','mathematical_status':'SCOPED_THEOREM_AUTHOR_PROVED; FULL_FEI_OPEN',
 'claim_versions_used':[dep,{'claim_id':accepted['claim_id'],'version':1,'statement_sha256':accepted['statement_sha256'],'use':'A070 independent full-scope acceptance consumed, no repair'},
 {'claim_id':'A070-PARTIAL-PRIVACY-TRANSFER-AND-EXPOSED-EVENT-BOUNDARY','version':1,'statement_sha256':'eaebf2e1dcbac52e3dd1b9f973df942d95583a470633eef85fb9a43fe49a7b0f','use':'Consumed full-exposure obstruction and A067 independent acceptance; not a paid ancestral budget dependency'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','FROZEN_SPEC_V2.json','FROZEN_HISTORY_SPEC.json','code/check.py','code/check_v1.py','code/history.py','out/PILOT_V1.json','out/CHECK.json','out/HISTORY.json','out/REVIEW_RECEIPTS.json','out/SOURCE_MANIFEST.json'],
 'next_consumers':claim['next_consumers'],'next_action':nxt,'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A069']}
assert set(progress)=={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
save(R/'out/REVIEW_RECEIPTS.json',{'previous_stage4':{'claim_id':accepted['claim_id'],'statement_sha256':accepted['statement_sha256'],'review_records':accepted['review_records'],'claims_sha256':sha(review/'CLAIMS.json')},'used_flag':{'claim_id':flag['claim_id'],'statement_sha256':flag['statement_sha256'],'review_records':flag['review_records'],'claims_sha256':sha(flagreview/'CLAIMS.json')},'new_stage_review':'PENDING'})
sources=[P,ROOT/'BOARD.md',ROOT/'claude/B14/STREAM_NOTES.md',review/'DERIVATION.md',review/'CLAIMS.json',leadsrc/'DERIVATION.md',leadsrc/'CLAIMS.json',flagreview/'CLAIMS.json']
save(R/'out/SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'hash_time':'finalization'} for p in sources])
report=(R/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('This stage moves C020')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
save(R/'out/SCHEMA_CHECK.json',{'claim_fields':'PASS','progress_fields':'PASS','report_fields':'PASS','canonical_statement_hash':'PASS','compatibility_copy':'IDENTICAL','main_cases':res['cases'],'main_assertions':res['exact_assertions'],'history_cases':hist['cases'],'history_assertions':hist['exact_assertions']})
(A/'STATUS.md').write_text('STATE: A069 stage5 complete: exposed cancellation final reference preserves actual terminal B, control coefficient<28/5; SAME-reference core-query signed ledger; 6403 cases/463814 main plus256/2817 history checks PASS; stage4 accepted by A070; FEI OPEN.\nNEXT: A070/A088 review; pay signed KInf_i-Delta complete reference from one unused SAME-core-reference child surplus at an actual Y query, keeping both terminals and original five-cell law; no renewed global flag bank.\n',encoding='utf-8')
marker='2026-10-14 06:06 UTC stage 5:'
if marker not in (A/'WORKLOG.md').read_text():
 with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(marker+' Read new board/B14 lead and A070/A067/A088 source reviews; stage4 accepted by A070. Consumed partial-privacy/full-exposure obstruction. Proved final exposed-event five-cell normalized reference preserving SAME common core R and both/four actual terminal bills, with control coefficient4+log2(20/7)<28/5. Original checker first fixture exposed normalization implementation error; preserved and fixed to multiplier2 before same-domain rerun. Main6403 cases/463814 assertions PASS10.8619843s; physical core query exact common-reference decrement/signed ledger256 cases/2817 assertions PASS0.587872s. Universal2I_Y and signed unused child slack remain open; new independent review/mirrors pending.\n')
fact='Stage 5 exposed cancellation common reference:'
if fact not in (A/'LEARNED.md').read_text():
 with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
  f.write(fact+' For g=q1G(c,u,Y), q=q1q2, F=q2G, where q1 exposes c,u and q2 is a point event on c,Z, original/final core marginal and SAME common core reference cost B coincide exactly. Arbitrary four unequal cores allowed; do not try to bound canceled ancestral influence bill.\n')
  f.write('Control subsets form three visible singleton cells and two flat nonempty-Z cells with fixed u membership. Normalized weights1/4,1/4,1/16,7/20,7/80 absorb singleton costs and u-membership into2degree. Remaining log2(20/7) is charged only to Z. Complete final reference cost<=B+2I_Y+4I_cu+(4+log2(20/7))I_Z, coefficient<28/5. This assumes a common R_Y, not four unrelated H<=KI statements; retained2I_Y is still unpaid for same-C recursion.\n')
  f.write('Physical Y query carries R_Y by frequency marginalization to SAME Rprime for all cores/both children. Full reference decrement equals expected conditional core-reference cost plus binary JS of actual tail priors. Exact ledger KI-C=avg(KI_child-C_child)+KInf_i-DeltaC; nonnegative decrement is not a positive query budget or newly unused child slack.\n')
  f.write('Maj3,y0,-y0,-Maj3 on one 3-bit tree with Kraft sum13/16 are genuinely nonfactorizing four branches paid by common K3; resulting family H<(28/5)I for all private widths. No universal source reference or private-Z row flatness asserted.\n')
assert len((A/'STATUS.md').read_text().splitlines())==2
files=sorted(p for p in R.rglob('*') if p.is_file() and p.name!='RECEIPTS.json')+[A/n for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]
for p in files:assert p.stat().st_size<20_000_000
save(R/'out/RECEIPTS.json',{'scope':'LOCAL_ONLY; new independent review, supervisor copy, registry and mirrors pending','files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]})
print(json.dumps({'schema':'PASS','main_cases':res['cases'],'main_assertions':res['exact_assertions'],'history_cases':hist['cases'],'history_assertions':hist['exact_assertions'],'statement_sha256':claim['statement_sha256'],'receipts_sha256':sha(R/'out/RECEIPTS.json')},indent=2))
