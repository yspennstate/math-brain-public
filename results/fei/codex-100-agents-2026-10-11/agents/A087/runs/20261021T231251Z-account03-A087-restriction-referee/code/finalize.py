from pathlib import Path
from fractions import Fraction as F
import json,hashlib,datetime,importlib.util
ROOT=Path(__file__).resolve().parents[1];OWN=ROOT.parents[1]
def write(name,v):
 p=ROOT/name;p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n' if not isinstance(v,str) else v,encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
run=ROOT.name
priority=json.loads((ROOT/'out/PRIORITY.json').read_text(encoding='utf-8'))
profiles=json.loads((ROOT/'out/PROFILES.json').read_text(encoding='utf-8'))
assert priority['status']==profiles['status']=='PASS'
total=priority['exact_assertions']+profiles['exact_assertions']
assert total==444190
leanpath=ROOT/'out/LEAN.json'
lean=json.loads(leanpath.read_text(encoding='utf-8')) if leanpath.exists() else None
if lean:
 try:formal=json.loads(lean['stdout'])
 except json.JSONDecodeError:formal={}
else:formal={}
formal_status=str(formal.get('result',{}).get('status','NOT_STARTED_MEMORY_ADMISSION' if not lean else 'RUNTIME_UNVERIFIED'))
# Freeze this single already-declared branch witness readback before computing it.
write('READBACK_SPEC.json',{'helper':'a087-independent-referee-v1','family':'priority core mask194 only','domain':'actual a=0,x=1,y0=1 branch','case_count':2,'symmetry':'none','arithmetic':'same audited exact Fraction interval helper; direct characters/edges','memory_estimate_mb':30,'maximum_runtime_seconds':55})
s=importlib.util.spec_from_file_location('a087_referee',ROOT/'code/referee.py');M=importlib.util.module_from_spec(s);s.loader.exec_module(M)
v=tuple(1 if (194>>i)&1 else -1 for i in range(8));t=M.compose(v)
parent=M.restrict(M.restrict(t,1,0),0,1);child=M.restrict(parent,1,1)
rp=M.add(M.stats(parent)[3],M.tail(parent));rc=M.add(M.stats(child)[3],M.tail(child))
M.check(rc[0]<=1<=rc[1]);M.check(M.sub(rc,rp)[0]>F(1,4))
write('out/BRANCH_READBACK.json',M.serial({'status':'PASS','core_mask':194,'physical_history':'a=0,x=1,y0=1','reach':F(1,8),'parent_R':rp,'child_R':rc,'increase':M.sub(rc,rp),'assertions':M.NTEST}))
sources=[]
base=Path('agents')
for a,r,files in [('A064','20261021T151814Z-account03-A064-global-debt-potential',['PROOF.md','CLAIMS.json','code/adaptive.py','out/FULL.json']),('A062','20261021T223510Z-account03-A062-influence-compensator',['PROOF.md','CLAIMS.json','code/check.py']),('A065','20261021T171653Z-account03-A065-stopping-rule-falsifier',['REPORT.md','CLAIMS.json']),('A061','20261014T085352Z-account05-A061-entropy-process',['out/EXHAUSTIVE_CHECK.json'])]:
 for f in files:
  p=base/a/'runs'/r/f;sources.append({'path':str(p),'sha256':digest(p),'use':'A064 canonical root import only' if a=='A061' else 'source-bound scoped reconstruction'})
write('out/SOURCE_PINS.json',sources)
statements=[
 ('A087-A064-ALL-POLICY-RESERVE-AUDIT','For every labelled three-bit Boolean core in the A064 essential-exposed priority fixture, conditional on the pinned A061-reviewed canonical root debit and one originally unused expected mean child S4 owner, the actual booked-product backward maximum over every adaptive physical continuation and stopping cut has total positive booking W<Sbar/20. The nonnegative R=TC+T after root has drift at least the actual outcome KL, retaining both terminal H+TC bills, with no renewed descendant owner. The mask194 a=0,x=1,y0=1 branch of physical reach1/8 has reserve increase greater than1/4. This is finite conditional scope only.', ['three ambient core bits, genuine sign outputs, disjoint actual controls','canonical root debit from pinned source; post-root products and fair extension on reference-only fibers','original EXPECTED Sbar owner genuinely unused; no branchwise renewal','finite adaptive physical policies; full terminal H+TC retained'], 'A064-OWNED-NONFLAT-TWO-CONVERSION-REFERENCE-RESERVE',2),
 ('A087-A062-ALL-PRICE-EARLY-TAG-AUDIT','For every real C>=6 and positive even k, the canonical quadratic bent/zero-vertex-flip profile M and independent majority3 seed a have zero least nonnegative prescribed increasing-data-pair-then-tag and increasing-seed complete reserves. Nevertheless the actual tag-then-all-seed stopping prefix for F=A+w*a*B, t=2^-k, has full-terminal debt epsilon_C=D_w(M)+2t-(5/2)Ct>t(k-(5/2)C). Therefore every fixed C>=6 fails the proposed early-tag extension with the SAME zero inherited graft bank at sufficiently large even k. Debts and both terminal spectra add on every finite disjoint product. This refutes that policy extension, not delayed-tag payment or full FEI.', ['finite uniform cubes and bit entropy','canonical quadratic bent k and single zero-vertex sign flip; k positive even','fresh independent majority3 seed and fair tag','C any real >=6, with k>5C/2 for positive guaranteed debt','prescribed profile tag-last versus challenged tag-first policy; both terminals and queried influence retained'], 'A062-B05-MINIMAL-RESERVE-CREDIT',6)
]
claims=[]
for cid,statement,hyp,source,version in statements:
 claims.append({'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A087 independent referee; source authors credited in dependencies'],'proof_source':{'paths':['PROOF.md','REPORT.md','code/referee.py'],'validation':['out/PRIORITY.json','out/PROFILES.json','out/BRANCH_READBACK.json']},'proof_dependencies':[{'claim_id':source,'version':version,'scope':'new appended scope only; no acceptance of older bundled claims'},*([{'artifact':'A061 out/EXHAUSTIVE_CHECK.json','sha256':'6c48a94c44b030dfb851f33d99024e9fa91c7761dbfbd1bee400aa01862d2582','scope':'reviewed canonical root debit imported without reset'}] if version==2 else [])],'review_records':[{'reviewer':'A087','verdict':'HOLDS_AT_STATED_SCOPE','method':'independent written reconstruction, direct character sums and physical edges; exact rational interval sign certificate','material_source_repair':False}],'status':'INDEPENDENT_RECONSTRUCTION_HOLDS_SCOPED','supersedes':[],'refutes':[] if version==2 else ['hypothetical same-zero-bank early-tag extension for any fixed C>=6'],'first_unproved_line':None,'next_consumers':['A038','A039','A061','A062','A064','A065','A094','B20']})
write('CLAIMS.json',claims)
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run,'stream':'B18','packet_id':'A087','gap_id':'G-R-MISMATCH','attempt_id':'A087-resumed-owned-reference-independent-audit','method':'independent physical-child reconstruction and exact bounded certificates','mathematical_delta':'A064 v2 all-policy finite interface and appended A062 v6 all-price early-tag obstruction independently HOLD at explicit scope; 444190 main exact assertions plus targeted branch readback; arbitrary-core eligibility unpaid','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_AUDITS_HOLD_FULL_FEI_OPEN','claim_versions_used':[{'claim_id':'A064-OWNED-NONFLAT-TWO-CONVERSION-REFERENCE-RESERVE','version':2},{'claim_id':'A062-B05-MINIMAL-RESERVE-CREDIT','version':6},{'claim_id':'A065-EARLY-TAG-GRAFT-OBSTRUCTION','version':1}],'claims_created_or_changed':[c['claim_id']+'@1' for c in claims],'source_artifacts':sources,'next_consumers':['A038','A039','A061','A062','A064','A065','A094','B20'],'next_action':'Carry the SAME hidden-tag reserve through the next mixed data/seed physical query with both actual terminals, or name additional unused signed ancestor capacity; no price sweep or finite-depth extension','stagnant_substantive_attempts':0,'blockers':['Universal arbitrary-core eligible unused ancestor bank or selected paid policy remains unproved; no mirror/adoption observed'],'packet_ids':['A087']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Independently audit A064 v2 all-policy owned-reference transfer on all256 labelled three-bit cores and the appended A062 v6 all-price early-tag obstruction for every real C>=6 and every positive even width. Use exact physical children, conditional fair probabilities, one inherited owner and complete terminal entropy. Entropies/KL are bits. Full FEI remains OPEN. Current owner October23 deadline supersedes the older protocol endpoint; no schedule is changed.

# sources actually read, revisions and theorem locators

Read machine instructions and execution protocol2; current BOARD, B18 leadv2, own prior STATUS/LEARNED and substantive result chain; campaign README/status/registries/actions and plan restriction passages; supplemental campaign/claims/counterexamples/seed/crosswalk and supplied paper restriction/composition locators, including earlier versions. B18's old NPN/A057 targets were already completed in the inherited results; current live board dependencies and saved NEXT govern this resumption. New proof sources: A064 PROOF sections Product-query quantities, Coverage and Exact certificate; A062 PROOF sections1--3, including all-width bases; A065 exact prefix/terminal scope; pinned A061 canonical root intervals. Source pins and baseline intake distinguish read passages from byte-loaded navigation; no new external paper theorem is imported. One read-only math recall gave related bent-splice and restriction cards, no added premise. The session wake reported stale personal-context notes; owner was alerted before reliance and these notes are not mathematical inputs.

# complete derivation or exact first unsupported line

PROOF.md gives both complete reconstructions. A064: actual incoming product support contains p; predicted outcomes include reference-only fibers and actual outcomes remain fair. D=O+mean TCchild-TCparent equals the signed spectator-Jensen formula. Backward max over next coordinates and separately optimal physical branches covers EVERY adaptive policy and stopping cut. R=TC+T has required drift. All256 strict rational comparisons20W_upper<Sbar_lower pass conditional on the pinned original root transaction. Terminal H+TC remains. The mask194 physical reach1/8 branch has reserve growth>1/4, independently read back. The surviving19/20 owner claim is EXPECTED over cuts, not separately available on every branch.

A062: reconstruct both exceptional-state transitions, coefficient multiplicities, clean branch price4, width0/2/4 bases, and C=6 induction with strict -21/128 margin. Monotonicity in C proves zero profile/seed bank for every real C>=6. A self-contained scalar JS derivative bound verifies the channel estimate used in the odd-state induction. The actual tag/seed prefix retains bent and flipped-bent terminal spectra with fair total weights; debt>2^-k(k-5C/2). Every finite disjoint product adds these debts and terminal costs. Root influence also grows, so this is no FEI disproof. Older retained A062 v5 clauses are not reaccepted wholesale.

First unsupported universal line: an arbitrary-dimensional nonflat core admits an eligible actually unused ancestor source paying the selected signed conversion and both continuations, or a globally paid policy keeping the tag hidden. Neither the finite positive Sbar certificate nor increasing a fixed early-tag price proves that line.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC predates searches. Run python -B -X utf8 code/referee.py priority --pilot, profiles --pilot, then priority and profiles from this run's parent path. Four-core pilot:7625 assertions; two-width pilot:139 assertions. Main priority:256 roots,12050 restricted states,34448 query choices,1920 reference-only queries,{priority['exact_assertions']} exact assertions in{priority['seconds']:.6f}s. Main profiles:widths2,4,6,8,10,12; direct character spectra and complete physical profile trees through6; exact C=6 boundary and fixed6.5218 witness;{profiles['exact_assertions']} exact assertions in{profiles['seconds']:.6f}s. Total main {total}; pilot counts excluded. Targeted READBACK_SPEC and out/BRANCH_READBACK independently record source mask194 branch growth. No automatic dimension change, symmetry quotient or floating signs. Estimate120MB; peak unmeasured; each mathematical job within55s and below the heavy-job threshold.

The source uses FWHT and96-bit32-term logs; this reconstruction uses direct character dot products and112-bit40-term positive atanh logarithm enclosures. For normalized u in[1,2], z in[0,1/3], tail<=2z^81/(81(1-z^2)); outward Fraction dyadic rounding and denominator endpoints bound every log. All inequalities use separated rational endpoints. Identity interval overlaps are diagnostics only; written algebra proves identities. Fresh memok precedes the isolated core Lean attempt. Formal status and exact compiler/source receipt are in out/LEAN.json or the admission record: {formal_status}. No full entropy theorem is claimed Lean-certified. Mathematical rung: independent written proof reconstruction plus exact finite certificates; formal check concerns only one-step integer accounting.

# proof dependencies and changed downstream conclusions

Conditional A064 canonical root debit is imported at SHA2566c48a94c44b030dfb851f33d99024e9fa91c7761dbfbd1bee400aa01862d2582, with every repeated root record checked consistent. Every subsequent product/reference transaction, physical child, influence and maximum is independently recomputed. A064's finite all-history interface HOLDS at its original owner hypothesis; no arbitrary-dimensional estimate is imported. Appended A062 all-price obstruction HOLDS independently and validates the A065 early-tag prefix/product mechanism. No material source repair was required, and no broader retained claim is implicitly accepted. Source trees and other agents are unchanged.

# one next mathematical action and independent reviewer

Carry the SAME delayed-tag reference/reserve through the next actual mixed seed/data query, keeping prior bookings and both complete terminals, or exhibit a separately unused signed ancestor source. A062/A064 develop this policy invariant; A094 independently reviews this source-bound reconstruction; A038/A039/A061 consume the completed finite boundary. No further depth extension of this three-bit interface or fixed-price sweep is useful.

# actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS, identical PACKET_DELTA, PROOF, frozen specs, independent executable checker, main/pilot outputs, branch readback, source pins, formal-attempt evidence and schema/hash receipts are saved locally in the assigned A087 run. STATUS is two lines; WORKLOG appended and LEARNED updated. No git, mail, brain write, other-agent mutation, trading access, GPU, detached process or running-work termination. Supervisor copy, mirror verification, central adoption and public release remain unobserved; no local save blocker.

**Universal bridge:** C019 stopping-tree payment and C024 history transfer gain independent acceptance of A064's EVERY-policy finite owned-reference certificate and A062's EVERY-fixed-price early-tag obstruction, with one original owner and full terminal H+TC retained. The remaining universal gap is arbitrary-core bank eligibility or a paid reveal policy preserving the hidden tag. NEXT addresses that specific ownership/policy step, while the now-closed finite-depth and price-sweep routes would leave full FEI untouched.
'''
write('REPORT.md',report)
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(OWN/'STATUS.md').write_text('STATE: Resumed audit complete: A064 v2 all-policy finite reserve and A062 v6 all-price early-tag obstruction independently HOLDS;444190 main exact assertions;full FEI OPEN.\nNEXT: Carry SAME hidden-tag ancestor reserve through next mixed data/seed query with both terminals; identify additional unused signed capacity if revealing tag early.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} {run}: independently reconstructed A064v2 and appended A062v6. Main444190 exact assertions PASS; finite expected-owner1/20 bound and all-real-C>=6 obstruction HOLD. Direct-character checker and branch-growth readback saved. Root canonical debit remains pinned dependency. Full FEI OPEN.\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n## Resumed account03 independent review\n\n- A064v2 all-policy finite certificate independently HOLDS: direct-character/physical-edge reconstruction reproduces12050 states,34448 queries,1920 reference-only cases; one original expected Sbar funds W<Sbar/20. This is a stopping-cut expectation, never a new branchwise19/20 bank.\n- Appended A062v6 independently HOLDS: exceptional E/O induction has price6 zero profile reserve for every even width, hence every real C>=6 by monotonicity; early tag then majority3 seed costs epsilon>2^-k(k-5C/2) with both complete terminals. No larger fixed price repairs this same-zero-bank policy.\n- Scalar JS check: phi(z)<=1-sqrt(1-z^2), by atanh(z)<=z/sqrt(1-z^2), proves JS<=2d/ln2 including endpoint limits.\n- Universal unpaid step remains eligible unused ancestor signed capacity or selected delayed-tag policy through mixed seed/data queries. Do not repeat the completed three-bit depth extension or fixed-price sweep.\n')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
pf={s.split(' (')[0] for s in protocol['progress_fields']};cf=set(protocol['claim_fields'])
assert set(progress)==pf
for c in claims:
 assert set(c)==cf
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for heading in protocol['report_fields']:assert '# '+heading in report
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[p for p in ROOT.rglob('*') if p.is_file()]
assert all(p.stat().st_size<20_000_000 for p in files)
write('out/SCHEMA_CHECK.json',{'status':'PASS','exact_claim_fields':True,'exact_progress_fields':True,'statement_hashes':True,'packet_delta_identical':True,'report_fields':True,'rolling_status_two_lines':True,'file_size_limit':True,'main_assertions':total,'formal_status':formal_status})
write('out/PERSISTENCE_RECEIPTS.json',[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files])
print(json.dumps({'status':'COMPLETE_LOCAL','main_assertions':total,'formal_status':formal_status,'run_id':run,'branch_readback_assertions':M.NTEST}))
