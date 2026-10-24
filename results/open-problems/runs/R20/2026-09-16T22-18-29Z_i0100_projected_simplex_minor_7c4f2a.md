Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6 / maximum was requested, but the exposed scheduler/runtime provides no model selector or reasoning-effort selector, so this run is not claimed to be GPT-6 at maximum. **No movement: fixed metric 421 -> 421. Methods used: #15 BREAK THE SYMMETRY, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT.**
Problem/source: Afonso S. Bandeira (2025), Randomstrasse 101, Conjecture 26 / intake I0100 — one-localization of the prime Paley graph.

# R20 / I0100 — projected-simplex radial depth and positive Fourier-minor certificates

Status: **PARTIAL / source OPEN**. Finite certificates are not a proof of the asymptotic conjecture.

## 1. Continuity, ownership, scope and required reads

I continued from the newest immutable R20 report

`runs/R20/2026-09-16T20-47-17Z_i0100_p421_projection_cone_b3e921.md`

rather than restarting. Its exact-covered prime set is

`{5,13,17,29,41,181,241,421}`

and the fixed metric remains largest exact prime `421`.

The canonical claim `operations/claims/I0100.md` still assigns exactly Randomstrasse Conjecture 26 to R20 in the CLOSABLE OUTSIDE lane. The retired Kalikow assignment remains retired. P04/I0101 Conjecture 27, the historical R12/I0102 Conjecture 28 handoff, and C28/I0103 Conjecture 29 are distinct scopes and are not reassigned here.

Before new work I reread:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- the canonical I0100 claim;
- the newest R20 report and the newest located neighboring Paley surfaces, including P04/I0101, the R12/I0102 handoff, C28/I0103, and I0099/Conjecture 25.

The intake JSONL families are connector-truncated if rendered wholesale. I recovered I0100 through its canonical ownership record and repository-wide exact-ID search, but I do not falsely claim a manual byte-for-byte display of all roughly 780 intake rows.

P26 remains the shared-ledger writer. This run edits no shared root and no peer file.

## 2. Source normalization and current-status check — 2026-09-16/17

The live Randomstrasse source was checked again this run. For prime `p == 1 mod 4`, `G_p` is the Paley graph on `F_p`, and `G_{p,1}` is the graph induced on the neighbors of 0. Thus, after choosing a generator `alpha` of the nonzero quadratic residues, the vertex set is identified with

\[
Q^*=\{\alpha^j:j\in\mathbb Z_n\},\qquad n=\frac{p-1}{2}.
\]

The source uses the standard clique-bounding convention and Conjecture 26 remains

\[
\boxed{\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}.}
\tag{2.1}
\]

The source still displays this as a conjecture and separately lists Conjecture 27 (two-localization), Conjecture 28 (degree-four SOS), and Conjecture 29 (Paley ETF). A bounded current search this run covered the source page, Magsino--Mixon--Parshall's localized-Paley LP work, Kunisky's localized spectral work, current Randomstrasse/Jig surfaces, Hanson--Petridis and later clique-bound work, Turan/Delsarte support optimization, random circulant theta, and projected-simplex/orthant geometry. I found no source-matching proof or refutation of (2.1). This is a dated bounded search miss, not a worldwide novelty certificate.

Relevant current prior art for this run:

- Magsino--Mixon--Parshall derive the circulant localized-Paley theta LP and dual; the basic Fourier LP mechanism is standard, not claimed novel here.
- Kunisky proves weak spectral pseudorandomness for the one-localization, but the spectral edge remains conjectural and weak eigenvalue-distribution convergence does not determine the positive cone section.
- The 2025 random-circulant theta paper proves only a `sqrt(n)` lower scale and `sqrt(n log log n)` upper scale in expectation for a random analogue. Its discussion explicitly leaves the exact `sqrt(n)` scale open and notes positivity as a missing ingredient. Thus a generic random/RIP import does not close the present deterministic arithmetic case.
- Donoho--Tanner projected-simplex/orthant theory is the nearest geometric analogue, but it concerns random or specially ordered Fourier projections, not this deterministic Paley row set.

## 3. Frozen exact metric: no movement, 421 remains the largest certified prime

No new finite exact prime was pursued as the main research objective this run. The exact domain remains

\[
\boxed{\{5,13,17,29,41,181,241,421\}},
\qquad
\boxed{p_{\max}^{\mathrm{exact}}=421}.
\tag{3.1}
\]

The existing exact p=421 certificate remains

- `artifacts/R20/i0100_p421_exact_interval_certificate.py`,
- `artifacts/R20/i0100_p421_exact_interval_certificate.out`.

Its archived exact arithmetic proves matching primal/dual objectives at p=421; the finite claim remains PARTIAL evidence only.

This is the first unchanged R20 I0100 run after the preceding metric movement, so the consecutive unchanged count is **1**. The stuck threshold is not reached.

## 4. Setup for the new methods

Let

\[
H_p=G_{p,1}=\operatorname{Cay}(\mathbb Z_n,S_p),
\]

where

\[
S_p=\{s\in\mathbb Z_n\setminus\{0\}:\alpha^s-1\in Q^*\}.
\]

The set `S_p` is symmetric. Its cardinality is the local Paley degree

\[
d:=|S_p|=\frac{p-5}{4}=\frac n2-1,
\qquad n=2d+2.
\tag{4.1}
\]

Let

\[
T_p:=\vartheta(\overline{H_p}).
\]

The previous run proved the exact positive-cone projection formulation

\[
T_p
=\min\{\mathbf 1^Tq:q\ge0,\ q_0=1,\ K_pq=q\},
\tag{4.2}
\]

where

\[
K_p=F P_{\Omega_p}F^*,\qquad
\Omega_p=\{0\}\cup
\bigl(\mathbb Z_n\setminus(\{0\}\cup S_p)\bigr).
\]

This run breaks that symmetric cone formulation one step further.

## 5. Move #15 — break the symmetry: an exact moment-measure / projected-simplex formulation

Let

\[
\zeta=e^{2\pi i/n}.
\]

### Theorem 5.1 — exact moment-measure formulation

For every admissible prime,

\[
\boxed{
T_p^{-1}
=
\max\left\{
\nu_0:
\nu_m\ge0,\quad
\sum_{m\in\mathbb Z_n}\nu_m=1,\quad
\sum_m\nu_m\zeta^{sm}=0\ \ \forall s\in S_p
\right\}.
}
\tag{5.1}
\]

### Proof

Take any feasible `q` in (4.2) and write

\[
T=\sum_m q_m,
\qquad
\nu_m=\frac{q_m}{T}.
\]

Then `nu` is a probability vector and

\[
\nu_0=\frac1T
\]

because `q_0=1`.

The condition `K_pq=q` says exactly that the inverse Fourier transform of `q` is supported on `Omega_p`. Equivalently, its Fourier coefficients vanish at every forbidden lag `s in S_p`:

\[
\sum_m q_m\zeta^{sm}=0
\qquad (s\in S_p).
\]

Scaling by `T` gives the moment constraints in (5.1). Conversely, if a probability vector `nu` satisfies those constraints and `nu_0>0`, then

\[
q=\frac{\nu}{\nu_0}
\]

has `q>=0`, `q_0=1`, the required Fourier support, and objective

\[
\sum_mq_m=\nu_0^{-1}.
\]

Taking the optimum proves (5.1). QED.

### Corollary 5.2 — projected regular simplex radial depth

Let

\[
E_{S_p}=\{z\in\mathbb C^{S_p}:z_{-s}=\overline{z_s}\},
\]

viewed as a real vector space. Since `S_p=-S_p` and `0 notin S_p`,

\[
\dim_{\mathbb R}E_{S_p}=|S_p|=d.
\]

Define

\[
v_m=(\zeta^{sm})_{s\in S_p}\in E_{S_p},
\qquad
C_p=\operatorname{conv}\{v_m:m\ne0\}.
\]

Put

\[
t_p=\max\{t\ge0:-t v_0\in C_p\}.
\tag{5.2}
\]

Then

\[
\boxed{T_p=1+\frac1{t_p}.}
\tag{5.3}
\]

Indeed, if `a=nu_0` and

\[
y=\frac1{1-a}\sum_{m\ne0}\nu_m v_m\in C_p,
\]

the moment constraints say

\[
a v_0+(1-a)y=0,
\]

so

\[
y=-\frac a{1-a}v_0.
\]

Thus `t=a/(1-a)`, and because `a=1/T_p`, (5.3) follows.

The columns satisfy the exact tight-frame identities

\[
\boxed{
\sum_{m\in\mathbb Z_n}v_m=0,
\qquad
\|v_m\|_2^2=d,
\qquad
\sum_m v_mv_m^*=nI_{E_{S_p}}.
}
\tag{5.4}
\]

These are immediate from the orthogonality of distinct characters of `Z_n`.

To see the underlying simplex, define full nonzero-frequency vectors

\[
w_m=(\zeta^{rm})_{r\in\mathbb Z_n\setminus\{0\}}.
\]

Then, in the real conjugation subspace,

\[
\langle w_m,w_{m'}\rangle
=\sum_{r\ne0}\zeta^{r(m-m')}
=\begin{cases}
n-1,&m=m',\\
-1,&m\ne m'.
\end{cases}
\tag{5.5}
\]

Hence the `w_m` are the vertices of a regular simplex, and `v_m` is exactly its coordinate projection onto the rows indexed by `S_p`.

Therefore Conjecture 26 is exactly a deterministic half-dimensional projected-simplex radial-depth problem.

Since

\[
\|v_0\|=\sqrt d\sim\sqrt{n/2},
\]

and `T_p~sqrt(n)`, (5.3) gives the equivalent normalized statement

\[
\boxed{
\operatorname{dist}_{\text{radial}}
\left(0,\partial C_p; -v_0\right)
=t_p\|v_0\|
\longrightarrow\frac1{\sqrt2}.
}
\tag{5.6}
\]

This `1/sqrt(2)` is the same source constant, now interpreted geometrically.

### Polar form

The Minkowski gauge/polar identity applied to (5.2) gives another exact equivalent:

\[
\boxed{
T_p-1
=\max\left\{
-\langle y,v_0\rangle:
\langle y,v_m\rangle\le1\ \forall m\ne0
\right\}.
}
\tag{5.7}
\]

This is a margin/supporting-hyperplane problem for the projected simplex.

### Bandlimited peak form

Set

\[
f=n\nu-\mathbf1.
\]

Then

\[
f_m\ge-1,\qquad \sum_m f_m=0,
\]

and the Fourier transform of `f` is supported on the local nonedge set

\[
N_p=\mathbb Z_n\setminus(\{0\}\cup S_p).
\]

Also

\[
f_0=\frac n{T_p}-1.
\]

Therefore, defining

\[
M_p=\max\left\{
f_0:
 f\ge-1,\ \sum_m f_m=0,\
 \operatorname{supp}\widehat f\subseteq N_p
\right\},
\]

we get the exact identity

\[
\boxed{T_p=\frac n{1+M_p}.}
\tag{5.8}
\]

The source conjecture is equivalently

\[
M_p\sim\sqrt n.
\tag{5.9}
\]

This is a one-sided bandlimited/Turan extremal problem rather than an extreme-eigenvalue problem.

## 6. Move #24 — identify the extremal object: positive half-size Fourier minors

The moment LP (5.1) has real equality rank at most `d+1`: one normalization equation and `d` real Fourier moment conditions. Therefore an optimum exists at an extreme point supported on at most

\[
\boxed{d+1=\frac n2}
\tag{6.1}
\]

frequencies.

This is the precise benefit of deliberately breaking reflection symmetry. The previous even/cosine representation can hide a much sparser nonsymmetric basic optimum.

Assume a nondegenerate extreme support has the form

\[
A=\{0\}\cup B,
\qquad |B|=d,
\]

and define the square partial Fourier minor

\[
W_B=(\zeta^{sb})_{s\in S_p,\ b\in B}.
\tag{6.2}
\]

If `W_B` is nonsingular, write

\[
a=\nu_0,\qquad x=(\nu_b)_{b\in B}.
\]

The equality system is

\[
a+\mathbf1^Tx=1,
\qquad
a\mathbf1+W_Bx=0.
\]

Hence

\[
x=-aW_B^{-1}\mathbf1
\]

and

\[
a\left(1-\mathbf1^TW_B^{-1}\mathbf1\right)=1.
\]

Therefore the associated objective is

\[
\boxed{
T_B
=1-\mathbf1^TW_B^{-1}\mathbf1,
\qquad
\nu_0=T_B^{-1},
\qquad
\nu_B=-T_B^{-1}W_B^{-1}\mathbf1.
}
\tag{6.3}
\]

By the matrix determinant lemma,

\[
\boxed{
T_B
=\frac{\det(W_B-\mathbf1\mathbf1^T)}{\det W_B}.
}
\tag{6.4}
\]

If

\[
-W_B^{-1}\mathbf1\ge0
\tag{6.5}
\]

coordinatewise and `T_B>0`, then (6.3) gives an explicit feasible moment measure and therefore the rigorous upper certificate

\[
T_p\le T_B.
\tag{6.6}
\]

If `B` is an optimal basic support, equality holds.

This gives a concrete infinite-prime certificate-family target that was absent from the previous cone formulation:

> find a deterministic rule `p -> B_p`, `|B_p|=d`, such that
> \[
> -W_{B_p}^{-1}\mathbf1\ge0,
> \qquad
> 1-\mathbf1^TW_{B_p}^{-1}\mathbf1
> \le(1+o(1))\sqrt n.
> \tag{6.7}
> \]

The lower half of the asymptotic can be obtained without a separate lower-bound method if the analogous construction is made for the complement local Cayley graph as well. Because `H_p` is vertex-transitive,

\[
\vartheta(H_p)\vartheta(\overline{H_p})=n.
\tag{6.8}
\]

Thus paired upper certificates

\[
\vartheta(H_p)\le(1+o(1))\sqrt n,
\qquad
\vartheta(\overline{H_p})\le(1+o(1))\sqrt n
\]

would force both quantities to be `(1+o(1))*sqrt(n)` and close Conjecture 26.

### Numerical discovery only — not a finite theorem

To see whether (6.3) reflects actual optimizers, I ran a deliberately non-exact HiGHS discovery calculation on the already exactly certified primes. The script/output are archived and explicitly marked discovery-only:

- `artifacts/R20/2026-09-16T22-18-29Z_i0100_basic_support_discovery.py`;
- `artifacts/R20/2026-09-16T22-18-29Z_i0100_basic_support_discovery.out`.

Results:

- p=181: a nonsymmetric optimum with support size `45=d+1`; the minor formula matches the known exact theta numerically to about `2.7e-13`;
- p=241: support size `60=d+1`; formula match about `2.8e-12`;
- p=421: the returned optimum is degenerate with support size `104=d`, so the tempting stronger guess `every optimum has exactly d+1 positive coordinates` is already numerically false and is **not** promoted.

This discovery computation does not extend the exact prime metric and is not used as a proof.

## 7. Move #20 — find why the obvious algorithm fails

The most immediate algorithm after the previous projection formulation is: project the coordinate spike `e_0` into the allowed Fourier subspace and scale it until it becomes feasible.

Let

\[
g=K_pe_0-\frac1n\mathbf1.
\tag{7.1}
\]

Then `g` has zero mean and Fourier support in `N_p`. From the exact kernel formula of the previous report,

\[
g_0=\frac12,
\qquad
 g_m=-\frac{\lambda_m+1}{n}\quad(m\ne0),
\tag{7.2}
\]

where `lambda_m` are the local adjacency eigenvalues.

For `f=cg` to obey the bandlimited constraint `f>=-1`, one must have

\[
c\le\frac n{1+\lambda_{\max}}
\tag{7.3}
\]

whenever the positive spectral edge controls the most negative coordinate. Hence the attainable peak is at most

\[
f_0\le\frac n{2(1+\lambda_{\max})}.
\tag{7.4}
\]

Plugging this into (5.8) gives only

\[
T_p
\le
\frac{n}{1+n/[2(1+\lambda_{\max})]}
=
\frac{2n(1+\lambda_{\max})}{n+2(1+\lambda_{\max})}.
\tag{7.5}
\]

At the expected local Paley spectral scale

\[
\lambda_{\max}\asymp\frac{\sqrt p}{2}\asymp\sqrt{\frac n2},
\]

(7.5) is asymptotic to

\[
\sqrt{2n}\asymp\sqrt p,
\]

which misses the target `sqrt(n)` by the familiar factor `sqrt(2)`.

So `project a delta and rescale` provably collapses the full cone problem back to a one-extreme-eigenvalue certificate. The missing constant is genuinely carried by coordinated positivity across many Fourier modes.

This diagnosis also explains why a generic RIP route is insufficient. The current random-circulant literature gets an extra `sqrt(log log n)` in the analogous upper bound and explicitly notes that positivity is discarded in the RIP step. The exact constant `sqrt(n)` is still conjectural even for that random model. Therefore `prove Paley RIP, then quote random-circulant theta` is not presently a closure mechanism; it would also risk duplicating the distinct Paley-ETF/RIP scope owned by C28.

A second instructive comparison is Donoho--Tanner's deterministic low-frequency partial Fourier matrix. There, the row ordering creates a cyclic-polytope/variation-diminishing sign theorem, and the all-ones row is crucial. The Paley row set `S_p` is arithmetically scattered, so that exact sign-variation argument does not transfer. The missing theorem should be viewed as an arithmetic analogue of inverse-positivity/neighborliness for the Paley Fourier minor, not as another generic spectral norm bound.

## 8. The current exact obstruction in one displayed formula

The strongest concrete analytic target emerging from this run is:

\[
\boxed{
\exists B_p\subset\mathbb Z_n\setminus\{0\},\ |B_p|=d:\qquad
-W_{B_p}^{-1}\mathbf1\ge0,
\quad
1-\mathbf1^TW_{B_p}^{-1}\mathbf1
=(1+o(1))\sqrt n.
}
\tag{8.1}
\]

Together with the analogous statement for the complementary row set, this would close the source conjecture via (6.8).

Equivalently, without choosing a basis, the target is the projected-simplex radial-depth theorem

\[
\boxed{
\max\left\{r\ge0:
-r\frac{v_0}{\sqrt d}
\in
\operatorname{conv}\left\{\frac{v_m}{\sqrt d}:m\ne0\right\}
\right\}
\longrightarrow\frac1{\sqrt2}.
}
\tag{8.2}
\]

This is exactly equivalent to Conjecture 26, not a stronger invented replacement.

## 9. What the three methods changed

### #15 BREAK THE SYMMETRY

The even/cosine theta LP was replaced by the full probability-moment LP. This exposes basic optimizers supported on at most `n/2` frequencies and reveals a sparse nonsymmetric certificate architecture hidden by the symmetric dual.

### #20 FIND WHY THE ALGORITHM FAILS

The natural projected-spike construction was calculated exactly enough to show it reduces to the extreme eigenvalue and loses the target constant by `sqrt(2)`. Generic random-circulant/RIP methods currently have the same conceptual weakness: they discard positivity.

### #24 FIND THE EXTREMAL OBJECT

The target is now identified exactly as either:

1. radial depth of a deterministic half-dimensional projection of a regular simplex;
2. an inverse-positive half-size Paley Fourier minor;
3. a one-sided bandlimited peak problem.

These are three equivalent representations of the same source quantity, and they point to different mature toolboxes without changing scope.

## 10. Scheduler/model escalation status

The exposed automation interface still has no model selector and no reasoning-effort selector. It exposes prompt/title, schedule, enabled state and timing mode, but the requested `GPT-6 / maximum` line is prompt text rather than a verified runtime configuration. A real fix requires product/platform support or a scheduler/UI/API revision that exposes model and reasoning fields; a GitHub prompt edit cannot change that.

Repository deployment history records a context-dependent P26 error `You cannot modify this task` and also later successful P/C prompt deployment from an authorized context. If a task refuses modification, the allowed workaround is to use its authorized owning product context or platform/admin support. Do not create a duplicate task, bypass ownership, or claim that editing repository text altered the native schedule.

No scheduler modification was attempted in this run under the current operational addendum.

## 11. Audit state

Existing independent OTHER-track exact finite-case audits recovered this run include:

- `R19-AUDIT-R20-I0100-P181-01=PASS_EXACT_FINITE_CASE`;
- `R19-AUDIT-R20-I0100-P241-02=PASS_EXACT_FINITE_CASE`.

No independent p=421 audit was located, and no asymptotic audit exists. These finite audits do not close Conjecture 26.

## 12. Ledger delta

```yaml
ledger_delta:
  worker: R20
  source: "Afonso S. Bandeira, Randomstrasse 101 (2025), Conjecture 26 / I0100"
  target: "theta(complement G_{p,1}) ~ sqrt(p/2) for primes p=1 mod 4"
  metric: "largest admissible prime with matching exact primal/dual certificate"
  covered_primes: [5, 13, 17, 29, 41, 181, 241, 421]
  before: 421
  after: 421
  movement: "no movement"
  status: PARTIAL
  source_status: OPEN
  unchanged_count: 1
  section_B_moves: [15, 20, 24]
  exact_evidence:
    - artifacts/R20/i0100_p421_exact_interval_certificate.py
    - artifacts/R20/i0100_p421_exact_interval_certificate.out
  discovery_evidence:
    - artifacts/R20/2026-09-16T22-18-29Z_i0100_basic_support_discovery.py
    - artifacts/R20/2026-09-16T22-18-29Z_i0100_basic_support_discovery.out
  audit_ids:
    - R19-AUDIT-R20-I0100-P181-01=PASS_EXACT_FINITE_CASE
    - R19-AUDIT-R20-I0100-P241-02=PASS_EXACT_FINITE_CASE
  remaining_obligation: >-
    Prove the projected-simplex radial-depth theorem / inverse-positive Paley Fourier-minor family, and the complementary upper certificate needed with the vertex-transitive theta product. Finite certificates remain PARTIAL.
```

## 13. Next attack

Do **not** spend the next run mainly extending the prime cutoff unless a new analytic rule predicts the support.

The highest-value next attack is to study the sign of

\[
-W_B^{-1}\mathbf1
\]

for structured half-size Paley Fourier minors. Three concrete directions are now available:

1. seek a Paley analogue of the Donoho--Tanner cyclic-polytope inverse-sign theorem, replacing monotone low Fourier frequencies by multiplicative-character/Jacobi phase ordering;
2. exploit the complementary row split `S_p` / `N_p` and Naimark-complement geometry to construct paired upper certificates directly, because the theta product then supplies the missing lower bound automatically;
3. use exact p=181/241/421 optimizers only as discovery data to guess a deterministic rule for `B_p`, then prove inverse positivity and asymptotic determinant ratio analytically before spending further effort on large-prime certification.

**NO CLOSURE CLAIM.**
