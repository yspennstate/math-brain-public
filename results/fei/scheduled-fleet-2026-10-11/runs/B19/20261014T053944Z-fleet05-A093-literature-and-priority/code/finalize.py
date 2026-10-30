from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1];A=R.parent.parent
old=R.parent/'20261013T234909Z-fleet05-A093-literature-and-priority'
previous=R.parent/'20261014T024314Z-fleet05-A093-literature-and-priority'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
receipts=[]
for p,kind,locator in [
 (old/'out/gmp26.pdf','PRIMARY_PDF','Lemmas 3.5-3.6, Proposition 5.1 and Section5.2, Appendix32'),
 (old/'out/gmp26.txt','PRIMARY_TEXT','Same source passages'),
 (previous/'DERIVATION.md','PRIOR_AUTHOR_PROOF_PENDING_REVIEW','Paid alternative tree with complete terminal entropy'),
 (previous/'CLAIMS.json','PRIOR_CLAIM','A093-GMP26-CLASS-REPAIR v1'),
 (Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),'DISPATCH','Supervisor 2026-10-14 05:31 UTC'),
 (Path(r'~\brain_workers\FEI100_20261011\claude\B19\STREAM_NOTES.md'),'DISPATCH','Unchanged B19 v2'),
 (A/'STATUS.md','DISPATCH','Before this stage update')]:
 b=p.read_bytes();receipts.append({'path':str(p),'kind':kind,'locator':locator,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
save('out/SOURCE_RECEIPTS.json',{'stage_at_utc':now,'sources':receipts,'primary_url':'https://arxiv.org/pdf/2606.00246v2',
 'version_page_checked':'https://arxiv.org/abs/2606.00246','current_version_page_result':'v2 2026-06-09; no withdrawal indicated','raw_page_acquisition':'Viewed with web tool this stage; previous stage also saved raw metadata page'})
claim={'claim_id':'GMP26-PROPOSITION-5.1-SOURCE-AUDIT','version':'arxiv-v2-A093-review1',
 'exact_statement':'For every K>0 there exist n and an actual monotone Boolean F:{-1,1}^{n+1}->{-1,1} with sum_T |Fhat_plus(T)^2-Fhat_minus(T)^2| > K sum_T (Fhat_plus(T)-Fhat_minus(T))^2 at the specified last-coordinate split. This is GMP26 Proposition5.1 at its original stronger-surrogate scope.',
 'hypotheses':['Uniform measure, sign-valued monotone Boolean F','Plus/minus children are physical restrictions at the specified last coordinate','K>0 fixed; dimension may depend on K'],
 'statement_sha256':'','contributors':['Maria Jose Gonzalez','Paul MacManus','Maria Cristina Pereyra'],
 'proof_source':['GMP26 arXiv:2606.00246v2 Proposition5.1, PDF pp18-19','DERIVATION.md, explicit width-three Boolean product spectrum','code/audit_prop51.py','out/VALIDATION.json'],
 'proof_dependencies':[],
 'review_records':[{'reviewer':'A093','reviewed_at_utc':now,'verdict':'HOLDS','scope':'Original V-versus-D Proposition5.1 only; additional true-decrement bounds remain author calculations pending external review',
 'independence':'Explicit product coefficients and exact binomial packet multiplicities; direct Boolean Fourier and influence reproduction instead of the source l1-growth recurrence'}],
 'status':'INDEPENDENTLY_RECONSTRUCTED_AT_SOURCE_SCOPE','supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['B19 lead','A090','A085','A028','A061','A064','A095','A099','A100']}
claim['statement_sha256']=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B19','packet_id':'A093',
 'gap_id':'B19-GMP26-CORRECTION-IMPACT','attempt_id':'A093-proposition51-scope-audit-v1',
 'method':'Independent primary-theorem reconstruction and exact actual-Boolean spectrum; binomial packet compression; analytic true-decrement bounds with terminal retention',
 'mathematical_delta':'Source Proposition5.1 HOLDS at V/D scope; its family also has true Delta/I_z >=(k/4-2k/8^k)log2(7) and <=3k+log2(e)+4. Root-relative node cost <7^(1-k) for k>=2, so this is not a whole-tree obstruction. No new broad pending candidate.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'PUBLISHED_SOURCE_RECONSTRUCTED; QUANTITATIVE_AUDIT_AUTHOR_PROOF_PENDING_EXTERNAL_REVIEW; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':'A093-GMP26-CLASS-REPAIR','version':'v1','statement_sha256':'173599f77b9ce0b630c42026c71119f90cec9fbb9159ef312245331abf77dda3','status':'SOURCE_COMPLETE_PENDING_REVIEW','usage':'Alternative paid-tree rate23 only; not needed by local lower bound'}],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':claim['version'],'kind':'SOURCE_REVIEW_NOT_NEW_BROAD_CANDIDATE'}],
 'source_artifacts':['DERIVATION.md','out/FROZEN_SPEC.json','out/VALIDATION.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A090/A085 reconstruct true-decrement and root-relative estimates; inspect WWW14 primary whole-tree payment and exact terminal assumptions to identify funding for locally bad nodes.',
 'stagnant_substantive_attempts':0,'blockers':['Quantitative audit awaits independent external reconstruction.','Two earlier A093 correction candidates remain pending; no third broad candidate opened.','Universal adaptive/amortized query payment unresolved.'],
 'packet_ids':['A093']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
proto=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf8'))['required_per_run']
assert set(claim)==set(proto['claim_fields'])
assert set(progress)=={v.split(' (')[0] for v in proto['progress_fields']}
text=(R/'REPORT.md').read_text(encoding='utf8')
assert all('## '+v in text for v in proto['report_fields'])
assert text.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
cert=json.loads((R/'out/VALIDATION.json').read_text());assert cert['status']=='PASS'
assert cert['script_sha256']==hashlib.sha256((R/'code/audit_prop51.py').read_bytes()).hexdigest()
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
(A/'STATUS.md').write_text('STATE: A093 GMP Proposition5.1 independently reconstructed; true wrong-selector Delta/I grows linearly, but node Delta/I_root<7^(1-k); k9 exact ratio>4;765 exact checks PASS; audit external review pending; full FEI OPEN.\nNEXT: A090/A085 reconstruct true-decrement bounds; inspect WWW14 primary whole-tree payment and terminal assumptions for funding locally bad nodes; earlier GMP corrections remain pending review.\n',encoding='utf8')
with (A/'WORKLOG.md').open('a',encoding='utf8') as f:
 f.write(f'\n{now} | {R.name}: Read board05:31/B19/status and resumed source obstruction audit. Width-three tribes actual point-deletion family proves B/I_z >=(k/4-2k/8^k)log2(7), true Delta/I_z <=3k+log2(e)+4; root-relative cost<7^(1-k). Source V/D grows exponentially and original Proposition5.1 HOLDS. Exact k9 ratio>150994935/33554432>4;765 checks PASS including compressed laws k<=12 and retained terminals k<=3. No third broad pending candidate; source review recorded, quantitative audit pending external review. All protocol/rolling files saved locally.\n')
with (A/'LEARNED.md').open('a',encoding='utf8') as f:
 f.write('\n'+now+' | GMP wrong-variable scope: OR of k AND3 blocks, boundary deletion minus child, epsilon8^-k. I_z=epsilon; nonempty coefficient abs=2epsilon7^j with j missed blocks. True Delta/I_z >=(k/4-2k/8^k)log2(7) and <=3k+log2(e)+4. V/D>=2(7/4)^k-3. Yet I_root=(3k/4)(7/8)^(k-1)+epsilon(3k-5), so Delta/I_root<7^(1-k) for k>=2. Local-rate failure is not aggregate stopping-tree failure. Exact compressed counts N_j=C(k,j)7^(k-j), S_j=7C(k-1,j)-C(k-1,j-1), sign multiplicities(N_j+-S_j)/2. Preserve terminal H/G on the alternative shared-block tree. No general novelty/priority claim.\n')
entries=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20_000_000
  entries.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/ARTIFACT_RECEIPTS.json',{'saved_at_utc':now,'validation':'PASS: exact field sets, report headings, claim hash, packet compatibility, certificate hash, file size limit','files':entries,'local_only':True,'quantitative_audit_externally_reviewed':False,'remote_verified':False})
print(json.dumps({'status':'PASS','files_pinned':len(entries),'exact_assertions':cert['exact_assertions'],'claim_sha256':claim['statement_sha256'],'rolling_files_updated':True}))
