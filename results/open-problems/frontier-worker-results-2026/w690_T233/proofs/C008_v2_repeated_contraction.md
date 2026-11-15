# C008 v2 — repeated polynomial contractions destroy every polynomial kernel bound

Kind: route-failure. Target 1. Author: codex-w690. ACCEPTED by an agent (route-failure, no move).
Strengthens v1 without exponentially ill-conditioned individual matrices.
No novelty claim. This is NOT a Gaussian or actual-GD counterexample.

## Statement and scope

For L=4n+2, m=L and fixed scalar X=Y=1 there are deterministic initial
weights satisfying C003/C004 initialization bounds, C005 boundary margins
m/4, and minimum ORIGINAL hidden singular value >=4/sqrt(m).
A modified tuple has max original-W Frobenius drift <=20/L, full imbalance
drift O(L^-3/2)=o(1/L), the same order-sqrt(m) hidden-block bound, and
    scalar kernel ~ (25pi^2/256) n^(-2n).                  (8v2.1)
Both losses equal 1/2. All hidden matrices at both tuples and along their
straight interpolation are invertible with polynomial conditioning.
Consequently these summary constraints do not furnish even a polynomial
lower bound on the averaged kernel over a fixed displacement neighborhood.
The actual Gaussian GD trajectory remains entirely open.

## Construction

Use the scalar-root, matrices and four disjoint coordinate definitions of
proofs/C008_averaged_kernel_obstruction.md, but now m=4n+2, eps=1/n and
M=n copies of each contracting projector. Let t=sqrt(m)/n,
w=tan(phi/n), u=w^2/t, rho=sqrt(1+w^2), k=sqrt(5/4), where
    (k+u^2/k)cos(phi)+(k u^2/w-w/k)sin(phi)=0,
    pi/4<phi<pi/2.
The same sign proof gives existence, cot(phi)=O(1/n), nw->pi/2.
Initial normalized layers in order:
    k e1; B^n; P^M; Q^M; C^n; k e2^T,
where powers here mean repeated LAYERS, B=I+tE_13, C=I+tE_42,
P=I-(1-eps)E_33 and Q=I-(1-eps)E_44.

Modified layers:
    a; A^n; P'; P^(M-1); Q^(M-1); Q'; Z^n; b^T,
where
    a=k e1-(u/k)e3, b=k e2-(u/k)e4,
    A=B-uE_31, Z=C-uE_24,
    P'=P-uE_13, Q'=Q-uE_42.
Each tuple has exactly 2n+2M+2=L layers. Extra contracting layers are
UNPERTURBED, so they cost no displacement. Everything acts on disjoint
(1,3) and (2,4) planes; the other hidden coordinates remain identity.

## Initialization, neighborhood and imbalance checks

Every initial forward prefix is k e1 and every initial backward suffix
k e2^T. Thus all endpoint Grams are k^2 and P_0=k^4(L-2)+2k^2.
Initial hidden-block norms are <=1+sqrt(m), because each plane contains
at most n shears and otherwise contractive projectors.
The first/last imbalance Rayleigh margins are -m/4,+m/4 as in v1.

All initial hidden singular values in original units are at least
sqrt(m)/n=(m/n)/sqrt(m)>=4/sqrt(m). Projectors attain sqrt(m)/n;
the shears have inverse norm <=1+t<=n. At modified projectors, inverse
norm <=(1+u)/eps, so their original singular values are at least
sqrt(m)/(n(1+u)); modified shears have singular values bounded away
from zero in normalized units for sufficiently large n. These statements
also hold with u replaced by s u, 0<=s<=1, along straight interpolation.

The largest original-W displacement is sqrt(m)u=nw^2<=4/n<=20/L.
Hidden block norms at the modified tuple remain
<=max{1,(1+u)rho^n(1+t/w)}<=2sqrt(m) for sufficiently large n:
the extra projectors are contractions, and the two coordinate planes
combine by a maximum of norms rather than a product.

All repeated-A, repeated-Z and boundary imbalance changes are the same
as v1 and have norm <=m u^2. The A-to-P' and Q'-to-Z seams have zero
change. The only additional changes divided by m are:
    P'-to-P: -u^2 E_11+eps u(E_13+E_31),
    Q-to-Q':  u^2 E_22-eps u(E_24+E_42).
All other projector seams are unchanged. Therefore
    max_i ||D_i(new)-D_i(old)||_op <=m(u^2+eps u)
       <=(16+4sqrt(m))/n^2 = O(L^-3/2).                   (8v2.2)
For any fixed nu>0, eta=nu/L and loss0=1/2, this is eventually
<=2eta loss0=nu/L. Replacing u by s u in the seam calculations shows
the same budget throughout the straight interpolation.

## Exact kernel

Let p_j=A^j a for 0<=j<=n, and r=(p_n)_3.
The scalar-root equation makes (P'p_n)_1=0 and gives
    P'p_n=eps r e3,  (P^(M-1)P')p_n=eps^M r e3.
The transposed backward statement is eps^M r e4 across all Q layers.
These vectors are unchanged by the factors on the opposite plane.
The entire network output is identically zero on the straight
interpolation, so its loss is 1/2 throughout.

Summing the ORIGINAL-W Jacobian contributions layer by layer yields
    P_new=2 eps^(2M) r^2 [
        1+sum_(j=0)^n ||p_j||^2
         +r^2 sum_(j=1)^(M-1) eps^(2j) ].                 (8v2.3)
The first sum accounts for the two boundary layers, shear blocks and
compensated projectors. The last geometric sum accounts for the extra
UNPERTURBED projectors; they too are TRAINABLE layers and are included.

As in v1, r^2~k^2 pi^2/(4m) and sum||p_j||^2~k^2 n/2.
The geometric correction is negligible. Since m=4n+2 and M=n,
    P_new/eps^(2n) -> k^4 pi^2/16=25pi^2/256.
With eps=1/n this proves (8v2.1), which is smaller than every inverse
polynomial in L. In particular (8v2.1) includes all L trainable layers,
rather than treating the added projectors as fixed maps.

## Why no Gaussian GD conclusion follows

The matrices and the imbalance tuple are highly structured and nongeneric;
this deterministic initialization has Gaussian probability zero.
The construction does not satisfy the GD update equations. In fact its
initial hidden gradients are -k^2 E_21, its first-layer gradient is
-k e2 and its last-layer gradient is -k e1^T (X=Y=1). Actual GD
therefore couples the two coordinate planes immediately, whereas the
constructed perturbations preserve them. Its straight
path has constant loss despite a nonzero initial gradient, so it is not a
strict sufficient-descent path. Thus the example only rules out universal
neighborhood lower bounds from these summaries, even with polynomial
individual conditioning, connected loss-sublevel feasibility and the
full imbalance-drift budget. It does not refute a trajectory argument
using the descent equations or richer Gaussian structure.

Independent 250-digit four-dimensional direct products, EVERY adjacent
imbalance, a scalar-root calculation, and the exact full-kernel sum
(including added trainable projectors) pass for n=8,16,32,64.
See scripts/check_repeated_contraction.py and
logs/repeated_contraction_check.json. No training experiment was run.
