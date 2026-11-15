# FEIB10 proofs

All information logarithms are base 2. The axiom has a nonnegative integer k. Ranges with zero mass have zero left side.

## 1. The Boolean axiom — PROVED

Let f take values in {-1,1}, mu(U)=fhat(U)^2, and g=D_R f. Write r=|R|. Then
`ghat(V)=fhat(R union V)` for V disjoint from R, and `||g||_2^2=up(R)`.
For r>=1 every nonzero value of g is an integer multiple of delta=2^(1-r), and |g|<=1. Thus
`delta^2 p(R) <= up(R) <= p(R)`.
The direction needed to eliminate p is **p(R)<=4^(r-1) up(R)**; the reverse inequality p>=up by itself does not do that.

Bonami hypercontractivity at rho=1/sqrt(3) gives

    sum_{|V|<=k} ghat(V)^2 <= 3^k ||T_rho g||_2^2 <= 3^k ||g||_(4/3)^2.

Hölder on the support gives `||g||_(4/3)^2 <= up(R) sqrt(p(R))`.
Consequently, for every nonempty R,

    mu{U >= R, |U-R|<=k} <= 3^k up(R) sqrt(p(R))
                              <= 3^k 2^(r-1) up(R)^(3/2).                 (Csharp)

For R=empty, up(R)=1 and the asserted C(3,2,1/2) bound is immediate. Thus the uniform axiom has a=3, b=2, c=1/2. The sharper nonempty prefactor is 2^(r-1), rather than 2^r or 4^r.
The norm/support/granularity factor is exact: a derivative equal to delta times an indicator has equality in both norm comparisons. For example the full r-fold derivative of an AND on r bits is constant of magnitude delta. At k=0 this example requires a uniform b to obey `b^r>=2^(r-1)`. Letting r increase proves that b=2 is optimal among constants that work uniformly over all dimensions with c=1/2. This does not assert optimality of the complete hypercontractive inequality for every k.

Numerical scope: see boolean_output.json and check_boolean.py.

## 2. A three-layer counterexample — PROVED

Let s be a multiple of 6 with s>=36. Define the integers and probabilities

    n=2^s,    d=2^(2s/3),    q=2^(-s),    h=4^(1-d),    w=1-q-h.

On subsets of [n], put total mass w uniformly on the s-subsets, total mass q uniformly on the d-subsets, and mass h on [n]. All other sets have mass zero. These are explicit rational probabilities. In particular,

    mu(S)=w/binom(n,s)  if |S|=s;
    mu(S)=q/binom(n,d)  if |S|=d;
    mu([n])=h.

Write T_l(r)=(l)_r/(n)_r (zero for r>l). For any R of size r,

    up(R)=w T_s(r)+q T_d(r)+h.

We prove even Csharp for every nonempty R. Its right-side coefficient at distance k is F=3^k 2^(r-1).

First suppose r<=s and s-r<=k<d-r. The left side is w T_s(r), independent of k. Since d>=2s,

    T_s(r) <= (s/n)^r,             T_d(r) >= (d/(2n))^r.

At the smallest k=s-r the ratio of the lower bound on the right side to the upper bound on the left side is

    3^s 2^(-3s/2-1) [2^(s/2)/(3 sqrt(2) s)]^r.             (1)

The prefactor is >=1 for s>=36: 3^s 2^(-3s/2-1)=(3/sqrt(8))^s/2.
The bracket is >=1 for s>=36, and increases as s increases by 6. Both assertions can be checked without square roots: `9^s>=2^(3s+2)` and `2^s>=18 s^2`; at the step s->s+6 their left/right ratios increase by factors (9/8)^6 and 64(s/(s+6))^2, respectively. Hence (1)>=1. If k<s-r, the left side is zero.

For s<r<=d the left side is zero until k=d-r. Next suppose r<=d and k>=d-r. Then

    F >= 3^(d-r) 2^(r-1) >= 2^(d-1)=1/sqrt(h).

Since up(R)>=h, one has `F up(R)^(3/2)>=up(R)`, which bounds any left side.
Finally, if r>d, the left side is zero until k>=n-r; at that point the same argument uses F>=2^(n-1)>=1/sqrt(h).
R=empty is trivial. This proves Csharp, hence C(3,2,1/2), in every dimension in the family.

Containment diverges. For any s-subset S,

    up(S)=w/binom(n,s)+q T_d(s)+h <= 3 q (d/n)^s.           (2)

Indeed `T_d(s)<=(d/n)^s`. For the first term, `1/binom(n,s)<=(s/n)^s<=q(d/n)^s` follows from `s^s<=n^(2s/3-1)`; for the last term, `h<=q(d/n)^s` follows from `2(d-1)>=s+s^2/3`. Both hold at s=36 and continue to hold as s increases by 6. For the first comparison, divide logarithms by s: the right side `2s/3-1` rises by 4, while `log2(s)` rises by less than 1. For the second, d multiplies by 16, while s+s^2/3 multiplies by less than 2 for s>=36.
Therefore

    A >= w [s^2/3+s-log2(3)],
    I = w s+q d+h n <= s+2^(-s/3)+2^(s+2-2d),

and A/I diverges at least linearly in s. In fact A/I=s/3+1+o(1), because T_d(s)=(d/n)^s(1+o(1)), the other terms in up(S) are negligible, and the d-layer's contribution to A is at most q log2(1/h)=2q(d-1)=o(1). This disproves containment from C alone, even from Csharp.

## 3. Additional Boolean properties — PROVED

### 3a. Granularity of the mean does not repair the axiom

For a Boolean spectrum, |E g_R|<=E|g_R|<=up(R)/delta, hence the necessary measure inequality

    mu(R) <= 4^(r-1) up(R)^2,       r>=1.                 (D)

The counterexample also satisfies D. It is automatic at zero atoms. At r=s, use
`mu(R)<=(s/n)^s` and `up(R)>=q(d/(2n))^s` to reduce it to
`4 s^s<=n^(s/3-2)`, valid for s>=36. To check propagation, divide logarithms by s: `2/s+log2(s)<=s/3-2`; the right side increases by 2 per step, and the left side increases by less than 1. At r=d, `mu(R)<=q(d/n)^d<=h`, while `4^(d-1)h^2=h`. At r=n it reduces to h>=4^(1-n), which holds because d<n.

### 3b. The p analogue does not repair it either

A genuine derivative supplies p_R satisfying

    up_R <= p_R <= min(1,4^(r-1)up_R),
    mu(R) <= up_R p_R,
    mu{U>=R,|U-R|<=k} <= 3^k up_R sqrt(p_R).              (P)

The measure-level version is the existence of numbers p_R satisfying these inequalities (p_empty=1). Our counterexample has such numbers: set p_R=min(1,4^(r-1)up_R). If p_R<1, the last inequality is Csharp; if p_R=1, it is the trivial left-side<=up_R bound. The middle inequality is D when p_R<1 and mu<=up otherwise. Thus this natural existential analogue of p does not distinguish the counterexample. Actual support probabilities of derivatives carry more structure than these scalar inequalities.

### 3c. Restriction thinning with unchanged constants is not a necessary property

Let mu be the spectrum of the dictator f=x_1, namely delta_{ {1} }. Under rho-thinning its law is
`tau_rho(empty)=1-rho`, `tau_rho({1})=rho`.
C(3,2,1/2) at R={1}, k=0 requires rho<=2 rho^(3/2), or rho>=1/4. It fails whenever 0<rho<1/4. Each individual restriction is Boolean and satisfies C; averaging spectral measures does not preserve this nonlinear inequality. Therefore the proposed thinning closure cannot be imposed as a Boolean necessity. With Csharp the same example fails for every rho<1.

### 3d. Parseval for squares gives a genuine obstruction

For any signs epsilon_U with fhat(U)=epsilon_U sqrt(mu(U)), define, for W disjoint from R,

    c_R(W)=sum_{V subset [n]\R} epsilon_(R union V) epsilon_(R union (V triangle W))
                                  sqrt(mu(R union V) mu(R union (V triangle W))).

These are the Fourier coefficients of (D_R f)^2. The pointwise bound |D_R f|<=1 implies

    sum_W c_R(W)^2 <= up(R),             c_R(empty)=up(R).                (SQ)

For R=empty, up=1, so SQ forces c_empty(W)=0 for every nonempty W. This is also f^2=1.

Our counterexample violates SQ for every choice of signs. Fix an s-subset S and W=[n]\S. Since n-s>2d, no two support sets of sizes at most d can have symmetric difference W. The full set and a d-set have symmetric difference of size n-d, not n-s. Thus the only ordered pairs contributing to c_empty(W) are (S,[n]) and ([n],S). Their sum has magnitude exactly 2 sqrt(mu(S)h)>0. Hence SQ is impossible, independently of signs.

A general measure-only necessary consequence is a polygon inequality: for every W!=empty, on the unordered pairs {U,U triangle W},

    max sqrt(mu(U)mu(U triangle W)) <= sum of all the other pair magnitudes.       (POLY)

The counterexample has a single positive pair for this W, so it violates POLY. POLY alone is not claimed sufficient for a Boolean realization or for containment.

### 3e. Level-1 for every derivative

The root level-1 theorem follows already from C; it therefore cannot exclude this counterexample. A normalized conditional derivative is not a Boolean function: its mass is one only after division by up(R), and its sup norm can then be 1/sqrt(up(R)). Applying the Boolean theorem unchanged to these normalized laws is not a valid necessity.

Here is a valid derivative version, stated entirely on mu. Set r=|R| and

    I_R=sum_{U>=R} (|U|-r)mu(U)=sum_{i outside R} up(R+i),
    M_R=up(R)-mu(R),
    L_R=sum_{U strictly contains R} mu(U) log2(1/min_{i in U\R} up(R+i)).

Then C alone implies

    L_R <= [4 log2(3)+4/(3e ln(2))] I_R + 8(r+1) M_R.       (L1D)

Proof: use natural logarithms temporarily and put t_i=ln(1/up(R+i)). For U strictly containing R write l=|U|-r and t=max_{i in U\R} t_i. If `t<=8(r+1)ln(2)+4ln(3)l`, charge the stated expression to U. On the remaining sets choose an i attaining the maximum. Then

    l < [t_i-8(r+1)ln(2)]/[4ln(3)].

Apply C at R+i with k=l_max-1, where l_max is the largest integer satisfying that inequality. The mass of such sets containing R+i is at most

    3^(l_max-1) 2^(r+1) up(R+i)^(3/2)
    <= (1/3) 2^(-(r+1)) up(R+i)^(5/4).

If no positive l_max exists, that mass is zero. Union bounding the chosen i, the additional cost is at most
`(1/3) sum_i up(R+i) t_i exp(-t_i/4) <= 4/(3e) I_R` since `t exp(-t/4)<=4/e`. Divide by ln(2). This proves L1D. The extra charge 8(r+1)M_R follows because every strict superset is nonempty outside R. All logarithms with positive weight have positive arguments.

At R=empty, M_R<=I_R, so this also proves a universal root level-1 bound. It is deliberately loose; optimal constants are unnecessary here. L1D holds for the counterexample because it follows from C. check_boolean.py checks L1D for every R on its exhaustive/sample bank; check_properties.py checks every R of the finite searched measures.

## 4. Cancellation branch

The numbered request makes the additional-axiom search conditional on containment following from C. Containment does not follow, so that branch is not triggered.

The same measure also shows directly that C cannot bound B. At an s-set, `up(S)>=q(d/(2n))^s` and `mu(S)<=(s/n)^s`, so

    log2(up(S)/mu(S)) >= 2s^2/3-2s-s log2(s).

All other contributions to B are nonnegative. Thus

    B/I >= w [2s^2/3-2s-s log2(s)]/[s+2^(-s/3)+2^(s+2-2d)] -> infinity.

This is PROVED. No claim is made that a separate cancellation axiom holds for all Boolean spectra.
