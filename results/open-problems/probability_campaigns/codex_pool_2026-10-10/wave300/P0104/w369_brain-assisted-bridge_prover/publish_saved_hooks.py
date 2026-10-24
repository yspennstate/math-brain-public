"""Publish only the two evidence-backed proposals requested by the resume contract."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = Path('~/primary_directive/hooks1000/proposals/math-w369.jsonl')
assert TARGET.parent.resolve() == Path('~/primary_directive/hooks1000/proposals').resolve()
assert TARGET.parent.is_dir()
hooks = [json.loads(line) for line in (ROOT / 'HOOK_PROPOSALS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
hooks[0]['text'] = 'Check the implication direction: uniform interval mass <=1-epsilon at length L implies Var(X)>=epsilon L^2/4 for square-integrable X. A variance lower bound alone can come from rare tails.'
hooks[0]['evidence'] = '~/brain_workers/w369/math_retrieval.json:claim_3ccc6fc493b4e17b5c29966949004f575c51205c8a4f0ba3bc516d0b752ebea4; REVIEW_RECEIPTS.json:w369-l0'
hooks[1]['evidence'] = '~/brain_workers/w369/MEASUREMENTS.json:log_n=192, TV=1.2664e-14, variance/n^(2/3)=1.5161e16; REVIEW_RECEIPTS.json:w369-l3,w369-l4'
fields = {'id','area','event','cue','fire_when','silent_when','text','evidence','proposer'}
for hook in hooks:
    assert set(hook) == fields and hook['proposer'] == 'w369' and hook['area'] == 'math'
    assert len(hook['text']) <= 300 and hook['fire_when'] and hook['silent_when']
    assert hook['event'] in {'UserPromptSubmit','PreToolUse','PostToolUse','Stop','stage-start'}
(ROOT / 'HOOK_PROPOSALS.jsonl').write_text(''.join(json.dumps(hook,ensure_ascii=False)+'\n' for hook in hooks),encoding='utf-8')
existing = [json.loads(line) for line in TARGET.read_text(encoding='utf-8').splitlines() if line.strip()] if TARGET.exists() else []
existing_ids = {row['id'] for row in existing}
added = []
with TARGET.open('a',encoding='utf-8') as handle:
    for hook in hooks:
        if hook['id'] not in existing_ids:
            handle.write(json.dumps(hook,ensure_ascii=False)+'\n')
            handle.flush()
            added.append(hook['id'])
readback = {row['id']:row for row in [json.loads(line) for line in TARGET.read_text(encoding='utf-8').splitlines() if line.strip()]}
assert all(hook['id'] in readback for hook in hooks)
receipt = {
    'path': str(TARGET),
    'proposal_ids': [hook['id'] for hook in hooks],
    'newly_added': added,
    'text_character_counts': [len(hook['text']) for hook in hooks],
    'readback_confirmed': True,
    'audited': False,
    'implemented': False,
    'authorization': 'Latest resume contract explicitly requests this proposals/<area>-<you>.jsonl output; live controls unchanged',
}
(ROOT / 'HOOK_PUBLICATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
