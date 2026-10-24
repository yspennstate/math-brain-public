"""Read-only targeted discovery for the named C0017 packet."""
import os
import pathlib
import subprocess

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
base = pathlib.Path("~/<private-repo>/06_math_research")
roots = sorted(p for p in base.glob("probability_1000_intake_*") if p.is_dir())
roots += [base / "probability_1000_attempts_H_20260912", base / "probability_1000_attempts_I_20260914", base / "prob1000_lean_20260908"]
print("NAMED_ROOTS", flush=True)
for root in roots:
    print(root, flush=True)
    if not root.exists():
        continue
    proc = subprocess.run(["rg", "--files", str(root)], capture_output=True, text=True, encoding="utf-8", timeout=45)
    files = proc.stdout.splitlines()
    relevant = [f for f in files if any(t in pathlib.Path(f).name.lower() for t in ("c0017", "percol", "conformal", "source", "candidate", "ranking", "solved", "retired"))]
    for f in relevant[:45]:
        print(f, flush=True)
    if not any("c0017" in f.lower() for f in relevant):
        proc = subprocess.run(["rg", "-l", "-F", "C0017", str(root), "-g", "*.jsonl", "-g", "*.csv", "-g", "*.md", "-g", "*.json"], capture_output=True, text=True, encoding="utf-8", timeout=45)
        print("ID_MATCH_FILES", proc.stdout[:12000], flush=True)
print("WORKER_PACKET_FILENAMES", flush=True)
for worker in ("w411", "w412", "w413", "w414", "w415", "w416", "w417", "w418", "w419", "w420", "w421", "w422"):
    folder = pathlib.Path("~/brain_workers") / worker
    if folder.exists():
        print(worker, [p.name for p in folder.iterdir() if p.is_file()], flush=True)
print("PERCOLATION_ATTEMPT_FILENAMES", flush=True)
large = pathlib.Path("~/Big Open problem in probability theory")
if large.exists():
    proc = subprocess.run(["rg", "--files", str(large)], capture_output=True, text=True, encoding="utf-8", timeout=45)
    for f in proc.stdout.splitlines():
        name = pathlib.Path(f).name.lower()
        if any(t in name for t in ("percol", "c0017", "conformal", "solved", "retired")):
            print(f, flush=True)
print("BUNDLE_SPEC_PATHS", flush=True)
for path in ("~/math-brain-inbox/BUNDLE_SPEC.md", "~/math-brain-inbox/README.md"):
    p = pathlib.Path(path)
    if p.exists():
        print(path, p.read_text(encoding="utf-8")[:22000], flush=True)
