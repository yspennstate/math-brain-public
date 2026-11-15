"""Record the arXiv checks of 11 Nov, sixth batch (general_lit9a.out, general_lit9b.out): 80 rows T001..T098 of the
probability list (q9.txt); extend the memory."""
import io
import os
import shutil

LIST = "TOP200_FAMOUS"
CH = "2026-11-11 abstracts read on arXiv (general_lit9a.out, general_lit9b.out), an agent"
IDS = """T001 T002 T003 T004 T005 T006 T007 T008 T010 T011 T012 T013 T014 T015 T016 T017 T019 T021 T022 T023 T024 T025 T027
T028 T029 T030 T031 T032 T033 T034 T036 T037 T038 T039 T042 T043 T044 T045 T046 T047 T048 T049 T050 T053 T054 T055 T056 T057
T058 T060 T063 T064 T065 T067 T068 T070 T071 T072 T075 T076 T077 T078 T079 T080 T081 T083 T084 T085 T086 T087 T088 T089 T090
T091 T092 T093 T094 T095 T097 T098""".split()
UPD = {
    "T042": ("REPORTED_SOLVED",
             "reported proved in 2026 (proof by Turturean); exposition arXiv 2611.11626 (Blanc, Docter, Strassle, Tan), short "
             "proof by the completion framework arXiv 2611.12795 (Huffstutler, Miloschewsky, Podder). Primary source not "
             "read. Replace, or keep as REPORTED_SOLVED"),
    "T070": ("RESTATE",
             "the density conjecture is proved in dimension one (new proof arXiv 2502.02579; arXiv 2605.00207 Hoffman, "
             "Johnson, Junge, Meisel: the driven-dissipative density equals the fixed-energy critical density, with fast "
             "mixing and power-law avalanches). Restate the row to dimension two and higher"),
    "T063": ("RESTATE",
             "convergence to the full-plane Gaussian free field is proved for -1 <= Delta <= -1/2 (arXiv 2603.06268) and, "
             "with Dirichlet boundary conditions in simply connected domains, for a range of Delta that includes Delta near 0 "
             "(arXiv 2610.07454, Averous, Duminil-Copin, He, Lammers, Manolescu). Restate the row to the remaining range of "
             "Delta"),
    "T023": ("CHECK_STATEMENT",
             "arXiv 2610.10480 and 2610.10505 (Holden, Yu, Oct 2026): the mated-CRT map and spanning-tree-weighted planar "
             "maps converge to Liouville quantum gravity under circle packing and Riemann uniformization. Other map models "
             "(uniform maps under circle packing among them) remain; say in the row which models are meant"),
}
NOTE = {
    "T001": "no change (long-range kernels only, arXiv 2611.01490)",
    "T012": "no change (dimension five is done, arXiv 2211.17023)",
    "T013": "no change (universality across isoradial graphs, arXiv 2611.00425)",
    "T016": "no change (shape exclusion, arXiv 2610.37625)",
    "T017": "no change (an upper bound 4.268 for 3-SAT is claimed, arXiv 2610.10599)",
    "T029": "no change (arXiv 2610.04745)",
    "T039": "no change: the propeller conjecture of Khot and Naor is reported proved (arXiv 2610.32158, Heilman, simplifying "
            "a proof credited to OpenAI); the standard simplex conjecture is a different statement",
    "T048": "no change (computer-assisted proof for offspring uniform on {2,3} up to bias 1.755, arXiv 2609.29894)",
    "T056": "no change: products of two infinite countable groups have fixed price one (arXiv 2509.08325); the general "
            "problem is open",
    "T084": "no change (the complete graph for every n, arXiv 2609.26134; arXiv 2610.00549)",
    "T088": "no change: the chemical-distance metric converges to the CLE_6 geodesic metric (arXiv 2604.14122); the value "
            "of the exponent is open",
}
for k in ("T007", "T010", "T028", "T038", "T057", "T060", "T078", "T085", "T086"):
    NOTE[k] = "no hit for the query; nothing found that settles it"
KEEP = {k: NOTE.get(k, "no change") for k in IDS if k not in UPD}
assert len(IDS) == 80 and len(KEEP) == 76 and not set(NOTE) - set(KEEP)

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
with io.open(p2, "a", encoding="utf-8", newline="") as f:
    f.write(head + "\n".join(add) + "\n")

MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Sixth batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Sixth batch, same day (probability list, 80 rows T001..T098; general_lit9a.out, general_lit9b.out; abstracts only):
- T042 Aaronson-Ambainis conjecture: reported proved (Turturean; exposition arXiv 2611.11626, short proof 2611.12795).
- T070 activated random walk density conjecture: proved in dimension one (arXiv 2502.02579, 2605.00207); open in higher dimension.
- T063 six-vertex height function: Gaussian free field limit proved for a range of Delta (arXiv 2603.06268, 2610.07454).
- T023 planar maps to Liouville quantum gravity: mated-CRT and tree-weighted maps done under circle packing (2610.10480, 2610.10505).
Seventy-six other rows unchanged. The classical statistical-mechanics rows (percolation in low dimension, self-avoiding walk,
3D Ising, Yang-Mills, spin glasses) show no movement; the rows that moved are again the named, checkable statements.
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("updated", len(UPD), "changed,", len(KEEP), "unchanged;", LIST, "rows still only title-read:", left)
