# Integrity addendum — account03/B03 FOREST 20260922T102421Z

This addendum supersedes one identity line in `report.md`.

The report's stated checker SHA-256 `4b7bbde12e5989265ab1b3dca143e620fbf5cf818f0ba7313636d930a5097e70` identifies the locally executed prototype used to obtain the exact regression output; comments were shortened before repository publication, so that SHA-256 is **not** the byte identity of the committed checker and must not be used as such.

Authoritative repository read-back identities are:

- committed checker creation commit `aa9edcb463c3663eb499d7e9905eb7cc392117a0`, Git blob `0609f73abf0b4ddf6255adb50caf72da7bb9a76f`;
- committed checker-output creation commit `db6241d598328a7603dbd6b9f6e354f10579536d`, Git blob `00e02a3c926f329f9cbcb7f15a9178debae76f83`;
- checker-output SHA-256 remains verified as `035b7a61d8eccabe8e362ab235b14711d583a905a08dcaf2b23dfbf60e50b12e`.

The published checker implements the same exact integer algorithms and assertions as the executed prototype, but this addendum does not claim a byte-identical rerun of the repository read-back checker. Scientific claims in the report rely on the displayed exact algebra plus the recorded exact output; the parent FOREST problem remains OPEN.
