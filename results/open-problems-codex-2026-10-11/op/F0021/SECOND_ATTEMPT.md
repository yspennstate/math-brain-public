# F0021 ? additional attempt, 2026-10-12

## Gap reread
The previous attempt does not prove original-polymer confinement in an n^(2/3+delta) tube or KPZ universality of the capped, nonintegrable model. Its entropy calculation controls one large weight in zero background, but not a chain of many large rewards. The one-sided tail assumption also provides only a second moment on the negative side.

## Two previously untried approaches

**A. Entropy-controlled chains of large rewards.** Instead of a single-site maximum or a fixed spatial tube, enumerate ordered chains of rare large sites under a constraint on their quadratic travel entropy. Develop a finite entropy-controlled last-passage estimate in the spirit of Berger?Torri, then sum dyadic weight layers. The goal is first to prove that the full-cone polymer made only of weights above n^kappa has log partition function o_P(n^(1/3)) for some kappa<1/3 and alpha>5. This would control multiple rewards without a tube-confinement hypothesis. To solve the original question it would still have to be upgraded from a bare-walk background to the random capped-polymer background.

**B. Cavity probabilities and Lindeberg replacement.** Delete a single site's value, write its insertion exactly as log(1+p(e^(beta w)-1)), where p is its cavity visit probability, and compare disorder laws site by site. Use moment matching and occupation/influence sums to compare with a tractable reference model. The risk is that fixed beta provides no small replacement parameter: even matched first two moments leave higher cumulants multiplied by localized occupation probabilities, and alpha>5 on the right does not give third moments on the left. A successful argument would require quantitative bounds on cavity probabilities through mixed environments, rather than the bare-walk bounds of the first attempt.

## Choice and current aim
Pursue A. It offers a finite combinatorial estimate we can prove and test without assuming the very confinement result we need. B currently imports both a universality comparison and localization estimates which are absent from the hypotheses. Any zero-background or rare-reward conclusion will be labelled a special case, not a solution of fixed-temperature universality.

## Brain query at the gap
Read-only math_recall.py query: ?directed polymer transversal confinement heavy tails Lindeberg replacement universality Ransford?. Returned the Lindeberg Replacement Lemma card claim_b180868f8baf65700c550d47cad854de04fd2fadbad9b3cf154e4be5219e1f87, general KPZ cards and a provisional C0120 attempt explaining the missing quantitative transversal/chaos estimates. No closure theorem was returned. These hints do not establish any polymer result.


## Lemma 9: lattice entropy-controlled chain count (proved)
Let n>=1, B>0, and ell>=1 be integers except that B is real. A chain is a sequence of sites (t_1,x_1),...,(t_ell,x_ell) with 1<=t_1<...<t_ell<=n, integer x_r, and starting point (t_0,x_0)=(0,0). Define

E(chain)=sum_{r=1}^ell (x_r-x_{r-1})^2 / (2(t_r-t_{r-1})).

Independently mark sites of the reachable cone with probability p. Let K(B) be the maximum number of marked sites in an ordered chain of entropy at most B, restricted to the cone. For 1<=ell<=n,

P(K(B)>=ell) <= [ e^2 n p/ell * (1+sqrt(2 pi B n)/ell) ]^ell.                 (9.1)

For ell>n the probability is zero. This bound retains a lattice correction, the term proportional to np/ell.

Proof. Write d_r=t_r-t_{r-1}>0 and y_r=x_r-x_{r-1}. For a chain of entropy at most B,
1 <= exp(ell) exp(-ell E/B).
For each fixed time tuple, sum the right-hand side over all integer spatial increments (enlarging from cone sites to every integer). This gives at most
exp(ell) product_{r=1}^ell [1+sqrt(2 pi B d_r/ell)].
Indeed sum_{z in Z} exp(-a z^2)<=1+sqrt(pi/a), by comparing the decreasing summands on the positive integers with the integral over [0,infinity). The Gaussian integral is the standard integral of exp(-a x^2).
By Cauchy–Schwarz, sum sqrt(d_r)<=sqrt(ell sum d_r)<=sqrt(ell n). The arithmetic–geometric mean inequality therefore bounds the product by
[1+sqrt(2 pi B n)/ell]^ell.
There are binomial(n,ell) time tuples, at most (en/ell)^ell. To justify the latter elementary bound, binomial(n,ell)<=n^ell/ell! and log(ell!)=sum_{j=1}^ell log j>=integral_1^ell log t dt=ell log ell-ell+1>=ell log ell-ell.
Thus the total number of entropy-constrained chains is at most the right-hand side of (9.1) with p removed. Every particular cone chain contains ell distinct sites, so its marking probability is p^ell by independence. A union bound proves (9.1). Finally, a longer chain has a subchain of length ell with no greater entropy (Lemma 10), so the union bound on exact length ell does cover K(B)>=ell.

## Lemma 10: entropy decreases when sites are deleted (proved)
For positive s,t and real x,y,

(x+y)^2/(s+t) <= x^2/s + y^2/t.

Proof. Subtracting the left numerator after multiplication by s+t gives the identity
(x^2/s+y^2/t)(s+t)-(x+y)^2=(t x-s y)^2/(st)>=0.
Divide by s+t>0. Deleting one interior point of a chain merges two increments and cannot increase its entropy by this inequality. Deleting the final point removes a nonnegative summand. Repetition proves the subchain assertion.
In particular each point (t,x) on a chain of entropy at most B satisfies x^2/(2t)<=B, by deleting every other point. No Lipschitz hypothesis is needed for these facts.

## Theorem 11: the polymer of all sufficiently large rewards is asymptotically the bare walk (proved special case)
Suppose only that the iid real disorder has a regularly varying right tail with exponent alpha>5. Fix beta>0 and choose

5/(3 alpha)<kappa<1/3.

Set u_n=n^kappa and eta^{(n)}_{i,x}=omega_{i,x} 1{omega_{i,x}>u_n}, and define

Z_n^{tail}=E_S exp(beta sum_{i=1}^n eta^{(n)}_{i,S_i}).

Then, with probability tending to one,

0<=Z_n^{tail}-1<=exp(-n^{1/3}/4).                                           (11.1)

Consequently log Z_n^{tail}->0 in probability, and the total variation distance between the quenched eta-polymer path law and the length-n bare-walk law tends to zero in probability. This is a triangular-array, rare-positive-reward special case. Its background is identically zero. It is not a statement about the original centered, unit-variance polymer.

### Step 1: choose an envelope exponent and count all large sites
Choose 5<q<alpha with q kappa>5/3; such a q exists since alpha kappa>5/3 and kappa<1/3. The dyadic-envelope proof in ATTEMPT.md, Lemma 1, gives P(omega>v)<=C v^{-q} for sufficiently large v.
Let A=n^{1/3}, L=ceil(log_2 n), and D=16 max(1,beta); assume n is sufficiently large that L>=1, u_n exceeds the envelope threshold, and A/(D L)>u_n. The last condition holds because kappa<1/3.
The number N of large sites in the entire cone satisfies
E N <= C n(n+3)/2 * u_n^{-q} <=2 C n^{2-q kappa}.
Therefore N/A->0 in probability, by Markov's inequality and q kappa>5/3.

### Step 2: no large point has small initial travel entropy
There are at most
S(B)=n+2 sqrt(2) n^{3/2} sqrt(B)
sites with x^2/(2t)<=B, t<=n (discarding parity and the cone boundary enlarges this count). Thus
P(exists large site with x^2/(2t)<=A)
 <= C S(A) u_n^{-q}
 =O(n^{1-q kappa}+n^{5/3-q kappa})->0.                                     (11.2)
By Lemma 10, on the complementary event, every nonempty chain consisting of large sites has entropy greater than A.

### Step 3: all chains of larger entropy have reward at most half their entropy
Use entropy levels B=2^b A, b=1,...,m, where m is the smallest nonnegative integer such that 2^m A>=n/2. For sufficiently large n, m>=1, and every such B is at most n. Every chain compatible with a nearest-neighbour walk has entropy at most n/2: each displacement obeys |y_r|<=d_r, so y_r^2/(2d_r)<=d_r/2, and sum d_r<=n.
Partition weights into dyadic layers I_j=(v_j,2v_j], v_j=2^j u_n, j>=0; every omega>u_n lies in exactly one such layer, including boundary values. Layer markings are independent across sites, with probability p_j<=C v_j^{-q}. We do not assume independence between different layers.

For a fixed B, call layers with v_j>B/(D L) high layers. The probability of any high-layer point with initial travel entropy at most B is at most
C S(B) [B/(D L)]^{-q}.
Indeed every such point has omega>B/(D L), which exceeds u_n for the n under consideration. Summing over the geometric B-levels gives an upper bound
C' (D L)^q [n A^{-q}+n^{3/2} A^{1/2-q}]
=O((log n)^q [n^{1-q/3}+n^{(5-q)/3}])->0,                               (11.3)
since q>5. Infinite high weight layers have been summed by this single threshold event; there is no unjustified finite upper cutoff on omega.

For each remaining (low) layer, v_j<=B/(D L). There are at most L+1<=2L such layers because u_n>=1 and B<=n. Put h_j=B/(D L v_j)>=1 and ell_j=floor(h_j)+1. If its entropy-controlled count K_j(B)>h_j, Lemma 9 applies at ell_j. Since ell_j>=h_j and q>2, its bracket is at most
R_n=C_1 L n^{2/3-kappa(q-1)} + C_2 L^2 n^{1-kappa(q-2)},                  (11.4)
with constants depending on C,D only. To verify (11.4), expand the bracket in (9.1), use p_j<=C v_j^{-q}, ell_j>=B/(D L v_j), and B>=A. This gives terms bounded by a constant times
L n v_j^{1-q}/B and L^2 n^{3/2} v_j^{2-q}/B^{3/2};
these decrease in v_j, so replace v_j by u_n and B by A.
Both n-exponents in (11.4) are strictly negative. Specifically,
kappa(q-1)=q kappa-kappa>5/3-1/3=4/3,
kappa(q-2)=q kappa-2kappa>5/3-2/3=1.
Thus R_n->0 polynomially up to logarithms. For all sufficiently large n it is below one, so the failure probability R_n^{ell_j} is at most R_n. There are at most O((log n)^2) entropy/layer pairs; a union bound makes the probability of any low-layer count failure tend to zero. If ell_j>n the event is impossible, which causes no exception to this reasoning.

On the event excluding both high-layer points and low-layer count failures, any compatible chain with A<E<=n/2 belongs to a dyadic level E in (B/2,B]. Each of its low-layer subchains has entropy at most B by Lemma 10, so it contains at most h_j points. Its total reward obeys
beta sum omega <= beta sum_{low j} 2 v_j K_j(B)
 <= beta * (2L) * 2B/(D L)
 =4 beta B/D <=B/4 < E/2.                                                (11.5)
High-layer points are absent from that chain because each of its points has initial travel entropy at most E<=B. Equations (11.2)–(11.5) prove, with probability tending to one, that EVERY nonempty compatible chain of large sites has E>A and beta sum omega<=E/2. All chains are controlled together, rather than one chain chosen independently of the disorder.

### Step 4: expand the exact partition function over subsets of large sites
For a realized finite environment, write R for its N large sites. For every path,
exp(beta sum eta)=product_{z in R} [1+(exp(beta omega_z)-1)1{path visits z}].
Expand this product and take bare-walk expectation. The empty subset contributes one. Any nonempty subset which cannot be visited by one path contributes zero. A compatible subset is ordered uniquely by its distinct visit times, and contributes
P_S(visits chain) product_{z in chain}(exp(beta omega_z)-1)
 <= exp(-E(chain)+beta sum_{z in chain} omega_z)
 <= exp(-E(chain)/2)
 <= exp(-A/2)
on the event from Step 3. The walk probability bound is the product of the simple-walk transition probabilities at successive time gaps, by the Markov property, each bounded by its quadratic Chernoff cost as proved in ATTEMPT.md, Lemma 3.
There are at most 2^N-1 nonempty subsets. Hence
0<=Z_n^{tail}-1<=(2^N-1) exp(-A/2)<=exp(N log 2-A/2).
Because N/A->0 in probability, with probability tending to one N log 2<=A/4; this proves (11.1). The assertion about log follows from 0<=log Z<=Z-1.

### Step 5: total variation of the quenched path measures
Let W=exp(beta sum eta)>=1 and Z=E_S W. The polymer density relative to the bare path law is W/Z. By the triangle inequality,
TV=(1/2) E_S|W/Z-1|
 <=(1/2)E_S[(W-1)/Z+(Z-1)/Z]=(Z-1)/Z<=Z-1.
Equation (11.1) completes the proof.

## Immediate limitation
Writing omega=min(omega,u_n)+(omega-u_n)_+ does NOT turn Theorem 11 into an upper bound on log Z(omega)-log Z(min(omega,u_n)). The latter partition ratio is an exponential expectation under the capped-polymer path law, not under the bare walk. The Chernoff transition estimate in Step 4 applies only to the bare walk. A product/subadditivity inequality for two backgrounds would be needed for that shortcut, and such an inequality is false in general (to be checked explicitly below).


## Proposition 12: the subadditivity shortcut is false (proved logical obstruction)
Already at time n=1, put two nonnegative reward fields on the same site (+1), of values a,b>0, with zero at (-1). At inverse temperature beta>0,

Z(a+b)=(1+exp(beta(a+b)))/2,
Z(a)Z(b)=(1+exp(beta a))(1+exp(beta b))/4,
Z(a+b)-Z(a)Z(b)=(exp(beta a)-1)(exp(beta b)-1)/4>0.

These are exact two-path partition functions. Thus a bound Z(background+tail)<=Z(background)Z(tail) is false, even when the two fields are positive and can be the cap and excess at one site. It cannot be inserted after Theorem 11.

A stronger deterministic example shows why bare-walk invisibility is insufficient. Fix kappa<1/3<rho<1, beta>0, and a>log 2/beta. At sites (i,i) for i=1,...,n-1 put the bounded reward a, at (n,n) put v_n=n^rho, and put zero at every other site. Cap above at u_n=n^kappa; for large n, a<u_n<v_n. The rare-only field in Theorem 11 is now just the terminal spike, whose bare-walk partition function is
1+2^{-n}(exp(beta v_n)-1)->1.
The original and capped partition functions instead equal

Z= C_n+exp(beta a(n-1)-n log 2+beta v_n),
Zcap=C_n+exp(beta a(n-1)-n log 2+beta u_n),
C_n=sum_{r=0}^{n-1}2^{-(r+1)} exp(beta a r).

Proof. A path has a unique initial run of r all-right steps. If r<n, it leaves the diagonal at step r+1 and can never return to a site (i,i); its reward is a r. If it takes n right steps it visits the terminal spike and receives a(n-1)+v_n (or a(n-1)+u_n). The probabilities of these events are 2^{-(r+1)} and 2^{-n}, respectively.
Since exp(beta a)/2>1, the geometric sum C_n is at most C exp((beta a-log 2)n), with C independent of n. The all-right capped term has this same exponential factor multiplied by exp(beta u_n-beta a). Hence C_n divided by that term is O(exp(-beta u_n)). Apply log(1+t)<=t to both partition functions after factoring their all-right terms to obtain

log Z-log Zcap=beta(v_n-u_n)+O(exp(-beta u_n)),

which is much larger than n^{1/3}. This is not iid disorder, so it is NOT a counterexample to F0021. It is a counterexample to a purely deterministic inference from bare-walk tail invisibility to invisibility in every capped background.

## Approach B: an explicit obstruction to a routine moment comparison
The source allows the negative side to have only a second moment. Fix alpha>5 and r in (2,3). Let Y and V be independent standard Pareto variables with tail exponents alpha and r, respectively, and define X to have mixture law Y with probability 1/2 and -V with probability 1/2. Its mean m and variance sigma^2 exist and sigma>0: moments of order p of a Pareto(s) variable exist for p<s, as follows by integrating its density s t^{-s-1}, t>=1. Normalize omega=(X-m)/sigma. Then E omega=0 and E omega^2=1, and for all sufficiently large t,

P(omega>t)=(1/2)(sigma t+m)^{-alpha}.

The quotient of this expression at ct and t tends to c^{-alpha} for c>0, so the right tail is regularly varying with exponent alpha. Yet E|omega|^3=infinity: on the negative mixture component, for all sufficiently large V, |(-V-m)/sigma|^3>=V^3/(8 sigma^3), and E V^3=infinity when r<3. This is an admissible Assumption 3 law. It shows that the third absolute moment used in the recalled elementary Lindeberg lemma is not implied by alpha>5.

For completeness, the exact cavity calculation is as follows. Delete the site's contribution and let p_0 be its visit probability under that deleted-site polymer. Then
F(w)=F(0)+log(1-p_0+p_0 exp(beta w)).
Splitting paths into visiting and nonvisiting paths proves this identity. Put p(w)=p_0 exp(beta w)/(1-p_0+p_0 exp(beta w)). Differentiation gives
F'(w)=beta p(w),
F''(w)=beta^2 p(w)(1-p(w)),
F^{(3)}(w)=beta^3 p(w)(1-p(w))(1-2p(w)).
These are bounded derivatives, but their fixed-beta uniform bound does not yield a vanishing replacement error after summing over order n^2 sites and scaling by n^{1/3}. This is a failure of that bound to establish a comparison, not a lower bound on the true error. Bounds on occupation probabilities in mixed replacement environments would be needed. An occupation sum for a SINGLE environment must not be used as though all hybrids share that environment. The infinite-third-moment example also does not refute KPZ universality; saturated derivatives or a different truncation argument could potentially handle it.

## What the selected approach has and has not achieved
Theorem 11 controls arbitrary collections of large rewards, with their actual bare-walk visit probabilities, over the entire reachable cone. It strengthens the isolated-spike result to a many-spike statement and even gives convergence of the tail-only quenched path law to the bare walk. It uses no original-polymer confinement estimate and no assumption about the negative tail.
The exact remaining gap is still the random background: prove that adding the excess (omega-u_n)_+ to min(omega,u_n) changes the centered, fixed-temperature polymer free energy by o_P(n^{1/3}), or prove an appropriate background-dependent multipoint visit bound that makes the chain expansion usable under that polymer law. Theorem 11 and Proposition 12 show that a bare-walk estimate alone cannot supply it. Even a successful perturbation estimate would leave the generic capped-model KPZ/Airy universality theorem unproved.


## Corollary 13: the rare-reward theorem permits a slowly growing inverse temperature (proved)
Retain the hypotheses and cutoff kappa of Theorem 11. Let r>=0 with kappa+r<1/3, and let beta_n be any deterministic positive sequence bounded by B_0 n^r for a fixed B_0. Then (11.1), including its total-variation conclusion, still holds with beta_n in place of beta.

Proof. Choose the same fixed envelope exponent 5<q<alpha with q kappa>5/3. In the proof of Theorem 11 replace D by D_n=16 max(1,beta_n), bounded by a constant times n^r. Step 1's condition A/(D_n L)>u_n follows from kappa+r<1/3. Site counts and Step 2 are unchanged.
For the high-layer bound (11.3), the two n-exponents become rq+1-q/3 and rq+(5-q)/3. Since 1/3-r>kappa and q kappa>5/3, these are both strictly negative: they are 1-q(1/3-r) and 5/3-q(1/3-r).
The low-layer bracket (11.4) now has exponents r+2/3-kappa(q-1) and 2r+1-kappa(q-2). The condition r<1/3-kappa makes them strictly less than 1-q kappa and 5/3-q kappa, respectively, which are negative. All logarithmic union bounds therefore still tend to zero. With D_n>=16 beta_n, the allocation inequality (11.5) holds unchanged. The subsequent subset expansion and the bound N log 2<=A/4 are unchanged. This proves all assertions.

## Lemma 14: a finite temperature-comparison identity (proved)
Let P be uniform on the 2^n length-n walk paths, let H be any finite real function on paths, and set F(t)=log E_P exp(tH), t>0. For any p>1,

0 <= F(p beta)/p-F(beta) <= n log 2 (1-1/p).                              (14.1)

Proof. Let mu_t have density exp(tH-F(t)) relative to P. Differentiating the finite sum gives F'(t)=E_{mu_t}H. The relative entropy satisfies
D(mu_t||P)=tF'(t)-F(t)=n log 2 + sum_{paths} mu_t(path) log mu_t(path).
It is nonnegative: Jensen applied to log under mu_t gives E_{mu_t} log(P/mu_t)<=log E_{mu_t}(P/mu_t)=log 1=0. It is at most n log 2 because each mu_t(path)<=1, so every mu_t log mu_t summand is nonpositive. Thus

(d/dt)(F(t)/t)=D(mu_t||P)/t^2 in [0,n log 2/t^2].

Integrate from beta to p beta and multiply by beta. The integral of beta/t^2 is 1-1/p, proving (14.1). All weights are finite for each fixed environment; this requires no exponential moment of the disorder law.

## Theorem 15: unconditional sublinear truncation bound for the ORIGINAL polymer (proved)
Let alpha>5 and beta>0, with the original iid disorder as in Assumption 3. Fix any

0<r<(alpha-5)/(3 alpha).

Choose kappa satisfying 5/(3 alpha)<kappa<1/3-r. Let u_n=n^kappa, c_{i,x}=min(omega_{i,x},u_n), and let F_n(beta)=log Z_n^beta(omega), F_n^cap(beta)=log Z_n^beta(c). Then, with probability tending to one,

0 <= F_n(beta)-F_n^cap(beta)
   <= [n log 2 + exp(-n^{1/3}/4)]/(1+n^r).                               (15.1)

In particular the truncation error is O_P(n^{1-r}), and the difference divided by n tends to zero in probability. This bound is unconditional: it does not assume confinement of either polymer. It applies with exactly the one-sided tail assumption and finite-variance negative side of the question (indeed its proof only needs the right tail).

Proof. The kappa interval is nonempty precisely because r<1/3-5/(3 alpha). Define delta=(omega-u_n)_+ and eta=omega 1{omega>u_n}; then omega=c+delta, 0<=delta<=eta. Put p_n=1+n^{-r} and h_n=p_n/(p_n-1)=1+n^r, so 1/p_n+1/h_n=1. Hölder's inequality in the finite bare-walk expectation gives

Z_n^beta(omega)
 <= [Z_n^{p_n beta}(c)]^{1/p_n} [Z_n^{h_n beta}(delta)]^{1/h_n}
 <= [Z_n^{p_n beta}(c)]^{1/p_n} [Z_n^{h_n beta}(eta)]^{1/h_n}.

The second inequality uses delta<=eta. The inverse temperature h_n beta is at most 2 beta n^r. Corollary 13 applies, because kappa+r<1/3, and shows with probability tending to one that
log Z_n^{h_n beta}(eta)<=Z_n^{h_n beta}(eta)-1<=exp(-n^{1/3}/4).
Subtract log Z_n^beta(c), take logarithms in the Hölder bound, and apply Lemma 14 to the SAME fixed capped environment c. Its temperature-comparison contribution is at most n log 2 (1-1/p_n)=n log 2/(1+n^r). This yields (15.1). The lower bound follows from omega>=c and beta>0. Finally the upper bound divided by n is at most log 2/(1+n^r)+o(1), which tends to zero.

### Where this attempt stops
For 5<alpha<=6 the allowed r is less than or equal to 1/18; hence the obtained scale n^{1-r} remains at least n^{17/18}, much larger than n^{1/3}. Even letting alpha grow, this particular growing-temperature argument allows r<1/3 and thus never reaches an n^{1/3} error through the n^{1-r} entropy comparison. For alpha>6 the first attempt already proves exact equality with a suitable global cap with high probability; Theorem 15 is not an improvement there.
The loss is identifiable: the deterministic comparison (14.1) spends order n(p_n-1) to change temperature. It does not exploit common random fluctuations or a sharply centered free-energy comparison, and bounded deterministic strongly favourable paths can have relative entropy of order n. No estimate proved here reduces this term to the KPZ scale. No KPZ/Airy law for the capped model has been proved either. The theorem proves a truncation bound, not universality and not a counterexample to universality.


## Formal checks of the additional attempt

`SECOND_F0021.lean` passed with exit code 0 using targeted imports only. It kernel-checks the merged-increment entropy inequality, the sparse-layer exponent signs, and the allocation of layer energies below half the chain entropy. Command: `lake env lean ~/brain_workers/TRIO_1011/op/F0021/SECOND_F0021.lean`, from `~/lean_verify`, with a 3600-second timeout; recorded elapsed time 136.57 seconds. The file contains no `sorry` and no `native_decide`. Encoding and tactic-layout failures were corrected, and their failed logs are retained separately. No probability theorem, total-variation theorem, or Holder asymptotic is claimed formally checked: their full proofs are in SECOND_ATTEMPT.md and their finite components are corroborated by the saved computations.

**Final verdict of this additional attempt: PARTIAL.** Both proposed approaches are written down. The entropy-controlled-chain approach was pursued through a rare-reward path-law theorem and an unconditional sublinear truncation bound for the original polymer. The other approach was checked against an admissible infinite-third-moment construction. The necessary KPZ-scale random-background comparison and a fixed-temperature KPZ/Airy universality theorem remain unproved; no counterexample satisfying Assumption 3 was found.
