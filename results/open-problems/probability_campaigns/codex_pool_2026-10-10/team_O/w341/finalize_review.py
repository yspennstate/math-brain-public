"""Write the review handoff only after the package validation has passed."""
import datetime as dt
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
summary=json.loads((ROOT/'measurements'/'package_summary.json').read_text(encoding='utf-8'))
validation=json.loads((ROOT/'measurements'/'package_validation.json').read_text(encoding='utf-8'))
assert validation['status']=='PASS'
assert summary['passed_experiment_batches']==10 and summary['independent_keeps']==0
stamp=dt.datetime.now().astimezone().isoformat(timespec='seconds')
report=f'''Prepared ten problem packets with {summary['typed_nodes']} typed draft nodes and {summary['edges']} quoted edges. The main measured advance is C0034: the earlier cited attempt left exact certification undone; our runs generated and independently replayed 72 rational coupling certificates, including eight rank-2 plus rank-2 instances in dimensions five and six. Every marginal residual in those eight cases is exactly zero. The rank-one-summand proof follows the published domination theorem; the explicit rank-two flow proof is also supplied. The general coupling question remains unresolved here.

The other packets recheck P0288's existing rank-two candidate, qualify the C0151 thinning endpoint, expose a lattice-growth TV error of 1/6, calibrate shared-weight bilateral graphs, correct site-colour state compression and the oriented-cluster walk convention, count degree-matched short cycles, recover known Fourier theta LPs and small expectations, and derive the four-regular-tree bootstrap critical vacancy 21/32. These are proofs of special cases, corrections, conditional reductions and explicitly labelled finite evidence. No new complete open-problem solution is claimed. C0151's literature refutation remains a lead: the two primary answer papers were not verified from the supplied caches.

Commands run: `python -X utf8 checks.py` (all ten batches passed; 6.793 seconds of reported batch time); `python -X utf8 higher_rank_certificates.py` (eight higher-rank certificates and exact replay passed; 0.268 seconds of measured certificate time); `python -X utf8 -B prepare_review.py`; `python -X utf8 -B validate_package.py` (bundle contracts, 11 exact existing logical targets, all 51 edge rationales, and both patch replays passed). Detailed numbers and commands are in measurements/. P0288 passed 784 exact resolvent recurrences; C0034 passed 2,580 subset cuts. The 60 theta LPs are numerical, with maximum equality residual 1.11e-15, and are not exact certificates. Lean returned SETUP_UNVERIFIED because compute telemetry was distressed/unknown; no Lean theorem is certified.

Apply: run `python -X utf8 -B validate_package.py` to replay patches/01_math_brain_bundles.diff against empty targets in a fresh local staging folder, then publish only independently kept drafts to ~/math-brain-inbox/w341/ using the BUNDLE_SPEC .part-to-.json procedure; patches/02_hook_proposals.diff supplies four hook proposals for their separate audit. Patch headers name live paths relative to ~. Local staged application was byte-identical to every prepared file. The immutable proof/certificate reports should be archived with ingestion. The local integrator was not run.

Audit handoff: AUDITOR_PACKET.md, CLAIMS_FOR_BLIND_AUDIT.json and READY_ROWS.jsonl. Every row has PENDING w347 and zero counted keeps. The reviewer should retire the two contradicted route assertions when promoting their correction nodes. Source status beyond the dated caches, novelty, and general versions of the open questions remain unverified. Package/data validation is not an independent mathematical audit. Live recall effects will need measurement after deployment.

All deliverables are in w341. COMMON.md requires "Write ONLY inside it" and forbids live-store writes and mesh sends, so the brain-inbox files, hook proposals and progress event are delivered as local review-ready changes rather than published here. No test bank was accessed. Account token/cost telemetry was not available; no estimate was invented.

NEXT: w347 blind-audit the 35 draft claims and replay the exact certificates; claude-4a88bc43 publishes and integrates only kept results.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
packet='''Auditor: w347 (gpt-6-luna). Proposer: w341. Manager: claude-4a88bc43.

For the blind pass, first read CLAIMS_FOR_BLIND_AUDIT.json and the original problem statements in reports/assigned_ledger_rows.json or reports/resolved_targets.json. Derive an independent verdict before opening the corresponding proofs/ report. Then check that report and the source passages it cites. No independent KEEP is currently recorded.

Write verdicts in your own folder, suggested path audits/w341.jsonl, one row per claim: {"problem", "key", "verdict": "KEEP"|"FIX"|"DROP", "why", "label"}. A KEEP of a finite certificate is not a KEEP of a general conjecture. For a FIX, provide the corrected statement and failed hypothesis. This handoff is by disk because the worker brief forbids mesh sends and live writes.

| Problem | What to check most closely | Proof report |
| --- | --- | --- |
| P0288 | Spectral boundary branch, zero atom, signed inversion, lambda-transience, positive minor; prior-art still unverified | proofs/P0288_recheck.md |
| C0034 | Capacitated Hall direction, second marginal, rank-one domination reduction; exact higher-rank replay | proofs/C0034_rank_two.md |
| C0151 | Fresh auxiliary labels, supremum versus attained endpoint, conditional large-d gap; primary literature lead unverified | proofs/C0151_thinning.md |
| P0127 | Rooted n-vertex convention, growth-history multiplicities, TV=1/6 and line complexity | proofs/P0127_growth_bias.md |
| P0456 | Shared edge weights, 2n-3 count, finite versus asymptotic obstruction | proofs/P0456_finite_calibration.md |
| C0058 | Vertex incidence identity; configurationwise obstruction does not prohibit weak lumping under a special law | proofs/C0058_boundary_identity.md |
| C0082 | Equal degree D=2d, unoriented rooted cycles; cycle counts are not lace coefficients | proofs/C0082_cycle_counts.md |
| C0126 | Undirected walk on oriented cluster, two-step return and disjoint-cut energy bound; random tails unproved | proofs/C0126_walk_direction.md |
| P0014 | Trace/eigenvalue normalization, even frequencies, exact small cases; float LP checks and tail gap | proofs/P0014_fourier.md |
| P0042 | Largest core fixed point, critical endpoint, root vacancy 21/32 and ergodicity | proofs/P0042_tree4.md |

Reproduction: copy checks.py and higher_rank_certificates.py into a new directory inside your own worker folder and run `python -X utf8 -B checks.py` followed by `python -X utf8 -B higher_rank_certificates.py` there, so generated measurements stay in your authorized folder. Inspect the original certificates using a separate Fraction/Gram-determinant calculation if possible. Original files are measurements/C0034_certificates.jsonl (64) and measurements/C0034_higher_rank_certificates.jsonl (8). No machine test bank is involved. The Lean receipt is unavailable, not a passed formal proof.

The drafts/ folder holds ten complete draft files. All 35 claims, including their dated status records, remain pending. Deployment and store mutation are reserved to the reviewer. No general problem may be marked newly solved merely because a numerical batch or algebra check passed.

NEXT: record blind verdicts before reading the proof reports, then check the proofs and replay certificates.
'''
(ROOT/'AUDITOR_PACKET.md').write_text(packet,encoding='utf-8')
claims=json.loads((ROOT/'CLAIMS_FOR_BLIND_AUDIT.json').read_text(encoding='utf-8'))
queue={'author':'w341','auditor':'w347','manager':'claude-4a88bc43','created_at':stamp,'status':'PENDING','claims':len(claims),'packet':str(ROOT/'AUDITOR_PACKET.md'),'claim_file':str(ROOT/'CLAIMS_FOR_BLIND_AUDIT.json'),'suggested_auditor_output':'~/brain_workers/w347/audits/w341.jsonl','counted_keeps':0}
(ROOT/'AUDIT_QUEUE.json').write_text(json.dumps(queue,indent=2)+'\n',encoding='utf-8')
event={'agent':'w341','row':'S1.O.w341','event':'10 packets; 35 draft nodes; 51 edges; 72 exact C0034 certificates; local validation PASS; w347 pending','evidence':str(ROOT/'REPORT.md'),'external_posted':False}
(ROOT/'PROGRESS_EVENT.json').write_text(json.dumps(event,indent=2)+'\n',encoding='utf-8')
receipt={**summary,'completed_at':stamp,'state':'NEEDS_REVIEW','account':'proofswarm (per brief)','model':'Codex GPT-6 (per developer description)','effort':'high (per brief)','token_cost':None,'token_cost_reason':'Not instrumented in available task tools; no forbidden account/profile inspection','validation':validation,'external_progress_posted':False,'external_audit_message_sent':False}
(ROOT/'SESSION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
old=(ROOT/'STATUS.md').read_text(encoding='utf-8').splitlines()
old[0]='STATE: NEEDS_REVIEW'
old[1]='NEXT: w347 blind-audit AUDITOR_PACKET.md and replay 72 exact certificates; reviewer publish only kept bundles from patches/01_math_brain_bundles.diff.'
old.append(stamp+': Completed ten proof reports, 35 draft nodes, 51 quoted edges, 72 exact coupling certificates and four hook proposals. Bundle and staged patch validation PASS. REVIEW READY; zero independent keeps, zero live ingestions. REPORT.md, AUDIT_QUEUE.json and SESSION_RECEIPT.json saved. Lean unavailable, source/novelty limits explicit.')
(ROOT/'STATUS.md').write_text('\n'.join(old)+'\n',encoding='utf-8')
print('STATE: NEEDS_REVIEW',flush=True)
print('35 draft nodes; 51 edges; 72 exact certificates; audit pending w347.',flush=True)
print(old[1],flush=True)
