# Commands

```text
python CHECK_BELLMAN.py > CHECK_BELLMAN.out
python -m json.tool CLAIMS.json >/dev/null
python -m json.tool PROGRESS.json >/dev/null
python -m json.tool PACKET_DELTA.json >/dev/null
```

The exhaustive checker fixes complement symmetry and uses exact rational
Walsh coefficients. Entropy evaluations and reported signs are floating;
they are diagnostic only.
