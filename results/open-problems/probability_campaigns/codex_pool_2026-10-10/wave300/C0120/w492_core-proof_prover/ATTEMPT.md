C0120 core proof attempt — w492 — 2026-10-10

This is a reduction and obstruction packet, not a solution of C0120. Current openness and novelty are UNKNOWN. The exact source model and quantified target are in STATEMENT.md.

Prior-attempt digest

The cited intake's C0120-A001 records the disorder-chaos route but proves no polynomial decorrelation rate. Its use of log Z in general dimension is broader than the cited Gaussian 1+1 zero-temperature model. The H/I attempt directories have no targeted C0120 result in the text/JSON/Lean scan; the Lean directory only repeats the ranking. Team O's board has no C0120 row. No claim that all owner work was exhaustively checked is made.

Lemma L1: exact Gaussian spectral energy and overlap representation

Let V_n={(i,j): i,j>=0, i+j<=n-1}. Work with independent standard Gaussian coordinates g_v, v in V_n. Let M_n be exactly as in STATEMENT.md. Let M_n-E M_n=sum_{k>=1} F_{n,k} be its orthogonal decomposition into total-degree k Gaussian Hermite chaoses, and put a_{n,k}=E[F_{n,k}^2]. Then

  sum_{k>=1} k a_{n,k}=n,
  Var(M_n)=sum_{k>=1} a_{n,k},
  Q_n(t):=E|P_n(g) intersect P_n(g^t)|
           =sum_{k>=1} k a_{n,k} exp(-(k-1)t),  t>=0,

where g^t=exp(-t)g+sqrt(1-exp(-2t))g' and g' is independent, and P_n is the almost surely unique maximizer.

Proof. Distinct paths have different incidence vectors, so their energy difference is a nondegenerate Gaussian. There are finitely many pairs, hence almost surely no ties. M_n is a finite maximum of linear functions of Euclidean gradient norm sqrt(n); it is sqrt(n)-Lipschitz and belongs to Gaussian W^{1,2}. Away from the union of tie hyperplanes its weak derivative is partial_v M_n=1_{v in P_n(g)}. Therefore ||grad M_n||^2=n almost surely.

Use the normalized product Hermite basis H_alpha, in which partial_v H_alpha=sqrt(alpha_v) H_{alpha-e_v}. If c_alpha is the coefficient of M_n, Gaussian W^{1,2} gives E||grad M_n||^2=sum_alpha |alpha| c_alpha^2. One may justify the derivative expansion by integration by parts against each Hermite polynomial, followed by Parseval for the weak derivatives; bounded gradient and linear growth give the needed integrability. Grouping by |alpha| proves the first two formulas.

Mehler's operator acts on degree r as multiplication by exp(-rt). Applying that to each derivative expansion yields E[partial_v M_n(g) partial_v M_n(g^t)]=sum_alpha alpha_v c_alpha^2 exp(-(|alpha|-1)t). Summing v gives the overlap formula. All series have nonnegative coefficients with finite total n, so limits and the sum are justified. In particular Q_n is nonnegative and nonincreasing. Integrating its series against exp(-t)dt gives Var(M_n)=int_0^infinity exp(-t)Q_n(t)dt. This does not assume independence of path choices across time layers.

Lemma L2: polynomial escape of gradient spectral mass is sufficient

For any integer K>=1 define D_n(K)=sum_{1<=k<=K} k a_{n,k}. Then

  Var(M_n) <= D_n(K)+n/(K+1),
  D_n(K) <= K Var(M_n).

Proof. The low-degree variance sum is at most D_n(K). For k>K, a_{n,k}<=k a_{n,k}/(K+1), and the total gradient energy is n by L1. The reverse inequality follows termwise from k<=K. No bound on D_n(K) is assumed in this proof.

Consequently if, for some a,b>0 and C<infinity, D_n(floor(n^a))<=C n^(1-b) for all sufficiently large n, then Var(M_n)<=(C+1)n^(1-min(a,b)). Conversely Var(M_n)<=C n^(1-epsilon) implies D_n(floor(n^(epsilon/2)))<=C n^(1-epsilon/2). Thus polynomial spectral escape is equivalent, with a possible exponent loss, to the desired polynomial improvement.

Lemma L3: finite-noise stability versus spectral mass

For K>=1 and t>=0,

  Q_n(t)<=D_n(K)+n exp(-Kt),
  D_n(K)<=exp((K-1)t) Q_n(t).

Proof. In L1's series, for k<=K the exponential is at most 1 and at least exp(-(K-1)t); for k>K it is at most exp(-Kt). Sum the nonnegative terms. This connects the missing spectral bound with disorder-chaos estimates without deriving a new rate from the target variance itself.

The single hardest remaining input G1

Prove that there exist a,b>0 and C,n_0<infinity such that

  sum_{k=1}^{floor(n^a)} k ||Proj_k(M_n-E M_n)||_2^2 <= C n^(1-b)
  for every n>=n_0 in the exact Gaussian quadrant/free-endpoint model.

G1 is UNPROVED. L2 is a proved conditional reduction, not a proof of its premise. Gaussian hypercontractivity alone produces logarithmic spectral escape and supplies no polynomial cutoff bound here. The origin coordinate contributes exactly 1 to degree-one energy, which is compatible with any exponent b<=1 and must not be discarded.

Attempt at G1 and boundary of the available method

The available source variance bound gives only D_n(K)<=C K n/log n by L2. At K=floor(n^a) this is weaker than the trivial D_n(K)<=n, so using it to obtain G1 is circular and ineffective. Vertex marginal influences and Euclidean Lipschitz control are the natural elementary inputs, but they do not by themselves force a power gain. The next proof step is an explicit parallel-corridor Gaussian maximum obstruction to that proposed generic inference; a lattice-specific input would still be needed.

Review status: L1-L3 have complete analytic proofs written by w492, not an independent audit or a formal-check receipt. Referee w494 pending. No admitted placeholders are being counted as proof.

Lemma L4: small vertex influences do not force a power improvement

Consider a different directed acyclic graph, consisting of a common root and m disjoint corridors, each with n-1 further vertices. The only admissible paths take the root and an entire corridor. Give every vertex an independent standard Gaussian weight. For n>=2 and m>=8 the path maximum is

  T_{n,m}=g_0+sqrt(n-1) U_m,  U_m=max_{1<=j<=m} G_j,

with independent standard Gaussian g_0,G_1,...,G_m. Its weak gradient has squared norm n almost surely; each nonroot vertex belongs to the maximizer with probability 1/m. Nevertheless, for an absolute c>0,

  1+c(n-1)/log(2m) <= Var(T_{n,m}) <= 1+2(n-1)/log m.

Lower bound proof. Let u solve Phi(u)^m=1/2. For m>=8, u>1, since Phi(1)<0.9 and 0.9^8<1/2. A union bound and the Gaussian Chernoff tail imply u^2<=2 log(2m). Set h=1/u and r=1-Phi(u)=1-2^(-1/m). The inequality 1-exp(-x)>=x/2 for 0<=x<=log 2 implies mr>=(log 2)/2.

The elementary Mills bounds x phi(x)/(x^2+1)<=1-Phi(x)<=phi(x)/x, x>0, imply

  [1-Phi(u+h)]/[1-Phi(u)]
     >= [u(u+h)/((u+h)^2+1)] exp(-uh-h^2/2)
     >= exp(-3/2)/5 =: r_0.

The last step uses u>=1, u(u+h)>=u^2, and (u+h)^2+1<=5u^2. The upper Mills bound follows by integrating x phi(x)/u; the lower follows from integration by parts in the Gaussian tail and bounding the residual integral by the tail divided by x^2. Thus this step requires no extreme-value limit theorem.

It follows that P(U_m>=u+h)>=1-exp(-r_0 log(2)/2)=:p_0>0. For an independent U'_m, the two events (U_m<=u,U'_m>=u+h) and their reversal are disjoint and each has probability p_0/2 or more. Consequently Var(U_m)=(1/2)E(U_m-U'_m)^2>=p_0/(2u^2)>=p_0/(4 log(2m)). Take c=p_0/4. Independence of the common root gives the stated lower bound for T.

Upper bound proof. The Gaussian hypercontractive event inequality is E[1_A(G)1_A(G^t)]<=P(A)^(2/(1+exp(-t))). It follows by writing the left side as ||P_{t/2}1_A||_2^2 and applying the standard Gaussian hypercontractivity inequality from L^{1+exp(-t)} to L^2. This is a named analytic input, also used in the primary paper's hypercontractive method; no formal certificate for that input is claimed.

For A_j={G_j is the unique maximizer}, P(A_j)=1/m. The Gaussian covariance identity therefore gives

  Var(U_m)<=int_0^infinity exp(-t) m^{-tanh(t/2)}dt
           =int_0^1 m^{-(1-rho)/(1+rho)}d rho
           <=int_0^1 exp(-(1-rho)log(m)/2)d rho
           <=2/log m.

Combining root independence and the two bounds proves L4. The elementary lower-bound portion alone suffices for the obstruction.

With m=n the nonroot marginal influences equal 1/n and Var(T_{n,n}) is of logarithmic order n/log n. If D^corr_n(K) denotes its Hermite gradient spectral energy, the same proof as L2 gives D^corr_n(K)>=Var(T_{n,n})-n/(K+1). For every fixed a,b>0, at K=floor(n^a) this is >=c n/(4 log(2n)) for all sufficiently large n, and therefore cannot be O(n^(1-b)). The factor 4 is a harmless weakening absorbing n-1 and the tail term.

Scope. This graph is not the nearest-neighbor quadrant lattice and L4 is not a counterexample to C0120. It disproves a generic inference based only on path length, Gaussianity, gradient energy n, and small nonroot vertex influences. The actual lattice geometry must supply additional information to prove G1.

Review status: L1-L4 are author-written analytic proofs pending w494's independent review. G1 remains the sole rate gap. No solved-parent or novelty claim.

NEXT: Freeze the packet, run a bounded one-dimensional consistency check of L4, and submit concept-only draft nodes for independent review.
