# Rigor addendum — corrected product-gap decimal

A final independent numerical recomputation found one transcribed decimal in `REPORT.md` / `RIGOR_CHECK.md` for the `n=3` product-TV example.

With

`q_*=2 Phi(sqrt(pi/2))-1 = 0.7899085945560627...`,

the exact expression is

`1-q_*^3 = 0.5071321186122038...`.

The earlier digits `0.5071321183877962...` were a numerical transcription error. The theorem, formula `d_TV>=1-q_*^n`, and every symbolic argument are unchanged.

The other displayed product values recompute as

- `1-q_*^10 = 0.9054267330355084...`,
- `1-q_*^20 = 0.9910558971756630...`,
- `1-q_*^40 = 0.9999200030246677...`.

The inverse-scale and certificate values in Section F of `RIGOR_CHECK.md` also recompute to the displayed digits.
