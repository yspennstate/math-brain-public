# Approximate code packets have an explicit genuine Boolean comparison

2026-09-30 UTC. Proved L2 comparison only. Full FEI and an influence-paid entropy transfer remain open.

## Statement

Let C<=F_2^n have rank r>=1 and distance D>2d. For an arbitrary actual Boolean f, retain only frequencies in the disjoint balls B(c,d), c in C, writing the truncation as

    g(x)=sum_(c in C) chi_c(x)u_c(x),       deg u_c<=d.

Let delta=||f−g||_2^2 be off-packet spectral mass. Use a generator matrix M of C. An information set A is a set of r coordinate columns for which M_A is invertible; put B=[n]\A. For uniform x in F_2^n and z in F_2^r, define x' by

    x'_B=x_B,             Mx'=z.

The A-coordinates of x' are uniquely determined. Set

    G_z(x)=f(x'),
    h_z(x)=sum_(c in C) chi_c(z)u_c(x),

where codewords are identified with their generator-coordinate labels for the character chi_c(z). Every G_z is genuinely Boolean and depends on only n−r physical x-coordinates. The h_z are degree-d polynomials; they need not be Boolean in this approximate setting.

For an in-packet frequency T=c+S, |S|<=d, call S its decoded residual, and put

    beta_A=sum_(c,S: S intersects A) fhat(c+S)^2.

Then the exact identity is

    E_(x,z) |h_z(x)−G_z(x)|^2 = delta+2 beta_A.          (1)

Moreover C has at least L=ceil(D/r) pairwise disjoint information sets. Hence some information set satisfies

    beta_A <= J_res/L,
    J_res=sum_(c,S) |S| fhat(c+S)^2,                    (2)

and its comparison error is at most delta+2J_res/L.

## Proof of the exact identity

Use row frequency vectors and write a codeword as c=lambda M. Since

    x'_A=M_A^(-1)(z−M_B x_B),

the original character at frequency T becomes the character on (z,x_B) with label

    (T_A M_A^(-1), T_B+T_A M_A^(-1)M_B).

This map is bijective on the original n frequency bits. Thus G has norm one and its Fourier coefficients are exactly the original coefficients placed at these canonical labels; it has no x_A frequencies.

The field h instead puts a packet coefficient fhat(c+S) at joint label (S,lambda). These labels are distinct, so its squared norm is 1−delta. A term with S_A nonempty is orthogonal to every G term because G has no x_A dependence. When S_A is empty, the h label is exactly the transformed label of T=c+S in G. Conversely, equality of one such canonical label identifies T uniquely; radius-d decoding is unique because D>2d, so no extra packet can contribute to this overlap. Therefore

    E_(x,z) h_z(x)G_z(x)=1−delta−beta_A.

Expanding the squared distance gives (1).

## Proof of the information-set count

Removing fewer than D coordinate columns from M preserves its row rank: otherwise some nonzero codeword would be supported entirely on those removed coordinates, contradicting distance D.

Choose an information set and remove its r columns, then repeat. The kth set can be chosen whenever (k−1)r<D. This yields ceil(D/r) disjoint information sets. For a fixed residual S, the number of these sets it intersects is at most |S|. Sum its spectral mass over those intersections, then average over the L sets to obtain (2).

## Exact limitation on the influence transfer

The comparison is a Boolean function on a sheared affine fiber, not an ordinary coordinate restriction. Its averaged remaining-coordinate influence is exactly

    E_z I(G_z)
      =sum_T |T_B+T_A M_A^(-1)M_B| fhat(T)^2.           (3)

A simple consequence is

    E_z I(G_z) <= J_res+(n−r)(beta_A+delta).             (4)

For a good packet residual S_A=0, the new frequency is S_B. A bad packet or an off-packet frequency contributes at most n−r, proving (4). This bound is displayed to expose the possible cost; it is not an O(I(f)) theorem.

Neither (1) nor (2) supplies a dimension-free Fourier-entropy continuity bound. The two missing steps are nonlinear entropy transfer to the h_z or G_z, and payment of the shear influence (3). In particular rare arbitrary Boolean perturbations of a constant already have small off-packet mass, so a universal tail-influence-paid repair would carry genuine FEI difficulty.

The parent independently checked the label bijection, absence of extra overlaps, normalization, and greedy information-set argument before publication. Bounded repository searches under code anchors, disjoint information sets, and packet translations found no matching P03 statement; this is not a novelty certification. No executable code is included.
