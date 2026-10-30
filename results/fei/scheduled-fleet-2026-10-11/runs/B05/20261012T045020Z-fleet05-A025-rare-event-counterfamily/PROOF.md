# All-depth face bookkeeping for the specified nested tower

All inputs are independent uniform bits; signs have ordinary total influence I.
Q is twice the odd-2-face count divided by cube size. Badness is B_i>4 Inf_i.
The construction is a concrete interpretation of the B05 nested-tower request:
it places the negative event of the previous activated flip tower inside the next
bent core's point flip. It does not assert that every interpretation of a rare
tower, every overlap, or every Boolean core has the properties below.

Fix an even k>=2. At level j use fresh data x_j in {0,1}^k, selector y_j,
and r_j>=0 point controls z_j. Set b_j=(-1)^(x_1*x_2+...+x_(k-1)*x_k),
D_j=(1-b_j)/2 and M_j=1_{x_j=0} y_j. The disjoint events D_j,M_j satisfy
D_j M_j=0. With A_j=1_{z_j=0}, define

    E_0=1; E_j=A_j(D_j+M_j E_(j-1)); F_j=1-2E_j.

These are actual Boolean functions since E_j takes values in {0,1}. Depth one
is exactly the activated bent/one-point-flipped selector baseline. Each higher
level activates its point flip only when the preceding tower is negative.
The dimension is sum_j(k+r_j+1); for common r it is L(k+r+1).

Write delta=2^-k, beta=2^(-k/2), a_j=2^-r_j, p_j=P(E_j=1),
i_j=I(F_j), q_j=Q(F_j), with (p_0,i_0,q_0)=(1,0,0).
Let S_j be the unactivated core sign 1-2(D_j+M_j E_(j-1)). Then exactly

    c_j=P(S_j=-1)=(1-beta)/2+delta p_(j-1)/2,
    J_j=I(S_j)=k/2+delta[(k+1)p_(j-1)+i_(j-1)/2],
    R_j=Q(S_j)=k/4+delta/2[k(k-1)p_(j-1)
                               +(k+1)i_(j-1)+q_(j-1)],
    p_j=a_j c_j,
    i_j=a_j[J_j+2r_j c_j],
    q_j=a_j[R_j+r_j J_j+r_j(r_j-1)c_j].                 (1)

Derivation of J: every k-data edge at x=0 changes from uncut to cut when
y Eprev=1, adding delta pprev to each coordinate. The selector adds delta
pprev. The previous coordinates are visible only on x=0,y=1 and therefore
add delta iprev/2. The unedited bent function contributes k/2.

Derivation of R: the bent core contributes k/4. Among the binomial(k,2)
data-data faces through x=0, precisely k/2 are initially odd; a flip toggles
every such face. The net change is delta k(k-3) pprev/2. Data-selector faces
add k delta pprev. Selector-previous faces add delta iprev/2, data-previous
faces add k delta iprev/2, and previous-previous faces add delta qprev/2.
Their sum is R in (1). This counts each unordered coordinate pair once.

Activation in r fresh point controls scales internal data faces by a.
The mixed control/core faces contribute r a I(core). The control-control
faces contribute r(r-1)a P(core=-1). Likewise ordinary influence is
a[I(core)+2r P(core=-1)]. This proves every line of (1).

We now prove a dimension/depth/control-uniform bound using only these counts.
For every integer r>=0,

    2^-r<=1, r 2^-r<=1/2, r(r-1)2^-r<=3/4.            (2)

The last maximum is at r=3,4; the ratio of consecutive terms is
(r+1)/(2(r-1))<=1 for r>=3. The analogous monotonicity proves the middle
bound. For every even k>=2,

    delta<=1/4, k delta<=1/2, k^2 delta<=1.             (3)

Verify k=2,4; thereafter the ratios after increasing k by two decrease.

Inductively i_j<=k+2 and q_j<=k+4. For the influence step, using pprev<=1,
(1)-(3) give

    i_j <= k/2+delta(k+1)+delta(k+2)/2+(1+delta)/2
        = k/2+(3/2)k delta+(5/2)delta+1/2
        <= k/2+15/8 <= k+2.

For the face step, the three activated terms in (1) give

    q_j <= k/2+delta[k^2+(9/4)k+35/8]+3/8
        <= k/2+115/32 <= k+4.

The base i_0=q_0=0 satisfies the induction. These absolute moment bounds
remain true for arbitrary different r_j at different levels.
Consequently the unactivated outer core has

    R_L <= k/4+delta[k^2+(3/2)k+3] <= k/4+5/2.         (4)

Every fair split with one constant child is 4-good. Here is a separate direct
proof, independently reconstructing the constant-child subclaim of A022 v1.
For a constant +1 child and a sign h, let d=(1-Eh)/2. In the parent spectrum,
each nonempty residual label has equal coordinate-sector masses, while the
empty label has masses d^2,(1-d)^2. Thus

    B=2d(1-d)+Psi(d^2,(1-d)^2),
    Psi(s,t)=(s+t)log2(s+t)-s log2 s-t log2 t.

The binary entropy remainder bound implies Psi(s,t)<=s log2(e(s+t)/s).
Since d^2+(1-d)^2<=1, with c=log2(e),

    B/d <= 2+d(c-2)+2d log2(1/d) <= 2+c/sqrt(e)<3.

The maximum of the variable term occurs at d=1/(2sqrt(e)). The endpoint
d=0 is irrelevant and d=1 has B=0. To certify the last constant comparison
without decimals, ln2>2/3 by its positive atanh series, so c<3/2; e>5/2
by the first four terms of its series, so sqrt(e)>3/2. Global sign reversal
handles constant -1. This proves the subclaim and the required strict margin.

Choose any complete restriction tree that queries the OUTERMOST r_L controls
first, in any order, stopping inactive branches at their constant leaf. Each
of those splits has a constant +1 child and is therefore good. Exactly one
active branch of probability a_L survives with core S_L. Whatever complete
order is then chosen, its localized bad-face cost is at most its TOTAL face
cost R_L, by the exact odd-face telescope. Since i_L>=a_L k/2, (4) proves

    Q_bad,4(T)/I(F_L) <= R_L/(k/2) <= 1/2+5/k <= 3.    (5)

This includes both requested orders control-first and control-data-selector,
because both begin with all outermost controls. For k>=4 the bound is <=7/4.
No influence is reserved once for every depth: (5) spends a single post-
outer-control face budget, with its uniform bound justified by the recursion.
Every complete-tree leaf is constant, so its terminal entropy and influence
are zero. If a tree stops at S_L instead, the terminal entropy is H(S_L) and
cannot be discarded; that is a different, unpaid stopping ledger.

The nested-tower candidate therefore does not refute the existential B05
localized bridge at K=4. The proof covers all L>=1, all even fixed k>=2,
and arbitrary r_j>=0. It is not a proof for growing/nonuniform k_j, shared
variables, colliding activation events or arbitrary terminal cores.
The exact first unsupported universal line is the existence of a comparable
single-owned face reserve after exposing controls of overlapping events
without losing the lower bound that pays it, for every Boolean function.
