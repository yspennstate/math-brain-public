# P0211: uniform relaxation order for linear polymers

Date: 2026-10-11. This is an original proof in this folder, not a claim of a solution already in print.

## Exact statement and result

For n>=2 and beta>0, let S_n={m: m_j nonnegative integers, sum j*m_j=n}. Each unordered pair of different clusters merges at rate 2/n. Each of the j-1 internal links of a size-j linear polymer splits at rate beta. Thus a j-cluster splits into i,j-i at rate 2 beta m_j for i<j/2, and beta m_j for i=j/2. The reverse rates are 2m_i m_{j-i}/n, or m_i(m_i-1)/n when i=j/2. Write gamma_M for the smallest positive eigenvalue of minus the continuous-time generator, and tau=1/gamma_M.

**Theorem.** For every n>=2 and beta>0, put s=beta+sqrt(beta)+1/n. Then

    s/6 <= gamma_M <= 4s,
    1/(4s) <= tau <= 6/s.

In particular beta_n comparable to 1/n gives tau=Theta(sqrt(n)). The constants in the uniform theorem do not depend on n or beta. Other regimes are tau=Theta(n) when beta is at most order n^-2, tau=Theta(beta^-1/2) when n^-2 << beta << 1, and tau=Theta(beta^-1) when beta is bounded below by a positive constant. For fixed beta the sharper source asymptotic lower bound remains available. No sharp asymptotic constant is claimed. The n=1 chain has one state and no positive spectral gap, so is explicitly excluded.

The source is Aldous's 'A special aggregation-fragmentation process', section 1 of coag_frag_mix.pdf, PDF pages 1-4. Proposition 1 concerns fixed beta as n tends to infinity. The page-4 remark specifically poses the gap between orders sqrt(n) and n at beta_n~b/n. Our theorem answers that question and supplies uniform orders for all positive beta.

## 1. Reversible edge representation, without claiming strong lumpability

Let Omega be the NONEMPTY subsets of the n labelled edges of a cycle. For S in Omega, put k=|S|. Each absent edge is added at rate beta, and each present edge is removed at rate (k-1)/n. Removal from a singleton has rate zero; the empty set is not a state. Call this generator L_B.

The mass per subset

    pi_B(S) = Z_B^-1 (beta*n)^k/(k-1)!

is reversible: across S -> S+{i}, its ratio is beta*n/k, while the reverse removal rate is k/n, so pi_B(S)*beta=pi_B(S+{i})*k/n. The chain is irreducible because one can add to the union of two nonempty sets and then remove to the target.

Cut the edges in S and let p(S) be the unordered multiset of segment lengths, represented by m in S_n. The number of subsets with p(S)=m and k clusters is

    N(m)=n*(k-1)! / product_j m_j!.

To see this, count pairs consisting of a cut set and a distinguished cut. There are k choices of the distinguished cut. Conversely choose its vertex location (n choices) and an ordered list of the k segment lengths (k!/product m_j! choices). Therefore k*N(m)=n*k!/product m_j!. This also applies at k=1 and k=n. The pushforward of pi_B is consequently

    pi_M(m) proportional to (beta*n)^k / product_j m_j!.

Conditioned on m, the cut set is uniform, or equivalently the segment lengths are in uniform cyclic order. Fragmentation rates are already the desired rates in each configuration: two internal cut locations yield i,j-i if i<j/2 and one if i=j/2, for each j-segment. When k>=2 and i!=j, the expected number of boundaries joining an i-segment to a j-segment is 2m_i m_j/(k-1): at each of the k boundaries the two distinct positions sample the multiset without replacement. Each boundary disappears at rate (k-1)/n, giving 2m_i m_j/n. For equal sizes the expected number is m_i(m_i-1)/(k-1), giving m_i(m_i-1)/n. At k=1 all merge rates are zero. The formulas include k=2, where the same pair of clusters has two boundaries.

For any function f on S_n and F=f composed with p, stationary conditional expectation therefore gives

    E_piB[L_B F | p(S)=m] = L_M f(m).

It follows exactly that Var_piB(F)=Var_piM(f), and the reversible Dirichlet forms satisfy

    E_B(F,F)=-E_piB[F L_B F]=E_M(f,f).

In particular gamma_M>=gamma_B. A second fact will be useful: every such F is invariant under rotating the labelled cycle. If a Poincare bound holds for all rotation-invariant observables of B, it also holds for M, by this exact identity. Nothing here asserts that p(B(t)) is a Markov process for every edge initial condition; that stronger lumpability assertion is unnecessary and generally false.

## 2. Finite positive-function comparison and the count chain

We use two elementary finite-state facts. A killed generator A has nonnegative off-diagonal entries and A*1=-V, with V>=0. Its exponential preserves coordinatewise positivity: add a sufficiently large multiple of the identity to make all entries nonnegative and expand the exponential in its power series. If h>0 and A h<=-c h, positivity and integration give

    exp(t A) h <= exp(-c t) h.

Indeed the derivative of exp(t(A+cI))h is exp(t(A+cI))(A+cI)h<=0. Since 1<=h/min(h), the survival probability starting at any state is at most (max h/min h)*exp(-c t).

If the off-diagonal graph of A is irreducible, Perron-Frobenius applied to A+dI gives a strictly positive eigenvector v with A v=-lambda v, where lambda is the smallest eigenvalue of -A whenever its spectrum is real. For any h>0,

    min_i(-A h/h)_i <= lambda <= max_i(-A h/h)_i.

At a coordinate minimizing v_i/h_i, positivity of off-diagonal entries gives A v_i >= (v_i/h_i) A h_i, which yields the upper inequality; the maximizing coordinate gives the lower one. This proves the comparison. In our applications the spectra are real because the matrices are reversible birth-death matrices, or are similar to restrictions of a reversible generator. A one-dimensional matrix is covered directly.

The number K of clusters of M is an actual Markov coordinate: total fragmentation rate is beta(n-K) and total merging rate K(K-1)/n. Its generator Q on {1,...,n} has rates

    lambda_k=beta(n-k),    mu_k=k(k-1)/n.

Every nonconstant count observable is an admissible polymer test function, so gamma_M<=gamma_Q by the variational principle.

Let (Dg)_k=g(k+1)-g(k), k=1,...,n-1. Expanding both sides gives

    D Q g = A_0 D g,

where the killed generator A_0 has birth beta(n-k-1), death k(k-1)/n, and killing

    lambda_k-lambda_{k+1}+mu_{k+1}-mu_k=beta+2k/n.

Terms outside 1,...,n-1 have zero coefficient. The derivative is an isomorphism from functions modulo constants onto R^(n-1). Hence the eigenvalues of -A_0 are exactly the nonzero eigenvalues of -Q, including multiplicity. Its principal eigenvalue is gamma_Q. Applying the comparison to h=1 yields

    gamma_Q >= beta+2/n.

For the upper bound put a=max(1,n*sqrt(beta)) and

    h(k)=1/[(k+a)(k+a+1)].

The two ratios are h(k+1)/h(k)=(k+a)/(k+a+2) and h(k-1)/h(k)=(k+a+1)/(k+a-1). Substitution and cancellation give exactly

    -A_0 h(k)/h(k)
      =2 beta(n-k-1)/(k+a+2) + beta + 2 k a/[n(k+a-1)]
      <=2 beta*n/a + beta + 2a/n.

Here a>=1 ensures k/(k+a-1)<=1. If a=n*sqrt(beta), the last bound is beta+4sqrt(beta). If a=1, then beta*n<=1/n, so it is at most beta+4/n. Therefore

    gamma_M <= gamma_Q <= beta+4 max(sqrt(beta),1/n) <= 4s.       (U)

This argument requires no central limit theorem, stationary variance estimate, or interchange of n and beta limits.

## 3. Boolean-lattice decomposition and a rotation-invariant Poincare bound

We give the algebraic decomposition in full, to account for a slow labelled mode that cannot be used to bound polymer relaxation in the very small beta regime.

Let V_j be the real functions on j-subsets of [n], with counting inner product. Define the upward map U:V_j->V_{j+1} by

    (Ua)(T)=sum_{i in T} a(T-{i}),

and its adjoint D:V_j->V_{j-1} by

    (Da)(R)=sum_{i notin R} a(R+{i}).

Use V_-1=0. Direct double counting gives, on V_j,

    D U - U D = (n-2j) I.                                   (C)

Indeed the diagonal terms in DU count n-j extensions; those in UD count j deletions. Every off-diagonal term on either side exchanges one present and one absent element and has exactly the same coefficient.

For j<n/2,

    ||Ua||^2=||Da||^2+(n-2j)||a||^2,

so U is injective and its adjoint D at the next level is surjective. For 0<=l<=floor(n/2), define H_l=ker(D:V_l->V_{l-1}). Then

    dim H_l=binom(n,l)-binom(n,l-1),

where binom(n,-1)=0. The surjectivity needed at l follows from injectivity at l-1<n/2.

For a in H_l, induction using (C) proves

    D U^j a = j(n-2l-j+1) U^(j-1) a.                        (R)

For j=1 this is (C) with Da=0. For the inductive step, commute D past the final U at level l+j-1 and add n-2(l+j-1) to the preceding coefficient (j-1)(n-2l-j+2); the sum is j(n-2l-j+1). In particular U^j is injective on H_l for 0<=j<=n-2l: taking an inner product with U^(j-1)a gives a positive scalar times its squared norm at every step. At j=n-2l+1 the same norm identity gives U^j a=0.

On the layer of k-subsets define

    F_a(S)=sum_{T subset S, |T|=l} a(T)=U^(k-l)a(S)/(k-l)!.

It is nonzero as a map H_l->V_k for l<=k<=n-l and is zero on other layers. For l<h, the layer subspaces U^(k-l)H_l and U^(k-h)H_h are orthogonal: moving k-h upward maps across the inner product gives a scalar multiple of <U^(h-l)a,b>, which is zero since Db=0 and h-l>=1. Their dimensions, summed over l<=min(k,n-k), telescope to binom(n,k). Thus they form an orthogonal decomposition of the ENTIRE layer V_k. This proves both completeness and absence of any unaccounted sectors. The stationary weight pi_B is constant within each layer, so the same subspaces are orthogonal for the stationary inner product.

The sector of degree l consists of functions with, at layer k, an arbitrary vector from H_l lifted by F. Equivalently, choose a basis of H_l and multiply each F_a by an arbitrary radial function g(k) on l<=k<=n-l. Degree 0 has k=1,...,n because the empty state was excluded. Each such sector is preserved by L_B. To compute the action, observe

    sum_{i in S} F_a(S-{i})=(k-l)F_a(S),
    sum_{i notin S} F_a(S+{i})=(n-k-l)F_a(S).

The first formula counts each l-subset k-l times. For the second, the terms already inside S contribute (n-k)F_a(S). The remaining terms sum a(R+{i}) over (l-1)-subsets R of S and i outside S. Harmonicity says that sum is the negative of the sum with i inside S but outside R; the latter counts each l-subset l times. This proves the second formula; for l=0 it holds directly.

Consequently L_B(F_a g)(S)=F_a(S) A_l g(k), with

    A_l g(k)= beta(n-k-l)[g(k+1)-g(k)]
             +(k-1)(k-l)/n [g(k-1)-g(k)]
             -[l beta+l(k-1)/n]g(k).                       (H)

The zero boundary coefficients make this a killed birth-death generator on l,...,n-l. For l>=2 the killing is at least

    l beta+l(l-1)/n >= 2beta+2/n.

All eigenvalues of -A_l are at least this number. One can either apply the positive-function comparison to the principal eigenvalue with h=1, or, for any real eigenvector, evaluate at a coordinate of maximal absolute value and use nonnegative off-diagonal rates. Degree 0 is exactly Q, whose nonconstant eigenvalues are at least beta+2/n by Section 2.

It remains to exclude degree 1 from a rotation-invariant function. At every nontrivial layer its degree-1 part is uniquely

    sum_{i in S} a_i(k),    with sum_i a_i(k)=0.

Uniqueness follows from the injectivity just proved. Rotation invariance forces the coefficient vector to be fixed by the n-cycle, hence every a_i(k) is equal. Its zero sum then forces every coefficient to be zero. Orthogonal projection onto a degree sector commutes with rotation: the sector and its orthogonal complement are both preserved by relabelling, as is the stationary inner product. Thus the degree-1 part of an invariant function is itself invariant and must vanish. Degree 1 is zero already at k=n.

The complete orthogonal decomposition, sector invariance and reversibility now show, for every mean-zero rotation-invariant F,

    E_B(F,F) >= (beta+2/n) Var_piB(F).

Only the constant degree-0 vector has eigenvalue zero, since Q is irreducible. Apply this to lifted polymer functions using Section 1 to obtain

    gamma_M >= beta+2/n.                                   (L0)

This is a bound on polymer observables, not on all labelled-edge observables. For example at extremely small beta, the latter have slow degree-1 modes.

## 4. A direct reciprocal certificate for every spectral sector

Assume n>=8 and 4/n^2<=beta<=1/16. Put a=n*sqrt(beta), so 2<=a<=n/4. We prove gamma_B>=sqrt(beta)/5 by the complete sector decomposition, avoiding any probabilistic tail approximation.

For degree 0, its positive spectrum is that of A_0 from Section 2. Use h(k)=1/(k+a). Direct substitution gives

    -A_0 h(k)/h(k)
      =beta(n-k-1)/(k+a+1)-k(k-1)/[n(k+a-1)]+beta+2k/n
      >=beta(n-k-1)/(k+a+1)+beta+k/n.

The inequality uses a>=1 to bound k(k-1)/(k+a-1)<=k. If k<=a then n-k-1>=n/2 (n>=8,a<=n/4) and k+a+1<=5a/2. Thus the birth term is at least beta*n/(5a)=sqrt(beta)/5. If k>=a the last term k/n is at least sqrt(beta). It follows from positive-function comparison that every positive eigenvalue in degree 0 is at least sqrt(beta)/5.

For each degree l>=1, use the same h(k)=1/(k+a) on l<=k<=n-l in (H). Its exact certificate is

    -A_l h(k)/h(k)
      =beta(n-k-l)/(k+a+1) + l beta
       +(k-1)[(l-1)k+l a]/[n(k+a-1)].                      (S)

To verify the cancellation, combine the death contribution

    -(k-1)(k-l)/[n(k+a-1)]

with the killing contribution l(k-1)/n; their numerator is (k-1)[l(k+a-1)-(k-l)]=(k-1)[(l-1)k+l a]. All terms displayed in (S) are nonnegative on the sector domain.

If k<=a, then l<=k implies n-k-l>=n-2a>=n/2, while k+a+1<=5a/2. Its birth term is again at least sqrt(beta)/5. If k>=a, then [(l-1)k+l a]>=a and

    (k-1)/(k+a-1)>=1/3,

because 3(k-1)-(k+a-1)=2k-a-2>=a-2>=0. The last term in (S) is therefore at least a/(3n)=sqrt(beta)/3. Positive-function comparison proves the principal eigenvalue of every -A_l is at least sqrt(beta)/5, hence so are all their eigenvalues.

Completeness of the orthogonal sector decomposition now gives

    gamma_B>=sqrt(beta)/5,    gamma_M>=sqrt(beta)/5.         (L1)

This proof works at the boundary n=8,beta=1/16,a=2 and has no unknown concentration estimate. A fully written independent coupling proof is retained in Appendix A below; it obtains the same bound and was useful for independently checking factors in the generator.

## 5. Combine the bounds

The upper bound (U) is gamma_M<=4s. For the lower bound use (L0) throughout.

* If beta>=1/16, sqrt(beta)<=4beta, so s<=5beta+1/n<=5(beta+2/n)<=5gamma_M.
* If beta<=4/n^2, sqrt(beta)<=2/n, so s<=beta+3/n<=(3/2)(beta+2/n)<=(3/2)gamma_M.
* If n<8 and beta<1/16, sqrt(beta)<=1/4<=2/n, and the preceding estimate again applies.
* In all remaining cases n>=8 and 4/n^2<beta<1/16. Bound (L1) gives sqrt(beta)<=5gamma_M, while (L0) gives beta+1/n<=gamma_M. Therefore s<=6gamma_M.

The endpoint cases are covered by the weak inequalities in the previous sections. Hence gamma_M>=s/6. Inverting positive bounds proves the theorem for every n>=2,beta>0. There is no remaining mathematical gap in this order statement. The two independent proofs of (L1) are the direct sector certificate in Section 4 and the coupling argument in Appendix A.

## 6. Hostile-referee checks and limits of verification

1. Wrong state space: the edge chain excludes the empty set. Singleton removals have rate zero. The harmonic degree-0 sector also excludes layer zero. Checked explicitly in all constructions.
2. False lumping: segment-size projection need not be Markov for arbitrary edge starts. The proof uses exact stationary averaged conductances and Dirichlet forms, with the averaging count written out in Section 1.
3. Factor two in coalescence: the Stage II joint absorption rate is beta+r/n. The simultaneous marginal jumps are counted once. Exhaustive joint-generator marginal tests for n=2,...,7 give error at most 1.12e-16 (verify.py).
4. Missing angular modes: the Boolean-lattice decomposition is proved by the up/down commutator, dimension count and orthogonality. Rotation invariance removes degree 1 but does not remove degree>=2. Full edge spectra for n=2,...,9 at beta=1e-5,1/n,1,100 match the radial-sector spectra with their stated multiplicities; maximum discrepancy below 1e-11 (sector_checks.json).
5. Stationary distribution and transitions: independently enumerated partition generators have reversible symmetry discrepancy at most 1.45e-14 through n=28. beta=1/n gap/sqrt(beta) ranges from about 2.12 at n=2 to 1.916 at n=28 (numerics.json). These are numerical checks, not premises of the proof.
6. Reciprocal certificate: an independent grid n=8,9,16,31,100,1000,10000 and beta in [4/n^2,1/16] gives minimum killed-certificate/sqrt(beta) above 0.5001, versus the proved conservative bound 0.2. Algebraic identity and inequalities are also isolated in CouplingCertificate.lean; its actual checker result is recorded separately and is not assumed here.
7. Uniform prefactors: the coupling tail prefactor need not be uniform in n. This is sufficient because the spectral gap is the asymptotic exponential rate for each finite chain; the resulting lower bound on that rate is uniform.
8. Small and large parameters: no Gaussian approximation is used. The discrete-gradient identity and double-reciprocal weight give the upper gap bound uniformly, even beta much smaller than n^-2 or much larger than 1.
9. Formalization scope: the full Markov-chain proof is a written mathematical proof, not a full Lean formalization. The Lean file checks only selected finite algebraic certificates when its run succeeds. Numerical eigensolvers provide evidence only.

Reproducibility: fetch.py, search_more.py, search_final.py, fetch_lead.py store source and search payloads; verify.py constructs partition generators and exhaustive coupling checks; verify_sectors.py checks the harmonic spectral formula. All output and code are confined to this problem folder. No brain, ledger or git repository was modified.

## Appendix A. Independent coupling proof of (L1)

Assume n>=8 and 4/n^2<=beta<=1/16. Put a=n*sqrt(beta), so 2<=a<=n/4. We prove

    gamma_B >= sqrt(beta)/5, hence gamma_M>=sqrt(beta)/5.    (L1)

Stage I starts with X subset Y, Y-X one edge and |X|=k. At each common vacant edge add to both at rate beta. At each common occupied edge remove from both at rate (k-1)/n and remove from Y alone at rate 1/n. At the unique differing edge add to X at rate beta and remove from Y at rate k/n. The first marginal has exactly birth beta and death (k-1)/n per appropriate edge; the second has exactly birth beta and death k/n. Thus these are valid marginal generators. The pair stays in Stage I until becoming equal, or entering Stage II with equal sizes and two differing edges. Internal k births have rate beta(n-k-1), deaths k(k-1)/n, and total exit rate beta+2k/n. Denote this killed internal generator A_I; it coincides with A_0 of Section 2.

Stage II has |X|=|Y|=r+1 and one edge exclusive to each set. Add each common vacant edge to both at rate beta; remove each common occupied edge from both at rate r/n. At rate beta add the unique absent edge to EACH chain simultaneously, producing their union. At rate r/n remove the unique exclusive edge from EACH chain simultaneously, producing their intersection. Each chain has exactly one marginal jump in each such joint event, so the total absorption rate is beta+r/n, NOT twice this rate. If r=0 the removal event is absent and no empty state is produced. Internal r births have rate beta(n-r-2), deaths r^2/n; call this killed generator A_II.

For either stage use h(z)=1/(z+a). Its birth and death ratios give

    -A_I h(k)/h(k)
      =beta(n-k-1)/(k+a+1)-k(k-1)/[n(k+a-1)]+beta+2k/n
      >=beta(n-k-1)/(k+a+1)+beta+k/n,

because a>=1 makes the negative death term at most k/n in absolute value. For Stage II, exact cancellation gives

    -A_II h(r)/h(r)
      =beta(n-r-2)/(r+a+1)+beta+r(a-1)/[n(r+a-1)].

If z<=a, then n-z-2>=n/2, since a<=n/4 and n>=8. Also z+a+1<=5a/2 since a>=2. The birth contribution in either expression is therefore at least

    beta*n/(5a)=sqrt(beta)/5.

If k>=a the remaining Stage I term k/n is at least sqrt(beta). If r>=a, then r/(r+a-1)>=1/2 and a-1>=a/2, so the remaining Stage II term is at least a/(4n)=sqrt(beta)/4. All terms omitted in these estimates are nonnegative. Thus for c=sqrt(beta)/5,

    A_I h<=-c h,    A_II h<=-c h.

By the finite killed-semigroup argument of Section 2 each stage duration has, uniformly over its starting states, a tail at most C exp(-c t), where C is finite for the particular n,beta. For every 0<theta<c, integration of the tail gives

    E exp(theta T_i) <= 1+theta*C/(c-theta).

Stage I either couples directly or enters Stage II. The strong Markov property and the uniform exponential-moment bound for Stage II give a finite bound on E exp(theta T) for the total coupling time. Thus its tail is O(exp(-theta t)). Constants here may depend on n,beta; only the exponential rate matters for relaxation.

The coupling inequality bounds total variation between the distributions started at every adjacent pair of nonempty subsets by O(exp(-theta t)). Any two nonempty subsets can be connected through their union by a finite path of single-edge additions and removals that never passes through the empty set. The triangle inequality gives the same exponential rate for every pair of initial states.

For completeness, if L_B has an eigenfunction f with eigenvalue -lambda, and f(x)!=f(y), then

    exp(-lambda t)|f(x)-f(y)|
      =|E_x f(B_t)-E_y f(B_t)|
      <=2||f||_infinity * TV(P_x^t,P_y^t).

The established exponential bound forces lambda>=theta. Since this holds for every theta<c, gamma_B>=c. This proves (L1) without any typical-count assumption or incorrect Jensen substitution.


Additional final audit: final_audit.py independently checks stationary projected rates and subset counts for n=2,...,9 (rate errors below 4.89e-15; exact subset counts), and the double-reciprocal upper certificate and count curvature bounds for n=2,3,8,16,100,1000,10000 and 33 logarithmically spaced beta values from 1e-12 to 1e4. No bound violation was found (final_audit.json).

Formal-check status at completion: the specified lake env lean command was submitted from ~/lean_verify and remains queued for the shared Lean slot (tool session 68041). CouplingCertificate.lean contains seven algebraic lemmas without sorry or native_decide. No successful Lean check has yet been observed, so these are NOT labelled formally checked. The full theorem is supported by the complete written proof and the independent finite checks above; it is not represented as a full formalization. LEAN_CHECK.json records the certificate hash and this limitation.

The final direct spectral certificate was also evaluated at 4,298,280 (n,beta,l,k) grid points; its minimum ratio to sqrt(beta) was 0.501, exceeding the rigorously proved conservative 0.2. See all_sector_certificate.json.
