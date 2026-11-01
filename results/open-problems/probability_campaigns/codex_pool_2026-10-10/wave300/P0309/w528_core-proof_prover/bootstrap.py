import json, os, pathlib, subprocess, time

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
ROOT = pathlib.Path(__file__).resolve().parent

def run(label, argv, timeout=60, limit=18000):
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout)
        data = {'label': label, 'command': argv, 'exit_code': proc.returncode, 'seconds': round(time.monotonic()-started,3), 'stdout': proc.stdout, 'stderr': proc.stderr}
    except subprocess.TimeoutExpired as exc:
        data = {'label': label, 'command': argv, 'seconds': round(time.monotonic()-started,3), 'status':'TIMEOUT', 'stdout': str(exc.stdout or ''), 'stderr': str(exc.stderr or '')}
    (ROOT / (label + '.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(data, ensure_ascii=False)[:limit], flush=True)
    return data

if __name__ == '__main__':
    import sys
    mode=sys.argv[1]
    if mode == 'recall':
        run('brain_recall', ['python','-X','utf8','~/.claude/dreaming/brain.py','recall','P0309 Riesz crystallization proof mistakes'], timeout=60, limit=6000)
    elif mode == 'paths':
        base=pathlib.Path('~/<private-repo>/06_math_research')
        for name in ['RANKING_2026-09-07.csv']:
            p=base/'probability_1000_intake_claude_20260907'/name
            if p.exists():
                for i,line in enumerate(p.open(encoding='utf-8'),1):
                    if 'P0309' in line: print(str(p),i,line.rstrip())
        for p in sorted(base.glob('probability_1000_intake_*')):
            print('INTAKE_DIR', str(p))
            run('rg_intake_'+p.name, ['rg','-l','--glob','*.json*','--glob','*.csv','--glob','*.md','P0309',str(p)], timeout=45, limit=6000)
        for dirname in ['probability_1000_attempts_H_20260912','probability_1000_attempts_I_20260914','prob1000_lean_20260908']:
            p=base/dirname
            if p.exists(): run('rg_'+dirname,['rg','-n','--max-count','5','--glob','*.md','--glob','*.json*','--glob','*.csv','--glob','*.lean','P0309|Riesz|crystall',str(p)],timeout=45,limit=6000)
    elif mode == 'paths2':
        base=pathlib.Path('~/<private-repo>/06_math_research')
        for p in sorted(base.glob('probability_1000_intake_*')):
            run('rg_v2_'+p.name, ['rg','-l','--no-ignore','--glob','*.json*','--glob','*.csv','--glob','*.md','--glob','*.txt','--glob','*.py','P0309|Positive-temperature crystalline Gibbs',str(p)], timeout=35, limit=2800)
        for p in base.iterdir():
            if p.is_file() and ('brain' in p.name.lower() or p.suffix in ('.db','.sqlite','.sqlite3')):
                print('CANONICAL_STORE_CANDIDATE',str(p),flush=True)
    elif mode == 'instructions':
        for raw in ['~/brain_workers/teams/W0300_O/TEAM_BOARD.md','~/primary_directive/hooks1000/README.md','~/math-brain-inbox/BUNDLE_SPEC.md']:
            p=pathlib.Path(raw)
            print('FILE',raw,'EXISTS',p.exists(),flush=True)
            if p.exists(): print(p.read_text(encoding='utf-8')[:15000],flush=True)
        run('audit_assignments',['rg','-n','--max-count','5','w528','~/primary_directive/hooks1000/AUDIT_ASSIGNMENTS.md'],limit=2000)
        run('memory_matches',['rg','-n','--max-count','12','Riesz|crystall|perceptron_proof_open_gaps_fleet_2026_07_12','~/.claude/projects/<project>/memory/MEMORY.md'],limit=5000)
        p=pathlib.Path('~/.claude/projects/<project>/memory/perceptron_proof_open_gaps_fleet_2026_07_12.md')
        print('SCAR',str(p),'EXISTS',p.exists(),flush=True)
        if p.exists(): print(p.read_text(encoding='utf-8')[:9500],flush=True)
