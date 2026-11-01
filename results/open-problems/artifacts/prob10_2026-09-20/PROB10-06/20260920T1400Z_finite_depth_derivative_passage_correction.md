# PROB10-06 finite-depth derivative-passage correction

This immutable artifact corrects one overstrong sentence in Section 5 of

`runs/prob10_2026-09-20/PROB10-06/20260920T1350Z_branch_gap_logderivative_bridge_4e2c9a71.md`.

The report says after defining the infinite-depth source bound `A` that `E U_N <= A+rho E U_{N-1}`. That statement need not hold at the first finite depths because the terminal approximation starts from `B_0=1`, whereas the sharper pathwise bound `B<=(3-lambda)/3` is an **infinite-depth** bound. The final theorem and exact checker do not require that finite-depth strengthening. The rigorous passage is as follows.

## 1. Truncation contraction is valid at finite depth

Couple `B_N downarrow B` on one tree. For

`Phi(s)=s/(lambda+s)`,

`partial Phi/partial B_i = lambda/(lambda+sum_j B_j)^2`.

Along the segment between finite-depth children and infinite-depth children, every child escape is at least its infinite-depth value. Therefore the derivative coefficient is at most the coefficient obtained after replacing the sibling escapes by their infinite-depth values and dropping the distinguished child's own nonnegative escape. The reciprocal-Jensen `K_1,K_2` bounds in the report apply to those infinite siblings. Hence the same exact

`rho=(1-p)2K_1(lambda)+p3K_2(lambda)<49/50`

controls the finite-depth difference:

`e_{N+1}:=E(B_{N+1}-B) <= rho e_N`, `e_0<=1`.

Thus

`E(B_N-B)<=rho^N<=(49/50)^N`.

This part of the report needs no change.

## 2. Uniform finite-depth derivative bound uses a crude source term

Let `U_N=-partial_lambda B_N`. Differentiating the finite recursion gives

`U_{N+1}=S_N/(lambda+S_N)^2`
`+lambda sum_i U_{N,i}/(lambda+S_N)^2`.

The elementary inequality

`s/(lambda+s)^2 <= 1/(4lambda)`

holds for every `s>=0`. The child-derivative coefficient is controlled by the same finite-depth argument in Section 1, so on the whole new rectangle

`E U_{N+1} <= 1/(4lambda)+rho E U_N`.

Since `lambda>=107/50` and `rho<49/50`, this gives a uniform-in-`N` `L^1` bound on `U_N`. No use of `B<=(3-lambda)/3` is made here.

## 3. `U_N` is `L^1` Cauchy

The source map

`h(s)=s/(lambda+s)^2`

has `|h'(s)|<=1/lambda^2` for `s>=0`. The child coefficient

`r(s)=lambda/(lambda+s)^2`

has `|r'(s)|<=2/lambda^2`.

Also the exact logarithmic-elasticity recursion, or direct induction from the derivative recursion, gives the crude pathwise finite-depth estimate

`0<=U_N<=N/lambda`.

Let

`w_N=E|U_N-U_{N-1}|`,
`b_N=E(B_{N-1}-B_N)`.

Monotonicity gives `b_N<=e_{N-1}<=rho^{N-1}`. Subtract the two finite-depth derivative recursions. The terms containing `U_{N-1,i}-U_{N-2,i}` are bounded, after dropping the distinguished child exactly as in Section 1, by `rho w_{N-1}`. The source-map difference is at most a constant times `b_N`. The change in derivative coefficients is at most a rectangle-uniform constant times the child escape difference; multiplying by the crude `U_{N-1}<=N/lambda` bound gives at most `C N b_{N-1}`. Consequently, with a finite constant `C` depending only on the fixed rectangle,

`w_N <= rho w_{N-1}+C N rho^{N-2}`.

Iteration gives `w_N<=C'(1+N^2)rho^{N-2}`. Since `rho<1`, `sum_N w_N<infinity`; hence `U_N` is Cauchy in `L^1`, uniformly on the compact checker rectangle.

Therefore `U_N -> U` in `L^1`. Together with uniform geometric convergence of `B_N`, the standard uniform-derivative theorem applies to `E B_N` and to each finite product/ratio defining `c_2,c_3,J`: the infinite-depth quantities are differentiable and their derivatives are obtained by the limits used in the report.

## 4. The sharp source bound is applied only after the limit

For the infinite escape `B`, the essential-supremum recursion gives

`B<=u=(3-lambda)/3`.

Now pass to the infinite differentiated recursion. Its source expectation is bounded by

`A=(1-p)6(3-lambda)/(lambda+6)^2+p(3-lambda)/9`,

and the derivative term is bounded by the same `rho`, so only at this stage we use

`eta:=E U <= A+rho eta`,

hence

`eta<=A/(1-rho)`.

This is exactly the `eta` value used by the branch-gap checker. Thus the checker, branch-gap inequality, endpoint `lambda<=12/5` for `p>=3/4`, derivative margin `1/7290`, and truncation bound `(49/50)^N` remain unchanged.

Status remains **PARTIAL / OPEN parent**. This correction is preserved rather than rewriting the immutable report.