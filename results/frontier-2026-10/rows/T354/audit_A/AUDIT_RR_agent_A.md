# Audit of agent B's reshuffling remainder bound (T354, remainder_rr.py, push 6c525bf4)

Auditor agent A, 20 Oct 2026 03:0x. Scope: random reshuffling, beta1 = 0, eps = 0, the NOTE's test model
g_i = x + b_i, b = (9, -1 x 9), n = 10. Verdict: CONFIRMED at beta2 0.995, 0.999 and 0.9999.

## The independent route (rr_exact.py)

No Taylor step and no bound. On the test model only the position of the special sample in each epoch matters: with the
current sample at position p of its epoch, the special sample at q_0 in the current epoch and at q_m in the m-th earlier one
(uniform on 0..n-1, independent),

    v = g_o^2 + d (g_s^2 - g_o^2) [ beta^(p - q_0) 1{q_0 <= p} + sum_{m >= 1} beta^(p + m n - q_m) ],

and g = g_s if q_0 = p, else g_o. Then v^(-1/2) = (2/sqrt pi) int_0^inf e^(-w^2 v) dw, the earlier epochs factorize inside the
integral, and epochs whose weight has fallen below 1e-3 are summed in closed form through the cumulants of beta^(-q) to order 4.
D(x) = E[g v^(-1/2)] is computed by Gauss-Legendre quadrature in w and x* is its root.

Validation of the reduction (rr_exact_mc.py): at beta2 0.9, frozen x, a direct RR simulation of D(x) against the formula:

    x 0.05:  exact -0.060556,  sim -0.060567 +/- 0.000017  (0.6 se)
    x 0.20:  exact -0.010609,  sim -0.010641 +/- 0.000022  (1.5 se)

Node convergence: at beta2 0.995 the root is 0.993690 x0 with both 200 and 400 nodes.

## Against the peer's enclosures (remainder_rr_runs.txt)

    beta2    exact x*/x0    enclosure              second-order centre   centre - exact   (centre - exact)/d^2
    0.995    0.993690       [0.83118, 1.15518]     0.99290               -0.00079         -31.6
    0.999    0.998725       [0.99348, 1.00391]     0.99869               -0.000035        -35
    0.9999   0.999872       [0.99982, 0.99992]     0.99987               within rounding  (d^2 x 33 = 3e-7, below the 5-digit centre)

Every exact value is inside its enclosure, including the tight one at 0.9999 (width 1e-4, exact value 0.52e-4 from its lower end). The centre misses the exact root by an amount that scales as d^2 with a
roughly constant coefficient (about -32 to -35), which is what a correct second-order expansion with an O(d^3) remainder in
x* (O(d^2) in x*/x0) should show.

## Not covered

beta1 > 0 (remainder_rr_mom.py) and eps > 0 (remainder_rr_eps.py) are not re-derived here; the exact route handles beta1 = 0 only.
