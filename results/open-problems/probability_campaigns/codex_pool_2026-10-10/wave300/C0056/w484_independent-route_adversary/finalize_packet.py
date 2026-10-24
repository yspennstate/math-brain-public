from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parent
submission=json.loads((root/'SUBMISSION_RECEIPT.json').read_text(encoding='utf-8'))
assert submission['submitted'] and not submission['ingested']
measurements=json.loads((root/'MEASUREMENTS.json').read_text(encoding='utf-8'))
bundle=json.loads((root/'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
assert len(bundle['entries'])==4 and len(bundle['relations'])==3
assert all(row['kind']=='concept' and row['proof_text'] is None for row in bundle['entries'])

report=f'''C0056's review packet is ready. I saved an independent scalar-resolvent derivation before reading w483's proof: an atomic counterexample to the inference from an annealed first moment to sample absolute continuity, a conditional Lp compactness criterion, and exact single-site cavity upper and resonant lower bounds. A direct audit keeps w483's L1-L5 within their stated conditional scope. The parent problem is not proved.

The exact source requests AC spectrum and GOE statistics separately. The working bounded-density uniform-law slice and coupling normalization are explicit. Current openness is UNKNOWN: a September 2026 public manuscript claims a solution, but its full proof was not adopted as verified. The public Lean scope note concerns a two-dimensional spectral set and does not certify the three-dimensional AC conclusion. No formal-check receipt or served-model certification is claimed.

Measurement command: python -X utf8 ~/brain_workers/w484/verify_artifacts.py. For eta from 0.1 to 0.00001 the atomic sample's squared Poisson L2 norm grows from 1.5915494309 to 15915.4943092 (factor 10000), while its averaged density stays below 0.5. All 60 conditional upper-bound and 26 resonant lower-bound arithmetic controls passed. These are deterministic formula checks, not independent proof review or an experiment on Anderson delocalization. Six result/source/audit rows are saved.

Four DRAFT concepts and three relations were submitted to {submission['draft_path']}. Review is pending with w485; ingestion and retrieval are not verified. The brain improvement is a proposal until the coordinator validates and integrates it; no improvement to live recall has been measured. No live mathematical store or recall control was changed.

Apply line: patches/01_poisson_first_moment_hook.diff names ~/primary_directive/hooks1000/proposals/math-w484.jsonl; the reviewer can append its single proposal row, check its fire and silent cases, and route it through the normal hook audit. The worker's write-only-folder rule kept this hook local; the explicit task exception authorized only the w484 brain-inbox draft. Integrate the mathematical draft through the coordinator after review; do not use the sketch as a parent theorem.

The hardest remaining spectral step is uniform control of expected inverse cavity imaginary response on resonant environments as eta tends to zero at fixed positive disorder. The automatic b>=eta bound diverges. w483's equivalent route needs volume- and scale-uniform marked pair concentration. GOE remains a separate obligation. An Lp bound with p>1 is sufficient and stronger than mere AC, so failure to prove it would not disprove the conjecture. Nonzero spectral mass must also be justified when applying an abstract criterion.

NEXT: w485 independently checks L01-L03; the proof lane proves or refutes uniform resonant inverse-cavity control on a nonempty interior energy interval at fixed disorder.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')

review='''The packet covers C0056's spectral branch only. Review the independent L01-L03 in ATTEMPT.md before using CORE_AUDIT.md. Check the Fatou/pathwise subsequence quantifier, positivity and local measure identification, countable basis transfer, cavity conditioning sigma-field, pi factors and resonance boundary |a|+b<=lambda. Confirm normalization from uniform[-1,1] to the primary variance-one law. The zero-hopping counterexample refutes a route, not the target.

The frozen w483 direct-audit snapshot is review/w483_ATTEMPT_snapshot.md (SHA256 4f99ebdf4c964aacc446b9399db3eab0b6edcecf85ad00534470ccd9c9867338). Its pair inequality is assumed, never proved. The conditional route is kept; no parent theorem or GOE inference is kept.

SOURCE_STATUS.json records historical sources, the recent unaudited public proof claim and formalization scope. CLAIMS.jsonl gives statements, assumptions, sources, proof/counterexample, reviewer state and gaps. MEASUREMENTS.json records deterministic arithmetic controls only. DRAFT_BUNDLE.json contains four concepts, zero theorem/lemma entries and three supported relations. SUBMISSION_RECEIPT.json separates submitted, reviewed, ingested and retrievable. Neither requested model settings nor file hashes establish mathematical correctness or served model identity.

NEXT: Independently check L01-L03 and return item-specific verdicts with response-side served-model evidence where available; then retain the inverse-cavity estimate as an unresolved proof obligation.
'''
(root/'REVIEW_PACKET.md').write_text(review,encoding='utf-8')
paths=('ATTEMPT.md','CLAIMS.jsonl','CORE_AUDIT.md','SOURCE_STATUS.json','MEASUREMENTS.json','REPORT.md','REVIEW_PACKET.md','DRAFT_BUNDLE.json','SUBMISSION_RECEIPT.json')
hashes={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in paths}
(root/'REVIEW_HASHES.json').write_text(json.dumps({'purpose':'ordinary reviewer file checksums; no source manifest, store seal, release MAC or proof certificate','files':hashes},indent=2)+'\n',encoding='utf-8')
print('PACKET_READY', len(paths), 'hashed review artifacts')
print('ATTEMPT_SHA256',hashes['ATTEMPT.md'])
print('CLAIMS_SHA256',hashes['CLAIMS.jsonl'])
print('DRAFT_PATH',submission['draft_path'])
