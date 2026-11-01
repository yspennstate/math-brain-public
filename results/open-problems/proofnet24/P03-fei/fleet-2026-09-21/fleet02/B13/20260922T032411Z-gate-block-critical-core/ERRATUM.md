# Immutable provenance erratum

The mathematical statements and numerical values in `REPORT.md` are unchanged.

One provenance line in Section 8 needs correction. The displayed SHA-256
`4ff143e81804f6fcf74b5105a9ab05143720d0343ca7d51cec7afbd6bc51ce9f`
is the SHA-256 of the longer local standard-library implementation that was actually executed to produce the archived output. Before repository delivery I compacted that implementation without changing its formulas/tests, so that SHA-256 does **not** identify the committed adjacent `CHECKER.py` byte string.

Authoritative repository identity for the committed compact checker is Git blob
`0da1b308b4c571ebfc7e1b864d8d67c22d6d6085`, read back from commit
`e4c18e2088e937c83f32fe99052e1ccff9732a95`.

The archived `CHECKER_OUTPUT.txt` is byte-identical to the executed local output and has SHA-256
`11ab9f84002893d65251b5aa62fc473fffd1ee0fbfc5bdf1cef0472f4fa6cf92`; its read-back Git blob is
`97884a3bb63f1c1a03cf8f3fd207e664de8d9e82`.

No mathematical claim depends on the checker; Theorem 2.1 and the critical-core corollary are proved analytically in the report. This erratum exists only to keep execution provenance exact rather than silently treating two equivalent source files as byte-identical.
