# Ising perceptron capacity: working notes and reverification

Companion material for `papers/public/ising-perceptron-capacity`, the computer-assisted proof of the
Krauth--Mezard capacity prediction at kappa = 0 (Ding--Sun lower bound and Huang upper bound, with
their numerical hypotheses closed by Arb ball arithmetic).

- `notes/` the problem statement, the plans for verifying the Ding--Sun and Huang conditions, the
  obstruction at the degenerate point, and the arXiv submission note.
- `verification/huang_deep_replay.py` a deeper replay of the Huang-condition certificates.
- `reverification_2026_07_13/` an independent reverification of the released proof tree (tag v1.0)
  from fresh clones: full replays on two runtimes, high-precision and portable rechecks of the
  star-interior certificate, a symbolic audit of the closed-form identities, mutation tests of the
  Lean skeleton, and a finite-size scan. The README there gives the commits and every result; the
  logs are the raw output.
