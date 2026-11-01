import json
import runpy
from pathlib import Path

root=Path(__file__).resolve().parent
runpy.run_path(str(root/'research.py'),run_name='__main__')
runpy.run_path(str(root/'validate_package.py'),run_name='__main__')
rows=json.loads(root.joinpath('source_rows.json').read_text(encoding='utf-8'))
mapping=json.loads(root.joinpath('entry_problem_map.json').read_text(encoding='utf-8'))
statuses=[]
for pid in ('P0267','C0031','C0134','P0092','P0439','C0040','C0079','C0122','P0011','P0037'):
    source=next(r for r in reversed(rows) if r['row'].get('problem_id')==pid and r['row'].get('statement'))
    attempts=[r['row'].get('attempt_id') for r in rows if r['row'].get('problem_id')==pid and r['row'].get('attempt_id')]
    statuses.append({'problem_id':pid,'present_status':'UNVERIFIED: offline cache does not certify present openness',
        'historical_status':source['row'].get('historical_status'),'statement':source['row']['statement'],
        'primary_source_id':source['row']['source_id'],'locator':source['row']['locator'],
        'prior_attempts_read':attempts,'new_entry_keys':[key for key,val in mapping.items() if val==pid],
        'full_problem_solved':False,'audit_status':'PENDING w347',
        'scope_note':('General numbered Problem 5 has a source-matched candidate counterexample; scoped independent KEEP required.' if pid=='P0267' else
                      'Forward implication is answered by Drewitz-Ramirez Corollary 2.15; cached open content is the converse.' if pid=='C0040' else
                      'Bounded-density case is already answered by Bordenave-Chafai Theorem 6.2, printed page 39; unrestricted upgrade remains unverified.' if pid=='C0031' else
                      'Checked special case, necessary condition, or failed-route diagnostic; no full solution claimed.')})
root.joinpath('problem_status.json').write_text(json.dumps(statuses,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
valid=json.loads(root.joinpath('validation.json').read_text(encoding='utf-8'))
event={'agent':'w339','row':'S1.O.w339.002','event':f'10 problems checked; {valid["entries"]} draft claims with {valid["relations"]} quoted relations staged; BK 114640 checks pass; w347 review pending.',
       'evidence':'~/brain_workers/w339/REPORT.md',
       'reviewer_post_command':f'python -X utf8 ~/primary_directive/pd_progress.py --event "w339: 10 problems checked; {valid["entries"]} claims staged; BK 114640 controls pass; independent audit pending" --agent w339 --row S1.O.w339.002 --evidence ~/brain_workers/w339/REPORT.md',
       'staged_only_reason':'COMMON.md permits w339 to write only inside its folder; reviewer posts the receipt and stages the inbox draft.'}
root.joinpath('progress_event.json').write_text(json.dumps(event,indent=2)+'\n',encoding='utf-8')
