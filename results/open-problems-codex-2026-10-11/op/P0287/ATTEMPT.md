# P0287 research record — 2026-10-12

## Model and scope

Configurations are eta in {0,1}^Z. At rate one on each bond i,i+1, 10 changes to 01. At rate kappa>0, an occupied site 0 is set to 0. For a cylinder function f,

L f = sum_i eta_i(1-eta_(i+1))[f(eta^(i,i+1))-f(eta)] + kappa eta_0[f(eta^0)-f(eta)].

The graphical construction gives the usual Feller process on the compact product space. Only finitely many terms of L act on each cylinder. The workshop report, PDF p.5, asks about invariant measures of this model without specifying densities at infinity. Full classification includes correlated positive-through-current laws; the results below do not solve that problem.

## 1. Current identities (proved)

For any invariant probability mu, put p_i=mu(eta_i), J_i=mu[eta_i(1-eta_(i+1))]. Since eta_i is bounded and local, invariance gives mu(L eta_i)=0. Directly, L eta_i=eta_(i-1)(1-eta_i)-eta_i(1-eta_(i+1))-kappa 1_(i=0)eta_0. Thus J_(i-1)-J_i=kappa 1_(i=0)p_0. Therefore J_i=J_- for i<=-1, J_i=J_+ for i>=0, and J_-=J_++kappa p_0. All currents are nonnegative.

## 2. Classification of zero-incoming-current laws (proved)

If J_-=0, the preceding identity forces J_+=p_0=0. For each integer i, the nonnegative variable eta_i(1-eta_(i+1)) has zero expectation, so it is zero almost surely. Countable intersection implies every adjacent pair is ordered eta_i<=eta_(i+1), simultaneously. Also eta_0=0 almost surely. Every such binary configuration is either all zero or b^(m), with b^(m)_i=1_(i>=m) for an integer m>=1: if it contains a 1, the set of 1 sites is upward closed and bounded below by 1, hence has a minimum m. Conversely every one of these configurations has no 10 bond and eta_0=0, so every clock leaves it fixed. Hence precisely all probability mixtures of delta_empty and delta_(b^(m)), m>=1, have J_-=0. The extremal invariant laws in this sector are these point masses. This includes many nonempty invariant laws, but no stationary flow.

## 3. Product law necessity, including degenerate densities (proved)

Suppose mu is the independent product of Bernoulli(r_i), 0<=r_i<=1. For any i write a=r_(i-1), b=r_i, c=r_(i+1), d=r_(i+2), j_i=b(1-c). Define delta_i=1_(i=0). The two marginal generator expectations are

A_i=a(1-b)-b(1-c)-kappa delta_i b,
A_(i+1)=b(1-c)-c(1-d)-kappa delta_(i+1)c.

The internal jump leaves eta_i eta_(i+1) zero before and after; only the exterior bonds and killing contribute. Thus

B_i=a(1-b)c-bc(1-d)-kappa(delta_i+delta_(i+1))bc.

Subtracting c A_i+b A_(i+1) gives B_i-c A_i-b A_(i+1)=b(1-c)(c-b)=J_i(r_(i+1)-r_i). All three expectations are zero under stationarity, so J_i(r_(i+1)-r_i)=0. No division by a possibly zero density was used.

If J_->0, every edge i<=-1 has positive J_i and hence r_(i+1)=r_i. Consequently r_i=r for every i<=0, with 0<r<1. If also J_+>0, every edge i>=0 has positive current, so all r_i=r, giving J_-=J_+ and kappa r=0, a contradiction. Thus J_+=0. In particular r(1-r_1)=0, and r>0 forces r_1=1. Inductively, J_i=0 forces r_(i+1)=1 whenever r_i=1, so r_i=1 for all i>=1. The current identity now reads r(1-r)=kappa r; cancelling the strictly positive r yields r=1-kappa. Necessarily 0<kappa<1.

If J_-=0, Section 2 applies. An independent law supported on the ordered configurations has at most one site with density strictly between 0 and 1: if r_i>0, the equation r_i(1-r_(i+1))=0 forces r_(i+1)=1 and then all later densities equal 1. Also r_0=0. Hence its possibilities are the empty point mass, deterministic b^(m) with m>=1, and a single random interface site m>=1, with sites below m empty, sites above m occupied, and eta_m Bernoulli(theta), 0<theta<1. The last law is theta delta_(b^(m))+(1-theta)delta_(b^(m+1)) and is itself a product law.

## 4. Sufficiency of the positive-current product law (proved)

Let 0<kappa<1 and r=1-kappa. Consider mu_kappa with iid Bernoulli(r) on i<=0 and deterministic 1 on i>=1. It is supported on the closed set in which the entire right half is full; jumps at bond 0 and all later bonds are disabled. Its left restriction is TASEP on the negative half-line with removal at its right endpoint 0.

First verify an exact finite approximation. On [a,0], a<=0, use ordinary internal bonds, injection at a at rate r if empty, and removal at 0 at rate 1-r. The product Bernoulli(r) is stationary. Indeed, for any function f of this block, change of variables in its finite product sum gives

E[eta_i(1-eta_(i+1))(f(swapped)-f)] = E[(eta_(i+1)-eta_i)f].

The weights of 10 and 01 are equal since both site densities are r. For injection, changing eta_a from 0 to 1 gives E[r(1-eta_a)(f(eta_a=1)-f)]=E[(eta_a-r)f]. For removal, changing eta_0 from 1 to 0 gives E[(1-r)eta_0(f(eta_0=0)-f)]=E[(r-eta_0)f]. Summing internal bonds telescopes to E[(eta_0-eta_a)f], which the two boundary terms cancel. If a=0 there are no internal bonds and the two boundary terms cancel directly. Zero expected generator for every function on this finite state space implies stationarity by the finite forward equation.

Now let a tend to minus infinity. Initialize the finite block with its stationary product law; couple it with the infinite half-line initialized with iid Bernoulli(r), using identical initial states and identical graphical clocks on their common sites and bonds. The injection mechanism at a can differ from the infinite incoming bond, but that discrepancy can affect a fixed observation block [b,0] by time T only if there is an ordered nearest-neighbor clock path from the left boundary to that block. If n=b-a, it must cross the n intervening distinct bonds in order. The expected number of such ordered choices of ringing times is T^n/n!, so the probability is at most T^n/n!. (The discrepancy propagation under the TASEP update is local, and any crossing from left to right must use those bond clocks.) This tends to zero for fixed T,b. Thus the finite stationary cylinder distributions converge at time T to the infinite process cylinder distributions, and these are still the initial product distributions. This proves invariance for every T>=0. Adding the frozen occupied right half proves mu_kappa invariant for the original full-line process.

Its densities at infinity are rho_-=1-kappa, rho_+=1. Its currents are J_-=kappa(1-kappa)>0, J_+=0, and p_0=1-kappa. It has no transmitted flow to the right; the incoming flow is entirely removed. This is a special case, not the classification of arbitrary flowing laws.

Combining Sections 2–4 gives a complete classification **within independent Bernoulli laws**: the zero-current products listed in Section 3, and, only for 0<kappa<1, the one law mu_kappa.

## 5. Reduction of the entire zero-outgoing-current sector (proved)

Let mu be invariant with J_+=0. For each i>=0 the expected number of accepted jumps on bond i during [0,T] is T J_i=0, by stationarity and the Poisson compensator. That nonnegative integer count is therefore zero almost surely. Taking a countable intersection over i and positive integer T shows that the entire right half (sites >=1) remains unchanged almost surely along a stationary trajectory. At each fixed time, absence of 10 on all bonds i>=0 also holds almost surely. In particular eta_0<=eta_1, and eta_1=1 implies every site >=1 is occupied.

The event A={eta_1=0} is time-invariant along this stationary trajectory. If mu(A)>0, conditioning on A preserves stationarity: for any bounded measurable f, E[f(eta_t)1_A(eta_0)]=E[f(eta_t)1_A(eta_t)]=mu(f1_A). Under this conditional law, eta_0=0 almost surely and the outgoing current is zero. Section 1 then gives zero incoming current as well. Section 2 shows that the conditional law is a mixture of the empty configuration and b^(m) with m>=2, since eta_1=0 excludes m=1.

On A^c, every site >=1 is occupied. Conditioning again preserves stationarity. The coordinates <=0 evolve autonomously as half-line TASEP with extraction kappa at the endpoint 0, because the attempted hop 0 to 1 is always blocked. Conversely any stationary law of this half-line extraction process, extended with all sites >=1 occupied, is stationary for the full-line killing process. Together with arbitrary frozen mixtures from A this describes **all laws with J_+=0**, by reduction to half-line invariant measures. It is a reduction, not an explicit classification of those half-line measures.

The change of variables zeta_j=1-eta_(1-j), j>=1, reflects space and interchanges particles and holes. A left-half-line particle jump maps to a rightward zeta jump, and killing at eta_0 maps to injection at zeta_1 at rate kappa. Thus the remaining half-line problem is precisely the ordinary semi-infinite TASEP with injection kappa and no removal at the left endpoint. Semi-infinite ASEP literature is directly relevant to this sector; it does not settle J_+>0 for the full-line model.

## 6. Finite through-flow computations (numerical evidence only)

`finite_flows.py` builds the complete generator of an open interval of n=3,5,7,9 sites, centered at the killing site, with injection alpha=0.3 at its left boundary, extraction beta=0.7 at its right boundary, unit-rate internal bonds, and kappa=0.4,1,2 at its center. For each of the 12 chains it solves pi Q=0 and sum pi=1 with dense double-precision linear algebra. Matrices have at most 512 states, far below 1 GB. Nonnegativity and residuals <1e-10 are asserted, as is J_left-J_right=kappa p_0. Details, adjacent covariances, timings and residuals are in `finite_flows.json`.

For n=9 the outgoing currents are approximately 0.1445473, 0.1016973, 0.0686258 for kappa=0.4,1,2 respectively. These computations concern finite open systems and give no proof of a positive limiting current as n tends to infinity. Boundary values alpha and beta are injection/extraction rates, not asserted tail densities of the full-line model. A few short intervals do not justify extrapolation or uniqueness claims.

## 7. Elementary bounds and tail exclusions (proved)

The current formula gives J_+<=p_0 and J_-=J_++kappa p_0. Also J_-=E[eta_(-1)(1-eta_0)]<=1-p_0. Hence

J_++(kappa+1)p_0<=1, p_0<=1/(kappa+1), and J_+<=1/(kappa+2).

For the last inequality use p_0>=J_+ in the first. For the occupancy bound discard J_+>=0 in the first. In particular transmitted current vanishes uniformly over all invariant laws as kappa tends to infinity. These bounds need no assumptions about independence or tails. If p_0=0 then J_+=0 and hence J_-=0, so Section 2 applies; every invariant law with positive incoming current has p_0>0 and a strictly positive current loss.

If an invariant law is supported on configurations with finitely many particles, then eta_i tends to 0 as i tends to minus infinity, pointwise. The bounded bond variable is <=eta_i, so dominated convergence gives J_-=0. Section 2 then leaves only the empty state, since each b^(m) has infinitely many particles. If a law is supported on configurations with finitely many holes, eta_i tends to 1 as i tends to minus infinity, and the bond variable is <=1-eta_(i+1); again J_-=0. But none of the configurations classified in Section 2 has finitely many holes, so no such invariant law exists. No finite first moment of the total number of particles or holes is needed for these arguments.

## 8. Explicit correlated killed-flow laws for every kappa>0 (proved)

This constructs a larger family in the frozen-right sector, guided by the q=0 case of Sasamoto–Williams, arXiv:1204.1114, Theorems 4.1 and 5.1. We give the positivity, consistency and stationarity arguments directly, without assuming their formulas classify all half-line laws.

Define C_kappa=kappa(1-kappa) if 0<kappa<=1/2, and C_kappa=1/4 if kappa>=1/2. Fix 0<c<=C_kappa and put t=c/kappa. Work in the free real algebra on letters D,E, with the relation DE=c(D+E). A normal word contains no DE and hence is E^a D^b. Reducing any DE decreases word length. The reduction has a unique linear normal form: induct on word length; two possible first occurrences of DE never overlap, and expanding both in either order yields the same four shorter words with coefficient c^2. Induction then identifies their final reductions. Thus all choices of reductions agree. This also proves compatibility of normal reduction with concatenation and linear combinations.

Set H_0=1, H_1=1-t, and H_n=H_(n-1)-c H_(n-2) for n>=2. Define a linear functional g on normal words by g(E^a D^b)=t^a H_b, and on arbitrary words by their unique normal forms. Clearly g(empty word)=1, g(EY)=t g(Y), and

g(XDEY)=c[g(XDY)+g(XEY)].

The left-boundary identity follows because prepending E to a normal form creates no DE; reduction relations are compatible with concatenation. To check right consistency g(YD)+g(YE)=g(Y), first let K_b=g(D^b E). Then K_0=t=H_0-H_1; for b>=1, the final DE relation gives K_b=c H_b+c K_(b-1). Induction implies K_b=c H_(b-1)=H_b-H_(b+1). For a normal Y=E^aD^b, right consistency now reads t^a(H_(b+1)+K_b)=t^aH_b. By linearity and concatenation compatibility it holds for every word Y.

We next prove H_n>0. If c<1/4 let s=sqrt(1-4c), lambda_+=(1+s)/2, lambda_-=(1-s)/2. Both roots are positive, their sum is 1 and product is c. The parameter restriction implies lambda_-<=kappa: this is immediate if kappa>=1/2; otherwise 1-4c>=(1-2kappa)^2 and s>=1-2kappa. Consequently H_1=1-c/kappa>=1-lambda_+=lambda_-. The recurrence and its two initial values give

H_n=lambda_-^n+A(lambda_+^n-lambda_-^n), A=(H_1-lambda_-)/(lambda_+-lambda_-)>=0.

Indeed this expression has the correct initial values and each root satisfies lambda^2=lambda-c, so induction verifies the recurrence. It is strictly positive for every n. If c=1/4, the parameter restriction forces kappa>=1/2, H_1>=1/2, and instead H_n=[1+n(2H_1-1)]2^(-n)>0, again verified by substituting the initial values and recurrence. Since t>0, c>0 and every reduction expansion has positive coefficients, g(w)>0 for every word w.

For a binary word of hole occupancies zeta_1,...,zeta_n, let X_j=D when zeta_j=1 and X_j=E when zeta_j=0, and define nu_n(zeta)=g(X_1...X_n). Right consistency gives nu_(n+1)(wE)+nu_(n+1)(wD)=nu_n(w); iterating from g(empty)=1 also gives total mass 1. These strictly positive, consistent finite probabilities define a probability law nu_(kappa,c) on the semi-infinite lattice by the usual extension theorem. This specifies every cylinder, not just a mean density.

Here is a fully finite stationarity argument leading to the infinite law. On sites 1,...,n take internal TASEP bonds, injection kappa at site 1, and removal at site n with the state-dependent rate

b_n(wD)=c g(w)/g(wD),

where w is the first n-1 letters. These are finite strictly positive rates for each fixed n. Only the terminal site changes at a removal, even though the rate depends on the prefix. Define h(E)=c, h(D)=-c. For a target word w, the internal bond at i contributes to its forward-equation residual

h(X_i)g(w with position i deleted)-h(X_(i+1))g(w with position i+1 deleted).

For ED the term is the positive incoming g(...DE...)=c[g(...D...)+g(...E...)]; for DE it is its negative outgoing counterpart; for EE and DD the two terms cancel. Summing the bonds telescopes to h(X_1)g(X_2...X_n)-h(X_n)g(X_1...X_(n-1)). Injection contributes -h(X_1)g(X_2...X_n) because kappa g(EY)=c g(Y). Terminal removal contributes h(X_n)g(X_1...X_(n-1)) by its defining rate. All residuals therefore vanish. This covers n=1 as well: there are no internal bonds and injection/removal cancel. Hence nu_n is stationary for this finite Markov chain.

Couple the finite chain initially under nu_n with semi-infinite TASEP initially under nu_(kappa,c). Common initial coordinates are identical; use the same injection clock and the same unit-rate internal clocks. Any discrepancy originates at the terminal site n. For it to reach an observation block 1,...,L by time T, it must cross bonds n-1,n-2,...,L in that temporal order. The probability is at most T^(n-L)/(n-L)!, by counting ordered ringing times on these distinct rate-one clocks. Although terminal rates depend on the prefix, their updates still change only site n; the bound is independent of their magnitude or dependence. The bound tends to zero. Since all finite chains are stationary, their common fixed cylinder marginals converge to those of the semi-infinite process and prove invariance of nu_(kappa,c) at every time.

Its injection current is kappa nu(zeta_1=0)=kappa g(E)=c. Its current at every bond j,j+1 is

g((D+E)^(j-1)DE)=c g((D+E)^j)=c,

where expansion of D+E sums over the unspecified prefix, and repeated right consistency gives g((D+E)^j)=1. Applying the inverse reflection eta_i=1-zeta_(1-i) for i<=0, and freezing eta_i=1 for i>=1, produces an invariant full-line law mu_(kappa,c), with

J_-=c>0, J_+=0, and p_0=c/kappa.

Its downstream tail density is exactly 1. Its upstream law is specified by the entire cylinder formula above and the parameter c; no unproved asymptotic upstream density is asserted. In particular nonempty stationary killed flow exists for **every** kappa>0. When 0<kappa<1 and c=kappa(1-kappa), g reduces to independent holes of density kappa, recovering Section 4. For kappa>=1 every law in this positive-current family is necessarily nonproduct, by Section 3.

`halfline_checks.py` independently checks all words through length 8 for six exact rational (kappa,c) pairs: positivity, normalization, consistency, the left identity, every DE reduction location, finite forward-equation residuals, and current c on each bond. All 48 cases pass. These tests do not prove infinite positivity; the root argument above does.

## 9. Further attempt: positive transmitted flow and restricted uniqueness

The user requested another serious attempt. Its two previously untried approaches, full proofs and additional referee audit are in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md). The attractive-coupling approach was pursued; the alternative two-sided defect matrix ansatz was recorded but not used as a premise.

Theorem A there proves, for every kappa>0 and 0<rho<1, actual weak convergence from iid Bernoulli(rho) to a canonical greatest invariant law dominated by that product law. It has strictly positive transmitted current, with

J_+ >= [rho(1-rho)-kappa rho^(n+1)]/(1+kappa n) for every n>=1.

Choosing rho=1/[2(1+kappa)] yields J_+>=1/[4(1+kappa)^2]>0. Theorem B independently constructs infinite-volume stationary limits from finite reservoirs with injection rho and extraction 1-rho and the same current bounds. These results remove the earlier positive-through-flow existence gap, without extrapolating numerical data.

Using the classical homogeneous TASEP invariant classification as an explicitly identified external theorem, Theorem C establishes the Bernoulli(rho) upstream local tail and exact incoming current rho(1-rho) for rho<=1/2. Theorem D proves uniqueness among invariant laws globally dominated by Bernoulli(rho) with that incoming current. Thus the finite-reservoir stationary laws converge to the canonical law in this low-density range. Neither the global domination condition nor the low-density restriction is silently omitted.

Additional exact checks: 9 local ordered updates, 16,380 finite Boolean run identities, 50,000 finite path events, 8 rational stationary finite chains, and exhaustive resource-sufficient color reachability through length 9. CouplingChecks.lean passed with exit 0 for the new local coupling and current algebra. Full records and dependency limitations are in SECOND_ATTEMPT.md and LITERATURE.md.

## Hostile-referee checks

1. **Accidental independence assumption:** Sections 1, 2, 5, 7 use only invariance, nonnegativity and bounded local observables. Independence is assumed explicitly only in Sections 3 and 4.
2. **Dividing at an endpoint:** Section 3 divides by r only after positive incoming current forces 0<r<1. All zero/one-density cases were retained in the exact covariance enumeration.
3. **Killing covariance term/sign:** Four-site enumeration directly builds jumps and removals and computes the three derivatives independently of the claimed identity. All 768 exact rational cases pass. `ProductChecks.lean` verifies the polynomial identity for arbitrary real parameters.
4. **Local balance mistaken for stationarity:** The product-law sufficiency proof checks all functions on every finite approximation, not just one- and two-site observables; graphical convergence then establishes invariance at every time of the infinite process. Twenty-four exact forward-equation tests and a nonzero-residual negative control confirm the finite telescoping step.
5. **Finite approximation boundary contamination:** The distance-to-boundary clock-path estimate T^n/n! is explicit and tends to zero. No convergence of a finite stationary current is assumed.
6. **Conditioning on a noninvariant event:** Section 5 first proves zero expected accepted-jump counts on every right bond, so the entire right half is unchanged on stationary paths. Only then is conditioning on eta_1 justified. Conditional current identities are applied to the resulting invariant law.
7. **Misidentifying the boundary under particle-hole reflection:** zeta_1=1-eta_0, so killing becomes injection, not extraction. A 10 particle pair on increasing original coordinates becomes a 10 hole pair on increasing reflected coordinates after reversing their order.
8. **Overclaiming formal verification:** Lean checked five algebraic/Boolean theorems, exit code 0, with no sorry and no native_decide. It did not formalize graphical construction, conditioning, product measures, or classification. The full infinite-process arguments above remain ordinary mathematical proofs.
9. **Finite numerical data mistaken for an infinite theorem:** Section 6 is explicitly finite. Positive currents on 9 sites do not prove positive limiting current or identify tail densities. Rate-limited literature services are recorded as gaps, not negative search results.
10. **Signed matrix weights:** Section 8 proves strict positivity for every word, including the repeated-root case c=1/4. The restriction on c is essential; there is no appeal to a possibly signed stationary measure. Its finite stationary approximations have actual positive removal rates.
11. **Ambiguous word reduction or inconsistent cylinders:** Section 8 proves reduction independence by induction on word length and proves right consistency on normal words, then extends it linearly. The independent exact checks verify every possible first DE reduction through length 8, not only the selected recursive reduction.

## Remaining gap

After the second attempt, positive transmitted flow exists for every kappa>0; a canonical family, low-density upstream-tail identification, and uniqueness under a stated global Bernoulli domination condition are proved. The missing part is an **exhaustive classification of arbitrary correlated invariant laws**, including laws outside that domination condition, downstream tail identification and uniqueness for general prescribed pairs of tail densities. The J_+=0 sector reduces exactly to standard half-line laws plus frozen mixtures, but Section 8's explicit half-line family is still not shown here to exhaust all half-line invariant measures. See SECOND_ATTEMPT.md for the complete updated gap, new proofs and referee audit.
