# PROB10-10 idea before code — retitle the ten-local SAW dual after the new strip-9 axis cap

Runtime request: GPT-6 maximum. Actual model available to this run: GPT-5.6 Sol; reasoning level UNVERIFIED. I do not claim GPT-6 maximum.

The preceding canonical report proved that, **with the old fixed anisotropic tilt** `(A,B,r)`, scalar Chernoff retuning cannot cross its critical slope. P04 has since changed the source-facing input by proving the sharper axis cap

`a9 = 13247968739227/22500000000000 = 0.5887986106323111...`.

The new move is therefore not another `s,c` micro-search. It is to reopen the *dual tilt* of the already proved ten-local self-avoidance transfer: choose new horizontal/vertical weights `(A,B)`, recompute a Collatz/Perron upper bound `r(A,B)`, and minimize

`rho_*(A,B)=((r(A,B)-1)a9-log A)/log B`.

This is a distinct optimization layer. The old exact barrier applied only after `(A,B,r)` were frozen. A successful retitling improves the all-path entropy inequality itself.

Negation tests / three materially different routes for this run:

1. **Anisotropic nonbacktracking transfer (negation test).** Replace ten-local self-avoidance by the exact 4-state nonbacktracking automaton and optimize its two tilt parameters. It gives a critical slope about `1.68029`, worse than the current `1.6376495...`; so short memory alone cannot improve the source-valid cone.
2. **Retitled ten-local Collatz dual (main route).** Numerical Perron optimization proposes `A≈1.975886`, `B≈2.767213`. A simple rational nearby point `A=247/125`, `B=2767/1000` has Perron growth about `4.98691214`; the exact checker will attempt a positive integer Collatz vector and a rational upper bound `r=24934561/5000000`. If certified, this should lower the critical slope to about `1.637329`, a genuine direction-range improvement.
3. **Single-edge Busemann/HJB residual compiler.** P20 now needs only one reserved exponential residual clock and gives sharp local energy `f(p)=p+(1-p)log(1-p)`. The remaining source-scale obligation is still a lower bound on total charged probability mass along the actual axis geodesic above the `sqrt(n log n)` finite-to-infinite error. No such path-unavoidability estimate is presently available, so this route is not promoted this run.

A fourth direct-diagonal block route remains quantitatively far from the old source milestone: the retained axis lower bound `mu(e1)>=0.3002823` would require an upper bound `mu(1,1)<0.6005646`, while the certified diagonal construction remains much larger. No finite-size fit is treated as a theorem.

If the retitled Collatz certificate fails, preserve the failure rather than adjusting by floating signs. If it succeeds, report the source metric `c_*` separately from the restricted reflected-cone boundary and give an explicit finite-to-infinite error term using P04's strip-9 endpoint variance bound.
