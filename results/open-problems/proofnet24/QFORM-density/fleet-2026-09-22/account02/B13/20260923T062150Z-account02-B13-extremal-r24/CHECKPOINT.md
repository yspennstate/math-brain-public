# account02/B13 r24 — early mathematical checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Extremal product laws / complementary constructions  
Status at checkpoint: full QFORM open; continuity separate; `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication attacked

`QFORM-SCALAR-E2-GLOBAL-HUB-PEEL-v1`: replace the cut-by-cut tri-hub survivor after a nonzero original scalar pivot by a cut-free physical-core dichotomy, without selecting one reciprocal local minor. Then test whether that core can be collapsed to a bounded local pivot; if not, produce a target-valid obstruction family.

Let `k` be an original coordinate with `d=A_kk !=0`, and let `S` be the full scalar Schur complement on the remaining ORIGINAL coordinates. Define the cut-free disjoint pair volume

`D2perp(S)=sum det(S[P,T])^2`,

where the sum is over ordered disjoint two-subsets `P,T` of the residual physical coordinate set.

Give each residual physical coordinate an independent fair L/R color and put `M=S[L,R]`. Cauchy--Binet gives

`e2(M^T M)=sum_(P subset L,T subset R, |P|=|T|=2) det(S[P,T])^2`.

Every fixed disjoint ordered pair `(P,T)` is captured with probability `2^-4`, hence

`E e2(M^TM)=D2perp(S)/16`.                                      (C1)

Thus some ORIGINAL-coordinate cut has `E:=e2(M^TM)>=D2perp(S)/16`.

Apply the completed designated partner account03/B13 theorem `QFORM-E2-ENTROPY-OR-TRIHUB-v1` at `h=3/5,L=log 4`. Either its entropy branch gives

`||p_R||_3 < 7.681 E^(-1/6)`,                                   (C2)

or there are at most three row hubs and at most three column hubs such that deleting them leaves less than `E/4` of this cut's squared 2-minor mass.

In the entropy branch, the exact scalar square peel plus the already-proved `L3 -> H_{1/2}` interpolation gives

`||p_Q||inf <= 4(4/3)^(3/4) 7.681^(3/4) |d|^(-1/2) E^(-1/8)`
`             < 32.4 |d|^(-1/2) D2perp(S)^(-1/8)`.             (C3)

In the hub branch, putting the at most six physical hubs into `H`, the cut loses more than `3E/4 >= 3 D2perp(S)/64` of GLOBAL disjoint pair volume. Therefore

`D2perp(S[H^c,H^c]) < (61/64) D2perp(S)`.                        (C4)

This can be iterated because the partner theorem allows arbitrary outside couplings: the already selected hubs remain outside the next cut rather than being conditioned away.

Consequently, for every `0<eta<1`, either (C3) fires at some stage with the then-current disjoint pair volume at least `eta D2perp(S)`, giving

`||p_Q||inf < 32.4 eta^(-1/8)|d|^(-1/2) D2perp(S)^(-1/8)`,       (C5)

or there is a physical core `H` with

`|H| <= 6 ceil(log(eta)/log(61/64))`

such that

`D2perp(S[H^c,H^c]) < eta D2perp(S)`.                            (C6)

The bordered determinant identity `det A[{k} union P,{k} union T]=d det S[P,T]` rewrites (C5) entirely in original-matrix currency.

The next step in this run is to prove that the finite-core alternative cannot be replaced by a single-good-minor assertion: an explicit two-diffuse-star family has four eigenvalues `+/-1`, zero scalar diagonals, every principal pair determinant `O(1/m)`, every disjoint cross 3-volume and 5-volume exactly zero, while its order-two cross volume stays one and is concentrated on one row/one column hub. The family is nevertheless uniformly paid by product structure, so it is an obstruction to the local-minor method, not to QFORM.
