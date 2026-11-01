"""Save offline source receipts and local-only progress/hook handoffs."""
import difflib
import json
import re
from pathlib import Path
from package_result import ROOT,IDS

def append(path,row):
    with path.open('a',encoding='utf-8') as file:file.write(json.dumps(row,ensure_ascii=False)+'\n')

def run():
    (ROOT/'sources').mkdir(exist_ok=True)
    problem_cards=json.loads((ROOT/'problem_cards.json').read_text(encoding='utf-8'))
    campaign=json.loads((ROOT/'campaign_sources.json').read_text(encoding='utf-8'))
    source_rows=[]
    for pid in IDS:
        card=problem_cards[pid][0]
        exact=card['body'].split('Source: ',1)[1].split(' Status notes:',1)[0].split('\\nPosed',1)[0]
        row=dict(row_id=f'w336.{pid}.source-status',problem_id=pid,kind='source-status',
                 label='offline-current-status-unverified',historical_reference=exact,
                 source_node_id=card['id'],source_logical_id=json.loads(card['metadata_json'])['logical_id'],
                 source_quote=card['body'],current_literature_closure_verified=False,audit_status='pending-w346')
        if pid in campaign:
            records=[r for r in campaign[pid] if r['file'].endswith('problems.jsonl')]
            last=records[-1]
            row['latest_cached_ledger']=dict(path=last['file'],line=last['line'],
                result_status=last['row'].get('result_status'),verification=last['row'].get('verification'),
                recorded_at=last['row'].get('recorded_at'))
            if pid=='P0294':
                row['literature_lead']=last['row'].get('result_status')
                row['lead_verdict']='Unverified scope match; not a confirmed answer to the continuous-workload question.'
        source_rows.append(row)
        append(ROOT/'results.jsonl',row)
    (ROOT/'sources/status_checks.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in source_rows),encoding='utf-8')
    # Save short primary-source excerpts that were actually read.
    base=Path('~/Downloads/Probability_1000_intake_claude_20260907/sources')
    excerpts=[]
    for pid,name,needle in [('C0129','kosygina_zerner_erw_2012','Problem 3.11.'),
                           ('C0020','garban_steif_noise_2012','Open Question: Find the smallest'),
                           ('C0116','ding_lee_peres_cover_2012','Question 5.1.'),
                           ('C0074','heydenreich_hofstad_highd_2017','Open Problem 14.2 (')]:
        path=base/name/'text.txt'
        lines=path.read_text(encoding='utf-8',errors='replace').splitlines()
        at=next(i for i,s in enumerate(lines) if needle in s)
        excerpts.append(dict(problem_id=pid,path=str(path),first_line=at+1,
                             excerpt=' '.join(lines[at:at+3]),scope='Source-era question; no later closure verified.'))
    (ROOT/'sources/primary_excerpts.json').write_text(json.dumps(excerpts,ensure_ascii=False,indent=2),encoding='utf-8')
    hook=dict(id='cookie-critical-mean-w336-01',area='math',event='PreToolUse',
      cue=r'(?is)(?=.*\b(?:finite|bounded)[ -]cookie\b)(?=.*\b(?:fair|unbiased)\b)(?=.*(?:Lyapunov|log[ -]mean)).*',
      fire_when='A finite-cookie, fair-tail branching reduction invokes a Lyapunov or log-mean criterion.',
      silent_when='A standard BPRE has nonunit offspring means, or the finite-cookie calculation does not invoke a log-mean route.',
      text='Before a finite-cookie branching argument uses a log-mean test, compute the quenched prefix moments. With fair tails and m>=M, E F_m=m-delta: the linear coefficient is one. Track migration and check m<M separately.',
      evidence='~/brain_workers/w336/measurements/C0129.json: 365 exact moment cases; boundary m<M gives 3/8 rather than 0; proofs/C0129.md.',
      proposer='w336')
    assert len(hook['text'])<=300
    cases=[
      ('finite cookie stack with fair tail: use a Lyapunov exponent',True),
      ('bounded cookie prefix, fair tail, log-mean criterion',True),
      ('Lyapunov test for a finite-cookie stack followed by unbiased trials',True),
      ('finite cookie model; fair coins; LOG MEAN growth',True),
      ('BOUNDED COOKIE stack and fair tail: Lyapunov test',True),
      ('ordinary BPRE: use a log-mean criterion with nonunit offspring means',False),
      ('infinite cookie stack, fair tail, Lyapunov exponent',False),
      ('finite cookie stack with biased tail: Lyapunov exponent',False),
      ('finite cookie prefix with fair tail: compute exact failure moments',False),
      ('Brownian cover-time approximation and a Gaussian maximum',False)]
    controls=[]
    for text,want in cases:
        actual=bool(re.search(hook['cue'],text))
        controls.append(dict(text=text,expected=want,actual=actual))
        assert actual==want
    (ROOT/'hook_proposals').mkdir(exist_ok=True)
    payload=json.dumps(hook,ensure_ascii=False)+'\n'
    (ROOT/'hook_proposals/math-w336.jsonl').write_text(payload,encoding='utf-8')
    (ROOT/'measurements/hook_controls.json').write_text(json.dumps(dict(cases=10,passed=10,false_fires=0,false_silences=0,
        controls=controls,scope='Local cue controls; no installed-hook pilot or peer KEEP.'),indent=2),encoding='utf-8')
    target='~/primary_directive/hooks1000/proposals/math-w336.jsonl'
    patch=''.join(difflib.unified_diff([],payload.splitlines(keepends=True),fromfile='a/'+target,tofile='b/'+target))
    (ROOT/'patches/11_math_hook.diff').write_text(patch,encoding='utf-8')
    append(ROOT/'results.jsonl',dict(row_id='w336.hook.001',kind='hook-proposal',label='measured-local-controls',
        proposal_path='hook_proposals/math-w336.jsonl',measurement_path='measurements/hook_controls.json',
        result='10/10 cue controls passed; no installed pilot',audit_status='pending-pair-audit'))
    lean=json.loads((ROOT/'measurements/lean_receipt.json').read_text(encoding='utf-8'))
    append(ROOT/'results.jsonl',dict(row_id='w336.lean.001',problem_id='P0208',kind='formal-check-receipt',
        label='setup-unverified',verdict=lean['stdout'].strip(),source_path='lean/CyclePoisson.lean',
        receipt_path='measurements/lean_receipt.json',claim='No Lean certificate obtained.'))
    cost=dict(agent='w336',declared_login='proofswarm',date='2026-10-10',
        billable_tokens=None,monetary_cost=None,usage_note='Not available in worker tool receipts; no estimate invented.',
        recorded_check_seconds=sum(json.loads((ROOT/'measurements'/f'{pid}.json').read_text(encoding='utf-8')).get('seconds',0) for pid in IDS[1:])
            +json.loads((ROOT/'measurements/P0087_stationary_law.json').read_text(encoding='utf-8'))['seconds'],
        timing_scope='Sum of per-check wall times; excludes P0208, shell startup, reading and writing.',
        recall_timeout_seconds=60,lean_wrapper_calls=1,lean_certificates=0,live_ingester_calls=0,
        direct_web_searches=0,mesh_sends=0,source_current_openness_certificates=0,independent_keeps=0)
    (ROOT/'COST_RECEIPT.json').write_text(json.dumps(cost,indent=2),encoding='utf-8')
    append(ROOT/'progress_rows.jsonl',dict(agent='w336',row='S1.O.w336',
        event='Ten assigned problems checked; 15 candidate cards and 31 quoted edges ready for w346; no solved claim.',
        evidence=str(ROOT/'REPORT.md'),shared_post_status='Not sent: worker forbids shared progress writes and mesh sends.'))
    (ROOT/'RESUME.md').write_text('Read STATUS.md and the 15 keyed claims in CARD_INDEX.json.\n'
        'The ten assigned attempts are staged for w346; do not count them without KEEP or ingest during this worker session.\n'
        'After review, the first apparently unclaimed board row observed was C0143 at TEAM_BOARD.md:168; recheck its claim before taking it in a new task.\n'
        'The obsolete Codex worktree ledger path is gone; its cache is Downloads/Probability_1000_20h_20260906.\n'
        'Shared progress and hook writes were not performed; their local receipts/diff are ready for the authorized reviewer.\n'
        'A full P0087 stationary-law proof is saved; path convergence and its initial layer remain outside this result.\n',encoding='utf-8')
    print(json.dumps(dict(source_status_rows=len(source_rows),primary_source_excerpts=len(excerpts),hook_controls='10/10',
                          recorded_check_seconds=cost['recorded_check_seconds'],independent_keeps=0)))

if __name__=='__main__':run()
