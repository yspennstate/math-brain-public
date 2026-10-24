# Hostile-referee audit, 12 October 2026

No full LLN has been proved. The original first-order programme remains unresolved by this attempt. The counterexample concerns the literal grid model with unrestricted iid positive weights.

1. **Metric versus edge weights.** The source uses shortest paths. Our first/second-distance calculation uses exponential FPP exploration, giving rates (n-1)/n and 2(n-2)/n, not the first two iid incident-edge statistics. Numerical checks use all-pairs shortest paths. The nearby Bandyopadhyay–Sajadi theorem is explicitly excluded as a different model.

2. **Endpoint accounting.** The incidence sum counts each ordering segment twice and drops the second-distance obligation at the two endpoints. The clipped error is R, not a stochastic bound on an endpoint chosen after seeing the graph. The inequality was tested for 1,755 starts of random shortest-path metric graphs, with four clipping thresholds. All passed.

3. **Resampling influence.** The proof deletes the changed edge before taking its endpoint balls. Those balls are independent of both versions of that edge. A path using the edge must first reach an endpoint through the deleted-edge graph. This prevents circular conditioning. The inequality was tested in 360 resampling/threshold cases across n=5,12,25; all passed, with 213 changed root scores. This verifies finite examples, not the infinite-size theorem.

4. **Yule direction and moments.** The graph's k-vertex frontier rate is at most k, so it grows no faster than Yule. Using the reverse direction would invalidate the variance bound. Yule has second moment 2exp(2R)-exp(R). Efron–Stein's one-half factor and n(n-1)/2 edge count give 4(n-1)R^3 exp(2R). Only fixed R is used before the n limit; the estimate is not claimed uniform for increasing R.

5. **Grid locality.** The second arrival cannot require a third new vertex before the endpoint. Its score depends only on root edges and the edges incident to its first neighbor. The supports lie in the combinatorial radius-two ball. Distances beyond four imply independent scores; 41 nearby roots is a conservative covariance count. All but O(m) roots have rate-4 and rate-6 increments.

6. **Euclidean indegrees.** The sector proof concerns incoming two-neighbor edges, not the trivially bounded outgoing degree. Generic finite iid point configurations have no equal radial distances. At most twelve other scores depend on insertion/deletion of one point. Replacement adds at most 24 changed other scores and one replaced score; the proof uses the conservative bound 26R. Sampled configurations passed this influence test; maximum measured indegree was six, which is consistent with but does not prove the upper bound twelve.

7. **Binomial, not silently Poisson.** Euclidean score expectations are computed by conditional binomial counts in area-n squares and a vanishing boundary fraction. Poisson survival functions arise as an explicitly justified limit. The Gaussian integrals give the score limit 5/8.

8. **Infinite expectations.** No LLN with an infinite mean is invoked. The counterexample clips at each fixed K, proves concentration by finite dependence, then lets K increase after the grid size limit. It works for every start because the endpoint loss is at most K. Infinite E L for m>=4 is proved separately with two independent nonadjacent interior vertex minima, whose minimum has t^{-1} tail.

9. **Numerical scope.** `checks.json` records measured NUV and local-score means, not certified limiting NUV constants. Exponential grid bulk-score means were 0.33241, 0.33290, 0.33140 at m=8,16,25, versus 1/3. Euclidean score means 0.6720, 0.6524, 0.6417 at n=50,150,400 approach 0.625 from finite-size values; NUV means around 0.90 remain numerical evidence only. Mean-field samples were small and dependent across roots within an instance; they are consistency checks, not independent-root statistical tests. Clipped Pareto means agree with their exact finite expectations within ordinary sampling variation.

10. **Prior work and novelty.** The saved historical report's 0.629258 expectation floor was not independently certified here. Our 5/8 argument does not improve that claimed expectation bound. No novelty claim is made for the local-score method or constants.

11. **Formal-check scope.** `FiniteCharge.lean` checks the finite summation of local charges with endpoint losses, and (x+y)^2<=2x^2+2y^2. It does not formalize the metric incidence premises, probability models, Efron–Stein, or convergence. The first two Lean runs failed on missing imports; their logs are preserved. Final compilation status is recorded in `lean_check.txt`; only an exit-zero run is counted as checked. No `sorry`, `native_decide`, axiom, or broad `import Mathlib` is used.

12. **Remaining gap.** All concentration estimates concern bounded local scores. No local approximation, stabilization, subadditivity, or upper estimate matching those scores has been proved for the history-dependent NUV ordering. No claimed implication passes from score convergence to convergence of L. The light-tailed grid, Euclidean and exponential mean-field constants remain unidentified.

Final Lean result: exit 0, 134.52 seconds, as saved in lean_check.txt. Both declared theorems were accepted. No remaining numerical assertion failures or Lean errors remain in the final artifacts.
