"""Record the arXiv checks of 11 Nov, deep-learning list, first file (dl_lit11.out): rows T223..T289 of q11.txt
except T244 and T279, whose queries matched only unrelated records; extend the memory."""
import io
import os
import shutil

LIST = "TOP200_DL"
CH = "2026-11-11 abstracts read on arXiv (dl_lit11.out), an agent"
SKIP = {"T244": "A rigorous 1/width expansion (depth-to-width ratio as coupling)", "T279": "A reparametrization-invariant flatness measure"}
with io.open("q11.txt", encoding="utf-8") as f:
    IDS = [ln.split()[0] for ln in f if ln.strip()]
IDS = [k for k in IDS if k not in SKIP]
UPD = {
    "T250": ("RESTATE",
             "arXiv 2607.06290 (Agazzi, Mosig Garcia and coauthors, Jul 2026) gives explicit Wasserstein bounds of order "
             "width^(-1/2) between a finite network and its Gaussian-process limit for Tensor Programs, feed-forward and "
             "weight-sharing architectures included. Restate the row to what remains: rates along training (the "
             "feature-learning programs) and the optimal order"),
    "T283": ("REPORTED_SOLVED",
             "the conjecture is reported false in both standard forms: the quasi-polynomial form (arXiv 2505.17360, "
             "noted by agent) and now the polynomial-time binary form (arXiv 2607.20318, Mao, Jul 2026: a family of "
             "permutation-symmetric counterexamples for every fixed r >= 3). One preprint, abstract only read. Keep the "
             "row only with a named corrected conjecture; otherwise replace"),
    "T271": ("CHECK_STATEMENT",
             "arXiv 2510.21078 proves neural collapse under gradient flow for a two-layer ReLU network on orthogonally "
             "separable data, with no unconstrained-features assumption. The row must say which generality is meant "
             "(deep networks, general data, discrete steps)"),
}
NOTE = {
    "T223": "no change (global convergence for wide shallow models beyond homogeneous nonlinearities, arXiv 2605.10775)",
    "T232": "no change (SGD in the saddle-to-saddle regime of deep linear networks, arXiv 2604.06366)",
    "T233": "no change (arXiv 2502.02531)",
    "T235": "no change (arXiv 2610.22593, 2609.38453: no proof under standard training)",
    "T240": "no change (replica analysis of the ReLU soft committee machine, arXiv 2603.20010; not a proof)",
    "T242": "no change: commutation during training is proved for linear residual networks (arXiv 2610.30729); "
            "nonlinear networks are open",
    "T255": "the query matched unrelated records; not read further, the row is already REPLACE",
    "T256": "no change (discontinuous transition for other transfer functions, arXiv 2405.14607; physics level)",
    "T258": "no change (a learned linear skip removes the spurious minima for planar features, arXiv 2610.01728)",
    "T264": "no change (tempered overfitting proved for binary-weight networks, arXiv 2410.19092)",
    "T272": "no change (arXiv 2510.08023)",
    "T277": "no change: an algorithmic separation between constant and logarithmic depth is proved for layerwise "
            "coordinate descent on hierarchical Boolean targets (arXiv 2607.25200); end-to-end gradient descent is open",
    "T282": "no change (scope and breakdown of Gaussian universality for empirical risk minimization, arXiv 2604.03146)",
    "T284": "no change (stable algorithms cannot reliably find isolated perceptron solutions, arXiv 2604.00328)",
    "T289": "no change (free-energy fluctuations up to criticality, arXiv 2610.31736; strong freezing, arXiv 2610.06275)",
}
for k in ("T241", "T268"):
    NOTE[k] = "no hit for the query; nothing found that settles it"
KEEP = {k: NOTE.get(k, "no change") for k in IDS if k not in UPD}
assert len(IDS) == 65 and len(set(IDS)) == 65 and len(KEEP) == 62 and not set(NOTE) - set(KEEP)

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

p2 = "DL_LITCHECK.tsv"
head = "" if os.path.exists(p2) else "id\ttitle\tfinding\tchecked\n"
add = ["\t".join([k, seen[k], UPD[k][0] + ": " + UPD[k][1], CH]) for k in UPD]
add.append("\t".join(["-", "rows with no change", ", ".join(sorted(KEEP)) + ": nothing in the newest abstracts settles the row "
                      "(notes per row in DESERVE.tsv)", CH]))
for k in sorted(SKIP):
    add.append("\t".join([k, SKIP[k], "not checked: the query matched only unrelated records; query again with "
                          "narrower words", CH]))
with io.open(p2, "a", encoding="utf-8", newline="") as f:
    f.write(head + "\n".join(add) + "\n")

MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Eighth batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Eighth batch, same day (deep-learning list, 65 rows T223..T289; dl_lit11.out; abstracts only):
- T283 low-degree conjecture: reported false in the polynomial-time binary form as well (arXiv 2607.20318, Mao), after
  the quasi-polynomial form (arXiv 2505.17360). A row needs a named corrected conjecture.
- T250 quantitative Tensor Programs: width^(-1/2) Wasserstein rates to the Gaussian-process limit for any architecture
  (arXiv 2607.06290); what remains is rates along training.
- T271 neural collapse under gradient training: proved for a two-layer ReLU network on orthogonally separable data
  (arXiv 2510.21078); the row must name the generality.
Sixty-two other rows unchanged. T244 and T279 not checked (queries matched unrelated records). A query built on one
common word pair (depth-to-width, flatness with scale-invariant) returns physics and economics; put the field word
(neural, network) in every query.
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("updated", len(UPD), "changed,", len(KEEP), "unchanged;", LIST, "rows still only title-read:", left)
