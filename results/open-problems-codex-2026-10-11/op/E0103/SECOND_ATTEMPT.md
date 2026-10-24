# E0103 — second serious attempt

Date: 2026-10-11. Reopened at the user's request after reading all of ATTEMPT.md and its remaining gap. The full problem remains under investigation; this file records new work as it is obtained.

## Two approaches not used in the first attempt

1. **Interval clumps and an infinite-server queue in one dimension.** At a fixed observation time t, turn the moving grains into a stationary Poisson process of random intervals of length 2r+t|V|. Their covered components are the busy periods of a spatial M/G/∞ queue; their uncovered components begin at exposed right endpoints. Instead of the previous sparse test-point argument or maximum of identical exponential spacings, compute the exact factorial moment densities of these exposed endpoints. This may give a centered limit for genuinely random velocities and reveal an extremal-index correction when some grains are stationary.
2. **Mixed volumes for convex grains in higher dimension.** Replace balls by a deterministic convex body D with nonempty interior. A straight sweep has exact volume |D|+t|v| |projection_(v-perpendicular)D|. The old ball-net argument can be replaced by inner parallel bodies D⊖δB, and capsule intersections by intersections of bounded-width swept tubes. This would extend the first-order result to anisotropic grains, with rate λ E[|V| |projection_(V-perpendicular)D|]. It broadens the grain hypotheses but does not itself identify centered fluctuations. Difficulties include continuity of projection volumes under erosion and handling genuinely unbounded random grain sizes.

I pursue approach 1, because it directly attacks a missing distributional result rather than only extending the first-order class.

## Brain query about the gap

Read-only queries: math_recall.py "Boolean interval coverage clump M/G/infinity busy period Gumbel Poisson approximation" and brain.py recall "one dimensional Boolean coverage random interval lengths Gumbel mistakes". The math store returned general Poisson approximation, Le Cam, extreme-value and Last–Penrose cards, not a matching interval-clump theorem. Le Cam is not directly applicable because exposed endpoints are dependent. The exact factorial-moment computation below avoids that independence assumption. The second memory query is recorded in LITERATURE.md when complete.

## Exact interval reduction and exposed-endpoint density

Let d=1, λ,r>0, U=|V|, m=EU∈(0,∞), and b=2r. A grain starting at x sweeps

[x−r+t min(V,0), x+r+t max(V,0)],

an interval of length ℓ_t=b+tU. Map each marked germ (x,V) to its right endpoint B=x+r+t max(V,0), retaining the velocity mark. For each fixed t this is a mark-dependent translation of Lebesgue measure, so the mapped process is Poisson of intensity λ dB μ(dV); marks remain independent with their original law. The covered set is a union of [B−ℓ_t,B]. No independence between these processes at different t is asserted or needed.

Call B **exposed** if no other interval contains B. Coincident endpoints, and coincidences of an endpoint with another left endpoint, have zero probability because endpoint locations have a Lebesgue density. Since Eℓ_t<∞, only finitely many intervals meet each bounded region. Consequently an exposed B is exactly the start of a nonempty uncovered interval immediately to its right.

Write H_L(t) for the number of exposed endpoints in (0,L), and put

q_t=exp(−λEℓ_t),  ρ_t=λq_t,
k_t(h)=λ P(ℓ_t<h) exp(−λ E min(h,ℓ_t)), h>0.

**Lemma F1 (exact factorial density).** For ordered locations 0<x₁<⋯<x_k<L, the factorial moment density of exposed endpoints is

ρ_t ∏_(i=2)^k k_t(x_i−x_(i−1)).                    (F1)

Proof: insert k endpoints with independent marks using the Poisson insertion identity. An inserted interval ending at x_i, i≥2, avoids all earlier inserted endpoints exactly when its length is smaller than the immediately preceding gap x_i−x_(i−1). Earlier-ending intervals cannot cover later endpoints. This contributes ∏_(i=2)^k P(ℓ_t<x_i−x_(i−1)); the first inserted mark is unrestricted.

For a background mark of interval length ℓ, the endpoints that would cover at least one x_i form the union of [x_i,x_i+ℓ]. The length of this union is

ℓ+∑_(i=2)^k min(x_i−x_(i−1),ℓ).                    (F2)

Indeed, adding the interval with largest left endpoint increases the union length by the entire ℓ if the preceding gap is at least ℓ, and by that gap otherwise: the preceding interval has the furthest right endpoint among those previously inserted. Starting with length ℓ proves the formula by induction. After averaging (F2) over the background mark and multiplying by λ, the Poisson void law gives exp(−λEℓ_t)∏exp(−λEmin(gap,ℓ_t)). Multiplication with the insertion factors λ^k proves (F1).

The insertion identity follows, on a bounded window, by conditioning on the Poisson count n and integrating n independent uniform endpoints, using nP(N=n)=λ|window|P(N=n−1). For functionals also depending on points outside the window, first condition on the independent outside process, perform the same finite calculation, and average. Repetition gives the k-point version. Increasing the insertion windows and nonnegative monotone convergence then give the marked full-line identity, with the functional still evaluated on the entire process. Finite Eℓ_t makes all the void intensities here finite. Also H_L(t) is bounded by the total number of endpoints in (0,L), a Poisson(λL) count, so all its moments are finite.

**Lemma F2 (coverage boundary).**

|P(C([0,L])≤t)−P(H_L(t)=0)|≤q_t.                   (F3)

Proof: if [0,L] is covered then no exposed endpoint lies inside (0,L). Conversely, if 0 is covered and there is an uncovered point inside the target, the first uncovered component encountered from the left has a covered left boundary inside (0,L), which by local finiteness is an exposed endpoint. An uncovered point at L with all earlier points covered is impossible because the covered set is locally closed. Endpoint coincidences have probability zero. Thus H_L=0 together with initial point coverage implies full coverage. The only possible discrepancy is 0 being uncovered, with probability q_t by the pointwise void law. This proves (F3).

## Promising extension: stationary marks produce clusters

Set p₀=P(U=0). Since m>0, p₀<1. At large t, for each fixed h>b,

k_t(h) → λp₀ exp(−λ[p₀b+(1−p₀)h]);

for h<b the kernel is identically zero. This is immediate from dominated convergence for the bounded variable min(h,b+tU), and from P(b+tU<h)→p₀. The limiting local kernel has integral

J=p₀ exp(−λb)/(1−p₀).                              (F4)

If p₀=0 this integral vanishes, suggesting Poisson rare holes and a Gumbel coverage law. If p₀>0, it predicts clustered holes, not a Poisson count. In particular the earlier deterministic-speed centering cannot be extended blindly to laws with an atom at zero. The next step is to control the kernel uniformly on distances growing with L, and to compute the resulting clustered count law.

## Theorem F: a centered law for random velocities in dimension one

**Theorem F.** Let d=1, λ,r>0, U=|V|, 0<m=EU<∞, p₀=P(U=0)<1. Assume

(log h) E[U 1_(U>h)] →0 as h→∞.                    (T)

Let

b=2r,  J=p₀e^(−λb)/(1−p₀),  θ=1/(1+J)
  =(1−p₀)/(1−p₀+p₀e^(−λb)).

Then

λm C([0,L])+λb−log(λL)−log θ ⇒ G,
P(G≤z)=exp(−e^(−z)).                                (F5)

The velocity may have either sign, and its sign and magnitude may be dependent. Bounded speeds and every law satisfying E[U log(2+U)]<∞ satisfy (T). A positive lower bound on moving speeds is not required. If p₀=0, θ=1; Theorem C is the deterministic-speed special case. If p₀>0, subtracting log θ is essential.

The following proof also identifies the limiting count of uncovered components at a fixed centered time; the count is compound Poisson with geometric cluster sizes when p₀>0.

### Step 1: uniform control of the endpoint kernel

For fixed z∈R, set

t_L=(log(λL)+z−λb)/(λm),  ρ_L=λe^(−λ(b+t_Lm)).

For large L, t_L>0, and Lρ_L=e^(−z)=:μ exactly. Choose c>0 with p=P(U≥c)>0, possible since m>0. Choose a fixed

0<δ<min(1,pc/m),  B_L=L^δ.

Then t_L/log L→1/(λm). There are two kernel regions.

**Local region.** For b≤h≤b+ct_L, the marks with U≥c have ℓ_t≥h, while all marks have ℓ_t≥b. Consequently

E min(h,ℓ_t)≥ph+(1−p)b,
k_t(h)≤λexp(−λ[ph+(1−p)b]).                         (F6)

For h<b the kernel is zero. For fixed h>b, k_t(h) tends to the local kernel in (F4). Extend k_t(h)1_(h≤b+ct_L) by zero beyond b+ct_L. It is bounded by the integrable function in (F6), and converges pointwise almost everywhere to that local kernel. Dominated convergence gives its integral →J. On b+ct_L≤h≤B_L, monotonicity of min gives

k_t(h)≤λexp(−λ[b+pct_L]),

so this remaining integral is at most λB_Lexp(−λ[b+pct_L])=L^(δ−pc/m+o(1))→0. Since B_L eventually exceeds b+ct_L, we conclude

J_L:=∫_0^B_L k_(t_L)(h)dh →J.                      (F7)

**Far region.** For all h≥B_L,

k_t(h)/ρ_L=P(ℓ_t<h) exp(λE[(ℓ_t−h)_+]).             (F8)

Let a_L=(B_L−b)/t_L→∞. Then

sup_(h≥B_L) E[(ℓ_t−h)_+]
 ≤t_LE[U1_(U>a_L)]→0,

because log a_L∼δ log L, t_L/log a_L stays bounded, and (T) holds. Also inf_(h≥B_L)P(ℓ_t<h)≥1−P(U≥a_L)→1. Equality atoms at a_L cause no issue: U is finite almost surely and a_L→∞. Hence

sup_(h≥B_L)|k_(t_L)(h)/ρ_L−1|→0.                  (F9)

This is uniform relative error even though both numerator and denominator vanish. It is not just fixed-distance convergence.

### Step 2: all factorial moments of the hole count

Write H_L=H_L(t_L). By Lemma F1,

E binom(H_L,k)
 =∫_(0<x₁<⋯<x_k<L) ρ_L∏_(i=2)^k k_(t_L)(x_i−x_(i−1)) dx. (F10)

The factor k! disappears because the symmetric factorial density is integrated on the ordered simplex. Fix k≥1. Partition the k−1 consecutive gaps into “near” gaps <B_L and “far” gaps ≥B_L. If there are c−1 far gaps, there are c clusters and k−c near gaps. There are binom(k−1,c−1) such patterns.

Fix one pattern and the values of its near gaps z₁,…,z_(k−c)∈(0,B_L). Let S=∑z_j. Set each far gap equal to B_L plus a nonnegative variable. Together with x₁ these give c nonnegative variables whose sum is at most L−S−(c−1)B_L. Their integration volume is

(L−S−(c−1)B_L)_+^c/c!.                              (F11)

This simplex-volume formula follows by integrating successively: the volume V_c(A) satisfies V_1(A)=A and V_c(A)=∫_0^A V_(c−1)(A−u)du, giving A^c/c! by induction. The change of variables has Jacobian one. Since S≤(k−c)B_L and B_L=o(L), (F11), divided by L^c/c!, tends to one uniformly over all near-gap choices.

On far gaps (F9) replaces each kernel by ρ_L with a relative error tending to zero, uniformly. Since k is fixed, the product error tends to zero uniformly as well. Integrating the near gaps separately gives J_L^(k−c). Thus each pattern contributes

(Lρ_L)^c J_L^(k−c)/c! + o(1)
 → μ^c J^(k−c)/c!.

The estimate remains valid when J=0: use the uniform multiplicative bounds and J_L→0 rather than dividing by J_L. Summing over the finitely many patterns proves

E binom(H_L,k) → ∑_(c=1)^k binom(k−1,c−1) μ^c J^(k−c)/c!. (F12)

For k=0 both sides are one. In particular EH_L=μ exactly, and

Var(H_L)→μ(1+2J).                                  (F13)

The non-Poisson variance when p₀>0 is a check that clustering cannot be ignored.

### Step 3: identify the count law and justify moment convergence

Let N be Poisson with mean μθ. Let Z₁,Z₂,… be independent, independent of N, with

P(Z_i=j)=θ(1−θ)^(j−1),  j=1,2,…,

and put Y=∑_(i=1)^N Z_i. When θ=1, all Z_i=1 and Y is ordinary Poisson(μ). For |w| sufficiently small,

E(1+w)^Y=exp(μw/(1−Jw)).                            (F14)

Indeed, E(1+w)^Z=(1+w)/(1−Jw), and the Poisson random-sum generating function is exp(μθ[E(1+w)^Z−1]); using θ(1+J)=1 gives (F14). Expanding exp(μw/(1−Jw)) as

∑_(c≥0) μ^c w^c(1−Jw)^(−c)/c!

shows that its coefficient of w^k is the right-hand side of (F12), because the coefficient of w^(k−c) in (1−Jw)^(−c) is binom(k−1,c−1)J^(k−c). Thus (F12) gives convergence of every factorial moment of H_L to that of Y. Every ordinary moment is a finite linear combination of factorial moments: this identity follows by counting functions from a k-element labeled set according to the number of distinct image points. Therefore all ordinary moments converge too.

Here is why no moment-method assumption is hidden. First moments bound the laws tightly on the nonnegative integers by Markov's inequality. For each positive integer j, bounded (j+1)-st moments give uniform integrability of H_L^j via

E[H_L^j 1_(H_L>A)]≤E[H_L^(j+1)]/A.

Consequently any weak subsequential limit Y′ has every moment equal to that of Y; the limit is supported on the nonnegative integers, a closed subset of the real line. Y has a finite exponential moment for some ε>0, as follows from its geometric-cluster generating function. For any 0<s<ε, monotone expansion of the nonnegative exponential series gives

E e^(sY′)=∑_(j≥0) s^j E[(Y′)^j]/j!
          =∑_(j≥0) s^j E[Y^j]/j!=E e^(sY)<∞.

The probability generating functions of Y and Y′ are analytic on a disk of radius greater than one, and agree on the interval of real arguments e^s, 0<s<ε. The identity theorem for analytic power series then forces equality of every coefficient, hence equality of the probability distributions. Thus all subsequential limits equal Y, and H_L⇒Y. In particular

P(H_L=0)→P(Y=0)=exp(−μθ).                           (F15)

To pass to zero probabilities one may use the interval (−1/2,1/2), whose boundary has no mass for these integer-supported laws. This avoids a misuse of continuity at an atom.

### Step 4: translate back to coverage time

By (F3), the difference between P(C([0,L])≤t_L) and P(H_L=0) is at most q_t=μ/(λL)→0. Hence

P(λmC([0,L])+λb−log(λL)≤z)→exp(−θe^(−z)).          (F16)

Replacing z by z+log θ in (F16) proves the standard Gumbel limit (F5). This finishes the proof of Theorem F.

## Current remaining gap after Theorem F

Theorem F resolves the centered one-dimensional law for all speed distributions satisfying (T), including bounded random speeds, arbitrarily small positive speeds, stationary atoms, and finite logarithmic moments. The explicit heavy-tail Theorem B lies outside (T) and remains a different regime. General finite-mean one-dimensional tails beyond (T), higher-dimensional centered fluctuations, and genuinely general grains are still not classified. This is stronger partial progress, not a solution of the unrestricted source question.

## Theorem G: the critical finite-mean tail

**Theorem G.** In dimension one, let λ,r>0, U=|V|, and suppose

P(U>u) ∼ c/(u(log u)²),  u→∞,   c>0.                (F17)

Let m=EU. This tail makes m finite and positive (the bounded part of a nonnegative random variable has finite mean). Then

C([0,L])/log L ⇒ min(E,1/(λm)),  E∼Exp(rate λc).    (F18)

Moreover

E C([0,L])/log L → (1−exp(−c/m))/(λc).              (F19)

Signs of velocities and an atom at zero are allowed. The limit has an atom of size exp(−c/m) at 1/(λm). This is a whole critical tail class, not just the previously treated log-log heavy-tail example.

### Step 1: tails and single-grain spanning

Keep b=2r. Write R(h)=E[(U−h)_+]=∫_h^∞P(U>u)du. From (F17),

R(h)∼c/log h.                                       (F20)

Proof: for any η>0, above a sufficiently large h the integrand lies between (1−η)c/[u(log u)²] and (1+η)c/[u(log u)²]. Integrating these bounds gives (1±η)c/log h. Let η↓0. Integrability on this tail and boundedness on finite intervals give m<∞.

Fix s>0 and t=s log L. In the endpoint representation, a grain of length ℓ=b+tU spans [0,L] exactly when its endpoint is between L and ℓ. Therefore its eligible-endpoint measure is (ℓ−L)_+, and the count of spanning grains is Poisson with mean

β_L=λ E[(ℓ−L)_+]=λt R((L−b)/t)→λcs.               (F21)

This alone implies P(C([0,L])≤t)≥1−exp(−β_L). It is not enough to prove equality: combinations of smaller intervals could also cover the region.

### Step 2: condition away the global common cause

Let S_L be the marked initial-condition set of all grains spanning [0,L]. Restrictions of a Poisson process to S_L and its complement are independent. Conditional on no spanning grain, the complement remains a Poisson process with its original restricted intensity. Every deleted spanning mark covers every point of the target.

For a fixed y∈[0,L], its full hit-set intensity is λEℓ. After deletion it is λEℓ−β_L, independent of y. Thus its conditional uncovered probability is

q*=exp(−λEℓ+β_L).

For two points at distance h≤L, the full common hit-set intensity is

I_L(h)=λ E[(ℓ−h)_+].                                (F22)

Indeed, for a fixed ℓ their allowable endpoints are [y,y+ℓ] and [z,z+ℓ], whose intersection length is (ℓ−h)_+. The spanning set is contained in this intersection and has intensity β_L, so the conditional common-hit intensity is I_L(h)−β_L≥0. The void law gives exactly

P(y,z both uncovered | no spanning grain)
 =(q*)² exp(I_L(h)−β_L).                             (F23)

Subtracting β_L is essential; an unconditional second moment would retain the nonvanishing dependence caused by a single grain spanning the entire target.

### Step 3: below the local-coverage threshold there remain holes

Assume 0<s<1/(λm), and choose 0<δ<1−λms. Select n=⌊L/a₀⌋+1 test points at spacing a₀=max(1,3r) inside [0,L], using the indices 0,…,⌊L/a₀⌋. Let U_L be their number uncovered in the conditioned process. Then

EU_L=nq*≥C L^(1−λms)→∞,

because β_L stays bounded, λEℓ=λb+λms log L, and n is of order L. By (F23),

Var(U_L)/(EU_L)²
 ≤1/(nq*) + (1/n²)∑_(i≠j)(exp(I_L(h_ij)−β_L)−1).   (F24)

Split the off-diagonal sum into three distance ranges.

**Short separations h<L^δ.** At most C n L^δ pairs lie in this range, and I_L(h)≤λEℓ. Their normalized contribution is at most

C L^(δ−1) exp(λEℓ)=C′ L^(δ−1+λms)→0.              (F25)

**Bound the rest uniformly.** For h≥L^δ>b,

I_L(h)=λt R((h−b)/t)
 ≤λt R((L^δ−b)/t)→λcs/δ.                           (F26)

Thus exp(I_L(h)−β_L)−1 is bounded by a constant depending on δ,s,c,λ, uniformly in this range for all large L.

**Macroscopic separations.** For any fixed ε∈(0,1), monotonicity gives

0≤sup_(εL≤h≤L)(I_L(h)−β_L)
 ≤λt[R((εL−b)/t)−R((L−b)/t)]→0,                    (F27)

since each of the two terms after multiplication by λt converges to λcs by (F20). Therefore the normalized contribution of h≥εL tends to zero.

The remaining intermediate separations L^δ≤h<εL make up at most Cεn²+O(n) pairs; by (F26) their normalized contribution has limsup at most C_δε. First let L→∞, then ε↓0. Together with (F25) and the diagonal estimate, this proves (F24) tends to zero. Chebyshev's inequality gives

P(U_L=0 | no spanning grain)→0,

where expectations and variances in (F24) already refer to the conditioned process. Hence the conditional probability of full coverage also tends to zero.

It follows from (F21) that for 0<s<1/(λm),

P(C([0,L])≤s log L)→1−exp(−λcs).                    (F28)

This proves that smaller intervals do not add a competing full-coverage mechanism below that threshold, despite their strong local dependence.

### Step 4: above threshold and convergence in mean

If s>1/(λm), a fixed-mesh net with smaller-radius grains gives

P(C([0,L])>s log L)≤C L exp(−λm s log L)→0.          (F29)

In dimension one the swept-rate coefficient λm does not depend on the smaller positive radius. The net proof and static endpoint constant are exactly those in ATTEMPT.md Theorem A. At s=0, initial full coverage tends to zero by linearly many independently covered static test points. At negative s the probabilities vanish. Equations (F28)–(F29) identify the limiting CDF at every continuity point of min(E,1/(λm)); convergence at its threshold atom is not required. This proves (F18).

The uniform exponential-tail bound for C([0,L])/log L in ATTEMPT.md requires only 0<m<∞, so it applies here and gives uniform integrability. Thus distributional convergence also implies convergence of expectations. For E∼Exp(λc),

E min(E,1/(λm))=∫_0^(1/(λm)) exp(−λcs)ds
              =(1−exp(−c/m))/(λc),

which proves (F19). This completes Theorem G.

### Explicit critical law

Take P(U>u)=1/[u(log u)²] for u≥e, and P(U>u)=1/e for 0≤u<e (the remaining mass is at zero). Then c=1 and

m=e·(1/e)+∫_e^∞du/[u(log u)²]=2.

The limit is min(Exp(λ),1/(2λ)), with mass exp(−1/2) at 1/(2λ), and mean (1−exp(−1/2))/λ. This explicitly separates the critical case from both the Gumbel regime of Theorem F and the log-log regime of Theorem B.

## Theorem H and a complete logarithmic-power tail phase diagram

**Theorem H.** Suppose in dimension one that 0<m=EU<∞ and the integrated speed tail satisfies

R(h)=E[(U−h)_+]∼A/(log h)^α,  A>0,  0<α<1.

Then

C([0,L])/(log L)^α ⇒ Exp(rate λA),
E C([0,L])/(log L)^α →1/(λA).                       (F30)

### Proof

Fix s>0 and put t=s(log L)^α. The single-grain spanning intensity is

β_L=λt R((L−b)/t)→λAs,

because log((L−b)/t)/log L→1. Condition on no spanning grain exactly as in Theorem G. Equations (F22)–(F24) still hold, and for the same fixed-spacing test set

nq*=Θ(L) exp(−λb−λms(log L)^α+β_L)→∞.

Fix δ∈(0,1). Pairs with h<L^δ have normalized covariance contribution at most

C L^(δ−1) exp(λb+λms(log L)^α)=L^(δ−1+o(1))→0.

For the other pairs,

I_L(h)≤λt R((L^δ−b)/t)→λAs/δ^α,

so their covariance factors are uniformly bounded. For each fixed ε>0, on h≥εL,

0≤I_L(h)−β_L
 ≤λt[R((εL−b)/t)−R((L−b)/t)]→0,

because both terms converge to λAs. Pairs at intermediate separations L^δ≤h<εL have proportion O(ε), and the uniformly bounded covariance makes their normalized contribution O_δ(ε). Letting L→∞ and then ε↓0 proves the normalized conditional variance tends to zero. Therefore conditional full coverage without a spanning grain tends to zero. The spanning probability tends to 1−exp(−λAs). This proves the claimed exponential distributional limit at every s>0. At zero, initial coverage tends to zero by the static test-point argument; at negative s the probabilities vanish.

For expectation convergence, the spanning mechanism alone supplies uniform integrability on the smaller scale. For L sufficiently large and s≥1, let t=s(log L)^α. Since t≥1 and L>b, (L−b)/t≤L and R is nonincreasing, so

β_L(t)=λt R((L−b)/t)≥λs(log L)^α R(L)≥(λA/2)s.

Hence

P(C([0,L])/(log L)^α>s)≤exp(−λAs/2),  s≥1,

uniformly for large L. This exponential tail implies uniform integrability as in the earlier proof. The exponential limit has mean 1/(λA), giving the expectation assertion. This completes Theorem H.

**Corollary (all logarithmic-power tails).** Let

P(U>u)∼c/[u(log u)^p],  c>0,  p>1.

Integrating two-sided asymptotic bounds gives

R(h)∼c/[(p−1)(log h)^(p−1)],
E[U1_(U>h)]=hP(U>h)+R(h)∼c/[(p−1)(log h)^(p−1)].

Thus every such law has finite positive mean, and its one-dimensional interval coverage has the following regimes:

| Tail exponent | Scale and limiting law |
| --- | --- |
| 1<p<2 | C([0,L])/(log L)^(p−1) ⇒ Exp(rate λc/(p−1)); normalized mean →(p−1)/(λc). |
| p=2 | C([0,L])/log L ⇒ min(Exp(λc),1/(λm)); normalized mean →(1−e^(−c/m))/(λc). |
| p>2 | λmC([0,L])+2λr−log(λL)−log θ ⇒ standard Gumbel, with θ from Theorem F; E C([0,L])/log L→1/(λm). |

For 1<p<2 apply Theorem H with α=p−1 and A=c/(p−1). For p=2 apply Theorem G. For p>2, (log h)E[U1_(U>h)]→0 by the displayed asymptotic, so Theorem F applies. Tightness of its centered variable gives C/log L→1/(λm) in probability; the old uniform-integrability bound then gives the stated mean. These implications check every hypothesis; there is no interpolation conjecture in the table. No assertion is made for arbitrary oscillating or non-logarithmic-power tails.

## Hostile-referee audit of the second attempt

### Independent check of the stationary correction

The following local static-clump computation gives the same θ through a separate algebraic calculation. It is a consistency check on the constant, not a replacement for the global factorial-moment proof.

Let λ₀=λp₀ and λ₁=λ(1−p₀). Static intervals have length b. When λ₀>0, their covered-component length B starts with b and adds successive independent exponential(λ₀) gaps smaller than b, stopping at the first gap at least b. Its Laplace transform is

E e^(−sB)
 =e^(−sb)e^(−λ₀b) / [1−∫_0^b λ₀e^(−(λ₀+s)x)dx]
 =(λ₀+s)e^(−(λ₀+s)b)/(s+λ₀e^(−(λ₀+s)b)).

This follows by summing the geometric series over the number of short gaps; the series converges because the integral is less than one. Static clump starts have stationary intensity κ₀=λ₀e^(−λ₀b), since a Poisson start initiates a new clump exactly when the preceding start gap is at least b. For the residual static-covered length R from a typical covered point, Campbell integration over component starts gives

E[1_(0 covered) e^(−sR)]=κ₀(1−E e^(−sB))/s.

Indeed, one component contributes ∫_0^B e^(−s(B−u))du=(1−e^(−sB))/s to this integral per unit length. If D∼Exp(s) is independent, the probability that the static model fails to cover [0,D] is

e^(−λ₀b)+κ₀(1−E e^(−sB))/s
 =e^(−λ₀b)(s+λ₀)/(s+λ₀e^(−(λ₀+s)b)).

Take s=λ₁. A moving-only uncovered gap has exponential(λ₁) length: its exposed endpoint concerns only intervals whose left endpoints are at or before that location; future left endpoints form an independent Poisson process of rate λ₁. Multiplying the moving-only hole intensity λ₁e^(−λ₁b−λmt) by the last static-failure probability yields

λe^(−λb−λmt) · λ₁/(λ₁+λ₀e^(−λb))
 =ρ_t θ,

the same effective cluster rate obtained in Theorem F. For λ₀=0 the correction is trivially θ=1. No independence across different gaps is inferred from this local calculation.

### Steps that could fail and their disposition

1. **Endpoint transformation and signs:** the right-endpoint shift is x+r+t max(V,0), and length is b+t|V|. The map preserves the marked intensity because it is a translation in x for each fixed mark. It is used separately at each t. No time-process independence is assumed.
2. **Background versus inserted marks in F1:** background blocking intervals have a common length for each *fixed* background mark, allowing (F2). Inserted lengths are independently integrated and contribute P(ℓ<h). Confusing these two operations would yield the wrong factorial density. Equalities at discrete mark lengths occur on zero-measure gap hyperplanes, so the density identity is an almost-everywhere identity sufficient for all its integrals.
3. **Hole count versus coverage:** local finiteness gives a genuine uncovered interval after every exposed endpoint and an exposed endpoint at each interior uncovered-component start. The possible initial uncovered segment is bounded by q_t; it is not discarded without a probability estimate.
4. **Uniform far kernel:** condition (T) is used on the growing cutoff (L^δ−b)/t. Fixed-h convergence alone is insufficient. The proof explicitly controls the relative kernel error at every h≥L^δ.
5. **Stationary atoms:** the local kernel mass is J, not zero, and therefore the count is compound Poisson. In particular its variance is μ(1+2J), not μ. Both the factorial-moment calculation and independent static-clump coefficient check give θ=1/(1+J).
6. **Moment method:** tightness, uniform integrability of each moment, and exponential-moment determinacy are all proved in Step 3. Bonferroni summation at −1 is not used: its factorial series need not converge when J≥1.
7. **Simplex factor:** the c free coordinates have volume A^c/c!, and the number of near/far patterns is binom(k−1,c−1). Their product reproduces the compound-geometric generating function; losing either factor would give incorrect count moments.
8. **Critical/heavier tail covariance:** the proof conditions on deleting every whole-target spanning mark and subtracts β_L from the common-hit intensity. Conditional point survival gains the factor e^β_L. This deletion is independent Poisson restriction, not an informal assertion of conditioning on rare holes.
9. **Three distance ranges:** near pairs have a polynomially small proportion which beats the maximal exponential correlation below the local threshold. Intermediate correlations are bounded; macroscopic conditional correlations vanish uniformly. Sending ε↓0 is done after L→∞. The p=2 threshold atom is explicitly excluded from the CDF convergence argument, as required for weak convergence.
10. **Mean limits:** Theorem G uses the old log-scale uniform integrability. Theorem H needs the stronger smaller-scale bound; its single-spanning-grain probability gives the required uniform exponential tail directly.

### Numerical and formal checks

- `second_checks.py` constructs exactly the marked intervals meeting [0,L] for exponential positive speeds mixed with a zero-speed atom. It samples endpoints in [0,L] with the base mark law; endpoints beyond L use the length-biased law of b+tU, a mixture of base marks and Gamma(2) speed marks. This includes arbitrarily large speeds without truncation. The code merges intervals directly and checks the coverage/endpoint-count boundary identity in every replicate. It used 49,500 samples across p₀=0,0.4,0.8, L=300,3000 and three centered times, in about 10.6 seconds, with one modest array per sample.
- These exponential-speed samples show visible finite-size effects. For p₀=0, L=300, z=0, the empirical coverage probability 0.4303 is appreciably above the limiting 0.3679. This is **not** presented as agreement within simulation error. The exact finite variance from the pair kernel is 1.3607, compared with empirical 1.3817 and limiting variance 1; the residual local kernel mass explains why the limit is slow. For p₀=0.8, L=3000, z=0, the empirical variance is 7.0313, the numerically integrated finite variance 7.5930, and the limiting variance 6.3626. Large cluster sizes increase sampling variation.
- `second_finite_checks.py` independently evaluates

  Var(H_L)=μ+2ρ_L∫_0^L (L−h)(k_t(h)−ρ_L)dh.

  For exponential moving speeds, k_t/ρ_L=(1−(1−p₀)e^(−x))exp(λ(1−p₀)t e^(−x)), x=(h−b)/t. All 18 sampled means were within five standard errors based on this finite variance. Integration in x was capped at 100 when L was larger. The omitted tail is bounded by 2ρ_L²Lt C exp(Ce^(−100))e^(−100), C=(1−p₀)/(1−e^(−100))+λ(1−p₀)t; this is negligible for the sampled parameters. Quadrature is a numerical check, not a formal certificate.
- A separate bounded-speed simulation has U=0 with probability p₀ and U=1 otherwise, L=3000, z=0, and 5,000 samples per p₀. At p₀=0.4, empirical coverage 0.4952 compares with corrected limit 0.5010 and uncorrected 0.3679. At p₀=0.8, empirical coverage 0.7678 compares with corrected 0.7621 and uncorrected 0.3679. Each corrected comparison is within one binomial standard error; this directly tests the consequential stationary-atom correction. The supplementary script took about 6.7 seconds.
- `critical_tail_checks.py` evaluates exact integrated-tail formulas in log coordinates for the explicit p=2 and p=1.5 models. The spanning means converge to their stated rates, macroscopic conditional common-hit intensities tend to zero, and the near-pair log bounds tend to −∞. These are algebra/asymptotic diagnostics rather than direct samples of the full heavy-tail coverage law. No gigantic arrays or unrepresentable velocities are generated.
- `ClusterAlgebra.lean` imports only Real.Basic, Linarith, Ring and FieldSimp. `lake env lean ~/brain_workers/TRIO_1011/op/E0103/ClusterAlgebra.lean`, from ~/lean_verify with a one-hour subprocess timeout, exited 0 in 35.930 seconds. It checks the piecewise equal-interval increment and the rational cluster-index identity. Its output contains harmless unused-simp/tactic warnings, no errors. There is no sorry, native_decide, or new axiom. It does not formalize the stochastic asymptotics.

## Final scope and verdict of this second attempt

The new interval-clump approach succeeded: it proves a centered law for all one-dimensional speed laws satisfying (T), including genuinely random speeds and stationary atoms, and a full one-dimensional logarithmic-power tail phase diagram. The higher-dimensional convex-grain route was recorded but not pursued; no theorem is claimed from it.

The source's unrestricted problem is still not fully resolved. Higher-dimensional centered laws, arbitrary oscillating or other one-dimensional finite-mean tails, general random/irregular grains, and more general thin-target distributions remain open within this work. VERDICT: PARTIAL, with stronger proved special cases than the first attempt. No matching literature solution or novelty claim is asserted.
