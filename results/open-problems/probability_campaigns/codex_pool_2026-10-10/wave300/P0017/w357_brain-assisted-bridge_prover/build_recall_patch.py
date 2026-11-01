"""Produce and apply a narrowly scoped diff in the worker's private clone."""
from __future__ import annotations

import difflib
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LIVE = Path("~/math-brain-build/src/math_brain/cli.py")
TARGET = ROOT / "repo/src/math_brain/cli.py"
snapshot = ROOT / "snapshot"
snapshot.mkdir(exist_ok=True)
original = LIVE.read_text(encoding="utf-8")
(snapshot / "cli.py").write_text(original, encoding="utf-8")
TARGET.write_text(original, encoding="utf-8")
assert "--with-statements" not in original, "live source already has the proposed option; reassess instead of duplicating"


def once(text, old, new):
    assert text.count(old) == 1, "source anchor changed; stop for a fresh review"
    return text.replace(old, new, 1)


changed = once(original, '    recall.add_argument("--limit", type=int, default=10)\n',
               '    recall.add_argument("--limit", type=int, default=10)\n'
               '    recall.add_argument(\n'
               '        "--with-statements",\n'
               '        action="store_true",\n'
               '        help="include each selected card\'s complete statement and stored review "\n'
               '        "provenance for checking theorem hypotheses",\n'
               '    )\n')
helper = '''def _include_recall_statements(output, hits, enabled: bool) -> None:
    """Expose complete selected statements without promoting their review status."""
    if not enabled:
        return
    nodes = {hit.node.id: hit.node for hit in hits}
    rows = output if isinstance(output, list) else output["hits"]
    for row in rows:
        node = nodes[row["id"]]
        row["statement"] = node.body
        row["statement_provenance"] = {
            "logical_id": node.metadata.get("logical_id"),
            "truth_status": node.metadata.get("truth_status"),
            "statement_fidelity_reviewed": node.metadata.get("statement_fidelity_reviewed"),
        }


'''
changed = once(changed, "def _decision_json(result) -> dict:\n", helper+"def _decision_json(result) -> dict:\n")
changed = once(changed, '                output["background"] = _background_json(result)\n',
               '                output["background"] = _background_json(result)\n'
               '                _include_recall_statements(output, result.hits, args.with_statements)\n')
changed = once(changed, '                print(json.dumps(_decision_json(result), ensure_ascii=False))\n',
               '                output = _decision_json(result)\n'
               '                _include_recall_statements(output, result.hits, args.with_statements)\n'
               '                print(json.dumps(output, ensure_ascii=False))\n')
old_plain = '''        print(
            json.dumps(
                [
                    {
                        "id": hit.node.id,
                        "kind": hit.node.kind.value,
                        "title": hit.node.title,
                        "score": hit.total_score,
                        "warning_score": hit.warning_score,
                    }
                    for hit in hits
                ],
                ensure_ascii=False,
            )
        )
'''
new_plain = '''        output = [
            {
                "id": hit.node.id,
                "kind": hit.node.kind.value,
                "title": hit.node.title,
                "score": hit.total_score,
                "warning_score": hit.warning_score,
            }
            for hit in hits
        ]
        _include_recall_statements(output, hits, args.with_statements)
        print(json.dumps(output, ensure_ascii=False))
'''
changed = once(changed, old_plain, new_plain)
compile(changed, str(TARGET), "exec")
patch_dir = ROOT / "patches"
patch_dir.mkdir(exist_ok=True)
diff = "".join(difflib.unified_diff(original.splitlines(True), changed.splitlines(True),
                                  fromfile="a/~/math-brain-build/src/math_brain/cli.py",
                                  tofile="b/~/math-brain-build/src/math_brain/cli.py"))
patch = patch_dir / "01_recall_full_statements.diff"
patch.write_text(diff, encoding="utf-8")
command = ["git", "-C", str(ROOT/"repo"), "apply", "-p5", "--check", str(patch)]
check = subprocess.run(command, capture_output=True, text=True, timeout=60)
assert check.returncode == 0, check.stderr
apply = subprocess.run(["git", "-C", str(ROOT/"repo"), "apply", "-p5", str(patch)],
                       capture_output=True, text=True, timeout=60)
assert apply.returncode == 0, apply.stderr
receipt = {"live_file":str(LIVE), "baseline_sha256":hashlib.sha256(original.encode()).hexdigest(),
           "patch":str(patch), "apply_check_command":command, "apply_check_exit":check.returncode,
           "private_clone_apply_exit":apply.returncode, "live_file_changed":False,
           "note":"The source digest binds an engineering baseline; it is not mathematical proof evidence."}
(ROOT / "PATCH_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n", encoding="utf-8")
print("Scoped patch syntax and apply check passed in the private clone.")
