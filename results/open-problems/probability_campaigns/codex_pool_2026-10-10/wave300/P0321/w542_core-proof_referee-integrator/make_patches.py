"""Make reviewable new-file diffs without touching live destinations."""

from difflib import unified_diff
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "patches"
OUT.mkdir(exist_ok=True)

for source_name, live_name, patch_name in [
    (
        "brain_bundle_001.json",
        "~/math-brain-inbox/w542/bundle_001.json",
        "01_brain_bundle.diff",
    ),
    (
        "HOOK_PROPOSAL.jsonl",
        "~/primary_directive/hooks1000/proposals/math-w542.jsonl",
        "02_hook_proposal.diff",
    ),
]:
    lines = (ROOT / source_name).read_text(encoding="utf-8").splitlines(keepends=True)
    prefix = f"diff --git a/{live_name} b/{live_name}\nnew file mode 100644\n"
    body = "".join(
        unified_diff([], lines, fromfile="/dev/null", tofile=f"b/{live_name}")
    )
    (OUT / patch_name).write_text(prefix + body, encoding="utf-8")
