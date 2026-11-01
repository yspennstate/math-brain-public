from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];TEAM=AGENT.parents[1]
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTO.read_text(encoding='utf-8-sig'))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
v=json.loads((ROOT/'out/VALIDATION.json').read_text());r=json.loads((ROOT/'out/TERMINAL_OWNER.json').read_text())
assert v['status']==r['status']=='PASS' and v['labelled_prefix_trees']==15360
total=v['assertions']+r['assertions'];assert total==127656
prior=AGENT/'runs/20261013T222630Z-fleet05-A003-minimal-target-formulation/CLAIMS.json'
old=json.loads(prior.read_text())
hashes=['4c5518b43c13eabc5828606942a620d4257f6e51e2fdfe28607e62c4f84489f3','b95bc46e28f201fe75376df07dbde98584cc26b50ba192c171d582ae9e7033e9']
for c,expected in zip(old,hashes):
 assert c['statement_sha256']==expected
 assert hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()==expected
sources=[PROTO,TEAM/'BOARD.md',TEAM/'claude/B01/STREAM_NOTES.md',prior,
 TEAM/'agents/A026/runs/20261014T011337Z-fleet05-A026-good-coordinate-erasure/REPORT.md',
 TEAM/'agents/A026/runs/20261014T011337Z-fleet05-A026-good-coordinate-erasure/PROOF.md',
 TEAM/'agents/A026/runs/20261014T011337Z-fleet05-A026-good-coordinate-erasure/CLAIMS.json',
 TEAM/'agents/A004/runs/20261013T235034Z-fleet05-A004-constant-and-unit-ledger/REPORT.md',
 TEAM/'agents/A004/runs/20261013T235034Z-fleet05-A004-constant-and-unit-ledger/REVIEW.md',
 TEAM/'agents/A096/runs/20261014T013836Z-fleet05-A096-live-gap-ledger/REPORT.md',
 TEAM/'agents/A096/runs/20261014T013836Z-fleet05-A096-live-gap-ledger/DERIVATION.md',
 TEAM/'agents/A027/runs/20261014T015108Z-fleet05-A027-block-selection/REPORT.md']
save(ROOT/'out/SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sources])
save(ROOT/'out/PRIOR_ACCEPTANCE.json',[{'claim_id':c['claim_id'],'version':1,'statement_sha256':c['statement_sha256'],'reviewer':'A004','verdict':'HOLDS_AT_ORIGINAL_ABSTRACT_SCOPE','review_source':str(sources[8]),'source_run_unchanged':True} for c in old])
statement='For every disjoint actual Boolean substitution F=A+hD, f(z,r)=A+zD, and every adaptive physical prefix interleaving encoder and data queries, let V_v=Var(h_v)B_z(f_v), Q=sum_encoder w gamma_v^2 B_z(f_v), and R=sum_data w Var(h_v)[B_z(f_v)-average B_z(f_child)]. Then Q+R=V_root-E V_leaf exactly; R may be negative and physical data influence uses encoder-output bias q=(1+E h_v)/2. With A026 C0=log2(32/27)+2/(e ln2), a=2/ln2, H(root)<=E H(leaf)+E_inner+E_data+V_root-E V_leaf-R+(C0+a)S_encoder+a S_data. For every even k>=4, source bent-flip g(s,y)=b(y)-1_0+s1_0, f(z,u,y)=g(zu,y), encoder h=Maj3, querying u then completing only the encoder gives R=-B_s(g), Q=B_s(g)>=2^-k(k-1), spent unlocking plus encoder influence=(5/2)2^-k, so no uniform local price funds this bank even using both accounts. Actual unlocking erasure is zero, terminal entropy is [k+H(b-2*1_0)]/2, and E_inner=2^-k. A single actual terminal K=2 surplus S2>=2k*2^-k pays Q+E_inner<S2 once. H(F)/I(F)<3; no FEI disproof or arbitrary-seed reserve follows.'
hypotheses=['Entropy in bits; actual fair physical restriction weights; encoder support disjoint from outer data; fresh auxiliary shadow z is not physically queried.',
 'Use current actual restricted f_v,h_v and retain terminal V and entropy; no assumption that signed data drops are nonnegative.',
 'Bent control b is the tensor quadratic bent sign positive at the origin; all-k ownership/no-go scope even k>=4; no data-core coordinates y queried in its stated policy.']
c=dict(claim_id='A003-INTERLEAVED-SHADOW-SIGNED-OWNERSHIP',version=1,exact_statement=statement,hypotheses=hypotheses,
 statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 contributors=['A003; consumes the explicit A096 bent-flip/parity-pair family'],
 proof_source={'run_id':ROOT.name,'path':'DERIVATION.md','locator':'sections 1-5','validation':['out/VALIDATION.json','out/TERMINAL_OWNER.json']},
 proof_dependencies=[{'claim_id':'A026-SIGNED-ROW-UNIFORM-SHADOW-TRANSFER','version':1,'review':'scoped independent reconstruction in REVIEW.md'},
 {'source':'A096 stage4 DERIVATION.md','locator':'section 4 explicit bent-flip/parity-pair construction; directly reconstructed, full KL chain not assumed'}],
 review_records=[],status='SCOPED_AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW',supersedes=[],
 refutes=['Uniform local price for negative data-shadow drop from its queried physical influence','Uniform shadow-bank price using the unlocking bit plus entire downstream encoder influence while excluding the terminal data core'],
 first_unproved_line=None,next_consumers=['A026','A004','A087','A094','A096','B01','B06','B20'])
assert set(c)==set(protocol['required_per_run']['claim_fields']);save(ROOT/'CLAIMS.json',[c])
progress=dict(protocol_revision=protocol['revision'],run_id=ROOT.name,stream='B01',packet_id='A003',gap_id='G-R-SELECT',attempt_id='A003-interleaved-shadow-v1',
 method='Exact signed variance-potential telescope; encoder-biased physical data influence; source-bound bent-flip ownership control and single terminal surplus',
 mathematical_delta='Interleaved shadow ownership Q+R=Vroot-EVleaf; unlocking-plus-encoder bank no-go at ratio>=2(k-1)/5; actual terminal K2 surplus pays full witness bank once; 127656 exact assertions PASS.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='SCOPED_SIGNED_TRANSFER_AND_OWNER_PROVED_PENDING_REVIEW; FULL_FEI_AND_P4_OPEN',
 claim_versions_used=[{'claim_id':cc['claim_id'],'version':1,'review':'A004 independent HOLDS consumed at abstract scope'} for cc in old]+[
 {'claim_id':'A026-SIGNED-ROW-UNIFORM-SHADOW-TRANSFER','version':1,'review':'scoped independent reconstruction recorded locally'},
 {'source':'A096 stage4 DERIVATION.md','locator':'explicit witness only'}],
 claims_created_or_changed=[{'claim_id':c['claim_id'],'version':1,'status':c['status']}],
 source_artifacts=['REPORT.md','DERIVATION.md','REVIEW.md','FROZEN_SPEC.json','RESERVE_SPEC.json','CLAIMS.json','code/check.py','code/reserve.py','out/VALIDATION.json','out/TERMINAL_OWNER.json','out/PRIOR_ACCEPTANCE.json'],
 next_consumers=c['next_consumers'],next_action='Derive a conditional remainder owned by actual certified core-child surplus at the first unlocking data query, retaining signed R, complete terminal law and one physical influence partition.',
 stagnant_substantive_attempts=0,blockers=['No general arbitrary-seed surplus pays the signed data debit, actual data erasure and terminal entropy; no save or source blocker.'],packet_ids=['A003'])
assert set(progress)=={f.split(' (',1)[0] for f in protocol['required_per_run']['progress_fields']}
save(ROOT/'PROGRESS.json',progress);save(ROOT/'PACKET_DELTA.json',progress)
report=(ROOT/'REPORT.md').read_text()
for field in protocol['required_per_run']['report_fields']:assert '## '+field in report
assert report.rstrip().splitlines()[-1].startswith('**Universal bridge:**')
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A003 stage4 complete: A004 acceptance consumed; signed interleaved shadow account, unlocking-plus-encoder no-go and single terminal K2 owner proved; 127,656 exact assertions PASS; review pending; FEI OPEN.\nNEXT: A026/A004/A087/A096 review; derive actual certified core-child surplus for the signed unlocking debit with complete terminal law and one physical influence budget.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} A003 stage4: consumed A004 independent acceptance of both prior claims; reconstructed A026 signed-row/interface/variance theorem and reused A096 actual parity-pair witness. Proved exact interleaved Q+R ownership, signed negative data debit locally unpayable even pooling downstream encoder, and explicit single terminal K2 surplus paying this full witness bank. 15360 prefix trees/1280 compositions plus three controls and six encoder orders each; {total} exact assertions PASS. Main 53.7776s, supplemental 0.0111s, frozen domains respected. Arbitrary seed surplus remains open; all artifacts local.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nA003 stage4: A004 independently accepts both stage3 claims at original abstract scope. A026 signed shift kappa=log2(32/27) is closed at source scope. Shadow bank under interleaved actual queries obeys Q_encoder+R_data=Var(h_root)B_z(f_root)-E Var(h_leaf)B_z(f_leaf); data R is signed and physical data influence uses encoder output bias. On A096 bent-flip parity pair with Maj3, querying partner u has zero actual erasure but unlocks R=-B_s(g); Q/spent unlocking+encoder>=2(k-1)/5. Local driver/encoder cannot pay this bank. Terminal core K2 surplus>=2kdelta pays Q+inherited delta once for k>=4; the missing universal object is a sufficient certified child surplus, not variance monotonicity or another majority slice. I(g)=k/2+(k+1)delta, parity shadow I(f)=k/2+(k+2)delta, physical Maj3 variant I(F)=k/2+(k+5/2)delta; preserve function distinctions.\n')
save(ROOT/'out/SCHEMA_VALIDATION.json',{'status':'PASS','claims':1,'progress_fields':len(progress),'report_fields':7,'compatibility_identical':True,'assertions':total,'saved_at':stamp})
receipts=[]
for p in ROOT.rglob('*'):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  assert p.stat().st_size<20*1024**2
  receipts.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(ROOT/'out/ARTIFACT_RECEIPTS.json',receipts)
print(json.dumps({'status':'PASS','artifacts':len(receipts),'assertions':total,'claims':1}))
