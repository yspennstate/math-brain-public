Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning telemetry or binding model/effort selector is exposed.

# E0070 addendum — exact pullback to Björklund's source normalization

This addendum makes the source-normalization step in the star-transposition proof completely explicit. It does not alter the earlier immutable proof artifact.

Let `X=G/H` and let `u:X->C`. Define its right-`H`-invariant pullback

\[
\widetilde u(g)=u(gH),\qquad g\in G.
\]

Björklund's source definition says that a left quasi-`mu`-harmonic function on the group satisfies

\[
\int_G \widetilde u(sg)\,d\check\mu(s)
=
\widetilde u(g)
+
\int_G \widetilde u(s)\,d\check\mu(s),
\qquad g\in G,
\tag{A.1}
\]

with the displayed integrals defined. The natural quotient meaning is precisely (A.1) for the right-`H`-invariant pullback.

In the R7-03 construction `check(mu)=mu`. Under `G/H≅N_0`, define

\[
c:=\int_G\widetilde u(s)\,d\mu(s)
=\sum_{n\ge1}p_nu(n).
\tag{A.2}
\]

Then (A.1) is exactly

\[
Pu(x)=u(x)+c
\qquad (x\in X),
\tag{A.3}
\]

for the star kernel from the main artifact. Thus every source-normalized left quasi-harmonic quotient function belongs to the constant-defect class treated in Theorem 5.1 there.

There is also an extra normalization identity. Taking `g=e` in (A.1) yields

\[
\int_G \widetilde u(s)\,d\mu(s)
=
\widetilde u(e)+
\int_G \widetilde u(s)\,d\mu(s),
\]

hence

\[
\boxed{u(H)=\widetilde u(e)=0.}
\tag{A.4}
\]

The main theorem proves that every integrable solution of (A.3), even without imposing (A.2) or (A.4), has `c=0` and is constant. Therefore a source-normalized quasi-harmonic solution must in fact be the **zero function**. Ordinary left harmonic functions correspond to `c=0` without the normalization (A.4), and the same theorem makes all of them constant.

Finally, source integrability is exactly the condition used in the contradiction: because the support of `mu` is `{tau_n:n>=1}` and `tau_nH` corresponds to `n`,

\[
\int_G|\widetilde u(s)|\,d\mu(s)
=
\sum_{n\ge1}p_n|u(n)|<\infty.
\]

So no hidden conditional-convergence convention is present: the center series in the proof is a genuine complex Lebesgue integral and is absolutely summable.

**Conclusion.** The star-transposition construction matches Björklund's literal left quasi-`mu`-harmonic normalization, not merely an informal constant-defect variant. The source-level verdict remains **PROVED CANDIDATE**, with protocol audits still outstanding.
