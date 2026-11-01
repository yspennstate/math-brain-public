"""Build eight small, unreviewed concepts/definitions; never touch a store."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = {'source_id':'owner-probability300-w579-C0044-20261010',
          'url':'file:///~/brain_workers/w579/ATTEMPT.md',
          'revision':'author-draft-2026-10-10-v1',
          'license':'owner-own-work (campaign derivation, independent review pending)',
          'excerpt':None}
setup = ['Static nearest-neighbor RWRE on Z^d with displacement set E={+/-e_i}',
         'P is stationary and ergodic under the full lattice shift group',
         'Every allowed transition omega(x,e) is strictly positive P-almost surely',
         'The annealed walk starts at 0; ell is a fixed nonzero real direction',
         'T_x omega(y,e)=omega(x+y,e)']

def entry(key,name,title,statement,assumptions,kind='concept'):
    return {'key':key,'namespace':'probability.randomenvironment',
            'logical_name':name,'kind':kind,'title':title,
            'statement':statement,'proof_text':None,'assumptions':assumptions,
            'domain':'probability theory','source':dict(source)}

entries = [
 entry('c0044-target','c0044-directional-zero-one-target-status-20261010',
  'C0044: exact directional zero-one target; current status unknown',
  'DRAFT SOURCE-STATUS NOTE, 2026-10-10. For d>=3, iid transition probability rows omega(x,.) on {+/-e_i}, all components strictly positive almost surely, and a fixed nonzero ell in R^d, the target is P_0(X_n dot ell tends to +infinity) in {0,1}. P_0 averages over the environment sampled once and the walk from 0. Uniform ellipticity, speed and simultaneous uncountable-direction conclusions are not assumed. Drewitz-Ramirez Open Question 3.2 is the intake source; Zerner arXiv:0706.0745v1 recovers the model. A newer public formalization scope claims a solution, but this packet has no implementation theorem/axiom receipt. Current openness UNKNOWN; no new-solution claim.',
  ['d>=3','IID strictly elliptic transition rows','Fixed direction ell!=0']),
 entry('uncertainty','quenched-directional-escape-uncertainty',
  'Quenched directional escape uncertainty',
  'For a static nearest-neighbor environment omega and fixed nonzero ell, define A_ell={X_n dot ell tends to +infinity}, h(omega)=P_{0,omega}(A_ell), p=E_P h, and u(omega)=h(omega)(1-h(omega)). The quantity u is uncertainty about directional escape in the fixed environment. Define eta_n=T_{X_n}omega and F_n as the sigma-field containing the entire environment and the path X_0,...,X_n. The filtration reveals the whole environment already at time zero. These definitions do not assume h is local, translation invariant, or independent of the walked path.',
  setup,kind='definition'),
 entry('reverse-density','reverse-occupation-density-for-environment-seen-from-walk',
  'Draft: finite-time reverse occupation density',
  'UNREVIEWED AUTHOR DERIVATION. Under a stationary environment law P, the annealed law mu_n of eta_n=T_{X_n}omega has density f_n(omega)=sum_{x in Z^d} P_{-x,omega}(X_n=0). Only |x|_1<=n contributes. E_P f_n=1, f_0=1, and f_{n+1}(omega)=sum_e omega(-e,e)f_n(T_{-e}omega). The density follows by translation of each endpoint term; it is generally not one. Finite-time absolute continuity does not imply a uniformly controlled density as n grows.',
  [setup[0],setup[4],'P is stationary under every lattice shift','The annealed walk starts at 0']),
 entry('ui-criterion','directional-zero-one-under-uniform-integrability-subsequence',
  'Draft restricted theorem: a density UI subsequence gives directional zero-one',
  'UNREVIEWED RESTRICTED RESULT. Let h=P_{0,omega}(A_ell), eta_n=T_{X_n}omega, f_n=dLaw(eta_n)/dP, and bar_f_N=N^-1 sum_{n<N} f_n. If either {f_{n_k}} for n_k->infinity or {bar_f_{N_k}} for N_k->infinity is uniformly integrable in L1(P), then P_0(A_ell) is zero or one. A uniform L^r bound with r>1, or a uniform relative entropy bound on the respective subsequence, is sufficient. This is not an equivalence, and the author has not derived the UI assumption from IID and strict ellipticity. The proof combines u=h(1-h)>0 under a mixed probability with integral u f_n dP->0 and uniform absolute continuity.',
  setup+['The specified subsequence is uniformly integrable with respect to P']),
 entry('density-obstruction','mixed-directional-escape-forces-density-and-entropy-divergence',
  'Draft: quantitative density concentration forced by mixed escape',
  'UNREVIEWED AUTHOR DERIVATION. Let p=P_0(A_ell), h=P_{0,omega}(A_ell), u=h(1-h), f_n=dLaw(T_{X_n}omega)/dP, and bar_f_N=N^-1 sum_{n<N}f_n. If 0<p<1, then u>0 P-a.s., D_n=integral u f_n dP->0, and m_N=integral u bar_f_N dP->0. For g=f_n or bar_f_N, a=integral u g dP, delta_t=P(u<=t) with 0<delta_t<1, b=max(1-a/t,0), and r>1: ||g||_r>=b delta_t^{-(1-1/r)}, and integral g log g dP>=b log(1/delta_t)-log 2. Thus both finite-time and Cesaro L^r norms and relative entropies tend to infinity. These implications do not exclude the mixed probability under IID; that missing step is separate.',
  setup+['Hypothetical mixed directional probability 0<p<1','Natural logarithm; 0 log 0=0']),
 entry('hard-gap','c0044-reverse-density-route-hardest-gap',
  'C0044 draft route: the density concentration gap',
  'UNPROVED BRIDGE GAP-G1. To extend the density UI restricted zero-one theorem to general IID strictly elliptic rows in d>=3, this attempt must exclude concentration of f_n or bar_f_N on small-P sets where h(1-h) is near zero. The martingale convergence h(T_{X_n}omega)->1_{A_ell} controls the particle-seen law, not the stationary environment law. No UI subsequence, absolutely continuous invariant probability, finite regeneration mean, deterministic drift, or local measurability of h has been established under the original target assumptions. Compactness alone does not fill the gap. No parent-problem solution or novelty claim is made.',
  ['Original strict-elliptic IID C0044 setup','Lemmas are authored and pending independent review']),
 entry('compactness','finite-time-absolute-continuity-can-have-singular-compact-limit',
  'Control: absolutely continuous densities can have a singular compact limit',
  'UNREVIEWED ELEMENTARY COUNTEREXAMPLE TO A GENERAL INFERENCE. On compact [0,1] with uniform law P, g_N(x)=N*1_{(0,1/N)}(x) is a probability density for every N. The measures g_N P converge weakly to the singular point mass at zero. For u(x)=x>0 P-a.s., integral u g_N dP=1/(2N)->0. For r>1, ||g_N||_r=N^{1-1/r}; integral g_N log g_N dP=log N. The example refutes the inference that compactness and finite-time absolute continuity give absolute continuity of a weak limit. It is not an IID RWRE counterexample to the directional zero-one law.',
  ['P is uniform Lebesgue probability on [0,1]','N is a positive integer','r>1']),
 entry('formal-receipt','comparator-specification-is-not-implementation-proof-receipt',
  'C0044 source check: comparator specification versus implementation receipt',
  'DRAFT VERIFICATION NOTE, 2026-10-10. The primary public scope at github.com/openai/math/blob/main/lean/docs/220.md claims a strict-elliptic IID directional zero-one proof. Its linked ComparatorChallenges/DirectionalWalk.lean states OAI.DirectionalZeroOne.directional_zero_one for d>=3, a probability row law, strict ellipticity and nonzero real ell, but the comparator body is admitted. This comparator is a specification; an admitted challenge target does not audit the implementation or disprove a separate solution. Locate the implementation theorem, match the assumptions, and check trusted axioms before using the public scope as a mathematical proof receipt. This worker has no such receipt and leaves current openness UNKNOWN.',
  ['Source check concerns the linked comparator only','No implementation build or axiom audit was performed'])
]
relations = [
 {'from_key':'reverse-density','to_key':'uncertainty','kind':'semantic_association','rationale':'Uncertainty is integrated under the particle-seen law whose density is the reverse occupation density.'},
 {'from_key':'ui-criterion','to_key':'reverse-density','kind':'depends_on','rationale':'The sufficient condition is uniform integrability of the exact particle-seen densities.'},
 {'from_key':'ui-criterion','to_key':'uncertainty','kind':'depends_on','rationale':'Under a mixed escape probability, uncertainty is positive P-a.s. but its particle-seen expectation tends to zero.'},
 {'from_key':'density-obstruction','to_key':'reverse-density','kind':'depends_on','rationale':'The concentration, norm and entropy bounds are for the stated finite-time and Cesaro densities.'},
 {'from_key':'density-obstruction','to_key':'uncertainty','kind':'depends_on','rationale':'The small sets are the low-uncertainty level sets; martingale convergence gives their concentration.'},
 {'from_key':'hard-gap','to_key':'ui-criterion','kind':'depends_on','rationale':'The attempted extension still needs a UI subsequence or another way to exclude the concentration; the sufficient theorem does not provide it.'},
 {'from_key':'compactness','to_key':'hard-gap','kind':'analogous_to','rationale':'The elementary density sequence exposes the missing absolute-continuity control in a compactness shortcut; it is outside the RWRE class.'},
 {'from_key':'formal-receipt','to_key':'c0044-target','kind':'semantic_association','rationale':'The claimed new formal solution changes source-status uncertainty, but the comparator alone supplies no proof receipt.'},
 {'from_key':'c0044-target','to_existing_logical':'math:probability.randomenvironment:open-problem-c0044-zero-one-law-for-directional-transience-in-dimensions-d-3','kind':'cites','rationale':'The new dated source-status note concerns exactly the strict-elliptic IID directional question in the canonical intake card; it does not assert that its dated open status is current.'}
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w579',
          'bundle_slug':'c0044-reverse-density-uncertainty-draft-20261010',
          'entries':entries,'relations':relations}
dest=ROOT/'DRAFT_BUNDLE.json'
dest.write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
bykey={e['key']:e for e in entries}
prior=json.loads((ROOT/'C0044_PRIOR_EXTRACT.json').read_text(encoding='utf-8'))
canonical=next(x for x in prior['store'] if x['id']=='claim_77b8c8b3e552560382a17be2fac6b00021e3a08ff74f780812e6f39787d2abb8')
with (ROOT/'RELATION_EVIDENCE.jsonl').open('w',encoding='utf-8') as f:
    for rel in relations:
        target=bykey[rel['to_key']]['statement'] if 'to_key' in rel else canonical['body']
        row={'relation':rel,'source_end_quote':bykey[rel['from_key']]['statement'],
             'target_end_quote':target,'review_state':'DRAFT; w581 pending'}
        if 'to_existing_logical' in rel:
            row['existing_card_id']=canonical['id']
            row['existing_card_digest']=canonical['digest']
        f.write(json.dumps(row,ensure_ascii=False)+'\n')
print(json.dumps({'bundle':str(dest),'draft_entries':len(entries),'relations':len(relations),
                  'lemma_or_theorem_entries':sum(e['kind'] in ['lemma','theorem'] for e in entries)}))
