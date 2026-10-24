SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-23T18:15:22Z.
attacking: the positive-leakage near-null physical-hub collar; first force every surviving leaf transverse leverage below 1/61, then convert that spread into the row-marginal gate of the new arbitrary-rank projected-crossing receiver.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.
Control source at start: `yspennstate/math-research-brain@6831428e0be00570f90a3559ea42d16594fc930f`, OWNER CONTROL revision `2026-09-22.15`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

Work in the live exact-rank-three near-coloop collar already reduced by B10. Thus

- `A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`, `D=|det M|>=1`;
- one ORIGINAL physical row is `u_0=sqrt(c)e`, with `c>63/64`, `||e||=1`;
- the physical scalar pivot obeys `|A_00|<1/64`, while `alpha=e^T M e` obeys `|alpha|<1/16`;
- each leaf spectral row is `u_j=t_j e+p_j`, `p_j perpendicular e`;
- with `rho=1-c`, Parseval gives `sum t_j^2=rho<1/64`, `sum t_j p_j=0`, `sum p_jp_j^T=I_2`.

In particular every leaf has `|t_j|<1/8`.

## Leakage-improved transverse-heavy lemma

**Claim.** If one leaf `u=t e+p` has `h=||p||^2>=1/61`, then at least one of

`|e^T M u| >= 1/64`,

`|u^T M u| >= 1/128`

holds.

**Proof.** Put `v=p/sqrt(h)`, so `(e,v)` is orthonormal, and abbreviate

`b=e^T M u`, `q=u^T M u`.

The compression of `M` to `E=span(e,v)` is

`C=[[alpha,delta],[delta,zeta]]`,

where the exact identities are

`delta=(b-alpha t)/sqrt(h)`,

`zeta=(q-2tb+alpha t^2)/h`.

Assume for contradiction that `|b|<1/64` and `|q|<1/128`. Since `h>=1/61`, `1/sqrt(h)<=sqrt(61)<8`; since `|t|<1/8` and `|alpha|<1/16`,

`|delta| < 8(1/64+1/128)=3/16`.

Also

`|zeta| < 61(1/128+1/256+1/1024)=793/1024`.

Therefore the two absolute row sums of `C` are respectively less than

`1/16+3/16=1/4`,

`3/16+793/1024=985/1024<1`.

Hence `||C||_op<1`. But `E` is two-dimensional in `R^3`, so the map

`P_(E^perp) M |_E : E -> E^perp`

has a nonzero kernel. Choose a unit `z` in that kernel. Then `Mz` lies in `E`, and therefore

`||Mz||=||Cz||<1`,

contradicting `sigma_min(M)>=1`. QED.

This improves the previous `1/4` transverse-heavy gate to `1/61` by using the actual near-coloop leakage bound `|t|<1/8`; no upper bound on `||M||` is used.

## Immediate payment of that branch

If the second alternative holds, then the leaf leverage is `||u||^2>=h>=1/61`, and the completed exact-rank-three scalar-pivot estimate gives

`||p_Q||_infinity <= 128[(1/61)(1/128)D]^(-1/4) < 1204`.

If instead `|b|>=1/64` while `|q|<1/128`, then the physical pair `(0,j)` has

`|A_0j|=sqrt(c)|b| >= sqrt(63)/512`,

`|A_00|<1/64`, `|A_jj|<1/128`.

It is uniformly indefinite, and its smaller singular value obeys

`kappa >= |A_0j|-(|A_00|+|A_jj|)/2 >= (sqrt(63)-6)/512 >1/265`.

The fixed-pair rank-three determinant-bank identity gives

`P_0j=sum_(k!=0,j)|det A_{ {0,j,k} }| = D*c*h >= 63/(64*61)`.

Feeding the total bank into the completed indefinite-pair Schur-bank theorem gives

`||p_Q||_infinity <= 8*2^(3/4)(kappa P_0j)^(-1/4) <153`.

Thus every still-unpaid member of this near-coloop collar may henceforth assume

`boxed: ||p_j||^2 <1/61 for every leaf j.`

This is the first input needed for a dimension-free volume-marginal argument; the next step is to use it before any reciprocal tiny-minor payment.
