# Independent adversarial review of `f02_separation.md` and `f03_cone.md`

## Verdict

Both results are mathematically consistent with the paid theorems in `BOUNDARY_GRID.md` and `MACRO_COMPACTNESS.md`. I found no fatal gap in the same-initialization separation proof or in the selected mixed-cone theorem. The latter has the stronger, correct statement: on `rho<0`, initial residual `(-,+)`, the limiting residual cone is globally invariant because the selected matrix has nonnegative off-diagonal entries. This makes the terminal mask persistence argument valid on every fixed physical horizon, beyond the short interval needed for the initial-slope comparison.

The one claim not supplied by either manuscript is distinct **marginal** output path laws for `gamma=1` and `.1`: `f02` explicitly limits itself to a same-initialization coupling, and `f03` treats one fixed gamma. The extra monotonicity argument in `agents/f04_audit.md` pays that step. It should be integrated if the run's headline asserts marginal nonuniversality.

## Checks of `f02_separation.md`

1. The selected mark has strict, open margins: at `rho=-.5,z=1,r=(-1,1),v=(.14,-.12)`, the coarse step is `(-.86,.38)` and the fine two steps are `(.04,-.07),(-.06,-.02)`. Under `r2>0,z>0`, `-+` is invariant, while `--` has exactly zero row update. Actual residual/weight variation is `o(1)` over the first two steps and controlled thereafter by the macro bootstrap.
2. The isolating event has positive limiting probability. The designated endpoint is one atom in a finite-intensity box, all other `|z|>epsilon` atoms are excluded, and the independent small-`z` square mass is below `delta` with positive probability. The hidden energy bound uses `V_U`, whose joint signed-ray limit is the sum of the signed coordinate square variables. The previous initialization proof's rare-jump independence supports its independence from the marked `W` endpoint process.
3. The exact output identity is used, not a tangent-Gram averaging step. The designated row yields an order-`T` positive second-coordinate contribution for the coarse grid; it yields zero for the fine grid. The common second-layer term differs by `O(T^2)`, and the other rows contribute at most `O(delta T)` on the event. Choosing the energy localization first, then `delta`, then `T`, avoids a circular constant choice.
4. The positive-probability coupling separation does not alone distinguish marginal laws. `f02` states this limitation correctly.

## Checks of `f03_cone.md`

1. The frozen selectors (3)--(4) are exact outside null threshold sets. Positive `z` has only dead or permanently `-+` terminal sectors; negative `z` has only dead or permanently `+-` sectors. If an orbit lands on an axis, taking one more step yields a strictly interior terminal sector except at a threshold equality; the mark law makes the exceptional set null.
2. Fixed-step convergence is applied only through a finite terminal step on each finite cutoff of atoms. Although the maximum terminal step is random and small-`z` terminal times are unbounded, a countable deterministic-step coupling plus the square-mass cutoff justifies the limit. This is the key bridge from the boundary-grid theorem to `O(L)` steps.
3. The terminal sectors remain invariant while `r1<0<r2` and the retained weight keeps its sign. The macro row displacement estimate ensures that sign stability; dead rows are exactly stationary. The first-layer output then converges to `diag(P1,P2) integral r`, and the same argument gives the strong positive-time tangent-Gram limit, since terminal gates are constant binary masks.
4. `C_{m,0}` has nonnegative off-diagonal entries because all ReLU coordinates are nonnegative. Thus for `Q_m=C_{m,0}+diag(P1_m,P2_m)`, `s=(-r1,r2)` follows a Metzler linear comparison system. Its positive coordinates stay positive at finite time. Localization in `Q_m` and initial cone margin, followed by Gronwall on the stopped actual path, rules out a cone exit. The global fixed-horizon claim is sound.
5. A finite set of gamma values can be handled jointly from the same initialization by taking the union of their vanishing error events. This supplies the common primitive coupling needed for the marginal-law argument.

## Marginal-law addendum

For `gamma_c=1=10 gamma_f`, the next coarse grid time after any `x`-crossing is at least the next fine grid time. Hence `P_{2,c}>=P_{2,f}` atom by atom for positive `z`; similarly `P_{1,c}>=P_{1,f}` for negative `z`. The robust target mark makes the second inequality strict in the relevant coordinate with positive probability on an open initial-residual box. More precisely `P_{2,c}>P_{2,f}` there. In the selected laws,

`f'_{2,c}(0+)-f'_{2,f}(0+)=R_2(P_{2,c}-P_{2,f})>=0`,

and it is strictly positive with positive probability when `R` is near `(-1,1)`. The derivative and `R=y-f(0)` are measurable from the output path. A bounded increasing transform of the derivative, multiplied by the observable residual-box indicator, therefore has different expectations under the two path laws. The `z^2` Poisson sum need not have a finite mean, so the bounded transform is necessary. This establishes distinct marginal output path laws without the rare isolation event in `f02`.

I independently ran 100,000 random frozen selectors in the mixed cone at the nested pair `(1,.1)` and found no fine-only escape. This computational check is supplementary; the grid-ceiling inequality gives the proof. The escape sets are not monotone for arbitrary nonnested multipliers: the exact central mark escapes at `.13` but dies at `.2`.
