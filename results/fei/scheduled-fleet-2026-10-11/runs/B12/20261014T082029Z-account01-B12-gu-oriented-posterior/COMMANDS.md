# Commands

```text
python3 CHECK.py | tee CHECK.out
python3 -m py_compile CHECK.py
python3 -m json.tool CLAIMS.json
python3 -m json.tool PROGRESS.json
python3 -m json.tool PACKET_DELTA.json
sha256sum REPORT.md PROOF.md CLAIMS.json PROGRESS.json PACKET_DELTA.json CHECK.py CHECK.out SOURCES.md COMMANDS.md
```

Deterministic seed: `0xB12A05806` (`47557138438`).  Walsh coefficients,
squared masses and influences are exact rationals.  Binary logarithms and
reported residual comparisons use floating point.  The all-`n` rare-family
formulas are analytic; finite construction is only a verification control.
