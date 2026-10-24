Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but this runtime exposes no authenticated model-effort selector or applied-effort receipt, so I do not claim otherwise.

**SOURCE MOVEMENT.** The exact certified interval for the true iid-binary-string Chvatal--Sankoff constant shrinks strictly again. The previous P02 spectral strictification used a non-primitive integer scaling of the C045 covering operator. This run extracts the exact common monomial content first and proves a stronger algebraic-integer gap. In exact form,

\[
W_{\rm before}=\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm old})}-L
\quad\longrightarrow\quad
W_{\rm after}=\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm prim})}-L
<W_{\rm before},
\]

where

\[
L=\frac{99083249}{125000000}=0.792665992,
\qquad t=\frac{256717}{800000},
\]

and

\[
\varepsilon_{\rm prim}=K^N\varepsilon_{\rm old},
\qquad
K=36663618914556095488>1,
\qquad N=11614187.
\]

Thus this is a strict improvement of the original problem's deterministic upper bound, not another decimal enclosure of the same endpoint. It is still numerically microscopic: the new half-gap is of order `10^(-703831633)`, versus about `10^(-931054321)` in the preceding run.

# P02 / T02 — primitive-content algebraic spectral gap for the binary LCS covering operator

## 1. Source recovery and current status

The source target is the Chvatal--Sankoff constant for two independent iid uniform binary strings,

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,\operatorname{LCS}(X_1^n,Y_1^n)}{n}.
\]

The model throughout this run is the actual pair of source strings and hence the genuinely dependent match array. The independent Bernoulli matching model is not substituted.

Alexander Tiskin's `arXiv:2212.01582v2`, last revised 2024-08-13, still states that the coefficient is unresolved. Its comments explicitly say that claims in the preprint about the process and the constant turned out to be incorrect and were removed, retaining only the supported estimate. Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer (`arXiv:2407.10925`) give the rigorous lower bound

\[
\gamma_2\ge 0.792665992.
\]

The conventional published upper endpoint remains Lueker's `0.826280`. The stronger C045 upper certificate used below is a private-repository exact candidate; it remains distinct from a public-priority claim and from final independent certification.

The prior P02 target, Aldous--Fill Open Problem 2.34, remains only a completed handoff and is not reopened.

## 2. Continuity and nonduplication

The latest P02 report was

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T01-37-20Z__algebraic-integer-spectral-gap-report.md`.

That report started from the exact C045 cone certificate and proved that its rational Collatz number cannot equal the spectral radius of an integer scaling. With the old scaling constant

\[
C_{\rm old}=50707486515870312693760000000000000000000000000000000000000000,
\]

it obtained an explicit half-gap

\[
\varepsilon_{\rm old}
=\frac{1}{2C_{\rm old}b(2a_{\rm old})^{N-1}}.
\tag{2.1}
\]

The complementary P13 report

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T01-24-00Z__boundary-carry-reachable-reset-certified-endpoint.md`

works the dependence-preserving boundary-carry / stationary-strip route. P13 derives an exact stationary boundary-event formula and a reset estimate. This P02 run does not duplicate that recursion; it stays on the finite covering/cone variational side.

The essential earlier LCS attempts are preserved rather than restarted:

- C027: dependence-preserving bivariate diagonal covering transfer for actual ordered string pairs;
- C045: complete length-six local-deficiency language, 11,614,187-state reachable product, exact all-row positive cone witness and the retained rational upper certificate;
- C046--C050: tail stability, reset, symbolic Bellman and symmetry attempts without a stronger deterministic endpoint;
- first P02 T02 run: log-convex interpolation theorem and proof that geometric interpolation of existing certificates cannot beat the better endpoint;
- previous P02 run: universal algebraic-integer strictification, source-level but with an enormous degree-`N` separation loss;
- P13: a different correlated-strip lower-bound program, reserved to P13.

## 3. Exact C045 symmetric weights and the hidden primitive content

At the inherited symmetric fugacity

\[
t=\frac pq=\frac{256717}{800000},
\qquad r=q-p=543283,
\]

the normalized C045 label weights are, for hook magnitude `a=0,...,6`,

\[
w_a=t^{a+2},
\]

and for the geometric tail `|ell|=7`,

\[
w_7=\frac{t^9}{1-t}.
\]

This is read directly from the exact C045 cone checker: after division by its common raw denominator, the finite operator `A` is a nonnegative sum of transition matrices weighted by these eight numbers.

Every weight has a common factor `t^2`. Write

\[
A=t^2H.
\tag{3.1}
\]

Then the label weights of `H` are

\[
1,t,t^2,\ldots,t^6,\frac{t^7}{1-t}.
\tag{3.2}
\]

Because `gcd(p,q)=gcd(q,q-p)=1`, their reduced denominators are

\[
1,q,q^2,\ldots,q^6,q^6(q-p).
\]

Hence their exact least common denominator is

\[
\boxed{S=q^6(q-p)
=142418378752000000000000000000000000000000.}
\tag{3.3}
\]

The executed checker also verifies that after multiplying the eight weights in (3.2) by `S`, their integer gcd is exactly `1`. Thus the scalar normalization is primitive at the label level; the preceding run's `C_old` scaling carried a very large avoidable common content.

## 4. Primitive algebraic-integer strictification

The inherited exact C045 cone certificate is

\[
AV\le \lambda V
\]

for a positive integer vector `V`, with

\[
\lambda=
\frac{10114875937111444750637950885399422919832438289108176982868202874026753}
{29591135160849999997918500618240000000000000000000000000000000000000000}.
\tag{4.1}
\]

Using (3.1),

\[
HV\le \Lambda V,
\qquad
\Lambda:=\frac{\lambda}{t^2}.
\tag{4.2}
\]

Set

\[
B:=SH.
\]

By (3.2)--(3.3), `B` is a nonnegative integer matrix of dimension `N=11,614,187`.
Reduce

\[
R:=S\Lambda=\frac ab.
\]

Exact arithmetic gives

\[
\boxed{
a=1995237757733917147310102692686664915858011319606812684127301,
}
\tag{4.3}
\]

\[
\boxed{b=4220452010631561279>1.}
\tag{4.4}
\]

### Theorem P02-T02-B (primitive-content spectral gap)

With the preceding notation,

\[
\rho(A)
\le
\lambda-
\frac{t^2}{S b(2a)^{N-1}}.
\tag{4.5}
\]

Consequently, defining

\[
\boxed{
\varepsilon_{\rm prim}
:=\frac{t^2}{2S b(2a)^{N-1}},
\qquad
\lambda_{\rm prim}:=\lambda-\varepsilon_{\rm prim},
}
\tag{4.6}
\]

we have

\[
\rho(A)<\lambda_{\rm prim}<\lambda.
\tag{4.7}
\]

### Proof

Since `B=SH` is an integer matrix, every eigenvalue of `B`, in particular `mu=rho(B)`, is an algebraic integer. The rational number `R=a/b` in lowest terms is not an integer because `b>1`; therefore `mu != R`. From the inherited cone bound, `rho(H)<=Lambda`, hence `mu<=R`, so in fact `mu<R`.

Let `chi_B(z)` be the monic characteristic polynomial of `B`, of degree `N`. Since `R` is not an eigenvalue,

\[
\chi_B(R)\ne0.
\]

Because `chi_B` has integer coefficients and `R=a/b` is reduced,

\[
|\chi_B(R)|\ge b^{-N}.
\tag{4.8}
\]

Write the eigenvalues of `B` as `mu=mu_1,mu_2,...,mu_N`. Nonnegativity gives `|mu_j|<=mu<R`. Hence

\[
|R-\mu_j|<2R
\]

for every `j`, and separating the Perron factor,

\[
b^{-N}
\le |\chi_B(R)|
=(R-\mu)\prod_{j=2}^N|R-\mu_j|
\le (R-\mu)(2R)^{N-1}.
\]

Therefore

\[
R-\mu
\ge
\frac{1}{b(2a)^{N-1}}.
\tag{4.9}
\]

Divide by `S` to obtain

\[
\Lambda-\rho(H)
\ge\frac{1}{S b(2a)^{N-1}}.
\]

Finally multiply by `t^2` and use `A=t^2H` to get (4.5). Taking half the certified gap gives (4.6)--(4.7). QED.

No irreducibility, eigenvalue numerics, independent-cell model, or unproved asymptotic assumption appears in this argument.

## 5. Exact improvement over the previous P02 strictification

The previous run reduced

\[
C_{\rm old}\lambda=\frac{a_{\rm old}}b
\]

with the same denominator `b` and

\[
a_{\rm old}=
73152636793489737215990673737054116728851707313438976312511094995075475303717888.
\]

The new primitive normalization gives the exact integer factor

\[
\boxed{
K:=\frac{C_{\rm old}t^2}{S}
=36663618914556095488,
}
\tag{5.1}
\]

and exact arithmetic verifies

\[
a_{\rm old}=Ka.
\tag{5.2}
\]

Combining (2.1), (4.6), (5.1) and (5.2),

\[
\frac{\varepsilon_{\rm prim}}{\varepsilon_{\rm old}}
=
\frac{C_{\rm old}t^2}{S}
\left(\frac{a_{\rm old}}a\right)^{N-1}
=K^N.
\tag{5.3}
\]

Since `K>1`, this proves exactly

\[
\boxed{\varepsilon_{\rm prim}>\varepsilon_{\rm old}}
\tag{5.4}
\]

without materializing either enormous power. For scale only,

\[
\log_{10}K^N\approx 227222687.636467,
\]

so primitive normalization improves the explicit spectral separation by more than `10^227,222,687` relative to the preceding universal certificate. The absolute gap is nevertheless still tiny because the characteristic-polynomial separation retains degree `N`.

## 6. Dependence-preserving transfer and the new source upper bound

The C045 finite operator is a covering operator for actual ordered binary string pairs. C027, and the first P02 T02 run independently, proved the following source-faithful transfer: if the accepted-list weights of the covering machine at `(x,y)` have exponential rate at most `z<1`, then counting underlying ordered string pairs gives

\[
\Pr(L_n\ge m)\le C_0(4xy)^{-n}z^m
\]

for a finite prefactor `C_0`, and hence

\[
\gamma_2\le\frac{\log(4xy)}{\log z}.
\tag{6.1}
\]

The proof counts the actual pairs `(X_1^n,Y_1^n)` and divides by their exact probability `4^{-n}`; it never makes the `n^2` match indicators independent.

By (4.7), every number strictly above `rho(A)` is a valid finite-matrix exponential rate, so `z=lambda_prim` is admissible in (6.1). At `x=y=t`,

\[
\boxed{
\gamma_2\le
U_{\rm prim}:=
\frac{\log(4t^2)}{\log\lambda_{\rm prim}}.
}
\tag{6.2}
\]

Because `0<4t^2<1` and the map

\[
z\mapsto\frac{\log(4t^2)}{\log z}
\]

is strictly increasing on `(0,1)`, (5.4) implies

\[
\boxed{
U_{\rm prim}<U_{\rm old}:=
\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm old})}.
}
\tag{6.3}
\]

This is the required strict source-level interval shrink.

## 7. Metric before and after

The rigorous lower endpoint is unchanged:

\[
L=0.792665992.
\]

Before this run, the strongest P02 exact interval was

\[
\boxed{L\le\gamma_2\le U_{\rm old}},
\qquad
U_{\rm old}=\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm old})}.
\]

After this run,

\[
\boxed{L\le\gamma_2\le U_{\rm prim}},
\qquad
U_{\rm prim}=\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm prim})},
\]

with `U_prim<U_old`. Thus the fixed metric moves exactly from

\[
\boxed{W_{\rm before}=U_{\rm old}-L}
\]

to

\[
\boxed{W_{\rm after}=U_{\rm prim}-L<W_{\rm before}.}
\]

At ordinary displayed precision all these repository-internal upper endpoints still begin

`0.82627594276228262501510658...`.

The executed checker reports, diagnostically,

`log10(epsilon_old) ~= -931054320.784411`,

`log10(epsilon_prim) ~= -703831633.147943`.

These logarithms are scale diagnostics only; the interval comparison is exact through (5.3).

The source problem remains **OPEN / PARTIAL**. This run does not determine `gamma_2`.

## 8. Failed/closed routes and next attack

The earlier geometric interpolation idea remains closed: P02 already proved that coefficientwise geometric interpolation of existing positive cone certificates cannot beat the better endpoint. The current run also explains why the preceding algebraic gap was unnecessarily weak: it applied algebraic integrality before extracting the common `t^2` content and primitive denominator of the label weights.

The next high-value route is graph-specific rather than another arithmetic normalization. The remaining loss comes entirely from the degree-`N` root-separation step. A useful next theorem would identify a small recurrent quotient, SCC, synchronizing family, or local multiplicative correction to the C045 witness, yielding a gap controlled by an actual short graph scale rather than by `N=11,614,187`. That is complementary to P13's stationary boundary recursion.

## 9. Exact checker and readback

Executed exact checker:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T02-09-23Z__primitive_content_gap_checker.py`

creation commit `65ca748693fbb21d51d2fabe1b1cee64f42194ab`, verified blob `ca7a50c007b59308f5e0e3c79f6dd6eec6bee941`.

Archived output:

`proofnet24/P02-progress-lcs/artifacts/2026-09-20T02-09-23Z__primitive_content_gap_checker.out`

creation commit `8ef2b7c5717a054fd6233d6e1482f0734ea5d319`, verified blob `756f0b3d84bc2342709421e64272e56dc3d4ea31`.

The output ends `source_interval_strictly_shrinks_again=PASS` and `ALL_EXACT_CHECKS_PASS`.

No historical file, peer file, shared root ledger, schedule, email, Drive object, public posting, paid compute, or access permission was changed.

```yaml
ledger_delta:
  track: P02
  target: T02
  source: "Chvatal--Sankoff gamma_2 for two independent iid uniform binary strings"
  source_status: OPEN
  metric: "certified deterministic interval width U-L"
  lower_before: "99083249/125000000"
  lower_after: "99083249/125000000"
  upper_before: "log(4*t^2)/log(lambda-epsilon_old)"
  upper_after: "log(4*t^2)/log(lambda-epsilon_prim)"
  width_before: "log(4*t^2)/log(lambda-epsilon_old)-99083249/125000000"
  width_after: "log(4*t^2)/log(lambda-epsilon_prim)-99083249/125000000"
  strict_movement: true
  t: "256717/800000"
  N: 11614187
  primitive_scalar_factor: "t^2"
  primitive_lcd_S: "142418378752000000000000000000000000000000"
  primitive_R_num: "1995237757733917147310102692686664915858011319606812684127301"
  primitive_R_den: "4220452010631561279"
  epsilon_improvement_factor: "36663618914556095488^11614187"
  mechanism_advance: "primitive-content extraction before algebraic-integer root separation"
  dependence_preserving: true
  bernoulli_matching_used: false
  companion_scope: "P13 owns boundary-carry/stationary-strip recursion; not duplicated"
  status: PARTIAL
```
