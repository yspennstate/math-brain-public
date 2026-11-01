from pathlib import Path
from hashlib import sha256
import json
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def read(p):return p.read_text(encoding='utf-8')
def write(p,s):p.write_text(s,encoding='utf-8')
def js(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def sha(p):return sha256(p.read_bytes()).hexdigest()
tr=json.loads(read(R/'out/TRANSFER.json')); assert tr['status']=='PASS' and tr['reference_cases']==84
checks=sum(json.loads(read(R/'out'/f))['assertions'] for f in ['CHECK.json','INTERSECTING.json','TRANSFER.json'])
claims=json.loads(read(R/'CLAIMS.json')); prior=claims[-1]
cid='A006-PAID-CORE-LIFT-CONDITIONAL-ALL-INNER-CODE-TRANSFER'
statement=('For every nonconstant Boolean indicator V on a physical cube, every disjoint core Z of size k>=1, and EVERY supplied fixed positive normalized nonempty reference q for h=2V-1, set b=EV,t=2^-k and G=2[OR(Z) OR V]-1. A fair once-only branch chooses a uniform nonempty core subset, or runs q once and appends an independent uniform subset of Z including empty. The resulting normalized actual-run reference R has EXACT complete nonempty cost C_R(G)=4t(1-t)(1-b)^2[1+log2(2^k-1)]+t(k+1)Var(h)+t C_q(h), with I(G)=2tk(1-b)+t I(h). Therefore for EVERY K>=0, C_q(h)<=K I(h) implies C_R(G)<=max(4,K) I(G), retaining the full underlying actual-run posterior. In particular the explicit normalized reference compiled from the two paid star references by their independent three-sector code and this k=1 core lift repairs the genuinely intersecting-core family in the preceding A006 claim at complete nonempty cost<11I(G). Universal existence of a paid inner q and arbitrary nonfactorable physical overlaps are not proved.')
hyp=['Uniform physical cube, bits, and true physical flip influence; core Z disjoint from all inner coordinates.',
 'q is supplied and fixed before the Fourier output; its cost, normalization and actual-run posterior are paid, not assumed free.',
 'Actual branch, core-subset and underlying q draws are real events; no aliases or shuffled descriptions counted as different runs.',
 'The intersecting-core repair uses the preceding explicit A006 component references and independent component composition, followed by the genuinely shared x-coordinate lift; it does not apply that independent identity across physical overlap.']
c={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),
 'contributors':['A006'],'proof_source':['CORE_TRANSFER.md','code/transfer.py','TRANSFER_SPEC.json','out/TRANSFER.json'],
 'proof_dependencies':[{'claim_id':prior['claim_id'],'version':prior['version'],'statement_sha256':prior['statement_sha256'],'scope':'Explicit intersecting-family repair only; the generic all-inner-function conditional cost identity is self-contained.'}],
 'review_records':[{'reviewer':'A006','kind':'AUTHOR_ALL_INNER_FUNCTION_PROOF_AND_EXHAUSTIVE_TWO_BIT_CERTIFICATES','acceptance':'INDEPENDENT_AGENT_REVIEW_PENDING','formal_status':'NOT_FORMALLY_CHECKED'}],
 'status':'AUTHOR_PROOF_EXACT_CERTIFICATES; INDEPENDENT_AGENT_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A008','A015','A009','A010','A007','Claude/B02','B20']}
assert not any(x['claim_id']==cid for x in claims),'do not rerun completed extension'
claims.append(c);js(R/'CLAIMS.json',claims)
p=json.loads(read(R/'PROGRESS.json'))
p['mathematical_delta']+=' Conditional all-inner-function paid core lift has an EXACT cost identity and preserves max(4,K) whenever supplied q costs<=K I. It compiles an explicit <11I repair of the genuinely intersecting-core counterfamily; only individual-core-plus-intersection augmentation is refuted. The remaining universal line is paid representation for nonfactorable overlapping cores.'
p['claims_created_or_changed'].append({'claim_id':cid,'version':1})
p['source_artifacts']+=['CORE_TRANSFER.md','TRANSFER_SPEC.json','code/transfer.py','out/TRANSFER.json']
p['next_action']='A008/A015 review both new source-complete claims; then produce an influence-paid joint-core representation for NONFACTORABLE interacting cores, where neither common-core lifting nor independent-component sectors apply. Keep one physical influence account and every selector/allocation charge.'
js(R/'PROGRESS.json',p);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=read(R/'REPORT.md')
para='CORE_TRANSFER.md supplies an additional EXACT conditional code identity for EVERY Boolean inner indicator V and supplied paid positive reference q: with b=EV,t=2^-k, C_R(G)=4t(1-t)(1-b)^2[1+log2(2^k-1)]+t(k+1)Var(h)+t C_q(h), and I(G)=2tk(1-b)+t I(h). A once-only core/lift branch therefore preserves max(4,K) when C_q(h)<=K I(h). This is a conditional code compiler, not a proof that a universally paid q exists or a novelty claim for read-once FEI. Applied after the explicit two-component sectors, it gives a genuinely normalized <11I repair of THIS intersecting-core counterfamily, charging every branch and core subset. The first unsupported universal line is now paid joint-core representation for NONFACTORABLE overlaps, rather than this particular shared-core example.\n\n'
report=report.replace('## executed validation with domain, arithmetic, commands and outputs',para+'## executed validation with domain, arithmetic, commands and outputs')
validation=f'Separately frozen TRANSFER_SPEC.json and command python -X utf8 code/transfer.py PASS: all14 nonconstant two-bit truth tables, core sizes1,2,3, two fixed unequal/uniform references:84 reference cases on42 physical functions, {tr["assertions"]} exact assertions, {tr["truth_inputs_with_reference_repetition"]} direct-character truth inputs counted with reference repetition, {tr["seconds"]:.6f}s. Direct physical influence, full reference normalization, EVERY spectral coefficient, the exact cost identity and <=4I for these supplied references all pass; no source executable or previous stage helper imported. The bound is proved conditionally for arbitrary inner h in CORE_TRANSFER.md; finite cases do not prove universal q existence. All nonpilot certificates now total{checks} assertions, excluding the overlapping pilot.\n\n'
report=report.replace('## proof dependencies and changed downstream conclusions',validation+'## proof dependencies and changed downstream conclusions')
report=report.replace('## one next mathematical action and independent reviewer','The second new claim is conditional all-inner code transfer. Its generic identity is self-contained; only its explicit intersecting-family repair depends on the first new A006 claim at the pinned version/hash, with an acyclic edge. Both new claims await independent review.\n\n## one next mathematical action and independent reviewer')
report=report.replace('## actual persistence receipts or precise save blocker',p['next_action']+'\n\n## actual persistence receipts or precise save blocker')
report=report.rsplit('## Universal bridge',1)[0]+'''## Universal bridge

C020 whole-set witness cost moves by two whole source reviews, a paid arbitrary-width shared-core dictionary (<=17I/2), and an all-prior obstruction to individual-core-plus-intersection dictionaries on genuinely intersecting physical cores. Crucially an EXACT conditional all-inner-function core-lift identity preserves max(4,K), compiling an explicit <11I paid hierarchical repair of this very counterfamily from the independently separated component references. Every branch, core subset and actual anchor/allocation posterior remains charged. What remains is an influence-paid fixed JOINT representation for NONFACTORABLE overlaps, where neither common-core extraction nor independent sectors are available; universal paid inner-reference existence is not assumed. NEXT is the shortest route to full FEI because it both excludes the failed individual-core interface and pays its exhibited replacement, isolating the first genuinely unpaid general representation step rather than claiming a known composition class proves FEI. Both new claims await independent-agent review; full FEI remains OPEN.
'''
write(R/'REPORT.md',report)
write(R/'CHECKPOINT.md',f'Stage11 COMPLETE_LOCAL: shared-core dictionary<=17I/2, all-prior individual-core/intersection obstruction on genuine overlap, EXACT conditional core-lift preserves max(4,K), and explicit<11I repair of that counterfamily. Two source proofs HOLD; {checks} nonpilot assertions PASS. Both new claims await review; FEI OPEN. NEXT: paid JOINT representation on nonfactorable overlaps.\n')
write(A/'STATUS.md',f'STATE: Stage11 saved: shared-core<=17I/2; individual-core/intersection dictionaries fail on genuine overlap; EXACT core-lift compiler repairs witness<11I;{checks} exact checks PASS;two source reviews HOLD;new reviews pending;FEI OPEN.\nNEXT: A008/A015 review both claims; pay JOINT representation/selector on NONFACTORABLE physical overlaps, beyond common-core lifts and independent sectors, from ONE influence account.\n')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n2026-10-23 stage11 continuation: exact generic core-lift cost identity for ANY Boolean inner h and supplied q; conditional payment max(4,K)I. Applied to paid two-star sectors, it explicitly repairs the genuine intersecting-core obstruction at<11I without free resets. Exhaustive14 nonconstant two-bit truths x3core sizes x2fixed references gives84cases/{tr["assertions"]} assertions PASS in{tr["seconds"]:.6f}s; combined nonpilot{checks}. Original local claim bytes/statement hash preserved; second source-complete conditional claim added with acyclic repair dependency. Both await independent review. No job left running; fullFEIopen.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-23 stage11 continuation durable: A paid common-core LIFT, unlike merely adding individual dictionary atoms, works for EVERY inner Boolean indicator V with a supplied paid q. For G=OR_k(Z) OR V, t=2^-k,b=EV, exact C=4t(1-t)(1-b)^2[1+log(2^k-1)]+t(k+1)Var(h)+tC_q(h), I=2tk(1-b)+tI(h). Core and lift output classes are disjoint, so q posterior is preserved without fake multiplicity. The first two debits combined<=4I_core; hence K-paid q yields max(4,K)-paid lift, independent of k. This explicitly repairs G=x OR[(z OR U_X)AND(y OR U_Y)] at<11I via paid independent sectors then x-lift, even though ANY individual-core/intersection branch mixture with ONE flat global clause law diverges. Remaining universal target: influence-paid joint representation of NONFACTORABLE overlaps, not this now-paid shared-core counterfamily. New theorem awaits independent review; no fullFEIclaim.\n')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
assert set(p)=={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert all('## '+s in report for s in protocol['required_per_run']['report_fields'])
assert len(read(A/'STATUS.md').splitlines())==2
files=[]
for f in sorted(R.rglob('*')):
    if f.is_file() and f.name!='PERSISTENCE.json':
        assert f.stat().st_size<20*1024*1024
        if f.suffix in ['.md','.json','.py']:read(f)
        files.append({'path':str(f.relative_to(R)),'bytes':f.stat().st_size,'sha256':sha(f)})
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
js(R/'out/PERSISTENCE.json',{'status':'PASS_FINAL_EXTENSION_READBACK','schemas':'PASS','compatibility_copy':'IDENTICAL','source_reviews':2,'new_claims':2,'new_reviews':'PENDING','nonpilot_assertions':checks,'full_FEI':'OPEN','remote':'UNVERIFIED','files':files,'rolling':[{'path':str(f),'sha256':sha(f)} for f in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]})
assert all(sha(R/f['path'])==f['sha256'] for f in files)
print(json.dumps({'status':'SAVED_FINAL_EXTENSION_READBACK_PASS','files':len(files),'source_reviews':2,'new_claims':2,'nonpilot_assertions':checks,'full_FEI':'OPEN'}))
