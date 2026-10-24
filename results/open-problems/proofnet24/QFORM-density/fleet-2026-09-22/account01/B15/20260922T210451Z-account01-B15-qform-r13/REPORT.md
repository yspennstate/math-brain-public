SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B15, 2026-09-22T21:04:51Z.
attacking: target-wide regularity closure and a zero-loss analytic-Schwartz normal form for the remaining universal-height problem.

# QFORM account01/B15 r13 — exact analytic-Schwartz normal form; qualitative regularity separated from universal height

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `account01/B15`  
**Run:** `20260922T210451Z-account01-B15-qform-r13`  
**Fresh control used before publication:** `yspennstate/math-research-brain@d237d41561430eafd611bbcc7a2999e2908a9eeb`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_REGULARITY_NORMAL_FORM / FULL UNIVERSAL HEIGHT OPEN`

## 1. Target and exact status

The sole target remains: for every `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove

`||p_(X^T A X)||_infinity <= C`

for one universal finite constant `C`, or give a valid counterexample.

This report does **not** prove that universal estimate. It separates the qualitative regularity issue from the quantitative one and proves a zero-loss normal form for the latter.

## 2. Completed assigned-partner result actually consumed

I consumed the completed account02/B15 report

- repository/commit visible in the current source chain: `yspennstate/math-open-problems`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`;
- that report's fresh control pin is `math-research-brain@200ae47caf9830c8810adcf4c513470ba03c8d6d`, revision `2026-09-22.15`.

Its target-level theorem is:

> For every fixed real symmetric `A` with `rank(A)>=3`, and every independent product law with one-dimensional densities bounded by one, `Q=X^TAX` has an instance-dependent bounded density with a representative in `C_0(R)`.

The account02 proof closes the physical zero-diagonal branch by an original-coordinate triangle/bilinear-block argument and uses the completed account03/B15 nonzero-diagonal theorem for the complementary branch. It explicitly avoids the corrected arbitrary-joint coarea, conditional positive-moment, rotated-independence and pointwise oscillatory-decay interfaces.

I apply this partner theorem below to the **actual sharp interval-density inequality**, not merely as a qualitative citation.

## 3. Absolute continuity is much cheaper than bounded density

The following elementary lemma is useful for keeping the logical levels separate.

### Lemma 3.1 — every nonconstant quadratic polynomial preserves null sets under an absolutely continuous input

Let

`q(x)=x^T A x+2b^T x+c`

be nonconstant on `R^n`, and let `X` have any absolutely continuous joint law. Then `q(X)` is absolutely continuous.

### Proof

For a Lebesgue-null set `N subset R`, set

`E_k={x: |x|<=k, |grad q(x)|>=1/k}`.

The coarea formula gives

`int_(E_k cap q^{-1}(N)) |grad q(x)| dx = int_N H^{n-1}(E_k cap q^{-1}(t)) dt =0`.

Hence `Leb(E_k cap q^{-1}(N))=0` for every `k`. The critical set is

`{x: Ax+b=0}`.

Because `q` is nonconstant, this set is either empty or a proper affine subspace, hence Lebesgue-null. The union of the `E_k` covers the complement of the critical set up to a null set. Therefore `Leb(q^{-1}(N))=0`, and an absolutely continuous input assigns it probability zero. QED.

Thus absolute continuity needs neither product structure nor three large eigenvalues. The difficult content of QFORM is the quantitative density height.

## 4. Partner theorem applied to the exact density constant

For a probability law `mu` on `R`, define its interval-density seminorm

`D(mu)=sup_{open intervals I} mu(I)/|I|`,

with the value `+infinity` allowed.

For every target instance, the account02/B15 theorem gives a bounded `C_0` density `p`. Therefore

`D(mu_Q)=||p||_infinity=max_t p(t)`.      (4.1)

Indeed `mu(I)<=||p||_infinity |I|`, while continuity gives for every `t`

`p(t)=lim_(h->0+) mu((t-h,t+h))/(2h) <= D(mu)`.

Since `p in C_0`, its supremum is attained. This is the promised actual inequality application of the assigned-partner result: the owner target can henceforth be formulated equivalently as a **pointwise attained maximum bound**, with no ambiguity between essential supremum, interval norm and pointwise representative.

In particular the qualitative continuous-representative issue is no longer the same missing step as the universal constant. The partner theorem gives continuity instance by instance; the unresolved issue is making the heights uniform in `A`, `n` and the laws.

## 5. A cap-preserving analytic-Schwartz approximation

Let `f` be any one-dimensional probability density with `0<=f<=1`.

### Lemma 5.1

There exists a sequence `g_m` such that

1. `g_m` is a strictly positive real-analytic Schwartz probability density;
2. `0<g_m<=1` everywhere;
3. `||g_m-f||_1 ->0`.

### Proof

First choose `R_m->infinity` so the truncated mass

`a_m=int_{-R_m}^{R_m} f ->1`.

Let `eta_eps` be a compactly supported smooth probability mollifier and choose `eps_m->0` so

`h_m=(f 1_{[-R_m,R_m]})*eta_{eps_m}`

satisfies

`||h_m-f 1_{[-R_m,R_m]}||_1 ->0`.

Then `0<=h_m<=1`, `h_m in C_c^infinity`, and `int h_m=a_m`.

Choose a fixed compactly supported smooth probability density `psi` with `0<=psi<=1`, translate it so its support is disjoint from `supp(h_m)`, and set

`k_m=h_m+(1-a_m) psi_m`.

Then `k_m` is a compactly supported smooth probability density, `0<=k_m<=1`, and

`||k_m-f||_1 <= ||h_m-f1_{[-R_m,R_m]}||_1 +2(1-a_m) ->0`.

Finally let `gamma_sigma` be a centered Gaussian probability density and choose `sigma_m->0` so

`g_m=k_m*gamma_{sigma_m}`

also satisfies `||g_m-k_m||_1->0`. Convolution with a probability kernel preserves the cap:

`||g_m||_infinity <= ||k_m||_infinity<=1`.

Because `k_m` is nonzero compactly supported and the Gaussian is strictly positive, `g_m>0` everywhere. Gaussian convolution of a compactly supported smooth function is real analytic and Schwartz. QED.

This approximation preserves the original-coordinate product structure when applied separately to each marginal.

## 6. Exact zero-loss analytic-Schwartz normal form for the full constant

Write `s_3(A)` for the third largest eigenvalue modulus. Let

`C_full = sup D(Law(X^T A X))`

over all target instances with `s_3(A)>=1` and arbitrary independent cap-one marginals.

Let `C_AS` be the same supremum restricted to instances satisfying simultaneously

- `s_3(A)=1`;
- every marginal is a strictly positive real-analytic Schwartz probability density bounded by one.

### Theorem 6.1

`boxed( C_full = C_AS )`.      (6.1)

Moreover, by (4.1), on both sides `D` can be replaced by the attained pointwise maximum `max_t p_Q(t)`.

### Proof

The inequality `C_AS<=C_full` is immediate because the analytic-Schwartz class is a subclass of the target class.

For the reverse inequality, fix an arbitrary target instance `(A,f_1,...,f_n)` and put

`alpha=s_3(A)>=1`, `B=A/alpha`.

Then `s_3(B)=1`, and if `Q_A=X^TAX`, `Q_B=X^TBX`,

`Q_A=alpha Q_B`.

Therefore

`D(Law(Q_A))=alpha^{-1} D(Law(Q_B)) <= D(Law(Q_B))`.      (6.2)

For each `i`, apply Lemma 5.1 to obtain analytic-Schwartz cap-one probabilities `g_i^(m)` with

`||g_i^(m)-f_i||_1 ->0`.

Let `nu_m` and `nu` be the corresponding product input laws. By telescoping,

`||nu_m-nu||_TV <= (1/2) sum_i ||g_i^(m)-f_i||_1 ->0`.

Pushforward by the measurable map `x -> x^T B x` contracts total variation, so for the output laws `mu_m,mu`,

`||mu_m-mu||_TV ->0`.      (6.3)

Every `mu_m` lies in the analytic-Schwartz normalized subclass, hence for every open interval `I`,

`mu_m(I)<= C_AS |I|`.

Passing to the limit using (6.3) gives

`mu(I)<=C_AS |I|`.

Taking the supremum over intervals yields

`D(mu)<=C_AS`.

Combining with (6.2),

`D(Law(Q_A))<=C_AS`.

Since the original target instance was arbitrary, `C_full<=C_AS`. QED.

## 7. Exact bad-sequence formulation

The universal conjecture fails if and only if there exists a sequence of target instances with

- `s_3(A_m)=1`;
- independent strictly positive real-analytic Schwartz marginals bounded by one;
- continuous densities `p_m in C_0(R)`;
- actual maximizers `t_m`;
- `p_m(t_m)->infinity`.

The forward implication follows from Theorem 6.1 and (4.1); the reverse implication is immediate. Thus any genuine obstruction to the universal bound can be searched for inside a completely classical smooth source class with an attained peak. Rough supports, discontinuous marginals and representative ambiguities are not essential obstructions.

This does **not** mean smoothness seminorms are uniformly controlled; they may diverge along the bad sequence. Therefore derivative-based Fourier estimates whose constants depend on those seminorms still do not prove QFORM.

## 8. Consequence for the regularity ledger

The logical hierarchy is now:

1. **Absolute continuity:** proved for every nonconstant quadratic polynomial under any absolutely continuous joint input (Lemma 3.1).
2. **Fixed-instance boundedness and continuity:** completed account02/B15 theorem gives `p_Q in C_0 cap L^infinity` for every fixed rank-`>=3` matrix and arbitrary cap-one product marginals; constants may depend badly on physical minors of `A`.
3. **Universal height:** still OPEN. By Theorem 6.1 it is exactly enough to prove it on normalized analytic-Schwartz product inputs.
4. **Uniform continuity modulus:** not claimed and not needed for the central theorem.

No pointwise law-uniform quadratic Fourier decay, no rotated-coordinate independence, no arbitrary-joint rank-three coarea theorem, and no projection-only shortcut is used.

## 9. First unpaid implication

The remaining problem is purely quantitative:

`sup_{s_3(A)=1, g_i analytic-Schwartz cap-one} max_t p_(X^T A X)(t) < infinity`.      (9.1)

The current source state indicates that fixed local-block estimates can diverge on diffuse matrices even when the true output remains uniformly controlled. Therefore the next proof must aggregate original-coordinate product structure before paying reciprocal small physical minors; the analytic-Schwartz reduction allows all manipulations to be performed on classical densities but supplies no uniform derivative constants.

Suggested next recipient: `account01/B19` (universal proof assembly), with `account02/B15` as regularity-source owner.

## 10. Integrity ledger

- Full QFORM universal constant: **OPEN / NOT PROVED**.
- New exact theorem: `C_full=C_AS`, no constant loss.
- New exact bad-sequence normal form: normalized `s_3=1`, analytic-Schwartz cap-one product laws, continuous outputs with attained diverging maxima.
- Partner theorem applied to the exact equality `D(mu)=||p||_infinity=max p`, not merely cited.
- No claim of native brain ingestion; repository retrieval/synchronization only.
