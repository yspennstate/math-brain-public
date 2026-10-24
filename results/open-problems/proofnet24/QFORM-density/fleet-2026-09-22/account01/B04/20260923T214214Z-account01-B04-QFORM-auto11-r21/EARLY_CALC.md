SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T21:42:14Z.
attacking: average the exact indefinite-pair logarithmic envelope against a genuinely bounded clean-bank Schur-remainder density, and optimize the scale exactly.

# Early substantive calculation

Let an original-coordinate physical pair have invertible indefinite block B, with D=|det B| and kappa=sigma_min(B). The proved pair-log theorem gives, after completing the pair and writing the scalar Schur remainder as R,

p_Q(t) <= 2 sqrt(2)/r + D^(-1/2) E log_+(2 r^2/(kappa |t-R|))                       (1)

for every r>0. Suppose now R itself has an essentially bounded density, ||p_R||_infinity<=K. Then

P(|R-t|<rho) <= min(1,2K rho).

With a=2r^2/kappa and x=2Ka=4Kr^2/kappa, layer cake gives exactly

E log_+(a/|t-R|)
 <= int_0^infinity min(1,x e^(-v)) dv
 = F(x),

where F(x)=x for 0<x<=1 and F(x)=1+log x for x>=1. Hence

p_Q(t) <= A x^(-1/2)+B0 F(x),
A=4 sqrt(2K/kappa),  B0=D^(-1/2).                                      (2)

The one-variable minimization is explicit.

If A<=2B0, equivalently 8KD/kappa<=1, the minimizer is x=(A/(2B0))^(2/3)<=1 and

||p_Q||_infinity <= 6 D^(-1/6)(K/kappa)^(1/3).                         (3)

If A>=2B0, equivalently 8KD/kappa>=1, the minimizer is x=(A/(2B0))^2=8KD/kappa and

||p_Q||_infinity <= D^(-1/2)[3+log(8KD/kappa)].                        (4)

The two formulas agree at 8KD/kappa=1. Under A -> cA, one has D -> c^2D, kappa -> |c|kappa and K -> K/|c| for a Schur remainder scaled with A, so both branches scale as |c|^(-1), as a density bound must.

This converts a completed bounded-density receiver for the Schur remainder into a rank-free indefinite-pair receiver without requiring any square-root small-ball loss.
