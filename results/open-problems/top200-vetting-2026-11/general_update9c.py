"""Record the arXiv checks of 11 Nov, deep-learning list, third file (dl_lit13.out): rows T357..T422 of q13.txt
except thirteen whose queries matched only unrelated records (queried again in q14.txt); extend the memory."""
import io
import os
import shutil

LIST = "TOP200_DL"
CH = "2026-11-11 abstracts read on arXiv (dl_lit13.out), an agent"
SKIP = {"T357": "Overconfidence of overparameterized classifiers",
        "T358": "Intrinsic robustness of natural data distributions",
        "T361": "Emergence of skills from random skill graphs",
        "T379": "How much must calibrated language models hallucinate?",
        "T384": "Heavy-tailed weights at infinite width",
        "T387": "Does a curriculum provably speed up SGD on sparse parities?",
        "T391": "Diffusion models adapt to the intrinsic dimension",
        "T392": "What classifier-free guidance does to the sampled distribution",
        "T395": "Deep-learning PDE solvers and the curse of dimensionality",
        "T396": "Oversmoothing in deep graph neural networks",
        "T399": "When does next-token prediction fail to learn planning tasks?",
        "T409": "Testing the manifold hypothesis",
        "T411": "The computational complexity of posterior sampling with diffusion priors"}
with io.open("q13.txt", encoding="utf-8") as f:
    IDS = [ln.split()[0] for ln in f if ln.strip()]
IDS = [k for k in IDS if k not in SKIP]
UPD = {
    "T416": ("CHECK_STATEMENT",
             "arXiv 2602.12107 answers one form in the negative: Q*-realizability and Bellman completeness are not "
             "sufficient for sample-efficient offline reinforcement learning under partial coverage (an "
             "information-theoretic lower bound). The row must say which coverage question is still asked"),
    "T412": ("CHECK_STATEMENT",
             "convergence guarantees now exist in some generality: bounds free of the vocabulary size in any integral "
             "probability metric, for masked and uniform priors (arXiv 2605.17232), and minimax optimality under "
             "sparsity (arXiv 2610.19020). The row must say which bound is asked"),
}
NOTE = {
    "T359": "no change (capacity scaling of spectral optimizers on linear associative memory, arXiv 2603.26554)",
    "T362": "no change: arXiv 2611.07406 states that random reshuffling dominates SGD for smooth convex problems, "
            "arXiv 2610.19444 gives a last-iterate bound with large steps; abstracts only, the optimal rates in the "
            "other regimes are open",
    "T364": "no change (an algorithm through Koszul-Young flattenings, arXiv 2411.14344; the landscape is open)",
    "T366": "no change (an exact operator identity for i.i.d. task sampling, arXiv 2604.13460)",
    "T368": "no change (a fixed number of large steps reaches any accuracy on separable multiclass logistic "
            "regression, arXiv 2610.26748)",
    "T369": "no change: exponential convergence of semi-gradient TD for two-layer networks in the mean-field regime "
            "under an entropy condition (arXiv 2610.20014); without that condition it is open",
    "T377": "no change (linear models, arXiv 2605.05742; random features, arXiv 2610.09044)",
    "T381": "no change (arXiv 2604.12051, 2602.15323)",
    "T382": "no change (arXiv 2510.21888)",
    "T390": "no change (finite-sample bounds for exponential families, arXiv 2605.14168)",
    "T393": "no change (minimax optimality of the Wasserstein GAN estimator, arXiv 2311.18613; trained networks open)",
    "T397": "no change: for message passing on the sparse contextual block model the value of depth is governed by "
            "the Kesten-Stigum ratio (arXiv 2607.16676); trained networks are open",
    "T408": "no change (arXiv 2609.07031)",
    "T413": "no change (error bounds for multistep sampling under stability assumptions, arXiv 2610.03414)",
    "T418": "no change, the statement check stands: UCB-style algorithms reach near-optimal regret under Gaussian "
            "noise by data thinning (arXiv 2610.28136)",
    "T421": "no change (arXiv 2611.08358)",
}
KEEP = {k: NOTE.get(k, "no change") for k in IDS if k not in UPD}
assert len(IDS) == 53 and len(set(IDS)) == 53 and len(KEEP) == 51 and not set(NOTE) - set(KEEP)

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
                          "narrower words (q14.txt)", CH]))
with io.open(p2, "a", encoding="utf-8", newline="") as f:
    f.write(head + "\n".join(add) + "\n")

MD = "~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/"
MR = "~/brain-repo/01_ai_consciousness/claude/memory/"
m2 = "general_top200_four_rows_reported_settled_in_2026_2026_11_11.md"
with io.open(MD + m2, encoding="utf-8", newline="") as f:
    b = f.read()
bnl = "\r\n" if "\r\n" in b else "\n"
assert "Tenth batch, same day" not in b
b = b.rstrip("\r\n") + bnl + ("""
Tenth batch, same day (deep-learning list, 53 rows T357..T422; dl_lit13.out; abstracts only):
- T416 offline reinforcement learning, coverage: Q*-realizability with Bellman completeness is not enough under
  partial coverage (arXiv 2602.12107); T412 discrete diffusion: vocabulary-free convergence bounds exist (arXiv
  2605.17232). Both rows must say what more they ask.
Fifty-one other rows unchanged; thirteen rows not checked (off-topic hits), queued in q14.txt. A two- or three-word
query on a deep-learning row returns applied papers first; a first query needs a theory word (theorem, prove, lower
bound, sample complexity) next to the topic.
""").replace("\n", bnl)
with io.open(MD + m2, "w", encoding="utf-8", newline="") as f:
    f.write(b)
shutil.copyfile(MD + m2, MR + m2)
print("updated", len(UPD), "changed,", len(KEEP), "unchanged;", LIST, "rows still only title-read:", left)
