from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def save(name,obj):
    (ROOT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
statement='For every n>=1 and every fresh disjoint block partition of n, the nested constant-seed activation tower is the Boolean point defect f_n=1-2*1{x=0}, with I=2n*2^(-n), H<=4I and H/I tending to 4. Every complete one-coordinate restriction tree, with irrelevant queries skipped, has blind exact-minority surcharge R=2^(-n)n(n-1), hence R/I=(n-1)/2. Retaining the exact base-two KL rebate gives Q<=2I and, for n>=2, 1-1/n<=Q/I<=1+3/n, hence Q/I tends to 1. For disjoint products and sequential factor trees, H,I,R,Q add.'
claim=dict(claim_id='A077-MULTISCALE-MINORITY-KL-LEDGER',version=1,exact_statement=statement,hypotheses=['uniform independent physical bits','Boolean sign outputs','fresh disjoint activation blocks and constant negative seed','entropy and KL in bits','M is the sum of smaller parent spectral masses in each residual fiber','full one-coordinate physical restriction tree; zero-M terms vanish','tensor extension uses disjoint variable blocks and sequential factor trees'],statement_sha256=sha(statement.encode()),contributors=['A077/account05'],proof_source='REPORT.md; SPARSE_DEFECT_TOWERS.tex; code/check.py; out/validation.json',proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_EXACT_CHECKED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=['blind universal sum_v w_v M_v log2(1/M_v)<=K I(f), for any absolute finite K, even after optimizing complete coordinate order'],first_unproved_line=None,next_consumers=['A022','A023','A064','A075','A080','A092','A088','B20'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',[claim])
progress=dict(protocol_revision=protocol['revision'],run_id=ROOT.name,stream='B16',packet_id='A077',gap_id='G-R-MISMATCH',attempt_id='A077-G-R-MISMATCH-01',method='exact fresh-block sparse-defect tower spectra, complete physical restriction ledger and explicit KL calculation',mathematical_delta='Blind actual-minority surcharge is coordinate-order-independent and has R/I=(n-1)/2; exact KL correction has Q<=2I and Q/I->1. Cross-scale activation interference is computed by Boolean collapse; disjoint tensor control is explicit.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='RESTRICTED_MULTISCALE_NO_GO_AND_PAYMENT_PROVED_FULL_FEI_OPEN',claim_versions_used=[],claims_created_or_changed=['A077-MULTISCALE-MINORITY-KL-LEDGER-v1'],source_artifacts=['REPORT.md','SPARSE_DEFECT_TOWERS.tex','FROZEN_SPEC.json','MULTISCALE_COST_LEDGER.json','code/check.py','out/validation.json','out/SOURCE_RECEIPTS.json'],next_consumers=claim['next_consumers'],next_action='Compute retained-KL Q with bent-core point-surgery terminal seeds across fresh activation levels, retaining physical history weights and terminal entropy.',stagnant_substantive_attempts=0,blockers=['B16 STREAM_NOTES.md absent at supplied path; independent review and supervisor mirror not performed'],packet_ids=['A077'])
# The protocol annotates its packet_ids field with a parenthetical description.
# Its compatibility instructions and owner request explicitly name the key packet_ids.
expected_progress={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
v=json.loads((ROOT/'out/validation.json').read_text())
save('MULTISCALE_COST_LEDGER.json',dict(claim_id=claim['claim_id'],units='bits',family='nested point-defect activation towers on disjoint controls',all_dimension_formulas={'defect_probability':'2^(-n)','influence':'2*n*2^(-n)','raw_tree_cost':'2^(-n)*n*(n-1)','raw_ratio':'(n-1)/2','residual_minor_mass':'M=2^(-(m-1)) for m>=2; M=0 for m=1','residual_history_weight':'2^(-(n-m))','rebated_per_minor_mass':'1-M+2*M*(m-1)+M*log2(1-2*M+2*M^2)','corrected_cost':'2^(1-n)*sum_(m=2)^n a_m','corrected_ratio_bounds':'1-1/n <= Q/I <= min(2,1+3/n), n>=2'},verified_rows=v['rows'],tensor_controls=v['tensors']))
source_paths=[]
p=Path(r'~\mop_fei100\reports\fei-2026-10-11')
source_paths += [p/s for s in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
source_paths += list((p/'runs').rglob('REPORT.md'))
p=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
source_paths += [p/s for s in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','SOURCES_README.md']]
source_paths += list((p/'sources').glob('*.md'))
p=Path(r'~\brain_workers\FEI100_20261011')
source_paths += [p/'BOARD.md']+list((p/'context').glob('*.txt'))
save('out/SOURCE_RECEIPTS.json',{'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':[dict(path=str(f),bytes=f.stat().st_size,sha256=sha(f.read_bytes())) for f in source_paths],'missing':['~/brain_workers/FEI100_20261011/claude/B16/STREAM_NOTES.md'],'note':'Source receipts identify local bytes; inspection scope and theorem locators are in REPORT.md. These are not mirror or independent-review receipts.'})
files=[f for f in ROOT.rglob('*') if f.is_file() and f.name!='ARTIFACT_MANIFEST.json']
assert all(f.stat().st_size<20_000_000 for f in files)
save('out/ARTIFACT_MANIFEST.json',{'files':[dict(path=str(f.relative_to(ROOT)),bytes=f.stat().st_size,sha256=sha(f.read_bytes())) for f in files]})
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
report=(ROOT/'REPORT.md').read_text()
assert all(s in report for s in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
print(json.dumps({'claim_fields':'exact protocol schema','progress_fields':'exact protocol schema','delta_equal':True,'artifact_files':len(files),'largest_bytes':max(f.stat().st_size for f in files),'claims':1,'assertions':v['assertions']}))
