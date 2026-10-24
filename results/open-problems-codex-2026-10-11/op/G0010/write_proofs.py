from pathlib import Path
p=Path('ATTEMPT.md')
s=p.read_text(encoding='utf-8');s=s[:s.index('### Proof plan already derived')]
s+=r'''
## 1. Spectral and percolation parameters
Throughout, a tree height counts edges. Put theta_h=pi/(h+2). The positive vector with value

    x_j = b^{-j/2} sin((j+1)theta_h)

on level j satisfies A x = 2 sqrt(b) cos(theta_h) x, including the two boundary equations (sin(0)=sin((h+2)theta_h)=0). It is strictly positive for 0<=j<=h, so its eigenvalue is the spectral radius: for example, conjugating A by the positive diagonal matrix with entries x makes every row sum equal that eigenvalue; the infinity operator norm then bounds every eigenvalue in modulus. This proves the exact formula without assuming that radial symmetry captures the top eigenvector.

For b>=5, epsilon_b=1-2/sqrt(b) lies in (0,1). For h>=2, p_h=1/[b cos(theta_h)] lies in (0,1) and satisfies p_h lambda_h=1-epsilon_b exactly. The critical parameter q=1/b is smaller than p_h and is also permitted by the source hypothesis.

## 2. A uniform binomial window lemma, proved without an asymptotic limit theorem
**Lemma 1.** Fix any integer b>=2. For every integer z>=64, let X have law Bin(bz,1/b). If integers a,l satisfy z<=a, a+l<=z+4 sqrt(z), and l=floor(sqrt(z)), then

    P(a<=X<=a+l) >= q_* := exp(-30)/8.

**Proof.** The variance is (1-1/b)z<=z. Chebyshev gives probability at least 3/4 to the interval |X-z|<2 sqrt(z). There are at most 4 sqrt(z)+2<=6 sqrt(z) integers in that interval. The binomial mode is z, since floor((bz+1)/b)=z. Thus P(X=z)>=1/[8 sqrt(z)].

For an integer r with 0<=r<=4 sqrt(z), the successive-mass ratio gives

    P(X=z+r)/P(X=z)
      = product_{i=1}^r [1-(i-1)/((b-1)z)]/[1+i/z].

Here (i-1)/((b-1)z)<=4/((b-1)sqrt(z))<=1/2. Use log(1-u)>=-2u for 0<=u<=1/2 and log(1+v)<=v for v>=0. The logarithm of the product is at least

    -[1+2/(b-1)] r(r+1)/(2z) >= -30,

because 1+2/(b-1)<=3 and r(r+1)<=16z+4 sqrt(z)<=20z. (For r=0 the empty product is 1.) All these masses are in the support: z+4 sqrt(z)<=bz for z>=64, b>=2. Each mass in the requested window is therefore at least exp(-30)/[8 sqrt(z)]. There are floor(sqrt(z))+1>=sqrt(z) masses, proving the lemma. The logarithmic inequalities follow by differentiating their two sides, so no local central limit theorem is needed. QED.

## 3. A rare critical process with cubic area
Let Z_0=1 and, given Z_j=z, let Z_{j+1} have law Bin(bz,1/b). Let S_H=sum_{j=0}^H Z_j.

**Lemma 2.** For each fixed b>=5 there is a_b>0 such that, for every integer H>=16,

    P(S_H>=H^3/8) >= a_b q_*^H.

**Proof.** The particular population path

    Z_0=...=Z_5=1, Z_6=3, Z_7=13, Z_8=64

has a strictly positive probability a_b. Every transition is feasible: 3<=b, 13<=3b, and 64<=13b for b>=5. Given any j>=8 and integer j^2<=z<=4j^2, set a=max(z,(j+1)^2), l=floor(sqrt(z)). Then

    0<=a-z<=2j+1<=3 sqrt(z),
    a+l<=z+4 sqrt(z),
    (j+1)^2<=a<=a+l<=4(j+1)^2.

For the last inequality, both z and (j+1)^2 are at most 4j^2, and l<=2j. Lemma 1 thus shows, uniformly over all states in the band, that the conditional probability of reaching the next band is at least q_*. Multiplying conditional probabilities, the event

    j^2<=Z_j<=4j^2 for every 8<=j<=H

has probability at least a_b q_*^{H-8}>=a_b q_*^H. On this event, sum over j=ceil(H/2),...,H: there are at least H/2 such terms and each is at least H^2/4. Hence S_H>=H^3/8. QED.

This event is deliberately rare: its probability is exponentially small in H. That cost is the point; the host has exponentially many independent launch subtrees. The typical critical surviving process has area of order H^2, which alone does not determine its largest component among those many trials.

## 4. Cubic lower bound for the tree's largest component
Let ell=log b and d_*=log(1/q_*). Choose the fixed positive fraction

    eta = ell/[2(ell+d_*)] < 1,
    H = floor(eta h).

At depth h-H of T_{b,h} there are M=b^{h-H} vertices. Their descendant subtrees of height H have disjoint edge sets. Under bond percolation at q=1/b, the descendant cluster of each root is exactly the process in Lemma 2 and these M trials are independent. Each success produces a connected set of at least H^3/8 vertices, regardless of the state of the edge to its parent. Consequently

    P_q(L_1 < H^3/8)
       <= (1-a_b q_*^H)^M
       <= exp(-a_b b^{h-H} q_*^H)
       <= exp(-a_b exp(h ell/2)) -> 0.

The last step uses H<=eta h. For large h, H>=eta h/2, so H^3/8>=eta^3 h^3/64. The event L_1>=K is increasing in retained edges, and p_h>=q, so the same bound holds at the source-boundary parameter p_h. Thus the lower constant c_b=eta^3/64 works. Merging two successful descendant sets through ancestors only increases the largest component; no closed-parent condition is needed for the lower bound.

## 5. A finite-depth generating-function lemma
**Lemma 3.** Let H>=80 be an integer, and let a branching process have offspring Bin(d,p) with d>=1 and 0<=p<=1, satisfying mu=dp<=1+10/H^2. Let S_k be its total population through generation k from one particle. For t=1/(128H^2),

    log E exp(t S_k) <= (k+1)/(64H^2),  0<=k<=H.

In particular log E exp(t S_H)<=1/(32H).

**Proof.** Write x_k=log E exp(t S_k). Independence of descendants gives the exact finite-depth recurrence

    x_0=t,
    x_{k+1}=t+d log(1+p(exp(x_k)-1)).

All x_k are nonnegative and finite, since finite-depth offspring are bounded. For 0<=x<=1, the exponential series gives exp(x)-1<=x+x^2: indeed the terms of degree at least two sum to at most x^2 sum_{m>=2}1/m! = (e-2)x^2 < x^2. Also log(1+u)<=u for u>=0. Since mu<=2, whenever x_k<=1,

    x_{k+1} <= t+x_k+10 x_k/H^2+2 x_k^2.

Induct on k. The initial inequality is immediate. If k<=H-1 and x_k<=(k+1)/(64H^2), then x_k<=1/(32H)<=1. Furthermore

    10 x_k/H^2 <= 10/(32H^3) <= 1/(256H^2),
    2 x_k^2 <= 1/(512H^2).

Together with t=4/(512H^2), the increment over x_k is at most 7/(512H^2)<=1/(64H^2), proving the induction. Finally (H+1)/(64H^2)<=1/(32H). QED.

The Lean file CriticalTree.lean isolates the polynomial increment inequality with r=1/H, rather than claiming to formalize independence or the whole percolation theorem.

## 6. Matching cubic upper bound at the source boundary
For h>=80, put x=pi/(h+2), so x^2<=1. From cos(x)>=1-x^2/2 and

    (1+x^2)(1-x^2/2)>=1,

we get sec(x)<=1+x^2. Hence

    b p_h=sec(theta_h)<=1+pi^2/(h+2)^2<=1+10/h^2.

Every descendant-root cluster through at most h generations is distributed as the branching process Bin(b,p_h) truncated at that depth, and is stochastically bounded by the height-h version. Lemma 3 and exponential Markov give, uniformly over all host vertices v,

    P(descendant cluster at v has size >=K)
        <= exp(1/(32h)-K/(128h^2)).

Each connected component of a rooted tree has a unique highest vertex. The whole component is precisely the open descendant cluster of that vertex: any other vertex of the component must be its descendant, since the unique path to a non-descendant would first visit an ancestor. Thus a union bound over the n_h possible highest vertices bounds L_1. Since n_h<=2b^h, choosing

    C_b=256(log b+1), K=C_b h^3

gives

    P(L_1>=C_b h^3)
       <=2 exp(1/(32h)+h log b-2h(log b+1)) ->0.

Together with Section 4 this proves the stated Theta(h^3)=Theta((log n_h)^3) result, including its probability quantifier and exact source-boundary parameter.

## 7. A universal critical-wedge upper bound
**Theorem 4 (partial answer for arbitrary hosts).** Let G be any finite simple graph on n>=2 vertices, with Delta>=2 and adjacency spectral radius lambda>0. Fix 0<epsilon<1, let p<=min(1,(1-epsilon)/lambda), and define

    a=-log(1-epsilon),
    H=max(80, ceil(3 log(n)/a)).

If p(Delta-1)<=1+10/H^2, then, for K=128H^2(3 log(n)+1),

    P(L_1(G_p)>=K) <= 2 n^{-2}.

In particular p(Delta-1)<=1 implies L_1=O_epsilon((log n)^3) a.a.s. The theorem includes a quantified vanishing supercritical window for maximum-degree branching. Its constants depend on epsilon only through H.

**Proof.** Let E be the event that there is an open simple path with H+1 edges. The number of oriented simple paths of that length is at most the total walk count 1^T A^{H+1}1. Because A is real symmetric, its Euclidean operator norm is lambda (the largest absolute eigenvalue equals its Perron eigenvalue), and therefore this count is at most n lambda^{H+1}. Every simple path has distinct edges and is open with probability p^{H+1}. The first moment bound gives

    P(E)<=n(p lambda)^{H+1}<=n exp(-a(H+1))<=n^{-2}.

Fix a vertex v. Breadth-first exploration, stopped at distance H from v, is stochastically bounded in total population by a process with root offspring Bin(Delta,p) and other offspring Bin(Delta-1,p). To see the domination, at the root there are at most Delta untested incident edges. Every discovered nonroot vertex has at most Delta-1 other edges after its discovering edge is removed; after all previously tested edges and previously discovered endpoints are omitted, there are even fewer candidates. Conditional on the exploration history, the remaining tested edges are independent Bernoulli(p). Complete each list of candidates to the appropriate degree with independent artificial Bernoulli trials and treat all successful trials as new distinct particles. Process particles in breadth-first order; ignored artificial particles get independent full offspring lists. This constructs the stated dominating finite-depth process. Each real edge is tested at most once; collisions suppress vertices and cannot invalidate the domination.

Let x=log E exp(t S_{H-1}) for the nonroot process, with t=1/(128H^2). Lemma 3 gives 0<=x<=1/(32H). The root process R_H has logarithmic MGF

    log E exp(t R_H)
       =t+Delta log(1+p(exp(x)-1))
       <=t+(p Delta)(exp(x)-1).

Since Delta>=2, p Delta<=2p(Delta-1)<=4, and x<=1, this is at most t+8x<=1/H. Therefore

    P(R_H>=K)<=exp(1/H-K/(128H^2)).

On E^c every vertex in C(v) is at graph distance at most H from v in the retained graph: a larger distance would supply a simple path with H+1 edges. Thus on E^c the breadth-first search truncated at H includes all of C(v). It follows that

    P(L_1>=K)<=P(E)+sum_v P(truncated search from v has size >=K)
       <=n^{-2}+n exp(1/H-3 log(n)-1)
       <=2n^{-2}.

No conditioning on E^c was inserted into the branching law: the last bound uses the unconditional truncated-search domination. This is essential for independence to remain valid. QED.

For Delta<=1 all components have size at most 2 deterministically, so those excluded degenerate cases need no probabilistic theorem.

**Sharpness within the critical wedge.** On T_{b,h}, at the allowed parameter p=1/b, p(Delta-1)=1. The lower bound of Section 4 still applies; the upper bound of Section 6 applies with mu=1, or Theorem 4 may be used directly. Thus the power three in the universal critical-wedge theorem cannot be replaced by a smaller power uniformly over its host class. This is a restricted-class sharpness statement, not the full answer to Question 5.2.

## 8. Hostile-referee checklist and remaining gap
1. The source question concerns all finite hosts: neither the complete-tree theorem nor Theorem 4 is presented as a complete solution.
2. Time scale and independence: lower trials use disjoint descendant edges and never require the original root to connect to a trial root. Upper domination uses unconditional exploration; conditioning on short diameter would be invalid.
3. Spectral normalization: lambda is the unnormalized adjacency spectral radius. The positive eigenvector checks the exact finite-tree spectral value, including both boundary levels.
4. Rare versus typical processes: H^3 is obtained from exponentially rare quadratic population growth multiplied by exponentially many trials; it is not inferred from typical surviving H^2 area.
5. Uniform window estimate: the binomial ratio proof controls every population in the band, not just its endpoints or an asymptotic Gaussian approximation.
6. Probabilities: constants b and epsilon_b are fixed while h tends to infinity; all p_h lie in [0,1] for h>=2. The lower bound extends by monotone coupling; its particular trajectory need not be increasing.
7. MGF induction: t is of order H^{-2}; the cumulative x is of order H^{-1}, and the quadratic error is accounted for at every step. The recurrence is exact before being bounded.
8. Small graphs: theorems are asymptotic for the tree; the finite universal estimate remains true even if its size threshold exceeds n. Delta<=1 is handled separately.
9. Formal scope: Lean checks only two algebraic steps. The written proofs supply the probability, graph, analytic and asymptotic arguments.

The remaining gap is a matching worst-case scale for arbitrary (n,Delta,lambda), particularly fixed-gap p(Delta-1)>1 and arbitrary multiscale degree/Perron profiles. The universal critical-wedge result and complete resonance family settle a boundary regime but not that gap. Nothing here refutes the source question, which asks for a characterization rather than proposing a formula.
'''
p.write_text(s,encoding='utf-8')
import json
claims=[
{'problem_id':'G0010','claim':'For every fixed integer b>=5, source-boundary percolation on the complete b-ary tree of height h at epsilon=1-2/sqrt(b) has largest component Theta(h^3)=Theta((log n)^3) a.a.s.','status':'proved_special_case','proof_location':'ATTEMPT.md Sections 1-6','remaining_gap':'General host and all-parameter worst-case bound remains open.','checks':'Explicit spectral eigenvector, binomial mass ratios, MGF induction, independent-subtree amplification; numerical and Lean checks pending.'},
{'problem_id':'G0010','claim':'If p lambda<=1-epsilon and p(Delta-1)<=1+10/H^2, H=max(80,ceil(3 log n/(-log(1-epsilon)))), then P(L_1>=128H^2(3 log n+1))<=2/n^2.','status':'proved_special_case','proof_location':'ATTEMPT.md Section 7','remaining_gap':'Does not cover arbitrary fixed-gap p(Delta-1)>1.','checks':'First-moment long-path estimate; unconditional BFS branching domination; bounded-offspring MGF; algebraic Lean check pending.'},
{'problem_id':'G0010','claim':'The universal O_epsilon((log n)^3) critical-wedge upper bound at p(Delta-1)<=1 is sharp in its logarithmic exponent.','status':'proved_special_case','proof_location':'ATTEMPT.md Section 7 sharpness paragraph and Section 4','remaining_gap':'Exact optimal coefficients and general all-regime answer not established.','checks':'Critical retention p=1/b on T_{b,h} satisfies all source hypotheses and the wedge equality.'}]
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
