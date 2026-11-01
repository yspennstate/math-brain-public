# PROB20-14 — addendum: TV rate versus weighted Cramér cutoff

**Parent report:** `runs/2026-09-16/2026-09-16T01-55-00Z__report.md`  
**Status:** substantive sharpening; universal theorem remains **OPEN**.

The parent report proved two facts for every fixed level `k`:

1. the full depth-`k` conditioned-prefix law `Q_{M,k}` converges in total variation to the Kesten-prefix law `P^_k`;
2. for the ordinary prefix boundary count `B=Z_k`, with
   \[
   \tau_k(j)=\mathbb E[B^q;B\ge j],\qquad q=1+r,
   \]
   the conditioned fractional tail satisfies
   \[
   \mathbb E_{Q_{M,k}}[B^r;B\ge j]
   \le \frac{\tau_k(j)}j\exp\{L_M-I_M(j)\}.
   \tag{A.1}
   \]

This addendum combines them into one quantitative master inequality.

## A.1 Exact TV error parameter

Put
\[
\delta_{M,k}:=\|Q_{M,k}-\widehat P_k\|_{\rm TV}.
\tag{A.2}
\]
By the Scheffé theorem proved in the parent report,
\[
\delta_{M,k}\to0.
\tag{A.3}
\]
Moreover, under the Kesten-prefix law,
\[
\mathbb E_{\widehat P_k}[B^r;B\ge j]
=\mathbb E[B^q;B\ge j]
=\tau_k(j).
\tag{A.4}
\]

## A.2 NEW: three-term moment error bound

For every integer `j>=1`,
\[
\boxed{
\left|
\mathbb E_{Q_{M,k}}B^r-
\mathbb E_{\widehat P_k}B^r
\right|
\le
2j^r\delta_{M,k}
+\tau_k(j)
+\frac{\tau_k(j)}j e^{L_M-I_M(j)}.
}
\tag{A.5}
\]

### Proof
Split both moments at `B<j` and `B>=j`. On `B<j`, the function `B^r` is bounded by `j^r`, hence the standard total-variation estimate gives
\[
\left|
\mathbb E_Q[B^r;B<j]-
\mathbb E_{\widehat P}[B^r;B<j]
\right|
\le2j^r\delta_{M,k}.
\]
The Kesten tail is exactly (A.4), and the conditioned tail is bounded by (A.1). Summing the three errors proves (A.5). `QED`

This inequality is all-level, contains no unverified LLT, and makes the remaining endpoint obstruction quantitative.

## A.3 Canonical Scheffé scale

Because `delta_{M,k}->0`, one may choose, for example,
\[
j^{\rm TV}_{M,k}
:=\left\lfloor \delta_{M,k}^{-1/(2r)}\right\rfloor
\tag{A.6}
\]
when `delta>0` (and any diverging value when `delta=0`). Then
\[
j^{\rm TV}_{M,k}\to\infty,
\qquad
(j^{\rm TV}_{M,k})^r\delta_{M,k}\to0.
\tag{A.7}
\]
Therefore a sufficient condition for the full fixed-level conjecture is
\[
\boxed{
\frac{\tau_k(j^{\rm TV}_{M,k})}{j^{\rm TV}_{M,k}}
\exp\{L_M-I_M(j^{\rm TV}_{M,k})\}
\longrightarrow0.
}
\tag{A.8}
\]
The ordinary Kesten tail `tau_k(j_TV)` then also tends to zero automatically.

Thus the problem can be read as an overlap question between an *actual total-variation convergence scale* and the weighted Cramér free-energy scale.

## A.4 NEW: simple sufficient criterion using the weighted safe cutoff

Let `gamma_{M,k}` be the weighted safe cutoff from the parent report, chosen with `omega_M->infinity`, so that
\[
\mathbb E_{Q_{M,k}}[B^r;B\ge\gamma_{M,k}]
\le e^{-\omega_M},
\tag{A.9}
\]
and `gamma_{M,k}->infinity` when `B` is unbounded. Then (A.5) with `j=gamma` simplifies to
\[
\boxed{
\left|
\mathbb E_{Q_{M,k}}B^r-
\mathbb E_{\widehat P_k}B^r
\right|
\le
2\gamma_{M,k}^r\delta_{M,k}
+\tau_k(\gamma_{M,k})
+e^{-\omega_M}.
}
\tag{A.10}
\]
Consequently,
\[
\boxed{
\gamma_{M,k}^r\delta_{M,k}\to0
\quad\Longrightarrow\quad
\{\ell_k(T_n)^r\}_n\text{ is uniformly integrable.}
}
\tag{A.11}
\]

This criterion is stronger conceptually than the earlier `alpha_M >= gamma_M` overlap condition: it does not demand a uniform pointwise ratio theorem throughout the whole lower window. It only asks that the **global prefix TV error** decay faster than the reciprocal `r`-power of the tail-adapted safe cutoff.

## A.5 NEW: necessary obstruction to any counterexample

Conversely, because
\[
\tau_k(\gamma_{M,k})\to0,
\qquad e^{-\omega_M}\to0,
\]
(A.10) implies:

> If the fixed-level fractional moment fails to converge (equivalently, UI fails), then along some subsequence
> \[
> \boxed{
> \limsup \gamma_{M,k}^r\delta_{M,k}>0.
> }
> \tag{A.12}
> \]

Thus a counterexample now has to satisfy **two simultaneous anomalies**:

1. the parent report's tail-amplified mesoscopic local-probability spike below `gamma_{M,k}`; and
2. total-variation convergence of the entire finite-depth conditioned prefix to the Kesten prefix that is slow enough that `delta_{M,k}` is at least of order `gamma_{M,k}^{-r}` along the same subsequence.

The second condition is not a formal consequence of the first and gives a new independent quantitative target for both proof and counterexample construction.

## A.6 Updated next attack

The strongest proof route is now to obtain **any quantitative rate** for the Scheffé convergence
\[
\delta_{M,k}
=\frac12\mathbb E_{P_k}|R_M(A,B)-B|
\tag{A.13}
\]
that beats `gamma_{M,k}^{-r}`. It is not necessary to prove a global pointwise linear Kesten bound.

Potential ingredients already available in the campaign are:

- finite-core Bernoulli smoothing for nearby exact local atoms;
- the central-atom exponent and the exact Cramér penalty `I_M`;
- exponential elimination of disproportionate prefixes;
- the `q`-tail modulus `tau_k`, already built into `gamma_{M,k}`.

A proof of
\[
\delta_{M,k}=o(\gamma_{M,k}^{-r})
\]
for each fixed `k` would close the requested theorem directly via (A.10). No such rate is proved here; (A.5)–(A.12) are a reduction and quantitative obstruction, not a full solution.