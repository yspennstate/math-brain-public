"""Finish local hooks, unified diffs and reviewer commands; no live writes."""
from pathlib import Path
import datetime
import difflib
import json

root = Path(__file__).resolve().parent
bundle = json.loads((root/'bundle_001.json').read_text(encoding='utf-8'))
hooks = [
 dict(id='open-problems-w338-01',area='math',event='stage-start',
      cue=r'(?i)(rare.event|condition\w*.{0,25}surviv).{0,50}(limit|converg|scal)',
      fire_when='C0077: an unconditioned scaling limit plus exact one-arm probability is proposed as sufficient for the conditioned limit.',
      silent_when='A joint bounded-continuous-test asymptotic or the conditional limit has already been proved.',
      text='For a rare-event conditioned limit, check joint test expectations at the event-probability scale. An exact survival denominator and an unconditioned limit alone leave the conditional law uncontrolled.',
      evidence='~/brain_workers/w338/PROOFS.md C0077; special_case_measurements.json: exact n*P(A_n)=1, alternating conditional point masses.',
      proposer='w338'),
 dict(id='open-problems-w338-02',area='math',event='stage-start',
      cue=r'(?i)(iterated|recursive).{0,30}3.majority.{0,80}(revealment|greedy)',
      fire_when='C0021: the greedy (5/6)^k revealment is reused as the best achieved construction without testing interleaving.',
      silent_when='The problem is an arbitrary majority function or the depth-two policy and composition have already been checked.',
      text='For iterated 3-majority, try exact small-block query optimization. The author-checked depth-two certificate gives 131/192 revealment; audit its Bellman certificate and composition before promoting the bound.',
      evidence='~/brain_workers/w338/majority_measurements.json: 19,683 states, cost 393/64 versus 25/4, zero certificate errors; independent audit pending.',
      proposer='w338')]
for h in hooks:
    assert len(h['text'])<=300
(root/'hook-proposals.jsonl').write_text(''.join(json.dumps(h)+'\n' for h in hooks),encoding='utf-8')
patches = root/'patches'
patches.mkdir(exist_ok=True)
for filename,target,output in [
 ('bundle_001.json','math-brain-inbox/w338/bundle_001.json','01_math_bundle.diff'),
 ('hook-proposals.jsonl','primary_directive/hooks1000/proposals/open-problems-w338.jsonl','02_hooks.diff')]:
    after = (root/filename).read_text(encoding='utf-8').splitlines(keepends=True)
    diff = ''.join(difflib.unified_diff([],after,fromfile='a/'+target,tofile='b/'+target))
    (patches/output).write_text(diff,encoding='utf-8')
index = [dict(entry_key=e['key'],problem_id=e['key'].split('-')[1].upper(),
              logical_id=f"math:{e['namespace']}:{e['logical_name']}",audit='PENDING_W346')
         for e in bundle['entries']]
(root/'ROW_INDEX.json').write_text(json.dumps(index,indent=2),encoding='utf-8')
handoff = f'''The ten-problem batch contains {len(bundle['entries'])} draft nodes and {len(bundle['relations'])} quoted edges. All await w346 KEEP. The draft publication receipt is delivery_receipt.json; it confirms staging, not integration.

Auditor packet: ~/brain_workers/w338/AUDIT_REQUEST_w346.md
Draft: ~/math-brain-inbox/w338/bundle_001.json
Evidence and measurements: ~/brain_workers/w338/REPORT.md
Verdicts should be saved by w346 in its own folder, then used by the reviewer.

Progress command for a peer authorized to write the progress page (not run by this worker):
python -X utf8 ~/primary_directive/pd_progress.py --event "w338: 10 problems; 11 draft nodes; 22 quoted edges; C0021 exact finite cost 393/64 versus 25/4; w346 audit pending" --agent w338 --row S1.O.w338.004 --evidence ~/math-brain-inbox/w338/bundle_001.json

IDs/counts/paths-only team notice, to be posted only by an authorized peer:
w338; 10; 11; 22; ~/math-brain-inbox/w338/bundle_001.json; w346; KEEP=0.

Hook proposals are local review artifacts, with the target path in patches/02_hooks.diff. They require the hook pipeline's audits before landing.

NEXT: w346 audits ROW_INDEX.json entry keys; reviewer integrates kept nodes and edges, records acceptance, and returns fixes.
'''
(root/'HANDOFF.md').write_text(handoff,encoding='utf-8')
receipt = dict(agent='w338',team='O',finished_local=datetime.datetime.now().astimezone().isoformat(),
               problems=10,unique_nodes=len(index),quoted_edges=len(bundle['relations']),
               result_rows=len((root/'results.jsonl').read_text(encoding='utf-8').splitlines()),
               hook_proposals=2,auditor='w346',auditor_keeps=0,promoted_solutions=0,
               recall='timed out after 60 seconds',
               memory_fallback_slug='fei_opus_wave1_reduction_small_influences_gates_and_ltf_2026_09_23',
               lean='SETUP_UNVERIFIED: compute governor refusal',
               token_usage='Not exposed by this session; no estimate claimed',
               live_store_writes=0,mesh_sends=0,network_requests=0,test_material_opened=0)
(root/'WORK_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(dict(local_artifacts='READY',nodes=len(index),edges=len(bundle['relations']),hooks=2),indent=2))
