# R03 run43 immutable-report correction: range of `r_{n,k}` in C300

The immutable report `runs/R03/20260917T2108Z_43_fractional_cavity_energy.md` contains one unused lower-bound typo in Section 6. It writes

`1 <= r_{n,k}(a) <= a_k^{-1}`.

The correct range is

\[
\frac{1-2^{1-k}}{(1-2^{-k})^2}
\le r_{n,k}(a)\le
\frac1{1-2^{-k}}=a_k^{-1}.
\]

The lower endpoint is strictly below `1`; for `k=3` it is `48/49`. The upper endpoint occurs at full agreement `a=n`.

This correction does **not** change C300, Paley--Zygmund (5.4), or the Section-6 exponential-cost bound

\[
\mathbb E_{\mu_F^2}r_{n,k}(A)^K\le a_k^{-K}=\exp(O(K)),
\]

because that argument uses only the upper bound `r_{n,k}(a)<=a_k^{-1}`. The statement that `r_{n,3}` is asymptotically `1` at independent-overlap scale `a/n=1/2` is also unchanged.

No other claim is modified by this correction.
