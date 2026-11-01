from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
TEAM=AGENT.parents[1]
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
def save(path,value):path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
validation=json.loads((ROOT/'out/VALIDATION.json').read_text())
assert validation['status']=='PASS' and validation['composed_slice_cases']==120
sources=[PROTO,TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md',
 TEAM/'agents/A026/runs/20261013T214810Z-fleet05-A026-good-coordinate-erasure/REPORT.md',
 TEAM/'agents/A026/runs/20261013T214810Z-fleet05-A026-good-coordinate-erasure/CLAIMS.json',
 TEAM/'agents/A026/runs/20261013T214810Z-fleet05-A026-good-coordinate-erasure/PROOF.md',
 TEAM/'agents/A004/runs/20261012T030039Z-fleet05-A004-constant-and-unit-ledger/REPORT.md',
 AGENT/'runs/20261012T005637Z-fleet05-A003-minimal-target-formulation/code/finalize.py']
save(ROOT/'out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources])
claims=[]
def claim(cid,statement,hypotheses,locator,deps):
 item=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hypotheses,
 statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 contributors=['A003'],proof_source={'run_id':ROOT.name,'path':'DERIVATION.md','locator':locator,'validation':'out/VALIDATION.json'},
 proof_dependencies=deps,review_records=[],status='SCOPED_AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,
 next_consumers=['A026','A057','A087','A094','B01','B06','B20'])
 assert set(item)==set(protocol['required_per_run']['claim_fields']);claims.append(item)
claim('A003-ONCE-SLICED-MAJORITY-ERASURE',
 'For every r>=1, either first-bit slice h of Majority_(2r+1), and every remaining coordinate i, mu=E h=+/-rho, hat h({i})=Inf_i(h)=rho=binom(2r,r)/4^r and B_i(h)<=2rho; equality holds at r=1. For any actual Boolean split A+D z on disjoint rest, delta=E D^2>0, the composed slice satisfies B_i(A+hD)/(delta rho)<=2-2rho+rho log2(e/(rho^2 delta)), retaining the coherent empty-row correction. This is not a uniform arbitrary-outer price as delta tends to zero.',
 ['uniform actual Boolean physical cubes','bits; fresh encoder support disjoint from the arbitrary outer rest'],
 'sections 1-2',[{'source':'A026 stage3 PROOF.md','version':1,'locator':'section 2 coherent biased interface; directly reconstructed from coefficient packets'}])
claim('A003-TWO-QUERY-ELIGIBLE-PREFIX',
 'For every even k>=4 and actual outer Boolean sign with the influence types in A026-INTACT-ENCODER-BIASED-PREFIX v1, use disjoint Majority_M encoders on all 3k backgrounds, retaining selector y, with M=2k^2 2^(2k+4)+1 and rho=binom(M-1,(M-1)/2)/2^(M-1). At every actual history querying at most two bits per background block and never y, every available first/second-query bit i satisfies Inf_i>I/(2d) for the relevant residual dimension d. First queries have B_i/Inf_i<59/512; second queries have B_i/Inf_i<2+59/512-2rho. For any adaptive such prefix, let S1,S2 be expected spent influence at first/second queries. Then S1+S2=I(root)-E I(leaf), and H(root)<=E H(leaf)+(59/512+2/ln2)(S1+S2)+(2-2rho)S2. Full terminal entropy is retained. No third-query, arbitrary-outer or universal FEI payment follows.',
 ['bits; all actual uniform physical restrictions','delta0=2^-k,p=delta0^2; k backgrounds alpha=p(1/2+delta0),2k backgrounds alpha=p(1-sqrt(delta0)+delta0), selector alpha=pdelta0','fresh disjoint blocks; at most two queries per block; no selector query; candidates exist only before all blocks are queried twice'],
 'sections 3-5',[{'claim_id':'A003-ONCE-SLICED-MAJORITY-ERASURE','version':1,'status':'author proof pending independent review'},
 {'claim_id':'A026-INTACT-ENCODER-BIASED-PREFIX','version':1,'scope':'abstract outer influence hypotheses and binomial/density framework; own scoped reconstruction in A026_REVIEW.md; complete instantiated chain not independently accepted'}])
save(ROOT/'CLAIMS.json',claims)
progress=dict(protocol_revision=protocol['revision'],run_id=ROOT.name,stream='B01',packet_id='A003',gap_id='G-R-SELECT',attempt_id='A003-sliced-majority-v1',
 method='Coefficient recurrence and entropy-Hellinger bound; coherent signed packet transfer; actual biased-density and relevant-dimension cutoff algebra',
 mathematical_delta='Once-sliced majority inherited B_i<=2 Inf_i proved; signed credit retained; enlarged-encoder eligible paid prefix extended from 3k to 6k queries; 1754 exact assertions PASS.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='SCOPED_BRIDGE_PROVED_PENDING_REVIEW; FULL_FEI_AND_P4_OPEN',
 claim_versions_used=[{'claim_id':'A026-INTACT-ENCODER-BIASED-PREFIX','version':1,'review':'abstract influence-hypothesis argument reconstructed; instantiated A003 dependency chain not independently accepted'},
 {'source':'A004 stage2 REPORT.md','locator':'section 4 full/nonempty B and DTC identity, directly checked'}],
 claims_created_or_changed=[{'claim_id':c['claim_id'],'version':1,'status':c['status']} for c in claims],
 source_artifacts=['REPORT.md','DERIVATION.md','A026_REVIEW.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','out/VALIDATION.json','out/SOURCE_MANIFEST.json'],
 next_consumers=['A026','A057','A087','A094','B01','B06','B20'],
 next_action='Derive a single signed reserve for the arbitrary-outer coherent collision at sliced-encoder descendants, retaining full terminal entropy; twice-sliced inner pricing is a possible component, not the universal endpoint.',
 stagnant_substantive_attempts=0,blockers=['Arbitrary outer derivative delta has no lower bound; coherent collision and complete terminal payment remain unpaid; no access or save blocker.'],packet_ids=['A003'])
assert set(progress)=={f.split(' (',1)[0] for f in protocol['required_per_run']['progress_fields']}
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A003 stage3 complete: once-sliced majority B_i<=2 Inf_i; eligible paid two-query/block prefix with signed credit and full terminals; 1,754 exact assertions PASS; review pending; full FEI OPEN.\nNEXT: A026/A087/A094 review; pay arbitrary-outer coherent collision with one signed reserve and retained terminal entropy, using the sliced-majority lemma.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} A003 stage3: read updated board/lead/status and consumed A026 induced-bias prefix and A004 full-law correction. Reconstructed A026 abstract cutoff proof at scope (not own-source family dependency acceptance). Proved once-sliced majority B_i<=2 Inf_i via coefficient recurrence and exact Hellinger upper bound. Retained signed empty-row credit and extended enlarged-encoder eligible prefix to two queries/block. Exact frozen pilot: 120 composed cases, 14 once-sliced and 28 twice-sliced endpoints, 1754 assertions PASS in {validation["runtime_seconds"]:.4f}s. Arbitrary-outer collision and terminal entropy unpaid; all outputs saved locally.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nA003 stage3: Once-sliced odd majority has mean +/-rho, singleton and each influence rho, and B_i<=2rho. The zero-sum boundary derivative gives t c_t+(2r-t)c_(t+2)=0; even/odd derivative energies rho/2 and Phi<=2sqrt(ab) pay the whole inherited erasure. In composition its exact subtraction is Phi(rho^2,rho^2)=2rho^2, so price<=2-2rho+rho log2(e/(rho^2 delta)). Arbitrary delta still prevents universal pricing. With M=2k^2 2^(2k+4)+1, B05-type backgrounds admit two queries/block with Ghalf eligibility and collision price<59/512. Terminal entropy persists. Full-law DTC=h2(v)+vDTC(nonempty)-T0 was checked; conditioning never removes that correction.\n')
save(ROOT/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claims':len(claims),'report_fields':7,'progress_fields':len(progress),'compatibility_identical':True,'validation_assertions':validation['assertions'],'saved_at':stamp})
receipts=[]
for p in ROOT.rglob('*'):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  assert p.stat().st_size<20*1024**2
  receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)})
save(ROOT/'out/ARTIFACT_RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','artifacts':len(receipts),'claims':len(claims),'assertions':validation['assertions']}))
