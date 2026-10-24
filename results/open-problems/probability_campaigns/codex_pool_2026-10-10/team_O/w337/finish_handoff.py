from pathlib import Path
import datetime as dt
import json
import sys

import package_handoff
import validate_handoff

ROOT=Path(__file__).resolve().parent
package_handoff.main()
validate_handoff.main()
audit=json.loads((ROOT/'AUDIT_REQUEST_w347.json').read_text(encoding='utf-8'))
validation=json.loads((ROOT/'measurements'/'handoff_validation.json').read_text(encoding='utf-8'))
assert validation['verdict']=='PASS'
comparison=json.loads((ROOT/'measurements'/'p0209_before_after.json').read_text(encoding='utf-8'))
report='''Prepared ten checked problem reports, 20 typed draft nodes, 34 edges quoting both ends, and two hook proposals. Blind audit is PENDING with w347. No open-problem solution is promoted.

The main measured change replaces the cached P0209 numerical check with exact algebra and an analytic normal-distance bound. An unchanged local copy produced four Monte Carlo estimates using 80,000 paths and a Gaussian substitute for the fast chain. The replacement uses zero random paths, verifies six scales exactly, and gives a bound evaluated as 0.49974999995 at t=10,000. Two additional boundary cases s=2,3 pass. The original proof already had the correct rare-event argument; the later memory explanation needed a variance-versus-probability-limit correction. The initial apparent ranking conflict is explicitly superseded in results.jsonl.

| Problem | Saved result and limit of scope | Measurement |
|---|---|---|
| P0209 | Candidate negative answer with rational parameters; uniform-integrability correction | Six exact scales, two boundary cases |
| P0459 | Actual-mean deficit and sufficient simultaneous concentration | 78 exact pairs; 720 edge orders |
| C0130 | Finite-interval escape upper bounds; whole-half-line state correction | Seven intervals; 0.8 to 0.662156 |
| P0088 | Marked birth coupling and conditional exploration bound | 25 vectors; count distance 0 versus marked 1/2 |
| P0336 | Opposite vanishing tilts select different plans | 720 matchings; 36 primary versus one per tilt |
| C0022 | Summable separator criterion; moments alone do not prove singularity | Exact third-moment gap 1/4 with equivalent laws |
| C0076 | Necessary exponent and explicit tightness obstruction | Six scales retain height-one oscillations |
| C0117 | Complete-graph variance and tails with clock convention explicit | 200 exact harmonic cases; 800 cumulant checks |
| P0009 | Added mirror opens a periodic orbit; iid conjecture remains unresolved | Period 12 to a certified unbounded ray |
| P0035 | Exact speed on products of regular trees | 28 bias cases; 296 root patterns |

Reproduce the principal comparison with `python -X utf8 benchmark_p0209.py`; validate the handoff with `python -X utf8 validate_handoff.py`. Each problem's `*_check.py` command is recorded in measurements/. All ten check runs passed. Validation passed all 34 quote matches, dependency acyclicity, schema checks, and two fire plus two silent hook controls.

Risks: author proofs still need blind review; current literature status and novelty were not verified beyond the cached papers. Floating-point evaluations of analytic expressions are not interval-arithmetic certificates. Lean admission returned "Compute status is distressed or unknown", so no Lean certification is claimed. The observed full-process times were 5.16 seconds for the baseline and 7.59 seconds for the replacement; this is a verification-quality comparison, not a speedup or deployed-recall claim.

Apply: after the required KEEP and full proof check, copy `bundles/bundle_001.json` to DESTINATION; `patches/01_ten_problem_bundle.diff` names that live target. `patches/02_math_hook_proposals.diff` prepares the two proposals for the usual pair audit. The manager routes `AUDIT_REQUEST_w347.json` and posts `PROGRESS_PENDING.jsonl` on landing. The worker brief's "Write ONLY inside it" and prohibition on mesh send commands are why this handoff remains local for reviewer deployment.

NEXT: w347 blind-audits the 20 entries and 34 edges; claude-4a88bc43 applies only kept material after the full P0209 proof check.
'''
report=report.replace('DESTINATION','`'+audit['draft_destination_after_review']+'`')
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
receipt={'agent':'w337','date_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
         'task':'Team O assigned ten open-problem attempts','problem_ids':package_handoff.IDS,
         'state':'NEEDS_REVIEW','problem_results':10,'draft_nodes':20,'quoted_edges':34,'hook_proposals':2,
         'blind_auditor':'w347','audit_state':'PENDING','solutions_promoted':0,
         'checks':'ten mathematical check scripts plus handoff validation passed',
         'lean_certified':False,'live_store_writes':0,'network_requests':0,'mesh_messages_sent':0,
         'writes_root':ROOT.as_posix(),'python_version':sys.version,
         'provider_tokens_read':None,'provider_tokens_written':None,'provider_cost':None,
         'cost_note':'Provider token and billing telemetry is not exposed in this worker; supervisor ledger must supply actual usage.',
         'before_after_receipt':(ROOT/'measurements'/'p0209_before_after.json').as_posix(),
         'validation_receipt':(ROOT/'measurements'/'handoff_validation.json').as_posix()}
(ROOT/'RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
status=(ROOT/'STATUS.md').read_text(encoding='utf-8')
assert status.splitlines()[0]=='STATE: WORKING'
status=status.replace('STATE: WORKING','STATE: NEEDS_REVIEW',1)
lines=status.splitlines()
lines=[('NEXT: w347 blind-checks AUDIT_REQUEST_w347.json; manager applies kept material after the full P0209 proof check.' if line.startswith('NEXT:') else line) for line in lines]
lines.append('2026-10-10: Completed ten reports, twenty typed nodes, thirty-four quoted edges and two local hook proposals. All mathematical checks and handoff validation passed; blinded review and deployment remain pending. REPORT.md, RUN_RECEIPT.json and both live-path diffs are saved.')
(ROOT/'STATUS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','report':(ROOT/'REPORT.md').as_posix(),
                  'bundle':(ROOT/'bundles'/'bundle_001.json').as_posix(),'blind_audit':'PENDING'}))
