# Exact committed-byte execution evidence

The initially executed local checker candidate had SHA-256 `b71f2bdee9168742c29caeff2a5be607bb65008cae953f139f4f8ba6b45532c0`. The committed checker intentionally omitted one nonfunctional comment, so byte identity was not assumed.

After repository readback, the committed checker Git blob was `b72830e4de3f8fde79bc152380fd2cdb3f4caf40`. A local replica was reconstructed and `git hash-object` matched that blob exactly. That exact committed byte sequence was then executed successfully and returned `PASS` with output Git blob `c178ef3eedab86bdcfec4b5bfa222ce444c8c2e9`, matching the committed `CHECK_OUTPUT.txt` byte-for-byte.

Exact committed checker SHA-256: `c1fb10565f9e3b0f06d87590f3abf5bf94d33d793214cdda71d2a7572c1f038b`.

Exact output SHA-256: `d5b896d4a43439f0271601f840b3aa2f93251fa72624226c4bb1ef53a06e1586`.

The checker is a falsification/consistency check only. The mathematical claim rests on the analytic derivation in `REPORT.md`.
