"""an agent, 13 Nov 2026: replace the five DL rows marked REPLACE by the five kept candidates (N05, N06, N04, N03,
N02), and restate PD14. Writes REPLACEMENTS_1113.tsv and appends PD14 to RESTATED_STATEMENTS.tsv (once)."""
import csv, io

ROWS = [
    ("T255", "N05", "solved by us on the repaired statement (17 Oct, triple audit)",
     "Learning coefficients of deep ReLU networks",
     "For a deep ReLU (or tanh) network of fixed widths, a realizable true parameter w0 and inputs from a compactly supported "
     "law with positive density, compute the real log canonical threshold of K(w) = E[(f_w(x) - f_w0(x))^2] at w0 as a "
     "function of the widths and of the true network's structure. The deep linear case is known (Aoyagi; Pepin Lehalleur and "
     "Rimanyi: half the codimension of the fibre); an exact algorithm exists only for two-parameter models.",
     "arXiv 2411.19920 (Pepin Lehalleur, Rimanyi), 2608.20183; abstracts read 11 Nov (NEW_DL_CANDIDATES.tsv N05)."),
    ("T303", "N06", "KLS conjecture: duplicate of retired probability row T018, not deep learning",
     "The neural feature ansatz for a gradient-trained two-layer network",
     "For f(x) = a^T sigma(W x) trained by gradient descent from small initialisation on a single-index target "
     "y = g(<theta, x>) with Gaussian x, prove that W^T W at the end of training is, up to a vanishing error, proportional to "
     "a power of the average gradient outer product E[grad f(x) grad f(x)^T] (the ansatz says the square root), or give a "
     "counterexample. Exact analysis exists only for linear recursive feature machines.",
     "arXiv 2610.09196 (Cheng, Kiani, Lu, Radhakrishnan); one search only, 11 Nov (N06)."),
    ("T314", "N04", "reported solved (Lee-Sandhu-Shi arXiv 2609.30590, unrefereed; also 2610.17717)",
     "The limit of iterated rectified flow",
     "For an absolutely continuous law mu on R^d, d >= 2, coupled with the standard Gaussian, does the k-fold rectified-flow "
     "coupling converge as k grows; is the limit straight (non-crossing transport paths); and is it the Brenier optimal "
     "transport coupling? Two steps are not straight in general: Pham, Roy, Rinaldo and Sarkar characterise when two-step "
     "rectified flow is straight for smooth strongly log-concave densities and Gaussian mixtures.",
     "arXiv 2610.36090v2 (Pham, Roy, Rinaldo, Sarkar), abstract read 11 Nov (N04)."),
    ("T352", "N03", "answered for full batch (2401.10371v7 Thm 3.3) and minibatch (2410.01068); see T352_READ.md",
     "A chain-of-thought learning separation for composition in S_5",
     "For the word problem of S_5 (composing n permutations), gradient-trained transformers with chain-of-thought tokens "
     "are known to learn state tracking. Prove the matching lower bound: gradient descent on the same constant-depth "
     "architecture without intermediate tokens needs superpolynomially many samples or steps (a gradient or "
     "statistical-query lower bound, not only the conditional TC0 versus NC1 expressivity separation).",
     "arXiv 2511.07378 (Huang, Wen, Singh, Chi, Chen), 2508.08222 (Yang, Huang, Liang, Chi); abstracts read 11 Nov (N03)."),
    ("T363", "N02", "duplicate of T269 (which margin gradient descent finds in homogeneous networks)",
     "The limit direction of sharpness-aware minimization on two-layer ReLU networks",
     "On linearly separable data, with the practical unnormalised l2 perturbation of fixed radius, does the normalised "
     "parameter of SAM on a two-layer homogeneous ReLU network converge in direction, to a KKT point of which margin "
     "problem, and does it differ from the max-margin KKT direction that gradient descent reaches (Lyu and Li; Ji and "
     "Telgarsky)? Diagonal linear networks are done (Moon, Si, Yun).",
     "arXiv 2603.08290 (Moon, Si, Yun), 2410.14802 (Li, Zhang, He); abstracts read 11 Nov (N02)."),
]

PD14 = ("PD14", "Global regularity in three dimensions for defocusing energy-supercritical wave and Schroedinger equations",
        "Prove or disprove that smooth compactly supported data give global smooth solutions for the defocusing wave "
        "equation u_tt - Laplacian u + |u|^(p-1) u = 0 on R^(1+3) for odd p >= 7, and for the defocusing Schroedinger "
        "equation i u_t + Laplacian u = |u|^(p-1) u on R^(1+3) for odd p with 7 <= p <= 25. Blow-up from smooth data is "
        "known for the Schroedinger equation at (d, p) = (3, 27), (4, 9), (5, 7) and for the real wave equation at p = 3, "
        "d >= 9; p = 5, d >= 7; p = 7, d >= 6; none of these covers the cases stated.",
        "arXiv 2609.23685 (Buck, Carballeira, Gomez-Serrano, Shi; computer-assisted), 2610.06678v3 (Cadiot, Ionescu, "
        "Palasek); abstracts read 11 Nov (GENERAL_LITCHECK). The open range is what those two abstracts leave; other "
        "constructions were not searched for on 13 Nov.")

with open("REPLACEMENTS_1113.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["old_id", "new_key", "why_old_leaves", "new_title", "statement", "sources"])
    w.writerows(ROWS)

txt = open("RESTATED_STATEMENTS.tsv", encoding="utf-8").read()
if not any(line.startswith("PD14\t") for line in txt.splitlines()):
    buf = io.StringIO()
    csv.writer(buf, delimiter="\t", lineterminator="\n").writerow(PD14)
    with open("RESTATED_STATEMENTS.tsv", "a", encoding="utf-8", newline="") as fh:
        if not txt.endswith("\n"):
            fh.write("\n")
        fh.write(buf.getvalue())
print("ok", len(ROWS), "replacements; PD14 present:", "PD14\t" in open("RESTATED_STATEMENTS.tsv", encoding="utf-8").read())
