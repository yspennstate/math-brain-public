# E0103 — inertial cumulative coverage

Date: 2026-10-11. This is a partial answer, not a solution of the survey's unrestricted question.

## Exact source and model

Takis Konstantopoulos, *The mobile Boolean model: an overview and further results*, arXiv:1407.6834v1 (25 July 2014), PDF p.18, Open problem 1:

> We did not touch at all the coverage problem, i.e., the law of the random variable inf{t ≥ 0 : K ⊂ W(t)}. For the Brownian Boolean model, and when the diameter of R tends to infinity, the problem has been solved in [12]. What are the corresponding asymptotics for the inertial cases?

The source literally says “diameter of R”, although its target is denoted K; it does not specify a family of enlarging targets, a grain regularity assumption, or velocity-tail hypotheses here. Page 4 defines W(t) as the union of instantaneous covered sets over 0≤s≤t. It is cumulative, not simultaneous, coverage. Page 5 henceforth uses homogeneous Poisson germs and independence of grain shape and motion. Section 5, pp.8–9, takes independent velocities V with trajectories sV; its homogeneous ball-detection formula assumes E|V|<∞ and also discusses infinite mean speed. No restriction to bounded speeds is imposed by Open problem 1.

Our precise model: a marked Poisson process on R^d × R^d of intensity λ dx μ(dv), λ>0; each germ carries the deterministic closed ball rB, r>0. Let

W_r(t)= ⋃_(x,v) (x+[0,t]v+rB),  C(K)=inf{t≥0:K⊂W_r(t)}.

The constant ω_j is the volume of the unit ball in R^j, with ω_0=1. Put m=E|V| and a=λω_(d−1)r^(d−1)m.

## 1. Exact point law and local finiteness

For a fixed y, the initial positions of a particle of velocity v that cover y by t form y−[0,t]v+rB. Its volume is

ω_d r^d + ω_(d−1) r^(d−1)t|v|.                         (1)

Proof: rotate v to the first coordinate axis. The segment's interior contributes a cylinder of length t|v| and cross-sectional (d−1)-ball radius r; its two ends contribute two hemispheres, altogether one d-ball. They have disjoint interiors. For d=1 the cross-section has volume 1 and the interval has length 2r+t|v|. For v=0 the cylinder vanishes. Rotation preserves volume. Applying the Poisson void probability to the measurable initial-condition set gives

P(y∉W_r(t))=exp(−λω_d r^d−at).                       (2)

The source's (14)–(15) on p.9 instead print σ_(d−1)=dω_d as the cylinder coefficient. This is an error: e.g. in d=2 a capsule's area is πr²+2rt|v|, not πr²+2πrt|v|. We use (1), not that printed coefficient.

If m<∞, only finitely many trajectories meet any fixed compact spatial region during any bounded time interval, almost surely. Indeed, enclose the region and the grain in a ball of radius R. The marked intensity of trajectories meeting it by T is at most λ(ω_d R^d+ω_(d−1)R^(d−1)Tm)<∞. A Poisson count of finite mean is finite. Taking a countable exhaustion gives local finiteness simultaneously on all bounded regions and time intervals. Consequently W_r(t) is closed locally, and coverage of a fixed compact set is a closed condition in t: on a bounded time interval only finitely many relevant segments occur; their distance functions change by at most |v||t−s|, and the maximum over the compact target of their minimum distance is continuous. In particular {C(K)≤t}={K⊂W_r(t)} (when coverage occurs) and no issue of unattained infima arises.

## 2. Sharp leading order with bounded velocities

**Theorem A.** Let 0<m<∞ and |V|≤M almost surely, M<∞. Let K be any fixed compact set in R^d with nonempty interior. Then, as L→∞,

C(LK)/log L → d/a  almost surely and in L¹.          (3)

No isotropy, direction density, or lower bound on nonzero speed is required. Atoms at zero are allowed. Balls and cubes are included.

### Proof, upper bound

First consider a cube Q_L of side L (a translated cube is equally valid). Fix ε>0 and choose 0<δ<r sufficiently small that

(1+ε)((r−δ)/r)^(d−1)>1.

For d=1 this holds for every δ<r. There is a δ-net N_L of Q_L with |N_L|≤A_δ(1+L)^d; a cubic lattice of mesh δ/√d, with its closest points to Q_L, supplies one. If every point of N_L is covered by radius-(r−δ) grains, then every point of Q_L is covered by radius-r grains: choose a net point within δ and use the triangle inequality for distance to a segment. The same marked process is used for both radii. Thus, writing a_δ=λω_(d−1)(r−δ)^(d−1)m,

P(C(Q_L)>t) ≤ A_δ(1+L)^d exp(−λω_d(r−δ)^d−a_δt). (4)

At t=(1+ε)d log L/a this is O(L^(−η)) for some η>0. This proves the upper bound in probability. For L=2^n it is summable in n; Borel–Cantelli proves the upper bound along dyadic side lengths.

To obtain the exact almost-sure coefficient for all L, use side lengths L_n=b^n, for arbitrary fixed b>1, instead of only dyadic lengths. The same summability holds. For centered cubes coverage time is monotone in side length. For b^n≤L≤b^(n+1), sandwich C(Q_L) between the two cube times. The ratios log(b^(n+1))/log(b^n) tend to 1. A countable sequence of ε↓0 proves the upper limsup ≤d/a almost surely.

### Proof, lower bound

At a deterministic time t, a trajectory covering y must start within distance Mt+r of y. Choose n_L(t) points inside Q_L mutually separated by more than 2(Mt+r), using a lattice of spacing 3(Mt+r). For L/(Mt+r) large, n_L(t)≥c_d(L/(Mt+r))^d. The sets of marked initial conditions that cover distinct selected points are disjoint, because their projections to initial-position space lie in disjoint balls. Counts in these sets are independent Poisson variables. Therefore the selected points are independently uncovered with probability q(t)=exp(−λω_d r^d−at), and

P(C(Q_L)≤t) ≤ (1−q(t))^n_L(t) ≤ exp(−n_L(t)q(t)). (5)

At t=(1−ε)d log L/a, 0<ε<1, this is at most

exp(−c L^(dε)/(log L)^d)                           (6)

for all sufficiently large L. It tends to zero and is summable on geometric L_n. The same monotonic interpolation proves the almost-sure lower liminf ≥d/a. Together with the upper bound, this proves almost-sure convergence for cubes.

### General targets and L¹

There exist fixed cubes Q_in⊂K⊂Q_out with positive inner side length and finite outer side length. Their centers may differ. Then LQ_in⊂LK⊂LQ_out. For each family of scaled cubes the previous estimates are uniform in their centers, so convergence in probability follows directly. To justify almost-sure interpolation for these potentially moving centers, use instead the bounds at geometric L_n and enclose all LQ_out, L∈[L_n,L_(n+1)], in one cube of side O(L_n), centered at the origin. For the lower bound, place a fixed cube of side cL_n in the common interior of LQ_in for L in a sufficiently fine geometric interval. Such a common cube exists if b>1 is sufficiently close to 1: the center moves by at most (b−1)L_n times the fixed center norm, while its minimum side is proportional to L_n. Apply (4) and (6) to these deterministic cubes. Their logarithmic sizes equal log L_n+O(1), which gives the same coefficient. Countably many ε↓0 and Borel–Cantelli complete the almost-sure assertion for K.

For uniform integrability one need not use bounded speed: (4) with fixed δ=r/2 works whenever 0<m<∞. For L≥e, X_L=C(LK)/log L satisfies

P(X_L>u) ≤ min(1,B L^d exp(−a_(r/2) u log L)),

with B independent of L. For u≥2d/a_(r/2), this is ≤B exp(−a_(r/2)u/2). This exponential bound implies

E[X_L 1_(X_L>H)] ≤ H B exp(−a_(r/2)H/2) + ∫_H^∞ B exp(−a_(r/2)u/2)du →0

uniformly in L≥e. Almost-sure convergence, hence convergence in probability, and uniform integrability prove L¹ convergence. This completes Theorem A.

## 2a. All compact targets with a Minkowski dimension

**Theorem A′.** Under the bounded-speed assumptions of Theorem A, let K be a nonempty compact set whose Minkowski dimension α exists. Then

C(LK)/log L → α/a in probability and in L¹,
E C(LK)/log L → α/a.                                (3′)

This includes α=0; its conclusion there is o(log L), not an equivalent with zero denominator. Almost-sure convergence for arbitrary thin K is not claimed.

Proof: let N(K,η) be the least number of balls of radius η covering K. The dimension assumption means log N(K,η)/log(1/η)→α. A maximal finite h-separated set in K exists by compactness; its h-balls cover K (otherwise one more point could be added), so its cardinality is at least N(K,h). Conversely, disjoint radius-h/2 balls centered in K give a packing bound by a radius-h/4 cover, though only the preceding lower bound is needed.

For the upper bound choose δ∈(0,r) and a δ-net for LK with N(K,δ/L) points, allowing centers outside LK. Its cardinality is L^(α+o(1)). The same net argument as (4) gives P(C(LK)>t)≤L^(α+o(1))exp(−a_δt), up to a fixed factor. For any u>α/a choose δ small enough that a_δu>α. At t=u log L this probability tends to zero. If α=0, every u>0 works with any fixed δ.

For the lower bound, when α>0 and 0<u<α/a, set t=u log L and choose a maximal h_L-separated set in K with h_L=3(Mt+r)/L. After scaling, its points have disjoint initial-position influence balls. Its cardinality n_L≥N(K,h_L)=L^(α+o(1)), because log(1/h_L)/log L→1. By (2), n_Lq(t)=L^(α−au+o(1))exp(−λω_dr^d)→∞. Independence gives P(C(LK)≤t)≤exp(−n_Lq(t))→0. For α=0 the lower bound C≥0 suffices. Together these bounds prove convergence in probability. The same uniform exponential tail bound as in Theorem A follows by enclosing LK in a cube and implies uniform integrability. Hence convergence in L¹ and of expectations follow. This proves (3′).

## Scope at this stage

Theorem A supplies the sharp first-order asymptotic in a substantive special case. It does not supply centered fluctuations in dimensions d≥2, nor a theorem for arbitrary velocity tails or arbitrary thin compact targets. The diameter alone cannot determine the answer for arbitrary compact targets: two points at distance L have two detection times with tight marginal exponential laws, so their coverage time is tight by the union bound, whereas Theorem A's solid cubes grow logarithmically.

## 2b. Extension to unbounded speeds with a logarithmic moment

**Theorem D.** Let 0<m=E|V|<∞ and suppose

(log h) E[|V|1_(|V|>h)] →0 as h→∞.                 (T)

For fixed ball grains, every nonempty compact target K with an existing Minkowski dimension α satisfies (3′). In particular (T) holds whenever E[|V|log(2+|V|)]<∞. If instead the stronger hypothesis E|V|^(1+η)<∞ holds for some η>0, then the almost-sure conclusion of Theorem A also holds for every compact K with nonempty interior.

### Proof of the tail extension

The upper bound and uniform-integrability argument of Theorem A′ require only finite positive m, so remain valid. Assume α>0, fix ε∈(0,1), and let

t=(1−ε)α log L/a,   δ∈(0,ε),   b_L=L^δ/t.

Divide the marked Poisson process into short-speed marks |V|≤b_L and fast marks |V|>b_L. These two processes are independent. Short trajectories have influence radius at most R_L=L^δ+r. Select a maximal set in LK with mutual distances at least 3R_L. Its cardinality n_L is at least N(K,3R_L/L)=L^((1−δ)α+o(1)). The hit sets of these points for short marks are disjoint, so their short-uncovered indicators are independent with common probability

q_short=exp(−λ E[(ω_dr^d+ω_(d−1)r^(d−1)t|V|)1_(|V|≤b_L)])
       ≥exp(−λω_dr^d−at).

Thus U, their number, satisfies

P(U=0)≤exp(−n_L q_short)→0,
n_Lq_short≥L^(α(ε−δ)+o(1))exp(−λω_dr^d)→∞.

The intensity of fast marks covering any specified test point equals

γ_L=λω_dr^d P(|V|>b_L)
    +λω_(d−1)r^(d−1)t E[|V|1_(|V|>b_L)].

Since log b_L=δ log L−log t∼δ log L, t/log b_L is bounded and (T) implies γ_L→0. Condition on the short process and its U uncovered selected points. When U>0, the expected number hit by fast marks is at most γ_L U. Markov's inequality bounds the conditional probability that all U are hit by γ_L. It follows that

P(C(LK)≤t)≤P(U=0)+γ_L→0.                            (13)

This proves the lower bound. If α=0 the upper bound alone proves convergence to zero. Uniform integrability proves convergence in L¹ and of expectations.

To prove the sufficient logarithmic-moment condition, for h>1 note

(log h)E[|V|1_(|V|>h)]≤E[|V|log(2+|V|)1_(|V|>h)]→0,

by integrability and decreasing tail truncations.

For the stronger power moment, put B=E|V|^(1+η). Then P(|V|>b)≤B/b^(1+η) and E[|V|1_(|V|>b)]≤B/b^η. Consequently

γ_L≤c B (1+t)^(1+η)L^(−δη)

for large L. This is summable along geometric L_n; P(U=0) is also summable because its exponent grows as a positive power of L. The upper bound is summable along that sequence as before. Borel–Cantelli and the same common-inner-cube/outer-cube interpolation from Theorem A give almost-sure convergence for solid K. This proves Theorem D.

The fast process need not have a finite spatial range. Equation (13) uses only its small marginal coverage probability and independence from the short process; assuming independence of fast coverage across test points would be an error. Theorem B below violates (T) and exhibits why an unrestricted finite-mean extension fails.

## 2c. Finite mean alone in spatial dimension at least two

**Theorem E.** Suppose 0<m=E|V|<∞, with no further tail or directional assumptions. If d≥2 and K is compact with nonempty interior, then

C(LK)/log L → d/a almost surely and in L¹.            (14)

More generally, if a nonempty compact K has an existing Minkowski dimension α>1, then C(LK)/log L→α/a in probability and in L¹, and its expectation has the same limit. This theorem does not assert a finite-mean-only result for dimension α≤1.

### Uniform tube-packing bound

Let n test points be mutually separated by s, with r≤s≤L, all lying in a cube of side O(L). For every fixed test point y and every unit vector e, at most C_d L/s other test points z can satisfy

|projection_(e-perpendicular)(z−y)|≤2r.              (15)

Proof: balls of radius s/3 around the eligible z have disjoint interiors. Their centers have perpendicular distance at most 2r from the line y+Re, and axial coordinates of absolute value at most the diameter of the cube, O(L). The balls therefore lie in a capped tube of length O(L+s) and radius 2r+s/3. Its volume is at most C_d(L+s)(r+s)^(d−1)≤C′_d Ls^(d−1). Each ball has volume ω_d(s/3)^d. Dividing proves (15), uniformly in the orientation e. This elementary packing argument uses no density of velocity directions.

### Poisson covariance and its average

Consider first a cube of side L. Fix ε∈(0,1), δ∈(0,ε),

t=(1−ε)d log L/a,  b_L=L^δ/t,

and select n≥c L^(d(1−δ)) points from a lattice of spacing s=3(L^δ+r). Their short-speed initial-position hit sets (|V|≤b_L) are disjoint. Let U be the number uncovered by the *full* process. Each point is uncovered with probability q=exp(−λω_dr^d−at).

For distinct y,z define I(y,z) as the intensity of marked initial conditions covering both by t. Inclusion–exclusion of their finite-intensity hit sets and the void law give exactly

P(y,z both uncovered)=q² exp(I(y,z)).                 (16)

Only fast marks contribute to I, since short hit sets are disjoint. Put

γ_L=λω_dr^d P(|V|>b_L)
    +λω_(d−1)r^(d−1)t E[|V|1_(|V|>b_L)].

Then 0≤I(y,z)≤γ_L. Because m<∞ and b_L→∞, γ_L=o(log L): divide by log L and use that the truncated first-moment tail tends to zero.

For a fixed fast velocity v, the two initial-position capsules can intersect only if the perpendicular distance of y−z to the line directed by v is at most 2r. Indeed, their orthogonal projections are radius-r balls centered at the projections of y,z. Each capsule intersection has volume at most the single-capsule volume (1). By (15), for every fixed y,v at most C L/s choices of z have nonzero intersection. Tonelli's theorem, applied to nonnegative volumes, therefore gives

∑_(y≠z) I(y,z) ≤ C n (L/s) γ_L.                    (17)

For 0≤I≤γ, the elementary integral identity e^I−1=∫_0^I e^u du implies e^I−1≤Ie^γ. From (16) and the variance expansion of a sum of indicators,

Var(U)/(EU)²
 ≤ 1/(nq) + (1/n²)∑_(y≠z)(e^(I(y,z))−1)
 ≤ 1/(nq) + C e^(γ_L) γ_L (L/s)/n.                 (18)

The first term is at most C L^(−d(ε−δ)). The second is

L^(−(d−1)(1−δ)+o(1)),

because γ_L=o(log L), so e^(γ_L) max(γ_L,1)=L^o(1), and n is of order (L/s)^d. Since d≥2, both terms tend to zero. Chebyshev's inequality gives P(U=0)≤Var(U)/(EU)²→0, which proves the lower bound for coverage. The net upper bound and uniform integrability, which require only finite mean, complete convergence in probability and L¹.

Moreover, both terms in (18) are bounded by negative powers of L for all sufficiently large L. They are summable on geometric L_n. The upper estimates are also summable. Borel–Cantelli and the common-inner-cube/outer-cube interpolation already proved in Theorem A establish almost-sure convergence for every solid K. This proves (14).

### Compact targets of dimension α>1

At t=(1−ε)α log L/a, take a maximal s-separated subset of LK with s=3(L^δ+r). Its size is at least N(K,s/L)=L^((1−δ)α+o(1)). The same tube-packing bound applies because LK lies in a cube of side O(L). The diagonal term in (18) is at most L^(−α(ε−δ)+o(1)); the second term is at most

L^(−(1−δ)(α−1)+o(1))→0.

No upper bound on n is needed for these estimates. The net upper bound and uniform integrability prove the stated probability and L¹ limits. This completes the proof of Theorem E.

The distinction between α>1 and α≤1 comes from the tube-packing estimate, not from an assumption that isotropy can be imposed. It is consistent with the heavy-tail line example below.

## 3. A finite-mean heavy-tail case with an exponential limit

**Theorem B.** Work in d=1 with target [0,L]. Let speeds be nonnegative and have survival function

P(V>u)=1/(u log u (log log u)²),   u≥u₀=exp(e),

and P(V>u)=1/exp(e+1) for 0≤u<u₀. This is a probability law: it puts the complementary mass at zero, and its positive part lies above u₀. For fixed λ,r>0,

C([0,L])/log log L ⇒ Exp(rate λ).                    (7)

In particular C([0,L])/log L→0 in probability, although 0<EV<∞. Thus finite mean speed alone does not imply the logarithmic first-order formula of Theorem A.

### Tail integrals

For h≥u₀, substituting w=log log u gives

∫_h^∞ P(V>u)du = 1/log log h,

EV = u₀ P(V>u₀) + 1/log log u₀ = 1/e + 1.

Also

E[V 1_(V>h)] = hP(V>h)+∫_h^∞P(V>u)du
             = 1/(log h (log log h)²)+1/log log h.   (8)

The tail is decreasing, continuous at u₀, and tends to zero. These computations prove validity and finite positive mean without any truncation approximation.

### Long grains

Fix s>0, and set t=s log log L and H=(L−2r)/t, which exceeds u₀ for large L. Write the start of a swept interval as A=x−r and its length as ℓ=tV+2r. It spans [0,L] exactly when A≤0 and A+ℓ≥L. For fixed V, the eligible A form [L−ℓ,0], of length (ℓ−L)_+. Therefore the number of single grains spanning [0,L] is Poisson with mean

β_L=λ E[(tV+2r−L)_+]
   =λt ∫_H^∞ P(V>u)du
   =λs log log L / log log((L−2r)/(s log log L)) →λs. (9)

Any such grain ensures coverage. For speeds V>H, interval lengths exceed L. The A for which the interval intersects [0,L] form [−ℓ,L], length ℓ+L, while spanning A have length ℓ−L. Thus long grains that intersect but do not span have total mean

2λL P(V>H)
 =2λL/[H log H (log log H)²] →0.                    (10)

Endpoint equalities have zero intensity in A, so they do not affect these formulas. Markov's inequality shows that with probability tending to one, every long grain meeting the target spans it.

### Short grains leave many independent uncovered test points

Put h=√L/t. Short grains have V≤h, hence interval length ≤√L+2r. Choose deterministic test points inside [0,L] separated by 2(√L+2r). Their number n_L is at least c√L for large L. A short grain covers a point y only if its start A lies in [y−(√L+2r),y]. These intervals are disjoint for distinct chosen points. Restrictions of the marked Poisson process to their hit sets are independent. Thus the number U_L of test points uncovered by short grains is binomial with parameters n_L and

q_L=exp(−λ E[(tV+2r)1_(V≤h)])
   ≥exp(−λ(2r+tm))
   =exp(−2λr)(log L)^(−λsm).

Consequently n_L q_L→∞ and P(U_L=0)≤exp(−n_Lq_L)→0.

### Intermediate grains cannot cover all those points

Intermediate grains have h<V≤H. They form a Poisson process independent of both the short and long processes. The marked intensity of intermediate grains covering any specified point equals

γ_L=λ E[(tV+2r)1_(h<V≤H)].

Since h,H→∞ and the law has no atoms there, (8) gives

γ_L ≤2λr P(V>h)+λt(F(h)−F(H)),
F(u)=1/log log u+1/(log u (log log u)²).

Let A_L=log log L. Then

log h = (1/2)log L−log(sA_L),
log H = log L−log(sA_L)+o(1),
log log h = A_L−log 2+o(1),
log log H = A_L+o(1).

It follows by taking the difference of reciprocal denominators that F(h)−F(H)=O(A_L^(−2)); the second terms in F are O(1/(log L A_L²)). As t=sA_L, γ_L→0. The probability that a specified point is covered by intermediate grains is 1−exp(−γ_L)≤γ_L.

Condition on the entire short process and the resulting set of U_L uncovered test points. If U_L>0, the expected number of these points covered by intermediate grains is ≤γ_L U_L. Markov's inequality gives conditional probability at most γ_L that *all* U_L points are covered by intermediate grains. This argument does not assert independence of intermediate coverage between test points.

### Distributional conclusion

Let S_L be the event of at least one spanning grain, and B_L the event of a long nonspanning grain meeting the target. If full coverage occurs and S_L does not, then either B_L occurs, U_L=0, or all the short-uncovered test points are covered by intermediate grains. Hence

0 ≤ P(C([0,L])≤t)−P(S_L)
  ≤ P(B_L)+P(U_L=0)+γ_L →0.

By (9), P(S_L)=1−exp(−β_L)→1−exp(−λs). This proves convergence of the distribution functions at every s>0. At s<0 the distribution functions vanish. At s=0, the static model's coverage probability tends to zero: choose linearly many points separated by more than 2r; their initial coverage indicators are independent and have probability 1−exp(−2λr)<1. Thus (7) follows, including its continuity point at zero.

Distributional convergence in (7) implies tightness of C/log log L. Multiplying this tight family by (log log L)/(log L)→0 proves the final assertion. This completes the proof of Theorem B.

Theorem B does not contradict Open problem 1, which asks a question rather than asserts a universal scale. It demonstrates why a single finite-mean-speed answer would require additional hypotheses. It is a new derivation in this attempt, not a claimed theorem found in the literature.

## 4. A Gumbel law for deterministic one-dimensional motion

**Theorem C.** In d=1, let every velocity equal c>0. For fixed λ,r>0,

λc C([0,L])+2λr−log(λL) ⇒ G,
P(G≤z)=exp(−exp(−z)).                                (11)

### Proof

The interval starts A=x−r form a stationary Poisson process of rate λ. Every swept interval has common length ℓ=ct+2r. For z∈R fixed, put ℓ_L=(log(λL)+z)/λ and t_L=(ℓ_L−2r)/c>0 for large L. Let N_L count starts in [0,L], and label the starts in [0,∞) as A₁<A₂<⋯. Their successive forward gaps E_i=A_(i+1)−A_i, i≥1, are iid exponential of rate λ. This follows directly from independent increments: the first arrival after a deterministic location is exponential, and iterating the same property at successive arrival times gives independent exponential gaps. Define D_L to be the event E_i≤ℓ_L for every i≤N_L (vacuously true if N_L=0).

Let A₀ be the last start before zero. Coverage and D_L can differ only on the following events: 0 is uncovered; A₁−A₀>ℓ_L; or a start A in [max(0,L−ℓ_L),L] has forward gap greater than ℓ_L. Outside these events, the interval beginning at A₀ covers zero and reaches A₁; every internal gap at A≤L−ℓ_L is checked by D_L and would create a hole before L if it exceeded ℓ_L. Conversely, if coverage holds but D_L fails, its offending gap must start within ℓ_L of the right endpoint. This also handles N_L=0: A₁>L and A₁−A₀≤ℓ_L imply that A₀'s interval covers all of [0,L].

The probability that 0 is uncovered is exp(−λℓ_L). The independent exponential distances −A₀ and A₁ give P(A₁−A₀>ℓ_L)=(1+λℓ_L)exp(−λℓ_L). Integrate over 0≤−A₀≤ℓ_L and add P(−A₀>ℓ_L) to verify this identity. The expected number of exceptional right-end starts is at most λℓ_L exp(−λℓ_L). Here the Poisson insertion identity is E∑_(A∈Π∩I) f(A,Π without A)=λ∫_I E f(a,Π)da. On a bounded window it follows by conditioning on its Poisson count n, integrating n iid uniform points, and using nP(N=n)=λ|window|P(N=n−1); an increasing exhaustion proves the identity here. Take f(a,Π)=1_(Π∩(a,a+ℓ_L)=∅) and I=[max(0,L−ℓ_L),L]. The integrand is exp(−λℓ_L) by the void law. A union bound gives

|P(C([0,L])≤t_L)−P(D_L)| ≤ (2+2λℓ_L)exp(−λℓ_L)→0. (12)

Although N_L depends on the gaps, no independence with N_L is used. Take δ_L=L^(−1/4), n_−=floor((1−δ_L)λL), and n_+=ceil((1+δ_L)λL). Since N_L is Poisson with mean and variance λL, Chebyshev's inequality gives P(N_L∉[n_−,n_+])→0. On this event's complement,

{max_(i≤n_+)E_i≤ℓ_L} ⊂ D_L ⊂ {max_(i≤n_−)E_i≤ℓ_L}.

For either deterministic n=n_±,

P(max_(i≤n)E_i≤ℓ_L)=(1−e^(−λℓ_L))^n
 =(1−e^(−z)/(λL))^n →exp(−e^(−z)).

The limit follows from log(1−u)=−u+O(u²), n/(λL)→1, and n/L²→0. The sandwich and (12) prove (11). This completes the proof.

## 5. Zero and infinite mean speed

If m=0, then V=0 almost surely. Coverage times equal zero on initial full coverage and infinity otherwise. For a solid target LK the initial full-coverage probability tends to zero, by the same independent static test-point argument.

If m=∞ and r>0, then for every t>0 the entire R^d is cumulatively covered almost surely, and all compact coverage times are zero as infima. Proof: apply the pointwise void law to radius r/2. The marked hit set has infinite intensity, so every fixed point is covered with probability one (obtain this by monotone exhaustion with finite-intensity sets). Take a countable lattice that is an r/2-net of R^d. With probability one all its points belong to W_(r/2)(t). Enlarging the same grains to radius r covers every point of R^d, by the triangle inequality. Intersect these probability-one events over positive rational t; monotonicity then covers every real t>0. At t=0 there need not be coverage. Local finiteness of swept grains fails in this regime, so there is no conflict with the finite-mean attainment argument.

## Remaining gap

The source's unrestricted problem is not solved here. The strongest higher-dimensional first-order result is Theorem E: finite positive mean speed suffices for solid targets in d≥2, with almost-sure and L¹ convergence to d/a, and for compact targets of dimension α>1 with probability and L¹ convergence to α/a. Theorem D handles all existing Minkowski dimensions under a logarithmic speed-moment condition. The second serious attempt, fully written in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md), proves a centered one-dimensional Gumbel limit for every speed law satisfying (T), including an explicit correction for stationary atoms, and gives exponential and truncated-exponential coverage laws for all tails c/[u(log u)^p], p>1. The earlier log-log example remains another proved regime. Missing are centered fluctuations for general velocity laws in d≥2, a classification of arbitrary finite-mean one-dimensional tails outside the proved classes, general random/irregular grains, and finer limits for thin/fractal target families. No matching published solution was identified by the successful searches; OpenAlex was unavailable, so the literature status is not exhaustive.

## Hostile-referee audit and computations

1. **Meaning of coverage:** checked the source definition, p.4, and used cumulative coverage throughout. Finite-mean local finiteness and continuity justify replacing the infimum event by containment at a fixed time. Infinite mean is treated separately.
2. **Cylinder constant:** derived the volume from a cylinder plus hemispheres, including d=1 and v=0. Direct 2D Poisson-particle simulations with λ=0.4, r=0.5, speeds 1, and t=0,1,2,5 (12,000 independent samples each) agreed within two standard errors with the corrected law. At t=1 the simulated void probability was 0.496, the correct value 0.489604, and the printed-source value 0.207880. See spatial_checks.py and spatial_checks.json.
3. **False independence:** exact independence is used only for disjoint marked hit sets, or for disjoint velocity classes. Theorem E uses exact two-point covariance, not independence. Theorems B and D condition on the slow process and use a first-moment bound for the remaining process; no independence between fast-covered test points is assumed.
4. **Uniform tube geometry:** disjoint packing balls prove the O(L/s) bound even for an atom of velocities in a lattice direction. Tests with 10×10, 20×20, 40×40 lattices, axes and 100 random directions found maxima 9,19,39 other centers in a radius-2 tube at spacing 10. This checks the dangerous alignment case; it does not substitute for the packing proof.
5. **Tail truncation:** in Theorem E the fast marginal intensity is o(log L), not necessarily o(1). The exponential covariance factor is therefore L^o(1), and the tube-count power beats it only when target dimension exceeds one. Theorem D instead requires o(1). The heavy-tail counterexample shows that confusing these two requirements would invalidate a d=1 extension.
6. **Almost-sure interpolation:** for Q_in=c+[−s/2,s/2]^d choose b>1 with (b−1)||c||_∞≤s/4. The fixed cube L_nc+[−sL_n/4,sL_n/4]^d lies in every LQ_in for L∈[L_n,bL_n]; an O(L_n) centered outer cube encloses every LQ_out in the same interval. This supplies the inclusions needed for continuum-L interpolation, without assuming LK is nested.
7. **Heavy-tail proof:** mean speed is exactly 1+1/e. Transformed numerical integration at log log h=1,2,5,10 agrees with 1/log log h to better than 10^−10. Exact asymptotic intensities in log coordinates show the spanning mean tending to 1 at t=log log L, while nonspanning-long and intermediate point intensities tend to zero. The intermediate convergence is slow (about 0.0192 at log L=10^16), so an ordinary-size simulation would not establish the asymptotic regime. No enormous speeds or unbounded-memory samples were generated.
8. **Gumbel endpoints:** the proof explicitly includes the gap from the last start before zero to the first start after zero, and the final truncated gap at L. A direct particle simulation used 5,000, 3,000, 1,500 samples at L=100,1000,10000, respectively. For L=1000 the empirical CDF at normalized value zero was 0.370 versus the Gumbel value 0.367879. Across 20,000 random finite configurations, all 709 differences between the full-coverage and internal-gap events were accounted for by the stated boundary exceptions. See checks.py and checks.json.
9. **Random sample count:** the deterministic-index maximum sandwich avoids treating N_L as independent of exponential spacings. Its Poisson count concentration follows from its explicit mean and variance.
10. **Lean scope:** Geometry.lean checks the exact spanning-interval criterion, disjoint influence intervals, and the 2L nonspanning-length identity. The final command `lake env lean ~/brain_workers/TRIO_1011/op/E0103/Geometry.lean`, run from ~/lean_verify, exited 0 in 61.093 seconds. Only Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith are imported. No sorry, axiom declaration, or native_decide is used. These are kernel-checked deterministic lemmas; the stochastic limits are complete written proofs, not Lean formalizations. The first run failed because the tactic import alone did not import the real-number structure; adding Data.Real.Basic fixed it.

Computations finished in roughly 2.6 and 2.1 seconds of reported script time, with one small array per replicate; jobs were far below 1 GB. No empirical result is promoted to a proof. The full-question verdict remains PARTIAL.

## Second serious attempt — 2026-10-11

Two new routes were recorded: random-interval clumps/M/G/∞ queues, and mixed-volume rates for anisotropic convex grains. The interval route was pursued. All proofs and its separate referee audit are in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md).

Theorem F proves, with U=|V|, m=EU>0, p₀=P(U=0),

λmC([0,L])+2λr−log(λL)−log θ ⇒ standard Gumbel,
θ=(1−p₀)/(1−p₀+p₀exp(−2λr)),

under (log h)E[U1_(U>h)]→0. This includes all bounded speed laws with positive mean and all finite logarithmic speed moments. The count of uncovered components at a centered time has a compound-Poisson/geometric limit when p₀>0. The stationary correction is not a heuristic: exact exposed-endpoint factorial moments yield it.

For P(U>u)∼c/[u(log u)^p], the second attempt proves the entire p>1 phase diagram:

- 1<p<2: C([0,L])/(log L)^(p−1) ⇒ Exp(λc/(p−1)), and normalized mean →(p−1)/(λc).
- p=2: C([0,L])/log L ⇒ min(Exp(λc),1/(λm)), and normalized mean →(1−exp(−c/m))/(λc).
- p>2: the centered Gumbel law above applies.

The critical and heavier cases are proved by conditioning the Poisson process on the absence of any single grain spanning the target, subtracting that common-hit intensity, and controlling the remaining covariance at all three separation scales. Two further deterministic algebraic lemmas passed Lean in ClusterAlgebra.lean. Simulations include stationary atoms, unbounded exponential speeds via exact length-biased sampling, and separate finite-size second-moment integration. None replaces the written probability proofs. The full-question verdict remains PARTIAL.
