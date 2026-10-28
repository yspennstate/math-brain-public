"""Actual helper integration controls, all source fixtures reviewed in this file."""
import datetime as dt
import hashlib
import json
from lean_target_check import check_source
from run_component_pilot import ROOT, guard

CASES = [
    ('closed', 'theorem Checked : True := by trivial\n', 'Checked', False, 'FORMAL_TARGET_VERIFIED'),
    ('admitted', 'theorem Admitted : False := by sorry\n', 'Admitted', False, 'ADMITTED_TARGET'),
    ('custom_axiom', 'axiom Unsupported : False\ntheorem Dependent : False := Unsupported\n', 'Dependent', False, 'UNAPPROVED_AXIOMS'),
    ('number', 'def Number : Nat := 7\n', 'Number', False, 'TARGET_KIND_UNSUPPORTED'),
    ('namespaced', 'namespace Receipt\ntheorem Named : True := by trivial\nend Receipt\n', 'Receipt.Named', False, 'FORMAL_TARGET_VERIFIED'),
    ('anonymous', 'example : 2 + 3 = 5 := by rfl\n', None, False, 'COMPILED_NO_NAMED_TARGET'),
    ('false', 'theorem Incorrect : (1 : Nat) = 2 := by rfl\n', 'Incorrect', False, 'COMPILE_FAILED'),
    ('mathlib', 'import Mathlib.Tactic.NormNum\ntheorem MathlibChecked : (2 : Rat)^3 = 8 := by norm_num\n', 'MathlibChecked', True, 'FORMAL_TARGET_VERIFIED'),
]


def main():
    rows = []
    result_path = ROOT / 'LEAN_HELPER_INTEGRATION_RESULTS.json'
    if result_path.exists():
        raise RuntimeError('Preserve completed evidence; do not overwrite it')
    for label, source, target, mathlib, expected in CASES:
        raw = source.encode('utf-8')
        print('HELPER_CONTROL_START', label, flush=True)
        receipt = check_source(raw, target=target, reviewed_sha256=hashlib.sha256(raw).hexdigest(),
                               use_mathlib=mathlib)
        passed = receipt['result']['status'] == expected
        rows.append({'case': label, 'expected_status': expected, 'control_pass': passed, 'receipt': receipt})
        guard(str(result_path))
        result_path.write_text(json.dumps({'as_of': dt.datetime.now(dt.timezone.utc).isoformat(),
                                          'complete': len(rows) == len(CASES), 'rows': rows,
                                          'all_controls_pass': len(rows) == len(CASES) and all(r['control_pass'] for r in rows)},
                                         indent=2) + '\n', encoding='utf-8')
        print('HELPER_CONTROL_RESULT', label, receipt['result']['status'], passed, flush=True)


if __name__ == '__main__':
    main()
