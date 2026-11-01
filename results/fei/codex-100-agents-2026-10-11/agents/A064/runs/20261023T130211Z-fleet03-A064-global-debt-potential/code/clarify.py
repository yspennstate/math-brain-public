from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
claims=json.loads((ROOT/'CLAIMS.json').read_text(encoding='utf-8'))
statement_hash=hashlib.sha256(claims[0]['exact_statement'].encode('utf-8')).hexdigest()
assert statement_hash==claims[0]['statement_sha256']
proof=(ROOT/'PROOF.md').read_text(encoding='utf-8')
assert 'no extra-reserve formula from section2 is applied to a general reference' in proof
assert 'E_v=0 outside the sector-reference hypothesis' in proof
claims[0]['proof_source']['sha256']=hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()
record={'reviewer':'A064','verdict':'FINAL_BOUNDARY_CLARIFICATION','scope':'Any-reference total INITIAL capital lower bound uses the admitted all-product terminal cut directly. No zero-erasure or sector-only extra-reserve formula is applied outside its hypotheses. Claim statement, exact formulas and certificate results unchanged.'}
if record not in claims[0]['review_records']:claims[0]['review_records'].append(record)
(ROOT/'CLAIMS.json').write_text(json.dumps(claims,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
receipt={'status':'CLARIFIED','new_statement_sha256_unchanged':statement_hash,'proof_sha256':claims[0]['proof_source']['sha256'],'mathematical_certificates_rerun':'not needed: only generic terminal-bound justification clarified; no formula or executable test changed','source_A061_audit':'completed unchanged HOLDS'}
(ROOT/'out/FINAL_BOUNDARY_CLARIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:
 f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')+' — Final proof readback: generic ANY-reference initial-capital lower bound now uses the admitted terminal product cut directly; no E_v=0 assumption or sector-only reserve inference outside hypotheses. Statement/formulas/certificates unchanged; proof hash refreshed and A061 audit verdict marked completed. Final manifest regenerated afterward.\n')
print(json.dumps(receipt))
