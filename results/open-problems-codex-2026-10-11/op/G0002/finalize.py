from pathlib import Path
import json,datetime,hashlib
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8').replace('subject to the recorded final checks.','with the final checks below completed.')
s+='''
## 9. Completed checks

- `python -X utf8 verify.py` passed. Exhaustive monotone families in dimensions 1 through 5 had counts 3,6,20,168,7581. The literal formula produced maxima phi_2=1,6,15,36,100 and phi_{2\\1}=0,4,12,24,76; all their maximizers satisfied the band in these dimensions. The direct formula and occupied-coordinate pair-witness characterization agree AFTER restricting the direct formula to occupied coordinates.
- `python -X utf8 verify_open.py` passed. The occupied-coordinate variant produced maxima phi_2=1,4,9,24,62 and phi_{2\\1}=0,2,6,12,38, reproducing the source tables.
- All 729 arrays with n=3,r=2,M=3 were enumerated; all 2640 successful array/support pairs satisfied the duplicate-safe graph lemma.
- `lake env lean ~/brain_workers/TRIO_1011/op/G0002/Certificate.lean`, from ~/lean_verify, completed with exit code 0. Only Mathlib.Tactic.NormNum is imported. No sorry, no native_decide, and no unverified axioms are used. The Lean file checks the generic clause-witness implication and five explicit rational margins, including r^2/2592>10 sqrt(n) at the chosen square dimension. It does not formalize the full probability proof.
- The first Lean invocation failed because PowerShell wrote a UTF-8 BOM before the import. Rewriting the file as UTF-8 without BOM resolved that parser error. A small-case assertion also exposed the literal-versus-occupied discrepancy; the proof was corrected to cover both and the test now records each separately.

The final lower-bound certificate is r^2/2592=31250000000/81. The conservative common band bound is 100000000. Their exact positive difference is 23150000000/81. The more precise computed graph lower bound before weakening to r^2/24 is 249991360000/3. See verification.json and lean_check.txt.
'''
p.write_text(s,encoding='utf8')
claims=[
 {'claim':'The retrieved source sums phi_2 and phi_{2\\1} over configurations in A and counts coordinate indices, not pairs; its literal (49.1) and small-case tables differ on initially zero pivots.','status':'proved','proof_location':'LITERATURE.md; ATTEMPT.md section 1; source_49_notation_positions.json','remaining_gap':'Editorial intent is not resolved; the refutation applies to both literal and occupied-coordinate readings.','checks':'PDF pp.268-269,373,391,394,398; exact OR_2 check; exhaustive tables n<=5.'},
 {'claim':'For even n>=20, every increasing set in the conjectured band has normalized phi_2 and phi_{2\\1} at most 10 sqrt(n), for both readings.','status':'proved','proof_location':'ATTEMPT.md section 2','remaining_gap':'None.','checks':'Five contributing levels; elementary central-binomial induction; |P_2|<=n.'},
 {'claim':'A vertex covered by a two-positive distinct-coordinate clause and outside all bad-edge endpoints is an occupied second pivot that is not first-order.','status':'proved','proof_location':'ATTEMPT.md section 4; Certificate.lean pair_witness','remaining_gap':'None; the Lean theorem checks the deterministic witness implication, with first-order absence expressed by successful single deletions.','checks':'Lean exit 0; exhaustive 729 arrays and 2640 successful array/support pairs, including repeated samples.'},
 {'claim':'At n=10^14, the finite random-CNF construction has mean normalized phi_{2\\1} at least n/259200=31250000000/81, under both readings.','status':'proved','proof_location':'ATTEMPT.md sections 3-7','remaining_gap':'None; existence by finite averaging, not an explicitly materialized gigantic truth table.','checks':'Duplicate-safe singleton probabilities; independent conditioned clauses; Bonferroni and union bounds; exact Fraction margins; partial Lean rational checks.'},
 {'claim':'Conjecture 53.1 is false for BOTH phi_2 and phi_{2\\1}: at n=10^14 every global maximizer of either objective violates the proposed band. This holds for literal (49.1) and the occupied-coordinate variant matching the source tables.','status':'counterexample','proof_location':'ATTEMPT.md section 7','remaining_gap':'None in the finite existential refutation; the exact global maximizing family is not computed or needed.','checks':'Finite existence of maximizers; strict exact separation 31250000000/81 > 100000000; Lean exit 0 for the strict margin.'},
 {'claim':'Exhaustive checks reproduce the source maxima for the occupied-coordinate variant for n<=5; literal formula maxima and their band locations were independently enumerated for n<=5.','status':'numerical_evidence','proof_location':'verify.py; verify_open.py; verification.json','remaining_gap':'Small cases alone would not prove the general conjecture; they only validate definitions and implementations.','checks':'Counts 3,6,20,168,7581 monotone functions; direct definition compared with pair characterization restricted to occupied coordinates.'}
]
for c in claims:c['problem_id']='G0002'
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
# Exact cached Crossref bibliographic details, without another network query.
x=json.loads(Path('crossref.txt').read_text())
for e in x['message']['items']:
 if e.get('DOI')=='10.1080/00029890.2025.2459044':
  ref={k:e.get(k) for k in ['title','author','container-title','volume','issue','page','published','DOI']}
  Path('crossref_relevant_reference.json').write_text(json.dumps(ref,ensure_ascii=False,indent=2),encoding='utf8')
  with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\nExact cached Crossref metadata for the related first-order paper: '+json.dumps(ref,ensure_ascii=False)+'\n')
Path('STATUS.md').write_text('''STATE: DONE
NEXT: None required for the refutation; optional future work is to reduce the counterexample dimension or seek explicit small witnesses.
VERDICT: SOLVED
2026-10-11: Source verified (Conjecture 53.1 p.398). Literature services queried; OpenAlex/Semantic Scholar rate-limited, no exact printed solution identified.
2026-10-11: Section 62 supplied a random-CNF lead. Independent duplicate-safe proof gives normalized phi_{2\\1} >= n/259200 at n=10^14, exceeding the common band bound 10 sqrt(n). Therefore every global maximizer of either objective is outside the claimed band. The proof covers both literal (49.1) and the occupied-coordinate interpretation matching the tables.
2026-10-11: Hostile-referee checks completed: exact arithmetic, exhaustive monotone functions n<=5, 729 tiny clause arrays, and Lean 4 exit 0 for the key deterministic witness and rational margins. Full proof and limitations in ATTEMPT.md; search audit in LITERATURE.md; claims in CLAIMS.jsonl.
''',encoding='utf8')
files=['ATTEMPT.md','STATUS.md','LITERATURE.md','CLAIMS.jsonl','Certificate.lean','lean_check.txt','verification.json','verify.py','verify_open.py','source_pdf.pdf']
manifest={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in files}
Path('artifact_sha256.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
print(Path('STATUS.md').read_text());print(Path('lean_check.txt').read_text());print('Claims',len(claims))
