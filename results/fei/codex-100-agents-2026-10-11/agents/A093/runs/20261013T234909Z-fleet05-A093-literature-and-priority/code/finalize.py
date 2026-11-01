from pathlib import Path
import json, hashlib, datetime
R=Path(__file__).resolve().parents[1]
A=R.parent.parent
def save(name,value): (R/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
claim={
 'claim_id':'A093-GMP26-CONSTANT-CORRECTION','version':'v1',
 'exact_statement':'For uniform Boolean f, GMP26 v2 Corollary 4.2 cannot replace Delta_i H<=K I_i by E_i<=K I_i with the same K: two-variable AND at K=2 has Delta_i H=2, E_i=1, I_i=1/2. Its printed (20) binary-entropy bound fails at t=1/2. Retaining R_i gives Delta_i H=E_i+R_i, 0<=R_i<=4I_i, hence E_i<=K I_i implies Delta_i H<=(K+4)I_i.',
 'hypotheses':['f:{-1,1}^n->{-1,1}, uniform measure','Entropy in bits; influence I_i=sum_{S containing i} fhat(S)^2','E_i=sum_T (a_T^2+b_T^2)/2 * h2((a_T-b_T)^2/(2(a_T^2+b_T^2))); zero fibers omitted','a_T and b_T are Fourier coefficients of the plus/minus restrictions'],
 'statement_sha256':'', 'contributors':['A093'],
 'proof_source':['REPORT.md, complete derivation','code/check_witness.py','out/EXACT_WITNESS.json','out/gmp26.pdf, (20), Corollary 4.2, Appendix (32)'],
 'proof_dependencies':[], 'review_records':[], 'status':'SOURCE_COMPLETE_PENDING_REVIEW',
 'supersedes':[], 'refutes':['GMP26 arXiv:2606.00246v2 equation (20) as printed','GMP26 arXiv:2606.00246v2 Corollary 4.2 same-K replacement'],
 'first_unproved_line':None,
 'next_consumers':['B19 lead','A090','A085','A041','A069','A095','A099','A100']}
claim['statement_sha256']=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
save('CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B19','packet_id':'A093',
 'gap_id':'B19-PRIMARY-RESTRICTION-OVERLAP','attempt_id':'A093-restriction-priority-v1',
 'method':'Primary version/theorem comparison; exact Boolean source counterexample; algebraic refund repair',
 'mathematical_delta':'CKLS Lemma 3.2 restriction inequality and GMP Appendix (32) identity located; same-K GMP replacement refuted exactly; safe +4 query-influence repair derived; bounded all-LTF overlap comparison completed without priority superlatives.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_SOURCE_CORRECTION_PROVED_PENDING_INDEPENDENT_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':[], 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':'v1'}],
 'source_artifacts':['PRIMARY_SOURCE_OVERLAP.md','CITATION_STATUS.json','out/PRIMARY_RECEIPTS.json','out/ADDITIONAL_RECEIPTS.json','out/EXACT_WITNESS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A090/A085 independently reconstruct source constants; rebuild C019 stopping-tree payment retaining E_i+R_i and terminal entropy.',
 'stagnant_substantive_attempts':0,'blockers':['Global first-result/latest-best priority not established by bounded screening.','Independent review and downstream adoption not yet recorded.'],
 'packet_ids':['A093']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
save('CITATION_STATUS.json',{
 'audited_at_utc':now,'scope':'Named primary versions, theorem statements and bounded 2025-2026 screening; no exhaustive priority claim',
 'restriction_bound':{'source':'CKLS ECCC TR13-052 revision 2 Lemma 3.2','status':'EXPLICIT_SINGLETON; BLOCK_BY_ITERATION'},
 'one_coordinate_identity':{'source':'GMP26 v2 Appendix (32)','status':'EXPLICIT_AFTER_COEFFICIENT_CHANGE'},
 'GMP_correction':{'versions_checked':['2606.00246v1','2606.00246v2'],'status':'SAME_K_SUBSTITUTION_AND_PRINTED_ENTROPY_BOUND_FAIL; TRUE_DECREMENT_TELESCOPE_RETAINED'},
 'CKLS_correction':{'status':'REVISION_2_GOVERNS; OLD_ALL_LTF_CLAIM_NOT_ADOPTED','url':'https://eccc.weizmann.ac.il/report/2013/052/'},
 'Han_priority_note':{'version':'2312.08271v2','revised':'2025-12-10','status':'NOTE_ADDED_ACKNOWLEDGES_KMS12; NO_WITHDRAWAL_INDICATED_ON_VERSION_PAGE'},
 'LTF_comparison':{'read_statement_comparators':['CKLS corrected Corollary 4.8','CKKLS Theorem 1 and Corollaries 10,15,16','Han Theorem 1','Potapov Theorems 1,2','Chang Theorem 1','Fang-Wang Theorem 4'],
 'result':'No read statement equals local all-LTF Theorem A; first and best remain uncertified'},
 'negative_search_standard':'Not located in focused passages/keyword scan; not a universal absence claim'})
# Persist the exact additional acquisition/extraction commands as regeneration recipes.
save('out/REGENERATION.json',{
 'primary_command':'python -X utf8 code/fetch_sources.py',
 'witness_command':'python -X utf8 code/check_witness.py',
 'additional_sources':[
 {'url':'https://arxiv.org/pdf/2608.27908v1','file':'out/fangwang26.pdf','recipe':'urllib.request.urlopen(url,timeout=20).read(); save PDF; fitz.open(stream=bytes,filetype="pdf"); extract page.get_text() with PDF page markers'},
 {'url':'https://arxiv.org/pdf/2606.00246v1','file':'out/gmp26_v1.pdf','recipe':'same urllib/fitz extraction; exact bytes pinned by ADDITIONAL_RECEIPTS.json'}],
 'image_recipe':'python -X utf8 -c "import fitz; d=fitz.open(\'out/gmp26.pdf\'); d[15].get_pixmap(matrix=fitz.Matrix(1,1)).save(\'out/gmp_page16.png\')"'})
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf8'))
fields=protocol['required_per_run']
assert set(claim)==set(fields['claim_fields'])
assert set(progress)=={f.split(' (')[0] for f in fields['progress_fields']}
report=(R/'REPORT.md').read_text(encoding='utf8')
assert all('## '+field in report for field in fields['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
assert json.loads((R/'out/EXACT_WITNESS.json').read_text())['status']=='PASS'
(A/'STATUS.md').write_text('STATE: A093 restriction/literature audit saved; CKLS/GMP overlap pinned; GMP same-K substitution refuted by exact AND2 witness, safe +4I repair; 25 exact checks PASS; independent review pending; full FEI OPEN.\nNEXT: A090/A085 reconstruct source constants; B19/A095 retain full E_i+R_i and terminal entropy in C019 stopping-tree payment; no first/latest-best claim.\n',encoding='utf8')
with (A/'WORKLOG.md').open('a',encoding='utf8') as f:
 f.write(f'\n{now} | {R.name}: Read board/lead/status and resumed restriction priority assignment. Pinned nine primary papers plus GMP v1; CKLS Lemma 3.2 supplies +2 restriction bound, GMP (32) supplies full identity. AND2 refutes same-K Corollary 4.2 and t=1/2 refutes printed (20); 25 Fraction checks pass. Derived +4I safe refund repair. Corrected preliminary dictator interpretation before persistence. No priority superlatives; local stage artifacts saved; independent review pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf8') as f:
 f.write('\n'+now+' | GMP26 v1/v2: true decrement = E_i+R_i, R_i>=0 and <=4I_i by the binary-entropy series. Two-bit AND has Delta=2, E=1, R=1, I_i=1/2, refuting same-K replacement at K=2. A dictator has Delta=0 and is NOT a witness. Printed h(t)<=sqrt(t(1-t)) fails at 1/2. Stopping-tree telescope survives with true decrement. CKLS corrected Lemma3.2 explicitly gives +2; its all-LTF result is only O(sqrt n). Han v2 acknowledges KMS12; CKKLS regularity means small maximum weight. Bounded screening cannot establish first-result or latest-best priority.\n')
entries=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000,p
  entries.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/ARTIFACT_RECEIPTS.json',{'saved_at_utc':now,'local_only':True,'files':entries,'validation':'PASS: exact fields, claim hash, report headings, packet compatibility, witness, file sizes','mirror_verified':False,'independent_review_complete':False})
print(json.dumps({'status':'PASS','files_pinned':len(entries),'claim_sha256':claim['statement_sha256'],'exact_assertions':25,'rolling_files_updated':True}))
