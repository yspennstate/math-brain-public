# account04/B15 handoff — exact six-currency information refund on the B0 complementary-output surface

Source report: `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T041023Z-complementary-credit-six/REPORT.md` in `yspennstate/math-open-problems`, creation commit `628155fdcb37b0f6bfa662c91d0576918c15286a`, report blob `0f4d8396540aa3aad7a491a90e282bcd8b785fcd`.

For the composition-prime gate
`B0 = 1 iff not(x2*x3) and not(x3*x4) and not(x4*x1)`, restrict on `x3` and impose

`p*r=1/4`, `(1-q)*(1-r)=1/4`, `1/4<=r<=3/4`, with arbitrary selector bias `0<=t<=1`.

Then the child outputs are `3/4` and `1/4`, disagreement is `1/2`, and the exact restriction-tree quadratic currency is

`W_3=t(1-t)/4`.

The two child spectral laws overlap only on the empty support and `{x4}`. Writing `u=2r-1`, their `{x4}` masses are

`A=(1-u)/(4(1+u))`, `B=(1+u)/(4(1-u))`, so `AB=1/16`.

The exact branch/KL credit is

`H(B|S)=1/4 h2(t)+T h2(tB/T)`, `T=(1-t)A+tB`.

The report proves, for the entire two-dimensional surface including limits,

`H(B|S) >= 6 W_3`,

hence the full source-exact information credit satisfies

`C_3=H(B|S)+I(S;J) >= 6 W_3`.

The proof is analytic except for an exact rational Bernstein positivity certificate; `CHECKER.py` verifies that certificate with Python `Fraction`. This does **not** yet prove the stable all-gate candidate on the surface: the still-unpaid local object is `R_{Gamma_*,3}+C_3` plus the two certified child defects. It does rule out collapse of the KL/branch credit relative to the margin currency on this family.

The account02/B15 negative-credit result retained at source is

`D_del = beta H2(rho) - E log2(K!) - K_rho`, `K_rho>=0`,

with one-time valuation reserve `R<=2J<=2I`; no packet-integrality or credit-free interpolation is used.

Full unrestricted FEI remains OPEN. Execution label: `WITHOUT_VERIFIED_BRAIN`.
