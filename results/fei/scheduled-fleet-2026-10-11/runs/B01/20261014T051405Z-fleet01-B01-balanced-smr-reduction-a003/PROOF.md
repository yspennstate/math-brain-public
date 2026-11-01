# Balanced sublinear-terminal reduction for signed mismatch

All logarithms are base two.  Let

\[
p_f(S)=\widehat f(S)^2,\quad
\pi_f(S)=\sum_{T\supseteq S}p_f(T),\quad
U(f)=\sum_Sp_f(S)\log_2\frac{\pi_f(S)}{p_f(S)}.
\]

Write

\[
B(f)=\sum_iH(1_{i\in S}\mid S\setminus\{i\}),\qquad
M(f)=G(f)-B(f)=\sum_i(K_i-\Gamma_i).
\]

## 1. Disjoint products

If `f` and `g` use disjoint physical variables and `F=fg`, then

\[
p_F(A\cup C)=p_f(A)p_g(C),\qquad
\pi_F(A\cup C)=\pi_f(A)\pi_g(C).
\]

The logarithm in `U` therefore splits, so `U(F)=U(f)+U(g)`.  Restricting a
coordinate in the `f` block leaves the independent `g` factor in both
children, hence its `U` decrement is the decrement for `f`; similarly for
the other block.  Thus `G(F)=G(f)+G(g)`.  Spectral membership variables from
the two blocks are independent, so the conditional entropies defining `B`
also split.  Consequently

\[
I(F)=I(f)+I(g),\quad B(F)=B(f)+B(g),\quad M(F)=M(f)+M(g). \tag{1}
\]

For the `t`-fold disjoint tensor power,

\[
(U,I,G,B,M)(f^{\otimes t})=t(U,I,G,B,M)(f). \tag{2}
\]

## 2. Fresh-character balancing preserves the GU quantities

For a fresh sign `y`, define

\[
\mathcal Bq(y,x)=yq(x).
\]

This is balanced, and its only nonzero Fourier coefficients are

\[
\widehat{\mathcal Bq}(S\cup\{y\})=\widehat q(S). \tag{3}
\]

All spectral labels therefore contain `y`.  Equation (3) gives

\[
\pi_{\mathcal Bq}(S\cup\{y\})=\pi_q(S),
\]

so every nonzero summand in `U` is unchanged.  Hence

\[
U(\mathcal Bq)=U(q),\qquad I(\mathcal Bq)=I(q)+1. \tag{4}
\]

For the new coordinate, the two restrictions are `q` and `-q`; `U` is
sign-invariant, so `Delta_y U=0`.  For an old coordinate `i`, the two
children are the balanced lifts of the two children of `q`, and (4) for `U`
shows `Delta_i U(\mathcal Bq)=Delta_i U(q)`.  Therefore

\[
G(\mathcal Bq)=G(q). \tag{5}
\]

The membership bit of `y` is deterministic, so its contribution to `B` is
zero.  Conditioning an old membership bit on the always-present `y` changes
nothing.  Thus

\[
B(\mathcal Bq)=B(q),\qquad M(\mathcal Bq)=M(q). \tag{6}
\]

This extends the earlier `H,I` balancing ledger to the actual GU quantities
`U,G,B,M`.

## 3. The sufficient balanced target

Fix `0<eta<=1` and `0<=c<infinity`.  Let `(e_N)` be any real sequence with

\[
\frac{|e_N|}{N}\longrightarrow0. \tag{7}
\]

Assume that every balanced genuine Boolean sign `h` on every `N`-cube
satisfies

\[
\boxed{
M(h)+(1+\eta)U(h)\le cI(h)+e_N.
}\tag{BAL-SMR-o(N)}
\]

Let `f` be an arbitrary nonconstant Boolean sign on `n` inputs and put

\[
h_t=\mathcal B(f^{\otimes t}).
\]

This is a balanced Boolean sign on `N_t=tn+1` inputs.  Equations (2), (4),
and (6) turn `BAL-SMR-o(N)` into

\[
t\{M(f)+(1+\eta)U(f)\}
\le c\{tI(f)+1\}+e_{tn+1}. \tag{8}
\]

After division by `t`, (7) gives

\[
\frac{e_{tn+1}}t
=\frac{e_{tn+1}}{tn+1}\frac{tn+1}t\longrightarrow0.
\]

Letting `t` tend to infinity in (8) proves the exact universal estimate

\[
\boxed{M(f)+(1+\eta)U(f)\le cI(f).}\tag{SMR}_{c,\eta}
\]

Constants have `I=U=G=B=M=0`, so the conclusion holds for them without
division.  Conversely, universal exact `SMR` trivially implies
`BAL-SMR-o(N)` with `e_N=0`.  Thus the universal signed-mismatch target is
equivalent to its balanced version even after allowing an arbitrary
sublinear dimension terminal loss.

## 4. Consequence for GU and FEI

The reviewed inputs are

\[
G=B+M,\qquad B\le H,
\qquad H\le2(I-\operatorname{Var})+2U. \tag{9}
\]

Combining (9) with universal `SMR` gives

\[
G\le(c+2)I+(1-\eta)U-2\operatorname{Var}
\le(c+2)I+(1-\eta)U. \tag{10}
\]

Hence `BAL-SMR-o(N)` yields the admissible GU pair

\[
(a,b)=(c+2,1-\eta).
\]

The source-reviewed restriction induction then gives

\[
U\le\frac{c+2}{\eta}I,qquad
H\le\left(2+\frac{2(c+2)}{\eta}\right)I. \tag{11}
\]

No such `c,eta,e_N` has been proved here; (10)--(11) are conditional.

## 5. Sharp-helper obstruction survives balance and all sublinear terminals

Let `F` be the independently certified five-bit fair activation from B05/B19.
For `eta=1/4`,

\[
\delta=M(F)+\frac54U(F)-2I(F)
=0.0923435545007156\ldots>0. \tag{12}
\]

Set `H_t=\mathcal B(F^{\otimes t})`.  It is balanced on `5t+1` inputs and

\[
M(H_t)+\frac54U(H_t)-2I(H_t)=t\delta-2. \tag{13}
\]

The left side divided by `5t+1` tends to `delta/5>0`.  Therefore the
refuted `(c,eta)=(2,1/4)` helper cannot be repaired by restricting to
balanced functions or by adding any `o(N)` terminal allowance.  More
generally, the same witness forces

\[
c\ge\frac{M(F)+(5/4)U(F)}{I(F)}
=2.067158948727793\ldots \tag{14}
\]

for any `BAL-SMR-o(N)` theorem at `eta=1/4`.  This is a lower bound on this
proof route, not a universal upper bound and not an FEI counterexample.

