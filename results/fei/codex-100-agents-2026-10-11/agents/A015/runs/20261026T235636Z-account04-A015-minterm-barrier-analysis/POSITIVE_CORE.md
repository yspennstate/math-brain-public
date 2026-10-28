# Positive anchors retain the whole monotone FEI problem

For every nonconstant monotone sign function g on s>=1 uniform bits, there is a sequence of actual monotone positive-anchor CNFs F_L whose H/I converges to H(g)/I(g). Each displayed clause is an irredundant prime implicate and has exactly one relevant positive private bit. Consequently the supremum H/I over this positive-anchor class equals the supremum over all monotone Boolean functions. This does not identify monotone FEI with full FEI.

All entropies are in bits. Write G=(1+g)/2. Choose any finite positive CNF G=AND_j C_j(z), with nonempty core clauses C_j, j=1,...,t. Such a CNF exists: for each maximal false core point v, take the OR of the coordinates where v is zero. A true point cannot lie below v; a false point lies below some maximal false point. These two facts prove the representation. Nonconstancy gives t>=1 and every such anchor is nonempty. Dummies in the supplied core may be omitted, but are harmless.

Introduce fresh bits y_(j,l), 1<=l<=L, and put

    U_L=AND_(j,l) (C_j(z) OR y_(j,l)),   F_L=2U_L-1,
    epsilon=2^-L, B(z)={j:C_j(z)=0}, b(z)=|B(z)|,
    a(z)=epsilon^b(z), q=Pr[g=-1], N=s+tL.                 (1)

Private bits for different clauses and repeats are distinct. At fixed z, U_L is the AND of exactly Lb(z) private bits, so E_y F_L=2a-1. At true cores a=1; at false cores 0<a<=epsilon. Every private bit is relevant by setting its anchor false and all other private bits true. Setting precisely that private bit false also witnesses irredundancy. To delete its private literal, set its anchor false and all private bits true. To delete a chosen core literal, satisfy its anchor only through that literal, set the chosen private bit false, and all other private bits true. The function then equals one while the shortened clause fails. Thus each displayed clause is prime, even if the chosen base CNF contains redundant anchors. Completeness of the prime table is not asserted.

## Physical influence, including the overlap

Let I_core and I_private denote the sums over the two physical blocks. The exact identities are

    I_private(F_L)=2L E_z[b(z) epsilon^b(z)],
    I_core(F_L)=sum_i E_z |a(z)-a(z xor e_i)|.             (2)

For the first identity, each active private bit is pivotal exactly when all other Lb-1 active bits are true. For the second, neighboring positive-core assignments have nested false-clause sets. The two conjunction events on the SAME private cube are therefore nested, and their disagreement probability is the absolute difference of their probabilities. No independent-clone substitution is used.

Since b epsilon^(b-1)<=b/2^(b-1)<=1 for integer b>=1 and L>=1,

    I_private<=2Lq epsilon,
    |I_core-I(g)|<=2sq epsilon,
    |I(F_L)-I(g)|<=2q(s+L)epsilon.                         (3)

The second bound follows from | |a-a'|-|G-G'| |<=|a-G|+|a'-G'| and E|a-G|<=q epsilon. The induction b<=2^(b-1) has equality at b=1,2 and advances because b+1<=2b. Thus I(F_L)->I(g)>0. The bound is independent of the number of anchors t; that independence would be lost by replacing b epsilon^b with t epsilon.

Monotonicity is used at the nested-event line in (2). On signed anchors with incomparable B,B', the correct edge probability is a+a'-2 epsilon^|B union B'|. Equal a,a' can have a positive disagreement probability. This is a mandatory negative control, not an extension of (2).

## Signed spectrum and the growing private entropy

Every core-only coefficient equals the Walsh coefficient of m(z)=2a(z)-1. For a nonempty private set T, let J(T) be the set of anchor groups met by T. Its exact coefficient, for any core set S, is

    Fhat_L(S,T)=2 E_z[chi_S(z) epsilon^b(z) 1_{J(T) subset B(z)}]. (4)

The condition is on the actual set of private groups. It cannot be replaced by a positive pushforward of squared slice spectra. Parseval on each slice gives the exact total private spectral mass

    M=E_z Var_y(F_L|z)=4 E_z[a(z)(1-a(z))]<=4q epsilon.   (5)

Collapse ALL private-supported Fourier sets to one cemetery atom. The resulting probability law P_L has 2^s core atoms and one cemetery atom of mass M. The core signed amplitude vectors converge because ||m-g||_2<=2epsilon sqrt(q). Hence P_L converges to the squared spectrum of g with an additional zero atom. Its finite-dimensional entropy converges to H(g).

The private detail lost by this collapse is at most M log2(number of private-supported subsets)<=MN. Thus

    H(P_L)<=H(F_L)<=H(P_L)+4q epsilon(s+tL).              (6)

The last term tends to zero for FIXED finite g and its fixed t. This order of quantifiers is essential; no uniform entropy-continuity assertion in a growing cube is assumed. Equations (3),(6) prove H(F_L)->H(g) and the claimed ratio limit.

An optional finite bound makes the error explicit. The total variation distance between P_L and (ghat^2,0) is at most 2epsilon(sqrt(q)+q)<=4epsilon: apply Cauchy-Schwarz to the difference of the squared core amplitudes, then add M. For L>=3, d<=4epsilon<=1/2. The coupling entropy bound on an alphabet of size 2^s+1 gives |H(P_L)-H(g)|<=h2(d)+d s<=h2(4epsilon)+4epsilon s. To see the coupling bound, use a maximal coupling with disagreement event E of probability d: conditioning on E, one variable has at most 2^s alternatives to the other, so both conditional entropies are at most h2(d)+ds. Therefore

    |H(F_L)-H(g)|<=h2(4epsilon)+4epsilon s
                         +4qepsilon(s+tL),   L>=3.       (7)

No division by I(g) occurs until g is fixed and nonconstant. Constants obey FEI trivially and need no embedding.

## What this says about an original reference

Every F_L is monotone, so its supremum ratio is at most the monotone supremum. Every monotone g has the ratio limit just proved, giving the reverse inequality. A same-constant FEI theorem for all these positive-anchor CNFs is therefore exactly as strong as monotone FEI. If a complete normalized reference on ALL Fourier subsets costs at most C I(F_L), Gibbs' inequality yields that same conditional reduction. A NONEMPTY reference alone still needs its empty/nonempty wrapper; the wrapper is not discarded here.

Unlike A007's signed-point embedding, positive anchors generally do NOT give a common scaling of all nonempty core amplitudes. For g=AND2 and anchors z1,z2, the singleton amplitude ratio to g is 1-epsilon^2, while the pair ratio is (1-epsilon)^2. Consequently A007's exact finite conditioned-reference extraction identity cannot be copied into (1). Entropy convergence proves the stated same-constant FEI equivalence; an arbitrary changing supplied reference requires its own finite extraction or smoothing account.

The unpaid universal line is a core-sensitive original whole-set reference paid by one physical influence account. Positive anchor geometry can encode an arbitrary monotone truth table; positivity alone is no compression theorem. This result narrows the burden of the next source lemma without claiming any entropy/influence counterfamily.
