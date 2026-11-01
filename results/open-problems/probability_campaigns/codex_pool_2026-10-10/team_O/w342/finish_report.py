"""Finalize review artifacts after the measured checks have passed."""
import difflib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
validation=json.loads((root/'bundle_validation.json').read_text(encoding='utf-8'))
handoff=json.loads((root/'bundle_handoff.json').read_text(encoding='utf-8'))
assert validation['valid_bundles']==10 and validation['rejected_negative_controls']==5
assert validation['proposed_entries']==sum(x['entries'] for x in handoff)
assert validation['proposed_relations']==sum(x['relations'] for x in handoff)
assert validation['deployed_store_change']==0
measurements={p:json.loads((root/(p.lower()+'_measurements.json')).read_text(encoding='utf-8')) for p in [x['problem_id'] for x in handoff]}
comb=json.loads((root/'p0133_comb_measurements.json').read_text(encoding='utf-8'))
hook=json.loads((root/'hook_measurements.json').read_text(encoding='utf-8'))
audit=json.loads((root/'AUDIT_RECEIVED.json').read_text(encoding='utf-8'))
hook_text=(root/'hooks/math-w342.jsonl').read_text(encoding='utf-8')
live='~/primary_directive/hooks1000/proposals/math-w342.jsonl'
patch=''.join(difflib.unified_diff([],hook_text.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
(root/'patches/11_math_hooks.diff').write_text(patch,encoding='utf-8')
counts={'lemma':0,'theorem':0,'concept':0}
for item in handoff:
    for entry in json.loads((root/item['bundle_file']).read_text(encoding='utf-8'))['entries']:
        counts[entry['kind']]+=1
table=[
 ('P0289','Independent bounded-Cox remainder proof; cyclic workload-rise candidate','715 configurations; 6,435 additions; 9 quadratures'),
 ('C0035','Equal pair laws miss triple phase by 16/15625','256 sublattice determinant checks'),
 ('P0001','Pairwise negative correlation for weighted theta blocks','420 exact covariance formulas; 21 weighted cases'),
 ('P0133','Unimodular theta windings; explicit bouquet convention caveat','11,664 trees; 9,072 theta cores; 4 comb witnesses'),
 ('C0002','Relative 1/log N correction to the bulk one-point Gaussian tail','24 tails; scaled remainder maximum 9.696'),
 ('C0059','Same quartic growth with opposite recurrence behavior','12 generation checks; transient flow energy 7/6'),
 ('C0083','Exact cycles and cubic susceptibility coefficient','6 graphs; 19,825 edge-subset checks'),
 ('C0128','Sublinear adverse-cookie drift gives directional transience','4,095 prefix checks; exact martingale mean zero'),
 ('P0015','Proof candidate for p_M<1 for all M>=2; p_2=p_3=0','7 exact Jacobians, M=2,...,8'),
 ('P0044','Canonical invariant inclusion coupling on all tree networks','54 wired trees; 48 joint-law symmetry checks'),
]
report=(
 f'Prepared ten problem bundles with {validation["proposed_entries"]} typed nodes ({counts["lemma"]} lemmas, {counts["theorem"]} theorems, {counts["concept"]} concepts) and {validation["proposed_relations"]} quoted edges. All thirteen result rows are saved in results.jsonl. w346 has kept {len(audit["kept_row_ids"])} rows: S1.w342.001 (second-order coefficient sign criterion) and .002 (prior-source scope correction). The larger proofs and full bundles await review; no complete open problem is reported solved. Novelty is unverified. This is a proposal for brain enrichment: no live ingestion or recall-improvement measurement has occurred.\n\n'
 'The main additions are the weighted theta-forest extension and the explicit phase-retrieval implicit-function argument. P0289 independently reconstructs the earlier candidate rather than claiming a new discovery. Every problem was checked against its earlier attempt and a bounded excerpt of its cached primary statement; later-ledger lookup is in later_status_scan.json. Literature status outside these cached sources remains unverified.\n\n'
 '| Problem | Saved result | Run evidence |\n|---|---|---|\n'
 + ''.join('| '+p+' | '+result+' | '+evidence+' |\n' for p,result,evidence in table)
 + '\nReproduce the mathematical checks with `python -X utf8 verify_p0289.py`, `python -X utf8 verify_structural.py`, `python -X utf8 verify_remaining.py`, and `python -X utf8 verify_torus_comb.py`. Receipts are the corresponding *_measurements.json files. These finite or numerical checks support the separate written proofs; they do not prove general asymptotic claims.\n\n'
 + f'Before/after preparation: 0 matching new logical ids in the live store versus {validation["after_matching_ids_in_prepared_drafts"]} in the prepared drafts; deployed store change is 0. `python -X utf8 validate_bundles.py` used the live parser read-only: 10/10 drafts accepted, 5/5 invalid controls rejected, {validation["resolved_existing_links"]} existing links resolved, and {validation["exact_endpoint_quote_checks"]} exact endpoint quotations verified. `python -X utf8 verify_hooks.py` passed all three fire and three silent controls; no hook was activated.\n\n'
 + 'Lean arithmetic was attempted with lean_check.py on lean/ross_margin.lean, named target ross_margin_bound and the reviewed source hash. It returned `SETUP_UNVERIFIED: Compute status is distressed or unknown`. No result is labeled Lean-checked; the rational margin passed exact Python checks.\n\n'
 + 'Audit risks: P0015 needs the full implicit-function and rank-two witness proof checked for all M, beyond the seven finite Jacobians. P0133 needs Claude source-convention review: a comb-tree bouquet has four no-repeated-edge trail winding classes, whereas the cached primary text says precisely three paths. The theta statement is explicitly conditional. C0002 does not give level-set fluctuations; C0059 does not model the Boltzmann law; C0083 does not determine a critical-value coefficient.\n\n'
 + 'Apply one kept bundle by running `python -X utf8 ~/brain_workers/w342/stage_reviewed.py --problem <ID> --verdict-file ~/brain_workers/w346/<verdict>.jsonl --apply`; it reconstructs the matching patches/NN_<id>_bundle.diff and requires w346 KEEP with proof_reviewed=true. Then the reviewer runs `python -X utf8 ~/math-brain-build/tools/integrate_drafts.py --only w342`. The three hook proposals are separately reviewable in patches/11_math_hooks.diff.\n\n'
 + 'Audit and progress handoffs are local because this worker brief forbids external writes and mesh/chat sends. AUDIT_REQUEST_w346.md lists the proof checks; bundle_handoff.json maps every patch to its intended live path; progress_rows.jsonl is ready for the reviewer to post.\n\n'
 + 'NEXT: w346 blind-check P0015 and P0289 first, claude-4a88bc43 reconcile the P0133 source convention, then land only fully kept bundles and measure live recall.\n'
)
(root/'REPORT.md').write_text(report,encoding='utf-8')
progress=[
 {'agent':'w342','row':'S1.w342.001','event':'w346 KEEP received for the second-order sign criterion and prior-source correction; full workload proof remains pending','evidence':str(root/'AUDIT_RECEIVED.json'),'posted':False},
 {'agent':'w342','row':'S1.w342.006','event':'P0289 candidate proof and 7,150 exact configuration/addition checks saved; pending blind audit','evidence':str(root/'proofs/P0289.md'),'posted':False},
 {'agent':'w342','row':'S1.w342.011','event':'P0015 first-clause proof candidate for every M and seven exact Jacobians saved; pending full blind audit','evidence':str(root/'proofs/P0015.md'),'posted':False},
 {'agent':'w342','row':'S1.w342.013','event':f'Ten bundles ready: {validation["proposed_entries"]} nodes, {validation["proposed_relations"]} quoted edges, parser and controls passed; NEEDS_REVIEW','evidence':str(root/'REPORT.md'),'posted':False},
]
(root/'progress_rows.jsonl').write_text(''.join(json.dumps(row)+'\n' for row in progress),encoding='utf-8')
rows=[json.loads(s) for s in (root/'results.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
assert len(rows)==13 and len({r['row_id'] for r in rows})==13
receipt={'agent':'w342','assigned_problems':10,'result_rows':len(rows),'proposed_nodes':validation['proposed_entries'],'proposed_edges':validation['proposed_relations'],'independent_keeps':len(audit['kept_row_ids']),'kept_row_ids':audit['kept_row_ids'],'full_bundle_approvals':0,'full_problems_claimed_solved':0,'lean_status':'SETUP_UNVERIFIED','ingested_bundles':0,'hooks_proposed':3,'patches':11,'publication_or_message_sends':0,'cost':'API token and monetary usage unavailable; not estimated'}
(root/'FINAL_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
