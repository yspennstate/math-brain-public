# PROB10-10 idea before code — retune the oblique lower-tail envelope after the moving-centered axis gain

Model: nearest-neighbor **undirected** FPP on `Z^2` with iid `Exp(1)` physical-edge weights.

Status target: **PARTIAL / OPEN**. The full-source axis/diagonal metric is still `c_*=0`; the purpose of this run is to enlarge the already rigorous restricted reflected strict-triangle cone without relabeling the neighboring P04 block theorem.

## Consumed new input

The newest complementary P04 report

`proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T07-44-45Z__moving-strip8-wandering-cone1640.md`

proves, by a moving-centered fresh-slab construction,

`mu(e1) <= a_* := 294639/500000 = 0.589278`,

with the finite construction

`E T(0,8N e1) <= 8N a_* + sqrt(N)`.

The canonical PROB10-10 ten-local self-avoiding-path transfer already supplies the all-length weighted endpoint count with

`A=3889/2000`, `B=27893/10000`, `r=1993/400`.

The previous cone used a lower-tail level `c=0.605`; that is now unnecessarily far above the stronger axis cap. The new idea is to lower `c` to only `10^-5` above `a_*`, and simultaneously tune the Chernoff parameter `s` extremely close to the critical value `r-1`. This minimizes the price of the geometric sum while preserving `q=r/(1+s)<1`.

## Candidate exact parameters

Take

- `c = 73661/125000 = 0.589288`, so `c-a_*=1/100000`;
- `rho_0 = 4099/2500 = 1.6396`;
- `s = 3982501/1000000 = 3.982501`;
- `q = r/(1+s) = 4982500/4982501`;
- `beta_hat = 99997/100000`.

For the canonical weighted-count theorem the lower-tail base is

`beta(rho)=A^(-1) B^(-rho) exp(s c) q^(1+rho)`.

Because `q/B<1`, `beta(rho)` is decreasing in `rho`. It is therefore enough to certify `beta(rho_0)<beta_hat<1` by exact rational upper/lower bounds on logarithms. If this succeeds, then for every `rho>=rho_0`,

`mu(1,rho) >= c`,

and P04's axis theorem yields

`mu(x,y)+mu(x,-y)-mu(2x,0) >= 2(c-a_*)x = x/50000`

throughout `|y|>=rho_0 x`.

This would move the certified cone boundary from `41/25=1.64` to `4099/2500=1.6396` while leaving the global strict-convexity problem and canonical `c_*` open.

## Explicit finite-to-infinite error plan

Use P04's finite axis estimate with horizontal scale `M=4N`:

`E T(0,2M e1) <= 2M a_* + (1/2)sqrt(M)`.

Use the ten-local weighted endpoint theorem with a safe all-length startup constant `Kbar` already derived in P04, so

`P(T(0,(M,rho M)) <= cM) <= C beta_hat^M`, `C=Kbar/(1-q)`.

Then

`[E T(M,rho M)+E T(M,-rho M)-E T(2M,0)]/M`

is at least

`delta - 2 c C beta_hat^M - 1/(2 sqrt(M))`, `delta=1/50000`.

For a finite exact check, use `M=10^12` (divisible by both 4 and 2500) and avoid constructing the enormous rational `beta_hat^M` directly: prove

`beta_hat^25000 < 1/2`

by the exact integer inequality

`2*99997^25000 < 100000^25000`.

Hence `beta_hat^M <= 2^-100` already from the first `2,500,000` steps, and the remaining exponent only improves the bound. The resulting finite residual should remain strictly positive after the `1/(2 sqrt(M))` repair.

## Three materially different attacks this run

1. **Critical-envelope recombination (selected).** Retune the already proved all-length ten-local count against the new P04 axis cap. This is a scalar variational improvement, not a new block theorem.
2. **Moving-centered diagonal slab (diagnostic / not promoted).** Apply the same fresh-slab/recentering principle directly across antidiagonal levels to upper-bound `mu(1,1)` and attack the canonical `Delta_12`. Small finite CTMC diagnostics remain far above the required `2*0.3002823=0.6005646` threshold, so no theorem claim is made. The exact missing finite lemma is a certified block with asymptotic diagonal cost below that threshold (or a stronger compatible axis lower bound).
3. **Busemann/HJB policy disagreement (not closed).** The P20 lane has a positive local mixed Bellman-gap under a hypothetical flat face, but the unresolved step is still a quantitative statement that every long competitor must incur positive density of disagreement/residual sites. Without that spatial unavoidability estimate, a local positive expectation cannot be summed into a macroscopic strict-triangle defect.

Only Attack 1 is promoted if the exact checker verifies all signs. Attacks 2 and 3 are recorded as nonclaims and as reasons not to repeat the retired generic surgery route.
