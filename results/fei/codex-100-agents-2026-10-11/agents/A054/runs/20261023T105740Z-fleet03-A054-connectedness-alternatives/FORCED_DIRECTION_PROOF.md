# Forcing a qualifying direction inside the SAME labelled reset bank

This is a refinement of A054-RESET-COMPONENT-CROSSING-INTERFACE@1,
not a proof of universal query selection. All entropy is in bits. Inputs
are the uniform binary cube V=F2^n, n>=2. No output character is used.

## 1. The finite labelled metric and the exact constrained optimum

Let f=1-2*1_U, p=|U|/2^n>0. Partition U into labels L such that
no ordinary coordinate edge within U joins different labels. Actual
connected components qualify. Original component labels inherited by
an actual coordinate restriction also qualify, even when disconnected.
For each nonzero translation v define

    w(v)=P[f(X)!=f(X+v)],
    gamma(v)=P[X,X+v in U and L(X)!=L(X+v)],
    ell(v)=w(v)+2 gamma(v).

Both probabilities are directed, normalized by 2^n. Thus
ell(v)=2p-2 sum_l P[X,X+v in U_l], so 0<=ell(v)<=2p.
In the original coordinate basis gamma(e_i)=0 and
I0=I(f)=sum_i ell(e_i).

Write E_t={v!=0:ell(v)<=t},

    M=min_{basis B} sum_{v in B} ell(v),
    lambda(v)=min{t: v in span(E_t)},
    T={v!=0:ell(v)>=p},
    tau=min_{v in T}(ell(v)-lambda(v)).

If T is empty put tau=+infinity. All minima other than this convention
are finite and attained; 0<=lambda(v)<=ell(v). The following exact
identity is the additional selection result:

    min_{basis B: B intersects T} sum_{v in B} ell(v) = M+tau.       (1)

Proof, including ties: a minimum weight basis B has
span(B intersect E_t)=span(E_t) at every weight threshold t.
Otherwise exchange a heavier basis vector for a vector of E_t outside
that span, strictly reducing cost. In the unique expression of v in B,
the largest weight of a used vector is therefore lambda(v). Replace
one such vector by v. If v was already in B nothing changes. This
constructs a basis containing v of cost M+ell(v)-lambda(v).
Conversely, let B' contain v and remove v, leaving a hyperplane W.
Since v belongs to span(E_lambda(v)) but not W, some z in that threshold
set is outside W. Replacing v by z gives a basis of cost at most
cost(B')-ell(v)+lambda(v), hence cost(B')>=M+ell(v)-lambda(v).
Minimize over T to prove (1). This is ordinary vector-basis exchange;
no sums of dependent single-vector gains are used.

Consequently, for any already booked debit u>=0, a basis containing a
qualifying direction and with total labelled cost <=I0-u exists IFF

    tau <= I0-u-M.                                                (2)

This compares the forcing surcharge with the SAME remaining rank
release. It is stronger than choosing an arbitrary minimum basis and
then hoping that it has a qualifying direction. Also

    tau=0 iff rank span{v:ell(v)<p}<n.                             (3)

For the forward implication, full rank below p would give lambda(v)<p
for every v, whereas ell(v)>=p. For the reverse implication, every
minimum basis needs a vector of weight >=p, and any of its vectors has
lambda(v)=ell(v) by the threshold span property.

## 2. Interface payment, retaining old debit and actual terminals

Take a basis supplied by (2), put a qualifying vector v first, and
reset the INPUT chart using these columns. Write f' for the result,
rho=I0-I(f'), gamma_all=sum_{b in B}gamma(b), and
rho_L=I0-sum_{b in B}ell(b). Then exactly

    rho = rho_L+2 gamma_all,   rho_L>=u.                          (4)

For the first singleton i, the inherited-label fibre mass entropy
W_i=ell(v)/2>=p/2. This is because a two-point fibre with one supported
endpoint contributes its supported mass once, while a fibre with two
different supported labels contributes twice that mass. The ordinary
singleton influence is w(v), so W_i=w(v)/2+gamma(v).

Retain the earlier row bound from version1,
L_i(f')<=4p+a0*w(v), a0=2/ln2+4/(e ln2), C=4+a0<37/4.
Since p<=ell(v)=w(v)+2 gamma(v),

    L_i(f') <= C*w(v)+8 gamma(v)
             <= C*w(v)+4*(rho-u)
             <= C*(w(v)+rho-u).                                 (5)

The explicit component-crossing interface is 8 gamma(v). It is paid
from unused ordinary reset release rho-u because (4) gives
2 gamma(v)<=rho-u. Neither M nor tau creates a new reserve: (1) merely
selects a basis within the existing I0-u budget. Earlier u is retained.

For the two actual restriction children h_0,h_1 of f', the complete
signed identity, for every real K, is

    D_K(f)+(1/2)sum_b[K I(h_b)-H(h_b)]
       = L_i(f')-K*(w(v)+rho),  D_K=H-KI.                       (6)

This includes all children and uses entropy invariance of an input
linear map. At a least-essential-dimensional positive K-witness with
K>=C, u=0, each actual child is smaller and has nonnegative reserve.
Equations (2),(5),(6) give a contradiction. Thus such a witness must
satisfy M+tau>I0 for BOTH choices of sign support and every admissible
label partition. This is an explicitly paid critical class, not a
universal rank assertion.

## 3. Sharp boundaries and application after an ORIGINAL restriction

If f is already input-influence minimal, ordinary basis cost is at
least I0, and labelled cost dominates it. The identity basis attains
I0, hence M=I0. Condition (2) with u=0 then reduces exactly to the
rank deficiency in (3). A hypothetical critical witness must therefore
have all translations with ell(v)<p spanning V. This does not contradict
the prior singleton necessary bounds: it is a translated-rank condition.

For the activated bent family of version1, n=k+4, k>=2, q=2^-k,
f=1-A_k-A_k*(-1)^(ab+cd), actual negative components of sizes9 and1,
p=5q/8, I0=(2+5k/4)q. All data translations have w=q/2; at most two
directed crossing pairs join the singleton and the large component for
any fixed translation, so gamma<=q/8. The four physical data directions
have gamma=0 and ell=q/2<p. Every translation with a nonzero control
part has ell=w=5q/4>p, and none is spanned by the data directions.
Therefore rank(ell<p)=4<n, M=I0 and tau=0. The ORIGINAL control
singleton is paid already; the zero-release crossing shear remains a
valid warning against paying flux from ordinary release alone. This
family is not an obstruction to the corrected existential criterion.

After an actual ORIGINAL coordinate restriction, inherited original
component labels remain edge-homogeneous, so (1)--(5) apply verbatim
to each child. A reset already fully booked to pay that original query
has no unspent credit: its debit u must remain in (2). Query-partition-
preserving affine preprocessing supplies no additional credit; A052's
compensated invariant still applies. This proof uses input maps only,
and does not extend inherited support labels across output characters.

First unsupported universal line: show that some actual ORIGINAL
proper restriction of every genuine high-K critical source leaves a
child with tau <= I0-u-M and that its complete signed original-query
bill and all siblings fit the same unused bank. Neither threshold
rank deficiency nor a positive labelled release alone proves this.

## 4. Sharper exact frontier: pay ONLY the queried crossing interface

The all-labelled optimizer above funds all crossing directions. The
actual singleton theorem (5) only needs the queried gamma(v). Thus
define ordinary-cost thresholds F_t={z!=0:w(z)<=t} and

    M0=min_basis sum_b w(b),
    lambda0(v)=min{t:v in span(F_t)},
    tau0=min_{v:ell(v)>=p}[ell(v)-lambda0(v)].

Use +infinity for an empty qualifying set. Ordinary basis exchange,
proved in Section1 without any assumption on weights, gives

    min_{B basis, v in B, ell(v)>=p}
        [sum_{b in B}w(b)+2 gamma(v)] = M0+tau0.                 (7)

Indeed for a fixed v the ordinary constrained basis costs
M0+w(v)-lambda0(v); adding the ONE required interface cost2 gamma(v)
gives M0+ell(v)-lambda0(v). This is an exact minimum over actual
invertible input charts AND their selected query directions.

Therefore the original sufficient singleton hypotheses
W_i>=p/2 and 2 gamma_i<=rho-u can be achieved by some input reset and
some singleton query IFF

    M0+tau0 <= I0-u.                                             (8)

No all-direction flux payment is required. The selected ordinary reset
has rho>=u+2 gamma(v)>=0; equation(5) and the complete terminal identity
(6) apply without change. Other crossing edges are NOT treated as a
debit of this singleton. If another query later uses them, it must pay
its own interface from its then remaining budget.

The minimum in (7) is at most M+tau: each candidate's required single
crossing charge is at most its total labelled crossing charge. The
inequality can be strict, so Section1 is a convenient sufficient class,
while (8) is the exact frontier for this singleton payment mechanism.
This exactness does NOT assert that an actual entropy bill is unpaid
when (8) fails: the row bound and the W threshold are only sufficient
tools. It also says nothing about output-character resets.

Strict actual Boolean example with nonzero L: on three bits take
U={1,2} with the two singleton component labels (integers use low bit
first). Then p=1/4, I0=3/2, M=3/2 and tau=0. Every direction other
than3 has w=1/2, gamma=0, ell=1/2; direction3 has w=0, gamma=1/4,
ell=1/2. Thus M0=1, lambda0(v)=1/2 for v!=3, tau0=0. The sharp cost
is1, whereas the all-labelled cost is3/2. Choose columns(1,3,4) and
query the first coordinate. The reset support is {1,3}, a one-dimensional
subcube; Inew=1, rho=1/2, queried w=1/2 and gamma=0. The other basis
direction3 has gamma=1/4. With old debit u=1/2, no reset release is
left, but this query needs no crossing payment. Its actual children
are a constant and a literal, each Fourier entropy0; H(f)=2, so L=2.
Equation(5) pays this full bill since 2<=C/2. The all-labelled test
fails because M+tau=3/2>I0-u=1. This does not offer the booked1/2
again; it removes an unrelated crossing charge from this query.

At any genuine least-essential-dimensional positive K-witness with
K>=C, (8) with u=0 is impossible; hence M0+tau0>I0 for each admissible
label partition and either sign support. At an input-influence-minimal
root M0=I0. Then tau0>0: no qualifying direction can both have zero
crossing flux and lie in an ordinary minimum basis.

The shortest remaining universal line is now the sharper (8) AFTER an
actual ORIGINAL restriction, with the original query's complete signed
bill and ALL siblings retained and u reflecting every earlier booking.
This is a measurable independent-rank/forcing-cost condition; it is
not supplied by source preprocessing or by criticality alone.
