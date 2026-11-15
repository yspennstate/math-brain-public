"""Repair Markdown math delimiters and check report numbers against saved outputs."""
from pathlib import Path
import json
import re
import sys

path = Path("REPORT.md")
text = path.read_text()
controls = [(i, repr(ch)) for i, ch in enumerate(text) if ord(ch) < 32 and ch not in "\n\t"]
if "--check" in sys.argv:
    assert text.startswith("Overall verdict: SOUND\n")
    assert not controls
    assert text.count("$$") % 2 == 0
    assert len(re.findall(r"^## Result \d+", text, flags=re.M)) == 22
    theory = json.loads(Path("referee_theory.json").read_text())
    for d in theory[:8]:
        assert d["c"] in text, d["name"]
    for d in theory[:6]:
        for key in ("ball_H0", "ball_H1"):
            assert f'{float(d[key]):.10f}'.lstrip("0") in text
    sims = json.loads(Path("referee_simulations.json").read_text())
    for s in sims[:12]:
        assert f'{s["S_over_n"]:.9f}' in text
    assert "1.772178369" in text
    print("PASS: 22 result sections; scalar values and ball limits match saved calculations;")
    print("PASS: all 12 main simulation normalisations match saved outputs;")
    print("PASS: display math balanced; no control characters; corrected error ratio present.")
    raise SystemExit()
if "--inspect" in sys.argv:
    print("control characters", controls)
    pieces = []
    block = False
    for line in text.splitlines():
        if line.startswith(chr(96)*3) or line in (r"\[", r"\]"):
            block = not block
            continue
        if block:
            continue
        depth = 0
        for i, ch in enumerate(line):
            if ch == "(":
                if depth == 0:
                    start = i
                depth += 1
            elif ch == ")" and depth:
                depth -= 1
                if depth == 0:
                    piece = line[start+1:i]
                    if piece not in pieces:
                        pieces.append(piece)
    print(json.dumps(pieces, indent=2))
    raise SystemExit()

# The report's original JS string lost the leading backslash of some inline
# TeX commands. Restore those command tokens, then use Markdown dollar math.
text = text.replace("\x08eta", r"\beta")
text = text.replace("\t" + "au", r"\tau")
restore = {"ell": r"\ell", "alpha": r"\alpha", "mathcal": r"\mathcal",
           "mathbf": r"\mathbf", "sum": r"\sum", "mu": r"\mu",
           "sigma": r"\sigma", "kappa": r"\kappa", "pi": r"\pi",
           "mathbb": r"\mathbb", "min": r"\min"}
skip = {"E1", "E2", "E3", "i", "ii", "iii", "error"}
lines = []
block = False
for line in text.splitlines():
    if line.startswith(chr(96)*3) or line in (r"\[", r"\]"):
        block = not block
        lines.append(line)
        continue
    if block:
        lines.append(line)
        continue
    spans = []
    depth = 0
    in_code = False
    for i, ch in enumerate(line):
        if ch == chr(96):
            in_code = not in_code
        if in_code:
            continue
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
            if depth == 0:
                spans.append((start, i+1))
    for start, end in reversed(spans):
        piece = line[start+1:end-1]
        if piece in skip or chr(96) in piece or piece.startswith(("E1)", "OpenAI")):
            continue
        for bad, good in restore.items():
            piece = re.sub(r"(?<![A-Za-z\\])" + bad + r"(?![A-Za-z])",
                           lambda match, replacement=good: replacement, piece)
        line = line[:start] + "$" + piece + "$" + line[end:]
    lines.append(line)
text = "\n".join(lines) + "\n"
text = text.replace("-1.7582,-2.4704,-2.3889,-3.4016,-1.6800,-2.3714",
                    "-1.7582,-2.4704,-2.3535,-3.2329,-1.5905,-2.3132")
# Prefer standard Markdown display math too.
text = text.replace("\n\\[\n", "\n$$\n").replace("\n\\]\n", "\n$$\n")
assert not any(ord(ch) < 32 and ch not in "\n\t" for ch in text)
assert text.count("$$") % 2 == 0
assert len(re.findall(r"^## Result \d+", text, flags=re.M)) == 22
theory = json.loads(Path("referee_theory.json").read_text())
assert [round(float(d["derivative"]), 4) for d in theory[:6]] == [
    -1.7582, -2.4704, -2.3535, -3.2329, -1.5905, -2.3132]
path.write_text(text)
print("22 result sections; display math balanced; scalar derivatives checked; no control characters.")
