from pathlib import Path
import difflib
import json
import re

from facets import FACETS
from save_row import STATEMENTS

ROOT=Path(__file__).resolve().parent
IDS=['P0209','P0459','C0130','P0088','P0336','C0022','C0076','C0117','P0009','P0035']
ASSUMPTIONS={
 'P0209':['s is an integer at least two','Independent stationary Y and Z chains with the displayed rates','The normalization uses the displayed additive-functional asymptotic variance'],
 'P0459':['n>=2 and 1<=k<=n-1','Common iid continuous edge costs','Both endpoints choose their k lowest costs','0<eta<1'],
 'C0130':['Deterministic nearest-neighbor environment with at most M cookies per site, then fair transitions','Uniform ellipticity by a fixed epsilon>0','Start at one with fresh positive-site cookies','Fixed finite interval for the finite-state representation'],
 'P0088':['Finite family of probabilities in [0,1] and independent coordinates','Full target labels are retained','Countable adaptive exposure and history spaces','Conditional kernel error bounds hold uniformly whenever histories agree'],
 'P0336':['Uniform probability marginals on the two stated rectangles','Euclidean distance is the primary cost','epsilon>0 for each perturbed cost'],
 'C0022':['P and Q are probability laws on the same measurable space','The separating events are measurable functions of the observed object','The two wrong-side probability sums are finite'],
 'C0076':['The two-sided one-arm bounds are hypotheses','A finite strictly positive scaled-event-mass limit is assumed for the exponent lemma','n>=8 and the spike center is uniform on [5/4,7/4]','Path non-tightness is a toy-process obstruction, not a percolation counterexample'],
 'C0117':['n>=2 and the graph is K_n','Simple random walk from one fixed vertex','Continuous holding times, if used, are independent mean-one exponentials','s>=0 for the centered tail bound'],
 'P0009':['Manhattan orientations are exactly as stated','A mirror switches axes and a blank vertex keeps the axis','The displayed configurations have no additional mirrors','The example concerns pathwise monotonicity, not iid almost-sure localization'],
 'P0035':['Finite Cartesian product of infinite regular rooted trees','Integer b_i>=2','0<lambda<min_i b_i','Closer neighbors have weight lambda and farther neighbors weight one']}

FACET_ASSUMPTIONS={
 'rare-state-standardization':ASSUMPTIONS['P0209'],
 'bilateral-mean':ASSUMPTIONS['P0459'][:3],
 'cookie-interval-state':['Fixed finite interval [0,L]','Deterministic nearest-neighbor cookie stacks, at most M cookies per site, then fair transitions'],
 'adaptive-marked-coupling':['Countable history and exposure spaces','Uniform conditional kernel variation bounds at matched histories','At most m steps, except a separately bounded tail event'],
 'rectangle-vertical-stability':['The two stated uniform probability marginals','Euclidean distance cost'],
 'moment-nonsingularity':['The two probability vectors on the stated common four-point support'],
 'one-arm-exponent':['Fixed 0<c<=C<infinity','The two-sided event-probability bounds','A finite strictly positive scaled-mass limit is assumed'],
 'complete-clock-variance':['Simple random walk on K_n, n>=2','Independent mean-one exponential holding times for the continuous-time convention'],
 'bijective-pinball-routing':['Two incoming and two outgoing edges per Manhattan vertex','The local routing is a permutation of incoming edges to outgoing edges'],
 'tree-product-coordinate':['Finite product of regular rooted trees','lambda>0','lambda<b_i for the coordinate-transience conclusion; lambda<min b_i for all coordinates']}

def proof_for_bundle(pid):
    paragraphs=(ROOT/(pid+'.md')).read_text(encoding='utf-8').split('\n\n')
    omitted=('Label:','Literature status:','Checks:','Sources:','Source:','Prior work:','Status:','# ')
    text='\n\n'.join(p for p in paragraphs if not p.startswith(omitted))
    # The source memory quote belongs only in the local audit report, not in a draft body.
    text=text.replace('This corrects the saved memory\'s assertion, "It does not - its standard deviation stays near 1". The variance argument in that sentence cannot disprove convergence in probability.',
                      'A nonvanishing variance does not disprove convergence in probability; a second-moment limit needs uniform integrability of the squares.')
    return text

def write_json(path,data):
    path.parent.mkdir(exist_ok=True,parents=True)
    part=path.with_suffix('.part')
    part.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    part.replace(path)

def quote(text,limit=380):
    text=text.replace('\r',' ').replace('\n',' ')
    if len(text)<=limit:
        return text
    end=text.rfind(' ',0,limit)
    return text[:end]

def main():
    rows=[json.loads(line) for line in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines()]
    completed={r['problem_id']:r for r in rows if r.get('proof_path')}
    assert set(completed)==set(IDS)
    revised=[]
    for pid in IDS:
        if completed[pid]['statement']!=STATEMENTS[pid][2] or completed[pid]['label']!='proof':
            row=dict(completed[pid])
            row['supersedes']=[row['row_id']]
            row['row_id']='S1.w337.'+pid+('.r3' if completed[pid]['row_id'].endswith('.r2') else '.r2')
            row['statement']=STATEMENTS[pid][2]
            row['label']='proof'
            revised.append(row)
            completed[pid]=row
    if not any(r['row_id']=='S1.w337.001r1' for r in rows):
        revised.append({'row_id':'S1.w337.001r1','problem_id':'P0209','label':'status-audit',
          'verdict':'RECONCILED','supersedes':['S1.w337.001'],
          'statement':'candidate_fu denotes a full-answer candidate and is consistent with a negative answer. Inspection of the original proof and store attempt resolves the initial apparent conflict. The later memory explanation, unlike the original proof, incorrectly inferred failure of convergence in probability from a nonvanishing variance.',
          'evidence_path':(ROOT/'P0209.md').as_posix(),'auditor':'w347','audit_state':'PENDING'})
    if revised:
        with (ROOT/'results.jsonl').open('a',encoding='utf-8') as f:
            for row in revised:
                f.write(json.dumps(row,ensure_ascii=False)+'\n')
    cards=json.loads((ROOT/'evidence'/'store_cards.json').read_text(encoding='utf-8'))
    entries=[]; relations=[]; edge_evidence=[]
    for pid in IDS:
        ns,name,stmt=STATEMENTS[pid]
        entries.append({'key':'result-'+pid.lower(),'namespace':ns,'logical_name':name,'kind':'lemma',
          'title':'[Blind audit pending] '+name.replace('-',' '),'statement':stmt,
          'proof_text':proof_for_bundle(pid),
          'assumptions':ASSUMPTIONS[pid],'domain':'probability theory',
          'source':{'source_id':'owner-campaign:w337:'+pid+':20261010','url':(ROOT/(pid+'.md')).as_uri(),
                    'revision':'author-check-2026-10-10','license':'owner-own-work (campaign proof; blind audit pending)','excerpt':None}})
    for facet in FACETS:
        pid=facet['problem']
        entries.append({'key':facet['key'],'namespace':facet['namespace'],'logical_name':facet['name'],
          'kind':facet['kind'],'title':'[Blind audit pending] '+facet['name'].replace('-',' '),
          'statement':facet['statement'],'proof_text':facet['proof'],'assumptions':FACET_ASSUMPTIONS[facet['key']],
          'domain':'probability theory','source':{'source_id':'owner-campaign:w337:'+pid+':'+facet['key']+':20261010',
           'url':(ROOT/(pid+'.md')).as_uri(),'revision':'author-check-2026-10-10',
           'license':'owner-own-work (campaign proof; blind audit pending)','excerpt':None}})
    bykey={e['key']:e for e in entries}
    def edge(source,target,kind,description,target_quote,target_card_id=None,existing=False):
        source_quote=quote(bykey[source]['statement'])
        target_quote=quote(target_quote)
        rel={'from_key':source,'kind':kind,
             'rationale':'Source: "'+source_quote+'". Target: "'+target_quote+'". '+description}
        rel['to_existing_logical' if existing else 'to_key']=target
        relations.append(rel)
        edge_evidence.append({'from_key':source,'target':target,'kind':kind,'source_quote':source_quote,
                              'target_quote':target_quote,'existing_card_id':target_card_id})
    for pid in IDS:
        anchors=[c for c in cards if c['problem_id']==pid and c['title'].startswith(('Open problem:','Attempt on '))]
        assert len(anchors)==2
        for card in anchors:
            text=card['body']
            if card['title'].startswith('Open problem:') and '). ' in text:
                text=text.split('). ',1)[1].split(' Source: ',1)[0]
            elif ' Result: ' in text:
                text=text.split(' Result: ',1)[1]
            edge('result-'+pid.lower(),card['metadata']['logical_id'],'cites',
                 'Addresses the cached question or continues this author-only attempt; it does not certify full resolution.',
                 text,card['id'],True)
        if pid in ('P0459','P0088','P0035'):
            card=next(c for c in anchors if c['title'].startswith('Attempt on '))
            text=card['body'].split(' Result: ',1)[1]
            edge('result-'+pid.lower(),card['metadata']['logical_id'],'generalizes',
                 {'P0459':'Extends the sufficient threshold regime to an explicit actual-mean bound and arbitrary error probability.',
                  'P0088':'The vector coupling retains marks and implies the older count bound by projection.',
                  'P0035':'The product result includes the old regular-tree calculation at m=1.'}[pid],text,card['id'],True)
        if pid=='C0130':
            card=next(c for c in anchors if c['title'].startswith('Attempt on '))
            pos=card['body'].find('finite vector')
            assert pos>=0
            text=card['body'][max(0,pos-80):]
            edge('result-c0130',card['metadata']['logical_id'],'refutes',
                 'Refutes only the whole-half-line finite-state interpretation; fixed-interval truncations remain valid.',
                 text,card['id'],True)
    for facet in FACETS:
        pid=facet['problem']
        kind='cites' if pid=='P0009' else 'depends_on'
        edge('result-'+pid.lower(),facet['key'],kind,
             'This explicit reusable step is proved or defined within the same problem report.',facet['statement'])
    draft={'spec':'mathbrain-draft-v1','author_agent':'w337','bundle_slug':'team-o-ten-problem-checks-w337-20261010',
           'entries':entries,'relations':relations}
    write_json(ROOT/'bundles'/'bundle_001.json',draft)
    write_json(ROOT/'evidence'/'edge_quotes.json',edge_evidence)
    inbox=Path('~/math-brain-inbox/w337')
    target=next(inbox/f'bundle_{i:03d}.json' for i in range(1,1000) if not (inbox/f'bundle_{i:03d}.json').exists())
    patch=''.join(difflib.unified_diff([], (ROOT/'bundles'/'bundle_001.json').read_text(encoding='utf-8').splitlines(True),
              fromfile='a/'+target.as_posix(),tofile='b/'+target.as_posix()))
    (ROOT/'patches').mkdir(exist_ok=True)
    (ROOT/'patches'/'01_ten_problem_bundle.diff').write_text(patch,encoding='utf-8')
    hooks=[
     {'id':'math-w337-01','area':'math','event':'UserPromptSubmit',
      'cue':r'(?is)(?:variance|standard deviation|second moment).{0,80}(?:does not|cannot|rules out|prevents).{0,80}(?:convergence|converge|vanish).{0,35}(?:in probability|probabilit)',
      'fire_when':'Its standard deviation stays near one, which rules out convergence in probability to zero.',
      'silent_when':'The variance calculation gives convergence in L2 under a proved uniform-integrability bound.',
      'text':'Variance bounded away from zero does not prevent convergence to zero in probability. Before passing second moments through that limit, prove uniform integrability of the squares; rare events can carry all the variance.',
      'evidence':'memory:aldous_fill_430_refuted_by_a_rare_state_four_state_chain_2026_09_08; w337/P0209.md; measurements/p0209.json',
      'proposer':'w337'},
     {'id':'math-w337-02','area':'math','event':'UserPromptSubmit',
      'cue':r'(?is)(?:bounded|finite).{0,45}cookie.{0,90}finite.?state.{0,80}(?:half.?line|whole|unbounded|infinite lattice)',
      'fire_when':'Bounded cookie stacks give a finite-state escape problem on the whole half-line.',
      'silent_when':'On the fixed interval [0,L], position and cookie counts form a finite state chain.',
      'text':'Bounded cookies per site still leave an unbounded vector of visited-site histories. Specify a finite interval and count its states. Finite-interval hitting probabilities are upper bounds on escape; a lower bound needs a separate tail argument.',
      'evidence':'w337/C0130.md; measurements/c0130.json: state bound grows from 3 at L=2 to 15309 at L=8',
      'proposer':'w337'}]
    controls=[]
    for h in hooks:
        assert len(h['text'])<=300
        assert re.search(h['cue'],h['fire_when'])
        assert not re.search(h['cue'],h['silent_when'])
        controls.append({'id':h['id'],'fire_pass':True,'silent_pass':True})
    (ROOT/'proposals').mkdir(exist_ok=True)
    hook_text=''.join(json.dumps(h,ensure_ascii=False)+'\n' for h in hooks)
    (ROOT/'proposals'/'math-w337.jsonl').write_text(hook_text,encoding='utf-8')
    hook_target=Path('~/primary_directive/hooks1000/proposals/math-w337.jsonl')
    # If another session has already proposed under this name, preserve it in the append diff.
    old=hook_target.read_text(encoding='utf-8') if hook_target.is_file() else ''
    assert len(old)<50000,'Existing same-agent proposal file is too large for a bounded append patch'
    new=old+('' if not old or old.endswith('\n') else '\n')+hook_text
    hook_patch=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),
                    fromfile='a/'+hook_target.as_posix(),tofile='b/'+hook_target.as_posix()))
    (ROOT/'patches'/'02_math_hook_proposals.diff').write_text(hook_patch,encoding='utf-8')
    write_json(ROOT/'measurements'/'hook_controls.json',{'command':'python -X utf8 package_handoff.py','controls':controls,
                'scope':'two prescribed fire and two silent controls only; no live deployment or pilot fires'})
    audit={'auditor':'w347','manager':'claude-4a88bc43','state':'PENDING_BLIND_CHECK',
           'result_rows':[completed[pid]['row_id'] for pid in IDS],
           'entries':[{'key':e['key'],'logical_name':e['logical_name'],'kind':e['kind']} for e in entries],
           'bundle_path':(ROOT/'bundles'/'bundle_001.json').as_posix(),
           'edge_evidence_path':(ROOT/'evidence'/'edge_quotes.json').as_posix(),
           'verification_scripts':[str(ROOT/(pid.lower()+'_check.py')) for pid in IDS],
           'requested_verdicts':'KEEP/FIX/DROP per entry; verify every quoted edge and mathematical hypotheses independently.',
           'full_proof_check_required_before_solution_claim':['P0209'],
           'solution_counted':False,'literature_novelty_verified':False,'lean_certification':'UNAVAILABLE: compute admission refused',
           'delivery_mode':'local reviewer handoff; worker brief prohibits mesh send commands and writes outside its folder',
           'draft_destination_after_review':target.as_posix()}
    write_json(ROOT/'AUDIT_REQUEST_w347.json',audit)
    (ROOT/'PROGRESS_PENDING.jsonl').write_text(json.dumps({'agent':'w337','row':'S1.w337.P0209',
      'event':'w337 saved ten problem reports, twenty typed draft nodes and thirty-four quoted edges; blind review pending',
      'evidence':(ROOT/'REPORT.md').as_posix(),'delivery':'manager posts on landing; no worker external write'})+'\n',encoding='utf-8')
    print(json.dumps({'problem_results':len(IDS),'draft_entries':len(entries),'quoted_relations':len(relations),
                      'hook_proposals':len(hooks),'destination_after_review':target.as_posix(),'audit':'PENDING'}))

if __name__=='__main__':
    main()
