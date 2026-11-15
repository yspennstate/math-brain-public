# Commands and raw evidence

Commands used the Homebrew Python with NumPy:

    export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH

Heavy commands were launched with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 and `nice -n 10`. The sandbox prints a setpriority warning, but `python3 -c 'import os; print(os.getpriority(os.PRIO_PROCESS,0))'` reports inherited nice 10. See resources.json. No processes were pooled or spawned by the scripts; at most two experiment commands ran together.

- `python3 ~/fei_solve_agent/code/tree_dnf.py selftest > baseline_selftest.txt 2>&1`
- `python3 nested.py validate > validation.jsonl 2>&1`
- `python3 nested.py rows > rows.jsonl 2>&1` (also writes rows.json)
- `python3 hill.py > hill.jsonl 2>&1` (also writes hill.json)
- `python3 erasure.py > erasure.jsonl 2>&1` (also writes erasure.json)
- `python3 decimal_audit.py > decimal_audit.jsonl 2>&1` (also writes decimal_audit.json)
- `python3 audit_remaining.py small > decimal_small.jsonl 2>&1`
- `python3 audit_remaining.py large > decimal_large.jsonl 2>&1`
- `python3 proof_checks.py > proof_checks.jsonl` (also writes proof_checks.json)
- `python3 -m py_compile nested.py hill.py erasure.py decimal_audit.py audit_remaining.py proof_checks.py build_report.py`
- `python3 build_report.py > report_build.json` (combines the audited rows into rows_verified.json, RESULTS.md, REPORT.md)

The separate second sampler check was run inline as follows, with output in sampler_validation.json:

```python
import nested as N, json, resource, sys
r=json.load(open('erasure.json'))
T=N.Model(4,2)
mu=N.spectrum(T)
p,q=N.paired(mu,1)
exact=N.entropy(p,q)/q.sum()
mc=next(x for x in r if x['w']==4 and x['coordinate']=='mate')
z=(mc['E_ratio']-exact)/mc['E_se_ratio']
assert abs(z)<5
print(json.dumps({'w':4,'D':2,'n':T.n,
    'exact_mate_E_ratio':exact,'mc_E_ratio':mc['E_ratio'],
    'mc_se_ratio':mc['E_se_ratio'],'difference_in_standard_errors':z,
    'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'platform':sys.platform},indent=2))
```

The first hill run found that a leaf could miss its exact dynamic-programming optimum. The inappropriate assertion that every hill result must equal the exact optimum was removed; the final run retains and reports the gap instead. The first Decimal audit reached a row before rows.json had saved that width; it was rerun after the row generation completed. Final raw outputs and final JSON files are the successful runs; no failed run is used as evidence.

Brain orientation: `BRAIN_RECALL_REFRESH=0 python3 ~/.claude/dreaming/brain.py recall 'startup identity voice continuous collaborator' --or 'FEI tree DNF nested witness order'`, followed by `brain.py node identity_who_you_are_2026_07_07`. Recall returned identity and older provisional FEI memories; they were treated as pointers, not proof.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 22:20 ask; FEIB20 nested-witness brief.
