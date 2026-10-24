"""Reviewer-only application of an approved new-file unified diff.

Default is read-only. This worker must not invoke --apply: its brief forbids live
writes. The reviewer uses --apply only after w346's full-proof KEEP is on disk.
"""
import argparse
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--problem',required=True)
parser.add_argument('--verdict-file',type=Path,required=True)
parser.add_argument('--apply',action='store_true')
args=parser.parse_args()
manifest=json.loads((ROOT/'bundle_handoff.json').read_text(encoding='utf-8'))
item=next(x for x in manifest if x['problem_id']==args.problem)
verdict_path=args.verdict_file.resolve(strict=True)
auditor_root=Path('~/brain_workers/w346').resolve()
if not verdict_path.is_relative_to(auditor_root):
    raise SystemExit('The verdict must come from w346\'s own folder.')
if verdict_path.suffix.lower()=='.jsonl':
    verdicts=[json.loads(s) for s in verdict_path.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
else:
    payload=json.loads(verdict_path.read_text(encoding='utf-8-sig'))
    verdicts=payload if isinstance(payload,list) else payload.get('verdicts',[payload])
keeps=[v for v in verdicts if v.get('problem_id')==args.problem and v.get('verdict')=='KEEP' and v.get('auditor')=='w346' and v.get('proof_reviewed') is True]
if not keeps:
    raise SystemExit('Missing w346 KEEP with proof_reviewed=true for this full bundle.')
lines=(ROOT/item['patch_file']).read_text(encoding='utf-8').splitlines(keepends=True)
assert lines[0].rstrip()=='--- a/'+item['intended_live_path']
assert lines[1].rstrip()=='+++ b/'+item['intended_live_path']
hunk=re.fullmatch(r'@@ -0,0 \+1,(\d+) @@\n',lines[2])
assert hunk and len(lines)-3==int(hunk.group(1))
assert all(line.startswith('+') for line in lines[3:])
contents=''.join(line[1:] for line in lines[3:])
assert contents==(ROOT/item['bundle_file']).read_text(encoding='utf-8')
target=Path(item['intended_live_path']).resolve()
intended_root=Path('~/math-brain-inbox/w342').resolve()
assert target.is_relative_to(intended_root)
if not args.apply:
    print('READY (read-only): '+str(target))
elif target.exists():
    if target.read_text(encoding='utf-8')!=contents:
        raise SystemExit('Existing live file differs; refusing to overwrite it.')
    print('ALREADY STAGED: '+str(target))
else:
    target.parent.mkdir(parents=True,exist_ok=True)
    part=target.with_suffix('.part')
    with part.open('x',encoding='utf-8',newline='\n') as handle:
        handle.write(contents)
    part.rename(target)
    print('STAGED: '+str(target))
