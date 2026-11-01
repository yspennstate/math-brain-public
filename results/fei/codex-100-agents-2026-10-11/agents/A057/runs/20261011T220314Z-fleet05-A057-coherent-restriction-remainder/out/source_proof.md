# Coherent balanced composition and a narrow remainder-bound obstruction

## Scope and conclusion

The proposed composition identity is correct for Boolean sign functions on
disjoint input blocks when every inner function is balanced. The proposed
universal estimate `R <= C q alpha^2` is false, already with the fixed two-bit
AND outer function and a realizable balanced-inner family. This is only an
obstruction to that remainder estimate: the selected full-composition
coordinate ratio in the family tends to zero. It is not an FEI counterexample,
not an all-coordinate obstruction, and not a novelty claim.

All entropies below use natural logarithms. Zero-weight logarithmic terms are
zero by continuity. Input characters use signs in `{-1,+1}`.

## 1. Definitions and disjoint spectral bookkeeping

Let `F=g(h_1,...,h_m)`, with Boolean sign functions `g,h_1,...,h_m`; assume the
inner input blocks are pairwise disjoint and `E h_l=0` for every `l`. Fix a leaf
coordinate `i` in block `j`. Write the outer decomposition

`g(y)=a(y_-j)+y_j b(y_-j)`.

Here `a=(g(+1,y_-j)+g(-1,y_-j))/2` and
`b=(g(+1,y_-j)-g(-1,y_-j))/2`. Booleanity gives pointwise
`a b=0` and `a^2+b^2=1`. For their Fourier vectors `(a_T),(b_T)` on the
remaining outer variables, put

`q=Inf_j(g)=sum_T b_T^2`,

`sum_T a_T^2=1-q`, and `sum_T a_T b_T=0`.

For any coefficient vector `v`, define its unnormalized spectral entropy by

`Eraw(v)=sum_T v_T^2 ln(1/v_T^2)`.

Let `A_T=sum_(l in T) H(h_l)`. Balancedness means that every Fourier term of
`h_l` uses a nonempty subset of block `l`. Thus different outer frequency
sets `T` occupy disjoint physical spectral sectors, even if individual
coefficients have signs. Products across disjoint blocks have product spectra.
The exact raw tensor identity is

`Eraw(v tensor w)=||w||_2^2 Eraw(v)+||v||_2^2 Eraw(w)`.

Applying it sector by sector gives

`H(F)=Eraw(a)+Eraw(b)+q H(h_j)+sum_T (a_T^2+b_T^2) A_T`.       (1)

Constant frequencies are included throughout.

## 2. Influence and singleton coefficient

Let `alpha=hat h_j({i})`. The physical derivative

`delta_i h_j=(h_j|_(x_i=+1)-h_j|_(x_i=-1))/2`

takes values in `{-1,0,+1}`, has mean `alpha`, and has mean absolute value
`Inf_i(h_j)`. In particular,

`|alpha| <= Inf_i(h_j)`.                                      (2)

Flipping the leaf changes `F` precisely when it changes `h_j` and the outer
coordinate `j` is pivotal for the other inner outputs. Those two events depend
on disjoint blocks; the other inner outputs are independent fair signs. Hence

`Inf_i(F)=q Inf_i(h_j)`.                                      (3)

This statement includes the zero-influence cases without dividing by zero.

## 3. Exact physical-child masses and phase coherence

For `s=+1,-1`, write `h_s=h_j|_(x_i=s)`. Balancedness of `h_j` gives
`E h_s=s alpha`. Let `nu_s` be its nonconstant Fourier vector. Parseval gives

`||nu_s||_2^2=1-alpha^2`,

`Eraw(nu_s)=H(h_s)-alpha^2 ln(1/alpha^2)`.                      (4)

The composition child has two disjoint spectral sectors: no nonconstant
block-j frequency, with outer vector `a+s alpha b`; and a nonconstant block-j
frequency, with outer vector `b` tensored with `nu_s`.

The raw squared mass in these sectors is respectively
`||a+s alpha b||_2^2=1-q+q alpha^2` and `q(1-alpha^2)`, summing to one.
For each individual other-outer frequency `T`, the coefficient multiplying
its other-block entropy `A_T` is

`(a_T+s alpha b_T)^2+(1-alpha^2)b_T^2`

`= a_T^2+b_T^2+2s alpha a_T b_T`.                              (5)

The interference term in (5) cannot be discarded in one child. It cancels
only after the fair average over `s`. Applying the raw tensor identity gives

`H(F_s)=Eraw(a+s alpha b)+(1-alpha^2)Eraw(b)+q Eraw(nu_s)`

`       +sum_T [a_T^2+b_T^2+2s alpha a_T b_T] A_T`.             (6)

Subtract the average of (6) from (1), using (4), to obtain

`D_i(F)=q D_i(h_j)+R(alpha)`,                                  (7)

where

`R(alpha)=q alpha^2 ln(1/alpha^2)+Eraw(a)+alpha^2 Eraw(b)`

`         -[Eraw(a+alpha b)+Eraw(a-alpha b)]/2`.                (8)

Here `D_i` always means parent spectral entropy minus the fair average of the
two physical restriction entropies. Equation (8) retains signed Fourier
coefficients inside `a±alpha b`; replacing them by separate squared masses
would lose coherence.

## 4. Remainder as an equal-mass raw entropy decrement

Consider the generally real-valued noisy outer function

`w(y)=a(y_-j)+alpha y_j b(y_-j)`.

Its Fourier vector consists of `a` and `alpha b`, so

`Eraw(w)=Eraw(a)+alpha^2 Eraw(b)+q alpha^2 ln(1/alpha^2)`.

Its restrictions have vectors `a±alpha b`. Thus (8) is exactly the raw
physical entropy decrement of `w`. Orthogonality `sum_T a_T b_T=0` implies
that the parent and both children have common squared mass

`M=1-q+alpha^2 q`.                                            (9)

For `M>0`, divide all functions by `sqrt(M)`. Their spectral probabilities
are normalized. Let

`P(T,0)=a_T^2/M`, `P(T,1)=alpha^2 b_T^2/M`,

`P_T=P(T,0)+P(T,1)`, and `P_T^±=(a_T±alpha b_T)^2/M`.

Both `P^+` and `P^-` are probability distributions and their average is `P_T`.
The entropy chain rule yields

`H(P(T,e))=H(P_T)+B_i`,

`B_i=sum_T P_T h_nat(P(T,1)/P_T) >= 0`,

with zero-mass terms omitted. Define the fair Jensen–Shannon divergence

`JS=H(P_T)-[H(P^+)+H(P^-)]/2 >= 0`,

where nonnegativity is entropy concavity. The common raw scaling term
`M ln(1/M)` cancels, leaving

`R=M(B_i+JS) >= 0`.                                           (10)

If `M=0`, (9) forces `q=1, alpha=0`, and `a=0`; the noisy outer and both
children vanish, and `R=0`. No normalization is performed in that case.
This is an application of elementary spectral entropy bookkeeping, not a new
entropy inequality.

## 5. Endpoint checks

- `q=0`: then `b=0`, so `R=0`, `Inf_i(F)=0`, and `D_i(F)=0`
- `alpha=0`: the two coherent vectors both equal `a`, so `R=0` and `D_i(F)=q D_i(h_j)`
- `alpha=±1`: Booleanity implies `h_j=±x_i`; its children are constants, `D_i(h_j)=0`, and `R` is exactly the physical decrement of outer coordinate `j` in `g`. The child nonconstant block-j mass is zero, and the formula remains valid by continuity

These are algebraic endpoint statements, not ratio definitions at zero
influence.

## 6. Fixed AND outer: no universal R <= C q alpha^2

Use `g(y_1,y_2)=-1/2+y_1/2+y_2/2+y_1 y_2/2`, the sign AND function that is
`+1` only when both input signs are `+1`. For `j=1`,

`a=(-1/2,1/2)`, `b=(1/2,1/2)`, `q=1/2`,

`Eraw(a)=Eraw(b)=ln(2)`.

For `|alpha|<1`, direct substitution and cancellation of the `ln(2)` terms
in (8) gives the exact even expression

`R(alpha)=(alpha^2/2)ln(1/alpha^2)`

` +[(1-alpha)^2 ln(1-alpha)+(1+alpha)^2 ln(1+alpha)]/2`.        (11)

Let the second line of (11) be `S(alpha)`. It is even and analytic near zero,
with `S(0)=S'(0)=0` and

`S''(alpha)=3+ln(1-alpha^2)`.

Consequently

`R(alpha)=(alpha^2/2)ln(1/alpha^2)+(3/2)alpha^2+O(alpha^4)`,

`R(alpha)/(q alpha^2)=ln(1/alpha^2)+3+O(alpha^2) -> +infinity`. (12)

This asymptotic follows analytically, not by extrapolating the finite table.
It disproves a fixed universal `C` for the proposed remainder estimate once
arbitrarily small nonzero realizable `alpha` are supplied.

## 7. Realizable balanced family and its benign full-coordinate ratio

For `n>=3`, start with parity on `n` signs and flip its values at a pair of
adjacent inputs differing only in coordinate `i`. Write the other signs as
`z`, and let `v` be their fixed value on that pair. The result has the exact
form

`h_n(x_i,z)=x_i u_n(z)`,

`u_n(z)=product_r z_r * [1-2*1_(z=v)]`.

It stays Boolean and balanced. Since parity on the `n-1` other signs has
zero mean,

`alpha=E u_n=-2^(2-n) product_r v_r`, so `|alpha|=2^(2-n)`.

Every i-edge is bichromatic, giving `Inf_i(h_n)=1`. The parent spectrum is
the spectrum of `u_n` shifted to contain `i`; the two child spectra are those
of `±u_n`. All three entropies agree, so `D_i(h_n)=0` exactly.

Compose with the AND outer and an independent fair one-bit second inner.
Equations (3) and (7) give `Inf_i(F_n)=1/2` and `D_i(F_n)=R(alpha)`, hence

`D_i(F_n)/Inf_i(F_n)=alpha^2 ln(1/alpha^2)+3alpha^2+O(alpha^4) -> 0`.

Thus (12) is not an exploding full-coordinate ratio. In this example
`|alpha|` tends to zero while the inner influence stays one; confusing the
singleton Fourier mass `alpha^2` with that influence creates the false
counterexample interpretation.

## 8. Restrictions and remaining scope

Whenever `alpha != 0`, the physically restricted inner functions have means
`±alpha`, so they are not balanced. The balanced-block hypothesis is therefore
not preserved by arbitrary physical restriction. Equations (7)–(8) alone are
not a restriction-closed reduction of full FEI: biased descendants still need
to be treated. The nonnegative remainder also needs an appropriate payment;
nonnegativity does not furnish an upper bound.

No inference here resolves FEI, rules out every good-coordinate route, proves
an all-coordinate counterexample, establishes novelty, or demonstrates a
held-out benchmark benefit. All original files remain local at this stage.

