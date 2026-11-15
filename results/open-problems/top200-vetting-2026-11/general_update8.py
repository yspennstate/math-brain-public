"""Record the arXiv checks of 11 Nov, seventh batch (general_lit10a.out, general_lit10b.out): 74 rows T099..T222 of the
probability list (q10.txt; T195 is left, its query matched everything); extend the memory."""
import io
import os
import shutil

LIST = "TOP200_FAMOUS"
CH = "2026-11-11 abstracts read on arXiv (general_lit10a.out, general_lit10b.out), an agent"
IDS = """T099 T100 T102 T103 T105 T106 T107 T108 T109 T110 T111 T115 T116 T117 T118 T119 T120 T122 T123 T125 T126 T128 T129
T130 T131 T132 T133 T136 T137 T138 T139 T141 T142 T144 T145 T146 T151 T152 T153 T154 T155 T156 T159 T160 T163 T165 T167 T168
T169 T170 T171 T172 T173 T174 T176 T177 T178 T179 T180 T181 T185 T186 T188 T190 T194 T200 T201 T212 T215 T217 T218 T220 T221
T222""".split()
UPD = {
    "T115": ("REPORTED_SOLVED",
             "the Gotsman-Linial conjecture is reported solved in 2026 (credited to OpenAI in the abstract of arXiv "
             "2604.08095, Chang, Slote and coauthors, which studies the Boolean surface area of polynomial threshold "
             "functions after it). Primary source not read. Replace, or keep as REPORTED_SOLVED"),
    "T188": ("REPORTED_SOLVED",
             "arXiv 2609.26771 (Kogler, Sep 2026) states an unconditional proof of the Odlyzko-Poonen conjecture; one "
             "preprint, abstract only read. Replace, or keep as REPORTED_SOLVED"),
    "T163": ("RESTATE",
             "arXiv 2609.04789 (Huang, Sep 2026) proves Gaussian free field fluctuations for lozenge tilings of simply "
             "connected polygonal domains with a connected liquid region, the Kenyon-Okounkov prediction. Restate the "
             "row to what remains (non-polygonal boundaries, several liquid components, domains with holes)"),
    "T168": ("RESTATE",
             "arXiv 2605.26664 (Aggarwal, Toninelli) proves mixing in time N^{2+o(1)} for the hexagon, the first domain "
             "whose limit shape has frozen facets. Restate the row to general domains with frozen regions"),
    "T107": ("CHECK_STATEMENT",
             "the first two orders of the maximum of zeta on short intervals are established (Arguin, Bourgade, "
             "Radziwill, parts I and II; cited from the literature, not among this batch's hits); arXiv 2405.06474 "
             "treats mesoscopic intervals. What stays open is the limiting law of the recentred maximum; say in the "
             "row that this is meant"),
    "T129": ("CHECK_STATEMENT",
             "the singularity probability is exponentially small (arXiv 2203.06141, Campos, Jenssen, Michelen, "
             "Sahasrabudhe: P(sigma_min <= eps/sqrt n) <= C eps + exp(-cn)). The sharp rate (1/2 + o(1))^n is open; "
             "say in the row that the sharp rate is meant"),
}
NOTE = {
    "T103": "no change: the scaling limit in three dimensions is characterized (arXiv 2610.12047); the value of the "
            "growth exponent is open",
    "T105": "no change (Poissonian correlations of alpha n^d mod 1 for almost all alpha, arXiv 2605.06974)",
    "T117": "no change: the capacity is located within 0.0095 bits by a computer-assisted proof (arXiv 2609.19412); "
            "the exact value is open",
    "T118": "no change (arXiv 2610.08872)",
    "T125": "no change (the one-dimensional polymer is constructed and superdiffusive, arXiv 2509.05286; weak coupling "
            "in two dimensions, arXiv 2403.06730)",
    "T138": "no change: the reconstruction threshold and single-flip connectivity are settled for large k (arXiv "
            "2611.05981); the algorithmic threshold for finding solutions is open",
    "T155": "no change (arXiv 2510.27507)",
    "T156": "no change (0.6421 <= beta <= 0.8810, arXiv 2610.02809)",
    "T172": "no change (policies approaching the conjectured scaling under uniform traffic, arXiv 2610.37521)",
    "T176": "no change: an upper bound of order d^{5/3} for 2^d cards is claimed (arXiv 2610.18884, one author, "
            "unconfirmed); the order of the mixing time is open",
    "T177": "no change (arXiv 2609.11435)",
    "T179": "no change: weak uniqueness for Holder exponent above 2/3 is proved (arXiv 2608.01279), the row's starting "
            "point",
    "T180": "no change (matroid prophet secretary beats 1 - 1/e, arXiv 2611.06891)",
    "T181": "no change (improved power laws, arXiv 2509.02882)",
    "T212": "no change: annealed Markov chains reach the algorithmic threshold (arXiv 2610.16705, 2610.38206); "
            "hardness below it is open",
}
for k in ("T130", "T141", "T151", "T153", "T159", "T169", "T185", "T200"):
    NOTE[k] = "no hit for the query; nothing found that settles it"
KEEP = {k: NOTE.get(k, "no change") for k in IDS if k not in UPD}
assert len(IDS) == 74 and len(set(IDS)) == 74 and len(KEEP) == 68 and not set(NOTE) - set(KEEP)

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
add.append("\t".join(["T195", "#BIS", "not checked: the search drops the # sign and the query matched 20012 records; "
                      "query again by words", CH]))
with io.open(p2, "a", encoding="utf-8", newline="") as f:
    f.write(head + "\n".join(add) + "\n")

MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Seventh batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Seventh batch, same day (probability list, 74 rows T099..T222; general_lit10a.out, general_lit10b.out; abstracts only):
- T115 Gotsman-Linial conjecture: reported solved (credited to OpenAI in the abstract of arXiv 2604.08095).
- T188 Odlyzko-Poonen conjecture: an unconditional proof is stated in arXiv 2609.26771 (Kogler); one preprint.
- T163 Kenyon-Okounkov: Gaussian free field fluctuations proved for simply connected polygonal domains (arXiv 2609.04789).
- T168 lozenge Glauber dynamics: mixing time N^{2+o(1)} proved for the hexagon (arXiv 2605.26664).
- T107 Fyodorov-Hiary-Keating and T129 singularity of symmetric sign matrices: the main statements are theorems
  (Arguin-Bourgade-Radziwill; arXiv 2203.06141); the rows must say which sharper statement is meant.
Sixty-eight other rows unchanged. With this batch the probability list is checked except T127 (a peer's claim) and T195
(#BIS: the search drops the # sign; query it by words). A row name that contains the letters RR is rewritten by the
query script's RR placeholder; keep RR out of row names.
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("updated", len(UPD), "changed,", len(KEEP), "unchanged;", LIST, "rows still only title-read:", left)
