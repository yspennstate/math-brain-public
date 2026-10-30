SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T17:37:38Z.
attacking: the four-hub max-norm twist survivor by an exact residual-energy pair-count estimate that keeps the twist as a genuine quadratic term.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target: OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication after this checkpoint

`QFORM-SCALEFREE-FRAGMENTATION-OR-LOWRANK-GLUE-v1`: in the remaining at-most-four-hub chamber, combine the scale-normalized pair separation forced below with the partner's physical cross-rank collapse and the pinned D5 fifth-volume collapse, without imposing support diameter, moments, a fragment-count bound, or post-rotation independence. Otherwise construct a genuine unit-product-indicator counterexample respecting all three constraints.

## Exact diagonal-twist residual-energy estimate

Condition the at-most-four physical hubs from the preceding B13 hierarchical skeleton. On some hub fibre the slab ratio is at least the original `rho`; the leaf form is

`q(x)=x^T(D+S+E)x+l^T x+c`,

where `D` is diagonal, `rank S=d` and `E` is the genuine zero-diagonal twist. Assume `3<=d<=4` and the range projection of `S` has maximum physical coordinate leverage at most `1/2`. Put

`M_S = [4d/(d-2)] |pdet S|^(-1/d)`.

The source-proved range-curvature Fresnel--Brascamp--Lieb theorem applies to `D+S` with every affine term. For every deterministic centre `z`,

`q_z(x):=q(x)-(x-z)^T E(x-z)
        =x^T(D+S)x+(l+2Ez)^T x+c-z^TEz`

therefore has density at most `M_S`, uniformly in `z`.

Let `J` have length `L`, `S_J={q in J}`, and let the conditional fibre ratio be `rho_f=Pr(S_J)/L>=rho`. Then for every `delta>=0`,

`Pr(S_J and |(X-z)^TE(X-z)|<=delta) <= M_S(L+2delta)`.

Take an independent copy `X'`, set `z=X'`, integrate over `X' in S_J`, and divide by `Pr(S_J)^2`. This gives the exact pair-count bound

`Pr( |(X-X')^TE(X-X')|<=delta | X,X' in S_J )
 <= (M_S/rho_f)(1+2delta/L)
 <= (M_S/rho)(1+2delta/L).`

Hence the conditional median residual-energy scale obeys

`med |(X-X')^TE(X-X')|
 >= (L/2) (rho/(2M_S)-1)_+.`

If `epsilon=||E||_max`, then `|z^TEz|<=epsilon||z||_1^2`, so

`med [ ||X-X'||_1/sqrt(L) ]
 >= { [rho/(2M_S)-1]_+ /(2 epsilon) }^(1/2).`

Using the preceding B13 four-hub skeleton `epsilon<=C0/rho`, `C0=27 sqrt(3e)`, the survivor necessarily satisfies

`med [ ||X-X'||_1/sqrt(L) ]
 >= { rho [rho/(2M_S)-1]_+ /(2C0) }^(1/2).`

Thus the twist cannot be deleted, but high density forces a scale-free fragmentation/separation phenomenon in the actual slab. This statement is compatible with arbitrarily fragmented and unbounded supports and therefore does not assume away the extremal-product obstruction.

## Cross-rank consequence for the same genuine twist

For every disjoint physical leaf cut `I,J`, `A[I,J]=S[I,J]+E[I,J]` because `D` is diagonal. The designated partner's completed theorem gives

`s_3(A[I,J]) <= C3/rho`, `C3=9 sqrt(3e)`.

Since `rank S[I,J]<=4`, singular-value interlacing under a rank-four perturbation gives

`s_7(E[I,J]) <= C3/rho`.

The pinned Claude/Fourier D5 theorem also gives `s_5(A[I,J])<=C5/rho`, `C5=5sqrt(2e)`, hence

`s_9(E[I,J]) <= C5/rho`,

and, more strongly on the original physical block,

`e_5(A[I,J]^T A[I,J]) <= (C5/rho)^10`.

These are coefficient statements only; no transformed random coordinates are declared independent and no small quadratic remainder is discarded.
