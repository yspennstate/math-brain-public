# fleet01/B13 — sharp Fourier-L^q phase transition on the bang-bang extreme class

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T123305Z-fleet01-B13-qform-r12`  
Status: **AUXILIARY STRUCTURAL OBSTRUCTION / full QFORM OPEN**  
Control read: `yspennstate/math-research-brain@780aaad88dacb14ffb70eded3d052d52f39925f8`, owner revision `2026-09-22.5`.

## 1. Exact target context

The full target remains: for every dimension, every independent real input family with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal density bound for `X^T A X`, or give a valid counterexample.

This report does **not** prove the full target. It isolates a sharp obstruction in the leverage-heavy branch of the current Fourier/Brascamp-Lieb mechanism.

The named partner result actually applied is fleet02/B13, canonical report
`yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T115714Z-fleet02-B13-qform-480ba28b/REPORT.md`.
It proves that the target small-ball supremum reduces with zero loss to product indicators `1_{E_i}`, `|E_i|=1`, and that bounded finite unions of intervals are sufficient for approximation. Thus any obstruction already present on finite-union indicators is genuinely present inside the canonical extreme class.

Also consumed: the current diffuse separable-phase theorem
`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb:proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`, which closes the rank-r diffuse Fourier branch under row leverages `c_i<=1/2` and leaves the leverage-heavy branch open.

## 2. Theorem: exact Fourier L^q threshold for admissible extreme laws

Use the Fourier convention

`hat f(t)=int_R exp(i t x) f(x) dx`.

Let

`D={f: 0<=f<=1, int f=1}`

and let

`E={1_E: |E|=1}`.

### Theorem

For every `q>=2`,

`sup_{f in D} ||hat f||_q <= (2 pi)^(1/q)`.

For every `1<q<2`,

`sup_{E: |E|=1, E a bounded finite union of intervals} ||hat 1_E||_q = infinity`.

More explicitly, for every integer `N>=13`, define

`E_N = union_{k=1}^N [2^k, 2^k+1/N]`.

Then `|E_N|=1`, `E_N` is a bounded union of exactly `N` intervals, and

`int_0^N |hat 1_{E_N}(t)|^q dt
 >= 2^(q/2-4) pi^(-q) N^(1-q/2)`.

Hence

`||hat 1_{E_N}||_q
 >= 2^(1/2-4/q) pi^(-1) N^(1/q-1/2) -> infinity`

for every `1<q<2`.

### Proof for q>=2

For every `f in D`,

`||hat f||_infinity <= ||f||_1=1`

and Plancherel gives

`||hat f||_2^2 = 2 pi ||f||_2^2 <= 2 pi ||f||_infinity ||f||_1 <= 2 pi`.

Therefore, for `q>=2`,

`int |hat f|^q <= ||hat f||_infinity^(q-2) ||hat f||_2^2 <= 2 pi`,

which is the asserted bound.

### Explicit construction for 1<q<2

For `E_N` above,

`hat 1_{E_N}(t)
 = (int_0^(1/N) exp(i t s) ds) sum_{k=1}^N exp(i 2^k t)`.

Write

`S_N(t)=sum_{k=1}^N exp(i 2^k t)`.

For `0<=t<=N`, since `0<=t/(2N)<=1/2` and `sin x >= (2/pi)x` on this range,

`|int_0^(1/N) exp(i t s) ds|
 = 2 |sin(t/(2N))|/t
 >= 2/(pi N)`.

Thus

`|hat 1_{E_N}(t)| >= (2/(pi N)) |S_N(t)|`,  `0<=t<=N`.

Now `S_N` is `2 pi`-periodic. Under normalized Lebesgue measure on one period,

`E |S_N|^2 = N`.

Also

`E |S_N|^4 = 2N^2-N <= 2N^2`.

Indeed the fourth moment counts ordered solutions of

`2^a+2^b=2^c+2^d`,

and uniqueness of binary expansion implies that the multisets `{a,b}` and `{c,d}` agree. There are `N` diagonal ordered pairs and `N(N-1)` off-diagonal ordered pairs, the latter having two matching orders, giving `N+2N(N-1)=2N^2-N`.

Apply Paley-Zygmund to `Z=|S_N|^2` with threshold `N/2`. Then

`P(|S_N|^2 >= N/2)
 >= (1/2)^2 N^2/(2N^2) = 1/8`.

Therefore

`int_0^(2 pi) |S_N(t)|^q dt
 >= (pi/4) (N/2)^(q/2)`.

For `N>=13`, `[0,N]` contains at least `N/(4 pi)` complete periods, so

`int_0^N |S_N(t)|^q dt
 >= 2^(-4-q/2) N^(1+q/2)`.

Multiplying by `(2/(pi N))^q` gives

`int_0^N |hat 1_{E_N}(t)|^q dt
 >= 2^(q/2-4) pi^(-q) N^(1-q/2)`.

Since `1-q/2>0`, the norms diverge.

## 3. Consequence for the current diffuse Fourier proof

In the rank-r spectral-frame notation, write the row vectors as

`u_i=sqrt(c_i) v_i`,  `||v_i||=1`,

with

`sum_i c_i v_i v_i^T=I_r`.

The current geometric Brascamp-Lieb/Fourier proof uses the one-factor exponent

`q_i = 1/c_i`.

The theorem above shows a sharp law-uniform phase transition at exactly

`q_i=2 <=> c_i=1/2`.

Consequently:

**Any attempted extension of the current diffuse proof that keeps the same factorwise step and asks for a fragmentation-uniform bound on `||hat f_i||_{1/c_i}` cannot cross a row leverage `c_i>1/2`.**

This is not merely a limitation of Hausdorff-Young. For every `c>1/2`, set `q=1/c<2`; the explicit finite-union extreme laws `1_{E_N}` above force that factor norm to diverge polynomially like

`N^(c-1/2)`

(up to the explicit constant after taking the q-th root).

Thus the leverage-heavy closure must aggregate/cancel across coordinates before taking factorwise absolute Fourier norms, or use a physical-space mechanism. It cannot be obtained by an unchanged continuation of the diffuse product-of-one-dimensional-L^q argument.

## 4. Why this matters for the live hard branch

The current fleet01/B19 hard family has a leverage-one physical row and nevertheless admits a universal output-density bound through fleet02/B10's aggregate hyperbolic-square mechanism. The theorem above explains analytically why the diffuse Fourier proof fails there even though the target theorem survives: leverage one demands a one-dimensional Fourier `L^1` payment, and finite-union extreme laws have no uniform such bound.

This cleanly separates two questions:

1. `c_i<=1/2`: the current factorwise Fourier/Brascamp-Lieb theorem is viable and already proved.
2. `c_i>1/2`: a different mechanism is mathematically necessary in general; high-cardinality aggregation or physical-space smoothing must occur before local reciprocal/Fourier costs are paid.

This does not rule out every possible Brascamp-Lieb reweighting, nor does it prove a QFORM counterexample.

## 5. Classification and first unpaid implication

Classification: **ESSENTIAL STRUCTURAL OBSTRUCTION / AUXILIARY_ONLY**.

Full QFORM remains **OPEN**.

The old tempting implication

`extend the diffuse separable-phase proof beyond leverage 1/2 by the same one-factor Fourier L^(1/c_i) control`

is **refuted**.

The sharpened unpaid implication is the live heavy-light problem:

`QFORM-RANK3-HYBRID-HEAVY-LIGHT`: whenever some spectral row has leverage `>1/2`, combine that physical coordinate with the residual diffuse frame *before* taking absolute Fourier norms or paying reciprocal minors, yielding one dimension-free density bound. The mechanism must also be compatible with the high-cardinality hyperbolic-square model and cannot assume a fixed well-conditioned triple.

Corrections respected: pointwise law-uniform Fourier decay remains false globally; cross-minor-alone and generic X-ray-only mechanisms remain refuted; no claim of full proof is made.
