# Proof of `B05-FIXED-SHARED-BLOCK-TRANSPORT-v1`

Let `X,U,V` be pairwise disjoint, `|X|=k`, and let `f(X,U),g(X,V)` be
Boolean.  All expectations are uniform and all logarithms in `q` are base
two.

## Scalar facts

For `0<t<=1`,

\[
q'(t)=\log_2(1/t)+1/\ln2>0,
\qquad q''(t)=-1/(t\ln2)<0.
\]

Thus `q` is increasing and concave on `[0,1]` (continuously extended at
zero).

## Product inequality

For a base set `S subset U`, define

\[
F_S(\xi)=E_u[f(\xi,u)\chi_S(u)].
\]

Its Walsh coefficients on `X` are `fhat(S union A)`, `A subset X`; hence

\[
E_\xi F_S(\xi)^2=E_X^f(S). \tag{P1}
\]

Define `G_T` analogously.  For `h=fg` and `i in U`, its conditional
`i`-coefficient equals `F_{i}(xi)G_empty(xi)`.  Because `g` is Boolean,
`|G_empty(xi)|<=1`, and therefore

\[
\sum_{A subset X} hhat(i union A)^2
=E_\xi F_i(\xi)^2G_empty(\xi)^2
<=E_X^f(i). \tag{P2}
\]

In particular `hhat(i)^2<=E_X^f(i)`, so monotonicity of `q` pays the
singleton.  The argument for `j in V` is symmetric.

For the empty/private orbit,

\[
E_X^h(empty)=E_\xi F_empty(\xi)^2G_empty(\xi)^2
<=min(E_X^f(empty),E_X^g(empty)). \tag{P3}
\]

Each of the `k` shared singleton coefficients is one component of this orbit.
Monotonicity of `q`, followed by summation over the shared coordinates, gives
the `k q(min)` term.  Adding the private terms proves (3.1), and (3.2) follows
by discarding the minimum and adding nonnegative empty-orbit credit.

## Full revelation

For `i notin X`, restriction to `X=xi` gives

\[
fhat_xi(i)=sum_{A subset X} fhat(i union A) chi_A(xi). \tag{R1}
\]

Parseval says `E_xi fhat_xi(i)^2=E_X^f(i)`.  Jensen and concavity of `q`
give

\[
E_xi q(fhat_xi(i)^2)<=q(E_X^f(i)). \tag{R2}
\]

Sum over all unrevealed coordinates to prove (3.3).

## Sequential revelation

Fix `x in X` and put `X'=X-{x}`.  For a base set `S` disjoint from `X`,
write

\[
a_B=fhat(S union B),\qquad
b_B=fhat(S union B union {x}),\quad B subset X'.
\]

After restriction `x=sigma`, the child orbit energy is

\[
Z_sigma(S)=sum_{B subset X'}(a_B+sigma b_B)^2.
\]

Consequently

\[
E_sigma Z_sigma(S)=sum_B(a_B^2+b_B^2)=E_X^f(S). \tag{S1}
\]

Jensen yields `E_sigma q(Z_sigma(S))<=q(E_X^f(S))` for each private
singleton base.  For `S=empty`, multiplication by the child's weight `k-1`
and the inequality `k-1<=k` give the parent's empty-orbit term.  Summing proves
(3.4).  Induction proves contraction under any full reveal order.

No Boolean-specific fact beyond the pointwise bounds on conditional means is
hidden in the proof; Booleanity guarantees those bounds uniformly for every
terminal core and bias.

