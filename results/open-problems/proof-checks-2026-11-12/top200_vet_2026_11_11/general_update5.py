"""Record the arXiv checks of 11 Nov, fourth batch (general_lit7a.out, general_lit7b.out, lit_ids1.out): the last 71
general rows; fix the notes of DG08 and DG02 if a note is passed; extend the memory.
usage: general_update5.py [DG08 note] [DG02 note]"""
import io
import shutil
import sys

CH = "2026-11-11 abstracts read on arXiv (general_lit7a.out, general_lit7b.out), an agent"
UPD = {
    "PD06": ("RESTATE",
             "arXiv 2606.28253 (Hintz, Jun 2026) announces nonlinear stability of Kerr in the full subextremal range; one "
             "preprint, not confirmed. What stays open is the final state conjecture; restate the row to it"),
    "LO05": ("REPORTED_SOLVED",
             "reported solved in the negative in 2026 (undecidable; credited to OpenAI, by a height estimate and a pole-parity "
             "construction); follow-up arXiv 2610.20691 (Sun: already undecidable with 86 unknowns). Primary source not read. "
             "Replace, or keep as REPORTED_SOLVED"),
    "PD15": ("CHECK_STATEMENT",
             "arXiv 2609.35419 (Guo, Sep 2026) claims convex real-analytic counterexamples to the Schiffer and Pompeiu "
             "conjectures in dimensions 2 to 18, 20 and 21; one preprint by one author, not confirmed (a computer-assisted "
             "counterexample to the related planar Berenstein conjecture is 2608.08953). Read it before changing the row"),
    "LO01": ("RESTATE",
             "arXiv 2610.15217 (Ackerman, Freer, Knight, Oct 2026) gives a counterexample for L_{omega_1,omega}, formally "
             "verified in Lean. The first-order conjecture stays open; restate the row to first-order theories"),
}
KEEP = {
    "NT01": "no change (only unrefereed claims)", "NT03": "no change", "NT04": "no change",
    "NT05": "no change: a weak form is proved in arXiv 2611.05217 (Soule)",
    "NT06": "no change", "NT07": "no change (one unrefereed claim, arXiv 2611.09007, not taken as settling)",
    "NT08": "no change", "NT11": "no change", "NT14": "no change",
    "NT18": "no change (new exponents for the exceptional set, arXiv 2611.14167, 2611.08717)",
    "AG01": "no change", "AG02": "no change (ordinary Calabi-Yau threefolds, arXiv 2610.13939)", "AG03": "no change",
    "AG11": "no change", "AG12": "no change", "AG15": "no change", "AG16": "no change", "AL02": "no change",
    "TO03": "no change", "TO05": "no change",
    "DG10": "no change: the hyperkaehler SYZ conjecture is proved (arXiv 2610.12277, Engel, Mauri); the Calabi-Yau "
            "statement is open",
    "DG13": "no change", "DG14": "no change", "AN02": "no change", "AN03": "no change", "AN04": "no change",
    "AN05": "no change", "AN08": "no change",
    "AN10": "no change (sixth and seventh coefficients, arXiv 2610.15206, 2611.00397)", "AN12": "no change",
    "PD01": "no change", "PD02": "no change", "PD03": "no change", "PD04": "no change", "PD05": "no change",
    "PD07": "no change",
    "PD10": "no change in dimension three; the one-dimensional case with exponent one is confirmed (arXiv 2609.10478)",
    "PD11": "no change", "PD12": "no change",
    "PD13": "no change (spacetime inequality for a special class of data, arXiv 2610.20559)",
    "PD16": "no change", "PD17": "no change",
    "DY01": "no change (parabolically bounded primitive renormalization, arXiv 2606.27272)", "DY02": "no change",
    "DY03": "no change",
    "DY06": "no change (the Margulis-Zimmer conjecture on commensurated subgroups, a different statement, is proved for "
            "nonuniform lattices, arXiv 2607.17078)",
    "DY08": "no change", "GE01": "no change (new bounds in dimensions 32 to 39, arXiv 2611.03682)", "GE08": "no change",
    "LO02": "no change", "LO03": "no change", "LO04": "no change", "LO06": "no change",
    "CS01": "no change", "CS02": "no change", "CS03": "no change", "CS04": "no change", "CS05": "no change",
    "CS06": "no change",
    "CS07": "no change (a deterministic n^{O(log n)} algorithm is claimed in arXiv 2611.01399; not polynomial)",
    "CS08": "no change", "CS09": "no change", "CS11": "no change", "IT02": "no change", "OA01": "no change",
    "OA02": "no change", "OA05": "no change",
}
NOTE = {
    "DG08": "arXiv 2610.37817 (Agnoletto, Da Silva, Nardulli, Resende) states the generalized conjecture with rigidity in the "
            "equality case, also for Alexandrov spaces with two-sided curvature bounds; one preprint, not confirmed",
    "DG02": "arXiv 2609.11980 states a smooth metric of strictly positive sectional curvature on S^3 x S^3, found by an "
            "automated research agent; no independent check is named",
    "AN09": "arXiv 2607.15632 (Zhang) states that both directions fail in dimension two (two 60-point sets in "
            "Z_60 x Z_12, lifted to unions of unit squares); dimension one is then the remaining case; one preprint",
}

p = "DESERVE.tsv"
with io.open(p, encoding="utf-8", newline="") as f:
    s = f.read()
nl = "\r\n" if "\r\n" in s else "\n"
rows = s.split(nl)
seen = {}
noted = 0
for k, r in enumerate(rows):
    c = r.split("\t")
    if len(c) < 7 or c[1] != "TOP200_GENERAL":
        continue
    if c[0] in UPD:
        assert "title read" in c[6], c[0]
        seen[c[0]] = c[2]
        c[4], c[5], c[6] = UPD[c[0]][0], UPD[c[0]][1], CH
        rows[k] = "\t".join(c)
    elif c[0] in KEEP:
        assert "title read" in c[6], c[0]
        seen[c[0]] = c[2]
        c[5] = (c[5] + "; " if c[5] else "") + KEEP[c[0]]
        c[6] = CH
        rows[k] = "\t".join(c)
    elif c[0] in NOTE:
        c[5] = c[5] + "; whole abstract read (lit_ids1.out): " + NOTE[c[0]]
        rows[k] = "\t".join(c)
        noted += 1
missing = sorted((set(UPD) | set(KEEP)) - set(seen))
assert not missing, missing
assert noted == len(NOTE)
out = nl.join(rows)
assert len(out) > len(s) and out.count(nl) == s.count(nl)
left = sum(1 for r in rows if "\tTOP200_GENERAL\t" in r and "title read" in r.split("\t")[-1])
with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(out)

p2 = "GENERAL_LITCHECK.tsv"
with io.open(p2, encoding="utf-8", newline="") as f:
    t = f.read()
nl2 = "\r\n" if "\r\n" in t else "\n"
add = ["\t".join([k, seen[k], UPD[k][0] + ": " + UPD[k][1], CH]) for k in UPD]
add.append("\t".join(["-", "rows with no change", ", ".join(sorted(KEEP)) + ": nothing in the newest abstracts settles the row "
                      "(notes per row in DESERVE.tsv)", CH]))
t = t.rstrip("\r\n") + nl2 + nl2.join(add) + nl2
with io.open(p2, "w", encoding="utf-8", newline="") as f:
    f.write(t)

MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Fourth batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Fourth batch, same day (the last 71 general rows; general_lit7a.out, general_lit7b.out; abstracts only):
- LO05 Hilbert's tenth problem over Q: reported undecidable (credited to OpenAI; follow-up arXiv 2610.20691 Sun, 86 unknowns).
- PD06 Kerr stability: arXiv 2606.28253 (Hintz) announces the full subextremal range; the final state conjecture stays open.
- LO01 Vaught: counterexample for L_{omega_1,omega}, verified in Lean (arXiv 2610.15217); first-order case open.
- PD15 Schiffer and Pompeiu: arXiv 2609.35419 claims convex counterexamples in dimensions 2 to 18; one preprint, unconfirmed.
Sixty-seven other rows unchanged (the Clay problems among them: only unrefereed claims). The whole general list has now been
checked by name: 158 rows, 18 changed. How to repeat: q<N>.txt (one line per row, "ID name|arXiv query", RR for the resolution
words), general_lit6.py, then an update script with UPD and KEEP dictionaries (general_update5.py).
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("updated", len(UPD), "changed,", len(KEEP), "unchanged, notes", noted, "; general rows still only title-read:", left)
