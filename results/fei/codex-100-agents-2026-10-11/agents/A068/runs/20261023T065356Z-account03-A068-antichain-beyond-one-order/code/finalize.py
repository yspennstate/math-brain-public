from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
RUN=Path(__file__).resolve().parent.parent;HOME=RUN.parent.parent;ROOT=HOME.parent.parent
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):p.write_text(s,encoding='utf-8')
def put(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
o=json.loads(read(RUN/'out'/'obstruction.json'));t=json.loads(read(RUN/'out'/'transfer.json'));g=json.loads(read(RUN/'out'/'guard.json'));orbit=json.loads(read(RUN/'out'/'orbit.json'))
assert o['status']==t['status']==g['status']==orbit['status']=='PASS'
assert (o['formula_cases'],o['physical_cases'],t['parents'],t['policy_frontiers'],t['partial_nodes'],g['cases'])==(16,8,265,34715,7155,8)
for result,name in [(o,'obstruction.py'),(t,'transfer.py'),(g,'guard.py'),(orbit,'orbit.py')]:assert result['helper_sha256']==sha(RUN/'code'/name)
total=o['assertions']+t['assertions']+g['assertions']+orbit['assertions'];assert total==356426
report=read(RUN/'REPORT.md').replace('Proof checkpoint saved before exact validation.','Both complete author derivations and all frozen exact validations are saved; independent review remains pending.')
report=report.replace('three frozen specifications','four frozen specifications')
report=report.replace('Exact transfer results will be entered after execution.','The v2 pilot passed1048 policies/7274 assertions in0.231s; full transfer validation passed265 parents,34715 complete policy frontiers and7155 partial physical states:353011 assertions/211 certified log signs in25.949s. These are NEW stage19 counts, separate from stage18\'s1517305 checks. Sparse fixtures were added explicitly in the frozen v2 specification, not by automatic dimension escalation.')
report=report.replace('Proof checkpoint, frozen specification and independent verifier are saved locally. Final four protocol records, rolling notes, source hashes and receipt/schema validation will be saved before stopping.','The four protocol files, three frozen specifications, both full verifiers, failed pilot/source, source receipts and rolling files are saved locally. out/SCHEMA_CHECK.json validates exact protocol field sets, compatibility-byte equality, required report headings and two-line STATUS; out/RECEIPTS.json pins sizes/SHA256. Local persistence is verified; independent review, supervisor collection, shared registry adoption and remote mirror verification are not claimed.')
needle='## proof dependencies and changed downstream conclusions'
guard=('A separately frozen adversarial control in GUARD_SPEC.json runs the SAME8 physical Boolean functions with their actual root spectra as references. Marginalization followed by vacuum calibration then equals the exact AND child spectrum in every case (24 exact assertions,0.118s). Thus the heavy conditional NONEMPTY source shape, rather than the Boolean family or empty normalization, causes the obstruction. This finite control is not a universal entropy-priced reference supplier. Together the three full checks certify354330 assertions. The strongest contrary case would be that marginalization/calibration secretly redistributes the small nonempty atoms; direct full-source checks and this replacement-source control distinguish that possibility and reject it for Q_k.\n\n')
if 'A separately frozen adversarial control in GUARD_SPEC.json' not in report:report=report.replace(needle,guard+needle)
report=report.replace('Orbit pilot/full results are recorded in out/orbit_pilot.json and out/orbit.json.','The orbit pilot passed49 assertions; full orbit validation passed8 child cases,530 matrix candidates and175 invertible maps:2096 assertions/15 certified log signs in0.074s. These2096 additional checks raise the stage total from354330 to356426. Receipts are in out/orbit_pilot.json and out/orbit.json.')
write(RUN/'REPORT.md',report)

consumers=['A066','A070','A088','A094','A096','A097','A069']
def claim(cid,statement,hypotheses,deps,source,unproved,refutes):
 return {'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A068'],'proof_source':source,'proof_dependencies':deps,'review_records':[],'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':refutes,'first_unproved_line':unproved,'next_consumers':consumers}
claims=[]
claims.append(claim('A068-NONEMPTY-DATA-HEREDITY-OBSTRUCTION',
 'For every k>=1 let L=2^k,rho=1/L,N=2^(k+1)-2,epsilon=2^-L and F_k=OR(x,AND_k(y)), an all-relevant threshold. Its squared Fourier spectrum has full support. The normalized full-support ORIGINAL source Q_k has mass1/2 on{x},1/2-epsilon on{y1},epsilon/N elsewhere, and Gamma_Q(F_k)<5I(F_k). After ONE physical x query, even the optimal vacuum-only calibration of its inherited frequency marginal gives negative-child complete cost at least4rho(1-rho)*[((L-2)^2-k)/(L-1)]. For k>=3 this is >=2(1-rho), so child and two-child-average CE/I ratios are at least(7/8)2^k/k, unbounded. Both full physical children retained; the positive child costs0 after optimal calibration. At k8 averaged terminal CE minus25 times remaining average influence is >=9727/8192. Hence no universal finite rate makes arbitrary paid full references hereditary under one data query plus vacuum-only repairs. This is a complete-reference obstruction, not a Boolean FEI counterexample; supports agree exactly and no variable is dummy.',
 ['Uniform cube; spin=(-1)^bit; k>=1; reference probabilities exactly as stated.','A vacuum-only repair may choose any empty mass, but must retain the conditional distribution on nonempty frequency labels.','A lower bound on complete cross entropy is not asserted to be a lower bound on the actual Fourier entropy.'],
 ['Self-contained Boolean threshold Fourier formula, physical edge counts and binary/conditional cross-entropy decomposition; all derived in REPORT.'],
 ['REPORT.md: complete derivation or exact first unsupported line','code/obstruction.py','out/obstruction.json','code/guard.py','out/guard.json'],
 'Scoped obstruction completely proved; next universal line must constrain or PAY a genuine conditional NONEMPTY source-shape change. The accepted Euler rank source is not refuted.',
 ['Universal inference: arbitrary ORIGINAL normalized complete reference paid at root => all one-DATA-query descendants payable at some dimension-independent rate using only inherited marginal and vacuum calibration.']))
claims.append(claim('A068-PRIVATE-LITERAL-DATA-CUT-TRANSFER',
 'Supply ANY Boolean h on Y with normalized full reference Q_h satisfying Gamma_Qh(h)<=cI(h), c<=143/16. Let x be a private independent bit, beta any independent quadratic F2 Boolean phase, p=Pr(beta=+1), F=x on beta=+1 and h otherwise. Start with ORIGINAL data Q_root=p delta_{x}+(1-p)(delta_empty_x times Q_h) and stage18 control activation/affine-source reference. Allow arbitrary finite adaptive control prefix to its first-x frontier, query x on EVERY leaf of that cut with BOTH children retained, then arbitrary x-dependent adaptive control continuation, no Y queries. Physical frequency erasure gives EXACTLY Q_after=p delta_empty+(1-p)Q_h, unchanged in all later descendants. Prescribed actual activation and ORIGINAL affine-fiber returns release exact nonnegative KL credits. At every complete frontier after the all-path first-x cut, average full cost <=(1-p)Gamma_Qh(h)+4I(h)+2 average remaining control influence. For nonconstant beta, the SAME ORIGINAL rate25 signed owner therefore retains >=(1-p)I(h)/16+23 average remaining control influence, including ALL old debits, both full terminal bills and actual releases, without renewing root contrast reserve. Constant beta handled directly. No child-local bank or partially processed x-cut solvency is asserted.',
 ['Uniform independent x,Y,Z; h arbitrary Boolean on Y, beta quadratic over F2 on Z.','Q_h is a SUPPLIED paid COMPLETE supporting reference; theorem does not supply such a reference for arbitrary h.','Root literal full source is its character point mass; h embeds with empty x frequency. No Y queried.','Every final path queries x exactly once; prefix may stop at different control depths; whole first-x cut is included.','All source changes/negative credits explicitly booked. Activation-only repair is not called a nonempty-shape repair.'],
 ['A068-ACTIVATED-QUADRATIC-CONTRAST@1: complete inherited log-sum, JS<=3I(product), output entropy tensorization.','A068-ORIGINAL-AFFINE-CONTROL-FRONTIERS@1: exact source-conditioning return credits; prior REPORT SHA2568c179f9bda7da9b29cd35fad2e64483150726730e558e6db365b90efc90bc13b.','Private-literal source erasure, total-expectation and all-old-transaction ledger reconstructed here.'],
 ['REPORT.md: Paid transfer through a private literal DATA cut','code/transfer.py','out/transfer.json'],
 'One SHARED Y-query after the paid literal cut: ORIGINAL Q_h nonempty profile is not automatically hereditary, by the companion obstruction. Need a certified conditional shape invariant or explicitly paid prescribed replacement.',[]))
claims.append(claim('A068-ORIGINAL-ORBIT-SOURCE-RETURN',
 'For ANY finite frequency-permutation group G and ACTUALLY G-invariant Boolean squared spectrum P, normalized complete source Q may be returned to its ORIGINAL-source orbit average Q^G=average g_*Q with full cost CE(P,Q^G)<=CE(P,Q). On the companion all-relevant threshold/source family F_k,Q_k, after physical x query, GL(k,2) invariance of the actual AND_k child makes this SAME-source average uniform on nonempty frequencies while preserving original vacuum mass. Subsequent actual-vacuum calibration yields the actual child spectrum. This is an explicit genuine NONEMPTY shape conversion derived from the ORIGINAL source, not a fresh source supplier. Its full child cost H(AND_k)<=4I(AND_k); the positive child costs0. Therefore the ORIGINAL paid rate5 root owner pays the whole query and BOTH full source conversions, with average final surplus>=average remaining influence=k2^-k. All old signed debits and nonnegative reference-cost releases retained. This repairs the vacuum-only obstruction family and does not retract that obstruction. Arbitrary noninvariant children are not covered.',
 ['Uniform cube and normalized complete supporting references.','The orbit lemma requires ACTUAL spectral invariance under the group. It is false as an unrestricted free mixing assertion.','GL repair uses point-defect AND_k invariance under all invertible linear maps fixing zero; k>=1; all source permutations come from the ORIGINAL inherited q.','The SAME rate5 owner and both physical x children are used; no replacement source or new allowance is granted.'],
 ['Convexity of -log and invariance, proved locally; GL transitivity from basis extension.','A068-NONEMPTY-DATA-HEREDITY-OBSTRUCTION@1 supplies ORIGINAL family/reference and physical child law.','Elementary -a ln(a)<=1-a and ln2>1/2 give H(AND_k)<=4I.'],
 ['REPORT.md: Genuine nonempty repair from the SAME source by orbit averaging','ORBIT_SPEC.json','code/orbit.py','out/orbit.json'],
 'Universal source mixing after a SHARED data query requires a certified symmetry/phase-defect charge when actual spectrum is NOT invariant, or paid orbit-mass geometry; these are not supplied.',[]))
put(RUN/'CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B14','packet_id':'A068','gap_id':'G-LOWSEL-COLLISION','attempt_id':'A068-first-DATA-cut-nonempty-source-shape-v1',
 'method':'Adversarial full-support threshold source with optimal binary calibration; conditional nonempty KL lower certificate; private-literal physical source erasure and all-history exact signed ledger.',
 'mathematical_delta':'Vacuum-only paid-source DATA heredity FALSE: all-relevant thresholds/rootCE<5I, descendantCE/I>=(7/8)2^k/k, k8 rate25 deficit>=9727/8192. SAME ORIGINAL source GL averaging repairs its genuine NONEMPTY shape at SAME5, residual>=average remaining influence. Private-literal DATA cut after quadratic-control histories fits SAME25/original Q_h, residual>=(1-p)I(h)/16+23E I_controls.356426 exact assertions PASS.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOFS_COMPLETE; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A068-ACTIVATED-QUADRATIC-CONTRAST@1','A068-ORIGINAL-AFFINE-CONTROL-FRONTIERS@1','A066 stage9 calibrated-repair boundary: motivation only, no theorem imported'],
 'claims_created_or_changed':[c['claim_id']+'@1' for c in claims],
 'source_artifacts':['REPORT.md','CLAIMS.json','SPEC.json','TRANSFER_SPEC.json','GUARD_SPEC.json','ORBIT_SPEC.json','code/obstruction.py','code/obstruction_v1_failed.py','code/transfer.py','code/guard.py','code/orbit.py','out/obstruction.json','out/transfer.json','out/guard.json','out/orbit.json','out/obstruction_v1_failed.json','out/SOURCES.json','out/SCHEMA_CHECK.json','out/RECEIPTS.json'],
 'next_consumers':consumers,
 'next_action':'After paid private-literal cut expose one shared Y using ORIGINAL Q_h/old debits/full terminals. Consume fresh A096/A097 phase-funded profile results to pay ACTUAL noninvariant orbit/source mixing, or derive an Euler nonempty-shape invariant; keep Q_k no-go and SAME5 orbit repair as guards.',
 'stagnant_substantive_attempts':0,
 'blockers':['General shared-data nonempty source-shape payment remains open; arbitrary-root-cost heredity refuted.','Independent review, supervisor pickup and external mirror adoption unverified.','Brain self-care degraded/unverified: model/state personal notes stale; not proof premises.'],
 'packet_ids':['A068']}
put(RUN/'PROGRESS.json',progress);(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
status=('STATE: Stage19: vacuum-only DATA heredity fails unbounded; ORIGINAL nonempty GL-source return repairs witness SAME5; private-literal DATA cut SAME25;356426 exact assertions PASS; FEI OPEN.\n'
 'NEXT: Shared Y query after paid literal cut, ORIGINAL Q_h/old debits/full children: consume A096/A097 phase-funded noninvariant mixing or certify Euler-source shape; keep Q_k/SAME5 orbit guards; A066/A070/A088/A094 review.\n')
write(HOME/'STATUS.md',status)
work=(f'\n{now} | {RUN.name} | Read updated BOARD/B14/own state and A066 repaired source witness. '
 'Proved stronger nonempty no-go: all-relevant threshold OR(x,AND_k), original full-support source CE<5I, AFTER optimal vacuum calibration descendant CE/I>=(7/8)2^k/k; k8 whole-bank25 deficit>=9727/8192. '
 'Also proved supplied-source private-literal DATA cut after arbitrary adaptive quadratic-control histories, SAME original Q_h/rate25/old debits and exact credits; residual>=(1-p)Ih/16+23E Ictrl, no partial-cut/local-bank claim. '
 'Pilotv1 spin convention failed, source/receipt retained; v2 direct physical+formula1295 checks PASS. Transfer34715 policies7155 states353011 checks PASS25.949s; negative-control same functions actual root source cal equals true child24 checks PASS; total354330. '
 'Added genuine NONEMPTY repair: SAME original inherited source averaged over GL(k,2), then vacuum calibrated; ACTUAL child invariance gives free full-cost return and H(AND)<=4I, SAME5 root retains>=average Iremaining. Orbit2096 extra checks/175 invertible matrices PASS0.074s; updated total356426. '
 'No full-FEI or independent acceptance claim; next shared Y nonempty-profile transfer with accepted-source invariant/phase-funded symmetry defect.\n')
oldlog=read(HOME/'WORKLOG.md')
if not any(RUN.name in line and 'Orbit2096' in line for line in oldlog.splitlines()):write(HOME/'WORKLOG.md',oldlog+work)
lesson=('\nA068 stage19 NONEMPTY source-heredity obstruction: on all-relevant threshold F_k=OR(x,AND_k), root Walsh main{x}=1-rho, every other coefficient magnitude rho, rho=2^-k. '
 'Take ORIGINAL Q({x})=1/2,Q({y1})=1/2-2^(-2^k), remaining N=2^(k+1)-2 atoms equal2^(-2^k)/N. Gamma_Q<5I despite full support/no ghosts. '
 'After physical x, negative child AND_k has uniform actual NONEMPTY spectrum but inherited conditional source has one heavy atom. Even BEST empty/vacuum rescaling leaves KL>=((2^k-2)^2-k)/(2^k-1)>=2^(k-1) for k>=3, so CE>=2(1-2^-k), CE/I>=(7/8)2^k/k. '
 'Averaged child rate25 deficit at k8 is at least9727/8192, not an exact entropy equality. Therefore arbitrary paid-root references are NOT data-hereditary even after optimal vacuum calibration; rank-specific source shape must be constrained/paid. Actual root spectral reference on SAME functions calibrates exactly to true child: obstruction is source shape, not FEI or support. '
 'Positive transfer: private literal x versus ANY supplied paid h(Y), independent quadratic beta. After arbitrary control prefix, expose x at EVERY leaf of first-x cut, then arbitrary x-dependent control continuation. ORIGINAL source erasure gives Q_after=p delta_empty+(1-p)Q_h; keep Q_h unchanged and book exact control activation/affine-source KL credits. '
 'Whole final signed owner retains at SAME25 at least(1-p)Ih/16+23E I_controls. No renewed contrast grant, no child-local/partial-cut/positive-only solvency claim. This exposure changes activation, NOT conditional nonempty phase shape. Next shared Y query needs real nonempty-shape invariant or paid replacement. '
 'Genuine nonempty repair of the SAME witness: ACTUAL AND child is GL(k,2)-invariant. Convexity plus actual spectral invariance makes ORIGINAL-source orbit averaging free; transitive nonzero orbit uniformizes the heavy source profile. Vacuum calibration then yields actual AND spectrum, H<=4I. SAME5 owner therefore retains>=average remaining influence after query and BOTH full conversions. This does not contradict vacuum-only failure; arbitrary group mixing without actual invariance is NOT free. '
 'Failed pilot bit convention preserved: Walsh and physical restrictions must use same bit0=+1. Proof/certificates '+RUN.name+'/REPORT.md; independent review pending, FEI OPEN.\n')
oldlearn='\n'.join(line for line in read(HOME/'LEARNED.md').splitlines() if not line.startswith('A068 stage19 NONEMPTY'))+'\n'
write(HOME/'LEARNED.md',oldlearn+lesson)

sources=[(ROOT/'BOARD.md','relevant current agent rows'),(ROOT/'claude'/'B14'/'STREAM_NOTES.md','full lead direction'),
 (Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),'protocol and exact field arrays'),
 (Path('~/<private-repo>/12_cognitive_architecture/scheduled_tasks/README.md'),'current full-FEI-only order'),
 (Path('~/AGENTS.md'),'machine operational restrictions read'),
 (RUN.parent/'20261023T024829Z-account03-A068-antichain-beyond-one-order'/'REPORT.md','complete predecessor proof'),
 (RUN.parent/'20261022T211502Z-account03-A068-antichain-beyond-one-order'/'code'/'verify.py','pinned rational log/FWHT helper'),
 (HOME.parent/'A066'/'runs'/'20261023T052148Z-account03-A066-semigroup-dissipation'/'REPORT.md','opening sections1-4; calibration repairs specific witness')]
put(RUN/'out'/'SOURCES.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'read_scope':scope,'text_encoding':'utf-8'} for p,scope in sources])
protocol=json.loads(read(sources[2][0]))
def fields(x):
 if isinstance(x,dict):
  if all(k in x for k in ('report_fields','claim_fields','progress_fields')):return x
  for value in x.values():
   got=fields(value)
   if got:return got
 if isinstance(x,list):
  for value in x:
   got=fields(value)
   if got:return got
f=fields(protocol);assert f
assert set(progress)=={s.split(' (')[0] for s in f['progress_fields']}
assert all(set(c)==set(f['claim_fields']) for c in claims)
assert all('## '+h in report for h in f['report_fields'])
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len(read(HOME/'STATUS.md').splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in RUN.rglob('*') if p.is_file())
put(RUN/'out'/'SCHEMA_CHECK.json',{'status':'PASS','utc':now,'exact_claim_fields':True,'exact_progress_fields':True,'required_report_headings':True,'universal_bridge_last':True,'compatibility_byte_identical':True,'status_two_lines':True,'files_under_20mb':True,'full_assertions':total,'independent_review':'PENDING','formal_compiler':'NOT_RUN; no formal certification claimed','remote_adoption':'UNVERIFIED'})
put(RUN/'out'/'RECEIPTS.json',{'utc':now,'scope':'local persistence only; excludes self-referential receipt',
 'artifacts':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json'],
 'rolling':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in [HOME/'STATUS.md',HOME/'WORKLOG.md',HOME/'LEARNED.md']]})
print(json.dumps({'status':'PASS','run':RUN.name,'report_sha256':sha(RUN/'REPORT.md'),'claims':[c['claim_id']+'@1' for c in claims],'full_assertions':total,'schema':'PASS','four_protocol_files':'SAVED','full_fei':'OPEN'}))
