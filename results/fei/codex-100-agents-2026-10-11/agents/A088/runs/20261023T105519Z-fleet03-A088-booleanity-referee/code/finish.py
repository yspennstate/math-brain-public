import json,hashlib,platform
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];HOME=R.parents[1];BASE=HOME.parents[1]
OLD=R.parent/'20261023T070855Z-fleet03-A088-booleanity-referee'
PROTO=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
def read(p):return p.read_text(encoding='utf-8-sig')
def load(p):return json.loads(read(p))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat();check=load(R/'out'/'CHECK.json');real=load(R/'out'/'REAL_SCOPE.json');pilot=load(R/'out'/'PILOT.json')
assert all(x['status']=='PASS' for x in (check,real,pilot))
assert check['old_arithmetic_sha256']==sha(OLD/'code'/'check.py')
# Preserve the reviewed input version without inventing a new independent review.
claims=load(OLD/'CLAIMS.json');save(R/'CLAIMS.json',claims)
for c in claims:assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
total=check['checks']+real['checks'];progress=load(OLD/'PROGRESS.json')
progress.update({
 'run_id':R.name,'attempt_id':'A088-premature-w-paid-selected-continuation-v1',
 'method':'Canonical source-review continuation: exact positive w allowance plus negative paired moments for changed post-w profile; global full-terminal KL cap; literal actual Boolean reconstruction and normalized real phase diagnostic',
 'mathematical_delta':'At SAME original rate3, old D/reference and incoming diminished reserve, one w query after ANY H completed pairs followed by ANY T-H selected edited paired blocks is paid uniformly,0<=H<=T<=m. Whole root-weighted CE<7/48, full terminal KL<19/32, actual entropy invoice<71/96, legacy rate2 invoice<119/96.15374 exact checks PASS; new derivation pending external review, arbitrary-core supplier and full FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF',
 'mathematical_status':'AUTHOR_PROOF_EXACT_CERTIFICATES_FOR_SCOPED_SOURCE_REVIEW_CONTINUATION_PENDING_EXTERNAL_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':[
  {'claim_id':'A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK','version':1,'statement_sha256':'c8972812430c4b66c2874a9746d9fe2f5305397434ca62d56dc42755c2c3bee1','status':'INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_LOCAL_RECEIPT'},
  {'claim_id':claims[0]['claim_id'],'version':1,'statement_sha256':claims[0]['statement_sha256'],'status':claims[0]['status']},
  {'source':str(OLD/'PROOF.md'),'locator':'sections2--5, all pre-w completed-pair credits and full old clean-exit KL','status':'AUTHOR_PROVED_EXACTLY_CHECKED_PENDING_EXTERNAL_REVIEW'}],
 'claims_created_or_changed':[],
 'source_artifacts':[str(R/'PROOF.md'),str(R/'out'/'CHECK.json'),str(R/'out'/'REAL_SCOPE.json'),str(OLD/'PROOF.md'),str(OLD/'CLAIMS.json')],
 'next_consumers':['A067','A070','A094','A066','A096','B14','B18','B20'],
 'next_action':'A067/A070/A094 review the one-w changed-profile proof. Price a physical data query INSIDE a stopped clean exit using the actual remaining original account r+I_X-E_H, same Q_c marginal, old D and J, both full terminal CE/KL bills. Seek arbitrary-core phase control replacing the moment signs; no renewed initial source.',
 'stagnant_substantive_attempts':0,
 'blockers':['Full FEI and arbitrary-core original supplier OPEN','New scoped continuation proof and prior pre-w all-pair lemma await independent review','Queries within retained clean exits and arbitrary phases outside current proof','Full-history real relaxation after every pair queried not established; only proper prefix tested','Supervisor mirror/adoption unverified; packet forbids git','Brain self-care degraded/unverified: stale owner-model/state-of-mind notes not used'],
 'packet_ids':['A088']})
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

For canonical G_m and c_m, every integer m>=2,0<=H<=T<=m: retain the paid H completed-pair edited-zero history, query actual physical w before completion if desired, keep BOTH full w children, then continue T-H completed pairs only on the w=0 edited-zero branch. All stopped siblings and original b_m remain. Rate3 is chosen ONCE at the original source; use only marginals of original Q_c, unchanged old D, complete rate2 invoices and the actually diminished original reserve. Uniform physical Boolean influences, base-two H/CE/KL. Full FEI is OPEN.

# sources actually read, revisions and theorem locators

Current BOARD, B18 STREAM_NOTES v2 and own STATUS were read at stage start, including current A031--A040,A066--A070,A094,A096,A097 changes. The post-crash common.md was read: saved products were checked rather than restarted. The board still has A067 first-block stage19 and no newer continuation, so this stage resumes the unpaid early-w profile in A088 run20261023T070855Z PROOF6. Previous PROOF2--5 supplies the pre-w all-pair bound, explicitly author-checked/pending independent review. A067's canonical source and first-block rate3 reviewed versions are retained unchanged in CLAIMS.json. Earlier required protocol/campaign/supplement/paper baseline reads remain inherited; no new paper theorem is used. Current source/helper bytes are pinned in out/SOURCES.json. Brain self-care remains degraded/unverified: stale owner-model97.3h and state-of-mind81.9h notes were not used.

# complete derivation or exact first unsupported line

PROOF1 preserves every pre-w invoice and original reach. PROOF2 prices the genuine positive occupancy-changing w query with root-weighted CE charge<d(m+1/3)<=7/48. PROOF3 derives the CHANGED post-w law P'_j=B^2(1-2B sigma)^2 versus original marginal Q'_j=B^2(1+2d-2alpha sigma), and recalculates physical influences1/2+2B^2 and4B^2. Both new query likelihood moments are strictly negative, so both CE drops are<1; every post-w completed block contributes negative original-reach credit<-3d. No conditional-equality assumption or fresh child reference is used.

PROOF4 retains all old clean exits, the new w=1 terminal, all new pair exits and the active edited terminal. Their ONE entire-frontier KL bound is<5/12+4^-H/24+(1+12T)/(24*4^T)<=19/32. Consequently the complete entropy invoice is<71/96, retaining the old first invoice in r+I_X-E_H rather than reissuing its bank. The original once-only increment I_X>m pays it with remaining reserve>m-71/96. Complete legacy rate2 invoice is<119/96 via exact original removed influence J=1/3-4^-H/6-4^-T/6+(T+1/2)d<1/2. All bounds are all-dimensional analytic statements, not finite extrapolation.

The normalization/phase scope was challenged with actual real functions: Id-2 E_R on an untouched pair commutes with early w and the subsequent edited block. Nine actual root/child nodes remain norm1 and retain every full spectrum and physical Dirichlet energy while becoming nonBoolean; a nonempty XOR convolution is-63/64. Thus the new profile payment, once its canonical laws/energies are given, does not itself enforce full Boolean convolution constraints. No real full-history extension is asserted once the last untouched pair is queried.

The exact first unsupported line is payment for a physical data query inside a retained clean exit with the same incoming nonflat reference and diminished source, or a universal replacement for the canonical moment signs/source pricing on arbitrary Boolean cores. The old early-w positive-sign obstruction is not withdrawn: its cost is now explicitly funded. The generic signed no-reset identity is background; the new mathematical delta is the funded changed-profile inequality. Under the existing pending-candidate cap, this is saved as the continuing source review's complete scoped derivation, not promoted into an accepted broad campaign candidate.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes code/check.py pilot/full. Commands use python -X utf8 -B. Pilot m=2: {pilot['checks']} exact checks PASS in{pilot['runtime_seconds']:.6f}s,6(H,T)cuts. Full frozen grouped m=2..20: {check['grouped_cuts']}(H,T)cuts and209 DISTINCT post-w block profiles applied1539 times; separate literal m=2..5:18 actual w nodes,34 subsequent paired blocks and52 stopping cuts. {check['checks']} exact predicates PASS in{check['runtime_seconds']:.6f}s. Literal truth tables, integer Walsh coefficients, physical pivotal edges, direct original-Q marginals and BOTH child CE bills are recomputed; the grouped lane separately checks the rational likelihood moments and full frontier caps. The infinite parameter range is supplied by PROOF, not this finite census.

The exact arithmetic kernel is reused from our OWN prior helper by AST loading only imports and named function definitions. No old top-level job executes and no old output is rewritten; no other agent's checker is imported. Its source SHA is checked in CHECK.json. Rational logs use28 positive atanh terms, proved tail2z^57/[57(1-z^2)], exact range reduction and outward2^-90 endpoints. Floating approximations are descriptive only. Predicate failures raise exceptions and could reject the claim on normalization, child bills, signs, moment identities, old influence invoices or any reserve cap.

REAL_SCOPE_SPEC.json precedes code/real_scope.py: {real['checks']} exact predicates PASS in{real['runtime_seconds']:.6f}s, nine actual normalized nonBoolean nodes at m=3,H=0,T=1, independent direct-character sums, all Dirichlet edges and failed Boolean convolution. Total final predicates {total}, excluding pilot. Main estimate100MB/180s; guard25MB/55s. No job above300MB, heavy search, GPU, automatic dimension escalation, detached job or remote computation. No compiler/Lean certificate is claimed.

# proof dependencies and changed downstream conclusions

Canonical original-source v1 and first-block rate3 v1 remain independently accepted at their precise scope; their statements/review receipts are unchanged. The pre-w all-pair derivation remains author-proved/pending external review and is stated as such in PROOF1 and PROGRESS. The changed post-w laws and payment are reconstructed here with their own exact certificates, not attributed to A067 or independently accepted. Claims created/changed is empty because no additional broad candidate is opened; the scoped source-review continuation is complete in PROOF. C024/C019 now have an explicit uniformly funded early occupancy query and its entire selected edited continuation with all old bills retained. Arbitrary clean-exit continuation and arbitrary-core FEI remain open.

# one next mathematical action and independent reviewer

A067/A070 reconstruct PROOF2--5; A094 challenge the full KL, old J and diminished-source arithmetic. Next price one ordinary data query INSIDE a stopped clean exit from r+I_X-E_H(H,T), original Q_c marginal, old D/J, and both full terminal CE/KL bills. Then identify the arbitrary-core phase control that could replace the two canonical rational moment signs; another supplied-source identity cannot establish full FEI.

# actual persistence receipts or precise save blocker

The four protocol files, complete proof, frozen specs, scripts and exact outputs are saved here. STATUS has exactly STATE/NEXT, WORKLOG/LEARNED are appended. out/PERSISTENCE_RECEIPTS.json verifies exact schemas, byte-identical progress/delta, unchanged carried input statement hash, current source bindings, UTF-8 readback and file sizes below20MB. No prior run or another agent's folder is changed. Supervisor copying and remote adoption remain unverified under A088's no-git rule. Did: funded the early-w altered profile and its full selected continuation. Stopped: nothing. Left running: no A088 job.

# Universal bridge

C024 history transfer and C019 stopping-tree payment advance by funding ONE genuine early occupancy-changing w query after ANY paid completed-pair prefix and ALL subsequent selected paired cuts,0<=H<=T<=m, from the SAME original rate3 source. The whole CE invoice is<7/48, the entire terminal KL bill<19/32, complete entropy invoice<71/96 and legacy rate2 invoice<119/96; old D, actual reaches, diminished source and every full sibling bill remain. This closes the previous unpaid early-w profile, not a universal FEI constant. What remains is an inherited clean-exit query and ultimately arbitrary-core phase/source control. NEXT attacks that actual changed inherited profile with the remaining account because it tests the universal transfer bottleneck rather than adding an isolated H/I class estimate.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
nextline='NEXT: A067/A070/A094 review early-w/post-w proof; pay one data query INSIDE a retained clean exit from SAME r+I_X-E_H, original Q, old D/J and BOTH full CE/KL terminals; arbitrary-core phase/source remains open.'
(HOME/'STATUS.md').write_text(f'STATE: A088 stage20: early w after ANY paid H pairs and ALL T-H selected post-w pairs funded SAME original rate3; E_H<71/96, full KL<19/32;{total} exact checks PASS; review pending; FEI OPEN.\n'+nextline+'\n',encoding='utf-8',newline='\n')
with (HOME/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write('\n'+now+' | '+R.name+' | Paid genuine early w after any H and all selected post-w pair cuts T>=H from SAME original rate3 account. Global W<7/48; full K_F<19/32; E_H<71/96; legacy E_H2<119/96. '+str(total)+' exact final predicates PASS;1767 grouped cuts/52 literal cuts, nine actual normalized real gauge nodes. Prior sources unchanged; new proof pending external review; FEI OPEN. '+nextline+' No A088 job left running.\n')
with (HOME/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:f.write('\n'+now+' | One early w after completed prefix: original-weighted positive charge<d(m+1/3)<=7/48. Afterwards actual P=B^2(1-2B sigma)^2 and inherited original Q=B^2(1+2d-2alpha sigma), alpha B=d. New physical influences1/2+2B^2 and4B^2; both CE likelihood moments negative, each post-w original-weighted paired block<-3d. All OLD exits+w clean sibling+new exits+active terminal give K_F<5/12+4^-H/24+(1+12T)/(24*4^T)<=19/32. Hence cumulative entropy invoice<71/96, legacy rate2<119/96, paid by SAME original increment I_X with old D/J. Explicit diminished-account update prevents renewal. Real untouched-pair filter preserves all nine early-w/post-w prefix nodes and full Dirichlet/spectral data while violating phase convolution-63/64; no universal Boolean phase inequality follows.\n')
sourcepaths=[PROTO,BASE/'BOARD.md',BASE/'claude'/'B18'/'STREAM_NOTES.md',Path('~/CRASH_RESTORE_2026_10_23_1330/common.md'),OLD/'PROOF.md',OLD/'CLAIMS.json',OLD/'code'/'check.py',OLD/'code'/'real_scope.py',R/'PROOF.md',R/'FROZEN_SPEC.json',R/'REAL_SCOPE_SPEC.json',R/'code'/'check.py',R/'code'/'real_scope.py',R/'code'/'finish.py']
save(R/'out'/'SOURCES.json',{'timestamp_utc':now,'python':platform.python_version(),'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sourcepaths]})
schema=load(PROTO)['required_per_run'];fields=set(schema['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids')
assert set(progress)==fields
for c in claims:assert set(c)==set(schema['claim_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for h in schema['report_fields']:assert '# '+h in report
assert report.rfind('# Universal bridge')>report.rfind('# actual persistence')
assert len(read(HOME/'STATUS.md').splitlines())==2
files=[]
for p in sorted(R.rglob('*')):
 if not p.is_file() or p.name=='PERSISTENCE_RECEIPTS.json':continue
 assert p.stat().st_size<20_000_000
 if p.suffix in ('.md','.json','.py'):read(p)
 files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(R/'out'/'PERSISTENCE_RECEIPTS.json',{'status':'PASS','timestamp_utc':now,'schema_exact':True,'progress_byte_identical':True,'carried_claim_hashes_unchanged':True,'own_old_arithmetic_hash_matches':True,'files':files,'remote_adoption':'UNVERIFIED'})
print(json.dumps({'status':'PASS','checks':total,'files':len(files),'run':str(R)},indent=2))
