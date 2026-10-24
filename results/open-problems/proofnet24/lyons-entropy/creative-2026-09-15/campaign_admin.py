"""Local bookkeeping and text export for the explicitly requested campaign.

Run only with actual launch and completion observations from collaboration.
An assignment being listed or a report existing never counts as a completion.
"""
import argparse,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument('--launch',nargs='*',type=int,default=[])
p.add_argument('--complete',nargs='*',type=int,default=[])
p.add_argument('--interrupt',nargs='*',type=int,default=[])
p.add_argument('--restart',nargs='*',type=int,default=[])
p.add_argument('--export',action='store_true')
p.add_argument('--index',action='store_true')
a=p.parse_args()
ledger=json.loads((ROOT/'execution_ledger.json').read_text())
by_id={r['id']:r for r in ledger}
tasks={r['id']:r for r in json.loads((ROOT/'ASSIGNMENTS.json').read_text())}
for i in a.launch:
    id=f'C{i:03d}'
    if id in by_id:raise ValueError(f'Duplicate launch {id}')
    row={'id':id,'task':f'/root/creative{i:03d}',
         'model':'gpt-6-astra','reasoning_effort':'max','status':'running',
         'campaign':'2026-09-15-new-creative','method':tasks[id]['method']}
    ledger.append(row);by_id[id]=row
for i in a.interrupt:
    id=f'C{i:03d}';row=by_id[id]
    if row['status']!='running':raise ValueError(f'Not running: {id}')
    row.setdefault('attempts',[{'task':row['task'],'status':'running','model':row['model'],'reasoning_effort':row['reasoning_effort']}])
    row['attempts'][-1]['status']='interrupted_without_terminal_handoff'
    row['status']='interrupted'
    row['interruption_reason']='Worker unavailable after session transition; no terminal handoff received.'
for i in a.restart:
    id=f'C{i:03d}';row=by_id[id]
    if row['status']!='interrupted':raise ValueError(f'Not interrupted: {id}')
    task=f"/root/creative{i:03d}_resume{len(row['attempts'])}"
    row['attempts'].append({'task':task,'status':'running','model':row['model'],'reasoning_effort':row['reasoning_effort']})
    row['task']=task;row['status']='running'
for i in a.complete:
    id=f'C{i:03d}'
    if id not in by_id:raise ValueError(f'Unlaunched completion {id}')
    if not (ROOT/'agents'/f'{id}.md').is_file():raise ValueError(f'Missing report {id}')
    by_id[id]['status']='completed'
    if 'attempts' in by_id[id]:by_id[id]['attempts'][-1]['status']='completed'
for row in ledger:row['method']=tasks[row['id']]['method']
if a.launch or a.complete or a.interrupt or a.restart:
    (ROOT/'execution_ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
completed={r['id'] for r in ledger if r['status']=='completed'}
attempts=[a for row in ledger for a in row.get('attempts',[{'task':row['task'],'status':row['status']}])]
agent_launches=len({x['task'] for x in attempts})
summary={'launched':agent_launches,'execution_attempts':len(attempts),'assignments_launched':len(ledger),'interrupted_attempts':sum(x['status']=='interrupted_without_terminal_handoff' for x in attempts),'completed':len(completed),
         'running':[r['id'] for r in ledger if r['status']=='running']}
if a.export or a.index:
    status_path=ROOT/'CURRENT_STATUS.md'
    if status_path.exists():
        status=status_path.read_text()
        start='<!-- CAMPAIGN_COUNTS_START -->'
        end='<!-- CAMPAIGN_COUNTS_END -->'
        active=', '.join(summary['running']) or 'none'
        count_text='\n'.join([start,
            f"- Creative assignments completed with terminal handoffs: **{len(completed)}/100**.",
            f"- Distinct assignments launched: **{len(ledger)}/100**.",
            f"- Actual distinct agent launches: **{agent_launches}**; assignment execution attempts: **{len(attempts)}**; interrupted attempts without terminal handoffs: **{summary['interrupted_attempts']}**.",
            f'- Active assignments: {active}.',end])
        if start in status and end in status:
            status=status.split(start,1)[0]+count_text+status.split(end,1)[1]
        else:
            first=status.index('- Creative assignments completed')
            last=status.index('- All completed assignments',first)
            status=status[:first]+count_text+'\n'+status[last:]
        status_path.write_text(status)
    rows=['# Creative agent index','',f"Actual distinct agent launches: {agent_launches}. Assignment execution attempts: {len(attempts)}. Assignments launched: {len(ledger)}. Terminal completions: {len(completed)}. Interrupted attempts: {summary['interrupted_attempts']}. Planned assignments: 100.",'',
          '| ID | Method | Actual status | Full report |','|---|---|---|---|']
    for id,task in tasks.items():
        status=by_id[id]['status'] if id in by_id else 'planned; not launched'
        link=f'[report](agents/{id}.md)' if id in completed else ''
        rows.append(f'| {id} | {task["method"]} | {status} | {link} |')
    (ROOT/'AGENT_INDEX.md').write_text('\n'.join(rows)+'\n')
    files=[ROOT/n for n in ['TARGET.md','README.md','AGENT_INDEX.md','ASSIGNMENTS.json','execution_ledger.json','campaign_admin.py','publish_checkpoint.js']]
    files += [ROOT/'agents'/f'{id}.md' for id in sorted(completed)]
    for id in sorted(completed):
        files += [f for f in (ROOT/'computations'/id).rglob('*')
                  if f.is_file() and f.suffix in ['.py','.json','.md','.txt','.csv','.tex','.sage','.jl']]
    extra=[ROOT/n for n in ['PROGRESS.md','PRIOR_FRONTIER.md','sources/PRIOR_PARTIAL_RESULTS.md','FINAL_REPORT.md','CLAIM_LEDGER.md','ROOT_FISHER_IDENTITY.md','ROOT_STIELTJES.md','ROOT_LOW_DENSITY.md','ROOT_BLOCK_QUARTIC.md','ROOT_COUNT_LEAD.md','ROOT_PAIRWISE_CAUCHY.md','ROOT_GENERAL_DIAGONAL_CONE.md','ROOT_SHUFFLE_LEAD.md','ROOT_TWO_VALUE_LEAD.md','ROOT_UNITARY_GLUE_LEAD.md','ROOT_RANK_TWO_SPECTRAL.md','ROOT_PROJECTION_ENTROPY_LEAD.md','ROOT_RANK_TWO_SUPPORT.md','ROOT_RANK_ONE_BOUNDARY.md','ROOT_RANK_ONE_BOUNDARY_check.py','ROOT_RANK_ONE_BOUNDARY_results.json','ROOT_PROJECTION_BOUNDARY.md','ROOT_PROJECTION_BOUNDARY_results.json','ROOT_PROJECTION_ENTROPY_GLUE.md','ROOT_CONDITIONAL_SYMMETRIZATION.md'] if (ROOT/n).is_file()]
    extra += [f for f in ROOT.glob('ROOT_*') if f.is_file() and f.suffix in ['.md','.py','.json']]
    extra += [ROOT/'CURRENT_STATUS.md'] if (ROOT/'CURRENT_STATUS.md').exists() else []
    files += [f for f in (ROOT/'checkpoints').rglob('*') if f.is_file() and f.suffix in ['.py','.json','.md','.txt','.csv','.tex','.sage','.jl','.js','.ipynb']]
    files += [f for f in (ROOT/'recovery').rglob('*') if f.is_file() and f.suffix in ['.py','.json','.md','.txt','.csv','.tex','.sage','.jl']]
    files+=extra
    manifest={str(f.relative_to(ROOT)):{'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files}
    (ROOT/'ARCHIVE_MANIFEST.json').write_text(json.dumps({'counts':summary,'files':manifest},indent=2)+'\n')
    files.append(ROOT/'ARCHIVE_MANIFEST.json')
    if a.index:
        f=ROOT/'ARCHIVE_MANIFEST.json'
        manifest[f.name]={'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
        print(json.dumps({'counts':summary,'files':manifest}))
    else:
        print(json.dumps({str(f.relative_to(ROOT)):f.read_text() for f in files}))
else:print(json.dumps(summary))
