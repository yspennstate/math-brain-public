# T354: momentum, uniform in n, audit 2 (agent C, 20 Oct 2026 09:0x)

Object: agent_B/NOTE.md, "Momentum, uniform in n", as revised after audit 1 (agent A, NOTE 530db612). Two claims are
tested:
- x* = x0(beta1)(1 + O(d/K_rr(beta1))) uniformly in n at fixed beta1, with x0(beta1) = d K_rr(n, beta1, beta2) B3/(2 B2);
- the sentence in "c(n d) in closed form": "the same c holds at every fixed beta1". Audit 1 checked it on 9/-1 only, where r1 = r2.

Verdict: CONFIRMED, on a three-valued b with r1 != r2.
- At beta1 0.5 the exact roots extrapolated to d = 0 give c = -0.4771 at n d 1 and -0.2267 at n d 2. The beta1 = 0 closed form gives
  -0.4775 and -0.2268.
- At beta1 0.9, n d 1, the d -> 0 sequence is slower but heads to the same value: the Richardson extrapolations of order 1, 2 and 3
  give -0.448, -0.470 and -0.474 through n 400. Adding n 800 (d 0.00125) moves them to -0.469, -0.476 and -0.477, and order 4 gives
  -0.4773 against -0.4775.
- So beta1 moves x*/x0(beta1) only at O(d^2), as the note says. The d^2 coefficient is large at beta1 0.9: the raw rows change by about
  20 per unit d there, against about 3 per unit d at beta1 0.5. This is the beta1/(1 - beta1) growth the note names.
- I re-derived nothing by hand that audit 1 did not. This audit is numerical, from a solver written independently of audit 1's.

## Exact solver (rrm3m.py, r3m_batch.sh, r3m_out/)

rrm3m.py is rrm3v.py (the three-type exact solver of AUDIT_CCLOSED) with a momentum numerator, m_k = sum_i w_i g_{k-i},
w_i = (1 - beta1) beta1^i.
- Given u in the Laplace integral 1/sqrt(v) = (2/sqrt(pi)) int exp(-u v) ds, u = s^2, the b-part of E[m_k exp(-u v_k)] is the
  derivative at lambda = 0 of the same placement mean with each slot factor z_T,t replaced by z_T,t (1 + lambda w_t b_T).
- So each placement table M gets a companion table N, built by the same recursion:
  N_h(t) = ((t-h1-h2)/t)(N + w_t b0 M)_h(t-1) + (h1/t) z1 (N + w_t b1 M)_{h-e1}(t-1) + (h2/t) z2 (N + w_t b2 M)_{h-e2}(t-1).
- An earlier epoch e enters through R(y) = N/M of its own table, weighted by beta1^(p + e n). The slot at lag 0 enters with weight
  1 - beta1.
- x0 uses K_rr from agent_B/kfactor.py.

Validation:
- beta1 = 0, b = (9, -1, -1): -0.648602, the rrm3v.py and rrm_indep.py value at n 100, beta2 .99.
- beta1 = 0.9, b = (9, -1, -1), n 100, beta2 .99: x* 0.02027286560121, (x*/x0 - 1)/d 0.051861. Audit 1's independent route
  (audit_A/mom_b1/n100_b10.9_b20.99.txt) gives x* 0.0202728655845 and 0.05186. The two agree to 1e-10 relative in x*.

## Rows (r3m_table.py, r3m_table.txt)

b = (6, 2, -1) with weights 0.1, 0.1, 0.8 (B2 4.8, B3 21.6, r1 4.7292, r2 5.5231); (x*/x0(beta1) - 1)/d at fixed n d:

| beta1 | n d | d = 0.02 | d = 0.01 | d = 0.005 | d = 0.0025 | d -> 0 | c(s) at beta1 0 |
|---|---|---|---|---|---|---|---|
| 0 (AUDIT_CCLOSED) | 1 | -0.555531 (n 50) | -0.516668 (n 100) | -0.497093 (n 200) | -0.487299 (n 400) | -0.4775 | -0.4775 |
| 0.5 | 1 | -0.413517 (n 50) | -0.441057 (n 100) | -0.458028 (n 200) | | -0.4771 | -0.4775 |
| 0.5 | 2 | -0.212092 (n 100) | -0.217376 (n 200) | -0.221547 (n 400) | | -0.2267 | -0.2268 |
| 0.9 | 1 | +0.200744 (n 50) | -0.010923 (n 100) | -0.197326 (n 200) | -0.322771 (n 400) | -0.4773 (order 4, with n 800: -0.395995 at d 0.00125) | -0.4775 |

d -> 0 is the highest-order Richardson extrapolation in d (halving), assuming an expansion in whole powers of d.
- At beta1 0 and 0.5 the rows approach the limit at a steady rate, and the extrapolations of different order agree to 1e-3.
- At beta1 0.9 the row is still far from its limit at d 0.00125 (-0.396 against -0.477). Here d/(1 - beta1) runs 0.2 to 0.0125, so the
  higher terms are not yet small. The two order-3 values are -0.4743 and -0.4771, and order 4 is -0.4773: the error is now a few 1e-4.
- Note the sign. At beta1 0.5 and 0.9 the finite-d rows sit ABOVE the limit, and at beta1 0 they sit below it. That is visible in audit 1's
  9/-1 table too (beta1 0.9: +0.607, +0.052, -0.206 at d .05, .01, .005).

## Not covered

- eps > 0 with momentum: now in AUDIT_CEPS_agent_C.md. At eps 1, n d 1, beta1 0, 0.5 and 0.9 give -0.5390, -0.5388 and
  -0.5368 against the eps closed form's -0.5390.
- beta1 -> 1. Audit 1's observation, that (x*/x0 - 1)/d stays bounded even where d/K_rr is 18, was not re-tested here.
- n d beyond 2 at beta1 > 0 on this b.
- A by-hand rederivation of the earlier-epoch O(d^2) step (audit 1's piece count). The rows test the conclusion, not that step.

Files: rrm3m.py (imports rrm3v.py and ../agent_B/kfactor.py), r3m_batch.sh, r3m_out/, r3m_table.py, r3m_table.txt.
