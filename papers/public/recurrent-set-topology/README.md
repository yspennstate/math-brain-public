# The topology of the recurrent and transient sets of homogeneous random walks

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

Each point a of a simplex A defines the random walk on a finitely generated abelian group that takes the i-th step of
a fixed finite set S with probability a_i. Li, Mossel and Weiss (Ann. Appl. Probab. 36 (2026), 4291-4310; arXiv:2403.04108, Section 6) asked when the set R of
recurrent walks is path-connected or simply connected, and when the set R^c of transient walks is path-connected,
simply connected or convex. The paper answers these questions in terms of the projections v_i of the steps to the free
part Z^n of the group.

- If some step projects to 0, R is star-shaped. If the v_i span a space of dimension at most 2, R is convex.
- Otherwise R is homotopy equivalent to the bipartite graph whose vertices are the lines and planes through the origin
  on which the steps balance, a line joined to each plane containing it. So R is path-connected exactly when this
  graph is connected, and simply connected exactly when it is a tree.
- R^c is empty when every v_i is zero, and otherwise contractible unless 0 lies in the relative interior of the convex hull of the v_i and the v_i span a line or a
  plane; then R^c has two contractible components or is homotopy equivalent to a circle.
- R^c is convex exactly when every recurrent walk is positive recurrent.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/check_nerve.py`: for random step sets with no zero step and rank at least 3, builds the cover of R by the
  polytopes C_V, decides every intersection by linear programming, and compares the Betti numbers of the nerve with
  those of the line-plane graph. `python check_nerve.py 300 1`.
- `code/check_more.py`: the same comparison on step sets biased towards cycles, and a count of the components of R^c on
  a rational grid of the simplex against the predicted count. `python check_more.py 200 150 7`.

Both scripts need Python 3 with numpy and scipy. All runs reported in Section 5 of the paper gave no mismatch.

`SHA256SUMS`: sha256 of each file above.
