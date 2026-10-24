import pathlib
for filename in ['LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']:
 p=pathlib.Path(filename); s=p.read_text(encoding='utf8')
 s=s.replace('its final part is titled **“Uniformity in p”**, on page 7','its final part is **Step 3**, on page 7, proving uniformity in p')
 s=s.replace('with the final “Uniformity in p” part on page 7','with the final Step 3 proving uniformity in p on page 7')
 s=s.replace('Proof Section 2 pages 4-7 includes Uniformity in p','Proof Section 2 pages 4-7 includes Step 3 proving uniformity in p')
 if filename=='LITERATURE.md':s=s.replace('Started 2026-10-12. Search responses and source excerpts will be saved locally. No solution in print identified yet.','Started 2026-10-12. Initial status was unverified; final outcome below is SOLVED_IN_LITERATURE. Search responses and source excerpts are saved locally.')
 p.write_text(s,encoding='utf8')
import json
for s in pathlib.Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines():json.loads(s)
print('Final page-heading correction and JSONL validation complete.')
