# A data query can fund a selected reset under an inherited reference

This is a finite, source-specific theorem. It gives no universal bound for
the initial entropy. Entropies and divergences are in bits. Independent
review is pending.

## 1. Every source and reference in the transaction

Let f:{-1,1}^n->{-1,1}, n>=1, be Boolean, i any physical coordinate,
P(S)=fhat(S)^2, and Q any NORMALIZED reference supporting P. No product
structure or source equality of Q is assumed. Write K=KL(P||Q), H=H(P),
and C=H+K, the full current cross entropy. K is finite and already booked.
An old debit omega>=0 remains spent throughout.

For T not containing i put a_T=fhat(T), b_T=fhat(T+i), p_T=a_T^2+b_T^2,
q_T=Q(T)+Q(T+i). The actual coherent outcome kernel is

    k_e(T)=(a_T+(-1)^e b_T)^2/(2p_T) if p_T>0,
    k_e(T)=1/2 if p_T=0,                         e=0,1.

The second clause applies to ALL source-zero rows. Q's source-zero mass
is retained. Booleanity and Parseval give actual outcome probabilities
1/2. Its actual reference predictions are t_e=sum_T q_T k_e(T)>0.
Let P_e(T)=2p_T k_e(T) be the actual physical-child spectrum and
Q_e(T)=q_T k_e(T)/t_e its inherited conditional reference. Q_e supports
P_e. Every reference and conditional law here is fully normalized.

Define

    E=K-KL(p||q)>=0,     O=KL((1/2,1/2)||t)>=0,
    D=H-(H(P_0)+H(P_1))/2>=0,
    R=D+E,              C_e=H(P_e)+K_e,
    K_e=KL(P_e||Q_e).

Erasure data processing gives E>=0. The common-kernel chain rule gives

    K=E+O+(K_0+K_1)/2,
    C=R+O+(C_0+C_1)/2.                            (1)

These identities follow by expanding the finite log sums. In the joint
laws p_T k_e(T),q_T k_e(T) the identical kernel cancels on positive source
atoms; disintegration then separates outcome KL and actual child KL.
Terms with zero source mass contribute zero but their reference mass is
not removed. There are no zero denominators on positive source atoms.
For completeness D>=0 follows from
H(P)=H(p)+H(S_i|S_-i) and H(p)>=mean H(P_e), since
(P_0+P_1)/2=p. No influence bound for D is used.

Let Pi_e be the child's actual coordinate marginal product. It supports
P_e, including deterministic endpoint marginals. Its KL is the child's
total correlation T_e. ACTUALLY installing Pi_e instead of Q_e has SIGNED
debit J_e=T_e-K_e. The sign is not clipped in the actual final reference
or terminal bill.

## 2. Declare the lottery and all permitted cuts

Append k>=0 physical dummy bits to f, extending Q by deterministic empty
Fourier marginals on them. Their actual outcomes are independent fair
bits, their coherent predictions are fair, and their erased/outcome KL
charges are zero. This FULL reference condition is needed; an arbitrary
reference on the new dummy Fourier coordinates would have an extra
erasure charge. Every dummy prefix leaves the original reference intact.

Let z in {0,1}^k be the fair dummy string and fix arbitrary decisions
a_e(z) in {0,1}. The two decisions may be coupled in any fashion through z.
At the end install Pi_e if a_e(z)=1, otherwise retain Q_e. No other query
or reset is allowed in this local rule. In particular no core data query
occurs AFTER its one declared installation.

Every adapted stopping cut is admitted: before/after any dummy or i query,
immediately before/after installation, and at the root. Early stopping
retains the CURRENT actual reference. Deterministic installation is a
separate step, so a cut can stop before a negative debit in one outcome
and after a positive debit in another. Source entropy H is never replaced
by zero merely because a cut stops.

Write

    b_e=[J_e]_+,
    L(z)=(a_0(z)b_0+a_1(z)b_1)/2,  lambda=E_z L(z).

L is the NONNEGATIVE pending all-cut bill, not the signed complete-terminal
KL increment. This distinction is essential when J_e<0.

For any cut tau, charge the actual O from (1) once if i has been queried
before that cut. It is a predictable charge at the queried node, not a
random realized log-likelihood and not an independently chosen tariff.

## 3. Exact minimum when information is revealed AFTER i

Query i, then reveal z, then perform the selected installation. Set
m_e(s)=E[a_e(z)b_e | dummy prefix s]. This is a nonnegative finite
harmonic function with terminal value a_e(z)b_e. A full potential is

    V_root=C+[lambda-R]_+,
    V_(e,s)=C_e+m_e(s) after query i and before installation,
    V_after_install=H(P_e)+K_e+a_e(z)J_e.

At every node V dominates actual current full CE. At a selected negative
debit the potential decreases to the actual lower CE; it does not refund
an already consumed old debit. At a positive debit installation preserves
V. Dummy transitions are harmonic. At i, (1) gives

    O+mean_e V_(e,empty) = C-R+lambda <=V_root.

By finite tree induction, for EVERY admitted cut

    E[H(P_tau)+KL(P_tau||Q_tau)]
      +E[O * 1_{i queried before tau}] <= C+[lambda-R]_+.       (2)

No optional-stopping limit or independence between reset decisions is used.
The exact minimum total initial capital is the right side of (2): root
stopping forces C; continuing through all dummy bits and in each actual
branch resetting only when a_e(z)J_e>0 (otherwise stopping before reset)
gives charged expectation C-R+lambda. This is a legal adapted cut. The
displayed potential attains their maximum.

In particular ONE original supplied account S funds this rule iff

    S-omega >= C+[lambda-R]_+.                         (3)

There is no new influence allocation at the physical children.

## 4. Exact minimum when information is revealed BEFORE i

Reveal the SAME z first, then query i, then perform its selected reset.
The complete final joint laws of physical outcomes and installed references
are the same as before. At each fully revealed z, root stopping costs C
and the best post-query cut costs C-R+L(z), so the necessary capital there
is C+[L(z)-R]_+. Earlier dummy prefixes have full potential

    V_s=C+E[(L(z)-R)_+ | s].

It dominates the current C and is harmonic along the dummy queries.
After i use C_e+a_e(z)b_e; after installation use actual full CE. The
query inequality is O+mean(C_e+a_e(z)b_e)=C-R+L(z), so the same finite
induction proves that the exact least original capital is

    A_before=C+E[(L-R)_+],
    A_after =C+(E L-R)_+.                              (4)

For the lower bound take the adapted cut that, after observing z, stops
before i when L(z)<=R and otherwise queries i and stops after selected
positive installations and before selected negative ones. All actual
outcome-KL charges are retained. Thus the ordering premium is exactly
E[(L-R)_+]-(E L-R)_+>=0: its first term is at least zero and at least
E L-R. Formula (4) concerns ALL cuts, not just the complete terminal.

At the COMPLETE terminal the two separate boundary terms in either order
are

    E H_terminal=mean_e H(P_e),
    E KL_terminal=mean_e(K_e+epsilon_e J_e),
    epsilon_e=E_z a_e(z),

and expected outcome charge is O. These use SIGNED J_e. Their sum can
be strictly smaller than the least all-cut capital. Both full entropies,
conditional KL, source-zero reference atoms and old consumption remain.

## 5. A useful selection criterion, and its exact limit

If lambda<=R, the after-order rule needs NO extra root capital beyond the
already paid C. For a common rare reset of both children, put
B=(b_0+b_1)/2. If B=0, every lottery has zero extra cost. If R>0 and
B>0, choose any finite k with 2^-k B<=R and reset only on z=0^k.
This can make the growing conditional pending bill arbitrarily rare,
while (2) controls every full terminal. If R=0<B, no positive-probability
reset lottery is free at the root: its exact extra is lambda>0. No division
by R or assertion of a dimension-independent k is made in that case.

The entropy release and KL erasure credit are both usable in R=D+E.
The actual query prediction loss O is NOT usable again: it is paid on the
left of (2). Replacing R by D+E+O while also charging O would spend that
same amount twice. Ignoring O changes the mathematical account.

A concrete ordinary relevant-coordinate example is
f(x,y)=(-1)^x point3(y), with Q=Ber(31/32) on the x Fourier indicator
tensor the ACTUAL point3 spectrum. Here Inf_x=1, D=O=0,
E=K=log2(32/31), both inherited child KLs are zero, and
J_0=J_1=T=2-(9/8)log2(3)>0. With a common reset probability1/8,
T/8<E<T. Thus after-order extra is0 while before-order extra is
(T-E)/8>1/50. The SAME original C=H(point3)+E, not a newly allocated
child account, pays every full cut in the after order. A separate actual
point2 source with reference weights(1,2,3,4)/10 has predictions(7/10,3/10)
and O=log2(25/21)/2>1/10, so that actual query charge cannot be assumed zero.
All displayed signs are certified by the rational interval audit.

These formulas extend the earlier special threshold2 to an ordinary data
query with an ARBITRARY inherited reference. For its old protected mask
and exact source reference D=2,E=O=K=0, so (4) reduces to the previous
stage verbatim. No change in that stage's numerical example is claimed.

## 6. New dependency consumed: A087's heterogeneous cut guard

For g=point4*point3 on disjoint coordinates, start with its exact spectrum,
use common residual size r=3, and immediately install the point3 product
before touching point4. Root full CE is H4+H3. The completed rule has
expected full CE (3/2)M3. The admissible intermediate actual bill is H4+M3.
Here

    H3=4-(9/8)log2(3),  M3=6-(9/4)log2(3),
    H4=6-(49/32)log2(7).

The gap above the root is M3-H3=2-(9/8)log2(3)>1/5.
The gap above completed expectation is
H4-M3/2=3-(49/32)log2(7)+(9/8)log2(3)>1/5.
Both strict signs are checked with proved rational log intervals by an
independent actual128-entry Boolean/reference calculation. Thus the bill
exceeds max(root,completed) by >1/5. This independently HOLDS without
repair. It does not refute A061's identical-block result, and does not
assert that heterogeneous sums always equal a maximum of endpoints.

## 7. The exact unpaid universal line

Equations (2)--(4) are a local conditional payment theorem on ANY Boolean
core and ANY supplied supporting reference. They do not bound the initial
C=H+KL by influence. Nor do they automatically renew a descendant reserve
or justify a second installation. A general selected policy must transport
its actual remaining potential and actual references through the next data
query. The first unsupported full-FEI line is an ORIGINAL O(I) source and
compatible nontrivial continuation on an arbitrary indecomposable core,
with the very O charges and full boundaries above paid from that SAME
unused account. Rarely buying an optional reset is not such a supplier.
