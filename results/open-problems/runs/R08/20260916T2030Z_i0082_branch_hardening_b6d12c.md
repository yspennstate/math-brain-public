Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this scheduler exposes no model selector or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT in the frozen explicit-candidate metric: 2/3 -> 2/3; unchanged count 3. Section-B moves actually tried: 4 (PROVE SOMETHING WEAKER, COMPLETELY), 16 (COMPUTE SMALL EXACTLY SOLVABLE CASES), 26 (HUNT THE SPORADIC/DEGENERATE CASE).**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2 / ALEA 15 (2018), **Problem 3.11**.

# R08 CLOSABLE OUTSIDE — I0082 branch selection hardening for the local-Voiculescu no-FSU theorem

Run ID: `20260916T2030Z_i0082_branch_hardening_b6d12c`  
Date checked: 2026-09-16  
Repository: `yspennstate/math-open-problems`, branch `master`  
Canonical claim: `operations/claims/I0082.md`, owner R08, status `ADMITTED_ACTIVE`  
Portfolio status after this run: **PARTIAL / AUDIT_PENDING**  
Mathematical source-answer candidate after this run: **NO — only Dirac measures are freely strongly unimodal.**

The fixed metric stays exactly as assigned: for the frozen positive free strict `1/4`-stable candidate, obligations (1) non-Dirac probability law and (2) unimodality are proved, while obligation (3) universal preservation of unimodality is disproved by an explicit unimodal witness. Thus the metric is still `2/3`. I do not change candidates to manufacture movement.

The source-level theorem `R08-I0082-C005` from the preceding run is stronger progress than that frozen metric. This run does not invent another adjacent theorem merely to create a new claim count. Instead, Move 4 isolates and closes the most serious analytic branch-selection point in C005: why the local implicit equation involving the Voiculescu transform is the actual free-convolution branch near the three real density points, not merely a formal branch of an algebraic equation.

Because the fixed metric has now remained unchanged for three consecutive active I0082 runs, **the next run is subject to the owner's Section-I stuck protocol unless the portfolio closes first by receiving the two required external audits.**

## 1. Continuity, source, ownership, and current-status gate

I continued from current `master` and the newest own immutable report:

`runs/R08/20260916T1928Z_i0082_local_phi_no_fsu_7f3a91.md`.

Before new mathematics I read/recovered the required control surfaces:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0082.md`;
- targeted I0082 intake/attempt/ownership searches;
- the newest related R19 Hasebe-Ueda stable-process report;
- the newest R09 package for the required independent audit.

The large intake JSONL corpus cannot be rendered row-for-row through this connector before truncation. I therefore used targeted searches for I0082, its source, aliases, ownership, and previous attempts and record that access limitation instead of claiming a fictitious visual reread of all roughly 780 rows.

The canonical claim remains R08-owned and `ADMITTED_ACTIVE`; no competing current owner surfaced. `POSTED.md` excludes the distinct Hasebe-Ueda Problem 3.3 result, not Problem 3.11. The old R08 FPP route remains retired from this slot with its immutable handoff and was not reopened.

### Source scope rechecked

The ALEA paper states:

- Definition 3.8: `lambda` is freely strongly unimodal (FSU) iff `lambda boxplus nu` is unimodal for **every** unimodal probability measure `nu`;
- Theorem 3.10: every non-Dirac finite-variance law fails FSU;
- Problem 3.11: whether any non-Dirac FSU probability measure exists.

This run does not reprove Theorem 3.10.

### Dated bounded literature search, 2026-09-16

Fresh queries included:

1. exact `"freely strongly unimodal" Dirac`;
2. exact `"freely strongly unimodal" "delta measure"`;
3. exact Hasebe-Ueda `Problem 3.11` and later-author work;
4. `"freely strongly unimodal" 2026`;
5. later multiplicative Hasebe-Ueda work;
6. current symmetric free-additive unimodality material;
7. local Voiculescu-transform and additive-subordination references needed for the branch-selection hardening below.

No primary-source resolution of the additive Problem 3.11 surfaced. Ueda's later thesis repeats the finite-variance theorem and the same open problem. The later Hasebe-Ueda paper is multiplicative (`boxtimes`), a different question. A September 2026 unrefereed symmetric-free-addition candidate explicitly says it does not resolve free strong unimodality for arbitrary nonsymmetric unimodal inputs.

This is a bounded negative prior-art search, not a worldwide novelty certificate. The local-transform mechanism in C005/C006 is potentially folklore until specialist audits and broader literature review are complete.

## 2. Recovered C005 state and the branch-selection issue

The preceding report proved on the page the candidate classification

> **R08-I0082-C005.** A probability measure on `R` is freely strongly unimodal iff it is a Dirac measure.

The fixed elementary witness is

\[
\nu_r=r\delta_0+(1-r)\mathbf 1_{(0,1)}(x)\,dx,
\qquad r=\frac1{1000}.
\]

On the upper boundary of `(0,1)`,

\[
G_{\nu_r}(x+i0)
=
A_r(x)-i\beta_r,
\qquad
A_r(x)=\frac r x+(1-r)\log\frac{x}{1-x},
\qquad
\beta_r=\pi(1-r),
\]

with

\[
A_r'(x)=\frac{x-r}{x^2(1-x)}.
\]

At

\[
x_1=r,\qquad x_2=2r,\qquad x_3=\frac12
\]

the exact derivatives are

\[
A_r'(x_1)=0,\qquad
A_r'(x_2)=\frac{125000}{499},\qquad
A_r'(x_3)=\frac{499}{125}.
\]

For an arbitrary non-Dirac candidate `mu`, the preceding run dilates it by `c`, writes

\[
S_c=-\phi_{D_c\mu},
\]

normalizes at

\[
z_3=F_{\nu_r}(x_3)
\]

using

\[
a_c=\Re S_c(z_3),\qquad
\eta_c=\Im S_c(z_3)>0,
\qquad
H_c(z)=\frac{S_c(z)-a_c}{\eta_c},
\]

and sets

\[
\lambda_c=D_c\mu\boxplus\delta_{a_c}.
\]

Then locally

\[
\phi_{\lambda_c}(z)=-\eta_c H_c(z).
\]

The preceding Harnack calculation gives

\[
\Im H_c(z_2)>\frac3{100},
\qquad
H_c(z_3)=i,
\]

where \(z_j=F_{\nu_r}(x_j)\), and the exact margin is

\[
\frac3{100}\frac{125000}{499}
>
\frac{499}{125}.
\]

The one place worth hardening was the step that identifies

\[
W_c(z):=F_{\lambda_c\boxplus\nu_r}(z)
\]

with the local solution of

\[
W_c(z)
=
F_{\nu_r}\!\left(
z+\eta_c H_c(W_c(z))
\right).
\tag{2.1}
\]

Equation (2.1) is immediate on a sufficiently high common inverse cone from Voiculescu-transform linearization, but near the finite boundary points `x_j` one must justify that the actual free-convolution transform remains on the same analytic inverse branch. That is what Move 4 addresses.

# 3. Move 4 — prove the local branch lemma completely

## R08-I0082-C006 — local branch and first-order perturbation lemma

**STATUS: PROVED.**

Let `mu` be any non-Dirac probability law and let `nu=nu_r` with `r=1/1000`. Define `lambda_c`, `eta_c`, and `H_c` as above. Then for each

\[
x_j\in\left\{r,2r,\frac12\right\}
\]

there is a complex neighborhood `U_j` of `x_j` and `c_j>0` such that for all `0<c<c_j`:

1. the reciprocal Cauchy transform
   \[
   W_c=F_{\lambda_c\boxplus\nu}
   \]
   admits a holomorphic continuation from `C+` to `U_j` on the upper boundary sheet of `nu`;

2. on `U_j` it is the **actual** branch satisfying
   \[
   \boxed{
   W_c(z)
   =
   \widehat F_\nu\!\left(
   z+\eta_c H_c(W_c(z))
   \right),
   }
   \tag{C006.1}
   \]
   where `widehat F_nu` denotes the local holomorphic continuation of `F_nu`;

3. uniformly on compact subsets of `U_j`,
   \[
   \boxed{
   W_c(z)
   =
   \widehat F_\nu(z)
   +
   \eta_c\widehat F_\nu'(z)
   H_c(\widehat F_\nu(z))
   +
   O(\eta_c^2),
   }
   \tag{C006.2}
   \]
   and therefore
   \[
   \boxed{
   G_{\lambda_c\boxplus\nu}(z)
   =
   \widehat G_\nu(z)
   +
   \eta_c\widehat G_\nu'(z)
   H_c(\widehat F_\nu(z))
   +
   O(\eta_c^2).
   }
   \tag{C006.3}
   \]

The constants in the `O(eta_c^2)` term can be chosen uniformly for the three fixed neighborhoods.

### Proof

For every probability measure `sigma`, its reciprocal Cauchy transform
\(F_\sigma\) has a canonical inverse on a sufficiently high truncated
Stolz cone; the Voiculescu transform is

\[
\phi_\sigma(w)=F_\sigma^{-1}(w)-w.
\]

On a common high cone,

\[
\phi_{\lambda_c\boxplus\nu}
=
\phi_{\lambda_c}+\phi_\nu.
\]

If \(w=F_{\lambda_c\boxplus\nu}(z)\) there, then

\[
z
=
F_{\lambda_c\boxplus\nu}^{-1}(w)
=
w+\phi_{\lambda_c}(w)+\phi_\nu(w).
\]

Since

\[
F_\nu^{-1}(w)=w+\phi_\nu(w),
\]

we obtain

\[
F_\nu^{-1}(w)=z-\phi_{\lambda_c}(w)
=
z+\eta_cH_c(w),
\]

and hence C006.1 on a nonempty high-cone open set.

Now fix one of the three points \(x_j\). Because \(x_j\in(0,1)\), the
explicit formula for \(G_\nu\) has a holomorphic continuation through a
small complex neighborhood of \(x_j\) on its upper boundary sheet. Moreover

\[
G_\nu(x_j+i0)=A_r(x_j)-i\beta_r
\]

has strictly negative imaginary part, so

\[
z_j=F_\nu(x_j+i0)\in\mathbb C^+.
\]

Choose a path in `C+` from a point of the high common cone down to a small
upper-half-plane neighborhood of \(x_j\), and a thin connected tubular
neighborhood `V_j` of this path. Add a sufficiently small disk through
\(x_j\) on the chosen continuation sheet. The image
\(\widehat F_\nu(\overline{V_j})\) is contained in a compact subset of
\(\mathbb C^+\) after making the tube and disk small enough.

For the dilated law,

\[
\phi_{D_c\mu}(w)
=
c\,\phi_\mu(w/c).
\]

The canonical local domains of \(\phi_{D_c\mu}\) exhaust \(\mathbb C^+\)
on compact sets as \(c\downarrow0\), and
\(\phi_{D_c\mu}\to0\) locally uniformly there because
\(\phi_\mu(\zeta)=o(\zeta)\) nontangentially at infinity. Since
\(a_c\to0\), the same is true for

\[
\phi_{\lambda_c}=\phi_{D_c\mu}+a_c.
\]

By Cauchy estimates on a slightly larger compact neighborhood,

\[
\|\phi_{\lambda_c}\|_{C^1(K_j)}\to0
\tag{C006.4}
\]

for a fixed compact `K_j` containing
\(\widehat F_\nu(\overline{V_j})\).

Define

\[
\mathcal E_c(z,w)
=
w-\widehat F_\nu\!\left(z-\phi_{\lambda_c}(w)\right).
\]

At \(c=0\),

\[
\mathcal E_0(z,w)=w-\widehat F_\nu(z),
\qquad
\partial_w\mathcal E_0=1.
\]

By C006.4, after shrinking the tube once and taking `c` small,
\(\partial_w\mathcal E_c\) stays uniformly separated from zero in a
fixed neighborhood of the graph
\(w=\widehat F_\nu(z)\). Thus the analytic implicit-function theorem gives
a unique analytic solution

\[
\widetilde W_c(z)
\]

near \(\widehat F_\nu(z)\) all along the connected tube and through the
local boundary disk.

It remains to identify this solution with the actual free-convolution
transform. Since

\[
\lambda_c\Rightarrow\delta_0
\]

and free additive convolution is weakly continuous,

\[
\lambda_c\boxplus\nu\Rightarrow\nu.
\]

Therefore

\[
F_{\lambda_c\boxplus\nu}\to F_\nu
\]

locally uniformly on `C+`. In particular, on the upper-half-plane part of
the tube, the actual transform lies in the same uniqueness neighborhood of
\(\widehat F_\nu\) for all small `c`.

On the high-cone portion, the actual transform satisfies C006.1 by the
canonical inverse calculation above, so it equals
\(\widetilde W_c\) there. The set along the connected tube where the two
branches agree is nonempty and, by local uniqueness plus analytic
continuation, both open and closed. Hence the actual transform agrees with
\(\widetilde W_c\) throughout the upper-half-plane tube. The latter
continues holomorphically through \(x_j\), proving parts 1 and 2.

For the expansion, use

\[
-\phi_{\lambda_c}=\eta_cH_c.
\]

The maps \(H_c\) are normalized Pick maps on a fixed domain containing the
relevant compact transform neighborhoods and satisfy \(H_c(z_3)=i\).
Harnack/Schwarz-Pick normal-family bounds therefore give uniform local
bounds on \(H_c\) and its first derivative. Taylor expansion of C006.1
about \(\eta_c=0\) gives

\[
W_c(z)
=
\widehat F_\nu(z)
+
\eta_c\widehat F_\nu'(z)
H_c(\widehat F_\nu(z))
+
O(\eta_c^2),
\]

uniformly on the fixed compact neighborhoods. Since \(G=1/F\),

\[
\frac{1}{W_c}
=
\frac{1}{\widehat F_\nu}
-
\eta_c
\frac{\widehat F_\nu'}{\widehat F_\nu^2}
H_c(\widehat F_\nu)
+
O(\eta_c^2).
\]

But

\[
\widehat G_\nu'
=
-\frac{\widehat F_\nu'}{\widehat F_\nu^2},
\]

which proves C006.3. QED.

### Why this matters

C006 removes the main branch ambiguity in C005. The local equation is not
merely a formal root chosen after the fact: it is analytically connected to
the canonical high-cone free-convolution branch and is unique near the
unperturbed transform.

The proof uses only standard weak continuity of free additive convolution,
the canonical local Voiculescu inverse at infinity, and analytic
subordination/continuation; it does not assume free infinite divisibility,
moments, or a globally defined Voiculescu transform.

# 4. C005 after C006 — the strict valley is now on the actual convolution branch

On the interval `(0,1)`,

\[
\widehat G_\nu(x)=A_r(x)-i\beta_r
\]

and

\[
\widehat G_\nu'(x)=A_r'(x)\in\mathbb R.
\]

Taking upper boundary values in C006.3 gives the actual local density

\[
p_c(x)
=
1-r
-
\frac{\eta_c}{\pi}
A_r'(x)
\Im H_c(F_\nu(x+i0))
+
O(\eta_c^2).
\tag{4.1}
\]

At \(x_1=r\),

\[
A_r'(x_1)=0,
\]

so

\[
p_c(x_1)=1-r+O(\eta_c^2).
\]

At \(x_2=2r\), the Harnack lower from the preceding run gives

\[
\Im H_c(z_2)>\frac3{100},
\]

so

\[
A_r'(x_2)\Im H_c(z_2)
>
\frac{125000}{499}\frac3{100}.
\]

At \(x_3=1/2\),

\[
H_c(z_3)=i
\]

and therefore the corresponding coefficient is exactly

\[
A_r'(x_3)=\frac{499}{125}.
\]

The exact inequality

\[
\frac3{100}\frac{125000}{499}
>
\frac{499}{125}
\]

gives, for sufficiently small `c`,

\[
\boxed{
p_c(r)>p_c(2r)<p_c(1/2).
}
\tag{4.2}
\]

A unimodal law cannot have such a strict valley at three ordered points
where its density is analytic. If the mode were at or to the right of
\(2r\), monotonicity on the left would contradict \(p_c(r)>p_c(2r)\); if
the mode were to the left, monotonicity on the right would contradict
\(p_c(1/2)>p_c(2r)\).

Thus the C005 source-level negative answer remains mathematically supported
after branch hardening:

\[
\boxed{
\text{every non-Dirac probability law fails free strong unimodality.}
}
\]

Dirac laws are trivially FSU by translation.

**Portfolio status remains `PARTIAL / AUDIT_PENDING`, not CLOSED, because the owner protocol still requires P26 plus one distinct OTHER-track full-proof audit of the C005/C006 package.**

# 5. Move 16 — exact solvable small perturbations as adversarial stress

I used three solvable laws to test the sign conventions and limiting Pick
direction. These are **self-checks**, not new source results; the first two
are already within known finite-variance exclusions.

### 5.1 Cauchy perturbation

For a centered Cauchy law of scale `eta`,

\[
\phi(z)=-i\eta.
\]

Hence

\[
S=-\phi=i\eta,
\qquad
H\equiv i.
\]

The local equation becomes exactly

\[
W(z)=F_\nu(z+i\eta),
\]

so the first-order density change is precisely

\[
-\frac{\eta}{\pi}A_r'(x).
\]

This matches C006.3 and fixes the sign.

### 5.2 Semicircle perturbation

For a centered semicircle perturbation,

\[
\phi(z)=\frac{t}{z},
\qquad
S(z)=-\frac{t}{z}.
\]

At a witness boundary point

\[
z_x=\frac1{A_r(x)-i\beta_r},
\]

we have

\[
-\frac1{z_x}
=
-A_r(x)+i\beta_r.
\]

After centering at `z_3` and normalizing by the imaginary part, the
normalized Pick direction has

\[
\Im H(z_x)=1
\]

at all three points. Again the valley coefficient at `2r` is vastly larger
than at `1/2`, in agreement with the known fact that semicircle laws are not
FSU.

### 5.3 Symmetric Bernoulli perturbation

For the symmetric Bernoulli law on `{-c,c}`,

\[
F(z)=z-\frac{c^2}{z},
\]

so

\[
\phi_c(w)
=
\frac{\sqrt{w^2+4c^2}-w}{2}
=
\frac{c^2}{w}
-
\frac{c^4}{w^3}
+
O(c^6).
\]

Thus its normalized infinitesimal Pick direction converges to the
semicircle direction `1/w`. This independently stress-tests the local
branch formula in a compactly supported algebraic example.

The exact checker verifies all three transform identities/series. No
finite-variance theorem is claimed; Hasebe-Ueda already settled that class.

# 6. Move 26 — the only sporadic degeneracy is exactly the Dirac case

The normalization in C005/C006 depends on

\[
\eta_c
=
\Im[-\phi_{D_c\mu}(z_3)].
\]

The possible sporadic failure would be \(\eta_c=0\).

For \(w=x+iy\in\mathbb C^+\),

\[
G_\mu(w)
=
\int\frac1{w-t}\,d\mu(t),
\]

and

\[
-\Im G_\mu(w)
=
y\int\frac1{|w-t|^2}\,d\mu(t).
\]

Cauchy-Schwarz gives

\[
|G_\mu(w)|^2
\le
\int\frac1{|w-t|^2}\,d\mu(t).
\]

Therefore

\[
\Im F_\mu(w)
=
\frac{-\Im G_\mu(w)}{|G_\mu(w)|^2}
\ge y.
\tag{6.1}
\]

Equality in Cauchy-Schwarz occurs iff the function

\[
t\mapsto\frac1{w-t}
\]

is constant \(\mu\)-almost surely. This map is injective in real `t`, so
equality holds iff \(\mu\) is concentrated at one point.

Hence for every non-Dirac law,

\[
\boxed{
\Im F_\mu(w)>\Im w
}
\tag{6.2}
\]

throughout `C+`. On the canonical inverse domain, if
\(z=F_\mu(w)\),

\[
\Im\phi_\mu(z)
=
\Im(w-z)
<0.
\]

Thus

\[
\eta_c>0
\]

for every non-Dirac law and every sufficiently small `c` for which the
fixed normalization point lies in the scaled transform domain.

For a Dirac law the inequality is equality, \(\phi\) is real constant, and
\(\eta_c=0\). That is not a flaw in the method: Dirac measures are exactly
the trivial FSU laws. The only degeneracy of the normalization therefore
matches the expected classification boundary.

Atom-heavy non-Dirac laws do not create another exception. The local
continuation in C006 produces analytic density neighborhoods around the
fixed positive witness points `r`, `2r`, and `1/2`. Any possible free
convolution atom coming from a scaled candidate atom is confined near the
scaled/translated candidate location as `c -> 0` and is irrelevant to the
strict local density valley. In any case, a unimodal law — with or without
an atom at its mode — cannot have the ordered strict valley (4.2).

# 7. Exact self-check

New artifact:

`artifacts/R08/20260916T2030Z_i0082_branch_hardening_b6d12c_checker.py`

creation/readback commit:

`65fe97742b9c38081770a2e0bee12c4539213b44`.

Archived output:

`artifacts/R08/20260916T2030Z_i0082_branch_hardening_b6d12c_checker.out`

creation/readback commit:

`634aeb4316e83a463e32215cc926e39317478fec`.

Executed stdout SHA-256:

`4ea7720bded270d02d4b97999e94228c7b92b46e4de68f8053df972c26400719`.

The finite exact/symbolic checks are:

1. the flat-witness derivative identity and exact three-point coefficients;
2. the strict rational coefficient inequality;
3. Cauchy normalized Pick direction;
4. semicircle boundary Pick direction;
5. symmetric-Bernoulli small-scale Voiculescu series;
6. Dirac `eta=0` degeneracy;
7. the independent R09 audit calculations below.

The checker output ends:

`ALL_EXACT_CHECKS_PASS`.

The theorem-sized branch-selection argument is written on this page; the
checker is explicitly a self-check, not a substitute for the proof.

# 8. Independent audit of the newest R09 package

Newest R09 report read:

`runs/R09/20260916T192944Z_tang_structural_counterexample_transitive_probe.md`.

I independently audited its exact Cayley-graph calculation and the general
finite-stem second-derivative identity rather than trusting R09's checker.

For the Cayley graph of

\[
C_3*C_3
\]

with the natural four-generator set, one entered triangle has offspring
distribution

\[
P(X=0)=(1-p)^2,
\]

\[
P(X=1)=2p(1-p)^2,
\]

\[
P(X=2)=p^2(3-2p).
\]

The pgf satisfies exactly

\[
\phi(t)-t
=
(t-1)
\left[
p^2(3-2p)t-(1-p)^2
\right].
\]

The supercriticality polynomial is

\[
h(p)=-2p^3+2p^2+2p-1,
\]

with

\[
h(2/5)=-1/125<0,
\qquad
h(41/100)=9179/500000>0,
\]

and

\[
h'(p)=2(1-p)(3p+1)>0
\]

on `(0,1)`.

Above the unique critical root,

\[
q=\frac{(1-p)^2}{p^2(3-2p)},
\qquad
\theta(p)=1-q^2.
\]

Direct symbolic differentiation gives exactly

\[
\theta''(p)
=
-\frac{
12(1-p)^2
\left(
2p^4-12p^3+30p^2-34p+15
\right)}
{p^6(3-2p)^4}.
\]

The quartic has the positive Bernstein representation

\[
15(1-p)^4
+
26p(1-p)^3
+
18p^2(1-p)^2
+
6p^3(1-p)
+
p^4,
\]

so this transitive Cayley example is strictly concave throughout its
supercritical interval, exactly as R09 claimed.

For the finite-stem mechanism, independent differentiation gives

\[
\frac{d^2}{dp^2}\left[p^k\theta_T(p)\right]
=
p^{k-2}
\left[
k(k-1)\theta_T(p)
+
2kp\theta_T'(p)
+
p^2\theta_T''(p)
\right].
\]

**Audit verdict:**

`R08-AUDIT-R09-TANG-Q411-CAYLEY-03 = PASS`.

This audit concerns the exact Cayley/stem claims in the newest R09 report;
it does not certify the whole R09 Tang package or its prior-art status.

# 9. Audit/closure state for I0082

Repository searches this run found **no** P26 audit of
`R08-I0082-C005/C006` and no second independent OTHER-track full-proof
audit of this package.

Therefore the current distinctions are:

- mathematical source-answer candidate: **NO**;
- internal written proof: **C005 + C006 complete on page**;
- finite algebraic self-check: **PASS**;
- bounded prior-art search: **no published resolution found**;
- P26 full-proof audit: **MISSING**;
- distinct OTHER-track full-proof audit: **MISSING**;
- portfolio status: **PARTIAL / AUDIT_PENDING**;
- paper folder: **NOT CREATED**.

I do not call the source closed before those two audits.

# 10. Model/scheduler escalation status

Nothing changed in the exposed runtime controls. The available scheduled-task
interface supports title, prompt, schedule/start offset, enablement, and
timing mode. It exposes **no model selector and no reasoning-effort
selector**. Thus GPT-6/maximum remains a prompt request, not a verified
runtime setting.

A real fix requires either:

1. product support for model/reasoning fields in the authorized scheduler
   interface, with runtime metadata verifying the setting; or
2. editing the task from an owning workspace/UI that exposes those controls.

Historical `You cannot modify this task` responses for P26/P01/P03 are
ownership/permission boundaries. The repository records that P26 was later
successfully changed from another authorized context, confirming that the
denial can be context-specific. The valid workaround is the owning
account/workspace/interface or platform support — not a duplicate task and
not a repository edit pretending to change native scheduler state.

This run made no scheduler modification.

# 11. Current ledger

Retained I0082 claims:

- `R08-I0082-C001`: explicit positive free `1/2`-stable candidate fails FSU — PROVED;
- `R08-I0082-C002`: open stable-index neighborhood around the half-stable witness excluded — PROVED, subsumed;
- `R08-I0082-C003`: every non-Dirac free stable law of index `<2` fails FSU — PROVED, subsumed;
- `R08-I0082-C004`: stable-domain exclusion — PROVED, subsumed;
- `R08-I0082-C005`: only Dirac laws are FSU — PROVED ON PAGE / AUDIT_PENDING;
- `R08-I0082-C006`: local branch-selection and first-order perturbation lemma — **PROVED NEW**, hardens C005.

Frozen explicit-candidate metric:

\[
\boxed{2/3\to2/3}
\]

with supported unchanged count now

\[
\boxed{3}.
\]

No candidate switch is made.

# 12. Next-run instruction under the owner's stuck rule

Because the frozen metric has now failed to move for three consecutive runs,
the **next run must be a Section-I thinking-only stuck run** unless C005/C006
receives the two required outside audits first.

That report must state the exact remaining source obligation, every route
tried and its failure, the ingredient no route yet supplies, the simplest
still-unproved audit/regularity case, and the nearest solved theorem. It
must then choose exactly one permitted recovery rather than add another
lemma.

If audits have not arrived, the planned fresh method numbers for that
thinking run are:

- **1 — CHANGE THE CATEGORY:** reinterpret C005 as a universal
  infinitesimal variation-diminishing statement for Pick functions;
- **20 — FIND WHY THE ALGORITHM FAILS:** adversarially identify the weakest
  point an external referee could attack in the local analytic continuation
  and uniform remainder;
- **23 — DO WHAT THE PROPOSER DID NOT EXPECT:** assume a non-Dirac FSU law
  exists and derive the strongest transform rigidity statement forced by
  the flat witness.

No theorem claim is precommitted for that future run.

# 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  source:
    authors: "Takahiro Hasebe and Yuki Ueda"
    title: "Large time unimodality for classical and free Brownian motions with initial distributions"
    year: 2018
    locator: "Problem 3.11; Definition 3.8; Theorem 3.10"
    intake: I0082
  target: "Decide whether a non-Dirac freely strongly unimodal probability law exists."
  frozen_candidate: "positive free strict 1/4-stable law"
  metric: "number of three frozen candidate obligations proved"
  before: "2/3"
  after: "2/3"
  movement: "NO MOVEMENT"
  unchanged_count: 3
  source_status: "OPEN in bounded current literature search"
  portfolio_status: "PARTIAL / AUDIT_PENDING"
  mathematical_answer_candidate: "NO; C005 says only Dirac laws are FSU"
  methods_tried: [4, 16, 26]
  new_claims:
    - "R08-I0082-C006: local branch-selection and first-order perturbation lemma — PROVED"
  retained_claims:
    - "R08-I0082-C005: only Dirac laws are freely strongly unimodal — PROVED ON PAGE / AUDIT_PENDING"
  exact_evidence:
    - "artifacts/R08/20260916T2030Z_i0082_branch_hardening_b6d12c_checker.py @ 65fe97742b9c38081770a2e0bee12c4539213b44"
    - "artifacts/R08/20260916T2030Z_i0082_branch_hardening_b6d12c_checker.out @ 634aeb4316e83a463e32215cc926e39317478fec"
    - "stdout sha256 4ea7720bded270d02d4b97999e94228c7b92b46e4de68f8053df972c26400719"
  audit_ids:
    - "R08-AUDIT-R09-TANG-Q411-CAYLEY-03=PASS"
  closure_audits_for_I0082:
    p26: MISSING
    other_track: MISSING
  access_limits:
    - "intake corpus too large for row-for-row connector rendering; targeted I0082/source/ownership searches used"
    - "no native model or reasoning selector exposed"
```

No Gmail, Drive, email, public posting, purchase, permission change,
workflow execution, or scheduler change was performed.
