import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
TEAM=AGENT.parents[1]
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT))
from EXACT_WALSH_INTERFACE import BASE
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def expr(d):return ' + '.join(f'({c}) log2({p})' for p,c in d.items()) or '0'
engine=load(ROOT/'ENGINE_CERTIFICATE.json');assert engine['failures']==0
w=[load(ROOT/f'out/witness_n{n}.json') for n in (5,6)]
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=load(protocol_path)
statement=('For the uniform sign functions encoded by negative-bit masks 4194372 on five variables '
 'and 1103806792023 on six variables, the exact integer Walsh/sign-inverse/physical-edge and '
 'child checks pass. Each coordinate has an exact rational prime-log erasure B_i, '
 'Jensen-Shannon term JS_i and entropy decrement Delta_iH, with Delta_iH=B_i+JS_i. '
 'The saved prime-log E(f)=min_i B_i/Inf_i has the saved minimizing coordinates and '
 'is greater than 539/200 and 368/125 respectively; both exceed Kstar='
 '4+(5/2)log2(5)-(9/2)log2(3). The six-bit E is strictly greater than the five-bit E.')
hyp=['Little-endian uniform assignments x=0..2^n-1',
     'Negative-bit mask m means f(x)=1-2*((m>>x)&1)',
     'B_i=H(S_i|S_-i); JS_i=H((mu_0+mu_1)/2)-(H(mu_0)+H(mu_1))/2',
     'All logarithms base two; integer/Fraction arithmetic; exact integer-product sign comparisons']
claim={'claim_id':'A072-UNIFORM-ERASURE-WITNESSES','version':1,'exact_statement':statement,
       'hypotheses':hyp,'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
       'contributors':['A072 reconstruction','Claude B15 witness discovery'],
       'proof_source':['REPORT.md','EXACT_WALSH_INTERFACE.py','code/verify.py','out/witness_n5.json','out/witness_n6.json','out/comparison.json'],
       'proof_dependencies':[],'review_records':[],
       'status':'EXACT_FINITE_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
       'first_unproved_line':None,'next_consumers':['A073','A074','A075','A085','A092','B15','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields']);dump(ROOT/'CLAIMS.json',[claim])
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B15','packet_id':'A072',
 'gap_id':'G-R-SELECT','attempt_id':'A072-ERASURE-2',
 'method':'Extend checked Walsh engine with rational prime-log B/JS/decrement forms; exact integer products certify minima and strict inequalities',
 'mathematical_delta':'Independent exact reconstruction of f5/f6 erasure witnesses, all 11 per-coordinate identities and exact minimizing coordinates; f6 E exceeds f5 E and both exceed the four-bit leaf constant.',
 'deliverable_status':'COMPLETE_LOCAL_SAVED_REVIEW_PENDING','mathematical_status':'FINITE_WITNESSES_CERTIFIED_UNIVERSAL_SELECTION_AND_FEI_OPEN',
 'claim_versions_used':[],'claims_created_or_changed':['A072-UNIFORM-ERASURE-WITNESSES@1'],
 'source_artifacts':['EXACT_WALSH_INTERFACE.py','ENGINE_CERTIFICATE.json','FROZEN_SPEC.json','out/witness_n5.json','out/witness_n6.json','out/comparison.json','out/source_receipts.json'],
 'next_consumers':['A073','A074','A075','A085','A092','B15','B20'],
 'next_action':'A075 derive the parameterized sparse Hamming-ball-plus-matching spectrum, then A072 certify a fixed bounded list of family parameters and physical restrictions using this interface; no larger exhaustive census.',
 'stagnant_substantive_attempts':0,'blockers':['Universal dimension-independent selection or erasure payment remains unproved.'], 'packet_ids':['A072']}
assert set(progress)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
dump(ROOT/'PROGRESS.json',progress);dump(ROOT/'PACKET_DELTA.json',progress)
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
proof=[]
for r in w:
    proof.append(f"n={r['n']}, mask={r['negative_bit_mask']}, negative assignments={r['negative_assignments']}; minimizing coordinates={r['minimum_coordinates']}.\n\n    E(f) = {expr(r['minimum_prime_log'])}\n")
report=f'''## exact target, quantifiers, hypotheses and units

Stage 2 follows the explicit A072 direction in B15 STREAM_NOTES v2 (2026-10-11 23:25 UTC): add B_i, JS_i and Delta_iH to the uniform engine and reconstruct masks 4194372 (n=5), 1103806792023 (n=6). Define E(f)=min over relevant physical coordinates of B_i/Inf_i. Spectral law mu(s)=W_s^2/N^2, N=2^n; characters are (-1)^popcount(x&s), tables use little-endian x. A negative mask bit means f(x)=-1. Entropy uses bits. No symmetry reduction or search: exactly two named witnesses, all 11 coordinates and 22 physical children. Pilot: all 16 two-bit truth tables, 32 coordinate cases.

## sources actually read, revisions and theorem locators

BOARD.md was read at stage start, supervisor snapshot 2026-10-12 00:39 UTC. B15 STREAM_NOTES.md v2 was read in full, including its exact witness masks, selection/composition scope, retired targets and one target per agent. Own STATUS.md was read: prior baseline complete, no need to repeat the B09 grid. The earlier protocol was retained, revision {protocol['revision']}; exact field sets are rechecked against its current local bytes. A072's prior EXACT_WALSH_INTERFACE.py and certificate/report are the reused algebraic interface. B15 lead original CLAIMS.json was read; its REPORT.md is absent. The present reconstruction uses only the original truth masks and definitions, not lead-computed spectra. Source hashes and exact consultation scopes are in out/source_receipts.json. No entropy theorem, external fact or unpublished class result is needed for this finite certificate. A073/A074 already handle selected bias-grid log/reproduction work; that work is not repeated.

## complete derivation or exact first unsupported line

First run the prior uniform certificate on every parent and physical child: integer WHT; WHT(W)=Nf; sum W_s^2=N^2; direct character sums agree; physical undirected edge counts give Inf_i=2e_i/N=sum_(s containing i)mu(s). These checks precede entropy expressions. The exact masks reconstruct the actual Boolean functions, rather than assuming a proposed spectral law is Boolean.

For a packet indexed by s not containing i let a=mu(s), b=mu(s union i), q=a+b. Define phi(a,b)=q log2 q-a log2 a-b log2 b, with zero terms omitted. Then B_i=sum_s phi(a,b)=H(S_i|S_-i). Physical children are independently made from the truth table by setting x_i=0 or 1; their spectra are certified as above. Their signed Walsh coefficients satisfy 2W_child,0=u+v and 2W_child,1=u-v for parent packet values u,v. Consequently (mu_0+mu_1)/2=q exactly, also checked by Fractions. Define JS_i=H(q)-(H(mu_0)+H(mu_1))/2 and Delta_iH=H(mu)-(H(mu_0)+H(mu_1))/2. Since H(mu)=H(q)+B_i, Delta_iH=B_i+JS_i, verified by exact prime-log coefficient equality for all 11 witness coordinates (and all 32 pilot coordinates). The average physical-child influence vector equals the parent's retained-coordinate influence vector exactly. This is the conserved physical ledger, not an entropy-payment bound.

For every positive rational t, factor numerator and denominator and record log2 t=sum_p valuation_p(t) log2 p. Every entropy and erasure expression is therefore a finite rational coefficient map. The zero term t log t is omitted. Exact equality of maps certifies equality of the expressions. Nonzero prime-log forms cannot cancel: clearing denominators gives a product of prime powers; unique factorization detects exact zero. To compare two maps, clear rational denominators D and compare A=product_(e_p>0)p^e_p with B=product_(e_p<0)p^(-e_p). The sign of the original form is the sign of A-B because the logarithm is strictly increasing and D>0. All products are Python arbitrary-precision integers. The checker uses the integer bound sum_p |e_p| bit_length(p) before construction and refuses above the frozen 8000000-bit budget. It stores the exponents, denominator and product bit sizes; recomputation requires no numerical logarithm.

Exact minima and their prime-exponent forms:

{chr(10).join(proof)}

The saved minimum_comparisons compare every relevant coordinate's ratio to the selected minimum; every sign is nonnegative and exactly zero identifies the listed minimizing coordinates. The strict-cutoff products certify E(f5)>539/200 and E(f6)>368/125. Separate integer products show both E values exceed Kstar=4+(5/2)log2 5-(9/2)log2 3, and E(f6)>E(f5). Thus these are genuine counterexamples to using Kstar as a universal physical-coordinate selection constant; they do not contradict the proved four-bit leaf theorem. The JSON records include each coordinate's exact influence, B_i, JS_i, Delta_iH, ratio, physical children, and child entropies.

The first unsupported line is any extrapolation that this finite rise continues without bound in a Boolean family, or that it refutes all finite selection constants. Neither is claimed. No independent 30-digit interval reconstruction is claimed; that remains A073's directed task.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before computation. Commands from A072:

    python -X utf8 runs/{ROOT.name}/code/verify.py --pilot
    python -X utf8 runs/{ROOT.name}/code/verify.py
    python -X utf8 runs/{ROOT.name}/code/finalize.py

Pilot: 16 functions, 32 coordinate checks, zero failures; {load(ROOT/'out/pilot.json')['runtime_seconds']} seconds. Witness verification: 2 functions, 11 coordinates, 22 children, 2 exact minima and 11 exact entropy-decrement identities; zero failures; {engine['runtime_seconds']} seconds. One serial job, runtime cap 55 seconds, estimated memory below 100 MB (not measured), explicit integer-product bit budget, no GPU or dimension escalation. Exact witness outputs were saved immediately as each witness completed; out/comparison.json and ENGINE_CERTIFICATE.json follow. Mathematical arithmetic is integer/Fraction only; runtime uses perf_counter. No floating entropy comparison is used.

## proof dependencies and changed downstream conclusions

No unreviewed entropy/helper theorem is a premise. The baseline FWHT/sign/edge algorithm is reused from the prior source-complete A072 interface, whose hash is pinned; its elementary Walsh orthogonality proof remains in that prior report. The truth masks are sourced to Claude B15, but all spectra, physical children, edge counts, entropy expressions and exact comparisons are independently reconstructed here. One bundled finite claim A072-UNIFORM-ERASURE-WITNESSES@1 is created, review pending. This corroborates the lead's B15-LKSTAR-FAILS-N5-N6 algebraic claim; it is not acceptance of a full census or a universal theorem. Full FEI remains OPEN. No shared registry is modified; there is no new refutation propagation beyond the already reported finite failure of Kstar universality.

## one next mathematical action and independent reviewer

Next: consume A075's parameterized sparse Hamming-ball-plus-matching formula, then certify a frozen bounded list of parameters and physical restrictions with this interface. That tests whether the rise survives heredity and identifies the exact unpaid erasure term; it avoids another exhaustive census. Reviewers A085/A092 should reconstruct the exponent products and min-coordinate comparisons. A073 can use the exact maps for its 30-digit intervals; A074 can compare its third-path conditional-entropy reconstruction without importing our spectrum as independent input.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json with packet_ids=[A072], EXACT_WALSH_INTERFACE.py, ENGINE_CERTIFICATE.json, FROZEN_SPEC.json, code and out records are locally saved in the requested stage directory. The finalizer validates protocol field sets, delta equality and file sizes below 20 MB, and writes out/manifest.json with SHA256 receipts. Rolling STATUS.md is current; WORKLOG.md and LEARNED.md receive dated stage facts without discarding previous entries. Supervisor copying, independent review, adoption and mirror verification remain pending and are not inferred from local saving. All writes remain inside A072.

**Universal bridge:** This stage moves C018's erasure-selection diagnostics by independently certifying E(f5)>539/200, E(f6)>368/125 and E(f6)>E(f5), while making B_i, JS_i and the actual physical decrement auditable together. It changes no universal constant and supplies no unbounded-ratio family: the first unpaid obligation is a dimension-independent erasure/influence payment or a proved Boolean family violating every finite bound. A075's parameterized sparse matching family, checked through actual restrictions and retained child costs, is the shortest next route because it tests that dimension bridge directly rather than repeating a completed baseline or closing another isolated finite class.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:assert '\n## '+field+'\n' in '\n'+report
sources=[(protocol_path,'Protocol fields and inherited execution rules'),(TEAM/'BOARD.md','Full stage-start board returned; supervisor 00:39 UTC snapshot'),
 (TEAM/'claude/B15/STREAM_NOTES.md','Full v2 directions and witness definitions'),(BASE,'Reused checked Walsh/sign/edge engine'),
 (BASE.parent/'REPORT.md','Prior normalization and orthogonality derivation'),
 (TEAM/'claude/B15/runs/20261011T225100Z-claude-B15-erasure-countersearch/CLAIMS.json','Lead discovery context; independent mask reconstruction uses no source spectra')]
dump(ROOT/'out/source_receipts.json',[{'path':str(p),'scope':scope,'sha256':sha(p),'bytes':p.stat().st_size} for p,scope in sources if p.exists()])
(AGENT/'STATUS.md').write_text('STATE: A072 stage 2 complete: exact B/JS/decrement engine and f5/f6 minimum erasure ratios certified by integer products; review pending; full FEI OPEN.\nNEXT: A085/A092 review; A073/A074 consume exact prime-log records; A075 supply parameterized sparse matching family for fixed-domain hereditary checks.\n',encoding='utf-8')
stamp='2026-10-12 00:40 UTC stage'
for name,text in [('WORKLOG.md',f'{stamp}: Followed new B15 v2 target. Added exact prime-log B_i, JS_i, Delta_iH wrappers to reused Walsh/sign/edge engine. Pilot 16/32 cases passed; f5/f6 all 11 coordinates and 22 physical children passed. Exact integer products certify min coordinates, E5>539/200, E6>368/125, both>Kstar, E6>E5. Saved all witness records and protocol files; no universal inference.\n'),
 ('LEARNED.md',f'{stamp}: Erasure phi(a,b)=(a+b)log2(a+b)-a log2 a-b log2 b can be stored as rational prime-log coefficients. Physical-child JS and full entropy decrement obey exact coefficient identity Delta=B+JS. For lead masks 4194372 and 1103806792023, independent certificates yield the minimizing ratios saved in stage 2; a finite rise above the n<=4 leaf constant does not imply unbounded growth. Next test the parameterized sparse family and its actual restrictions.\n')]:
    if text not in (AGENT/name).read_text(encoding='utf-8'):
        with (AGENT/name).open('a',encoding='utf-8') as f:f.write('\n'+text)
manifest=[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name!='manifest.json']
assert all(r['bytes']<20000000 for r in manifest)
dump(ROOT/'out/manifest.json',{'saved_at_utc':datetime.now(timezone.utc).isoformat(),'files':manifest,'protocol_fields_checked':True,'independent_review':'PENDING','mirror_verification':'PENDING_SUPERVISOR'})
print(json.dumps({'saved':True,'files':len(manifest),'protocol_fields_checked':True,'minima':[r['minimum_coordinates'] for r in w]}))
