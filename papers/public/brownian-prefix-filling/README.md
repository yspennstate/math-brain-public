# A Brownian piece in front of a process absolutely continuous with respect to Brownian motion

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in `paper/main.tex`).

Burdzy and Scheutzow (Forward Brownian motion, Probab. Theory Related Fields 160 (2014), Problem 7.5) asked whether,
for every process (X_t, t >= 0) whose law is equivalent to Wiener measure, one can put a random piece of path in front
of X so that the new process is a Brownian motion.

The paper proves:

1. Yes, and absolute continuity with respect to Wiener measure is enough: on an extension of the probability space
   there are a standard Brownian motion B and an almost surely finite random integer N >= 0 with X_t = B_{N+t} - B_N
   for all t >= 0, so the piece (B_t, 0 <= t <= N) put in front of X gives B. The time N cannot in general be a
   stopping time for B.
2. For an invertible measure-preserving map θ of a probability space (E, P) and a target law fP, a forward shift
   θ^N with N built from a P-distributed point and independent uniforms carries P to fP if and only if
   E[f | I] = 1, where I is the invariant σ-field. Without the auxiliary uniforms only integer-valued densities can
   be reached.

The construction is Rost's filling scheme (Chacon-Ornstein, Rost 1971) for the unit shift of two-sided Brownian
motion, the tool Pitman and Tang (Patterns in random walks and Brownian motion, 2015) use to embed meanders.

## Files

- `code/checks.py` runs the filling recursion in exact rational arithmetic on permutations of finite sets
  (orbit-balanced targets are filled within |E| steps, unbalanced ones leave a positive residual) and on the
  Bernoulli shift with cylinder targets (equal remaining masses, decreasing residual, a Monte Carlo run of the
  randomized rule against the exact accepted law), and checks the integer-density remark on cycles.
  `code/checks_output.txt` is its output (`python checks.py`, standard library only).
