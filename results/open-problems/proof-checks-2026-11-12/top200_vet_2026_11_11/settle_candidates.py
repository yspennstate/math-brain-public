"""Write the literature status of the eight NEW_DL_CANDIDATES rows (abstracts read 11 Nov 2026, files
cand_lit.out, cand_abs1.out, arxiv_cand_check1.xml, arxiv_cand_check2.xml). Adds the column verdict_2026_11_11."""
import csv

SRC = "abstract read on arXiv 2026-11-11, an agent"
S = {
 "N01": ("DROP_AS_STATED_RESTATE_AS_WIDTH",
         "SOLVED as stated: Bakaev-Brunck-Hertrich-Stade-Yehudayoff (arXiv 2505.14338, STOC'26) disproved the "
         "ceil(log2(n+1)) conjecture; Brunck et al. (arXiv 2610.28587v1, Oct 2026, unrefereed) prove every ReLU network "
         "is exactly simulated with two hidden layers, so the depth is 2. What is open is size: two hidden layers "
         "compute max of N numbers with widths O(N^2) and 2^{O(N log N)} (Zimmermann 2610.26795), and Safran "
         "(2601.01417) gives width Omega(d^{1+1/(2^{k-2}-1)}) at depth 3 <= k <= log2 log2 d. Restated problem: is "
         "max of n numbers computable exactly by a two-hidden-layer ReLU network of size polynomial in n?"),
 "N02": ("KEEP_LOW",
         "OPEN: diagonal linear L-layer networks are done (Moon-Si-Yun 2603.08290: l2-SAM reaches the l1 max-margin "
         "direction at L = 2, l-infinity-SAM depends on initialisation); scale-invariant two-block problems in "
         "Li-Zhang-He 2410.14802. No result found for a nonlinear two-layer model. The row needs a sharp statement "
         "(limit direction of l2-SAM on a two-layer homogeneous ReLU network on separable data)."),
 "N03": ("KEEP_LOW_RESTATE",
         "PARTLY DONE: beyond parity, gradient-trained transformers with chain of thought provably learn state tracking "
         "with length generalisation (Huang-Wen-Singh-Chi-Chen 2511.07378) and path-finding in trees "
         "(Yang-Huang-Liang-Chi 2508.08222). Neither abstract states a lower bound without chain of thought, so the "
         "separation with matching lower bounds is open outside parity. Restate with one named task."),
 "N04": ("KEEP_RESTATE",
         "NARROWED: Pham-Roy-Rinaldo-Sarkar (2610.36090v2) characterise when two-step rectified flow is straight for "
         "smooth strongly log-concave densities and Gaussian mixtures and construct non-straight couplings otherwise. "
         "So two steps are not always straight. Open: the limit of the k-fold rectification as k grows, for general laws."),
 "N05": ("KEEP",
         "OPEN: the deep linear case is done (Aoyagi; Pepin Lehalleur-Rimanyi 2411.19920: threshold C/2 with C the "
         "codimension of the fibre); an exact algorithm exists only for two-parameter models (2608.20183). No exact "
         "learning coefficient found for deep ReLU or tanh networks."),
 "N06": ("KEEP",
         "OPEN: exact analysis found only for linear recursive feature machines (Cheng-Kiani-Lu-Radhakrishnan "
         "2610.09196). One search query only; no proof for a nonlinear gradient-trained network among the hits. "
         "The row must name the model."),
 "N07": ("RESTATE_MERGE_WITH_H35",
         "SETTLED WITH PADDING: averaging-hard-attention masked pre-norm transformers with polynomial padding recognise "
         "exactly FO-uniform TC0 (Merrill-Sabharwal 2505.18948v2); growing-precision padded transformers reach L-uniform "
         "TC0 regardless of width (Svete-Merrill-Cotterell-Sabharwal 2605.30523). Open: the same question without "
         "padding. Overlaps agent's H35; keep one row."),
 "N08": ("DROP",
         "MOSTLY SETTLED: Gronich-Vardi (2602.16340v3) show Adam without the stability constant converges to KKT points "
         "of the l-infinity margin problem on smooth homogeneous models under a decaying learning rate; Gronich-Vardi "
         "(2611.01929) show that for constant or weakly decaying schedules (alpha > 1/L - 1/2) Adam has no "
         "trajectory-independent margin bias on deep linear networks. What is left (non-smooth ReLU, positive "
         "stability constant) is too narrow for a top-200 row."),
}

with open("NEW_DL_CANDIDATES.tsv", encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
head = rows[0]
if "verdict_2026_11_11" not in head:
    head.append("verdict_2026_11_11")
iv, ist = head.index("verdict_2026_11_11"), head.index("status")
for r in rows[1:]:
    while len(r) < len(head):
        r.append("")
    v, s = S[r[0]]
    r[ist] = s + "  [" + SRC + "]"
    r[iv] = v
with open("NEW_DL_CANDIDATES.tsv", "w", encoding="utf-8", newline="") as f:
    for r in rows:
        f.write("\t".join(r) + "\n")
print(len(rows) - 1, "rows;", ", ".join(r[0] + "=" + r[iv] for r in rows[1:]))
