# Pinned source artifact

Repository: [openai/math](https://github.com/openai/math/commit/adc7f1241b42e322a6451854ab7e4b4c146bf78a).
Revision: `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

The `snapshot/` directory contains 38 files, totaling 1,680,281 bytes before the local manifest. These include the complete 31-module transitive OAI import closure of `OAI.Probability.TraceReconstruction`, its comparator statement and configuration, manuscript header and introduction, and Lean environment metadata. The OAI sources have 33,984 lines. The only import outside the saved OAI closure is `Mathlib`; its contents and transitive dependencies are not included.

Files were fetched through the read-only connected GitHub `fetch_file` tool at the explicit revision. Full source is in the tool's `structuredContent.content`, even when its displayed text says only “Action completed.” The accompanying blob SHA was checked against `SHA1("blob " + decimal_byte_length + NUL + file_bytes)` before each write. [MANIFEST.json](snapshot/MANIFEST.json) records paths, pinned URLs, blob hashes, byte counts and independent SHA-256 checksums. The manifest is local metadata, not an upstream file.

Run:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_snapshot.py
```

The script checks file identities, exact OAI import closure and source tokens. Both full-buffer and streamed hash calculations must agree; both forward and reverse reachability checks must pass. A small scanner masks nested comments and strings before counting `sorry`, `admit`, `axiom` and `opaque`. It finds none in the solution closure. The challenge statement has three `sorry` tokens. This scanner is not a Lean parser and does not establish kernel acceptance or determine the theorems' actual axioms.

The pinned environment specifies Lean `leanprover/lean4:v4.34.1` and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The comparison configuration permits `propext`, `Quot.sound` and `Classical.choice` and sets `enable_nanoda` to false. These are input settings, not an observed comparison verdict.

The [construction module](snapshot/lean/OAI/Probability/TraceReconstruction/Induction.lean) imports Amplification and Propagation. Its final producer `source_final_pair_eventually` is now available at an immutable revision. Its estimates and the dependencies below it still need mathematical review or a resource-compliant formal check. No Lean build, package installation or comparator run was performed.

The snapshot is a source artifact, not a complete offline build environment. Do not run package setup blindly under the task's one-gigabyte limit. The intended upstream comparator command, once an appropriate environment exists, is `lake env comparator ComparatorChallenges/TraceReconstruction.json`.
