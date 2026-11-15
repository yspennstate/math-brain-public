# Checks and limitations

## Independent derivation of the parity coefficient

The probability generating polynomial of one uncentered summand is
\[
 f_n(t)=(1-\lambda/n)(q+pe^{2it})+(\lambda/n)e^{it}.
\]
At zero, \(f_n(0)=1\). At the other saddle, \(f_n(\pi)=1-2\lambda/n\). These are direct evaluations of the polynomial, independently of conditioning on the midpoint count. Fourier inversion for an integer \(k\) contains both saddles, with relative sign \((-1)^k\).

Here is a check of the leading local coefficient. For \(s=u/\sqrt n\), the expansion at zero, after removal of the phase \(n\mu_ns\), tends to \(\exp(-2pq u^2)\). At \(\pi\), the value raised to the nth power tends to \(e^{-2\lambda}\). The first logarithmic derivative there, divided by \(i\), is
\[
 \mu_{\pi,n}=\frac{2p(1-\lambda/n)-\lambda/n}{1-2\lambda/n}.
\]
Its difference from \(\mu_n\) is \(O_{p,\lambda}(1/n)\), so it has the same centered Gaussian limit on this scale. The limiting variance at either saddle is \(4pq\). Outside fixed neighborhoods of 0 and pi the modulus is bounded strictly below 1. Inside those neighborhoods,
\[
 |f_n(t)|\leq(1-\lambda/n)|q+pe^{2it}|+\lambda/n
\]
gives Gaussian domination after scaling. Dominated convergence in Fourier inversion therefore gives, for bounded standardized \(z=(k-n\mu_n)/(\sigma_n\sqrt n)\), the leading mass
\[
 \Pr(T_n=k)=\frac{\phi(z)}{2\sqrt{npq}}
       (1+(-1)^k e^{-2\lambda})+o(n^{-1/2}).
\]
This reproduces the coefficient in PROOF.md (13). In particular, the factor is **not** simply the span-one lattice correction: the second saddle survives when the midpoint probability is of order 1/n. At lambda=0 the odd masses vanish and the even ones double; at p=1/2 the central half-jump gives the predicted constant directly.

## Other analytic checks

- The unperturbed standardized third cumulant, computed directly from the two endpoint probabilities, is `(q-p)/sqrt(pq)`. Its integrated Hermite correction is `(q-p)(1-z^2)phi(z)/(6 sqrt(npq))`, agreeing with the skew term derived by Stirling in the proof.
- The conditional normal shift is proportional to `lambda-J`; its mean is exactly zero. Omitting that cancellation would create a spurious skew correction.
- The mean and variance formula (8) were independently checked against summing the three raw probabilities and centered squares in every numerical row.
- Optimizing the limiting ratio was done twice: by differentiation, and by completing a square with `M^2-BM=1`. This recovers the exact Esseen value at zero contamination.
- The upper bound for the supremum uses both the Gaussian and its second Hermite factor. The latter has absolute maximum at zero; the other local maximum has height `2 exp(-3/2)<1`. Restricting to the central jump without this global check would only prove a lower bound.
- Left limits and right values are both needed. Reflection p to 1-p changes which side attains the leading error; the formula must contain an absolute value on q-p. The exact arithmetic audit includes p=4/5 as well as p<1/2, and an independent reflection check used n=511.
- Even and odd n occur in the exact checks. Choosing an even *raw threshold* near the row mean is allowed for either parity of n and makes the larger parity coefficient accessible.
- At lambda=0 the distribution is supported only on even integers; including zero-mass odd integers in the endpoint supremum does not change it.
- Binomial parameters near zero or one are excluded from uniform remainder claims. Compactness is used explicitly in the stability corollary. Unbounded n times contamination is also excluded.

## Numerical checks

The exact command and full output are in LOG.md. The main script computes conditional binomial convolutions, without Monte Carlo or FFT. A separate algorithm multiplies integer polynomials for rational laws and evaluates all left and right CDF errors with 90-digit arithmetic. This audit checked 48 laws at n=8,31,64. Its maximum ratio discrepancy against the main implementation was `7.605027718682322e-15`.

The 80 larger finite cases use n=128,512,2048,8192,32768. They include symmetry, the Esseen p, the limiting optimizing p, and p=1/5, at lambda=0,1/10,1,4. The largest omitted binomial-mixture tail was approximately `1.381205554665212e-43`; floating probability mass error was at most `1.4588330543574557e-13`.

Both uniform CDF expansions were evaluated at every integer threshold. Their worst residual, multiplied by sqrt(n), decreased across the five n values as follows:

| n | maximum scaled residual over tested parameters and both jump sides |
|---:|---:|
| 128 | 0.03216367675300817 |
| 512 | 0.015784973859630937 |
| 2048 | 0.007842789850519363 |
| 8192 | 0.0039080641672447165 |
| 32768 | 0.0019502285557495983 |

These numerical values are checks of the asymptotic derivation, not certified enclosures. The theorem does not use them.

## What this does not settle

There is no universal finite-n upper bound here. In fact the lambda=4 optimized example at n=32768 is slightly ABOVE its limiting value, demonstrating that an asymptotic formula cannot be promoted to such a bound. Nothing is claimed for arbitrary three-point locations, nonlattice perturbations, contaminations with unbounded n times mass, or all distributions. Novelty of the special-family theorem has not been established. The October full-solution claim was located and read at the theorem/abstract level, but its long proof and certificate reductions have not been validated.
