SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T17:08:21Z.
attacking: convert the newest account03/B15 countable heat core into a countable point-density core, then test whether algebraic genericity repairs the ruled physical-triple degeneration.

# Early checkpoint — point-density core and generic ruled-certificate obstruction

Status: full QFORM OPEN. This is a supporting reduction and a proof-interface obstruction, not a counterexample to the conjecture.

## 1. First unpaid implication

Let
\[
C_*:=\sup_{\substack{n\ge3,\ s_3(A)\ge1\\X_i\ \mathrm{independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty.
\]
The unpaid statement is `C_*<infinity`.

Use the completed account03/B15 result at `math-open-problems@a0ff8602933dff6df3182b969fec03af0f2dcc25`: if `R` is the class of finite unions of bounded rational half-open intervals of total length one, and `G_n` is the rational symmetric generic class (simple spectrum, all entries and all principal minors nonzero), then
\[
C_*=
\sup_{\substack{n\ge3,\ B\in G_n,\ s_3(B)>1\\E_i\in R,\varepsilon\in\mathbb Q_{>0},\ y\in\mathbb Q}}
\int_{\prod_iE_i}\gamma_\varepsilon(x^TBx-y)\,dx.
\tag{1}
\]

The completed fixed-instance account02/B15 theorem at `math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056` gives `p_{B,E}\in C_0(R) cap L^infinity(R)` for every core instance, since `rank(B)>=3`. The heat-height identity used by account03/B15 therefore gives
\[
\boxed{
C_*=\sup_{\substack{n\ge3,\ B\in G_n,\ s_3(B)>1\\E_i\in R,\ y\in\mathbb Q}}
p_{B,E}(y).
}
\tag{2}
\]
Indeed for each core instance the heat supremum is `||p||_infinity`, while continuity makes `sup_{y in Q}p(y)=||p||_infinity`.

Consequently, if the universal constant is false, there is a sequence of compact finite-fragment cap-one product laws, algebraically generic rational target matrices and rational centers `y_m` with continuous bounded output densities such that
\[
p_m(y_m)\to\infty.
\tag{3}
\]
Thus failure of the universal theorem cannot require a single target instance with an unbounded density: fixed-instance `C_0 cap L^infinity` already rules that out. It must be loss of uniformity along a sequence.

Continuity is used in (2) only to replace each already-defined essential norm by a rational pointwise supremum. It is not used to prove any height bound.

## 2. Genericity does not create a uniformly conditioned physical triple

For `m>=3` define
\[
A_m=2\,\operatorname{diag}\!\left(1,\frac1mJ_m,-\frac1mJ_m\right),
\]
where `J_m` is the all-ones matrix. Its three nonzero eigenvalues are `2,2,-2`, hence `s_3(A_m)=2`.

Every `3 x 3` principal block of `A_m` has smallest singular value at most `2/m`: a block containing the singleton and one coordinate from each bank is `diag(2,2/m,-2/m)`, while every other three-block is singular or has still smaller third singular value.

The generic rational set `G_{2m+1}` is dense. Choose
\[
B_m\in G_{2m+1},\qquad
\|B_m-A_m\|_{op}<\frac1{10m}.
\tag{4}
\]
Then Weyl gives
\[
s_3(B_m)>2-\frac1{10m}>1,
\tag{5}
\]
so `B_m` lies in the exact countable core, while for every physical triple `S`,
\[
\boxed{\sigma_{\min}((B_m)_{SS})\le\frac{21}{10m}.}
\tag{6}
\]
Thus the algebraic-generic reduction cannot be followed by an assertion that generic target matrices possess one universally conditioned physical triple.

## 3. Apply the completed ruled theorem to the obstruction

The completed ruled one-sheet theorem from the required Claude source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` says that for an invertible indefinite physical `3 x 3` block with eigenvalue magnitudes `lambda_1,lambda_2,mu` and signature `(2,1)`, conditioning on the outside original coordinates and completing the square pays the majority-side submeasure by
\[
\mu_+(I)\le C_S|I|,
\qquad
C_S=\int_0^{2\pi}
\frac{d\theta}{\sqrt{\lambda_2\mu\sin^2\theta+\lambda_1\mu\cos^2\theta+\lambda_1\lambda_2}}.
\tag{7}
\]
The displayed form is algebraically the source coefficient after cancelling the spectral prefactor.

For the generic matrices `B_m` above, the exact ruled certificate degenerates on every indefinite physical triple. If the triple contains the singleton coordinate, one eigenvalue has magnitude at most `3` and the other two at most `5/m`; hence the denominator squared in (7) is at most `55/m`, so
\[
C_S\ge2\pi\sqrt{m/55}.
\tag{8}
\]
If the triple avoids the singleton, all three eigenvalue magnitudes are at most `7/m`, so
\[
C_S\ge\frac{2\pi m}{\sqrt{147}}
\ge2\pi\sqrt{m/55}
\quad(m\ge3).
\tag{9}
\]
Therefore
\[
\boxed{
\inf_{\substack{|S|=3\\(B_m)_{SS}\ \mathrm{indefinite}}} C_S
\ge2\pi\sqrt{m/55}\to\infty,
}
\tag{10}
\]
with the infimum interpreted as `+infinity` if no indefinite physical triple exists.

This is not a large-density example. It says that even on the exact algebraically generic rational core, the direct proof interface “pick one physical triple and pay its majority side by the law-uniform ruled constant” has no universal certificate. Product aggregation must occur before reciprocal local curvature is paid, or the remaining minority/two-sheet geometry must be coupled to an aggregate structural resource.

## 4. Rough-input passage in the ruled theorem

For completeness, the rough bridge uses no continuity. Mollify the three active original-coordinate marginals: `f_i^(eta)=f_i*gamma_eta`. Independence and the cap `<=1` are preserved, and the three-variable product densities converge in `L^1`. For fixed outside coordinates the completion-of-square translation does not change this `L^1` distance. Deterministic quadratic pushforward and restriction to the majority event contract total variation, so the smooth one-sheet interval domination passes to arbitrary measurable cap-one marginals with the same `C_S`. Averaging the untouched outside product law preserves the interval bound.

The factor `1/2` in the ruled coarea parametrisation and the non-arclength factor `1/|v_theta|` are exactly the two constants encoded in (7); neither is replaced by a pointwise evaluation of an `L^infinity` projection representative.

Remaining gap: prove a uniform bound for (2), necessarily by an aggregate product-preserving mechanism robust to the generic family (4), with the minority/two-sheet obstruction kept explicit.
