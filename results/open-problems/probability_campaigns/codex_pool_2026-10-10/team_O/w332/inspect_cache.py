from pathlib import Path
import json

root=Path(__file__).resolve().parent
base=Path('~/Downloads')
paths=[base/'Probability_1000_intake_claude_20260907/sources/levine_peres_sandpiles_2017',base/'Probability_1000_intake_claude_20260907/sources/heydenreich_hofstad_highd_2017',base/'Probability_1000_intake_claude_20260907/sources/biskup_dgff_extrema_2020',base/'Probability_1000_20h_20260906']
out=[]
for path in paths:
    item={'path':str(path),'exists':path.exists()}
    if path.is_dir():
        item['immediate_files']=[p.name for p in path.iterdir() if p.is_file() and p.suffix in {'.txt','.json','.jsonl','.pdf','.md'}]
        item['immediate_directories']=[p.name for p in path.iterdir() if p.is_dir() and not any(word in p.name.lower() for word in ['bank','keys','test'])]
    out.append(item)
candidate=Path('~/.codex/worktrees/probability-1000-20h-20260906/06_math_research/probability_1000_20h_20260906')
out.append({'campaign_path':str(candidate),'exists':candidate.exists()})
(root/'reports/cache_availability.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
