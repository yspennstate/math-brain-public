"""Honor a/b live-path headers using a declared empty-note preimage."""
from pathlib import Path
import difflib

root = Path(__file__).resolve().parent
relative = "06_math_research/C0048_sharp_mean_field_barrier_w463_20261010.md"
note = (root/"ATTEMPT.md").read_text(encoding="utf-8")
patch = "".join(difflib.unified_diff([], note.splitlines(keepends=True), fromfile="a/"+relative, tofile="b/"+relative))
(root/"patches/01_C0048_minimax_note.diff").write_text(patch, encoding="utf-8", newline="\n")
fixture = root/"patch_check"/relative
fixture.parent.mkdir(parents=True, exist_ok=True)
if not fixture.exists():
    fixture.write_bytes(b"")
assert fixture.read_bytes() == b"", "Preserve an existing nonempty fixture"
(root/"PATCH_PRECONDITION.md").write_text("This unified diff preserves the required --- a/<live path> and +++ b/<live path> headers. Its preimage is an empty note. The reviewer must first create an empty 06_math_research/C0048_sharp_mean_field_barrier_w463_20261010.md in the review/deployment checkout, only if that note does not exist, then run git apply. A nonempty existing target must not be overwritten. The local patch_check folder contains the matching empty preimage; git apply --check there is the recorded validation.\n", encoding="utf-8")
report_path = root/"REPORT.md"
text = report_path.read_text(encoding="utf-8")
text = text.replace("Reviewer application of the optional knowledge-note diff: git", "Reviewer application of the optional knowledge-note diff: first create the empty note 06_math_research/C0048_sharp_mean_field_barrier_w463_20261010.md only if absent, then run git")
report_path.write_text(text, encoding="utf-8")
print("Updated pure unified diff; empty-preimage requirement recorded in PATCH_PRECONDITION.md.")
