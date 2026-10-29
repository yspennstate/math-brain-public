# Frontier rows

Records of single rows of the top-400 frontier board (probability T001-T222, deep learning T223-T422) whose result passed an
independent check. Each folder keeps the row's dossier (the statement, the literature, the obstruction and every result in order),
the scripts behind each numerical claim with their outputs, and the second agent's audit or referee report. Agents are named by
letter inside each row.

| Row | Question | Result | Checks |
|---|---|---|---|
| `T417/` | Does heavy-ball momentum beat SGD in mean square on Gaussian least squares at batch size B? | The optimally tuned speedup is S(B) = Theta(min(max(1, B h_max/tr H), sqrt kappa)), with explicit constants 1/16 and 64/3 for kappa >= 4. The same dichotomy, in a high-dimensional finite-sum limit, is in Lee, Cheng, Paquette and Paquette (arXiv:2206.01029); the version here is non-asymptotic and streaming. | proved by hand plus exact root isolation; the lower-bound proof re-derived independently in `audit/` |
| `T362/` | Last-iterate rate of SGD with random reshuffling, tight in kappa | On the one-dimensional two-curvature quadratic instance the bias-side last-iterate error is Theta(G^2 ln^2 T / (mu T^2)), worst case over the start; exact recursion, Monte Carlo and sweeps over every condition-number regime. One instance, not the general bound. | refereed in `referee/` |
| `T352/` | Renyi privacy of hidden-state noisy SGD on nonconvex losses: does the time-uniform plateau decrease with n? | The question as posed is answered by arXiv:2401.10371. The convergent nonconvex bound of Chien and Li (arXiv:2410.01068, Theorem 3.7) has an n-free floor: its limit in T is at least alpha D^2 (2 eta L D^(lam-1) + eta^2 L^2 D^(2 lam - 2)) / (2 sigma^2) for every n. | one audit, CONFIRMED |
| `T353/` | Exact privacy of DP-SGD with shuffled batches: Conjecture 3.2 of Chua, Ghazi, Kamath, Kumar, Manurangsi and Sinha (arXiv:2403.17673) on the worst-case pair for one epoch | Refuted for every T >= 2 at s = 1, eps = 1/2: an adaptive query method beats the conjectured pair. Ball-arithmetic certificates at T = 2 and T = 3 and a reduction from T = 3 to every T. | each of the three steps audited twice, CONFIRMED |
| `T354/` | Where Adam settles with the hyperparameters used in practice | Under a vanishing step, Adam (PyTorch form, bias correction on) settles at the zero x* of the frozen-x drift, x* = (1 - beta2) K r B3 / (2 abar B2) (1 + O(1 - beta2)) with r = sqrt(B2)/(sqrt(B2) + eps); K is given for with-replacement sampling and in closed form under reshuffling. Scalar model and its coordinatewise vector form. | audited, CONFIRMED on a distribution the note had left untested |
