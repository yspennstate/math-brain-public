# FEI normalized-convolution continuation

**Full FEI: OPEN.** Four analytic contributions with exact finite self-checks:

- Raw all-shift logarithmic tariffs fail exponentially under Boolean tensor powers
- `T=L/Z` is exactly additive for tensor amplitude vectors
- Conditioning on paired Fourier support destroys shape-KL recovery
- A physically realizable unconditioned sign completion restores the missing scale on that same family

Read [REPORT.md](REPORT.md) for full quantifiers, proofs, limitations, and the exact open step. Run `python verify.py` to reproduce [verification.json](verification.json). The checker uses the standard library and rational logarithm enclosures. It is neither an independent audit nor a formal proof assistant.

[explore.py](explore.py) and [exploration.json](exploration.json) retain the floating exploratory search, explicitly separated from proof evidence. [CLAIMS.json](CLAIMS.json) records statuses and unpaid obligations.

The normalized universal transfer remains unproved and FEI-hard. This package does not redirect the scheduled worker fleet or change schedules.
