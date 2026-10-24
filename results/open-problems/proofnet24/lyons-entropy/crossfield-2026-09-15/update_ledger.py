import json,sys
from datetime import datetime,timezone
from pathlib import Path

p=Path(__file__).resolve().parent
ledger=json.loads((p/'execution_ledger.json').read_text())
action=sys.argv[1]
for ident in sys.argv[2:]:
 row=next(r for r in ledger['assignments'] if r['id']==ident)
 if action=='launch':
  assert row['status']=='planned'
  row.update(status='running',task='/root/crossfield'+ident[1:],launched_utc=datetime.now(timezone.utc).isoformat())
 elif action=='complete':
  assert row['status']=='running'
  assert (p/'agents'/f'{ident}.md').is_file()
  row.update(status='completed',completed_utc=datetime.now(timezone.utc).isoformat(),report=f'agents/{ident}.md')
 else: raise ValueError(action)
rows=ledger['assignments']
ledger.update(launched=sum(r['status']!='planned' for r in rows),completed=sum(r['status']=='completed' for r in rows),active=sum(r['status']=='running' for r in rows),distinct_agent_tasks=len({r['task'] for r in rows if r['task']}),updated_utc=datetime.now(timezone.utc).isoformat())
(p/'execution_ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
(p/'README.md').write_text('# Creative cross-field Lyons entropy campaign\n\n'+f"**{ledger['launched']}/100 launched; {ledger['completed']}/100 completed; {ledger['active']} running.** These are actual execution counts. The full conjecture remains open.\n\n"+'The user requested 100 creative proof assignments and ongoing publication. No audit assignments are used. See [TARGET.md](TARGET.md) for the exact statement and name assumption, [FRONTIER.md](FRONTIER.md) for earlier results, and [execution_ledger.json](execution_ledger.json) for the execution record. Full derivations are saved in agents/ and supporting artifacts in computations/.\n\n## Assignments\n\n'+'\n'.join(f"- [{r['id']}](agents/{r['id']}.md): {r['topic']} — {r['status']}" if r['status']=='completed' else f"- {r['id']}: {r['topic']} — {r['status']}" for r in rows)+'\n')
print(json.dumps({k:ledger[k] for k in ['launched','completed','active','distinct_agent_tasks']}))
