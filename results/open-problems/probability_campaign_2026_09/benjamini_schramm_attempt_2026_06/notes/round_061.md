# Round 061 log

## Goal

Make the exact bridge-certificate checker usable for certificate collections,
not only one JSON file at a time.

## Directory verification

Updated `scripts/bridge_certificate_verify.py` with:

```powershell
python scripts\bridge_certificate_verify.py --directory research\certificates
```

The directory mode verifies every `*.json` file in the directory, reports each
certificate's exact final value, and exits nonzero if any certificate fails.
The single-certificate command and `--self-test` mode are unchanged.

This remains only the exact algebra audit for the Collatz--Wielandt bridge
criterion.  The graph-specific bridge-majorization inequality is still the
mathematical obligation of the construction that produces the certificate.
