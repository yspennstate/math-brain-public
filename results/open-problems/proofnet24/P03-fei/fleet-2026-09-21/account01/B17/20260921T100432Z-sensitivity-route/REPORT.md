# B17 FEI creative attempt: the full sensitivity-set entropy route is impossible, but a one-coordinate probe has the right activation scale

Status: **full FEI remains OPEN / NOT PROVED.** This is a creative route test and replacement mechanism, not an audit and not a claim of literature novelty. Work was done `WITHOUT_VERIFIED_BRAIN` under the live B17 FEI assignment.

## 1. Route tested

Approach 3 in the current FEI continuation proposes coupling the spectral sample `S` to the sensitivity set `Sens(X)` of a uniform input, with the hope of reducing FEI to an input-side entropy bound

`H(Sens(X)) <= C I(f)`.

The one-point Boolean function kills this reduction analytically, and in fact kills every input-side surrogate that reveals whether the sampled vertex is on the sensitivity boundary.

## 2. Exact counterexample family

Let `f_n:{0,1}^n -> {-1,+1}` be `-1` at `0^n` and `+1` everywhere else. For uniform `X`,

- `Sens(0^n)=[n]`;
- `Sens(e_i)={i}` for each `i`;
- `Sens(x)=empty` at every other vertex.

Hence, with `q_n=(n+1)/2^n`,

`P(Sens=empty)=1-q_n`,

`P(Sens=[n])=2^-n`, and `P(Sens={i})=2^-n` for every `i`.

Therefore

`H(Sens(X)) = h_2(q_n) + q_n log_2(n+1)`.

There are exactly `n` boundary edges, and each sensitive edge is seen from both endpoints in the influence probability, so

`I(f_n)=n 2^(1-n)`.

Using `h_2(q)=q log_2(1/q)+q/ln 2+O(q^2)` gives

`H(Sens(X))/I(f_n) = ((n+1)/(2n)) (n+1/ln 2) + o(1) = n/2 + O(1)`.

Thus no dimension-independent constant can satisfy `H(Sens(X)) <= C I(f)` for all Boolean functions.

This is not a failure of FEI itself. The Fourier coefficients of the same function are

`fhat(empty)=1-2^(1-n)`, and `|fhat(S)|=2^(1-n)` for every nonempty `S`.

Consequently

`H(f_n)/I(f_n) -> 4`.

So the sensitivity-set surrogate loses a factor of order `n` on a family whose actual FEI ratio stays bounded and tends to four.

The same obstruction survives if the surrogate forgets the identities of the sensitive coordinates and keeps only `|Sens(X)|`. Here

`P(|Sens|=0)=1-q_n`, `P(|Sens|=1)=n/2^n`, `P(|Sens|=n)=1/2^n`,

and `H(|Sens(X)|)/I(f_n)` is still unbounded (numerically 7.2663 at `n=16` and 14.7439 at `n=32`).

## 3. Stronger boundary-revealing obstruction

The issue is not the labels of the set; it is the activation event itself.

Let `R` be any random variable constructed from a uniform input (possibly also using independent auxiliary randomness) such that the event

`B={Sens(X) != empty}`

is determined by `R`. Then data processing gives

`H(R) >= H(B) = h_2(q_n)`.

For the one-point family,

`h_2(q_n)/I(f_n) = (n-log_2 n)/2 + O(1) -> infinity`.

Therefore **any proposed input-side code that explicitly reveals whether the sampled vertex is a boundary vertex cannot have entropy `O(I)` in general.** A successful sensitivity-based FEI proof must either random-thin the boundary event or avoid exposing it.

This is the precise reason the full-set coupling route, as originally stated, cannot close FEI.

## 4. A replacement with the correct activation probability

There is a natural one-coordinate probe that avoids the obstruction.

Choose `J` uniformly from `[n]`, independently of the uniform input `X`. Then

`P(J in Sens(X)) = I(f)/n`.

For the spectral sample `S`, independently choose the same kind of uniform coordinate `J`. Since `P(i in S)=Inf_i(f)` and `sum_i Inf_i(f)=I(f)`,

`P(J in S)=I(f)/n`.

In fact the marginal identity is coordinatewise:

`P(i in Sens(X)) = Inf_i(f) = P(i in S)`.

For the one-point defect the probe activation is `I/n=2^(1-n)`, not `(n+1)/2^n`; its Bernoulli entropy is `O(I)`, so the factor-`n` activation loss disappears.

There is also an exact conditional Fourier duality. For fixed `i`, define the discrete derivative on the `(n-1)`-cube

`D_i f(x_{-i}) = (f(x_i=+1,x_{-i})-f(x_i=-1,x_{-i}))/2`.

It takes values in `{0,+1,-1}` and has squared `L2` norm `Inf_i(f)`. Its physical squared law, normalized by `Inf_i(f)`, is uniform on the sensitive `i`-fibres. Its Fourier coefficients are exactly the parent coefficients with `i` adjoined (up to the standard sign convention), so its normalized squared Fourier law is

`Law(S\{i} | i in S)`.

Thus a corrected sensitivity route should couple or code the **one-coordinate Palm laws** rather than the entire random sensitivity set. The two activation events have exactly matching mass, and the conditional laws are Fourier transforms of the same ternary derivative.

Entropic uncertainty by itself points in the wrong direction for FEI (it lower-bounds the derivative Fourier entropy when `Inf_i` is tiny), so an additional Boolean comparison lemma is still needed. But the route is now formulated at the correct activation scale and avoids the exact one-point obstruction above.

## 5. Executed checks

`verify_sensitivity_obstruction.py` evaluates the closed forms at `n=2,3,4,5,8,12,16,24,32` and directly enumerates the sensitivity-set distribution through `n=8`. Representative ratios are:

| n | H(Sens)/I | H(|Sens|)/I | H(Fourier)/I |
|---:|---:|---:|---:|
| 8 | 5.2971 | 3.7971 | 3.8428 |
| 16 | 9.2663 | 7.2663 | 3.9303 |
| 24 | 13.2514 | 10.9589 | 3.9536 |
| 32 | 17.2439 | 14.7439 | 3.9652 |

The direct finite distribution checks passed for every tested `n<=8`. The local checker SHA-256 before repository upload was `b5fc6048392227a70b7a7f8fe0fcdbcc777c0a7486d018d5f3b72f0aedbb17f9`; the full local JSON stdout SHA-256 was `6245de94ff6daa967cc65d84892b9494925b14172e8b42f7648b75c6e2bc7145`.

## 6. What is killed, what survives, and the next move

Killed: the proposed reduction `H(Sens(X)) <= C I(f)`; the same reduction using only sensitivity-set size; more generally any `O(I)`-entropy proxy from which boundary nonemptiness can always be recovered.

Not killed: FEI; the entropy comparison `H(S) <= H(Sens(X))+I`; a randomized/thinned sensitivity coupling; or the one-coordinate probe construction above.

**Next B17 move:** work with the coordinate-Palm pair `1_{i in Sens(X)}` / `1_{i in S}` and the ternary derivative `D_i f`. The first decisive target is an inequality that upper-bounds the information needed to pass from the physical sensitive-fibre law of `D_i f` to its Fourier law, after averaging over `i` with weights `Inf_i`, without paying the boundary-activation entropy separately for every coordinate. Stress it first on width-two tribes, Hod's recursive lower-bound family, and the one-point defect.
