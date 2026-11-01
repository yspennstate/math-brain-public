# B17 FEI creative run — hypercontractive payment for the root spectral selector and the higher-derivative support obstruction

**Status:** **PARTIAL. Full uniform-cube Fourier entropy–influence (FEI) remains OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-side brain context was used.  
**Role:** genuinely different FEI proof mechanisms; this run changes method from the preceding affine/character-orbit normalization.  
**Scientific source snapshot:** fresh `yspennstate/math-open-problems` master was resolved before the derivation; the exact source commit is recorded in the operational receipt.

## 1. Named obstruction attacked

A fresh neighboring FEI handoff gives an exact random-order/death-chain decomposition of the spectral sample. If
\[
\mu(S)=\widehat f(S)^2,\qquad K=|S|,\qquad I=\mathbb E K,
\]
and
\[
v_A=\sum_{B\supseteq A}\frac{\mu(B)}{\binom{|B|}{|A|}},
\]
then `v_A` is the probability that a uniformly ordered spectral set has prefix `A`. Its entropy splits into a hazard term and a selector-information term. The universal difficulty is an amortized bound on selector information; pointwise selector bounds are false on tribes.

This run attacks the first nontrivial part of that obstruction by comparing the **first revealed spectral coordinate** with a Boolean derivative through hypercontractivity. The result is a dimension-free root payment. The same calculation also exposes exactly why a naive iteration to deeper prefixes is false and produces the corrected higher-derivative quantity that a future proof must control.

Throughout, logarithms in entropy are base 2; `ln` denotes the natural logarithm.

## 2. A universal hypercontractive cap on the first-prefix shadow

For a coordinate `i`, set
\[
p_i=\Pr(i\in S)=\operatorname{Inf}_i(f),\qquad
v_i=\sum_{S\ni i}\frac{\mu(S)}{|S|}.
\]
Then
\[
\sum_i v_i=V:=\Pr(K>0)=1-\widehat f(\varnothing)^2.
\tag{2.1}
\]
Conditioned on `K>0`, the first coordinate of a uniformly random ordering of `S` therefore has law
\[
q_i=\frac{v_i}{V}.
\tag{2.2}
\]

### Theorem 2.1 — root-shadow cap

For every Boolean `f:{-1,1}^n -> {-1,1}` and every coordinate `i`,
\[
\boxed{
 v_i\le F(p_i):=\int_0^1 p_i^{\,2/(1+t)}\,dt
 \le \min\!\left\{p_i,\frac{2p_i(1-p_i)}{\ln(1/p_i)}\right\},
}
\tag{2.3}
\]
with the endpoint values interpreted continuously.

#### Proof

Use the normalized difference
\[
D_i f(x)=\frac{f(x)-f(x^{\oplus i})}{2}.
\]
After factoring the character in coordinate `i`, this is a function on the other `n-1` coordinates taking values only in `{-1,0,1}`. Hence
\[
\|D_i f\|_2^2=\|D_i f\|_{1+t}^{1+t}=p_i,
\]
so
\[
\|D_i f\|_{1+t}^2=p_i^{2/(1+t)}.
\tag{2.4}
\]
Its Fourier coefficients are exactly the coefficients of `f` whose support contains `i`, with `i` removed. Consequently
\[
\|T_{\sqrt t}D_i f\|_2^2
=\sum_{S\ni i}t^{|S|-1}\mu(S).
\tag{2.5}
\]
Integrating from `0` to `1` gives
\[
v_i=\int_0^1\|T_{\sqrt t}D_i f\|_2^2\,dt.
\tag{2.6}
\]
Bonami--Beckner hypercontractivity with `q=1+t` and `rho=sqrt(t)` gives
\[
\|T_{\sqrt t}D_i f\|_2\le \|D_i f\|_{1+t},
\]
which proves the first inequality in (2.3).

For the explicit cap, write `L=ln(1/p_i)`. Since `2/(1+t)>=1`, the integrand is at most `p_i`. Also
\[
\begin{aligned}
F(p_i)
&=p_i\int_0^1\exp\!\left[-L\frac{1-t}{1+t}\right]dt\\
&=2p_i\int_0^1\frac{e^{-Lu}}{(1+u)^2}\,du\\
&\le 2p_i\int_0^1 e^{-Lu}\,du
=\frac{2p_i(1-p_i)}{L}.
\end{aligned}
\]
This proves (2.3). \(\square\)

The essential Boolean input is not merely `\|D_i f\|_2^2=p_i`; it is the stronger indicator-amplitude fact `|D_i f| in {0,1}`. That is the feature that will fail at higher derivative order.

## 3. Dimension-free payment for the root selector

Let
\[
\phi(x)=x\log_2(1/x),\qquad
C_{\rm root}:=\frac{2}{\ln2}\left(1+\frac1{2e}\right)
=3.4161279272009697\ldots .
\tag{3.1}
\]

### Corollary 3.1 — weighted first-coordinate entropy

For every Boolean `f`,
\[
\boxed{
V H(q)\le C_{\rm root}\,I(f).
}
\tag{3.2}
\]
Consequently the root selector-information contribution obeys the same bound.

#### Proof

First,
\[
V H(q)=\sum_i v_i\log_2\frac{V}{v_i}
\le\sum_i\phi(v_i),
\tag{3.3}
\]
because `V<=1`.

It remains to show `phi(v_i)<=C_root p_i` coordinatewise. If `p<=1/8`, Theorem 2.1 gives `v<=2p/L` with `L=ln(1/p)`. This upper bound lies below `1/e`, where `phi` is increasing, so
\[
\frac{\phi(v)}p
\le \frac{2}{\ln2}
\left(1+\frac{\ln L-\ln2}{L}\right).
\tag{3.4}
\]
The last fraction is maximized at `L=2e`, where it equals `1/(2e)`. If `1/8<=p<=1/e`, use `v<=p` and monotonicity to get `phi(v)<=phi(p)<=3p`. If `p>=1/e`, use the global maximum `phi(v)<=1/(e ln2)<=p/ln2`. Thus (3.2) follows after summing `p_i`, whose sum is `I(f)`. \(\square\)

If `j_empty` denotes the information about the terminal spectral set carried by the first revealed coordinate after conditioning on continuation, the exact death-chain identity gives
\[
j_\varnothing=H(q)-\mathbb E[\log_2K\mid K>0].
\]
Hence
\[
\boxed{Vj_\varnothing\le C_{\rm root}I(f).}
\tag{3.5}
\]
This is a genuine universal selector payment, but it is only for the root. It is **not** a proof of FEI.

## 4. What survives at an arbitrary prefix

Let `A` have size `a>=1`, and define the Fourier upper mass
\[
U_A:=\sum_{S\supseteq A}\mu(S)=\|D_A f\|_2^2.
\tag{4.1}
\]
After factoring the character `chi_A`, `D_A f` is a function on the complementary coordinates. Let
\[
s_A:=\Pr(D_A f\ne0)
\tag{4.2}
\]
for uniform complementary input. For any `1<=q<=2`, Holder on the support gives
\[
\|D_A f\|_q^2\le U_A\,s_A^{2/q-1}.
\tag{4.3}
\]
Combining this with hypercontractivity and the Green-kernel formula for the death-chain shadow yields
\[
\boxed{
 v_A\le aU_A\int_0^1(1-t)^{a-1}
 s_A^{(1-t)/(1+t)}\,dt.
}
\tag{4.4}
\]

Booleanity supplies a sharp but degrading quantization substitute. An `a`-fold normalized derivative is an average of `2^a` signs with spacing `2^{1-a}`. Therefore any nonzero value has magnitude at least `2^{1-a}` and
\[
\boxed{s_A\le \min\{1,4^{a-1}U_A\}.}
\tag{4.5}
\]
Thus
\[
\boxed{
 v_A\le aU_A\int_0^1(1-t)^{a-1}
 \min\{1,4^{a-1}U_A\}^{(1-t)/(1+t)}\,dt.
}
\tag{4.6}
\]
For `a=1`, (4.6) is exactly the root mechanism because `s_i=U_i=p_i`. For `a>1`, the factor `4^{a-1}` records the precise loss from higher-derivative amplitude splitting.

This identifies a concrete remaining proof target: **an amortized bound on the support inflation `s_A/U_A` under the continuation-Palm law**. A p-only iteration that silently sets `s_A=U_A` is false.

## 5. Exact admissible Boolean counterexample to the naive iteration

Take the two-bit one-point defect
\[
f(00)=-1,\qquad f(01)=f(10)=f(11)=+1.
\]
Its twice-normalized derivative has values
\[
D_{\{1,2\}}f=(-1/2,+1/2,+1/2,-1/2),
\]
up to the harmless character factor. Hence
\[
U_{\{1,2\}}=\frac14,\qquad s_{\{1,2\}}=1=4U_{\{1,2\}}.
\tag{5.1}
\]
At `q=3/2`,
\[
\|D_{\{1,2\}}f\|_{3/2}^2=\frac14,
\]
whereas the invalid first-derivative extrapolation would predict
\[
U_A^{2/q}=\left(\frac14\right)^{4/3}
=0.1574901312\ldots <\frac14.
\tag{5.2}
\]
The corrected support/quantization bound (4.3)--(4.5) gives exactly `1/4`, so it is tight on this example. This is an actual Boolean obstruction, not an abstract spectral distribution.

## 6. Executed stress tests

The checker `verify_hypercontractive_shadow.py` has SHA-256
`69a511713fe5b5c77b7af4029ba5352c2185d9a70c1620f56a1b8f1dac317eb4`.
Its captured output has SHA-256
`6e69f9509cf6c6322d3a674e3f1212e7519125d333c50e75cf8599556f152716`.

It executed three independent finite tests:

1. **Exhaustive Boolean functions modulo global negation through dimension four.** Counts were `2, 8, 128, 32768`. The maxima of `V H(q)/I` were respectively
   `0`, `0.75`, `1.0566416671474375`, `1.3125`. The explicit cap (2.3) had no negative slack.
2. **Published Numaro 18-variable seed.** The reconstructed truth table was accepted only after matching SHA-256
   `f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`. It has `I=261/128=2.0390625`, `V=1`, and this root quantity is
   \[
   VH(q)=3.235732753238979,
   \qquad \frac{VH(q)}I=1.5868727678719896.
   \]
   The minimum numerical slack of the simple cap `min(p,2p(1-p)/ln(1/p))-v` over its 18 coordinates was `0.0005370182964919073`.
3. **Higher-derivative boundary example.** The two-bit defect above numerically gives `U=0.25`, support `1`, `L_{3/2}^2=0.25`, naive bound `0.15749013123685915`, corrected bound `0.25`.

These checks validate the implementation and boundary examples only. The universal statements in Sections 2--4 rely on the analytic proofs above, not on finite enumeration.

## 7. What this does and does not solve

**PROVED in this run:** a dimension-free hypercontractive payment for the entropy of the first revealed spectral coordinate, with explicit constant `C_root=3.4161279272...`, and a general-prefix hypercontractive inequality that retains the exact higher-derivative support fraction.

**REFUTED at its exact scope:** the tempting iteration that replaces the higher-derivative support fraction by its squared `L2` mass. The two-bit one-point defect saturates the missing factor four already at derivative order two.

**OPEN:** the amortized selector information over all prefixes. The new comparison says the obstacle is no longer an unspecified selector mystery: it is the growth of
\[
\frac{s_A}{U_A}
\]
for higher Boolean derivatives along the continuation process. The raw worst-case quantization bound `s_A/U_A<=4^{a-1}` is exponentially bad and cannot simply be inserted prefix-by-prefix.

The next attack should therefore be a **face-support budget**: prove that under the continuation-Palm weighting, the logarithmic inflation
\[
\log\frac{s_A}{U_A}
\]
(or an appropriate increment of it) has a summable charge to original-coordinate influence. Such a statement would preserve exactly the rare-history logarithm that earlier unweighted Hellinger approaches lose. It should be stress-tested first on one-point defects, tribes, recursive balanced composition, and the Numaro seed.

No claim of publication priority or novelty is made here; full FEI remains open.
