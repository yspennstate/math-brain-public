# Rigor check — simultaneous subdensity Fresnel receiver

Run: 20260924T111432Z-fleet02-B15-QFORM-auto11

## Scope check

The source Theorem F is used only in its stated product-preserving scope: A=sum_{k=1}^3 lambda_k v_k v_k^T+B, an original-coordinate set I with B_II diagonal, G=sum_{i in I}rho_i rho_i^T invertible, normalized leverages c_i=rho_i^T G^{-1}rho_i<=1/2, arbitrary outside blocks, and arbitrary affine terms. No spectral-coordinate independence is asserted.

Selected factors are finite subdensities 0<=h_i<=1. Unselected cap-one subdensities can be completed to cap-one probability densities, so the source L^p lemma remains applicable to them. A selected row with c_i=0 is absent from the Fresnel/BL variables and contributes at most its mass m_i; this is exactly the continuous c_i=0 convention in the theorem.

## Fourier-factor check

For p=1/c>=2 and a=h exp(i tau),

||hat a||_infinity <= ||a||_1=m,

integral |hat a|^2 = 2 pi ||a||_2^2 <=2 pi m.

Therefore

integral |hat a|^p <= m^{p-2}(2 pi m)=2 pi m^{p-1}.

The source probability-factor estimate at the same exponent is

integral |hat a|^{1/c} <=4 pi sqrt(c).

After the BL normalization c^{-1/2} and the outer exponent c, replacing the source factor by the submass factor changes it by

[(2 pi)c^{-1/2}m^{1/c-1}]^c/(4 pi)^c
=(2 sqrt(c))^{-c}m^{1-c}.

Thus

|hat nu(t)| <= B|t|^{-3/2},

B=(4 pi)^{3/2}(L det G)^(-1/2)
  product_{i in S}(2 sqrt(c_i))^{-c_i}m_i^{1-c_i}.

## Fourier-inversion constant check

The finite measure has total mass at most M=product_{i in S}m_i, hence

|hat nu(t)|<=min(M,B|t|^{-3/2}).

At t_0=(B/M)^{2/3},

integral_R min(M,B|t|^{-3/2})dt
=2[M t_0 + integral_{t_0}^infinity B t^{-3/2}dt]
=6B^{2/3}M^{1/3}.

Multiplication by (2pi)^{-1} and

[(4pi)^{3/2}]^{2/3}=4pi

gives the exact outer constant 12. For each selected coordinate the mass exponent is

(2/3)(1-c_i)+1/3=1-2c_i/3.

Therefore

||dnu/ds||_infinity
<=12(L det G)^(-1/3)
  product_{i in S}(2 sqrt(c_i))^{-2c_i/3}m_i^{1-2c_i/3}.

## Uniform factor check

For K(c)=(2sqrt(c))^{-2c/3},

log K(c)=-(c/3)log(4c).

Its derivative vanishes at c=1/(4e), giving

max_{0<=c<=1/2}K(c)=exp(1/(12e))=1.0311313732990348... .

Also 1-2c/3>=2/3, so for 0<=m<=1,

K(c)m^{1-2c/3}<=exp(1/(12e))m^{2/3}.

## Diffuse-bank substitution

For Q_m=Y_1^2+Y_2^2-Y_3^2 with Y_a=m^{-1/2}sum_{r=1}^m X_{a,r}, the three frame columns are orthonormal, G=I_3 and each row leverage is c=1/m. Hence k selected equal-mass theta factors give

||dnu/ds||_infinity
<=12(2/sqrt(m))^{-2k/(3m)}theta^{k(1-2/(3m))}.

The full matrix spectrum is {1,1,-1,0,...,0}; this is an exact owner-target family.

## Partner obstruction check

The newest fleet03/B15 result gives q_*=0.7899085945560627... as the largest possible unit-interval mass under the fixed inverse-scale Gaussian-mixture budget. Since Uniform[0,1] gives that interval mass one,

d_TV>=1-q_*=0.2100914054439373... .

For probability densities, ||f-g||_1=2d_TV, hence the L1 gap is at least

0.4201828108878746... .

So fixed-budget Gaussian-mixture approximation cannot make the input perturbation tend to zero; this is only a proof-route obstruction, not a QFORM counterexample.

## Ruled rough-input bridge check

The source one-sheet theorem is used only where its affine-range hypothesis is met. In an ambient conditional application with an invertible active physical block B, the affine term lies in Range(B) automatically and square completion is an original-coordinate translation. Original-coordinate mollification preserves independence and the cap and converges in product L1 by telescoping. Restriction to the fixed sheet event and deterministic pushforward contract total variation, so interval domination passes with no loss. Output continuity is not used to obtain the height.

Verdict: no hidden moment, support, log-concavity, diagonal-basis, or post-rotation-independence assumption was introduced. Full QFORM remains open.
