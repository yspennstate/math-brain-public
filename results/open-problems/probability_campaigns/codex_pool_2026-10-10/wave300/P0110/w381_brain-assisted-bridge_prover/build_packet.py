"""Build local DRAFT artifacts and append claims; never integrates a live store."""
import difflib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
attempt=(root/'ATTEMPT.md').read_text(encoding='utf-8')

def proof(section):
    text=attempt.split('## '+section+':',1)[1]
    return text.split('\n## ',1)[0].strip()

def entry(key,kind,title,statement,assumptions,proof_text=None):
    return {'key':key,'namespace':'probability.first-passage-percolation',
      'logical_name':'p0110-w381-'+key,'kind':kind,'title':title,
      'statement':statement,'proof_text':proof_text,'assumptions':assumptions,
      'domain':'probability / undirected first-passage percolation',
      'source':{'source_id':'owner-p0110-w381-20261010:'+key,
        'url':'urn:owner-own-work:p0110:w381:20261010:'+key,
        'revision':'draft-20261010-independently-unchecked',
        'license':'owner-own-work (campaign deductions; independent review pending)', 'excerpt':None}}

entries=[
entry('terminal-bias-detour','lemma','Terminal-only mean bias controls a geodesic norm detour',
 'Let T be an integrable, translation-invariant undirected lattice FPP metric, h(x)=E T(0,x), and g a norm with g(x)=lim_m h(mx)/m on lattice x. Write b(x)=h(x)-g(x) and X(x,y)=T(x,y)-h(y-x). Then b(x)>=0. If z lies on any attained minimizing path from 0 to v, then g(z)+g(v-z)-g(v)=b(v)-b(z)-b(v-z)+X(0,v)-X(0,z)-X(z,v) <= b(v)+X(0,v)-X(0,z)-X(z,v). In particular, if the three centered errors have magnitude at most s, the detour is at most b(v)+3s. No upper bound on the two interior mean biases is required.',
 ['Finite mean passage times','Translation invariance of the edge law','A limiting norm g with the stated expectation limit','An attained minimizing path contains z'],proof('L1')+'\n\n'+proof('L2')),
entry('euclidean-segment-detour','lemma','Euclidean detour inequality measures distance to a segment',
 'For any d>=1, v in R^d with v!=0, and z in R^d, put L=|v|, S=|z|+|v-z| and r=dist(z,[0,v]) in Euclidean norm. Then S-L>=2r^2/S. The inequality includes projections of z beyond either endpoint.',
 ['Euclidean norm','v is nonzero'],proof('L3')),
entry('support-sphere-rounding','lemma','A norm has a lower sphere-contact direction, with bounded lattice-rounding defect',
 'Let g be a norm on R^d with g(x)<=b||x||_1, b>0. Let rho=min_{|u|=1}g(u)>0 and choose a minimizing unit u. Then g(x)>=rho|x| for all x and g(u)=rho. For integer n>=sqrt(d), round coordinates of nu to obtain v_n in Z^d. If delta=sqrt(d)/2 and K0=bd/2+rho delta, then v_n!=0, |v_n-nu|<=delta, and 0<=g(v_n)-rho|v_n|<=K0. This supplies a lower detour direction and no upper-curvature assertion.',
 ['A positive norm g on a finite-dimensional real vector space','g(x)<=b||x||_1','Coordinatewise nearest-integer rounding'],
 'Compactness of the Euclidean unit sphere gives u and rho. Homogeneity gives g(x)>=rho|x|. Coordinate rounding has Euclidean error <=sqrt(d)/2 and l1 error <=d/2. Thus g(v_n)<=rho n+bd/2 and |v_n|>=n-sqrt(d)/2, giving the upper defect bound. The lower defect bound follows from the global norm bound.'),
entry('finite-scale-wandering-tail','lemma','Finite-scale wandering tail from centered concentration and terminal mean bias',
 'Consider iid edge FPP on Z^d, d>=2, with a<=tau_e<=b almost surely, 0<a<b<infinity. Let h(x)=E T(0,x), g its limiting norm, rho=min_{|u|=1}g(u), and u any minimizer. For integer n>=sqrt(d), round nu to v_n and put L_n=|v_n|, C=(b/a)sqrt(d), K0=bd/2+rho sqrt(d)/2, B_n=h(v_n)-g(v_n), Lambda_n={z in Z^d:||z||_1<=(b/a)||v_n||_1}, and A_n=2|Lambda_n|+1. Let D(0,v_n) be the maximum distance of all minimizing paths to the segment [0,v_n]. Suppose q>=0, alpha>0, K>=1 and E exp(alpha |T(0,w)-h(w)|/|w|^q)<=K for every nonzero lattice w. Then for s>=0, P(D(0,v_n)>sqrt(C L_n (B_n+K0+3s)/(2rho))) <= min(1,A_n K exp(-alpha s/(((C+1)L_n)^q))). If B_n<=H n^q log(2+n), choosing s=(((C+1)L_n)^q/alpha) log(A_n K n^p) gives probability <=n^(-p) and a threshold O(n^((1+q)/2)sqrt(log n)) for any fixed p>0. No independence of the centered passage times is used; this is an upper bound along one rounded direction and does not assert matched global exponents.',
 ['Iid undirected nearest-neighbor lattice FPP','Strictly positive bounded weights a<=tau_e<=b','The stated uniform centered exponential-moment input','For the final asymptotic consequence, the stated terminal mean-bias bound'],proof('L4')+'\n\n'+proof('L5')),
entry('centered-subadditive-shortcut','concept','Rejected generic shortcut from centered concentration to nonrandom error',
 'REJECTED INFERENCE: abstract subadditivity of h(n)=E T_n and a centered exponential concentration envelope alone do not imply h(n)-n lim_m h(m)/m=O(n^q log n) on that envelope scale. An FPP subadditive approximation theorem requires its additional stochastic and geometric hypotheses. This concept records a failed shortcut, not a theorem asserting the shortcut.',
 ['The rejected statement concerns arbitrary subadditive sequences, not a proved iid FPP representation']),
entry('subadditive-bias-countermodel','lemma','Deterministic subadditive countermodel has perfect centered concentration and large bias',
 'Fix 0<beta<1. Put h(0)=0, h(n)=n+n^beta for integers n>=1, and T_n=h(n) deterministically. Then h is subadditive, lim_m h(m)/m=1, and E exp(alpha |T_n-E T_n|/n^q)=1 for every n>=1, alpha>0 and q>=0. Nevertheless h(n)-n=n^beta is not O(n^q log n) for q<beta. This is a counterexample to a generic inference, not an iid lattice FPP law.',
 ['0<beta<1','Deterministic sequence rather than an FPP metric'],proof('L6')),
entry('lower-to-upper-curvature-shortcut','concept','Rejected reuse of a lower-curvature direction as an upper-curvature direction',
 'REJECTED INFERENCE: a norm satisfying a lower quadratic transverse bound at a supporting outer-sphere direction need not satisfy an upper quadratic transverse bound at that same direction. The direction in a lower-bound argument cannot be reused in an upper-bound argument without verifying the upper hypothesis.',
 ['This is a rejected implication about arbitrary norms']),
entry('lower-not-upper-curvature','lemma','The l1 norm separates lower from upper quadratic curvature',
 'For g(s,t)=|s|+|t| on R^2 and u=(1,0), u minimizes g on the Euclidean unit circle. For |t|<=1, g(u+(0,t))-g(u)=|t|>=t^2. There is no finite C such that g(u+(0,t))-g(u)<=C t^2 for every sufficiently small nonzero t, since the ratio is 1/|t|. This norm example makes no assertion about the limit shape of any particular iid FPP law.',
 ['The l1 norm on R^2'],proof('L7')),
entry('primary-curvature-hypothesis-check','concept','Primary-source clarification for the conditional KPZ theorem, pending Claude review',
 'PRIMARY-SOURCE CHECK, review pending: Chatterjee, Annals of Mathematics 177 (2013), Theorem 1.1, states iid lattice weights, a nearly-Gamma law, a moment generating function near zero, the uniform upper/lower exponent definitions, and the matching conditions chi_a=chi_b and xi_a=xi_b for the relation chi=2xi-1. Its complete hypothesis list does not include a separate uniform-positive-curvature assumption. Proposition 5.1 provides suitable sphere-contact directions. This resolves an unknown-curvature flag in the retrieved secondary brain card only after source review; it supplies no matched-exponent proof for Uniform[1,2] and no current-openness certificate.',
 ['Historical statement: the original 2013 theorem, not every subsequent theorem','Primary hypothesis list read on 2026-10-10','Claude source clarification review pending'])
]
relations=[
 {'from_key':'finite-scale-wandering-tail','to_key':'terminal-bias-detour','kind':'depends_on','rationale':'The terminal-bias identity controls the norm excess on every minimizing path; its two interior mean biases are nonnegative.'},
 {'from_key':'finite-scale-wandering-tail','to_key':'euclidean-segment-detour','kind':'depends_on','rationale':'The segment-distance bound includes longitudinal overshoot and turns a geometric detour into a quadratic cost.'},
 {'from_key':'finite-scale-wandering-tail','to_key':'support-sphere-rounding','kind':'depends_on','rationale':'The selected norm direction and bounded rounding defect supply the quadratic norm lower bound without asserting uniform curvature.'},
 {'from_key':'subadditive-bias-countermodel','to_key':'centered-subadditive-shortcut','kind':'refutes','rationale':'The deterministic subadditive sequence has centered concentration on every scale but a mean bias n^beta.'},
 {'from_key':'lower-not-upper-curvature','to_key':'lower-to-upper-curvature-shortcut','kind':'refutes','rationale':'The l1 norm has a lower quadratic bound at the selected direction and an unbounded ratio to any upper quadratic bound there.'},
 {'from_key':'finite-scale-wandering-tail','to_existing_logical':'math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation','kind':'semantic_association','rationale':'A conditional passage-time-to-wandering bridge useful for P0110; neither exponent matching nor a solution of the target is proved.'},
 {'from_key':'primary-curvature-hypothesis-check','to_existing_logical':'math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation','kind':'semantic_association','rationale':'Clarifies the conditional theorem hypotheses for the P0110 target while retaining the unresolved matching-exponent gap.'}
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w381','bundle_slug':'p0110-terminal-bias-sphere-20261010-001','entries':entries,'relations':relations}
out=root/'drafts'
out.mkdir(exist_ok=True)
(out/'bundle_001.json').write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Record exact support at both ends, separately from the integrator's schema.
by_key={e['key']:e for e in entries}
cards=json.loads((root/'brain_cards.json').read_text(encoding='utf-8'))
target_card=next(c for c in cards if c['metadata'].get('bundle_entry_key')=='op-p0110')
supports=[]
for rel in relations:
    supports.append({**rel,'from_statement_quote':by_key[rel['from_key']]['statement'],
      'to_statement_quote':by_key[rel['to_key']]['statement'] if 'to_key' in rel else target_card['claim']['statement'],
      'review_status':'draft; w383 review pending','target_proof_status':'unresolved by this packet'})
(root/'EDGE_SUPPORT.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in supports),encoding='utf-8')

existing=[json.loads(x) for x in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if x]
for c in existing:
    if c['claim_id']=='w381-L1':
        c['exact_statement']='For every lattice x with h(x)=E T(0,x) finite, translation-invariant passage times, and g(x)=lim_m h(mx)/m, one has h(x)-g(x)>=0.'
        c['assumptions']=['Finite h(x)','Translation invariance and the passage-time triangle inequality','The stated limit defining g exists']
        c['proof_or_counterexample']=proof('L1')
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in existing),encoding='utf-8')
ids={x['claim_id'] for x in existing}
mapping=[('w381-L1','terminal-bias-detour'),('w381-L2','terminal-bias-detour'),('w381-L3','euclidean-segment-detour'),('w381-L4','support-sphere-rounding'),('w381-L5','finite-scale-wandering-tail'),('w381-L6','subadditive-bias-countermodel'),('w381-L7','lower-not-upper-curvature'),('w381-C1','primary-curvature-hypothesis-check')]
with (root/'CLAIMS.jsonl').open('a',encoding='utf-8',newline='\n') as handle:
    for claim_id,key in mapping:
        if claim_id in ids: continue
        e=by_key[key]
        handle.write(json.dumps({'claim_id':claim_id,'target':'P0110','exact_statement':e['statement'],
          'assumptions':e['assumptions'],'source':e['source'],'proof_or_counterexample':e['proof_text'] or 'Primary Theorem 1.1 complete hypothesis list; see PRIMARY_SOURCES.md. This is source verification, not a concrete-law exponent proof.',
          'independent_reviewer':'claude-4a88bc43 (pending source clarification)' if claim_id=='w381-C1' else 'w383 (pending)',
          'remaining_gap':'Matched global exponent theorem for a concrete law such as iid Uniform[1,2] on Z^2; no target solution claimed.',
          'status':'sketch' if claim_id=='w381-C1' else 'proved special case',
          'audit_status':'not independently checked','novelty_status':'no novelty claim; bounded specialization/counterexample or primary-source clarification'},ensure_ascii=False)+'\n')
    if 'w381-R1' not in ids:
        metric=json.loads((root/'route_receipt.json').read_text(encoding='utf-8'))
        handle.write(json.dumps({'claim_id':'w381-R1','target':'P0110',
          'exact_statement':'On the single task query in route_receipt.json, ordinary memory recall returned zero exact P0110 target cards among three memories; the opt-in read-only pilot returned the exact target first, with its prior attempt and complete conditional theorem hypotheses. All three card proof statuses remain unverified.',
          'assumptions':['The recorded P0110 query and the pinned historical math-card revisions','One loaded-machine observation; retrieval substrates differ'],
          'source':'route_receipt.json and route_output.json; command python -B -X utf8 ~/brain_workers/w381/measure_route.py',
          'proof_or_counterexample':metric,'independent_reviewer':'claude-4a88bc43 (pilot review pending)',
          'remaining_gap':'No held-out target-ID evaluation or broad recall improvement is established; installation and default recall changes are not performed.',
          'status':'numerical evidence','audit_status':'not independently checked'},ensure_ascii=False)+'\n')

source_status={
 'target_id':'P0110','working_title':'An iid FPP law with proved KPZ exponent relation',
 'current_openness':'UNKNOWN','target_status':'unresolved by this attempt',
 'exact_statement_status':'recovered and primary-reference checked',
 'primary_target_source':{'url':'https://arxiv.org/pdf/1511.03262v2','question':22,'physical_pdf_page':89,'printed_page':88,'equation':'4.19'},
 'concrete_candidate':{'law':'Uniform[1,2]','graph':'undirected nearest-neighbor Z^2','nondegenerate':True,'law_eligibility':'satisfied; matching exponents not proved'},
 'exponent_formulation':'Chatterjee global chi_a, chi_b, xi_a, xi_b; exact definitions in STATEMENT.md',
 'conditional_relation_sources':['https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p07-p.pdf','https://arxiv.org/pdf/1109.0523v2'],
 'source_clarification':{'existing_node_id':'claim_e090760039c41cb781c56fbb85679625a58a678ff42cfb3ec11a01d8887de6c5','flag':'separate curvature hypothesis unknown','primary_check':'No separate curvature condition in Theorem 1.1; matching remains required','claude_review':'pending'},
 'recent_literature_checked':[{'url':'https://arxiv.org/abs/2312.14143','scope':'rotationally invariant planar FPP; no iid lattice transfer supplied'},{'url':'https://arxiv.org/abs/2604.01214','date':'2026-04-01','scope':'rotationally invariant Riemannian FPP; no iid lattice transfer supplied'}],
 'prior_work':{'ranking':'2026-09-07 tier 5 / attempted_un; historical only','intake':'brain_bundle_C006p01.json and brain_bundle_C006a04.json; full task card and attempt retrieved read-only','H_I_attempts':'targeted case-insensitive exact-ID/title searches found no match','lean_campaign':'P0110 found in annotated ranking only; no formal proof located','original_codex_worktree':'recorded old importer path absent','solved_owner_memory':'directed width-3 strip time constant; different model and claim'},
 'formal_check':{'performed':False,'counts_as_proof':False},
 'brain_states':{'submitted':False,'reviewed':False,'ingested':False,'retrievable':False},
 'independent_audit':'pending; own consistency checks are not an independent audit',
 'hardest_gap':'Matched global exponents chi_a=chi_b and xi_a=xi_b for one concrete nondegenerate iid lattice law'}
(root/'SOURCE_STATUS.json').write_text(json.dumps(source_status,indent=2),encoding='utf-8')

hooks=[{'id':'p0110-w381-01','area':'math','event':'PreToolUse','cue':'P0110 or claim_e090760.* together with unconditional KPZ/solved wording',
 'fire_when':'An agent cites the conditional KPZ theorem as proving exponents exist for Uniform[1,2].',
 'silent_when':'The agent states chi_a=chi_b and xi_a=xi_b as unproved assumptions and keeps the target unresolved.',
 'text':'For this lattice FPP target, write the two exponent-matching assumptions beside the KPZ relation. The relation theorem does not prove those assumptions for your law. Check the model before using rotationally invariant results.',
 'evidence':'w381/brain_cards.json conditional-result assumptions; w381/PRIMARY_SOURCES.md Theorem 1.1; recall scar perceptron_proof_open_gaps_fleet_2026_07_12','proposer':'w381'},
 {'id':'p0110-w381-02','area':'brain','event':'stage-start','cue':'query contains the exact verified identifier P0110',
 'fire_when':'P0110 memory recall has no exact target card even though the math store contains op-p0110.',
 'silent_when':'The query has no P0110 identifier, or a complete exact target card has already been retrieved.',
 'text':'A verified problem ID may live in the math store rather than the memory index. For P0110, use the bounded read-only target route and read its full conditional-result hypotheses before proving.',
 'evidence':'w381/route_receipt.json: exact target hits 0 to 1 on one query; three full cards and unverified statuses preserved','proposer':'w381'}]
for h in hooks: assert len(h['text'])<=300
(root/'HOOK_PROPOSALS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in hooks),encoding='utf-8')

patches=root/'patches'
patches.mkdir(exist_ok=True)
for filename,destination,contents in (
 ('01_p0110_math_route.diff','.claude/dreaming/p0110_math_route.py',(root/'p0110_math_route.py').read_text(encoding='utf-8')),
 ('02_p0110_hooks.diff','primary_directive/hooks1000/proposals/p0110-w381.jsonl',(root/'HOOK_PROPOSALS.jsonl').read_text(encoding='utf-8')),
):
    # The requested review diff names both live paths. Git creation patches
    # additionally require /dev/null as the old file, so ship both forms.
    review_diff=''.join(difflib.unified_diff([],contents.splitlines(keepends=True),fromfile='a/'+destination,tofile='b/'+destination))
    (patches/filename).write_text(review_diff,encoding='utf-8')
    git_diff='diff --git a/'+destination+' b/'+destination+'\nnew file mode 100644\n'+''.join(difflib.unified_diff([],contents.splitlines(keepends=True),fromfile='/dev/null',tofile='b/'+destination))
    (patches/filename.replace('.diff','.git.patch')).write_text(git_diff,encoding='utf-8')

print(json.dumps({'entries':len(entries),'relations':len(relations),'claim_rows':len((root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()),'local_bundle':str(out/'bundle_001.json'),'live_ingestion':False}))
