# Convergence of the forward-loop-erased ants process at distance two

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

In the forward-loop-erased ants process, the nth ant walks from a nest N to a food source F with transition probabilities proportional to the current edge weights, and every edge of the chronological loop erasure of its path gains weight one. Armfield and Mailler (arXiv:2610.18453) showed that when N and F are at distance two the ants find the shortest paths, and left open whether W(n)/n converges. The paper shows that it converges almost surely and that every path of length two keeps a positive share in the limit. The key fact is that for a common neighbour i of N and F the relative drift of the product W_{N,i}(n) W_{i,F}(n) is the inverse effective conductance between N and F, the same for all i, up to a summable error; hence ratios of these products converge on every finite graph.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/simulate.py`: checks the two edge identities of Lemma 2.1 against 200,000 simulated loop-erased paths on two graphs, and runs the process from unit weights to n = 100,000 with three seeds on each graph (the table in Section 5). Run `python3 simulate.py`; it needs Python 3 with numpy and takes about 30 seconds.
- `SHA256SUMS`: sha256 of each file above.
