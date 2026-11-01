import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
path = root / "CLAIMS.jsonl"
rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
note = " Full-lattice scope: every avoiding path leaving G_n costs at least 2n+1, and T_n<=2n, so its slack is at least 1. Thus the proved finite-box slack >=1/128 also holds for the infimum over all full-lattice avoiding paths."
for row in rows:
    if row["claim_id"] == "w360-C4" and note not in row["proof_or_counterexample"]:
        row["proof_or_counterexample"] += note
assert len(rows) == 9
path.write_text("".join(json.dumps(row,ensure_ascii=False)+"\n" for row in rows),encoding="utf-8")
with (root/"STATUS.md").open("a",encoding="utf-8") as stream:
    stream.write("2026-10-10 Clarified C4 full-lattice scope: outside-box avoiding paths have slack >=1, so cannot spoil the proved 1/128 margin. No statement or draft payload changed.\n")
with (root/"REVIEW_PACKET.md").open("a",encoding="utf-8") as stream:
    stream.write("\nC4 scope clarification saved: outside-box avoiding paths cost >=2n+1, so have slack >=1 and preserve the claimed full-lattice margin of 1/128.\n")
print("C4 full-lattice scope clarified; nine claim rows preserved; DRAFT payload unchanged.")
