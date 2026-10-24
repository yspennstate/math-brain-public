# account02/B18 early calculation — projected private-square Lorentz lift

Run: `account02-B18-20260924T031145Z-auto11`.
Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: supporting calculation; full QFORM remains OPEN.

## First unpaid implication

The preceding account02/B18 funnel leaves, among other states, a retained low-cross-rank carrier. Account01/B18 has already paid exact rank-one cross when the complement-active source plane has dimension at most two, and a definite two-plane subfamily. The still-useful source-separated endpoint is therefore: replace account03/B18 auto17's *single original-coordinate* private square by a delocalized linear projection of a whole disjoint ORIGINAL product bank, without ever asserting independence after a rotation.

## Calculation

Latest compatible partner account03/B18 auto17 proves that for disjoint original banks X,Y and

`R=X^T M Y + alpha^T X + G(Y)`, `sigma=||M||op>0`,

the density satisfies the Lorentz estimate

`||p_R||_{2,1}# <= 16/sqrt(sigma)`,

where `||f||_{2,1}#=int_0^infinity t^(-1/2) f*(t) dt`.

Let Z be a third disjoint original-coordinate product bank and `L=q^T Z`, `rho=||q||2>0`. Rudelson--Vershynin Theorem 1.2, applied literally to the ORIGINAL Z coordinates, gives

`||p_L||infinity <= sqrt(2)/rho`.

For `S=aL^2+dL` with `a!=0`, complete the square. If `K=||p_L||infinity`, its density g obeys

`g*(t) <= K / sqrt(|a| t)`.

Because the Z bank is disjoint from X,Y, S and R are genuinely independent. Hardy--Littlewood rearrangement then gives

`||(p_R*g)||infinity <= (K/sqrt(|a|)) ||p_R||_{2,1}#`

and hence

`boxed: ||p_(R+aL^2+dL+c)||infinity <= 16 sqrt(2)/(rho sqrt(|a| sigma)).`

The same approximation argument as in account03/B18 auto17 gives a continuous C0 density.

For a physical quadratic cross `2 X^T B Y`, use `M=2B`, so

`boxed: ||p_Q||infinity <= 16/(rho sqrt(|a| ||B||op))}`

whenever the remaining Z-dependence is exactly the displayed rank-one square/parallel linear term and the Y-side contribution is arbitrary.

## Exact rank-three target family

Let u,v,w be unit vectors supported on three disjoint ORIGINAL coordinate banks, and define

`Q_(a,b)=2 b (u^T X)(v^T Y)+a(w^T Z)^2`, `a,b>0`.

The physical matrix has exactly the nonzero eigenvalues `{a,b,-b}`. Thus for `a,b>=1` it is in the exact owner target. The new projected-square Lorentz lift gives

`||p_Q||infinity <=16 (ab)^(-1/2)`.

The earlier account02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, applied to the three independent projected scalars whose one-dimensional density caps are each at most sqrt(2), gives independently

`||p_Q||infinity <=3*2^(5/3) (a b^2)^(-1/3)`.

Therefore

`boxed: ||p_Q||infinity <= min{16(ab)^(-1/2), 3*2^(5/3)(ab^2)^(-1/3)}.`

The Lorentz branch is sharper when `a/b > (16/(3*2^(5/3)))^6 = 22.474622770919...`.

Pinned `e5f71d79...` Theorem C applies to the SAME family: signature `(2+,1-)`, positive eigenvalues `a,b`, negative magnitude `b`, hence for a.e. `t>=0`,

`p_Q(t) <= pi sqrt(2)`.

This pinned bound controls the one-sheet side uniformly; the new lift controls the whole line and decays in the anisotropic product `ab`.

No moments, support, log-concavity, iid, post-rotation independence, conditional-cap-as-independence, arbitrary-joint coarea, small-coefficient deletion, or fixed-good-minor assumption is used.
