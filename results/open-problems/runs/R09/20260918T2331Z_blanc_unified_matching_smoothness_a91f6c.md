Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT on `BLANC-RENAUDIE-2026-MEANFIELD-7-10`: `M_A=0 -> 0`; stagnation count remains UNKNOWN. Methods used: #3, #21, #30.**

# R09 — Blanc-Renaudie `d=7,8,9,10`: one directional matching object for both mixing and high-frequency contraction

## 1. Continuity, source status, and ownership

I continued from `runs/R09/20260918T2234Z_blanc_polynomial_localmod_budget_c2a941.md`. I did **not** reopen Tang Question 4.11, G0013, the retired Chen--Wang successor, or the distinct C0064 Fourier-infrared-bound source.

Before research I re-read the controlling campaign roots (`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`), `operations/NEW_METHODS_2026-09-16.md`, the exclusive claim `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md`, the preceding R09 report, and the neighboring C0064 attempt. The active claim remains exclusively R09-owned, `READY / CLOSABLE OUTSIDE / OPEN`, with the frozen metric

\[
M_A=\#\{d\in\{7,8,9,10\}:\text{a complete rigorous Blanc--Renaudie initialization certificate is proved}\}.
\]

A fresh 2026-09-19 (Jerusalem-local date; 2026-09-18 UTC) exact-title/arXiv/author search recovered Arthur Blanc-Renaudie's arXiv:2609.20764, submitted 2026-09-17 and updated 2026-09-18, together with older related papers, and no later source-matching resolution of the nearest-neighbour `d=7,8,9,10` cases. This is bounded negative evidence, not a worldwide novelty certificate. Fitzner--van der Hofstad remains the rigorous nearest-neighbour mean-field result for `d>=11`. The older C0064 attempt remains distinct: it targets the Fourier infrared bound and records the failure of the NoBLE small-parameter bootstrap in `7<=d<=10`.

The source notation used below was checked directly against Sections 3.1, 3.4, and 3.5. In particular,

\[
\pi_p(\vec A):=\mathbb P_p^\otimes(\vec A_i=\vec A)
=\frac{\mu_p(\vec A)}{\Omega\chi(p)},
\quad
P_3^\otimes(\vec A,\vec B)
=\mathbb P_p^\otimes(T_{\rm cut}>3\mid \vec A_0=\vec A,\vec A_3=\vec B),
\]

and, conditional on the endpoints and survival, the Fourier factor in Proposition 3.25 is the characteristic function of
\(\Delta(\vec A_1)+\Delta(\vec A_2)\).

## 2. Method #3 — PROVE SOMETHING STRONGER: replace two source subroutines by one directional bridge-matching quantity

The source handles Theorem 3.14 (mixing) and Proposition 3.25 (high-frequency Fourier contraction) by two related but separately packaged local-modification arguments. I looked for one stronger object which implies both.

Fix endpoints \(\vec A,\vec B\in\vec C(0)\), and define the **surviving displacement subprobability**

\[
\zeta_{\vec A,\vec B}(x)
:=\mathbb P_p^\otimes\!\left(
T_{\rm cut}>3,\ 
\Delta(\vec A_1)+\Delta(\vec A_2)=x
\ \middle|\ 
\vec A_0=\vec A,\ \vec A_3=\vec B
\right),\qquad x\in\mathbb Z^d.
\]

Its total mass is exactly

\[
 s(\vec A,\vec B):=\sum_x\zeta_{\vec A,\vec B}(x)
 =P_3^\otimes(\vec A,\vec B)\in[0,1].
\]

For a coordinate direction \(e_i\), define the **fractional unit-shift matching mass**

\[
\mathfrak m_i(\vec A,\vec B)
:=\sup\left\{\sum_{x\in\mathbb Z^d}\eta_x:
\eta_x\ge0,\quad
\eta_x+\eta_{x-e_i}\le \zeta_{\vec A,\vec B}(x)\ \forall x
\right\}.
\tag{2.1}
\]

This is a weighted matching problem on the disjoint union of lattice lines parallel to \(e_i\). For finite support it is exactly a weighted bipartite matching / weighted vertex-cover problem and is rational when the input weights are rational.

### Proposition 2.1 (one raw matching mass gives both survival and Fourier contraction)

For every endpoint pair and every coordinate \(i\),

\[
\boxed{2\mathfrak m_i(\vec A,\vec B)\le s(\vec A,\vec B).}
\tag{2.2}
\]

If \(s>0\), then for every \(\kappa\in[-\pi,\pi]^d\),

\[
\boxed{
\Upsilon_{3,\kappa}(\vec A,\vec B)
\le
1-\frac{\mathfrak m_i(\vec A,\vec B)}{s(\vec A,\vec B)}
\frac{\kappa_i^2}{\pi^2}.
}
\tag{2.3}
\]

Consequently, for any \(a\in(0,1/2)\),

\[
\mathfrak m_i(\vec A,\vec B)\ge a
\quad\Longrightarrow\quad
\begin{cases}
P_3^\otimes(\vec A,\vec B)\ge 2a,\\[2mm]
\Upsilon_{3,\kappa}(\vec A,\vec B)
\le 1-(a/\pi^2)\kappa_i^2.
\end{cases}
\tag{2.4}
\]

#### Proof

Summing the capacity inequalities in (2.1) over all \(x\) gives
\(2\sum_x\eta_x\le\sum_x\zeta(x)=s\), proving (2.2).

Assume \(s>0\), write \(q_x=\zeta(x)/s\), and divide a feasible matching by \(s\). Let
\(m=\sum_x\eta_x/s\). The residual masses

\[
r_x=q_x-\eta_x/s-\eta_{x-e_i}/s
\]

are nonnegative and sum to \(1-2m\). Hence

\[
\widehat q(\kappa)
=\sum_xr_xe^{i\langle\kappa,x\rangle}
+\sum_x\frac{\eta_x}{s}
\left(e^{i\langle\kappa,x\rangle}+e^{i\langle\kappa,x+e_i\rangle}\right).
\]

Taking absolute values,

\[
|\widehat q(\kappa)|
\le 1-2m+2m\cos(|\kappa_i|/2)
=1-2m(1-\cos(|\kappa_i|/2)).
\]

For \(|t|\le\pi\),
\(1-\cos(t/2)=2\sin^2(t/4)\ge t^2/(2\pi^2)\). Thus

\[
|\widehat q(\kappa)|\le1-m\kappa_i^2/\pi^2.
\]

Taking the supremum over feasible matchings gives (2.3). By the source definition, this conditional characteristic-function modulus is exactly \(\Upsilon_{3,\kappa}\). Finally, \(s\le1\) implies \(\mathfrak m_i/s\ge\mathfrak m_i\), and (2.4) follows. \(\square\)

### Corollary 2.2 (a single typical matching test implies Proposition 3.25)

Suppose that for some \(a>0\) and \(\delta>0\), for every coordinate \(i\),

\[
(\pi_p\otimes\pi_p)
\{(\vec A,\vec B):\mathfrak m_i(\vec A,\vec B)<a\}
\le\delta.
\tag{2.5}
\]

Fix \(\kappa\) and take an index \(i\) with \(|\kappa_i|=\|\kappa\|_\infty\). Outside a set of endpoint probability at most \(\delta\), (2.3) gives

\[
\Upsilon_{3,\kappa}\le1-(a/\pi^2)\|\kappa\|_\infty^2.
\]

Therefore the conclusion of source Proposition 3.25 holds with \(c=a/\pi^2\) and exceptional probability \(\rho'=\delta\); in fact this is stronger because it does not need to condition on \(P_3^\otimes>\rho\).

### Proposition 2.3 (the same matching test supplies the overlap input for Theorem 3.14)

For the mixing argument only one coordinate is needed. Fix \(i=1\), let

\[
G=\{(\vec A,\vec B):\mathfrak m_1(\vec A,\vec B)\ge a\},
\]

and assume \((\pi_p\otimes\pi_p)(G^c)\le\delta\). Let \(\nu_p^\uparrow,\nu_p^\downarrow,Z_p\) be the source measures in (3.26). Pointwise,

\[
\nu_p^\uparrow(\vec A)\le\pi_p(\vec A),\qquad
\nu_p^\downarrow(\vec B)\le\pi_p(\vec B),
\qquad
\|\nu_p^\uparrow\|_1=\|\nu_p^\downarrow\|_1=Z_p.
\tag{2.6}
\]

Define the raw three-step bridge mass

\[
J(\vec A,\vec B)
:=\pi_p(\vec A)\pi_p(\vec B)P_3^\otimes(\vec A,\vec B).
\]

On \(G\), Proposition 2.1 gives

\[
\boxed{
J(\vec A,\vec B)
\ge2a\,\pi_p(\vec A)\pi_p(\vec B)
\ge2a\,\nu_p^\uparrow(\vec A)\nu_p^\downarrow(\vec B).
}
\tag{2.7}
\]

Also

\[
(\nu_p^\uparrow\otimes\nu_p^\downarrow)(G^c)
\le(\pi_p\otimes\pi_p)(G^c)\le\delta.
\tag{2.8}
\]

For \(\vec A\), let
\(b(\vec A)=\nu_p^\downarrow\{\vec B:(\vec A,\vec B)\notin G\}\). Given \(0<\eta<1\), set

\[
H=\{\vec A:b(\vec A)\le\eta Z_p\}.
\]

By (2.8),

\[
\boxed{
\nu_p^\uparrow(H^c)\le\frac{\delta}{\eta Z_p}.
}
\tag{2.9}
\]

For every \(\vec A\in H\), (2.7) yields the exact overlap bound

\[
\boxed{
\sum_{\vec B}
\min\{J(\vec A,\vec B),\,2a\nu_p^\uparrow(\vec A)\nu_p^\downarrow(\vec B)\}
\ge2a(1-\eta)\nu_p^\uparrow(\vec A)Z_p.
}
\tag{2.10}
\]

This is precisely the kind of bridge-overlap estimate for which source Lemmas 3.19--3.23 introduce the \(h_p\)-weighted norms. In particular, the local-modification Proposition 3.16 and Lemma 3.18 can be bypassed if (2.5) is certified with \(\delta\) small enough: source Lemma 3.15 gives \(Z_p\ge\lambda_p^2\), and the earlier R09 finite Perron certificate gives a finite route to \(\lambda_p\ge\ell>0\). Hence (2.9) is at most \(\delta/(\eta\ell^2)\), while (2.10) supplies the positive common-mass constant \(2a(1-\eta)\). Choosing \(\delta\) below the same smallness budget used in Proposition 3.23 lets the rest of the source's weighted-norm contraction proof run unchanged.

The key point is conceptual and quantitative: **one number, \(\mathfrak m_i\), simultaneously certifies a non-negligible surviving bridge and a unit spatial shift inside that bridge.** The source currently pays separately for these via finite-energy surgery.

## 3. The stronger criterion is itself finitely certifiable

The previous R09 run `20260918T2130Z_blanc_palm_sizebias_adaptive_core_4f72c9.md` proved the size-adaptive Palm tail

\[
\pi_p\{|\underline A|>N\}\le \frac{U^2}{N}
\tag{3.1}
\]

whenever an independent finite Simon--Lieb certificate gives \(\chi(p)\le U\). Let

\[
F_N:=\{\vec A:|\underline A|\le N\}.
\]

For endpoints \(\vec A,\vec B\in F_N\), restrict the two intermediate pointed clusters also to \(F_N\) and define the **unnormalized finite bridge displacement measure**

\[
\widetilde\zeta^{(N)}_{\vec A,\vec B}(x)
:=\sum_{\vec C,\vec D\in F_N}
\mu_p(\vec C)\mu_p(\vec D)
\mathbf1_{(\vec A,\vec C),(\vec C,\vec D),(\vec D,\vec B)\notin\mathcal C_{\rm cut}}
\mathbf1_{\Delta(\vec C)+\Delta(\vec D)=x}.
\tag{3.2}
\]

Let \(\widetilde{\mathfrak m}^{(N)}_i(\vec A,\vec B)\) be the same fractional matching LP (2.1) applied to (3.2). Since \(W:=\Omega\chi(p)\le\overline W:=\Omega U\), monotonicity and homogeneity of the matching LP imply

\[
\mathfrak m_i(\vec A,\vec B)
\ge \frac{\widetilde{\mathfrak m}^{(N)}_i(\vec A,\vec B)}{W^2}
\ge \frac{\widetilde{\mathfrak m}^{(N)}_i(\vec A,\vec B)}{\overline W^2}.
\tag{3.3}
\]

Therefore the finite exact inequalities

\[
\boxed{
\widetilde{\mathfrak m}^{(N)}_i(\vec A,\vec B)
\ge a\,\overline W^2
\quad\text{for every }\vec A,\vec B\in F_N,\ 1\le i\le d
}
\tag{3.4}
\]

imply (2.5) with

\[
\boxed{
\delta\le1-\pi_p(F_N)^2\le2\pi_p(F_N^c)\le\frac{2U^2}{N}.
}
\tag{3.5}
\]

At rational \(p\), every \(\mu_p(\vec A)\) in a finite family is a reliability polynomial evaluated at a rational number, and the matching LP is a weighted bipartite matching on finitely many lattice chains. Thus (3.4) is an exact-arithmetic finite certificate. This is a substantially tighter target than enumerating all source constants: one finite computation would feed **both** the mixing and the Fourier modules.

I did not run a large finite enumeration this hour. The point of the run was to replace two separate local-modification subroutines by one candidate finite statistic before spending compute on it.

## 4. Method #21 — ASK WHO ELSE HAS THIS SHAPE: translated-Poisson / lattice-smoothness language

The matching statistic has a clean equivalent lower bound in the language of lattice smoothness. For a probability mass function \(q\) on \(\mathbb Z^d\), let \(\tau_iq(x)=q(x-e_i)\). Then

\[
\sum_x\min\{q(x),q(x-e_i)\}
=1-d_{\rm TV}(q,\tau_iq).
\tag{4.1}
\]

Setting

\[
\eta_x=\tfrac12\min\{q(x),q(x+e_i)\}
\]

is feasible in the fractional matching LP, because the two incident edge masses at any vertex sum to at most its mass. Hence

\[
\boxed{
\mathfrak m_i(q)
\ge\frac12\left(1-d_{\rm TV}(q,\tau_iq)\right).
}
\tag{4.2}
\]

So the desired directional matching is exactly controlled by **unit-translate total-variation smoothness** of the surviving bridge displacement law.

This points to an adjacent literature that the original proof does not use: translated-Poisson and discrete-normal approximation for additive functionals of Markov chains. Barbour--Lindvall, *Translated Poisson approximation for Markov chains* (J. Theoret. Probab. 19 (2006), arXiv:0810.0599), obtains total-variation approximation under an aperiodicity assumption on regeneration-block sums; later Barbour--Xia work develops multivariate total-variation discrete-normal approximations under local dependence. The transferable idea is not their final approximation theorem verbatim, but their **smoothing mechanism**: aperiodic/regenerative block increments give control in the strong TV metric rather than only Kolmogorov distance.

This is unusually well matched to (4.2). A possible replacement for the source's forced ball surgery is therefore:

1. find a genuine regeneration event for the killed pointed-cluster chain with probability bounded away from zero;
2. prove that one regeneration block has two displacement values differing by \(e_i\), each with non-negligible conditional mass;
3. convolve regeneration blocks to force
\(d_{\rm TV}(q,\tau_iq)\le1-\epsilon\);
4. feed (4.2) into the unified criterion above.

There is an important circularity warning. Blanc--Renaudie's later local CLT cannot simply be invoked to prove (4.2), because that local CLT uses the high-frequency estimate from Theorem 3.24, whose Proposition 3.25 is exactly what we are trying to replace. The adjacent translated-Poisson/regeneration route is useful only if its unit-shift smoothing is proved **before** the source high-frequency theorem.

## 5. Method #30 — ONE SCALE AT A TIME: identify the first genuinely explosive quantitative layer

The preceding run made Proposition 3.8's error probability polynomially explicit. Its two long-range terms were

\[
C^2r^{4-d},\qquad C^3r^{6-d}.
\]

For every \(d>6\),

\[
\frac{3}{d-6}>\frac{2}{d-4},
\]

so the three-Green-kernel term is always the scale-setting one. Ignoring harmless target-error constants, the natural choice is

\[
\boxed{r\asymp C^{\kappa_d},\qquad \kappa_d=\frac{3}{d-6}.}
\tag{5.1}
\]

The two dominant finite-window / susceptibility terms then tie exactly:

\[
r^d/\chi
\quad\text{and}\quad
C^3r^6/\chi,
\]

because

\[
\kappa_dd=3+6\kappa_d=\frac{3d}{d-6}.
\tag{5.2}
\]

Thus the sharp real exponent generated by this bookkeeping is

\[
q_d^*=\frac{3d}{d-6},
\]

namely

\[
\boxed{
q_7^*=21,\qquad q_8^*=12,\qquad q_9^*=9,\qquad q_{10}^*=15/2.
}
\tag{5.3}
\]

The previous exact checker `artifacts/R09/20260918T2234Z_blanc_localmod_exponents_c2a941.py` already certifies the corresponding integer sufficient thresholds `(21,12,9,8)` and all competing exponent inequalities. No new checker was manufactured for the same arithmetic.

However, this run identifies a more serious layer that the polynomial table hides. The source's Lemma 3.18 and Proposition 3.29 pay a **finite-energy Radon--Nikodym cost** for forcing the local modifications \(f_r^\uparrow,f_r^\downarrow\). Those maps alter only edges in a bounded number of radius-\(O(r)\) balls plus an \(O(r)\)-length path, hence at most

\[
E_r\le K(d,L)(r+L)^d
\tag{5.4}
\]

edge states for an explicit geometric constant \(K(d,L)\).

In the regime relevant to the source, \(\chi(p)>2\) already forces \(p\ge1/(4d)\): if \(2dp<1/2\), the elementary walk union bound gives \(\chi(p)\le\sum_{n\ge0}(2dp)^n\le2\). Also \(p<p_c(\mathbb Z^d)\le p_c(\mathbb Z^2)=1/2\), so \(1-p\ge1/2\). Therefore each prescribed edge state has probability at least \(1/(4d)\). Allowing also for the finite preimage multiplicity of the deterministic modification, a completely explicit but crude version of the source's probability-ratio suprema is of the form

\[
M_r^\uparrow M_r^\downarrow
\le \exp\{K'(d,L)r^d\},
\tag{5.5}
\]

and the comparison constants in Lemma 3.18 / equation (3.34) can correspondingly be certified only at a scale

\[
\boxed{c_{\rm mod}\ge \exp\{-K'(d,L)r^d\}.}
\tag{5.6}
\]

This is a **guaranteed crude lower bound**, not a claim that the true constant is this small. But inserting (5.1) shows why a direct constant extraction becomes huge:

\[
\boxed{
|\log c_{\rm mod}|
\lesssim C^{3d/(d-6)}
}
\tag{5.7}
\]

with exponents `21,12,9,15/2` in dimensions `7,8,9,10` respectively. The source itself exposes these probability-ratio suprema in Lemma 3.18 and again in the proof of Proposition 3.29 (equation (3.34)); the latter is the step converting a local shift by \(-e_i\) into a Fourier gap.

This changes the quantitative diagnosis. The error **probabilities** in Proposition 3.8/3.16/3.26 can be made small with polynomial susceptibility thresholds, but the naive finite-energy implementation can still inject an exponentially small bridge/Fourier constant through the local surgery cost. That is a much more plausible explanation for the source's warning that a literal computation may be enormous.

The unified matching quantity \(\mathfrak m_i\) is designed precisely to avoid paying for an adversarially prescribed ball configuration. It asks only whether the *natural surviving bridge law already contains enough adjacent displacement mass*.

## 6. Outcome of the three methods

- **#3 (stronger statement): SUCCESS as a reduction.** Proposition 2.1 and the typical-set argument show that one directional fractional matching statistic can replace the two separate conceptual ingredients: surviving bridge overlap for mixing and one-step spatial shift for high-frequency Fourier contraction. It is also finitely certifiable once a finite susceptibility bound and finite pointed-cluster family are available.
- **#21 (adjacent shape): PROMISING but not yet imported as a theorem.** The matching statistic is bounded below by unit-translate TV smoothness, placing the problem in the translated-Poisson/discrete-normal smoothing framework for additive Markov functionals. The source's own LCLT is circular here, so a regeneration-level smoothness proof must be independent of Theorem 3.24.
- **#30 (one scale at a time): SUCCESS in isolating the true quantitative bottleneck.** The three-Green-kernel tail fixes `r ~ C^(3/(d-6))`; the first brute-force finite-energy constants then scale exponentially in `r^d`, with exponent `3d/(d-6)`. Improving only the polynomial error estimate will therefore not make the numerical program practical.

No dimension is certified this run. The honest source status remains **PARTIAL / OPEN** and

\[
\boxed{M_A:0\longrightarrow0.}
\]

## 7. Next fresh attacks

Reserve the previously unused Blanc-target moves **#2, #9, #29** for the next run:

- **#2 ATTACK THE NEGATION FIRST:** search for endpoint pairs / small pointed-cluster families where the normalized raw matching \(\mathfrak m_i\) collapses, to learn whether the unified criterion is too strong before building a large certifier.
- **#9 RANDOMIZE:** sample the natural finite bridge law only as a discovery tool to locate which endpoint geometries minimize matching; any promoted finite claim must then be exact-arithmetic certified.
- **#29 ADD THE POINTS AT INFINITY:** rescale the two-step bridge displacement at the correlation-length scale and ask whether the limiting law has a strictly positive directional shift-overlap; if so, compactness plus a quantitative local limit *before* Theorem 3.24 could supply a uniform matching constant.

## 8. Model/scheduler control status

The control limitation remains unchanged. The exposed scheduler interface offers prompt/title text, schedule/timing, enablement, and timing mode, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no hour-long execution guarantee**. Therefore the requested `GPT-6 / maximum` remains prompt text only; this report does not claim it ran.

Actually enforcing that setting requires an authorized product/workspace/API/admin surface that persists model and reasoning fields and attests the model used on each run. The historical P26 `You cannot modify this task` event was later followed by a successful P26 prompt update from another authorized context; R-series edits were denied from that P/C context. Any live modification denial must be resolved from the owning authorized context or through platform/admin support. I did not attempt to bypass permissions or create a duplicate schedule.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R09
  active_claim: BLANC-RENAUDIE-2026-MEANFIELD-7-10
  lane: CLOSABLE OUTSIDE
  source_status: OPEN
  mathematical_status: PARTIAL
  metric: M_A
  before: 0
  after: 0
  movement: no movement
  stagnation_count: UNKNOWN
  methods_used: [3, 21, 30]
  new_results:
    - raw directional fractional-matching lemma: one matching mass controls both three-step survival and conditional Fourier modulus
    - typical matching criterion reduces source Proposition 3.25 directly
    - same typical matching criterion supplies the bridge-overlap deficit needed by the source mixing proof
    - finite exact matching certificate using a finite pointed-cluster core plus an upper susceptibility bound
    - unit-shift TV smoothness lower-bounds the matching statistic
    - local-modification constant extraction has an exponential-in-r^d finite-energy layer; r is set by the three-Green-kernel tail
  certified_dimensions: []
  new_artifacts: []
  checker_note: previous exact exponent checker already covers the finite dimension table; no duplicate checker created
  next_methods: [2, 9, 29]
  prohibited_actions_taken: []
```
