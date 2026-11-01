"""Create reviewable new-file diffs without writing outside the worker folder."""

from difflib import unified_diff
from pathlib import Path


root = Path(__file__).resolve().parent
patch_dir = root / "patches"
patch_dir.mkdir(exist_ok=True)
targets = [
    ("DRAFT_BUNDLE.json", "~/math-brain-inbox/w512/bundle_001.json", "01_bundle.diff"),
    ("HOOK_PROPOSALS.jsonl", "~/primary_directive/hooks1000/proposals/math-w512.jsonl", "02_hook.diff"),
]
for local_name, target, patch_name in targets:
    lines = (root / local_name).read_text(encoding="utf-8").splitlines(keepends=True)
    diff = "".join(unified_diff([], lines, fromfile=f"a/{target}",
                                tofile=f"b/{target}", lineterm="\n"))
    (patch_dir / patch_name).write_text(diff, encoding="utf-8")
    print(f"{patch_name}: {len(lines)} source lines -> {target}")
