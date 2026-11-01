SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T15:28:33Z.
attacking: product-preserving regularity from an indefinite physical pair plus a disjoint square, extending the newest fleet04/B15 zero-self-coupling branch without rotating the independent coordinates.

# Early substantive checkpoint

Status: supporting derivation in progress; full QFORM remains open.

Let U,V be independent cap-one real variables and let F be an arbitrary affine perturbation of an invertible indefinite physical pair B. Write D=|det B| and kappa=sigma_min(B). The completed pair-log theorem gives, for every r>0, a decomposition p_F=p_far+p_near into nonnegative subprobability densities with

p_far(t) <= 2 sqrt(2)/r,

p_near(t) <= D^(-1/2) log_+(2r^2/(kappa |t-t0|)).

Therefore

||p_far||_3 <= (2sqrt(2)/r)^(2/3)=2 r^(-2/3),

while the exact logarithmic integral

int_{|x|<L} log(L/|x|)^3 dx = 2L Gamma(4)=12L,

with L=2r^2/kappa, yields

||p_near||_3 <= 24^(1/3) D^(-1/2) kappa^(-1/3) r^(2/3).

Optimizing in r gives

||p_F||_3 <= 4*3^(1/6) D^(-1/4) kappa^(-1/6).

If Z is an independent cap-one coordinate and S=gamma Z^2+2wZ with gamma !=0, fleet04/B15 supplies the square receiver bound ||p_S||_(3/2)<=2|gamma|^(-1/3). Hence, whenever the chosen original-coordinate 3x3 physical block is B direct_sum [gamma], conditioning on every outside coordinate leaves F and S independent and Young gives

||p_Q||_infinity <= 8*3^(1/6) D^(-1/4) kappa^(-1/6)|gamma|^(-1/3).

Moreover L^3 * L^(3/2) is contained in C_0, so this branch has a continuous density after averaging over the outside coordinates. The next step is to optimize the conjugate exponents and state the rough-law/outside-conditioning argument with all quantifiers. No claim is made that the bare three-large-eigenvalue hypothesis forces this block pattern.
