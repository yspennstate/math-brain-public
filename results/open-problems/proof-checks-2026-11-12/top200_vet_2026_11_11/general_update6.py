"""Record the arXiv checks of 11 Nov, fifth batch (general_lit8a.out, general_lit8b.out): 44 named rows of the
probability list (q8.txt; T195 is left for a new query, its query was too broad); extend the memory."""
import io
import os
import shutil

LIST = "TOP200_FAMOUS"
CH = "2026-11-11 abstracts read on arXiv (general_lit8a.out, general_lit8b.out), an agent"
UPD = {
    "T189": ("REPORTED_SOLVED",
             "an FPRAS for general graphs is reported in 2026 (credited to OpenAI; by a restricted Poincare inequality for "
             "two matchings); simplified proof arXiv 2610.26803 (Liu, Meng). Primary source not read. Replace, or keep as "
             "REPORTED_SOLVED"),
    "T197": ("REPORTED_SOLVED",
             "the free group factors are reported isomorphic in 2026 (proof credited to OpenAI); arXiv 2610.19590 "
             "(Shlyakhtenko) builds on it for the C*-algebras of free semicircular systems. Primary source not read. Replace, "
             "or keep as REPORTED_SOLVED"),
    "T199": ("CHECK_STATEMENT",
             "arXiv 2608.19869 (Huang, Liu, Liu, Aug 2026) claims that Marton's inner bound is strictly suboptimal for some "
             "discrete memoryless broadcast channels; one preprint, not confirmed. The capacity region itself stays open; "
             "if the row asks whether Marton's bound is tight, restate it"),
}
KEEP = {
    "T059": "no change (algorithms by Markov decision processes, arXiv 2608.27419)", "T062": "no change",
    "T073": "no change", "T096": "no hit for the query; nothing found that settles it", "T101": "no change",
    "T104": "no change; arXiv 2610.22151 (Alon) reduces it to a spectral comparison conjecture on Specht modules",
    "T112": "no change (checked through fourteen elements, arXiv 2607.23926)", "T121": "no change",
    "T124": "no hit for the query; nothing found that settles it", "T134": "no change", "T147": "no change",
    "T148": "no change (the constant is raised to 0.382709, arXiv 2610.02295)", "T149": "no change",
    "T157": "no change", "T158": "no change", "T162": "no change",
    "T166": "no change (one author's claim, arXiv 2501.14941, not taken as settling)", "T175": "no change",
    "T182": "no change", "T183": "no change", "T184": "no change", "T187": "no change",
    "T191": "no change (diameter bounds for arbitrary finite groups, arXiv 2604.15303)", "T192": "no change",
    "T193": "no change", "T196": "no change",
    "T198": "no change (the 5/4 threshold is reproved, arXiv 2610.05015)",
    "T202": "no hit for the query; nothing found that settles it",
    "T203": "no change (new lower bounds for odd cycles, arXiv 2607.21517, 2607.29681)",
    "T204": "no change (Neumann balls in higher dimensions, arXiv 2607.29305)", "T205": "no change", "T206": "no change",
    "T207": "no change (paths, arXiv 2610.24887, 2611.01963)", "T208": "no change",
    "T209": "no change: 1.773 <= K_G <= 1.7799 is proved (arXiv 2610.10477); the exact value is open",
    "T210": "no change", "T211": "no change",
    "T213": "no change (a certified bound on the threshold, arXiv 2608.15870)", "T214": "no change", "T216": "no change",
    "T219": "no change",
}

p = "DESERVE.tsv"
with io.open(p, encoding="utf-8", newline="") as f:
    s = f.read()
nl = "\r\n" if "\r\n" in s else "\n"
rows = s.split(nl)
seen = {}
for k, r in enumerate(rows):
    c = r.split("\t")
    if len(c) < 7 or c[1] != LIST or c[0] not in UPD and c[0] not in KEEP:
        continue
    assert "title read" in c[6], c[0]
    seen[c[0]] = c[2]
    tail = c[6].split(";", 1)[1] if ";" in c[6] else ""
    if c[0] in UPD:
        c[5] = UPD[c[0]][1] + " (verdict before the check: " + c[4] + ")"
        c[4] = UPD[c[0]][0]
    else:
        c[5] = (c[5] + "; " if c[5] else "") + KEEP[c[0]]
    c[6] = CH + (";" + tail if tail else "")
    rows[k] = "\t".join(c)
missing = sorted((set(UPD) | set(KEEP)) - set(seen))
assert not missing, missing
out = nl.join(rows)
assert len(out) > len(s) and out.count(nl) == s.count(nl)
left = sum(1 for r in rows if ("\t" + LIST + "\t") in r and "title read" in r.split("\t")[-1])
with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(out)

p2 = "FAMOUS_LITCHECK.tsv"
head = "" if os.path.exists(p2) else "id\ttitle\tfinding\tchecked\n"
add = ["\t".join([k, seen[k], UPD[k][0] + ": " + UPD[k][1], CH]) for k in UPD]
add.append("\t".join(["-", "rows with no change", ", ".join(sorted(KEEP)) + ": nothing in the newest abstracts settles the row "
                      "(notes per row in DESERVE.tsv)", CH]))
add.append("\t".join(["T195", "#BIS", "not checked: the query was too broad (20020 hits); query again", CH]))
with io.open(p2, "a", encoding="utf-8", newline="") as f:
    f.write(head + "\n".join(add) + "\n")

MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Fifth batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Fifth batch, same day (probability list, 44 named rows that are not probability problems or need a statement check;
general_lit8a.out, general_lit8b.out; abstracts only; table FAMOUS_LITCHECK.tsv):
- T189 FPRAS for perfect matchings in general graphs: reported found (credited to OpenAI; simplified proof arXiv 2610.26803).
- T197 free group factor isomorphism: reported proved (credited to OpenAI; arXiv 2610.19590 Shlyakhtenko builds on it).
- T199 broadcast channel: arXiv 2608.19869 claims Marton's inner bound is strictly suboptimal; one preprint, unconfirmed.
Forty-one other rows unchanged. Pattern across the batches: the rows that fell in 2026 are the ones with a named, checkable
statement, and several are credited to an automated system; read the list against the last six months of arXiv before a
worker is put on any row.
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("updated", len(UPD), "changed,", len(KEEP), "unchanged;", LIST, "rows still only title-read:", left)
