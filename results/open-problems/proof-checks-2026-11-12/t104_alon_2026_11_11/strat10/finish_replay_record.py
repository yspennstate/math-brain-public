"""Record the one full replay and its already-completed targeted type correction."""
import json,hashlib
from pathlib import Path

def main():
    path=Path('replay_summary.json');data=json.loads(path.read_text())
    failures=data['failures']
    assert len(failures)==1 and failures[0]['script']=='verify_family.py',failures
    target=Path('verify_family_fix.out').read_text();assert target.startswith('PROVED: r=1 connected residual family')
    assert all(c['status']=='PASS'or c['script']=='verify_family.py'for c in data['checks'])
    data['original_full_run_label']=data['label'];data['label']='PROVED current exact certificates verified; one full-run metadata failure corrected by targeted replay'
    data['full_replay_runs']=1
    data['resolved_failures']=[dict(script='verify_family.py',status='PASS targeted',output='verify_family_fix.out',reason='JSON tuple/list metadata mismatch; every reconstructed rational value matched; edge and rest fields now return lists',certificate_values_changed=False)]
    data['final_certificate_status']='PASS with recorded targeted correction'
    path.write_text(json.dumps(data,indent=2)+'\n')
    line='PROVED: PASS (targeted correction): verify_family.py. Every current exact certificate is verified. The one full run and its original FAIL line are retained; the full run was not repeated.'
    with open('replay_all.out','a')as f:f.write('\n'+line+'\n')
    peak=max(c['peak_RSS_MiB']for c in data['checks']);seconds=data['total_seconds']
    p=Path('RESULT.md');text=p.read_text()
    old='OPEN: The final one-pass replay result will be recorded in replay_all.out and replay_summary.json.'
    assert old in text
    text=text.replace(old,'PROVED: Every current exact certificate passed. The one full sequential run reported a tuple/list metadata mismatch in verify_family.py. Returning the reconstructed edge/rest metadata as lists changed no certificate value; its targeted rerun passed. The original FAIL and correction remain in replay_all.out, with original failures and their resolution separated in replay_summary.json. The full run was not repeated. No box splitting or new numerical search followed the stop instruction.')
    measurements=f'NUMERICAL: The full sequential replay took {seconds:.3f} seconds and peaked at {peak:.3f} MiB RSS. These operational measurements are separate from exact certificate signs.'
    text=text.replace('## OPEN\n',measurements+'\n\n## OPEN\n')
    text=text.replace('The complete machine-readable table is ceiling_table.csv', 'The r=0 entry is auxiliary; the actual stratum has r>0. The complete machine-readable table is ceiling_table.csv')
    p.write_text(text)
    with open('LOG.md','a')as f:f.write('\n'+line+'\n\n'+measurements+'\n\nPROVED partial: finalization complete. RESULT.md, LOG.md, replay_all.out and replay_summary.json are saved. OPEN: the corner neighborhood and 5244 retained leaves remain for a separate STRAT11 run. No new work is started. Task: “shrink region (11), aiming to close it” — received 2026-11-13 approximately 08:33 +04.\n')
    print(line);print(measurements)
if __name__=='__main__':main()
