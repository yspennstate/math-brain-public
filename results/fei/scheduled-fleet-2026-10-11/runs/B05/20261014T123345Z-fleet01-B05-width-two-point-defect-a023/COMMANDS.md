# Commands

Executed from the run directory:

```text
python CHECK.py > CHECK.out
python CERTIFY.py > CERTIFY.out
python -m json.tool CLAIMS.json >/dev/null
python -m json.tool PROGRESS.json >/dev/null
python -m json.tool PACKET_DELTA.json >/dev/null
sha256sum REPORT.md PROOF.md CLAIMS.json PROGRESS.json PACKET_DELTA.json CHECK.py CHECK.out CERTIFY.py CERTIFY.out COMMANDS.md SOURCE_PINS.md > MANIFEST.sha256
```

`CHECK.py` contains no random search.  `CERTIFY.py` uses exact rational
arithmetic except when printing already-certified interval endpoints.
