"""Record the arXiv checks of 11 Nov, second batch (general_lit4a.out, general_lit4b.out, general_lit5.out)."""
import io

CH = "2026-11-11 abstracts read on arXiv (general_lit4a.out, general_lit4b.out, general_lit5.out), an agent"
UPD = {
    "CO06": ("REPORTED_SOLVED",
             "reported proved in July 2026 (proof announced by OpenAI; expositions arXiv 2607.15399 Geelen, 2607.16356 Oum). "
             "Primary source not read. Replace"),
    "AL03": ("REPLACE_DISPROVED",
             "counterexamples reported in Sep 2026 (arXiv 2609.07996 Adamczewski, Boehmler, Marczinzik; a second short "
             "construction 2609.15080 Greenfeld, King, Vendramin). Primary papers not read. Replace"),
    "OA06": ("REPLACE_DISPROVED",
             "non-sofic groups reported: arXiv 2611.04599 (Mghirbi, Douglas) gives torsion-free hyperbolic groups G with ab = 1, "
             "ba != 1 in F_p[G] for every prime p, so G is not sofic; p = 2 from a construction credited to OpenAI. One preprint "
             "read as an abstract. Replace, or keep as reported until confirmed"),
    "AL04": ("RESTATE",
             "reported false over every field of positive characteristic (p = 2 by a construction credited to OpenAI; odd p "
             "arXiv 2610.17662 Ivanov and 2611.04599). Characteristic zero is the open statement; restate the row to it"),
    "AN09": ("RESTATE",
             "arXiv 2607.15632 (Tao Zhang, Jul 2026) claims both directions fail in dimension two (60-point sets in "
             "Z_60 x Z_12, lifted to unions of unit squares); one preprint. Dimension one stays open (three intervals done, "
             "2607.24005). Restate the row to dimension one"),
    "IT01": ("RESTATE",
             "arXiv 2610.28208 (Chen, Huang, Oct 2026) claims the linear MDS conjecture in even characteristic; prime q is "
             "Ball's theorem. The open part is odd non-prime q (linear-in-q range of dimensions in 2610.03740). Restate"),
    "DG08": ("REPORTED_SOLVED",
             "dimension five proved in arXiv 2609.11005 (Chen, Ghomi, Wang); arXiv 2610.37817 (Agnoletto, Da Silva, Nardulli, "
             "Resende) states in its abstract that it establishes the generalized conjecture with rigidity. One preprint, "
             "abstract only: read it before replacing the row"),
}
KEEP = {
    "CO01": "no change: best bound now O(t logloglog t) (arXiv 2609.06867)",
    "CO02": "no change",
    "CO04": "no change to the conjecture itself; two neighbours reported false (partial list colouring, arXiv 2609.23291; "
            "list total colouring, 2609.38417)",
    "CO05": "no change to the conjecture itself; its list version is reported false (arXiv 2609.38417)",
    "CO07": "no change", "CO09": "no change (bounded VC-dimension case, arXiv 2609.18995)", "CO10": "no change",
    "CO11": "no change", "CO13": "no change", "GE02": "no change", "GE03": "no change", "GE04": "no change",
    "GE05": "no change", "GE06": "no change (a related conjecture of Tao on vanishing area, arXiv 2610.21076)",
    "AN06": "no change", "AN11": "no change", "AN13": "no change", "AN14": "no change", "DY04": "no change",
    "DY05": "no change", "DY07": "no change", "DG04": "no change", "DG05": "no change", "TO10": "no change",
    "TO02": "no change", "AL05": "no change (no hits)", "AL06": "no change", "PD09": "no change",
    "OA04": "no change: ghost SICs exist for d >= 4, existence of SICs open (arXiv 2611.01524)",
    "OA03": "no change in characteristic zero; the positive-characteristic idempotent conjecture is reported false "
            "(arXiv 2611.04599)",
    "CS10": "no change", "NT26": "no change", "NT16": "no change", "NT15": "no change",
    "NT17": "no change (conditional on a non-abelian large sieve, arXiv 2608.21573)",
}

p = "DESERVE.tsv"
with io.open(p, encoding="utf-8", newline="") as f:
    s = f.read()
nl = "\r\n" if "\r\n" in s else "\n"
rows = s.split(nl)
seen = {}
for k, r in enumerate(rows):
    c = r.split("\t")
    if len(c) < 7 or c[1] != "TOP200_GENERAL":
        continue
    if c[0] in UPD:
        seen[c[0]] = c[2]
        c[4], c[5], c[6] = UPD[c[0]][0], UPD[c[0]][1], CH
        rows[k] = "\t".join(c)
    elif c[0] in KEEP:
        seen[c[0]] = c[2]
        c[5] = (c[5] + "; " if c[5] else "") + KEEP[c[0]]
        c[6] = CH
        rows[k] = "\t".join(c)
missing = sorted((set(UPD) | set(KEEP)) - set(seen))
assert not missing, missing
out = nl.join(rows)
assert len(out) > len(s) and out.count(nl) == s.count(nl)
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
print("updated", len(UPD), "changed,", len(KEEP), "unchanged")
