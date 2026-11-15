"""Record the arXiv checks of 11 Nov, deep-learning list, second file (dl_lit12.out): rows T290..T356 of q12.txt
except seven whose queries matched only unrelated records; one note for probability row T096; extend the memory."""
import io
import os
import shutil

LIST = "TOP200_DL"
CH = "2026-11-11 abstracts read on arXiv (dl_lit12.out), an agent"
SKIP = {"T293": "Hardness of learning random-weight neural networks",
        "T309": "Computational complexity of learning Gaussian mixtures by score matching",
        "T313": "Do GANs learn the distribution?",
        "T320": "Depth needed by normalizing flows",
        "T324": "Metastable clustering times in mean-field transformer dynamics",
        "T332": "Graph neural networks on sparse random graphs",
        "T346": "The limits of randomized smoothing"}
with io.open("q12.txt", encoding="utf-8") as f:
    IDS = [ln.split()[0] for ln in f if ln.strip()]
IDS = [k for k in IDS if k not in SKIP]
UPD = {
    "T311": ("RESTATE",
             "arXiv 2412.10295 proves the Stein log-Sobolev inequality in every dimension for kernels whose Fourier "
             "transform has quadratic decay at infinity, which gives the exponential rate for the continuous method. "
             "Restate the row to the kernels left out (the Gaussian kernel among them)"),
    "T333": ("CHECK_STATEMENT",
             "arXiv 2603.18168 proves convergence of the training dynamics of residual networks with two-layer blocks "
             "to a large-scale limit, with error O(1/L + sqrt(D/(L M)) + 1/sqrt(D)) in depth L, width M and embedding "
             "dimension D. The row must say what it asks beyond this (other block structures, long times, sharp rates)"),
    "T310": ("CHECK_STATEMENT",
             "a rate of order N^(-1/2) in kernel Stein discrepancy for the time-averaged empirical measure is in the "
             "literature (Balasubramanian, Banerjee, Ghosal, 2024; cited from memory, not among this batch's hits, to "
             "be confirmed by the follow-up query); arXiv 2607.00149 gives uniform-in-time propagation of chaos with "
             "logarithmic rates in Wasserstein distance. The row must name the metric in which a polynomial rate is "
             "asked"),
}
NOTE = {
    "T291": "no change: sample complexity d^(1 v k/2) with the generative leap exponent k is shown necessary for "
            "low-degree polynomials and sufficient (arXiv 2506.05500); the statement check stands",
    "T301": "no change (arXiv 2610.28800 separates depth 2 from depth 3 under the Gaussian measure)",
    "T303": "no change, already REPLACE; two preprints state an O(1) bound (arXiv 2610.07728, 2610.01447)",
    "T304": "no change: a lower bound exp(Omega(log^(1/3) d)) at condition number 2 (arXiv 2611.05813); the exact "
            "complexity is open",
    "T314": "no change, already REPLACE; a second source: simulated annealing samples the model for beta < 1 (arXiv "
            "2610.17717)",
    "T317": "no change (arXiv 2607.19176, 2510.20871)",
    "T322": "no change (arXiv 2606.30574)",
    "T327": "no change (arXiv 2607.02800, 2508.07208)",
    "T329": "no change (arXiv 2603.09589)",
    "T343": "no change (arXiv 2611.03653)",
    "T349": "no change (capacity of wide treelike networks, arXiv 2402.05719; not the fully connected machine)",
    "T351": "no change (arXiv 2610.21201)",
    "T352": "no change, already REPLACE (arXiv 2410.01068, 2407.06496)",
    "T355": "no change (arXiv 2607.16384)",
    "T356": "no change (a criterion for avoiding collapse, arXiv 2611.00259)",
}
NOTE["T331"] = "no hit for the query; nothing found that settles it"
KEEP = {k: NOTE.get(k, "no change") for k in IDS if k not in UPD}
assert len(IDS) == 60 and len(set(IDS)) == 60 and len(KEEP) == 57 and not set(NOTE) - set(KEEP)
T096 = ("; 11 Nov: simulated annealing is proved to sample the model for beta < 1 (arXiv 2610.17717); rapid mixing of "
        "Glauber dynamics itself up to beta = 1 is a different statement")

p = "DESERVE.tsv"
with io.open(p, encoding="utf-8", newline="") as f:
    s = f.read()
nl = "\r\n" if "\r\n" in s else "\n"
rows = s.split(nl)
seen = {}
n096 = 0
for k, r in enumerate(rows):
    c = r.split("\t")
    if len(c) >= 7 and c[0] == "T096" and c[1] == "TOP200_FAMOUS":
        assert "2610.17717" not in c[5]
        c[5] = c[5] + T096
        rows[k] = "\t".join(c)
        n096 += 1
        continue
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
assert n096 == 1
out = nl.join(rows)
assert len(out) > len(s) and out.count(nl) == s.count(nl)
left = sum(1 for r in rows if ("\t" + LIST + "\t") in r and "title read" in r.split("\t")[-1])
with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(out)

p2 = "DL_LITCHECK.tsv"
head = "" if os.path.exists(p2) else "id\ttitle\tfinding\tchecked\n"
add = ["\t".join([k, seen[k], UPD[k][0] + ": " + UPD[k][1], CH]) for k in UPD]
add.append("\t".join(["-", "rows with no change", ", ".join(sorted(KEEP)) + ": nothing in the newest abstracts settles the row "
                      "(notes per row in DESERVE.tsv)", CH]))
for k in sorted(SKIP):
    add.append("\t".join([k, SKIP[k], "not checked: the query matched only unrelated records; query again with "
                          "narrower words (q14.txt)", CH]))
with io.open(p2, "a", encoding="utf-8", newline="") as f:
    f.write(head + "\n".join(add) + "\n")

MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Ninth batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Ninth batch, same day (deep-learning list, 60 rows T290..T356; dl_lit12.out; abstracts only):
- T311 Stein log-Sobolev inequality: proved for kernels with quadratic Fourier decay (arXiv 2412.10295); restate to the
  other kernels.
- T333 scaling limit of trained residual networks: a quantitative large-scale limit of training is proved for
  two-layer blocks (arXiv 2603.18168); T310 finite-particle rate for SVGD: a rate in kernel Stein discrepancy exists;
  both rows must say what more they ask.
- KLS (T303, already out of the list): two preprints state an O(1) bound (arXiv 2610.07728, 2610.01447). Sampling SK
  for beta < 1 (T314, already out): a second source, simulated annealing (arXiv 2610.17717).
Fifty-seven other rows unchanged; seven rows not checked (off-topic hits), queued in q14.txt.
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("updated", len(UPD), "changed,", len(KEEP), "unchanged;", LIST, "rows still only title-read:", left)
