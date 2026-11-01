"""Build LOCAL draft bundles and deployment patches; never ingest or send messages."""
from collections import defaultdict
import difflib
import json
from pathlib import Path
import re
import sqlite3

ROOT=Path(__file__).resolve().parent
IDS=['P0288','C0034','C0151','P0127','P0456','C0058','C0082','C0126','P0014','P0042']
FILES=['P0288_recheck','C0034_rank_two','C0151_thinning','P0127_growth_bias','P0456_finite_calibration','C0058_boundary_identity','C0082_cycle_counts','C0126_walk_direction','P0014_fourier','P0042_tree4']
NAMES=dict(zip(IDS,FILES))
NS=dict(zip(IDS,['probability.markov','probability.determinantal','probability.factors','probability.latticetrees','probability.randomgraphs','probability.planarmaps','probability.percolation','probability.percolation','combinatorics.spectral','probability.bootstrap']))

def dump(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def patch_additions(name,files):
    chunks=[]
    for live,local in files:
        content=local.read_text(encoding='utf-8').splitlines(keepends=True)
        chunks.append('diff --git a/'+live+' b/'+live+'\n')
        chunks.extend(difflib.unified_diff([],content,fromfile='a/'+live,tofile='b/'+live))
    dest=ROOT/'patches'/name
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(''.join(chunks),encoding='utf-8')

def main():
    targets=json.loads((ROOT/'reports'/'resolved_targets.json').read_text(encoding='utf-8'))
    oldcards=json.loads((ROOT/'reports'/'existing_cards.json').read_text(encoding='utf-8'))
    metrics=json.loads((ROOT/'measurements'/'summary.json').read_text(encoding='utf-8'))
    higher=json.loads((ROOT/'measurements'/'C0034_higher_rank_summary.json').read_text(encoding='utf-8'))
    entries=defaultdict(list)
    relations=defaultdict(list)
    proofs={pid:(ROOT/'proofs'/(NAMES[pid]+'.md')).read_text(encoding='utf-8') for pid in IDS}
    bykey={}
    def add(pid,key,kind,title,statement,assumptions):
        logical=pid.lower()+'-'+key
        entry={'key':key,'namespace':NS[pid],'logical_name':logical,'kind':kind,
               'title':title+' [audit pending w347]','statement':statement,
               'proof_text':proofs[pid] if kind in ('lemma','theorem') else None,
               'assumptions':assumptions,'domain':'probability theory' if pid!='P0014' else 'graph theory and probability',
               'source':{'source_id':'owner-work:w341:'+logical,'url':(ROOT/'proofs'/(NAMES[pid]+'.md')).as_uri(),
                         'revision':'author-checked-2026-10-10; independent audit pending w347',
                         'license':'owner-own-work (campaign mathematics; literature attributed)','excerpt':None}}
        entries[pid].append(entry); bykey[pid,key]=entry
        return key
    def rel(pid,frm,to,kind):
        a,b=bykey[pid,frm]['statement'],bykey[pid,to]['statement']
        relations[pid].append({'from_key':frm,'to_key':to,'kind':kind,'rationale':'From: "'+a+'" To: "'+b+'".'})
    def cross(pid,frm,target,kind='cites',quote=None,note=''):
        relations[pid].append({'from_key':frm,'to_existing_logical':target['logical_id'],'kind':kind,
            'rationale':'From: "'+bykey[pid,frm]['statement']+'" To: "'+(quote or target['body'].split('\n')[0])+'". '+note})

    add('P0288','killed-walk-definition','definition','Two-ended killed continuous-time walk',
        'On the transient class Z, the chain jumps from i to i+1 and i-1 at rate one each and jumps to a separate absorbing cemetery at rate kappa+v*1_{i=0}, with kappa>0 and v>0. Its transient generator is Delta-kappa I-v|0><0|, where Delta f(i)=f(i+1)+f(i-1)-2f(i).',['kappa>0','v>0'])
    add('P0288','positive-rank-two-asymptotic-kernel','lemma','Existing killed-walk candidate: explicit rank-two minor',
        'For the two-ended killed walk just defined, lambda=kappa, the class is lambda-transient, and for fixed integers i,j the limit of t^(3/2)*exp(kappa*t)*p_t(i,j) is [max(ij,0)+(|i|+|j|)/v+2/v^2]/(2*sqrt(pi)). This strictly positive kernel has rank two and its {0,1} minor is 1/(4*pi*v^2). It cannot factor as a rank-one product. This rechecks an existing campaign candidate and does not certify novelty.',['rate-one nearest-neighbor jumps on Z','uniform killing kappa>0','extra killing v>0 at lattice zero','separate absorbing cemetery'])
    rel('P0288','positive-rank-two-asymptotic-kernel','killed-walk-definition','depends_on')

    add('C0034','projection-singleton-pair-laws','definition','Rank-one and rank-two finite projection laws',
        'For finite E and orthogonal unit vectors u,v in C^E, the projection law on span(u) chooses singleton {i} with mass |u_i|^2. The law on span(u,v) chooses {i,j}, i<j, with mass |u_i*v_j-u_j*v_i|^2. These are fixed-cardinality determinantal projection laws.',['E finite','u and v orthogonal unit vectors'])
    add('C0034','constructive-rank-two-union-coupling','lemma','Constructive disjoint coupling for two rank-one projections',
        'For finite E and orthogonal unit vectors u,v in C^E, there is a coupling of singleton projection laws on span(u) and span(v) whose disjoint union has projection law on span(u,v). A capacitated flow splits edge masses q_ij=|u_i*v_j-u_j*v_i|^2 between endpoints with first marginal |u_i|^2. Every required cut holds because its internal mass is U_A*V_A-|c_A|^2<=U_A, where U_A=sum_A|u_i|^2, V_A=sum_A|v_i|^2 and c_A=sum_A u_i*conjugate(v_i).',['E finite','u and v orthogonal unit vectors'])
    add('C0034','rank-one-complement-domination-reduction','lemma','Rank-one summand: reduction to published stochastic domination',
        'If H=H_1 orthogonal-sum H_2 on a finite ground set and one summand has rank one, the union-marginal coupling exists. Couple the other summand as a subset of a sample from P_H using projection stochastic domination and Strassen. The set difference is a singleton with inclusion masses equal to the rank-one projection diagonal, hence has exactly that summand law. This is a consequence of Lyons (2014), Theorem 2.7.',['finite ground set','orthogonal summands','one summand has rank one','published projection stochastic domination theorem'])
    add('C0034','exact-higher-rank-coupling-certificates','concept','Eight exact certificates for rank-two plus rank-two projections',
        'Finite evidence for the general union-marginal coupling question: eight rational orthogonal-matrix instances with summand ranks (2,2), four each in dimensions five and six, admit nonnegative rational coupling masses with all three determinantal marginals exactly correct. All eight saved points were independently replayed using Gram determinants. A float LP supplied only a support; exact arithmetic certified the points. These examples do not prove the general question.',['the eight matrices and rational masses in measurements/C0034_higher_rank_certificates.jsonl'])
    add('C0034','conditional-splitting-exact-failure','concept','Naive conditional splitting has an exact rational counterexample',
        'Sampling a rank-two projection pair C, choosing a singleton i in C with probability proportional to |u_i|^2, and giving the remaining endpoint to the second marginal need not reproduce either intended rank-one law. The saved rational three-coordinate counterexample has second-marginal total variation about 0.1136890368; the exact fraction and vectors are preserved. This refutes this splitting rule, not existence of another coupling.',['the rational vectors in measurements/C0034_naive_counterexample.json','orthogonal rank-one summands'])
    rel('C0034','constructive-rank-two-union-coupling','projection-singleton-pair-laws','depends_on')
    rel('C0034','rank-one-complement-domination-reduction','projection-singleton-pair-laws','cites')
    rel('C0034','exact-higher-rank-coupling-certificates','constructive-rank-two-union-coupling','analogous_to')
    rel('C0034','conditional-splitting-exact-failure','constructive-rank-two-union-coupling','cites')

    add('C0151','fiid-independent-density-thinning','lemma','Factor independent-set densities are downward closed; endpoint qualified',
        'If an automorphism-equivariant factor-of-i.i.d. independent set on the d-regular tree has root density a>0, every b in [0,a] is also attainable by independently retaining its vertices with probability b/a, using an independent label family obtained by splitting the i.i.d. labels. If A is the supremum of attainable densities, the attainable set contains [0,A) and is contained in [0,A]; inclusion of A requires an attainment argument.',['d-regular tree','automorphism-equivariant factor of independent uniform labels','root density a>0'])
    add('C0151','large-degree-gap-conditional-refutation','lemma','Conditional reduction of Szegedy density equality to known asymptotic bounds',
        'Suppose for every sufficiently large d the factor-of-i.i.d. density supremum on the d-regular tree is at most (5/4)*log(d)/d, while random d-regular graphs admit asymptotic independent-set density at least (7/4)*log(d)/d. Then the two attainable-density sets differ for those d. The cited Rahman-Virag and Ding-Sly-Sun asymptotics are a local literature lead; their primary statements were not reverified here.',['both explicitly stated large-d bounds','same independent-set and density conventions','d sufficiently large'])
    rel('C0151','large-degree-gap-conditional-refutation','fiid-independent-density-thinning','cites')

    add('P0127','uniform-rooted-line-lattice-tree-sampler','lemma','Exact uniform rooted lattice-tree sampler on the line',
        'The n-vertex lattice trees in Z containing zero are exactly the n intervals [-L,n-1-L], L=0,...,n-1. Uniform L gives exact uniform rooted sampling using expected O(log n) unbiased random bits and a compact O(log n)-bit endpoint representation. Listing vertices takes O(n) word operations on an O(log n)-bit word RAM and O(n log n) bits of coordinate output. Trees modulo translation instead have one class.',['n positive integer','rooted trees containing zero','vertex count n','nearest-neighbor lattice Z','unbiased random bits','word RAM for the stated word-operation bound'])
    add('P0127','uniform-frontier-growth-tv-obstruction','lemma','Uniform frontier growth is biased at three vertices',
        'On Z^d, d>=1, grow a rooted tree from the origin by choosing uniformly from available boundary edges at each step. At three vertices the resulting distribution has total variation exactly 1/6 from the uniform rooted lattice-tree law. With D=2d there are 2D(D-1) equiprobable growth histories, but center-rooted trees have two histories and endpoint-rooted trees have one. This obstruction concerns this uncorrected growth rule.',['nearest-neighbor lattice Z^d','d>=1','rooted trees containing origin','two uniform frontier additions'])
    rel('P0127','uniform-frontier-growth-tv-obstruction','uniform-rooted-line-lattice-tree-sampler','analogous_to')

    add('P0456','k-one-matching-isolation-formula','lemma','Bilateral k=1 graph: exact isolation probability',
        'Give each edge of K_n one independent identically distributed continuous weight and retain it if both endpoints rank it among their single lowest incident weights. For n>=2 the graph is a matching, a fixed edge is present with probability 1/(2n-3), and a fixed vertex is isolated with probability (n-2)/(2n-3). The expected number of isolates is n(n-2)/(2n-3); connectivity is impossible for n>2.',['n>=2','one shared i.i.d. continuous weight per undirected edge','k=1'])
    add('P0456','no-isolates-finite-disconnection-obstruction','lemma','No isolates need not imply bilateral-preference connectivity',
        'In the same shared-weight bilateral model with n=6 and k=2, the event that all six edges inside two vertex triples precede all nine cross edges produces two disjoint triangles. It has probability 1/binomial(15,6)=1/5005, yet minimum degree is two. Thus absence of isolates is not a deterministic connectivity criterion. This finite event does not settle the asymptotic fine window.',['n=6','k=2','shared i.i.d. continuous edge weights'])
    rel('P0456','no-isolates-finite-disconnection-obstruction','k-one-matching-isolation-formula','analogous_to')

    add('C0058','nonsimple-boundary-colour-word-obstruction','lemma','A site-colour word does not retain boundary vertex identity',
        'For independent Bernoulli(p) site colours, 0<p<1, boundary incidence patterns [a,b,a,c] and [a,b,c,d] both initially have colour word UUUU but induce different occurrence-colour laws. After exposing occurrence zero as black, occurrence two is black with probability 1 in the first pattern and p in the second. The full-law total variation is 2p(1-p). Thus the word alone cannot determine transitions uniformly conditional on each full boundary configuration. Retain incidence identities or supply a valid averaging/lumping theorem; no impossibility of weak lumping for a particular process is asserted.',['independent colours on distinct vertices','0<p<1','general boundaries may repeat vertices','same unexposed word and length','configurationwise transition rule, without a proved averaging theorem'])
    add('C0058','bounded-faces-markov-iff-not-established','concept','Bounded face degree is not a demonstrated criterion for Markov peeling',
        'The prior claim that a Markov description of site-percolation peeling exists exactly for bounded face degrees is unsupported. Unbounded finite faces expose finitely many labels per step and allow larger states; bounded face degrees alone do not bound the accumulated boundary length. The proven correction here is only that nonsimple boundaries require vertex-identity information in addition to a colour word. No threshold or sufficient compressed state is established.',['finite degrees at each exposed face','general-boundary site-percolation exploration'])
    rel('C0058','bounded-faces-markov-iff-not-established','nonsimple-boundary-colour-word-obstruction','cites')

    add('C0082','degree-matched-square-six-cycle-counts','lemma','Exact square and six-cycle counts at equal lattice/cube degree',
        'Let D=2d. Unoriented simple cycles through a fixed vertex in Z^d have square count 4*binomial(d,2) and six-cycle count 12*binomial(d,2)+96*binomial(d,3). In Q_D the corresponding counts are binomial(D,2) and 12*binomial(D,3). Thus lattice-minus-cube differences are -D/2 for squares and -(9/2)D(D-2) for six-cycles. The graphs are compared at the same degree, not the same dimension.',['d positive integer','Q_D is the D-dimensional hypercube','cycles simple and unoriented','fixed root vertex','D=2d'])
    add('C0082','cycle-counts-do-not-certify-critical-coefficient','concept','The rectangle heuristic does not identify a critical expansion coefficient',
        'Lattice two-axis rectangles are absent from a hypercube, but at equal degree the hypercube has more total six-cycles. Therefore a comparison that counts only the extra lattice rectangles omits other subleading cycle-count changes. These exact counts do not identify the first distinct coefficient of the critical-probability expansions: lace-diagram weights, cancellation and the cube critical-parameter convention still require analysis. The earlier a_4 prediction remains a heuristic.',['bond-percolation critical expansion comparison','equal-degree cycle counting'])
    rel('C0082','cycle-counts-do-not-certify-critical-coefficient','degree-matched-square-six-cycle-counts','cites')

    add('C0126','underlying-walk-backward-steps','lemma','Undirected cluster walk can return despite oriented bonds',
        'Orient a diamond as 0->a,b->c and let simple random walk use its underlying undirected unit-edge graph. Its probability of returning to 0 at two steps is 1/2, although a forward-only walk has return probability zero. Thus bond orientation in oriented percolation does not justify forbidding backward steps in the undirected random-walk spectral-dimension problem.',['simple random walk uses the underlying undirected cluster','unit conductances','the four-edge diamond'])
    add('C0126','singleton-cutset-resistance-reduction','lemma','Separating singleton cuts give a deterministic resistance lower bound',
        'In a finite unit-conductance network between an origin and a target boundary, if m distinct singleton edge cuts separate them, effective resistance is at least m. Every unit flow has current of magnitude one through each cut edge, so its energy is at least m. More generally pairwise edge-disjoint separating cutsets C_j give the lower bound sum_j 1/|C_j|. This alone provides no random IIC bottleneck tail estimate.',['finite connected unit-conductance network','origin separated from wired target boundary','cutsets edge-disjoint','Thomson variational principle'])
    rel('C0126','singleton-cutset-resistance-reduction','underlying-walk-backward-steps','cites')

    add('P0014','circulant-theta-frequency-lp','lemma','Known Fourier LP for the Lovasz theta number, with even frequencies explicit',
        'For a simple undirected circulant graph on Z/nZ, let S contain one representative of each included unordered nonzero generator pair and m=floor(n/2). Its Lovasz theta number is n times the maximum z_0 subject to z_j>=0, sum_{j=0}^m z_j=1, and sum_{j=0}^m z_j*cos(2*pi*j*s/n)=0 for every s in S. Paired Fourier frequencies are aggregated; the zero and even-n self-inverse frequency remain unpaired. This is a rederivation of the LP already described in the cached 2025 source.',['simple undirected circulant graph','trace-one PSD primal theta convention','nonzero generator pairs'])
    add('P0014','fair-circulant-theta-exact-small-expectations','lemma','Exact small expected theta values for fair random circulants',
        'Include every unordered nonzero generator pair of Z/nZ independently with probability 1/2. Expected Lovasz theta is 3/2 for n=2, 2 for n=3, 9/4 for n=4, and (3+sqrt(5))/2 for n=5. At n=4 the four theta values are 4,2,2,1; at n=5 they are 5,sqrt(5),sqrt(5),1. These finite values do not establish the conjectured large-n asymptotic.',['fair independent inclusion of unordered nonzero generator pairs','n in {2,3,4,5}'])
    add('P0014','log-theta-tail-reduction','lemma','A necessary log-variance condition and a sufficient MGF route',
        'For fair random circulants on n vertices set Z=log(theta(G)/sqrt(n)). Vertex transitivity and complement symmetry give E theta(G)/sqrt(n)=E cosh(Z)>=1+E[Z^2]/2. Hence asymptotic expectation ratio one requires E[Z^2]->0. If also E exp(Z)<=exp(sigma_n^2/2) with sigma_n->0, that expectation ratio tends to one. The latter MGF bound is a sufficient hypothesis, not a bound proved for the random graph here.',['vertex-transitive complement theta identity','complement-invariant fair model','MGF hypothesis for the sufficient direction only'])
    add('P0014','small-circulant-numerical-lp-evidence','concept','Sixty numerical circulant-theta LP checks',
        'Double-precision Fourier LP enumeration for all 60 fair-generator configurations on n=2,...,9 agrees with the exact n=2,...,5 expectations. Maximum equality residual was 1.1102230246251565e-15 and maximum theta-complement product discrepancy was 8.881784197001252e-15. These are numerical solver checks, not rational feasibility certificates and not proof of a large-n limit.',['the saved n=2,...,9 floating-point LP outputs'])
    rel('P0014','fair-circulant-theta-exact-small-expectations','circulant-theta-frequency-lp','depends_on')
    rel('P0014','small-circulant-numerical-lp-evidence','circulant-theta-frequency-lp','cites')
    rel('P0014','log-theta-tail-reduction','fair-circulant-theta-exact-small-expectations','analogous_to')

    add('P0042','tree4-two-neighbor-bootstrap-critical-boundary','lemma','Two-neighbor bootstrap on the four-regular tree: infimum and boundary',
        'For Bernoulli initial infection probability p on the four-regular tree, two-neighbor bootstrap has complete occupation almost surely for p>1/9 and fails almost surely for p<=1/9. Thus the complete-occupation critical infimum is 1/9. At p=1/9 the probability a specified root remains vacant is 21/32. Directed vacancy messages converge to the largest solution x=q(3x^2-2x^3), q=1-p; the critical largest solution is x=3/4 at q=8/9. This is a tree special case, not the general group characterization.',['four-regular infinite tree','two-neighbor bootstrap','independent Bernoulli initial infections','complete occupation on the infinite graph'])
    add('P0042','bootstrap-critical-endpoint-comparison','concept','Tree bootstrap infima need their own endpoint check',
        'Two-neighbor bootstrap on the three-regular tree completes almost surely at its critical infimum p=1/2, whereas on the four-regular tree it fails at its critical infimum p=1/9. The latter has positive critical residual vacancy 21/32 at the root. A critical threshold specified as an infimum therefore does not automatically assert occupation at the threshold itself.',['the three- and four-regular tree Bernoulli models'])
    rel('P0042','bootstrap-critical-endpoint-comparison','tree4-two-neighbor-bootstrap-critical-boundary','cites')

    status={
      'P0288':'The supplied campaign already contains a candidate refutation of the rank-one polynomial-limit assertion for a lambda-transient killed chain. Its source and formula were rechecked here; independent audit and novelty remain unverified. Foley-McDonald arXiv:1709.07578v1 is a prior-art lead, not an established identification with this continuous-time example.',
      'C0034':'Lyons arXiv:1406.2707 (2014), Question 2.8, asks whether orthogonal projection laws can be coupled with their union having the summed projection law. The supplied caches give no later general disposition. This packet proves rank-one-summand special cases and supplies eight exact higher-rank examples; the general question remains unresolved here.',
      'C0151':'Pete Conjecture 14.16 historically asks whether independent-set densities on random d-regular graphs equal factor-of-i.i.d. independent-set densities on the d-regular tree. The supplied ranking and C0151-A001 record a large-d refutation attributed to Rahman-Virag and Ding-Sly-Sun, but those primary answer papers were not verified here. The thinning endpoint correction is independently proved; current literature classification stays a lead pending source review.',
      'P0127':'Schramm (2006v2), Problem 2.9, asks for efficient approximate uniform sampling of n-vertex lattice trees containing the origin. The supplied prior attempt only gives inefficient enumeration. This packet solves the line special case and disproves uncorrected uniform frontier growth; general higher-dimensional status is unresolved from the supplied caches.',
      'P0456':'Dabirian-Subramanian (cached 2025 version) establish a first-order logarithmic connectivity threshold for shared-weight bilateral preference graphs, while their introductory Open Problems leave a finer window. The supplied cache contains no later answer. The finite calibrations here establish no window width or limiting connectivity law.',
      'C0058':'Curien, Peeling random planar maps (cached 2019 notes), asks for useful site-percolation peeling leading to threshold computation. This packet proves a necessary vertex-identity correction for nonsimple boundaries. It supplies neither that threshold nor a sufficient compressed exploration process; later literature status is unverified.',
      'C0082':'Heydenreich-van der Hofstad, Open Problem 15.9, asks for the first difference between lattice and cube critical-probability expansion coefficients after the first three agree. Exact short-cycle counts here correct an earlier heuristic but do not determine that index; later literature status is unverified.',
      'C0126':'Kumagai Section 6.3 asks for random walk on oriented-percolation IIC in spatial dimensions five and six; its displayed mean-field resistance proof needs dimension greater than six. This packet corrects the walk convention and gives a deterministic cutset reduction. Neither the needed random estimates nor a later answer were established.',
      'P0014':'Randomstrasse101 (2025), Conjecture 18, asks whether fair random circulants have expected theta asymptotic to sqrt(n). Its cached source already knows the Fourier LP and cites Bandeira et al., arXiv:2502.16227, for a partial bound. This packet rederives that reduction, proves small expectations and states a tail criterion; it does not resolve the asymptotic conjecture.',
      'P0042':'Lyons-Peres (19 August 2026 cached version), Question 7.42, asks whether endpoint-only bootstrap thresholds for every finite generating set characterize amenable groups. Four-regular-tree calculations here are standard special cases with explicit critical vacancy. They do not settle all generating sets or the group characterization.'}
    for pid in IDS:
        add(pid,'source-limited-status-20261010','concept','Source-limited status and scope for '+pid,status[pid],['only the supplied local caches and prior records were consulted','independent review pending'])
        for e in entries[pid]:
            if e['key']!='source-limited-status-20261010':
                rel(pid,e['key'],'source-limited-status-20261010','cites')
        if targets[pid]:
            cross(pid,'source-limited-status-20261010',targets[pid][0])
    for pid,needle,key,quoted,note in [
        ('C0058','attempt-c0058','nonsimple-boundary-colour-word-obstruction','The frontier becomes Markov if one records the boundary word','This refutes that compression when boundary occurrences may repeat a vertex; it makes no threshold claim.'),
        ('C0126','attempt-c0126','underlying-walk-backward-steps','paths in the oriented IIC cannot return to earlier times','This refutes its use as a prohibition on backward steps of the underlying undirected random walk, not the definition of a directed percolation path.')]:
        matches=[x for x in oldcards[pid] if needle in str(x.get('logical_id'))]
        if matches:
            assert quoted in matches[0]['body']
            cross(pid,key,matches[0],'refutes',quoted,note)

    con=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
    allcross={r['to_existing_logical'] for rs in relations.values() for r in rs if 'to_existing_logical' in r}
    for logical in allcross:
        assert con.execute("SELECT 1 FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=? LIMIT 1",(logical,)).fetchone(),logical
    con.close()
    draftdir=ROOT/'drafts'; draftdir.mkdir(exist_ok=True)
    livefiles=[]; rows=[]; claims=[]
    for no,pid in enumerate(IDS,1):
        bundle={'spec':'mathbrain-draft-v1','author_agent':'w341','bundle_slug':'w341-'+pid.lower()+'-checked-results-20261010','entries':entries[pid],'relations':relations[pid]}
        for e in entries[pid]:
            assert e['kind'] in ('definition','lemma','theorem','concept')
            assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
            assert e['proof_text'] if e['kind'] in ('lemma','theorem') else e['proof_text'] is None
            assert e['statement'] and e['source']['license'].startswith('owner-own-work')
        dep=defaultdict(list)
        for r in relations[pid]:
            assert r['from_key'] in {e['key'] for e in entries[pid]}
            assert '\n' not in r['rationale']
            if 'to_key' in r:
                assert r['to_key'] in {e['key'] for e in entries[pid]}
                if r['kind']=='depends_on': dep[r['from_key']].append(r['to_key'])
        def visit(k,path):
            assert k not in path,'cyclic dependency'
            for nxt in dep[k]: visit(nxt,path|{k})
        for k in list(dep): visit(k,set())
        file=draftdir/('bundle_'+str(no).zfill(3)+'.json')
        dump(file,bundle)
        livefiles.append(('math-brain-inbox/w341/'+file.name,file))
        for e in entries[pid]:
            label='proof' if e['kind'] in ('lemma','theorem') else 'definition' if e['kind']=='definition' else 'source-limited record or evidence'
            rows.append({'row_id':'S1.O.w341.'+pid+'.'+e['key'],'problem':pid,'label':label,'kind':e['kind'],'statement':e['statement'],'proof_or_report':str(ROOT/'proofs'/(NAMES[pid]+'.md')),'measurements':str(ROOT/'measurements'/(pid+'.json')),'bundle':str(file),'audit_status':'PENDING w347','counted_keeps':0})
            claims.append({'problem':pid,'key':e['key'],'kind':e['kind'],'claim':e['statement'],'assumptions':e['assumptions'],'audit_status':'PENDING w347'})
    patch_additions('01_math_brain_bundles.diff',livefiles)
    proposals=[
       {'id':'open-status-w341-01','area':'math','event':'stage-start','cue':'A new solution or novelty claim is about to be made for a named open problem','fire_when':'About to call a candidate proof a new solution of a named conjecture','silent_when':'Reproducing a known special case with no novelty claim','text':'Check the problem status and prior attempts before verifying novelty. A correct proof and a new proof are different claims; cached status stays dated.','evidence':'memory:verify_the_problem_is_open_before_you_verify_the_proof_2026_09_07; proofs/P0288_recheck.md; proofs/P0014_fourier.md','proposer':'w341'},
       {'id':'exact-certificate-w341-02','area':'math','event':'PostToolUse','cue':'Floating-point LP output is being described as an exact feasibility certificate','fire_when':'HiGHS reports zero residual and the result is about to be labelled exact','silent_when':'A rational point has been independently replayed with all marginals exactly correct','text':'A float LP can propose a support. Before calling it exact, check a rational point for nonnegative masses and every required marginal.','evidence':'measurements/C0034.json: 64 rational replays; measurements/C0034_higher_rank_summary.json: 8 rational replays, residual exactly 0','proposer':'w341'},
       {'id':'boundary-identity-w341-03','area':'math','event':'stage-start','cue':'A colour-word-only site-percolation state is proposed without identities, simplicity or a proved averaging theorem','fire_when':'Compressing a nonsimple site boundary to its colour word without retaining identities or proving an averaging theorem','silent_when':'A simple boundary is proved, identities are retained, or a valid averaging theorem supplies the reduced law','text':'Site colours belong to vertices. Repeated boundary occurrences share a label; retain incidence identities or prove a valid averaging theorem before claiming a reduced Markov state.','evidence':'measurements/C0058.json: identical UUUU states have colour-law TV 1/2 at p=1/2','proposer':'w341'},
       {'id':'logical-id-field-w341-04','area':'brain','event':'PreToolUse','cue':'A logical store target is resolved by substring search over the full metadata_json','fire_when':'Using metadata_json LIKE %c0151% to identify a problem card','silent_when':'Querying the logical_id field and verifying the exact target','text':'Resolve a store edge through the logical_id field. Full-metadata substring searches can match hashes; confirm the target identity before writing an edge.','evidence':'reports/metadata_substring_false_matches.json: all 3 first matches were false logical targets','proposer':'w341'}]
    hp=ROOT/'proposals'/'math-w341.jsonl'; hp.parent.mkdir(exist_ok=True)
    with hp.open('w',encoding='utf-8') as f:
        for proposal in proposals:
            assert len(proposal['text'])<=300
            f.write(json.dumps(proposal,ensure_ascii=False)+'\n')
    patch_additions('02_hook_proposals.diff',[('primary_directive/hooks1000/proposals/math-w341.jsonl',hp)])
    with (ROOT/'READY_ROWS.jsonl').open('w',encoding='utf-8') as f:
        for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    # Preserve the initial rows and append only previously unseen result ids.
    rp=ROOT/'RESULTS.jsonl'
    previous={json.loads(line)['row_id']:json.loads(line) for line in rp.read_text(encoding='utf-8').splitlines() if line}
    with rp.open('a',encoding='utf-8') as f:
        for row in rows:
            if row['row_id'] not in previous:
                f.write(json.dumps(row,ensure_ascii=False)+'\n')
            elif previous[row['row_id']]['statement']!=row['statement']:
                revision={**row,'row_id':row['row_id']+'.v2','supersedes_row':row['row_id'],'revision_reason':'Statement hypotheses or scope tightened before independent audit.'}
                if revision['row_id'] not in previous:f.write(json.dumps(revision,ensure_ascii=False)+'\n')
    dump(ROOT/'CLAIMS_FOR_BLIND_AUDIT.json',claims)
    exitdata=json.loads((ROOT/'measurements'/'lean_cut_exit.json').read_text(encoding='utf-8'))
    raw=(ROOT/'measurements'/'lean_cut_receipt.json').read_text(encoding='utf-8')
    try: lean=json.loads(raw)
    except json.JSONDecodeError:
        (ROOT/'measurements'/'lean_cut_stdout.txt').write_text(raw,encoding='utf-8')
        lean={'status':'SETUP_UNVERIFIED','stdout':raw,'exit_code':exitdata['exit_code'],'compiler_launched':False}
        dump(ROOT/'measurements'/'lean_cut_receipt.json',lean)
    summary={'agent':'w341','problems':len(IDS),'bundles':len(IDS),'typed_nodes':len(rows),'edges':sum(map(len,relations.values())),'resolved_cross_targets':len(allcross),'hook_proposals':len(proposals),'passed_experiment_batches':sum(r['status']=='PASS' for r in metrics.values()),'exact_coupling_certificates':metrics['C0034']['after_exact_certificates']+higher['after_exact_higher_rank_certificates'],'exact_higher_rank_certificates':higher['after_exact_higher_rank_certificates'],'main_check_seconds':round(sum(r['seconds'] for r in metrics.values()),3),'higher_rank_check_seconds':higher['seconds'],'lean':lean.get('status',lean.get('result',{}).get('status')),'independent_keeps':0,'live_nodes_ingested':0,'test_material_accessed':False,'explicit_deliverables_outside_worker_folder':0,'account_cost':'not available in task tools; no figure invented','next':'w347 blind-audit the claims and replay certificates; reviewer apply only kept bundles from the local deployment patch.'}
    dump(ROOT/'measurements'/'package_summary.json',summary)
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':main()
