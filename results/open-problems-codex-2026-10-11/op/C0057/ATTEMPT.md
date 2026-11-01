# C0057: research attempt, 2026-10-12

## Exact question and outcome

For every admissible critical face-weight sequence q on bipartite maps, every initial half-perimeter l >= 1, and every continuing adapted filled-in peeling algorithm A, does the exploration under P_infinity^(l) exhaust the map almost surely? Additional algorithmic randomness must be independent of the unexplored map. A deliberately stopping rule is excluded, as in the source.

SOLVED: Every continuing adapted filled-in peeling algorithm exhausts the infinite map for every admissible critical q. The universal proof below uses the exact positive-to-negative jump kernel and a localized martingale argument. It needs neither regular variation nor a finite second derivative. The finite-second-derivative proof and exact example are retained as independent special-case checks. This is a proof supplied here, not SOLVED_IN_LITERATURE.

Source.pdf PDF pp. 27, 48-49, 57, 60-61 (printed pp. 23, 44-45, 53, 56-57) were checked. The printed type interval in Corollary 27 includes 3/2, but type 3/2 is subcritical and the preceding paragraph excludes it from the infinite-plane perimeter chain. Type 2 in these notes is a specific explicit sequence, not every sequence with exponent 2.

## Source identities

Throughout, sum means an infinite sum over the indicated indices, integral means a Lebesgue integral, and pi is the circle constant. Write

    f(x) = sum_{k>=1} q_k binom(2k-1,k-1) x^(k-1),
    Z = Z_q, c = 4Z.

Admissibility means f(Z)=1-1/Z at the smallest finite positive solution Z. Criticality means Z^2 f'(Z)=1. Use the source's nondegenerate convention: some q_k>0 for k>=2. These imply Z>1 and q_1<1.

Put d(j)=4^(-j) binom(2j,j), j>=0, and h(j)=2j d(j), j>=1; h(j)=0 for j<=0. Thus d(j)~1/sqrt(pi*j), h(j)~2 sqrt(j/pi). If P_n is the half-perimeter, its transition kernel is

    K(x,y)=nu(y-x) h(y)/h(x), x,y>=1,
    nu(k-1)=q_k c^(k-1), k>=1,
    nu(-j)=2 W^(j-1) c^(-j), j>=1.

The source proves nu is a probability distribution, h is harmonic, and the underlying nu-walk oscillates for critical q (Lemmas 9, 11, Proposition 14). Section 3.3.3 identifies P with this walk conditioned to stay strictly positive. Each specified-side gluing event with finite half-perimeter k has probability

    b_infinity^(p)(*,k) = [nu(-k-1)/2] h(p-k-1)/h(p), 0<=k<=p-2.

The same formula holds on the other side, independently of the algorithm selecting the edge. Source (5.3), with (q_g)_k=q_k g^(k-1), gives

    W^(j)=d(j) integral_0^1 (g c_{q_g})^j dg.

## Universal argument: exact kernel and logarithmic convergence (new main result)

The full C0057 statement has an affirmative answer by the following argument. It uses no tail regular variation and no finite f'' hypothesis. Algebra checks and numerical stress tests passed; their limited scope is recorded below.

### 1. Exact positive-to-negative kernel

Budd, 'The peeling process of infinite Boltzmann planar maps', arXiv:1506.01590v3, Lemma 4, equation (40) (PDF p.16), and the displayed bipartite simplification on PDF p.17, give, in the half-perimeter notation of this attempt,

    nu(-k) = [d(k)/(2k-1)] T(k), k>=1,
    T(x) = sum_{m>=1} w_m/(m+x), x>0,
    w_m = m(2m+1)d(m) nu(m).

These formulas require criticality, not regularity. To check the conventions: define Budd's full-perimeter law nu_B(2m)=nu(m), nu_B(odd)=0, and use r=1. His bipartite kernel is

    R_1(2k,2m)=d(k)d(m) m(2m+1)/[(m+k)(2k-1)].

His h_1^(1)(2p) equals our h(p): summing his h_1^(0)(2j)=d(j) for j=0,...,p-1 gives 2p d(p). His c_plus is sqrt(c). Thus the kernel transfers exactly, without a parity average or missing factor. The null positive jump nu(0) is eliminated by harmonicity in Lemma 4; the sum starts at m=1.

Finiteness is automatic: harmonicity at p=1 says sum_{m>=0} nu(m)h(m+1)=1. Since h(m+1) is comparable to sqrt(m), sum_{m>=1} sqrt(m)nu(m)<infinity. Also w_m is comparable to m^(3/2)nu(m), so T(x)<infinity for each x>0. At least one nu(m)>0, m>=1, by nondegeneracy, so T(x)>0.

We will use constants that are independent of p and of tail oscillations. For k>=1 there are fixed constants a_0,b_0>0 such that a_0/sqrt(k)<=d(k)<=b_0/sqrt(k); this follows from Stirling's formula and adjusting finitely many k. Consequently

    nu(-k) is comparable to k^(-3/2)T(k),
    w_m is comparable to m^(3/2)nu(m),
    h(k) is comparable to sqrt(k).

Moreover, term by term,

    T(p)<=T(k)<= (p/k)T(p) if 1<=k<=p,
    (p/k)T(p)<=T(k)<=T(p) if k>=p.

Define the finite positive rate

    R(p)=p^(-1/2)T(p), p>=1.

R(p)<=R(1)<infinity, since both factors are decreasing.

### 2. Quantitative bounds at one state

There is a finite constant C such that, for all p>=1 (with a constant adjustment for p<8), the following hold:

    delta(p):=sum_{k>=p}nu(-k) <= C R(p),                 (A)
    sum_{1<=k<=p} k^2 nu(-k)/p^2 <= C R(p),             (B)
    sum_{1<=m<=p} m^2 nu(m)/p^2 <= C R(p),              (C)
    sum_{m>p/2} sqrt(m/p) nu(m) <= C R(p).              (D)

Proof of (A). For k>=p, nu(-k)<=C k^(-3/2)T(k)<=C k^(-3/2)T(p). Summing k^(-3/2) gives at most a constant times p^(-1/2), including p=1. The same argument with cutoff p/2 and T(p/2)<=2T(p) shows sum_{k>p/2}nu(-k)<=C R(p).

Proof of (B). Use T(k)<=(p/k)T(p) to get sum_{k<=p} k^2 nu(-k)<=C pT(p)sum_{k<=p} k^(-1/2)<=C p^(3/2)T(p). Divide by p^2.

Proof of (C). Since m<=p, m^2<=sqrt(p)m^(3/2). Further sum_{m<=p}w_m<=2p T(p), since m+p<=2p for these terms. Comparability of w_m yields sum_{m<=p}m^2nu(m)<=C p^(3/2)T(p). Divide by p^2.

Proof of (D). When m>p/2, m+p<3m and w_m/(m+p)>=c sqrt(m)nu(m). Thus sum_{m>p/2}sqrt(m)nu(m)<=C T(p); divide by sqrt(p). QED.

These bounds imply that under K(p,y)=nu(y-p)h(y)/h(p),

    K(p,{y:|y-p|>p/2}) <= C R(p).                     (E)

For downward jumps h(y)/h(p)<=1, so the bound follows from the negative tail above. For upward jumps m>p/2, the h comparison gives h(p+m)/h(p)<=C sqrt(m/p); use (D). This includes arbitrarily large upward overshoots and does not require their logarithmic moments to be finite.

The swallowing probability b(p) defined earlier satisfies

    b(p)>=c_0 R(p) for p>=p_0,                         (F)

for a fixed p_0. Indeed restrict k to ceil(p/2)<=k<=floor(3p/4). There are at least p/8 terms for large p; h(p-k-1)/h(p)>=c>0. For j=k+1 in this range, j is comparable to p and T(j)>=c T(p) (including the possible j>p for finitely many small p, absorbed into p_0). The exact kernel gives nu(-k-1)>=c p^(-3/2)T(p). Multiplication by the number of terms proves (F).

### 3. Escape to infinity, with a direct proof

The perimeter chain P_n tends to infinity almost surely. We prove this rather than relying only on source Proposition 13. Let V(p)=1/h(p). Directly from the h-transform,

    E[V(P_{n+1})|P_n=p]=[1-delta(p)]/h(p).

V is bounded and positive. Telescoping expectations gives

    E[sum_{n>=0} delta(P_n)/h(P_n)] <= 1/h(P_0)<infinity.

Therefore this sum is finite almost surely. The exact kernel and nonzero positive law imply nu(-k)>0 for every k>=1, so delta(p)/h(p)>0 at every finite state p. Each such state is thus visited finitely often almost surely. A countable union and then a finite union over p<=M show P_n>M eventually for every M. Hence P_n tends to infinity. QED.

### 4. Truncated log increments

Set U(p)=log h(p). At a transition p -> y define

    L(p,y)=[U(y)-U(p)] 1_{|y-p|<=p/2}.

This variable has a fixed absolute bound B. Indeed h(j+1)/h(j)=1+1/(2j). If |y-p|<=p/2, summing log(1+1/(2j)) over the intervening integers gives |U(y)-U(p)|<=C |y-p|/p; a universal constant works for all p, and the case p=1 has L=0. The transition h-ratio on this interval is also bounded above and below by constants.

Combining this Lipschitz bound with (B),(C),

    E_p[L(p,P_1)^2] <= C R(p).                        (G)

The finite-state adjustment is legitimate: L is bounded and R(p)>0 at each of finitely many exceptional p.

To bound the conditional mean without assuming integrability of the full log jump, write H=h(y)/h(p). The exact identity

    E_p[1-1/H]=delta(p)

holds: E_p[1/H]=sum_{j>-p}nu(j)=1-delta(p). The integrand is absolutely integrable because E_p[1/H]<=1.

On the large-jump set B_p={|y-p|>p/2},

    E_p[|1-1/H|;B_p]
       = sum_{y in B_p}nu(y-p)|H-1|
       <= K(p,B_p)+sum_{y in B_p}nu(y-p)
       <= C R(p).

The last step uses (E), the negative tail bound, and for positive jumps H>=1 so their untransformed mass is at most their K-mass. Thus the mean of (1-1/H) restricted to the small-jump set has absolute value at most C R(p), by (A).

For |u|<=B, Taylor's theorem gives |u-(1-exp(-u))|<=C_B u^2. On the small-jump set u=U(y)-U(p), while on its complement L=0. Apply (G) to the Taylor error to conclude

    |E_p L(p,P_1)| <= C R(p).                         (H)

This cancellation is the key step: summing positive small jumps alone would give the wrong rate. The reciprocal-h identity accounts for both signs and the killed mass delta(p).

### 5. The rate sum must diverge

We prove sum_n R(P_n)=infinity almost surely. Suppose instead it is finite on an event E. Let L_n=L(P_n,P_{n+1}), mu_n=E[L_n|F_n], and D_n=L_n-mu_n. By (G),(H), |mu_n|<=C R(P_n) and E[D_n^2|F_n]<=C R(P_n); the D_n are uniformly bounded martingale differences.

Here are explicit localization details. Put A_n=sum_{i<n}R(P_i), and tau_K=inf{n:A_n>K}. Since R(p)<=R(1), pathwise

    sum_{n<tau_K}R(P_n)<=K+R(1).

The stopped martingale sum_{n<N}1_{n<tau_K}D_n has total second-moment bound C[K+R(1)], by orthogonality of martingale differences and (G). Thus it is L^2 bounded and converges almost surely by the martingale convergence theorem. On E, choose an integer K>A_infinity; then tau_K=infinity. Taking the union over integers K shows sum D_n converges on E. Absolute summability of mu_n there implies sum L_n converges on E.

Large relative jumps occur only finitely often on E as well. In fact (E) and localization give

    E[sum_{n<tau_K}1_{|P_{n+1}-P_n|>P_n/2}]
        <= C E[sum_{n<tau_K}R(P_n)] <= C[K+R(1)]<infinity.

The stopped count is therefore finite almost surely. Again choose K>A_infinity on E. This proves finite many large jumps on E without any independence assumption.

Since each individual P_n is a finite positive integer, every individual actual log increment is finite. On E, only finitely many of these increments differ from L_n; hence the telescoping sum U(P_N)-U(P_0) converges to a finite real limit. But Section 3 proves P_N tends to infinity, so U(P_N)=log h(P_N) tends to infinity. Contradiction. Therefore P(E)=0, proving the asserted rate divergence. QED.

### 6. Finish the map argument

Since P_n tends to infinity, (F) and rate divergence imply sum_n b(P_n)=infinity almost surely. Apply the already proved survival-compensator lemma, uniform marked-edge geometry, countable enumeration of exposed edge occurrences, and finite dual-path argument in Lemma 6 above. These arguments do not use f'' or stable attraction. They give exhaustion for every admissible critical q and every continuing adapted filled-in peeling algorithm.

The only literature input beyond the standard peeling identities is Budd's exact kernel, stated for all critical laws. We have not found a published theorem stating this final general exhaustion assertion; the conclusion here is a new deduction. This proof must be assessed on its complete argument, not treated as SOLVED_IN_LITERATURE.

### Independent derivation of the exact kernel from the source integral

This removes dependence on transferring Budd's notation and also checks the kernel in the infinite-f'' case. The argument for the monotone inverse G(y)=y(1-f(y)) in Lemma 1 only needs finite f'(Z), which is guaranteed by criticality. Its strict derivative on (0,Z) and continuous limit at Z remain valid even when f''(Z) is infinite. Thus

    W^(j)/c^j = d(j) integral_0^1 r^j J'(r) dr,
    J(r)=Zr(1-f(Zr)),

continues to hold for every critical q. Set a_k=q_k binom(2k-1,k-1)Z^(k-1). The two critical equations imply sum_{k>=1} k a_k = f(Z)+Zf'(Z)=1. In particular

    J'(r)=Z sum_{k>=2} k a_k (1-r^(k-1)), 0<=r<=1.

This is a nonnegative series; at r=1 each term vanishes, and sum k a_k is finite. Tonelli therefore permits integration term by term. For k>=1 (now the negative-jump index),

    integral_0^1 r^(k-1)J'(r)dr
      = Z sum_{l>=2} l a_l [1/k-1/(k+l-1)]
      = (Z/k) sum_{m>=1} m(m+1)a_{m+1}/(k+m)
      = (Z/k) T(k),

because a_{m+1}=[(2m+1)/(m+1)]d(m)nu(m). Using c=4Z and d(k)=[(2k-1)/(2k)]d(k-1),

    nu(-k)=2c^(-1)d(k-1)(Z/k)T(k)
           = [d(k)/(2k-1)]T(k).

This proves the kernel directly for the exact model of C0057 without any analytic continuation, finite f'', or regular variation. For k=1 the formula gives T(1)=1/Z and nu(-1)=1/(2Z)=2/c, as required by W^(0)=1. All sums in this derivation are nonnegative; there is no unjustified exchange of a conditionally convergent series.


## Auxiliary finite-second-derivative proof and exact example

## Lemma 1: negative tail for finite f''(Z)

Assume f''(Z)<infinity, meaning the one-sided increasing limit. Put

    D=1+(Z^3/2) f''(Z) >= 1.

Then

    W^(j) ~ [2D/sqrt(pi)] c^j j^(-5/2),
    nu(-j) ~ p_minus j^(-5/2), p_minus=4D/[c sqrt(pi)]>0.

Proof. Let G(y)=y(1-f(y)), 0<=y<=Z. Criticality gives G(Z)=1 and G'(Z)=0. In the interior G''(y)=-2f'(y)-y f''(y)<0 for y>0: some positive coefficient has index k>=2, hence f'(y)>0. Therefore G'(y)>0 for y<Z. G maps [0,Z] continuously and strictly increasingly onto [0,1]. The equation for q_g is f(g Z_{q_g})=1-g/(g Z_{q_g}); hence y=g Z_{q_g}=G^(-1)(g). This is the smallest solution since G is strictly increasing up to Z. Consequently g c_{q_g}/c=y/Z.

Set J(r)=G(Zr), 0<=r<=1. Then J(0)=0, J(1)=1, J'(1)=0, and J''(1-)=-2D. One-sided continuity of f' and f'' follows by monotone convergence of their nonnegative power series. Integrating J'' from r to 1 therefore gives J'(r)=2D(1-r)+o(1-r). No extension beyond Z is assumed. Change variables in the partition-function integral:

    W^(j)/c^j = d(j) I_j,
    I_j = integral_0^1 r^j J'(r) dr.

Given epsilon>0, choose r_0<1 so J'(r)/(1-r) lies between 2D-epsilon and 2D+epsilon for r>=r_0. The integral below r_0 is at most r_0^j integral_0^{r_0} J'(r) dr <= r_0^j. Also integral_0^1 r^j(1-r)dr=1/[(j+1)(j+2)]. Comparing the integrals and then taking epsilon to zero proves j^2 I_j -> 2D. The d(j) asymptotic proves the W formula. Substitution in nu(-j)=2W^(j-1)c^(-j) proves the nu formula. QED.

## Lemma 2: positive moment and zero centering

Under this hypothesis sum_{m>=1} m^(3/2) nu(m)<infinity, and the nu-walk has mean zero.

Proof. The defining series gives

    Z^2 f''(Z) = sum_{k>=3} (k-1)(k-2) binom(2k-1,k-1) q_k Z^(k-1).

Since binom(2k-1,k-1) 4^(-(k-1)) ~ 2/sqrt(pi*k), the coefficient relative to nu(k-1) is asymptotic to (2/sqrt(pi)) k^(3/2). Thus f'' finiteness is equivalent to the stated positive moment; finitely many indices do not affect finiteness. Lemma 1 gives a finite first negative moment. The walk has a finite first absolute moment and oscillates by source Proposition 14. Its mean must be zero, since otherwise the strong law gives a nonzero drift. QED.

## Lemma 3: conditioned perimeter scaling

For each fixed starting p>=1, P_n/n^(2/3) converges in law to a finite strictly positive random variable Y.

Proof. Set alpha=3/2. Since the mean is zero, the characteristic function satisfies

    phi(t)-1 = sum_j nu(j) [exp(itj)-1-itj].

There is an absolute constant C such that |exp(ix)-1-ix|<=C min(x^2,|x|)<=C |x|^alpha. For each fixed nonnegative j, division by |t|^alpha gives a term tending to zero. Dominated convergence using Lemma 2 proves the positive-side sum is o(|t|^alpha).

On the negative side Lemma 1 and Riemann sums, separately as t approaches zero from either side, give

    [phi(t)-1]/|t|^alpha ->
    p_minus integral_0^infinity
      [exp(-i sign(t)x)-1+i sign(t)x] x^(-1-alpha) dx.

For completeness the improper Riemann sums are justified as follows. The absolute integrand below epsilon is bounded by C x^(1-alpha), with integral tending to zero as epsilon decreases. Above R it is bounded by C x^(-alpha), with integral tending to zero as R increases. The corresponding discrete bounds follow from nu(-j)<=C j^(-1-alpha) for sufficiently large j, using respectively |tj|^2 and |tj|. Finitely many j contribute O(t^2)=o(|t|^alpha). On [epsilon,R] the tail asymptotic is uniform as j tends to infinity, and ordinary Riemann sums apply. This proves the limit.

Taking nth powers at t=theta n^(-1/alpha) proves unconditioned stable attraction on the n^(1/alpha) scale, with no centering. The limit is the nondegenerate spectrally negative alpha-stable law with negative-jump Levy density p_minus x^(-1-alpha) and mean zero. It has positivity parameter rho=1/alpha=2/3 in (0,1).

Apply Francesco Caravenna and Loic Chaumont, 'Invariance principles for random walks conditioned to stay positive', Ann. Inst. H. Poincare Probab. Statist. 44(1) (2008), 170-190, DOI 10.1214/07-AIHP119, Theorem 1.1 (conditioned.pdf PDF p.4, printed p.173). Its hypotheses are uncentered stable attraction and rho in (0,1), both verified. The paper explicitly extends the result to strict positivity on PDF p.2 using V(x-). The source identifies our h-transform with this conditioning; the fixed initial p rescaled by n^(2/3) tends to zero. Therefore P converges after rescaling to the positive conditioned stable process from entrance state zero. Its value at time 1 is finite and strictly positive, giving Y (see the cited paper Section 1.2 and the use of this support property in source Corollary 27). QED.

Budd, arXiv:1506.01590, Proposition 5 (PDF p.18), already gives a related general finite-L_nu invariance principle. We used the attraction calculation above to avoid mixing his full-perimeter conventions with these half-perimeter conventions. These are established inputs, not solutions in print to the unrestricted question.

## Lemma 4: uniform swallowing lower bound

Define

    b(p) = (1/2) sum_{k=ceil(p/2)}^{p-2}
                     nu(-k-1) h(p-k-1)/h(p),

with empty sum zero. There are a>0 and p_0>=8 such that b(p)>=a p^(-3/2) for every p>=p_0. While a marked exposed boundary edge survives, its conditional probability of becoming interior at the next step is at least b(p).

Proof. For large p, restrict the sum to ceil(p/2)<=k<=floor(3p/4). These indices are admissible, there are at least p/8 of them, and p-k-1>=p/8. The h asymptotic implies h(p-k-1)/h(p)>=c_1>0 uniformly there. Lemma 1 gives nu(-k-1)>=c_2 p^(-5/2). Thus b(p)>=c_1 c_2 p^(-3/2)/16.

For the geometry, consider the cyclic sequence of 2p boundary edge occurrences. If the marked edge is selected, it becomes interior at that step. Otherwise it is at directed distance at most p on at least one side of the selected edge. Choose that side. A finite gluing event of half-perimeter k swallows an arc of 2k+1 boundary edges, including the peeled edge. For k>=ceil(p/2), this arc reaches strictly past the marked edge, so filling the finite component makes it interior. The specified-side event probabilities sum to b(p); the chosen algorithm has no effect on that formula. Treating edge occurrences avoids repeated-boundary-vertex issues in lazy peeling. QED.

## Lemma 5: Jeulin's argument without independence

If nonnegative X_n converge in law to a strictly positive finite X, then sum_{n>=1} X_n/n=infinity almost surely.

Proof. Otherwise some event A of probability epsilon>0 has the sum bounded by a finite M. Choose delta>0 a continuity point of X with P(X<delta)<epsilon/4. Eventually P(X_n<delta)<epsilon/2. Hence E[1_A X_n]>=delta[P(A)-P(X_n<delta)]>=delta epsilon/2. Tonelli implies E[1_A sum X_n/n]>= (delta epsilon/2) sum_{n>=N}1/n=infinity, contradicting the bound M. QED.

Take X_n=a n P_n^(-3/2) 1_{P_n>=p_0}. Lemma 3 and the continuous mapping theorem show X_n converges in law to aY^(-3/2)>0. The cutoff has probability tending to zero, since the rescaled perimeter has a strictly positive limit. Lemma 4 gives b(P_n)>=X_n/n, so sum_n b(P_n)=infinity almost surely. Deleting any finite prefix preserves divergence.

## Lemma 6: survival compensator, then exhaustion

Let T>=1 be a target's discovery time, a stopping time for the actual exploration filtration F_n. Put r_n=E[1_{T=n+1}|F_n], A_m=sum_{n<m}r_n. Then

    P(T=infinity, A_infinity=infinity)=0.

Proof. The process Z_m=1_{T>m} exp(A_m) is a nonnegative supermartingale starting at one. On {T>m}, its conditional next expectation is Z_m exp(r_m)(1-r_m)<=Z_m; on {T<=m} both sides are zero. This uses the actual stopped hazard r_m, not an unconditional perimeter probability. Set sigma_K=inf{m:A_m>=K}. Bounded optional stopping gives E Z_{min(sigma_K,N)}<=1. On {sigma_K<=N,T>sigma_K}, this variable is at least exp(K), so the probability is at most exp(-K). Let N increase. The event {T=infinity,A_infinity=infinity} is contained in {sigma_K<infinity,T>sigma_K} for every K. Let K increase to infinity. QED.

For a surviving edge Lemma 4 gives r_n>=b(P_n). Lemma 5 makes its compensator divergent on infinite survival outside a null set, so the edge becomes interior in finite time almost surely. Edges introduced at a random finite time s are covered by conditioning on F_s and its finite perimeter, or by deleting the finite prefix. The Markov perimeter law is preserved under adapted edge choices. Enumerate edge occurrences by introduction step and position; there are countably many, since each finite step exposes finitely many edges. A countable union of null events shows every exposed edge eventually becomes interior.

Suppose a face were missing from the exploration union. The dual map is connected, so choose a finite dual path from the initial root face to that face. The first missing face on this path has a predecessor explored at a finite step. The separating edge is then exposed and stays exposed until that missing face is explored or filled in. This contradicts eventual interiorization of every exposed edge. Thus all faces are explored, and their finite degrees give exhaustion of the map. This proves exhaustion for every continuing adapted algorithm when f''(Z)<infinity. QED.

No necessity claim about divergence of a stopped hazard is made. Discovery at the first step has total stopped hazard one, so necessity does not follow from conditional Borel-Cantelli.

## An exact nonregular critical example

Let zeta(s)=sum_{k>=1} k^(-s), C=1/[zeta(3)-1], Z=[zeta(3)-1]/[zeta(3)-zeta(4)], and define q_1=0,

    q_k = C k^(-4) Z^(1-k)/binom(2k-1,k-1), k>=2.

Then f(Zr)=C sum_{k>=2} k^(-4) r^(k-1). Since zeta(3)>zeta(4)>1, Z>1 and C>0. Direct substitution gives

    f(Z)=C[zeta(4)-1]=1-1/Z,
    Z f'(Z)=C[zeta(3)-zeta(4)]=1/Z,
    f''(Z)=C Z^(-2)[zeta(2)-3zeta(3)+2zeta(4)]<infinity.

The positivity and concavity argument for G shows Z is the smallest solution, so q is admissible critical. The radius of f is exactly Z: its coefficients after multiplying by Z^(k-1) are C k^(-4). Thus f(Z+epsilon)=infinity for every epsilon>0. It is not regular, hence not type 5/2 as defined in the notes, yet the theorem proves exhaustion.

Here J(r)=Z[(1+C)r-C Li_4(r)] and D=(ZC/2)[zeta(2)-zeta(3)]. For integers j>=1 the integral in Lemma 1 has the exact formula

    I_j=ZC[-zeta(3)/(j(j+1))+zeta(2)/j^2-H_j/j^3],
    H_j=sum_{k=1}^j 1/k.

Proof. J'(r)=ZC[zeta(3)-Li_3(r)/r]; the bracket equals sum_{k>=1} k^(-3)(1-r^(k-1)), a nonnegative series, so termwise integration is justified by Tonelli. Use

    1/[k^3(k+j)] = 1/(jk^3)-1/(j^2k^2)+1/(j^3k)-1/[j^3(k+j)]

and sum over k>=1. The last two terms telescope to H_j/j^3. Subtracting from zeta(3)/(j+1) gives the displayed I_j. In particular j^2 I_j -> ZC[zeta(2)-zeta(3)]=2D. QED.

## Hostile referee checks

- Verified source critical/admissible equations, side factor 1/2, half-perimeter conventions, and type endpoint qualifications.
- Endpoint derivatives are one-sided; no analytic extension is smuggled in. Contributions away from the endpoint have an explicit exponential bound.
- Positive moment and mean zero were proved, not presumed. Attraction is uncentered; Riemann sums were controlled at both endpoints.
- The invariance theorem was fetched and its exact assumptions checked, including strict positivity and entrance from zero. It does not assume exponential positive tails.
- The swallowing bound is target-specific on survival and uniform in the selected edge. Small perimeters are handled by a cutoff whose probability vanishes in the one-time scaling limit.
- Jeulin's argument requires no independence and no pathwise assertion P_n~n^(2/3). None is made.
- The stopped compensator is only a sufficient condition. Countability and finite dual paths finish exhaustion.
- PeelingAlgebra.lean verifies the finite Taylor polynomial identity and positivity of D only. It does not formalize the probability theorem or the full open problem. Its command and exit result are in lean_check.txt.
- experiment.py and experiment_results.json compare the exact example with quadrature, asymptotics, and transition normalization. These are consistency checks, not proofs of the unrestricted claim.



## Final referee audit and limitations

There is no remaining mathematical gap asserted in the universal proof. The proof is a new deduction and has not received independent human peer review. Only its finite algebra is Lean checked; the probability and planar-map arguments are written proofs using standard martingale convergence and the source's peeling identities. Numerical experiments are consistency checks, not logical premises.

The universal proof was separately checked for: (i) Tonelli in the kernel derivation with infinite f''; (ii) finite positive sqrt-moment from harmonicity at state 1; (iii) the p/2 cutoff and finite exceptional states; (iv) exact reciprocal-h cancellation rather than a positive-drift estimate; (v) lack of log-integrability for huge positive jumps, handled by truncation; (vi) predictable stopping and the one-step rate overshoot in localization; (vii) irreducibility not being needed for escape; (viii) the uniform side choice for each surviving exposed edge; and (ix) countability and dual connectivity.

universal_checks.py examined 70 transition rows from single positive-jump laws and lacunary mixtures with atom sizes up to 1,000,000, at perimeters up to 16,384. Maximum normalization error was 5.56e-16; observed ratios of big-jump probability, absolute truncated drift, and truncated second moment to R(p) were at most 2.653, 0.503, and 0.293. The smallest tested b(p)/R(p) for p>=8 was 0.04417. No numerical assertion about all laws is inferred from these samples. The job used less than 100 MB and ran for seconds.

Final Lean run: `lake env lean ~/brain_workers/TRIO_1011/op/C0057/PeelingAlgebra.lean`, from ~/lean_verify; exit code 0. There is one unused-hypothesis warning. All six finite algebra lemmas are checked without sorry or native_decide. The formalization covers the Taylor identity, D positivity, denominator comparisons, and recurrence factor identity.
