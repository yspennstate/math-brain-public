"""Render the actual execution ledger as a navigable research report index."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return re.sub(r'\s+', ' ', str(value)).replace('|', '\\|')


def main():
    agents = json.loads((ROOT / 'execution_ledger.json').read_text())['agents']
    complete = sum(a['status'] == 'completed' for a in agents)
    interrupted = sum(a['status'] == 'interrupted' for a in agents)
    lines = ['# Actual agent execution and report index', '',
             f'Actual distinct agents launched: **{len(agents)}/100**. '
             f'Completed reports: **{complete}/100**. '
             f'Interrupted sessions: **{interrupted}** (excluded from completed reviews).', '',
             'Every recorded agent uses `gpt-6-astra` with `reasoning_effort=max`. '
             'Agents run in batches under the concurrency limit. Follow-up turns '
             'are not counted as additional agents. These are execution counts, '
             'not counts of solved open problems.', '',
             'Each numbered report preserves its precise hypotheses, proof or '
             'counterexample, tests, sources, and remaining obligations. A later '
             'audit can qualify an earlier report; read the consolidated '
             '[claim ledger](CLAIM_LEDGER.md) and coordinator [011](agents/011.md) '
             'alongside the original reports.', '',
             '| Agent | Status | Report | Recorded result or assignment |',
             '|---|---|---|---|']
    for agent in sorted(agents, key=lambda a: int(a['number'])):
        number = agent['number']
        path = ROOT / agent['report_path']
        title = ''
        if path.is_file():
            title = next((s.lstrip('# ').strip() for s in path.read_text().splitlines()
                          if s.startswith('# ')), '')
        if not title:
            title = agent.get('assigned_task', agent['task_name'].rsplit('/', 1)[-1])
        summary = agent.get('result', agent.get('assigned_task', 'See complete report.'))
        report = f'[{cell(title)}]({agent["report_path"]})' if path.is_file() else cell(title)
        lines.append(f'| {number} | {cell(agent["status"])} | {report} | {cell(summary)} |')
    lines += ['', 'The machine-readable [execution ledger](execution_ledger.json) '
              'retains the actual task identities, model settings, assignments, '
              'completion states, and available provenance. The '
              '[archive manifest](ARCHIVE_MANIFEST.json) binds the final source '
              'and report bytes with SHA-256 and Git blob hashes.', '']
    (ROOT / 'AGENT_INDEX.md').write_text('\n'.join(lines))
    print(json.dumps({'launched': len(agents), 'completed': complete,
                      'index': str(ROOT / 'AGENT_INDEX.md')}))


if __name__ == '__main__':
    main()
