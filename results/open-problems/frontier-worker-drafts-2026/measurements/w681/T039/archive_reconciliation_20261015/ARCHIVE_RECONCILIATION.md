# T039 target 2 archive reconciliation

The completed rho=.43 certificate is intact on main. No restoration or mathematical rerun was needed.

Inspected main: b606e61034a9a93c11a2d36e715e38419e45b24c. Its complete target2 Git tree equals the tree at final certificate commit 383e86e6b61bf225dc61f41e8450666180b514bd, which is an ancestor. The manifest reports completion, endpoint .43 and 114 payload files. The saved ls-remote check returned the same main head. Claims C004 v2 and C005 v2 remain proof (unaudited); no independent audit file was present.

The shared brain checkout still has the older README saying no new interval is claimed. Its measured SHA-256 is d2653e74617a1e9aff3287a4703f88c251cc952d4072ce1e06511aeef88024c3 and modification time is 2026-10-15T03:41:34.288406+00:00. A file timestamp does not identify its writer.

All four saved publication destination records point to this worker's isolated T039/publication_checkout. Seven own archive helpers were inspected at their recorded hashes. The only copy operation found by the own-scripts destination search copies the source PDF into the worker directory. No own synchronizer to the shared brain checkout was found. This inspection does not identify the external writer of the shared stale files.

The isolated publisher updates Git main, not the other shared working checkout. Therefore the stale shared checkout must not be used as the authoritative export of this certificate. Keep named staging paths and compare snapshot manifests against main before exporting a shared directory. The hook proposal is staged locally for audit; no shared checkout, live hook or brain store was edited.

Scientific result unchanged: 61 certified slabs cover [.40,.43], worst full operator upper 1.9994729860206248 < 2; endpoint N=4000 replay matched all rows. The composed [.10,.43] theorem is C005 v2, proof (unaudited).

NEXT: an agent-r / an agent independently audit C005 v2 and C004 v2. Do not rerun completed target 1/2 computations.
