from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1];O=R/'out'
def write(p,s):
    with p.open('w',encoding='utf-8',newline='\n') as f:f.write(s)
def js(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
result=json.loads((O/'RESULT.json').read_text(encoding='utf-8'))
rep=json.loads((O/'REPRODUCTION.json').read_text(encoding='utf-8'))
assert result['status']==rep['status']=='PASS'
prior=A/'runs/20261023T124010Z-fleet03-A073-certified-logarithms'
root=Path('~')
sources=[prior/'PROOF.md',prior/'CLAIMS.json',prior/'code/check.py',
         root/'brain_workers/FEI100_20261011/BOARD.md',
         root/'brain_workers/FEI100_20261011/claude/B15/STREAM_NOTES.md',
         root/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json',
         root/'brain_workers/FEI100_20261011/context/threshold_paper_38pp.txt',
         root/'brain_workers/FEI100_20261011/context/percolation_spectral_pivotal_entropy_30pp.txt']
pins=[{'path':str(p),'sha256':sha(p)} for p in sources]
compiler={'version':'4.35.0','commit':'eb6cafb7290e8bd5f2937522d8d804f58f02bafc',
          'platform':'x86_64-w64-windows-gnu Release','source_sha256':sha(R/'code/LogSigns.lean'),
          'axioms':[],'checked_scope':'four integer comparison theorems, not the full account theorem'}
for tc in (root/'.elan/toolchains').iterdir():
    p=tc/'bin/lean.exe'
    if p.is_file():
        compiler.setdefault('installed_compilers',[]).append({'path':str(p),'sha256':sha(p)})
js(O/'COMPILER.json',compiler)
consumers=['A050','A049','A085','A094','A096','A097','B15','B20']
next_action=('A050/A094 independently reconstruct full signed original-account substitution, all sign trees and ghost rows; '
             'then supply a necessary arbitrary-core compatible source/continuation priced from actual diminished ORIGINAL capacity. '
             'The scalar 29/16 lower-envelope guards alone cannot certify or refute further histories.')
statement=('Retain every hypothesis and complete signed account of A073-EIGHT-WHOLE-CORE-POSITIVE-REFRESHES@1: '
           'uniform Boolean h; supplied q(0)=p_h(0), normalized dominating q with CE<=4I; specified correlated lift; b then selected a; '
           'both signs/all complements, fresh adaptive data queries, x unqueried, full whole-essential-core alpha=1/7 activation refreshes '
           'in at most N physical antichain generations; actual restricted-core H<=4I; all old debits/complete terminal KLs and omega<=1/4 retained. '
           'For N<=28 the SAME original remaining reserve is >=11/400, dimension independently. The earlier N<=8 reserve>=3/4 remains valid. '
           'For every finite disjoint product of <=3-bit Boolean factors, the explicit NEW initial whole-core1/8 reference and hereditary '
           'S4(h)>=(25/8)(1-|Eh|) close both interface hypotheses and pay N<=15 with SAME original reserve>=3/4. '
           'Exact all256 factor certificates, 7^112<2^25*6^112, 7^300<2^67*6^300, and 8^5<2*7^5 certify the claims. '
           'The full transport interface remains dependent on v1 and independent review is pending; arbitrary initial suppliers and full FEI remain OPEN.')
claim={'claim_id':'A073-EIGHT-WHOLE-CORE-POSITIVE-REFRESHES','version':2,'exact_statement':statement,
       'hypotheses':['Complete v1 supplied-reference lift/physical-history/full-signed-ledger hypotheses, repeated in PROOF.md section1',
                     'General all-dimensional theorem conditional on initial CE<=4I and hereditary terminal core H<=4I',
                     'Unconditional application only for finite disjoint products of <=3bit Boolean factors using the NEW initial whole-core1/8 supplier',
                     'alpha=1/7, x unqueried, finite policies, both a signs and every complementary terminal retained; omega<=1/4; bits'],
       'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A073'],
       'proof_source':['PROOF.md','code/certify.py','code/reproduce.py','code/LogSigns.lean','out/RESULT.json','out/REPRODUCTION.json','out/INTEGER_SIGNS.json','out/FACTOR_CERTIFICATES.json','out/LEAN_CHECK.txt','out/COMPILER.json'],
       'proof_dependencies':['A073-EIGHT-WHOLE-CORE-POSITIVE-REFRESHES@1 (unreviewed full signed transport interface and lift identities; reconstructed local variance/account algebra)',
                             'A050-CORRELATION-PRESERVING-SIGNED-LIFT@1 (via v1; no new blanket acceptance)'],
       'review_records':[{'reviewer':'A073','kind':'second implementation, not independent-agent review','verdict':'PASS','artifact':'out/REPRODUCTION.json'},
                         {'reviewer':'Lean4.35.0 kernel','kind':'four Nat inequalities only','verdict':'PASS_NO_AXIOMS','artifact':'out/LEAN_CHECK.txt'}],
       'status':'CONDITIONAL_PROOF_EXACT_FINITE_CERTIFICATES_PARTIAL_LEAN_CHECK_REVIEW_PENDING',
       'supersedes':['A073-EIGHT-WHOLE-CORE-POSITIVE-REFRESHES@1'],'refutes':[],
       'first_unproved_line':'Produce noncircular influence-priced complete initial references and hereditary stopping eligibility for arbitrary Boolean cores; no universal source price or full FEI theorem.',
       'next_consumers':consumers}
js(R/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B15','packet_id':'A073',
          'gap_id':'C019-C024-GENUINE-NONEMPTY-PROFILE-TRANSFER','attempt_id':'A073-stage23-original-account-envelope',
          'method':'Exact integer logarithm products; complete factor census; original supplied-slack/variance antichain account; independent butterfly reproduction',
          'mathematical_delta':'Conditional count8->28 with reserve11/400 (uses original constant margin); SAME tensor family count8->15 retains reserve3/4 using new exact S4>=(25/8)(1-|mean|) and supplier slack. Scalar29/16 insufficiency guards are NOT failing histories.',
          'deliverable_status':'COMPLETE_LOCAL_PERSISTED','mathematical_status':'CONDITIONAL_PROOF_FINITE_CERTIFICATES_PARTIAL_LEAN_CHECK_FULL_FEI_OPEN_REVIEW_PENDING',
          'claim_versions_used':['A073-EIGHT-WHOLE-CORE-POSITIVE-REFRESHES@1','A050-CORRELATION-PRESERVING-SIGNED-LIFT@1 (inherited interface)'],
          'claims_created_or_changed':['A073-EIGHT-WHOLE-CORE-POSITIVE-REFRESHES@2'],'source_artifacts':pins,
          'next_consumers':consumers,'next_action':next_action,'stagnant_substantive_attempts':0,
          'blockers':['Universal original source price and hereditary stopping certificates remain open',
                      'Independent-agent review of v1/v2 and remote mirror adoption unverified',
                      'Stale compute telemetry/low-disk hook: no large jobs, services or governor changes undertaken'],
          'packet_ids':['A073']}
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
report='''# A073 stage23: exact original-account envelopes

## exact target, quantifiers, hypotheses and units

For the full supplied-reference lift/history interface of v1, in every finite dimension, pay up to 28 whole-core alpha1/7 refresh generations from the SAME original account, retaining every prior signed debit, both a sign trees, reference-only rows, complete terminal KL and old omega<=1/4. Reserve>=11/400. The general theorem requires supplied CE<=4I and hereditary terminal H<=4I. For finite products of disjoint <=3bit factors, a strengthened exact factor certificate and the NEW initial whole-core1/8 supplier pay up to15 generations with reserve>=3/4. Bits throughout. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Protocol2026-10-11-execution-v2 read in full; current B15 lead v2, BOARD B15/B10/B20 entries and own stage22 STATUS/LEARNED/WORKLOG. Stage22 PROOF.md sections1-7, CLAIMS.json and checker read in full. Current report README/CURRENT_STATUS, relevant registry/packet/action entries and campaign-plan opening; supplementary CAMPAIGN, seed-lemma opening, C019/C024 claim and counterexample entries, mapping and LOG_ALLOCATION sections2-3 consulted. Threshold38pp Proposition7.1 and abstract, percolation30pp opening/definitions and earlier-version abstracts consulted; neither paper is a proof dependency for the new account inequality. Source hashes are in PROGRESS.json. One prescribed read-only two-wording math recall found no applicable source/refresh supplier; no recalled theorem is used. The latest user-authorized continuation is26Oct; no schedules or deadline settings were changed.

## complete derivation or exact first unsupported line

PROOF.md reconstructs the original variance1/4 factor and the exact min(S,M0-sigma)-omega account. With l<25/112, N<=28 gives3/4+2t-(25/4)t(1-t)=(25/4)(t-17/50)^2+11/400. The larger generic count spends original constant slack, so its reserve11/400 is deliberately smaller than the prior3/4. For the SAME tensor family, all256 factors satisfy S4>=(25/8)(1-|mean|); supplier slack plus l<67/300 and l0<1/5 pays N<=15 while retaining3/4. This includes any positive ninth increment but does not construct nine strictly positive increments. The first unsupported universal line remains the arbitrary-core initial supplier and hereditary terminal entropy eligibility. The scalar29/16 guards concern lower-bound insufficiency ONLY.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede the exact runs. `python -X utf8 <run>/code/certify.py`: ALL256 masks, no symmetry, integer products/Fractions;2574 checks PASS. `python -X utf8 <run>/code/reproduce.py`: separate butterfly/raw-denominator representation;1546 checks PASS. Runtimes and byte-pinned helper versions are saved in out/. Four logarithm signs passed `lean <run>/code/LogSigns.lean`; exit0 and each #print axioms reports none. Lean4.35.0 commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc; installed compiler/source hashes in out/COMPILER.json. These are ONLY the four integer inequalities; the full theorem is a conditional prose proof with exact finite certificates, not a Lean-checked FEI proof. The exponent300 warning did not prevent checking. An initial attempt passed the mathematical sign but failed decimal serialization at4300 digits; preserved FIRST_ATTEMPT.json, switched output to exact hex, and reran without mathematical or precision changes. No logarithm precision refinement occurred. Small/boundary rational cases and scalar counterguards passed.

## proof dependencies and changed downstream conclusions

This is version2 of the existing account claim, preserving the earlier eight-generation reserve and replacing its narrower count handoff. It depends on the v1 supplied lift/coherent likelihood interface; no independent-agent acceptance of that entire interface is newly claimed. The finite factor bound is newly certified twice. General count28 and tensor count15 consume ACTUAL original allowance, including initial supplier loss; no reset bank is renewed. The existing arbitrary-core source obstruction remains. No finite certificate is promoted to universal FEI.

## one next mathematical action and independent reviewer

A050/A094 independently reconstruct the28/15 substitution in the FULL signed original interface, especially both a sign trees and reference normalization; A085 checks the integer-product and factor certificates. Then price a necessary arbitrary-core compatible source/continuation from ACTUAL remaining original capacity. Repeating the coarse29/16 envelopes cannot pay the universal source. No messages were sent; this is a saved source-bound handoff.

## actual persistence receipts or precise save blocker

All four required protocol files, complete proof, code and outputs are local in this assigned run; out/MANIFEST.json pins bytes and code/persist.py checks field sets against the actual protocol. STATUS.md has exactly two lines; WORKLOG.md and LEARNED.md are appended. No git, mail, external publication, brain write, other-agent mutation, service/governor mutation, GPU job, detached process or >300MB job was launched. All owned validation commands ended. Supervisor/GitHub adoption remains unverified. Wake warned of stale owner-model/state/dream notes, surfaced to the owner; those notes are not evidence. Compute_state timestamp and interventions were read; telemetry is stale and was not treated as live headroom. The last snapshot's large holders were Claude/ffmpeg/Python groups; they were left running under the no-shedding order.

Universal bridge: C019 stopping-tree payment and C024 history transfer advance from8 to28 conditional whole-core refresh generations with reserve11/400, and from8 to15 on the SAME unbounded tensor family while preserving3/4. All prior debits, both sign trees and full terminal laws remain. The universal arbitrary-core source and terminal eligibility are still unpaid. NEXT attacks that exact missing original payment after independent reconstruction of this stronger account; it avoids another isolated family search or a renamed FEI-equivalent assumption.
'''
write(R/'REPORT.md',report)
stamp=datetime.now(timezone.utc).isoformat()
write(A/'STATUS.md','STATE: A073 stage23 saved: SAME original account pays28 conditional refresh generations (reserve11/400), tensor family15 (reserve3/4);2574+1546 checks PASS;4 integer signs Lean no axioms;FEI OPEN.\nNEXT: A050/A094/A085 review full signed28/15 account and exact factors; pay arbitrary-core ORIGINAL source/necessary compatible continuation with all old debits/both terminals; scalar29/16 guards are only envelope insufficiency.\n')
with (A/'WORKLOG.md').open('ab') as f:f.write(('\n'+stamp+' stage23: Retained original constant and supplier slack; conditional refresh8->28 (11/400 reserve), SAME tensor family8->15 (3/4 reserve). New all256 factor S4>=(25/8)(1-|mean|),2574 exact primary+1546 separate butterfly checks PASS. Four integer signs Lean4.35 no axioms; full account conditional/unreviewed. Initial decimal-serialization failure preserved/fixed with hex; no precision refinement. Scalar29/16 guard is NOT actual history failure. All required files saved; universal source/FEI OPEN.\n').encode('utf-8'))
with (A/'LEARNED.md').open('ab') as f:f.write(('\n2026-10-26 stage23: In supplied original lift, M0>=1+2t, sigma_N<=N*t(1-t)*log2(7/6), S>=1. ForN<=28, SAME reserve afteromega<=1/4 >=11/400 by7^112<2^25*6^112 and completing square at17/50. Larger count intentionally spends old constant margin; earlier3/4 is not asserted for28. Exact all256 three-bit census provesS4>=(25/8)(1-|mean|), tensor-hereditary. NEW whole-core1/8 initial supplier loss<=Var*log2(8/7), with8^5<2*7^5; its genuine surplus paysN<=15 atSAME3/4 reserve, using7^300<2^67*6^300. Four integer signs Lean-checked/noaxioms; full account still conditional and independent review pending.29/16 negative scalar lower envelopes show only these estimates are insufficient, never a failing Boolean history. No arbitrary-core source price/FEI solution.\n').encode('utf-8'))
protocol=json.loads((root/'mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
required=protocol['required_per_run']
pf=[x.split(' (')[0] for x in required['progress_fields']]
assert set(progress)==set(pf)
assert set(claim)==set(required['claim_fields'])
assert all(('## '+x) in report for x in required['report_fields'])
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
paths=[p for p in R.rglob('*') if p.is_file() and p.name!='MANIFEST.json']
assert all(p.stat().st_size<20*1024*1024 for p in paths)
manifest={'created_utc':stamp,'run_id':R.name,'status':'ALL_LOCAL_REQUIRED_FILES_SAVED_SCHEMAS_CHECKED',
          'artifacts':[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in paths],
          'rolling_files':[{'path':str(p),'sha256':sha(p)} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']],
          'remote_adoption':'UNVERIFIED'}
js(O/'MANIFEST.json',manifest)
print(json.dumps({'status':'SAVED_SCHEMA_CHECKED','artifacts':len(paths),'primary_checks':result['checks'],'reproduction_checks':rep['checks']}))
