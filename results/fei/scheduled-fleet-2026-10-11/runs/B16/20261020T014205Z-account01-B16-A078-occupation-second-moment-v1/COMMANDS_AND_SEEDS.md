# Commands, environment, seeds

No randomness is used by the verifier; seed: `null`.

Command:

```sh
python3 -S verify_occupation_second_moment.py
```

Python version recorded by the actual verifier: `3.13.5`.
The verifier uses only Python standard-library `math`, `fractions`, `decimal`, and `json`.

A separate inherited exact restriction-identity verifier was rerun from the prior two-sided repair artifact:

```sh
python3 -S /mnt/data/20261019T204506Z-account01-B16-A078-two-sided-central-band-repair/verify_two_sided_central_band.py
```

Its output is preserved separately as `CHECK_INHERITED_RESTRICTION_IDENTITY.json`; it checks finite exact identities through physical dimension 12 and finite constant arithmetic only. Both verifier commands completed with exit status 0.
