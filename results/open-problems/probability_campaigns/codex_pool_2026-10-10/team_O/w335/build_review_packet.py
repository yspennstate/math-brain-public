import difflib
import json
import math
import pathlib
import re
import time

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()
validation=json.loads((root/'validation_receipt.json').read_text(encoding='utf-8'))
assert validation['result']=='PASS' and not validation['errors']
problem_ids=['P0205','P0429','C0127','P0050','P0255','C0014','C0073','C0109','P0004','P0027']
bundles=[json.loads((root/'bundles'/('bundle_%03d.json'%number)).read_text(encoding='utf-8')) for number in range(1,11)]
cards=json.loads((root/'baseline_cards.json').read_text(encoding='utf-8'))
rows=[json.loads(line) for line in (root/'results.jsonl').read_text(encoding='utf-8').splitlines() if line]
existing_row_ids={row['row_id'] for row in rows}
for problem_id in problem_ids:
    row_id='w335-'+problem_id+'-literature-scope'
    card=next(card for card in cards if card['title'].startswith('Open problem:') and ('open-problem-'+problem_id.lower()+'-') in card['metadata_json'])
    row={'row_id':row_id,'problem_id':problem_id,'result_type':'bounded_status_receipt','label':'literature_check_pending','source_logical':json.loads(card['metadata_json'])['logical_id'],'source_quote':card['body'],'statement':'The observed cached card records source_says_open and current status unverified. No exact literature solution was established by this bounded offline pass. The new bundle contains limited author proofs and is not a solved-problem certificate.','scope':'Assigned ranking, scoped prior-attempt searches, existing problem/attempt cards; four named cached primary texts. The old Codex campaign worktree path no longer exists. No web search.','audit_status':'pending_w347','created':'2026-10-10'}
    if row_id not in existing_row_ids:
        with (root/'results.jsonl').open('a',encoding='utf-8') as stream:
            stream.write(json.dumps(row,ensure_ascii=False)+'\n')
        existing_row_ids.add(row_id)

sections=json.loads((root/'cached_primary_sections.json').read_text(encoding='utf-8'))
patterns={'biskup_dgff_extrema_2020':r'Problem 16\.14|\(13\.13\)','heydenreich_hofstad_highd_2017':r'Open Problem 14\.1','chatterjee_chaos_2008':r'equivalent.*chaos|equivalent.*superconcentration|^12\.','tao_vu_littlewood_offord_2009':r'rate of convergence|convergence rate'}
alignment=[]
texts={}
for section in sections:
    if not section.get('match_verified'):
        continue
    path=section['path']
    if path not in texts:
        texts[path]=pathlib.Path(path).read_text(encoding='utf-8',errors='replace')
    number=section['match_line']
    pattern=patterns[section['source_id']]
    text=texts[path]
    lf_line=text.split('\n')[number-1]
    legacy_line=text.splitlines()[number-1]
    now_matches=bool(re.search(pattern,lf_line,re.I))
    old_matches=bool(re.search(pattern,legacy_line,re.I))
    assert now_matches
    alignment.append({'source_id':section['source_id'],'rg_line':number,'legacy_splitlines_matches':old_matches,'lf_line_matches':now_matches})
assert alignment
alignment_receipt={'command':'python -X utf8 build_review_packet.py','cases':alignment,'legacy_bad_windows':sum(not value['legacy_splitlines_matches'] for value in alignment),'corrected_bad_windows':sum(not value['lf_line_matches'] for value in alignment),'result':'PASS'}
(root/'line_alignment_audit.json').write_text(json.dumps(alignment_receipt,indent=2),encoding='utf-8')

hooks=[
    {'cue':r'(?is)(?=.*geometric)(?=.*(?:monoton|relaxation))(?=.*\bp\b)(?=.*(?:decreas|increas))','fire_when':'Geometric stopping p: relaxation decreases as p increases.','silent_when':'Mean geometric time grows; the derived relaxation decreases under that parametrisation.','text':'Write the geometric law explicitly. For Geo0(p), increasing p decreases the mean time. Compare spectral-gap conventions and degree restrictions before asserting a relaxation monotonicity or uniform bound.','evidence':str(root/'p0205_measurement.json')+'; 60 exact cases, ratio/n tends to 2/3 in the proved lazy family.'},
    {'cue':r'(?is)(?=.*(?:wired|wiring))(?=.*(?:annul|layer|interface))(?=.*resistance)(?=.*(?:upper bound|original resistance\s*<=))(?!.*\bmatched\b)','fire_when':'Upper bound: original resistance <= sum of independently wired layer resistances.','silent_when':'Wiring interfaces gives a lower resistance comparison; unit flows for an upper construction are explicitly matched.','text':'Wiring layer interfaces lowers resistance. A sum of independently wired layer minima is a lower comparison. For an upper construction, check that consecutive unit flows match their interface currents.','evidence':str(root/'c0014_measurement.json')+'; M=100 gives original/wired=25.5025 and a nonzero interface current mismatch.'},
    {'cue':r'(?is)(?=.*(?:growing|many))(?=.*near.?peaks)(?=.*(?:superconcentr|chaos))(?=.*(?:bounded away from one|bounded below one))','fire_when':'Many near-peaks with covariance bounded below one imply superconcentration.','silent_when':'Growing near-peaks have covariance tending to zero after the common component is removed.','text':'Test for a common Gaussian component. Many near-maximal points and covariance bounded away from one can coexist with variance bounded below. Specify whether overlaps must vanish and whether the peak event has probability tending to one.','evidence':str(root/'C0127_proof.md')+' and '+str(root/'c0127_measurement.json')+'; Var(M)>=rho=1/2, while the proved near-peak count diverges.'},
    {'cue':r'(?is)(?=.*Rayleigh)(?=.*diffusion)(?=.*monoton)(?=.*(?:implies|therefore|\bso\b))','fire_when':'Rayleigh implies monotonic diffusion with increasing conductance.','silent_when':'Rayleigh gives monotonic conductivity; diffusion is computed under both specified clocks.','text':'Specify the walk clock and speed measure. Rayleigh controls electrical conductivity. Dividing by a changing speed mass can reverse diffusion monotonicity; a dangling leaf gives D_CS=1/(1+a).','evidence':str(root/'c0073_measurement.json')+'; conductivity=1, constant-speed variance rate falls from 1/2 to 1/100, variable-speed rate stays 1.'},
    {'cue':r'(?is)(?=.*rank)(?=.*(?:nonnormal|non.normal|non.Hermitian))(?=.*(?:empirical eigen|ESD))(?=.*bound)','fire_when':'Nonnormal ESD discrepancy is bounded by rank/n after truncation.','silent_when':'Hermitian ESD discrepancy is bounded by rank/n; singular values use a Hermitian dilation.','text':'A rank-one nonnormal perturbation can change the eigenvalue law by one on a bounded Lipschitz test. Use Hermitization and singular-value control; do not transfer a Hermitian eigenvalue rank bound or infer an optimal rate from a truncation upper estimate.','evidence':str(root/'c0109_measurement.json')+'; n=64, rank fraction=1/64 but the radial spectral test gap is 1.'},
    {'cue':r'(?is)(?=.*(?:pdf|extracted))(?=.*\brg\b)(?=.*splitlines)','fire_when':'Quote rg line numbers from extracted PDF text using Python splitlines.','silent_when':'Quote rg line numbers using LF splitting and check the needle at each cited line.','text':'Match rg line numbers with LF splitting. Python splitlines also splits PDF control separators and can shift source quotations. Verify the expected match at the cited line before saving a source verdict.','evidence':str(root/'line_alignment_audit.json')+'; old bad windows='+str(alignment_receipt['legacy_bad_windows'])+', corrected='+str(alignment_receipt['corrected_bad_windows'])+'.'},
]
hook_controls=[]
for number,hook in enumerate(hooks,1):
    hook.update({'id':'math-w335-%02d'%number,'area':'math' if number<6 else 'brain','event':'stage-start','proposer':'w335'})
    assert len(hook['text'])<=300
    fire=bool(re.search(hook['cue'],hook['fire_when']))
    silent=bool(re.search(hook['cue'],hook['silent_when']))
    hook_controls.append({'id':hook['id'],'fire':fire,'silent':silent})
assert all(control['fire'] and not control['silent'] for control in hook_controls),hook_controls
(root/'hooks').mkdir(exist_ok=True)
hook_text=''.join(json.dumps(hook,ensure_ascii=False)+'\n' for hook in hooks)
(root/'hooks'/'math-w335.jsonl').write_text(hook_text,encoding='utf-8')
(root/'hook_controls.json').write_text(json.dumps({'command':'python -X utf8 build_review_packet.py','controls':hook_controls,'result':'PASS'},indent=2),encoding='utf-8')

packet={'agent':'w335','auditor':'w347','reviewer':'claude-4a88bc43','state':'author_checked_pending_independent_review','full_problem_solutions_claimed':0,'independent_keeps_recorded':0,'entries':[],'validation':str(root/'validation_receipt.json'),'lean_scope':'Optional scalar identity only; helper refused to start: distressed or unknown compute state; not Lean-checked.'}
for problem_id,bundle in zip(problem_ids,bundles):
    for node in bundle['entries']:
        packet['entries'].append({'problem_id':problem_id,'key':node['key'],'logical_id':'math:'+node['namespace']+':'+node['logical_name'],'label':'author proof of explicitly stated limited result; pending KEEP','bundle':str(root/'bundles'/('bundle_%03d.json'%(problem_ids.index(problem_id)+1))),'proof':str(root/(problem_id+'_proof.md')),'checks':str(root/(problem_id.lower()+'_measurement.json')),'requested_verdict':'KEEP, FIX or DROP after blind proof check'})
(root/'REVIEW_PACKET.json').write_text(json.dumps(packet,indent=2),encoding='utf-8')
(root/'AUDIT_REQUEST.md').write_text('w347: blind proof review requested for the 15 entries in REVIEW_PACKET.json, with KEEP/FIX/DROP per key. No full open problem is claimed solved. Numerical samples are explicitly illustrative; please check the complete arguments and boundary assumptions. The optional Lean check did not start. All independent keep counts remain zero.\n\nThe ten complete draft bundles are in ~/math-brain-inbox/w335/ and mirrored in bundles/. AUDIT_REQUEST.jsonl gives one request per problem. This file handoff obeys the packet ban on mesh send commands and SQLite writes.\n',encoding='utf-8')

patches=root/'patches'
patches.mkdir(exist_ok=True)
diff=[]
for number in range(1,11):
    name='bundle_%03d.json'%number
    live_path='math-brain-inbox/w335/'+name
    diff.extend(difflib.unified_diff([], (root/'bundles'/name).read_text(encoding='utf-8').splitlines(keepends=True),fromfile='a/'+live_path,tofile='b/'+live_path))
(patches/'01_math_bundle_drafts.diff').write_text(''.join(diff),encoding='utf-8')
hook_path='primary_directive/hooks1000/proposals/math-w335.jsonl'
(patches/'02_math_hooks.diff').write_text(''.join(difflib.unified_diff([],hook_text.splitlines(keepends=True),fromfile='a/'+hook_path,tofile='b/'+hook_path)),encoding='utf-8')
events=[]
for number,(problem_id,bundle) in enumerate(zip(problem_ids,bundles),1):
    events.append({'agent':'w335','row':'S1.O.w335','event':'w335 '+problem_id+' nodes='+str(len(bundle['entries']))+' edges='+str(len(bundle['relations']))+' ~/math-brain-inbox/w335/bundle_%03d.json'%number,'evidence':str(root/(problem_id+'_proof.md')),'status':'staged_not_sent_under_packet_no_sends_and_folder_only_rule'})
(root/'PROGRESS_PENDING.jsonl').write_text(''.join(json.dumps(event)+'\n' for event in events),encoding='utf-8')

report='''15 draft lemma nodes and 27 edges are saved for the ten assigned problems, with both endpoints quoted on every edge. All ten numerical or algebraic check scripts passed. The strongest measured extension is P0205: an exact Metropolis relaxation formula for every complete Cayley graph, extending the earlier two-state calculation. All results await w347; zero independent keeps and zero full open-problem solutions are claimed.

For the lazy P0205 family with alpha=p=1/2, `python -X utf8 check_p0205.py` gives a relaxation ratio of 1.5 at n=2 and 682.777850 at n=1024 from the proved formula. Complete kernels were checked with exact fractions at n=2,3,4,8,16,32: 60 cases and 16,388 assertions. The ratio grows linearly while the base relaxation stays below 2; proposal degree grows with n. This is a measured family calculation, not a deployed recall benchmark or a fixed-degree result.

| Problem | Saved result | Run evidence |
|---|---|---|
| P0205 | Complete-Cayley spectrum and explicit parameter direction | 60 exact cases; 16,388 assertions |
| P0429 | Simultaneous arrivals obstruct path independence at the cubic scale | 170 exact hypergeometric cases |
| C0127 | Common-factor counterexample to the stated growing-peaks criterion; two-peak quantifier correction | Proof plus 1,200 illustrative samples |
| P0050 | Divergent squared marginal gap implies singularity under negative correlations | 40 exact product-law cases |
| P0255 | Weighted-star variation at most 1/(2 sqrt(6)) | 1,360 weight vectors, four one-leaf cases; 200 general graphs searched numerically |
| C0014 | Wired layer minima give the lower comparison; incompatible currents block gluing | Six exact four-vertex cases; ratio 25.5025 at M=100 |
| C0073 | Added dangling conductance slows a constant-speed walk while conductivity stays fixed | Eight exact clock cases |
| C0109 | Sharp scalar truncation envelope; rank-one nonnormal spectral obstruction | Ten exact tail cases and seven spectral cases |
| P0004 | A nonstationary bounded-degree tree lacks a connective limit; p=1 lattice boundary works | Eight block ends and lattice enumeration through length ten |
| P0027 | Smooth all-starts deterministic maps are rigid; positive displacement characterizes the isometry class | Four exact tensor ranks and 16 rotation gaps |

`python -X utf8 validate_deliverables.py` passed the integrator's isolated shape-validator function, all 27 endpoint quotations, and 18 existing targets read from SQLite in read-only mode. Recorded successful check-body runtimes total %.6f seconds; this excludes process launch, queueing, reading and inference cost. Commands and full receipts are in each `<problem>_measurement.json`; the additional star boundary command is `python -X utf8 finalize_corrections.py`.

The Lean helper returned `SETUP_UNVERIFIED: Compute status is distressed or unknown`. GapIdentity.lean formalizes only the scalar gap identity and remains unverified. No result is labelled Lean-checked.

Literature status is `literature_check_pending` for all ten. The ranking and observed cards record historical source statements, not present-openness certificates. Four named cached primary texts were inspected. The earlier Codex worktree path no longer exists; existing typed attempt cards supplied those six earlier attempts. No exact literature solution was established in this bounded offline pass; no web search was used. Source receipts are in results.jsonl and source_records.json.

The material limits are explicit in each node: P0429 treats whole paths, P0050 still needs a divergent forest marginal gap, C0127 keeps nonzero overlap, and the tree, periodic network and deterministic nonnormal examples lie outside the full models in their assigned questions. Numerical searches are not proofs. Six measured hook proposals passed one fire and one silent control each and are staged in hooks/math-w335.jsonl. Source-line alignment improved from %d wrong windows to zero over %d checked hits.

Apply: after w347's KEEP/FIX/DROP review, the reviewer should retain only approved entries and run `python -B -X utf8 ~/math-brain-build/tools/integrate_drafts.py --only w335`; patches/01_math_bundle_drafts.diff names the same live inbox paths, and patches/02_math_hooks.diff stages the separately audited hook proposals. No live store or code was edited. Audit and progress handoffs are files because the packet forbids sends and SQLite writes; PROGRESS_PENDING.jsonl is not a claim of publication.

NEXT: w347 audits REVIEW_PACKET.json; the reviewer integrates only KEEP entries and records the receipts in the brain.
'''%(validation['sum_measurement_compute_seconds'],alignment_receipt['legacy_bad_windows'],len(alignment))
(root/'REPORT.md').write_text(report,encoding='utf-8')
cost={'agent':'w335','date':'2026-10-10','draft_nodes':15,'quoted_edges':27,'problem_bundles':10,'independent_keeps':0,'successful_latest_check_body_seconds':validation['sum_measurement_compute_seconds'],'inference_tokens':None,'inference_cost':None,'accounting_limit':'No authorized API usage meter was available; local check seconds are not inference cost. Earlier failed bundle-link run is excluded from the successful-check sum.'}
(root/'COST_RECEIPT.json').write_text(json.dumps(cost,indent=2),encoding='utf-8')
assert len(packet['entries'])==15
receipt={'command':'python -X utf8 build_review_packet.py','draft_entries':len(packet['entries']),'bundles':len(bundles),'hooks':len(hooks),'hook_fire_controls':sum(control['fire'] for control in hook_controls),'hook_silent_controls':sum(not control['silent'] for control in hook_controls),'legacy_bad_source_windows':alignment_receipt['legacy_bad_windows'],'corrected_bad_source_windows':0,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS'}
(root/'review_packet_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2),flush=True)
