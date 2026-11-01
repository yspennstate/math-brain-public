# T354 next-order term, eps = 0 and eps > 0 (agent_B/NOTE.md, sections of 20 Oct 02:4x and 03:0x), audit 1 (agent C, 20 Oct 2026 03:0x)

Objects: the bracket x*/x0 = 1 + d [ r K - (p2/4) S/B2^2 - (p2/r)(K2/K) E[b Z^2]/(B2 B3) - (p3/(2r)) S/B2^2 ] + O(d^2) under iid
sampling (eps = 0: K + (3/4)(S/B2^2 - (K2/K) E[b Z^2]/(B2 B3))), the psi derivatives, the kernel k(u), and both exact tables.

Verdict: CONFIRMED, by hand and by an exact route that shares no code or representation with the note's.

## By hand
- With psi(1+u) = 1 + p1 u + p2 u^2/2 + p3 u^3/6 and E[m] = f'(x) = x (abar = 1), D(x) = 0 reads x = -p1 E1 - (p2/2) E2 - (p3/6) E3.
  Put in E1 = d K (2 x B2 + B3)/B2 + O(d^3), E2 and E3 as stated, divide by x0 = r d K B3/(2 B2) and keep O(d): the four terms of
  the bracket come out as written, and at eps = 0 (r 1, p2 3/4, p3 -15/8) it reduces to the eps = 0 bracket.
- p1, p2, p3 checked symbolically (psi_derivs_check.py: all three differences simplify to 0).
- Kernel: int_0^inf t e^(-t eps - t^2/(4u)) dt = 2u [1 - eps sqrt(pi u) erfcx(eps sqrt u)], times u^(-3/2)/(2 sqrt pi), is the
  k(u) of the note.

## Exact, by another route (eps_moment_route.py, eps0_rows.py)
No Laplace kernel. For lag i, v = d b2^i g_{k-i}^2 + W_i with W_i independent of g_{k-i} and kappa_m(W_i) = d^m kappa_m(g^2)
(1/(1 - b2^m) - b2^(i m)). 1/(sqrt v + eps) is expanded in Y = v/V - 1 to order 14 with the exact moments of Y given g. Y is
bounded (v <= max g^2), and J = 10, 14, 18 give the same root to 1e-10 relative. Root by brentq; lags summed to (1 - b1)^-1 x 40.

(x*/x0 - 1)/d, mine at d 0.002 / 0.001 / 0.0005, with the note's exact values at 0.002 / 0.001 in brackets:

| model | eps | family | exact | predicted | Richardson |
|---|---|---|---|---|---|
| test | 1 | b1 0 | 0.2966 0.3011 0.3033 (0.2966 0.3011) | 0.3056 | 0.3056 |
| test | 1 | r 0.1 | 0.5975 0.6027 0.6052 (0.5976 0.6027) | 0.6021 0.6049 0.6063 | 0.6078 |
| test | 3 | b1 0 | -0.1750 -0.1708 -0.1687 (same) | -0.1667 | -0.1667 |
| test | 3 | r 0.1 | 0.0737 0.0790 0.0816 (same) | 0.0795 0.0818 0.0830 | 0.0842 |
| test | 10 | b1 0 | -0.4320 -0.4293 -0.4280 (same) | -0.4267 | -0.4267 |
| test | 10 | r 0.1 | -0.2389 -0.2350 -0.2331 (same) | -0.2348 -0.2330 -0.2321 | -0.2311 |
| three | 3 | b1 0 | -0.4090 -0.4061 -0.4046 (same) | -0.4032 | -0.4032 |
| three | 3 | r 0.1 | -0.2375 -0.2334 -0.2314 (same) | -0.2326 -0.2310 -0.2302 | -0.2294 |
| test | 0 | b1 0 | 0.9965 0.9983 0.9992 | 1 | 1.0000 |
| test | 0 | r 0.1 | 1.3508 1.3522 1.3529 (1.3510 at 0.002) | limit 1.3535 | 1.3536 |
| test | 0 | r 1 | 2.3006 2.2891 2.2834 (2.3005) | limit 2.2778 | 2.2778 |
| three | 0 | b1 0 | 0.3952 0.3999 0.4022 (same) | 0.4045 | 0.4045 |
| three | 0 | r 0.1 | 0.6482 0.6536 0.6562 (same) | 0.6541 0.6564 0.6576 | 0.6588 |

At b1 = 0 the Richardson value equals the predicted bracket to four digits in every row. With momentum the predicted value moves
with d at fixed r, and the exact-minus-predicted gap halves each time d halves (eps 1: 4.6e-3, 2.2e-3, 1.1e-3), so the limits
agree there too. Four eps values and two b-models fix all four terms of the bracket separately (the eps dependence of p2/4, p2/r
and p3/(2r) differs, and the three-valued model separates S/B2^2 from E[b Z^2]); the r 0.1 and r 1 families test K2/K.

## Not covered
Reshuffling at next order, a rigorous O(d^2) remainder for eps > 0 under iid (the note says it carries over, not written out),
and the vector case at next order.
