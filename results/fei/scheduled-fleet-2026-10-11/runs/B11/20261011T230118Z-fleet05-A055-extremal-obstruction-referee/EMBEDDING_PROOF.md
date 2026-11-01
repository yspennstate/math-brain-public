# Exact critical-class admission referee

All inputs are uniform physical cubes, outputs are signs, and H is in bits. Define D_C(f)=H(f)-C I(f), and L_A(f)=H(f)-E_a H(f_a). Constants have D=0. A threshold-critical sign has D_C(f)>0 and D_C(f_a)<=0 for every proper physical restriction. Ratio-critical means H(f_a)<=R(f) I(f_a) for every proper restriction; this convention covers constant children without dividing by zero.

## 1. The precise necessary inequality

Physical edge averaging gives I(f)=I_A(f)+E_a I(f_a). Hence, without any criticality assumption,

    L_A-C I_A-D_C(f)=-E_a D_C(f_a).                 (1)

Threshold-criticality requires the left side to be nonnegative for each nonempty proper block. Failure is quantitative: if the right side is negative, some actual child has positive deficit. This is a necessary test; passing its average for every block is weaker than passing every individual descendant. The block identity does not authorize component pruning. Ratio-criticality gives L_A-R(f) I_A>=0 by the same algebra.

## 2. Tensor embedding: a complete block-failure ledger

Let g(x), h(y) be signs on disjoint nonempty blocks X,Y, and F=g h. Fourier coefficients multiply, so H(F)=H(g)+H(h), I(F)=I(g)+I(h), D_C(F)=D_C(g)+D_C(h). Fixing Y leaves +/-g, with constant factors +/-1 even if h is constant. Consequently

    L_Y=H(h), I_Y=I(h),
    L_Y-C I_Y-D_C(F)=-D_C(g).                     (2)

The first tested block Y fails by precisely D_C(g)>0 when g is a hard core. The X block fails by D_C(h)>0 when h also violates. There is no invariant notion of the chronologically first failing block; Y is an explicit certificate and need not have minimum cardinality. For an arbitrary A=A_X union A_Y,

    L_A(F)=L_A_X(g)+L_A_Y(h), I_A(F)=I_A_X(g)+I_A_Y(h).

This specifies every averaged block test from the corresponding core tests. Individual proper restrictions exposing g already disqualify minimal criticality. Nontrivial tensor primitivity fails as well. If h has zero essential coordinates, the operation adds only dummies and cannot be treated as essential-dimension growth.

At the ratio R(F), L_Y-R(F) I_Y = -[H(g)-R(F)I(g)]. A product can pass ratio-criticality only if its nonconstant factors have exactly the same ratio and their descendants do not improve it; thus the strict-threshold and ratio tests must not be conflated. Equal-ratio factors may yield a ratio-critical product while never giving a dimension-minimal threshold witness.

## 3. Activation for an arbitrary biased core

Let r>=1, t=2^-r, a(y)=1_{y=0}, F_r(x,y)=1+a(y)(g(x)-1), mu=E g, v=1-mu^2, and q=(1-mu)/2. For a selector subset U and a core subset S the exact coefficients are

    empty/empty: b=1-t+t mu;
    S=empty,U!=empty: t(mu-1);
    S!=empty,any U: t ghat(S).

All selector characters take value +1 at the active point. This also handles mu=+/-1 by zero-mass conventions. Let c=t^2(1-mu)^2. Summing entropy of these coefficients gives

    H(F_r)=-b^2 log2 b^2 -(2^r-1)c log2 c
           +t H(g)+t mu^2 log2 mu^2+2rt v,       (3)
    I_X(F_r)=t I(g), I_Y(F_r)=rt(1-mu).          (4)

Terms 0 log0 vanish. For mu=0, (3) reduces exactly to the published balanced-activation formula; no new baseline claim is made.

Fix all controls Y. One child is g and the other 2^r-1 are +1. Therefore

    L_Y=H(F_r)-t H(g),
    L_Y-C I_Y-D_C(F_r)=-t D_C(g).               (5)

Every hard-core activation fails this averaged block test by t D_C(g)>0; the all-on restriction itself is a smaller violating child. Small support and small influence do not repair criticality.

Fix all core inputs X. A fraction q of children are the r-bit point-defect d_r=1-2*1_0, and the rest are constant. Consequently

    L_X=H(F_r)-q H(d_r),
    L_X-C I_X-D_C(F_r)=-q D_C(d_r).             (6)

Here I(d_r)=2r t and

    H(d_r)=-(1-2t)^2 log2(1-2t)^2
           +8t(1-t)(r-1).

The second block test fails precisely when q>0 and H(d_r)>C I(d_r); its outcome is independent of the core entropy. In particular it can fail alongside the control-block test. If r=1, H(d_1)=0 and I(d_1)=1: the core-block test instead passes by q C. These are exact conditional conclusions, not a proposed universal C.

For any k controls fixed together (1<=k<=r), the all-on branch is F_{r-k} and others are constant, with F_0=g. Hence

    L_A-C I_A-D_C(F_r)=-2^-k D_C(F_{r-k}).       (7)

This locates the earliest singleton failure whenever the smaller activation still violates; if it does not, the full control block still fails (5). For core subset A, averaged restricted deficits are E_x D_C(activate(g_x,r)); this is the exact remaining test, with no unsupported inheritance claim.

## 4. Independent review of the near-tensor repair, and a stronger failed test

Take any sign G on d physical core bits (it can itself be a tensor), form F(x,z)=(-1)^z G(x) on N=d+1>=2 bits and flip a single point a to obtain J. Put p=2^-N and e=2p. Flipping z is an exact signed translation of F. The defect breaks this relation at exactly a and a xor e_z, so

    epsilon_z=(1-|E J(X)J(X xor e_z)|)/2=e,
    Inf_z(J)=1-e.                               (8)

Thus full Fourier support and primitivity do not erase the near-symmetry.

For a singleton i, write coefficients as alpha_T at T and beta_T at T union {i}. Let A_T=alpha_T^2, B_T=beta_T^2. Pairing the spectrum gives the conditional entropy B_i=sum_T(A_T+B_T) h2(B_T/(A_T+B_T))<=h2(Inf_i) by concavity. The children have amplitudes alpha_T +/- beta_T; their Jensen-Shannon information obeys JS<=kappa min(Inf_i,1-Inf_i), kappa=2/ln2. A proof of this centered bound is given in the review below; in particular it does not assume FEI. Therefore

    L_z(J)<=h2(e)+kappa e.                      (9)

Equation (1) for z then gives

    E_z D_C(J_z)>=D_C(J)+C(1-e)-h2(e)-kappa e.   (10)

For N>=5 and C>=1 this has an explicit uniform positive margin. Indeed h2(e)<=e log2(1/e)+e log2(euler), where log2(euler)=1/ln2. This follows from -(1-e)ln(1-e)<=e, proved by integration of 1/(1-u) or differentiation. Since ln2=2 atanh(1/3)>2/3, log2(euler)<3/2. Thus

    C(1-e)-h2(e)-kappa e
       >=1-e[N+3 log2(euler)]
       >1-2^(1-N)(N+9/2)>=13/32.               (11)

The last product decreases with integer N>=5 and equals 19/32 at N=5. Hence any J of this form with D_C(J)>0 has a violating fresh-sign child, with averaged deficit >D_C(J)+13/32. This fails a singleton extremality test, before one needs the larger restriction exposing g used in A053. Even for D_C(J)=0, ratio-criticality with R(J)>=1 is impossible. This is an exclusion for this surgery embedding, not a dimension-free FEI bound.

To prove (9)'s centered JS bound directly, apply the two-point cube logarithmic Sobolev inequality Ent(w^2)<=2||D_i w||_2^2 to the partial Fourier fiber w_T(x_i)=alpha_T+x_i beta_T, after choosing either w_T or x_i w_T. Their squares agree, and the smaller derivative energy is min(alpha_T^2,beta_T^2). Summing fibers gives (ln2) JS<=2 sum_T min(A_T,B_T)<=2 min(Inf_i,1-Inf_i). The full two-point proof appears in REVIEW_A053.md; zeros are harmless. This is also the rank-one epsilon test in A052's interface, here rederived independently.

## 5. Other live critical-class tests and scope verdict

A051 all-descendant criticality: tensor and activation fail (2),(5); balanced-tensor surgery fails the stronger singleton test (10)--(11). The impossibility of these constructions is not a proof that the entire critical class is easier or excludes all encodings of arbitrary cores.

A052 syndrome/translation concentration: (8)--(11) is an explicit failed rank-one test, despite A053's qualitative admissions. No dimension-independent lower bound on every translation mismatch has been proved for general critical signs; the necessary bound still depends on influence and deficit.

A053 qualitative full support, all essential coordinates, tensor primitivity and connected multiplicative-curvature graph: independently accepted as FEI-hard admissions, with their criticality failure retained. Tensor and activation alone need not satisfy these qualitative conditions. The surgery repair satisfies them but still fails (10).

A054 thin-cylinder plus density condition: simple activation has negative-set density t q. For connected nonempty negative core support its single selector cylinder passes the geometry, while p>=p0 imposes t q>=p0. For arbitrary disconnected core support, several actual components share the same selector point, so the disjoint-selector-cylinder condition fails as well. Balanced connected cores have q=1/2; at p0=1/4 only r=1 fits. Rare r->infinity activations fail density, and the admitted ones still fail criticality by (5).

Both geometry and density can nevertheless be preserved for an arbitrary core using a different, two-tag construction. Let K(x,w)=-1 when w=0 and K(x,w)=g(x) when w=1. Define T(x,w,y)=K(x,w) when y=0 and +1 when y=1. Its negative set is

    {y=0} x [({w=0} x full data cube) union ({w=1} x {g=-1})].

The bracket is connected: the w=0 cube is connected and each other negative vertex is adjacent to it. Thus there is exactly one actual component, a selector cylinder fixing d_y=1 on A={y}; this is a proper separator, with d_y>=|A|/2. Its density is p=(3-mu)/8 in [1/4,1/2] for every Boolean g. These facts retain every geometric and density hypothesis in A054's sign-critical theorem; no condition that the data set is a subcube is required there.

Direct physical edges give I_x(T)=I(g)/4, Inf_w(T)=(1+mu)/4, Inf_y(T)=(3-mu)/4, so I(T)=I(g)/4+1 exactly. Since K=-activate(-g,1), apply (3) twice to get

    H(T)=H(g)/4+E(g), 0<=E(g)<=9/2.             (12)

For any one-control activation, entropy minus half its core entropy is between zero and three: the lower bound is L_control>=0 from entropy concavity/conditional entropy, and the upper bound follows from (3), using -a log2 a<=1 for a in [0,1], mu^2 log2 mu^2<=0 and v<=1. Composition gives E<=3/2+3. The inequality -a log2 a<=1 follows from its maximum 1/(euler ln2)<1 (ln2>2/3 and euler>2). No log approximation enters (12).

Use g_m=g on m independent data copies. Then I(T_m)=m I(g)/4+1, H(T_m)=m H(g)/4+E(g_m), and H(T_m)/I(T_m)->H(g)/I(g) for every fixed nonconstant g. Hence the geometric/density class alone has exactly the unrestricted extended optimal FEI constant. This does not refute the critical subclass bound.

Indeed fixing both tags yields three constant branches and g with probability 1/4. Equation (1) gives the exact failed criticality test

    L_{w,y}(T)-C I_{w,y}(T)-D_C(T)=-D_C(g)/4.  (13)

This block is proper whenever the core has positive dimension; I_{w,y}=1. A violated core threshold therefore fails the test by D_C(g)/4. Fixing y=0,w=1 is an actual smaller violating child. The one-bit separator may have a different averaged deficit, namely -D_C(K)/2; (13) supplies a certificate even when that singleton does not fail. This construction identifies precisely what the genuine all-descendant criticality contributes to A054, rather than assuming its geometry rules out arbitrary cores.

No embedding here preserves every genuine criticality test for an arbitrary violating core. The first unsupported universal line is an affordable proper-block descent for every prospective dimension-critical C-witness at one fixed finite C. The exact low-deficit proper children, not generic hardness-preserving encodings, are the next target.
