# Component-fiber payment without projection separation

All cubes are finite and uniform; all Fourier entropies below are in bits.
Let g=1_U, f=1-2g, p=E g>0. Let U_k be the actual connected components
of U in the physical cube, with inherited indicators g_k and masses p_k.
Let A be a nonempty proper physical block of r coordinates, X the queried
coordinates and Y the retained coordinates. Set

    m_y=E_X g(X,y), m_ky=E_X g_k(X,y),
    Q_A=E_Y m_y log2(1/m_y),
    Omega_A=E_Y m_y H((m_ky/m_y)_k),
    W_A=sum_k E_Y m_ky log2(1/m_ky)=Q_A+Omega_A.       (1)

Zero fibers contribute zero. These quantities are defined directly from
the actual truth table and component labels, independently of an entropy
deficit or desired inequality. Under the uniform law conditioned on U,
write L for the component label. The Shannon chain rule gives

    Q_A=p[r-H(X|Y,U)], Omega_A=p H(L|Y,U),
    W_A=p[r-H(X|Y,L,U)].                              (2)

Each occupied fiber is uniform on its occupied queried vertices; the
label is a deterministic function of (X,Y). This proves (1)--(2), including
overlapping projections and fiber labels absent from some retained values.

## 1. Label overlap supplies a physical edge credit

For any indicator h on an r-cube with mean m,

    E(h)=sum_s |s| hhat(s)^2 >= (m/2)log2(1/m).        (3)

Here is a proof with the normalization explicit. Induct on r. Split the
last bit into means m0,m1. The new coordinate contributes at least
|m0-m1|/4; the inductive retained contribution is at least
[m0 log2(1/m0)+m1 log2(1/m1)]/4. With t=m0/(m0+m1), their sum exceeds
(m/2)log2(1/m) by (m0+m1)[h2(t)+|2t-1|-1]/4, which is nonnegative
because h2(t)>=2min(t,1-t). The base r=0 and zero means are immediate.

Apply (3) to every labeled fiber. Actual components have no adjacent
vertices with different labels, so their coordinate boundary energies add
exactly: E_A(g)=sum_k E_A(g_k). Consequently

    E_A(g)>=W_A/2=(Q_A+Omega_A)/2.                    (4)

No separation of component projections is required. In particular label
entropy Omega_A is a credit here, not a substitute for the spectral
terminal cross term. If R_k is the projection of U_k on A and
mu_k=|R_k|/2^r, then m_ky<=mu_k and

    W_A>=sum_k p_k log2(1/mu_k).                     (5)

Thus the previous projection-information condition remains sufficient
even when every component projection overlaps. Connected support is also
admitted when its actual fiber entropy satisfies W_A>=rp/2.

An exact decisive example uses n=5, A={bits0,1}, and components
{0,4,12,13,15} and {3,19,27,26,24}. Both are paths, have size5 and
project onto three queried vertices, with overlapping projections. Here
p=5/16, Q_A=9/16-(3/16)log2 3, Omega_A=1/16, and
W_A=5/8-(3/16)log2 3. Thus Q_A<p, but W_A>p=rp/2:
the former follows from 3^3>2^4, and the latter from 3^3<2^5.
The old projection credit is only 5/8-(5/16)log2 3<p. The actual
signed terminal cross term is -3/4+(9/32)log2 3, so it is retained,
not set to zero. The actual sign drop is 5/2-(9/16)log2 3 and
I_A=3/4. These identities are checked by independent physical fibers,
edge counts, integer Walsh transforms and original-label child tables.

## 2. The terminal cross term is retained explicitly

Let F denote raw indicator Fourier entropy, Lambda_A(h)=F(h)-E_X F(h_X),
B_A(h) its partial-Fourier conditional entropy, and E_A(h) its queried
Fourier energy. Write kappa=2/ln2. The standard raw row identity and cube
logarithmic Sobolev give

    Lambda_A(g)=B_A(g)+Jraw_A(g),
    B_A(g)<=rp, Jraw_A(g)<=kappa E_A(g).             (6)

Indeed the row masses sum to p, their queried squared Fourier laws have
at most 2^r atoms, and the squared-row entropy tensorizes with
Ent(v^2)<=2 sum_i E(D_i v)^2 in natural units. Summing rows by Parseval
gives (6). The elementary two-point proof and tensorization are supplied
in the preceding A054 RAW_SIGN_TRANSFER.md section3; no FEI premise is
used here.

Put Delta(h_1,...,h_t)=F(sum_k h_k)-sum_k F(h_k). Keeping the ORIGINAL
component labels in every child, define

    Z_A=E_X Delta((g_k)_X : k),
    X_A=Lambda_A(g)-sum_k Lambda_A(g_k),
    Gamma_A=[rp+kappa E_A(g)-sum_k Lambda_A(g_k)]_+.

Then the exact controlled-excess ledger is

    Delta(g_1,...,g_t)=X_A+Z_A <= Gamma_A+Z_A.        (7)

Z_A is signed and can be nonzero even when (4) pays a block. It must not
be dropped, bounded by Omega_A without proof, or interpreted as a
collection of certified physical descendants. When component projections
are disjoint, each child has at most one nonzero label and Z_A=0.
Equation (7) is the explicit general interface replacement for false
unrestricted component entropy and maximum-component ratio inequalities.

## 3. Actual sign payment pays the combined terminal interface

The prior universal transfer, with actual child masses p_x=E_Y g(x,Y), is

    L_A(f)<=4Lambda_A(g)+c I_A(f), c=4/(e ln2),
    I_A(f)=4E_A(g).                                 (8)

Its exact scalar correction is T(p)-E_X T(p_x), divided by ln2, where
T(p)=-(1-2p)^2ln((1-2p)^2)+4p^2ln(p^2)-8ln2 p(1-p).
The proof uses T''=16ln(2p/|1-2p|), convexity of T+(8/e)p ln p,
and Ent(p_x)<=2E_A(g). We use the exact version proved last stage;
the child orientation remains inherited, including child means above1/2.

For fixed K define the ACTUAL terminal-inclusive paid interface

    P_A(K)=4[Delta(g_k)-Z_A+sum_k Lambda_A(g_k)]
             +[T(p)-E_X T(p_x)]/ln2-K I_A(f).

This is an exact, independently specified component/child ledger, not
the unsigned root excess. Substituting (7)'s identity proves

    P_A(K)=L_A(f)-K I_A(f)
           <=4rp+(kappa+c-K) I_A(f).               (9)

Thus overlapping component terminal cross terms cancel only against
their actual retained ledger; they are never declared intrinsically
affordable. If W_A>=rp/2, (4) implies I_A>=rp, and (9) gives

    L_A(f)<=C I_A(f), C=4+2/ln2+4/(e ln2)<37/4.     (10)

This covers overlapping projections, arbitrary rarity, arbitrary
component shapes and connected supports meeting the fiber condition.
The improvement is geometric admission, not a change of the constant.

For a least-essential-dimension K-violator D=H(f)-K I(f)>0, each proper
actual child has nonpositive deficit. With S_A=-E_X D_K(f_X)>=0,

    D+S_A=P_A(K)=L_A(f)-K I_A(f).                   (11)

K>=C and W_A>=rp/2 contradict (9)--(11). A physical-descendant
ratio-critical source in the same class instead has H/I<=C. The class
is not asserted to be closed under restriction. For a finite physical
restriction tree, (9) sums with reach weights, preserves all leaf
entropies and charges only erased influence; (10) applies nodewise only
where its fiber hypothesis holds. No root bank is charged again.

## 4. Necessary giant-component structure of every critical witness

Let a=kappa+c. For every proper block of a minimal K-violator, K>a,
(4), (9) and (11) force

    2(K-a)W_A+D+S_A <=4rp,
    H(X|Y,L,U)>=r[1-2/(K-a)]+(D+S_A)/(2p(K-a)).      (12)

Here a<21/4. Hence the exact weaker rational version at K=10 is
H(X|Y,L,U)>=11r/19+2(D+S_A)/(19p). All reserves are retained once.

Suppose n>=2 is the essential dimension and choose ANY block of n-1
coordinates. Conditional entropy is at most

    H(X,Y|L,U)=sum_k (p_k/p)log2|U_k|
             =log2|U|-H(L|U).

Together with (12), this yields the quantitative necessary condition

    sum_k (p_k/p)log2|U_k|
       >=(n-1)[1-2/(K-a)]+(D+S_A)/(2p(K-a)).        (13)

In particular at K>=C, EVERY component of size at most
2^((n-1)/2) would give W_A>=rp/2 and is excluded. Therefore every
minimal such violation has a component larger than 2^((n-1)/2).
The same statement applies independently to BOTH sign level sets,
since replacing f by -f preserves every entropy, influence and
physical deficit. The weighted geometric mean bound (13) is stronger
than merely demanding one giant component. n=1 is separately certified
by the constant/character cases H/I<=1.

This is critical-source exclusion, not FEI(C) for every function with
small components after arbitrarily discarding terminal deficits.

## 5. Exact remaining gap

The first unsupported universal line is a proper block with affordable
conditional within-component fiber entropy for a hypothetical witness
whose BOTH sign sets have giant components and fail (10). Actual child
reserves could still pay a signed row/refund interface, but (12) alone
does not select that block. Neither physical label entropy nor the
component size threshold establishes universal FEI. Full FEI is OPEN.
