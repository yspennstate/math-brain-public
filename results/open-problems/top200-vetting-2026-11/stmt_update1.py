"""Update STATEMENT_PASS.tsv rows T418 and T391 after reading the arXiv abstracts (stmt_lit2.out)."""
U = {
 "T418": ("KEEP_RESTATE", "the minimax rate of the problem is attained by elimination-type algorithms, so the title overstates what is open. "
          "For GP-UCB itself: in the Bayesian setting it attains sqrt(T) up to logarithms under a Matern kernel of sufficient smoothness and "
          "under the squared exponential kernel (Iwazaki, arXiv 2506.01393v4); in the RKHS setting its known bound is still suboptimal "
          "(stated in Takeno-Iwazaki-Takeuchi, arXiv 2610.28136, Oct 2026, who get near-optimal bounds only for a thinned variant under Gaussian noise). "
          "Restate as: does GP-UCB attain the optimal regret in the RKHS setting for Matern kernels?",
          "2026-11-11 abstracts read on arXiv, an agent"),
 "T391": ("REPLACE_OR_RESTATE", "the part the row calls open (step counts free of the ambient dimension) is answered: Liang-Huang-Chen "
          "(arXiv 2501.12982v3) prove iteration complexity of order k/eps in total variation for DDIM and DDPM, k an intrinsic dimension, "
          "with exact scores and with learned scores; Roy-Rinaldo-Sarkar (2601.15500v4) do the same for rectified flow. A row survives only "
          "as the end-to-end minimax statement (score estimation and sampling in one theorem with a matching lower bound).",
          "2026-11-11 abstracts read on arXiv, an agent"),
}
with open("STATEMENT_PASS.tsv", encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
n = 0
for i, l in enumerate(lines):
    p = l.split("\t")
    if p and p[0] in U:
        v, r, c = U[p[0]]
        lines[i] = "\t".join([p[0], v, r, c]); n += 1
with open("STATEMENT_PASS.tsv", "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(lines))
print("rows updated:", n)
