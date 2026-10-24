# P20 immutable readback correction — 2026-09-15 21:11:17

This file preserves the immutable run report at commit `6d78499790be2ff9538df3f2cdf212445310fa77` and records one notation-only readback correction.

In Section 2 of `2026-09-15_21-11-17__run-report.md`, immediately after `Write x=ru`, the angular variable was serialized as `\nu\sim\operatorname{Unif}(S^{d-1})`. It should read

\[
u\sim\operatorname{Unif}(S^{d-1}).
\]

That is, the intended symbol is the same `u` appearing in `x=ru` and in `h(u)`. No formula, claim status, proof, dependency, audit verdict, or conclusion changes.