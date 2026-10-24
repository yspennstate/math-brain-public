# Early substantive checkpoint — one-coordinate fractional regularity

Let `Q=X^TAX` under the target product law and suppose one original-coordinate diagonal pivot `a=A_ii` is nonzero. Conditioning on `W=X_{-i}` gives

`Q=a X_i^2+2 d(W) X_i+c(W)=a(X_i+d(W)/a)^2+C(W)`.

Because `X_i` is independent of `W` and its density is bounded by one, the conditional output density satisfies, for `a>0`,

`p_w(t) <= [a(t-C(w))]^{-1/2} 1_{t>C(w)}`

(and the reflected analogue for `a<0`). Hence with `nu=Law(C(W))`,

`p_Q(t) <= |a|^{-1/2} int |t-s|^{-1/2} 1_{sign(a)(t-s)>0} nu(ds)`.

For every measurable `E` of finite Lebesgue measure `m`, rearrangement of the one-sided kernel gives

`int_E (t-s)_+^{-1/2} dt <= int_0^m u^{-1/2}du=2 sqrt(m)`.

Therefore

`P(Q in E) <= 2 sqrt(|E|/|a|)`.

Consequently

`|{t:p_Q(t)>lambda}| <= 4/(|a| lambda^2)`

and `||p_Q||_{L^{2,infty}} <=2/sqrt(|a|)`. This is an original-coordinate product-preserving rough-law statement; arbitrary outside quadratic coefficients and cross couplings are retained through the moving critical value `C(W)`. It proves a precise target-level regularity statement but not the universal L-infinity target, because the exponent 1/2 is the sharp one-coordinate square singularity.

Next calculation in this run: compile this measurable-set bound with the completed account02/B15 majority one-sheet / two-sided minority-packing theorem at an actual heat-mode inequality, keeping continuity separate.
