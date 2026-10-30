# fleet02/B16 multiplicity-eight replacement, part 1 of 3

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924. This is a complete fixed-multiplicity-eight proof together with Parts 2 and 3. It does not claim the unrestricted three-eigenvalue theorem.

## Theorem and audited dependencies

For independent real coordinates with densities <=K, arbitrary symmetric A, arbitrary b,c, if s_8(A)>=s>0 then

||p_(X^TAX+b^TX+c)||_infinity < 2400 K^2/s.

Normalize K=s=1. Set eta=1/100 and kappa=1/6400. A physical pivot means |A_ii|>=eta or a principal 2x2 determinant of modulus >=eta.

Dependencies independently audited in this run:
(1) baseline 7c0d6e... volume sampling/completion: global rank <=3r, restricted complement rank <=r;
(2) baseline no-pivot s_5 consequence V_2>=kappa^2;
(3) latest-nine eeb752c8... grouped physical order-three receiver
||p_Q||_infinity <= C_3 Z_3^(-1/6), C_3=14.818337662843...<15;
(4) latest-nine five-eigenvalue full half-potential and pair envelopes, after the two-tail coordinate repair recorded in AUDIT.md.

## Pivot branches

Scalar pivot: complete the literal physical square in X_i. Its Schur complement retains at least seven unit spectral directions, hence s_5>=1. The latest-nine five-eigenvalue full half-potential is

max{70, 16(1/400)^(-1/4),
1+(3/40)^(-1/2)(J_0+2L_0)} <115,

with J_0=pi+4 log2 and L_0=4+4 log5. Hence the square profile gives density <10*115=1150.

Definite pair pivot: conditioning on the other original coordinates and using the deterministic elliptic change of variables gives pi/sqrt(D)<=10pi<32.

Indefinite pair pivot: the Schur critical value retains at least six unit directions. The repaired hyperbolic envelope and L_0 give

||p_Q||_infinity
<=10(6+log16+L_0)+1/e <197.

Thus every pivot branch is below 2400.

## No pivot: large V_3 is already paid

Assume no eta-pivot and s_8(A)>=1. If V_3>=kappa^3, a fair literal partition retains each ordered disjoint 3-by-3 minor with probability 4^(-3), so some crossing has

Z_3>=V_3/64>=kappa^3/64.

The audited order-three receiver gives

||p_Q||_infinity <=160 C_3
=2370.934026054879...<2400.

It remains to prove that V_3<kappa^3 is impossible.

## Good order-two seeds in the hypothetical small-V_3 chamber

Suppose V_3<kappa^3. Since s_8>=1 implies s_5>=1, the audited order-two structural proposition gives V_2>=kappa^2.

Sample every nonsingular ordered disjoint two-set seed B=A[S,T] with probability det(B)^2/V_2. Let L be the seed complement and P=A[.,T]B^(-1)A[S,.]. The exact sampling estimate gives

E_seed ||E||_F^2 <=9 V_3/V_2 <9 kappa.

Therefore seeds with ||E||_F^2<=18kappa carry at least half the determinant-squared mass. Call them good and put

epsilon=sqrt(18kappa)=3sqrt(2)/80.

For a good seed, the completion A=D+R+E has rank R<=6, rank R[L,L]<=2, D diagonal and zero on S union T. Hence

s_8(D+R)>=1-epsilon,
s_2(D)>=1-epsilon.

Choose H={h_1,h_2} subset L with |D_h|>=1-epsilon. Since D_h=A_hh-P_hh,

|P_hh|>=1-epsilon-eta,

while for h_1!=h_2,

|P_h1h2|<sqrt(eta^2+eta)+epsilon

and likewise for the reversed entry. Therefore

|det P[H,H]|>=delta_*,

where

delta_*=(1-epsilon-eta)^2
-(sqrt(eta^2+eta)+epsilon)^2
=97/100-(297sqrt(2)+3sqrt(202))/4000
=0.854335140191...>0.85.

Because P[H,H]=A[H,T]B^(-1)A[S,H],

|det A[S,H] det A[H,T]|
>=delta_* |det B|.                         (1)

Part 2 converts the determinant-squared family of inequalities (1) into one robust literal physical two-anchor.
