# Immediate saved derivation: bounded lookahead versus stopping at a bad core

Use binary coordinates and Fourier characters (-1)^(S dot x).
For any Boolean sign g on m bits, define F_g(x,y)=(-1)^(x dot y)g(y).
Direct Fourier summation over x gives

  Fhat(A,B)=2^-m g(A)(-1)^(A dot B).

Thus F_g is bent: H=2m, I=m, D2=0. All physical influences are 1/2.
For every one-coordinate split the child coefficients are either zero
or +/-2^(1-m), so both child entropies are 2m-2. Every local ratio is 4.

Take m=3 and g(y)=-1 at y=0 and +1 elsewhere. Its Fourier law has
mass 9/16 at the empty set and 1/16 at each of seven nonempty sets:
H_g=4-(9/8)log2(3), I_g=3/4, D2(g)=(9/8)log2(3)-5/2<0.

Tree: reveal all three x coordinates; stop at x=0, leaving g;
at each x!=0 reveal all three y coordinates to constant leaves.
Terminal expected H=H_g/8 and I=3/32. The physical costs are

  Pi_H=6-H_g/8, Pi_I=3-3/32=93/32,
  Pi_H/Pi_I=(352+9 log2(3))/186<2.

Therefore r1-r_all >= (392-9 log2(3))/186 > 2.
The exact integer inequality 3^5=243<256=2^8 gives log2(3)<8/5,
and proves r1-r_all>944/465>203/100, without a floating-point sign.
Root D2=0; the stopped terminal cut has expected deficit D2(g)/8<0,
so the queried-node ledger is 2 Pi_I-Pi_H=-D2(g)/8>0. It is the
negative terminal deficit that permits this tree ratio below2. Keeping
that deficit makes the full ledger sum exactly zero, not an FEI gain.

The same paired seed construction explains why depth two does NOT
break. In a physical restriction, partition indices into P (both pair
coordinates free), U (x fixed, y free), V (y fixed, x free), and W
(both fixed). Let p=|P| and ell be the number of V indices with fixed
y=1. For t in {0,1}^P define the actual Boolean U-core
u_t(z)=g(t,z,fixed y) (-1)^(fixed x_U dot z), up to a harmless global sign.
Partial Fourier summation forces the x_P frequency to equal t; the
y_P frequency is uniform; the x_V spectral set is the fixed character.
Exactly, with expectation uniform over t,

  H(F_rho)=2p+E_t H(u_t),
  I(F_rho)=p+ell+E_t I(u_t),
  D2(F_rho)=2ell+E_t D2(u_t).

If the cut fixes at most two physical coordinates, |U|<=2. All Boolean
signs on at most two variables satisfy H<=2I (their complete classification
is constants, characters, and signed AND2). Hence every such leaf has
D2>=0. Since root D2=0, baseline B06 R2 gives Pi_H>=2 Pi_I for every
tree of depth<=2. Equality is achieved by querying y_j, then x_j only
in the y_j=1 branch: the second query removes a deterministic character
with entropy drop0 and weighted influence1/2. So r_depth2=2 for every
m>=1 and EVERY seed g; the depth-two gain is exactly2 on this broad family.

For quadratic bent functions in any even dimension, every restriction
is a quadratic Boolean sign. A quadratic with adjacency rank r has
entropy r and at least r nonisolated vertices, each influence1/2;
isolated character variables add nonnegative influence. Hence D2>=0
in all restrictions; a complete tree attains ratio2, so r_all=2.
The unrestricted "bent gain exactly2" statement needs the quadratic
hypothesis, and is false for the above cubic six-variable bent sign.

More generally, if D_K(f)=0, then every nonempty physical stopping tree
has Pi_H/Pi_I>=K iff every proper physical restriction f_rho has D_K>=0.
One direction is B06 R2. For the other, isolate any restriction with
D_K<0 along its fixed-coordinate path, complete every off-path branch
to constants, and stop at that restriction. Its terminal expected
deficit is 2^-codim D_K(f_rho)<0. This is a signed terminal-ownership
test, not a new derivation of the baseline telescope.

Disjoint tensors of the six-variable witness remain bent, have r1=4,
and inherit the same depth-six paid-tree ratio by running the witness
tree in one factor and leaving the other bent factors as spectators.
Thus the arbitrary-tree gain exceeds 2.03 in every dimension 6t, while
H/I remains exactly2. This refutes a helper, not the FEI conjecture.
