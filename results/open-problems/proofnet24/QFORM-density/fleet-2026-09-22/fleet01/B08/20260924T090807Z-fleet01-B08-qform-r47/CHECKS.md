# r47 exact arithmetic checks

Run: `20260924T090807Z-fleet01-B08-qform-r47`.

These are deterministic arithmetic checks for the proof in `REPORT.md`; no Monte Carlo evidence is used.

1. Frame-balance deviation:

`delta=47/96-3/10=91/480`.

`P(frame bad) <= (1/64)/delta^2 =3600/8281 =0.4347301050597754...`.

2. Star-energy concentration from `||b||_inf<B/16`:

`Var Z < B^4/1024` and the gap from `EZ=B^2/2` to `9B^2/20` is `B^2/20`, hence

`P(star bad)<=400/1024=25/64=0.390625`.

The union-bound slack is

`1-3600/8281-25/64 =92559/529984 =0.17464489494022462...>0`.

3. Star fraction:

`sqrt(9/20)=0.6708203932499369...`.

4. Partner deletion constants:

`c0=sqrt(67/800)=0.28939592256975566...`,

`sigma=c0/2=0.14469796128487783...`.

With `rho=0.0006247538095703261`, the relative-nonalignment physical distance gate gives

`delta_abs=sqrt(9/20)*rho/2=0.00020954879811018115...`.

Thus

`kappa=(sigma^2*delta_abs)^(1/3)=0.016370803646028022...`.

The marginal-free third-compound constant is

`C3=6^(4/3)=10.902723556992836...`,

so

`C3/kappa=665.9858485101381...`.

5. Sixteen-bank partition:

`eta=(1/256)/(9/20)=5/576`.

`1/16-eta=31/576`, hence every bank has star norm larger than

`sqrt(31/576)||z||=(sqrt(31)/24)||z||=0.23199018178458425...||z||`.

Relative to the original row norm `B`, this is

`sqrt(31/576)*sqrt(9/20)=sqrt(31/1280)=0.15562374497485915...`,

and at `B>rho L` it exceeds

`9.722652753264413e-5 L`.

6. Four-bank carrier footprint:

`1/4-eta=139/576`, so each four-bank star piece has norm larger than

`sqrt(139)/24=0.4912427551063165...` times `||z||`.

If two carrier pieces were each below `||z||/8`, each corresponding residual piece would exceed

`(sqrt(139)/24-1/8)||z||=0.3662427551063165...||z||`.

Twice the square of this number is

`0.2682675113357306...>1/4`,

contradicting the relative-alignment residual bound `||e||^2<||z||^2/4`.

Therefore at most one of the four physical banks is carrier-light, and at least three have normalized carrier mass at least `1/8`.

Marker: `QFORM_B08_R47_CHECK_PASS`.
