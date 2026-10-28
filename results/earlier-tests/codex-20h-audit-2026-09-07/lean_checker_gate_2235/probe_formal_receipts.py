"""Bounded actual-compiler controls; all source fixtures are manually reviewed."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import subprocess
import time
from formal_receipt import classify
from windowless_job import run
from solver_probe import pressure_check
from run_component_pilot import guard, ROOT

LEAN = Path.home()/'.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean.exe'
CASES = [
    ('closed', 'ProbeClosed', 'theorem ProbeClosed (n : Nat) : n + 0 = n := by rfl\n#print axioms ProbeClosed\n', 'FORMAL_TARGET_VERIFIED'),
    ('admitted', 'ProbeAdmitted', 'theorem ProbeAdmitted : False := by sorry\n#print axioms ProbeAdmitted\n', 'ADMITTED_TARGET'),
    ('custom_axiom', 'ProbeDependent', 'axiom PrivateAssumption : False\ntheorem ProbeDependent : False := PrivateAssumption\n#print axioms ProbeDependent\n', 'UNAPPROVED_AXIOMS'),
    ('unused_admission', 'ProbeIndependent', 'theorem UnusedAdmission : False := by sorry\ntheorem ProbeIndependent : True := by trivial\n#print axioms ProbeIndependent\n', 'FORMAL_TARGET_VERIFIED'),
    ('missing_target', 'ProbeMissing', '#check Nat\n', 'TARGET_EVIDENCE_MISSING_OR_AMBIGUOUS'),
]


def main():
    folder = ROOT/'formal_receipt_controls'
    guard(str(folder), 'topic:math-brain-20h-processes-20260907')
    folder.mkdir(exist_ok=False)
    pressure_check()
    version = run([str(LEAN), '--version'], cwd=ROOT, timeout=900)
    rows = []
    for label, target, source, expected in CASES:
        guard(str(folder))
        path = folder/(label+'.lean')
        path.write_text(source, encoding='utf-8')
        pressure_check()
        start = time.monotonic()
        def progress(event):
            print('FORMAL_RECEIPT_CONTROL', label, event['phase'], event.get('seconds', ''), flush=True)
            if event['phase'] == 'waiting':
                pressure_check()
        try:
            proc = run([str(LEAN), str(path)], cwd=ROOT, timeout=900, progress=progress)
            code, output, timeout = proc.returncode, proc.stdout+proc.stderr, False
        except subprocess.TimeoutExpired as exc:
            code, output, timeout = None, (exc.output or '')+(exc.stderr or ''), True
        result = classify(code, output, target=target, timed_out=timeout, source_reviewed=True)
        row = {'case': label, 'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
               'compiler_exit_code': code, 'compiler_output': output, 'result': result,
               'expected_status': expected, 'control_pass': result['status'] == expected,
               'legacy_would_call_this_PASS': code == 0 and 'error' not in output.lower(),
               'seconds': round(time.monotonic()-start, 3)}
        rows.append(row)
        guard(str(folder/(label+'.json')))
        (folder/(label+'.json')).write_text(json.dumps(row, indent=2)+'\n', encoding='utf-8')
        print('FORMAL_RECEIPT_RESULT', label, result['status'], row['control_pass'], flush=True)
    report = {'as_of': dt.datetime.now(dt.timezone.utc).isoformat(), 'compiler_version': version.stdout.strip(),
              'compiler_sha256': hashlib.sha256(LEAN.read_bytes()).hexdigest(), 'rows': rows,
              'all_controls_pass': all(row['control_pass'] for row in rows),
              'scope': 'Manually reviewed fixtures; stdout parsing is not an adversarial untrusted-source certificate',
              'production_deployed': False}
    guard(str(ROOT/'FORMAL_RECEIPT_RESULTS.json'))
    (ROOT/'FORMAL_RECEIPT_RESULTS.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'all_controls_pass': report['all_controls_pass'], 'compiler_version': report['compiler_version']}), flush=True)


if __name__ == '__main__':
    main()
