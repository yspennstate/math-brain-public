# All subsequential limits of the alternating-branch tree

The graph below is the tree constructed in the earlier T160 report. The new
conclusion is a classification of its limiting conditional laws. This is a
statement about a nontransitive tree, not about percolation on Z³.

## Theorem

Put N₀=0 and Nₖ=2^(k²+10) for k≥1. In rooted branch A, every vertex at
generation i−1 has one child if

    Nₖ₋₁ < i ≤ Nₖ₋₁+2k−1

for an odd k, and two children otherwise. Branch B uses the same prescription
with even k. Join their roots a,b to a new vertex o by edges e_A,e_B. Call the
resulting tree T. All generation numbers below are measured from a or b.

The tree has maximum degree three, p_c(T)=1/2, and almost surely no infinite
open cluster at p=1/2. There are two explicitly specified probability laws
Q_A,Q_B on its edges such that the set of all cylinder subsequential limits of

    μₙ = P₁/₂( · | o connects to the sphere of radius n+1)

is exactly

    { λ Q_A + (1−λ) Q_B : 0≤λ≤1 }.                         (1)

Under Q_A, e_A is open, the A branch has the uniform-spine law defined below,
and all other edges have independent Bernoulli(1/2) states. Q_B is defined
with A and B exchanged. Every law in (1) has exactly one infinite open cluster,
and that cluster contains o and has exactly one infinite simple ray from o.

In particular, the set of subsequential limits of μₙ(e_A open) is [1/2,1].
Thus the earlier two single-edge limits are endpoints of a full interval of
distinct limiting laws. No assertion of literature novelty is made.

## 1. Rechecking the earlier construction

For either branch let bᵢ∈{1,2} be its offspring numbers, let Zₙ count the open
vertices connected to its root in generation n, and let D(n) count the indices
i≤n with bᵢ=1. At edge parameter p write

    M₀(p)=1,    Mₙ(p)=Eₚ Zₙ=(2p)ⁿ 2^(−D(n)).

Conditionally on Zᵢ₋₁, Zᵢ is Binomial(bᵢZᵢ₋₁,p). Its conditional second moment
is (pbᵢ)²Zᵢ₋₁²+pbᵢ(1−p)Zᵢ₋₁. Dividing the expectation by Mᵢ(p)² gives

    Eₚ[Zₙ²]/Mₙ(p)² = 1+(1−p) Σᵢ₌₁ⁿ 1/Mᵢ(p).

Cauchy–Schwarz applied on {Zₙ>0} therefore implies

    qₚ(n):=Pₚ(Zₙ>0) ≥ [1+(1−p) Σᵢ₌₁ⁿ 1/Mᵢ(p)]⁻¹.     (2)

Hereafter omit p when p=1/2; then Mₙ=2^(−D(n)). Since Mᵢ≥Mₙ for i≤n,

    q(n) ≥ Mₙ/(Mₙ+n/2) ≥ Mₙ/(n+1).                      (3)

For a full binary branch the critical survival probabilities s_L obey
s₀=1 and s_{L+1}=s_L−s_L²/4. Since

    1/(s−s²/4)−1/s = 1/[4(1−s/4)] ≥ 1/4,

we have s_L≤4/(L+4). If the last L generations of a branch are binary, a union
bound conditional on generation n−L gives

    q(n) ≤ Mₙ₋L s_L ≤ 4 Mₙ/(L+4).                       (4)

For k=1, N₀+2k−1=1≤N₁/2. For k≥2, Nₖ₋₁≤Nₖ/8 and 2k−1≤Nₖ/8, so
Nₖ₋₁+2k−1≤Nₖ/4. The latter elementary inequality follows from
2^(k²+7)≥2ᵏ≥2k−1 for k≥2; the last inequality follows by induction.
Consequently the suppression intervals are disjoint, and the binary plateau
ending at Nₖ has length

    Lₖ=Nₖ−Nₖ₋₁−(2k−1) ≥ Nₖ/2.                          (5)

Counting suppressed levels gives

    D_A(Nₖ)+D_B(Nₖ)=k²,
    D_A(Nₖ)−D_B(Nₖ)=(−1)^(k+1)k.                        (6)

The second identity follows by induction after adding the next signed odd
number; equivalently the two counts are (k²±(−1)^(k+1)k)/2.
For Nₖ₋₁<n≤Nₖ and k≥2, D_s(n)/n≤k²/Nₖ₋₁→0 for s=A,B, while
D_s(n)→∞. At p≤1/2, Mₙ(p)≤2^(−D_s(n))→0. Markov's inequality gives
extinction from the branch root. From any fixed generation j the expected
number of open descendants at generation n is Mₙ(p)/Mⱼ(p)→0 for p>0;
p=0 is immediate. Thus every vertex has no infinite open descendant component.
Any infinite component of a rooted locally finite tree has a vertex nearest
o, with an infinite descendant component. Taking the countable union over
vertices proves absence of all infinite clusters at p≤1/2.

For p>1/2, log Mₙ(p)=n log(2p)−D_s(n)log 2 grows at least linearly with a
positive slope for large n. Hence Σ1/Mₙ(p)<∞. Equation (2) bounds qₚ(n)
away from zero. The decreasing events {Zₙ>0} then have an intersection of
positive probability. A finite-branching tree reaching every generation has
an infinite ray: at each vertex choose a child with descendants arbitrarily
far away. The attachment edge has positive probability p of being open, so
o percolates for p>1/2. This proves p_c(T)=1/2 and the extinction assertions.

By (3)–(6), at odd k,

    q_A(Nₖ)/q_B(Nₖ) ≤ 8 (Nₖ+1)/Nₖ · 2^(−k) ≤16·2^(−k), (7)

and at even k the same inequality holds with A and B exchanged.

For later reference set

    wₙ=q_A(n)/(q_A(n)+q_B(n)).

Thus w_{Nₖ}→0 along odd k and w_{Nₖ}→1 along even k.

The attachment offset can be checked directly. Let Uₙ be the event that e_A
is open and A reaches generation n, and let Vₙ be the analogous B event.
Then the radius-n+1 event is Eₙ=Uₙ∪Vₙ. These two events are independent with
probabilities uₙ=q_A(n)/2 and vₙ=q_B(n)/2. Since {e_A closed}∩Eₙ has
probability vₙ/2,

    μₙ(e_A open)=1−vₙ/[2(uₙ+vₙ−uₙvₙ)].                 (8)

Equations (7) and (8) recover the earlier limits 1/2 and 1.

## 2. Each branch has its own unique conditioned limit

Consider a branch with deterministic offspring numbers bᵢ∈{1,2}, and suppose
critical extinction holds from every generation. Write F_m for the states of
all its edges through generation m. This is a finite set of edges. Let
t=t_m(n)>0 be the probability that a fixed generation-m vertex reaches
generation n through descendants. Independence and spherical symmetry imply

    P(Zₙ>0 | F_m)=g_t(Z_m),    g_t(z)=1−(1−t)ᶻ.          (9)

The decreasing descendant-survival events and extinction give t_m(n)→0 for
fixed m. For each nonnegative integer z, g_t(z)/t→z. Since Z_m is bounded,

    q(n)/t=E[g_t(Z_m)/t]→E Z_m=M_m.

Consequently the F_m density of the conditional law converges to Z_m/M_m.
This holds in total variation, since F_m has finitely many atoms. The densities
are consistent in m, because

    E[Z_{m+1}/M_{m+1} | F_m]=Z_m/M_m.

They therefore define a probability law Q on the countable edge set, by the
extension theorem for consistent finite-dimensional distributions.

There is a useful explicit bound. Put K_m=E[Z_m(Z_m−1)/2]. The union bound
and its two-term inclusion–exclusion lower bound give

    0≤zt−g_t(z)≤z(z−1)t²/2.                             (10)

Define measures on F_m with densities α=g_t(Z_m)/t and β=Z_m relative to
ordinary critical percolation. Their masses are A=q(n)/t and M_m, and
0≤β−α has mass D=M_m−A≤K_m t. If D>0, normalizing β writes Q as
(A/M_m) times the normalized α measure plus (D/M_m) times the normalized
β−α measure. If D=0 the measures agree. In either case,

    || P( · | Zₙ>0)|F_m − Q|F_m ||_TV ≤ K_m t_m(n)/M_m. (11)

Our convention for total variation is sup_C|P(C)−Q(C)|, equivalently half
the sum of absolute atom-mass differences on a finite space.

The law Q also has a direct construction. Starting at the branch root,
choose a child uniformly at each successive generation to obtain a ray.
Force all its edges open and make all other edges independent Bernoulli(1/2).
Let V_m=∏ᵢ₌₁ᵐ bᵢ be the number of deterministic generation-m vertices.
Each root-to-generation-m path is selected with probability 1/V_m. For a fixed
edge configuration through generation m, the selected path is compatible with
it for exactly Z_m choices. For any compatible choice forcing m open edges
multiplies the ordinary configuration probability by 2ᵐ. The resulting density
is therefore 2ᵐZ_m/V_m=Z_m/M_m, as required.

This construction gives exactly one infinite ray in the root cluster.
Condition on the chosen ray. Every subtree hanging off it has ordinary
critical percolation and dies out almost surely, by extinction at its root.
There are countably many such subtrees. Any other infinite ray would leave
the chosen ray into one of them, which is impossible almost surely.
Moreover each hanging subtree has no infinite open cluster anywhere, by the
vertexwise extinction argument of Section 1. Thus there is exactly one
infinite open cluster in the branch under Q. Apply this construction separately
to A and B to obtain branch laws Q^A and Q^B.

## 3. The full conditional law is asymptotically a two-law mixture

Define Q_A by forcing e_A open, putting Q^A on branch A, and independently
putting ordinary Bernoulli(1/2) percolation on e_B and branch B. Define Q_B
symmetrically. In particular

    Q_A(e_A open)=1,    Q_B(e_A open)=1/2.                (12)

Let H_m contain both attachment edges and all edges through generation m
in both branches. The laws P( · | Uₙ)|H_m and P( · | Vₙ)|H_m converge in
total variation to Q_A|H_m and Q_B|H_m, respectively, by Section 2 and
independence of the unused branch. Denote their distances by η_A(m,n),
η_B(m,n); both tend to zero for fixed m.

On the whole edge space form the measure

    Rₙ=[uₙP( · | Uₙ)+vₙP( · | Vₙ)]/(uₙ+vₙ).

Inclusion–exclusion, as an identity of measures, gives

    Rₙ=(1−aₙ) μₙ + aₙ P( · | Uₙ∩Vₙ),
    aₙ=uₙvₙ/(uₙ+vₙ).

Hence ||Rₙ−μₙ||_TV≤aₙ≤min(uₙ,vₙ)→0. Since
uₙ/(uₙ+vₙ)=wₙ, restricting to H_m gives

    || μₙ|H_m − [wₙQ_A+(1−wₙ)Q_B]|H_m ||_TV
       ≤aₙ+wₙη_A(m,n)+(1−wₙ)η_B(m,n) →0.               (13)

Every finite edge set is contained in some H_m.

It follows that if w_{n_j}→λ, then μ_{n_j} converges on every cylinder event
to λQ_A+(1−λ)Q_B. Conversely, if μ_{n_j} converges on cylinder events, apply
(13) to {e_A open} and use (12):

    μₙ(e_A open)=(1+wₙ)/2+o(1).                         (14)

Thus w_{n_j} must converge. This proves that all cylinder subsequential limits
are precisely the mixtures whose parameters are subsequential limits of wₙ.
It also proves the following ratio criterion for these two branches: the full
sequence μₙ converges if and only if wₙ converges, equivalently if
q_A(n)/q_B(n) converges in the extended interval [0,∞].

## 4. Adjacent survival ratios tend to one

This step is needed: the endpoint oscillations alone would not show that
intermediate mixture parameters occur.

At p=1/2, backward survival across one level has maps

    f₁(t)=t/2,    f₂(t)=t−t²/4.

In reciprocal variables these become, for r≥1,

    R₁(r)=2r,    R₂(r)=r+r/(4r−1).

They are increasing. R₁ has Lipschitz constant 2, and

    R₂'(r)=1−1/(4r−1)² ∈[8/9,1].                       (15)

For fixed n let Cₙ=R_{b₁}∘…∘R_{bₙ}; its Lipschitz constant on [1,∞)
is at most 2^(D(n))=1/Mₙ. All intermediate arguments remain at least one.
Since 1/q(n)=Cₙ(1), while
1/q(n+1)=Cₙ(R_{bₙ₊₁}(1)) and R_{bₙ₊₁}(1)∈{2,4/3},

    0≤1/q(n+1)−1/q(n)≤1/Mₙ,
    1/(1+q(n)/Mₙ)≤q(n+1)/q(n)≤1.                       (16)

Here the terminal reciprocal displacement is at most one, which explains
the constant in (16).

We now prove q_s(n)/M_s(n)→0 uniformly through each successive stage of
our particular schedule. For k≥2 and Nₖ₋₁≤n≤Nₖ, monotonicity of survival,
the previous plateau bound (4), and the fact that at most 2k−1 further
levels can be suppressed imply

    q_s(n)/M_s(n)
      ≤ q_s(Nₖ₋₁)/M_s(n)
      ≤ 4 M_s(Nₖ₋₁)/[(Lₖ₋₁+4)M_s(n)]
      ≤ 4·2^(2k−1)/(Lₖ₋₁+4)
      ≤ 8·2^(2k−1)/Nₖ₋₁
      = 2^(−k²+4k−9) =: εₖ.                            (17)

This tends to zero as k→∞. Both branches obey the same bound.

One can also obtain the plateau estimate in (17) without its union bound.
Let tᵢ be survival from generation i to a fixed target generation n and let
rᵢ=1/tᵢ. A unary level has rᵢ₋₁=2rᵢ, whereas a binary level has
rᵢ₋₁=rᵢ+cᵢ, where cᵢ=1/[4(1−tᵢ/4)]∈[1/4,1/3]. Substitution gives

    1/q_s(n)=1/M_s(n)+Σᵢ₌₁ⁿ cᵢ/M_s(i−1),              (18)

with cᵢ=0 on unary levels. The Lₖ₋₁ terms in the previous binary plateau
contribute at least Lₖ₋₁/[4M_s(Nₖ₋₁)]. Therefore
q_s(n)/M_s(n)≤4·2^(2k−1)/Lₖ₋₁≤εₖ, independently proving the needed
bound. Notice that this plateau lies earlier than the target; the argument
does not assume a long binary suffix at every n.

## 5. Every mixture parameter occurs

For Nₖ₋₁≤n≤Nₖ and k≥2 put
r_A=q_A(n+1)/q_A(n), r_B=q_B(n+1)/q_B(n). Equations (16)–(17) give

    1/(1+εₖ)≤r_A,r_B≤1.

Writing w=wₙ,

    wₙ₊₁=wr_A/[wr_A+(1−w)r_B],
    wₙ₊₁−wₙ=w(1−w)(r_A−r_B)/[wr_A+(1−w)r_B].

The denominator is at least 1/(1+εₖ), and |r_A−r_B|≤εₖ/(1+εₖ). Thus

    |wₙ₊₁−wₙ|≤εₖ w(1−w)≤εₖ/4
             =2^(−k²+4k−11)→0.                         (19)

For each λ∈(0,1), (7) places w_{N_{2j−1}} below λ and w_{N_{2j}} above λ
for all large j. Choose n_j to be the first integer between these endpoints
with w_{n_j}≥λ. Its predecessor has weight below λ. Both indices tend to
infinity, so (19) shows 0≤w_{n_j}−λ≤|w_{n_j}−w_{n_j−1}|→0.
The endpoints λ=0,1 occur along the odd and even stage endpoints. Conversely
all wₙ belong to [0,1]. Their subsequential-limit set is therefore [0,1].
Together with (13)–(14) this proves (1), including its assertion about the
single-edge interval. The measures in (1) are distinct by (12).

Finally, the spine description and critical extinction of the unused branch
show that Q_A and Q_B each have precisely one infinite open cluster and one
infinite ray from o. That event has probability one under every mixture as
well. Even these properties shared by all subsequential limits do not select
a unique limiting law.

## Scope for T160

The earlier obstruction is now reduced to an explicit scalar ratio: both
branch conditioned laws converge, but their relative survival probabilities
do not. The set of possible full limits is an entire line segment. Critical
extinction, existence of branch limits, and uniqueness of the infinite ray
under every subsequential law are therefore insufficient to establish a
general convergence argument. This tree has no lattice transitivity and has
multiple infinite clusters with positive probability above criticality.
No corresponding ratio estimate on Z³, and no proof of T160, is obtained.
