from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parent.parent
AGENT=ROOT.parent.parent;BASE=AGENT.parent.parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):(ROOT/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('For every finite uniform-cube Boolean sign, two-coordinate queried block A and K>=4, '
 'let c_t=E(w_t^2/q_t-1)^2, C_A=sum q_t c_t, Gamma_A=sum q_t log2(1+c_t), '
 'and classify actual Boolean phases sign(w_t), sign(0)=1, into constant mass W0, nonconstant good mass Wg '
 '(c_t<=1/16) and nonconstant bad mass Wb. With S_A=-E D_K(physical child), '
 'D_K(f)+S_A+(K/2-2)Wg<=Gamma_A+log2(1+3*2^-K)W0+2Wb. '
 'An alternative upper bound is Gamma_A+psi_2(min(1,C_A))+2Wb, where '
 'psi_2(s)=h2(s)+s log2 3 up to s=3/4 and equals2 thereafter. '
 'Wb<=16C_A and C_A<=6I_A; hence for C_A<=3/4 the alternative is at most '
 'log2(1+C_A)+h2(C_A)+(log2 3+32)C_A, an O(C_A log(1/C_A)) modulus. '
 'On a least-essential-dimension FEI(K) violation these identities retain S_A>=0 and D_K>0 on every pair, '
 'without assuming an optimizer. The actual sign (-1)^((x1 xor x2)y) has singleton collisions0 '
 'and joint pair collision1, so no unconditional finite-constant comparison C_pair<=c(C_x1+C_x2) holds. '
 'No uniform paid pair or full FEI bound is claimed.')
claim={'claim_id':'A051-TWO-BIT-CRITICAL-PHASE-RESERVE','version':1,'exact_statement':statement,
 'hypotheses':['Actual Boolean signs on finite uniform cubes, entropy in bits; zero-q rows omitted',
 'Two queried coordinates, K>=4; row-phase sign(0)=1; full cuts allowed for identities only',
 'S_A has its actual sign for general roots; S_A>=0 and D_K>0 require least essential dimension among all K-violators and a proper cut',
 'K>4 for a strictly positive good-phase coefficient; C_A<=3/4 only for the displayed uncapped entropy formula',
 'Parity guard is not a critical witness or FEI counterexample; constants6 and32 are not claimed sharp'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['fleet05/A051'],
 'proof_source':{'path':str(ROOT/'TWO_BIT_RESERVE.md'),'sha256':digest(ROOT/'TWO_BIT_RESERVE.md'),'locator':'Sections1--6; out/SUMMARY.json, REVIEW_REPLAY.json and PARITY_GUARD.json'},
 'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_NARROW_REFINEMENT_EXACTLY_REPLAYED_PENDING_INDEPENDENT_AGENT_REVIEW',
 'supersedes':[],'refutes':['Unconditional finite-c comparison C_{i,j}<=c(C_i+C_j) for actual Boolean signs'],
 'first_unproved_line':None,'next_consumers':['claude/B11','A052','A053','A055','A090','A094','B20']}
save('CLAIMS.json',[claim])
source52=BASE/'agents/A052/runs/20261013T221539Z-fleet05-A052-critical-source-structure'
source55=BASE/'agents/A055/runs/20261014T004129Z-fleet05-A055-extremal-obstruction-referee'
sources=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),
 BASE/'BOARD.md',BASE/'claude/B11/STREAM_NOTES.md',source52/'REPORT.md',source52/'CRITICAL_PHASE_PROOF.md',source52/'REVIEW_A051.md',source55/'REPORT.md',source55/'PROOF.md',source55/'CLAIMS.json',
 AGENT/'runs/20261013T215311Z-fleet05-A051-near-extremizer-definition/JOINT_CHANNEL_PROOF.md',
 AGENT/'runs/20261013T215311Z-fleet05-A051-near-extremizer-definition/code/exact_tools.py',
 AGENT/'runs/20261013T215311Z-fleet05-A051-near-extremizer-definition/code/independent_replay.py']
save('out/SOURCE_MANIFEST.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sources])
save('out/REVIEW_RECORDS.json',[
 {'claim_id':'A055-SINGLETON-CRITICAL-RESERVE','version':1,'statement_sha256':'bfc2c09293d9446e7301b5c562668288de096d6758459530ec93bf1db80c09bf',
 'reviewer':'fleet05/A051','verdict':'HOLDS_AT_COMPLETE_ANALYTIC_SCOPE','scope':'All analytic clauses; source finite count not adopted; direct-character validation independently executed',
 'review_source':str(ROOT/'REVIEW_A055.md'),'review_sha256':digest(ROOT/'REVIEW_A055.md'),'contributor_conflict':False},
 {'claim_id':'A051-JOINT-COLLISION-DESCENT','version':1,'statement_sha256':'93d304a363feb3a2315e5fffc3c0163e377f0617807490f6b3fb6f835fe90c2f',
 'reviewer':'fleet05/A052','verdict':'SOURCE_BOUND_ACCEPTANCE_CONSUMED','review_source':str(source52/'REVIEW_A051.md'),
 'review_sha256':digest(source52/'REVIEW_A051.md'),'contributor_conflict':False,'registry_adoption_verified':False}])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B11','packet_id':'A051',
 'gap_id':'B11-UNIVERSAL-PROPER-BLOCK-SELECTION','attempt_id':'A051-stage4-two-coordinate-margin',
 'method':'Independent analytic review of singleton reserve; finite two-bit phase classification and Gibbs envelope; exact retained-child bank; quartic physical-influence bound; frozen Boolean checks and parity guard',
 'mathematical_delta':'For K>=4, two-bit phase error improves from sqrt collision to C log(1/C), retaining (K/2-2)Wg and all four child deficits. C_A<=6I_A uses the same physical queried budget. Exact actual-Boolean guard refutes unconditional comparison of pair collision to its singleton collisions.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS; remote mirror unverified',
 'mathematical_status':'NARROW_ALL_DIMENSIONAL_TWO_BIT_REFINEMENT_PROVED; UNIVERSAL_PAID_BLOCK_SELECTION_AND_FEI_OPEN',
 'claim_versions_used':['A051-JOINT-COLLISION-DESCENT@1 (A052 independent acceptance consumed)',
 'A055-SINGLETON-CRITICAL-RESERVE@1 (analytic scope independently reconstructed by A051)',
 'A052-CRITICAL-BOOLEAN-PHASE-EXCLUSION@1 (source read and contextual comparison; not a pending proof premise)'],
 'claims_created_or_changed':['A051-TWO-BIT-CRITICAL-PHASE-RESERVE@1','A055-SINGLETON-CRITICAL-RESERVE@1 local analytic review record','A051-JOINT-COLLISION-DESCENT@1 source acceptance consumed'],
 'source_artifacts':['TWO_BIT_RESERVE.md','REVIEW_A055.md','out/SOURCE_MANIFEST.json','out/REVIEW_RECORDS.json','out/SUMMARY.json','out/REVIEW_REPLAY.json','out/PARITY_GUARD.json'],
 'next_consumers':['claude/B11','A052','A053','A055','A090','A094','B20'],
 'next_action':'Price the signed degree-two row term alpha*delta+beta*gamma by actual singleton orientation and child reserves under dimension minimality, preserving Wg and one influence budget; retain the zero-singleton parity guard.',
 'stagnant_substantive_attempts':0,
 'blockers':['No uniform K and paid pair/larger-block selection on dimension-critical witnesses','Neither C_A nor Wb has a proved bound below the retained critical reserve','New theorem awaits independent-agent review; remote mirrors and registry adoption unverified'],
 'packet_ids':['A051']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
(AGENT/'STATUS.md').write_text('STATE: A051 stage4 saved: K>=4 two-bit critical phase error O(C log(1/C)), retained child/phase bank and C_A<=6I_A; 52750 exact pilot/replay checks plus parity guard; A055 analytic reserve reviewed; FEI OPEN.\nNEXT: A052/A055 price signed alpha*delta+beta*gamma on minimal K-witnesses using actual singleton orientation/child reserves and one influence budget; unconditional pair-versus-singleton collision comparison is false; A090/A094 review.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n2026-10-14 01:26 UTC stage ('+ROOT.name+'): Read updated BOARD/B11 direction and own status; consumed A052 independent acceptance of joint collision and A055 singleton critical reserve. Independently reconstructed A055 at analytic scope without repair. Derived two-bit row-class bank for K>=4, retaining every physical child deficit and (K/2-2)Wg; constant phases have e<=c and exponential Gibbs envelope, good nonconstant phases provide I>=1/2, bad mass<=16C. Pure error improves to O(C log(1/C)); quartic Cauchy--Schwarz gives C_A<=6I_A. Frozen pilot281 tables/833 cuts passed35473 assertions in22.282s; independent review/replay804 singleton+49 pair cuts passed17277 in1.619s. Exact three-bit parity guard has C_i=C_j=0 but C_pair=1, ruling out unconditional comparison. Saved complete protocol/rolling artifacts. Uniform paid critical block and full FEI remain OPEN; new review/mirror pending.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
- Two-bit refinement (stage4): classify phases sign(w) as constant W0, nonconstant c<=1/16 Wg, and nonconstant c>1/16 Wb. Every nonconstant two-bit Boolean phase has I>=1; TV<=sqrt(c) gives I(row)>=1/2 on Wg. For K>=4, D_K+S_A+(K/2-2)Wg<=Gamma_A+log2(1+3*2^-K)W0+2Wb, with the actual signed child reserve S_A and Wb<=16C_A. S_A>=0 requires dimension minimality; it is not granted to arbitrary roots.
- Constant-phase row nonempty Fourier mass e=1-(E u)^2<=||u-phase||_2^2<=c. Jensen gives the pure modulus Gamma+psi_2(min(1,C))+2Wb<=log2(1+C)+h2(C)+(log2(3)+32)C for C<=3/4. Thus at fixed pair size and K>=4, the generic sqrt(C) phase error improves to O(C log(1/C)) by absorbing good-phase error in a known influence margin. This does not assert spectral TV is order C on nonconstant rows.
- Two-bit quartic bound: with row Fourier coefficients alpha,beta,gamma,delta, c=4[(alpha beta+gamma delta)^2+(alpha gamma+beta delta)^2+(alpha delta+beta gamma)^2]/q^2. Three Cauchy--Schwarz bounds yield c<=6I(row) and C_A<=6I_A. Constant6 is not claimed sharp; collision and exceptional mass use one queried influence account.
- Pair collision cannot be reduced unconditionally to singleton collision: actual f=(-1)^((x1 xor x2)y) has C_x1=C_x2=0 and C_pair=1, I_pair=1. Its R=4/3 and a singleton child has R=2, so it is not dimension-minimal. The degree-two signed term alpha*delta+beta*gamma requires a criticality/reserve argument; dropping it or using an unconditional comparison is invalid.
- A055-SINGLETON-CRITICAL-RESERVE@1 independently accepted at complete analytic scope via exact pair expansion and Gibbs KL maximization; source finite count not adopted. A052 acceptance of A051 joint collision is consumed. Stage4 final checks35473+17277 pass, plus exact parity guard. No uniform selection, positive deficit lower bound, global optimizer or FEI bound has been proved.
''')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
report=(ROOT/'REPORT.md').read_text()
assert all('# '+s in report for s in protocol['required_per_run']['report_fields'])
assert report.rsplit('\n## ',1)[1].startswith('Universal bridge\n')
pilot=json.loads((ROOT/'out/SUMMARY.json').read_text());replay=json.loads((ROOT/'out/REVIEW_REPLAY.json').read_text())
assert pilot['assertions']==35473 and replay['assertions']==17277
receipt={'schema':'PASS','byte_identical_delta':True,'report_fields':'PASS','final_pilot_replay_assertions':52750,
 'parity_guard':'EXACT_PASS','new_independent_agent_review':'PENDING','remote_mirror_verified':False}
save('out/HANDOFF_CHECK.json',receipt)
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.name!='ARTIFACT_MANIFEST.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save('out/ARTIFACT_MANIFEST.json',{'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files],
 'rolling':[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']],
 'all_files_under_20MB':True,'remote_mirror_verified':False})
print(json.dumps({**receipt,'run':ROOT.name,'files_saved':len(files),'claim_hash':claim['statement_sha256']}))
