# Dyadic rare activation: exact scale and complete-reference endpoint

All logarithms are natural. This is an arbitrary-seed theorem, not a proof of FEI.
Let g be any Boolean sign on a finite independent product cube with interior
active probabilities. Contract deterministic coordinates first. Write mu=Eg,
a=(1-mu)/2, V=Var(g)=4a(1-a), I=I(g), Delta_g=I-V.
For nonempty T let c_T be the physical normalized mixed coefficient,
P_T=v_T c_T^2. For occupied T choose the unique integer j_T>=0 with
1/2<2^j_T |c_T|<=1. Put W_T=v_T 4^-j_T, Z_g=sum W_T,
J_g=ln4 sum P_T j_T, E_g=sum P_T ln(1/c_T^2), L_g=E_g-J_g.
The complete flat reference is Q_g(empty)=1-V and
Q_g(T)=V W_T/Z_g. Its ordinary KL is K_g, and
n_g=V ln(Z_g/V), so E_g=J_g+n_g-K_g.

Independently choose X Bernoulli epsilon=2^-k, k>=1 integer, and set
F=1 on X=0 and F=g on X=1. For now 0<a<1; constants are treated below.
Let j_a be the cell of a and b=4^-j_a. Every formula below is exact.

## 1. Physical spectrum, deficit and zero carry

F=1-X+Xg. Direct mixed differences give, for nonempty T,
c_F(T)=epsilon c_T, c_F(XT)=c_T/2, c_F(X)=-a.
Thus P_F(T)=epsilon^2 P_T, P_F(XT)=epsilon(1-epsilon)P_T,
P_F(X)=4epsilon(1-epsilon)a^2, and EF=1-2a epsilon.
Consequently w=Var(F)=4a epsilon(1-a epsilon),
I_F=epsilon I+4a epsilon(1-epsilon),
Delta_F=epsilon I-epsilon^2 V
=epsilon Delta_g+epsilon(1-epsilon)V.
The last term is the original two-input activation gate's deficit Delta_o;
it is not a renewed seed bank.

Because epsilon and 1/2 are dyadic, j_F(T)=k+j_T,
j_F(XT)=1+j_T, and j_F(X)=j_a: all composition carries are zero.
Put B=V+4a^2 j_a. Then

J_F=epsilon J_g+ln4[epsilon(1-epsilon)B+epsilon^2 k V].       (1)

The bracket is the two-input activation gate's own scale charge /ln4.
For j_a=0, a^2 j_a=0. For j_a>=1, a<=2^-j_a and
j_a a<=j_a 2^-j_a<=1-2^-j_a<=1-a, because j<=2^j-1.
Therefore 0<=4a^2 j_a<=V, V<=B<=2V.
Also k/(2^k-1)<=1. Dividing (1)'s gate part by Delta_o gives

J_o/Delta_o=ln4[B/V+k/(2^k-1)]<=3ln4.                     (2)

Equality holds at a=epsilon=1/2. This constant for the DYADIC SCALE charge
is sharp; it is not the entropy constant for all binary biases.
If J_g<=K Delta_g, then J_F<=max(K,3ln4)Delta_F, without a carry surcharge.
Finite repeated independent dyadic activations obey the same bound by induction.

The exact endpoint certificate is

J_F/epsilon=J_g+ln4 B+ln4 epsilon(kV-B),
|J_F/epsilon-J_g-ln4 B|<=ln4 epsilon(k+2)V,                (3)
Delta_F/epsilon=I-epsilon V.

This error bound is uniform in the seed, with its actual V retained.
For a fixed seed, J_F/Delta_F tends to (J_g+ln4 B)/I.
Thus endpoint localization retains the arbitrary seed scale charge.

## 2. Corrected entropy and endpoint rounding remainder

The same spectrum yields

E_F=epsilon E_g+epsilon(1-epsilon)ln4 V
    +2epsilon^2 V ln(1/epsilon)+4epsilon(1-epsilon)h(a),    (4)

where h(t)=t^2 ln(1/t^2). Since 2ln(1/epsilon)=k ln4,
subtracting (1) gives the exact no-carry identity

L_F=epsilon L_g+4epsilon(1-epsilon)a^2 ln(b/a^2).          (5)

The last term is the outer gate's remainder L_o. In particular no finite
truncation or reset of the seed law has been used. Formula (4) gives the
corrected FEI+ expansion, while the exact Delta identity gives I-Var.

## 3. Complete reference and ordinary KL, with both full laws

Dyadic cells give W_F(T)=epsilon^2 W_T,
W_F(XT)=epsilon(1-epsilon)W_T, W_F(X)=4epsilon(1-epsilon)b.
Hence

Z_F=epsilon Z_g+4epsilon(1-epsilon)b,
Z_o=epsilon V+4epsilon(1-epsilon)b,
n_F=w ln(Z_F/w), n_o=w ln(Z_o/w).                         (6)

The complete flat Q_F has empty mass 1-w, and nonempty mass w W_F/Z_F.
Partition the nonempty atoms into the singleton {X} and the seed sector
{T,XT:T nonempty}. Let
s=4epsilon(1-epsilon)a^2/w,
t=4epsilon(1-epsilon)b/Z_F,
t_o=4epsilon(1-epsilon)b/Z_o.
The physical seed sector has total mass epsilon V; its conditional seed
label is P_T/V. The reference sector has conditional label W_T/Z_g.
In BOTH laws, conditional on the seed label, the two placements T and XT
have probabilities epsilon and 1-epsilon. These placement terms cancel
inside the logarithmic likelihood ratio. The empty atom's ratio is one.
Therefore the FULL ordinary KL satisfies

K_F=epsilon K_g+w d_Bern(s||t).                          (7)

No terminal entropy was discarded. In the complete composed reference
Q_tree formed from the outer gate Q_o and the complete seed Q_g, the
corresponding identity is

K_tree=epsilon K_g+w d_Bern(s||t_o),
n_tree=n_o+epsilon n_g,
CE_tree^+=J_F+n_tree,
E_F=CE_tree^+-K_tree.                                    (8)

The superscript + means corrected nonempty cross entropy. For FULL ordinary
cross entropy append exactly (1-w)ln(1/(1-w))+sum_nonempty P_F ln(1/v_S).
Both references have the same actual empty mass and no missing occupied atom.

Equations (5)-(8) imply the exact signed conversion

K_F-K_tree=CE_flat^+-CE_tree^+
         =w ln(Z_F/Z_o)-epsilon n_g.                     (9)

This conversion replaces the KL together with its reference. It does not
subtract both KLs. Since b>=a^2 and Z_g>=V, Z_o>=w and Z_F>=Z_o.
The elementary ln x<=x-1 gives the original-owner bound

0<=n_F-n_o=w ln(Z_F/Z_o)<=epsilon(Z_g-V).                 (10)

Thus A044's bound Z_g-V<=9Delta_g-6R_g, when imported, funds this positive
transfer by epsilon(9Delta_g-6R_g). This uses the inherited SEED allocation
once. It is not an additional available root account after that allocation
has already been spent. The identities and (10) themselves do not depend
on A044's bound.

For fixed nonconstant seed, as epsilon tends to zero through dyadic values,
s tends to a, t tends to t_*=4b/(Z_g+4b), and

n_F/epsilon -> 4a ln[(Z_g+4b)/(4a)],
K_F/epsilon -> K_g+4a d_Bern(a||t_*).                     (11)

Both Bernoulli arguments are interior. This is an ordinary finite-dimensional
continuity limit of (6)-(7), with the full seed KL retained exactly.

## 4. Zero deficit, constants and the unit-atom endpoint

Reflecting the selector X to 1-X preserves every squared Fourier mass,
absolute normalized coefficient, reference weight and influence. Consequently
the same results apply to activation on X=0 with Pr(X=1)=1-2^-k; they cover
the corresponding selected probability tending to one as well as to zero.

For a=0, F=1 and all displayed costs are zero; omit undefined conditionals.
For a=1, F=1-2X is a signed literal: j_X=0, Z_F=w,
E_F=J_F=n_F=K_F=Delta_F=0. The occupied conditional nonempty spectrum is
a unit atom, and both complete laws agree. For interior epsilon and 0<a<1,
Delta_o>0, hence Delta_F>0. Thus these constants exhaust zero deficit
inside this activation family, including deterministic seed contractions.
At epsilon=0, contract X and F is constant; do not use a normalized
conditional law of zero mass. At epsilon=1 the physical function is g
after contraction, but epsilon=1 is outside k>=1: no claim extrapolates
the dyadic cell formula to a new positive coordinate at that boundary.

## 5. Gap and adversarial audit

The strongest tempting misreading is that a rare selector makes the seed
scale charge negligible relative to the root deficit. Equations (1),(3)
and Delta_F/epsilon=I-epsilon V explicitly refute that inference: the seed
term is epsilon J_g, on the SAME scale as epsilon I. A fair parity seed
has Delta_g>0 but J_g=0; an arbitrary seed need not. Normalizer bounds
and zero carry alone do not pay J_g. No full FEI statement follows.

Independent implementation checks direct physical mixed differences against
these identities and complete likelihood-ratio factorizations. The continuum
and arbitrary-dimension theorem follows from the derivation, not finite
extrapolation. No Lean proof is claimed.
