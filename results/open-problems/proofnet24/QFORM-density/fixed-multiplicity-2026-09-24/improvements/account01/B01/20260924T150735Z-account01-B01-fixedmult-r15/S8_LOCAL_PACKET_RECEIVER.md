# account01/B01 r15 improvement — a local `s_3` theorem and a paid concentrated-overlap branch for `s_8`

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Pinned active paper: `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.

**Status:** proved supporting results. This note does **not** prove the full eight-eigenvalue theorem. It removes the concentrated single-overlap-packet branch from the remaining `s_8` problem and leaves a genuinely diffuse shared-anchor analytic endpoint.

The active normalized constants are

\[
 d=\frac3{40},\qquad p=\frac1{400},\qquad h=\frac2{25},\qquad \kappa=\frac4{625}.
\]

## 1. A finite-dimensional three-direction theorem

### Theorem `QFORM-LOCAL16-S3-DENSITY-400-v1`

Let `1<=m<=16`. Let `X_1,...,X_m` be independent real variables with densities at most `K`. Let `B=B^T in R^{m x m}` and let all affine terms be arbitrary. If

\[
 s_3(B)\ge s>0,
\]

then

\[
\boxed{
 \|p_{X^TBX+b^TX+c}\|_\infty<400\,\frac{K^2}{s}.
}
\]

This is a fixed-dimensional supporting theorem, not a lower-threshold theorem in arbitrary dimension.

### Proof

By the same scaling as the active paper it is enough to take `K=s=1`.

Call a scalar/pair a pivot using the active thresholds `d,p`. If `B` has no pivot, then

\[
 |B_{ii}|<d,\qquad |B_{ij}|^2<p+d^2=\frac{13}{1600}\quad(i\ne j).
\]

Hence

\[
 \|B\|_F^2
 <m\frac9{1600}+m(m-1)\frac{13}{1600}
 =\frac{13m^2-4m}{1600}.
\]

For `m<=16` this is at most

\[
 \frac{3264}{1600}=2.04<3.
\]

But `s_3(B)>=1` implies

\[
 \|B\|_F^2=\sum_js_j(B)^2\ge3,
\]

a contradiction. Thus `B` has a pivot.

#### Scalar pivot

Suppose `|B_{ii}|>=d`. Complete this literal original coordinate. The Schur child `S` has at least two eigenvalues of modulus at least one by the active Schur-count lemma. Also `dim S<=15`.

If `S` had no pivot, the same entry estimate would give

\[
 \|S\|_F^2
 <\frac{13(15)^2-4(15)}{1600}
 =\frac{2865}{1600}<2,
\]

contradicting `s_2(S)>=1`. Therefore `S` itself has a pivot.

If that child pivot is scalar, its next Schur remainder has at least one unit spectral direction. The active quarter-power/logarithmic-potential lemma and sharper scalar kernel therefore give the full half-potential bound

\[
 \sup_a\mathbb E|R-a|^{-1/2}
 \le 1+d^{-1/2}(J_0+2L_0),
\]

where

\[
 J_0=\pi+4\log2,\qquad L_0=4+4\log5.
\]

Applying the outer scalar profile gives

\[
 \|p_Q\|_\infty
 \le d^{-1/2}+\frac{J_0+2L_0}{d}<383.
\]

If the child pivot is a two-coordinate pivot, the active full-pair theorem gives

\[
 \sup_a\mathbb E|S-a|^{-1/2}<16p^{-1/4},
\]

so the outer scalar profile gives

\[
 \|p_Q\|_\infty<16p^{-1/4}d^{-1/2}<320.
\]

#### Pair pivot

If the original pivot pair is definite, direct conditioning gives

\[
 \|p_Q\|_\infty\le\pi p^{-1/2}<80.
\]

If it is indefinite, its Schur remainder retains at least one unit spectral direction because the original matrix has three. The active hyperbolic envelope plus quarter-power logarithmic-potential estimate is therefore exactly the same calculation as the final indefinite-pair branch of the nine-direction paper:

\[
 \|p_Q\|_\infty
 \le p^{-1/2}(6+\log16+L_0)+1/e<392.5.
\]

All alternatives are below 400. Rescaling gives `400 K^2/s`. QED.

### Why dimension 16 appears

The first no-pivot contradiction only needs the Frobenius upper bound to be below three and by itself remains valid through dimension 19. The scalar-pivot child, however, has only two guaranteed spectral directions; the corresponding no-pivot Frobenius contradiction is uniform through child dimension 15. This is why the complete two-level argument above is stated for `m<=16`.

## 2. Every nonzero overlap packet gives a concrete local receiver

Now work in the normalized **global no-pivot** chamber of the active paper. Take an invertible-seed overlap packet

\[
 p=(S,T,h),\qquad |S|=|T|=2,\quad S\cap T=\varnothing,
 \quad h\notin S\cup T,
\]

and set

\[
 \Delta_p=\left|\det A_{S\cup\{h\},\,T\cup\{h\}}\right|>0.
\]

Let `U=S union T union {h}` and `B=A[U,U]`, a literal `5 x 5` principal block. Global no-pivot entry bounds imply

\[
 \|B\|_F^2
 <5d^2+20(p+d^2)
 =\frac{305}{1600}=\frac{61}{320}.
\tag{2.1}
\]

The overlap determinant is a `3 x 3` minor of `B`. By the exterior-power/minor bound,

\[
 \Delta_p\le s_1(B)s_2(B)s_3(B).
\]

Moreover

\[
 s_1(B)s_2(B)
 \le\frac{s_1(B)^2+s_2(B)^2}{2}
 \le\frac{\|B\|_F^2}{2}<\frac{61}{640}.
\]

Consequently

\[
\boxed{
 s_3(B)>\frac{640}{61}\Delta_p.
}
\tag{2.2}
\]

Condition on every original coordinate outside `U`. The conditional five-coordinate quadratic polynomial has quadratic matrix exactly `B`; outside variables only change its affine terms. Applying Theorem `QFORM-LOCAL16-S3-DENSITY-400-v1` and (2.2) gives the dimension-free packet receiver

\[
\boxed{
 \|p_Q\|_\infty
 \le\frac{305}{8}\,\Delta_p^{-1}.
}
\tag{2.3}
\]

No shared-coordinate independence is invented: the entire five-coordinate packet is handled at once as a literal principal block.

## 3. The concentrated overlap branch of `s_8` is now paid

The active paper proves that in the normalized no-pivot `s_8(A)>=1` chamber, either `V_3>=kappa^3` (already paid by the order-three crossing density theorem), or

\[
 W:=W_{2,1}^{\times}(A)
 \ge W_0:=\frac{19424}{244140625}
 \approx7.9560704\times10^{-5}.
\tag{3.1}
\]

In the latter branch assign determinant-squared packet weights

\[
 w_p=\frac{\Delta_p^2}{W},\qquad\sum_pw_p=1.
\]

If one packet has `w_p>=omega`, then

\[
 \Delta_p\ge\sqrt{\omega W_0},
\]

and (2.3) yields

\[
\boxed{
 \|p_Q\|_\infty
 \le\frac{305}{8\sqrt{\omega W_0}}
 <4275\,\omega^{-1/2}.
}
\tag{3.2}
\]

In particular,

\[
\boxed{
 \max_p w_p\ge\frac1{64}
 \quad\Longrightarrow\quad
 \|p_Q\|_\infty<34200.
}
\tag{3.3}
\]

Thus the unresolved `s_8` endpoint can be restricted, without loss, to the genuinely diffuse packet regime

\[
\boxed{
 \max_pw_p<1/64.
}
\tag{3.4}
\]

This is a full-quantifier statement for that subbranch: all signs, all remaining spectrum, arbitrary dimension and arbitrary cap-one product laws are retained.

## 4. The determinant/entropy bill in the remaining diffuse branch is small

For completeness, the prior B01 five-role entropy argument is reproduced in the strengthened active `W_0` scale. Let

\[
 \alpha_i=\Pr_{p\sim w}\{i\in S\cup T\cup\{h\}\},\qquad \sum_i\alpha_i=5.
\]

Uniformly order the two elements of `S` and the two of `T`. The resulting five-role tuple has entropy `H(w)+log4`. Entropy subadditivity and concavity give

\[
 H(w)+\log4
 \le5H(\alpha/5)
 =5\log5-\sum_i\alpha_i\log\alpha_i,
\]

so

\[
 H(w)+\sum_i\alpha_i\log\alpha_i\le\log(5^5/4).
\tag{4.1}
\]

Since `Delta_p^2=w_pW`, at exponent `theta=1/2`,

\[
 \prod_p\Delta_p^{-w_p/2}
 \prod_i\alpha_i^{\alpha_i/4}
 \le\left(\frac{5^5}{4W}\right)^{1/4}
 \le\left(\frac{5^5}{4W_0}\right)^{1/4}
 <56.
\tag{4.2}
\]

Therefore packet cardinality and determinant entropy are quantitatively harmless at the new overlap scale. The remaining problem is genuinely analytic rather than combinatorial.

## 5. Exact remaining implication at multiplicity eight

After the active paper, the preceding local receiver, and (4.2), the no-pivot `s_8` terminal branch is reduced to:

1. `V_3<kappa^3`;
2. `W_{2,1}^cross>=W_0`;
3. every overlap packet has `w_p<1/64`;
4. determinant/entropy geometric cost is `<56`;
5. one must exploit the common physical anchor in the packets **without** conditioning away product structure and gain an integrable improvement beyond the critical `|t|^{-1}` endpoint.

Call this remaining gap

`QFORM-S8-DIFFUSE-SHARED-ANCHOR-LOG-REMOVAL-v2`.

A robust two-anchor cross pair alone cannot pay this gap: the existing rank-two counterexample shows that a small indefinite self-block plus robust cross map may still have logarithmically divergent density if the inherited Schur/spectral information is discarded. The surviving `s_8` proof must consume the overlap/spectral currency jointly.

## 6. Status

- `QFORM-LOCAL16-S3-DENSITY-400-v1`: **PROVED SUPPORTING THEOREM**.
- Local overlap packet receiver (2.3): **PROVED**.
- Concentrated overlap branch (3.2)–(3.3): **PROVED**.
- General multiplicity-eight theorem: **OPEN**.
- General multiplicity-three conjecture: **OPEN**.

The finite-dimensional theorem is explicitly a subclass statement and is not represented as a reduction of the arbitrary-dimensional spectral threshold.
