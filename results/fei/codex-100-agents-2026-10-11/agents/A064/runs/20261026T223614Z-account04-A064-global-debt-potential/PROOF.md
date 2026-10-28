# Selected resets: the order of information changes the required capital

All entropy and divergence are in bits. Everything is finite. This is a
source-complete proof awaiting independent review, not a proof of full FEI.

## 1. Source, reference and admissible actions

Let g be any Boolean function on n uniform bits, n>=0. Write P for its
squared Fourier law, H=H(P), and T=TC(P)=sum_j h2(Inf_j g)-H>=0. Constants
and characters, for which T=0, are included. Set

    F(u,v,y)=g(y) if v=0, and (-1)^u g(y) if v=1.

The mask has four Fourier coefficients of magnitude 1/2. Thus

    H(F)=H+2, I(F)=I(g)+1.

Start with the ACTUAL spectral reference Q=P_F, not with a free product
reference: initial KL is zero and initial cross entropy is H+2. All dummy
bits introduced below are physical bits on which F does not depend. Their
Fourier coordinates have deterministic empty reference marginals.

The protected query is v. Its two Fourier rows indexed by the u-frequency
have pairs of equal or opposite coefficients. The coherent channel sends
each occupied row deterministically to the corresponding outcome. Both
outcome masses are exactly 1/2, so prediction KL O_v=0 and erased KL E_v=0.
After this query the actual children are g and (-1)^u g. Their entropy is H,
their inherited reference is their exact spectrum, and their KL is zero.
Consequently this query releases EXACTLY two bits of full cross entropy.
This is physical entropy release, not extra influence or a new owner.

Querying any unused dummy bit leaves source and FULL reference unchanged,
predicts both physical outcomes with probability 1/2, and has E=O=0.
This remains true on source-zero rows: the zero-row channel extension is fair.
No data coordinate is queried anywhere in this theorem.

Fix a finite fair dummy decision tree and a terminal reset choice. For a
single core, its cost is L=T on reset leaves and L=0 on retention leaves.
At a reset replace the inherited reference by the actual marginal product;
its KL is T and its full cross entropy is H+T. Retention costs H. A reset
is performed only once. Every tree prefix, immediately before and after
the reset, and every early stopping cut is admissible. Early stopping
retains the current reference. Any old debit omega>=0 stays consumed.

More generally, if g is a product of Boolean functions on DISJOINT blocks,
choose at each leaf any subset A of blocks to reset. Write T_j for the
block total correlations. The full chosen reference is the tensor of the
chosen block products and the retained exact block spectra (and the
deterministic u-frequency). Its cost is

    L=sum_{j in A} T_j.

No independence of the choices is assumed; the fair dummy path may couple
all choices. Tensor spectral entropy and KL add because the DATA blocks
are disjoint. Reference-only atoms of each product law are all retained.
All these references support the source, including endpoint marginals.

## 2. Lottery after the protected query

First query v, then reveal the dummy decision tree, then perform its declared
reset. Put lambda_s=E[L | dummy prefix s] at every lottery node, with the
expectation computed under its actual remaining fair outcomes. It is finite,
nonnegative, and harmonic: lambda_s=(lambda_s0+lambda_s1)/2. At a leaf it
equals its declared nonnegative cost L. Let lambda=E L at the lottery root.

Define the FULL potential V as follows:

    at the original root:     V=H+max(2,lambda);
    after v, during lottery:  V=H+lambda_s;
    after the reset choice:   V=H+L.

At each node V is at least the CURRENT actual cross entropy. At the
original root this requires the 2 in the maximum, since stopping there
retains H(F)=H+2. Before reset the current KL is zero. After reset the
current KL is L. Dummy transitions and reset transitions preserve expected
V, while the root transition decreases it by [2-lambda]_+.

Finite backward induction, WITHOUT independence between separate reset
events, proves for EVERY stopping cut tau of this declared rule

    E[H(F_tau)+KL(P_tau||Q_tau)] <= H+max(2,lambda).       (1)

There are no hidden query charges: all outcome KL costs are zero. If they
are written as a sum on the left of (1), that sum is zero. At the complete
terminal cut entropy is H and expected KL is lambda, separately. The root
extra reserve above its already booked full CE H+2 is

    G_after=[lambda-2]_+.

This value is MINIMAL among all nonnegative reserves above current full
CE controlling every admitted cut: stopping immediately forces H+2, and
finishing forces H+lambda. The potential displayed above attains their
maximum. This also establishes the exact initial condition from a SAME
original supplied account S:

    S-omega >= H+max(2,lambda).                          (2)

One may supply an independent proof H<=c I(g), but it is an explicit
additional hypothesis, not a conclusion from Q=P. No unknown root entropy
is hidden inside the word 'supplied'.

## 3. The same lottery before the protected query

Now reveal the SAME finite dummy decision tree before v, with its eventual
choice L known at the leaf. Then query v and perform that choice. Terminal
source/reference distributions, expected entropy H, expected KL lambda,
and zero outcome KL costs are exactly the same as in section 2.

At a lottery leaf BEFORE v, stopping costs H+2; continuing costs H+L.
Its least capital is H+max(2,L). At an earlier dummy prefix s, the least
capital is

    V_before(s)=H+2+E[(L-2)_+ | s].

Indeed each future child has this value in expectation, and this value
already dominates the current H+2. After v use H+L until reset; after
reset use actual H+L. This yields the exact least root capital

    A_before=H+2+E[(L-2)_+],
    A_after =H+2+(E L-2)_+.

For necessity in the before order, choose the ADAPTED cut that at each
lottery leaf stops before v if L<=2, and otherwise executes v and reset.
Its expected actual full CE is exactly A_before. This cut is missing if
one merely checks the complete terminal cut. Sufficiency follows from the
displayed harmonic potential. Thus the exact ordering penalty is

    E[(L-2)_+] - (E L-2)_+ >= 0,                       (3)

by the two elementary inequalities E[(L-2)_+]>=0 and
E[(L-2)_+]>=E L-2. No Jensen regularity or limiting argument is needed.

For a reset event of dyadic probability epsilon and one cost T>2,

    G_before=epsilon(T-2), G_after=(epsilon T-2)_+.

If epsilon T<=2, moving the actual lottery after v removes ALL extra root
reserve. On the success branch V still grows from H+epsilon T to H+T.
Taking success to mean k consecutive zero dummy outcomes gives epsilon=2^-k
and arbitrarily rare, arbitrarily large conditional growth. Failures stop
with the full inherited entropy H; no zero-entropy endpoint is substituted.

## 4. Relation to the all-product-stop obstruction

A087's full-terminal refinement is valid. For point_m=1-2*1[x=0], let
d=2^(1-m), N=1/d, and g_m be the tensor of N independent copies (m>=2).
Every point influence is d, so I(g_m)=m. If BOTH full product stops after
v are admitted, each terminal CE is M(g_m)=N m h2(d). Since
h2(d)>=d log2(1/d)=d(m-1), ANY account, regardless of starting reference,
must satisfy A/I(F_m)>=m(m-1)/(m+1). Other KL outcome costs are nonnegative.
This independently reconstructs the stated lower bound without using the
source's GU proof. It is not a counterexample to FEI.

The selected after-order rule instead admits that expensive reset only on
its declared dummy event. Choosing any k with 2^-k TC(g_m)<=2 gives
lambda<=2 and NO extra reserve above H(g_m)+2. The exact core entropy bound
H(g_m)<=4m, proved below, gives H(g_m)+2<=4I(F_m). Therefore S=5I(F_m)
with already consumed omega<=I(F_m) suffices from the SAME original
account. This is an explicit sufficient bound, not fresh money at a
descendant. The exact condition S-omega>=H(g_m)+2 remains authoritative.

For completeness, point spectrum has p_empty=(1-d)^2 and p_S=d^2 for
nonempty S. Its entropy divided by d is

    H(point_m)/d = -2(1-d)^2 log2(1-d)/d + 2(2-d)(m-1).

Using -ln(1-d)<=d/(1-d) gives the first term <=2(1-d)/ln2.
For m>=2, ln2>1/2 implies this term <4(1-d), hence
H(point_m)/d <=4(m-1)+4 =4m. Thus H(g_m)<=4m. Endpoints m=1 and all constants are handled separately
and are not used by this tensor family. The theorem in sections 1--3 is
valid also for n=0 and T=0.

## 5. Exact unpaid step

The lottery theorem applies to EVERY arbitrary core but starts with its
explicit full entropy H(g)+2. Consequently it DOES NOT influence-price an
arbitrary core's original entropy. Its new content is an exact difference
between two physically implementable orders with identical complete
terminal laws, and a selected reset schedule paid by actual entropy release,
without the invalid universal ALL-product-stop requirement. The initial
arbitrary-core bound S-omega>=H(g)+max(2,E L), or a noncircular mechanism
replacing that initial full-entropy source, remains the first unsupported
universal line. Another independent tensor or finite point example cannot
remove that line.
