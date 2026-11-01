"""Five rewritten RWRE attempts; two primary-source resolutions excluded."""
from campaign_tools import *
import hashlib

PEER=OWNER_ROOT/'<private-repo>/06_math_research/probability_1000_intake_claude_20260907'
PEER_OUT=OWNER_ROOT/'Downloads/Probability_1000_intake_claude_20260907'
SID='drewitz_ramirez_rwre_2014'
ROWS=[
(40,'Open question2.19 PDF24; Corollary2.15 PDF20-21',
 'Ballisticity and an absolutely continuous stationary environment law',
 'Under stationary ergodicity and ellipticity, does directional ballisticity imply an invariant probability law for the environment viewed from the particle that is absolutely continuous with respect to the environment law?',
 'The opposite implication, assuming directional transience, is already Corollary2.15 of the source. Its stationary-increment recurrence argument supplies strict positive speed; this is not an unresolved part of the target.',
 'Let R be the environment transition kernel. Every P*R^i is absolutely continuous with respect to the translation-invariant P. Its density is the finite sum f_i(omega)=sum_x P_(-x),omega[X_i=0], obtained by changing variables under a spatial shift in the annealed endpoint formula. Set g_n=(1/n)*sum_(i=0)^(n-1) f_i. If these densities are uniformly integrable in L1(P), Dunford-Pettis gives a weak-L1 convergent subsequence g_n to g, with g>=0 and integral g=1. For bounded measurable h, integral(Rh-h)*g_n dP=((P*R^n)h-P h)/n tends to zero. Weak-L1 convergence passes both bounded test functions, so g dP is invariant. A uniform Lp bound for some p>1 would suffice, since integral_(g_n>K) g_n<=K^(1-p)*integral g_n^p. This isolates an explicit missing estimate: positive speed must supply enough control of these occupation densities, not merely weak compactness of the environment space.',
 'Shift invariance and summing the quenched endpoint probabilities give integral f_i dP=1. The stationary defect telescopes exactly and has absolute value at most2*||h||infinity/n. Weak limits of absolutely continuous probabilities without uniform integrability can be singular, as n*1_[0,1/n] dx demonstrates.',
 'No density-uniform-integrability estimate follows here from ballisticity. The invariant-law-to-positive-speed direction is credited to the source; no unsupported assertion that iid regeneration alone always gives a full-space absolutely continuous invariant law.'),
(41,'Open question2.20 PDF24; renewal identities PDF47-49',
 'Directional transience versus positive speed under uniform ellipticity',
 'For nearest-neighbor iid uniformly elliptic RWRE on Z^d, d>=2, does transience in direction ell imply positive limiting speed in that direction?',
 'Equivalence of conditions(T) and(Tprime), proved by Guerra-Ramirez, does not answer this question.',
 'Uniform ellipticity gives a precise finite-trap bound. Suppose every site of a finite set A has a nearest-neighbor path of at most m steps leading outside A, and every transition probability is at least kappa. At each block of m steps before exit, the conditional probability of leaving is at least kappa^m. The strong Markov property yields P_x,omega[tau_A>j*m]<=(1-kappa^m)^j and E_x,omega[tau_A]<=m*kappa^(-m). For A=[-R,R]^d intersect Z^d, m=2R+1 works by moving along one coordinate. Thus no fixed-size trap has an arbitrarily large quenched mean under uniform ellipticity. But the bound grows exponentially with R; it cannot be summed over the random spatial extent explored before regeneration without a further tail estimate. For coordinate directions, the source renewal formula gives positive speed exactly when the conditional mean regeneration time is finite; almost-sure finite regeneration times alone do not supply it.',
 'The event of following a selected path of length r<=m has probability at least kappa^r>=kappa^m. Summing the survival bound over successive blocks gives the mean estimate, with no independence assumption between blocks. Taking a singleton checks m=1 and actual exit time1; the general upper bound is deliberately loose.',
 'No estimate on the distribution of the size or shape of a regeneration excursion, and no proof that transience implies an integrable regeneration time.'),
(43,'Open question2.23 PDF25',
 'Transience of elliptic iid environments in dimension at least three',
 'Is every nearest-neighbor elliptic iid random walk in random environment on Z^d transient when d>=3?',
 'Transience means finitely many visits to each site, not transience in a specified direction. The following homogeneous calculation is a classical special case.',
 'For a deterministic homogeneous elliptic environment, the increments are iid. Nonzero mean gives transience by the strong law. If the mean is zero, nearest-neighbor steps force p(e_i)=p(-e_i)>0 for every i. The characteristic function is phi(t)=2*sum_i p(e_i)*cos(t_i). Its absolute value equals1 only at the two torus points with all coordinates0 or all coordinates pi. Taylor expansion at each gives |phi(t)|<=1-c*dist(t,S)^2 locally, while compactness bounds it strictly below1 elsewhere. Fourier inversion therefore bounds the return probability by C*n^(-d/2). The sum over n is finite for d>=3, proving transience through the expected visit count. For a spatially varying environment the quenched increments are no longer iid and there is no one fixed characteristic function whose nth power gives the transition law.',
 'The covariance quadratic form is sum_i 2*p(e_i)*t_i^2 and is positive definite. The two absolute-value maxima account for bipartite periodicity; ignoring the pi point would miss the even-time contribution. A finite expected total number of returns implies the actual count is finite almost surely.',
 'No heat-kernel estimate for general iid elliptic environments. A central limit theorem by itself is not a local return-probability bound.'),
(44,'Open question3.2 PDF42',
 'Directional zero-one law beyond the plane',
 'For elliptic iid nearest-neighbor RWRE on Z^d, d>=3, prove or disprove P_0[A_ell] in{0,1} for every direction ell.',
 'A_ell and A_minusell are disjoint by definition. Showing their intersection is empty proves no zero-one law. The source credits the dimension-two theorem to Zerner-Merkl.',
 'There is a useful stationary-measure special case. Suppose additionally that the environment process has an invariant probability Q absolutely continuous with respect to P. Kozlov gives Q equivalent to P. Put q(omega)=P_0,omega[A_ell]. By the Markov property and invariance of A_ell under deleting finitely many steps, q(eta_n)=E[1_Aell|omega,X_0,...,X_n] is a bounded martingale and tends to1_Aell. Under initial law Q the variables q(eta_n) all have the same distribution, so q(eta_0) itself must take values only0 and1. The harmonic identity q(omega)=sum_e omega(0,e)*q(t_e omega), together with ellipticity, then forces every neighboring shift to have the same value on a common full-measure set. Spatial ergodicity of P makes q constant, establishing the directional zero-one law in this restricted class. The absent invariant law is the obstruction to applying this stationary argument to all iid environments.',
 'For any bounded continuous test function F, stationarity gives E_Q F(q(eta_n))=E_Q F(q(eta_0)); dominated convergence identifies this law with a distribution supported on{0,1}. A convex combination with all positive weights can equal0 or1 only when each summand equals that value.',
 'No existence proof for Q in a general elliptic iid environment. The argument is a credited stationary special-case rederivation, not a solution of the higher-dimensional question.'),
(45,'Open question3.20 PDF52; Theorem3.17 PDF51',
 'Does positive velocity force a quantitative ballisticity condition?',
 'Under iid uniform ellipticity, does positive velocity in direction ell imply the polynomial ballisticity condition(P)_M for M>15d+5?',
 'The source links stretched-exponential slab conditions to exponential moments of the spatial regeneration radius, not to an asserted equivalence with arbitrary time moments.',
 'For the known non-nestling subcase with local projected drift at least delta>0 everywhere, let xi be a one-step displacement in direction ell. Since |xi|<=1, E[exp(-a*xi)|past]<=1-a*delta+a^2*exp(a)/2. Choosing0<a<=min(1,delta/exp(1)) makes exp(-a*X_n dot ell) a nonnegative supermartingale. Stopping at a backward level-bL gives probability at most exp(-a*bL) of ever reaching it. Nearby directions retain a positive drift lower bound, giving the slab decay needed for(T), and hence the known polynomial condition. Positive limiting velocity alone supplies no such uniform local drift. Even at the level of abstract regeneration times, finite first moment gives only n*P[T>n]->0: the valid tail P[T>n]=1/((n+1)*log(n+exp(1))^2), n>=0, has finite mean and no moment1+epsilon. This is an implication counterdiagnostic, not a RWRE construction or a claimed equivalence between slab exits and time moments.',
 'The exponential remainder follows from Taylor expansion for |xi|<=1; optional stopping at the minimum of the backward hitting time and n followed by Fatou gives the probability bound. Summing the displayed tail gives finite mean, whereas the tail integral for any moment1+epsilon diverges. The source Theorem3.17 involves max_(i<=tau1)|X_i|, which is a spatial variable.',
 'No self-improvement from positive velocity to the required exit bound in the nestling case, and no counterexample satisfying iid uniform ellipticity.')
]

def main():
    incoming=latest(PEER/'problems.jsonl','problem_id');s=latest(PEER/'sources.jsonl','source_id')[SID]
    raw=(PEER_OUT/s['raw_relative_to_downloads']).read_bytes();txt=(PEER_OUT/s['text_relative_to_downloads']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==s['sha256']=='5b79b728fd6a0add60442b5a686ed69fdff9041c04d595269824a91e1792ff43'
    assert hashlib.sha256(txt).hexdigest()==s['extracted_sha256']=='228d342e370491646ade982d684e079fc308727b28cef1919d388f77ab38ffab'
    import fitz
    with fitz.open(stream=raw,filetype='pdf') as d:
        assert len(d)==68 and 'Corollary 2.15' in d[19].get_text() and 'Open question 2.19' in d[23].get_text()
    assert SID not in latest(HERE/'sources.jsonl','source_id')
    prior=latest(HERE/'problems.jsonl','problem_id');assert all(f'P{i:04d}' not in prior for i in range(482,489))
    ids={f'C{i:04d}' for i in range(40,47)};freeze=HERE/'intake_rwre_frozen_038.json'
    dest=OUTPUT/s['raw_relative_to_downloads'];desttxt=OUTPUT/s['text_relative_to_downloads']
    guard(freeze,dest,desttxt);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw);desttxt.write_bytes(txt)
    freeze.write_text(json.dumps(dict(as_of_utc=now(),source=s,problems=[incoming[k] for k in sorted(ids)],
      attempts=[a for a in records(PEER/'attempts.jsonl') if a['problem_id'] in ids],
      warning='Untrusted incoming record frozen; mathematical corrections and later-source resolutions in main ledger supersede it.'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    s.update(source_date='2013-09-10',reading_status='Primary definitions PDF6-8, Corollary2.15 PDF20-21, examples PDF22-23, questions PDF24-25,42,52,55, regeneration PDF45-51 read',
      statement_validation='Five distinct remaining targets matched; site-index typo exposed; corrected edge-moment question and T/Tprime question resolved by later sources',intake_reverified_at=now(),intake_raw_and_text_hashes_reverified=True)
    append(HERE/'sources.jsonl',s)
    ps=[];ats=[]
    for cid,loc,title,statement,caveat,result,check,gap in ROWS:
        pid=f'P{482+cid-40:04d}'
        ps.append(dict(schema='probability-problem.v1',problem_id=pid,source_id=SID,title=title,locator=loc,source_statement_date='2013-09-10',
          statement=statement,statement_caveat=caveat,admitted=True,historical_status='source_says_open',current_status='unverified',result_status='unsolved',
          dedup_key=title.lower().replace(' ','_'),recorded_at=now(),intake_origin={'agent':'claude-probability-1000-continue-0907','id':f'C{cid:04d}','frozen_record':freeze.name},
          status_search='Bounded2026-09-07 primary searches and archived later theorems checked. No current-openness certificate; known stationary/non-nestling/homogeneous cases credited.'))
        ats.append(dict(schema='probability-attempt.v1',attempt_id=pid+'-A001',problem_id=pid,recorded_at=now(),substantive=True,
          method='Integrator-authored exact restricted argument and corrected proof-obstruction analysis',result=result,independent_check=check,obstruction=gap,
          verification='author_checked_restricted_argument',independent_review='none',full_problem_solved=False,novelty='not_claimed'))
    for cid,later,loc,reason in [
      (42,'fribergh_kious_trapping_2015','Proposition4.4 PDF24-25; construction PDF22-24',
       'Literal source moment is automatic since omega(0,e)*omega(0,-e)<=1/4. The intended edge product uses omega(e,-e). Even that corrected sufficiency claim is false: Fribergh-Kious Proposition4.4 constructs elliptic iid directionally transient zero-speed walks in dimension D=d+1>=3 with at least two outgoing edges per vertex of probability>=c=1/(4(d+1)). Any single transition is thus<=1-c, so every corrected edge product is<=(1-c)^2 and its reciprocal escape denominator is uniformly bounded. Larger hypercube traps cause zero speed. No new counterexample claimed.'),
      (46,'guerra_ramirez_ballistic_2018','Theorem2.1 PDF3',
       'Guerra-Ramirez Theorem2.1 proves(Tprime) implies(T) under iid uniform ellipticity in d>=2. The reverse implication follows directly from the definitions, resolving the historical question.')]:
        pid=f'P{482+cid-40:04d}';inc=incoming[f'C{cid:04d}']
        ps.append(dict(schema='probability-problem.v1',problem_id=pid,source_id=SID,title=inc['title'],locator=inc['locator'],statement=inc['statement'],
          source_statement_date='2013-09-10',admitted=False,historical_status='source_says_open',current_status='resolved_in_literature',result_status='literature_resolved',
          exclusion_reason=reason,resolution_source_id=later,resolution_locator=loc,recorded_at=now(),intake_origin={'id':f'C{cid:04d}','frozen_record':freeze.name}))
    append_many(HERE/'problems.jsonl',ps);append_many(HERE/'attempts.jsonl',ats)
    ss=latest(HERE/'sources.jsonl','source_id')
    for sid,scope in [('guerra_ramirez_ballistic_2018','Primary PDF1-3 read; Theorem2.1 matches historical question3.28'),('fribergh_kious_trapping_2015','Primary PDF1-11,22-27 read; Proposition4.4 gives corrected-edge-moment counterexample, with dimension D=d+1>=3')]:
        row=ss[sid];row.update(reading_status=scope,statement_validation='Later theorem matched directly; historical resolved target excluded');append(HERE/'sources.jsonl',row)
    snapshot(None)
    print(json.dumps({'admitted':5,'resolved_exclusions':2,'next_id':'P0489','promoted_solutions':0}))

if __name__=='__main__':main()
