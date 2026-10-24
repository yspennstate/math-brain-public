# Uniform-cycle apex real-rootedness and a cyclic-backbone disjoint-pair theorem

3 October 2026.  Complete analytic derivation, subject to the accompanying
fresh independent audit.  This is a restricted extension beyond forest
backbones; it is not the general forest negative-correlation conjecture.

## Theorem

Let `H=C_n`, `n>=3`, and give every rim edge the same finite activity
`lambda>=0`.  Give every rim vertex the same positive profile (normalized to
one).  Add four new vertices whose spoke activities to every rim vertex are,
respectively, `a,b,c,d>=0`, and add exactly the two disjoint marked edges
joining the first pair and the second pair.  There are no other edges
incident to the four new vertices.

At every pair of positive marked-edge activities, the two marked indicators
are negatively correlated.  The inequality is strict exactly when
`a b c d>0`.  Positive fields on the two marked edges are allowed.  Unequal
rim activities, unequal vertex profiles, individual spoke fields, and
general conditioning are outside the claim.

The inequality also survives any positive-probability rim-edge cylinder
conditioning that forces at least one rim edge absent.  After deleting that
edge and contracting forced-present edges, the backbone is a forest, so the
earlier arbitrary-profile forest theorem applies.  Its strictness criterion
uses the number of resulting components having positive contracted profile.

The new input is the following exact real-rootedness statement.  If `D_n(s)`
is the unrooted-forest partition function after adding one apex with spoke
activity `s` to every vertex of `C_n`, then `D_n` has degree `n` and all its
zeros are negative real numbers.  For positive rim activity the zeros are
distinct.

## 1. Coefficients by cyclic gaps

Put

    p=lambda/(1+lambda),             0<=p<1,
    Z_H=(1+lambda)^n-lambda^n=(1+lambda)^n(1-p^n).

Fix a set `S` of `k>=1` apex spokes.  List its selected rim vertices in
cyclic order, and let `ell_1,...,ell_k>=1` be the numbers of rim edges in
the successive cyclic gaps; their sum is `n`.  The augmented edge set is a
forest exactly when every one of these gaps contains a missing rim edge.
The gaps are edge-disjoint, so the rim-edge partition sum compatible with S
is

    (1+lambda)^n product_i (1-p^(ell_i)).                 (1)

This includes `k=1`: the sole gap is the whole cycle, and (1) is `Z_H`.

Define

    F(z)=sum_(ell>=1)(1-p^ell)z^ell
        =(1-p)z/[(1-z)(1-pz)].                            (2)

An ordered positive composition together with a chosen initial rim vertex
specifies a cyclically ordered marked set, but each k-set is obtained once
for each of its k possible initial marked vertices.  Hence, writing
`P_n(s)=D_n(s)/Z_H`,

    [s^k]P_n(s)
      = n/k * (1-p)^k/(1-p^n)
          * [z^(n-k)](1-z)^(-k)(1-pz)^(-k),              (3)

for every `1<=k<=n`; the constant coefficient is one.  Formula (3) in
particular gives `[s]P_n=n`, as it must because a single spoke never creates
a cycle.

## 2. A Chebyshev closed form

Summing (3) before extracting the coefficient gives

    P_n(s)-1
      = n/(1-p^n) [z^n] {-log(1-sF(z))}.                 (4)

Set

    A=1+p+(1-p)s,

and let `r_+,r_-` be the two roots of `r^2-Ar+p=0`.  Since

    1-sF(z)=[1-Az+pz^2]/[(1-z)(1-pz)],

coefficient extraction from the three logarithms in (4) yields the
polynomial identity

    P_n(s)=[r_+^n+r_-^n-2p^n]/(1-p^n).                  (5)

No choice of square-root branch is involved: the numerator is the Lucas
polynomial determined by `L_0=2,L_1=A,L_n=A L_(n-1)-pL_(n-2)`.

For `0<p<1`, put

    x=A/(2 sqrt(p)).

Then `r_+^n+r_-^n=2p^(n/2)T_n(x)`, and the zeros of `P_n` are exactly the
solutions

    T_n(x)=p^(n/2).                                     (6)

Because `0<p^(n/2)<1`, (6) has n distinct real solutions, all strictly
between -1 and 1.  Their corresponding s-values satisfy

    s=[2 sqrt(p)x-(1+p)]/(1-p)
      < [2 sqrt(p)-(1+p)]/(1-p)<0.                      (7)

Thus every zero is negative.  When `p=0`, the rim has zero activity and
`P_n(s)=(1+s)^n`, proving the remaining boundary directly.

Consequently there are positive numbers `x_1,...,x_n` such that

    D_n(s)=Z_H product_i(1+s x_i),   sum_i x_i=n.        (8)

## 3. Transfer to the two marked edges

Sections 2 and 3 of
`forest_disjoint_rank_one_attachment_forest_backbone_proof.md` are purely
algebraic for an arbitrary weighted backbone.  They express the marked
Rayleigh difference, with `sigma=a+b+c+d`, as

    (EF-AC)/(D^2 abcd)
      =2(U T-Omega)
       +(a+b)(c+d)(Gamma^2+U^2T-2U Omega).               (9)

The only forest-specific input in that earlier proof occurs after (9),
where a negative-real-root factorization of D is required.  Factorization
(8) supplies exactly the same input for the present cyclic backbone.
Writing

    alpha_i=x_i^2/(1+sigma x_i),
    tau_i=x_i^2/(1+sigma x_i)^2,
    gamma_i=x_i^3/(1+sigma x_i)^2,
    eta_i=alpha_i tau_i,

the two brackets in (9) are the already verified identities

    U T-Omega=sum_(i!=j) alpha_i tau_j,                  (10)

and

    Gamma^2+U^2T-2U Omega
      =sum_(i!=j)alpha_i^2 tau_j
       +2sum_(i<j)gamma_i gamma_j
       +2sum_(i<j, h notin {i,j})alpha_i alpha_j tau_h. (11)

They are nonnegative.  Since `n>=3`, (10) is strictly positive.  Therefore
`EF-AC>0` exactly when all four row factors are positive; if one vanishes,
the corresponding marked edge is a bridge and the difference is zero.
The covariance equals the negative of the positive marked-activity factor
times `(EF-AC)`, divided by the squared total partition function.  This
proves the theorem.

## Scope

The unconditional result allows a genuinely cyclic backbone, but only a
uniform cycle and uniform profile.  Conditioning without any forced-absent
rim edge can destroy that uniformity after contraction and is not claimed.
The theorem neither proves real-rootedness for arbitrary cyclic backbones
nor covers arbitrary marked positions or whole-vector negative association.
The general forest/arboreal-gas conjecture remains open.
