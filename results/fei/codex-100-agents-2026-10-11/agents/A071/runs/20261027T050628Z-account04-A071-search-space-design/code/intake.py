from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
report=Path(r'math-open-problems/reports\fei-2026-10-11')
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'context')
base=Path(r'agents')
source=base/'A080/runs/20261027T015619Z-account04-A080-universal-counterexample-standard'
files=[report/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((supp/'sources').glob('*.md'))+list(ctx.glob('*.txt'))
files += [source/n for n in ['REPORT.md','PROOF.md','CLAIMS.json']]
files += list((report/'runs').rglob('REPORT.md'))
manifest=[]
for p in files:
    b=p.read_bytes()
    try: s=b.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=b.decode('cp1252');enc='cp1252'
    manifest.append(dict(path=str(p),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),decoding=enc))
    if p.parent==ctx:
        lines=[l for l in s.splitlines() if any(w in l.lower() for w in ['composition','activation','singularity','read-once'])]
        print(p.name,enc,'\n'+'\n'.join(lines[:12])[:1600])
(R/'out/SOURCE_INTAKE.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
c=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8'))['claims'][0]
# Preserve the producer's convention, not our preferred raw-statement hash.
digest=hashlib.sha256(json.dumps({'exact_statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
verdict=dict(claim_id=c['claim_id'],version=c['version'],statement_sha256=c['statement_sha256'],verdict='HOLDS_UNCHANGED',reviewer='A071',antecedent_conflict='A071 authored the earlier row criterion; no independent reacceptance of that antecedent is claimed',reconstruction='PROOF.md section1',new_corollary='PROOF.md sections2-3; separate pending claim',canonical_hash_reconstruction=digest)
(R/'out/REVIEW.json').write_text(json.dumps(verdict,indent=2)+'\n',encoding='utf-8')
print('SOURCE_INTAKE',len(manifest),'files; source statement digest',c['statement_sha256'])
