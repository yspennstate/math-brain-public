from pathlib import Path
from fractions import Fraction as Q
import datetime, hashlib, json, platform, sys
sys.set_int_max_str_digits(100000)

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
ROOT=AGENT.parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
PROTOCOL_PATH=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL_PATH.read_text(encoding='utf-8-sig'))
schema=protocol['required_per_run']

def dump(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

src073=ROOT/'agents/A073/runs/20261014T023508Z-account05-A073-certified-logarithms'
src096=ROOT/'agents/A096/runs/20261014T013836Z-account05-A096-live-gap-ledger'
src098=ROOT/'agents/A098/runs/20261014T024504Z-account05-A098-resource-reallocation'
paths=[PROTOCOL_PATH,ROOT/'BOARD.md',ROOT/'claude/B17/STREAM_NOTES.md',
       src073/'REPORT.md',src073/'CLAIMS.json',src073/'DERIVATION.md',src073/'code/audit.py',
       src096/'DERIVATION.md',src098/'REPORT.md',src098/'CLAIMS.json']
dump(RUN/'out/source_receipts.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'receipt_timestamp':NOW} for p in paths])

audit=json.loads((RUN/'out/audit.json').read_text())
pilot=json.loads((RUN/'out/pilot.json').read_text())
assert audit['status']=='PASS' and audit['physical_cases']==4 and audit['compressed_cases']==540 and audit['checks']==4241
assert audit['elapsed_seconds']<55 and pilot['elapsed_seconds']<55
assert (audit['first_naive_nonpositive_d'],audit['first_gate_atom_mass_underflow_d'])==(104,538)
failure=json.loads((RUN/'out/float_failure.json').read_text())
lo,hi=Q(failure['true_lower_exact']),Q(failure['true_upper_exact'])
assert 0<lo<=hi and float.fromhex(failure['naive_D0_hex'])==0
scale=1<<160
short_lower=Q((lo*scale).numerator//(lo*scale).denominator,scale)
short_upper=Q(-(-(hi*scale).numerator//(hi*scale).denominator),scale)
assert 0<short_lower<=lo<=hi<=short_upper
cert_failure={'verdict':'IMPLEMENTATION_FALSE_ZERO; ORIGINAL_SOURCE_LEMMA_SURVIVES',
 'actual_family':'A073 F_d=b(y)+1_(y=0)(q(u,v)-1), q negative only at (1,1)',
 'first_frozen_false_zero_d':104,'physical_dimension':106,
 'floating_D0_hex':failure['naive_D0_hex'],
 'true_D0_outward_lower_exact':str(short_lower),'true_D0_outward_upper_exact':str(short_upper),
 'full_fraction_certificate':'out/float_failure.json',
 'implementation_domain':'Python binary64/math.log2; even d=2..1080; first for this frozen formula only',
 'python':sys.version,'platform':platform.platform(),'helper_sha256':sha(RUN/'code/audit.py'),
 'first_gate_atom_mass_underflow_even_d':538,'first_query_influence_underflow_even_d':1074,
 'first_delta_underflow_even_d':1076,'original_claim_refuted':False,'full_FEI':'OPEN'}
dump(RUN/'CERTIFICATE_FAILURE.json',cert_failure)

source_claims=json.loads((src073/'CLAIMS.json').read_text())
original=next(c for c in source_claims if c['claim_id']=='A073-NONZERO-ERASURE-BINARY-REMAINDER')
reviewed=next(c for c in json.loads((src098/'CLAIMS.json').read_text()) if c['claim_id']==original['claim_id'])
assert reviewed['exact_statement']==original['exact_statement'] and reviewed['hypotheses']==original['hypotheses']
assert reviewed['statement_sha256']==original['statement_sha256']
reviewed['review_records'].append({'reviewer':'A085','timestamp':NOW,'verdict':'ACCEPT_AT_FULL_STATED_SCOPE_NO_REPAIR',
 'method':'Direct character/physical-edge reconstruction; complete conditional-law prime-log identities; all-even-d proof plus certified first false zero',
 'proof_source':str(RUN/'PROOF.md'),'validation_source':str(RUN/'out/audit.json'),
 'reviewer_contributed_repair':False,
 'scope':'Original complete-normalizer family lemma and remainder-only allocation; no arbitrary-row terminal payment. A085 sharper refinement is a separate author claim.'})
reviewed['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A098_AND_A085_LOCAL_ADOPTION_PENDING'

statement=('For the actual A073 bent-core/one-vertex two-bit gate Boolean family F_d, every even d>=2, '
 'delta=2^-d and e=delta/2, retaining only the partner occupancy in either queried pair row gives '
 'D_full=D_binary+D0/2 and weighted loss L_i=eD0/2. Uniformly (24/169)delta<D0<(15/16)delta. '
 'The two losses together satisfy 0<L_u+L_v<(15/32)delta^2<(3/64)Inf_(y1), '
 'where Inf_(y1)=(1+delta)/2; this dedicated fraction pays only these two losses, once. '
 'The frozen naive binary64 formula first returns zero at even d=104 in the ordered range 2..1080 '
 'although an exact rational enclosure is positive, and directly squared gate atom masses first underflow at d=538. '
 'These numerical failures do not refute A073@1. Its retained M_i/e grows with d and no universal terminal-core or FEI payment follows.')
hypotheses=['Actual specified Boolean family and physical coordinates; uniform cube; bits and ordinary influence',
 'Even d>=2; complete derivative and reference laws, no derivative-support conditioning',
 'Dedicated 3/64 core fraction is only a partial reserve for both quotient losses; no other debit claimed',
 'Numerical minima refer only to frozen Python binary64 formula, fixed even range and recorded platform; analytic bounds cover all even d']
new={'claim_id':'A085-QUADRATIC-CONDITIONAL-REMAINDER-CERTIFICATE','version':1,
 'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 'contributors':['A085'],'proof_source':{'path':str(RUN/'PROOF.md'),'validation':str(RUN/'out/audit.json'),'float_witness':str(RUN/'CERTIFICATE_FAILURE.json')},
 'proof_dependencies':[],
 'review_records':[{'reviewer':'A073','verdict':'PENDING_PRIMARY'},{'reviewer':'A096','verdict':'PENDING'},{'reviewer':'A094','verdict':'PENDING_ALTERNATE'}],
 'status':'NARROW_CERTIFICATE_AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Frozen naive binary64 positive-remainder computation is sign-exact at every even dimension'],
 'first_unproved_line':None,'next_consumers':['A073','A096','A001','A099','B17','B20']}
for claim in [reviewed,new]:assert set(claim)==set(schema['claim_fields'])
dump(RUN/'CLAIMS.json',[reviewed,new])
dump(RUN/'out/review_verdict.json',{'original_source':str(src073/'CLAIMS.json'),'original_statement_sha256':original['statement_sha256'],
 'verdict':'HOLDS_FULL_STATED_SCOPE_NO_REPAIR','new_refinement_review':'PENDING',
 'independent_source_acceptance_consumed':'A098','implementation_failure':'CERTIFICATE_FAILURE.json','full_FEI':'OPEN'})

progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B17','packet_id':'A085',
 'gap_id':'C018-COMPLETE-CONDITIONAL-REFUND','attempt_id':'A085-stage4-quadratic-remainder-and-float-adversary',
 'method':'Direct characters, physical edges, exact conditional likelihoods, rational intervals and all-dimensional Jensen/atanh envelope',
 'mathematical_delta':'Original positive-erasure lemma independently holds; d104 false zero certified; O(delta^2) pair remainder fits dedicated 3/64 core fraction instead of 1/10',
 'deliverable_status':'COMPLETE_LOCAL_SAVE','mathematical_status':'SCOPED_CERTIFICATE_PROVED; NEW_REFINEMENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A073-NONZERO-ERASURE-BINARY-REMAINDER@1 (independent source target)',
 'A096-SINGLE-SPECTATOR-REFUND-OWNERSHIP@1 (context; not a new theorem premise)'],
 'claims_created_or_changed':[original['claim_id']+'@1 (review record only)',new['claim_id']+'@1'],
 'source_artifacts':[str(p) for p in paths],'next_consumers':new['next_consumers'],
 'next_action':'Audit one non-product conditional row paying within-cell remainder plus retained terminal bill from actually available child surplus, complete Q and one influence owner; A073/A096 review refinement',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal retained terminal-core KL payment remains open','New refinement review, shared adoption and remote mirrors unverified'],
 'packet_ids':['A085']}
assert set(progress)=={s.split(' (')[0] for s in schema['progress_fields']}
dump(RUN/'PROGRESS.json',progress)
(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())

(AGENT/'STATUS.md').write_text('STATE: A085 stage4 complete: A073 positive-erasure lemma independently HOLDS; d104 false zero certified; quadratic pair remainder fits 3/64 core fraction; 4241 checks PASS; FEI OPEN.\n'
 'NEXT: A073/A096/A094 review quadratic certificate; audit non-product conditional-row remainder plus retained terminal KL paid once from actual child surplus, complete Q and one I owner.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+NOW+' — '+RUN.name+': consumed A073/A096 binary quotient after A098 acceptance; no census replay. Reconstructed full original A073 scope with direct characters and complete conditional laws. Proved (24/169)delta<D0<(15/16)delta and combined loss<(15/32)delta^2<(3/64)Inf_y1, dedicated once; original 1/10 allowance improved. Pilot 1 physical+40 compressed,255 checks,0.011236s; main 4 physical+540 compressed,4241 checks,1.364325s PASS. Naive float first zero d104 certified positive by exact48-term interval; gate mass underflow d538, query influence d1074,delta d1076. Saved all protocol files; refinement review pending, full terminal payment/FEI OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n## '+NOW+' — Quadratic conditional remainder guard\n'
 'A073 F_d, even d>=2: delta=2^-d, sign weights(1+-sqrt(delta))/2. Complete binary quotient retains mu=(1/2,1/2),r=(1-delta/2,delta/2). Conditional gap D0 satisfies (24/169)delta<D0<(15/16)delta by strong Jensen lower bound and exact natural log/atanh identity. Pair loss=delta D0/2<(15/32)delta^2<(3/64)Inf_y1. Dedicated fraction only pays these two remainder losses; it does not pay retained growing M_i/e or terminal entropy. A073@1 independently accepted unchanged; sharper certificate pending separate review. Frozen naive binary64 formula first zero at even d104 while trueD0>0; squared gate mass underflow d538, query influence d1074,delta d1076. Firsts are formula/platform-specific, not universal algorithm minima. Analytic rational envelopes avoid fixed-precision positive-sign and dimension-cutoff assumptions.\n')

report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+field in report for field in schema['report_fields'])
assert report.rsplit('## ',1)[1].startswith('Universal bridge\n')
assert len((AGENT/'STATUS.md').read_text().splitlines())==2
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert reviewed['exact_statement']==original['exact_statement'] and reviewed['hypotheses']==original['hypotheses']
dump(RUN/'out/validation.json',{'status':'PASS','timestamp':NOW,'protocol_fields':'EXACT','source_statement':'UNCHANGED',
 'packet_delta':'BYTE_IDENTICAL','true_false_zero_interval':'STRICTLY_POSITIVE','counts':audit,
 'new_refinement_review':'PENDING','full_FEI':'OPEN'})
files=[p for p in sorted(RUN.rglob('*')) if p.is_file() and p.name!='manifest.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
manifest=[{'path':str(p.relative_to(RUN)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files]
dump(RUN/'out/manifest.json',{'timestamp':NOW,'files':manifest,'maximum_bytes':max(p['bytes'] for p in manifest)})
assert all(sha(RUN/x['path'])==x['sha256'] for x in manifest)
print(json.dumps({'status':'PASS','files':len(manifest)+1,'maximum_bytes':max(p['bytes'] for p in manifest),
                  'D0_d104_lower':str(short_lower),'D0_d104_upper':str(short_upper),'timestamp':NOW}))
