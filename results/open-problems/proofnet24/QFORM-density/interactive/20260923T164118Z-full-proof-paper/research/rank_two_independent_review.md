# Independent check of the rank-two potential chapter

The completed paper_work/rank_two.tex and the revised exact-rank-two
concentration theorem in paper_work/structure.tex were independently
checked. No mathematical gap was found.

## Checks

- The rank-one Gaussian smoothing calculation gives the exact constant
  e^(3/4)Gamma(1/4), which is less than8. The manuscript's elementary
  degree-four Taylor bound for the gamma integral also proves that
  numerical inequality without a numerical quadrature assumption.
- The translated-square kernel bound5Psi(a) holds on both signs of a.
  For a>=1, the tail split is in the regime where the two-root
  sublevel estimate4/(sqrt(a)s^2) is valid.
- The averaging lemma uses
  sup_{s>=1}s^2 exp((1-s)/2)=16 exp(-3/2)<4.
  Integrating min(1,4L/s^2) gives exactly4sqrt(L).
- The diffuse rank-two half-potential Fourier coefficient is
  (2pi)^(-1/2). Integration of the1/t envelope gives
  4sqrt(2e) D^(-1/4).
- In the heavy-coordinate case, the Schur remainder retains arbitrary
  affine dependence on the other original coordinates. The rank-one
  coefficient of the scaled discriminant has modulus k^2 D/beta^2.
  All beta powers cancel, giving40*2^(3/4) D^(-1/4)<68 D^(-1/4).
- The zero-beta case has a nonzero affine slope almost surely.
  Two fractional-moment bounds give at most8 D^(-1/4).
- The conditional two-coordinate theorem uses only a marginal capH
  and conditional capK. Its weakL2 level estimate is less than
  15delta0^(-1/2), giving10sqrt15 sqrt(KH) D^(-1/4).
  The in-range reduction has K=h^(-1/2), H=sqrt2, h>1/2,
  hence10sqrt30 D^(-1/4).
- The rank-three Schur complement has an orthonormal two-frame
  W=V_-T and determinant detN=h detM/a. This gives the claimed
  68(h|a||detM|)^(-1/4) bound. The normalized simplification follows
  from |detM|>=||M|| and |a|<=h||M||.
- The revised exact-rank-two concentration proof has discriminant
  coefficient at least1/2 in modulus. Rank-one constant8 gives
  alpha2<=32sqrt2<46, including arbitrary affine terms.
  The diffuse branch's Fejer bound is smaller than28.

The last estimate is the input used in the exact definite rank-three
constant58 in paper_work/semidefinite.tex. Its heavy-pivot layer-cake
value at V=20 is57.53072879613092.

These checks concern the precise hypotheses stated in the manuscript.
They do not add an arbitrary indefinite high-rank theorem or resolve
the remaining structural problem.
