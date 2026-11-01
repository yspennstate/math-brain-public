Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala `B(t,n)` metric remains a KNOWN current-literature baseline on the stated September 2026 Komlos preprints, while the active R16/H0002 successor moves strictly from the complete envelope `G_core=a1+Phi(d_core-d1)` to `G_split=a1+Phi(d_split-d1)>G_core` on the unchanged H1--H2--H3 class. Section-B methods actually used: **#1 CHANGE THE CATEGORY, #24 FIND THE EXTREMAL OBJECT, #26 HUNT THE SPORADIC CASE**. All 30 Section-B moves were already exhausted on H0002, so these are honest nonconsecutive reuses; the preceding triple was #5/#15/#20.

# R16 — H0002: split the complement before compressing

## 1. Continuity, ownership, required reads, and current-source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The active source is Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: identify natural graph hypotheses under which `p >= (1+epsilon)/lambda(G)` forces a component of order `Omega(|G|)` with constant probability.

Before new mathematics I reconciled the current repository state rather than restarting: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H0002 source row in `probability_1000_intake_H_20260914/problems.jsonl`, the newest own report `runs/R16/2026-09-19T03-44-45Z_h0002-full-complement-core-profile_c7a4.md`, and the current repository search for same-source neighboring work. The same-source neighbors recovered in the prior R16 chain have already rotated or handed off; no current peer ownership conflict with the R16-exclusive H0002 claim was found.

A fresh bounded web check still recovered CMW as arXiv:2608.19145v1 and did not surface a later source-matching resolution of Question 5.1. This is negative search evidence only, not a worldwide openness or novelty certificate.

The nominal Beck--Fiala scheduler title remains stale as an unresolved existence target. Current primary-source comparison is unchanged in substance:

- Bansal--Jiang, arXiv:2508.03961v2, obtain the conjectured `O(sqrt(t))` order directly for `t >= log^2 n`, with a weaker polylogarithmic loss below that regime.
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce

  `B(t,n) < 3 sqrt(2 pi t)`

  for every integer `t>=1` and every `n`.
- Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), independently give an elementary Komlos proof with universal constant `36`.

These are extremely recent manuscripts / technical reports, not mature refereed consensus. On their stated theorems, however, the fixed Beck--Fiala existence metric is already uniformly `O(sqrt(t))` for all `t,n`; R16 therefore does not relabel that literature theorem as fleet progress and continues the already-admitted H0002 successor.

Current links checked:

- https://arxiv.org/abs/2608.19145
- https://arxiv.org/abs/2508.03961
- https://arxiv.org/abs/2609.11189
- https://eccc.weizmann.ac.il/report/2026/188/

## 2. Frozen H0002 class and incoming strongest complete bound

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n=|G|`, `lambda=lambda(G)`,

`h:=1-epsilon/8`,

`q0:=1-exp(-epsilon^2/288)`,

`alpha:=rho*q0/64`.

The hypothesis class is unchanged:

1. H1: `lambda(G-S) >= h lambda` whenever `|S|<=rho n`;
2. H2: `e_G(X,Y) >= kappa lambda n` for all disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. H3: `lambda -> infinity`.

As before, nonvacuity forces `0<rho<1`; put

`s:=1-rho>0`.

The tracked quantity remains `g_twoaxis(epsilon,rho,kappa)`, the largest explicit uniform giant fraction proved for this exact class at every `p >= (1+epsilon)/lambda`.

Preserve the preceding notation

`a(d):=rho-alpha+d`,

`b(d):=alpha-d`,

`c(d):=1-a(d)=s+b(d)`,

`K(d):=a(d)*kappa/alpha`,

and

`Xi(d):=kappa*a(d)*c(d)/alpha^2` if `c(d)>=alpha`,

`Xi(d):=a(d)*kappa/alpha-(alpha-c(d))` if `c(d)<alpha`.

The full H1 complement-core report proved

`q_C:=2e(C)/(lambda*c*n) >= h*b/c-o(1)`

for the complement `C=V\A`. Its resulting two-block profile is

`F_core(d):=K(d)-d
  + d*Xi(d)^2/[a(d)*(c(d)-h*b(d))].`

It defined the first positive-profile endpoint `d_core`, proved

`d_core<alpha`, `Xi(d_core)>0`, `F_core(d_core)=0`,

and obtained the complete incoming envelope

`G_core:=a1+Phi(d_core-d1)`.

Here `d1`, `a1`, and the strictly increasing `Phi` are the frozen quantities from the preceding chain:

`beta:=alpha-d1`, `a1:=rho-beta`,

`Rhat:=1-exp[-Delta*Fhat1/beta] in (0,1)`,

`Delta:=epsilon*(7-epsilon)/(8-epsilon)`,

`Phi(D):=Rhat*s+D*(1-Rhat)` for `0<=D<=s`,

`Phi(D):=D` for `D>=s`.

Every fixed `g<G_core` was already proved with probability tending to one. This is the strongest complete incoming result, not merely the last displayed receipt.

## 3. Method #1 — change category: from a two-block cut estimate to a split-complement spectral feasibility problem

The previous profile compresses the partition only as

`A | C`, where `C=B union R`.

For the actual seed quotient failure, however, there are three canonical pieces:

- `A`: the large seed side, density `a=a(d)`;
- `B`: the deficient seed side, density `b=b(d)=alpha-d`;
- `R`: the untouched reservoir, density `s=1-rho`.

Thus `C=B union R` has density `c=b+s`.

Write the normalized host edge masses

`x:=e(A,B)/(lambda n)`,

`z:=e(A,R)/(lambda n)`,

`t:=x+z=e(A,C)/(lambda n)`,

and the internal normalized Rayleigh quantities

`q_A:=2e(A)/(lambda a n)`,

`q_R:=2e(R)/(lambda s n)`.

Every actual quotient cut satisfies the following four necessary inequalities, up to uniform `o(1)` errors from rounding / harvested mass.

### (i) One-sided padding

Pad `B` by `d n` vertices chosen from `A`, and average H2 over the disjoint `alpha n` test block in the remainder of `A`. Exactly as in the earlier one-sided-padding proof,

`x+d*q_A >= K(d)-o(1).`

### (ii) Full-complement H2

The density-amplified H2 calculation gives

`t >= Xi(d)-o(1).`

### (iii) Aggregate `A | C` spectral compression with the full H1 core

The normalized two-block compression of `Adj(G)/lambda` to the indicators of `A,C` gives

`(1-q_A)(1-q_C) >= t^2/(a*c)`.

Since H1 gives `q_C>=h*b/c-o(1)`,

`q_A <= 1 - t^2/[a*(c-h*b)] + o(1).`

This is the inequality that generated `F_core`.

### (iv) The forgotten principal `A | R` compression

Compress instead to the indicators of `A,R`. Its matrix is

`[[q_A, z/sqrt(a*s)], [z/sqrt(a*s), q_R]].`

Since the ambient top eigenvalue is `lambda`, `I-Q_AR` is positive semidefinite, hence

`(1-q_A)(1-q_R) >= z^2/(a*s).`

Because `q_R>=0`, we obtain the simpler universal necessary inequality

`boxed: q_A <= 1-z^2/(a*s).`

This inequality costs no new hypothesis. It was lost only because the preceding argument merged `B` and `R` before compressing.

## 4. A strictly stronger one-dimensional cut-capacity profile

The two spectral inequalities can be combined before using the padding inequality.

From `t=x+z>=Xi`,

`z >= (Xi-x)_+`.

Therefore every actual cut satisfies

`q_A <= 1 - max{
    Xi(d)^2/[a(d)*(c(d)-h*b(d))],
    (Xi(d)-x)_+^2/[a(d)*s]
  } + o(1).`

Insert this into the one-sided padding inequality `x+d q_A>=K`. Define

`A0(d):=Xi(d)^2/[a(d)*(c(d)-h*b(d))]`

and the scalar obstacle function

`Psi_d(x):=K(d)-d
 + d*max{ A0(d), (Xi(d)-x)_+^2/[a(d)*s] } - x.`

Then every actual cut must satisfy, asymptotically,

`Psi_d(x) <= o(1).`

Equivalently, ignoring only the vanishing finite-`n` error, its normalized crossing mass is at least

`F_split(d):=inf{x>=0 : Psi_d(x)<=0}.`

This is a one-dimensional, explicit semialgebraic profile. It is not an SDP black box.

The old profile is exactly

`F_core(d)=K(d)-d+d*A0(d).`

The second spectral term becomes equal to the old aggregate term at the positive threshold

`L(d):=Xi(d)*[1-sqrt{s/(c(d)-h*b(d))}].`

Because `b(d)>0` for every `d<alpha` and `h<1`,

`c-hb = s+(1-h)b > s`,

so whenever `Xi(d)>0`,

`boxed: L(d)>0.`

On the interval `x<L(d)`, the split `A|R` term strictly dominates the aggregate term, and `Psi_d(x)=0` becomes the explicit quadratic

`x = K(d)-d + d*(Xi(d)-x)^2/[a(d)*s].`

If `F_core(d)<L(d)` and the continuation is in the positive regime, `F_split(d)` is the unique root in `(max{0,F_core(d)},L(d))`. Writing

`Astar(d):=d/[a(d)*s]`,

that root has the closed form

`r(d) = [1+2*Astar*Xi
         - sqrt(1+4*Astar*(Xi-K+d))]
        /(2*Astar)`

whenever this branch is active. At the transition `F_core=L`, the two descriptions meet continuously.

Thus the new object is still just a one-variable piecewise algebraic function.

## 5. Method #24 — the old zero-capacity extremizer is impossible after the split

Let

`dc:=d_core`,

`ac:=a(dc)`, `bc:=b(dc)`, `cc:=c(dc)`,

`Xic:=Xi(dc)`, `Kc:=K(dc)`.

The preceding report proved

`dc<alpha`, `bc>0`, `Xic>0`,

and

`F_core(dc)=Kc-dc
 + dc*Xic^2/[ac*(cc-h*bc)] = 0.`

Evaluate the new obstacle at `x=0`. Since

`cc-h*bc=s+(1-h)bc>s`,

we have

`Xic^2/(ac*s)
 > Xic^2/[ac*(cc-h*bc)].`

Therefore

`Psi_dc(0)
 = Kc-dc + dc*Xic^2/(ac*s)`

`= dc*Xic^2/ac
   *[1/s - 1/(cc-h*bc)]`

`= dc*Xic^2*(1-h)*bc
   /[ac*s*(cc-h*bc)]`

`>0.`

Call this explicit positive gap

`M_split:=dc*Xic^2*(1-h)*bc
         /[ac*s*(cc-h*bc)] > 0.`

Hence

`boxed: F_split(dc)>0.`

This is the crucial strict movement statement: the point where the merged-complement profile had zero crossing capacity still has a positive crossing capacity once the reservoir is kept as a separate spectral block.

There is also a direct extremal interpretation. If one tries to realize `x=0` at the old root, the one-sided padding inequality forces

`q_A >= Kc/dc`.

The aggregate `A|C` compression plus `t=z>=Xic` forces the opposite inequality

`q_A <= 1-Xic^2/[ac*(cc-h*bc)] = Kc/dc`,

so all of these inequalities must be equalities and necessarily `z=Xic`. But the principal `A|R` compression then gives

`q_A <= 1-Xic^2/(ac*s)
     < 1-Xic^2/[ac*(cc-h*bc)]
     = Kc/dc`,

a contradiction.

Thus the old zero-capacity extremizer does not exist even at the level of the three-block quotient compression.

## 6. Method #26 — hunt the apparent knife-edge; there is no `d=s` exception

The mixed-padding calculation in the preceding report suggested a possible knife-edge when the deficit `d` exactly equals the reservoir density `s`: scalar padding identities can then collapse to equality.

The split-compression proof above shows that this apparent sporadic case is not a genuine obstruction. Nothing in the strict inequality

`cc-h*bc = s+(1-h)bc > s`

depends on the sign of `dc-s`. It uses only

`bc=alpha-dc>0`, `s>0`, and `1-h=epsilon/8>0`.

Therefore the positive gap `M_split` persists when `dc=s` just as it does for `dc<s` or `dc>s`. The sporadic scalar degeneracy is eliminated by the `A|R` principal minor.

This is useful route information: a full three-by-three determinant is not yet needed. The first genuinely new correlation already appears in one principal minor after refusing to merge `B` with `R`.

## 7. The positive-profile endpoint moves strictly to the right

The function `Psi_d(x)` is continuous jointly in `(d,x)` on every compact subinterval of `[d1,alpha)`, including across the branch `c=alpha`, because `Xi` is continuous there. At `d=dc`, `Psi_dc(0)=M_split>0`.

Hence there exist fixed `eta>0` and `delta>0` such that

`Psi_d(x)>0`

whenever

`dc <= d <= dc+delta`, `0<=x<=eta`.

No actual cut in this parameter range can therefore have normalized crossing mass below `eta+o(1)`.

Define the exact new continuation endpoint

`d_split:=sup{d in [d1,alpha):
  Xi(u)>0 and F_split(u)>0 for every u in [d1,d]}`.

For `u<dc`, the old profile already had positive capacity and `F_split>=F_core`. The strict positive gap at `dc` plus continuity gives

`boxed: d_split>d_core.`

The new endpoint is still an ordinary one-dimensional algebraic/semialgebraic obstruction. As `d->alpha-`, `b->0`, so

`c-hb -> s`

and the split and aggregate spectral denominators coalesce. Thus the new correction vanishes at the boundary and the negative boundary behavior established for `F_core` is recovered. In particular the continuation does not gain by redefining infinity; its movement comes from a genuine interior spectral gap.

## 8. Propagation to the complete giant-fraction metric

Fix any `d<d_split`. By compactness of the interval `[d1,d]`, the new scalar profile has a positive minimum after choosing the usual finite-`n` slack. Thus every relevant macroscopic quotient cut has

`e(A,B) >= c_d*lambda*n`

for some fixed `c_d>0` depending only on the frozen parameters and `d`.

The already-proved two-scale harvesting theorem still gives genuine first-round seed components of total mass `(rho-o(1))n`, with only

`O(n/lambda^(2/3))`

seed components. The independent gluing round at probability `lambda^(-4/3)` leaves any one positive-capacity cut unglued with probability

`exp[-Theta(n/lambda^(1/3))]`,

whereas the number of quotient cuts is only

`exp[O(n/lambda^(2/3))]`.

The union bound therefore tends to zero. Round two yields a connected seed component of normalized size at least

`rho-alpha+d-o(1)`.

The fixed-anchor absorption theorem is unchanged. Put

`D_split:=d_split-d1`

and define

`boxed: G_split:=a1+Phi(D_split).`

The incoming strongest complete bound was

`G_core=a1+Phi(d_core-d1)`.

Since `Phi` is strictly increasing and `d_split>d_core`,

`boxed: G_split>G_core.`

Consequently every fixed

`g<G_split`

satisfies

`boxed: P(L1(G_p)>=g*n)->1`

uniformly on the unchanged H1--H2--H3 class for every

`p>=(1+epsilon)/lambda(G)`.

No endpoint attainment is claimed.

A single frozen receipt strictly beyond the entire incoming envelope is

`boxed: g_receipt:=(G_core+G_split)/2.`

Thus the supported unchanged count remains zero.

## 9. What this route did and did not prove

This is a source-valid PARTIAL theorem for CMW Question 5.1 on exactly the already-frozen H1--H2--H3 class. It does not classify all natural graph conditions and does not close the open-ended source question.

The new mechanism is also narrower than a generic claim that `3x3 PSD` solves the problem. The exact gain comes from retaining the untouched reservoir as a separate block and intersecting two necessary spectral caps on `q_A`:

1. the aggregate `A|C` cap, strengthened by the H1 complement core;
2. the principal `A|R` cap.

The old root saturates the first cap and therefore cannot also satisfy the strictly stronger second cap when all cross mass is forced out of the deficient seed side.

A bounded prior-art search did not locate this exact split-compression feedback in the CMW source or the immediate finite-graph percolation search results. The mechanisms themselves—Rayleigh compression, principal minors, sprinkling—are standard and are not claimed as novel in isolation. Negative search evidence is not a novelty certificate.

The next genuinely different obstruction is now the first zero of `F_split`. If that route stalls, the next useful step is a full `(A,B,R)` determinant / Schur-complement optimization retaining `q_B,q_R,e(B,R)` jointly, rather than another scalar slack optimization.

## 10. Beck--Fiala current comparison

The native title remains historically meaningful but no longer represents an unresolved existence theorem on the current primary sources. Bansal--Jiang's direct result covers the conjectured scale only for `t>=log^2 n`. Guo--Fang--Lu's 10 Sep 2026 arXiv manuscript states the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly yields

`B(t,n)<3 sqrt(2 pi t)`

for every integer `t>=1`, all `n`, with no logarithmic restriction. Karingula--Lovett's 17 Sep ECCC report independently gives Komlos constant `36` and explicitly describes itself as simplifying the recent Guo--Fang--Lu proof.

Accordingly, R16 labels the nominal Beck--Fiala existence target **KNOWN current-literature baseline**, not a new R16 proof. The active mathematical movement in this report is H0002 only.

## 11. Model / scheduler control check

The model-control limitation is still unchanged. The exposed task controls available in this environment include task prompt/title, schedule or relative start, timing mode, and enablement. They expose **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt**. Therefore `GPT-6 / maximum` remains prompt text only; this run actually used GPT-5.6 Sol and the reasoning level is UNVERIFIED.

Actually enforcing the requested configuration would require scheduler/API fields for model family and reasoning effort plus per-run runtime attestation. The historical P26 `You cannot modify this task` denial was authorization-context-specific; root `RESULTS.md` records that the P26 full update later succeeded from an authorized context. If such a denial recurs, the compliant workaround is the owning authorized workspace/account context or platform support, never task duplication or permission bypass.

No scheduler was modified in this run.

## 12. Run disposition

- target: H0002 / CMW Question 5.1;
- lane: HARD OUTSIDE;
- source status: OPEN-LOOKING in bounded current search;
- frozen class: unchanged H1--H2--H3;
- metric before: every fixed `g<G_core=a1+Phi(d_core-d1)`;
- metric after: every fixed `g<G_split=a1+Phi(d_split-d1)` with `d_split>d_core`;
- movement: **YES, strict**;
- concrete receipt: `g_receipt=(G_core+G_split)/2`;
- supported unchanged count: `0`;
- stuck recovery: `false`;
- finite checker: none, because the new theorem is analytic and has no finite computational core;
- peer/shared files modified: none;
- email/Drive/public posting/workflow/permission/scheduler actions: none.

```yaml
ledger_delta:
  track: R16
  canonical_target: H0002
  source: "Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.1"
  lane: HARD_OUTSIDE
  status_before: "PARTIAL / SOURCE OPEN-LOOKING / ACTIVE"
  status_after: "PARTIAL / SOURCE OPEN-LOOKING / ACTIVE"
  frozen_metric: "g_twoaxis(epsilon,rho,kappa) on unchanged H1-H2-H3"
  before: "every fixed g < G_core = a1 + Phi(d_core-d1)"
  after: "every fixed g < G_split = a1 + Phi(d_split-d1), where d_split>d_core"
  new_profile: "F_split(d)=inf{x>=0: K-d+d*max(Xi^2/[a(c-hb)],(Xi-x)_+^2/(a s))-x<=0}"
  old_root_gap: "M_split=d_core*Xi_core^2*(1-h)*b_core/[a_core*s*(c_core-h*b_core)] > 0"
  strict_root_gain: "d_split>d_core"
  concrete_receipt: "g_receipt=(G_core+G_split)/2"
  movement: true
  supported_unchanged_count: 0
  methods: [1, 24, 26]
  method_outcomes:
    B1: "SUCCESS: retain A,B,R separately; principal A|R compression adds a new spectral cap missed by A|C aggregation"
    B24: "SUCCESS: the old zero-capacity extremizer saturates A|C and is incompatible with the A|R principal minor"
    B26: "SUCCESS: the apparent d=s scalar knife-edge is not an exception because c-hb>s whenever b>0 and epsilon>0"
  stuck_recovery: false
  nominal_beck_fiala_status: "KNOWN current-literature baseline on stated Sep-2026 Komlos manuscripts"
  nominal_uniform_bound: "B(t,n) < 3 sqrt(2 pi t) for every integer t>=1 and all n, per Guo-Fang-Lu arXiv:2609.11189v1"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  model_selector_exposed: false
  reasoning_selector_exposed: false
```
