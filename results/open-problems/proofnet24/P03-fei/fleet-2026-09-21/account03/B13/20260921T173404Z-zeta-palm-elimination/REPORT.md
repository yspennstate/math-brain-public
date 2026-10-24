# B13 FEI Booleanity profile — zeta-Palm elimination and vector phase constraints

**Status:** PARTIAL / PROVED universal auxiliary identities + REFUTED stronger shortcuts + new OPEN proof target. Full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.

**Execution:** **WITHOUT_VERIFIED_BRAIN**. No genuine authenticated mathematical/cognitive brain retrieval or receiver-context use occurred in this run.

**Route:** APPROACHES 2/13/14. The run changes category from atomwise cancellation payment to **coordinate elimination of the upper-zeta cancellation functional**, and keeps the exact Boolean phase/autocorrelation constraints rather than replacing the spectral sample by an arbitrary random set. It does not re-run the settled read-once certificate or settled sweeps.

**No novelty claim:** the statements below are new-to-this fleet run unless explicitly inherited. No publication-priority claim is made without a dedicated primary-literature comparison.

## 1. Frontier used

The owner handoff records the exact cancellation functional

\[
B_{\rm can}(P)=\sum_A P(A)\log_2\frac{U_P(A)}{P(A)},\qquad
U_P(A)=\sum_{B\supseteq A}P(B),
\]

and the exact reduction

\[
H(f)\le 2I(f)+2B_{\rm can}(f).
\]

It also records a balanced-composition lower obstruction: any universal bound `B_can <= c I` must have

\[
c\ge c_*:=2.32399499026264678602\ldots.
\]

Thus proving `B_can <= c_* I` would already prove full FEI with the explicit universal constant

\[
2+2c_*=6.64798998052529357204\ldots,
\]

not claimed sharp for FEI.

The immediately preceding complete B13 report proved the exact zeta-posterior Jensen-gap identity and showed that paying every zeta gap atomwise by `(2/ln 2) * disagreement` is false. The later B13 run left a reproducer for a coordinate-elimination experiment but no accompanying report. This run completes that route.

## 2. Exact universal statement attempted: sharp projected coordinate elimination

Let `f:{-1,1}^n->{-1,1}` be Boolean and let `S` be its spectral sample,

\[
\Pr[S=A]=\widehat f(A)^2.
\]

For `R subseteq [n]`, write `P_R` for the law of `S intersect R` and

\[
B_R:=B_{\rm can}(P_R).
\]

For `i in R`, the spectral marginal is projection-invariant:

\[
\alpha_i:=\Pr[i\in S]=\operatorname{Inf}_i(f).
\]

The new target is

> **Projected zeta-Palm elimination conjecture `E(c_*)`.** For every Boolean `f` and every nonempty `R`, there is an `i in R` with `alpha_i>0` such that
> \[
> \boxed{B_R-B_{R\setminus\{i\}}\le c_*\alpha_i.}
> \tag{E}
> \]
> Irrelevant coordinates with `alpha_i=0` may simply be deleted at zero cost.

If (E) holds, recursively choose such a coordinate and telescope:

\[
B_{[n]}
=\sum_t\bigl(B_{R_t}-B_{R_{t+1}}\bigr)
\le c_*\sum_i\alpha_i
=c_* I(f).
\]

Together with `H <= 2I+2B_can`, this would prove full FEI with constant `6.64798998052529357204...`.

The composition obstruction makes `c_*` the smallest plausible universal constant for this exact cancellation route: a smaller constant cannot hold globally.

**Current classification of (E): OPEN.** The computations below support it only in finite/structured tests.

## 3. PROVED: exact zeta-Palm deletion identity

This identity is valid for **every** probability law on subsets, with no Boolean assumption.

Let `P` be a law on subsets of a finite coordinate set `R`, fix `i in R`, and for `A subseteq R\{i}` define

\[
a_A=P(A),\qquad b_A=P(A\cup\{i\}),\qquad q_A=a_A+b_A,
\]

\[
r_A=\frac{b_A}{q_A},\qquad
U_A=\sum_{B\supseteq A}q_B,\qquad
V_A=\sum_{B\supseteq A}b_B,
\qquad
\bar r_A=\frac{V_A}{U_A},
\]

with zero-mass cells omitted. Then `q` is exactly the projection deleting coordinate `i`, and

\[
\alpha_i=\sum_A b_A=\sum_Aq_Ar_A.
\]

### Proposition 3.1 — zeta-Palm deletion formula

\[
\boxed{
B_{\rm can}(P)-B_{\rm can}(q)
=\sum_Aq_A\left[(1-r_A)\log_2\frac1{1-r_A}
+r_A\log_2\frac{\bar r_A}{r_A}\right].
}
\tag{3.1}
\]

Equivalently,

\[
B_{\rm can}(P)-B_{\rm can}(q)
=\sum_Aq_A h_2(r_A)+\sum_Aq_Ar_A\log_2\bar r_A.
\tag{3.2}
\]

### Proof

For a cell `A` not containing `i`, its upper-zeta mass in `P` is `U_A`; for the paired cell `A union {i}` it is `V_A`. Hence the pair's contribution to the difference is

\[
a_A\log_2\frac{U_A}{a_A}
+b_A\log_2\frac{V_A}{b_A}
-q_A\log_2\frac{U_A}{q_A}.
\]

Substitute `a_A=q_A(1-r_A)`, `b_A=q_Ar_A`, and `V_A/U_A=\bar r_A`; this is exactly the summand in (3.1). Summing over `A` proves the claim. QED.

Two useful universal corollaries are

\[
B_{\rm can}(P)-B_{\rm can}(q)
\le \sum_Aq_A h_2(r_A)
\le h_2(\alpha_i),
\tag{3.3}
\]

because `log_2 bar r_A <= 0` and binary entropy is concave, and

\[
\frac{B_{\rm can}(P)-B_{\rm can}(q)}{\alpha_i}
\le \frac1{\ln2}
+\mathbb E_{A\sim\mu_i}\log_2\frac{\bar r_A}{r_A},
\qquad
\mu_i(A)=\frac{q_Ar_A}{\alpha_i},
\tag{3.4}
\]

because `(1-r) log_2(1/(1-r)) <= r/ln 2`.

Thus the hard part of a sharp elimination theorem is now isolated as an **upper-zeta Palm inflation term**. A sufficient form of (E) is to find at every projected state a coordinate satisfying

\[
\mathbb E_{\mu_i}\log_2\frac{\bar r_A}{r_A}
\le c_*-\frac1{\ln2}
=0.8812999493736835\ldots.
\tag{3.5}
\]

This is a target, not a proved inequality.

## 4. PROVED: the exact Boolean constraint that survives projection is vector-valued

The deletion identity alone applies to arbitrary random sets, so Booleanity must enter elsewhere. For a projected Boolean spectrum it survives as a full family of phase/cross-correlation equations.

Let `E=[n]\R` be the eliminated coordinates. For `A subseteq R\{i}` and `B subseteq E`, define

\[
u_A(B)=\widehat f(A\cup B),\qquad
v_A(B)=\widehat f(A\cup\{i\}\cup B).
\]

Since `f^2=1`, Fourier convolution gives

\[
\sum_T\widehat f(T)\widehat f(T\triangle C)=0
\quad\text{for every nonempty }C.
\]

Taking `C={i} triangle D` with `D subseteq E` and pairing the terms with and without `i` gives the exact projected constraint

\[
\boxed{
\sum_{A\subseteq R\setminus\{i\}}
\sum_{B\subseteq E}u_A(B)v_A(B\triangle D)=0
\quad\text{for every }D\subseteq E.
}
\tag{4.1}
\]

Meanwhile

\[
q_A=\|u_A\|_2^2+\|v_A\|_2^2,
\qquad
r_A=\frac{\|v_A\|_2^2}{q_A}.
\]

So after coordinates are projected away, Booleanity is **not** captured by a scalar sign choice for `sqrt(q_A r_A(1-r_A))`; it is a simultaneous cyclic cross-correlation cancellation for vector amplitudes. This is the concrete phase information that an arbitrary subset-law relaxation throws away.

In the unprojected case `E` is empty and (4.1) reduces to

\[
\sum_A \widehat f(A)\widehat f(A\cup\{i\})=0.
\]

Hence the edge magnitudes

\[
x_A=\sqrt{a_Ab_A}=q_A\sqrt{r_A(1-r_A)}
\]

admit signs summing to zero. In particular the largest satisfies the polygon inequality

\[
\max_A x_A\le\sum_{B\ne A_{\max}}x_B.
\tag{4.2}
\]

This supplies an exact, elementary Booleanity rejection test for candidate scalar laws.

## 5. Decisive counterexample searches and finite tests

### 5.1 `E(c_*)` survives every Boolean function through n=4, including every projection

The computation enumerated all Boolean functions modulo global sign for `n<=4`, and for **every** nonempty projection `R` evaluated

\[
M(f,R)=\min_{i\in R,\alpha_i>0}
\frac{B_R-B_{R\setminus\{i\}}}{\alpha_i}.
\]

The maxima over `(f,R)` were

| n | max M(f,R) |
|---:|---:|
| 1 | 0 |
| 2 | 1.000000000000000 |
| 3 | 1.450067264945063 |
| 4 | 1.5986262864861307 |

All are well below `c_*=2.3239949902626468...`. These are **exhaustive finite numerical checks**, not a universal proof.

The corresponding sufficient Palm-log quantity from (3.5) has max-min values `0`, `0`, `0.3304820237218406`, `0.42510992953527305` for `n=1,2,3,4`, again below the target `0.8812999493736835...`.

### 5.2 External Numaro n=18 seed: good existential path, bad adversarial path

The recovered external balanced monotone seed was reconstructed from the archived slices and its published truth-table SHA-256 was matched exactly:

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

For this seed,

\[
I=261/128=2.0390625,
\]

\[
B_{\rm can}=2.4147760445697815,
\qquad
B_{\rm can}/I=1.184257983543801.
\]

At the full 18-coordinate state, the largest single-coordinate deletion ratio is

`2.0999462531209474`.

A greedy elimination path that always removes a currently cheapest coordinate has maximum deletion ratio

`1.439873600991221`.

Along that greedy path, the largest Palm-log term from (3.4) is only

`0.055013879112037596`.

However, deliberately removing the nine auxiliary coordinates first gives successive deletion ratios

`2.0999462531, 2.2409437567, 2.3541992326, 2.4389706530, 2.5213648518, 2.5893302447, 2.6466280338, 2.7000391297, 2.7496083601`.

The corresponding Palm-log terms start

`0.8767673631, 0.9652354075, 1.0433240615, ...`

and reach `1.3728768176`.

Therefore the stronger statement

> every coordinate at every projected state obeys the `c_*` payment

is **REFUTED computationally with a large margin** on this genuine Boolean-derived projection family. The proof target must be existential/selection-based, exactly as (E) states. The current greedy path is evidence only; it does not check all `2^18` projections.

### 5.3 Arbitrary subset laws can cross c_* locally, but a phase certificate rejects the example

For a three-coordinate base set let

\[
q_A=(1/16)^{|A|}(15/16)^{3-|A|},
\qquad
r_A=\frac{9^{|A|}}{72900},
\]

and add a fourth coordinate with conditional inclusion probability `r_A`. This is a valid random-set law. For the added coordinate,

\[
\alpha=1/21600,
\qquad
\frac{\Delta B_{\rm can}}{\alpha}=2.538865093660809>c_*.
\]

So a pointwise `c_*` deletion inequality is false for arbitrary subset laws.

But this law fails the exact unprojected Boolean phase condition (4.2). Its empty-cell edge magnitude is

`0.0030517368813046766`,

while the sum of all other edge magnitudes is only

`0.002221240771854085`.

The dominance can be certified without floating point. With `c=1/72900`,

\[
\left(\frac{3375}{4096}\right)^2(1-c)
>
\left(\frac{2457}{4096}\right)^2,
\]

which is exactly the squared form of `x_empty > sum_{A!=empty} x_A` after upper-bounding the nonempty terms by `sqrt(c)[(9/8)^3-(15/16)^3]`. Hence no choice of Fourier signs can satisfy the required shift autocorrelation. This is a concrete demonstration that Booleanity, not random-set entropy alone, is doing essential work.

### 5.4 APPROACH 14 shortcut killed exactly: spectral samples need not be negatively associated

Take the Boolean truth table, in lexicographic order on three bits,

\[
(-1,1,1,-1,-1,-1,-1,-1).
\]

Its normalized Walsh coefficients are

\[
(-1/2,0,0,-1/2,1/2,0,0,-1/2),
\]

so the spectral sample is uniform on masks `{0,3,4,7}`. For coordinates 0 and 1,

\[
\Pr[0\in S]=\Pr[1\in S]=1/2,
\qquad
\Pr[0,1\in S]=1/2.
\]

Thus

\[
\operatorname{Cov}(1_{0\in S},1_{1\in S})=1/4>0.
\]

Therefore the blanket claim that Boolean spectral samples are negatively associated is **REFUTED exactly**. In particular, a route that first proves all spectral samples are standard determinantal/negatively-associated point processes cannot prove unrestricted FEI. Coding/point-process transfer must use a different structure, such as the vector phase identities (4.1).

## 6. What moved and what did not

**PROVED, universal for arbitrary subset laws:** the zeta-Palm deletion identity (3.1), the entropy corollary (3.3), and the Palm-log reduction (3.4).

**PROVED, universal for projected Boolean spectra:** the vector cross-correlation constraints (4.1). The scalar polygon test (4.2) is the unprojected special case.

**REFUTED exactly:** universal negative association of Boolean spectral samples.

**REFUTED computationally on a genuine Boolean-derived projection path:** the stronger rule that every coordinate/every elimination order satisfies the `c_*` local payment.

**COMPUTATIONAL EVIDENCE ONLY:** exhaustive `n<=4` survival of the existential projected elimination conjecture, the Numaro greedy-path maximum `1.439873600991221`, and the reported floating-point deletion ratios.

**OPEN:** projected elimination conjecture (E), a universal dimension-independent bound on `B_can/I`, and full uniform-cube FEI.

## 7. Next attack

The next useful target is no longer another atomwise constant or another small-n audit. It is a **coordinate-selection lemma from the vector autocorrelation constraints**:

> Given the projected vectors `u_A,v_A` satisfying all equations (4.1), prove that for at least one remaining coordinate `i`, the Palm-log term in (3.4) is at most `0.8812999493736835...`, or prove a slightly weaker constant still sufficient for some dimension-independent FEI bound.

A concrete first move is to Fourier-transform (4.1) in the eliminated shift `D`. For every assignment/character of the eliminated coordinates this turns the entire cross-correlation family into a scalar orthogonality relation between the two restriction-side coefficient vectors. The desired payment should then be sought as an **average of scalar orthogonality deficits over restriction fibers**, rather than as a scalar polygon inequality on the projected square masses. This keeps the phase information that the zeta-posterior counterexamples show is indispensable, while giving an explicit selection variable (the coordinate `i`) to avoid the adversarial Numaro elimination path.
