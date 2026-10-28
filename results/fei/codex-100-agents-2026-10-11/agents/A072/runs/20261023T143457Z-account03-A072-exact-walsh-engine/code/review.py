"""A072 independent whole-row reconstruction; imports only own prior engine."""
from drift import *
from pathlib import Path
import hashlib,copy
R=ROOT; BASE=R.parents[1]; PEER=BASE.parent/'A075'/'runs'/'20261023T133516Z-account03-A075-search-to-theorem-bridge'
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
spec=dict(helper='A072 stage21 whole-row v1; own stage20 arithmetic/FWHT',family='all16 two-input outer gates; cores from constant+, parity2, OR2, negated OR2',domain='two cores each two physical bits',case_count=256,query_rows=1024,symmetry='none',arithmetic='integer direct/FWHT/inverse/edges then exact rational prime-log with outward192bit bounds',memory_estimate_MB=80,max_runtime_seconds=55,pilot='first circuit before remaining255; under60seconds',automatic_dimension_escalation=False)
write(R/'out'/'FROZEN_SPEC.json',spec)
start=time.perf_counter()
def eta(a):return logprofile(a,-a) if a else {}
def L(a,b):return sub(add(eta(a*a),eta(b*b)),times(add(eta((a+b)**2),eta((a-b)**2)),F(1,2)))
def circuit(ts,h):
 p=compose(ts,h); rows=0
 for j in range(2):
  for i in range(2):
   axis=p['offs'][j]+i; N=len(p['truth']); mu=F(sum(ts[j]),4); t=F(p['cores'][j]['W'][1<<i],4)
   special={}; innerother=(3<<p['offs'][j])^(1<<axis)
   for s in range(N):
    if not s>>axis&1 and not s&innerother:
     term=L(F(p['W'][s],N),F(p['W'][s|1<<axis],N));nonnegative(term);special=add(special,term)
   kids=[]
   for b in [0,1]:
    u=list(ts);u[j]=restrict(u[j],i,b);kids.append(compose(tuple(u),h))
   drift=sub(mean([k['C'] for k in kids]),p['C']);ell=L(mu,t)
   ck(drift==sub(times(ell,p['q'][j]),special));nonnegative(ell)
   # Strong bound checked without dividing by approximate ln2: L*ln2 <=2d.
   hi=iv(ell)[1]; bound=ceildiv(hi*__import__('arithmetic').LN2[1],Q)
   ck(bound<=2*p['cores'][j]['ds'][i]*Q)
   nonnegative(sub({2:3*p['ds'][axis]},drift))
   ck(p['I']-sum(k['I'] for k in kids)/2==p['ds'][axis])
   bank=add(p['C'],{2:3*p['I']});kb=[add(k['C'],{2:3*k['I']}) for k in kids]
   nonnegative(bank)
   for a in kb:nonnegative(a)
   margin=sub(bank,mean(kb));nonnegative(margin);credit=[add(a,margin) for a in kb];ck(mean(credit)==bank)
   rows+=1
 return rows
cores=[(1,)*4,(1,-1,-1,1),g(2),tuple(-x for x in g(2))]
count=rows=0
for mask in range(16):
 h=tuple(-1 if mask>>x&1 else 1 for x in range(4))
 for a in cores:
  for b in cores:
   rows+=circuit((a,b),h);count+=1
   if count==1:write(R/'out'/'PILOT.json',dict(verdict='PASS',circuits=1,rows=rows,runtime_seconds=time.perf_counter()-start))
   assert time.perf_counter()-start<55
ck(2**74>3**9*5**25)
write(R/'out'/'VALIDATION.json',dict(verdict='PASS',circuits=count,physical_rows=rows,checks=__import__('drift').CHECKS,runtime_seconds=time.perf_counter()-start,primitive_2d_countercontrol=True,peer_executable_imported=False))
source=json.loads((PEER/'CLAIMS.json').read_text(encoding='utf-8'))[0]
digest=hashlib.sha256(json.dumps({k:source[k] for k in ['exact_statement','hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
assert digest==source['statement_sha256']
source['review_records'].append(dict(reviewer='A072',independent_reviewer=True,verdict='HOLDS_UNCHANGED_SCOPE',method='Independent complete Fourier-row reconstruction and Boolean conditional-mean bound; own engine;256 circuits/1024 physical queries; full proof in REVIEW.md',evidence=['REVIEW.md','out/VALIDATION.json']))
source['status']='INDEPENDENTLY_ACCEPTED_UNCHANGED_SCOPE'
write(R/'CLAIMS.json',[source])
pins={n:hashlib.sha256((PEER/n).read_bytes()).hexdigest() for n in ['CLAIMS.json','PROOF.md']}
write(R/'out'/'SOURCE_PINS.json',dict(source=str(PEER),hashes=pins,statement_sha256=digest))
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B15',packet_id='A072',gap_id='C019-INHERITED-COMPONENT-ELIGIBILITY',attempt_id='stage21-independent-whole-row-review',method='whole-row exact cancellation and independent integer Walsh controls',mathematical_delta='A0752/ln2 drift independently accepted unchanged; rational reserve3 replaces6, saving exactly3I required headroom; INITIAL price remains open',deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_THEOREM_ACCEPTED_FULL_FEI_OPEN',claim_versions_used=['A075-WHOLE-ROW-SIGNED-COMPOSITION-DRIFT@1'],claims_created_or_changed=['A075-WHOLE-ROW-SIGNED-COMPOSITION-DRIFT@1 review only'],source_artifacts=[str(PEER/'PROOF.md'),str(PEER/'CLAIMS.json'),'out/VALIDATION.json','REVIEW.md'],next_consumers=['A075','A074','A080','A089','B20'],next_action='Price initial signed bank on arbitrary indecomposable Boolean cores from genuinely unused original influence; retain both full terminals',stagnant_substantive_attempts=0,blockers=['Universal INITIAL bank payment unproved','Supervisor remote mirror not verified','Brain self-care owner/state/dream stale; mathematical proof checked directly'],packet_ids=['A072'])
assert set(progress)=={k.split(' (')[0] for k in protocol['required_per_run']['progress_fields']}
for claim in [source]:assert set(claim)==set(protocol['required_per_run']['claim_fields'])
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
validation=json.loads((R/'out'/'VALIDATION.json').read_text(encoding='utf-8'))
sections=[
'All finite Boolean outer gates and disjoint Boolean inner cores, fixed partition, uniform physical bits; entropy in bits. Independently review A075-WHOLE-ROW-SIGNED-COMPOSITION-DRIFT@1 unchanged, including all real K>=0 envelope and supplied-credit scope.',
'Current BOARD.md, B15 STREAM_NOTES.md v2, own STATUS.md, execution protocol v2; A075 stage10 PROOF.md sections1-6 and CLAIMS.json. Source byte hashes and original statement digest are pinned in out/SOURCE_PINS.json. Own stage20 engine and exact log helper reused; no peer executable imported. Older campaign intake retained in prior stages, not claimed reread here.',
'REVIEW.md reconstructs the complete all-dimensional proof: whole-row decrement L is nonnegative and homogeneous; all nonexceptional rows cancel; Boolean |mu|+|t|<=1 yields L(mu,t)<=2 Inf/ln2. This is independent acceptance without repair. First unsupported universal line: fund INITIAL C+3I+sum(q rho) by dimension-independent unused original influence. Singleton partition gives H+3I, so coherence alone does not imply FEI.',
'Frozen out/FROZEN_SPEC.json before any circuit. Command: python -B -X utf8 code/review.py. '+json.dumps(validation)+'. Integer Walsh/direct characters, Parseval, every sign inverse and direct physical edges precede entropy. Exact row identity, rational3 drift, nonnegative bank, conditional mean credit conservation and integer-power stronger-guess rejection pass. Finite controls validate implementation; REVIEW.md supplies universal proof. No >300MB job was planned or started.',
'A075 statement, hypotheses, contributors and original digest unchanged; added A072 independent HOLDS record. Original A072 rational6 result remains valid. Downstream may use3I less required headroom, preserving actual already arriving credit; this creates no fresh donor and pays no initial bill.',
'A075/A080/A089: prove an influence price of initial signed bank for arbitrary indecomposable cores using same unused original owners and both full terminal obligations. A074/A092 can audit this independent review; no message sent.',
'Local files saved and reread, schema equality and statement digest checked. Final manifest hashes all run artifacts except itself. Supervisor copying/GitHub/math-brain mirrors remain unverified. Brain self-care degraded: owner101h/state85.6h/dream36.3h stale; direct mathematical source checks used.'
]
textreport='# A072 stage21: independent acceptance of the half-size drift reserve\n\n'
for title,body in zip(protocol['required_per_run']['report_fields'],sections):textreport+='## '+title+'\n\n'+body+'\n\n'
textreport+='## Universal bridge\n\nC019 stopping-tree payment and C024 history transfer gain independently checked reserve2/ln2<3 instead of4/ln2<6: the rational coherent bank needs exactly3I less headroom at every fixed-partition state. This is a verified conditional-transfer improvement, not initial funding. Arbitrary initial signed correction plus inner hulls remains unpaid; singleton cores retain H+3I. The shortest next route is to price that initial bank from actual unused original influence on indecomposable Boolean cores, rather than repeat finite coherence cases. Full FEI remains OPEN.\n'
(R/'REPORT.md').write_text(textreport,encoding='utf-8')
(BASE/'STATUS.md').write_text('STATE: A072 stage21 saved: A075 whole-row drift2/ln2<3 and coherent bank independently HOLDS unchanged;256 circuits/1024 rows exact; FEI OPEN.\nNEXT: A075/A080/A089 price INITIAL signed bank on arbitrary indecomposable cores from SAME unused original influence; singleton bank H+3I remains FEI-equivalent.\n',encoding='utf-8')
for name,entry in [('WORKLOG.md','2026-10-23 stage21: independently reconstructed A075 whole-row cancellation and Boolean mean constraint, accepted original statement unchanged;256 circuits/1024 rows exact with own integer engine. Rational reserve6->3 saves3I headroom, not fresh donor. Initial payment and FEI open.'),('LEARNED.md','A075 whole-row cancellation: drift=q L(mu,t)-sum special L, L>=0 homogeneous. L<=2 min(|mu|,|t|)(|mu|+|t|)/ln2<=2 Inf_inner/ln2 since Boolean conditional means imply |mu|+|t|<=1. Thus rational3 coherent bank suffices universally. A072 independent review stage21 accepts source unchanged. Required headroom falls3I; initial bank not funded, singleton H+3I.')]:
 with (BASE/name).open('a',encoding='utf-8') as f:f.write('\n'+entry+'\n')
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
manifest={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in R.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
write(R/'out'/'MANIFEST.json',manifest)
for name,d in manifest.items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==d
print(json.dumps(dict(verdict='PASS',validation=validation,manifest_entries=len(manifest),source_digest=digest,full_FEI='OPEN')))
