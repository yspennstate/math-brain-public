# Independent counterexample review: B05 rare shared-coordinate degree shift

## Verdict

**ACCEPTED AT THE PRECISE LOCAL-PAYMENT SCOPE, WITH TWO WORDING/TYPESETTING CORRECTIONS.**

Target claim: `B05-OVERLAP-SINGLETON-PAYMENT-v1` from B05/A025 at canonical revision `71c9d6a3127c9d893aa5b6b89ca615e26bcf1be2`.

The genuine Boolean family proves that no finite absolute `C` can make

\[
\Phi(fg)\le \Phi(f)+\Phi(g)+C(\operatorname{Inf}_x f+\operatorname{Inf}_x g)
\]

hold for all factors sharing only `x`. It also refutes the one-sided extension
`Phi(Bf) <= Phi(f)+M I(B)` when `B` reuses `x`.

## Independent reconstruction

Let `n=2m+1`, let `K_n` be balanced majority, and put

\[
c_m=\widehat K_n(\{u_i\})=\binom{2m}{m}/4^m.
\]

For a one-point event `E` in `r` controls, `epsilon=2^-r`, define

\[
f=xK_n,\qquad g=1+\mathbf1_E(x-1),\qquad h=fg.
\]

Direct expansion, without importing the author's spectrum, gives:

- every singleton coefficient of `f` is zero;
- `|g-hat({x})|=epsilon` and every control singleton of `g` has magnitude `epsilon`;
- every private-core singleton of `h` is `epsilon c_m`, while its `x` and control singletons vanish.

Therefore

\[
\Phi(f)=0,\qquad \Phi(g)=(r+1)\phi(\epsilon),\qquad
\Phi(h)=n\phi(\epsilon c_m).
\]

The exact physical-input ledger is

\[
\operatorname{Inf}_x(f)=1,quad
\operatorname{Inf}_x(g)=\epsilon,quad
\operatorname{Inf}_x(h)=1-\epsilon,quad
I(g)=(r+1)\epsilon.
\]

For general Boolean factors sharing only `x`, private-variable independence and
`D_xF\,\bar F=0` give

\[
\operatorname{Inf}_x(FG)=p(1-q)+(1-p)q=p+q-2pq.
\]

The central-binomial bounds were re-proved by induction from
`c_(m+1)/c_m=(2m+1)/(2m+2)`:

\[
\frac1{2\sqrt m}\le c_m\le\frac1{\sqrt{m+1}}.
\]

Consequently

\[
\Phi(h)\ge\frac{\epsilon^2}{2}\log_2(m+1).
\]

The claimed sufficient violation range follows immediately. This proves the
sign for an infinite tail for every fixed `r` and every finite proposed
constant. The author's displayed finite samples have not yet crossed the huge
thresholds and are calibration only; the analytic inequality, not those
samples, certifies the counterfamily.

## Reveal-order audit

Both order formulas are correct.

- Controls first: all but the event leaf give `xK_n`, whose singleton potential
  is zero; the event leaf gives `K_n`. The expectation is
  `epsilon Phi(K_n)`.
- `x` first: the children are `K_n` and `K_n(2 1_E-1)`, giving
  \[
  \frac n2\{\phi(c_m)+\phi((1-2\epsilon)c_m)\}.
  \]
- After both `x` and the controls are fixed, every remaining function is
  `+/-K_n`, so the terminal potential is always `Phi(K_n)`.

Thus the counterfamily blocks a nonnegative local shared-edge account, but not
a signed global telescope.

## Mandatory scope corrections

1. The rare quantity is the **new factor's** `x`-pivotal mass `epsilon`.
   The complete shared edge is not rare because `Inf_x(f)=1`. The stronger
   bounded-total-shared-edge no-go is nevertheless valid because `1+epsilon`
   is independent of `m`.
2. The source `RARE_COUNTERFAMILY.tex` dropped backslashes before several
   `qquad/quad` commands. This is a typesetting defect only and should be fixed
   before TeX ingestion.

The final function can be rewritten as

\[
h(u,x,v)=K_n(u)s(x,v),
\]

with disjoint blocks. Hence ordinary spectral entropy and influence are
exactly additive across `K_n` and `s`. This is an especially direct reason the
family is not an FEI counterexample.

## Literature boundary

O'Donnell--Tan's composition theorem assumes inner functions on disjoint
variable sets. It neither states nor repairs the shared-factor `Phi` law under
review. The O'Donnell--Wright--Zhou symmetric-function theorem covers the
majority core's ordinary FEI endpoint, not this upper-set singleton potential.

## Reproduction

`CHECK_REVIEW.py` constructs the original Boolean truth tables for nine
`(r,m)` pairs, recomputes every relevant Walsh coefficient and physical
influence, verifies both reveal orders, and checks 1,000 exact rational forms
of the central-binomial inequalities. It imports no author code.
