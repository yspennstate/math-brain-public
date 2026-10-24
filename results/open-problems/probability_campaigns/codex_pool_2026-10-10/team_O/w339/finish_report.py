import json
from pathlib import Path

root=Path(__file__).resolve().parent
validation=json.loads(root.joinpath('validation.json').read_text(encoding='utf-8'))
measure=json.loads(root.joinpath('measurements.json').read_text(encoding='utf-8'))
assert validation['valid'] and measure['completed']
assert validation['entries']==16 and validation['relations']==38
assert validation['keeps_received']==0
lean_command=json.loads(root.joinpath('lean_command.json').read_text(encoding='utf-8'))
lean_output=root.joinpath('lean_receipt.json').read_text(encoding='utf-8')
assert lean_command['returncode']==2 and 'SETUP_UNVERIFIED' in lean_output
root.joinpath('lean_status.json').write_text(json.dumps({
    'status':'SETUP_UNVERIFIED','certificate':False,
    'reason':'Compute status is distressed or unknown',
    'scope':'attempted final BK algebra inequality only; no Lean claim for any mathematical entry',
    'raw_stdout_file':'lean_receipt.json','command_file':'lean_command.json',
    'source_file':'BKCore.lean'},indent=2)+'\n',encoding='utf-8')

report=f'''Checked the ten assigned problems and saved {validation['entries']} draft nodes, {validation['relations']} quoted relations, 17 stable result rows, and four narrow hook proposals. This is a proposal for the live brain until independent review and deployment; no recall improvement or open-problem solution is claimed. The current literature status is unverified outside the examined offline cache.

The main proof is BK for every co-singleton omission law, hence all increasing events for weighted connected unicyclic spanning trees. P0267's earlier reciprocal-BES(4) candidate survived an independent calculation of the Ito constants, finite-horizon minimum tail, scalar theorem assumptions, and the endpoint-norm failure; it still requires w347's full proof KEEP. Other nodes cover reset-automaton endogeny through criticality, SLO capacity bounds, a one-dimensional invariant density, and explicit failed-route controls. The source already answers C0031 with bounded density (Bordenave-Chafai Theorem 6.2, printed p.39) and C0040's forward implication (Drewitz-Ramirez Corollary 2.15). C0079's bond-pivotal +1 and C0122's signed-Markov inference are invalid.

Command: python -X utf8 ~/brain_workers/w339/check_math.py. All controls passed in {measure['elapsed_seconds']:.3f} seconds: 114640 exact integer BK comparisons, 371 connected-graph cases, 12 queue convolutions (maximum error 7.29e-17), eight exact invariant-density identities, and Bessel, dependency-tree, Gaussian, and SIR controls. The staffing diagnostic changed 3 servers using waiting alone to 4 using response time; the response miss rates are 0.050877 and 0.021443 for target 0.03 at lambda=2, mu=1, deadline=4. Numerical controls do not replace the displayed analytic proofs.

Command: python -X utf8 ~/brain_workers/w339/finalize.py. The final draft passed required-field, kind, license-prefix, acyclic-dependency, existing-target, exact-both-end-quotation, and 4 fire/4 silence checks. Two C0040 links initially quoted superseded A001; they now quote observed A002. The read-only live baseline contains {validation['proposed_logical_ids_already_live']} of these proposed logical IDs; {validation['entries']} are staged locally. A live after-run was not performed.

Lean returned SETUP_UNVERIFIED because compute status is distressed or unknown. The checked source, invocation, raw receipt, and normalized status are preserved; no Lean certificate is claimed. Important limits: the BK result needs co-singleton support; the automaton result uses reset innovations; the SIR diagnostic uses fixed contacts; the C0134 bound concerns infinite uniformly biased stacks. They do not solve the general questions. All {validation['entries']} claims await w347; zero KEEP verdicts have been received.

Apply: the reviewer uses patches/01_w339_brain_bundle.diff to stage drafts/bundle_001.json at ~/math-brain-inbox/w339/bundle_001.json.part and atomically rename it to .json after scoped KEEP verdicts, then uses the normal integrator. patches/02_w339_hook_proposals.diff stages the four proposals for paired hook audit. No live integrator or send command was run by w339 under COMMON.md's write restriction. REVIEW_REQUEST.md is the local auditor handoff; progress_event.json contains the exact progress-post command for the reviewer.

NEXT: w347 checks the 16 claims independently; the reviewer stages kept entries, binds verdicts, and measures recall after integration.
'''
root.joinpath('REPORT.md').write_text(report,encoding='utf-8')
old=root.joinpath('STATUS.md').read_text(encoding='utf-8').splitlines()
log='\n'.join(line for line in old[2:] if line.strip())
status=f'''STATE: NEEDS_REVIEW
NEXT: w347 independently audits the 16 claims; reviewer stages kept entries and measures recall after integration.

{log}
2026-10-10: Source-matched C0031 bounded-density special case added; final package has 16 nodes and 38 relations, 17 stable result rows, four validated hook proposals, two reviewer patches, and a local blind-audit request. C0040 quotations now bind to the observed superseding A002. Final schema/target/quote/acyclic/license/control validation passed. All math controls passed. No KEEP or live improvement claimed; session deliverables ready for review.
'''
root.joinpath('STATUS.md').write_text(status,encoding='utf-8')
print(json.dumps({'state':'NEEDS_REVIEW','entries':validation['entries'],'relations':validation['relations'],
                  'result_rows':len(root.joinpath('results.jsonl').read_text(encoding='utf-8').splitlines()),
                  'hooks':validation['hooks'],'auditor':'w347','keeps':0,'report':str(root/'REPORT.md')}))
