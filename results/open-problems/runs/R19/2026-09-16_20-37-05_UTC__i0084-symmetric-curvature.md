Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed interface has no model selector or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT in the fixed metric: 2/2 -> 2/2; unchanged count 4 -> 5. Section-B moves: 4, 5, 16.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2 (2018), Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY at alpha=1/2; frozen-arXiv repository closure remains PARTIAL / AUDIT_PENDING.** The fixed alpha=1/2 metric was already saturated at 2/2. This run does not manufacture metric movement. It follows the recovery choice made in the preceding stuck report and proves the previously isolated simplest extra case, then extends that calculation along the whole symmetric free-stable line `0<alpha<1`.

# 1. Continuity, repository state, and exact source version

I continued from current `master` rather than from chat memory. Before the new calculation I read or queried:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the I0084 row in `probability_1000_intake_I_20260914/problems.jsonl`;
- the newest complete own report, `runs/R19/2026-09-16_19-39-47_UTC__i0084-stuck1-sourcegate.md`;
- the newest relevant R18 and R20 reports;
- the newest P26 audit-recovery report.

The preceding R19 report was a required thinking-only stuck run. It isolated the optional free-interior obstruction to the local curvature of the unique mode and chose exactly one recovery target:

\[
\boxed{f''_{4/5,1/2}(0)<0.}
\]

No theorem was claimed there. This run attacks exactly that target.

The source-version distinction remains essential. The current arXiv v2 HTML states Conjecture 5.5 as follows: `S_t` may be the law of a **classical or free** alpha-stable process, the initial law satisfies

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\]

and the conclusion is ordinary classical convolution

\[
\boxed{\mu*S_t\text{ is unimodal for all sufficiently large }t.}
\]

This is the frozen target in the owner prompt. The later published ALEA version changed the wording to classical `mu*S_t` respectively free `mu \boxplus T_t`. I do **not** replace the frozen arXiv asterisk by free convolution.

Primary pages checked on 2026-09-16:

- arXiv source/version page and HTML: `https://arxiv.org/html/1710.08240v2`, especially Conjecture 5.5;
- Hasebe--Kuznetsov, `https://arxiv.org/html/1404.2981v2`, especially Theorem 2 and its boundary parametrization;
- Hasebe--Simon--Wang, `https://arxiv.org/html/1805.01133v2`, especially the discussion of strict unimodality and Theorem 4;
- ALEA version of record: `https://alea.impa.br/articles/v15/15-15.pdf`.

# 2. Audit update that arrived after the preceding run

A new P26 audit now exists:

`P26-AUDIT-R19-I0084-C002-ENDTOEND-06 = PASS_FULL_MATHEMATICAL_PROOF / PUBLISHED_ALEA_SCOPE`,

in

`proofnet24/P26-proof-audit-recovery/runs/2026-09-16/2026-09-16_23-00-17__run-report.md`.

This is useful but it does **not** discharge the frozen task's audit gate. P26 explicitly scope-gates its PASS to the **published ALEA free-boxplus branch** and explicitly says it is not settling the later R19 target that freezes the arXiv ordinary-convolution formulation.

Existing distinct audits preserved:

- `R18-I0084-C001=PASS` for the classical positive-half-stable finite/symbolic core;
- `R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF` for the different ALEA free-boxplus branch;
- `R18-AUDIT-R19-I0084-C010-ABSTRACT-004=PASS_FULL_MATHEMATICAL_PROOF` for the abstract sparse-bump theorem C010 only;
- the new P26 ALEA-scope PASS above.

There is still no P26 end-to-end PASS and no distinct OTHER-track end-to-end PASS for the **frozen arXiv ordinary-`*` package** C008/C009 and the endpoint refutation as one source-level package. Therefore closure is not claimed.

# 3. The three new-method moves

**Move 4 — PROVE SOMETHING WEAKER, COMPLETELY.** The preceding stuck report isolated `alpha=4/5, rho=1/2` as the smallest free-interior point beyond the previously imported bell-shape range. I attacked the single scalar statement `f''(0)<0` first, without trying another all-parameter shape theorem.

**Move 5 — ADD A PARAMETER AND DIFFERENTIATE.** The exact Hasebe--Kuznetsov small-`x` series makes the `alpha` dependence transparent. Keeping `alpha` symbolic turns the one-point calculation into an exact formula for every symmetric free stable law with `0<alpha<1`.

**Move 16 — COMPUTE SMALL CASES AND STARE AT THE SEQUENCE.** Exact rational checks at `alpha=1/2,2/3,3/4,4/5,9/10` exposed the simple closed form and were used only after the analytic derivation was found. The same check also verifies the rational identity needed for a second, stronger result: strict monotonicity of the symmetric density on each side of zero.

# 4. R19-I0084-C014 — exact symmetric free-stable mode curvature

**STATUS: PROVED internally. Dependency: Hasebe--Kuznetsov Theorem 2, equation (17). Independent audit pending.**

Let

\[
0<\alpha<1,
\qquad
\rho=\frac12,
\]

and let `psi_{alpha,1/2}` denote the density of the Hasebe--Kuznetsov normalized free strictly stable law. Then

\[
\boxed{
\psi_{\alpha,1/2}''(0)
=
-\frac{3-\alpha}{\pi\alpha^2}<0.
}
\tag{C014.1}
\]

In particular,

\[
\boxed{
\psi_{4/5,1/2}''(0)=-\frac{55}{16\pi}<0.
}
\tag{C014.2}
\]

## Proof

For `0<alpha<1`, Hasebe--Kuznetsov Theorem 2, equation (17), gives for `0<=x<=x_*`

\[
\psi_{\alpha,\rho}(x)
=
\frac1\pi
\sum_{n\ge1}
(-1)^{n-1}
\frac{\Gamma(1+n/\alpha)}
{n!\,\Gamma(2+(1/\alpha-1)n)}
\sin(n\rho\pi)x^{n-1}.
\tag{C014.3}
\]

Set `rho=1/2`. The `n=1` term is exactly `1/pi`, since

\[
\frac{\Gamma(1+1/\alpha)}
{\Gamma(2+(1/\alpha-1))}=1.
\]

Every even `n` vanishes because `sin(n pi/2)=0`. The next nonzero term is `n=3`, and `sin(3pi/2)=-1`, so its `x^2` coefficient is

\[
-\frac1{6\pi}
\frac{\Gamma(1+3/\alpha)}
{\Gamma(3/\alpha-1)}.
\tag{C014.4}
\]

The gamma ratio is elementary:

\[
\frac{\Gamma(1+3/\alpha)}
{\Gamma(3/\alpha-1)}
=
\left(\frac3\alpha-1\right)\frac3\alpha
=
\frac{3(3-\alpha)}{\alpha^2}.
\tag{C014.5}
\]

Hence

\[
\psi_{\alpha,1/2}(x)
=
\frac1\pi
-
\frac{3-\alpha}{2\pi\alpha^2}x^2
+O(x^4),
\tag{C014.6}
\]

and differentiating twice gives C014.1. At `alpha=4/5`,

\[
-\frac{3-4/5}{(4/5)^2}
=-\frac{55}{16},
\]

which proves C014.2. QED.

The previously retained half-stable value is recovered at `alpha=1/2`:

\[
\psi_{1/2,1/2}''(0)=-\frac{10}{\pi}.
\]

The limit `alpha -> 1-` gives `-2/pi`, consistent with the symmetric Cauchy normalization.

# 5. Adversarial check of the route: curvature alone is not enough

Before promoting C014 into an eventual-unimodality theorem I rechecked the hypotheses of retained C008. A subtlety matters.

C008 requires a genuinely signed derivative away from the mode, not merely a unique mode and local negative curvature. A real-analytic unimodal density can in principle have an isolated stationary inflection on the decreasing side. At such a point an arbitrarily small far-tail perturbation can be dangerous. Therefore the statement

> `f''(0)<0` + strict unimodality

is **not by itself** sufficient for C008.

This is an exact correction to the simplified blocker description in the preceding stuck report. The missing global sign can, however, be proved directly in the symmetric free-stable case from the Hasebe--Kuznetsov boundary parametrization.

# 6. R19-I0084-C015 — strict monotonicity of every symmetric free stable density for 0<alpha<1

**STATUS: PROVED internally from the published Hasebe--Kuznetsov boundary parametrization. Independent audit pending.**

For every `0<alpha<1`, the normalized symmetric free stable density satisfies

\[
\boxed{
\psi'_{\alpha,1/2}(x)<0\quad(x>0),
\qquad
\psi'_{\alpha,1/2}(x)>0\quad(x<0).
}
\tag{C015.1}
\]

Thus there are no off-mode stationary points at all.

## Proof

Hasebe--Kuznetsov parameterize the boundary value of the Cauchy transform on the positive real axis as

\[
w=G_{\alpha,1/2}(x)=r(\theta)e^{-i\theta},
\qquad
0<\theta<\frac\pi2,
\tag{C015.2}
\]

with

\[
q=q(\theta)
=\frac{\alpha\pi}{2}+(1-\alpha)\theta,
\qquad
r(\theta)
=
\left(\frac{\sin\theta}{\sin q}\right)^{1/\alpha}.
\tag{C015.3}
\]

Their inversion identity is

\[
x=w^{-1}-e^{i\pi\alpha/2}w^{\alpha-1}.
\tag{C015.4}
\]

The imaginary part of C015.4 vanishes precisely because of C015.3. Its real part simplifies to

\[
x(\theta)
=
\frac{1}{r(\theta)}
\frac{\sin(q-\theta)}{\sin q}.
\tag{C015.5}
\]

Put

\[
\beta=1-\alpha,
\qquad
A=q-\theta
=\alpha\left(\frac\pi2-\theta\right).
\tag{C015.6}
\]

Then `A>0`, `q=theta+A`, and `theta<q<pi/2`.

Stieltjes inversion gives

\[
\psi_{\alpha,1/2}(x(\theta))
=
\frac{r(\theta)\sin\theta}{\pi}.
\tag{C015.7}
\]

Differentiate its logarithm:

\[
\frac{d}{d\theta}
\log\psi_{\alpha,1/2}(x(\theta))
=
\left(1+\frac1\alpha\right)\cot\theta
-
\frac{\beta}{\alpha}\cot q.
\tag{C015.8}
\]

Because `0<theta<q<pi/2`, `cot(theta)>cot(q)>0`; hence, after multiplying by `alpha`,

\[
(1+\alpha)\cot\theta-\beta\cot q
>
[(1+\alpha)-\beta]\cot q
=2\alpha\cot q>0.
\tag{C015.9}
\]

So the density value in C015.7 is strictly increasing as a function of `theta`.

It remains to verify that `x(theta)` is strictly decreasing. From C015.5,

\[
\log x
=
\log\sin A
+
\left(\frac1\alpha-1\right)\log\sin q
-
\frac1\alpha\log\sin\theta,
\]

and therefore

\[
\frac{x'}x
=
-\alpha\cot A
+
\frac{\beta^2}{\alpha}\cot q
-
\frac1\alpha\cot\theta.
\tag{C015.10}
\]

Set

\[
u=\cot\theta>0,
\qquad
v=\cot A>0.
\]

Since `q=theta+A`,

\[
\cot q=\frac{uv-1}{u+v}.
\tag{C015.11}
\]

Multiplying C015.10 by `alpha(u+v)` gives the exact identity

\[
\begin{aligned}
\alpha\frac{x'}x(u+v)
&=
\left[-\alpha^2v+\beta^2\frac{uv-1}{u+v}-u\right](u+v)\\
&=
-\left[(u+\alpha v)^2+\beta^2\right]
<0.
\end{aligned}
\tag{C015.12}
\]

Hence `x'(theta)<0`. Combining this with C015.9 gives

\[
\frac{d}{dx}\psi_{\alpha,1/2}(x)
=
\frac{d\psi/d\theta}{dx/d\theta}<0
\qquad(x>0).
\]

The Hasebe--Kuznetsov reflection identity

\[
\psi_{\alpha,\rho}(x)=\psi_{\alpha,1-\rho}(-x)
\]

makes `rho=1/2` symmetric, so the derivative is strictly positive for `x<0`. QED.

This calculation is stronger than the single curvature target and avoids importing bell-shape beyond the range where Hasebe--Simon--Wang proved it.

# 7. R19-I0084-C016 — symmetric free-stable ordinary-convolution case for every 0<alpha<1

**STATUS: PROVED internally, conditional only on retained internally proved C008 plus published free-stable formulas. Independent source-level audit pending.**

Let `0<alpha<1`, and let `T_t^{(alpha,1/2)}` denote the symmetric free strictly stable law at time `t`, used as an **ordinary classical convolution kernel**, exactly as in the frozen arXiv Conjecture 5.5.

Then for every probability measure `mu` satisfying the exact source moment condition

\[
M_{2+\alpha}
:=
\int_{\mathbb R}|y|^{2+\alpha}\,d\mu(y)<\infty,
\tag{C016.1}
\]

there exists a finite threshold `t_0=t_0(alpha,mu)` such that

\[
\boxed{
\mu*T_t^{(\alpha,1/2)}
\text{ is unimodal for every }t\ge t_0.
}
\tag{C016.2}
\]

More quantitatively, for the fixed Hasebe--Kuznetsov normalization there is a kernel constant `C_alpha<infty` such that

\[
\boxed{
t\ge C_\alpha
M_{2+\alpha}^{\alpha/(2+\alpha)}
}
\tag{C016.3}
\]

is sufficient.

In the special case selected by the preceding stuck report,

\[
\alpha=\frac45,
\qquad
2+\alpha=\frac{14}{5},
\qquad
\frac{\alpha}{2+\alpha}=\frac27,
\]

so

\[
\boxed{
t\ge C_{4/5}M_{14/5}^{2/7}}
\tag{C016.4}
\]

is sufficient.

## Proof

Apply retained C008 to the unit-scale density

\[
k(x)=\psi_{\alpha,1/2}(x).
\]

I verify every C008 hypothesis rather than invoking the name of the theorem blindly.

**(i) Smoothness and bounded first two derivatives.** Hasebe--Kuznetsov show that the free stable law has a smooth density. For the interior parameter `rho=1/2` it is analytic on the real line. On compact sets its first two derivatives are bounded; the convergent tail series below shows both derivatives tend to zero polynomially at infinity. Thus `||k'||_infty,||k''||_infty<infty`.

**(ii) Strict derivative signs.** This is exactly C015:

\[
k'(x)>0\ (x<0),
\qquad
k'(x)<0\ (x>0).
\]

**(iii) Uniform negative curvature near the mode.** C014 gives

\[
k''(0)= -\frac{3-\alpha}{\pi\alpha^2}<0.
\]

By continuity there are `epsilon,c_0>0` such that

\[
k''(x)\le-c_0
\qquad(|x|\le2\epsilon).
\]

**(iv) Critical derivative tails.** Hasebe--Kuznetsov Theorem 2, equation (16), gives for large positive `x`

\[
k(x)
=
\frac{\sin(\pi\alpha/2)}{\pi}x^{-1-\alpha}
+O(x^{-1-2\alpha}).
\tag{C016.5}
\]

The series is convergent in the tail region, so termwise differentiation there gives

\[
k'(x)
=
-\frac{(1+\alpha)\sin(\pi\alpha/2)}{\pi}
 x^{-2-\alpha}
+O(x^{-2-2\alpha}).
\tag{C016.6}
\]

The leading constant is strictly positive for every `0<alpha<1`. Hence for sufficiently large `R`

\[
-k'(x)\ge c_+x^{-(2+\alpha)}
\qquad(x\ge R)
\]

for some `c_+>0`. Symmetry gives

\[
k'(x)\ge c_-|x|^{-(2+\alpha)}
\qquad(x\le-R).
\]

Thus C008 applies with

\[
p=2+\alpha.
\]

If `k_s(x)=s^{-1}k(x/s)`, C008 yields unimodality of `mu*k_s` once

\[
s^{2+\alpha}\ge C'_\alpha M_{2+\alpha}.
\tag{C016.7}
\]

Strict stability gives the time-`t` free stable law as the spatial dilation with scale

\[
s=t^{1/\alpha}
\]

under the standard normalization (an alternative fixed scale convention only changes the constant). Substitution into C016.7 yields

\[
t\ge C_\alpha M_{2+\alpha}^{\alpha/(2+\alpha)},
\]

which proves C016.2--3. QED.

## Exact scope

C016 is **not** an all-skewness theorem beyond the previously proved range. It settles the symmetric line `rho=1/2` for every `0<alpha<1`. For nonsymmetric interior `rho != 1/2` with `alpha>3/4`, the needed global derivative/curvature control has not been proved here. The endpoint counterexamples from earlier R19 runs still refute the universal source statement.

# 8. Exact self-check and a source-label correction

Only after deriving C014--C016 analytically did I run an exact SymPy check. The authoritative run-specific checker is

`artifacts/R19/2026-09-16_20-37-05_UTC__i0084_symmetric_curvature_checker_v3.py`

created at commit

`4f7cbe893ccbf81f3e9c78d9001bc0367b8e4d2e`

and read back at that exact commit. Its archived output is

`artifacts/R19/2026-09-16_20-37-05_UTC__i0084_symmetric_curvature_checker_v3_output.txt`

created at commit

`c78fb96795f17d5c3d37f1d653eee3d76d2814ec`

and read back at that exact commit. Output SHA-256:

`a66e5e70f329ef81d80874878638bbbb2df55a8350ac886c99e3e8e09fee70bc`.

It checks:

1. the exact gamma ratio in C014;
2. the closed formula `pi*f''(0)=-(3-alpha)/alpha^2`;
3. the exact monotonicity identity C015.12;
4. rational special cases `alpha=1/2,2/3,3/4,4/5,9/10`;
5. `p=14/5` and threshold exponent `2/7` at `alpha=4/5`;
6. the Cauchy-limit consistency `alpha->1-`.

The output ends `PASS`.

An earlier checker file from this same run had a **comment-only source-label error**: it called the Hasebe--Kuznetsov small-`x` series “formula (16)”, while the current v2 HTML labels the small-`x` series (17) and the tail series (16). The algebra in that file used the correct small-`x` formula, but I did not overwrite the immutable artifact. I created corrected v2 and then the stronger v3 above. **v3 is the authoritative evidence.** This correction changes no mathematical calculation.

# 9. Prior-art/status search on 2026-09-16

I performed a fresh bounded search before treating C014--C016 as potentially new fleet contributions. Queries included:

- exact Hasebe--Ueda title + `Conjecture 5.5`;
- `stable unimodality finite 2+alpha moment`;
- `free stable symmetric density second derivative mode`;
- `free stable density strictly decreasing`;
- `free stable ordinary convolution eventual unimodality`;
- Hasebe--Kuznetsov and Hasebe--Simon--Wang later/source papers;
- Bercovici--Pata/Biane free-stable density and unimodality references.

Accessible primary literature confirms:

- arXiv v2 Conjecture 5.5 has the frozen ordinary-`*` formulation;
- the ALEA version has the later classical/free `*`/`boxplus` split;
- Hasebe--Kuznetsov provide the exact density series and boundary parametrization used here;
- Hasebe--Simon--Wang record analyticity and strict unimodality for free stable densities and prove bell shape for `0<alpha<=3/4, 0<rho<1`.

I did not find an accessible later source stating C016, nor a later resolution of the frozen arXiv ordinary-convolution Conjecture 5.5. This is a bounded negative search, **not proof of absolute novelty**. C014 and C015 are direct consequences of published formulas and may be folklore/implicit; they are presented as explicit derivations, not priority claims.

# 10. R20 directed-audit duty

No R20 package newer than

`runs/R20/2026-09-16T17-46-41Z_i0100_p241_newmethods_c91f2e.md`

was found. R19 already independently audited that `p=241` exact certificate in an earlier run. I did not manufacture a duplicate audit.

# 11. Runtime/model and scheduler limitation

The limitation is still real. The exposed automation interface available to this worker has controls for prompt/title/schedule/timing/enabled state, but no model selector and no reasoning-effort selector. Therefore `GPT-6 / maximum` remains a prompt request rather than a verified runtime setting. Changing this requires an authorized product/platform context that actually exposes model/reasoning configuration; it cannot be accomplished by rewriting mathematical prompts.

The implementation manifest records that one attempt to modify P26 scheduler ID

`6aa7b43682948191b697d72fec69d539`

returned exactly `You cannot modify this task.` That boundary was not bypassed. Later work records that an authorized P/C context could update the same task, so the legitimate workaround is **owner/admin/platform authorization in a context with permission**, not a duplicate schedule or permission evasion.

No scheduler was changed in this run.

# 12. Ledger delta

```yaml
ledger_delta:
  track: R19
  source: "Hasebe-Ueda arXiv:1710.08240v2, Conjecture 5.5 / intake I0084"
  source_version_scope: "frozen arXiv v2; ordinary classical convolution * for both classical/free stable kernels"
  metric: "number of complete classical-stable/free-stable alpha=1/2 source cases proved for all admissible initial measures and full source skewness scope"
  before: "2/2"
  after: "2/2"
  movement: "NO MOVEMENT"
  unchanged_count_before: 4
  unchanged_count_after: 5
  status: "PARTIAL / AUDIT_PENDING; universal source statement mathematically refuted internally"
  tried_moves: [4, 5, 16]
  new_claims:
    - "R19-I0084-C014: exact symmetric free-stable mode curvature for all 0<alpha<1"
    - "R19-I0084-C015: strict monotonicity on each side of zero for symmetric free stable densities, 0<alpha<1"
    - "R19-I0084-C016: exact-(2+alpha)-moment eventual ordinary-convolution unimodality on the symmetric free-stable line, 0<alpha<1"
  exact_evidence:
    - "artifacts/R19/2026-09-16_20-37-05_UTC__i0084_symmetric_curvature_checker_v3.py @ 4f7cbe893ccbf81f3e9c78d9001bc0367b8e4d2e"
    - "artifacts/R19/2026-09-16_20-37-05_UTC__i0084_symmetric_curvature_checker_v3_output.txt @ c78fb96795f17d5c3d37f1d653eee3d76d2814ec"
    - "checker output sha256 a66e5e70f329ef81d80874878638bbbb2df55a8350ac886c99e3e8e09fee70bc"
  audit_ids:
    - "R18-I0084-C001=PASS"
    - "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF [ALEA free-boxplus scope]"
    - "R18-AUDIT-R19-I0084-C010-ABSTRACT-004=PASS_FULL_MATHEMATICAL_PROOF [C010 only]"
    - "P26-AUDIT-R19-I0084-C002-ENDTOEND-06=PASS_FULL_MATHEMATICAL_PROOF/PUBLISHED_ALEA_SCOPE"
  audit_scope_warning: "No P26 and no distinct other-track end-to-end PASS yet for the frozen arXiv ordinary-* source package."
  remaining_obligation: "Obtain the two frozen-arXiv ordinary-* end-to-end audits. If they arrive, package the exact source refutation. If the fixed metric is unchanged next run, unchanged_count reaches six and the closable-track rotation/handoff rule is triggered unless closure completes."
```

# 13. Remaining obligations / next run

The fixed metric cannot exceed 2/2. Therefore extra lemmas are not a substitute for closure or rotation.

At the next invocation:

1. first search for a P26 **frozen-arXiv ordinary-`*`** end-to-end audit and a distinct other-track audit;
2. if both required audits now exist, assemble the required self-contained paper package with exact source/version scope and do not misdescribe the ALEA statement;
3. if the metric remains unchanged and the frozen-source audit gate is still unmet, the unchanged count becomes six. Under the closable-track rule, leave a preserved handoff and rotate rather than continue producing optional stable-density lemmas.

The strongest optional unresolved analytic extension, if the target is ever reassigned, is the nonsymmetric free-stable interior for `alpha>3/4`: C014--C016 solve the entire symmetric line but do not establish the needed global derivative control for general `rho`.

**NO CLOSURE CLAIM.**
