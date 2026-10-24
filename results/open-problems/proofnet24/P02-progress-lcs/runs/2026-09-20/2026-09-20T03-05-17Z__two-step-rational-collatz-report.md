Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but this runtime exposes no authenticated model/effort selector or applied-effort receipt, so I do not claim otherwise.

**SOURCE-LEVEL MOVEMENT.** For the true iid-uniform binary-string Chvatal--Sankoff problem, the exact repository-internal certified interval shrinks strictly again. The preceding P02 run had

\[
L\le \gamma_2\le U_{\rm prim}
:=\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm prim})},
\qquad
L=\frac{99083249}{125000000}=0.792665992,
\]

with

\[
\varepsilon_{\rm prim}
=\frac{t^2}{2Sb(2a)^{N-1}}.
\]

This run proves the much stronger two-step rational-Collatz gap

\[
\boxed{\rho(A)^2\le
\left(\frac{t^2}{Sb}\right)^2(a^2-1)}
\]

and hence the rational strict upper rate

\[
\boxed{\lambda_2:=\lambda-\varepsilon_2},
\qquad
\boxed{\varepsilon_2:=\frac{t^2}{2Sab}},
\]

with

\[
\rho(A)<\lambda_2<\lambda-\varepsilon_{\rm prim}.
\]

Therefore

\[
\boxed{
L\le\gamma_2\le U_2:=\frac{\log(4t^2)}{\log\lambda_2}
<U_{\rm prim}
}
\]

and the tracked width moves strictly from `U_prim-L` to `U_2-L`.

The gain is still tiny in decimal terms (the source endpoint decrease relative to the unstrictified C045 rate is about `9.67e-122`), but it replaces the preceding characteristic-polynomial gap of order `10^-703831633` by a two-step gap of order `10^-121`. This is a genuinely different mechanism: it uses the arithmetic of *tight Collatz rows plus one successor step*, not degree-`N` root separation.

# P02 / T02 — two-step rational Collatz strictification for the binary LCS covering operator

## 1. Source, status, and continuity

The target is

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The same raw source letters generate all match indicators in a row or column; no independent Bernoulli matching surrogate is used.

Fresh source check on 2026-09-20:

- Alexander Tiskin, `arXiv:2212.01582v2`, revised 2024-08-13, still calls the coefficient unresolved and explicitly says the incorrect claims from the earlier preprint were removed.
- Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`, prove the rigorous lower bound `0.792665992`.
- Lueker's published upper bound remains `0.826280`; Li--Ren--Wen (Cambridge, published online 2026-03-02) still summarize the binary constant as open with the public rigorous range ending at Lueker's upper bound.

The stronger upper endpoint below is a private-repository exact candidate, not a public-priority or external-review claim.

The latest P02 report recovered is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T02-18-00Z__primitive-content-spectral-gap-report.md`.

That run extracted the primitive scalar content of C045 and improved the previous algebraic-integer separation by an enormous factor, but retained the degree `N=11,614,187` characteristic-polynomial loss.

The prior P02 target, Aldous--Fill Open Problem 2.34, remains a completed handoff and is not reopened.

## 2. Coordination and nonduplication

The newest P13 report recovered is

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T02-06-47Z__overlapping-reset-error-and-p02-strict-update.md`.

P13 owns the correlated boundary-carry/stationary-strip recursion and improved its reset-transfer error. P02 does not duplicate that route.

The newest R17 same-source report recovered is

`runs/prob10_2026-09-20/PROB10-02/20260920T0212Z_r17_suffix_control_obstruction_4a6c.md`.

R17 is studying exact compression of the forgotten-prefix controller and proved an obstruction to arbitrary-carry suffix relaxations. P02 remains entirely on the complementary C045 covering/cone variational side.

Relevant inherited LCS work preserved rather than repeated:

1. C027: dependence-preserving bivariate covering transfer for actual ordered binary string pairs.
2. C045: complete six-factor local-deficiency language, exact 11,614,187-state reachable covering product, and an exact positive cone witness.
3. P02-T02 first run: log-convex certificate interpolation and a proof that geometric interpolation cannot improve the best endpoint.
4. P02-T02 second run: algebraic-integer strictification of the exact C045 Collatz bound.
5. P02-T02 third run: primitive-content extraction, reducing the root-separation exponent but still leaving a degree-`N` loss.
6. P13/R17: complementary correlated-strip and hidden-prefix routes, not used here.

No POSTED exclusion covers this T02 target.

## 3. Exact inherited C045 data

At the retained symmetric fugacity

\[
t=\frac{256717}{800000},
\]

the C045 covering operator can be written

\[
A=t^2H.
\]

The normalized label weights of `H` are

\[
1,t,t^2,\ldots,t^6,\frac{t^7}{1-t}.
\]

Their exact least common denominator is

\[
\boxed{S=800000^6(800000-256717)
=142418378752000000000000000000000000000000.}
\]

Thus

\[
B:=SH
\]

is a nonnegative integer matrix of dimension

\[
N=11614187.
\]

C045's frozen positive integer witness `V` satisfies the exact all-row inequality

\[
AV\le\lambda V,
\]

where

\[
\lambda=
\frac{10114875937111444750637950885399422919832438289108176982868202874026753}
{29591135160849999997918500618240000000000000000000000000000000000000000}.
\]

Equivalently,

\[
BV\le RV,
\qquad
R:=\frac{S\lambda}{t^2}=\frac ab,
\]

with

\[
\boxed{a=1995237757733917147310102692686664915858011319606812684127301},
\]

\[
\boxed{b=4220452010631561279},
\qquad \gcd(a,b)=1.
\]

The frozen-witness construction uses scale

\[
\boxed{M=5000000000000000000}
\]

and hence every integer coordinate satisfies

\[
1\le V_i\le M.
\]

The archived construction/output gives the stronger exact inequalities needed below:

\[
\boxed{b\le M<2b},
\qquad
\boxed{a>M}.
\]

## 4. New general theorem: two-step rational Collatz strictification

### Theorem P02-T02-C

Let `B` be a nonnegative integer matrix and `V` a positive integer vector with

\[
1\le V_i\le M.
\]

Suppose `a,b` are coprime positive integers with

\[
b>1,\qquad b\le M<2b,\qquad a>M,
\]

and

\[
BV\le \frac ab V.
\tag{4.1}
\]

Then

\[
\boxed{
B^2V\le\frac{a^2-1}{b^2}V
}
\tag{4.2}
\]

componentwise. Consequently

\[
\boxed{
\rho(B)\le\frac{\sqrt{a^2-1}}b
<\frac ab-\frac1{2ab}.
}
\tag{4.3}
\]

### Proof

Write

\[
r_i:=\frac{(BV)_i}{V_i}\le R:=\frac ab.
\]

Call row `i` **tight** when `r_i=R`.

#### Case 1: row `i` is not tight

Because `(BV)_i` and `V_i` are integers,

\[
aV_i-b(BV)_i
\]

is a positive integer. Therefore

\[
RV_i-(BV)_i\ge\frac1b.
\tag{4.4}
\]

Since `B` is nonnegative and `BV<=RV`,

\[
B^2V\le R BV.
\]

Thus for a non-tight row,

\[
(B^2V)_i
\le R^2V_i-\frac Rb.
\]

Because `R=a/b` and `a>M>=V_i`,

\[
\frac{R}{bV_i}=\frac{a}{b^2V_i}>\frac1{b^2},
\]

so

\[
\frac{(B^2V)_i}{V_i}
< R^2-\frac1{b^2}.
\tag{4.5}
\]

#### Case 2: row `i` is tight

Tightness means

\[
(BV)_i=\frac ab V_i.
\]

The left side is an integer and `gcd(a,b)=1`, hence

\[
b\mid V_i.
\]

But `V_i` is positive and `b<=V_i<=M<2b`; therefore

\[
\boxed{V_i=b.}
\tag{4.6}
\]

Now suppose, toward contradiction, that every successor `j` with `B_{ij}>0` were also tight. Applying (4.6) to every such successor gives `V_j=b`. Hence

\[
\frac{(BV)_i}{V_i}
=\frac{\sum_j B_{ij}b}{b}
=\sum_j B_{ij}\in\mathbb Z.
\]

But this ratio equals `R=a/b`, which is nonintegral because `b>1` and `gcd(a,b)=1`. Contradiction.

Therefore a tight row has at least one successor `j` with `B_{ij}>0` that is non-tight. For every non-tight successor, (4.4) gives

\[
RV_j-(BV)_j\ge\frac1b.
\]

Since `B_{ij}` is a positive integer, at least one such successor contributes at least `1/b` to the total two-step slack. Using tightness of row `i`,

\[
\begin{aligned}
(B^2V)_i
&=\sum_jB_{ij}(BV)_j\\
&=R\sum_jB_{ij}V_j
 -\sum_jB_{ij}\bigl(RV_j-(BV)_j\bigr)\\
&\le R(BV)_i-\frac1b\\
&=R^2V_i-\frac1b.
\end{aligned}
\]

By (4.6), `V_i=b`, so

\[
\frac{(B^2V)_i}{V_i}
\le R^2-\frac1{b^2}.
\tag{4.7}
\]

Combining (4.5) and (4.7) proves (4.2). Applying the Collatz bound to `B^2` gives

\[
\rho(B)^2=\rho(B^2)
\le\max_i\frac{(B^2V)_i}{V_i}
\le\frac{a^2-1}{b^2}.
\]

Finally,

\[
\left(a-\frac1{2a}\right)^2
=a^2-1+\frac1{4a^2}>a^2-1,
\]

so

\[
\sqrt{a^2-1}<a-\frac1{2a},
\]

which gives the strict second inequality in (4.3). QED.

### Interpretation

The theorem turns a one-step rational cone certificate into a strict two-step certificate without a characteristic polynomial, eigenvalue computation, irreducibility hypothesis, SCC enumeration, or degree-dependent root separation.

Its mechanism is arithmetic: every exactly tight row must have the same witness coordinate `b`; such a tight row cannot have only tight successors because that would make its row ratio an integer, contradicting the noninteger rational target `a/b`. Therefore every tight row loses at least one unit of integer slack after one successor step.

## 5. Instantiation for C045

For C045,

\[
A=\frac{t^2}{S}B.
\]

Theorem P02-T02-C yields

\[
\rho(A)
\le
\frac{t^2}{Sb}\sqrt{a^2-1}
<
\frac{t^2a}{Sb}-\frac{t^2}{2Sab}.
\]

But

\[
\frac{t^2a}{Sb}=\lambda.
\]

Hence define

\[
\boxed{
\varepsilon_2:=\frac{t^2}{2Sab}
}
\]

and

\[
\boxed{
\lambda_2:=\lambda-\varepsilon_2.
}
\]

Then

\[
\boxed{\rho(A)<\lambda_2<\lambda.}
\tag{5.1}
\]

Exact reduction gives

\[
\varepsilon_2=
\frac{65903618089}
{1535075104345526372517606188348729153714335661502571495486834616756974290524327316887426826240000000000000000000000000000000000000000}.
\]

For scale only,

\[
\log_{10}\varepsilon_2\approx -121.36722037053.
\]

The exact rational `lambda_2` is

\[
\frac{
22813962695543209451642208224784911108963451823248409652175723262282435016555417982747706647371718311476966393656869531077126963343
}{
66742395841109842283374182102118658857145028760981369368992809424216273501057709429888122880000000000000000000000000000000000000000
}.
\]

## 6. Strict improvement over the previous P02 certificate

The previous run used

\[
\varepsilon_{\rm prim}
=\frac{t^2}{2Sb(2a)^{N-1}}.
\]

Therefore

\[
\boxed{
\frac{\varepsilon_2}{\varepsilon_{\rm prim}}
=\frac{(2a)^{N-1}}a
=2^{N-1}a^{N-2}>1.
}
\tag{6.1}
\]

Thus

\[
\boxed{
\lambda_2<\lambda-\varepsilon_{\rm prim}.
}
\tag{6.2}
\]

This completely removes the degree-`N` root-separation loss from the strictification mechanism. The finite operator and its original exact witness are unchanged; only the way the certificate is converted into a spectral bound is stronger.

## 7. Dependence-preserving finite-to-infinite transfer

The inherited C027 transfer is source-faithful, but the exact logic is recorded here because it is the bridge from the finite operator to the original problem.

The covering machine enumerates actual ordered pairs of finite binary strings. If at positive fugacities `(x,y)` its accepted-list weights at LCS order `m` satisfy

\[
f_m(x,y)\le K z^m
\]

for some finite `K` and `0<z<1`, coefficient positivity implies that the number of length-`n`, length-`n` source pairs with LCS at least `m` is at most

\[
Kx^{-n}y^{-n}z^m.
\]

Every ordered binary source pair has probability exactly `4^{-n}`, hence

\[
\Pr(L_n\ge m)
\le K(4xy)^{-n}z^m.
\tag{7.1}
\]

No independence between the `n^2` match indicators is introduced: the probability space is the original pair `(X_1^n,Y_1^n)`.

If

\[
\alpha>\frac{\log(4xy)}{\log z},
\]

then the right side of (7.1) decays exponentially for `m>=alpha n`. Since `0<=L_n<=n`, summing the tail and dividing by `n` gives

\[
\limsup_{n\to\infty}\frac{\mathbf E L_n}{n}
\le \alpha.
\]

Letting `alpha` decrease to the threshold yields

\[
\boxed{
\gamma_2\le\frac{\log(4xy)}{\log z}.
}
\tag{7.2}
\]

For a finite nonnegative matrix, any `z>rho(A)` is a valid exponential rate up to a finite prefactor. By (5.1), `z=lambda_2` is admissible.

At `x=y=t`, therefore,

\[
\boxed{
\gamma_2\le U_2:=
\frac{\log(4t^2)}{\log\lambda_2}.
}
\tag{7.3}
\]

Because `0<4t^2<1` and `z -> log(4t^2)/log z` is strictly increasing on `(0,1)`, (6.2) gives

\[
\boxed{U_2<U_{\rm prim}.}
\tag{7.4}
\]

This is a strict improvement for the original dependent binary-string problem.

## 8. Fixed metric before and after

The rigorous lower endpoint remains

\[
L=0.792665992.
\]

Before this run,

\[
W_{\rm before}=U_{\rm prim}-L,
\qquad
U_{\rm prim}=
\frac{\log(4t^2)}{\log(\lambda-\varepsilon_{\rm prim})}.
\]

After this run,

\[
\boxed{
W_{\rm after}=U_2-L
<W_{\rm before}.
}
\]

The unstrictified C045 endpoint is diagnostically

`0.826275942762282625015106581537296632823461996193190023880806...`.

The new two-step endpoint differs only around the 122nd decimal place; the high-precision diagnostic decrease relative to the unstrictified endpoint is about

`9.6675594816635453005e-122`.

The exact source movement is (7.4), not this decimal diagnostic. The source problem remains **OPEN / PARTIAL**; this run does not determine `gamma_2`.

## 9. Essential exact check

New artifacts:

- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T03-05-17Z__two_step_collatz_checker.py`
  - creation commit `b107fad5695917fd5266a1a64828f287ec4c31dd`
  - readback blob `5d578888eec0366d8ff353d0e2629ff4e027f5d7`
- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T03-05-17Z__two_step_collatz_checker.out`
  - creation commit `a007f81e0620f7ceedaf613152dbcd83d50b43ae`
  - readback blob `df429e49c37188b0790836f056b40370c9f5fefc`

The checker verifies exactly:

- `gcd(a,b)=1`;
- `b<=M<2b`;
- `a>M`;
- the identity `S*lambda/t^2=a/b`;
- the exact rational `epsilon_2` and `lambda_2`;
- the symbolic comparison `epsilon_2/epsilon_prim=2^(N-1)*a^(N-2)>1`.

Its archived output ends

`EXACT_TWO_STEP_CONSTANT_CHECKS_PASS`,
`SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS`,
`ALL_EXACT_CHECKS_PASS`.

The high-precision logarithms printed by the checker are diagnostics only; theorem strictness is exact and rational before the final monotonicity step.

## 10. Residual obstruction and next attack

This run eliminates the most artificial defect of the two preceding P02 strictifications: **degree-`N` algebraic root separation is no longer needed**. The remaining strict gap is controlled instead by the denominator `b` and the arithmetic of one tight-to-nontight successor.

However, the new source improvement is still only about `1e-121`. A visible endpoint gain requires additional information about actual slack or transition structure.

Highest-value next P02 attack:

1. strengthen Theorem P02-T02-C from the universal one-unit successor slack to an exact lower bound on the *total* integer slack leaving every tight row;
2. or prove that a tight row must encounter several non-tight rows within a short fixed number of steps, yielding a `k`-step Collatz gap with a numerator substantially larger than one;
3. or construct a local multiplicative perturbation `V' = V exp(phi)` on a small exact state statistic, so that the maximal row itself drops rather than relying on strictification after the fact.

These are graph-specific improvements to the existing cone and do not overlap P13's strip recursion or R17's hidden-prefix controller.

```yaml
ledger_delta:
  track: P02
  parent: T02
  source: "Chvatal--Sankoff binary LCS constant for two independent iid uniform binary strings"
  metric: "exact certified width U-L"
  lower_before: "99083249/125000000"
  lower_after: "99083249/125000000"
  upper_before: "log(4 t^2)/log(lambda-epsilon_prim)"
  upper_after: "log(4 t^2)/log(lambda-epsilon_2)"
  t: "256717/800000"
  epsilon_prim: "t^2/[2 S b (2a)^(N-1)]"
  epsilon_2: "t^2/(2 S a b)"
  strict_comparison: "epsilon_2/epsilon_prim = 2^(N-1) a^(N-2) > 1; hence U_after < U_before"
  width_before: "U_before - 0.792665992"
  width_after: "U_after - 0.792665992"
  movement: "STRICT SOURCE-LEVEL SHRINK"
  mechanism_advance: "two-step rational Collatz theorem: rho(B)^2 <= (a^2-1)/b^2 from tight-row arithmetic"
  model: "actual dependent match array induced by two iid binary strings; no Bernoulli matching substitution"
  status: PARTIAL
  source_status: OPEN
  public_interval: "0.792665992 <= gamma_2 <= 0.826280"
  prior_p02_target_handoff: "Aldous-Fill OP2.34 remains completed and is not reopened"
  companion_scopes:
    P13: "boundary-carry/stationary-strip recursion"
    R17: "hidden-prefix controller compression / correlated suffix obstruction"
  next_attack: "graph-specific total slack or short-step tight-to-nontight recurrence for a visible cone improvement"
```
