"""Final consistency check. Writes the manifest after every other artifact settles."""
import json,hashlib,pathlib,math,csv,datetime
R=pathlib.Path(__file__).resolve().parent
def read(n):return json.load(open(n+'.json'))
def main():
    required=['STATUS.md','RESULTS.md','REPORT.md','REFEREE.md','PROOFS.md','FAMILIES.md','FAMILIES.csv','LITERATURE.md','LEARNINGS.md','reproduce.sh']
    for name in required:assert pathlib.Path(name).is_file() and pathlib.Path(name).stat().st_size
    fc=read('final_checks');co=read('composition');au=read('audit');pm=read('pm')['data'];native=read('native_audit');res=read('resources')
    assert max(fc['census4']['errors'].values())<1e-12
    assert max(au['data']['errors'].values())<1e-12
    assert max(co['validation']['errors'].values())<1e-12
    assert fc['structural']['composition_L_error']<1e-12
    assert abs(native['PM_all_core']['mp_residual'])<1e-12
    assert abs(native['cyclic16']['residual'])<1e-12
    assert abs(native['cyclic16']['E_residual'])<1e-10
    assert res['all_nice_10'] and res['max_instrumented_python_rss_bytes']<3*1024**3
    assert au['data']['adaptive_counterexample']['adaptive']<au['data']['adaptive_counterexample']['E']
    assert pm['tail_upper']<1e-10
    ledger=list(csv.DictReader(open('FAMILIES.csv')))
    assert len(ledger)>1000
    for r in ledger:
        assert math.isfinite(float(r['F'])) and math.isfinite(float(r['E']))
        assert float(r['F'])>=float(r['E'])-1e-10
    # Negative roundoff gaps are harmless, but no row may claim a false lower witness bound.
    extent=sum(p.stat().st_size for p in R.rglob('*') if p.is_file());assert extent<1024**3
    d=dict(status='PASS',ledger_rows=len(ledger),folder_bytes=extent,maximum_composition_residual_bits=max(co['validation']['errors']['L'],fc['structural']['composition_L_error']),PM_mp_residual=native['PM_all_core']['mp_residual'],Fano_90digit=fc['fano']['F_finite'],native_precision=native['native_precision'])
    json.dump(d,open('delivery_audit.json','w'),indent=2)
    paths=[p for p in sorted(R.rglob('*')) if p.is_file() and p.name not in ['manifest.json','events.jsonl'] and '__pycache__' not in p.parts]
    hashes={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    json.dump(dict(created=datetime.datetime.now().isoformat(),excluded_live_files=['events.jsonl'],files=hashes),open('manifest.json','w'),indent=2)
    print(json.dumps(d,indent=2))
if __name__=='__main__':main()
