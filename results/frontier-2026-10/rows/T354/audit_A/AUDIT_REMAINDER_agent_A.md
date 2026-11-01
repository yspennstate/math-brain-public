# T354 scalar Adam: second audit, the iid remainder lemma of agent B (d9d625e8) (agent A, 20 Oct 2026 02:2x)

The lemma's algebra was checked by hand (02:0x NEXT). Here the eight parameter cases of its enclosure table are recomputed by a
route with no Monte Carlo (laplace_exact.py): y^(-1/2) = pi^(-1/2) int_0^inf s^(-1/2) e^(-s y) ds turns E[g_{k-i} v_k^(-1/2)]
into one integral of a product over lags, which under iid sampling factorizes; the product is summed exactly while the lag
weight is large and by the cumulant series of log E e^(-u g^2) to order 5 beyond. Model: the NOTE's g_i = x + b_i,
b = (9, -1 x 9). x0 = (1-b2) K m3/(2 abar V0) with K = (1-b1)/(1-b1 b2); x* is the root of D, bracketed by sign
(D(x0/2) < 0 < D(2 x0) in every case). 200 and 400 Gauss-Legendre nodes give the same six digits at b2 0.99.

    beta2    beta1   exact x*/x0   peer enclosure
    0.99     0       1.009790      inside (peer MC 1.0105)
    0.995    0       1.004953      inside (peer MC 1.0046)
    0.999    0       1.000998      inside (peer MC 1.0009)
    0.9999   0       1.000100      [0.9994, 1.0014]
    0.999    0.9     1.001037      [0.9936, 1.0169]
    0.99     0.9     1.013338      [0.7726, 1.5826]
    0.999    0.99    1.001352      [0.9939, 1.0164]
    0.99     0.99    1.023949      [0.8324, 1.4857]

All eight exact values lie inside the lemma's enclosures, and the three with peer Monte Carlo agree with it to its error.
The leading law x* = x0 (1 + O(1-b2)) holds in every case. The next-order term, read from the table: at b1 = 0,
x*/x0 - 1 = 0.98 (1-b2) to 1.00 (1-b2); with momentum it grows with (1-b2)/(1-b1). The two cases with that ratio equal to 0.1
(0.999/0.99 and 0.99/0.9) give 1.352 and 1.334 times (1-b2), and 0.999/0.9 (ratio 0.01) gives 1.037, so for small ratios the
correction is about (1-b2)[1 + 3.5 (1-b2)/(1-b1)]. The 3.5 is fitted to these three points only, not derived. At b1 = b2 the ratio
is 1 and the series form fails (2.39, not 4.5), as expected when momentum and the second moment average over the same window.

Verdict: the remainder lemma's enclosures are CONFIRMED on every case it states. Its widths at b2 0.99 (about +-40 per cent) are
loose against the exact 1-2 per cent correction; that is a sharpness remark, not an error.
