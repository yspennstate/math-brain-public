# Addendum — primitive carry layers are low-degree Boolean codewords

**Status: proved lemma / FEI still OPEN.** This strengthens the carry-multiplicity observation in the main report; it is not a proof of unrestricted FEI and no publication-priority claim is made.

Let

\[
V(x)=\sum_{S\in A}\epsilon_S(-1)^{\langle S,x\rangle},\qquad \epsilon_S\in\{\pm1\},
\]

and let `r` be the minimum 2-adic valuation of a nonzero value of `V`. The main report proved the signed upper-incidence criterion

\[
r(V)\ge r\iff 2^{r-|T|}\mid \sum_{S\supseteq T}\epsilon_S\quad(|T|<r).
\]

Define the primitive parity shadow

\[
G_r(x)=\left(V(x)/2^r\right)\bmod2.
\]

Then `G_r` is nonzero and

\[
\boxed{\deg_{\rm alg}(G_r)\le r.}
\]

Indeed, after dividing the multilinear identity

\[
V(x)=\sum_T(-2)^{|T|}M_Tx_T
\]

by `2^r`, the carry criterion makes all coefficients integral, while every term with `|T|>r` has an extra factor 2 and vanishes modulo two. Also

\[
\{x:G_r(x)=1\}=\{x:V(x)\ne0,\ \nu_2(V(x))=r\}.
\]

The Reed--Muller minimum-distance bound for a nonzero degree-at-most-`r` Boolean polynomial therefore gives the stronger structural conclusion

\[
\boxed{\left|\{x:\nu_2(V(x))=r\}\right|\ge 2^{n-r}.}
\]

So a depth-`r` carry cannot occur only on a tiny exceptional set: the primitive valuation is attained on at least a `2^{-r}` fraction of the physical cube. Parseval then immediately recovers the packet-multiplicity bound `|A|>=2^r`.

For the exact Numaro n=18 record seed, the dedicated checker finds the primitive fractions of the ten magnitude packets to be

`1, 15/32, 1, 15/32, 1, 9/16, 17/32, 17/32, 15/32, 1`

in increasing Walsh magnitude order. In particular the two depth-3 packets have primitive fractions `9/16` and `17/32`, both far above the universal `1/8` floor.

This shifts the next universal target: one does not need to control arbitrarily rare deep-carry spikes. The unresolved problem is how these abundant primitive physical layers from **different Fourier magnitudes** interact under restriction/collision and how their joint packet entropy is charged to influence.

Reproducibility: `primitive_layer_check.py` imports the exact saved n=18 profiler, recomputes every packet, and checks the `2^(n-r)` lower bound exactly. Native result: PASS on all 10 packets. Checker SHA-256 `f6b85bd7bdbcfb4dfa6d9e04578f879db06b3c8e1dbad749f8eeb1d5b67f4942`; output SHA-256 `fa47e611a84fd7158308066b0b764657cbc7efbe01a283e60748110423d98293`.
