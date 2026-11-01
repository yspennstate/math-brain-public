"""Create reviewable new-file diffs without writing outside this worker folder."""

from pathlib import Path


root = Path(__file__).parent
out = root / "patches"
out.mkdir(exist_ok=True)


def new_file_patch(source_name: str, target_relative: str, patch_name: str) -> None:
    body = (root / source_name).read_text(encoding="utf-8").splitlines()
    lines = [
        f"diff --git a/{target_relative} b/{target_relative}",
        "new file mode 100644",
        "--- /dev/null",
        f"+++ b/{target_relative}",
        f"@@ -0,0 +1,{len(body)} @@",
        *("+" + line for line in body),
    ]
    (out / patch_name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{patch_name}: {len(body)} added lines -> ~/{target_relative}")


new_file_patch("bundle_001.json", "math-brain-inbox/w452/bundle_001.json", "01_bundle.diff")
new_file_patch("hook_proposal.jsonl", "primary_directive/hooks1000/proposals/math-w452.jsonl", "02_hook.diff")
