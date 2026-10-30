from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
R=Path(__file__).resolve().parents[1];A=R.parents[1];O=R/'out';H=Path('~')
def write(p,s):
    with p.open('w',encoding='utf-8',newline='\n') as f:f.write(s)
def save(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
main=json.loads((O/'RESULT.json').read_text(encoding='utf-8'))
paired=json.loads((O/'PAIRED_RESULT.json').read_text(encoding='utf-8'))
full=json.loads((O/'FULL_ACCOUNT_RESULT.json').read_text(encoding='utf-8'))
assert all(x['status']=='PASS' for x in [main,paired,full])
count=sum(x['exact_checks'] for x in [main,paired,full]);stamp=datetime.now(timezone.utc).isoformat()
lean_pass='--lean-pass' in sys.argv
lean_scope='Two concrete m58 integer signs only, NOT the uniform separation theorem or full account'
if lean_pass:
    write(O/'LEAN_RESULT.txt',"Command: lean <run>/code/InvoiceSigns.lean\nExit: 0\n'negative_neighbor' does not depend on any axioms\n'positive_neighbor' does not depend on any axioms\nScope: "+lean_scope+'\n')
compiler=H/'.elan/toolchains/leanprover--lean4---v4.35.0'
pin={'reported_version':'4.35.0','reported_commit':'eb6cafb7290e8bd5f2937522d8d804f58f02bafc','source_sha256':sha(R/'code/InvoiceSigns.lean'),
     'scope':lean_scope,'checked':lean_pass,'axioms':[] if lean_pass else 'UNVERIFIED'}
for rel in ['bin/lean.exe','lib/lean/Init.olean']:
    p=compiler/rel
    if p.is_file():pin[rel]={'path':str(p),'sha256':sha(p)}
save(O/'COMPILER.json',pin)
p85=H/'brain_workers/FEI100_20261011/agents/A085/runs/20261027T020848Z-fleet04-A085-certificate-adversary'
p97=H/'brain_workers/FEI100_20261011/agents/A097/runs/20261027T092641Z-fleet04-A097-cross-route-transfer'
sources=[p85/'PROOF.md',p85/'CLAIMS.json',p85/'code/independent.py',p97/'PROOF.md',p97/'CLAIMS.json',
         H/'brain_workers/FEI100_20261011/BOARD.md',H/'brain_workers/FEI100_20261011/claude/B15/STREAM_NOTES.md',
         H/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json',
         A/'runs/20261026T195758Z-fleet04-A073-certified-logarithms/PROOF.md']
pins=[{'path':str(p),'sha256':sha(p)} for p in sources]
reviewed=json.loads((p85/'CLAIMS.json').read_text(encoding='utf-8'))[1]
assert reviewed['claim_id']=='A085-SIGNED-ADMISSION-EXACT-SIGN-BOUNDARY'
assert hashlib.sha256(reviewed['exact_statement'].encode('utf-8')).hexdigest()==reviewed['statement_sha256']
review={'reviewer':'A073','at':stamp,'result':'HOLDS_UNCHANGED_SCOPE','independent_person':True,
        'contributor_conflict':False,'source_statement_sha256':reviewed['statement_sha256'],
        'artifact':'PROOF.md sections1,2,4; code/invoice.py; code/paired.py; out/RESULT.json; out/PAIRED_RESULT.json',
        'independence':'Full Boolean Walsh and direct full-CE reconstruction, integer bisection primary versus separate radical/product implementation; no A085 helper imported',
        'scope':'Exact sign boundary/all-m dyadic opposite signs/minimal dimension; observed first alias only in declared m4..160 sequence',
        'extension_separate':'New quantitative denominator margin is A073 claim, not a repair required for original A085 statement'}
reviewed['review_records'].append(review)
reviewed['status']='INDEPENDENTLY_RECONSTRUCTED_BY_A073_UNCHANGED_SCOPED_STATEMENT'
save(O/'A085_REVIEW.json',review)
consumers=['A085','A097','A094','A050','A011','A074','B15','B20']
statement=('For the actual uniform AND2 truth table (-1,1,1,1), p=(1/4)^4, calibrated references q_b=(1/4,(3/4-b)/2,(3/4-b)/2,b), '
           'and the compatible mass floor1/3, the full signed CE invoice is Delta=(1/4)log2(G), G=432b(3/4-b)^2/25. '
           'For every rational b=k/d in[1/8,1/4], d>0 integer (not necessarily reduced), its nonzero sign is the sign of '
           'N=27k(3d-4k)^2-25d^3=(3k-d)(144k^2-168kd+25d^2), and |Delta|>=1/(300d^2). '
           'At supplied disjoint full-terminal seed weight3/8 and positive actual reach rho the magnitude is>=rho/(800d^2); '
           'zero weights give exact zero. Thus 2m+11 absolute precision bits suffice for each weight3/8 unit-reach adjacent dyadic m>=4 invoice, '
           'while exact integer signs require no logarithm refinement. For any finite list of these invoices with rational nonnegative reaches/weights and '
           'finite rational-log current CE/old bills, the SAME-original payment inequality reduces exactly to an integer-product comparison after clearing positive '
           'denominators; all negative prices, BOTH terminal laws and old U remain. Explicit size holds are UNRESOLVED, never sign verdicts. '
           'A concrete original AND2 capacity B=(5/2)I with I=1, oldU=1/4, retains reserve>1/8 throughout this interval after full admission, '
           'certified by512<625; matched q=p at valid zero-unused B=9/4,U=1/4 rejects the positive admission exactly. '
           'No new arbitrary-core source, necessary policy or universal FEI constant is asserted.')
claim={'claim_id':'A073-RATIONAL-SIGNED-INVOICE-SEPARATION','version':1,'exact_statement':statement,
       'hypotheses':['Uniform actual AND2 seed; normalized references need not themselves be Boolean spectra; bits',
                     'Rational b=k/d in closed[1/8,1/4], d>0; fixed vacuum1/4 and CURRENT profiles; prescribed target floor1/3',
                     'Full terminal weighting uses supplied disjoint decomposition and actual nonnegative reaches; beta3/8 is explicit supplied-interface condition',
                     'Aggregate exact test uses rational-log finite costs; positive bases; all previous bills and BOTH full terminals retained; no source renewal'],
       'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A073'],
       'proof_source':['PROOF.md','code/invoice.py','code/paired.py','code/full_account.py','out/RESULT.json','out/PAIRED_RESULT.json','out/FULL_ACCOUNT_RESULT.json','out/SELECTED_CERTIFICATES.json','out/M58_FIXTURE.json'],
       'proof_dependencies':['A085-SIGNED-ADMISSION-EXACT-SIGN-BOUNDARY@1 (invoice independently reconstructed; original scoped claim accepted unchanged)'],
       'review_records':[{'reviewer':'A073 separate implementation','independent_person':False,'result':'PASS','artifact':'out/PAIRED_RESULT.json'},
                         {'reviewer':'Lean4.35.0 kernel','result':'TWO_CONCRETE_SIGNS_PASS_NO_AXIOMS' if lean_pass else 'UNVERIFIED','artifact':'out/COMPILER.json','scope':lean_scope}],
       'status':'UNIFORM_PROSE_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
       'supersedes':[],'refutes':[],
       'first_unproved_line':'Supply a useful REQUIRED arbitrary-core admission/source and prove its full cost fits ACTUAL unused original capacity after query KL and old bills; FEI OPEN.',
       'next_consumers':consumers}
claims=[reviewed,claim];save(R/'CLAIMS.json',claims)
next_action=('A085/A094 review denominator-separation and complete original CE compiler; A050/A011/A097 supply ONE necessary arbitrary-core '
             'compatible admission and its ACTUAL diminished original margin, including query KL/old U/BOTH full terminals, for exact aggregate payment. '
             'No further optional sign-grid or refresh-count escalation.')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B15','packet_id':'A073',
          'gap_id':'C019-C024-GENUINE-NONEMPTY-PROFILE-TRANSFER','attempt_id':'A073-stage24-rational-invoice-separation',
          'method':'Consume new A085 precision objection; independent unchanged scoped review; exact integer polynomial separation and full ORIGINAL rational-log invoice compiler',
          'mathematical_delta':'A085 boundary independently HOLDS; new uniform |Delta|>=1/(300d^2), weighted3/8 margin>=1/(800d^2), sufficient dyadic2m+11 absolute bits. Exact paired budget signs retain both prices; current CE and old U remain inside original-account compiler. No FEI constant improvement; earlier28/15 counts unchanged.',
          'deliverable_status':'COMPLETE_LOCAL_PERSISTED','mathematical_status':'A085_INDEPENDENT_REVIEW_COMPLETE_NEW_MARGIN_PROOF_REVIEW_PENDING_FULL_FEI_OPEN',
          'claim_versions_used':['A085-SIGNED-ADMISSION-EXACT-SIGN-BOUNDARY@1'],
          'claims_created_or_changed':['A085-SIGNED-ADMISSION-EXACT-SIGN-BOUNDARY@1 (review appended locally)','A073-RATIONAL-SIGNED-INVOICE-SEPARATION@1'],
          'source_artifacts':pins,'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
          'blockers':['No noncircular arbitrary-core original complete source/necessary paid interface; FEI OPEN',
                      'New denominator margin/full-account compiler awaits independent-agent review; supervisor mirror adoption unverified'],
          'packet_ids':['A073']}
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
lean_sentence=('Native Lean4.35.0 checked BOTH concrete m58 integer signs; exit0, no axioms for either statement. '
               'The uniform rational bound and full-account theorem are NOT Lean-checked.' if lean_pass else
               'Native Lean attempt is UNVERIFIED; no formal certification is claimed.')
report=f'''# A073 stage24: certified signed invoices

## exact target, quantifiers, hypotheses and units

Independently review A085-SIGNED-ADMISSION-EXACT-SIGN-BOUNDARY@1, then certify its ACTUAL AND2 compatible admission for every rational b=k/d in[1/8,1/4], d>0. New margin |Delta|>=1/(300d^2), or>=rho/(800d^2) for supplied seed weight3/8 and positive actual reach rho. Exact aggregate original-budget comparisons retain CURRENT full CE, all old U and BOTH terminal laws; no bank is renewed. Bits throughout. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Updated BOARD B15/B10/B17/B20 entries and stream lead v2 read with own STATUS/LEARNED; full execution protocol2026-10-11-execution-v2 reread. A08520261027T020848Z PROOF/REPORT, exact claim and independent checker read; A09720261027T092641Z PROOF read in full and claim entries consulted. A085 statement hash remains {reviewed['statement_sha256']}. Earlier campaign/paper baseline readings are preserved from prior stages and are not newly used as proof inputs. A097's high-moment/query-KL warning motivates retaining CURRENT full costs; its complete all-policy theorem is NOT newly accepted here. Source pins in PROGRESS. Current user stage authorization is27Oct12:15UTC; no schedules/settings changed.

## complete derivation or exact first unsupported line

PROOF.md independently reconstructs the full Boolean price and original A085 boundary unchanged. The integer factorization of N and parity of v2 in(12k-7d)^2=24d^2 give |G-1|>=1/(100d^2). The fixed integral bounds(g-1)/g<=ln(g)<=g-1 and2/3<ln2<25/36 give the stated rational separation and sign-safe interval without precision refinement. Dyadic m>=4 therefore has sufficient absolute precision2m+11 bits at weight3/8; no fixed ceiling as m grows is asserted. Exact common-denominator products retain all opposite signs before comparing to the diminished ORIGINAL owner. A concrete ACTUAL AND2 full account B=(5/2)I, oldU1/4, keeps reserve>1/8, with integer margin113 in512<625; a valid matched zero-unused owner rejects its positive floor conversion. First unsupported universal line: REQUIRED arbitrary-core compatible class/source with enough unused original influence capacity after query KL/old bills. Earlier conditional28/tensor15 counts and their different reserves are UNCHANGED.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede each job. `python -X utf8 <run>/code/invoice.py`:478 rational references,159 fixed dyadic brackets(m4..160,512,1024),5736 individual budget comparisons;9734 checks PASS. `python -X utf8 <run>/code/paired.py`: separate radical/direct full-likelihood representation;477 paired-budget comparisons,1914 checks PASS. `python -X utf8 <run>/code/full_account.py`:168 predeclared full-reference controls plus valid zero-unused counterguard,675 checks PASS. TOTAL={count}. All exact runs took under2seconds each internally; bit estimates stay below50000; resource holds are explicitly UNRESOLVED. m58 signs oppose despite identical binary64 inputs: weight3/8 lower invoice is<-2^-61 and upper is>2^-62, with complete rational bounds in M58_FIXTURE.json. Those sharper fixture bounds differ from the weaker universal denominator guarantee because they use ACTUAL integer numerators. {lean_sentence} Source/compiler/core import hashes and exact scope in out/COMPILER.json. No Mathlib or >300MB job; no GPU, dimension escalation, detached work, or precision refinement.

## proof dependencies and changed downstream conclusions

A085's original statement is independently accepted unchanged with a source-bound review appended ONLY in this run. The new quantitative bound/compiler is a separate A073 contribution awaiting review, not a repair to the accepted claim. The AND2 actual spectrum is verified H=2,I=1; beta3/8 weighting is a SUPPLIED disjoint-interface condition, not an invented Boolean realization. Signed invoices may cancel; the individual denominator gap is not used as a lower bound on their sum. Full current CE can remain an irrational rational-log form inside the exact comparator; it is not replaced by a rounded remaining margin. Finite cases validate the implementation; the written factorization/integral argument proves the uniform rational statement. Gain in universal FEI constant:0.

## one next mathematical action and independent reviewer

{next_action} The handoff is saved for those agents; no messages were sent. A085/A094 are the independent reviewers for the new margin and complete-owner compilation; no independent acceptance of that new result is claimed.

## actual persistence receipts or precise save blocker

Four required protocol files, complete proof, frozen specs, native-core fixtures and portable exact code/outputs are saved in the assigned run. out/MANIFEST.json pins artifacts; this persistence script checks protocol field sets, original statement hash, equality of PROGRESS/PACKET_DELTA, two-line STATUS and20MB caps. WORKLOG/LEARNED append dated durable facts. Shared sources and all other-agent folders stayed read-only; no git/mail/brain writes, service/governor changes or process shedding. One first command was rejected by an encoding acknowledgment gate, then rerun with the already-present explicit UTF8 reads; no mathematical run was blocked or misreported. Compute-state and interventions were read; current snapshot reported7.3GB physical/14.4GB commit available and10.8GB disk, so only tiny jobs were used. Existing shared work stayed running. Brain self-care is DEGRADED/UNVERIFIED: stale owner-model, state-of-mind and dream notes were disclosed and not used as evidence. Supervisor/GitHub mirror adoption remains unverified.

Universal bridge: C024 history transfer gains a checked exact sign oracle and a uniform denominator-dependent invoice separation, replacing A085's unresolved numerical-sign handoff; C019 receives a complete SAME-owner aggregate comparison retaining CURRENT CE, old U and BOTH terminal laws, with actual AND2 reserve>1/8 as a control. The gain in a universal FEI constant is0. Required arbitrary-core source/profile necessity and influence payment remain open. NEXT asks for ONE necessary arbitrary-core invoice with its actual depleted original owner and uses this exact oracle to settle that payment, instead of repeating optional finite resets or another refresh-count class result.
'''
write(R/'REPORT.md',report)
write(A/'STATUS.md',f'STATE: A073 stage24 saved: A085 exact sign-boundary independently HOLDS; rational invoice gap>=1/(300d^2), weighted>=1/(800d^2);{count} exact checks PASS;full original account retains oldU;FEI OPEN.\nNEXT: A085/A094 review margin/full-CE comparator; A050/A011/A097 supply ONE REQUIRED arbitrary-core admission and ACTUAL depleted original owner, queryKL/oldU/BOTH terminals retained; no optional sign-grid escalation.\n')
with (A/'WORKLOG.md').open('ab') as f:f.write((f'\n{stamp} stage24: Consumed new A085 m58 alias and A097 query-KL warning; independently accepted A085 boundary unchanged. Proved rational gap1/(300d^2), weight3/8 gap1/(800d^2), sufficient dyadic2m+11 absolute bits; no log refinement. Exact individual5736/paired477/full-source168 controls, {count} assertions PASS. Native core m58 signs '+('PASS/no axioms' if lean_pass else 'UNVERIFIED')+'. Actual oldU-retaining AND2 reserve>1/8 certified by512<625. No universal source/FEI progress or change to28/15 counts. Saved required protocol/rolling files; review new bound pending.\n').encode())
with (A/'LEARNED.md').open('ab') as f:f.write(('\n2026-10-27 stage24: For actual AND2 current q_b=(1/4,(3/4-b)/2,(3/4-b)/2,b), floor1/3, Delta=(1/4)log2[432b(3/4-b)^2/25]. For ANY rational b=k/d in[1/8,1/4], N=(3k-d)(144k^2-168kd+25d^2) nonzero, since a zero quadratic gives impossible odd v2 in(12k-7d)^2=24d^2. Hence |G-1|>=1/(100d^2), |Delta|>=1/(300d^2), weighted3/8 margin>=1/(800d^2). Fixed2/3<ln2<25/36 integral bounds settle signs without refinement. Sufficient dyadic absolute precision2m+11 bits is representation-dependent, not a fixed ceiling. Opposite invoice sums can cancel: combine exact rational-log terms including CURRENT CE/oldU against ORIGINAL capacity before a verdict; size holds meanUNRESOLVED. Full actual AND2 B=(5/2)I, U1/4 retains>1/8 by512<625. Matched B9/4,U1/4 has zero unused and cannot pay positive floor edit. A085 boundary independently HOLDS; no arbitrary-core source price/FEI solution; prior28/15 counts unchanged.\n').encode())
protocol=json.loads((H/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert all(set(c)==set(protocol['claim_fields']) for c in claims)
assert all('## '+h in report for h in protocol['report_fields'])
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
save(O/'CHECKPOINT.json',{'state':'COMPLETE_LOCAL','packet_id':'A073','stage':R.name,'exact_checks':count,'A085_review':'HOLDS_UNCHANGED','new_margin':'1/(300d^2); supplied weight3/8:1/(800d^2)','universal_status':'FEI OPEN','next':next_action})
artifacts=[p for p in R.rglob('*') if p.is_file() and p.name!='MANIFEST.json']
assert all(p.stat().st_size<20*1024*1024 for p in artifacts)
save(O/'MANIFEST.json',{'created_utc':stamp,'run_id':R.name,'schema_checks':'PASS','exact_checks':count,
     'artifacts':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in artifacts],
     'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],
     'remote_adoption':'UNVERIFIED'})
print(json.dumps({'status':'SAVED_SCHEMAS_CHECKED','exact_checks':count,'artifacts':len(artifacts),'A085_statement_unchanged':True,'native_Lean_concrete_signs':lean_pass}))
