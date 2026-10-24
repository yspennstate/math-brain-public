"""Record root-observed successful launches and actual completion notifications.

Read one JSON request from stdin. This is bookkeeping, not an agent launcher or
a mathematical acceptance mechanism. A completion must already have been
observed through the collaboration service before invoking this command.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    request = json.load(sys.stdin)
    path = ROOT / 'execution_ledger.json'
    ledger = json.loads(path.read_text())
    agents = ledger['agents']
    now = datetime.now(timezone.utc).isoformat()
    for event in request.get('register', []):
        number = str(event['number']).zfill(3)
        if int(number) != len(agents) + 1 or int(number) > 100:
            raise ValueError('Registration must be the next actual launch, up to100')
        if any(a['task_name'] == event['task_name'] for a in agents):
            raise ValueError('This actual agent identity is already counted')
        agents.append({'number': number, 'task_name': event['task_name'],
                       'model': 'gpt-6-astra', 'reasoning_effort': 'max',
                       'report_path': f'agents/{number}.md',
                       'assigned_task': event['assigned_task'], 'status': 'running',
                       'source': 'Root observed a successful collaboration.spawn_agent response.',
                       'registered_utc': now})
    for event in request.get('complete', []):
        number = str(event['number']).zfill(3)
        agent = next(a for a in agents if a['number'] == number)
        report = ROOT / agent['report_path']
        if agent['status'] == 'completed':
            raise ValueError('Completion is already recorded: ' + number)
        if not report.is_file() or report.stat().st_size < 100:
            raise ValueError('No substantive completed report exists: ' + number)
        agent.update(status='completed', immutable=True, result=event['result'],
                     completed_utc=now,
                     immutable_report_sha256=hashlib.sha256(report.read_bytes()).hexdigest())
    for event in request.get('interrupt', []):
        number = str(event['number']).zfill(3)
        agent = next(a for a in agents if a['number'] == number)
        if agent['status'] != 'running':
            raise ValueError('Only an unfinished actual launch can be interrupted')
        report = ROOT / agent['report_path']
        if not report.is_file() or report.stat().st_size < 100:
            raise ValueError('An explicit interruption record is required')
        agent.update(status='interrupted', immutable=True, result=event['result'],
                     completed_utc=now, report_author='/root',
                     immutable_report_sha256=hashlib.sha256(report.read_bytes()).hexdigest())
    ledger['actual_successful_spawns_recorded'] = len(agents)
    ledger['actual_completed_agents'] = sum(a['status'] == 'completed' for a in agents)
    ledger['actual_interrupted_agents'] = sum(a['status'] == 'interrupted' for a in agents)
    if 'completed_worker_reports' in ledger:
        ledger['coordinator_completed_children_at_handoff'] = ledger.pop('completed_worker_reports')
    if 'requested_additional_workers' in ledger:
        ledger['original_plan_coordinator_additional_workers'] = ledger.pop('requested_additional_workers')
    ledger['total_active_agent_cap_including_root'] = 7
    ledger['worker_concurrency_cap'] = 6
    ledger['updated'] = now
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(ledger, indent=2) + '\n')
    temporary.replace(path)
    print(json.dumps({'launched': len(agents),
                      'completed': ledger['actual_completed_agents'],
                      'interrupted': ledger['actual_interrupted_agents'],
                      'active': [a['number'] for a in agents if a['status'] == 'running']}))


if __name__ == '__main__':
    main()
