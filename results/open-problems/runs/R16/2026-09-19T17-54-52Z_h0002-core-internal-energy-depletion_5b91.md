Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala metric remains the current-preprint baseline `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`; on the active exclusive R16/H0002 successor, the complete uniform giant-fraction envelope improves from `G_rearr` to `G_H2energy`, with `G_H2energy>=G_rearr` for every frozen parameter triple and `G_H2energy>G_rearr` whenever `G_rearr<1`. Methods actually used: **#25 COUNT THE SAME THING TWICE, #3 PROVE SOMETHING STRONGER, #26 HUNT THE SPORADIC CASE**. All thirty Section-B moves had already appeared somewhere in the recovered H0002 history, so these are honest nonconsecutive reuses rather than falsely advertised first uses; the preceding triple was #1/#20/#24.

# R16 — H0002: macroscopic pair expansion forces internal core energy and depletes the absorption budget

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Continuity, required repository reads, source status, and ownership

This run continues from the newest immutable R16 report

`runs/R16/2026-09-19T16-46-14Z_h0002-opposite-monotone-weighted-energy_31d8.md`,

whose incoming complete envelope is `G_rearr`. It does not restart Beck--Fiala and it does not reopen any earlier R16 target.

Before new research I re-read/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical claim `operations/claims/H0002.md`;
- the H-intake identity `arxiv_2608_19145::Question 5.1; Section 5, Concluding remarks` in `probability_1000_intake_H_20260914/problems.jsonl`;
- the newest own R16 report above and the earlier all-padding / multi-anchor / prefix-majorization reports needed for notation; and
- the neighboring same-paper G0011 history, which is a distinct long-cycle target and creates no ownership conflict.

The compact root `RESULTS.md` still warns that its R-series table is stale and that a newer complete own-track report must be recovered before replacing a value. In accordance with policy, this run records its delta only here and does not edit the shared root.

### Current primary-source check, 2026-09-19

The nominal scheduler title is no longer an honest unresolved existence problem on the current manuscripts:

- Nikhil Bansal and Haotian Jiang, arXiv:2508.03961v2, directly prove the Beck--Fiala `O(sqrt(t))` scale for `t>=log^2 n`, and give a weaker polylogarithmic-loss estimate below that range. Their result is algorithmic. URL: https://arxiv.org/abs/2508.03961 .
- Shengtao Guo, Ethan X. Fang, and Junwei Lu, arXiv:2609.11189v1, submitted 2026-09-10, prove the stronger Komlos statement with constant `3 sqrt(2 pi)` and explicitly deduce discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`, with no restriction on `n`. URL: https://arxiv.org/abs/2609.11189 .
- Sankeerth Rao Karingula and Shachar Lovett, ECCC TR26-188, posted 2026-09-17, give an elementary Komlos proof with constant `36`. URL: https://eccc.weizmann.ac.il/report/2026/188/ .
- A fresh comparison also surfaced Dylan J. Altschuler, arXiv:2609.19714 (2026-09-17), on improved algorithms for Beck--Fiala with bounded set size; it does not change the existence-level supersession above.

These are very recent preprints / technical reports, not mature refereed consensus. On their stated theorems, however, literal Beck--Fiala is a **KNOWN CURRENT-PREPRINT BASELINE**, so R16 correctly continues the already-admitted successor rather than inventing a `t<log^2 n` gap.

The active source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (2026-08-19), Question 5.1: find natural graph conditions under which `p >= (1+epsilon)/lambda(G)` forces a component of order `Omega(|G|)` with constant probability. URL: https://arxiv.org/abs/2608.19145 . A fresh bounded title/author/question search did not surface a later source-matching resolution. That is negative search evidence only, not a proof of worldwide openness or novelty.

## 2. Frozen H0002 class and incoming endpoint notation

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n:=|G|`, `lambda:=lambda(G)`,

`q0:=1-exp(-epsilon^2/288)`,

`alpha:=rho*q0/64`,

`Delta:=epsilon*(7-epsilon)/(8-epsilon)>0`.

The graph class is unchanged:

1. **H1:** `lambda(G-S) >= (1-epsilon/8) lambda(G)` whenever `|S|<=rho n`;
2. **H2:** `e_G(X,Y) >= kappa lambda(G)n` for every disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. **H3:** `lambda(G)->infinity`.

The current R16 chain supplies an endpoint connected-core density

`a_P:=rho-alpha+d_P`,

with `d_P>d1>0` and `d_P<alpha`, hence

`b_P:=alpha-d_P>0`,

`u_P:=1-a_P`.

Because `alpha/rho=q0/64<1/64`, already `rho-alpha>63rho/64>2alpha`; therefore

`a_P>2alpha`.                                                    (2.1)

The established terminal threshold profile is

`t(b):=[a_P/(rho-b)] [F_pad(alpha-b)/b]`,

continuously extended by `t(b_P)=0`. Fix the already-selected `b_0>b_P` with

`t_0:=t(b_0)>0`,

and let

`bar_t(q):=sup_{b_P<=b<=q}t(b)`

on the terminal prefix, extended by zero for `q<b_P`. Then `bar_t(b_0)=t_0`.

For the sorted normalized outside-degree profile into the endpoint core,

`x(q)=d_W(v_q)/lambda`,

where `x` is nondecreasing on `[0,u_P]`, the previous reports give

`int_0^b x(q)dq >= b t(b)`                                     (2.2)

for every certified terminal `b`, hence

`int_0^{b_0}x(q)dq >= b_0 t_0`,                                (2.3)

and therefore

`x(q)>=t_0` for a.e. `q in [b_0,u_P]`.                         (2.4)

The preceding report used the global spectral-energy estimate

`int_0^{u_P}x(q)^2dq <= a_P`,                                  (2.5)

then deducted the forced tail energy from (2.4), obtaining

`A_tail:=a_P-(u_P-b_0)t_0^2`,                                  (2.6)

and combined opposite monotonicity with the Stieltjes weight

`v(q):=exp(-Delta bar_t(q))-exp(-Delta t_0)`.                  (2.7)

Put

`V_0:=int_0^{b_0}v(q)dq`.                                      (2.8)

Since `bar_t=0` on `[0,b_P)` and `b_P,t_0>0`,

`V_0 >= b_P(1-exp(-Delta t_0))>0`.                             (2.9)

For every old finite-anchor floor `L_D<=bar_t`, let

`y(q):=[x(q)-L_D(q)]_+`.

The preceding Stieltjes duality gives the exact positive weighted first moment

`int_0^{b_0}v(q)y(q)dq >= Theta>0`,                             (2.10)

where

`Theta=int K(s) mu(ds)`,

`K(s)=s bar_t(s)-int_0^s bar_t(q)dq`,

`mu=Delta exp(-Delta bar_t)d bar_t`.

The preceding report then proved

`int_0^{b_0}v(q)y(q)^2dq <= M_rearr`,                           (2.11)

with

`M_rearr:=(V_0/b_0)A_tail`,                                    (2.12)

and hence

`eta_rearr:=Theta g_Delta(M_rearr/Theta)`,                     (2.13)

where

`g_Delta(z):=(1-exp(-Delta z))/z`, `g_Delta(0)=Delta`.

It froze

`delta_rearr:=eta_rearr/4`,                                    (2.14)

and the complete incoming envelope

`G_rearr:=min{1,G_coreavg+E_rfgap+delta_rearr}`.               (2.15)

This run attacks the remaining looseness in (2.5): H2 itself forces a positive amount of `||A_G 1_W||_2^2` to lie **inside** the core, so the outside degree profile cannot consume the full budget `a_P`.

## 3. Method #26 — the apparent sporadic obstruction is divisibility of the core into alpha-blocks

A first attempt is to partition the connected core `W` into disjoint blocks of density `alpha` and apply H2 to every pair of blocks. This immediately forces many internal edges, but it introduces a staircase constant depending on `floor(a_P/alpha)` and leaves an annoying leftover block. The resulting bound changes discontinuously when `a_P/alpha` crosses an integer and is plainly not the natural invariant.

This is exactly the sort of sporadic finite obstruction that should be removed before doing analysis. Instead of partitioning, average over **all ordered pairs of disjoint alpha-subsets of W**. That erases every divisibility and leftover issue and produces an exact coefficient. No finite checker is needed because the counting identity is closed-form.

All thirty Section-B moves have already appeared in the H0002 history; #26 is therefore a deliberate nonconsecutive reuse against a new obstruction, not a claim that this is the first time the number was named.

## 4. Method #25 — count the same internal edges twice

### Lemma 1 (H2 forces internal core energy)

Let `W subset V(G)` satisfy

`|W|=a n+o(n)`

for a fixed `a>2alpha`. Then

`sum_{w in W} d_W(w)^2`
` >= [kappa^2 a^3/alpha^4-o(1)] lambda^2 n`.                  (4.1)

Consequently

`sum_{v notin W} d_W(v)^2`
` <= [a-kappa^2 a^3/alpha^4+o(1)] lambda^2 n`.                (4.2)

#### Proof

Let

`N:=|W|`, `m:=ceil(alpha n)`.

By `a>2alpha`, for all sufficiently large `n` we have `2m<=N`. Choose uniformly an ordered pair `(A,B)` of disjoint `m`-subsets of `W`. Every realization satisfies H2, so

`e_G(A,B)>=kappa lambda n`.                                    (4.3)

A fixed internal edge `{u,v}` of `W` is counted by `e(A,B)` precisely when its endpoints are split between `A` and `B`. Its probability is exactly

`P({u,v} crosses A,B)`
` =2 (m/N)(m/(N-1))`
` =2m^2/[N(N-1)]`.                                             (4.4)

Averaging (4.3) and counting every internal edge by (4.4) gives

`[2m^2/(N(N-1))] e(W) >= kappa lambda n`,                     (4.5)

hence

`2e(W) >= kappa lambda n N(N-1)/m^2`.                          (4.6)

Now use Cauchy--Schwarz on the internal degree sequence:

`sum_{w in W}d_W(w)^2`
` >= [sum_{w in W}d_W(w)]^2/N`
` = [2e(W)]^2/N`
` >= kappa^2 lambda^2 n^2 N(N-1)^2/m^4`.                      (4.7)

Since `N/n->a` and `m/n->alpha`, (4.1) follows.

On the other hand, if `A_G` is the adjacency matrix, then

`sum_{v in V}d_W(v)^2`
` = ||A_G 1_W||_2^2`
` <= lambda^2 ||1_W||_2^2`
` = lambda^2 N`,                                               (4.8)

because the operator norm of the symmetric nonnegative adjacency matrix is its spectral radius `lambda`. Subtracting (4.1) from (4.8) gives (4.2). `QED`

Define the endpoint depletion constant

`boxed: chi_P:=kappa^2 a_P^3/alpha^4>0.`                      (4.9)

Applying Lemma 1 to the endpoint core gives the sharpened outside-energy bound

`boxed: int_0^{u_P}x(q)^2dq <= a_P-chi_P.`                   (4.10)

### Sanity check: the known H2 compatibility bound drops out automatically

If one puts `W=V(G)` in the same argument, (4.1) together with (4.8) yields asymptotically

`kappa^2/alpha^4<=1`,

that is

`kappa<=alpha^2`,                                               (4.11)

exactly the H2 nonvacuity condition already recovered earlier in the chain. This independently checks the normalization and the power `alpha^4` in (4.9).

## 5. Method #3 — prove the stronger energy statement and feed it into the exact weighted moment theorem

Equation (4.10) is stronger than the preceding global budget (2.5) by the fixed positive amount `chi_P`. Retain the already-proved tail floor (2.4). Then

`int_0^{b_0}x(q)^2dq`
` <= a_P-chi_P-(u_P-b_0)t_0^2`.                               (5.1)

Define

`boxed: A_H2:=a_P-chi_P-(u_P-b_0)t_0^2.`                     (5.2)

This quantity is positive on every nonvacuous frozen sequence. Indeed (2.3) and Cauchy--Schwarz give prefix energy at least `b_0 t_0^2`, while (2.4) gives tail energy at least `(u_P-b_0)t_0^2`; therefore any feasible outside profile has total energy at least `u_P t_0^2`, and (4.10) forces

`a_P-chi_P >= u_P t_0^2`,

so in fact

`A_H2>=b_0 t_0^2>0`.                                          (5.3)

Now reuse the opposite-monotone rearrangement inequality from the incoming report. The weight `v` is nonincreasing and `x^2` is nondecreasing, while `0<=y<=x`. Hence

`int_0^{b_0}v(q)y(q)^2dq`
` <= int_0^{b_0}v(q)x(q)^2dq`
` <= (V_0/b_0) int_0^{b_0}x(q)^2dq`
` <= M_H2`,                                                    (5.4)

where

`boxed: M_H2:=(V_0/b_0)A_H2.`                                (5.5)

Comparing with (2.12),

`M_H2`
` = M_rearr-(V_0/b_0)chi_P`.                                  (5.6)

By (2.9) and (4.9),

`boxed: M_H2<M_rearr.`                                        (5.7)

The exact weighted first-moment lower bound `Theta` is unchanged. Therefore the exact two-moment lemma yields

`boxed: eta_H2:=Theta g_Delta(M_H2/Theta).`                   (5.8)

The function `g_Delta` is strictly decreasing on `(0,infinity)`, with its continuous value `Delta` at zero. Since `M_H2<M_rearr`,

`boxed: eta_H2>eta_rearr.`                                    (5.9)

This is strict endpoint progress without changing H1, H2, H3, the connected-core construction, the absorption reserve, or the old-anchor floor.

### A stronger direct H2 quantile was also tested, but not counted as movement

For completeness, fix an outside `alpha n`-set `B` and average H2 over uniform `alpha n`-subsets `A` of `W`. This gives

`e(W,B) >= (a_P/alpha) kappa lambda n-o(lambda n)`,            (5.10)

so all but fewer than `alpha n` outside vertices have degree into `W` at least approximately

`(a_P kappa/alpha^2)lambda`.                                   (5.11)

This produces a clean one-shot absorption bound. I do **not** promote it as the new metric because comparing that one-shot bound to the entire inherited multi-anchor/Stieltjes envelope is not uniformly monotone over all frozen parameters. The internal-energy route above is retained because it strictly improves the exact same correction term already used by `G_rearr`, so there is no comparison gap or double counting.

## 6. Finite connected core and finite sprinkling: the gain survives the actual proof

The endpoint argument is implemented through actual connected cores of density

`a_3=c_3 a_P`, `c_3<1`, `c_3->1`,

and a finite reserved sprinkling rate `r<Delta`, `r->Delta`.

For `c_3` sufficiently close to one, `a_3>2alpha`, so Lemma 1 applies **conditioned on the realized core**, because H2 is a deterministic property of the host graph and holds for every pair of subsets. It gives

`(1/n lambda^2) sum_{v notin W_3}d_{W_3}(v)^2`
` <= a_3-kappa^2 a_3^3/alpha^4+o(1)`.                         (6.1)

The finite-core prefix theorem from the existing R16 chain gives

`int_0^{b_0}x_3(q)dq >= c_3 b_0 t_0-o(1)`,                    (6.2)

and monotonicity of the sorted profile gives

`x_3(q)>=c_3t_0-o(1)` on `[b_0,u_3]`,                          (6.3)

where `u_3=1-a_3`. Therefore the finite prefix energy is at most

`a_3-kappa^2a_3^3/alpha^4-(u_3-b_0)c_3^2t_0^2+o(1)`,          (6.4)

which converges exactly to `A_H2`.

The same finite Stieltjes partitions and old-anchor approximations used in the incoming report converge to `V_0`, `Theta`, and the endpoint weight `v`. No new independence hypothesis is introduced. Consequently the finite weighted correction can be made arbitrarily close to `eta_H2`.

Choose `c_3`, `r`, the finite Stieltjes partition, and the inherited anchor/floor approximations sufficiently close to their endpoint values that the new correction is at least `eta_H2/2`, and then make all remaining connected-core trimming and concentration losses smaller than `eta_H2/4`. A safe frozen increment is therefore

`boxed: delta_H2:=eta_H2/4>0.`                                (6.5)

Since (5.9) is strict,

`boxed: delta_H2>delta_rearr.`                                (6.6)

## 7. New complete envelope and fixed-metric comparison

The H2 internal-energy correction replaces the incoming Stieltjes weighted correction; it is **not** added on top of the same absorption events. The inherited constant-weight prefix/tail term `E_rfgap` and core term `G_coreavg` remain unchanged.

Define

`boxed: E_H2:=E_rfgap+delta_H2`,                              (7.1)

and

`boxed: G_H2energy:=min{1,G_coreavg+E_H2}.`                   (7.2)

Then every fixed

`g<G_H2energy`                                                  (7.3)

satisfies

`boxed: P(L_1(G_p)>=g n)->1`                                 (7.4)

uniformly on the unchanged H1--H2--H3 class for every

`p>=(1+epsilon)/lambda(G)`.                                   (7.5)

Because `delta_H2>delta_rearr`,

`G_H2energy>=G_rearr`,                                         (7.6)

and whenever the incoming metric is not already saturated,

`boxed: G_rearr<1  ==>  G_H2energy>G_rearr.`                  (7.7)

For every nonsaturated frozen parameter triple, an explicit coefficient outside the whole incoming envelope is

`boxed: g_receipt:=G_rearr`
` +(1/2)min{delta_H2-delta_rearr,1-G_rearr}.`                  (7.8)

Then

`G_rearr<g_receipt<G_H2energy`.                                (7.9)

If `G_rearr=1`, the giant-fraction metric is already at its absolute ceiling and cannot move numerically above one; this is saturation, not stagnation. No endpoint attainment is claimed.

## 8. Why this is a genuinely different route

The incoming report improved the weighted second moment by exploiting the **ordering** of outside degrees. This run changes a different part of the proof: it proves that H2 consumes a fixed amount of the operator-norm energy **inside the connected core itself**.

The chain of implications is

`H2 on all alpha-by-alpha pairs inside W`
` -> exact random-pair double count of e(W)`
` -> Cauchy lower bound for sum_{W}d_W^2`
` -> subtract from ||A 1_W||_2^2`
` -> strictly smaller outside L2 budget`
` -> strictly stronger exact weighted absorption moment.`

Thus it is not another scalar threshold tweak and not another checker for an unchanged quantity.

## 9. Prior-art boundary

I searched, in addition to the current source checks, combinations of

- `pair expansion / internal edges / spectral norm / Cauchy / percolation`,
- `every two disjoint subsets / edges lower bound / averaging`,
- `sum squared degrees / subset / spectral radius / graph`, and
- `macroscopic pair expansion / percolation / spectral radius`.

The bounded search surfaced standard expander-mixing material and dense-base-graph percolation/Hamiltonicity results using pair-expansion hypotheses, but not the exact deterministic implication (4.1)--(4.2) coupled to the CMW threshold proof. **The random-pair double count, Cauchy--Schwarz, operator-norm bound, and rearrangement inequality are classical/folklore ingredients and are not claimed as new.** The only research claim here is that, on the already-frozen H0002 class and within the established R16 proof chain, retaining this previously unused consequence of H2 strictly improves the complete quantitative giant-fraction envelope. A bounded negative search is not a novelty certificate.

## 10. Status, stuck counter, and next obstruction

H0002 remains **PARTIAL / source OPEN-looking / ACTIVE**. The source asks for natural conditions in general; R16 has a stronger sufficient-condition theorem on one fixed H1--H2--H3 class, not a classification and not closure of Question 5.1.

The supported unchanged count remains **0** because the quantitative envelope moved this run. The HARD stuck protocol is therefore not triggered.

The remaining analytic obstruction is still the full isotonic obstacle problem, but its energy constraint has now changed to the stronger H2-depleted budget. A genuinely new next route would optimize

`int (1-exp(-Delta x(q)))dq`

under all prefix constraints, monotonicity, and

`int x(q)^2dq <= a_P-chi_P`,

rather than adding another scalar floor. An extreme-point/KKT theorem for that strengthened problem could subsume the current threshold-by-threshold refinements.

No exact-arithmetic checker was manufactured because the new claim is an analytic theorem with a closed-form finite counting identity and no finite-enumeration core.

## 11. Model, scheduler controls, and permission boundary

The runtime identifies the model as GPT-5.6 Sol; reasoning effort is not authenticated, so it is reported as UNVERIFIED. The exposed task-control interface still provides prompt/title, schedule/start, timing mode and enablement, but no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt. GPT-6/maximum therefore remains prompt-only. Enforcing it would require platform-level model/reasoning fields plus per-run attestation.

No scheduler modification was attempted because the controlling owner instruction forbids scheduler changes in research runs. The current repository ledger records that P26's historical `You cannot modify this task` denial was authorization-context-specific and that a later P26 update succeeded from an authorized context. If a task still rejects modification, the compliant route is the owning authorized workspace/account or platform support; no duplicate task or permission bypass is legitimate.

No email, Drive, public posting, purchase, permission change, workflow execution, or peer-file edit was made.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_source: Beck-Fiala_1981
  nominal_metric: complete_uniform_B(t,n)
  nominal_before: "B(t,n) < 3*sqrt(2*pi*t) for every integer t>=1, all n (Guo-Fang-Lu v1 current-preprint baseline)"
  nominal_after: "same KNOWN current-preprint baseline"
  nominal_movement: NONE_SOURCE_KNOWN
  metric_name: g_twoaxis_complete_envelope
  before: "G_rearr = min(1, G_coreavg + E_rfgap + delta_rearr)"
  after: "G_H2energy = min(1, G_coreavg + E_rfgap + delta_H2)"
  new_constants:
    chi_P: "kappa^2*a_P^3/alpha^4"
    A_H2: "a_P-chi_P-(u_P-b_0)*t_0^2"
    M_H2: "(V_0/b_0)*A_H2"
    eta_H2: "Theta*g_Delta(M_H2/Theta)"
    delta_H2: "eta_H2/4"
  comparison: "M_H2 = M_rearr-(V_0/b_0)*chi_P < M_rearr; eta_H2>eta_rearr; delta_H2>delta_rearr; G_H2energy>=G_rearr, strict if G_rearr<1"
  movement: STRICT_POINTWISE_ON_NONSATURATED_TRIPLES
  status: PARTIAL
  supported_unchanged_count: 0
  methods: [25, 3, 26]
  method_history_note: "all 30 moves already appeared in recovered H0002 history; these are nonconsecutive reuses, preceding triple [1,20,24]"
  finite_checker: NOT_APPLICABLE_ANALYTIC
  checker_reason: "closed-form double-counting identity; no finite enumeration claim"
  next_obstruction: "full isotonic/KKT optimization with all prefix constraints and H2-depleted L2 budget"
```
