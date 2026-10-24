# PROB10-05 idea checkpoint — retain the cyclic opposite-correlation gap via Plackett differentiation

Runtime request: GPT-6 / maximum. Authenticated scheduler model/effort telemetry is unavailable here; the execution environment identifies GPT-5.6 Sol while reasoning level is UNVERIFIED, so I do not claim GPT-6 maximum.

Current fleet baseline recovered before this idea: the complementary NM13-09 route has a candidate bound `theta_{2,1/4}>413/2500=0.1652`; canonical ownership remains `MOLCHAN-2025-THETA2H` with HARD7-05 / PROB10-05. The newest own PROB10-05 certified trace route had replaced the true cyclic Gaussian four-cycle by an equicorrelated vector, losing the strict opposite-correlation gap `a-b`.

## New idea before code

Do **not** evaluate the full quadrivariate orthant from scratch. Instead interpolate only the two opposite correlations in the cyclic four-cycle.

Let

`Sigma(c)=circ(1,a,c,a)`, `b<=c<=a`,

with

`a=168557580/170952323`, `b=167065920/170952323`.

At `c=b` this is the true four-cycle; at `c=a` it is the equicorrelated comparator already bounded in the previous PROB10-05 run. Write

`P(c)=P(X_0<0,X_1<0,X_2<0,X_3<0)` for `X~N(0,Sigma(c))`.

Plackett differentiation along the two opposite entries gives

`P'(c)=2 phi_2(0,0;c) * P(X_1<0,X_3<0 | X_0=X_2=0)`.

The conditional pair is centered Gaussian with correlation

`q(c)=[c(1+c)-2a^2]/[1+c-2a^2]`.

The key counterexample test is whether `q(c)` becomes so negative near `c=b` that the derivative gain is negligible. Exact arithmetic shows instead `q(b)>-3/8`. Since `q(c)` is increasing on `[b,a]`, and `arcsin(3/8)<pi/8`, the conditional orthant is uniformly larger than `3/16`. Hence

`P'(c) > 3/[16 pi sqrt(1-c^2)] >= 3/[16 pi sqrt(1-b^2)]`.

Therefore

`P(a)-P(b) > 3(a-b)/[16 pi sqrt(1-b^2)]`.

The deliberately coarse exact substitutions `pi<22/7` and `sqrt(1-b^2)<213/1000` should already give a rational decrement greater than `243/100000`. Dividing by `1-r^4`, `r=7/8`, should lower the inherited fourth-trace cap `273011/250000=1.092044` to below `5431/5000=1.0862`.

If that survives exact arithmetic, the existing degree-18 quasimode/Temple data should certify the source-level target `theta_{2,1/4}>1653/10000=0.1653`, strictly beating the current fleet candidate `0.1652` while preserving the continuous-time direction (the continuous event is contained in every sampled-grid event).

## Three materially different attacks compared

1. **Cyclic Plackett decrement (chosen):** use the exact `a-b` gap as a monotone derivative integral; avoids full special-function quadrature.
2. **Exact mode decomposition:** diagonalize the circulant covariance into `(A,C)` plus independent difference modes `(B,D)`, giving the exact event `A<-|B|, C<-|D|`; promising but leaves a two-dimensional Gaussian integral needing a separate certified enclosure.
3. **Reverse continuous-time interpolation:** use the deterministic mesh/margin sandwich plus Borell-TIS to attack the *upper* exponent endpoint. This remains conceptually independent, but a useful exponent improvement would require a nontrivial lower bound for the shrunken sampled persistence event and is not yet paid.

No theorem is claimed in this checkpoint. The next step is an exact-arithmetic checker for the rational inequalities only after this route has been written down.