from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,sys
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
BASE=Path('~/brain_workers/FEI100_20261011')
PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
S89=BASE/'agents/A089/runs/20261014T030932Z-account05-A089-repair-specialist'
def digest(data):return hashlib.sha256(data).hexdigest()
def save(path,obj): (ROOT/path).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
proto=read(PROTOCOL);v=read(ROOT/'out/VALIDATION.json');cert=read(ROOT/'out/COMPACT_PAYMENT_CERTIFICATE.json');fixture=read(ROOT/'out/EXISTING_HIGH_E_CORE_ONEFLIP_PAYMENT.json')
assert v['checks']==25460 and fixture['checks']==598
assert v['runtime_seconds']<60 and fixture['runtime_seconds']<60
assert len(cert['boxes'])==256
for offset,(start,end) in zip([0,128],[(Q(1,16),Q(7,32)),(Q(1,2),Q(25,32))]):
    box=cert['boxes'][offset:offset+128]
    assert Q(box[0]['input_bias_box'][0])==start and Q(box[-1]['input_bias_box'][1])==end
    for i,row in enumerate(box):
        a,b=map(Q,row['input_bias_box']);assert a<b
        if i:assert a==Q(box[i-1]['input_bias_box'][1])
        dl=Q(row['D_interval'][0]);assert dl>0
        assert max(Q(row['C_upper']),Q(row['minus_C_upper']))<=64*dl
assert Q(fixture['all_admissible_mixed_descendants_H_over_I_upper']['upper'])<12
assert Q(fixture['payment_margin_positive_debit']['lower'])>0
assert Q(fixture['payment_margin_negative_debit']['lower'])>0
assert 64*Q(11,16)==44

sourcepaths=[PROTOCOL,BASE/'BOARD.md',BASE/'claude/B15/STREAM_NOTES.md',S89/'REPORT.md',S89/'CLAIMS.json',BASE/'agents/A072/runs/20261014T020611Z-account05-A072-exact-walsh-engine/PROOF.md',BASE/'agents/A072/runs/20261014T020611Z-account05-A072-exact-walsh-engine/CLAIMS.json',BASE/'agents/A084/runs/20261014T030826Z-account05-A084-continuum-parameters/PROOF.md',BASE/'agents/A080/runs/20261014T005622Z-account05-A080-universal-counterexample-standard/REPORT.md',ROOT.parent/'20261014T005346Z-account05-A075-search-to-theorem-bridge/PROOF.md',ROOT.parent/'20261014T005346Z-account05-A075-search-to-theorem-bridge/code/arithmetic.py']
receipts=[]
for p in sourcepaths:
    assert p.is_file(),str(p)
    receipts.append({'path':str(p),'sha256':digest(p.read_bytes()),'bytes':p.stat().st_size,'role':'source-bound review' if S89 in p.parents else 'read-only protocol/context/own-helper provenance'})
save('out/SOURCE_RECEIPTS.json',{'mutable_board':'Hash binds finalization bytes; initial03:35 supervisor snapshot and later middle-section rereads were consulted, not mathematical premises.','sources':receipts})

review=read(S89/'CLAIMS.json')[0]
assert review['claim_id']=='A089-PAID-MODERATE-PREFIX-AND-COMPLETE-TERMINAL-LEDGER' and review['version']==1
canonical=json.dumps({'statement':review['exact_statement'],'hypotheses':review['hypotheses']},sort_keys=True,separators=(',',':')).encode()
stmt_only=review['exact_statement'].encode()
assert review['statement_sha256'] in [digest(canonical),digest(stmt_only)]
review['review_records'].append({'reviewer':'A075','decision':'ACCEPT_AT_STATED_SCOPE','independence':'Independent actual gate Walsh/pivotal polynomials, raw-coefficient entropy envelopes, reciprocal-influence constants and one-segment/two-complement counting reconstructed in PROOF Section7; own arithmetic/implementation; no substantive repair','proof':str(ROOT/'PROOF.md'),'certificates':['out/GATE_POLYNOMIALS.json','out/RATIONAL_PROFILES.json','out/PHYSICAL_FIXTURES.json','out/VALIDATION.json'],'source_statement_hash_preserved':True})
review['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_A075_LOCAL_RECORD'
consumers=['A071','A072','A074','A080','A084','A089','A092','B15','B20']
statement='For every nonconstant actual Boolean sign g0 on an arbitrary finite uniform cube, and every finite admissible word of six-disjoint-identical-copy substitutions, let g_s be the actual cores, reoriented to minority-negative outputs. Allowed steps are h on the minority orientation when minority<=7/32 or its complement otherwise, and J_j=-h(x xor(1<<j)) for any one flipped block j when minority<=1/16; h is negative exactly on {0,1,2,4,8,16,32,6,17,40}. With entropy in bits and Psi(g)=h2(p_min(g))/I(g), Psi is nonincreasing and 0<Psi<=1, and sum_(s<d) |H(g_(s+1))/I(g_(s+1))-H(g_s)/I(g_s)|<=64(Psi(g0)-Psi(g_d))<=64. If the starting core is rare, p_min<=1/16, this budget is<=44. Every level retains H_next=Q H+C and I_next=Q I, with Q the total actual outer pivotal probability and C=H_p(outer)-Q h2(4p(1-p)); the full arbitrary starting entropy is retained. The existing A080 actual core g0=h,g1=h(g0^6),g2=h((-g1)^6),g3=h(g2^6) has H/I<12 at every finite admissible mixed descendant, as certified by H(g3)/I(g3)+64Psi(g3)<12. This is a bounded composition ledger and fixed-seed mechanism closure, not an absolute bound on unknown starting cores, a nonnegative erasure reserve theorem, or physical restriction-tree payment.'
hypotheses=['Actual finite arbitrary-dimensional Boolean core on independent uniform physical bits, nonconstant','Specified two-gate library and allowed chosen bias domains; six identical cores on disjoint supports at each finite level','Every finite admissible word, including arbitrarily repeated escapes and returns; no uniform length required','All input/output sign changes preserve complete squared spectrum and physical influence; one-flip positions equivalent by matching automorphisms','Entropy units bits; ordinary binary output entropy h2(p_min) is distinct from spectral entropy H']
new={'claim_id':'A075-MIXED-EXCURSION-OUTPUT-ENTROPY-BUDGET','version':1,'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':digest(statement.encode()),'contributors':['A075'],'proof_source':{'path':str(ROOT/'PROOF.md'),'report':str(ROOT/'REPORT.md'),'certificates':['out/COMPACT_PAYMENT_CERTIFICATE.json','out/GATE_POLYNOMIALS.json','out/EXISTING_HIGH_E_CORE_ONEFLIP_PAYMENT.json'],'validation':['out/VALIDATION.json','out/RATIONAL_PROFILES.json','out/PHYSICAL_FIXTURES.json']},'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROVED_ALL_DIMENSION_ALL_ADMISSIBLE_WORDS_REVIEW_PENDING_FULL_FEI_OPEN','supersedes':[],'refutes':['Unbounded H/I from a fixed finite seed through arbitrarily repeated named one-flip/common-sign excursions'],'first_unproved_line':None,'next_consumers':consumers}
claims=[review,new]
assert all(set(claim)==set(proto['required_per_run']['claim_fields']) for claim in claims)
save('CLAIMS.json',claims)
progress={'protocol_revision':proto['revision'],'run_id':ROOT.name,'stream':'B15','packet_id':'A075','gap_id':'G-R-SELECT','attempt_id':'A075-MIXED-EXCURSION-BUDGET-4','method':'Output entropy tensorization deficit; signed full spectral correction; analytic rare endpoints and exact compact Bernstein/log certificates; arbitrary-word decreasing-potential ownership','mathematical_delta':'All-dimensional arbitrary legal return/escape words have total absolute H/I correction<=64, <=44 from rare starts; entire starting entropy retained. Existing1296-bit high-E rare seed has every mixed descendant H/I<12. A089 complete fixed-policy bill independently accepted. Full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'REPEATED_EXCURSION_ENTROPY_MECHANISM_PAID_AND_FIXED_SEED_GROWTH_CLOSED; REVIEW_PENDING; ARBITRARY_RETAINED_RARE_CORE_BOUND_OPEN; FULL_FEI_OPEN','claim_versions_used':['A089-PAID-MODERATE-PREFIX-AND-COMPLETE-TERMINAL-LEDGER@1 independently accepted at unchanged scope; not premise of new theorem','A072-ONEFLIP-RARE-ESCAPE-PRICE@1 motivation/interface; probabilities and full identity reconstructed','A084 stage4 common-policy budget context only','A075-RARE-CORE-LOCALIZATION@1 context/interface only; no acceptance of own pending theorem','A080 actual g3 high-E source context; exact circuit/bias/influence/entropy independently reconstructed, no new E certification'],'claims_created_or_changed':['A075-MIXED-EXCURSION-OUTPUT-ENTROPY-BUDGET@1','A089-PAID-MODERATE-PREFIX-AND-COMPLETE-TERMINAL-LEDGER@1 local independent acceptance record'],'source_artifacts':['REPORT.md','PROOF.md','DERIVATION.md','CLAIMS.json','out/FROZEN_SPEC.json','out/EXISTING_FIXTURE_SPEC.json','out/GATE_POLYNOMIALS.json','out/COMPACT_PAYMENT_CERTIFICATE.json','out/RATIONAL_PROFILES.json','out/PHYSICAL_FIXTURES.json','out/EXISTING_HIGH_E_CORE_ONEFLIP_PAYMENT.json','out/VALIDATION.json','out/SOURCE_RECEIPTS.json','out/MANIFEST.json','code/arithmetic.py','code/check_potential.py','code/check_fixture.py','code/finalize.py'],'next_consumers':consumers,'next_action':'Find an actual signed spectral-row constraint beyond singleton caps that pays arbitrary retained rare-core H from I-h2(p_min), whose rare capacity is>=5I/16; challenge on A080 actual high-E core and non-flat children. A074/A092 independently reconstruct tensorization gap and all-word ownership.','stagnant_substantive_attempts':0,'blockers':['Arbitrary retained starting rare-core E/H bound remains unproved; full FEI OPEN','The proved decreasing composition potential is not a physical restriction-tree influence ledger','Other gates/sign patterns/shared-data operations lie outside the frozen theorem','Independent review, shared adoption, supervisor copy and remote mirror verification pending'],'packet_ids':['A075']}
fields=set(proto['required_per_run']['progress_fields']);fields.remove('packet_ids (one primary ID, for compatibility)');fields.add('packet_ids');assert set(progress)==fields
save('PROGRESS.json',progress);(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
for field in proto['required_per_run']['report_fields']:assert '## '+field in report
assert report.strip().split('\n')[-1].startswith('**Universal bridge:**')
(AGENT/'STATUS.md').write_text('STATE: A075 stage4 complete: arbitrary legal one-flip/common-sign words have owned absolute H/I budget<=64 (rare start<=44); existing high-E rare seed mixed orbit H/I<12; A089 full bill independently accepted; new review pending; FEI OPEN.\nNEXT: Pay arbitrary retained rare-core H from an actual signed-row constraint on I-h2(p_min), beyond singleton caps; A074/A092 review output-entropy gap, compact certificates and all-word ownership.\n',encoding='utf-8')
tag='2026-10-14 stage4 20261014T034311Z'
work='\n'+tag+': read updated board and new A072/A084/A089 dependencies; did not redo fixed-policy payment. Independently accepted A089@1. Changed mechanism to Psi=h2(output minority)/I: exact deficit D=Qh2(p)-h2(p_next) pays full signed C by |C|<=64D. Analytic rare endpoints plus256 compact real boxes imply all legal mixed words have total absolute H/I correction<=64, rare start<=44. Main25460 assertions in'+str(v['runtime_seconds'])+'s; actual1296-bit rare core +7776-bit one-flip598 assertions in'+str(fixture['runtime_seconds'])+'s; retained core bill0.0064388 paid, all future mixed descendants H/I<12. Full FEI initial rare-core bill remains open.\n'
learn='\n'+tag+' durable: Ordinary OUTPUT entropy potential Psi=h2(p_min)/I differs from squared-spectrum H/I. Indicator-plus-complement entropy tensorization gives h2(output)<=Qh2(input) for every Boolean outer gate, so Psi drops by D/(QI); also Psi<=1 (rare Psi<=11/16). Complete spectral identity R_next-R=C/(QI), C=H_p(gate)-Qh2(4p(1-p)). Named h common policy and J rare escape satisfy |C|<=64D in all real allowed biases: h rare D>(105/4)p^2, |C|<=360p^2; J rare D>(3/4)p, positive price<40/negative<48; compact h price<20 by256 Bernstein/log boxes. Every finite legal word thus has absolute correction<=64(Psi_start-Psi_end), rare<=44; no new excursion budget is created. Existing A080 g3 has all such descendants H/I<12. This closes a fixed-seed growth mechanism, NOT arbitrary starting-core FEI or physical restriction-tree payment. A089 complete fixed-policy entropy ledger independently accepted at unchanged scope.\n'
for name,text in [('WORKLOG.md',work),('LEARNED.md',learn)]:
    p=AGENT/name
    if tag not in p.read_text(encoding='utf-8'):
        with p.open('a',encoding='utf-8') as f:f.write(text)
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.name=='MANIFEST.json' or '__pycache__' in p.parts:continue
    assert p.stat().st_size<20*1024*1024,str(p)
    files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())})
save('out/MANIFEST.json',{'local_only':True,'files':files,'regeneration_commands':['python -X utf8 code/check_potential.py','python -X utf8 code/check_fixture.py','python -X utf8 code/finalize.py'],'protocol_schema':'PASS','packet_delta_byte_identical':True,'claim_hashes_checked':True,'total_final_assertions':v['checks']+fixture['checks'],'all_word_constant':64,'rare_word_constant':44,'existing_seed_all_word_H_over_I_upper':12,'full_fei':'OPEN','independent_review_new_theorem':'PENDING','supervisor_copy':'PENDING','remote_mirror':'UNVERIFIED'})
print(json.dumps({'saved_run':ROOT.name,'claims':len(claims),'total_assertions':v['checks']+fixture['checks'],'compact_boxes':len(cert['boxes']),'full_fei':'OPEN'}))
