Model requested: GPT-6 maximum. Applied runtime metadata is not authenticated by the scheduler; reasoning level therefore recorded as UNVERIFIED.

# PROB10-10 idea before code — tropical k-front Bellman compiler

Frozen source: ordinary nearest-neighbor **undirected** FPP on `Z^2` with iid physical-edge `Exp(1)` weights. Let `mu` be its deterministic time-constant norm and

`Delta_12 = 2 mu(e1) - mu(1,1)`.

Source-facing metric before this attack is still `c_*=0` for a rigorous lower bound on `Delta_12`; a one-pair positive value would be PARTIAL, not full strict convexity.

## Why this is a different mechanism

The preceding asynchronous-carry run proved a correct full-profile Bellman compiler but left a continuous high-dimensional boundary profile and a hard rounded-state certificate. The new attack does **not** round or cap that profile and does not return to the retired R08 local-detour / fixed-corner route. Instead it tests whether a translation-covariant tropical Lyapunov function can collapse the full continuum of boundary labels to a finite `k`-subset problem **without any projection error**.

Use the rotated strip coordinates `s=x+y`, `d=x-y`. Fix half-width `W` and band length `L`, with even left/right antidiagonals. Let `D` be the finite offset set on a boundary. For one fresh band let

`T_omega(i,j)`

be its ordinary undirected restricted FPP passage time from left offset `i in D` to right offset `j in D`. For an incoming normalized arrival profile `y=(y_i)`, `min_i y_i=0`, the exact carried profile is

`F_omega(y)_j = min_i { y_i + T_omega(i,j) }`,
`g(y,omega)=min_j F_omega(y)_j`,
`Phi(y,omega)=F_omega(y)-g(y,omega) 1`.

For `1<=k<=|D|` and a real potential `phi` on the `k`-subsets of `D`, define

`h_phi(y) = min_{I subset D, |I|=k} { (1/k) sum_{i in I} y_i + phi(I) }`.

This function is translation covariant:

`h_phi(y+c 1)=c+h_phi(y)`.

Hence exactly

`g(y,omega)+h_phi(Phi(y,omega)) = h_phi(F_omega(y))`.

If `I` is any minimizer in the definition of `h_phi(y)`, then for every right `k`-subset `J` and every bijection `pi:I->J`,

`F_omega(y)_{pi(i)} <= y_i + T_omega(i,pi(i))`.

Therefore

`h_phi(F_omega(y))-h_phi(y)`
` <= min_{J, |J|=k} min_{pi:I->J bijection}`
`       { (1/k) sum_{i in I} T_omega(i,pi(i)) + phi(J)-phi(I) }`.

Define the finite random tropical operator

`(K_{k,omega} phi)(I)`
` := min_{J, |J|=k} min_{pi:I->J bijection}`
`       { (1/k) sum_{i in I} T_omega(i,pi(i)) + phi(J) }`.

The candidate one-band certificate is

`lambda_k(phi) := max_{I:|I|=k} { E[(K_{k,omega} phi)(I)] - phi(I) }`.

If finite, the displayed pathwise inequality gives the full Bellman drift inequality for **every** incoming profile with at least `k` finite labels. No mesh, cutoff, state truncation, independence approximation, or unproved finite-to-infinite step appears.

After the first connected band all right-boundary labels are finite almost surely, so one may start the Lyapunov telescope there. Since normalized labels are nonnegative,

`h_phi(y) >= min_I phi(I)`.

Thus for `N>=2` bands,

`E M_N <= E[M_1+h_phi(Y_1)] + (N-1) lambda_k(phi) - min_I phi(I)`.

The same fresh terminal zig-zag used in the preceding carry theorem costs at most `W` in conditional expectation. Consequently the exact finite-to-infinite target is

`mu(1,1) <= lambda_k(phi)/L`,

with the explicit finite-N upper error

`E T(0,(NL,NL))/(NL)`
` <= lambda_k(phi)/L`
`    + [E(M_1+h_phi(Y_1))-min_I phi(I)+W]/(L N)`

(for the harmless replacement `(N-1)lambda <= N lambda` when `lambda>=0`).

Hence, together with the retained exact axis lower bound

`mu(e1) >= b = 3002823/10000000`,

any rigorous finite certificate

`lambda_k(phi)/L < 2b = 0.6005646`

would prove the source-valid one-pair strict gap

`Delta_12 >= 0.6005646 - lambda_k(phi)/L > 0`.

That would still be PARTIAL, not global strict convexity.

## Negation-first plan

The theorem is useful only if the finite tropical certificate can beat `0.6005646`. Before attempting a large exact computation:

1. `k=1` is the rank-one min-plus potential. Numerically optimize/test it. If it remains near the single-source point-to-line cost, it cannot explain the previous asynchronous rate.
2. `k=2` is the first true multi-front certificate. On modest widths, estimate its additive eigenvalue by Monte Carlo/value iteration and test whether increasing width materially lowers the rate.
3. Compare against the already archived full-profile asynchronous screen (`W=40`, mean about `0.59475`, numerical only). A large gap between `k<=2` and the full carry will be recorded as a precise *rank obstruction*, not hidden by another checker.
4. Preserve all values as numerical route-selection evidence only unless an exact finite certificate is produced.

## Three materially different live approaches

A. **Tropical k-front Bellman reduction (pursued here):** finite subset state, exact dependence control, no rounded-profile error.

B. **Exact exponential finite-block/Richardson route (retained):** exact rational recursion for ordinary source-to-terminal blocks from the preceding run. Its obstruction is infection-set state explosion at widths large enough to approach the diagonal threshold.

C. **P20 true-geodesic Busemann/residual route (not duplicated):** under flatness, linearly many forced U-backtracks on the true axis geodesic must have vanishing diagonal-target residual except for `o(n)` occurrences. The remaining global co-calibration obstruction is distinct from the block computation and remains owned by P20.

The old R08 independent-detour, pointwise finite strictness, and fixed-corner square-block routes remain retired and are not revived.