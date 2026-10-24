SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T17:52:42.882125912Z.
attacking: repair the invalid interval-to-Borel frozen-slice receiver by identifying the exact Borel concentration currency, then test whether the newest partner half-Riesz trace supplies it.

# Early substantive checkpoint — Borel-Frostman hub receiver

Full QFORM remains OPEN. The live correction says that an interval-only square-root estimate on a frozen slice cannot be used as a Borel-set profile for an arbitrary rough hub. The first unpaid implication is therefore to identify the exact replacement currency rather than reuse the invalid transfer.

Let X be independent of (L,Y), with density f_X<=1, and let a!=0. Disintegrate the joint law of (L,Y) as

  nu(dl,dy)=dl mu_l(dy),   m(l):=mu_l(R),   integral m(l) dl=1.

For 0<beta<=1 define the Borel concentration seminorm

  K_beta(l):=sup_{0<|E|<infinity} mu_l(E)/|E|^beta.

For Q=2aXL+Y, conditioning on L=l gives a scaled hub kernel h_{q,l}(y) of mass one and height

  H_l=(2|a l|)^(-1).

If K_beta(l)<=K uniformly, layer cake gives, for every q and l!=0,

  integral h_{q,l} dmu_l
   <= K H_l^(1-beta).

Indeed h/H_l is [0,1]-valued, integral h/H_l = 1/H_l, and

  integral h dmu_l
   = H_l integral_0^1 mu_l({h>H_l s}) ds
   <= K H_l integral_0^1 |{h>H_l s}|^beta ds
   <= K H_l (integral_0^1 |{h>H_l s}| ds)^beta
   = K H_l^(1-beta),

using concavity of x^beta. Trivially the same integral is <=m(l)H_l. Hence

  p_Q(q) <= integral min{ K(2|a l|)^(beta-1), m(l)/(2|a l|) } dl.      (1)

Split at |l|=R. The first term on |l|<R and the second outside give

  p_Q(q) <= (2^beta K/beta)|a|^(beta-1) R^beta + 1/(2|a|R).

Optimising at

  R^(beta+1) = [2^(beta+1) K |a|^beta]^(-1)

gives the dimension-free rough-law receiver

  ||p_Q||_infinity <= ((1+beta)/beta) K^(1/(beta+1)) |a|^(-1/(beta+1)).      (2)

At beta=1/2 this is

  ||p_Q||_infinity <= 3 K^(2/3)|a|^(-2/3).                                  (3)

No density or continuity of the frozen Y-slices is assumed; (2) is a direct Borel-measure statement and so is compatible with arbitrary fragmented rough inputs. It also shows exactly what the invalid interval argument was missing: not another interval constant, but control of the top arbitrary measurable set of each frozen slice.

The interval/Borel gap is real. Let

  E_N = union_{k=1}^N [3Nk,3Nk+1/N],

and let X,U have density 1_{E_N}. Then |E_N|=1 and every interval J of length h obeys

  |E_N intersect J| <= sqrt(h/N).

Let L be independent Uniform[1/N,1+1/N], and Y=-sqrt(2) L U. For every frozen l and every interval I,

  P(Y in I | L=l) <= 2^(-1/4)|I|^(1/2),

uniformly in N and l. But the Borel square-root seminorm of that same frozen law is at least

  K_{1/2}(l) >= 2^(-1/4) l^(-1/2),

by taking the entire scaled support, so at l=1/N it is >=2^(-1/4)sqrt(N). Correspondingly

  p_{sqrt(2)L(X-U)}(0) = 2^(-1/2) log(N+1),

so the interval-only receiver really fails logarithmically.

Newest designated partner account03/B05 r29 proves a strong half-Riesz trace in its low-Psi active-shear chamber. That still cannot be converted abstractly into the Borel currency above. For N>=2 let delta=N^(-2), D=16N^4 and

  g_N(y)=N 1_{ union_{k=1}^N [kD,kD+delta] }(y).

This is a probability density. For every t, the interval nearest t contributes at most 2sqrt(2) to

  integral |y-t|^(-1/2) g_N(y) dy,

and all other intervals together contribute <1/8; hence the half-Riesz potential is uniformly <3. Yet for the union E of all N intervals, |E|=1/N and mu_N(E)=1, so K_{1/2}(mu_N)>=sqrt(N). Therefore a bounded half-Riesz potential does not Borelise the slice. The partner trace must be coupled to the independent scalar banks before this maximal-set loss occurs.

This is a supporting theorem / obstruction, not a QFORM counterexample. Next: apply the pinned e5f Theorem H to a target-valid lift of the logarithmic interval/Borel witness, confirming that genuine third curvature repairs the output even though the frozen Borel seminorm diverges.

Sources consumed: current owner continuation and correction; pinned e5f RESULTS/FOURIER_ROUTE_REPORT/COUNTEREXAMPLE_SEARCH; account03/B05 r29 REPORT. Status: proof calculation supplied here, independent review pending; WITHOUT_VERIFIED_BRAIN.
