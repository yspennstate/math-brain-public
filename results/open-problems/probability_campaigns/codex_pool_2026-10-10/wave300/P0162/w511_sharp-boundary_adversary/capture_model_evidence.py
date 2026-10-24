"""Extract only session/model metadata with rg; never read profiles or credentials."""
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

base = Path(__file__).resolve().parent
thread = os.environ.get('CODEX_THREAD_ID')
codex_home = Path(os.environ.get('CODEX_HOME', '~/.codex-img-acc2'))
day = codex_home / 'sessions' / '2026' / '10' / '10'
paths = list(day.glob(f'*{thread}*.jsonl')) if thread else []
result = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'agent': 'w511', 'thread_id': thread,
    'lookup_scope': 'Exact native thread file in the named session day; model metadata only.',
    'account_home': str(codex_home),
    'account_identity': 'UNVERIFIED; account-home name is not authenticated login evidence.',
    'served_model': 'UNVERIFIED',
    'response_side_model_fields': [], 'configuration_model_fields': [],
    'referee_served_model': 'UNVERIFIED; request exact evidence from w512/integration contact.',
}
pattern = r'"(?:type|role|model|model_provider|reasoning_effort|effort|id|cwd)"\s*:\s*"[^"\r\n]*"'
if len(paths) != 1:
    result['error'] = f'Expected one exact thread file; found {len(paths)}.'
else:
    path = paths[0]
    result['transcript_path'] = str(path)
    run = subprocess.run(['rg', '-n', '-o', pattern, str(path)],
                         capture_output=True, encoding='utf-8', timeout=30)
    result['command'] = run.args
    if run.returncode not in (0, 1):
        result['error'] = run.stderr.strip()
    else:
        lines = {}
        for matched in run.stdout.splitlines():
            number, field = matched.split(':', 1)
            try:
                data = json.loads('{' + field + '}')
            except json.JSONDecodeError:
                continue
            lines.setdefault(int(number), []).extend(data.items())
        result['assistant_metadata_rows_seen'] = sum(
            ('role', 'assistant') in fields for fields in lines.values())
        for number, fields in lines.items():
            models = [value for key, value in fields if key == 'model']
            if not models:
                continue
            record = {'line': number, 'models': models,
                      'types': [value for key, value in fields if key == 'type'],
                      'roles': [value for key, value in fields if key == 'role']}
            if ('role', 'assistant') in fields or ('type', 'assistant') in fields:
                result['response_side_model_fields'].append(record)
            else:
                result['configuration_model_fields'].append(record)
        values = sorted({model for row in result['response_side_model_fields'] for model in row['models']})
        if values:
            result['served_model'] = values
        else:
            result['limitation'] = 'No assistant response-side model field observed; context/configuration fields do not certify the served model.'
out = base / 'MODEL_EVIDENCE.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'evidence': str(out), 'served_model': result['served_model'],
                  'assistant_metadata_rows_seen': result.get('assistant_metadata_rows_seen', 0),
                  'response_side_model_fields': len(result['response_side_model_fields']),
                  'configuration_model_fields': len(result['configuration_model_fields'])}))
