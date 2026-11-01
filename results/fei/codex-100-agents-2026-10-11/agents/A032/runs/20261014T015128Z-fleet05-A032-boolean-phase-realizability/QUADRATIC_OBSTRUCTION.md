# Exact quadratic-phase impossibility for the heavy row

In arbitrary data dimension, let an integer-valued h with max|h|<=2 have a coordinate-product spectrum with exactly one nonfair active coordinate j. Suppose its primitive Fourier magnitude ratio on j is4:1, and every other active coordinate is fair. No choice of Fourier signs quadratic over F2 on the spectral coordinate face can realize h. This is a certificate for a magnitude family, not just for one failed sign assignment.

Remove the deterministic spectral character and parameterize the active face by its free frequency bits. If its signs were (-1)^q for a polynomial q of degree at most2, define g by replacing the4:1 magnitude factor by1:1, leaving the common scalar and the signs unchanged. The inverse of a flat quadratic-phase spectrum has support an affine physical subspace L and a constant nonzero modulus u on L. For completeness this follows from polar cancellation: the squared Walsh sum of a quadratic q equals a character sum over its polar kernel; it is either zero or the kernel size times the cube size. Frequencies with nonzero sum form a coset of the kernel annihilator, and all nonzero sums have the same modulus. Deterministic frequency coordinates add a character and free physical directions; hence this support/modulus assertion holds on the whole original physical cube. The same quadratic Fourier fact is used in A079's DERIVATION.md, but this reconstruction needs no pending theorem as a premise.

Since the magnitude factor is4 when the j-frequency bit is0 and1 when it is1, Fourier inversion gives

h=(5/2)g+(3/2)T_j g,

where T_j flips physical coordinate j. The supports L and L+e_j are affine cosets of the same subspace, so are either disjoint or identical.

If disjoint, h has nonzero magnitudes5u/2 and3u/2. Integrality and gcd(5,3)=1 imply u/2 is a positive integer, so max|h|>=5, a contradiction.

If identical, g and T_jg each have real values+/-u there. Their sign ratio cannot be constant: otherwise T_jg=+/-g globally, forcing ghat to vanish on one of the two j-frequency halves. But ghat is nonzero on the full active coordinate face. Thus both sign ratios+1 and-1 occur, giving h magnitudes4u andu. Integrality implies u is a positive integer, so max|h|>=4, again a contradiction. Reversing the4:1 orientation only changes the relative sign of the two summands and gives the same argument.

Apply this to the previous stage's actual64-entry Boolean witness. Its heavy address row has w=17/32, normalized conditional marginal16/17 on data coordinate0 and1/2 on the other three data coordinates. Its primitive coefficient magnitudes therefore have ratio1:4 in that coordinate and are fair in the others. Every realizing sign choice for THIS labeled conditional law needs degree at least3 in its Fourier-sign ANF on the active face. The existing Boolean witness has phase monomials0,3,5,9,13 (frequency-bit masks); mask13 has degree3. It attains the obstruction sharply in phase degree. One other row has quadratic sign phase, so its explicit two four-cycle violations do not by themselves prove cubic necessity; the magnitude-family argument above does.

This refutes extending the affine factor or a quadratic-phase admission mechanism to that genuine heavy conditional law. It does not refute weighted payment Q<=1/2(H(w)+I_A), which the same witness satisfies. Nor does it show every law with the same address masses has this ratio; the certificate uses the displayed labeled product conditional law, not masses alone. The next universal unpaid term is the influence/entropy payment when a cubic Fourier-sign phase mixes translated flat supports that may overlap partially.
