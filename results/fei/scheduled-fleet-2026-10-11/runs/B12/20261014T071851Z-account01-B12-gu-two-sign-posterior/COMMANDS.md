# Verification commands

Run from this directory:

```text
python3 CHECK.py | tee CHECK.out
python3 -m py_compile CHECK.py
sha256sum REPORT.md PROOF.md CLAIMS.json PROGRESS.json PACKET_DELTA.json CHECK.py CHECK.out SOURCES.md COMMANDS.md
```

The deterministic seed is `0xB12A05805` (`47557138437`).  The checker uses
exact rational Walsh coefficients, squared masses, influences and pivotality;
only logarithms and displayed residual comparisons use binary floating point.
No stochastic search is used for a mathematical certificate.
