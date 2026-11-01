# Single-hub endpoint: new window recovery estimate and research status

## Scope and source snapshot

Read-only source review and new derivations use `yspennstate/math-open-problems`, snapshot `20c8f358318f0753d3fbe1f59c04b8391c1bcb92` (2026-09-23 16:39:36 UTC), especially:

- `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`, blob `9ac295d0c2100aafe64cbc9f913385140de68fbd`;
- that directory's numerical README;
- sibling `degenerate_hub/REPORT.md` and `counterexample_search/REPORT.md`;
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

The latest single-hub source contains the conditional-hub sufficient statement (SP). The previous monotonicity conjecture (M) was removed by commit `c4c23b784395630c094ba299a50712209921d1ae`. The new text slightly expands the numerical qualifications but does not prove SP.

## New proved refinement: recovery from one symmetric window

Let a real random variable Z have characteristic function phi satisfying

    |phi(t)| <= B |t|^(-3/2), t != 0.

Then Z has a continuous bounded density p. For every h > 0,

    ||p||_infinity <= sup_s P(|Z-s| <= h)/(2h)
                     + [2 sqrt(2 pi)/(3 pi)] B sqrt(h).

### Complete proof

The bound `min(1,B|t|^(-3/2))` is integrable. Fourier inversion therefore gives a continuous density. Let `U_h(x)=1_{[-h,h]}(x)/(2h)`. Its Fourier transform is `sinc(ht)=sin(ht)/(ht)`. Since `sinc(u)<=1` for every real u,

    |p(s) - (p*U_h)(s)|
      <= (1/(2 pi)) int_R |phi(t)| (1-sinc(ht)) dt
      <= (B sqrt(h)/pi) int_0^infinity u^(-3/2)(1-sinc(u)) du.

Use `sinc(u)=int_0^1 cos(vu) dv`; Tonelli applies because `1-cos(vu)>=0`. For a >= 0,

    int_0^infinity u^(-3/2)(1-cos(au)) du = sqrt(2 pi) sqrt(a).

One elementary derivation integrates by parts, reducing the a=1 case to `2 int_0^infinity u^(-1/2) sin(u) du=sqrt(2 pi)`, with an exponential damping and its limit if desired. Consequently,

    int_0^infinity u^(-3/2)(1-sinc(u)) du
       = sqrt(2 pi) int_0^1 sqrt(v) dv = (2/3)sqrt(2 pi).

Finally `(p*U_h)(s)=P(|Z-s|<=h)/(2h)`. This proves the claim.

## Application to the leaking hub

Let X_0,X_1,...,X_m be independent with densities <=1; let w,v,e be orthonormal with `w_i^2+v_i^2+e_i^2<=1/2`. Put `L=w.X`, `V=v.X`, `P=e.X`. The form is

    Q = a X_0^2 + 2 X_0(L+beta) + lambda V^2
          + 2L(q_w L+q_v V+eps P) + sum_i phi_i(X_i),

where eps>0 and each phi_i is a real quadratic. Proposition 2.3's proof gives the exact characteristic-function constant

    |phi_Q(t)| <= 4 sqrt(2) pi^(3/2) (eps |lambda|)^(-1/2) |t|^(-3/2).

For a=0, the frozen-slice theorem gives

    P(|Q-s|<=delta)/(2delta) <= A_delta,
    A_delta = 1/2+2sqrt(2)+sqrt(2)log_+(2 B_delta^2),
    B_delta = [4+sqrt(4/pi+32log_+(|lambda|/delta))]/(2sqrt(|lambda|)).

Therefore, for **every** h>0,

    ||p_Q||_infinity <= A_h + (16 pi/3) sqrt(h/(eps |lambda|)).

Taking h=eps yields

    ||p_Q||_infinity <= 1/2+2sqrt(2)
      +sqrt(2)log_+(2 B_eps^2)+16pi/(3sqrt(|lambda|)).

This improves the existing report's `5.41 A_eps + 40.1/sqrt(|lambda|)` to `A_eps + 16.756/sqrt(|lambda|)`. It is a rigorous improvement of the constants and gives a one-parameter optimization in h. It does **not** remove the double logarithm or solve the uniform endpoint. Choosing `h/eps` of order `1/log(1/eps)^2` can reduce the additive recovery term while changing the leading double logarithm only by a lower-order amount.

## Further exact evaluation: large transverse coefficient in the pure hub

For `Q=2X_0(L+beta)+lambda(V-v_c(L))^2+F_c(L)` with orthonormal w,v, the water-filling argument in Proposition S can be evaluated also in its large-|lambda| branch. Writing mu=|lambda|,

    ||p_Q||_infinity <=
      2sqrt(2)+sqrt(2)log(1/3+4sqrt(2)/mu),  0<mu<=6sqrt(2),
      (192/mu)^(1/3),                       mu>=6sqrt(2).

The previous report replaced the second expression by the constant `2sqrt(2)`. Indeed the envelope for the effective partner mass is

    M(t)=min(sqrt(2),4sqrt(2)mu^(-1/2)sqrt(|t|)).

Its mass inside `|t|<=mu/16` is `sqrt(2)mu/12`. If this is >=1, the bathtub selects `|t|<=tau`, where

    tau=[3sqrt(mu)/(16sqrt(2))]^(2/3),

and integrates `M(t)/(2|t|)` to `(192/mu)^(1/3)`. This is an explicit evaluation of the same argument, not a new solution of the entangled problem.

## Creative endpoint work in progress

The following approaches were considered and do not yet yield a uniform theorem:

1. Weak-L2 control of frozen slices would immediately imply a Borel-set square-root profile and close the zero-diagonal hub. The available `|mu_hat(t)|<=C|t|^(-1/2)` is an endpoint Fourier estimate and does not imply weak-L2 by a valid general Hausdorff--Young endpoint theorem. Taking its truncated L2 norm is precisely the source of the logarithm.
2. Conditioning on P in SP permits hub roots to adapt to P. Pointwise bounded 1D/2D/3D projection densities do not control the resulting adapted supremum; the product-projection structure must enter more deeply. An independent subtask explores constructions and a conditional geometric proof.
3. Smoothing the hub alone requires control of unbounded partner values and does not preserve a useful error uniformly over rough product laws. Symmetric-window recovery above works after nonzero-leakage integrability is known, but cannot create uniformity from that alone.
4. In rank-three geometry the positive side of the indefinite form admits straight-line rulings; the difficult two-sheet side requires a curved-section inequality. A direct contraction from a curved sheet to the cone would require monotonicity or regularity of the projected density absent from cap-one product laws.

## Claims gate

- Proved here: symmetric-window recovery; its improved leaking-hub constant; exact large-mu evaluation of the pure-hub bathtub.
- Existing proved results re-derived for the paper: frozen-slice bound, interval-hub bound, nonzero leakage Fourier estimate, delta log log small balls, selected multihub and localized-block estimates.
- Open: a constant uniform as eps->0 for entangled rough laws, (SP), general orthogonal-twist control, and hub-diagonal/structural interpolation needed for the unrestricted theorem.
- No counterexample to the original three-eigenvalue conjecture is claimed.

## Further proved progress: uniformity for Gaussian scale-mixture light laws

The independent conditional-hub attack produced a new uniform subclass theorem, with full derivations in `adapted_attack.md` and professional proofs in `../paper_work/hubs.tex`.

Let `X_i=M_i+sqrt(T_i)G_i`, with pairs `(M_i,T_i)` independent across coordinates and standard independent Gaussian `G_i`. Assume `E T_i^(-1/2)<=sqrt(2pi)`. For an orthonormal spread triple `(w,v,p)` (coordinate leverage at most one half), and a hub `Y` with conditional density `g(y|P)<=1`, `P=p.X`, the form

    2Y L + lambda V^2 + B(Y,P)V + C(Y,P), |lambda|>=1,

has a universal bounded density. In particular `aH²+2H(L+beta)+lambda V²+2eps LP` is bounded uniformly in **all** `eps` and `a` for this class, by setting `Y=H+eps P`.

The component-moment condition is exactly the marginal cap-one condition for centered Gaussian scale mixtures (deterministic `M_i`). It allows component variances tending arbitrarily close to zero. The proof does not cover arbitrary mixtures whose density cap comes from spatially separating narrow components, and it does not handle arbitrary light diagonals or every aligned L²/LV term.

The proof has three ingredients:

1. Conditional Gaussian integration gives a bound `4(2pi)^(-3/4) lambda_min(M)^(-3/4)` in the projected covariance M, with an arbitrary cap-one conditional hub kernel. A fixed covariance floor `(2pi)^(-1) I` gives the explicit constant 3.
2. A fixed-dimension Parseval frame with all vector squared norms at most one half splits into two covariance matrices bounded below by `eta_d I`, with `eta_d>0` independent of the number of vectors. The proof combines finite matroid base packing with compactness of sorted atoms and a random split of the diffuse tail. It supplies a nonexplicit constant, not an unproved quantitative bound.
3. Matrix resolvent compression controls each block's expected inverse half moment by `3sqrt(2pi)/sqrt(eta_3)`. Independence of the blocks upgrades their sum to an integrable inverse three-quarter moment. The resulting constant is `4*2^(-3/4)*3^(3/2)*eta_3^(-3/4)`.

Independent translated Laplace inputs admit the explicit bound `12 pi^(-3/4) Gamma(1/4)<19`, without a spread assumption. An abstract nonproduct construction also proves that joint and coordinate-marginal density caps alone cannot establish SP: an auxiliary P encoding fine LV cells permits a cap-one adapted hub with a density growing at least `(1/4)log m-O(1)`. It is explicitly **not** a counterexample to SP for independent-product projections.

The conditional Gaussian, frame partition and mixture arguments were independently re-derived by two additional readers before being inserted into the manuscript. The conditional hub is realized using fresh randomness after X so its kernel remains valid after conditioning on the latent mixture variables. The unrestricted conjecture remains open.

## Further proved refinement: a scalar SQ constant of 2^(7/4)

For any density f<=1 of mass one, put p(x)=s-a*x^2-2*t*x and Delta=t^2+a*s. If Delta is nonzero, then

    integral f(x)/sqrt(|p(x)|) dx <= 2^(7/4) |Delta|^(-1/4).

This replaces the source constant 9.05 by approximately 3.363586. The proof is elementary and was independently re-derived by the project lead.

For a nonzero, let A=|a|, d=|Delta|, and z=A(x+t/a)/sqrt(d). The sublevel |p|<u becomes |z^2-sign(Delta)|<r with r=Au/d. For positive Delta the z-length is exactly

    2(sqrt(1+r)-sqrt(max(0,1-r))) <= 2sqrt(2)*r.

For negative Delta its length is 2sqrt(max(0,r-1))<=r. Returning to x gives sublevel length at most 2sqrt(2)*u/sqrt(d). Layer cake now bounds the integral by

    integral_0^infinity min(1,2sqrt(2)/(v^2 sqrt(d))) dv
       = 2^(7/4) d^(-1/4).

For a=0, the exact sublevel length u/|t| gives the sharper 2|t|^(-1/2).

Under the joint square-root domination (SQ) for the hub partner t and remainder R with random center C, the existing root-splitting argument consequently improves to

    p_Q(s) <= 1+2^(7/4) K E|t^2+a(s-C)|^(-1/4).

When C=sigma_c*t^2+eta_1*t+eta_0+C' and the conditional t-density given C' is at most D, factor the resulting quadratic discriminant and use the bathtub bound E|t-r|^(-1/2)<=2sqrt(2D). This gives

    ||p_Q||_infinity <= 1+2^(13/4) K sqrt(D) |1-a*sigma_c|^(-1/4).

The coefficient 2^(13/4)=9.513657 replaces 25.6 in the source. Complete statements and proofs, including a separate logarithmic estimate at the degenerate center and the independent-square corollary, are in the final hub chapter. The existence of the joint SQ domination in the general rough entangled problem is still unproved.

## Final consolidation: shell collisions and zero-diagonal Strichartz

The manuscript now also gives full proofs of the shell-collision bound 8/|lambda|*log(K/r), the resulting sqrt(log K) support dependence, the conditional weighted-collision (VD) implication, the elementary parabola L6 estimate, and the degenerate-hub Strichartz argument including uniformity through zero partner curvature.

For the support theorem, the source's informal statement that a chosen profile can be made concave is replaced by the explicit increasing concave majorant

    C/sqrt(|lambda|) * sqrt(x log(e+(1+K^2|lambda|)/x)).

For Strichartz, a symmetric-window comparison gives an explicit scale-joining constant without introducing an unspecified Schwartz kernel. If B0 is the dyadic bound coefficient and h=|sigma|, summing the multiplier 1-sinc(ht) on blocks T=2^j/h bounds the recovery error by

    (B0*h^(1/6)/pi) *
       [2/(1-2^(-1/6))+2/(3*(2^(11/6)-1))].

For zero hub diagonal, the |sigma| factor cancels. The exact remaining universal multiplier is approximately 99.388070, and the known normalized degenerate-hub density bound is 17.980066<18. These are complete positive subclasses; VD remains a stated conditional hypothesis, and the nonzero-hub-diagonal small-curvature corner remains open.
