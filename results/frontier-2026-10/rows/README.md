# Frontier rows

Records of single rows of the top-400 frontier board (probability T001-T222, deep learning T223-T422) whose result passed an
independent check. Each folder keeps the row's dossier (the statement, the literature, the obstruction and every result in order),
the scripts behind each numerical claim with their outputs, and the second agent's audit or referee report. Agents are named by
letter inside each row.

| Row | Question | Result | Checks |
|---|---|---|---|
| `T417/` | Does heavy-ball momentum beat SGD in mean square on Gaussian least squares at batch size B? | The optimally tuned speedup is S(B) = Theta(min(max(1, B h_max/tr H), sqrt kappa)), with explicit constants 1/16 and 64/3 for kappa >= 4. The same dichotomy, in a high-dimensional finite-sum limit, is in Lee, Cheng, Paquette and Paquette (arXiv:2206.01029); the version here is non-asymptotic and streaming. | proved by hand plus exact root isolation; the lower-bound proof re-derived independently in `audit/` |
| `T362/` | Last-iterate rate of SGD with random reshuffling, tight in kappa | On the one-dimensional two-curvature quadratic instance the bias-side last-iterate error is Theta(G^2 ln^2 T / (mu T^2)), worst case over the start; exact recursion, Monte Carlo and sweeps over every condition-number regime. One instance, not the general bound. | refereed in `referee/` |
