# Pair meeting times can concentrate while coalescence is slow

Yitzchak Shmalo, 16 November 2026.

Archived on Zenodo: [doi:10.5281/zenodo.24274954](https://doi.org/10.5281/zenodo.24274954).

For coalescing random walks driven by a chain with uniform stationary law, Aldous (Bernoulli 19, 2013; arXiv:1309.6766, Open Problem 2) asked what conditions, beyond concentration of the mean meeting times of pairs from independent uniform starts, give a mean coalescence time asymptotic to twice the stationary mean meeting time tau. The paper studies a weighted complete graph on m vertices joined to a two-vertex trap with scale r. The pair means concentrate exactly when r = o(m), and in every fixed L^p exactly when r = m^{o(1)}. Then tau ~ m, while the coalescence time divided by 2mr tends to a mean-one exponential law in Wasserstein distance, with all moments. With r = log m the ratio of the mean coalescence time to 2 tau grows like log m. Both stages of the plan Aldous proposed hold; the hand-off between them fails, because once few walkers remain, one of them sits in the trap. The worst-start mixing time is at least of order mr, much larger than tau.

## Files

- `main.tex`, `main.pdf`: the paper.
- `CREDITS.md`: which statements are known and which are new, and whose work they rest on.
- `checks/check_exact.py`: verifies the identities of Sections 2 and 3 symbolically (SymPy), then for small m and rational epsilon builds the graph, solves the meeting-time equations on all ordered pairs and the coalescing chain on all occupied subsets in exact rational arithmetic, and compares them with the closed forms and with the bounds of Theorem 3.2. Needs Python 3 and SymPy; runs in a few minutes. Its output is in `checks/output.txt`.

## License

The paper is licensed CC BY 4.0 and the code MIT.
