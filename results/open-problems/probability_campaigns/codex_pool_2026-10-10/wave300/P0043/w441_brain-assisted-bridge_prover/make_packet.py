"""Create reviewable mathematics and DRAFT data; no live store operations."""
from pathlib import Path
import difflib, json, math, re, sys

ROOT=Path(__file__).resolve().parent
INBOX=Path(r'~\math-brain-inbox\w441')

def write_json(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    attempt=(ROOT/'ATTEMPT.md').read_text(encoding='utf-8')
    attempt=attempt.replace('\n## The single hardest remaining gap\n','\n',1)
    anchor='Prove a mechanism specific to independent Bernoulli critical clusters'
    if '\n## The single hardest remaining gap\n' not in attempt:
        attempt=attempt.replace(anchor,'## The single hardest remaining gap\n\n'+anchor,1)
    marker='NEXT: Compare the returned brain theorem'
    if 'Independent adversary closure' not in attempt:
        pos=attempt.index(marker)
        attempt=attempt[:pos]+('Independent adversary closure: w442/ATTEMPT.md, lines 25-37, proves that every infinite subgraph of bounded-degree subexponential G has zero asymptotic anchored expansion. In particular h(C,o)=0. Therefore L004 cannot cover any subexponential ambient graph, even above criticality. This route is CLOSED. The valid L006 bound is retained as a necessary condition on general bounded-degree clusters; it is not a proof of critical absence. See ADVERSARY_RESPONSE.md.\n\n')+attempt[pos:]
    attempt=re.sub(r'NEXT: Compare the returned brain theorem[^\n]*','NEXT: w443 checks L002-L006 and w442 C003; a future proof step must handle zero anchored expansion directly, with one fixed thinning parameter and justified conditional probabilities.',attempt)
    (ROOT/'ATTEMPT.md').write_text(attempt,encoding='utf-8')

    original=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    def proof_section(label):
        headings=list(re.finditer(r'^## .*$',attempt,re.M))
        for i,m in enumerate(headings):
            if label in m.group(0):
                end=headings[i+1].start() if i+1<len(headings) else len(attempt)
                text=attempt[m.end():end].strip()
                if label=='L004':text=text.split('Corollary L004b:')[0].strip()
                return text
        raise ValueError('missing proof '+label)

    details=[
      ('L002','bernoulli-cluster-thinning-threshold-bound','Quenched threshold of a sampled Bernoulli cluster',
       'Let G be a countable undirected graph, p_c(G)=inf{r:P_r(some infinite open component exists)>0}, and p in (0,1]. Almost surely every infinite open component C in independent Bernoulli-p bond percolation satisfies p_c(C)>=min{1,p_c(G)/p}. In particular, when p=p_c(G)>0, every such component has p_c(C)=1.',
       ['G is countable and undirected','Independent Bernoulli bond percolation','p in (0,1]','The auxiliary q-thinning bits are independent of the entire p-configuration']),
      ('L003','bounded-corridor-branching-forces-exponential-growth','Bounded injective branching forces exponential volume',
       'Let b>=2 and L>=1 be integers. If the rooted b-ary tree has an injective vertex map into a locally finite graph G with each parent-child image pair at distance at most L, then liminf_{r->infinity}|B_G(f(root),r)|^(1/r)>=b^(1/L)>1. Hence such a map cannot exist in a graph of subexponential volume growth.',
       ['b and L are integers with b>=2 and L>=1','G is locally finite','The vertex map is injective','Every parent-child distance is at most the same L']),
      ('L004','anchored-expansion-peierls-survival-bound','Explicit survival from positive anchored edge expansion',
       'Let C be an infinite connected countable graph of maximum degree Delta>=2, o a vertex, and h=inf{|boundary_E K|/|K|:K finite connected and o in K}>0. Under independent Bernoulli-q bond percolation, if a=(1-q)^h<1/(Delta^2+1), then P_q^C(o belongs to an infinite open cluster)>=1-a/(1-Delta^2*a)>0. Consequently p_c(C)<=1-(Delta^2+1)^(-1/h).',
       ['C is infinite connected and countable','Maximum degree of C is at most the integer Delta>=2','h is the stated infimum over all finite connected sets containing o and is strictly positive','The q-bits are independent','a=(1-q)^h<1/(Delta^2+1)']),
      ('L005','exponential-decorated-ray-with-percolation-threshold-one','Exponential growth alone permits threshold one',
       'There is an infinite connected graph H of maximum degree 3 with liminf_r|B_H(s_0,r)|^(1/r)>=sqrt(2)>1 and p_c(H)=1: attach a full finite binary tree of depth n by one edge to the nth vertex of a spine ray. It has infinitely many vertex orbits. Thus exponential volume growth and bounded degree alone do not imply p_c<1; quasi-transitivity cannot be dropped from that implication.',
       ['H is the explicitly defined spine with finite binary grafts','Independent Bernoulli bond percolation on H','Each graft has finite depth n']),
      ('L006','near-critical-cluster-anchored-expansion-logarithmic-bound','Near-critical quenched bound on anchored expansion',
       'Let G be a countable undirected graph of maximum degree Delta>=2 with 0<p_c(G)<1. For each fixed p in (p_c(G),1], almost surely every infinite Bernoulli-p open component C and every o in C satisfy h(C,o)<=log(Delta^2+1)/log(p/(p-p_c(G))), where h(C,o)=inf{|boundary_E K|/|K|:K finite connected in C and o in K}. At p=p_c(G), almost surely all such h(C,o) equal zero. No simultaneity for uncountably many p is asserted.',
       ['G is countable and undirected','Maximum degree of G is at most the integer Delta>=2','0<p_c(G)<1','Independent Bernoulli bond percolation','p is fixed before the almost-sure statement'])
    ]
    existing={row['claim_id'] for row in original}
    claims=[]
    for label,name,title,statement,assumptions in details:
        row={'claim_id':'w441-'+label,'target':'P0043','statement':statement,'assumptions':assumptions,'source':{'type':'owner-own-work','artifact':'ATTEMPT.md','section':label,'novelty_claim':False},'proof':proof_section(label),'independent_reviewer':{'requested':'w443','status':'pending','w442_reported_verdict':'KEEP' if label in ('L002','L003','L004','L005') else 'not yet received','receipt':'TEAM receipt reported 05:28; PEER_AUDIT.md was not re-audited'},'remaining_gap':'No gap is claimed in this elementary written deduction; w443 review pending. The full target still needs a Bernoulli-specific argument for zero-anchored-expansion clusters.','status':'proved special case'}
        if row['claim_id'] not in existing:
            with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as stream:stream.write(json.dumps(row,ensure_ascii=False)+'\n')
        claims.append((label,name,title,row))
    first=next(row for row in original if row['claim_id']=='w441-L001')
    nodes=[]
    def node(key,name,title,statement,assumptions,proof,kind='lemma'):
        return {'key':key,'namespace':'probability.percolation.critical','logical_name':name,'kind':kind,'title':title,'statement':statement,'proof_text':proof,'assumptions':assumptions,'domain':'probability theory','source':{'source_id':'owner:w441:P0043:2026-10-10:'+key,'url':(ROOT/'ATTEMPT.md').as_uri() if key!='critical-boundary' else (ROOT/'CLAIMS.jsonl').as_uri(),'revision':'draft-as-written-2026-10-10','license':'owner-own-work (campaign derivation; independent review pending)','excerpt':None}}
    nodes.append(node('critical-boundary','critical-percolation-needs-threshold-below-one','Why the critical conjecture excludes p_c=1',first['statement'],first['assumptions'],first['proof']))
    labels={}
    for label,name,title,row in claims:
        key=name
        labels[label]=key
        nodes.append(node(key,name,title,row['statement'],row['assumptions'],row['proof']))
    nodes.append(node('growth-only-route','candidate-growth-only-thinning-route','Candidate growth-only transfer (refuted)',
        'REFUTED CANDIDATE, not an accepted theorem: the proposed implication that every infinite connected bounded-degree graph of exponential volume growth has p_c<1. The decorated-ray counterexample disproves this implication. Checking the symmetry hypothesis on the ambient graph does not establish it for a random open cluster.',[],None,'concept'))
    nodes.append(node('bounded-branching-route','candidate-bounded-branching-subexponential-route','Candidate bounded branching in subexponential graphs (refuted)',
        'REFUTED CANDIDATE, not an accepted theorem: the proposed construction of an injective b-ary tree with b>=2 and uniformly bounded parent-child graph distances inside a subexponential ambient graph. The branching-volume bound rules out this construction before any percolation probabilities are considered.',[],None,'concept'))
    relations=[
        {'from_key':labels['L006'],'to_key':labels['L002'],'kind':'depends_on','rationale':'The near-critical expansion bound uses the quenched lower bound on p_c(C).'},
        {'from_key':labels['L006'],'to_key':labels['L004'],'kind':'depends_on','rationale':'The near-critical expansion bound combines the quenched lower threshold with this explicit Peierls upper threshold.'},
        {'from_key':labels['L005'],'to_key':'growth-only-route','kind':'refutes','rationale':'The decorated ray has exponential growth and degree 3 but p_c=1, contradicting the proposed growth-only implication.'},
        {'from_key':labels['L003'],'to_key':'bounded-branching-route','kind':'refutes','rationale':'The proposed injective bounded-distance branching network would force exponential ambient growth.'},
        {'from_key':labels['L002'],'to_existing_logical':'math:probability.core:attempt-p0043-absence-of-infinite-clusters-at-critical-percolation','kind':'semantic_association','rationale':'Both concern the P0043 independence obstruction. Fresh thinning is conditionally independent on a fixed sampled graph; the existing regular-tree recursion needs independent forward branches and does not establish the general target.'}
    ]
    bundle={'spec':'mathbrain-draft-v1','author_agent':'w441','bundle_slug':'critical-percolation-thinning-bridge-001','review_status':'DRAFT: w443 pending; do not promote to independently checked proof','entries':nodes,'relations':relations}
    folder=ROOT/'drafts';folder.mkdir(exist_ok=True)
    write_json(folder/'bundle_001.json',bundle)
    by_key={n['key']:n for n in nodes}
    prior=json.loads((ROOT/'BRAIN_THEOREM_RETRIEVAL.json').read_text(encoding='utf-8'))
    old=next(row for row in prior['rows'] if 'Attempt on Absence of infinite clusters' in row['title'])
    edge_rows=[]
    for relation in relations:
        source=by_key[relation['from_key']]
        target=by_key[relation['to_key']]['statement'] if 'to_key' in relation else old['body']
        edge_rows.append({'relation':relation,'from_statement_quote':source['statement'],'to_statement_quote':target,'evidence':'ATTEMPT.md '+source['logical_name'],'status':'draft; independent review pending'})
    (ROOT/'EDGES.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in edge_rows),encoding='utf-8')
    source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    source['owner_solved_retired_check']={'readme':'Big Open problem in probability theory/README.md names the distinct nonuniqueness target p_c<p_2to2; it is not a proof of this critical-absence target.','solved_register':'Targeted percolation/P0043/criticality search in the cited Open problem project/solved_register.md had no matches; no exhaustive solved-status claim.','named_H_I_attempts':'Exact P0043/G0001/H0016 search did not locate a matching proof in the named H/I attempt folders. The existing math-store P0043 attempt was retrieved and digested instead.'}
    source['intake_alias_caution']={'H0016':'Not admitted, not attempted; site-lattice statement listed duplicate_of G0001/P0043.','G0001':'Distinct site-percolation finite-cluster-tail conjecture at all p in (0,1), not the exact quasi-transitive bond critical-absence target. Do not treat that shorthand alias as a statement-fidelity check.'}
    source['remaining_source_check']='No required source lookup remains for this packet. Mathematical verification of the recent whole proof remains outside the claimed result.'
    write_json(ROOT/'SOURCE_STATUS.json',source)
    review={'w442':{'statement_message':'msg-ad5f36607f','independent_work_preceded_route_message':True,'route_message':'msg-58e792a07e','reported_keep':['L002','L003','L004','L005'],'peer_audit_path':'~/brain_workers/w442/PEER_AUDIT.md','own_new_result_to_referee':'C003 in w442/ATTEMPT.md; zero anchored expansion in subexponential ambient graphs'},'w443':{'status':'complete packet ready; delivery pending'},'full_target':{'status':'unproved in this packet','recent_primary_full_proof':'claimed in source; independently unverified here'}}
    write_json(ROOT/'REVIEW_STATE.json',review)
    recall=json.loads((ROOT/'REPORT_RECALL.json').read_text(encoding='utf-8'))
    checks=json.loads((ROOT/'MATH_CHECKS.json').read_text(encoding='utf-8'))
    guard=json.loads((ROOT/'GUARD_CHECKS.json').read_text(encoding='utf-8'))
    rate=[{'p':p,'pc':.5,'Delta':3,'h_upper_bound':math.log(10)/math.log(p/(p-.5))} for p in (.51,.5001,.500001)]
    measurement={'general_recall_timeout_seconds':recall['timeout_seconds'],'general_recall_elapsed_seconds':recall['elapsed_seconds'],'general_recall_output_characters':len(recall['stdout']),'math_store_targeted_query_seconds':prior['query_seconds'],'math_check_seconds':checks['elapsed_seconds'],'exact_joint_configurations':checks['exact_joint_configurations'],'connected_set_bounds':len(checks['connected_set_bounds']),'decorated_ray_vertices':checks['decorated_ray']['vertices'],'guard_fixture_before':guard['before'],'guard_fixture_after':guard['after'],'guard_fixture_scope':guard['scope'],'rate_examples':rate,'commands':['python -X utf8 probe.py recall','python -X utf8 store_probe.py retrieve','python -X utf8 validate_math.py','python -X utf8 validate_guard.py']}
    write_json(ROOT/'MEASUREMENTS.json',measurement)
    hook={'id':'critical-hypotheses-w441-01','area':'math','event':'stage-start','cue':'Applying a percolation growth or anchored-expansion theorem when a required graph hypothesis is false or unknown','fire_when':'An exponential-growth criticality theorem is applied to the decorated ray without quasi-transitivity, or positive anchored expansion is asserted inside subexponential bounded-degree G.','silent_when':'The regular degree-3 tree is supplied with verified quasi-transitivity/exponential growth, or the Peierls lemma is explicitly restricted to h>0.','text':'Check the theorem on the graph it actually uses. Open clusters need not inherit quasi-transitivity. Positive anchored expansion is impossible inside bounded-degree subexponential G. A failed sufficient-condition route does not prove the target.','evidence':'w441/MATH_CHECKS.json: 4094-vertex degree-3 growth witness; GUARD_CHECKS.json: 3 invalid uses reduced to 0 on local fixture; w442/ATTEMPT.md: C003; memory scar perceptron_proof_open_gaps_fleet_2026_07_12','proposer':'w441'}
    assert len(hook['text'])<=300
    hooks=ROOT/'hooks';hooks.mkdir(exist_ok=True)
    line=json.dumps(hook,ensure_ascii=False)+'\n'
    (hooks/'math-w441.jsonl').write_text(line,encoding='utf-8')
    patches=ROOT/'patches';patches.mkdir(exist_ok=True)
    helper=(ROOT/'hypothesis_guard.py').read_text(encoding='utf-8')
    (patches/'01_hypothesis_guard.diff').write_text(''.join(difflib.unified_diff([],helper.splitlines(keepends=True),fromfile='a/~/math-brain-build/src/math_brain/proof_hypothesis_guard.py',tofile='b/~/math-brain-build/src/math_brain/proof_hypothesis_guard.py')),encoding='utf-8')
    (patches/'02_math_hook.diff').write_text(''.join(difflib.unified_diff([],line.splitlines(keepends=True),fromfile='a/~/primary_directive/hooks1000/proposals/math-w441.jsonl',tofile='b/~/primary_directive/hooks1000/proposals/math-w441.jsonl')),encoding='utf-8')
    submitted='--submit' in sys.argv
    if submitted:
        INBOX.mkdir(parents=True,exist_ok=True)
        final=INBOX/'bundle_001.json'
        content=(folder/'bundle_001.json').read_text(encoding='utf-8')
        if final.exists():
            if final.read_text(encoding='utf-8')!=content:raise FileExistsError('Refuse to replace an already submitted different bundle')
        else:
            part=INBOX/'bundle_001.part';part.write_text(content,encoding='utf-8');part.rename(final)
    write_json(ROOT/'BUNDLE_STATE.json',{'prepared':True,'submitted':submitted,'submission_path':str(INBOX/'bundle_001.json') if submitted else None,'narrow_claim':'clm-3865f63e1d','reviewed':'w442 reported KEEP L002-L005; w443 pending; remaining entries pending','ingested':'not observed','retrievable':'not observed','cryptographic_manifests_computed':False})
    print(json.dumps({'claims':len(original)+sum(row['claim_id'] not in existing for _,_,_,row in claims),'draft_entries':len(nodes),'exact_edges':len(relations),'submitted':submitted,'rate_examples':rate},indent=2))

if __name__=='__main__':main()
