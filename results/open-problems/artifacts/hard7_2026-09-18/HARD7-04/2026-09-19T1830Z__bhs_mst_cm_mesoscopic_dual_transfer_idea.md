Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-04 idea-before-bookkeeping checkpoint — finite-n Pareto duality through the whole mesoscopic collar

Canonical target remains `operations/claims/BHS-MST-CM-UNIV.md` (owner HARD7-04). The frozen source metric remains `beta_MST^- >= eta`, `eta=(tau-3)/(tau-1)`. This idea is aimed at the missing *upper/complement-control* direction and does not by itself move that metric.

Previous BHS-MST runs used B1/B2/B19 and B6/B20/B30. This run uses three fresh moves:

- **B3 PROVE SOMETHING STRONGER:** replace the previous limiting-law statement `m_-(p)=1-(tau-3)epsilon+o(epsilon)` by a finite-`n`, triangular-array statement valid for every mesoscopic `epsilon_n=lambda_n n^{-eta}` with `lambda_n -> infinity` and `lambda_n=o(n^eta)` in an explicit Pareto-quantile degree subclass.
- **B11 DUALIZE:** keep the exact extinction-root/secant identity at finite `n`; it reduces the desired dual mean deficit to the ratio between an endpoint derivative loss and its average.
- **B25 COUNT THE SAME THING TWICE:** compute that derivative loss once from the excess pgf and once by summation by parts against the cumulative degree counts. The second count exposes the `tau-3` regular-variation exponent with a rounding error only of critical order `n^{-eta}`, hence negligible as soon as `lambda_n -> infinity`.

## Candidate theorem to prove on the page

Write

`r=tau-1 in (2,3)`, `a=1/r`, `beta=tau-3=r-2 in (0,1)`, `eta=a beta`.

Consider the canonical deterministic Pareto-quantile degree subclass with minimum degree at least 3 and cumulative high-degree counts

`A_n(k):=#{i:d_i>=k}=floor(C n k^{-r})`

through its natural cutoff `K_n=Theta(n^a)`, with bounded-degree mass added at degree 3 and an `O(1)` parity correction. This has the required power-law exponent, finite limiting second moment, infinite third-moment scale, and `d_max=Theta(n^a)`.

Let

`h_n(s)=(1/ell_n) sum_i d_i s^(d_i-1)`, `nu_n=h_n'(1) -> nu>1`,

and

`g_n(y):=nu_n-h_n'(1-y)`.

The key finite-size estimate should be, uniformly whenever `z_n -> infinity` and `z_n=o(n^a)`,

`g_n(z_n n^{-a}) = K_0 n^{-eta} z_n^beta (1+o(1))`,

for an explicit `K_0>0`. The continuum constant obtained from the pure Pareto tail is

`K_0=(C r/mu) int_0^infinity x^(1-r)(1-e^{-x}) dx`

`    =(C r/mu) Gamma(3-r)/(r-2)`.

The integer-floor error is only `O(K_n^2/n)=O(n^{-eta})`, while the main term is `n^{-eta} z_n^beta`; this is the reason the mesoscopic condition `z_n -> infinity` kills the arithmetic roughness.

For

`A_n^*(y):=(1/y) int_0^y g_n(t) dt`,

regular variation then gives

`A_n^*(y_n)/g_n(y_n) -> 1/(beta+1)`

whenever `y_n n^a -> infinity` and `y_n ->0`.

Now set

`epsilon_n=lambda_n n^{-eta}`, `p_n=(1+epsilon_n)/nu_n`,

where `lambda_n -> infinity` and `lambda_n=o(n^eta)`, and let `q_n=1-y_n<1` be the nontrivial extinction root

`q_n=1-p_n+p_n h_n(q_n)`.

The exact finite-n identities are

`epsilon_n = p_n A_n^*(y_n)`,

`1-m_{n,-} = p_n [g_n(y_n)-A_n^*(y_n)]`,

`m_{n,-}:=p_n h_n'(q_n)`.

The first identity should force `z_n:=y_n n^a -> infinity`; since `epsilon_n ->0`, also `y_n->0`, and hence `z_n=o(n^a)`. Therefore

`z_n^beta ~ ((beta+1) nu/K_0) lambda_n`

and

`1-m_{n,-} = (beta+o(1)) epsilon_n = (tau-3+o(1)) lambda_n n^{-eta}`.

For a fixed collar `0<delta<tau-3`, let

`p_{n,delta}=(1+(1+delta)epsilon_n)/nu_n`.

Keeping the `p_n` extinction tilt gives the two-level proxy

`p_{n,delta} h_n'(q_n)=1-(tau-3-delta+o(1)) epsilon_n`.

Thus this route would upgrade the previous scalar collar calculation to the entire mesoscopic range `1 << lambda_n << n^eta` for a concrete source-compatible power-law subclass. It still does **not** control the actual configuration model after deleting its principal component: the remaining graph-level obligation is to show that the random deleted half-edge profile is close enough to this deterministic dual profile uniformly along a geometric lambda ladder.

## Failure tests before claiming anything

1. `lambda_n=O(1)`: the `O(n^{-eta})` integer-tail error is no longer negligible compared with the signal. This proof is not a replacement for the published critical-window limit or the previous limiting-law argument.
2. `lambda_n` comparable to `n^eta`: then `epsilon_n` is not small and the extinction root need not lie in the `y->0` regime. No nearcritical expansion is claimed there.
3. Actual deleted giant: pairing/conditioning changes the empirical half-edge law. The theorem below, if proved, is an analytic triangular-array input, not an MST upper bound.

No finite checker is warranted for this analytic theorem; the proof, if completed, must be written in the immutable run report.