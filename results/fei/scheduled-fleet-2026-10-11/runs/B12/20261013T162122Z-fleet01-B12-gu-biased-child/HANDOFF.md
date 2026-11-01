# Brain handoff — B12 / A056 biased-child GU cocycle

For arbitrary Boolean `g(y,z)` and arbitrary disjoint Boolean child `h`, this
run proves

`U(g(h,z)) = Inf_y(g) U(h) + Theta_{g,y}(E h)`.

The excess physical restriction decrement is exactly the scalar Doob
decrement of `Theta`.  Over every complete adaptive child restriction tree,
the full defect telescopes to

`Theta(mu) - (1+mu)Theta(1)/2 - (1-mu)Theta(-1)/2`.

This is cylinder-safe and independent of dimension, spectrum, depth, query
order, bias separation, and collision ratios.  The remaining payment is now a
one-dimensional endpoint-centered reserve.  The candidate bound

`centered Theta <= 3 Inf_y(g)(1-mu^2)`

survived 555,024 finite local tests with maximum normalized value `2.280249...`
but is **OPEN**, not proved.  The B19/A091 rare-bias correction must be retained
when proving it.

Route the exact formula and cocycle to B09/B18/B20 and the candidate scalar
lemma to A091/A090.  Universal GU and full FEI remain open.

