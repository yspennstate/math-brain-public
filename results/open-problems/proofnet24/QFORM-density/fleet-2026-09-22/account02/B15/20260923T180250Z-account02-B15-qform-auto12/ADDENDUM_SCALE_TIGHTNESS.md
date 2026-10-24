# Addendum — any fixed positive inverse-scale moment blocks compact-source weak approximation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T180250Z-account02-B15-qform-auto12`.

The BV barrier in `REPORT.md` can be strengthened in a direction relevant to possible relaxations of the Gaussian-mixture theorem: replacing the first inverse-scale moment by **any fixed positive fractional inverse-scale moment** still cannot make the mixture class weakly dense in the cap-one source class.

## Proposition — `QFORM-GAUSSIAN-MIXTURE-SCALE-TIGHTNESS-BARRIER-v1`

Let

\[
Y=M+\sigma G,
\]

where `G~N(0,1)` is independent of arbitrary mixture data `(M,sigma)`, `sigma>0`.  Suppose for some `r>0`

\[
E\,\sigma^{-r}\le K<\infty. \tag{1}
\]

Then for every interval `J` of length `L` and every `s>0`,

\[
\boxed{
\Pr(Y\notin J)
\ge 2\,(1-Ks^r)_+\,\Phi\!\left(-\frac{L}{2s}\right).}
\tag{2}
\]

In particular, for any fixed `K<infinity` and `r>0`, no sequence of such Gaussian mixtures can converge weakly to a probability law supported on a bounded interval.

### Proof

Conditional on `(M,sigma)`, the mass of `N(M,sigma^2)` in an interval of length `L` is maximized when the Gaussian mean is at the midpoint.  Therefore

\[
\Pr(Y\notin J\mid M,\sigma)
\ge2\Phi\!\left(-\frac{L}{2\sigma}\right).
\]

On `{sigma>=s}` the right side is at least `2 Phi(-L/(2s))`.  Markov applied to `sigma^{-r}` gives

\[
\Pr(\sigma<s)
=\Pr(\sigma^{-r}>s^{-r})
\le Ks^r.
\]

Multiplying these two bounds proves (2).

Now suppose `Law(Y_m)=>mu` and `mu` is supported on `[a,b]`.  Take any `epsilon>0` and let `J=[a-epsilon,b+epsilon]`, of finite length `L`.  Choose `s>0` with `Ks^r<1`, so the right side of (2) is a fixed positive number `c`.  The closed set

\[
F=(-\infty,a-\varepsilon]\cup[b+\varepsilon,\infty)
\]

then satisfies `P(Y_m in F)>=c` for every `m`, whereas weak convergence and Portmanteau require

\[
\limsup_m P(Y_m\in F)\le\mu(F)=0,
\]

a contradiction.  QED.

## Concrete cap-one target witness

Already `f=1_[0,1]` is an admissible cap-one probability density.  Hence for every `r>0` and finite `K`, it is outside the weak closure of Gaussian location-scale mixtures satisfying `E sigma^{-r}<=K`.

For the completed theorem's budget `r=1`, `K=sqrt(2*pi)`, taking `s=1/(2K)` in (2) for a unit interval gives the explicit fixed leakage

\[
\Pr(Y\notin J)
\ge \Phi(-\sqrt{2\pi})>0.006.
\]

(The numerical decimal is only illustrative; positivity is the proof-relevant fact.)

## Why this is stronger than the BV barrier

The main report proves that a bounded first inverse-scale moment forces a BV bound and gives analytic full-support witnesses requiring arbitrarily large budget.  The present proposition says something complementary: **even a bounded fractional inverse-scale moment of arbitrarily small positive order prevents weak approximation of compactly supported sources**.

Thus a prospective repair of the full Gaussian determinant argument cannot merely replace `E sigma^{-1}` by `E sigma^{-r}` with some universal `r>0` and then appeal to the completed account03/B15 weak-trace theorem.  For exact target inputs such as three independent `Unif[0,1]` coordinates and `A=I_3`, that approximation gate already fails, even though the true quadratic-form density is universally bounded by the diagonal theorem.

This remains an obstruction to a proof mechanism, not a counterexample to QFORM.
