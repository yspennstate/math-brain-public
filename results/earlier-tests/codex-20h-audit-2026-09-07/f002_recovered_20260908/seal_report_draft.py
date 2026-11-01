"""Capture validator output and seal the isolated report; no registration or deployment."""
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    out = HERE/'report_draft'
    report = out/'PARTIAL_PROOF_SCOPE_REPRODUCED_20260908.md'
    assert sha(report.read_bytes()) == 'a5ca8fab5f623e8bb376f451d07024a0918686b042441cbdb7f0c227f3f82a99'
    validator = Path.home()/'.codex/skills/audit-agent-fleet/scripts/validate_audit_report.py'
    completed = subprocess.run([sys.executable, '-B', str(validator), str(report)],
                               capture_output=True, timeout=60,
                               creationflags=subprocess.CREATE_NO_WINDOW | subprocess.BELOW_NORMAL_PRIORITY_CLASS)
    receipt = {'as_of': dt.datetime.now(dt.timezone.utc).isoformat(),
               'exit_code': completed.returncode, 'validator_sha256': sha(validator.read_bytes()),
               'report_sha256': sha(report.read_bytes()),
               'stdout': completed.stdout.decode('utf-8', errors='replace'),
               'stderr': completed.stderr.decode('utf-8', errors='replace'),
               'semantic_closure': False, 'windowless_creation_flags': True,
               'visible_window_census': 'NOT_PERFORMED_BY_THIS_LANE'}
    with (out/'VALIDATION.json').open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2)
    assert completed.returncode == 0
    scanner_path = Path.home()/'.claude/dreaming/scan_secrets.py'
    spec = importlib.util.spec_from_file_location('f002_report_scan', scanner_path)
    scanner = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = scanner
    spec.loader.exec_module(scanner)
    files = sorted(p for p in HERE.rglob('*') if p.is_file()
                   and '__pycache__' not in p.parts and p.name != 'primary_source_2608.23135v1.html')
    assert scanner.main([str(p) for p in files]) == 0
    manifest = {
        'schema': 'f002_report_draft_handoff.v1', 'as_of': dt.datetime.now(dt.timezone.utc).isoformat(),
        'report_sha256': sha(report.read_bytes()),
        'pins': {str(p.relative_to(HERE)): sha(p.read_bytes()) for p in files},
        'reviewed_file_set_scan': 'CLEAN',
        'publication_excluded': ['primary_source_2608.23135v1.html'],
        'publication_exclusion_reason': 'Full public HTML contains three unclassified key-like strings; exact relevant DOM fragments are clean and separately pinned.',
        'report_state': 'OPEN', 'sidecar_status': 'DRAFT_NOT_REGISTERED',
        'original_report_bytes': 'NOT_RECOVERED',
        'root_next': 'Review mathematical scope and evidence semantics, promote explicitly selected clean files, regenerate report paths/pins as needed, run validator, then register a superseding occurrence through canonical registrar in shared claim window. Never publish full raw HTML, fabricate original SHA, or call draft sidecar authoritative.',
        'brain_selfcare': 'Own wake remains degraded/unverified for correction-ingestion and stale orientation coverage; no credential rotation certification.',
        'rollback': 'No canonical writes made. Reject the proposed promotion if checks fail; retain the isolated evidence and failure history.'}
    with (out/'HANDOFF_REPORT.json').open('x', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    print(json.dumps({'handoff': str(out/'HANDOFF_REPORT.json'), 'sha256': sha((out/'HANDOFF_REPORT.json').read_bytes()), 'files': len(files)}))


if __name__ == '__main__':
    main()
