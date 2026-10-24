# Commands

```text
python REVIEW_CHECK.py > REVIEW_CHECK.out
python -m json.tool CLAIMS.json >/dev/null
python -m json.tool PROGRESS.json >/dev/null
python -m json.tool PACKET_DELTA.json >/dev/null
```

The review certificate is an independent closed-form implementation.  It
does not import the producer checker or enumerate producer truth tables.
