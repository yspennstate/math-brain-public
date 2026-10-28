from pathlib import Path
import json, hashlib, time, datetime
from fractions import Fraction as F
B=Path('agents/A097'); R=B/'runs/20261023T143952Z-account03-A097-cross-route-transfer'
for d in [R,R/'code',R/'out']: d.mkdir(parents=True,exist_ok=True)
def save(p,x): p.write_text(json.dumps(x,indent=2) if not isinstance(x,str) else x,encoding='utf-8')
spec={'helper_version':'signed-floor-v1','family':'arbitrary finite calibrated laws; actual Boolean three-bit equal-sign seed','domain':'t=12/16; a=1..11/16; 1<=b<ell<=11 in units1/16; candidate z>=ell on same grid; three actual-seed reference examples','case_count':605,'symmetry':'none','arithmetic':'Fraction, integer powers; no floating sign decisions','memory_estimate_MB':30,'maximum_runtime_seconds':20,'frozen_before_execution':datetime.datetime.now(datetime.timezone.utc).isoformat()}
save(R/'out/FROZEN_SPEC.json',spec)
proof='''# Signed sharp admission from an arbitrary current reference

All logarithms are base2. Let p be a finite probability law, r=p(empty), t=1-r>0, and A a subset of nonempty atoms with 0<a=p(A)<t. Let q0 be normalized, q0(empty)=r, finite CE(p,q0), and 0<b=q0(A)<ell<t. Partition-preserving compatibility means that admissible q_z keeps q0 conditional law on A and on C=nonempty\\A, keeps vacuum r, and has q_z(A)=z>=ell. Thus q_z(s)=z q0(s)/b on A and (t-z)q0(s)/(t-b) on C. Ghost atoms are retained in each profile, rather than discarded.

For every such p and q0, the exact minimum signed CE change over this DECLARED class is
Delta = a log(b/z*)+(t-a) log((t-b)/(t-z*)), z*=max(a,ell).
Equivalently Delta=t[D(Bern(a/t)||Bern(z*/t))-D(Bern(a/t)||Bern(b/t))].
The minimizer is unique in z (conditional laws are fixed); finite CE and 0<a<t exclude endpoint minimizers. Proof: expand the CE difference atom by atom. Its derivative is (z-a)/(z(t-z) ln2), so the minimum on [ell,t) is max(a,ell). This is a general theorem, with no Boolean or dimension assumption. The difference is signed. In particular a mandatory crossing b<ell does NOT imply a positive debit from arbitrary incoming q0. Positivity requires the displayed KL difference to be positive. For matched q0=p, b=a<ell, the minimum reduces exactly to stage20's positive binary-KL projection.

Constant bound: for the feasible choice z=ell, log(b/ell)<0 and log((t-b)/(t-ell))=log(1+(ell-b)/(t-ell)) <= (ell-b)/((t-ell)ln2). Hence Delta <= (t-a)(ell-b)/((t-ell)ln2). This bound is sufficient but need not be sharp; the exact signed expression is the payment interface. There is no assertion that every prescribed recipe permits profile preservation. If a recipe requires different within-cell conditionals, this theorem is not its full conversion price.

# Exact substitution into the original owner

At actual physical terminals h of a previously exposed finite query tree, retain BOTH outcomes and their actual reaches rho_h. Suppose full current spectral law P_h decomposes into disjoint controller part plus beta_h times seed law p_h, and full current reference Q_h has the IDENTICAL controller part plus beta_h q0_h, with 0<=beta_h<=1. Current references are normalized and finite CE. Apply the stated profile-preserving conversion only within each seed part, leaving beta_h and controller part fixed. Direct cancellation gives exact full CE change beta_h Delta_h. Let C=sum_h rho_h CE(P_h,Q_h), original capacity B, and ALL still-charged earlier bills U be supplied with C+U<=B. Set M=B-C-U. The same original account pays ALL converted full terminals if and only if sum_h rho_h beta_h Delta_h<=M. A conservative sufficient test is sum rho_h beta_h max(Delta_h,0)<=M. The exact residual is M-sum rho_h beta_h Delta_h. No capacity is renewed after revealing variables; no reach is omitted; no multiplier counting leaves is allowed. Negative changes are releases of prepaid CE, and must not be booked twice elsewhere. Inherited reference marginalization after conversion obeys the usual full-child identity CE increment=-D_occ<=0; both full children and old U stay in the account. This identity needs no new source or reset.

# Actual Boolean endpoint and signed contrast

Take g(y)=-1 exactly at (+,+,+) and (-,-,-), +1 elsewhere. Direct Walsh expansion is g=(1-y1y2-y1y3-y2y3)/2. Its spectral law is1/4 each on empty,12,13,23. Query y1; BOTH full children have uniform spectrum on empty,2,3,23. At each terminal let A={23}, ell=1/3, t=3/4. For matched seed q0=(1/4,1/4,1/4,1/4), Delta=(1/4)log(27/25)>0. For incoming q0=(1/4,5/16,5/16,1/8), the same required profile-class admission yields the same final q*=(1/4,5/24,5/24,1/3), but Delta=(1/4)log(27/32)<0. Both incoming laws are normalized, coherent, finite CE, and below the declared floor. With the supplied stage20 disjoint controller seed weight beta=3/8, full changes are (3/32)log(27/25) and (3/32)log(27/32). All stated signs follow from the rational arguments alone. The negative case starts with higher paid mismatch. This is not a new refund of zero-information physical queries.

# Scope and first unsupported line

This proves the sharp arbitrary-INCOMING-reference price for one compatible profile-preserving floor, and the exact substitution into a supplied original account. It does not construct a useful universally required floor, prove a given downstream algorithm accepts these within-cell profiles, or supply an influence-priced arbitrary-core initial source. First unsupported universal line: for every Boolean core construct a complete useful original source with B<=K I(core) and enough ACTUAL unused M to meet a necessary compatible admission/stopping obligation after all prior charges. No such construction is proved here. FEI is OPEN; no universal constant or counterfamily is claimed. External review is pending.
'''
save(R/'PROOF.md',proof)
checker='''from fractions import Fraction as F
import time,json
from pathlib import Path
start=time.perf_counter(); checks=0; cases=0; t=F(3,4)
def ck(v):
 global checks
 assert v
 checks+=1
for ia in range(1,12):
 a=F(ia,16)
 for ib in range(1,11):
  b=F(ib,16)
  for il in range(ib+1,12):
   ell=F(il,16); z=max(a,ell); cases+=1
   p=[F(1,4),a,(t-a)/3,2*(t-a)/3]
   q0=[F(1,4),b,(t-b)/5,4*(t-b)/5]
   q=[F(1,4),z,q0[2]*(t-z)/(t-b),q0[3]*(t-z)/(t-b)]
   ck(sum(p)==sum(q0)==sum(q)==1); ck(q[1]>=ell)
   ck(q[2]/q[3]==q0[2]/q0[3]); ck(q[0]==q0[0])
   raw=F(1)
   for pi,qi,qi0 in zip(p,q,q0): raw*=(qi0/qi)**int(48*pi)
   compressed=(b/z)**int(48*a)*((t-b)/(t-z))**int(48*(t-a))
   ck(raw==compressed)
   best=z**ia*(t-z)**(12-ia)
   for iz in range(il,12):
    v=F(iz,16); ck(best>=v**ia*(t-v)**(12-ia))
   ck(time.perf_counter()-start<20)
# Independent direct Walsh endpoint; no FFT helper imported.
g=[-1 if x in (0,7) else 1 for x in range(8)]
def law(vals):
 N=len(vals); out=[]
 for s in range(N):
  w=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals)); out.append(F(w*w,N*N))
 return out
ck(law(g)==[F(1,4),0,0,F(1,4),0,F(1,4),F(1,4),0])
for bit in (0,1):
 child=[g[(x<<1)|bit] for x in range(4)]; ck(law(child)==[F(1,4)]*4)
 p=[F(1,4)]*4; target=[F(1,4),F(5,24),F(5,24),F(1,3)]
 for q0,ratio in [([F(1,4)]*4,F(27,25)),([F(1,4),F(5,16),F(5,16),F(1,8)],F(27,32))]:
  product=F(1)
  for old,new in zip(q0,target):product*=old/new
  ck(product==ratio)
ck(F(27,32)<1<F(27,25))
print(json.dumps({'status':'PASS','cases':cases,'exact_assertions':checks,'seconds':time.perf_counter()-start,'arithmetic':'Fraction/integer products, direct characters; no floating signs'},indent=2))
'''
save(R/'code/check.py',checker)
import subprocess,sys
res=subprocess.run([sys.executable,'-B','-X','utf8',str(R/'code/check.py')],capture_output=True,text=True,timeout=25)
save(R/'out/CHECK_STDOUT.txt',res.stdout);save(R/'out/CHECK_STDERR.txt',res.stderr)
if res.returncode: raise RuntimeError(res.stderr)
val=json.loads(res.stdout);save(R/'out/VALIDATION.json',val)
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
prev=json.loads((B/'runs/20261023T121505Z-account03-A097-cross-route-transfer/PROGRESS.json').read_text())
sourcepaths=[Path('BOARD.md'),Path('claude/B20/STREAM_NOTES.md'),B/'runs/20261023T121505Z-account03-A097-cross-route-transfer/PROOF.md',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
sources=[]
for p in sourcepaths:
 content=p.read_bytes();sources.append({'path':str(p),'sha256':hashlib.sha256(content).hexdigest()})
save(R/'out/SOURCES.json',sources)
statement='For every finite calibrated current seed law p and finite-CE reference q0 with fixed vacuum r, t=1-r, event masses 0<a=p(A)<t and 0<b=q0(A)<ell<t, the minimum CE change over references preserving q0 conditional profiles on A and its nonempty complement and imposing mass>=ell is Delta=a log2(b/z)+(t-a)log2((t-b)/(t-z)), z=max(a,ell). For disjoint coherent seed blocks of weights beta_h in full actual terminals of reaches rho_h, replacement costs exactly sum rho_h beta_h Delta_h, payable from SAME original B after current full CE C and ALL old U iff this sum<=B-C-U. Signs may differ: actual three-bit equal-sign seed terminal gives beta3/8 prices (3/32)log2(27/25)>0 from matched reference and (3/32)log2(27/32)<0 from coherent (1/4,5/16,5/16,1/8).'
claim=dict(claim_id='A097-SIGNED-ARBITRARY-REFERENCE-FLOOR-OWNER',version=1,exact_statement=statement,hypotheses=['Finite laws and bits; fixed vacuum, 0<a<t and 0<b<ell<t','DECLARED class preserves current within-cell conditional profiles including ghosts','Actual supplied full coherent decomposition and original B,C,U; both outcomes retained','No universal necessity, influence source price or free renewal'],statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A097'],proof_source={'path':str(R/'PROOF.md'),'sha256':hashlib.sha256(proof.encode()).hexdigest(),'formal_verification':'NOT_CLAIMED'},proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_SCOPED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line='Construct a useful required compatible admission for every Boolean core and influence-price its original source and actual remaining capacity.',next_consumers=['A085','A083','A094','A096','A098','A099','B20'])
save(R/'CLAIMS.json',[claim])
nextaction='A085/A094 independently check signed profile-preserving admission and SAME original-owner substitution; A050/A011 specify a useful mandatory compatible class and original O(I) source. Supervisor reconcile old T-20261023-429 lock-blocked closure; mirror pending.'
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B20',packet_id='A097',gap_id='G-R-MISMATCH',attempt_id='stage21-signed-arbitrary-reference-floor',method='Exact arbitrary-reference binary projection; signed current CE substitution and direct Walsh Boolean endpoint',mathematical_delta='Sharp compatible-class admission from ARBITRARY supplied reference; nonpositive release example prevents double billing prepaid KL; same depleted original owner test is exact; '+str(val['exact_assertions'])+' exact assertions PASS.',deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_PROOF_PENDING_REVIEW_FULL_FEI_OPEN',claim_versions_used=[],claims_created_or_changed=[claim['claim_id']+'@1'],source_artifacts=['PROOF.md','out/FROZEN_SPEC.json','out/VALIDATION.json','out/SOURCES.json'],next_consumers=claim['next_consumers'],next_action=nextaction,stagnant_substantive_attempts=0,blockers=['Universal useful mandatory class and initial influence-priced source OPEN','Independent review and supervisor mirror pending','Previous shared checklist closure remains lock blocked; no shared mutation attempted','Brain self-care degraded: personal model/state/dream stale; current math sources used instead'],packet_ids=['A097'])
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
texts=[
'Price a compatible declared floor for an arbitrary incoming calibrated reference, in bits, retaining its conditional profiles; exact hypotheses and all constants are in PROOF.md. This is a supplied-source theorem, not full FEI.',
'Current BOARD read at stage start (14:39 UTC revision); B20 STREAM_NOTES v2 read; stage20 PROOF.md read in full for the matched special case; execution protocol v2 read in full. Exact byte hashes in out/SOURCES.json. Board review announcements are contextual, not new proof dependencies. No new literature priority asserted.',
'PROOF.md gives full elementary differentiation proof, disjoint full-law cancellation, exact SAME-owner substitution, Boolean endpoint and the first unsupported universal source/class construction. Admission cost can be negative because incoming mismatch is prepaid; neither negativity nor a necessary class permits booking the same release twice.',
'Frozen spec precedes checker. Command: python -B -X utf8 code/check.py. '+json.dumps(val)+'. Exact rational power comparisons validate finite candidates; direct Walsh reconstruction independently validates both physical children. Analytic derivative supplies continuum and all-dimensional finite-law proof. No numerical logarithm signs or Lean claim.',
'No external mathematical dependency is needed for the elementary projection and owner identity. Matched stage20 is recovered exactly. New scope is arbitrary incoming references in a profile-preserving class. Downstream accounts must use the signed CURRENT difference, rather than charge positive matched-source KL a second time.',
nextaction,
'All required local artifacts saved and read back by code/finalize.py; hashes and schema receipts in out/PERSISTENCE.json. Files remain below20MB; no >300MB job or shared writes. Previous shared checklist lock remains an administrative blocker; supervisor mirror and external review unverified.'
]
report='# A097 stage21: signed arbitrary-reference admission\n\n'
for h,t in zip(protocol['required_per_run']['report_fields'],texts): report+='## '+h+'\n\n'+t+'\n\n'
report+='**Universal bridge**: C024 history transfer advances by one exact arbitrary-INCOMING-reference admission interface: the price is signed, profile-compatible and charged against the SAME original remaining B-C-U across ALL full terminals. C018/C019/C020 receive no universal bound. What remains is a useful universally required compatible profile or an influence-priced original source with sufficient genuine unused capacity. Specifying that source/class is the shortest route because another matched-source restricted example cannot settle the unpaid universal supplier.\n'
save(R/'REPORT.md',report)
save(B/'STATUS.md','STATE: A097 stage21 saved: sharp SIGNED arbitrary-current-reference compatible-floor theorem; SAME depleted original account; '+str(val['exact_assertions'])+' exact checks PASS; independent review pending; FEI OPEN.\nNEXT: '+nextaction+'\n')
for name,entry in [('WORKLOG.md','Stage21: generalized matched floor to arbitrary incoming calibrated reference with fixed conditional profiles; exact Delta and depleted original-owner criterion. Actual Boolean endpoint proves required floor may RELEASE prepaid mismatch: beta price(3/32)log2(27/32)<0. '+str(val['exact_assertions'])+' exact checks PASS; universal source/class unresolved.'),('LEARNED.md','For fixed-vacuum profile-preserving floor q(A)>=ell and incoming b<ell, actual mass a, optimum z=max(a,ell), signed cost a log2(b/z)+(t-a)log2((t-b)/(t-z)). Mandatory crossing does not imply positive cost for arbitrary reference. Full budget change=sum reach*beta*Delta; charge SAME B-C-U, never double book released mismatch. Matched p recovers old positive theorem; useful universal compatible class/source still missing.')]:
 with (B/name).open('a',encoding='utf-8') as f:f.write('\n2026-10-23T14:39:52Z '+entry+'\n')
assert list(progress)==[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert list(claim)==protocol['required_per_run']['claim_fields']
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
assert len((B/'STATUS.md').read_text().splitlines())==2
files=[p for p in R.rglob('*') if p.is_file()]; assert all(p.stat().st_size<20000000 for p in files)
receipt={'schema':'PASS','progress_delta_equal':True,'status_two_lines':True,'claim_hash_verified':hashlib.sha256(json.loads((R/'CLAIMS.json').read_text())[0]['exact_statement'].encode()).hexdigest()==claim['statement_sha256'],'files':[{'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files],'time':datetime.datetime.now(datetime.timezone.utc).isoformat()}
save(R/'out/PERSISTENCE.json',receipt)
print(json.dumps({'run':str(R),'validation':val,'persistence':'PASS','time':receipt['time']}))
