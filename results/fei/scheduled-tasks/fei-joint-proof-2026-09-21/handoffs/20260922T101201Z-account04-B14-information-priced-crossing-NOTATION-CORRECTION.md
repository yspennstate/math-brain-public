# B14 notation correction — physical block values are not spectral support bits

This supplements `20260922T101201Z-account04-B14-information-priced-crossing.md` without changing its proved inequalities.

In the posterior-information theorem, write `Z_A` for the **physical cube values revealed on original-coordinate block A**. Then

`U=P(eta_j=1|Z_A)` and `I(eta_j;Z_A)>=h2(p_j)-h2(p_j-c_j(A))`.

Account01/B18 instead uses `X` for the **spectral support indicator vector**, with `B_A=H(X_A|X_{A^c})`. These are distinct random objects. This run proves no direct inequality relating `I(eta_j;Z_A)` to `B_A`.

The realizable stopping budget remains exact and unchanged:

`sum_v pi_v B_{A_v} <= K sum_v pi_v D_{A_v} <= K J(root)`

because it uses only the admission condition `B_A<=K D_A` and drift telescoping. The bridge between forced physical posterior information and spectral curvature/Shannon currencies remains the next **unproved** implication.

Scientific addendum: `yspennstate/math-open-problems`, commit `234ed5baf34886444781151a85fd9b4d3606a1ee`, path `proofnet24/P03-fei/fleet-2026-09-22/account04/B14/20260922T101201Z-information-priced-crossing/NOTATION_CORRECTION.md`.
