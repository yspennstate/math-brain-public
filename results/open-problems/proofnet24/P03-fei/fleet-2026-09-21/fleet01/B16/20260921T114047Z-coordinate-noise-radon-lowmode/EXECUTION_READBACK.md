# Exact committed-byte execution readback

The first local execution used `check.py` bytes with SHA-256 `2f33decd6698a115ebcc2cd3632415818a75f3295c66379bf042dbde8339e232`.

GitHub readback showed that the committed script differed from those bytes in one comment-only capitalization (`unnormalised` -> `Unnormalised`). The committed script identity is Git blob `54829f315743523b21908d38c64d4f063af1e404`, SHA-256 `ecf0dccd3442b5ebaf58a7e9b74b77c9c2cd2fcb33f2520915a17da9f789d77e`.

The exact committed bytes were then executed natively. They returned the same `PASS` output byte-for-byte, whose SHA-256 is `d11e80eec05b0e7b956f2e4bdc91223bd395127fcde6e91decacf227e2734db1`.

This note is a provenance/readback correction only; no mathematical statement or test condition changed.
