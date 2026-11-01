"""Add a cited local context only if the exact C0143 store target is absent."""
import json
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parent
cards=json.loads((ROOT/'cards.json').read_text(encoding='utf-8'))
if not any(c['problem_id']=='C0143' and c['kind']=='problem' for c in cards):
    export='~/math-brain-build/export/population/nodes.jsonl'
    found=subprocess.run(['rg','-n','-F','-e','open-problem-c0143-','-e','Open problem: Exponential decay of large finite clusters',export],capture_output=True,text=True,encoding='utf-8',check=False)
    assert found.returncode in (0,1),found.stderr
    for line in found.stdout.splitlines():
        number,raw=line.split(':',1)
        node=json.loads(raw)
        meta=json.loads(node.get('metadata_json') or '{}')
        logical=meta.get('logical_id','')
        if ':open-problem-c0143-' in logical:
            cards.append(dict(problem_id='C0143',logical_id=logical,kind='problem',title=node['title'],statement=node['body'],source_id=meta.get('source_id'),source_revision=meta.get('source_revision'),evidence_path=export,evidence_line=int(number)))
    if not any(c['problem_id']=='C0143' and c['kind']=='problem' for c in cards):
        ledger='~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl'
        found=subprocess.run(['rg','-n','-F','"problem_id": "C0143"',ledger],capture_output=True,text=True,encoding='utf-8',check=True)
        number,raw=found.stdout.strip().split(':',1)
        node=json.loads(raw)
        statement='CACHED QUESTION; current resolution not verified. For a transitive graph G, is the probability that a finite origin cluster has more than n graph-edge contacts with an infinite open cluster bounded by C_p exp(-c_p n) for every fixed p>p_c(G)? The cached intake attributes this to Pete, Conjecture 12.32, p.169, and leaves the possible unimodularity hypothesis unsettled. This context node records the question, not an accepted theorem or an up-to-date openness claim.'
        cards.append(dict(problem_id='C0143',logical_id=None,draft_target_key='c0143-question-context',kind='problem',title='C0143: exponential tail for finite-cluster contacts, cached question',statement=statement,source_id=node['source_id'],source_revision='cached-intake-2026-09-07-current-resolution-unverified',evidence_path=ledger,evidence_line=int(number)))
(ROOT/'cards.json').write_text(json.dumps(cards,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Problem contexts',sum(c['kind']=='problem' for c in cards),'existing',sum(c['kind']=='problem' and c['logical_id'] is not None for c in cards),'local',sum(c.get('draft_target_key') is not None for c in cards))
