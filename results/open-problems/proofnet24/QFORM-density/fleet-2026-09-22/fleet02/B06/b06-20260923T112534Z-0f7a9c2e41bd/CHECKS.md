# Deterministic checks for fleet02/B06 b06-20260923T112534Z-0f7a9c2e41bd

These are arithmetic/algebra sanity checks, not proof certificates.

## Constants

With

`gamma_star=1/(16sqrt(2))`, `eta_star=1/128`, `m=191`,

`c_area=gamma_star eta_star / sqrt(binomial(m,2))`

we get

`c_area = 2.563164996691298e-6`.

The ruled determinant constant

`C_R=(2/sqrt(3)) B(1/3,1/3)`

is

`C_R = 6.119816148228773`.

Thus

`C_R c_area^(-1/3) = 447.1770645262903 < 448`.

For the shared-bank scalar/dependent-pair theorem with a physical scalar (`L_X=1`) and an orthonormal two-dimensional product projection (`M<=e`), the universal coefficient is

`3 (8sqrt(2)e)^(2/3) = 29.44789341505909`.

For the disjoint-square subbranch, partner fleet03/B06 r34 with `L_U,L_V<=sqrt(e)` and `L_X=1` gives two-sheet coefficient

`4sqrt(2)e^(3/4) = 11.97556054015085`.

Newest-Claude Theorem C gives the complementary ruled-side coefficient

`pi sqrt(2) = 4.442882938158366`.

## Exact target spectrum

For every `eta>=0`,

`B_eta=[[-eta,sqrt(1+eta),0],[sqrt(1+eta),0,0],[0,0,1]]`.

The characteristic polynomial of the upper 2-by-2 block is

`lambda^2 + eta lambda -(1+eta) = (lambda-1)(lambda+1+eta)`.

Hence the three nonzero eigenvalues are exactly

`{1,-(1+eta),1}`.

If `X` is one original scalar and `U=u.Z`, `V=v.Z` with `u,v` orthonormal coefficient vectors in a disjoint product bank, the physical coefficient frame `(e_X,u,v)` is orthonormal even though `U,V` need not be independent. Therefore the ambient physical matrix has exactly this nonzero spectrum.

## Superlevel-area constant in the new proof

For `h>0`, `beta>0`, `c in R`,

`I(c,h)=int_{|c-beta v^2|<h} |c-beta v^2| dv`.

After `v=sqrt(h/beta) w`,

`I(c,h)=h^(3/2) beta^(-1/2) J(c/h)`

with

`J(q)=int_{|q-w^2|<1}|q-w^2|dw`.

The integrand is `<1`; the supporting set has length at most `2sqrt(2)` (for `-1<q<1` it is contained in `[-sqrt(q+1),sqrt(q+1)]`, and for `q>=1` its length is `2(sqrt(q+1)-sqrt(q-1))<=2sqrt(2)`). Hence

`I(c,h)<=2sqrt(2) beta^(-1/2) h^(3/2)`.

This is the sole numerical constant used in the weak-L^(3/2) kernel estimate.
