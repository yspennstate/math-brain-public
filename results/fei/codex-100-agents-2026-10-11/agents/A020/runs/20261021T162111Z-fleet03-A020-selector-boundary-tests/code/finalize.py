from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parents[1]
def put(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
check=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
assert check['status']=='PASS' and check['cases']==6
endpoints={
 '9^4<2^13':9**4<2**13,
 '(73/8)^4<2^13':Q(73,8)**4<2**13,
 '(9/8)^4<2':Q(9,8)**4<2,
 '577^5*65^3<2^64':577**5*65**3<2**64,
 '(4609/256)^4<2^17':Q(4609,256)**4<2**17,
 '(513/256)^4<2^5':Q(513,256)**4<2**5,
 'k3 bracket=417/128':2+11*Q(1,8)-Q(15,2)*Q(1,64)==Q(417,128),
 'final remaining bank endpoint':Q(53,16)-Q(417,128)-Q(1,64)==Q(5,128),
 'after positive final deficit':Q(5,128)-Q(1,128)==Q(1,32)}
assert all(endpoints.values());put(R/'out/RATIONAL_ENDPOINTS.json',endpoints)
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
prot=json.loads(protocol.read_text(encoding='utf-8-sig'))
statement=('For every integer k>=3, on F=1 at gate0 and s*[chi_u(1-A)+chi_q A] at gate1, A=1(v=0), '
 's the two-bit point-defect sign of mean1/2, supply Q_h=(P_h+point_{q})/2, Q_s=P_s and '
 'Q_F(e,T)=[Q_h(T_core)P_s(T_mask)+1_(T=empty)]/4. Under q followed by all k private v queries '
 'inherit only frequency marginals of this same Q_F. At every depth t after q, the full expected '
 'signed rate4 reserve is >5/4. The original half-core reserve S=2I(h_q)-CE(P_hq,(P_hq+point_empty)/2)/2 '
 'pays the exact first insertion J, its retained fresh-to-inherited conversion through J, all later marginal '
 'query charges and the positive weighted final terminal deficit, leaving >1/32 bit. '
 'Nevertheless at q=0,v_1=...=v_(k-1)=0 the nonconstant terminal has I=11/8 and '
 'CE=6+k/4-[17log2(18+d)+3log2(2+d)+4log2(2-3d)]/32>4I for k>=8, d=2^-k.')
hyp=['Independent uniform finite physical bits; Boolean signs; base-2 entropy/CE.',
 'The supplied root reference and query order are exactly as specified; no reference reset.',
 'Reserve is an expectation over both physical branches, not local eligibility at each history.',
 'This is the specified point-event family, not an arbitrary Boolean activation.']
digest=hashlib.sha256(json.dumps({'exact_statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={
 'claim_id':'A020-SAME-REFERENCE-ALL-PRIVATE-PREFIX-RESERVE','version':1,
 'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,
 'contributors':['A020; fixed-reference two-query antecedent supplied by A016'],
 'proof_source':['REPORT.md sections complete derivation 1--5','code/check.py','out/CHECK.json','out/RATIONAL_ENDPOINTS.json'],
 'proof_dependencies':[{'source':'A020 stage5 20261014T062539Z','scope':'specified starting family/reference; reconstructed here'}, {'source':'A016 stage6 20261014T075009Z','scope':'frequency marginal code identity and conversion; reconstructed here'}],
 'review_records':[{'reviewer':'A020','kind':'author exact validation','result':f"PASS {check['cases']} families / {check['assertions']} assertions; analytic bounds plus exact endpoint inequalities"}, {'reviewer':'Lean helper','kind':'attempt only','result':'RUNTIME_UNVERIFIED; no certification'}],
 'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Automatic CE<=4I eligibility of all nonconstant descendants under the specified marginal transport'],
 'first_unproved_line':'Universal initial-reference availability and conserved source reserve for arbitrary unequal-spectrum activations remain open.',
 'next_consumers':['A016','A018','A019','A090','A091','A092','A094','B04','B20']}
assert set(claim)==set(prot['required_per_run']['claim_fields']);put(R/'CLAIMS.json',[claim])
sources=[protocol,B/'BOARD.md',B/'claude/B04/STREAM_NOTES.md',A/'LEARNED.md',R/'FROZEN_SPEC.json']
for ident,stamp in [('A020','20261014T062539Z-fleet05-A020-selector-boundary-tests'),('A016','20261014T075009Z-fleet05-A016-addressing-benchmark'),('A018','20261014T051305Z-fleet05-A018-shared-data-collision-law'),('A019','20261014T055119Z-fleet05-A019-orthogonality-extensions')]:
 p=B/'agents'/ident/'runs'/stamp
 sources.extend([p/'REPORT.md',p/'CLAIMS.json'])
root=protocol.parent
sources.extend(root/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex'])
sup=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
sources.extend(sup/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md'])
sources.extend((B/'context').glob('*.txt'))
put(R/'out/SOURCE_RECEIPTS.json',{'as_of':now,'note':'Byte hashes at close, not historical board snapshot pins. Receipt does not certify source claims.','files':[{'path':str(p),'sha256':sha(p)} for p in sources if p.exists()]})
run=R.name
progress={
 'protocol_revision':prot['revision'],'run_id':run,'stream':'B04','packet_id':'A020',
 'gap_id':'G-LOWSEL-COLLISION-SAME-REFERENCE-HISTORY-BANK',
 'attempt_id':'A020-stage6-all-private-prefix-signed-reserve',
 'method':'Consume A016 continuation; exact signed full-reference transport and all-parameter point-event analysis; fixed k3..8 certificates.',
 'mathematical_delta':'All remaining private prefixes paid with SAME Q and original debit; signed reserve>5/4, original half-bank remainder>1/32 after final positive deficit. Nonconstant penultimate local eligibility false for k>=8.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_PROOF_PENDING_REVIEW_FULL_FEI_OPEN',
 'claim_versions_used':['A020 stage5 supplied reference','A016 stage6 marginal continuation; reconstructed scope'],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','CLAIMS.json','FROZEN_SPEC.json','code/check.py','out/CHECK.json','out/RATIONAL_ENDPOINTS.json','out/FIRST_FAILURE.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Replace point event by one unequal-spectrum Boolean activation; preserve SAME reference/source bank and derive a signed marginal-reference potential. A016/A019 review current proof; A090/A091/A094 audit falsifier.',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal arbitrary-core reference/bank premise unpaid. Independent review pending. Lean algebra check runtime unverified; no Lean certification. Supervisor adoption and mirrors not verified.'],
 'packet_ids':['A020']}
fields=[x.split(' (')[0] for x in prot['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
put(R/'PROGRESS.json',progress);put(R/'PACKET_DELTA.json',progress)
status='STATE: A020 stage6 saved: SAME reference all private prefixes paid; signed reserve>5/4, original half-bank leaves>1/32; nonconstant local eligibility false k>=8;6 families/832 exact assertions PASS; FEI OPEN, review pending.\nNEXT: Replace point event by one unequal-spectrum activation with SAME reference/source bank; A016/A019 review all-prefix proof, A090/A091/A094 audit signed terminals; do not require local eligibility.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' — Stage6: consumed A016 completed second-query target, extended SAME Q through every v prefix. Original half-core bank pays exact booked J, conversion, all later code charges and positive final terminal debt, remainder>1/32; signed physical reserve>5/4. First full check failed overstrong nonconstant eligibility; explicit k>=8 penultimate counterfamily derived, signed deficits/credits retained instead. Final6 frozen k3..8 families,832 assertions PASS in13.444s;9 rational endpoint checks PASS. Lean attempt RUNTIME_UNVERIFIED124.4s, no certification. Sources and four protocol files locally saved; independent review/mirrors pending.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('''
## Stage6 same-reference all-prefix bank

- A016 had already completed our second-v-query NEXT; consume that result rather than repeat it. Under frequency marginal transport, every q/v prefix on the rare point-event family has exact signed reserve R_t=R_root-[2(t+1)d-L_t]>5/4. Retain positive terminal deficits and negative terminal credits separately; their difference is this reserve.
- The original private half-bank S pays exact booked first insertion J plus every later marginal code charge, INCLUDING the conversion E<d^2: total J+C_0-C_end=C_root-C_end+E. Remaining S>5/128; final positive weighted constant-leaf excess<1/128 leaves>1/32. A conservative 5/8 ceiling is not an actual expense; retain the exact J.
- Local inherited rate4 eligibility fails already on NONCONSTANT penultimate core h=chi_u off last v0, constant+1 on it. At q0 and k-1 zero v bits it has full I=11/8 and CE=6+k/4-[17log2(18+d)+3log2(2+d)+4log2(2-3d)]/32>4I for all k>=8. Its history weight d makes this compatible with a paid expected signed bank. Do not silently assume every nonconstant terminal is eligible.
- Exact full k3..8 prefix checker passed832 assertions; analytic inequalities prove all k. Lean conservation-algebra attempt timed out RUNTIME_UNVERIFIED; do not claim formal certification. Universal reference construction and conservation for arbitrary unequal-spectrum activations remain open.
''')
report=(R/'REPORT.md').read_text(encoding='utf-8')
for label in prot['required_per_run']['report_fields']:assert ('## '+label) in report
assert report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for p in R.rglob('*'):
 if p.is_file():
  assert p.stat().st_size<20_000_000
  if p.suffix=='.json':json.loads(p.read_text(encoding='utf-8'))
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
put(R/'out/PERSISTENCE_RECEIPTS.json',{'as_of':now,'local_only':True,'schemas':'PASS','statement_sha256':digest,'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json'],'rolling':[{'path':p.name,'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]})
print(json.dumps({'status':'SAVED','cases':check['cases'],'assertions':check['assertions'],'rational_endpoints':len(endpoints),'claim':claim['claim_id'],'full_FEI':'OPEN'}))
