from pathlib import Path
import json
import re
import sqlite3

BASE = Path('~')
OUT = Path(__file__).resolve().parent

def read_small(path, cap=18000):
    if path.is_file():
        content = path.read_text(encoding='utf-8-sig', errors='replace')
        print(f'FILE {path}\n{content[:cap]}')
    else:
        print('MISSING', path)

for slug in ['perceptron_proof_open_gaps_fleet_2026_07_12', 'proof_steps_need_derived_joint_structure_2026_09_09', 'fpp_gap_event_is_the_overlap_event_2026_08_22']:
    read_small(BASE/'.claude/projects/<project>/memory'/f'{slug}.md', 12000)

for worker in ['w540','w541','w542','w543','w545','w546','w547','w548','w549','w550','w551']:
    folder=BASE/'brain_workers'/worker
    read_small(folder/'STATUS.md', 2200)
    if worker=='w543':
        print('PAIRED_ARTIFACT_NAMES', [(p.name, p.stat().st_size) for p in folder.iterdir() if p.is_file() and p.name in {'ATTEMPT.md','CLAIMS.jsonl','SOURCE_STATUS.json','REPORT.md','REVIEW_PACKET.md'}])

for folder in [BASE/'Big Open problem in probability theory', BASE/'math-brain-build/export/population', BASE/'math-research-brain']:
    if folder.is_dir():
        print('SOURCE_FOLDER_NAMES', folder, [p.name for p in folder.iterdir() if not p.name.lower().endswith(('.pem','.key','.env'))][:80])
    else:
        print('MISSING_FOLDER', folder)

store=BASE/'math-brain-build/local/population/brain.sqlite3'
if store.is_file():
    connection=sqlite3.connect(f'file:{store.as_posix()}?mode=ro', uri=True, timeout=5)
    print('STORE_TABLES', [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")])
    for table in ['claims','nodes','cards','concepts','sources']:
        if connection.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone():
            print('STORE_COLUMNS', table, connection.execute(f'PRAGMA table_info({table})').fetchall())
    connection.close()

read_small(BASE/'primary_directive/hooks1000/README.md', 12000)

