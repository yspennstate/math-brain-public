# P0110: terminal-bias bridge, with a supporting sphere

Status: conditional deductions and proved special cases, independently unchecked. P0110 is not solved. Current openness UNKNOWN; source recovery is recorded separately. No novelty is claimed for the classical KPZ inequalities.

## Target and precise provisional scope

The campaign intake asks for a nondegenerate iid undirected lattice FPP law with well-defined fluctuation and wandering exponents chi = 2 xi - 1. The primary conditional theorem is Auffinger--Damron, arXiv:1109.0523, Theorem 2.2: equality of the two global fluctuation exponents and of the two global wandering exponents is an assumption, not a conclusion about a particular law. Their model excludes an atom at the minimum of the support of size at least p_c(d).

For this attempt choose iid weights supported on [a,b], 0<a<b<infinity; Uniform[1,2] is an eligible concrete candidate, not a solved example. Let T be undirected lattice passage time, h(x)=E T(0,x), and g the FPP norm satisfying g(x)=lim_m h(mx)/m for lattice x. Let D(0,v) be the maximum Euclidean distance to the SEGMENT [0,v] over all minimizing paths. No unique-geodesic assumption is used below.

## Prior attempt and hypothesis comparison

The dated intake attempt at-p0110 computes n times (n^(xi-1))^2 = n^(2xi-1), conditional on curvature and on control of T-g. It explicitly leaves exponent existence and the error control open. A solved directed width-three strip in the owner memory is a different model and does not settle this target. The 2026 rotationally invariant results must also be checked for a lattice-iid transfer before use.

The useful reduction here is that one needs an upper bound on h(v)-g(v) only at the TERMINAL displacement v. The two interior nonrandom errors have the favorable sign. Furthermore, for at least one direction, a supporting Euclidean sphere supplies the geometric lower bound without assuming a particular iid limit shape has uniformly positive curvature. This is a specialization of the classical geometric mechanism, with explicit rounding and segment-distance details.

## L1: nonnegative mean bias

For every lattice x, b(x):=h(x)-g(x)>=0. Indeed h(mx)<=m h(x) by the triangle inequality and translation invariance; divide by m and take the defining limit. This uses neither independence of selected paths nor conditional-product estimates.

## L2: terminal-bias detour identity

Write X(x,y)=T(x,y)-h(y-x). If z belongs to ANY minimizing path from 0 to v, additivity on that path gives exactly

g(z)+g(v-z)-g(v) = b(v)-b(z)-b(v-z)+X(0,v)-X(0,z)-X(z,v).

Consequently the left side is at most b(v)+X(0,v)-X(0,z)-X(z,v), and at most b(v)+3s whenever the three centered errors have magnitude at most s. No upper bound on b(z) or b(v-z) is needed. All endpoints will be bounded on a deterministic set before taking a union bound; z is not treated as an independent or fixed random endpoint.

## L3: Euclidean detour inequality, including overshoot

For v!=0 let L=|v|, S=|z|+|v-z| and r=dist(z,[0,v]). Then S-L>=2r^2/S. Proof: if the projection of z onto the line through v lies in the segment, write its coordinate as t in [0,L] and perpendicular distance r. Convexity of t -> sqrt(t^2+r^2)+sqrt((L-t)^2+r^2) gives S>=sqrt(L^2+4r^2), hence S-L>=4r^2/(S+L)>=2r^2/S. If the projection lies outside the segment, r is the distance to the closer endpoint, the distance to the other endpoint is at least r, and S-L>=r. Thus S>=2r and the claimed bound follows. The case r=0 is immediate.

## L4: a lower curvature direction exists for every norm

Let rho=min_{|u|=1} g(u)>0 and choose a minimizing unit vector u. Then g(x)>=rho|x| for every x and g(u)=rho, by compactness and homogeneity. Equivalently the g-unit ball is contained in a Euclidean sphere tangent in direction u. This supplies a lower quadratic detour in that direction; it supplies no UPPER curvature bound, no explicit direction, and no exponent existence.

For integer n>=sqrt(d), choose v_n by rounding each coordinate of n u to a nearest integer. Put delta=sqrt(d)/2, K0=bd/2+rho delta, and L_n=|v_n|. Then |v_n-nu|<=delta, L_n>=n-delta>0, and

0 <= g(v_n)-rho L_n <= K0.

The upper bound uses g(v_n)<=ng(u)+g(v_n-nu)<=rho n+bd/2. This handles a minimizing direction that is irrational; no rational direction is assumed to attain the sphere contact.

Every minimizing path to v_n has at most (b/a)||v_n||_1 edges, since its time is at most b||v_n||_1 and each edge costs at least a. Minimizers exist: loops strictly increase time and only finitely many paths can meet this length bound. With C=(b/a)sqrt(d), any vertex z on such a path has S<=C L_n. L3 and the norm bound therefore give

g(z)+g(v_n-z)-g(v_n) >= (2rho/C) dist(z,[0,v_n])^2/L_n - K0.

This bound applies simultaneously to all minimizing paths, including vertices whose projection overshoots either endpoint.

## L5: finite-scale tail from a centered envelope and one terminal bias

Assume q>=0, alpha>0 and K>=1 satisfy, for every nonzero lattice w,

E exp(alpha |T(0,w)-h(w)| / |w|^q) <= K.

This is an extra input, not an estimate proved here for q=1/3. Let B_n=h(v_n)-g(v_n). Define the deterministic set Lambda_n={z in Z^d: ||z||_1<=(b/a)||v_n||_1}, and A_n=2|Lambda_n|+1. All path vertices lie in Lambda_n. For z in Lambda_n both |z| and |v_n-z| are at most (C+1)L_n. Translation invariance, exponential Markov, and a finite union bound give, for s>=0,

P(max{|X(0,v_n)|, |X(0,z)|, |X(z,v_n)|:z in Lambda_n}>s)
 <= A_n K exp(-alpha s/(((C+1)L_n)^q)).

Zero-displacement terms are identically zero and omitted from the moment hypothesis. There is NO independence assumption between these variables.

Combining L2 and L4 proves the finite-scale implication

P(D(0,v_n)>sqrt(C L_n (B_n+K0+3s)/(2rho)))
 <= min(1, A_n K exp(-alpha s/(((C+1)L_n)^q))).

The maximum over all minimizing paths causes no extra factor: all their vertices already belong to the same deterministic Lambda_n.

For any p>0 set s=(((C+1)L_n)^q/alpha) log(A_n K n^p). The right side is n^(-p). If B_n<=H n^q log(2+n), then D(0,v_n)=O(n^((1+q)/2) sqrt(log n)) with this polynomial tail, for any fixed p. This is an upper bound along the rounded support direction, not equality of global exponents or a lower bound on wandering.

## Hardest remaining gap

For ONE concrete law such as Uniform[1,2], prove a matched global-exponent theorem: chi_a=chi_b and xi_a=xi_b, with the uniform exponential upper bounds and variance/mean lower bounds in the primary definitions. The above bridge gives one side in a suitable direction from stated inputs. It neither proves matching nor supplies the reverse inequality unconditionally. Without the matching theorem, P0110 remains unresolved by this packet.

## L6: a refuted generic shortcut about the mean bias

Centered concentration plus abstract subadditivity alone cannot give the terminal bound. For 0<beta<1 let h(n)=n+n^beta for n>=1, h(0)=0, and T_n=h(n) deterministically. The concavity power inequality gives h(m+n)<=h(m)+h(n). The limiting slope is 1 and the centered variables vanish, so every centered exponential bound holds even with q=0. Yet h(n)-n=n^beta, which is not O(n^q log n) for q<beta. This is a countermodel to the GENERIC inference, not an iid lattice FPP example. Alexander's theorem has additional stochastic/geometric structure; that structure cannot be erased from a proof citation.

## L7: the lower curvature direction cannot be reused as an upper curvature direction

For g(s,t)=|s|+|t|, u=(1,0) minimizes g on the Euclidean unit circle and g(u)=1. For |t|<=1, g(u+(0,t))-g(u)=|t|>=t^2. But the ratio to t^2 is 1/|t|, unbounded as t tends to zero. Thus a supporting outer sphere giving a lower quadratic bound does not give an upper quadratic bound at the SAME direction. This norm example refutes that geometric substitution; it is not asserted to be the shape of Uniform[1,2] FPP.

## What the primary theorem supplies, and what it does not

Chatterjee's Theorem 4.1 states the nonrandom bound with a logarithm for every q>chi_a in its setup; the proof invokes the centered concentration input. Auffinger--Damron Lemma 4.1 states the corresponding epsilon-slack version in their setup. These can supply the terminal input when their hypotheses are respected, but are not proved here from an abstract subadditive sequence. Substituting such a bound into L5 and the GLOBAL lower-mean definition of xi_b recovers chi_a>=2xi_b-1: if q>chi_a and (1+q)/2<r<xi_b, the upper expectation bound along v_n contradicts E D(0,v_n)>=c|v_n|^r. The deterministic D<=C L_n and a polynomial tail with p large justify the expectation upper bound. This is a rederivation of a known conditional inequality, not a new result about a concrete law.

The retrieved brain card flagged Chatterjee's curvature hypotheses as UNKNOWN because its author had not read the Annals paper. The complete Theorem 1.1 hypothesis list has now been read: it does not list a separate uniform-curvature assumption. Proposition 5.1 and Section 6 instead use suitable contact directions. This is a proposed source clarification for the Claude reviewer, not an unreviewed edit of that theorem card. It does not remove the exponent-matching requirement.

## L8: variance-normalized tight concentration need not match fluctuation thresholds

This continuation addresses the remaining matching gap, not a new target. Let S={4^k:k>=1} and, for integers n>=0, set sigma_n=min(sqrt(n)/4, 1+dist(n,S)/4). Let epsilon be a single fair random sign shared by ALL n. Define tau_j=1+(sigma_j-sigma_(j-1)) epsilon, j>=1. Both functions inside the minimum are 1/4-Lipschitz on nonnegative integers, and their minimum has the same property. Since sigma_0=0, every tau_j lies in [3/4,5/4], and the unique path along the ray from 0 to n has passage time T_n=n+sigma_n epsilon. These edge weights are DEPENDENT and NONSTATIONARY, and the graph is a ray: this is not an iid Z^2 FPP counterexample.

Here E T_n=n, Var T_n=sigma_n^2, and E exp(alpha |T_n-E T_n|/sqrt(Var T_n))=exp(alpha) for every alpha>0 and n>=1. Thus concentration normalized by the actual standard deviation is uniformly tight, with zero nonrandom mean bias.

For n=4^k, k>=2, sigma_n=1. For n=2*4^k, the nearest element of S is 4^k and its distance is 4^k, so sigma_n=sqrt(n)/4. Also 1/4<=sigma_n<=sqrt(n)/4 for n>=1. Consequently the upper threshold a=inf{q: there is alpha>0 with sup_n E exp(alpha |T_n-E T_n|/n^q)<infinity} equals 1/2. The lower threshold b=sup{q: for some N, inf_(n>N) Var T_n/n^(2q)>0} equals 0. Indeed the midpoint subsequence forces a>=1/2 and the global upper bound gives a<=1/2; the anchor subsequence prevents b>0 and sigma_n>=1/4 gives b>=0. This refutes the GENERIC inference from variance-normalized tight concentration, path additivity, bounded positive weights and linear means to matching fluctuation thresholds. Iid/stationary lattice structure has not been preserved in this countermodel.

## L9: the exact additional variance regularity that would match chi

Let (T_v) be real random variables indexed by nonzero v in Z^d, with X_v=T_v-E T_v and 0<sigma(v)^2=Var T_v<infinity. Define chi_a by the uniform exponential upper threshold and chi_b by the uniform large-displacement variance lower threshold in STATEMENT.md. Suppose (i) some alpha>0, K<infinity satisfy sup_v E exp(alpha |X_v|/sigma(v))<=K; and (ii) there is chi>=0 such that, for EVERY eta>0, some c_eta,C_eta,R_eta>0 satisfy

c_eta |v|^(chi-eta) <= sigma(v) <= C_eta |v|^(chi+eta), for ALL |v|>=R_eta.

Then chi_a=chi_b=chi. Proof: for q>chi take eta=(q-chi)/2. The ratio sigma(v)/|v|^q is bounded for large v by (ii) and for the finitely many smaller lattice v by finiteness and positivity of sigma(v). Rescale alpha by that uniform ratio bound to obtain the upper exponential envelope, so chi_a<=chi. For q<chi take eta=(chi-q)/2 in the variance lower bound, proving chi_b>=chi. Finally chi_b<=chi_a for every such family: an upper exponential bound at exponent q implies E X_v^2<=2K |v|^(2q)/alpha_q^2, by e^t>=t^2/2. A variance lower bound at any r>q contradicts this as |v| tends to infinity. These three inequalities force equality.

The hypothesis is UNIFORM over all lattice displacements, not a fitted variance exponent on one ray or a subsequence. It is not proved here for Uniform[1,2]. L8 demonstrates why its regularity content cannot be erased. L9 addresses fluctuation matching only; wandering matching and the actual-law inputs remain unproved. No numerical experiment or formal check is claimed for L8--L9; both are exact written auxiliary deductions pending independent review.

NEXT: w383 audits L2--L5 and L8--L9; integrator obtains a different-model KEEP for C1. The next proof step is to isolate uniform two-sided variance power regularity for Uniform[1,2], without treating variance-normalized concentration alone as that regularity.
