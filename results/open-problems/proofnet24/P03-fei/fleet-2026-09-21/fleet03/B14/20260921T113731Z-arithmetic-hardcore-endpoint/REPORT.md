# B14 — arithmetic obstruction at the exact scalar-erasure hard-core endpoint

**Run:** 2026-09-21  
**Role:** FEI erasure and selector proof  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Target:** full uniform-cube Fourier entropy-influence conjecture. **OPEN / NOT PROVED.**  
**New result status:** the endpoint theorem below is **PROVED for its stated exact-equality hypothesis**. It is not a proof of FEI and has not received independent closure review. Publication/novelty priority is **UNVERIFIED**.

## 1. Exact route attempted

The immediately preceding B14 scalar-frontier result starts from the exact coordinate fibre representation

\[
\alpha_i=\sum_T w_Tq_T,\qquad
B_i=\sum_Tw_Th_2(q_T),\qquad
\Delta_iH=\sum_Tw_T\Psi(q_T),
\]

where

\[
\Psi(q)=h_2(q)+1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right).
\]

For `r>4`, put

\[
\beta(q)=\frac{h_2(q)}q,\qquad
\kappa(q)=\frac{\Psi(q)}q,
\]

and let `tau=tau(r) in (0,1/2)` be the unique solution `kappa(tau)=r`.  The sharp scalar theorem says that

\[
\Delta_iH\ge r\alpha_i
\quad\Longrightarrow\quad
B_i\ge\beta(\tau)\alpha_i,
\]

and equality in both statements forces every positive fibre posterior to equal `tau`.

If one restriction-critical Boolean function saturates this scalar frontier at **every** relevant coordinate, the preceding run proved that its squared Fourier law has the form

\[
\boxed{
 p_S=\widehat f(S)^2=p_\varnothing\,\theta^{|S|}\,\mathbf 1_{\{S\in\mathcal F\}},
 \qquad \theta=\frac\tau{1-\tau}\in(0,1),
}
\tag{1}
\]

where `mathcal F` is a downward-closed family containing `emptyset` and every singleton corresponding to a relevant coordinate.

The creative question in this run was:

> **Can an arbitrary real activity `theta` actually occur in an exact Boolean endpoint (1), once the signs of the Fourier coefficients and the exact Boolean convolution identities are restored?**

The answer is no: exact Booleanity discretizes the endpoint activity.

## 2. PROVED: exact endpoint activity is the reciprocal of an integer square

### Theorem 2.1 — arithmetic endpoint obstruction

Let `f:{-1,1}^n->{-1,1}` be nonconstant. Assume its squared Fourier law has the exact hard-core down-set form (1) for some `0<theta<1`, and assume every relevant coordinate belongs to the downward support in the sense inherited from the scalar-frontier equality case. Then there is an integer `m>=2` such that

\[
\boxed{\sqrt\theta=\frac1m,\qquad \theta=\frac1{m^2}.}
\tag{2}
\]

Consequently, if this law comes from an exact scalar-frontier critical endpoint with ratio `r`, then

\[
\boxed{
 \tau=\frac1{m^2+1},\qquad
 r=r_m:=\kappa\!\left(\frac1{m^2+1}\right).
}
\tag{3}
\]

Thus the simultaneous exact endpoint ratios form a discrete sequence, not a continuum.

### Proof

Because `f` is Boolean on `n` bits,

\[
2^n\widehat f(S)=\sum_x f(x)\chi_S(x)\in\mathbb Z
\tag{4}
\]

for every `S`.  Let `i` be relevant.  Downward closure gives `emptyset,{i} in mathcal F`, so both Fourier coefficients are nonzero.  From (1),

\[
\frac{|\widehat f(\{i\})|}{|\widehat f(\varnothing)|}=\sqrt\theta.
\tag{5}
\]

The left side is a ratio of nonzero integers after multiplication by `2^n`; hence

\[
\sqrt\theta=\frac ab
\]

for coprime positive integers `a<b`.

Now use Booleanity in its signed form, not merely the squared spectrum. Since `f^2=1`, the nonconstant Fourier coefficient of `f^2` at `{i}` vanishes:

\[
0=\widehat{f^2}(\{i\})
 =\sum_S\widehat f(S)\widehat f(S\triangle\{i\})
 =2\sum_{T\subseteq[n]\setminus\{i\}}
 \widehat f(T)\widehat f(T\cup\{i\}).
\tag{6}
\]

Define the lower link

\[
\mathcal L_i:=\{T\subseteq[n]\setminus\{i\}:T\cup\{i\}\in\mathcal F\}.
\]

It contains `emptyset`.  For `T in mathcal L_i`, write the Fourier signs as `sigma_T in {+-1}`.  Equation (1) gives

\[
\widehat f(T)\widehat f(T\cup\{i\})
=p_\varnothing\sqrt\theta\,
\varepsilon_i(T)\,\theta^{|T|},
\qquad \varepsilon_i(T)\in\{+-1\}.
\]

Dividing (6) by the nonzero factor `2p_emptyset sqrt(theta)` yields the exact signed-link identity

\[
\boxed{
\sum_{T\in\mathcal L_i}\varepsilon_i(T)\theta^{|T|}=0.
}
\tag{7}
\]

Group by rank and define

\[
P_i(z):=\sum_{T\in\mathcal L_i}\varepsilon_i(T)z^{|T|}\in\mathbb Z[z].
\tag{8}
\]

Its constant term is `epsilon_i(emptyset)=+-1`, so `P_i` is a nonzero integer polynomial.  Equation (7) says that

\[
P_i(\theta)=0.
\]

But `theta=a^2/b^2` is rational in lowest terms.  By the rational-root theorem its numerator `a^2` divides the constant term `+-1`. Therefore `a=1`.  Setting `m=b>=2` proves (2).  Formula (3) follows from `tau=theta/(1+theta)` and the endpoint defining relation `r=kappa(tau)`. QED.

## 3. PROVED: every exact endpoint link must be large and highly connected

The same signed identity gives a combinatorial expansion requirement that does not use the rational-root theorem.

### Proposition 3.1 — link-mass and co-neighbor lower bounds

Under Theorem 2.1, for every relevant coordinate `i`,

\[
\boxed{
\sum_{\substack{T\in\mathcal L_i\\T\ne\varnothing}}
\theta^{|T|}\ge1.
}
\tag{9}
\]

Hence, writing

\[
N_i:=\{j\ne i:\{i,j\}\in\mathcal F\},\qquad d_i:=|N_i|,
\]

one has

\[
\boxed{
 d_i\ge
 \left\lceil\frac{\log2}{\log(1+\theta)}\right\rceil
 =
 \left\lceil\frac{\log2}{\log(1+m^{-2})}\right\rceil.
}
\tag{10}
\]

Moreover

\[
\boxed{|\mathcal L_i|\ge m^2+1.}
\tag{11}
\]

### Proof

Separate the `T=emptyset` term in (7). Its absolute value is one, so the triangle inequality gives

\[
1\le\sum_{T\in\mathcal L_i,\,T\ne\varnothing}\theta^{|T|},
\]

which is (9).

If `T in mathcal L_i` and `j in T`, then `{i,j} subseteq T union {i} in mathcal F`; downward closure gives `{i,j} in mathcal F`. Thus every such `T` is a subset of `N_i`, and therefore

\[
1
\le\sum_{T\in\mathcal L_i,\,T\ne\varnothing}\theta^{|T|}
\le (1+\theta)^{d_i}-1.
\]

This proves (10).  Finally every nonempty term in (9) is at most `theta=1/m^2`, so at least `m^2` nonempty terms are required, proving (11). QED.

A convenient interpretation is that exact scalar equality is incompatible not only with a product endpoint, but also with any low-connectivity proper-down-set endpoint.  In particular, an exact endpoint Fourier-support graph cannot be `3`-degenerate at the first nontrivial activity relevant below.

## 4. Numbers: a genuine gap around the Hod scale

The accompanying `endpoint_arithmetic.py` evaluates only the closed forms above; it is not a Boolean-function sweep.  The first values are

| `m` | `tau=1/(m^2+1)` | `r_m=kappa(tau)` | minimum `d_i` from (10) | minimum link size |
|---:|---:|---:|---:|---:|
| 2 | 0.2 | 6.264662506490406 | 4 | 5 |
| 3 | 0.1 | 7.470674987019189 | 7 | 10 |
| 4 | 0.0588235294117647 | 8.312864878674464 | 12 | 17 |
| 5 | 0.0384615384615385 | 8.962245281593505 | 18 | 26 |
| 6 | 0.0270270270270270 | 9.491293501083415 | 26 | 37 |

The current rigorous lower-bound scale from Hod's read-once construction is

\[
r_H=6.4547837\ldots.
\]

Therefore

\[
\boxed{r_2=6.2646625\ldots<r_H<r_3=7.4706749\ldots.}
\tag{12}
\]

So an exact all-coordinate scalar-frontier critical endpoint cannot have any ratio in the entire open interval

\[
(6.26466250649\ldots,\,7.47067498702\ldots).
\tag{13}
\]

In particular it cannot sit exactly at the Hod scale.  If an exact endpoint critical core has ratio strictly above `r_H`, the first arithmetically possible endpoint is `m=3`, and then **every relevant coordinate must have at least seven Fourier co-neighbors and at least ten active lower-link fibres**.

This is a structural exclusion, not a dimension-free FEI bound.

## 5. Attempted refutation and boundary cases

The argument was attacked at the three places where an exact-endpoint proof could silently fail.

1. **Could `p_emptyset=0` evade the ratio argument?** No.  Equation (1) would then force `p_S=0` for every `S in mathcal F`, contradicting normalization. Thus the empty coefficient is nonzero at an exact hard-core endpoint.
2. **Could a relevant coordinate have `hat f({i})=0`?** No under the inherited endpoint theorem: some support set containing `i` is present and `mathcal F` is downward closed, hence `{i} in mathcal F`, so its coefficient is nonzero.
3. **Could the signed convolution disappear after squaring?** The proof explicitly restores Fourier signs before applying `widehat{f^2}({i})=0`; (7) is a signed identity and is not inferred from squared probabilities alone.

The numerical table was independently recomputed in the current run from the displayed formulas.  For example

\[
r_2=6.2646625064904056\ldots,\qquad
r_3=7.4706749870191887\ldots.
\]

No exhaustive FEI sweep or read-once certificate recheck was performed.

## 6. Dead route preserved: exact arithmetic discreteness is not yet a uniform stability rebate

The tempting closure step would be:

> “Because exact endpoint activities are discrete, a critical core near the Hod value must have a fixed positive amount of scalar slack.”

That inference is **NOT PROVED and should not be used**.  Fourier coefficients are dyadic rationals with arbitrarily large denominators as dimension grows, so ratios of coefficient magnitudes can approximate a non-endpoint activity increasingly well.  Likewise, signed link polynomials can acquire increasing degree and increasingly fine root geometry.  The exact rational-root obstruction therefore gives strict nonattainment at the Hod-scale endpoint, but by itself it does **not** provide the dimension-free quantitative gap needed for full FEI.

The older stronger claim that every prescribed coordinate has a bounded universal restriction payment remains **REFUTED** and is not revived here.  The balanced-tribes pivotal-curvature counterexample also remains in force.  This report concerns only the simultaneous exact equality endpoint forced by the sharp scalar frontier.

## 7. Next attack

The next useful B14 step is now sharply defined: prove a **quantitative signed-link stability lemma**.  The target should convert small scalar-frontier slack into an approximate version of

\[
\sum_{T\in\mathcal L_i}\varepsilon_i(T)\theta^{|T|}=0
\]

with the conditional fibre ratios simultaneously close to one common `theta`.  One then needs a dimension-free dichotomy:

- either this approximate signed cancellation forces substantial link expansion / cross-coordinate dependence, which can be charged to the dual-total-correlation or restriction-entropy budget; or
- at least one coordinate incurs a definite scalar erasure rebate, giving the desired existential selector.

The arithmetic gap (12) says exactly where to try first: `theta_H=0.2203367...` lies strictly between the exact reciprocal-square activities `1/4` and `1/9`.  A successful stability theorem would turn today's strict endpoint exclusion into a quantitative payment and would attack the remaining universal FEI gap rather than another every-coordinate surrogate.

## 8. Status ledger

- Full uniform-cube FEI: **OPEN / NOT PROVED**.
- Sharp scalar-erasure frontier from the previous B14 run: **PROVED at its stated scalar scope; independent closure not supplied here**.
- Hard-core down-set endpoint implication (1): **inherited from the previous exact-equality theorem**.
- Reciprocal-integer-square activity theorem (2)-(3): **PROVED here**.
- Signed-link expansion bounds (9)-(11): **PROVED here**.
- Exact endpoint exclusion on `(r_2,r_3)`, including the Hod scale: **PROVED under the simultaneous exact-endpoint hypotheses**.
- Dimension-free stability rebate from strict endpoint exclusion: **OPEN**.
- Every-prescribed-coordinate payment: **REFUTED; not revived**.
- Brain assistance in this run: **WITHOUT_VERIFIED_BRAIN**.
