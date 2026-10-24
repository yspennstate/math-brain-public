import pathlib,json
# Normalize manuscript encodings so STATUS's first line is literal ASCII text.
for name in ['STATUS.md','ATTEMPT.md']:
 p=pathlib.Path(name);p.write_text(p.read_text(encoding='utf-8-sig'),encoding='utf8')
# Save the additional brain recall conclusion without promoting its candidate claim.
p=pathlib.Path('LITERATURE.md')
p.write_text(p.read_text(encoding='utf8')+'\nThe during-attempt math-store recall again returned the candidate Problem 7.5 prefix-filling argument and standard ergodicity cards. Prefix insertion concerns a different problem and may change the path rather than only center it; it was not used to claim a solution to 7.1–7.3.\n',encoding='utf8')
required=['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl']
for name in required:assert pathlib.Path(name).exists()
a=[json.loads(s) for s in pathlib.Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(a)==4
for c in a:assert set(c)=={'problem_id','claim','status','proof_location','remaining_gap','checks'}
print('required records exist, claims parse:',len(a))
