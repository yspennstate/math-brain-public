from pathlib import Path
from fractions import Fraction
import datetime, hashlib, json

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
ROOT=AGENT.parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
fields=protocol['required_per_run']

def dump(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

audit=json.loads((RUN/'out/audit.json').read_text())
pilot=json.loads((RUN/'out/pilot.json').read_text())
assert audit['status']=='PASS' and audit['cases']==291 and audit['checks']==2475
assert audit['elapsed_seconds']<55 and pilot['elapsed_seconds']<55
assert audit['endpoint_eligible_counts']=={'1':2,'2':12,'3':16}
witness=json.loads((RUN/'out/witness_certificate.json').read_text())
assert len(witness)==5 and all(Fraction(row['gap_lower_exact'])>0 for row in witness)

source_paths=[protocol_path,ROOT/'BOARD.md',ROOT/'claude/B17/STREAM_NOTES.md',
    ROOT/'agents/A090/runs/20261013T213537Z-fleet05-A090-independent-reconstruction/REPORT.md',
    ROOT/'agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger/REPORT.md',
    ROOT/'agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger/CLAIMS.json',
    ROOT/'agents/A096/runs/20261013T220343Z-fleet05-A096-live-gap-ledger/DERIVATION.md',
    ROOT/'agents/A073/runs/20261013T234148Z-fleet05-A073-certified-logarithms/REPORT.md',
    ROOT/'agents/A099/runs/20261014T001305Z-fleet05-A099-candidate-assembly/REPORT.md',
    AGENT/'runs/20261013T213517Z-fleet05-A085-certificate-adversary/REPORT.md']
receipts=[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size,'receipt_time':stamp} for p in source_paths]
dump(RUN/'out/source_receipts.json',receipts)

statement=('For every N>=1 the minimum positive physical influence of a uniform-cube Boolean sign is N*2^(1-N). '
 'At equality the signs are exactly point defects and complements for N>=3, the two nonconstant one-bit signs for N=1, '
 'and the eight point/complement signs plus four signed dictators for N=2. For every fixed ell>=2, '
 'at cutoff s_*(N)=N-1-log2 N the all-dimensional suprema of R_geell/I and M_geell/I are exactly 2 and 1, '
 'strictly approached but unattained at finite N. Here R uses phi(x,y)=(x+y)h2(y/(x+y)) and M uses y log2((x+y)/y) '
 'on edges whose lower endpoint has size at least ell. The unrestricted constants exceed 107/40 and 47/40 respectively, '
 'witnessed by the five-bit sign negative exactly on {5,12,13}. Thus loss-free optimal-tail completeness cannot extend '
 'from sublinear cutoffs to arbitrary finite nonnegative cutoffs. A090@1 and A096@1 retain their explicitly stated '
 'sublinear scope; no full FEI conclusion is asserted.')
hypotheses=['Actual Boolean signs on finite uniform physical cubes; N>=1; constants excluded from ratios',
 'Bits and ordinary physical flip influence; zero masses by continuity',
 'Every fixed ell>=2; binomial coefficients outside their range interpreted as zero',
 'Endpoint cutoff s_*(N); no assertion for growing ell or arbitrary linear cutoffs']
claim={
 'claim_id':'A085-MINIMUM-INFLUENCE-CUTOFF-ENDPOINT','version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A085'],'proof_source':{'path':str(RUN/'PROOF.md'),'checker':str(RUN/'code/audit.py'),'validation':str(RUN/'out/audit.json')},
 'proof_dependencies':[],
 'review_records':[{'reviewer':'A090','verdict':'PENDING_PRIMARY'},{'reviewer':'A094','verdict':'PENDING_ALTERNATE'}],
 'status':'NARROW_SCOPE_CERTIFICATE_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unasserted extension of optimal higher-tail completeness to every finite nonnegative dimension cutoff'],
 'first_unproved_line':None,'next_consumers':['A090','A096','A073','A099','B17','B20']}
assert set(claim)==set(fields['claim_fields'])
dump(RUN/'CLAIMS.json',[claim])
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B17','packet_id':'A085',
 'gap_id':'C018-CUTOFF-TERMINAL-SCOPE','attempt_id':'A085-stage3-minimum-influence-endpoint',
 'method':'Independent direct-character/Fraction certificate plus all-dimensional edge-isoperimetry and tail counting',
 'mathematical_delta':'Exact nonempty cutoff endpoint has optimal higher-tail ratios 2 and 1; source sublinear hypotheses survive and cannot be dropped',
 'deliverable_status':'COMPLETE_LOCAL_SAVE','mathematical_status':'SCOPED_ENDPOINT_PROVED; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',
 'claim_versions_used':['A090-PARITY-TAIL-LOW-INFLUENCE-COMPLETENESS@1 (scope target, not proof premise)',
 'A096-TERMINAL-KL-REFUND-AUDIT@1 (scope target, not proof premise)'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':[str(p) for p in source_paths],
 'next_consumers':claim['next_consumers'],
 'next_action':'Audit a source-complete signed-Boolean terminal-core KL lower bound against complete normalized Q and one physical influence reserve; A090/A094 review endpoint certificate',
 'stagnant_substantive_attempts':0,
 'blockers':['No finite universal terminal-core KL payment supplied; source universal gap persists','Independent review/shared adoption/remote mirrors unverified'],
 'packet_ids':['A085']}
progress_keys={s.split(' (')[0] for s in fields['progress_fields']}
assert set(progress)==progress_keys
dump(RUN/'PROGRESS.json',progress)
(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())

(AGENT/'STATUS.md').write_text('STATE: A085 stage3 complete: exact minimum-influence endpoint tail suprema 2 and 1; 291 cases/2475 checks PASS; source sublinear scope survives; full FEI OPEN.\n'
 'NEXT: A090/A094 review endpoint certificate; audit A001/A096/A073 signed-Boolean terminal-core KL payment with complete Q and one influence reserve; helper-contract correction remains pending.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+' — Stage3 '+RUN.name+': read updated board/lead/status and complete protocol; retired repeated normalized-refund replay after A073/A099 independent audits. Proved sharp minimum-positive-influence equality classification and exact all-dimensional endpoint higher-tail suprema 2 (erasure), 1 (oriented), with N=2 dictator exceptions. Frozen pilot 20 cases/235 checks (0.127179s), full 291 cases/2475 checks (12.526274s), direct characters/Fraction/rigorous series, all PASS. Independently recertified five-bit witness >107/40 on every coordinate. A090/A096 sublinear scopes preserved; arbitrary-cutoff extrapolation fails. Saved all protocol files and handoff; review and full FEI remain open.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n## '+stamp+' — Sharp influence-cutoff endpoint\n'
      'For N>=1, minimum nonzero I is N*2^(1-N). Equality: point defects/complements for N>=3; two one-bit nonconstants; N=2 additionally four signed dictators. Proof: b(A)>=a(N-log2 a) from conditional-fiber entropy, strict concavity endpoint comparison for a>=2. At s_*=N-1-log2 N, for fixed ell>=2 the higher-tail erasure supremum is 2 and oriented supremum 1, never attained at finite N. Point ratio R/I=2-4*2^-N sum_(r<ell) binom(N-1,r); M/I half. K_E>107/40 and K_M>47/40 by actual five-bit {5,12,13}, so arbitrary-cutoff extrapolation fails even when every dimension admits functions. A090/A096 explicitly require o(N) and survive. Nonmonotone sublinear tail-envelope proof is dimension-safe. Endpoint scope does not pay complete terminal-core KL, and fixed ell must remain fixed.\n')

report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+s in report for s in fields['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in RUN.rglob('*') if p.is_file())
dump(RUN/'out/validation.json',{'status':'PASS','timestamp':stamp,'protocol_fields':'EXACT','required_report_fields':'ALL',
    'packet_delta':'BYTE_IDENTICAL','endpoint_counts':audit['endpoint_eligible_counts'],
    'witness_all_five_strict_lower_intervals':'POSITIVE','independent_review':'PENDING','full_FEI':'OPEN'})
manifest=[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':digest(p)}
          for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='manifest.json']
dump(RUN/'out/manifest.json',{'timestamp':stamp,'files':manifest,'max_bytes':max(p['bytes'] for p in manifest)})
print(json.dumps({'status':'PASS','files':len(manifest)+1,'maximum_bytes':max(p['bytes'] for p in manifest),'timestamp':stamp}))
