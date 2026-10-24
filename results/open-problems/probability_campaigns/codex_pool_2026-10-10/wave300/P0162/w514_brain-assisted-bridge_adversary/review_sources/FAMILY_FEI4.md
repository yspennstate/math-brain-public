# Explicit all-small-influence family: bad local split, global FEI constant 4

Own derivation, independent review pending, no novelty claim. This is a proved special family, not a solution of P0162.

Let M_3 be majority of three uniform sign bits. Its only nonzero Fourier coefficients are the three singletons (1/2 each) and the triple (-1/2). Hence it is balanced, H(M_3)=2, I(M_3)=3/2, and each individual influence is 1/2. Define G_d recursively as M_3 applied to three disjoint copies of G_(d-1), with G_0 a dictator. Every G_d is balanced and monotone, every leaf influence is alpha=2^-d, and

I(G_d)=beta=(3/2)^d,
H(G_d)=4(beta-1).

Here are the composition identities used to prove those formulas. If an outer Boolean F has k inputs and the k substituted gadgets are disjoint balanced Boolean copies of G, then

I(F(G,...,G))=I(F) I(G),
H(F(G,...,G))=H(F)+I(F)H(G).

Proof: balance forces every nonzero gadget coefficient to be on a nonempty subset. A physical Fourier subset therefore identifies its outer active-block set S uniquely. Its coefficient is Fhat(S) times the product of the gadget coefficients in the active blocks. Conditional on S under squared coefficients, the block spectral subsets are independent with the gadget's squared-coefficient law; Parseval normalizes each block. The entropy chain rule gives H(F)+E|S|H(G), and expected physical subset size gives E|S|I(G). This finite product factorization is valid specifically because the blocks are disjoint and balanced. Applying it to M_3 gives I(G_d)=(3/2)I(G_(d-1)) and H(G_d)=2+(3/2)H(G_(d-1)), proving the formulas. Leaf influences multiply by 1/2 at each level; this also follows directly by conditioning on the other disjoint branches.

Take the rare-switch outer function F_m of BRIDGE_CHECKPOINT.md, with m>=2 even, N=2^m. Its entropy is at most m+1, because it has at most 2^(m+1) Fourier outcomes. Its exact influence is

I(F_m)=m/2+(m+1)/N.

Proof: each original coordinate of the quadratic bent g is pivotal with probability 1/2. At zero and each unit vector g=+1. Flipping g only at zero to obtain h adds one previously nonpivotal edge for each coordinate, hence Inf_j(h)=1/2+2/N. Averaging the two restrictions gives Inf_j(F_m)=1/2+1/N; the selector has influence 1/N. Thus I(F_m)>=m/2 and H(F_m)<=m+1<=3m/2<=3I(F_m).

Define f_(m,d)=F_m(G_d,...,G_d) on (m+1)3^d physical bits. The composition identities give

H(f_(m,d)) <=I(F_m)[3+4(beta-1)]
=(4-beta^-1)I(f_(m,d)) <=4I(f_(m,d)).

All physical influences are at most alpha=2^-d. For any chosen selector-block leaf v, E[G_d+]=alpha and E[G_d-]=-alpha by balance and monotonicity, so the empty-selector-sector argument in SMALL_INFLUENCE_OBSTRUCTION.md applies unchanged:

Inf_v(f_(m,d))=alpha/N,
Delta_v(f_(m,d))/Inf_v(f_(m,d))>=alpha*m.

Consequently, for every tau>0 and M>0, choose d>=1 with 2^-d<=tau and even m>=max(2,M*2^d). This gives a Boolean f with all influences <=tau, with some coordinate restriction ratio >=M, and with H(f)<=4I(f). These three conclusions hold simultaneously.

This quantifier-preserving witness blocks a false arbitrary-coordinate lift of the brain's small-influence reduction. It leaves the existential good-coordinate route and the aggregate conditional-entropy budget open.

NEXT: Independent referee checks balanced block composition, the exact outer influence count, and the empty-selector sector. The unresolved target step remains the aggregate conditional-entropy estimate for arbitrary Boolean functions.
