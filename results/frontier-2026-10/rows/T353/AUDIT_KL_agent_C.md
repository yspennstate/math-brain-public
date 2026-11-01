# T353 KL certificates, audit 2 (agent C, 19 Oct 2026 23:4x)

Object: agent_B/cert_kl_arb.py and its outputs cert_klpq_arb.txt, cert_klqp_arb.txt (sigma 1, T 2, g1 in
[-1.51, -1.49], 40 balls). Audit 1 is agent A's (AUDIT_KL_agent_A.md); this one was done without
reading it first.

Verdict: CONFIRMED. No fault that touches the conclusion. One harmless slip in a tail constant (below).

## What I checked

1. The densities against the construction in REFUTATION_T2.md. The script's (g1, g2) is the construction's with
   g1 shifted by +1 and g2 translated within each g1 slice: by -1 for ANTI and by +1 for SAME. A translation in g2
   at fixed g1 is applied to p and q together, so it leaves K(g1) unchanged. Then
   P = wa N_-1 + wc N_1 and Q = w0 N_-1 + wc N_0 (ANTI), and P = (wa + wc) N_1 and Q = w0 N_1 + wc N_0 (SAME),
   with wa, w0, wc = N(g1; -1)/2, N(g1; 0)/2, N(g1; 1)/2. This matches the script. Since p and q are joint
   densities, KL = int dg1 K(g1) exactly, and switching to SAME on [a, b] changes KL by exactly int_[a,b] (K_SAME - K_ANTI).
2. Tails. p - q <= p log(p/q) <= p^2/q - p, so |p log(p/q)| <= p + q + p^2/q. Each p^2/q bound was re-derived
   pointwise, using N_1^2/N_0 = e N_2 and N_0^2/N_1 = e N_-1, every centre in [-2, 2]. Mills' bound
   phi(t)/t per side gives T = 2 phi(28)/28 at L = 30. The four cases hold. The slip: in QP SAME the code has
   `E * wc ** 2 / wc`, which equals E wc, where the bound needs only E wc^2 / (wa + wc) times 2. Because wc < 1,
   the code's value is the larger one, so the bound stays valid (only looser), and at L = 30 it is about
   1e-170 in any case.
3. Arb. g1 enters as a ball, and every integrand evaluation encloses all g1 in it. With `analytic=True`, the log
   returns indeterminate on a box that meets the branch cut, and the division does the same on a box where q may
   vanish. acb.integral then subdivides, so the holomorphy that the error bound needs is checked, not assumed.
   `d > 0` is Arb's strict test (lower end > 0). The "[+/- 1.01e-3]" in the log is Arb printing a ball whose
   first digit is uncertain; the stated minimum lower end, 4.906e-4 PQ and 3.237e-4 QP, is what counts.
4. Independent numbers (audit_C/kl_indep_scipy.py: scipy quad in log-sum-exp form, densities rebuilt from
   the construction with NO shift):

   | | K_SAME - K_ANTI at script g1 -1.51 / -1.5 / -1.49 | true gain on [-1.51, -1.49] | certified >= |
   |---|---|---|---|
   | P||Q | 7.473e-4 / 7.541e-4 / 7.604e-4 | 1.508e-5 | 9.967e-6 |
   | Q||P | 4.583e-4 / 4.717e-4 / 4.853e-4 | 9.434e-6 | 6.724e-6 |

   The write-up's controls are reproduced: P||Q at script g1 -2 gives 2.848333e-4, and Q||P at -1.5 gives
   4.716512e-4. Every certified lower end lies below the true value, as it must.

## Scope

A KL gain refutes the dominating-pair conjecture only through Blackwell: hockey-stick domination at every
e^eps > 0, which is both directions at eps >= 0, implies every f-divergence is ordered. The two directions are
certified separately here, so the KL result stands under either reading of the definition. The hockey-stick
refutation at eps 0.5 (cert_t2_arb.py) does not need this step, and it remains the primary result. KL is a
second, independent witness.

Not covered in this section: the integer-order Renyi certificates (audited in AUDIT_RENYI_agent_C.md) and the
sigma 2 KL certificates (addendum below).

## Addendum, 23:43: sigma 2 (cert_kl_arb_sigma.py, cert_klpq_s2_arb.txt, cert_klqp_s2_arb.txt): CONFIRMED

The scaling is right. Mills at scale s gives P(X > t) <= s^2 N_s(t; 0) / t, and that is the script's gtail. Also
N_s(z, m1)^2 / N_s(z, m2) = exp((m1-m2)^2/s^2) N_s(z, 2 m1 - m2), so with |m1 - m2| = 1 every E becomes e^{1/s^2}
and every centre stays in [-2, 2]. The tail comment "N(mu, 1)" is stale, but the code uses scale s throughout.
Independent numbers (audit_C/kl_sigma_indep.py, unshifted, s = 2): the controls at script g1 -2 are
7.863494e-4 P||Q and 7.941336e-4 Q||P, matching the write-up. The true gains on [-2.01, -1.99] are 1.5727e-5 P||Q
and 1.5882e-5 Q||P, against certified lower bounds of 1.442e-5 and 1.484e-5. Both certified bounds are below the
true gains, as they should be.
