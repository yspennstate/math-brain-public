from pathlib import Path

root = Path(__file__).resolve().parent


def stage(source: Path, target: str, output: Path) -> None:
    lines = source.read_text(encoding="utf-8").splitlines()
    patch = "\n".join(
        [
            f"--- a/{target}",
            f"+++ b/{target}",
            f"@@ -0,0 +1,{len(lines)} @@",
            *(f"+{line}" for line in lines),
            "",
        ]
    )
    output.parent.mkdir(exist_ok=True)
    output.write_text(patch, encoding="utf-8")
    print(f"patch_lines={len(lines)} target={target}")


stage(
    root / "draft_bundles" / "bundle_001.json",
    "~/math-brain-inbox/w392/bundle_001.json",
    root / "patches" / "01_p0117_review_bundle.diff",
)
stage(
    root / "hook_proposals" / "math-w392.jsonl",
    "~/primary_directive/hooks1000/proposals/math-w392.jsonl",
    root / "patches" / "02_p0117_proof_status_hook.diff",
)
