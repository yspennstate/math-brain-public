from pathlib import Path
import hashlib,json,datetime

R=Path(__file__).resolve().parents[1]; AGENT=R.parents[1]
P=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(path,obj): path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
registry=json.loads((P/'CLAIM_REGISTRY.json').read_text(encoding='utf-8-sig'))
original=next(c for c in registry['claims'] if c['claim_id']=='B09-BIASED-BLOCK-UNCERTAINTY')
claim={field:original.get(field) for field in protocol['required_per_run']['claim_fields']}
claim['contributors']=['account01/B09 original construction']
claim['review_records']=[{'reviewer':'A093 account05 B19','verdict':'ACCEPT_AT_STATED_SCOPE_CORE_ONLY','source':'REPORT.md; out/VALIDATION.json; PRIMARY_SOURCE_OVERLAP.md','method':'Primary Maassen-Uffink theorem matched to physical normalized fibers; independent rational child-marginal implementation','date_utc':now,'scope_exclusions':['No uniform influence payment','No claim of optimal tax','No broad substitution additivity','No new interval-certificate acceptance']}]
claim['status']='ANALYTICALLY_PROVED_INDEPENDENTLY_REVIEWED_CORE_ONLY'
claim['proof_dependencies']=[{'source':'Maassen-Uffink 1988, Phys Rev Lett 60 1103-1106','locator':'equations (5)-(6); Riesz step (10)-(13)','url':'https://www.math.ru.nl/~maassen/papers/EntrUncert.pdf','saved_file':'out/maassen_uffink_1988.pdf'}]
claim['first_unproved_line']=None
claim['supersedes']=[];claim['refutes']=[]
expected=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert expected==claim['statement_sha256']
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
dump(R/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B19','packet_id':'A093',
 'gap_id':'G-BIASED-TAX','attempt_id':'A093-primary-source-audit-1',
 'method':'Theorem-level primary version comparison and independent uncertainty specialization',
 'mathematical_delta':'B09 core v1 accepted independently at scope; primary corrections/withdrawal and local percolation statement discrepancy pinned; no universal influence payment or priority claim.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF',
 'mathematical_status':'CORE_DEPENDENCY_REVIEWED_FULL_FEI_OPEN',
 'claim_versions_used':['B09-BIASED-BLOCK-UNCERTAINTY v1','O-Donnell-Tan 1304.1347v1','GPS 0803.3750v4','KMS 1105.2651v1'],
 'claims_created_or_changed':['Independent core-only review record for B09-BIASED-BLOCK-UNCERTAINTY v1; statement hash unchanged'],
 'source_artifacts':['REPORT.md','CLAIMS.json','PRIMARY_SOURCE_OVERLAP.md','CITATION_STATUS.json','code/audit.py','out/FROZEN_SPEC.json','out/VALIDATION.json','out/SOURCE_INVENTORY.json','out/PRIMARY_RECEIPTS.json'],
 'next_consumers':['A041','A069','A095','A099','A100','A081','A096','A097','B20'],
 'next_action':'Consume accepted B09 core in a nonreusing stopping-tree ledger; A090 reconstruct GPS pivotal-bound transfer including boundary clusters before unconditional overlap adoption.',
 'stagnant_substantive_attempts':0,
 'blockers':['B19 STREAM_NOTES.md absent at supplied path; independent packet work completed','No authoritative ordering established between same-date 30pp and 31pp percolation versions','External adoption and mirror verification pending'],
 'packet_ids':['A093']}
progress_keys={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
# The schema catalog annotates packet_ids with a parenthetical description;
# protocol.compatibility.run_delta specifies the actual JSON key packet_ids.
assert set(progress)==progress_keys
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
citations={
 'retrieved_at_utc':now,'priority_verdict':'NOT_ASSERTED_BOUNDED_COVERAGE',
 'revision_order_policy':'Explicit revision history or immutable provenance, never page count',
 'sources':[
 {'key':'MU1988','version':'Final published article 21 March 1988','locator':'pp1103-1104 eq5-6,10-13','url':'https://www.math.ru.nl/~maassen/papers/EntrUncert.pdf','read':'Visual primary pages 1-2','status':'Valid finite uncertainty input; no erratum identified in targeted search'},
 {'key':'OT2013','version':'arXiv1304.1347v1; author PDF separately hashed','locator':'Theorems1-3; Section3','url':'https://arxiv.org/abs/1304.1347v1','read':'Primary theorem/definition/identity sections','status':'Established disjoint composition; no first-result claim for campaign'},
 {'key':'CKLS2013','version':'ECCC TR13-052 revisions1 and2','locator':'rev1 Lemma5.4 Theorem5.5; rev2 Corollary4.8 and revision notice','url':'https://eccc.weizmann.ac.il/report/2013/052/','read':'Primary old theorem, replacement theorem and explicit revision notice','status':'Use revision2 corrected O(sqrt(n)) statement; paper not withdrawn'},
 {'key':'WWW2013','version':'1312.3003v1 11 December2013','locator':'Abstract and submission history','url':'https://arxiv.org/abs/1312.3003v1','read':'Metadata/abstract only','status':'Coding/read-k antecedent; full proof not independently reviewed'},
 {'key':'RandomLTF','version':'1903.11635 abstract record','locator':'Abstract','url':'https://arxiv.org/abs/1903.11635','read':'Abstract only','status':'Random-model scope; insufficient for latest-priority verdict'},
 {'key':'KMS2011','version':'1105.2651v1 submission13May2011; fetched PDF internally displays22October2018','locator':'Claim4.1 p10, first inequality and proof','url':'https://arxiv.org/pdf/1105.2651v1','read':'Primary claim and proof','status':'Marginal subadditivity antecedent; normalization to unit L2 required for real-valued f'},
 {'key':'LiHan2025','version':'2512.03117v3 withdrawn9December2025; v2 also withdrawn','locator':'Withdrawal notice, comments and revision history','url':'https://arxiv.org/abs/2512.03117v3','read':'Primary withdrawal record; old proof not used','status':'Prior appearance in KMS Claim4.1; withdrawal is priority correction'},
 {'key':'GPS2013','version':'0803.3750v4 6February2013','locator':'Correction notice; Remarks1.7/4.6','url':'https://arxiv.org/abs/0803.3750v4','read':'Primary correction and pivotal transfer remarks','status':'Section4.4 corrected; full pivotal boundary/clustering transfer not reconstructed'},
 {'key':'ThresholdLocal','version':'29pp and38pp same cover date11October2026','locator':'TheoremA; 38pp Corollary7.2 Proposition8.6 Corollaries8.7-8.8','url':None,'read':'Relevant theorem/identity/proof sections; byte-hashed local inputs','status':'Creg13.415 versus8.937; no proof/priority acceptance of entire manuscript'},
 {'key':'PercolationLocal','version':'30pp and31pp same cover date11October2026','locator':'Theorem1.6; Section9.3','url':None,'read':'Both statements and dependency-bearing proof steps','status':'Unconditional versus conditional overlap11/12; order unresolved'}]}
dump(R/'CITATION_STATUS.json',citations)
(AGENT/'STATUS.md').write_text('STATE: A093 source audit complete locally; B09 core v1 independently accepted at scope; revisions/withdrawal and percolation dependency discrepancy pinned; 1,729 exact assertions PASS; full FEI OPEN.\nNEXT: A090/A085 review source audit; consume B09 core in nonreusing C019 tree payment; reconstruct pivotal-bound boundary transfer before unconditional overlap adoption.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+' — Read protocol/board and source contracts; lead notes absent. Compared primary MU, OT, CKLS revisions, GPS correction and KMS/Li-Han withdrawal. Reconstructed B09 core without repair, retaining necessity/composition objections. Identified percolation local-version dependency difference. Fixed legacy text decoding with cp1252. Frozen Fraction census:432 cases/1729 assertions PASS. Saved local handoff; no external copying or adoption claimed.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\n'+now+'\n- B09 core is a valid finite orthogonal MU specialization; its uncertainty theorem leaves global conditional-entropy and tax payment open.\n- CKLS TR13-052 rev2 removes inaccuracies in Lemma5.4/Theorem5.5; retain O(sqrt(n)) LTF result, not old abstract all-LTF FEI.\n- Li-Han2512.03117v3 withdrawn for KMS Claim4.1 priority overlap; natural-unit marginal entropy bound is not full FEI.\n- GPS0803.3750v4 corrects Section4.4. Its Remark4.6 states pivotal six-arm analogue; boundary/clustering reconstruction remains separate.\n- Local 30pp/31pp percolation Theorem1.6 differs unconditional/conditional; equal dates and page count do not determine revision order.\n- Local texts require cp1252 and lose math glyphs; primary PDF controls exact formula.\n')
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
receipts=[]
for path in sorted(R.rglob('*')):
 if path.is_file() and path.name!='PERSISTENCE_RECEIPTS.json':
  data=path.read_bytes();assert len(data)<20*1024*1024
  receipts.append({'path':str(path.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump(R/'out/PERSISTENCE_RECEIPTS.json',{'saved_at_utc':now,'location':str(R),'schema_validation':'PASS','compatibility_copy':'IDENTICAL','files':receipts,'mirror_status':'PENDING_SUPERVISOR_COPY'})
print(json.dumps({'schema':'PASS','files':len(receipts),'claim_statement_hash':expected,'local_save':'COMPLETE'}))
