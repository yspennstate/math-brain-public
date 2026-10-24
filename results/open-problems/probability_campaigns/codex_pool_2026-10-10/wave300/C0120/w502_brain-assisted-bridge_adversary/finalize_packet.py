"""Build only w502 reports and explicitly authorized draft/proposal files.

No live store, global control or code is changed; no integrator is invoked.
"""
from pathlib import Path
import difflib
import hashlib
import json
import os

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w502')
SOURCE_URL = 'https://arxiv.org/pdf/0810.4221v2'

def read(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))
def write(name,data):
    (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()

cards=read('brain_cards.json')['hits']+read('exact_bridge_cards.json')['hits']
by_id={x['id']:x for x in cards}
target=next(x for x in cards if x['title'].startswith('Open problem: Fluctuation exponent'))
cube=next(x for x in cards if x['title'].startswith("Talagrand's L1-L2"))
ou=next(x for x in cards if x['title']=='The Ornstein-Uhlenbeck Semigroup and Mehler\'s Formula')

entries=[]
def entry(key,name,title,statement,assumptions,kind='concept'):
    e={'key':key,'namespace':'probability.gaussian','logical_name':name,'kind':kind,
       'title':title,'statement':statement,'proof_text':None,'assumptions':assumptions,
       'domain':'directed polymers and Gaussian concentration',
       'source':{'source_id':'owner-campaign:w502:C0120:'+key,'url':(ROOT/'ATTEMPT.md').as_uri(),
                 'revision':'2026-10-10 author-derived draft; referee pending; see w502/ATTEMPT.md',
                 'license':'owner-own-work (campaign proof and source-caveat, not source prose reproduced)',
                 'excerpt':None}}
    entries.append(e)
    return e

model=entry('model','gaussian-directed-polymer-free-endpoint-source-model',
 'Gaussian directed-polymer maximum: exact C0120 source model',
 'In Chatterjee 0810.4221v2 Section 8, a path p has n vertices in Z^2_+, starts at (0,0), and takes right/up unit steps with final endpoint unrestricted on i+j=n-1. With independent standard Gaussian vertex weights g_v, X_p=sum_{v in p}g_v and M_n=max_p X_p. Distinct path sums tie with probability zero. Each path has variance n and Cov(X_p,X_q)=|p intersection q|. This is the zero-temperature Gaussian maximum; log Z at fixed finite inverse temperature is a different observable. Theorem 8.1 gives Var(M_n)<=C n/log n for n>=2. No current-openness conclusion is asserted.',
 ['n>=2','independent standard Gaussian vertex weights','right/up steps','origin start','free endpoint'], 'definition')
bridge=entry('ou-rate','directed-polymer-polynomial-ou-overlap-rate-reduction-draft',
 'DRAFT: exact polynomial OU-overlap to variance reduction',
 'AUTHOR-DERIVED DRAFT, referee pending. For the preceding Gaussian path model, set g^t=e^{-t}g+sqrt(1-e^{-2t})g\' with independent g\', and Q_n(t)=E|P_n(g) intersection P_n(g^t)|. Var(M_n)=integral_0^infinity e^{-t}Q_n(t)dt; Q_n is nonnegative, nonincreasing, Q_n(0)=n. Thus (1-e^{-h})Q_n(h)<=Var(M_n)<=n(1-e^{-h})+e^{-h}Q_n(h). If Q_n(n^{-a})<=K n^{1-b} for fixed a,b in (0,1) and K uniform in n, then Var(M_n)<=(1+K)n^{1-min(a,b)}. Conversely a bound K n^{1-delta} on variance gives Q_n(n^{-a})<=2K n^{1-delta+a} for 0<a<delta. None of these conclusions establishes the assumed power overlap bound. OU time h has noise amplitude of order sqrt(h).',
 ['the exact source model','unique Gaussian maximizer','fixed positive exponents','constants uniform in n'])
gap=entry('missing-rate','gaussian-polymer-polynomial-overlap-loss-missing-premise',
 'DRAFT missing premise: overlap loss at polynomial OU time',
 'UNPROVED MISSING PREMISE, not a theorem: establish fixed a,b in (0,1), K<infinity and n0 such that for every n>=n0, Q_n(n^{-a})<=K n^{1-b} in the exact Gaussian directed-polymer source model. Known Q_n(t)<=C n/((1-e^{-t})log n) is only the trivial bound n at t=n^{-a} for fixed a>0. Qualitative chaos at a logarithmic time and logarithmic variance savings do not prove this premise. The gap is joint optimal-path geometry beyond the one-site hypercontractive certificate; parent C0120 remains unsolved.',
 ['same source model and OU convention','a,b,K,n0 cannot depend on n'])
beta=entry('beta-transfer','finite-path-softmax-maximum-standard-deviation-comparison-draft',
 'DRAFT: finite-temperature to maximum variance comparison',
 'AUTHOR-DERIVED DRAFT, referee pending. For a nonempty finite path set P and square-integrable real energies X_p, beta>0, M=max_p X_p and F_beta=beta^{-1}log(sum_p exp(beta X_p)), put A=log(|P|)/beta. Then 0<=F_beta-M<=A and |sqrt(Var(F_beta))-sqrt(Var(M))|<=A/2. Proof: D=F_beta-M lies in [0,A], so Var(D)<=A^2/4; apply the reverse triangle inequality to centered L2 norms. For the source paths, A=(n-1)log(2)/beta. To transfer an O(n^{1-epsilon}) bound by this comparison it suffices to have beta(n)>=c n^{(1+epsilon)/2} and a variance constant uniform along beta(n). A theorem at fixed beta with arbitrary C(beta) does not supply that uniform premise. This is a limitation of this comparison, not a necessity claim for the actual model.',
 ['finite nonempty path family','all X_p square integrable','beta>0','unnormalized partition sum'])
norm=entry('indicator-caveat','talagrand-rare-indicator-magnitude-norm-ratio-caveat-draft',
 'DRAFT correction: rare indicator derivatives do gain in L1-L2',
 'AUTHOR-DERIVED DRAFT CAVEAT, referee pending. If |D|=c*1_A, c>0, P(A)=p in (0,1], then ||D||_1=cp and ||D||_2=c*sqrt(p), so ||D||_2/||D||_1=p^{-1/2}. The Talagrand denominator 1+log(||D||_2/||D||_1) is 1+(1/2)log(1/p), greater than one for p<1. A valid cube example is f(x)=x_1*1{x_2=x_3=1} on uniform {-1,1}^3: Delta_1 f=x_1*1{x_2=x_3=1}, norms 1/4 and 1/2. This refutes only the existing card explanatory no-gain clause for an indicator in magnitude; its displayed cube variance inequality is retained. Cube-flip derivatives do not directly apply to continuous Gaussian weights; obtain a Gaussian theorem with matching hypotheses.',
 ['0<p<=1','c>0','for the example: uniform discrete cube','Delta_i f=(f(x)-f(x flipped at i))/2'])
scope=entry('source-caveat','c0120-gaussian-maximum-versus-log-partition-source-scope-caveat',
 'DRAFT source caveat: C0120 finite-temperature attribution',
 'SOURCE-SCOPE CORRECTION DRAFT, independent source review pending. The C0120 intake and stored open-problem card cite Chatterjee 0810.4221v2 Section 12(3) while stating a general-dimensional finite-temperature Var(log Z_n) target. The cited paper Section 8 actually studies the (1+1)-dimensional Gaussian free-endpoint zero-temperature maximum M_n and Theorem 8.1 bounds its variance by C n/log n. Section 12(3) asks to improve its fluctuation exponent. The finite-temperature general-dimensional formulation is related research and needs separate sources and model assumptions, such as 1204.1819 or 2103.09199. Neither a solution nor present-day openness follows from the dated intake. Current openness UNKNOWN.',
 ['primary version 0810.4221v2','a citation-fidelity caveat, not a refutation of the research target'])

relations=[
 {'from_key':'ou-rate','to_key':'model','kind':'depends_on','rationale':'The overlap/variance identity uses exactly this Gaussian maximum and path-indicator gradient.'},
 {'from_key':'missing-rate','to_key':'ou-rate','kind':'depends_on','rationale':'The unproved overlap rate is the hypothesis of the quantitative reduction.'},
 {'from_key':'beta-transfer','to_key':'model','kind':'semantic_association','rationale':'The general finite-family comparison specializes numerically to 2^(n-1) source paths, without asserting temperature-uniform estimates.'},
 {'from_key':'source-caveat','to_key':'model','kind':'cites','rationale':'The exact source model explains the mismatch.'},
 {'from_key':'source-caveat','to_existing_logical':target['metadata']['logical_id'],'kind':'semantic_association','rationale':'Caveat only: this old card has a log Z/general-dimension attribution that does not match the named 2008 source; the open target is not refuted.'},
 {'from_key':'indicator-caveat','to_existing_logical':cube['metadata']['logical_id'],'kind':'semantic_association','rationale':'Correct the no-gain-for-indicator explanatory clause only. Retain the cube inequality and its assumptions.'},
 {'from_key':'ou-rate','to_existing_logical':ou['metadata']['logical_id'],'kind':'depends_on','rationale':'Mehler semigroup standard-Gaussian normalization and L2 self-adjointness underpin the independent overlap reduction.'},
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w502','bundle_slug':'c0120-source-and-bridge-caveats-w502-001','entries':entries,'relations':relations}
text=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
(ROOT/'bundle_001.json').write_text(text,encoding='utf-8')
INBOX.mkdir(parents=True,exist_ok=True)
part=INBOX/'bundle_001.json.part'
final=INBOX/'bundle_001.json'
if final.exists() and final.read_text(encoding='utf-8') != text:
    raise RuntimeError('Existing w502 bundle differs; refusing overwrite')
if not final.exists():
    part.write_text(text,encoding='utf-8')
    os.replace(part,final)

# The additive patch is provenance for the submitted draft, never a SQLite patch.
(ROOT/'patches').mkdir(exist_ok=True)
live=str(final).replace('\\','/')
diff=''.join(difflib.unified_diff([],text.splitlines(keepends=True),fromfile='a/'+live,tofile='b/'+live))
(ROOT/'patches/01_c0120_draft.diff').write_text(diff,encoding='utf-8')

ends={e['key']:e['statement'] for e in entries}
edges=[]
for i,r in enumerate(relations,1):
    old=next((x for x in cards if x['metadata'].get('logical_id')==r.get('to_existing_logical')),None) if 'to_existing_logical' in r else None
    edges.append({'id':f'C0120-W502-E{i:02d}','relation':r,'from_quote':ends[r['from_key']],
                  'to_quote':old['body'] if old else ends[r['to_key']],
                  'target_card_id':old['id'] if old else None,'status':'draft; independent review pending',
                  'reviewer':'w503','submitted':True,'ingested':False,'retrievable':False})
(ROOT/'EDGE_EVIDENCE.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in edges),encoding='utf-8')

intake=read('intake_records.json')
record=intake['sources.jsonl'][0]
source_dir=Path('~/Downloads/Probability_1000_intake_claude_20260907/sources/chatterjee_chaos_2008')
checks=[]
for file,field in [('source.pdf','sha256'),('text.txt','extracted_sha256')]:
    p=source_dir/file
    actual=sha(p)
    checks.append({'path':str(p),'sha256':actual,'intake_sha256':record[field],'match':actual==record[field]})
proof=Path('~/brain_workers/w501/LEMMAS.md')
proof_bytes=proof.read_bytes()
(ROOT/'REVIEWED_W501_LEMMAS.md').write_bytes(proof_bytes)
proof_hash=hashlib.sha256(proof_bytes).hexdigest()

write('SOURCE_STATUS.json',{
 'target':'C0120','current_openness':'UNKNOWN','parent_problem_solved':False,
 'exact_statement_recovered':True,'canonical_model':model['statement'],
 'exact_target':'Find epsilon>0 and C,n0 independent of n such that Var(M_n)<=C n^(1-epsilon) for every n>=n0 in the cited Gaussian source model.',
 'intake_model_status':'Related finite-temperature/general-dimensional formulation; not a faithful exact restatement of its 2008 citation.',
 'sources':[{'url':SOURCE_URL,'version':'v2, 2008-12-16','locators':['Section 8','Theorem 3.2','Theorem 8.1','Section 12(3)'],'checks':checks},
            {'url':'https://arxiv.org/abs/1204.1819','scope':'Finite-temperature near-gamma i.i.d. environment; abstract checked only.'},
            {'url':'https://arxiv.org/html/2103.09199v2','scope':'Section 2.4: fixed-beta point-to-plane polymer, Gaussian-Lipschitz pushforward disorder; C depends on d,beta,law.'}],
 'prior_work_checks':{'intake_and_attempt':'exact C0120 records saved','ranking':'tier 5 historical row recovered','lean':'annotated C0120 row; no theorem receipt located',
 'attempts_H_I':'targeted C0120 search returned no proof','team_O':'no C0120 row from scoped board query','owner_solved_retired':'targeted relevant README returned no matching polymer variance solution; completeness not claimed'},
 'recent_primary_search':'Checked public arXiv search for directed-polymer variance/polynomial superconcentration in 2025/2026; no scoped resolution certified. Search incompleteness preserves UNKNOWN.',
 'paired_proof_read':True,'paired_proof':{'path':str(proof),'sha256':proof_hash,'snapshot':'REVIEWED_W501_LEMMAS.md'},
 'served_model_evidence':{'author_w502':'UNAVAILABLE','paired_author_w501':'UNAVAILABLE','referee_w503':'UNAVAILABLE','requested_settings_are_not_evidence':True},
 'formal_check':{'performed':False,'receipt':None,'trusted_axioms':None},
 'review_state':'w503 pending; no theorem promotion or live-store edit'
})

exact=read('exact_check.json')
hook={'id':'math-talag-indicator-w502-01','area':'math','event':'stage-start',
 'cue':'Applying Talagrand L1-L2 while claiming an indicator-like derivative has no logarithmic gain',
 'fire_when':'Returned card claims no gain for Delta_1 f=x_1*1{x_2=x_3=1}; exact L2/L1 is 2.',
 'silent_when':'Derivative has constant magnitude almost surely (p=1), or no Talagrand norm-ratio inference is being made.',
 'text':'For |D|=c*1_A with P(A)=p, L2/L1=p^(-1/2). Rare indicators do gain in Talagrand L1-L2. State the measure and derivative convention; a discrete-cube theorem needs a separate Gaussian analogue.',
 'evidence':'~/brain_workers/w502/exact_check.json: eight cube points, L1=0.25, L2=0.5, denominator=1.6931471805599454; card claim_19af561bcf040b56cc9b3aa80d52d5dd62e1e00c1b7ecb97b574cbacb19b5603',
 'proposer':'w502'}
assert len(hook['text'])<=300
hook_line=json.dumps(hook,ensure_ascii=False)+'\n'
(ROOT/'hook_proposal.jsonl').write_text(hook_line,encoding='utf-8')
hp=Path('~/primary_directive/hooks1000/proposals/math-talag-indicator-w502.jsonl')
if hp.exists() and hp.read_text(encoding='utf-8') != hook_line:
    raise RuntimeError('Existing hook proposal differs; refusing overwrite')
if not hp.exists():
    hp.write_text(hook_line,encoding='utf-8')

packet={
 'packet_id':'C0120-w502-20261010','author_agent':'w502','reviewer':'w503','integration_contact':'codex-01a12190',
 'scoped_keep':'w501 L1-L4 as explicitly conditional source consequences, method obstruction and exponent arithmetic; see PAIR_AUDIT.md.',
 'hardest_gap':'Polynomial overlap loss at polynomially small OU time in actual nearest-neighbor Gaussian paths.',
 'own_pending_checks':['L02: precise OU rate reduction','L03: finite-beta/max standard-deviation comparison','L04: rare-indicator norm calculation','S01: source-citation caveat'],
 'bundle_path':str(final),'nodes':len(entries),'relations':len(relations),
 'lifecycle':{'prepared':True,'submitted':True,'reviewed':False,'ingested':False,'retrievable':False},
 'different_model_gate':'NOT SATISFIED: response-side served-model evidence unavailable; do not promote.',
 'proof_snapshot_sha256':proof_hash,'source_hash_checks':checks,
 'measurements':{'brain_recall_timeout_seconds':60,'memories_returned':0,
                  'scoped_export_elapsed_seconds':read('brain_cards.json')['elapsed_seconds'],
                  'scoped_sql_elapsed_seconds':read('exact_bridge_cards.json')['elapsed_seconds'],
                  'sql_speedup_claim':False,'different_queries_not_a_controlled_benchmark':True,
                  'cube_norm_ratio':exact['norm_ratio'],'cube_denominator':exact['talagrand_denominator'],
                  'live_improvement_claim':False},
 'next':'w503 independently check L03/L04 and source scope; coordinator reconcile with w501 packet, then ingest only approved concepts.'
}
write('review_packet.json',packet)
print(json.dumps({'submitted':str(final),'nodes':len(entries),'relations':len(relations),'proof_sha256':proof_hash,'source_hash_checks':checks,'hook':str(hp),'status':'DRAFT; review pending'},ensure_ascii=False))
