Open problem C0153. Source: G. Pete, "Probability and Geometry on Groups" (lecture notes, https://math.bme.hu/~gabor/PGG.pdf,
current version), Question 14.19, p. 215: if finite graphs G_n converge locally weakly to a nonamenable transitive graph G, is the
local limit of the FK(p,q) random-cluster measures on G_n (especially q > 1) the wired measure on G? Known for the WUSF
(q = p = 0 limit) and for Ising on regular trees (Montanari-Mossel-Sly: a symmetric mixture of plus and minus). Read the source
for the exact wording (which p, which q, which notion of local limit, whether the free measure is excluded by design).

Do this, in order, saving as you go:
1. Literature first. Get the source text into sources/ (plain text only). Search: Dembo-Montanari ("Ising models on locally
   tree-like graphs"), Dembo-Montanari-Sun ("Factor models on locally tree-like graphs"), Dembo-Montanari-Sly-Sun ("The
   replica symmetric solution for Potts models on d-regular graphs"), Basak-Dembo ("Ferromagnetic Ising measures on large locally
   tree-like graphs"), Helmuth-Jenssen-Perkins ("Finite-size scaling, phase coexistence, and algorithms for the random cluster
   model on random graphs", 2020-2023), Bencs-Borbenyi-Csikvari (random cluster on large girth graphs), Coja-Oghlan et al.
   (Potts on random regular graphs, metastability), Lyons ("The Ising model and percolation on trees and tree-like graphs"),
   Haggstrom (random-cluster on trees), Jonasson, and 2014-2026 work. Determine for which (p, q) the local limit on random
   d-regular graphs (and on general sequences converging to a regular tree) is known, and whether it is the wired measure, the
   free measure, or a mixture (at the critical point, below the uniqueness threshold, etc.). If a printed theorem decides the
   question (for instance a range of p where the limit is the FREE measure, which differs from the wired one on the tree), give the
   theorem and page and stop with RESOLVED_IN_LITERATURE, stating for which p and q.
2. Understand: on the d-regular tree the free and wired FK measures differ on an interval of p (nonuniqueness); on large-girth
   finite graphs the cycles act as a boundary. Explain which phenomenon decides the limit and why q = 2 (Ising) gives the plus/minus
   mixture, consistent or not with "wired".
3. Prove what you can, with complete proofs: the answer on random d-regular graphs for some range of p (via the Bethe free
   energy / belief propagation fixed points and known results), and an explicit counterexample sequence G_n (for example, graphs
   converging to the tree with a different boundary effect) if the general statement fails.
4. Compute (evidence only): Swendsen-Wang / Chayes-Machta sampling of FK on random 3- and 4-regular graphs, n up to 10^5, for
   q in {1.5, 2, 3, 5} across p, comparing local edge densities with the free and wired tree values.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
