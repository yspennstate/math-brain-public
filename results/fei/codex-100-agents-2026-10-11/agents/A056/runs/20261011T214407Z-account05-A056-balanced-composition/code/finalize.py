from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

run=Path(__file__).resolve().parents[1]
agent=run.parents[1]
stamp=datetime.now(timezone.utc).isoformat()
def dump(p,z): p.write_text(json.dumps(z,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
report=run/'REPORT.md'
t=report.read_text(encoding='utf-8')
if 'For comparison with Proposition 7.1, define strong entropy' in t:
    start=t.index('For comparison with Proposition 7.1, define strong entropy')
    end=t.index('The convention that actually composes is Eplus(g)')
    t=t[:start]+'For comparison with Proposition 7.1, the strong-entropy convention must be distinguished from conditional nonempty entropy. '+t[end:]
    t=t.replace('(7)','(6)').replace('(8)','(7)')
    report.write_text(t,encoding='utf-8')

r=Path(r'~\mop_fei100\reports\fei-2026-10-11')
s=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
c=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[r/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
paths += list((r/'runs').rglob('REPORT.md'))
paths += [s/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((s/'sources').glob('*.md'))+list(c.glob('*.txt'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
manifest=[]; excerpts=[]
for p in paths:
    data=p.read_bytes()
    try: text=data.decode('utf-8'); encoding='utf-8'
    except UnicodeDecodeError: text=data.decode('cp1252',errors='replace'); encoding='cp1252; undefined bytes replaced if any'
    manifest.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'encoding':encoding})
    lines=text.splitlines()
    selected=set()
    for i,line in enumerate(lines):
        if any(word in line.lower() for word in ['balanced','composition','substitution','strong entropy','normaliz','b12','a056']):
            selected.update(range(max(0,i-2),min(len(lines),i+7)))
    if not selected: selected.update(range(min(20,len(lines))))
    excerpt='\n'.join(f'{i+1}: {lines[i]}' for i in sorted(selected))
    excerpts.append('\nFILE '+str(p)+'\n'+excerpt)
dump(run/'out'/'source_manifest.json',manifest)
(run/'out'/'source_excerpts.txt').write_text('\n'.join(excerpts),encoding='utf-8')

consumers=['A013','A018','A024','A043','A053','A057','A059','A060','A091','A090','B20']
statements=[
('A056-DISJOINT-COMPOSITION', 'For every Boolean outer gate h and Boolean children g_i on mutually disjoint uniform physical blocks, after absorbing constant children, with m_i=E g_i, v_i=1-m_i^2>0, a_mu the output-product orthonormal Fourier coefficients and w_i=sum_{T containing i} a_mu(T)^2, E F=E_mu h, Var F=Var_mu h, H(F)=H_mu(h)+sum_i (w_i/v_i)(H(g_i)-h2(v_i)), and Inf_x(F)=(w_i/v_i)Inf_x(g_i) for x in block i. Balanced children specialize to H(F)=H(h)+sum_i Inf_i(h)H(g_i) and I(F)=sum_i Inf_i(h)I(g_i).'),
('A056-PHYSICAL-RESTRICTION-SCOPE', 'At every fixed physical restriction, disjoint composition identities hold with newly restricted children, absorbed constants, and the outer gate reexpanded under the new child-output product law. Balance before restriction does not imply balance afterwards. For AND_2 composed with majority_3(x,a,b) and dictator z, fixing x=+1 gives E F=-1/4, I(F)=5/4, H(F)=4-(9/8)log2(3), whereas retaining the initial balanced outer law predicts -1/2, 1, and 3 respectively.')]
claims=[]
for cid,statement in statements:
    claims.append({'claim_id':cid,'version':1,'exact_statement':statement,
        'hypotheses':['Boolean signs','independent uniform physical input coordinates','mutually disjoint child blocks','entropy in bits including empty coefficient','constant children absorbed before divisions'],
        'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['account05/A056'],
        'proof_source':{'path':str(report),'theorem_locators':'Equations (1)-(5), physical restriction section, exact witness; BALANCED_SUBSTITUTION_BASELINE.tex'},
        'proof_dependencies':[],'review_records':[], 'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',
        'supersedes':[],'refutes':([] if cid.endswith('COMPOSITION') else ['Reusing balanced gate coefficients and mean after arbitrary physical child restrictions']),
        'first_unproved_line':None,'next_consumers':consumers})
dump(run/'CLAIMS.json',claims)
checks=json.loads((run/'out'/'checks.json').read_text(encoding='utf-8'))
assert checks['failed_assertions']==0
assert checks['all_two_bit_outer_and_two_bit_children']==4096
assert checks['physical_restriction_cases']==864
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B12','packet_id':'A056',
    'gap_id':'FEI-B12-A056-INITIAL','attempt_id':'A056-baseline-1','method':'Exact coefficient reconstruction and spectral chain rule; recentered product-law extension; rational exhaustive validation',
    'mathematical_delta':'Completed the assigned known balanced disjoint baseline; explicit general-mean interface and exact physical-restriction scope witness. Full FEI remains open. Baseline should be adopted once and retired.',
    'deliverable_status':'COMPLETE_LOCAL; supervisor mirror pending',
    'mathematical_status':'BASELINE_PROVED_LOCAL; independent review pending; FULL_FEI_OPEN',
    'claim_versions_used':[], 'claims_created_or_changed':[{'claim_id':cid,'version':1} for cid,_ in statements],
    'source_artifacts':['REPORT.md','BALANCED_SUBSTITUTION_BASELINE.tex','COMPOSITION_INTERFACE.json','code/check.py','out/FROZEN_SPEC.json','out/checks.json','out/source_manifest.json','out/source_excerpts.txt'],
    'next_consumers':consumers,'next_action':'A091 independently reconstruct the coefficient identity and restriction witness; A057 consume a_T+m b_T for a signed restriction remainder. Do not repeat this baseline after adoption.',
    'stagnant_substantive_attempts':0,'blockers':['B12 lead STREAM_NOTES.md absent at initial read; did not block independent packet work','Independent review and supervisor copy not yet observed'],
    'packet_ids':['A056']}
dump(run/'PROGRESS.json',progress); dump(run/'PACKET_DELTA.json',progress)
(agent/'STATUS.md').write_text('STATE: A056 baseline complete locally: exact balanced/recentered H and I identities; 4961 exact cases passed; A091 review pending; full FEI OPEN.\nNEXT: A091 review/adopt once; A057 consume signed recentering a_T+m b_T for physical restriction remainder.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} — A056 stage 1: read protocol v2 and baseline sources; B12 lead notes absent. Proved unique-union coefficient identity, arbitrary-mean recentering, and branchwise physical restriction scope. Pilot 16 cases passed. Exhaustive 4096 substitutions, 864 restrictions and one majority/AND witness passed with Fraction/prime-log arithmetic; runtime {checks["runtime_seconds"]:.6f}s. Saved required run/TeX/interface artifacts. No shared edits; independent review/mirroring pending.\n')
(agent/'LEARNED.md').write_text('''# A056 durable composition facts

For disjoint balanced Boolean children, E F=E h, H(F)=H(h)+sum Inf_i(h)H(g_i), I(F)=sum Inf_i(h)I(g_i). The physical Fourier union recovers the outer set and each nonempty child set, so no hidden-label entropy is lost.

For means m_i and variances v_i=1-m_i^2>0, expand the gate under the independent output law. With biased spectral inclusion w_i, H(F)=H_mu(h)+sum (w_i/v_i)[H(g_i)-h2(v_i)], I(F)=sum (w_i/v_i)I(g_i). Absorb deterministic children first. Biased spectral inclusion w_i equals v_i times pivotal probability.

Physical restriction preserves disjoint supports and uniform product law on unrevealed coordinates, but need not preserve child balance. Recompute means, absorb constants, and reexpand the gate. If h=A+y_jB and the new child mean is m, outer coefficients become Ahat+m Bhat and sqrt(1-m^2)Bhat; retain 2m Ahat Bhat in squared weights.

Exact scope witness: AND_2(majority_3(x,a,b),z), restricted x=+1, has mean -1/4, I=5/4 and H=4-(9/8)log2(3); using initial balanced weights would incorrectly predict mean -1/2, I=1, H=3.

Conditional nonempty spectral entropy is (H(g)-h2(Var g))/Var g. The paper's strong entropy on a uniform physical cube is the raw NONEMPTY sum p log2(1/p), not H(g)-h2(Var g). Keep these conventions separate.

Exact rational prime-log entropy vectors certify finite identities without numerical logs. All 4096 two-bit gate/child triples, 864 physical restriction cases and one witness passed. This baseline is known and should be adopted once, not repeatedly advertised as overlap or full-FEI progress. Source-complete handoff is in the stage-1 run; reviewer A091, alternate A090; downstream signed remainder belongs to A057.
''',encoding='utf-8')
receipts=[]
for p in run.rglob('*'):
    if p.is_file() and p.name!='receipts.json' and '__pycache__' not in p.parts:
        data=p.read_bytes(); assert len(data)<20_000_000
        receipts.append({'path':str(p.relative_to(run)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump(run/'out'/'receipts.json',{'saved_at_utc':stamp,'local_only':True,'files':receipts})
print(json.dumps({'claims':len(claims),'checked_cases':4096+864+1,'source_files':len(manifest),'receipted_files':len(receipts),'checks_runtime_seconds':checks['runtime_seconds'],'local_saved':True,'review':'pending'},indent=2))
