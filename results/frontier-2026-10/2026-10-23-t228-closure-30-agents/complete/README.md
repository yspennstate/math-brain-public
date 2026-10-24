# T228 research package — 23 October 2026

T228's concrete-model requirement is complete and independently internally audited. The result supplies an explicit nonlinear, unclipped SGD model with global average contraction, a unique invariant probability law, and a strictly positive exact power tail of index between one and two. This is an application of existing tail theory. It is not a general neural-network theorem, a novelty certification, or external peer review.

Start with `campaign/manuscript/T228_Proof.pdf` (13 pages) and `campaign/RESULT.md`. The exact registry requirement and its thirteen proof obligations appear in `campaign/sources/T228_REGISTRY.json` and `campaign/T228_OBLIGATION_MAP.json`.

## Contents

- `campaign/proofs/`: the baseline proof, nonzero-teacher theorem, batch-two and signed-tail extensions, index dependence, and zero-teacher moment dynamics.
- `campaign/reviews/`: reports A07–A30; author/research reports A01–A06 are in their respective top-level directories.
- `campaign/AGENT_ROSTER.json`: all 30 distinct assignments, requested model/effort settings, completion status, and exact report hashes.
- `campaign/checks/`: reproducible checks, accepted certificates, audit outputs, and explicitly labeled negative-test evidence.
- `campaign/history/`, `CORRECTIONS.json`, and `SOURCE_PIN_RECOVERY.json`: retained earlier versions, explanations of corrections, and exact recovered source pins.
- `a01/`: prior Math Brain work credited in the proof. `a02/` and `a05/`: partial T336 attention/ERM results. `a03/`: portfolio triage. `a04/`: literature work. `a06/`: conditional T421 Adam results.
- `campaign/manuscript/rendered/`: all thirteen page images inspected during manuscript review.
- `MANIFEST.json`: SHA-256 and byte length of every archived substantive file, excluding the manifest itself and subsequent verification receipts.

The final frozen snapshot includes all substantive authored research and review files, exact recovered private source files, manuscript source/PDF, and visual review evidence. Python caches, TeX build auxiliaries/logs, and the third-party paper cache declared in `campaign/EXTERNAL_REFERENCES.json` are omitted. The missing bytes of an early superseded baseline draft are explicitly disclosed in `campaign/CORRECTIONS.json`; no current proof depends on them.

## Reproduce the integrity audit

From this directory with Python 3:

```bash
python campaign/checks/A26_verify_bundle.py --root . --manifest MANIFEST.json --output /tmp/T228-final-verification.json
```

Strict mode requires 30 completed agents, checks every manifest hash/length and preservation coverage, verifies source pins and review bindings, replays the exact rational checker, and checks the numerical-certificate safety boundary. Warnings about the disclosed historical draft and external paper cache are expected. They are distinct from failed checks or unfinished work. This audit is not a proof assistant.

To rebuild the manuscript with a TeX installation, run `pdflatex` twice on `campaign/manuscript/T228_Proof.tex` from its directory. A rebuild may have different PDF metadata; the manifest pins the actually reviewed PDF.

`FINAL_VERIFICATION.json` is an audit of the frozen manifest. It is kept outside the manifest to avoid self-reference. `ARCHIVE_RECEIPT.json` additionally hashes that audit and the manifest. Repository write/readback receipts are produced only after the final immutable commits exist and are saved alongside the package in both private repositories.

The first portfolio completion, T069, is carried forward from the earlier registry and was not re-audited here. T336 and T421 remain partial/conditional. Thirty configured agents do not imply thirty independent end-to-end mathematical reviews. Repository persistence does not assert native Brain graph ingestion.
