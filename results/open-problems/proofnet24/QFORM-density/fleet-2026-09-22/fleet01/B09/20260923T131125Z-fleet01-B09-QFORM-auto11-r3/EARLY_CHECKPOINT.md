SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T13:11:25Z.
attacking: the aggregate-heavy-row branch — prove a pay-or-contract deletion identity that either produces a rank-three original-coordinate cross payment or contracts the arbitrary-curvature obstruction without square-root loss.

# Early substantive checkpoint — exact deletion identity and pay-or-contract step

Work in the literal two-hub setup from fleet01/B09 r2. Let `H={h1,h2}` and let `R` be the current active leaf set. Write `C=A[R,H]` and `D=A[R,R]`. For every distinguished leaf `k in R` and every three-set `T subset R\{k}` define

`w(k,T)^2 = det([C_T^T ; D[k,T]])^2`.

Define the aggregate singleton third-volume

`S(R)=sum_(k in R) sum_(T subset R\{k}, |T|=3) w(k,T)^2`,

the distinguished-singleton mass

`G_i(R)=sum_(T subset R\{i}, |T|=3) w(i,T)^2 = Gamma_i(R)^2`,

and the row-participation mass

`R_i(R)=sum_(k in R\{i}) sum_(T subset R\{k}, |T|=3, i in T) w(k,T)^2`.

Then there is the exact physical-coordinate deletion identity

`boxed: S(R\{i}) = S(R) - G_i(R) - R_i(R).`                 (CP1)

Indeed every determinant term in `S(R)` belongs to exactly one of three disjoint classes: `k=i`; or `k!=i` and `i in T`; or neither, in which case it is exactly a term of `S(R\{i})`. No matrix approximation, distributional hypothesis, or rotation is involved.

Now use Bernoulli coloring with a leaf put on the promoted side `K` with probability `p=1/4` and on the retained side `I` with probability `3/4`. A term `(k,T)` appears in the anchored physical cross-cut determinant family exactly when `k in K` and all three rows of `T` lie in `I`; this has probability

`c=p(1-p)^3=27/256`.

Hence some literal source-coordinate cut satisfies `Z>=c S(R)`. Fix row-marginal cutoff `h=2/3`. If all selected determinant-family row marginals are `<=h`, the sharp fractional three-volume theorem applies with `q=4/3` and gives a continuous density and direct linear interval bound

`||p_Q||_infinity <= C_diff S(R)^(-1/6)`,

`C_diff = [3e/((3-8/3)sqrt(4/3))] (256/27)^(1/6)
        = 30.8233844570...`.

If the row-marginal gate fails, there is a literal physical leaf `i` with

`R_i(R) > h Z >= h c S(R) = (9/128) S(R)`.                 (CP2)

If simultaneously

`G_i(R)=Gamma_i(R)^2 >= (9/128) S(R)`,

then elevating `i` to the cross side gives an actual original-coordinate rank-three cut whose third singular product is `Gamma_i(R)`. The completed grouped rank-three cross theorem gives

`||p_Q||_infinity <= 3e Gamma_i(R)^(-1/3)
                   <= 3e (128/9)^(1/6) S(R)^(-1/6)
                   = 12.6933711829... S(R)^(-1/6)`,

continuously and with the same coefficient times interval length.

Otherwise condition on the single ORIGINAL coordinate `X_i`. This preserves product structure on the remaining leaves, retains their whole quadratic block exactly, and merely creates affine terms. By (CP1)-(CP2), regardless of the size of `G_i`,

`boxed: S(R\{i}) < (119/128) S(R).`                         (CP3)

Thus every unresolved aggregate-heavy row gives an exact PAY-OR-CONTRACT step: either a direct O(|I|) density payment through a real rank-three physical cross cut, or a one-coordinate conditioning that contracts the aggregate third-volume obstruction by a universal factor while retaining arbitrary complementary curvature.

This does NOT yet close the full theorem: after repeated conditioning the aggregate can become small, and one may not infer that a small matrix residual is a small random quadratic error on arbitrary unbounded product inputs. The next implication is to couple the contraction alternative to the third spectral resource (or an already-paid physical-pair/ridge/grouped-square exit) before the aggregate is exhausted.
