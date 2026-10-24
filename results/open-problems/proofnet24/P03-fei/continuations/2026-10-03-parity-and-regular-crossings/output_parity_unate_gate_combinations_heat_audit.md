# Independent analytic audit of output parity of unate-gate combinations

Date: 2026-10-02. **PASS.** I read the complete separate
[proof](output_parity_unate_gate_combinations_fei_proof.md), including its
more general influence-vector formulation, generic full-entropy bound,
real threshold optimization, differing unate orientations, shared inputs
and scope limitations. This is an internal mathematical audit, not a
priority certificate or external review.

For any Boolean `g`, parity multiplication preserves entropy and gives
`I(chi_T g)=ell+sum_outside Ii(g)-sum_inside Ii(g)`. If the Euclidean
influence-vector norm is at most `M`, Cauchy--Schwarz therefore yields
`I(chi_T g)>=ell-M sqrt(ell)`. This uses no monotonicity assumption.

The universal entropy estimate is independently valid: if `r` is the
minority density and `v=4r(1-r)`, splitting the empty Fourier mass gives
`H<=h_2(v)+vn`. For `r<=1/4`, the entropy upper bound
`h_2(v)<=v[log(1/v)+loge]` becomes at most
`v log(1/r)` because `4(1-r)>=3>e`. For `r>=1/4`, it is enough that
`h_2(v)<=1<=4r log(1/r)`. Hence `H<=8nr`, while Fourier Poincare gives
`I>=2r`, so `H<=4nI`. This includes the empty spectral atom and handles
constants before division. The other universal bound, `H<=n`, follows
from the number of spectral indices.

I rederived the exact transition point. With
`y=(M+sqrt(M^2+1))/2` and `t=y^2`, we have `y>M` and
`t-M sqrt(t)=y(y-M)=1/4` exactly. For `ell<=t`, `H/I<=4(q+ell)` is at
most `4(q+t)`. For `ell>=t`, the lower bound for influence is positive
and increases. The derivative numerator of
`(ell+q)/(ell-M sqrt(ell))` is

\[
 -\frac M2\sqrt\ell-q\left(1-\frac{M}{2\sqrt\ell}\right)<0
\]

for `M>0`, since `sqrt(ell)>=y>M`. The ratio is thus at most its value
`4(q+t)` at `t`. Optimizing over real `ell` safely bounds integer subset
sizes. When `M=0`, zero coordinate influences imply `g` is constant by
cube connectivity, so the proof correctly handles that case separately.

For every unate gate, orienting each coordinate independently gives
`abs(ghat({i}))=Ii(g)`, and Parseval yields
`sum_i Ii(g)^2<=Var(g)<=1`. Gate orientations need not be compatible:
only the squared identity is used. If the arbitrary outer Boolean output
changes on an edge, at least one gate changes there. Thus the pointwise
union bound and the Euclidean triangle inequality give

\[
 \|(I_i(F(g_1,\ldots,g_m)))_i\|_2
 \le\sum_j\|(I_i(g_j))_i\|_2\le m.
\]

No independence or disjoint-input premise enters this step. The stronger
choice `M=sum_j sqrt(Var(g_j))` is also justified. Substitution establishes
the displayed theorem with constant `4(q+t_m)`, and full parity has
constant `(m+sqrt(m^2+1))^2`.

All LTF gates are unate individually; unrelated weight orientations,
biases and complete input overlap are permitted. Removing constant gates
does not change the Boolean output after fixing their outer arguments.
With no remaining gates the output is constant, as stated.

The theorem controls **parity outputs** with bounded missing-coordinate
count `q`. Setting `T` empty leaves `q=n` and does not prove an ordinary
FEI theorem for the unmodulated gate combination. It does not claim
general overlapping-composition closure or biased-product-input FEI.
These restrictions are explicitly correct. The sharper unate single-gate
parity proposition is separately audited and is not used to justify an
ordinary gate-combination claim.

This audit is analytic; an author checker is supplementary and its
execution is recorded by the author/root. No universal conclusion is
inferred from finite tests. No historical novelty is asserted here.
