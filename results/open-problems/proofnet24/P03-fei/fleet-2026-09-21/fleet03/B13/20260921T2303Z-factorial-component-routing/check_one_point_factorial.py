#!/usr/bin/env python3
"""Numerical companion for the B13 factorial component-routing report.

For the Boolean one-point-defect family f_n=1-2*1_{0^n}, all nonempty
Fourier coefficients have the same magnitude. Hence every derivative Palm
row is exactly the uniform power-set law on the other n-1 coordinates.

The script evaluates two dimensionless ratios without forming exponentially
small probabilities:
  raw trigger load / E log2(K!)
  weighted logarithmic address / E log2(K!)
where K is the spectral-sample size.

Standard library only. The accompanying report contains the analytic proof;
this script is diagnostic/reproduction evidence, not a proof of full FEI.
"""

from math import comb, lgamma, log, log2

LN2 = log(2.0)


def binomial_expected_log_factorial(n: int) -> float:
    den = 2 ** n
    ans = 0.0
    for k in range(1, n + 1):
        pk = comb(n, k) / den
        ans += pk * (lgamma(k + 1) / LN2)
    return ans


def ratios(n: int):
    # For f_n, F := E_spectral log2(K!) = 2^(2-n) * E_Bin log2(K!).
    # W = n*2^(1-n), |T|=n. The common exponential factors cancel:
    #   W*n/F = n^2/(2 E_Bin log2(K!))
    #   W*log2(n)/F = n log2(n)/(2 E_Bin log2(K!)).
    e = binomial_expected_log_factorial(n)
    raw = n * n / (2.0 * e)
    address = n * log2(n) / (2.0 * e)
    analytic_lower = n / log2(n)
    return e, raw, address, analytic_lower


def main() -> None:
    ns = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    print("n E_bin_log2_Kfac raw_load_over_factorial "
          "weighted_log_address_over_factorial n_over_log2n")
    for n in ns:
        e, raw, address, lower = ratios(n)
        assert raw + 1e-12 >= lower
        assert address <= 4.0 + 1e-12
        print(f"{n:4d} {e:.12f} {raw:.12f} {address:.12f} {lower:.12f}")


if __name__ == "__main__":
    main()
