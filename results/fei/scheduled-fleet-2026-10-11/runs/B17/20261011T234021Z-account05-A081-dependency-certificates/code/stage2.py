from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,shutil,time
RUN=Path(__file__).resolve().parents[1]; OWN=RUN.parents[1]
PREV=OWN/'runs/20261011T214745Z-account05-A081-dependency-certificates'
TEAM=OWN.parents[1]
LEAD=TEAM/'claude/B17/runs/20261011T224300Z-claude-B17-erasure-census-affine-bridge'
R93=TEAM/'agents/A093/runs/20261011T223137Z-account05-A093-literature-and-priority'
R82=TEAM/'agents/A082/runs/20261011T221008Z-account05-A082-finite-inequalities'
R18=TEAM/'claude/B18/runs/20261011T222429Z-claude-B18-proof-audit'
(RUN/'out').mkdir(parents=True,exist_ok=True)
shutil.copyfile(PREV/'code/dependency_check.py',RUN/'code/dependency_check.py')
from dependency_check import validate,statement_hash,key
def read(p):
    raw=p.read_bytes(); return raw.decode('utf-16' if raw.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig')
def load(p):return json.loads(read(p))
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
g=load(PREV/'PROOF_DEPENDENCIES.json'); g['run_id']=RUN.name
sources=g['sources']; nodes=g['nodes']
def pin(sid,p,origin=None):
    raw=p.read_bytes(); lf=raw.replace(b'\r\n',b'\n')
    sources[sid]={'local_path':str(p),'local_sha256':hashlib.sha256(raw).hexdigest(),'lf_sha256':hashlib.sha256(lf).hexdigest(),'origin':origin,'pin_scope':'Exact immutable byte hash of read source snapshot.'}
    return sid
pin('stage1_graph',PREV/'PROOF_DEPENDENCIES.json')
pin('board_stage2',TEAM/'BOARD.md'); pin('B17_notes_v2',TEAM/'claude/B17/STREAM_NOTES.md')
pin('B17_claims',LEAD/'CLAIMS.json'); pin('B17_census_output',LEAD/'out/census_n4.json')
pin('B17_census_code',LEAD/'code/census_n4.py'); pin('B17_certlog',LEAD/'code/certlog.py')
pin('B17_cutoff_code',LEAD/'code/search_n56.py'); pin('B17_b09_code',LEAD/'code/b09_interval.py')
pin('B17_b09_output',LEAD/'out/b09_interval.json')
pin('A082_claims',R82/'CLAIMS.json'); pin('A082_proof',R82/'EXHAUSTIVENESS_LEMMA.tex')
pin('A082_certificate',R82/'FINITE_INEQUALITY_CERTIFICATE.json')
pin('B18_reviews',R18/'CLAIMS.json')
pin('A093_review',R93/'REPORT.md'); pin('A093_claims',R93/'CLAIMS.json'); pin('A093_primary_audit',R93/'PRIMARY_SOURCE_OVERLAP.md')
pin('MU1988_pdf',R93/'out/maassen_uffink_1988.pdf',{'doi':'10.1103/PhysRevLett.60.1103','url':'https://www.math.ru.nl/~maassen/papers/EntrUncert.pdf','title':'Generalized entropic uncertainty relations','version':'1988 final published article','locator':'p.1103 equations (3),(5),(6); p.1104 equations (10)-(13)'})
pin('MU1988_page1',R93/'out/mu_page1.png'); pin('MU1988_page2',R93/'out/mu_page2.png')
pin('stage2_code',Path(__file__))
leadclaims=load(LEAD/'CLAIMS.json'); lc={c['claim_id']:c for c in leadclaims}
hashchecks=[]
for c in leadclaims:
    computed=statement_hash(c['exact_statement'],c['hypotheses'])
    hashchecks.append({'claim_key':key(c),'expected':c['statement_sha256'],'computed':computed,'match':c['statement_sha256']==computed})
save(RUN/'out/LEAD_HASH_AUDIT.json',hashchecks)
assert all(x['match'] for x in hashchecks)

UNITS=nodes[0]['units']; BIASED=next(n for n in nodes if n['claim_id']=='B09-BIASED-BLOCK-UNCERTAINTY')['units']
def find(cid):return next(n for n in nodes if n['claim_id']==cid)
def edge(cid,why,conversion=None):
    n=find(cid); return {'claim_key':key(n),'statement_sha256':n['statement_sha256'],'hypothesis_instantiation':why,'unit_conversion':conversion}
def add(cid,statement,hyp,status,sid,locator,dependencies=(),evidence=(),units=None,first=None):
    n={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':statement_hash(statement,hyp),'units':units or UNITS,'status':status,'proof_sources':[{'source_id':sid,'locator':locator}],'proof_dependencies':list(dependencies),'evidence':list(evidence),'first_unproved_line':first}
    nodes.append(n); return n

# Source pin and exact finite-unitary theorem replacing the historical missing leaf.
mu=add('MU-FINITE-UNITARY-1988','For every N>=1, unitary U in C^(N x N), and unit vector a in C^N, let P_j=|a_j|^2, Q_k=|(Ua)_k|^2, c=max_j,k |U_kj|. Then H_nat(P)+H_nat(Q)>=-2 ln(c); equivalently H_2(P)+H_2(Q)>=-2 log2(c).',['finite N','U unitary','sum_j |a_j|^2=1','zero entropy atoms contribute zero','c in [N^-1/2,1]'],'IMPORTED_ACCEPTED','MU1988_pdf','p.1103 equations (3),(5),(6); proof p.1104 (10)-(13)',evidence=[{'classical_primary_source':'Final article visually inspected on pp.1103-1104','independent_application_review':'A093_claims B09 core review; A081 reconstructs finite-unitary specialization in this REPORT'}],units=BIASED)
find('MU-ENTROPIC-UNCERTAINTY-UNPINNED')['resolution']={'replacement_claim_key':key(mu),'kind':'HISTORICAL_UNPINNED_LEAF_RESOLVED','no_statement_overwrite':True}
b09=find('B09-BIASED-BLOCK-UNCERTAINTY'); prior=load(R93/'CLAIMS.json')[0]
assert b09['statement_sha256']==prior['statement_sha256']
b09['status']='IMPORTED_ACCEPTED'; b09['proof_dependencies']=[edge('MU-FINITE-UNITARY-1988','For each nonzero residual spectral fiber T, use N=2^|A|, normalized real a_R=fhat(R union T)/sqrt(q_T), U=tensor_i [[sqrt(1-p_i),-sqrt(p_i)],[sqrt(p_i),sqrt(1-p_i)]]. Orthogonality and norm one hold by product Parseval; c=product_i sqrt(max(p_i,1-p_i)). Average over q_T, then subtract from H(Z)=sum_i h2(p_i).','Natural-to-bit conversion divides both sides by ln(2); c^2=product_i max(p_i,1-p_i).')]
b09['evidence'].append({'reviewer':'A093','verdict':'ACCEPT_AT_STATED_SCOPE_CORE_ONLY','source_id':'A093_claims','record':prior['review_records'][0]})
b09['first_unproved_line']=None
b09['scope_exclusions']=['No uniform influence payment','No necessity or optimality of tax inferred','No arbitrary substitution or shared-variable additivity']
b09['proof_sources'].append({'source_id':'A093_review','locator':'complete derivation and source applicability reconstruction'})

# Freeze one finite witness before exact arithmetic; do not redo censuses.
spec={'helper_version':'stage2.py v1 sha256 '+hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'One five-bit sign g=-1 exactly on integer vertices {5,12,13}; a seven-coordinate signed permutation/dummy extension fixture','parameter_domain':'n=5 one named witness; one n=7 scope fixture; no further dimensions','case_count':2,'symmetry':'none','arithmetic':'integer Walsh transform, Fraction coefficients of log2 primes, dyadic-reduced rational atanh intervals (48 terms)','memory_estimate_MB':32,'maximum_runtime_seconds':60,'search':'No census or optimization; source graph integration and one named exact witness reconstruction.'}
save(RUN/'out/FROZEN_SPEC.json',spec)
start=time.perf_counter(); assertions=0
def check(b):
    global assertions
    assert b; assertions+=1
def fwht(vals):
    a=list(vals); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a
def factors(m):
    out={}; p=2
    while p*p<=m:
        while m%p==0:out[p]=out.get(p,0)+1; m//=p
        p+=1
    if m>1:out[m]=out.get(m,0)+1
    return out
def form_add(a,b,m=Q(1)):
    r=dict(a)
    for p,v in b.items():r[p]=r.get(p,Q(0))+m*v
    return {p:v for p,v in r.items() if v}
def mlog(m):return {p:Q(m*v) for p,v in factors(m).items()} if m>1 else {}
def erasure(W,i):
    f={}; d=len(W)**2
    for T in range(len(W)):
        if T&(1<<i):continue
        a=W[T]**2; b=W[T|(1<<i)]**2
        f=form_add(f,mlog(a+b)); f=form_add(f,mlog(a),Q(-1)); f=form_add(f,mlog(b),Q(-1))
    return {p:v/d for p,v in f.items()}
def lns(x):
    z=(x-1)/(x+1); s=Q(0); power=z
    for j in range(48): s+=2*power/(2*j+1); power*=z*z
    return s,s+2*power/(97*(1-z*z))
ln2=lns(Q(2)); logcache={}
def logs(p):
    if p not in logcache:
        k=p.bit_length()-1; a,b=lns(Q(p,2**k)); logcache[p]=(Q(k)+a/ln2[1],Q(k)+b/ln2[0])
    return logcache[p]
def bounds(form):
    lo=hi=Q(0)
    for p,c in form.items():
        a,b=logs(p)
        if c<0:a,b=b,a
        lo+=c*a; hi+=c*b
    return lo,hi
def rounded(a,digits=24):
    scale=10**digits
    def fmt(v):
        sign='-' if v<0 else ''; v=abs(v)
        return f'{sign}{v//scale}.{v%scale:0{digits}d}'
    return [fmt(a[0].numerator*scale//a[0].denominator),fmt(-((-a[1].numerator*scale)//a[1].denominator))]
W=fwht([-1 if x in (5,12,13) else 1 for x in range(32)])
check(sum(w*w for w in W)==1024)
rows=[]; fA={2:Q(16,3),3:Q(-3,8),13:Q(-169,24),89:Q(89,24)}; fB={2:Q(16),3:Q(-63,8),5:Q(15),13:Q(-169,8),17:Q(85,8)}
for i in range(5):
    I=Q(sum(W[S]**2 for S in range(32) if S&(1<<i)),1024)
    physical=Q(sum((x in (5,12,13))!=((x^(1<<i)) in (5,12,13)) for x in range(32)),32)
    check(I==physical); check(I==Q(3,16) if i in (1,2,4) else I==Q(1,16))
    E=erasure(W,i); R={p:v/I for p,v in E.items()}; check(R==(fA if i in (1,2,4) else fB))
    gap=form_add(R,{2:Q(107,40)},Q(-1)); check(bounds(gap)[0]>0)
    rows.append({'i':i,'I':str(I),'B_over_I_prime_form':{str(p):str(c) for p,c in R.items()},'ratio_interval':rounded(bounds(R)),'excess_over_107_40_interval':rounded(bounds(gap))})
check(bounds(form_add(fB,fA,Q(-1)))[0]>0)
k4={2:Q(4),3:Q(-9,2),5:Q(5,2)}
check(bounds(form_add({2:Q(107,40)},k4,Q(-1)))[0]>0)
# Scalar/aggregate names must remain distinct. This is not a new census.
aggregate=Q(0)
for i in range(5):aggregate+=Q(sum(W[S]**2 for S in range(32) if S&(1<<i)),1024)
aggregateForm={}
for i in range(5):aggregateForm=form_add(aggregateForm,erasure(W,i),1/aggregate)
check(bounds(form_add(aggregateForm,fA,Q(-1)))[0]>0)
# Output negation and physical translation, with two irrelevant dummy inputs.
W7=fwht([1 if ((x&31)^2) in (5,12,13) else -1 for x in range(128)])
check(sum(w*w for w in W7)==128**2)
for i in range(7):
    I7=Q(sum(W7[S]**2 for S in range(128) if S&(1<<i)),128**2)
    if i<5:
        check(I7==Q(rows[i]['I'])); check(erasure(W7,i)==erasure(W,i))
    else:check(I7==0); check(erasure(W7,i)=={})
check(time.perf_counter()-start<60)
result={'status':'PASS','assertions':assertions,'walsh_vector':W,'rows':rows,'min_ratio_interval':rounded(bounds(fA)),'K4_interval':rounded(bounds(k4)),'aggregate_B_over_I_interval':rounded(bounds(aggregateForm)),'elapsed_seconds':time.perf_counter()-start,'all_five_relevant':True,'seven_coordinate_translation_negation_dummy_fixture':'PASS; five ratios unchanged, two irrelevant B_i=I_i=0','census_repeated':False,'proof_error':'Mantissa in [1,2); z<=1/3; 48-term atanh tail <=2z^97/[97(1-z^2)]; all endpoints Fraction.'}
save(RUN/'out/FIVEBIT_EXACT.json',result)

# Preserve literal versions and distinguish acceptance from author certification.
base=find('BASE-ERASURE'); base['status']='IMPORTED_ACCEPTED'; base['evidence'].append({'reviewer':'A081 stage2','source_id':'stage2_code','reconstruction':'REPORT: packet Fourier identities, nonnegativity, chain rule and influence decomposition.'})
add('BASE-PACKET-RESTRICTION-IDENTITIES','For a uniform Boolean f, u_T=fhat(T), v_T=fhat(T+i), s_T=u_T^2+v_T^2; the child coefficients are u_T+v_T and u_T-v_T, their average squared law is s_T, B_i=sum_T s_T h2(v_T^2/s_T), Delta_i H=B_i+JS_i, I(f)=I_i+(I(f_+)+I(f_-))/2, and sum_i B_i<=H(f).',['actual Boolean physical restrictions','uniform finite cube','zero packets omitted','entropy in bits'],'IMPORTED_ACCEPTED','stage2_code','Algebra reconstructed in stage2 REPORT; separate identity node excludes the JS upper bound',evidence=[{'reviewer':'A081','method':'Fourier expansion of restrictions, Parseval and Shannon chain rule; no JS upper bound used.'}])
six=[c for c in leadclaims if c['claim_id']!='B17-SELECTION-GROWTH-EVIDENCE']
for c in six:
    status=('IMPORTED_ACCEPTED' if c['claim_id'] in ['B17-JS-PACKET-SCALAR','B17-KB-TWO-SIDED','B17-ZERO-ERASURE-TRANSPORT'] else 'PENDING_FINITE_AUDIT')
    n=add(c['claim_id'],c['exact_statement'],c['hypotheses'],status,'B17_claims','exact claim record and source locators therein',evidence=[{'author_status':c['status'],'author_review_records':c['review_records'],'original_proof_dependencies':c['proof_dependencies']}],first=c['first_unproved_line'],units=BIASED if c['claim_id']=='B17-B09-INTERVAL' else UNITS)
    check(n['statement_sha256']==c['statement_sha256'])
    if status=='IMPORTED_ACCEPTED':n['evidence'].append({'reviewer':'A081','verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent derivative proof and coordinate induction; written in stage2 REPORT. No repair to literal statement.'})
find('B17-JS-PACKET-SCALAR')['proof_dependencies']=[edge('BASE-PACKET-RESTRICTION-IDENTITIES','Use u=fhat(T), v=fhat(T+i), s=u^2+v^2 and z=2uv/s. Sum finite nonzero packets; scalar bound extends by evenness and endpoint continuity.')]
base['proof_dependencies']=[edge('BASE-PACKET-RESTRICTION-IDENTITIES','Use exactly its restriction, influence and chain-rule identities.'),edge('B17-JS-PACKET-SCALAR','Instantiate its packetwise JS upper bound; avoid using an upper bound to prove itself.')]
find('B17-KB-TWO-SIDED')['proof_dependencies']=[edge('B17-JS-PACKET-SCALAR','Choose a relevant i minimizing B_i/I_i; constants K_sel(n) nondecreasing in n. Each child has at most n-1 relevant coordinates.'),edge('BASE-PACKET-RESTRICTION-IDENTITIES','Sum_i B_i<=H gives min_i B_i/I_i<=H/I by weighting by I_i/I. Influence decomposition pays each node once.')]
find('B17-ZERO-ERASURE-TRANSPORT')['proof_dependencies']=[edge('BASE-PACKET-RESTRICTION-IDENTITIES','Each conditional packet entropy is nonnegative and vanishes iff u*v=0. Children u+v,u-v have the same squared coefficients u^2+v^2; projection is injective on support.')]
find('B17-KB4-CENSUS')['proof_sources']+=[{'source_id':'B17_census_code','locator':'census computation and exact maximum verification'},{'source_id':'B17_certlog','locator':'float_screen and sign_form'},{'source_id':'B17_census_output','locator':'results, separate selectable and aggregate maxima'}]
find('B17-KB4-CENSUS')['first_unproved_line']='A085 exact full-census and rigorous floating-screen audit still pending; author certificate retained without rerunning census.'

a82=load(R82/'CLAIMS.json')[0]
add(a82['claim_id'],a82['exact_statement'],a82['hypotheses'],'PENDING_REVIEW','A082_claims','A082-FINITE-TRUE-ERASURE@1',evidence=[{'author_status':a82['status'],'review_source':'B18_reviews: inspect HOLDS record before admission'}])
reviews=load(R18/'CLAIMS.json')
save(RUN/'out/B18_REVIEW_STRUCTURE.json',reviews)
# Admit the exact scoped A082 theorem from its recorded independent review,
# without adopting the unreviewed compound B17 census statement.
rv=next(r for r in reviews['review_verdicts'] if r['claim_id']=='A082-FINITE-TRUE-ERASURE')
assert rv['verdict']=='HOLDS'
an=find('A082-FINITE-TRUE-ERASURE'); an['status']='IMPORTED_ACCEPTED'; an['evidence'].append({'review_record':rv,'source_id':'B18_reviews','adoption_scope':'Original at-most-four-variable selectable theorem only; author certificate and independent reconstruction both source pinned.'})
an['proof_sources']+=[{'source_id':'A082_proof','locator':'Theorem 1 finite exact census argument'},{'source_id':'A082_certificate','locator':'frozen finite inequality certificate'},{'source_id':'B18_reviews','locator':'review_verdicts A082-FINITE-TRUE-ERASURE HOLDS and B18-N4-GOOD-COORDINATE-CERTIFICATE'}]
# Source pin a recorded review but avoid treating a free-form verdict as a proof certificate.
find('B17-KB5-CUTOFF')['proof_dependencies']=[edge('A082-FINITE-TRUE-ERASURE','Only the four-variable selectable constant is used; full B17 compound census maxima are not prerequisites.')]
find('B17-KB5-CUTOFF')['proof_sources'].append({'source_id':'stage2_code','locator':'fwht, erasure prime forms and rational sign comparisons; FIVEBIT_EXACT.json'})
find('B17-KB5-CUTOFF')['evidence'].append({'reviewer':'A081','verdict':'WITNESS_AND_CONSTANT_COMPARISONS_CHECKED','method':'Integer Walsh/Fraction log form reconstruction; census prerequisite evidence separate.'})
find('B17-KB5-CUTOFF')['status']='IMPORTED_CERTIFIED'
find('B17-KB5-CUTOFF')['first_unproved_line']=None
find('B17-B09-INTERVAL')['proof_sources']+=[{'source_id':'B17_b09_code','locator':'prime form and directed decimal rounding'},{'source_id':'B17_b09_output','locator':'claimed 30-decimal interval'},{'source_id':'B17_certlog','locator':'rational prime log enclosure'}]
find('B17-B09-INTERVAL')['first_unproved_line']='Stronger 30-decimal interval remains author-certified here; prior 18-decimal interval was already checked. No number rerun.'

cutoff=add('A081-FIVEBIT-SELECTION-CUTOFF','For the actual five-bit Boolean g=-1 exactly at vertices {5,12,13}, every relevant coordinate satisfies B_i/I_i>107/40. The minimum equals 16/3-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89). Thus a universal selectable-erasure rule with K<=107/40 is false.',['uniform physical cube','B_i=H(S_i|S_-i)','I_i physical pivotal probability, equal to squared-spectral inclusion','entropy in bits','all five coordinates relevant'],'LOCAL_CERTIFICATE_PENDING_REVIEW','stage2_code','FIVEBIT_EXACT.json and exact formulas',evidence=[{'exact_certificate':str(RUN/'out/FIVEBIT_EXACT.json'),'source_witness':'B17-KB5-CUTOFF@1','independent_algorithm':'integer Walsh and prime-log interval forms derived from truth table, no float screening'}])
add('OPEN-SELECTABLE-ERASURE','There exists finite dimension-independent K such that every nonconstant uniform Boolean f has some relevant coordinate i with B_i(f)<=K I_i(f).',['actual physical restrictions','existential i, not every i','one universal finite K'],'OPEN','B17_claims','B17-KB-TWO-SIDED first unproved line',first='K_sel=sup_n max_f min_i B_i/I_i remains unbounded by the current proofs; K must exceed 107/40.')
g['candidate_routes'].append({'route_id':'R-SELECTABLE-C018','conclusion':'FEI-FINAL@1','requires':['B17-KB-TWO-SIDED@1','OPEN-SELECTABLE-ERASURE@1'],'derivation':'For every descendant choose a relevant coordinate with B_i<=K I_i and use independently reconstructed JS bound; telescope influence to obtain FEI(K+2/ln2).','status':'CONDITIONAL_ROUTE_ONLY'})
g['scope_relations']=[{'from':'B17-KB5-CUTOFF@1','to':'A082-FINITE-TRUE-ERASURE@1','relation':'BLOCKS_DOMAIN_EXTENSION_ONLY','failed_strengthening':'Same four-coordinate constant for all dimensions','preserved':'A082 original at-most-four-variable claim and affine4/product domain are not refuted.'}]
g['metric_definitions']={'K_sel(n)':'max_f with <=n relevant coords min_relevant_i B_i/I_i; called K_B(n) by B17 lead','K_agg(n)':'max_f with <=n relevant coords (sum_i B_i)/I; aggregate C018 quantity','C(n)':'max_f with <=n relevant coords H/I','known_relationship':'K_sel(n)<=K_agg(n)<=C(n)<=K_sel(n)+2/ln2; aggregate erasure is sufficient, selectable erasure is a distinct equivalent-finiteness route.'}
g['change_receipts']={'prior_graph_sha256':sources['stage1_graph']['local_sha256'],'new_exact_B17_claims':6,'B09_literal_statement_unchanged':True,'MU_source_gap_resolved':True,'finite_census_not_repeated':True,'universal_constant_change':None}
# Freeze mutable/read-only original source snapshots inside this run. Preserve
# original metadata; never rewrite the imported source trees or old run.
snap=RUN/'out/source_snapshots'; snap.mkdir(exist_ok=True)
for sid,s in sources.items():
    original=Path(s['local_path']); raw=original.read_bytes()
    check(hashlib.sha256(raw).hexdigest()==s['local_sha256'])
    dest=snap/(sid+original.suffix)
    dest.write_bytes(raw); s['original_local_path']=str(original); s['local_path']=str(dest)
save(RUN/'PROOF_DEPENDENCIES.json',g)
v=validate(g); check(v['status']=='STRUCTURALLY_VALID'); check(not v['unresolved_closure']['B09-BIASED-BLOCK-UNCERTAINTY@1'])
save(RUN/'out/VALIDATION.json',v)
save(RUN/'out/STAGE2_SUMMARY.json',{'nodes':len(nodes),'source_pins':len(sources),'assertions':assertions,'B09_dependency_closure':v['unresolved_closure']['B09-BIASED-BLOCK-UNCERTAINTY@1'],'new_nodes':[key(n) for n in nodes if n['claim_id'] in [c['claim_id'] for c in six]],'new_primary_source_key':key(mu),'all_routes_still_open':all(not r['eligible_for_mathematical_review'] for r in v['candidate_routes'])})
print(json.dumps(load(RUN/'out/STAGE2_SUMMARY.json'),indent=2))
