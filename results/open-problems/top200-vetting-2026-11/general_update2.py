"""Record the arXiv checks of 11 Nov (general_lit2.out, general_lit3.out) for seven general-list rows."""
import io

CH = "2026-11-11 abstracts read on arXiv (general_lit2.out, general_lit3.out), an agent"
UPD = {
    "AN07": ("REPORTED_SOLVED",
             "reported proved in 2026 by Lech Mazur with computer assistance (Tao wrote an exposition); cited as proved in arXiv "
             "2609.19126 and 2609.04246; primary source not read, refereeing unknown. Replace, or keep as REPORTED_SOLVED"),
    "CO08": ("REPORTED_SOLVED",
             "reported proved in 2026 (a short counting proof credited to an OpenAI model; expositions arXiv 2609.17877 Wood, "
             "2609.32011 Cummings, simplified in 2609.21159 Frederickson; called recently proved in 2609.10987). Replace"),
    "DG09": ("REPORTED_SOLVED",
             "arXiv 2609.15720 (Hong, Li, Wang, Sep 2026) announces the stable Bernstein theorem in R^7 by a Green-function "
             "argument; one preprint, unrefereed as far as checked. Replace, or keep as REPORTED_SOLVED until it is confirmed"),
    "DG06": ("RESTATE",
             "smooth counterexamples are reported (announced by Alpoge; a simpler construction in arXiv 2610.34036, Ando and "
             "Umehara: a strictly convex closed C-infinity surface with exactly one umbilic). The open statement is the "
             "real-analytic case; restate the row to it"),
}
KEEP = {
    "TO13": "no change: partial results only (strong Atiyah for finite-index torsion-free subgroups of Out of surface, free and "
            "right-angled Artin groups, arXiv 2606.19606)",
    "AN01": "no change: 27 recent abstracts, none claims the Hilbert-space case",
    "CO03": "no change: nothing after Suk on the exact value",
}

p = "DESERVE.tsv"
with io.open(p, encoding="utf-8", newline="") as f:
    s = f.read()
nl = "\r\n" if "\r\n" in s else "\n"
rows = s.split(nl)
seen = {}
for k, r in enumerate(rows):
    c = r.split("\t")
    if c[0] in UPD and len(c) >= 7:
        seen[c[0]] = c[2]
        c[4], c[5], c[6] = UPD[c[0]][0], UPD[c[0]][1], CH
        rows[k] = "\t".join(c)
    elif c[0] in KEEP and len(c) >= 7:
        seen[c[0]] = c[2]
        c[5] = c[5] + "; " + KEEP[c[0]]
        c[6] = CH
        rows[k] = "\t".join(c)
assert len(seen) == 7, seen
out = nl.join(rows)
assert len(out) >= len(s)
with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(out)

p2 = "GENERAL_LITCHECK.tsv"
with io.open(p2, encoding="utf-8", newline="") as f:
    t = f.read()
nl2 = "\r\n" if "\r\n" in t else "\n"
add = []
for k in ("AN07", "CO08", "DG09", "DG06"):
    add.append("\t".join([k, seen[k], UPD[k][0] + ": " + UPD[k][1], CH]))
for k in ("TO13", "AN01", "CO03"):
    add.append("\t".join([k, seen[k], KEEP[k], CH]))
t = t.rstrip("\r\n") + nl2 + nl2.join(add) + nl2
with io.open(p2, "w", encoding="utf-8", newline="") as f:
    f.write(t)
print("updated", sorted(seen))
