SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-22T21:56:30Z.
attacking: near-square-completion rank-two survivor: derive a dependence-safe fractional endpoint that uses a dominant square plus the small transverse eigenvalue without collapsing to the false cross-Frobenius scaling.

# account01/B03 r17 — logarithmic bridge for the definite near-square residual

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Classification: **ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.


## 1. Partner result actually applied

The designated partner is account02/B03. I read its complete r12 report at

`yspennstate/math-open-problems@c2bc78fc4f8e642f5d8c85fcc7d53956730b5cb1`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T211507Z-account02-B03-QFORM-r12/REPORT.md`.

That report proves that the naive arbitrary-self cross-Frobenius endpoint is false. For

`R_eta=[(X+Y)^2+eta(X-Y)^2]/(2eta)`, `X,Y~Unif[-1/2,1/2]`,

one has `s_2(S_eta)=1` and a cross coefficient `b_eta~(2eta)^(-1)`, but

`H_eta(0) sqrt(b_eta) ~ log(4/eta)`.

Thus one cannot hope for `H_(1/2)<=C |b|^(-1/2)` uniformly under arbitrary self curvature. The same partner report also source-pins the immediately preceding completed account02/B03 theorem

`QFORM-AMBIENT-PIVOT-FRACTIONAL-COLLISION-v1`, canonical
`yspennstate/math-open-problems@d205dc643b8d2439efdbbe986f93ea8b4f2933f5`,

which gives, for any full quadratic form having a nonzero original-coordinate diagonal `a`,

`E|Q-Q'|^(-1/2) <= C_* |a|^(-1/2)`,                         (1.1)

`C_*=16sqrt(2)/3^(3/4)=9.9264518304...`, and equivalently

`int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=sqrt(2pi) C_* |a|^(-1/2)
 <24.882 |a|^(-1/2)`.                                          (1.2)

This is the dependence-safe independent-copy time integral used below.

## 2. New theorem: definite two-coordinate logarithmic endpoint

### Theorem 2.1 — `QFORM-DEFINITE-PAIR-LOG-HALF-RIESZ-v1`

Let `X,Y` be independent real random variables with densities bounded by one. Let

`P=[[a,b],[b,c]]`

be positive or negative definite, let `D=det P>0`, and put

`m=max{|a|,|c|}`.

For arbitrary affine coefficients `ell in R^2`, `q0 in R`, define

`R=(X,Y)^T P (X,Y)+ell^T(X,Y)+q0`.

Set

`A0=2sqrt(2)m^(-1/2)`,
`B0=2pi D^(-1/2)`,
`rho=B0/A0^2=pi m/(4sqrt(D))`.

Then for every `t in R` and `epsilon>0`,

`P(|R-t|<=epsilon)<=min{1,A0 sqrt(epsilon),B0 epsilon}`.        (2.1)

Consequently

`H_(1/2)(R):=sup_t E|R-t|^(-1/2)` obeys

`boxed{
H_(1/2)(R)
 <= A0[2+log rho],                 if rho>=1,
 <= 2sqrt(B0)=2sqrt(2pi)D^(-1/4), if rho<=1.
}`                                                                  (2.2)

In particular, in the nearly rank-one definite regime `rho>=1`,

`boxed{
H_(1/2)(R)
 <=2sqrt(2)m^(-1/2)
   [2+log(pi m/(4sqrt(D)))].
}`                                                                  (2.3)

Thus determinant collapse costs only a logarithm once a dominant **physical square** is retained.

### Proof of the square-root small-ball term

After permuting `X,Y`, assume `m=|a|`. Conditional on `Y=y`, complete the square in the original coordinate `X`:

`R=a(X-h_y)^2+s_y`,

where `h_y,s_y` may depend arbitrarily on `y` and on the affine coefficients. For any real `u`, the set

`{x: |a(x-h_y)^2-u|<=epsilon}`

has total length at most `2sqrt(2epsilon/|a|)`. Indeed, after scaling to `a=1`, if `u<=epsilon` the set is contained in `[-sqrt(u+epsilon),sqrt(u+epsilon)]`, and if `u>epsilon` its two components have total length

`2[sqrt(u+epsilon)-sqrt(u-epsilon)]<=2sqrt(2epsilon)`.

Since the conditional density of `X` is its original cap-one density, uniformly in `y`,

`P(|R-t|<=epsilon | Y=y)<=2sqrt(2epsilon/m)`.

Average in `y` to obtain the `A0 sqrt(epsilon)` term in (2.1). This uses only original-coordinate independence.

### Proof of the linear small-ball term

Because `P` is definite, completing the full two-dimensional square gives

`R=(z-z0)^T P(z-z0)+c0`

for some deterministic `z0,c0` (after reflection if `P` is negative definite). The joint density of `(X,Y)` is at most one. For the positive definite quadratic `q(z)=z^T Pz`,

`Leb{z:q(z)<=s}=pi s/sqrt(D)`, `s>=0`.

Therefore the Lebesgue measure of the preimage of any value interval of length `2epsilon` is at most

`2pi epsilon/sqrt(D)`.

The probability is no larger, proving the `B0 epsilon` term of (2.1). The affine shift does not change the cap or the shell volume.

### Layer-cake synthesis

For `Z=|R-t|`,

`E Z^(-1/2)
 =(1/2) int_0^infinity P(Z<=epsilon) epsilon^(-3/2) d epsilon`.    (2.4)

If `rho=B0/A0^2>=1`, the linear and square-root bounds cross at

`epsilon_0=(A0/B0)^2`,

while `A0 sqrt(epsilon)=1` at `epsilon_1=A0^(-2)`, and `epsilon_0<=epsilon_1`. Splitting (2.4) at these two scales gives exactly

`A0 + A0 log rho + A0=A0(2+log rho)`.

If `rho<=1`, using only `min{1,B0 epsilon}` in (2.4) gives `2sqrt(B0)`. This proves (2.2).

## 3. Decoupled-time interpretation using the named partner theorem

Apply account02/B03's completed collision theorem (1.1) to this same definite pair, choosing the original coordinate whose diagonal magnitude is `m`. Then

`boxed{
int_R |t|^(-1/2)|phi_R(t)|^2dt
 <=sqrt(2pi) C_* m^(-1/2)
 <24.882 m^(-1/2).
}`                                                                  (3.1)

At the same time, Theorem 2.1 gives in the near-square regime

`boxed{
H_(1/2)(R)
 <=2sqrt(2)m^(-1/2)
 [2+log(pi m/(4sqrt(D)))].
}`                                                                  (3.2)

Thus, **under definiteness**, the critical one-copy endpoint differs from the dependence-safe independent-copy time scale by at most a logarithm of the physical condition parameter `m/sqrt(D)`. This is precisely the loss that the partner's r12 counterexample shows cannot in general be removed.

The partner family gives an asymptotically sharp test. There

`m=(1+eta)/(2eta)`, `D=1/eta`,
`rho=pi(1+eta)/(8sqrt(eta))`,

so for small `eta`

`H_eta(0)
 <=4 sqrt(eta/(1+eta))
   [2+log(pi(1+eta)/(8sqrt(eta)))].`                              (3.3)

The partner's exact formula has

`H_eta(0) sqrt(m) ~ log(1/eta)`,

while (3.3) has the same logarithmic order. Hence the logarithm in the bridge is structurally genuine, not an artifact of a power-loss estimate.

Representative values:

`eta=1e-2`: theorem upper bound `1.34442410846`, exact partner value `0.871914127672`.

`eta=1e-4`: theorem upper bound `0.226811000740`, exact `0.150135084063`.

`eta=1e-8`: theorem upper bound `0.004110251470`, exact `0.002801157553`.

The ratio tends toward a constant (numerically about `sqrt(2)` at very small eta), consistent with matching logarithmic order.

## 4. Ambient three-coordinate corollary

Condition on every original coordinate except three `Z,X,Y`, and complete the genuine physical square in `Z`:

`Q=d(Z+h(X,Y,w))^2+R_w(X,Y)`, `d!=0`.

Suppose the quadratic coefficient matrix `P` of `R_w` in the still-independent original pair `(X,Y)` is definite. (The outside conditioning changes only affine terms, so `P`, `D`, and `m` are independent of `w`.) The one-square density envelope gives

`||p_(Q|w)||_infinity
 <=|d|^(-1/2) H_(1/2)(R_w)`.

Theorem 2.1 is uniform in the affine terms generated by `w`; averaging in `w` therefore yields

`boxed{
||p_Q||_infinity
 <=|d|^(-1/2) A0[2+log rho], if rho>=1,
 <=2sqrt(2pi)|d|^(-1/2)D^(-1/4), if rho<=1.
}`                                                                  (4.1)

This proves absolute continuity and an essential density bound in this entire physical-pivot + definite-Schur-pair branch. Continuity is **not** claimed here.

Compared with the generic orientation-free rank-two half-Riesz payment `128 D^(-1/4)`, (4.1) is substantially stronger in the near-square definite regime `D<<m^2`: the reciprocal determinant power is replaced by a logarithm.

## 5. What this pays and what remains open

This run directly answers the latest account02/B03 obstruction in the **definite** near-square-completion regime. The partner proved that collision/Frobenius scale alone cannot pay the one-copy endpoint; the new theorem identifies and proves the sharp repair: retain a physical square and pay only `log(m/sqrt(D))` for the transverse curvature.

It does not solve the full QFORM conjecture. In particular:

1. an indefinite near-square physical pair has no finite two-dimensional Lebesgue shell-density cap, so the linear small-ball half of this proof is unavailable there;
2. the bare hypothesis `s_3(A)>=1` does not itself force a uniformly favorable physical pivot/definite Schur pair;
3. the near-rank-two higher-dimensional tail cannot be discarded by a moment perturbation.

The first B03 unpaid implication is therefore narrower: in the surviving strong near-rank-two state, either (a) expose a definite physical Schur pair and use (4.1), or (b) for the indefinite/entangled survivor construct a grouped product-preserving replacement for the missing `B0 epsilon` small-ball estimate. The fresh account01/B06 vertex-cover smoother and account03/B08 near-rank-two compression are compatible possible structural inputs, but no exhaustive reduction is claimed here.

## 6. Status

- `QFORM-DEFINITE-PAIR-LOG-HALF-RIESZ-v1`: **PROVED**.
- dependence-safe independent-copy time integral (3.1): **APPLIED FROM account02/B03** to the same branch.
- logarithmic loss: **NECESSARY IN ORDER** by the partner's exact normalized adversary.
- ambient physical-pivot + definite-Schur-pair density branch: **PROVED ESSENTIALLY BOUNDED**.
- continuity in this branch: **NOT PROVED**.
- full QFORM universal theorem: **OPEN**.
