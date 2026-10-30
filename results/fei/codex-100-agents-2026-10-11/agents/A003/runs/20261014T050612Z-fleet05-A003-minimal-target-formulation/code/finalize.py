from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];TEAM=AGENT.parents[1]
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v=json.loads((ROOT/'out/VALIDATION.json').read_text());assert v['status']=='PASS' and v['assertions']==6496
reviewdir=TEAM/'agents/A004/runs/20261014T024610Z-fleet05-A004-constant-and-unit-ledger'
sources=[PROTO,TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md',reviewdir/'REPORT.md',reviewdir/'DERIVATION.md',reviewdir/'CLAIMS.json',
 TEAM/'agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger/REPORT.md',
 TEAM/'agents/A096/runs/20261014T042803Z-fleet05-A096-live-gap-ledger/DERIVATION.md',
 TEAM/'agents/A094/runs/20261014T031253Z-fleet05-A094-proof-chain-challenger/REPORT.md']
save(ROOT/'out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
sourceclaims=json.loads((reviewdir/'CLAIMS.json').read_text())
review=next(c for c in sourceclaims if c['claim_id']=='A004-KL-SHADOW-EXCLUSIVE-TERMINAL-TRANSFER')
assert review['statement_sha256']=='50023058787e5d377d362f5de415f98448e50375a8f9e6b608d49f599050ca32'
review['review_records'].append({'reviewer':'A003','at_utc':stamp,'verdict':'HOLDS_AT_ORIGINAL_STATED_SCOPE_WITHOUT_REPAIR','proof_source':str(ROOT/'REVIEW.md'),'validation':'out/VALIDATION.json','scope':'New A004 cross-route correction, actual terminal criterion and AND2 obstruction; not a new independent review of A003 own source ancestor','substantive_repair':False,'source_statement_sha256':review['statement_sha256']})
review['status']='INDEPENDENTLY_RECONSTRUCTED_LOCAL_BY_A003_ADOPTION_PENDING'
statement='For every d>=1, delta=2^-d, b_d=-1+2*1_0, c_d=-1, g_d(s,y)=-1+1_0(1+s), let Q_d=B_s(g_d) and S4=[4I(b_d)-H(b_d)]/2 be the actual fair terminal surplus. Then Q_d=Phi((1-delta)^2,delta^2)+2delta(1-delta), S4=4delta+4(d-1)delta^2-eta((1-2delta)^2)/2, and Q_d-S4<=(2/ln2-2)delta+[2-3/ln2-2d]delta^2<(2/ln2-2)delta. The optimal all-dimensional additive allowance for Q_d<=S4+A delta is A0=2/ln2-2, since (Q_d-S4)/delta tends to A0. For any fresh balanced Boolean encoder h and an actual partner-first, complete-encoder policy retaining y, the whole shadow-plus-inherited bank is Q_d+delta E_h and is paid by S4+(A0+E_h)delta, with E_h the actual cumulative encoder erasure. For Maj3, E_h=1 under every complete adaptive policy and the sharp allowance is A1=2/ln2-1. Tensoring any independent price-four-certified terminal preserves the charge and adds its full actual surplus, retaining terminal entropy. This prices the retained shadow bill, not the discarded mask-only conditional KL whose source threshold is five. No arbitrary-seed reserve or universal FEI constant follows.'
hypotheses=['Bits; actual uniform physical Boolean signs and full squared Fourier law, empty atom included.','Point-origin core and fresh disjoint balanced encoder; physical partner queried before complete encoder resolution; no y core queries.','Independent terminal tensor q must have H(q)<=4I(q); its surplus is kept once and its complete entropy is retained.']
claim=dict(claim_id='A003-RETAINED-POINT-SHADOW-SHARP-ALLOWANCE',version=1,exact_statement=statement,hypotheses=hypotheses,
 statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),contributors=['A003'],
 proof_source={'run_id':ROOT.name,'path':'DERIVATION.md','locator':'sections 1-5','validation':'out/VALIDATION.json'},
 proof_dependencies=[{'claim_id':'A004-KL-SHADOW-EXCLUSIVE-TERMINAL-TRANSFER','version':1,'scope':'Policy/terminal interpretation; independently reconstructed locally in REVIEW.md'},
 {'source':'A096 stage5 DERIVATION.md','locator':'section 3 same point-core fixture and source loss-only price-five comparison; positive bound self-contained'}],
 review_records=[],status='SCOPED_AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,
 next_consumers=['A004','A026','A096','A087','A094','A099','B01','B06','B20'])
claims=[review,claim]
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
save(ROOT/'CLAIMS.json',claims)
progress=dict(protocol_revision=protocol['revision'],run_id=ROOT.name,stream='B01',packet_id='A003',gap_id='G-R-SELECT',attempt_id='A003-retained-point-bank-v1',
 method='Retain whole shadow row instead of injecting discarded KL; exact full-law point-core terminal formulas and sharp all-dimensional surplus allowance; independent A004 criterion review',
 mathematical_delta='Same actual point children at price4 pay retained Q with sharp allowance 2/ln2-2 and whole Maj3 bank with 2/ln2-1, despite discarded KL loss threshold5; 6496 exact assertions PASS.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='SCOPED_RETAINED_BANK_BOUND_PROVED_PENDING_REVIEW; A004_CRITERION_RECONSTRUCTED; FULL_FEI_OPEN',
 claim_versions_used=[{'claim_id':'A004-KL-SHADOW-EXCLUSIVE-TERMINAL-TRANSFER','version':1,'review':'A003 independent original-scope reconstruction without repair'},
 {'source':'A096 stage5 DERIVATION.md','locator':'exact non-flat point-core fixture and discarded KL loss distinction'},
 {'claim_id':'A003-INTERLEAVED-SHADOW-SIGNED-OWNERSHIP','version':1,'scope':'previous policy/account baseline; positive point bound does not assume arbitrary-core payment'}],
 claims_created_or_changed=[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],
 source_artifacts=['REPORT.md','DERIVATION.md','REVIEW.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','out/POINT_CHECKPOINT.json','out/SYMBOLIC_BANKS.json','out/VALIDATION.json'],
 next_consumers=claim['next_consumers'],next_action='Price retained whole collision/reference bill on a genuinely non-point unequal-amplitude core with a destroyed-edge point edit and a prescribed certified child reserve, retaining signed data debit and complete terminals.',
 stagnant_substantive_attempts=0,blockers=['Arbitrary seed lacks the point coefficient profile and sufficient certified child bank; no universal selected-policy reserve established.'],packet_ids=['A003'])
assert set(progress)=={f.split(' (',1)[0] for f in protocol['required_per_run']['progress_fields']}
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
report=(ROOT/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
(AGENT/'STATUS.md').write_text('STATE: A003 stage5 complete: A004 terminal criterion reviewed; retained point shadow paid at actual K4 surplus plus sharp query allowance A0=2/ln2-2 (Maj3 A1=2/ln2-1); 6,496 exact assertions PASS; FEI OPEN.\nNEXT: A004/A096/A087/A094 review; remove point/bent spectral profile on a non-point unequal-amplitude destroyed-edge edit, with prescribed unused child reserve and complete terminals.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} A003 stage5: consumed A004 exact terminal criterion, A096 non-flat price5 lost-KL objection and A094 destroyed-edge direction. Independently reconstructed A004 new cross-route claim. Retained point-core shadow Q fits same actual K4 terminal surplus plus sharp A0=2/ln2-2 query price, or A1=2/ln2-1 including inherited Maj3. Full-law/tensor owner retained once. First pass5685 assertions; added direct physical flip checks on unchanged frozen domain, final6496 PASS in {v["runtime_seconds"]:.6f}s. Arbitrary non-point child reserve remains open. All files local.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nA003 stage5: Distinguish A096 discarded mask-only KL L_d (~d delta) from retained seed shadow Q (~2delta), and from partner deletion M=downward erasure. On b=-1+2point and constant other child, actual K4 terminal S4~(4-2/ln2)delta. Sharp Q-S4 query allowance A0=2/ln2-2; including Maj3 inherited delta gives A1=2/ln2-1. Both hold all d>=1 with a strict negative O(d delta^2) correction; independent certified terminal tensor retains its full bank. Thus price5 discarded-loss threshold does not obstruct retained shadow payment at4 plus a fixed local allowance. A004 terminal criterion and AND2 half-bit correction independently reconstructed. Next profile to remove is non-point/unequal-amplitude destroyed-edge editing, not another point or bent census.\n')
save(ROOT/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claims':len(claims),'progress_fields':len(progress),'report_fields':7,'compatibility_identical':True,'assertions':v['assertions'],'saved_at':stamp})
receipts=[]
for p in ROOT.rglob('*'):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  assert p.stat().st_size<20*1024**2
  receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(ROOT/'out/ARTIFACT_RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','artifacts':len(receipts),'claims':len(claims),'assertions':v['assertions']}))
