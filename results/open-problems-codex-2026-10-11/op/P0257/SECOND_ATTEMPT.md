# Second attempt — 12 October 2026

## Gap reread and two approaches not previously tried

The remaining gap is that the metric's local weak limit and laws of large numbers for local lower-bound scores do not control the history-dependent discovery ordering. The earlier attempt did not give a local approximation of NUV or an almost-subadditive inequality.

**Approach A: exact deferred-decisions Markov representation in the exponential mean-field model.** Reveal all weights between visited vertices, while retaining only conditional lower thresholds for edges from visited to unvisited vertices. Exponential memorylessness may preserve independent residuals and reduce the undiscovered part to a threshold vector. Derive the complete transition law, check it against ordinary shortest-path NUV, and determine what additional ergodic or hydrodynamic result would imply a length constant. This has not been tried in the first attempt.

**Approach B: compactness of rank-marked NUV paths, with uniqueness of a limiting path ensemble.** Mark each vertex by its discovery rank divided by n and mark directed successor edges. A local weak subsequential limit could encode visit history intrinsically rather than assume it disappears. One must prove tightness of directed edges, uniform integrability of their lengths, and uniqueness of the limiting marked ensemble. Adjacent successor ranks differ by 1/n, so a limiting path component must have constant rank mark, a nontrivial constraint. Underlying-graph convergence alone does not imply the required uniqueness. This compactness/uniqueness reduction has not been tried in the first attempt.

We pursue A: it offers an exact finite model before requiring any infinite-volume inference. B is recorded as an unpursued alternative, not as a theorem.

## Work in progress

Use K_n with independent edge weights Exp(rate 1/n). Let S be the visited set, s its current vertex, and k=n-|S|. Reveal all internal weights on S. Hypothesis to check by induction: conditional on revealed history, the cut weights W_xu, x in S, u outside S, have the independent form h_x+Exp(rate 1/n), for a history-measurable h_x>=0; outside–outside weights remain untouched iid exponentials. Set h_s=0 immediately after each discovery.

With d_S the internal shortest-path metric, set a_x=d_S(s,x)+h_x. The next discovery time T would have survival

    P(T>t | state)=exp[-(k/n) sum_{x in S}(t-a_x)_+].

Given T=t, the winning visited endpoint should be uniform among rows x with a_x<t, and the winning unvisited vertex uniform among the k remaining labels. Update h'_x=max(h_x,t-d_S(s,x)); give the new vertex threshold zero. Its edge to the winning endpoint has length t-d_S(s,x); other edges to old vertices have independent lengths h'_x+Exp(rate 1/n). Proving that this update does not conceal additional conditioning is the main finite check.

## 1. Exact Markov representation (proved)

The starting vertex is fixed in advance, or selected independently of the weights, as in the source's uniform-start model. The state consists of the visited metric D=d_S, a vector h, the current vertex s, and the remaining count k. Labels outside S can be suppressed by exchangeability. Initially S={s}, D(s,s)=0, h_s=0 and k=n-1.

**Invariant.** Conditional on the exploration filtration, all cut edges are mutually independent W_xu=h_x+E_xu, E_xu~Exp(rate 1/n), and all outside–outside edges are independent untouched exponentials, also independent of cut edges. The metric D and h are measurable in that filtration. The filtration reveals all visited–visited edge weights, the previous winning cut edges and discovery times, but not the unrevealed cut residuals.

**Why the cut minimum is the actual next NUV discovery.** Any path from s to an unvisited vertex has a first unvisited vertex q and a prefix confined to S up to its final cut edge {x,q}. This prefix has length at least D(s,x)+W_xq. Conversely the internal shortest path to any x followed by a cut edge realizes such a prefix. Thus the first discovery is exactly the minimum of D(s,x)+W_xu over all cut edges. Positive weights ensure that a path reaching a more distant unvisited vertex through q cannot beat its prefix. This proves equality with the source's shortest-path NUV rule, without assuming globally shortest paths between visited vertices avoid unvisited vertices.

Put a_x=D(s,x)+h_x and

    Z(t)=sum_{x in S}(t-a_x)_+,  u=k/n.

The independent residuals give P(T>t|state)=exp[-u Z(t)], t>=0. For t not one of the finitely many activation values a_x, the joint density for the winner (x,q) is

    (1/n) 1_{t>a_x} exp[-u Z(t)] dt.

Hence, conditional on T=t, the visited endpoint x is uniform over active rows {x:a_x<t}, and q is uniform over the k unvisited labels, independently of x. Times equal to activation values have probability zero; h_s=0 guarantees Z(t)>=t, so the distribution is continuous and proper.

**Conditional independence after the minimum.** Conditional on T=t and winner (x,q), every losing residual E_yv is conditioned only by E_yv>(t-a_y)_+. Independence and the exponential density give the independent laws

    W_yv=max(h_y,t-D(s,y))+Exp(rate 1/n).

This can be verified directly from the product density: the density of the winning variable at its required value factors against the product of the truncated losing densities; division by the survival product leaves independent rate-1/n exponential residual densities. The winning edge has deterministic length W_xq=t-D(s,x). Let h'_y=max(h_y,t-D(s,y)). For y!=x, reveal the losing edge W_yq=h'_y+Exp(rate 1/n); these residuals are independent of all cut edges to the still-unvisited vertices. The winner's weight is fixed, and h'_x equals that weight since t>a_x. The edges from q to the still-unvisited set were previously outside–outside edges, remain fresh independent exponentials, and get threshold h'_q=0. This proves the invariant inductively. Revealing the nonwinning edges to q imposes no additional constraints on edges to other unvisited labels.

**Metric update and sufficient state.** If w_y is the new edge {q,y}, put

    b_z=min_{y in S}(w_y+D(y,z)),
    D'(q,z)=b_z,
    D'(z,z')=min(D(z,z'),b_z+b_z').

Every shortest path in the enlarged visited graph uses q either zero times or once, proving these formulas. The concatenation realizing b_z+b_z' is a walk and can only decrease upon removing loops, so it still gives a valid upper bound; the zero/once decomposition gives the reverse bound. Thus D,h,s,k suffice as a finite-dimensional Markov state: a state of size growing with |S|, not a fixed-dimensional or local closure. After the update take s'=q and k'=k-1.

**Sampling the next time.** Draw E~Exp(1). The unique T>=0 solving

    u Z(T)=E                                                (A1)

has precisely the conditional law above. The transformed variables E along a presampled-graph NUV run are iid Exp(1): each has this law conditional on all past revealed information, and induction on products of bounded test functions proves independence. The state still contains substantial randomness besides E; this is not a claim that the original step lengths are independent.

## 2. Lipschitz constraint on the threshold field (proved)

At every state,

    h_s=0, h_x>=0, |h_x-h_y|<=D(x,y), and h_x<=D(s,x).        (A2)

Initially this holds. Suppose it holds before a transition. The function x -> t-D(s,x) is 1-Lipschitz in D by the triangle inequality. The pointwise maximum of this function and the old 1-Lipschitz h is again 1-Lipschitz: if both component values at x are <= their respective values at y plus D(x,y), their maximum has the same inequality, and exchange x,y. Thus h' restricted to S is 1-Lipschitz and nonnegative.

All new edges w_y>=h'_y. For any old z, w_y+D(y,z)>=h'_y+D(y,z)>=h'_z, so b_z>=h'_z. Assign h'_q=0. A shortcut through q has length b_z+b_z'>=h'_z+h'_z'>=|h'_z-h'_z'|; the old path bound gives the same inequality for D(z,z'). Their minimum D'(z,z') therefore preserves the Lipschitz constraint. Also D'(q,z)=b_z>=h'_z. This completes induction and proves h_x<=D(s,x).

In particular the activation values satisfy

    D(s,x)<=a_x<=2D(s,x).                                   (A3)

This is a rigorous geometric restriction on the history thresholds. It does not determine their law or eliminate them.

### Distance-cone representation and recovery of the history (proved)

Let v_0,...,v_{m-1}=s be the discovery prefix and tau_j its step from v_j to v_{j+1}, j=0,...,m-2. In the current visited metric D,

    h_x=max(0, max_{0<=j<=m-2}(tau_j-D(v_j,x))).              (A2b)

Proof by induction. The initial maximum is empty and h=0. Suppose the identity holds before a step of length t from s to q. The old-metric update h'_x=max(h_x,t-D(s,x)) is the stated cone maximum in the old metric, with the new departure added. Since D'<=D on old vertices, replacing D by D' can only increase that cone maximum. Conversely, (A2) after the update gives h'_x>=h'_{v_j}-D'(v_j,x)>=tau_j-D'(v_j,x) for each old departing vertex: h never decreases at an old vertex, and its height was at least its departure length immediately after that departure. The same bound holds for the new departure, since h'_s=t. This proves that the new cone maximum is <=h' at every old vertex, hence equality there. At q, (A2) gives 0=h'_q>=tau_j-D'(v_j,q) and >=t-D'(s,q), so all cone values are nonpositive and their maximum with zero is zero. Induction proves (A2b).

The entire discovery prefix can itself be recovered by running NUV on the current metric D over S from the original start. At an earlier discovery step j, its original shortest path to v_{j+1} uses only the then-visited vertices and its final cut edge, all contained in S, and has length tau_j. Thus D(v_j,v_{j+1})=tau_j: restriction to S cannot produce a shorter path than the original full graph. Every other vertex of S not yet visited at that earlier time had full-graph distance >=tau_j (strictly greater almost surely), so its distance in D is also >=tau_j. Inductively the greedy choices in D reproduce the original prefix and its lengths. This uses the current metric on S, not a recomputation in the smaller earlier induced graphs.

Consequently h and s are deterministic functions of D and the original start. After suppressing outside labels, the chain can be represented on rooted finite metrics alone, with the cone heights recomputed from their NUV prefix. This is an exact sufficient-state reduction; the metric state still grows with n. Reconstructing NUV inside the state is not a local characterization of its edges and does not establish mixing.

## 3. Long-step expectation estimate (proved)

Let T_i be the n-1 NUV step lengths. Then

    limsup_{n->infinity} E[n^(-1)sum_i (T_i-R)_+]
       <=24 exp(-R/8), R>=0.                                (A4)

The estimate is uniform over the choice of starting vertex, even one chosen after seeing the graph. It is stronger than tightness and is not inferred from tightness.

### Explicit expected covering bound

For n>=8, 0<=r<=log n, let N_n(r) be the minimum number of radius-r balls covering all vertices. Choose s=ceil(n exp(-r/4)) centers with fixed labels and append every uncovered vertex as a center. By exchangeability, for any vertex v outside the chosen labels, conditional on J=|B(v,r)|, its other J-1 ball labels form a uniform subset of the n-1 other vertices. The probability of avoiding the s centers is at most exp[-(s/n)(J-1)]: sampling without replacement can only decrease avoidance probability, and 1-s/(n-1)<=exp(-s/n).

The FPP ball exploration has independent interarrival times of rates j(n-j)/n. Until its size reaches M=floor(n/2), these rates are at least j/2. Coupling the holding times with the same independent unit exponentials shows J stochastically dominates min(Z,M), where Z is the rate-1/2 Yule population at time r, geometric with parameter p=exp(-r/2). For q=s/n,

    E exp[-q(J-1)]
      <= E exp[-q(Z-1)] + exp[-q(M-1)]
      <= p/(1-exp(-q)) + exp(-s/4)
      <= p(1+1/q) + exp(-s/4)
      <=2 exp(-r/4)+exp(-n^(3/4)/4).

The capped-Yule inequality follows by splitting Z<=M and Z>M, or pointwise bounding the capped exponential by its uncapped value plus the cap value. M-1>=n/4 for n>=8; s>=n^(3/4) on the stated r interval. The reciprocal inequality follows from exp(q)>=1+q. If s=n, there are no outside vertices and the covering bound below is immediate without applying the avoidance calculation. Therefore

    E N_n(r)/n<=3 exp(-r/4)+1/n+exp(-n^(3/4)/4).             (A5)

### Diameter moment

Let A be the maximum distance from one fixed root. Its FPP exploration gives A=sum_{j=1}^{n-1} Q_j with independent Q_j~Exp(rate j(n-j)/n). Since n/[j(n-j)]=1/j+1/(n-j),

    EA=2H_{n-1}, Var(A)<=4 sum_{j>=1}j^(-2)<=8.

The final inequality uses sum_{j>=1}j^(-2)<=1+integral_1^infinity x^(-2)dx=2. The graph diameter Delta<=2A, so

    E Delta^2<=16 H_{n-1}^2+32.                             (A6)

### Tail of step lengths

The source's deterministic metric-entropy observation (PDF p.4, equation (3)) gives #{i:T_i>2r}<=N_n(r). For completeness: in any radius-r ball, let z be its last discovered vertex. Every other discovered vertex in the ball has, at its departure, an unvisited vertex in that ball and hence a step <=2r by the greedy rule and triangle inequality. Assign each vertex to one ball in a minimal covering. At most one departure >2r occurs per assigned ball. Every step is <=Delta, so

    sum_i (T_i-R)_+ <=2 integral_{R/2}^{Delta/2}N_n(r)dr,

where an integral with upper endpoint below its lower endpoint is interpreted as zero. No integral of N_n(r) is extended to infinity, since N_n(r) stays at least one.

Put b=log n. For fixed R and sufficiently large n, b>=R/2. The part below b, bounded with (A5), has normalized expected value at most

    24 exp(-R/8)+2b[1/n+exp(-n^(3/4)/4)].

The remaining part is at most N_n(b)Delta/n. Since N_n(b)^2<=n N_n(b), Cauchy–Schwarz, (A5) and (A6) bound its expectation by

    sqrt[(3n^(-1/4)+1/n+exp(-n^(3/4)/4))
          (16H_{n-1}^2+32)] = O(n^(-1/8)log n).

This tends to zero and proves (A4). The same finite-n calculation holds when R=log n, giving an O(n^(-1/8)log n) bound on the normalized expected excess above log n.

## 4. Exact predictable-drift reduction (proved)

Let F_i be the exploration information immediately before step i, and let its state produce Z_i and u_i=k_i/n. Define

    m_i^R=E[min(T_i,R)|F_i]
          =integral_0^R exp[-u_i Z_i(t)]dt,
    m_i=E[T_i|F_i]
          =integral_0^infinity exp[-u_i Z_i(t)]dt,
    A_n=(1/n)sum_i m_i.

Each m_i is finite because Z_i(t)>=t and u_i>0. The differences min(T_i,R)-m_i^R are martingale differences bounded in absolute value by R. Orthogonality gives

    E|n^(-1)sum_i (min(T_i,R)-m_i^R)|^2 <= R^2/n.

The expectation of n^(-1)sum_i(m_i-m_i^R) equals the expected normalized excess step length. By the triangle inequality,

    E|L_n/n-A_n| <= R/sqrt(n)
                       +2 E[n^(-1)sum_i(T_i-R)_+].          (A7)

Taking n to infinity with R fixed, then R to infinity in (A4), proves L_n/n-A_n ->0 in L1. Using the finite-n tail bound with R=log n gives the stronger quantitative bound O(n^(-1/8)log n).

Consequently L_n/n converges in probability to a deterministic finite c **if and only if** A_n does; this equivalence follows by Markov's inequality on (A7) and the triangle inequality for convergence in probability. Also E A_n=E L_n/n exactly for each n. The unpredictable one-step exponential noise has been controlled; the random evolution of the state-dependent drift has not.

### End effects can be discarded

For any set I of at most eta n step indices, even chosen after seeing the graph, the pointwise bound

    n^(-1)sum_{i in I} T_i <=eta R+n^(-1)sum_i(T_i-R)_+

and (A4) give a limsup expectation bound eta R+24exp(-R/8). Choosing R=8log(1/eta) for 0<eta<1 gives 8eta log(1/eta)+24eta, which tends to zero. Thus the first/last eta n steps can be discarded uniformly as eta decreases. The same bound in expectation holds for deterministic sets of indices for m_i, by conditional expectation. This avoids leaving an uncontrolled small-u terminal regime in any future drift LLN argument.

### Stronger second-moment and L2 reduction (proved)

The covering argument actually gives

    limsup_n E[n^(-1)sum_i T_i^2]<=384,                      (A9)
    limsup_n n E|L_n/n-A_n|^2<=384.                         (A10)

To prove it, first bound the fourth moment of the diameter. Write the fixed-root radius A=sum_j mu_j E_j with mu_j=n/[j(n-j)], E_j~Exp(1), and B=sum_j mu_j=2H_{n-1}. Convexity of x^4 gives pointwise (A/B)^4 <=sum_j(mu_j/B)E_j^4. Since E E_j^4=24, E A^4<=24B^4; Delta<=2A therefore gives

    E Delta^4<=6144 H_{n-1}^4.

Now integrate the deterministic step-count inequality with a factor 2t:

    n^(-1)sum_i T_i^2 <=(8/n) integral_0^(Delta/2) r N_n(r)dr.

For r<=b=log n, (A5) bounds its expectation by

    8 integral_0^b r[3exp(-r/4)+1/n+exp(-n^(3/4)/4)]dr
      <=384+4b^2[1/n+exp(-n^(3/4)/4)].

For r>b, monotonicity bounds the contribution by N_n(b)Delta^2/n. Cauchy–Schwarz, N_n(b)^2<=nN_n(b), the fourth-moment estimate and (A5) bound its expectation by

    sqrt[(3n^(-1/4)+1/n+exp(-n^(3/4)/4))
          6144 H_{n-1}^4] ->0.

This proves (A9). For every finite n the steps are square-integrable since they are bounded by the diameter. Consequently the untruncated differences T_i-m_i are square-integrable martingale differences, orthogonal across i. Thus

    E|L_n/n-A_n|^2
      =n^(-2)sum_i E Var(T_i|F_i)
      <=n^(-2)sum_i E T_i^2,

which proves (A10). In particular the earlier L1 error bound can be improved to O(n^(-1/2)) by Cauchy–Schwarz. These are fluctuations around a *random predictable drift*, not concentration around a deterministic mean.

The normalized length and drift have uniformly bounded second moments over n>=2. Indeed (sum_i T_i/n)^2<=sum_i T_i^2/n by Cauchy–Schwarz; the analogous inequality for m_i, followed by conditional Jensen E m_i^2<=E T_i^2, gives the same bound for A_n. The asymptotic bound (A9) and finiteness at each of the finitely many remaining n imply uniform boundedness. Therefore if either L_n/n or A_n converges in probability to a finite deterministic c, both converge to c in L1 as well: for any K, Cauchy–Schwarz or the second-moment tail bound gives uniform integrability, and truncation plus convergence in probability gives L1 convergence. This does not assert L2 convergence to c.

### Higher moments and an equivalent pair of missing conditions (proved)

The same calculation extends to each positive integer p:

    limsup_n E[n^(-1)sum_i T_i^p]<=3 p! 8^p.                (A11)

Here are the details rather than an appeal to analogy. Convexity as above gives E Delta^(2p)<=(4H_{n-1})^(2p)(2p)!. The layer-cake formula and departure-count inequality give

    n^(-1)sum_i T_i^p
      <=(p2^p/n) integral_0^(Delta/2) r^(p-1)N_n(r)dr.

The part below b=log n has expected value at most

    3p2^p integral_0^infinity r^(p-1)exp(-r/4)dr
       +2^p b^p[1/n+exp(-n^(3/4)/4)]
     =3p!8^p+o(1).

The integral equals 4^p(p-1)!, by substituting r=4z and repeated integration by parts in the gamma integral. The remaining part is at most N_n(b)Delta^p/n; Cauchy–Schwarz bounds its expectation by sqrt[(E N_n(b)/n)E Delta^(2p)]=O(n^(-1/8)(log n)^p), which tends to zero. This proves (A11). No p growing with n is allowed.

Finite convexity/Jensen implies uniformly bounded p-th moments of L_n/n and A_n for every fixed p. In particular their fourth moments are bounded. A probability limit to deterministic c therefore implies L2 convergence: squared errors are uniformly integrable since their second moments (the fourth moments of the original errors) are bounded, and truncation of squared errors proves the implication. The earlier second-moment paragraph alone did not suffice for this conclusion; it is (A11) with p=4 that supplies it.

Thus the source mean-field probability and expectation programme would be settled by proving both

    c_n=E L_n/n=E A_n -> c,  and  Var(A_n)->0.               (A12)

Conversely a deterministic probability limit of L_n/n forces (A12), using the L2 equivalence, fourth-moment bound and (A10). Condition (A12) is therefore an equivalent pair of missing assertions, not a proved conclusion. Bounding the martingale innovations alone proves neither assertion.

## Precise remaining task

Prove that the random average of explicit drift functions

    A_n=(1/n)sum_i integral_0^infinity
          exp[-(k_i/n)sum_x(t-D_i(s_i,x)-h_{i,x})_+]dt

converges to a deterministic number, and identify it. The metric-threshold state grows with n. Neither (A2) nor exponential innovations proves mixing, ergodicity, convergence of empirical states, or concentration of this drift. Applying a standard Markov-chain ergodic theorem without proving those hypotheses would be invalid. Approach B remains an alternative route to that missing state-law theorem.

## 5. Exact small case and a falsified simplification (proved)

After the first discovery, let X be its step length. X~Exp(lambda), lambda=(n-1)/n. The current visited metric has two vertices at distance X, and its old-root height is X, so its two activation values are 0 and 2X. With u=(n-2)/n, the conditional mean next step is

    m(X)=integral_0^(2X) exp(-ut)dt
          +integral_(2X)^infinity exp[-u(2t-2X)]dt
        =1/u-(1/(2u))exp(-2uX).

Since E exp(-cX)=lambda/(lambda+c), the exact sum of the first two expected step lengths for n>=3 is

    n/(n-1)+n/(n-2)
        -[n/(2(n-2))] [(n-1)/(3n-5)].                       (A8)

For n=3 these are all the steps, so E L_3=15/4. For n tending to infinity, the second expected step tends to 5/6.

A proposed closure that discards the threshold field while keeping the visited metric would use activation values 0 and X instead. Its conditional next-step mean would be 1/u-(1/(2u))exp(-uX). Its error in the second-step expected length tends to

    (1/2)[1/2-1/3]=1/12>0.

Thus treating visited-to-unvisited edges as fresh exponentials after each discovery is false even in an early-step limiting calculation. This does not prove a nonzero discrepancy in the *bulk* length constant, since two initial steps have vanishing normalized contribution. It does rule out invoking memorylessness while ignoring the accumulated lower thresholds.

For a general state, (A3) also gives the valid comparison

    m_0(u)<=m(u)<=2m_0(2u)<=2m_0(u),
    m_0(v)=integral_0^infinity
             exp[-v sum_x(t-D(s,x))_+]dt.

Proof: (A3) implies sum_x(t-2D(s,x))_+<=Z(t)<=sum_x(t-D(s,x))_+. The upper comparison follows by substituting t=2z in the first exponent. Monotonicity of m_0 in its positive argument gives the last inequality. These factor comparisons do not show the threshold error tends to zero or identify the state law.


## Final checks and disposition

Both proposed new approaches were saved before the finite calculation; Approach A was pursued through exact transition, cone-field, tail/moment and drift-reduction proofs, while Approach B remains unpursued. All deterministic finite checks passed; quadrature warnings were resolved by independent integration with breakpoints. ThresholdUpdate.lean compiled with exit 0. SECOND_REFEREE.md records the conditioning, moment, limit and formalization checks and their scope.

Final verdict: PARTIAL. The exact missing mean-field assertions are (A12), with no demonstrated ergodic/hydrodynamic mechanism for the growing metric state. No full proof or counterexample to the intended light-tailed three-model programme was obtained.
