TASK: B12 ACCOUNT: fleet02 RUN: 2026-09-21T15:23:02.614305Z — Palm thinning / derivative-shadow semigroup for FEI sequential compression

# B12 — Palm thinning, derivative-shadow KL, and a Boolean curvature obstruction

**Role:** FEI approach 1 — spectral-sample compression / sequential prediction.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval or receiver-context use occurred.  
**Status:** **PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**FLEET_RULES moves used:** **#5** (introduce a continuous thinning parameter and study its information curve), **#11** (dualize the selector refund into a KL divergence between Palm channels), and **#20** (find why the obvious semigroup-curvature algorithm fails, with an admissible Boolean counterexample).

This run continues the preceding B12 Palm/state-capacity result rather than re-deriving it. That result identified, for spectral law
\[
p_B=\widehat f(B)^2,\qquad \lambda=I(f)=\sum_B |B|p_B,
\]
a continuation-Palm experiment whose prefix is `A`, next coordinate is `X`, and
\[
\Pr(X=i)=\pi_i=\frac{\operatorname{Inf}_i(f)}{\lambda}.
\]
It also proved
\[
\frac{\mathrm{Sel}(f)}{\lambda}
=H(\pi)-I(A;X)-\frac{\mathbb E_p\log_2(K!)}{\lambda},
\qquad K=|B|.
\tag{0.1}
\]
The current unrestricted FEI lower bound remains `>6.521845710923046575`; the read-once `6.4573` upper bound is a different, structured scope.

## 1. Uniform-thinning representation of the Palm prefix

Let `B` be the terminal spectral set in the Palm experiment. Conditional on `X=i`, the joint law simplifies exactly:
\[
\Pr(B\mid X=i)=\frac{p_B}{\operatorname{Inf}_i(f)}
\quad(B\ni i).
\tag{1.1}
\]
Now sample `U~Unif[0,1]`, independently of `B` conditional on `X=i`, and form
\[
A_U=\{j\in B\setminus\{i\}:V_j\le U\},
\tag{1.2}
\]
with iid `V_j~Unif[0,1]`. Equivalently, conditional on `U=u`, retain every element of `B\setminus\{i\}` independently with probability `u`.

### Theorem 1.1 — exact Palm thinning representation

The random set `A_U` has exactly the same conditional law as the unordered set of coordinates preceding `i` in a uniformly random ordering of `B`.

**Proof.** Put `k=|B|` and `a=|A|`. In the random-order model, conditional on `B,X=i`, the rank of `i` is uniform on `{1,...,k}`. Hence a particular `A subseteq B\{i}` of size `a` occurs with probability
\[
\frac1{k\binom{k-1}{a}}.
\]
In the thinning model,
\[
\Pr(A_U=A\mid B,X=i)
=\int_0^1u^a(1-u)^{k-1-a}\,du
=\frac{a!(k-1-a)!}{k!}
=\frac1{k\binom{k-1}{a}}.
\]
The two conditional laws coincide pointwise. QED.

This turns the whole sequential-prefix refund into an information quantity along a one-parameter thinning channel.

## 2. Derivative-shadow tomography

For `C subseteq [n]`, write
\[
\nu(C)=\sum_{B\supseteq C}p_B.
\tag{2.1}
\]
With discrete derivative `D_i f(x)=(f(x)-f(x^{\oplus i}))/2`, Fourier orthogonality gives
\[
\nu(C)=\|D_Cf\|_2^2.
\tag{2.2}
\]

Let `Q_i` denote the law of the Palm prefix `A` conditional on `X=i`. If
\[
v_A=\sum_{B\supseteq A}\frac{p_B}{\binom{|B|}{|A|}},
\tag{2.3}
\]
then:

### Proposition 2.1 — exact row law and moments
For `A` not containing `i`,
\[
\boxed{
Q_i(A)=\frac{v_{A\cup\{i\}}}{(|A|+1)\operatorname{Inf}_i(f)}.
}
\tag{2.4}
\]
For every `T` not containing `i`,
\[
\boxed{
\Pr(T\subseteq A\mid X=i)
=
\frac{\nu(T\cup\{i\})}{(|T|+1)\operatorname{Inf}_i(f)}
=
\frac{\|D_{T\cup\{i\}}f\|_2^2}
{(|T|+1)\|D_if\|_2^2}.
}
\tag{2.5}
\]

**Proof.** Equation (2.4) follows either by multiplying the already-proved `Pr(A)` and `Pr(X=i|A)`, or directly from Theorem 1.1 and the beta integral. For (2.5), conditional on `B`, all elements of `T` survive the common-`U` thinning with probability `E U^{|T|}=1/(|T|+1)`, provided `T subseteq B\{i}`, and otherwise with probability zero. Average (1.1) over `B`. QED.

Thus the entire conditional prefix channel is a normalized hierarchy of **higher-order derivative energies**, not an arbitrary statistic of the Fourier magnitudes.

Let
\[
\mu(A)=\Pr(A)=\frac{v_A-p_A}{\lambda}.
\tag{2.6}
\]
Then:

### Corollary 2.2 — exact derivative-shadow KL refund
\[
\boxed{
I(A;X)=\sum_i\pi_i D_2(Q_i\|\mu).
}
\tag{2.7}
\]
Consequently the selector identity becomes
\[
\boxed{
\frac{\mathrm{Sel}(f)}{\lambda}
=
H(\pi)
-\sum_i\pi_iD_2(Q_i\|\mu)
-\frac{\mathbb E_p\log_2(K!)}{\lambda}.
}
\tag{2.8}
\]

Equation (2.8) is a concrete universal target for approach 1. The dangerous entropy of the normalized influence profile has exactly two refunds: a factorial/order refund, and a KL separation between the derivative-shadow Palm rows `Q_i`.

## 3. A semigroup identity and the fixed-level simplification

For fixed `u in [0,1]`, define `A_u` by retaining every member of `B\{X}` independently with probability `u`, and set
\[
J_f(u)=I(X;A_u).
\tag{3.1}
\]
The actual Palm prefix is `A=A_U` with `U~Unif[0,1]` hidden. Since `U` is independent of `X`,
\[
I(X;A,U)=\int_0^1J_f(u)\,du.
\]
Therefore
\[
\boxed{
I(A;X)=\int_0^1J_f(u)\,du-I(X;U\mid A).
}
\tag{3.2}
\]
The correction term is real and must not be silently dropped.

### Theorem 3.1 — exact fixed-level semigroup formula

Suppose `p_B>0 => |B|=k`. Then
\[
I(X;U\mid A)=0,
\tag{3.3}
\]
and hence
\[
\boxed{I(A;X)=\int_0^1J_f(u)\,du.}
\tag{3.4}
\]
Moreover `H_haz=0`, so
\[
\boxed{
\frac{H(f)}{k}
=H(\pi)-\frac{\log_2(k!)}k-\int_0^1J_f(u)\,du.
}
\tag{3.5}
\]

**Proof of (3.3).** Conditional on `X=i`, `A=a`, and fixed terminal size `k`, the joint density in `u` contains the factor
`u^{|a|}(1-u)^{k-1-|a|}`. Every dependence on `i` and on which `k`-set generated `a` is a multiplicative factor independent of `u`. Thus
\[
U\mid(A=a,X=i)\sim\mathrm{Beta}(|a|+1,k-|a|),
\]
which does not depend on `i`. Therefore `U` is conditionally independent of `X` given `A`. QED.

This gives a genuine thinning-semigroup reformulation for homogeneous spectral laws. It does **not** by itself solve that class, because a conditioned Fourier level of a general Boolean function is not itself Boolean.

## 4. Exact parity calibration: co-set information is the wrong currency

A tempting bridge after (2.5) is to compare `I(A;X)` with the information in the complete co-set `B\{X}`. Parity kills every dimension-free constant comparison.

For the `k`-variable parity `f=chi_[k]`, the spectral set is deterministically `B=[k]`. Therefore `X` is uniform on `[k]`, and the full co-set determines `X`:
\[
I(X;B\setminus\{X\})=\log_2 k.
\tag{4.1}
\]
But conditional on a Palm prefix `A`, `X` is uniform on the `k-|A|` unexposed coordinates. The rank is uniform, so
\[
H(X\mid A)=\frac1k\sum_{r=1}^k\log_2 r=\frac{\log_2(k!)}k.
\]
Hence
\[
\boxed{
I(A;X)=\log_2k-\frac{\log_2(k!)}k\longrightarrow \log_2 e.
}
\tag{4.2}
\]
Thus `I(A;X)/I(X;B\{X}) -> 0`. No proof can replace the noisy random-prefix refund by a fixed positive fraction of the full co-set information. On parity, almost all of the profile-label entropy is paid by the factorial refund, not by the prefix KL term.

This sharply complements the preceding balanced-tribes result: there the factorial term is only `log_2 w+O(1)` while the prefix stores `w-O(1)` bits of active-block identity. A universal argument must allow these two payment mechanisms to trade off.

## 5. A natural curvature bridge is false even for Boolean functions

The thinning representation suggests a very attractive strategy: prove that `u -> J_f(u)` is convex (or has an equally simple universal curvature sign), then lower-bound its integral from local semigroup data. That bridge is false.

Take the 4-bit Boolean function obtained from the dictator `chi_{4}` by flipping its value at one vertex. Its squared Fourier spectrum is
\[
p_{\{4\}}=\frac{49}{64},\qquad p_S=\frac1{64}\quad(S\ne\{4\}).
\tag{5.1}
\]
Direct high-precision evaluation of the exact rational thinning channel gives
\[
\begin{aligned}
J(0.9)&=0.629239249842663916003048445848393828\ldots,\\
J(0.95)&=0.666063721654253050803161880485108859\ldots,\\
J(1)&=0.702759237067721172801364254177077297\ldots.
\end{aligned}
\]
Therefore
\[
J(0.9)+J(1)-2J(0.95)
=-0.000128956398121012801911060944746592\ldots<0.
\tag{5.2}
\]
Convexity would require the left side to be nonnegative. So the universal convexity bridge fails on an explicit admissible Boolean function in four variables.

This is not a counterexample to FEI. It is a counterexample to a proposed semigroup proof shortcut.

## 6. What remains alive

The useful new object is the family of derivative-shadow Palm rows
\[
Q_i(A)=\frac{v_{A+i}}{(|A|+1)\operatorname{Inf}_i},
\]
or equivalently their moment hierarchy
\[
\Pr(T\subseteq A\mid X=i)=\frac{\|D_{T+i}f\|_2^2}{(|T|+1)\|D_if\|_2^2}.
\]
A viable next route is not a scalar curvature inequality for `J_f`. It should exploit **multi-scale separation among the rows `Q_i`** while allowing the factorial term to dominate on parity-like spectra and the KL term to dominate on tribes-like clustered spectra.

One concrete target is a scale-integrated or Carleson-style inequality lower-bounding
\[
\sum_i\operatorname{Inf}_i D_2(Q_i\|\mu)+\mathbb E\log_2(K!)
\]
against
\[
\lambda H(\pi)-C\lambda,
\]
using Boolean identities among the derivative energies `||D_T f||_2^2`. By (2.8), such an inequality is exactly the missing selector payment. No such universal bound is proved here.

This scope is complementary to the current B13 projection/refund-restriction work and the new mass-weighted erasure composition work in another B14 account: those analyze restriction/composition payments, while this report isolates the random-prefix channel and its derivative-energy information geometry.

## 7. Executed self-check

`verify_palm_thinning.py` was executed with exact `fractions.Fraction` arithmetic for all finite probability identities and 80-digit `decimal.Decimal` logarithms for entropy evaluations. It passed **38 checks**:

- exact Palm/random-order = uniform-`U` thinning equality on a nontrivial rational 3-coordinate subset law;
- exact row normalization and all tested containment-moment identities (2.5);
- parity calibration for `k=2,3,4,8,16,32,64,128`;
- exact Walsh spectrum (5.1) for the one-point-flipped 4-bit dictator;
- a high-precision strict convexity violation margin `<-1.2e-4`.

The verification result digest is `49e29b59d869a9a974dab3599e230cb5ebfa1cc47333a636bea3e4eb0ab9e057`.

Finite checks support normalization and the explicit counterexample. The universal identities above are proved algebraically on the page; no finite test is treated as full-FEI evidence.
