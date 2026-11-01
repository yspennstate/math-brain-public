# R08 E0011 — idea before checker code: one global fixed-top uniformization

Methods this run: **B8 DISCRETIZE / B11 DUALIZE / B25 COUNT THE SAME THING TWICE**.

Starting point: the sound frozen certificate is `b19_full`, while the preceding stopping-frontier report showed an approximately `3.7x` synchronization loss at each of the eight post-bootstrap stages but did not move the frozen metric because its stage targets were attained at random stopping times rather than at the deterministic block top.

## New route

Replace the eight separately timed post-bootstrap cylinder events by one finite progress-state chain with a **single deterministic global horizon**. The progress coordinate is

`j in {h3,h4,h5,h6,h7,h8_terminal,gdown,gup}`,

and the local coordinate is the already-certified 14-cell descriptor. For stages before `gup`, hitting the six-vacancy target causes an instantaneous progress jump to the next stage. At a progress jump, instead of pretending to know the translated next-stage descriptor, take the minimum over that stage's full certified entrance class. This is source-safe because every existing stage theorem is uniform over precisely those classes.

Use one common uniformization rate with `Dmax=222`. Put `H=36*222`. At stage with protected hazard `D`, add an exact null/self-loop mass `36*(222-D)`; accepted reaction branches keep their old integer masses, and every protected clock outside the accepted local alphabet goes to the cemetery state. Thus all stages live on one discrete tick clock without adding any Harris clock or changing the protected spatial sigma-field.

For the final `gup` stage, do **not** make the vacancy target absorbing: success is that the target is actually present at the global top. This directly addresses the deterministic-top gap from the preceding run.

## Backward recurrence

Let `U_j(n,s)` be the integer numerator, over denominator `H^n`, of successful completion from progress stage `j`, local state `s`, and `n` common uniformization ticks remaining. For the final stage,

`U_last(0,s)=1_target(s)`

and for `n>=1`,

`U_last(n,s)=null_last*U_last(n-1,s)+sum_allowed sum_t w(s,l,t) U_last(n-1,t)`.

For an earlier stage, first define `m_{j+1}(n)=min_{s in entrance(j+1)} U_{j+1}(n,s)`. If `s` is already a target, set `U_j(n,s)=m_{j+1}(n)` (instantaneous progress with no tick spent). Otherwise, for `n>=1`, apply the same null-plus-accepted transition recursion, replacing any target successor by `m_{j+1}(n-1)`. Killed mass contributes zero.

Finally `m_0(n)=min_{s in entrance(h3)} U_0(n,s)` gives the exact worst-entrance fixed-**tick** success probability `m_0(n)/H^n`.

## Deterministic time

For a deterministic global time `T`, with `lambda=(222/4)T`, Poisson uniformization gives

`P_T = exp(-lambda) * sum_{n>=0} lambda^n/n! * m_0(n)/H^n`.

A rigorous finite lower bound is obtained by truncating this nonnegative series and replacing `exp(-lambda)` by a rational lower bound. Search rational `lambda` only after the exact coefficient sequence is known. Compare the resulting one-horizon corridor probability against the product of the eight old fixed-window factors. If it is larger, every upstream factor of `b19_full` is unchanged and the frozen metric moves by their exact ratio.

## B25 independent count

The same finite core should be recomputed forward by first-progress times: convolve the exact stage-transition kernel over common ticks and finish with the nonabsorbing `gup` endpoint kernel. Backward and forward integer numerators must agree for every checked tick count before a metric claim is made.

No claim is made in this note. It records the route before checker code as required.