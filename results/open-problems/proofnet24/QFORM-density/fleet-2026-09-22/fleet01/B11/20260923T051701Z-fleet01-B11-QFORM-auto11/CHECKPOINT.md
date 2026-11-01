SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T05:17:01Z.
attacking: opposite-sign pair plus an overlapping independent scalar bank: complete the scalar square first, then pay the exact rank-two Schur half-Riesz potential without rotating the product law.

# Early substantive checkpoint

The designated fleet02/B11 theorem at `math-open-problems@f2835c54b9f384f8f83e34c46bef5c40953e32a7` pays the disjoint case

`U^T B U + affine(U) + dW^2+2rW`,

where `U=(X1,X2)` consists of two original independent coordinates and `W` is independent of `U`, by convolving the rank-two half-Riesz receiver with the one-sided square kernel. Its remaining gap asks what survives when the third spectral direction overlaps the pair.

The first exact implication is that arbitrary quadratic cross coupling with the independent scalar can be absorbed without rotating the product law. Let

`H=[[B,c],[c^T,d]]`, `d!=0`,

and

`Q=U^TBU+2W c^T U+dW^2+ell^TU+2rW+q`,

where `W` is independent of `U` and has density cap `L`. Completing the square ONLY in the scalar `W`, conditional on the original `U`, gives

`Q=d(W+(c^TU+r)/d)^2 + U^T S U +(ell-2rc/d)^TU + q-r^2/d`,

with the exact Schur matrix

`S=B-cc^T/d`, `det H=d det S`.

The shift of `W` depends on `U`, so the shifted scalar is not independent of `U`; independence is neither claimed nor needed. Conditional on `U=u`, its density cap is still exactly `L`, hence the pushforward by `d z^2` has the uniform one-sided kernel bound

`p_{d(W+a(u))^2 | U=u}(y) <= L |d|^(-1/2)|y|^(-1/2)`

on the appropriate half-line. Therefore

`p_Q(t) <= L|d|^(-1/2) E |P_S(U)-t'|^(-1/2)`,

where `P_S` is the Schur-complement quadratic plus affine term. If `H` is invertible, then `S` is invertible. Applying the completed rank-two affine half-Riesz theorem in the two ORIGINAL variables gives

`||p_Q||inf <=16 sqrt(30) L |d|^(-1/2)|det S|^(-1/4)
               =16 sqrt(30) L (|d||det H|)^(-1/4)`.

For a normalized linear form `W` on a disjoint original-coordinate bank, `L<=sqrt(2)`, hence

`||p_Q||inf <=16 sqrt(60)(|d||det H|)^(-1/4)`.

Signature tracking is exact: if `H` has inertia `(2,1)` and `d>0`, Haynsworth inertia additivity forces `S` to have inertia `(1,1)`; if `H` has inertia `(1,2)` and `d<0`, the same conclusion holds. Thus a majority-sign scalar pivot leaves precisely the opposite-sign rank-two receiver. Its density may retain the logarithmic `2XY` singularity, but its half-order potential is finite, and the third square kernel consumes that potential.

Still to check before final report: source-level constant/provenance, a concrete target-valid cross-coupled family with exact spectrum and an actual use of both the designated fleet02/B11 theorem and the mandatory newest-Claude ruled one-sheet theorem, plus final control/correction refresh.
