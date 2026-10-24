# I0099 artifact manifest — 2026-09-16T18-58-00Z

This is a delivery manifest, not a second mathematical report.

- Mathematical report: `runs/2026-09-16/2026-09-16T18-58-00Z__report.md`; creation commit `d91b72f13e98edeb060cfe77e7a9577a94330a4e`; blob `49c38d20cd8557f3d8f5ffeff3f4f5aa3ec35b42`; exact-commit readback VERIFIED.
- Exact C++ generator: `artifacts/2026-09-16T18-58-00Z__i0099_paley_s3_v4_cert.cpp`; creation commit `ecbb96fd1b047978b4e88ccfda37b2a457bc9e27`; blob `1ef01749c62e05f70782f1c1752605397d07b7c3`; exact-commit readback VERIFIED. The local Git-blob hash independently matches this blob SHA.
- The first compressed transcript upload at `artifacts/2026-09-16T18-58-00Z__i0099_v4_extension_3061_3181.out`, creation commit `92e5467c684198350efd5d5d6e3d04bcef765890`, blob `baf930ac79925657c118b9c92a84a3fb3e6a3253`, was corrupted during text transport. It is **INVALID / NOT A CERTIFICATE** and is preserved immutably rather than overwritten.
- Corrected complete transcript: `artifacts/2026-09-16T18-58-00Z__i0099_v4_extension_3061_3181_v2.out`; creation commit `10dc4bd7c7f109d1d6fe47bff457109ae35156f1`; blob `e12455c0332c30d2fd66c98d7108b0359506c3de`; exact-commit readback VERIFIED. Local file size is 10203 bytes and its independently computed Git-blob SHA is exactly `e12455c0332c30d2fd66c98d7108b0359506c3de`. Its embedded decoded raw-transcript SHA-256 is `81d5a6504713f6d96b1e54dd62b62da33a3120189a267efe90d9eaf63e3bc086` for 48987 raw bytes.
- Structural audit script: `artifacts/2026-09-16T18-58-00Z__i0099_v4_extension_audit.py`; creation commit `ad782011f48be46d89babcb940e8016137fdba91`; blob `4340d69eb8cc64a6936275f5b1a8bba3b2ac3369`; exact-commit readback VERIFIED; local Git-blob SHA matches.
- Executed audit output: `artifacts/2026-09-16T18-58-00Z__i0099_v4_extension_audit.out`; creation commit `638a43815b27fa7b58734a80bc7f7e6497ca6be0`; blob `bc13527d885bb2db01259e1aa6a05e540358e92a`; exact-commit readback VERIFIED; local Git-blob SHA matches. It ends `I0099_V4_EXTENSION_AUDIT_PASS`.

The structural audit is a self-check and does not independently re-enumerate every branch-and-bound proof tree. The finite upper-bound evidence is the written completeness argument plus the completed deterministic C++ search transcript. No independent OTHER-task audit is claimed for this finite milestone.
