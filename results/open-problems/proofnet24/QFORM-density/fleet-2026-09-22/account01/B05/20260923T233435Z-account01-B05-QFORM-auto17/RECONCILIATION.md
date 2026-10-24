# Frontier reconciliation and overlap-saddle obstruction

This supplement is authoritative for the frontier status of run `20260923T233435Z-account01-B05-QFORM-auto17`. It preserves the already committed `REPORT.md` as useful mathematics but corrects its frontier description after reading the newer pre-existing B05 snapshot `20260923T222855Z-account01-B05-QFORM-auto19`, which predates this invocation in UTC time and had already advanced the zero-support-overlap branch.

## 1. Reconciliation with the newer existing B05 result

The pre-existing theorem `QFORM-SHARED-REMAINDER-DISJOINT-SQUARE-v1` in auto19 is stronger than this run's rank-two bridge on the canonical shared-multiplier/disjoint-square subcase: it permits arbitrary same-source remainder and linear-square coefficient functions and obtains a much smaller physical-space bound whenever one literal square carrier is absent from the hub multiplier. Therefore the statement in `REPORT.md` that the next frontier is merely `QFORM-SHARED-THIRD-CURVATURE-HALF-RIESZ-LIFT-v1` is superseded.

The current B05 frontier from auto19 is

`QFORM-INFINITESIMAL-SQUARE-CARRIER-OVERLAP-GLUE-v1`:

retain a transverse original square carrier whose coefficient in the hub multiplier is nonzero but arbitrarily small, and spend the third curvature before conditioning creates a rank-two saddle. The estimate must remain uniform as that overlap tends to zero.

The rank-two independent-square theorem in this run remains valid and useful as a repair theorem, but it is not itself the newest frontier advance.

## 2. New correction: an arbitrarily small nonzero overlap can create an unbounded rank-two conditional density

### Proposition — `QFORM-OVERLAP-VERTEX-ALIGNMENT-RECEIVER-FALSE-v1`

For every `0<delta<=1`, let `H,Y,X` be independent `Uniform[-1/2,1/2]` variables and define

`R_delta = Y^2 + 2 delta H Y + 2 H X - X^2/delta^2`.                (2.1)

Then:

1. `R_delta` has an unbounded density; in fact for `0<|s|<1/16`,

`boxed{ p_(R_delta)(s) >= (delta/2) log(1/(16|s|)). }`              (2.2)

2. Its homogeneous coefficient matrix

`M_delta = [[0,delta,1],[delta,1,0],[1,0,-delta^(-2)]]`             (2.3)

has rank two. Its two nonzero eigenvalues have opposite signs and both have absolute value strictly greater than one.

Thus **no proof may first demand a bounded-density receiver for the `(H,Y)` overlap core uniformly for every nonzero overlap, even arbitrarily small overlap, while discarding the third curvature direction**. The logarithmic rank-two saddle is real at every `delta>0`.

This is an intermediate-mechanism counterexample, not a counterexample to the three-large-eigenvalue conjecture.

### Proof of the logarithmic lower bound

Rewrite (2.1) exactly as

`R_delta = (Y+delta H)^2 - (delta H-X/delta)^2`.                    (2.4)

Condition on `H=h`. Put

`U=Y+delta h`, `V=delta h-X/delta`.

Given h, U and V are independent. The density of U is one on an interval of length one centered at `delta h`; the density of V is `delta` on an interval of length `1/delta` centered at `delta h`.

Fix `|h|<=1/4` and `0<delta<=1`. Both conditional supports contain `[-1/4,1/4]`. Hence the conditional joint density of `(U,V)` is at least `delta` on the square `[-r,r]^2` with `r=1/4`.

Use

`a=U-V`, `b=U+V`.

Then `R_delta=ab` and `dU dV=(1/2) da db`. The square `|a|,|b|<=r` maps inside `|U|,|V|<=r`, so for `0<|s|<r^2`,

`p_(R_delta|H=h)(s)`
` >= (delta/2) int_{|a|<=r, |s/a|<=r} da/|a|`
` = delta log(r^2/|s|).`                                           (2.5)

Since H has density one and the set `|h|<=1/4` has measure `1/2`, averaging gives

`p_(R_delta)(s) >= (delta/2) log(r^2/|s|)`
`                 = (delta/2) log(1/(16|s|)),`                     (2.6)

which proves (2.2) and the infinite essential supremum.

### Exact spectrum check

`det M_delta=0`. The two nonzero eigenvalues are the roots of

`g_delta(z)=z^2-(1-delta^(-2))z-(delta^2+1+delta^(-2)).`            (2.7)

For `0<delta<=1`,

`g_delta(1)=-(1+delta^2)<0`,

and

`g_delta(-1)=1-delta^2-2delta^(-2)<0`.                              (2.8)

Since `g_delta(z)->+infinity` as `z->+/-infinity`, its positive root is `>1` and its negative root is `<-1`. Thus the core has exactly two large eigenvalues, explaining why the logarithmic singularity is compatible with the sharp two-direction obstruction.

## 3. Spend the third curvature first: exact-target repair

Let `Z` be one more independent `Uniform[-1/2,1/2]` variable and define

`Q_delta=R_delta+Z^2`.                                               (3.1)

The matrix is `M_delta direct_sum [1]`. Therefore its spectrum consists of the two nonzero roots of (2.7), zero, and `1`; it has at least three eigenvalues of absolute value at least one for every `0<delta<=1`.

The determinant magnitude of the rank-two block is

`D_delta=delta^2+1+delta^(-2)>=3`.                                  (3.2)

Now apply this run's proved `QFORM-RANK2-INDEPENDENT-SQUARE-BRIDGE-v1` with the independent square carrier Z, `K_Z=1`, and `lambda=1`:

`boxed{
 ||p_(Q_delta)||_(infinity,ess)
 <=128 D_delta^(-1/4)
 <=128*3^(-1/4)
 <97.259.
}`                                                                   (3.3)

The repaired target-valid family has a continuous `C_0` density by the same split-convolution argument.

This gives a concrete end-to-end lesson for the current infinitesimal-overlap frontier: **the nonzero overlap cannot be regularized at the two-variable conditional stage; the third curvature must be retained before that rank-two saddle receiver is invoked.** The difficulty is therefore not continuity at `delta=0` of a two-variable bound. It is finding a product-preserving three-direction aggregation that remains uniform when the support incidence changes from zero to nonzero.

## 4. Current partner comparison

The newer designated account02/B05 theorem `QFORM-TWOBANK-HUB-LOG-PUNCTURED-v1` (run `20260923T213321Z-account02-B05-QFORM-auto11e`) shows that for the canonical two-bank source-shared shear with a genuinely independent hub, retaining the honest marginal density cap of L reduces the punctured loss from a power to `O(log(1/|b|))`; its remaining debt is the critical-window uniform limit. Auto19 then closes a different zero-support-overlap chamber by keeping an actual square carrier outside the multiplier.

The proposition above explains why the natural next interpolation cannot be obtained by a uniform conditional rank-two density estimate as the square-carrier overlap tends to zero: such an estimate is false for every nonzero overlap. Any successful glue theorem must use the third direction before this conditioning step, for example through an aggregate three-variable interval/coarea or a product-sensitive fractional trace that never isolates the saddle pair.

## 5. Final run status after reconciliation

- New valid mathematics retained from `REPORT.md`: `QFORM-RANK2-INDEPENDENT-SQUARE-BRIDGE-v1` and the determinant identity `D_R=t^2+b^2||p_perp||^2`.
- New frontier correction proved here: `QFORM-OVERLAP-VERTEX-ALIGNMENT-RECEIVER-FALSE-v1`, with the explicit logarithmic lower bound (2.2).
- New exact-target repair: adding an independent third square to the overlap saddle yields the universal bound (3.3), `<97.259`, and a continuous density.
- Required designated-partner result was already applied at an actual inequality in `REPORT.md`; the newer partner logarithmic theorem is additionally reconciled above.
- Full QFORM remains `OPEN_NOT_PROVED_NOT_DISPROVED`.
- Full-target continuity remains `OPEN`.
- Precise next step remains `QFORM-INFINITESIMAL-SQUARE-CARRIER-OVERLAP-GLUE-v1`, but now with a proved prohibition: do not condition away the third curvature and then seek a uniform two-variable density receiver.

Execution remains `WITHOUT_VERIFIED_BRAIN`.
