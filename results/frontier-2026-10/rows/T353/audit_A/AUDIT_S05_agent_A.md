# Audit of the sigma 0.5 certificates (agent A, 19 Oct 2026)

Files audited (agent_B/, pushed 8d14956d): cert_klpq_s05_arb.txt, cert_klqp_s05_arb.txt (cert_kl_arb_sigma.py 0.5),
cert_renyipq2_s05_arb.txt, cert_renyipq3_s05_arb.txt, cert_renyiqp2_s05_arb.txt, cert_renyiqp3_s05_arb.txt
(cert_renyi_arb_sigma.py 0.5), with the argv of run_kls05_*.cmd and run_rs05_*.cmd.

Verdict: the six certificates hold. One formal gap in the cover, now closed; no number changes.

## 1. Values (s05_audit.py, s05_audit_run1.txt)
S - A was recomputed from the raw densities with mpmath (dps 50, breakpoints every sigma/2 on [-6, 6]) at each certified point
and at 2-4 scan points per case, 24 points in all. Every arb difference agrees with the mpmath one to double precision, including
the KL PQ point at g = -1.4 where S - A = 1.3107e-7 on values near 1.04. Signs agree at the scan points where the difference is
negative (KL QP at -0.8, order 2 PQ at -1.6, order 3 PQ at -2.0), so the certified intervals are not chosen across a sign error.

## 2. Tails
The tail bound is the sigma-general one audited at sigma 2 (AUDIT_KL_S2, AUDIT_RENYI_S2). At sigma 0.5, E = exp(1/s^2) = e^4 and
L = 30 s = 15, so the Mills factor is about e^-392. It cannot affect any of the six results.

## 3. Gain arithmetic
min lower end x interval width reproduces each reported gain. The fourth digit of the order 3 PQ gain (2.59658e-17 against
1.2981e-5 x 2e-12 = 2.5962e-17) is the float width: -2.349999999999 - (-2.350000000001) = 2.000178e-12 in binary, and
2.59658e-17 / 2.000178e-12 = 1.29817e-5, inside the printed ball. The certified interval is the float one, and the gain is computed
on it, so this is correct.

## 4. The cover (the one finding)
Each ball was built as arb((lo + hi)/2, (hi - lo)/2). The midpoint is rounded to a double, and the radius is not widened for that
rounding. In 4 of the 5 sigma 0.5 argv sets some sub-interval endpoints lie outside their ball, by at most 2.2e-16:
KL PQ 5 of 40 endpoints, KL QP 8 of 40, order 3 PQ 4 of 20, the two -0.5 QP runs 12 of 40; order 2 PQ none. The sigma 1 and
sigma 2 intervals (width 1e-3 per ball) have none. Strict positivity on each ball was never in doubt, but "> 0 on all of [a, b]" and
the gain sum, which counts each sub-interval's full width, were not fully covered.
Re-certification with g = arb(lo).union(arb(hi)), which contains [lo, hi] exactly, same functions, intervals and ball counts
(s05_recert_exact_cover.py, s05_recert_exact_cover_run1.txt): all six CERTIFIED, with min lower ends and gains identical to the
originals to the printed digits:
  KL PQ 9.3520e-8 / 1.87040e-14,  KL QP 5.5837e-7 / 1.11673e-13,  order 2 PQ 3.3736e-7 / 6.74720e-17,
  order 3 PQ 1.2981e-5 / 2.59658e-17,  order 2 QP 0.0014407 / 2.88137e-11,  order 3 QP 0.23973 / 4.79457e-9.
The peer's new script cert_renyi_real_arb_sigma.py already builds its balls this way.

## 5. What the sigma 0.5 results say
The P||Q gains are tiny (1e-14 KL, 1e-17 Renyi) because the certified intervals are tiny: the difference S - A is 1e-7 to 1e-5 there
while arb's enclosure slack grows linearly in the ball width, so wide balls cannot separate it. They are strict and rigorous, which
is all the T2 refutation needs; they are not estimates of the size of the gain.
