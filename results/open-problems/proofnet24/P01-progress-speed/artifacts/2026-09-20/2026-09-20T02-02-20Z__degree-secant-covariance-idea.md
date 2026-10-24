# P01 T06 idea before code — conditional-degree secants for the derivative covariance

Controlling directive: `operations/PROGRESS20_2026-09-20.md`. P01 is the analytic regeneration/derivative worker for T06; live companion is NM13-05. The old Baum--Connes work remains under `proofnet24/P01-baum-connes` and is not probability progress.

## Frozen convention

At a vertex with `k` children the parent edge has weight `lambda` and each child edge weight `1`, so

`P(parent|k)=lambda/(lambda+k)`, `P(each child|k)=1/(lambda+k)`.

The original child-bias parameter is `beta=1/lambda`.

## Starting identity inherited from P01

For bounded offspring `d<=N<=D`, let `B_0,...,B_N` be iid escape variables, `U_i=-B_i'`,

`S=sum B_i`, `U=sum U_i`, `A=lambda-1+S`, `u=S/((N+1)A)`.

Under the `u`-tilted law `mu`, with `r=E_mu N`,

`ell=(r-lambda)/(r+lambda)`,

`r'=-Cov_mu(N,q)=r E_mu q-E_mu[Nq]`,

where

`q=(S+(lambda-1)U)/(S A)`.

The preceding P01 run used one global interval for `q` and obtained `2<=N<=74` through `lambda=6/5`.

## New input from the complementary R02/PROB10-06 route

`runs/prob10_2026-09-20/PROB10-06/20260920T0132Z_escape_elasticity_cone_bridge_7d4a2c91.md` proves for `d<=N<=D` and `1<=lambda<d` the pathwise logarithmic escape cone

`1/(D-lambda) <= U_i/B_i <= 1/(d-lambda)`.

The upper inequality is the He--Wang--Xiang bound; the new lower inequality is saturated by the deterministic `D`-regular tree. I will consume this lemma, not claim it.

## New route

Specialize first to `d=2`. Since `U/S` is a `B_i`-weighted average of `U_i/B_i`,

`(D-1)/(D-lambda) <= [S+(lambda-1)U]/S <= 1/(2-lambda)`.

Conditional on `N=n`, the escape bounds `1-lambda/2 <= B_i <= 1-lambda/D` give

`A^-_n = n-lambda(n-1)/2 <= A <= A^+_n = n+lambda(D-n-1)/D`.

Hence, pathwise on `{N=n}`,

`a_n(lambda) <= q <= b_n(lambda)`,

with

`a_n(lambda)=(D-1)/[(D-lambda) A^+_n]`,

`b_n(lambda)=1/[(2-lambda) A^-_n]`.

Write `g_n(lambda)=n a_n(lambda)`. For fixed `lambda`, as functions of real `x in [2,D]`,

- `b_lambda(x)` is decreasing convex (`const/(alpha x+beta)`),
- `g_lambda(x)` is increasing concave (`const*x/(alpha x+beta)`).

Therefore if `r=E_mu N`,

`E_mu[b_N] <= Sec[b_lambda](r)`,

`E_mu[g_N] >= Sec[g_lambda](r)`,

where `Sec` is the chord through the endpoint values at `2,D`. Thus

`r' <= r Sec[b_lambda](r)-Sec[g_lambda](r)`.

For a whole rectangle `1<=lambda<=L`, use the monotone endpoint envelopes

`b_lambda(n)<=b_L(n)`,

`g_lambda(2)>=g_L(2)` (for the concrete D below),

`g_lambda(D)>=g_1(D)`.

Let `B*(r)` be the chord through `(2,b_L(2)),(D,b_L(D))`, and `G*(r)` the chord through `(2,g_L(2)),(D,g_1(D))`. Then

`r' <= H(r):=r B*(r)-G*(r)`.

If `H(r)<0`, then `lambda r'-r<0` immediately. If `H(r)>=0`, then `lambda<=L` gives

`lambda r'-r <= L H(r)-r =: Psi(r)`.

Because `B*` is affine with negative slope and `G*` is affine, `Psi` is a concave quadratic. Its exact maximum on `[2,D]` is therefore elementary. This keeps the common tilted mean instead of paying the previous global range-width product.

### Target 1

Test `D=580, L=6/5`. Preliminary exact algebra gives `max Psi < -1/3000`, whereas `D=581` fails this certificate. If confirmed, this expands the arbitrary-support breadth `74 -> 580` at the same parent-bias endpoint and yields the clean derivative margin

`ell' <= -1/506690160` on `1<=lambda<=6/5`.

### Target 2

Test a deeper arbitrary-support rectangle `D=75, L=31/25`. Preliminary exact algebra gives `max Psi < -7/100`, implying

`ell' <= -175/7265672` on `1<=lambda<=31/25`.

### Target 3: nonadjacent two-point extension

For `P(N=2)=1-p`, `P(N=D)=p`, the tilted mean is `r=2+(D-2)theta` and

`r'=(D-2) theta(1-theta)(m_2-m_D)`.

Using the same conditional envelopes uniformly on `[1,L]`,

`m_2-m_D <= b_2(L)-a_D(1)=:Delta*`.

Set `K=L(D-2)Delta*`. Then

`lambda r'-r <= K theta(1-theta)-2-(D-2)theta`.

The right side is an explicit concave quadratic. For `D=13,L=3/2`, preliminary exact arithmetic gives maximum `<-3/200`, so all mixture weights should satisfy

`ell' <= -3/21025` on `1<=lambda<=3/2`.

This is complementary to the existing `{2,3}` workers: it is an all-mixture nonadjacent `{2,13}` theorem, not a rare-defect or adjacent-support estimate.

No simulation is evidence. The next step is an exact rational checker for the three claims, the method boundaries `D=581` and `{2,14}` at the chosen endpoints, and the secant inequalities.