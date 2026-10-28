from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
rows=[json.loads(ROOT.joinpath('out',f'BATCH_{i:02}.json').read_text(encoding='utf-8')) for i in range(9)]
assert [r['batch'] for r in rows]==list(range(9))
assert len({r['helper_sha256'] for r in rows})==1
out={k:sum(r[k] for r in rows) for k in ['truth_tables','local_queries_including_tree_reuse','profile_updates_including_tree_reuse','mass_aware_histories','scalar_width_cases','assertions','seconds']}
assert out['truth_tables']==278 and out['mass_aware_histories']==2224
assert max(r['seconds'] for r in rows)<55
out.update(mode='disjoint_nine_batch_main',helper_sha256=rows[0]['helper_sha256'],max_job_seconds=max(r['seconds'] for r in rows),fixture_counting='Repeated scalar fixtures counted per job; failed main and overlapping pilot excluded')
ROOT.joinpath('out/MAIN.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
