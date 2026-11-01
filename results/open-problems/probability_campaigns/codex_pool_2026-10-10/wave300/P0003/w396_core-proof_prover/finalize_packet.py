"""Prepare/submit draft artifacts; never integrate a store or change live recall."""
from pathlib import Path
import difflib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
INBOX=Path('~/math-brain-inbox/w396')
NS='probability.selfavoiding'

def put(name,value):
    path=ROOT/name
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def entry(key,logical,kind,title,statement,proof,assumptions):
    return {'key':key,'namespace':NS,'logical_name':logical,'kind':kind,'title':title,'statement':statement,'proof_text':proof,'assumptions':assumptions,'domain':'probability and self-avoiding walks','source':{'source_id':'owner:w396:P0003:'+key,'url':'owner://primary-directive/P0003/w396/ATTEMPT.md#'+key,'revision':'draft-2026-10-10','license':'owner-own-work','excerpt':None}}

def prepare():
    entries=[
      entry('length-kernel','fixed-length-self-avoiding-continuation-kernel','lemma','Length is retained by fixed-length SAW conditioning',
        'DRAFT, mathematical review pending. In a finite graph with inherited positive edge weights, give each simple n-edge path starting at a probability proportional to its product weight, with terminal vertex free, and assume positive total weight C_n(G;a). Define C_m(H;v) as the total weight of simple m-edge paths from v in H, with C_0=1 for a retained vertex. At a realized k-edge prefix eta, delete all its visited vertices except its tip to get G_eta. For a forbidden vertex or edge set A excluding a, the conditional avoidance probability is zero if the prefix hit A, and otherwise C_(n-k)(G_eta minus A;tip)/C_(n-k)(G_eta;tip). The denominator is positive on every realized prefix; at k=n use the avoidance indicator. Replacing C_(n-k) by an all-length partition sum changes the model.',
        'Every completion is uniquely a simple (n-k)-edge path from the retained tip avoiding the earlier visited vertices. Its full weight is the common prefix weight times the inherited completion weight. Cancellation in conditional probabilities proves the ratio. Completed prefixes retain the avoidance indicator.',
        ['Finite graph, fixed length n, positive inherited weights, C_n(G;a)>0','Free endpoint; no prescribed chordal terminal point','Only realized prefixes are divided by; forbidden vertices exclude the start']),
      entry('maximal-collar','self-avoiding-collar-maximal-avoidance-martingale-bound','lemma','Static collar deficit controls every exploration time',
        'DRAFT, mathematical review pending. Let P be a finite probability law on simple paths and F_k the prefix filtration, with completed paths retained and a finite deterministic horizon N. For nested forbidden sets A subset B let E_A,E_B be full-path avoidance events, so E_B subset E_A, and r(A)=P(E_A), r(B)=P(E_B). Put M_k^A=P(E_A|F_k), M_k^B=P(E_B|F_k). For every lambda>0, P(max_(0<=k<=N)(M_k^A-M_k^B)>=lambda)<=min(1,(r(A)-r(B))/lambda). This applies to exact fixed-length SAW kernels and to all-length finite endpoint-constrained SAW laws; no independence or path-length loss is required.',
        'D_k=M_k^A-M_k^B is the nonnegative martingale E[1_(E_A minus E_B)|F_k]. Stop at its first lambda crossing, or at N if none occurs. Finite optional stopping gives E D_tau=D_0=r(A)-r(B). Since D_tau is at least lambda on the crossing event and nonnegative elsewhere, lambda times that probability is at most D_0. The equal-weight two-path diamond attains equality for lambda=1.',
        ['Nested full-path avoidance events','Finite prefix horizon retaining terminal information','Conditional probabilities under one common path law']),
      entry('conditioning-cost','nested-self-avoiding-avoidance-total-variation-cost','lemma','Exact total variation cost of a thicker obstacle',
        'DRAFT, mathematical review pending. In any probability space, let E_B subset E_A have 0<P(E_B)<=P(E_A). With total variation defined as sup_C |P(C)-Q(C)|, TV(P(.|E_A),P(.|E_B))=1-P(E_B)/P(E_A). After any common measurable projection, including a stopped-prefix projection of a self-avoiding path, the corresponding total variation is at most this value.',
        'Writing p=P(E_B)/P(E_A), the law conditioned on E_A is p times the law conditioned on E_B plus complementary weight on E_A minus E_B. The components have disjoint support, so testing E_B attains 1-p and the mixture bounds all events by 1-p. For p=1 the laws coincide. Measurable projection contracts total variation.',
        ['Nested measurable events of positive probability','One common underlying probability law','Total variation convention is supremum over events']),
      entry('weak-conditioning','collar-stable-compact-trace-conditional-weak-convergence','lemma','Collar ratios justify conditioning a weak trace limit',
        'DRAFT, mathematical review pending. Let K_n be nonempty compact random sets in a fixed compact metric space, converging in distribution for Hausdorff distance to K. For nonempty closed A set d_n=dist(K_n,A). Suppose P(d_n>0)->r>0 and P(d_n>epsilon_j)->r_j for epsilon_j decreasing to zero, with r_j->r. Then P(K avoids A)=r and the conditional law of K_n given avoidance converges weakly to K conditioned on avoidance. Literal geometric neighborhood avoidance is required by these distance events; any substitute smooth collars need matching neighborhood inclusions.',
        'Continuity of distance and Portmanteau give P(d>0)<=r and r_j<=P(d>=epsilon_j)<=P(d>0); sending j to infinity proves equality. On a Skorohod coupling, d_n converges to d and false negatives of avoidance vanish. Equality of the limiting avoidance probabilities makes false positives vanish too. The indicators converge in L1, so their products with bounded continuous test functions converge, yielding conditional weak convergence after division by r.',
        ['Hausdorff weak convergence in a compact trace space','Nonempty closed obstacle and positive avoidance limit','Shrinking-neighborhood ratio limits agree with the uncollared limit','No ordered-curve tightness claim follows from this trace lemma']),
      entry('dependent-avoidance','self-avoiding-avoidance-events-diamond-counterexample','lemma','Avoidance marginals cannot be multiplied without justification',
        'DRAFT, mathematical review pending. In the graph whose only a-to-b simple paths are (a,c,b) and (a,d,b), assign each edge weight one and normalize the two path weights. Then P(avoid c)=P(avoid d)=1/2, while P(avoid both c and d)=0. Thus two avoidance marginals for the same path are not independent and their product 1/4 gives the wrong intersection probability.',
        'Each of the two equally likely paths hits exactly one of c,d. The marginals each count one path; their intersection counts none.',
        ['Exactly the two diamond paths, with equal inherited edge weights','Both events concern the same sampled path']),
      entry('catalog-scope','honeycomb-saw-fixed-length-versus-chordal-ensemble-gap','concept','P0003 requires its fixed-length ensemble to be preserved',
        'DRAFT source-scope correction. Grimmett, Selected problems in probability theory, arXiv:2205.07318 Question 2.2, asks about uniform n-step honeycomb SAW starting at the origin and suitable rescaling as n tends to infinity. The question does not specify all continuum normalization and stopping conventions. The critical all-length boundary-to-boundary ensemble in Bauerschmidt-Duminil-Copin-Goodman-Slade, arXiv:1206.2092 Conjecture 1.5 and Section 3.3, is related but has a different endpoint and length law. A proof in that chordal ensemble is not a proof of the fixed-length catalog target without an explicit transfer theorem. Present openness is UNKNOWN in this packet.',
        None,['The two primary formulations have been checked','No fixed-length/all-length transfer theorem or current-resolution certification was obtained']),
      entry('disk-gap','fixed-length-honeycomb-saw-shrinking-disk-collar-bound-conjecture','concept','H_disk: the unproved positive collar-count estimate',
        'DRAFT CONJECTURE, not proved. Fix a closed disk A of radius r about z with |z|>r and B_epsilon the concentric disk of radius (1+epsilon)r, still excluding zero. In the graph-distance-n honeycomb ball G_n, scale coordinates by n^(-3/4) and delete edges whose segments intersect A or B_epsilon, respectively. C_n denotes exact n-edge simple-path count from zero with free endpoint; c_n(H)=C_n(G_n;0). The missing estimate asks for alpha>0 and finite C(z,r) such that limsup_n [C_n(G_n minus A;0)-C_n(G_n minus B_epsilon;0)]/c_n(H)<=C(z,r) epsilon^alpha for sufficiently small epsilon. The spatial normalization is an operational conjectural choice. The maximal martingale bound would transfer this static estimate to all prefixes, but no such estimate is proved here; closing it would not alone prove the SLE scaling limit.',
        None,['Uniform fixed-length honeycomb model, free endpoint','Geometric forbidden edges and inherited lattice','Chosen spatial normalization n^(-3/4), not certified by the source question','Positive alpha and uniform collar estimate remain unproved'])
    ]
    relations=[
      {'from_key':'maximal-collar','to_key':'length-kernel','kind':'semantic_association','rationale':'The exact remaining-length kernel gives the concrete conditional avoidance probabilities to which the maximal bound applies in fixed-length SAW.'},
      {'from_key':'conditioning-cost','to_key':'maximal-collar','kind':'analogous_to','rationale':'Both bounds control obstacle thickening using the same initial nested-event probability deficit.'},
      {'from_key':'weak-conditioning','to_key':'maximal-collar','kind':'analogous_to','rationale':'Both use a vanishing static collar deficit to justify a uniform or limiting avoidance operation; neither supplies that deficit.'},
      {'from_key':'dependent-avoidance','to_key':'maximal-collar','kind':'semantic_association','rationale':'The same-path dependence seen on the diamond is handled by conditional expectation in the maximal bound.'},
      {'from_key':'catalog-scope','to_key':'length-kernel','kind':'semantic_association','rationale':'The fixed-length catalog ensemble requires the remaining-length parameter in its continuation kernel.'},
      {'from_key':'disk-gap','to_key':'length-kernel','kind':'depends_on','rationale':'The conjectured count ratio is defined for exact-length kernels, not for an all-length sum.'},
      {'from_key':'disk-gap','to_key':'maximal-collar','kind':'semantic_association','rationale':'Supplying the static conjectured bound would give maximal-prefix error at most C epsilon^alpha/lambda by the proved conditional inequality.'}
    ]
    bundle={'spec':'mathbrain-draft-v1','author_agent':'w396','bundle_slug':'probability-saw-fixed-length-collar-control-w396-001','entries':entries,'relations':relations}
    keys={x['key'] for x in entries}
    errors=[]
    allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
    for e in entries:
        if not re.fullmatch('[a-z][a-z0-9]*(?:[.][a-z][a-z0-9]*)*',e['namespace']):errors.append('namespace: '+e['key'])
        if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name']):errors.append('logical name: '+e['key'])
        if e['kind'] in {'lemma','theorem'} and not e['proof_text']:errors.append('missing proof: '+e['key'])
        if e['kind'] in {'concept','definition'} and e['proof_text'] is not None:errors.append('unexpected proof: '+e['key'])
        if not e['source']['license'].startswith('owner-own-work'):errors.append('license: '+e['key'])
    for r in relations:
        if r['from_key'] not in keys or r['to_key'] not in keys or r['kind'] not in allowed:errors.append('relation')
    if len(keys)!=len(entries):errors.append('duplicate key')
    if errors:raise ValueError(errors)
    filename='bundle_001.json'
    for i in range(1,1000):
        candidate=f'bundle_{i:03d}.json'
        if not (INBOX/candidate).exists() and not (INBOX/candidate).with_suffix('.part').exists():filename=candidate;break
    draft=ROOT/'drafts'/filename
    draft.parent.mkdir(parents=True,exist_ok=True)
    draft.write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    target=INBOX/filename
    put('SUBMISSION_PLAN.json',{'prepared_local':str(draft),'target':str(target),'resource':'file:'+target.as_posix(),'submitted':False})
    diff=''.join(difflib.unified_diff([],draft.read_text(encoding='utf-8').splitlines(True),fromfile='a/'+target.as_posix(),tofile='b/'+target.as_posix()))
    (ROOT/'patches').mkdir(exist_ok=True)
    (ROOT/'patches/01_saw_collar_draft.diff').write_text(diff,encoding='utf-8')
    baseline={'store_path':'~/math-brain-build/local/population/brain.sqlite3','mode':'read_only','scope':'Only the seven proposed logical identifiers; no export or benchmark data','matched_proposed_logicals':None}
    try:
        uri='file:'+baseline['store_path']+'?mode=ro'
        with sqlite3.connect(uri,uri=True,timeout=3) as conn:
            names={r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','cards','claims')")}
            for table in ['nodes','cards','claims']:
                if table not in names:continue
                columns={r[1] for r in conn.execute('PRAGMA table_info('+table+')')}
                column=next((c for c in ['logical_id','logical_name'] if c in columns),None)
                if column is None:continue
                values=[('math:'+NS+':'+e['logical_name']) if column=='logical_id' else e['logical_name'] for e in entries]
                hits=list(conn.execute('SELECT '+column+' FROM '+table+' WHERE '+column+' IN ('+','.join('?' for _ in values)+')',values))
                baseline.update({'table':table,'column':column,'matched_proposed_logicals':len(hits),'matches':[r[0] for r in hits]});break
    except (OSError,sqlite3.Error) as e:baseline['error']=str(e)
    finite=json.loads((ROOT/'FINITE_CHECKS.json').read_text(encoding='utf-8')) if (ROOT/'FINITE_CHECKS.json').exists() else {'status':'NOT_RUN','assertions':0}
    measures={'command':'python -B -X utf8 ~/brain_workers/w396/finalize_packet.py prepare','bundle_schema_validation':'PASS_LOCAL_SHAPE_ONLY','draft_entries':len(entries),'draft_lemmas':sum(e['kind']=='lemma' for e in entries),'draft_concepts':sum(e['kind']=='concept' for e in entries),'same_bundle_relations':len(relations),'invalid_relation_ends':0,'canonical_read_only_baseline':baseline,'numerical_regression':finite,'live_changes_applied':0,'reviewed_claims':0,'ingested_claims':0,'retrieval_effect_measured':False,'no_proof_or_performance_claim_follows_from_schema_check':True}
    put('measurements.json',measures)
    status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    status.update({'target_source':'Grimmett, arXiv:2205.07318v1, Question 2.2, printed p.3','target_conventions':{'source':'uniform n-step walks from honeycomb origin, free endpoint; suitable rescaling; source does not fully specify continuum normalization/stopping/topology','related_route':'critical all-length boundary-to-boundary ensemble; no transfer theorem proved','working_scale':'n^(-3/4) for H_disk, expressly conjectural'},'hardest_gap':'H_disk: the explicitly stated fixed-length positive disk-collar count estimate','additional_unproved_prerequisites':['length-resolved conformal identification H_len','ordered-curve tightness','scale/continuum stopping convention','interior simplicity/Loewner regularity','all-length/fixed-length transfer if the chordal route is used','H_5/8 for the related chordal route']})
    if not any(s['id']=='grimmett-original-target' for s in status['sources']):
        status['sources'].insert(0,{'id':'grimmett-original-target','url':'https://arxiv.org/abs/2205.07318','revision':'v1, 2022-05-15','locator':'Question 2.2, printed p.3','quote':'when suitably rescaled','supports':'Original uniform fixed-length origin/free-endpoint catalog target','source_verified':True,'mathematical_proof_of_target':False})
    put('SOURCE_STATUS.json',status)
    claims=[json.loads(s) for s in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
    extra=[
      {'id':'w396-S1.8','target':'P0003','status':'proved special case','statement':entries[0]['statement'],'assumptions':entries[0]['assumptions'],'source':entries[0]['source'],'proof_or_counterexample':entries[0]['proof_text'],'independent_reviewer':'w398; pending','remaining_gap':'H_disk and length-resolved conformal identification remain unproved.','review_state':'not_submitted','formal_check':False},
      {'id':'w396-S1.9','target':'P0003','status':'conjecture','statement':entries[-1]['statement'],'assumptions':entries[-1]['assumptions'],'source':entries[-1]['source'],'proof_or_counterexample':'ATTEMPT.md gives the exact first-entrance upper bound (U), but no useful asymptotic estimate of its mutually avoiding prefix/suffix terms.','independent_reviewer':'w398; pending','remaining_gap':'H_disk itself; resolving it alone does not solve the catalog target.','review_state':'not_submitted','formal_check':False},
      {'id':'w396-S1.10','target':'P0003','status':'proved special case','statement':'For nested forbidden edge sets A subset B and n-edge simple paths from 0 with free endpoint in a finite graph, the number avoiding A and entering B is at most the sum over k=0,...,n-1 and oriented edges (v,w) in B minus A of c_k^(G minus B)(0,v) C_(n-k-1)^(G minus A)(w). With positive inherited edge weights include the edge factor q_(v,w).','assumptions':['Finite graph, exact length n, inherited weights','Prefix c_k has prescribed endpoint v; suffix C_m has free endpoint','C_0=1 for retained vertices'],'source':{'source_id':'owner:w396:P0003:first-collar-entrance','url':'owner://primary-directive/P0003/w396/ATTEMPT.md#U','revision':'draft-2026-10-10','license':'owner-own-work'},'proof_or_counterexample':'Split each path at its unique first B edge. The prefix avoids B and the suffix avoids A. Dropping mutual avoidance injects this family into the counted prefix-edge-suffix products.','independent_reviewer':'w398; pending','remaining_gap':'Product bound loses mutual avoidance and may be too large to prove H_disk.','review_state':'not_submitted','formal_check':False}
    ]
    existing={c['id'] for c in claims}
    with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as f:
        for c in extra:
            if c['id'] not in existing:f.write(json.dumps(c,ensure_ascii=False)+'\n')
    (ROOT/'review_packet').mkdir(exist_ok=True)
    (ROOT/'review_packet/REVIEW.md').write_text('P0003 draft for w398, 2026-10-10. Full target not proved; no independent KEEP received.\n\nRead ATTEMPT.md and SOURCE_ADDENDUM.md first. Audit L0\u0027 (remaining length), L1 (finite optional stopping including terminal prefixes), L2 (TV convention), L3 (closed obstacle and collar-limit hypotheses), and first-entrance counting inequality (U). Check that no ensemble equivalence, conformal exponent, tightness, or open-status assertion is smuggled in.\n\nCLAIMS.jsonl records exact statements, assumptions, proof/counterexample, assigned reviewer and gap. SOURCE_STATUS.json records primary provenance separately. The initial STATEMENT_FOR_ADVERSARY.md is preserved; its initial ensemble identification is corrected explicitly in SOURCE_ADDENDUM.md. w397 received it before the proof (msg-168e5faa4e).\n\nReproduction: python -B -X utf8 ~/brain_workers/w396/local_checks.py . Current check status: '+finite['status']+'; assertions run: '+str(finite.get('assertions',0))+'. A closed gate exits 3 and must never be labeled PASS. No formal proof assistant was run.\n\nDraft: '+str(draft)+' . Schema checks validate '+str(len(entries))+' entries and '+str(len(relations))+' relations, not mathematics. Source license is owner-own-work; proofs are original campaign writeups of elementary arguments, with no novelty claim. Any integration/retrieval must be separately recorded after mathematical review.\n\nMain attempted gap: H_disk. Additional full-target gaps: H_len, curve tightness and continuum conventions; the related chordal H_5/8 route and any ensemble transfer are unproved.\n\nNEXT: Return a mathematical KEEP/FIX/DROP verdict on L0\u0027, L1--L3 and (U); send your own new results to w401 for independent review.\n',encoding='utf-8')
    report='Saved a corrected P0003 proof attempt centered on one change: static obstacle-collar deficits control every SAW exploration prefix without a path-length factor. The argument retains the remaining length n-k for the actual uniform fixed-length catalog target. Three auxiliary proofs and explicit counterexamples expose the assumptions still needed. P0003 is not solved; H_disk remains the concrete attempted gap.\n\nMeasured by finalize_packet.py prepare: '+str(len(entries))+' locally valid draft cards, '+str(len(relations))+' valid relation ends, zero live changes or independently reviewed claims. Finite regression status is '+finite['status']+' with '+str(finite.get('assertions',0))+' assertions; the distress gate is respected. These are draft-output measurements, not a measured recall or mathematical-proof improvement. This remains a proposal pending review and deployment.\n\nThe original catalog source is Grimmett Q2.2. The initial chordal-ensemble identification was corrected after w397 supplied that source. Main risks are losing the remaining-length parameter, replacing geometric edge deletion by vertex-only deletion, and treating collar continuity, tightness or an ensemble-transfer theorem as proved.\n\nApply: the validating coordinator should mathematically audit ATTEMPT.md, then integrate the explicitly submitted inbox draft with its normal integrator; no live code patch, direct store write or global recall change was made. The unified draft addition is patches/01_saw_collar_draft.diff.\n\nThe progress event and hook proposal are staged locally because the worker brief restricts writes to this folder, with its later explicit inbox and named-peer exceptions. No blind benchmark material was opened and pd_progress.py was not run.\n\nNEXT: Audit L0\u0027, L1--L3 and (U), then estimate mutually avoiding first-entrance prefix/suffix counts for H_disk.\n'
    (ROOT/'REPORT.md').write_text(report,encoding='utf-8')
    put('PROGRESS_OUTBOX.json',{'event':'w396 P0003: fixed-length maximal collar bound and conditional bridge saved; H_disk open; seven draft cards prepared; numerical checks gated','agent':'w396','row':'S1.2','evidence':str(ROOT/'ATTEMPT.md'),'state':'prepared_local_not_posted','reason':'worker write boundary; progress helper also references blind evaluation merge paths'})
    put('DRAFT_STATE.json',{'prepared':True,'submitted':False,'mathematical_review_received':False,'ingested':False,'retrievable':False,'draft_path':str(draft),'intended_inbox':str(target)})
    print(json.dumps(measures,ensure_ascii=False),flush=True)

def submit():
    plan=json.loads((ROOT/'SUBMISSION_PLAN.json').read_text(encoding='utf-8'))
    target=Path(plan['target']).resolve()
    if target.parent!=INBOX.resolve():raise ValueError('Inbox target outside authorized folder')
    mesh='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
    args=['python','-B','-X','utf8',mesh,'claim','--agent','w396','--resource',plan['resource'],'--mode','exclusive','--purpose','Submit corrected P0003 collar-control draft only','--ttl','1800']
    r=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30,creationflags=0x08000000 if os.name=='nt' else 0)
    receipt={'command':args,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
    put('INBOX_CLAIM_RECEIPT.json',receipt)
    if r.returncode!=0:
        print(json.dumps(receipt),flush=True);return r.returncode
    target.parent.mkdir(parents=True,exist_ok=True)
    part=target.with_suffix('.part')
    if target.exists() or part.exists():raise FileExistsError('Refusing to overwrite another draft or part')
    payload=Path(plan['prepared_local']).read_text(encoding='utf-8')
    with part.open('x',encoding='utf-8',newline='\n') as f:
        f.write(payload);f.flush();os.fsync(f.fileno())
    part.rename(target)
    plan['submitted']=True;put('SUBMISSION_PLAN.json',plan)
    state=json.loads((ROOT/'DRAFT_STATE.json').read_text(encoding='utf-8'))
    state.update({'submitted':True,'submitted_unix':time.time(),'submitted_path':str(target)})
    put('DRAFT_STATE.json',state)
    src=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'));src['submitted']=True;put('SOURCE_STATUS.json',src)
    print(json.dumps(state),flush=True)
    return 0

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'prepare'
    if mode=='prepare':prepare()
    elif mode=='submit':raise SystemExit(submit())
    else:raise SystemExit('Expected prepare or submit')
