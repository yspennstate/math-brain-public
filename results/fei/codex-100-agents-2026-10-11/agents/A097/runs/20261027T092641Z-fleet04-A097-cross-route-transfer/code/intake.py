import hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOT.joinpath('out').mkdir(exist_ok=True)
BASE = Path(r'~\brain_workers\FEI100_20261011')
CANON = Path(r'math-open-problems/reports\fei-2026-10-11')
SUPP = Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
files = [CANON/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [SUPP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += [p for p in (SUPP/'sources').iterdir() if p.is_file()]
files += [p for p in (BASE/'context').iterdir() if p.suffix == '.txt']
files += [BASE/'BOARD.md', BASE/'claude'/'B20'/'STREAM_NOTES.md', ROOT.parent.parent/'STATUS.md', ROOT.parent.parent/'LEARNED.md']
for who, name in [('A012','DERIVATION.md'),('A096','DERIVATION.md'),('A094','REPORT.md'),('A011','DERIVATION.md'),('A085','REPORT.md'),('A004','REPORT.md')]:
    files.append(sorted((BASE/'agents'/who/'runs').iterdir())[-1]/name)
files.append(ROOT.parent/'20261023T143952Z-fleet03-A097-cross-route-transfer'/'PROOF.md')
receipts = []
extracts = []
for path in files:
    raw = path.read_bytes()
    try:
        text = raw.decode('utf-8-sig')
        encoding = 'utf-8-sig'
    except UnicodeDecodeError:
        text = raw.decode('cp1252')
        encoding = 'cp1252 after strict UTF-8 rejection'
    receipts.append({'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(), 'decoder': encoding})
    lines = text.splitlines()
    picked = [(i+1, s) for i, s in enumerate(lines) if re.search(r'projection|restriction|shared.data|C018|C019|C020|C024|A097|complete reference', s, re.I)]
    extracts.append({'path': str(path), 'selected_lines': picked[:24]})
(ROOT/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts, indent=2)+'\n', encoding='utf-8')
(ROOT/'out'/'SOURCE_LOCATORS.json').write_text(json.dumps(extracts, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'sources_read': len(receipts), 'source_errors': 0, 'selected_paper_passages_only': True}))
