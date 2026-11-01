"""Recompile each exact source and check its transitive axiom reports."""
from pathlib import Path
import json, subprocess, re
root=Path(__file__).resolve().parents[1]
receipt=json.loads((root/'verification/component_runs.json').read_text(encoding='utf-8'))
allowed={'propext','Classical.choice','Quot.sound'}
for run in receipt['runs']:
    result=subprocess.run(['lake','env','lean','-j1',run['source']],cwd=root,capture_output=True,text=True,encoding='utf-8',check=True,timeout=600)
    reports=re.findall(r'depends on axioms: \[(.*?)\]',result.stdout,re.S)
    assert len(reports)==run['declarations'], (run['source'],len(reports))
    for report in reports:
        assert set(x.strip() for x in report.split(','))<=allowed, report
    print(result.stdout)
    print(run['source'], 'fresh compiler run and axiom reports passed')
