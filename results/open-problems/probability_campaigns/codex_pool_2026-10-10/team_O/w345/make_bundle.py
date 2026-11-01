"""Stage complete draft JSON, quoted edges, requests and unified diffs locally."""
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
rows=[json.loads(line) for line in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
research=[row for row in rows if row.get('slug')]
cards=json.loads((ROOT/'cards.json').read_text(encoding='utf-8'))
ids=['P0342','C0057','P0024','P0218','C0005','C0065','C0090','C0143','P0019','P0048']
assert set(row['problem_id'] for row in research)==set(ids)
research.sort(key=lambda row:(ids.index(row['problem_id']),row['row_id']))
entries=[]
relations=[]
edge_rows=[]

def source(path,slug,excerpt):
    return dict(source_id='owner:w345:'+slug,url=Path(path).resolve().as_uri(),revision='author-checked-2026-10-10-independent-audit-pending',license='owner-own-work',excerpt=excerpt[:180])

def quote(s):
    return s.replace('\n',' ')[:150]

def relation(from_key,kind,to_key=None,to_existing=None,target_statement=None,from_quote=None,to_quote=None,why=''):
    a=next(e for e in entries if e['key']==from_key)
    b=next((e for e in entries if e['key']==to_key),None) if to_key else None
    qa=from_quote or quote(a['statement'])
    qb=to_quote or quote(b['statement'] if b else target_statement)
    assert qa in a['statement'] or qa in (a['proof_text'] or '')
    assert qb in (b['statement'] if b else target_statement)
    rationale=f'From: "{qa}"; to: "{qb}". {why}'
    edge=dict(from_key=from_key,kind=kind,rationale=rationale)
    if to_key:
        edge['to_key']=to_key
    else:
        edge['to_existing_logical']=to_existing
    relations.append(edge)
    edge_rows.append(dict(row_id=f'S1.w345.E{len(edge_rows)+1:03d}',**edge,from_quote=qa,to_quote=qb,audit_status='PENDING_W347'))

for card in cards:
    if card.get('draft_target_key'):
        file=ROOT/'proofs'/(card['draft_target_key']+'.md')
        file.write_text(card['statement']+'\n\nCached source: '+card['evidence_path']+':'+str(card['evidence_line'])+'\n',encoding='utf-8')
        entries.append(dict(key=card['draft_target_key'],namespace='probability.percolation',logical_name='exponential-infinite-cluster-contact-tail-transitive-graphs-question',kind='concept',title=card['title'],statement=card['statement'],proof_text=None,assumptions=[],domain='probability theory',source=source(file,card['draft_target_key'],card['statement'])))

for row in research:
    namespace='probability.'+({'P0342':'random-trees','C0057':'planarmaps','P0024':'reflected-brownian-motion','P0218':'spatial-growth','C0005':'gaussian','P0019':'brownian-motion','P0048':'spanning-forests'}.get(row['problem_id'],'percolation'))
    entries.append(dict(key=row['slug'],namespace=namespace,logical_name=row['slug'],kind=row['kind'],title=row['title'],statement=row['statement']+' Scope: '+row['limitations'],proof_text=('Author-checked proof; independent audit pending. '+row['proof_text']) if row['proof_text'] else None,assumptions=row['assumptions'],domain='probability theory',source=source(row['proof_path'],row['slug'],row['statement'])))

for row in research:
    relation(row['slug'],'cites',to_key=row.get('target_key'),to_existing=row.get('to_existing_logical'),target_statement=row['target_quote'],why='Connects this scoped result to its original problem; no full solution is claimed.')

for pid,slug,kind,needle in [
 ('P0342','retained-root-fringe-perturbation-threshold','generalizes','n^-1/4*(B_n-p_n)'),
 ('P0024','annular-skoro-distance-expansion','analogous_to','Convexity makes both contributions nonpositive'),
 ('P0218','critical-immigration-logarithmic-lower-bound','analogous_to','Put theta=(1-alpha)/(1+d)'),
 ('C0065','susceptibility-derivative-inference-refuted','refutes','dtheta/dp <= C chi^f(p) and theta ~ (p - p_c) give chi^f(p) >= c/(p - p_c)'),
 ('P0019','holder-boundary-terminal-angle','specializes','every limit of (z-B_s)/|z-B_s|'),
 ('P0048','ergodic-forests-arbitrary-finite-component-count','generalizes','The two components are the even and odd integers')]:
    matches=[c for c in cards if c['problem_id']==pid and c['kind']=='attempt']
    assert len(matches)==1,(pid,len(matches))
    card=matches[0]
    assert needle in card['statement'],(pid,needle)
    relation(slug,kind,to_existing=card['logical_id'],target_statement=card['statement'],to_quote=needle,why='The relation concerns this quoted step, with the result assumptions and scope retained.')

relation('decorated-poisson-level-count-criterion','depends_on',to_key='truncated-decoration-poisson-mean',why='The cutoff expectation identity is used in the conditional law-of-large-numbers proof.')
relation('survival-compensator-exhaustion-criterion','cites',to_key='stopped-hazard-divergence-not-necessary',why='The deterministic example separates sufficient divergence from an unjustified necessity claim.')
relation('binary-tree-finite-susceptibility-exponent','analogous_to',to_key='regular-tree-infinite-contact-exponential-tail',why='Both use the explicit finite-cluster law conditioned on extinction; neither supplies a lattice result.')
relation('fringe-clt-uniform-error-threshold','analogous_to',to_key='retained-root-fringe-perturbation-threshold',why='Both expose the square-root scale that qualitative local convergence does not control.')
relation('critical-immigration-logarithmic-lower-bound','depends_on',to_key='max-influence-city-founding-rate',why='The verified max-influence bound supplies the probabilistic lemma hypotheses at alpha=1, beta>0, including the d=0 boundary case.')
relation('annular-skoro-distance-expansion','cites',to_key='one-hole-exclusion-source-restriction',why='The source restriction explains why finite annular expansion cannot establish persistent Brownian separation.')

# Include the measured receipt in the brain draft, not only in a scratch report.
metrics=json.loads((ROOT/'measurements.json').read_text(encoding='utf-8'))
receipt_statement=f'Research receipt dated 2026-10-10: w345 staged {len(research)} scoped results for the ten assigned probability problems. {metrics["check_groups"]} check groups passed across {metrics["cases"]} finite exact cases and numerical diagnostics. These checks supplement the written arguments; they do not certify general theorems or the half-space reversal sketch. Independent KEEP count is zero at handoff, no full open problem is claimed solved, and no live brain store was written in this worker round. Lean admission refused the distressed host; the prepared algebraic formalization is uncompiled. Actual model token and monetary usage telemetry is unavailable to this worker; no values are inferred.'
receipt_file=ROOT/'proofs'/'w345-first-ten-validation-receipt.md'
receipt_file.write_text(receipt_statement+'\n\nCommands: python -B -X utf8 check_results.py; python -B -X utf8 check_city_rate.py; python -B -X utf8 validate_bundle.py; python -B -X utf8 lean_admission.py.\n',encoding='utf-8')
entries.append(dict(key='w345-validation-receipt',namespace='probability.research',logical_name='w345-first-ten-open-problem-validation-receipt-20261010',kind='concept',title='w345 first-ten research validation receipt',statement=receipt_statement,proof_text=None,assumptions=[],domain='probability research validation',source=source(receipt_file,'w345-validation-receipt',receipt_statement)))
for key in ('critical-immigration-logarithmic-lower-bound','susceptibility-derivative-inference-refuted','decorated-poisson-level-count-criterion','halfspace-terminal-hemisphere-sketch'):
    relation('w345-validation-receipt','cites',to_key=key,why='Records the checked scope and pending independent-review status of this result; no theorem certificate is implied.')

bundle=dict(spec='mathbrain-draft-v1',author_agent='w345',bundle_slug='w345-first-ten-problem-results-20261010',entries=entries,relations=relations)
stage=ROOT/'staged'/'math-brain-inbox'/'w345'
stage.mkdir(parents=True,exist_ok=True)
file=stage/'bundle_001.json'
payload=json.dumps(bundle,indent=2,ensure_ascii=False)+'\n'
part=file.with_suffix('.part')
part.write_text(payload,encoding='utf-8')
part.replace(file)
(ROOT/'edges.jsonl').write_text(''.join(json.dumps(edge,ensure_ascii=False)+'\n' for edge in edge_rows),encoding='utf-8')

patches=ROOT/'patches'
patches.mkdir(exist_ok=True)
live='math-brain-inbox/w345/bundle_001.json'
diff=''.join(difflib.unified_diff([],payload.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live,n=3))
(patches/'01_brain_drafts.diff').write_text(diff,encoding='utf-8')

hooks=[
dict(id='math-w345-01',area='math',event='PostToolUse',cue='A claimed inverse-distance susceptibility bound is inferred only from theta(delta) asymptotic to delta and theta derivative bounded by C chi.',fire_when='A proof concludes chi(delta)>=c/delta from those two premises alone.',silent_when='The inverse-distance bound has a separate checked percolation argument with all extra premises supplied.',text='A linear order parameter and theta derivative <= C chi do not force inverse-distance divergence: theta(delta)=delta, chi(delta)=1 satisfy both. Check the missing percolation premise before recalling this as a theorem.',evidence=str(ROOT/'proofs'/'susceptibility-derivative-inference-refuted.md')+'; S1.w345.008; measurements.json: 1000 exact rational counterexamples',proposer='w345'),
dict(id='math-w345-02',area='math',event='PostToolUse',cue='A marked extremal Poisson sum with exponential decoration growth is assigned finite full expectation or L2 convergence without an upper-height cutoff.',fire_when='The proof integrates all heights and applies an unqualified moment law of large numbers.',silent_when='The proof controls finite cutoffs and removes them in probability, or independently proves the required full moments.',text='For heights with intensity e^(-alpha h), the substitution s=t+h gives e^(alpha t)e^(-alpha s). Exponential decoration means can make the full expectation infinite. Verify the sign and use an upper-height cutoff before a moment argument.',evidence=str(ROOT/'proofs'/'truncated-decoration-poisson-mean.md')+'; measurements.json: 27 original-coordinate integral checks',proposer='w345')]
hooks.append(dict(id='math-w345-03',area='math',event='PostToolUse',cue='Finite annular synchronous-reflection expansion is proposed as a counterexample to eventual Brownian contraction in a bounded domain.',fire_when='An annulus or a finite-time expanding path is claimed to solve Burdzy Problem 5(i).',silent_when='The calculation is explicitly a finite-time lemma, or a candidate with at least two holes includes a separate long-term argument.',text='Burdzy\'s cached author page says a bounded counterexample to positive limsup separation must have at least two holes (Burdzy-Chen-Jones, 2006). An annulus can expand at finite times and still fail as a long-term counterexample. Check the full theorem and time scale.',evidence=str(ROOT/'proofs'/'one-hole-exclusion-source-restriction.md')+'; cached burdzy_open_20260906/text.txt:120-123',proposer='w345'))
assert all(len(h['text'])<=300 for h in hooks)
proposals=ROOT/'staged'/'primary_directive'/'hooks1000'/'proposals'
proposals.mkdir(parents=True,exist_ok=True)
hook_payload=''.join(json.dumps(h,ensure_ascii=False)+'\n' for h in hooks)
(proposals/'math-w345.jsonl').write_text(hook_payload,encoding='utf-8')
live='primary_directive/hooks1000/proposals/math-w345.jsonl'
(patches/'02_hook_proposals.diff').write_text(''.join(difflib.unified_diff([],hook_payload.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live,n=3)),encoding='utf-8')

requests=[dict(to_agent='w347',row_id=row['row_id'],problem_id=row['problem_id'],label=row['label'],proof_path=row['proof_path'],draft_entry_key=row['slug'],verdict='PENDING',request='Independently check statement, assumptions, proof and scope; return KEEP/FIX/DROP with reasons. No open problem is claimed solved.') for row in research]
(ROOT/'audit_requests.jsonl').write_text(''.join(json.dumps(request,ensure_ascii=False)+'\n' for request in requests),encoding='utf-8')
metrics=json.loads((ROOT/'measurements.json').read_text(encoding='utf-8'))
receipt=dict(agent='w345',row='S1.w345.008',event=f'w345 saved {len(research)} result nodes for 10 problems; {metrics["check_groups"]} check groups pass; w347 audit pending.',evidence=str(ROOT/'REPORT.md'),dispatch_status='STAGED_ONLY_NO_EXTERNAL_WRITE')
(ROOT/'progress_receipts.jsonl').write_text(json.dumps(receipt)+'\n',encoding='utf-8')
summary=dict(problem_count=10,result_rows=len(rows),research_results=len(research),proof_results=sum(r['label']=='proof' for r in research),sketch_results=sum(r['label']=='sketch' for r in research),source_status_results=sum(r['label']=='source-status' for r in research),draft_entries=len(entries),draft_relations=len(relations),quoted_edge_rows=len(edge_rows),existing_problem_contexts=sum(c['kind']=='problem' and c['logical_id'] is not None for c in cards),local_problem_contexts=sum(c.get('draft_target_key') is not None for c in cards),hook_proposals=len(hooks),independent_keeps=0,brain_writes=0)
(ROOT/'bundle_summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary))
