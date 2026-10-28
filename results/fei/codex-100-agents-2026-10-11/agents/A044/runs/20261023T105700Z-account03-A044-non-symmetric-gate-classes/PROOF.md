# Arbitrary activation: carry is owned by the seed, not the fresh selector

All entropy and cross entropy are in natural units. This is an analytic
author proof, with exact finite validation, pending independent review.
It extends A042's dyadic activation identity and exhibits an actual Boolean
obstruction to funding arbitrary activation carry solely from the outer
gate's deficit. It does not refute FEI.

Let g be a Boolean sign on any finite independent interior product cube.
Write a=(1-Eg)/2, V=4a(1-a), Delta_g=I(g)-V. For each occupied nonempty
Fourier label T put P_T=v_T c_T^2, where v_T is the product of
4p_i(1-p_i). Boolean physical mixed differences give |c_T|<=1. Let
j(t) be the unique nonnegative integer with 1/2<2^j(t)t<=1 for 0<t<=1.
Set J_g=ln4 sum P_T j(|c_T|), W_T=v_T 4^-j(|c_T|), Z_g=sum W_T,
L_g=E_g-J_g. Zero terms are omitted. All deterministic coordinates are
contracted before using these definitions.

Independently let X have success probability e in (0,1), and define
F=1 if X=0 and F=g if X=1. Suppose first 0<a<1. The true two-input
activation gate is evaluated at the actual independent law of X and g;
there is no artificial reseeding. Put b=j(e), d=j(a), and

    k_T=j(e |c_T|)-b-j(|c_T|) in {0,1},
    C=e^2 sum_T P_T k_T.

Indeed the two factors' dyadic mantissas lie in (1/2,1], so their product
lies in (1/4,1], requiring either zero or one additional dyadic shift.
The exact-boundary convention is included in this statement.

## Physical identities and an arity-uniform outer-gate bound

Direct expansion F=1-X+Xg gives

    c_F(T)=e c_T, c_F(XT)=c_T/2, c_F(X)=-a,
    P_F(T)=e^2 P_T, P_F(XT)=e(1-e)P_T,
    P_F(X)=4e(1-e)a^2,
    w_F=4ae(1-ae),
    Delta_F=e Delta_g+Delta_o, Delta_o=e(1-e)V.

The term Delta_o is precisely the original outer gate deficit. The
inherited seed allocation is e Delta_g, not a second independent bank.
The exact dyadic scale identity is

    J_F=e J_g+J_o+(ln4) C,                              (1)
    J_o=(ln4)[e^2 V b+4e(1-e)a^2 d+e(1-e)V].

For every t in (0,1), j(t)t<=1-t. For j=0 this is immediate;
for j>=1 use t<=2^-j and j<=2^j-1. Hence

    J_o/Delta_o=(ln4)[1+e b/(1-e)+a d/(1-a)]<=3ln4.      (2)

This arity-uniform binary gate bound holds at EVERY interior induced
product law. Equality holds at e=a=1/2. It extends the gate-scale
part of A042 beyond dyadic selectors, but not its zero-carry conclusion.
The carry obeys the exact source envelope

    0<=C<=e^2 V,     C/Delta_o<=e/(1-e).                 (3)

The upper envelope in (3) is not asserted sharp at each e. If e is an
inverse power of two, k_T=0 for every T and (1) specializes exactly to
A042. Otherwise the seed mantissas matter.

## Actual Boolean obstruction: fresh selector deficit cannot pay carry

Take g(y,z)=-1+2yz, with independent success probabilities
q=(1+t)/2 on y,z. Let 0<t<=1/8 and e=1-2t. Its normalized physical
coefficients are c_y=c_z=q and c_yz=1/2, with

    v=4q(1-q)=1-t^2,
    P_y=P_z=v q^2, P_yz=v^2/4,
    V=4q^2(1-q^2), Delta_g=v^2/4.

Here j(e)=j(q)=0 and j(1/2)=1. Moreover
1/4<e q=(1-t-2t^2)/2<1/2, so k_y=k_z=1, whereas k_yz=0.
Therefore the actual, not surrogate, carry is

    C=2e^2 v q^2,
    C/Delta_o= e(1+t)/[t(3+t)].                          (4)

For t=2^-m and m>=3,

    C/Delta_o >= 6/(25t) = (6/25)2^m -> infinity.         (5)

The lower bound uses e>=3/4 and 3+t<=25/8. It proves that no finite
K can satisfy C<=K Delta_o for all actual Boolean activations, even for
these three-variable nested canalyzing functions under product laws.
They are activated AND2 gates, not three-input AND gates. Multiplying by
ln4 gives the same obstruction for the entropy-unit carry debit.
There is no dimension extrapolation and no floating-point premise.

This is compatible with (2): the outer gate's own J_o is uniformly paid,
but the NEW carry depends on the inherited seed coefficients. It also
does not contradict A042: its selector is dyadic, while e approaches one
here. As t tends to zero, F approaches the original AND2 after contracting
X, but the INHERITED seed's two singleton indices jump from 0 to 1 at
q=1/2; the composition carry drops from 1 to 0 there. Scale and mantissa
compensate the seed's dyadic discontinuity; entropy is continuous. A
continuity argument for the inherited J_g alone at this boundary is false.

More precisely, along this same sequence,

    C -> 1/2, L_g -> (ln4)/2, L_o -> 0, L_F -> 0.

For L_g, the two singleton masses tend to 1/4 with mantissas tending to
1/2 from above, while the pair mantissa is exactly one. For L_F, every
nonvanishing atom has mantissa tending to one and all other masses
vanish; the finitely many mantissa logarithms are bounded by ln4. Thus
the carry debit (ln4)C asymptotically consumes ALL of the seed's actual
mantissa remainder, even though the fresh outer deficit tends to zero.
This is the exact ownership content of the later identity (7).

## One complete inherited reference and both terminal laws

Use the seed's full flat reference
Q_g(empty)=1-V and Q_g(T)=V W_T/Z_g. Its ordinary KL is K_g;
n_g=V ln(Z_g/V), and E_g=J_g+n_g-K_g. The seed law is never
replaced by a Boolean conditioning of this auxiliary reference.

For the outer activation gate, the complete reference has its physical
empty mass. Its nonempty labels are X, Y, XY. Their dyadic weights are

    W_o(X)=4e(1-e)4^-d,
    W_o(Y)=V 4^-b,
    W_o(XY)=e(1-e)V.

Let Z_o be their sum, n_o=w_F ln(Z_o/w_F), and K_o the ordinary KL.
Compose Q_o with Q_g by replacing each occupied Y label by the complete
conditional nonempty seed law Q_g(T)/V. Explicitly,

    Q_tree(empty)=P_F(empty), Q_tree(X)=Q_o(X),
    Q_tree(T)=Q_o(Y) Q_g(T)/V,
    Q_tree(XT)=Q_o(XY) Q_g(T)/V.

This is normalized on ALL final labels, is positive on every occupied
physical atom, and retains the full empty and nonempty terminals. The
exact ordinary chain rule, from the displayed likelihood ratios, gives

    K_tree=K_o+e K_g,
    CE_tree^+=J_o+e J_g+n_o+e n_g
             =J_F-(ln4)C+n_o+e n_g,
    E_F=CE_tree^+-K_tree.                               (6)

The subtraction of (ln4)C in the second expression is required. An
arbitrary-selector extension using J_F+n_o+e n_g as the SAME tree
cross entropy would overcharge by exactly that amount. The seed and
root KL terms are not subtracted a second time in another reference.
Equivalently the exact mantissa identity is

    L_F=L_o+e L_g-(ln4)C.                               (7)

For an explicit comparison with the complete flat root reference, set

    Z_F=4e(1-e)4^-d+e(1-e)Z_g
          +4^-b sum_T W_T 4^-k_T.

The three terms are precisely its X, XT and T sectors. Let
n_F=w_F ln(Z_F/w_F) and K_F=KL(P_F||Q_flat,F). Both references
preserve the same empty atom, and full ordinary cross entropies are
obtained by adding the identical physical-bias correction and empty
entropy to CE^+. Subtracting their exact entropy identities gives

    K_F-K_tree = CE_flat^+-CE_tree^+
               = (ln4)C+n_F-n_o-e n_g.                 (8)

This is signed, not a new nonnegative reserve. In the counterfamily,
Z_g->9/4, V->3/4, n_g->(3/4)ln3 and
K_g->(3/4)ln3-(1/2)ln4>0 (the strict sign is 3^3>4^2).
Meanwhile n_o,n_F,K_F tend to zero, so (8) tends to -K_g<0.
The normalizer transfer therefore has an actual negative limiting sign;
relabeling it as fresh positive capacity would change the reference bill.
At dyadic e, C=0 and
the formula for Z_F and (8) reduce to A042's signed conversion. Equations
(6)-(8) retain all inherited normalizers, ordinary KL, and both complete
terminal laws. A043's singleton-preserving refinement may be substituted
only with its corresponding exact signed KL transfer, not as fresh credit.

## Composition corollary with controlled depth and fan-in

For a finite chain of independent activations F_l=activate(e_l,F_(l-1))
of an arbitrary seed F_0=g, put rho_l=product_{h=l+1}^d e_h and
rho_0=product_{h=1}^d e_h. Expanding (1) and the true deficit identity,

    Delta(F_d)=rho_0 Delta_g+sum_l rho_l Delta_o,l,
    J(F_d)=rho_0 J_g+sum_l rho_l J_o,l
                         +(ln4)sum_l rho_l C_l.         (9)

The complete Q_tree and ordinary KL compose with exactly the same
weights; no terminal entropy or fan-in factor is omitted. If all
selectors are dyadic, C_l=0, yielding A042's depth-independent
J(F_d)<=max(K,3ln4)Delta(F_d) whenever J_g<=K Delta_g.
For arbitrary selectors, the previous A044 mantissa-bank theorem gives

    (ln4)sum_l rho_l C_l+L(F_d)
       =rho_0 L_g+sum_l rho_l L_o,l
       <=(11/2)Delta(F_d).

Consequently, if J_g<=K Delta_g,

    J(F_d)<= [max(K,3ln4)+11/2] Delta(F_d),              (10)
    E(F_d)<= [max(K,3ln4)+11/2] Delta(F_d).

For the entropy inequality use the displayed bank WITH L(F_d), not a
second application of the bank. The constants do not depend on depth,
seed arity, or the independent biases. Constants seeds are contracted;
g=1 gives a constant and g=-1 gives a signed literal at the first
activation. Zero-deficit contracted literal leaves have J=L=0.
The same proof applies to a finite disjoint formula whose internal
gates are activation gates; use the usual influence/variance edge
weights and the same global bank, not one new bank per level.

This corollary is conditional on the seed estimate and imports the
previous checked-author mantissa-bank theorem. It is not claimed novel
relative to existing read-once binary-formula FEI results. Its purpose
is the explicit ownership of scale, carry, reference, and deficit.

## Sharper unconditional activation-family entropy corollary

There is a shorter entropy estimate for this gate family, which also
shows why the carry obstruction is not an FEI counterexample. The three
physical gate coefficients are -a,e,1/2. Direct division by Delta_o gives

    E_o/Delta_o=ln4+2e ln(1/e)/(1-e)+2a ln(1/a)/(1-a)
                 <=4+ln4=:B.                           (11)

Here t ln(1/t)<=1-t follows from ln x<=x-1. Both nonconstant
fractions tend to one when e,a tend to one, so B is the EXACT supremum
for this binary gate family. Its scale constant 3ln4 and entropy constant
B are distinct bills; neither is used as an extra reserve for the other.

Exact corrected-entropy composition, using the same complete references
and KL in (6), yields for every finite independent activation chain

    E(F_d)=rho_0 E_g+sum_l rho_l E_o,l.

Thus E_g<=C Delta_g implies E(F_d)<=max(C,B)Delta(F_d),
uniformly in depth, seed arity, and all product biases. Sign changes of
inputs or output preserve E and Delta with the reflected product law.
The corollary therefore covers all nested canalyzing decision-list gates
on distinct physical inputs: at each node one selector value forces a
fixed output sign and the other continues to the remaining gate. Literal
leaves have E=Delta=0. Consequently this explicit nonsymmetric family
satisfies E<=B Delta at EVERY interior product law. B is sharp already
for a two-input gate. For any fixed nonliteral gate, adjoining a selector
with e tending to one makes E and Delta converge to their original
positive-deficit values: all new selector masses vanish and t^2 ln(1/t^2)
is continuous on [0,1]. Thus adjoining finitely many essential selectors
preserves ratios arbitrarily closely, proving the same supremum at every
prescribed arity at least two. No boundary maximum is asserted.

For a fair physical cube, E=(ln2)H^+, and the omitted empty entropy
P_empty ln(1/P_empty) is at most Var(f). Hence ordinary uniform FEI
holds for this family with C=B/ln2=2+4/ln2, also with no depth or fan-in
surcharge. For an arbitrary seed with only J_g<=K Delta_g, the previous
mantissa bank gives the improved conditional bound

    E(F_d), J(F_d)<=max(K+11/2,B) Delta(F_d).

This replaces (10)'s weaker estimate when useful. These elementary
binary/read-once consequences are not asserted as a literature novelty.
They close this explicit gate family while leaving the arbitrary seed
payment unchanged. In a formula containing a nonbinary seed gate, the
bound on that seed must hold at its actual induced independent law.

## First unsupported universal line

No uniform bound on arbitrary seed J_g/Delta_g is proved. In particular,
paying the outer activation gate by (2) does not pay the inherited seed
or its carry from the fresh selector deficit; (5) rules out the latter
route. The next universal step must use the SAME unused seed capacity
while retaining (6)-(8), or bound the remaining high-degree scale in
A043's singleton-preserving complete reference. Full FEI remains OPEN.
