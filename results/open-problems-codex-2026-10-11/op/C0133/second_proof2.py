from pathlib import Path
import json
p=Path('SECOND_ATTEMPT.md');s=p.read_text(encoding='utf8');s+='''

## 4. Supplementary approach A: an exact discovery-order LLN (proved)
The warning about adaptive site selection in the first attempt can be made precise and overcome for discovery-order sums. Sample IID full stacks W_1,W_2,... with the source stack law, independently of a sequence of IID uniform variables driving transitions. On discovering a new site assign it the next unused W_j; at previously discovered sites use the already assigned stack. The walk cannot consult the stack at a new site before reaching it, so the label chosen for a new site is a function only of previously revealed stacks and driving uniforms. Induction on finite time shows that this lazy construction has the same joint law of the walk and its revealed stacks as the usual IID environment: conditional on the revealed past, the next untouched site has an independent stack of the original law. Finite-time joint laws determine the full observable path/revealed-stack law.

Let r_n be the number of distinct departure sites through time n-1. These are the first r_n discovered sites; the possible new arrival at time n is not counted until it is a departure site. Let F be any real integrable function of a stack, and f=E[F(W_1)]. The ordinary IID strong law gives sum_{j<=m}F(W_j)-fm=o(m) almost surely. On the event r_n->infinity, substitute m=r_n and use r_n<=n to obtain
(sum_{x in R_n}F(omega_x)-f r_n)/n -> 0.
If r_n stays finite, the sum and r_n are eventually constant, so the same conclusion holds. This is a pathwise almost-sure result on the whole space, and can be restricted to the non-transient event without conditioning the IID sequence on that event. The discovered stacks need not remain IID after conditioning on an event of recurrence; that conditional claim is not used.

Apply this with B(x)=sum_i |b(x,i)| and assume E[B(0)]<infinity. Then
|D_n|/n <= E[B(0)] r_n/n + o(1)
almost surely. Therefore sublinear range on an event implies zero projected speed there even for unbounded random cookie budgets with integrable total absolute drift. No uniform budget bound or uniform ellipticity is needed. This corrects the earlier incomplete caution: adaptive discovery does allow an IID budget law, because the newly selected stack has not yet been inspected.

For an exact signed version put delta(x)=sum_i b(x,i), mu=E[delta(0)], and
Q_n=sum_{x in R_n} sum_{i>N_n(x)} b(x,i).
Absolute summability makes these expressions well-defined. Grouping the consumed terms gives
D_n=sum_{x in R_n}delta(x)-Q_n,
so, using the martingale law from the first attempt,
X_n dot ell/n = mu r_n/n - Q_n/n + o(1).
This is a sharper reservoir reduction: under zero expected total drift, the remaining question is precisely whether outstanding signed drift Q_n=o(n).

The integrable budgets also control any sparse, even adversarially selected subset of discovered sites. If F_n is a subset of the first r_n discoveries and |F_n|/n->0, then for every fixed K>0,
sum_{x in F_n}B(x)/n <= K |F_n|/n + (1/n)sum_{j<=r_n} B(W_j)1_{B(W_j)>K}.
The discovery-order strong law makes the limsup at most E[B(0)1_{B(0)>K}], because r_n/n<=1. Integrability makes this expectation tend to zero as K->infinity. Thus the weighted sparse sum is o(n), despite the subset possibly depending on every revealed budget.

In particular, if the drifting cookies at each site are eventually exhausted after a finite random number M(x), define H_n={x in R_n:N_n(x)<M(x)}. If |H_n|/n->0 then |Q_n|<=sum_{x in H_n}B(x)=o(n). If also mu=0, zero speed follows. This is a proved conditional special case, not a proof that the unfinished-site count is sublinear on the non-transient event. Even when every fixed site is eventually exhausted, that conclusion is a separate density claim about a moving set of sites.

New remaining obstacle in approach A: control r_n/n (arbitrary mu) or outstanding signed cookie mass Q_n/n (zero mu). Eventual depletion at fixed sites alone does not justify either. Approach B does not need a finite drift budget, but does need infinite arrow exchangeability.
''';p.write_text(s,encoding='utf8')
claims=[
('An IID elliptic excited walk with infinitely exchangeable annealed arrow stacks has the same averaged full-path law as an IID Markovian RWRE; its directing transitions are strictly positive.','proved','SECOND_ATTEMPT.md Sections 1-2','The full original model need not have exchangeable arrow stacks; application of the RWRE non-transient theorem is pending exact-source verification.'),
('Integrable full-stack observables obey a discovery-order law: the discovered-site sum minus its mean times the range is o(n).','proved','SECOND_ATTEMPT.md Section 4','This gives no sublinear-range estimate on the non-transient event.'),
('For integrable absolute cookie-drift budgets, X_n dot ell/n = mu times range/n minus outstanding signed drift/n + o(1).','proved','SECOND_ATTEMPT.md Section 4','Need control of the outstanding reservoir or range density on returning paths.'),
('Integrable IID discovered budgets have o(n) mass on any adaptively selected subset of o(n) discovered sites; zero expected total drift and o(n) unfinished sites imply zero speed.','proved_special_case','SECOND_ATTEMPT.md Section 4','The unfinished-site count is not proved o(n) on the general returning event.')]
with Path('CLAIMS.jsonl').open('a',encoding='utf8') as f:
 for claim,status,loc,gap in claims:f.write(json.dumps({'problem_id':'C0133','claim':claim,'status':status,'proof_location':loc,'remaining_gap':gap,'checks':['Written proof; IID discovery construction and event-conditioning issue checked explicitly.']})+'\n')
print('discovery-order and reservoir refinements saved')
