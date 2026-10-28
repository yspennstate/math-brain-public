SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-24T09:15:14Z.
attacking: the genuinely overlapping projected-square/rank-two packet — prove a one-copy density bound for a dependent same-bank pair (S,T) coupled hyperbolically to one independent scalar, then convert it to the assigned whole-copy time integral without conditional-cap shortcuts.

# account03/B03 r51 — same-bank pair + independent hyperbolic scalar

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING DENSITY/TIME THEOREM; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN.**
Execution: `WITHOUT_VERIFIED_BRAIN`.


The immediate source target is account03/B16's fresh overlap frontier `QFORM-OVERLAPPING-PROJECTEDSQUARE-RANK2-PREABSOLUTE-v2`, canonical source

`yspennstate/math-open-problems@fb28047260afcaa64675fef64af6457e2815af2d`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260924T085813Z-account03-B16-QFORM-auto11-r3/REPORT.md`.

That frontier has a projected square scalar and a genuinely dependent transverse projection from the SAME original-coordinate product bank, with the remaining hyperbolic factor coming from a disjoint bank.

## 1. Main analytic theorem

### Theorem 1 — `QFORM-SAMEBANK-PAIR-HYPERBOLIC-SQUARE-v1`

Let `(S,R)` be an arbitrary real pair with a joint probability density `rho` satisfying

`||rho||_infinity <= M`.

Let `V` be independent of `(S,R)` with probability density `f_V` satisfying

`||f_V||_infinity <= N`.

Let `a,b` be nonzero real numbers. For arbitrary real translations `d,alpha,beta,c`, define

`Q = a(S+d)^2 + 2 b (R+alpha)(V+beta) + c`.

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_(infinity,ess)
 <= 6 M^(2/3) N^(2/3) |a|^(-1/3)|b|^(-2/3).
`

Equivalently,

`||p_Q||_(infinity,ess) <= 6 [M^2 N^2/(|a| |b|^2)]^(1/3)`.

The pair `(S,R)` may be arbitrarily dependent. No conditional density bound for `R|S` or `S|R` is assumed.

### Proof

Translations do not change the density caps, so write the translated variables again as `(S,R,V)` and suppress `c`. For `r!=0`, conditioning on `(S,R)=(s,r)` gives the conditional output density

`k_x(s,r)
 = [1/(2|b r|)] f_V((x-a s^2)/(2 b r))`

at target level `x`. Since `R` has an absolutely continuous marginal, the set `r=0` is null. Thus

`p_Q(x)=int_R int_R rho(s,r) k_x(s,r) ds dr`

for almost every `x`.

We use two bounds on the inner integral.

First,

`sup_s k_x(s,r) <= N/(2|b||r|)`.

Second, integrate in `s`. Under `u=a s^2`, the two inverse branches contribute total Jacobian

`du -> ds_total = |a|^(-1/2)|u|^(-1/2) du`

on the appropriate half-line. Dropping that half-line restriction and substituting `v=(x-u)/(2br)` gives

`int_R k_x(s,r) ds
 <= |a|^(-1/2) int_R f_V(v)|x-2brv|^(-1/2) dv.`

For every one-dimensional probability density `f<=N`, the decreasing-kernel bathtub bound is

`sup_y int f(v)|v-y|^(-1/2)dv <= 2 sqrt(2N)`.

Indeed the extremal cap-one rearrangement is `N 1_[y-1/(2N),y+1/(2N)]`, whose integral is exactly `2sqrt(2N)`. Scaling by `2br` therefore yields

`int_R k_x(s,r) ds
 <= 2 sqrt(N)/(sqrt(|ab|) sqrt(|r|)).`

Let `p_R(r)=int rho(s,r)ds`. Since `rho<=M`,

`F_x(r):=int rho(s,r)k_x(s,r)ds
 <= A |r|^(-1/2),`

where

`A=2M sqrt(N)/sqrt(|ab|)`.

Using instead the pointwise bound on `k_x`,

`F_x(r) <= B p_R(r)/|r|`,

where

`B=N/(2|b|)`.

For any cutoff `R0>0`,

`p_Q(x)
 <= int_(|r|<=R0) A|r|^(-1/2)dr
   + int_(|r|>R0) B p_R(r)/|r| dr
 <= 4A sqrt(R0) + B/R0`,

because `int p_R=1`. Optimize at

`R0=(B/(2A))^(2/3)`.

Then

`4A sqrt(R0)+B/R0
 =3*2^(2/3) A^(2/3)B^(1/3)
 =6 M^(2/3)N^(2/3)|a|^(-1/3)|b|^(-2/3).`

The bound is uniform in `x`, proving the theorem. QED.

### Why this is correction-safe

The logarithmic singularity of a bare product `2RV` is regularized here by the genuinely transverse square `aS^2` before any absolute-value integration. Near `r=0`, the square gives the integrable `|r|^(-1/2)` budget; away from `r=0`, probability normalization of the `R` marginal pays the `1/|r|` tail. We never condition `R` on `S` and never require `(S,R)` to be independent.

## 2. Product-bank specialization: the exact B16 overlap frontier

Let one original-coordinate product bank `X_K` produce two orthogonal projections

`S=r^T X_K`, `T=u^T X_K`,

with `r.u=0`, `rho0=||r||_2>0`, `sigma0=||u||_2>0`. Let a disjoint original-coordinate bank produce

`V=v^T X_J`, `tau0=||v||_2>0`.

Use the standard product-projection bounds already used in the fleet:

`||p_(S,T)||_infinity <= 2/(rho0 sigma0)`,

`||p_V||_infinity <= sqrt(2)/tau0`.

For arbitrary real `c0`, the linear shear

`R=T+c0 S`

has Jacobian one in `(S,T)`, so

`||p_(S,R)||_infinity <= 2/(rho0 sigma0)`.

Conditioning on any fourth disjoint source bank may add arbitrary measurable translations `d(W),alpha(W),beta(W),c(W)`; Theorem 1 is uniform in those translations, so averaging over `W` preserves the same bound.

Therefore every packet

`Q=a(S+d(W))^2
   +2b(T+c0 S+alpha(W))(V+beta(W))
   +c(W)`

with `ab!=0` satisfies

`boxed:
 ||p_Q||_(infinity,ess)
 <= 12 (rho0 sigma0 tau0)^(-2/3)
        |a|^(-1/3)|b|^(-2/3).
`

Equivalently,

`||p_Q||_(infinity,ess)
 <=12 [rho0^2 sigma0^2 tau0^2 |a| |b|^2]^(-1/3).`

This closes the exact B16 state in which the square scalar `S` and the transverse innovation `T` are two genuinely dependent projections of the SAME product bank. Only the third scalar `V` is required to come from a source-disjoint bank.

Essential boundedness is proved. Continuity is not proved by this argument and is recorded separately.

## 3. Strict owner-target example with genuinely dependent same-bank projections

Take four physical coordinates. On the first three let

`s=(1/sqrt(2),1/sqrt(2),0)`,

`t=(1/sqrt(6),-1/sqrt(6),2/sqrt(6))`,

so `s,t` are orthonormal. Put

`S=s.X_(1:3)`, `T=t.X_(1:3)`, `V=X_4`.

For generic independent non-Gaussian physical inputs, `S` and `T` are dependent. Consider

`Q_* = 3S^2 + 6(S+T)V`.

The effective orthonormal-coordinate matrix is

`B_*= [[3,0,3],[0,0,3],[3,3,0]]`.

Writing `B_*=3B_0`, the characteristic polynomial of `B_0` is

`mu^3-mu^2-2mu+1`.

Its signs at `-2,-1,1/3,1,2` locate the three roots in

`(-2,-1)`, `(1/3,1)`, `(1,2)`.

Hence the three eigenvalues of `B_*` lie in

`(-6,-3)`, `(1,3)`, `(3,6)`

and all have absolute value strictly larger than one. Thus `Q_*` is inside the exact owner target.

Here `rho0=sigma0=tau0=1` and `a=b=3`, so the new theorem gives

`boxed: ||p_(Q_*)||_(infinity,ess) <= 4.`

Therefore every interval `I` obeys the genuine linear small-ball estimate

`boxed: P(Q_* in I) <= 4 |I|.`

Again continuity is not claimed.

## 4. Assigned independent-copy / time-integral consequence

Let `Q'` be an independent copy of the WHOLE scalar output `Q`. The dependence inside `(S,T)` is untouched. Since

`p_(Q-Q') = p_Q * tilde(p_Q)`,

`||p_(Q-Q')||_infinity <= ||p_Q||_infinity =:H`.

For a probability density bounded by `H`, the same one-dimensional bathtub estimate gives

`E|Q-Q'|^(-1/2) <= 2sqrt(2H)`.

Using the programme Fourier convention,

`int_R |t|^(-1/2)|phi_Q(t)|^2dt
 =sqrt(2pi) E|Q-Q'|^(-1/2)`.

Hence

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <= 4 sqrt(pi H).`

Substituting Theorem 1 gives

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <= 4sqrt(6pi) M^(1/3)N^(1/3)
    |a|^(-1/6)|b|^(-1/3).`

For the orthogonal product-bank specialization,

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <= 8sqrt(3pi)
    (rho0 sigma0 tau0)^(-1/3)
    |a|^(-1/6)|b|^(-1/3).`

For the strict target `Q_*`,

`boxed:
 int_R |t|^(-1/2)|phi_(Q_*)(t)|^2dt
 <= 8sqrt(pi)
 =14.179630807244127... .`

This uses the independent-copy identity only for the whole scalar output; no `X-X'` variable is separated from its conjugate `X+X'`.

## 5. Designated partner account04/B03 applied to the same strict target

The newest completed designated-partner result remains account04/B03 r4,

`yspennstate/math-open-problems@5f93186cf8952b2b8b0255e08a78fd8506c613e4`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260924T051411Z-account04-B03-plucker-overlap2-r4/REPORT.md`.

It proves the literal overlap-two inequality

`||p_Q||_(infinity,ess)
 <=129.924435862525374 J_2(H)^(-1/6)`

for its exact-rank-three branch.

Apply it to the concrete orthonormal frame used above. Its nonzero Plucker weights are

`w_124=w_134=w_234=1/3`.

For the physical pair `H={1,4}`,

`q_H=2/3`, `r_H=2/9`.

Since `Delta=|det B_*|=27`,

`J_2(H)=Delta^2(q_H^2-r_H)
       =27^2(4/9-2/9)
       =162`.

Thus the partner theorem gives the actual strict-target inequality

`boxed:
 ||p_(Q_*)||_(infinity,ess)
 <=129.924435862525374 * 162^(-1/6)
 =55.64656197133566... .`

Applying the whole-copy Riesz conversion to this partner bound gives

`boxed:
 int |t|^(-1/2)|phi_(Q_*)(t)|^2dt
 <=52.88762884254536... .`

The new same-bank square/hyperbolic theorem improves this particular target to density `<=4` and time integral `<=8sqrt(pi)`, while the partner calculation independently pays the exact required overlap-two currency on the same physical frame.

## 6. What is and is not closed

Newly proved in this run:

1. A deterministic/probabilistic one-copy density compiler for a dependent same-bank pair plus one source-disjoint scalar, with determinant-homogeneous exponent `|a b^2|^(-1/3)`.
2. The exact B16 overlap packet `aS^2+2b(T+cS)V` is paid without any conditional-cap hypothesis.
3. A strict target family with genuinely dependent same-bank projections has density `<=4`.
4. The assigned whole-copy negative-half time integral is quantitatively bounded, and linear small-ball scaling is already obtained directly from the one-copy density theorem.
5. The designated account04/B03 result is applied to an actual physical-frame inequality.

Not proved:

- the unrestricted three-large-eigenvalue conjecture;
- continuity of the density in the new general theorem;
- a structural theorem forcing every remaining global geometry into this square/hyperbolic overlap packet or another completed receiver.

The next B03 implication is structural/analytic: locate this packet inside the current global heavy-hub / rank-two survivor with universal lower control of `rho0 sigma0 tau0 |a|^(1/2)|b|`, or splice the new theorem with the balanced-carrier/E3 branches when one factor degenerates. Do not replace this with a conditional density claim for same-bank projections.

## 7. Publication integrity

Changed-file allowlist for this run is confined to this immutable B03 run directory plus the corresponding account03/B03 handoff, worker-owned memory snapshot/pointer, receipt and finish records. No protected controls or peer artifacts are edited. Connector-only execution does not expose a repository secret-scanner command; a manual scoped review of the generated mathematical text found no credentials, personal data, private non-mathematical material, signed URLs, machine paths or secrets. This is a limited fallback scan, not a platform secret-scan attestation.
