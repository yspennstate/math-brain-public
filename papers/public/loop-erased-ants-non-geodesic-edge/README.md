# A non-geodesic edge that survives in the loop-erased ant process

Paper: `loop_erased_ants.pdf` (source `loop_erased_ants.tex`).

In the loop-erased ant process of Kious, Mailler and Schapira (Finding geodesics on graphs using reinforcement
learning, Ann. Appl. Probab. 32 (2022), arXiv:2010.04820), ants walk one after another from a nest N to a food source
F on a finite graph. Each ant steps along an edge with probability proportional to its weight, and then adds one to
the weight of every edge of the loop-erasure of its time-reversed trajectory. Conjecture 1.1(1) of that paper says
that the normalised weight of an edge has a non-zero limit exactly when the edge lies on a geodesic from N to F.

Let G_l be the graph made of a triangle N, u, v and two paths of l edges, one from u to F and one from v to F. The
paper proves that on G_l the normalised weights converge almost surely: to rho on the edges of the path N, u, ..., F,
to 1 - rho on the edges of the path N, v, ..., F, and to (1 - 1/l) rho (1 - rho) on the edge uv, where rho is a
non-degenerate random variable in (0, 1).

For l >= 2 the edge uv lies on no geodesic and keeps a positive share of the weight, so the conjecture fails on G_l.
For l = 1 the graph is the losange, the edge uv dies, and the theorem gives for the loop-erased rule the convergence
proved by Kious, Mailler and Schapira for the uniform-geodesic rule.

## Files

- `code/sim_ants.c` simulates the process as it is defined (walk, reversal, chronological loop erasure, +1 on the
  path). `sim_ants run l ants seed` prints the normalised weights at n = 10^3, 10^4, ...;
  `sim_ants freeze l A B C D R ants seed` keeps the weights fixed and compares the frequencies of the four paths
  with Lemma 6.
- `code/check_path_law.py` (SymPy) lists the spanning trees of G_l for l = 1, ..., 5, checks Lemma 6 against them,
  and checks the drift identities of Lemma 7.
- `data/run_l<l>_s<seed>.txt` are the runs of Table 1 (10^8 ants each), `data/freeze_out.txt` the fixed-weight
  frequencies quoted in Section 5, and `data/check_path_law_out.txt` the output of the symbolic check.

## Running

    cc -O2 -o sim_ants code/sim_ants.c
    ./sim_ants run 2 100000000 1
    ./sim_ants freeze 2 2 3 1 4 2 2000000 1
    python3 code/check_path_law.py
