# Delivery recovery: directional-compression package

20 September 2026. The owner requested that the preceding conversation package be pushed to the shared research brain and research continue.

## Completed repository delivery

The four substantive files in the original append-only patch have now been created on `master` in `yspennstate/math-open-problems`:

| File | Creation commit | Verified Git blob |
| --- | --- | --- |
| `REPORT.md` | `339c101301a3e3cdb8c7351615cff7ef5bbe3893` | `011865c0e85cc90c8af59bd9033173603ee5ebe0` |
| `verify_directional_compression.py` | `9f62524a3662a69b55d810d4300129fbd5a779e4` | `e0d518097b8cb0d2c644bcdbcd02fd9d9e1467cc` |
| `verification.json` | `c16749f128565fce34326b79e566d6d7090806ca` | `992fb6a9f592a25f477c5dc98420a03a19a40fe1` |
| `../../handoffs/2026-09-20__directional-compression.md` | `4dbc1933af960301eab530b452ebe200ee8418b4` | `0d31367092d80d826a5cb8dc087d9dfad563b34e` |

The source was the actual conversation ZIP `FEI_Directional_Compression_2026-09-20.zip`. Every file above was preserved byte-for-byte. Each remote blob SHA was read back and matched a Git blob hash computed from the local source bytes.

The exact original checker was replayed in a separate directory. It produced byte-identical `verification.json`. Checker SHA-256: `3ae698f3c826f2908558a5de13cd01e62f863e9dfef8a1d1f01f224ced00d037`; output SHA-256: `fdce850b34e440b4ad3574cd231581b39195cf8ddfec0507d4ffc217b64f149d`.

## Historical wording

The original report and handoff describe their creator session as unable to push. Those statements are retained as historical provenance, not as the current delivery status. This record supersedes only their pending-delivery statements. Their mathematical hypotheses, full-FEI-open status and lack of independent review are unchanged.

The original conversation archive also contains exploratory material and packaging metadata. This delivery uploads the four substantive patch files listed above, not a claim that every ancillary byte of that ZIP was separately added to the repository. The original ZIP remains a conversation backup.

## Substantive continuation delivered separately

Read the [concave restriction report](../2026-09-20-concave-restriction/REPORT.md), [checker](../2026-09-20-concave-restriction/verify_concave_cap.py), and [actual output](../2026-09-20-concave-restriction/verification.json).

Its creation commits are `1770be2243c753e1a2aeecbfe3b41b2ed07eb4d4` (proof), `62cac0e2bfa6e8f0cd4c924b0f84a136dcfac61b` (checker), and `fbad9be02ea31ce9b412e4caf17f1238c03dfb84` (output). Their verified blobs are respectively `b586723862b68d32dda97e0085b9868023fffa46`, `fe65f126bd44322607943857259aca309a0980bd`, and `3ed31f59b968f1a6121d7fd8cf634e34c1992195`. A separate replay of the exact new checker also produced byte-identical output.

The new theorem replaces the old directional-compression payment floor 6.130502579614... by 5.826796887175..., proves a variance credit and dyadic equality rigidity, and supplies a valid shared-control upper envelope without reinstating the false raw decrement subadditivity. These are not a proof of unrestricted FEI.

No schedule, permission, repository visibility, ownership, or unrelated research file was changed. Successful delivery establishes availability, not that any later worker has already read or used the files.
