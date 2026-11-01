# HARD7-03 idea extension before checker — complete the center zero-gap family

Runtime identification: GPT-5.6 Sol; reasoning level `UNVERIFIED`, not claimed GPT-6 maximum.

The preceding idea note isolates the right near-edge structural equality event. Before committing a checker, extend the same mechanism to the center triple `d=0`, where there are two disjoint orientations.

Let

- `S_{-1}=max(Y_{-2},Y_{-1},Y_0)`,
- `S_0=max(Y_{-1},Y_0,Y_1)`,
- `S_1=max(Y_0,Y_1,Y_2)`.

Put `M=max(Y_0,Y_1)` and `L=max(Y_{-1},Y_2)`.

On

`E_center,left = { Y_{-2} > M > L }`

we have `S_{-1}=Y_{-2}>S_0=S_1=M`, hence `(u,v)=(Y_{-2}-M,0)`. Reflection gives the disjoint event

`E_center,right = { Y_2 > max(Y_{-1},Y_0) > max(Y_{-2},Y_1) }`,

which yields the reflected zero-gap orientation. The two events are disjoint because the left event forces `Y_{-2}>Y_2`, while the right event forces `Y_2>Y_{-2}`.

These events are also disjoint from the previously corrected strict mixed-sign center branches: the old left-oriented strict branch has the intermediate predecessor strictly above the common-window maximum, whereas the new boundary branch has that ordering reversed.

For the left event, condition on the first layer. Write

`sU=A_{-1}`, `s0=max(A_{-1},A_0,A_1)`, `s1=max(A_0,A_1)`,
`ell1=max(A_{-1},A_0)`, `ell2=A_1`.

Then `M=max(s0+E_0,s1+E_1)` is always at least `s0`, and all other shifts are at most `s0`. Thus on `Y_{-2}>M>L` the pure-tail simplification from the near-edge note applies again. For

`T_r^c = E[e^{theta M-r(Y_{-2}-M)}; Y_{-2}>M>L]`

one gets exactly `T_r^c=T_0^c/(1+r)`, so the boundary bonus is

`C_center0 = theta*T_0^c*(1/b^2-1/c^2)>0`.

To evaluate `T_0^c`, use for `m>=s0`

`f_M(m)=e^{s0-m}+e^{s1-m}-2e^{s0+s1-2m}`

and

`P(L<m)=(1-e^{ell1-m})(1-e^{ell2-m})`,
`P(Y_{-2}>m)=e^{sU-m}`.

Expanding the three-term max density against the four-term lower-max CDF produces twelve exponential monomials. Each integrates explicitly from `m=s0`; on each of the six first-layer order cones the result is a rational product of gap rates. Reflection supplies a factor two.

If both the near-edge and center exact integrals are positive, the new four-step envelope is the 19:21Z carry-in envelope minus

`2*(C_near0+C_center0)/(1-theta)`.

This would complete the positive-measure structural `one gap = 0, the other > 0` correction family at the two near-edge and the two central orientations, while preserving the already archived edge correction.