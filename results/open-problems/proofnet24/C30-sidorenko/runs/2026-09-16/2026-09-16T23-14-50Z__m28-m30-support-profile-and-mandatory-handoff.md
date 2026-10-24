Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **NO MOVEMENT — C30 frozen metric `10 -> 10`; raw unchanged-run count `6 -> 7`. This is the ordinary research run selected by STUCK RECOVERY 2, using B8, B11, B16. It proves the new PARTIAL theorem `C30-N11-M28-M30-SUPPORT-PROFILE-03`, but because the frozen complete-order metric still does not move after both permitted hard-target recoveries, C30 now executes the mandatory same-target switch/handoff. No STUCK RECOVERY 3 is created.**

# C30 — exact support-profile dual certifies n=11 densities 28, 29, 30; mandatory hard-target handoff

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C30-sidorenko`.
Frozen graph: `H=K_{5,5}\setminus C_{10}`, ten vertices, fifteen edges.
Frozen metric: largest host order `n` for which **every** finite simple host on at most `n` vertices is verified for the source Sidorenko inequality by complete exact evidence.
Status: **PARTIAL / HARD HANDOFF**. The universal source conjecture is not claimed proved.

## 1. Continuity and preserved baseline

I continued from

`proofnet24/C30-sidorenko/runs/2026-09-16/2026-09-16T21-50-52Z__stuck-recovery-2.md`.

That report is STUCK RECOVERY 2/2 and selected exactly one ordinary-research route: discretize the support-profile obstruction, dualize it, and only then exact-check the resulting finite profile cases. I did not restart the earlier symmetry/operator route and did not launch another raw graph enumeration.

The complete finite baseline is preserved exactly:

- `U_7=1044`, `U_8=12346`, `U_9=274668`, `U_10=12005168`;
- all `12,005,168` unlabeled ten-vertex hosts were checked with integer arithmetic and zero violations;
- `K_10` is the finite normalized minimizer at order ten, with `hom(H,K_10)=2073451770`;
- the exact n=10 output ends `ALL_EXACT_CHECKS_PASS`;
- `C30-N11-M27-STRUCTURAL-02 = PROVED` remains intact;
- the preceding whole-image collision result covers the order-eleven densities through `m<=26`.

Thus before this run the largest **complete host order** is 10, not the stale compact-ledger value 7, 8, or 9.

The historical AF4.49(ii) service audit also remains untouched:

- `C30-AUDIT-C31-AF449-RAMANUJAN-CONE-01 = PASS`;
- `P26-AUDIT-C31-AF449-DIRECT-DUALITY-02 = PASS`.

They are two distinct claim-scoped audits of the no-universal-`K` source theorem. They do not certify all auxiliary claims in the larger flow-parameter paper, and this run does not request another receipt-only reconciliation.

## 2. Source and current-literature gate — checked 2026-09-17 local / 2026-09-16 UTC

The target remains the exact Sidorenko inequality

\[
\operatorname{hom}(H,G)|V(G)|^{20}\ge (2|E(G)|)^{15}
\tag{2.1}
\]

for `H=K_{5,5}\setminus C_{10}` and every finite simple host `G`.

Fresh bounded queries included:

1. `Yuqi Zhao Conjugacy Class Averages Sidorenko K5,5 C10 arXiv 2606.15368`;
2. `"K_{5,5}" "C_{10}" Sidorenko 2026`;
3. `"K_{5,5}\\setminus C_{10}" Sidorenko`;
4. `Zhao Tensor Amplification Spectral Transfer Sidorenko arXiv 2607.02260`.

The refresh recovered Zhao's June 13, 2026 conjugacy-averaging paper and July 2, 2026 tensor/spectral-transfer paper, neither of which supplies a proof of this fixed graph. Lee--Schülke still identify this graph as the notorious open example and prove it is not weakly norming. Conlon--Lee prove a blow-up/square, not the original graph. Szegedy proves the related determinant/GMRF inequality for the Möbius ladder without establishing Sidorenko. No later source-exact resolution was found in the bounded search. This is dated search evidence only, not a novelty certificate or proof of worldwide openness.

## 3. B8 — discretize the obstruction into support profiles, not hosts

Write

\[
C(a,b,c)=|N(a)\cap N(b)\cap N(c)|.
\]

With the five left vertices of `H` cyclically indexed, the exact homomorphism identity is

\[
\operatorname{hom}(H,G)
=
\sum_{x_0,\ldots,x_4\in V(G)}
\prod_{i\in\mathbb Z/5\mathbb Z}
C(x_i,x_{i+1},x_{i+2}).
\tag{3.1}
\]

Every summand is nonnegative. Group the five-tuples by the size of their image.

For a vertex `v` of degree `d_v`, support one contributes exactly

\[
A_1=\sum_v d_v^5.
\tag{3.2}
\]

For an unordered pair `{a,b}` with codegree `c=c(a,b)`, the already-proved exact binary-word calculation gives

\[
P_2(d_a,d_b,c)
=
10c^5+5(d_a+d_b)c^4+5(d_a^2+d_b^2)c^3.
\tag{3.3}
\]

For a three-set `S={a,b,c}`, put `t=c(S)`. Among the 150 surjective cyclic words of length five on three symbols, exactly 120 have no monochromatic three-window, and exactly 30 have one such window, ten for each symbol. Hence, if the host minimum degree is at least four and `q=max{4,t}`,

\[
P_3(S)\ge120t^5+30qt^4.
\tag{3.4}
\]

The exact integer minorant

\[
120t^5+30qt^4
\ge
240t+5280\binom t2
\qquad(t\ge0)
\tag{3.5}
\]

holds for every possible integer `t`. Summing and double-counting `K_{3,2}` gives

\[
\sum_{|S|=3}t_S=\sum_v\binom{d_v}{3}=:T_3,
\qquad
\sum_{|S|=3}\binom{t_S}{2}
=
\sum_{a<b}\binom{c(a,b)}3.
\tag{3.6}
\]

For support four there are 240 surjective words, and every three-window common neighborhood contains the common neighborhood of all four support vertices. Since `u^5>=u` for integer `u>=0`, the total support-four contribution is at least

\[
240T_4,
\qquad T_4:=\sum_v\binom{d_v}{4}.
\tag{3.7}
\]

Likewise the 120 permutations on five symbols give support-five contribution at least

\[
120T_5,
\qquad T_5:=\sum_v\binom{d_v}{5}.
\tag{3.8}
\]

Therefore every eleven-vertex host with minimum degree at least four satisfies

\[
\operatorname{hom}(H,G)
\ge
\sum_vd_v^5+240T_3+240T_4+120T_5
+
\sum_{a<b}W(d_a,d_b,c_{ab}),
\tag{3.9}
\]

where

\[
W(d,e,c):=P_2(d,e,c)+5280\binom c3.
\tag{3.10}
\]

This is the finite state space used below. It retains degree and codegree compatibility rather than independently minimizing unrelated support marginals.

## 4. B11 — an exact universal dual certificate

The finite profile optimization has a particularly compact dual. Set

\[
D=19,
\qquad M=309420,
\qquad L_6=9020,
\qquad L_d=0\ (d\ne6).
\tag{4.1}
\]

For `4<=d<=e<=10`, define the integer coefficients `A_{de}` by the triangular table

| `d\e` | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|
|4|-638130|-607350|-598500|-546640|-533720|-519280|-503320|
|5| | -576570|-567720|-538280|-525360|-510920|-494960|
|6| | | -575880|-546440|-533520|-519080|-503120|
|7| | | | -517000|-504080|-489640|-473680|
|8| | | | | -491160|-476720|-460760|
|9| | | | | | -462280|-446320|
|10| | | | | | | -430360|

The exact pointwise inequalities are

\[
\boxed{
19W(d,e,c)
\ge
A_{de}+[M+L_d+L_e]c
}
\tag{4.2}
\]

for every integer `4<=d<=e<=10` and `0<=c<=min(d,e)`. The checker verifies every one of these inequalities exactly; the minimum slack is zero, attained for example at `(d,e,c)=(4,4,3)`.

Now let `delta` be the minimum degree. Two elementary incidence identities/inequalities are

\[
\sum_{a<b}c(a,b)=\sum_v\binom{d_v}{2}=:T_2,
\tag{4.3}
\]

and, for every vertex `a`,

\[
\sum_{b\ne a}c(a,b)
=
\sum_{y\in N(a)}(d_y-1)
\ge d_a(\delta-1).
\tag{4.4}
\]

Because all `L_d` are nonnegative, summing (4.2) over unordered pairs and using (4.3)--(4.4) yields

\[
19\sum_{a<b}W(d_a,d_b,c_{ab})
\ge
\sum_{d\le e}N_{de}A_{de}
+MT_2
+\sum_d n_dL_d\,d(\delta-1),
\tag{4.5}
\]

where `n_d` is the number of degree-`d` vertices and `N_{de}` the number of unordered vertex pairs with endpoint degree types `(d,e)`.

Thus after the dual is fixed, the remaining finite optimization is only over the nondecreasing integer degree multisets with entries in `[4,10]` and total degree `2m`; no graph enumeration remains.

## 5. B16 — exact finite check and theorem for m=28,29,30

### `C30-N11-M28-M30-SUPPORT-PROFILE-03 = PROVED (PARTIAL relative to Sidorenko)`

For every simple graph `G` on eleven vertices with

\[
|E(G)|\in\{28,29,30\},
\]

we have

\[
\boxed{
\operatorname{hom}(H,G)\,11^{20}\ge(2|E(G)|)^{15}.
}
\tag{5.1}
\]

#### Low-degree branch

If `v` has degree `d<=3`, then `G-v` has ten vertices and `m-d` edges. The complete order-ten theorem gives

\[
\operatorname{hom}(H,G)
\ge
\operatorname{hom}(H,G-v)
\ge
\frac{(2(m-d))^{15}}{10^{20}}.
\tag{5.2}
\]

For each `m=28,29,30` and every `d=0,1,2,3`, the exact cross-multiplication

\[
(m-d)^{15}11^{20}-m^{15}10^{20}>0
\tag{5.3}
\]

is verified by the checker. Hence (5.1) follows in this branch.

#### Minimum-degree-four branch

Assume `delta>=4`. Apply (3.9) and (4.5). The possible degree multisets are finite. The exact checker ranges over **all** nondecreasing integer degree multisets in `[4,10]` with the required total degree; it does not even need to assume graphicality, so every actual graph is included.

For `m=28`, 57 degree multisets are checked. The weakest dual lower bound occurs at

\[
(5,5,5,5,5,5,5,5,5,5,6)
\]

and gives

\[
\operatorname{hom}(H,G)\ge\frac{5798504}{19}.
\]

The exact source cross-margin is

\[
5798504\,11^{20}-19\,56^{15}
=727184093687848641494160360>0.
\tag{5.4}
\]

For `m=29`, 86 degree multisets are checked. The weakest is

\[
(5,5,5,5,5,5,5,5,6,6,6),
\]

with

\[
\operatorname{hom}(H,G)\ge\frac{9833572}{19}
\]

and exact margin

\[
9833572\,11^{20}-19\,58^{15}
=1243071632424315147339376164>0.
\tag{5.5}
\]

For `m=30`, 124 degree multisets are checked. The weakest is

\[
(4,5,5,5,5,6,6,6,6,6,6),
\]

with

\[
\operatorname{hom}(H,G)\ge\frac{13800600}{19}
\]

and exact margin

\[
13800600\,11^{20}-19\,60^{15}
=350838873122287662979320600>0.
\tag{5.6}
\]

This proves (5.1).

Combining the retained `m<=26` result, `C30-N11-M27-STRUCTURAL-02`, and the present theorem, **every eleven-vertex host with at most 30 edges is now certified**. This is still only a restricted order-eleven result, so it is PARTIAL and the frozen complete-order metric remains 10.

## 6. Exact artifacts

Exact checker:

`proofnet24/C30-sidorenko/artifacts/2026-09-16T23-14-50Z__check_n11_m28_m30_support_profile.py`

created at commit `5fa1bd096536e375f3ada600e79aa7abf68662b5` and read back at that commit.

Executed output:

`proofnet24/C30-sidorenko/artifacts/2026-09-16T23-14-50Z__check_n11_m28_m30_support_profile.out`

created at commit `e9d1ffc7e7855b0fec4d846b487bc2fb5878c515` and read back at that commit. It ends

`ALL_EXACT_CHECKS_PASS`.

The checker uses integer arithmetic only and verifies the cyclic-word counts, the support-three minorant, every pointwise dual inequality, all deletion comparisons, and all 57+86+124 degree-profile cases.

## 7. Why this route now stops, rather than spawning another lemma

The same exact dual certificate already fails at the next density. At `m=31`, among the 170 nondecreasing degree multisets with entries in `[4,10]` and total 62, its weakest bound occurs at

\[
(4,5,5,6,6,6,6,6,6,6,6)
\]

and is only

\[
\frac{17557328}{19}=924069.894\ldots,
\]

whereas the source right-hand side is

\[
\frac{62^{15}}{11^{20}}=1142935.281\ldots.
\]

The exact cross-difference is negative:

\[
17557328\,11^{20}-19\,62^{15}
=-2797592070997272741275078064<0.
\tag{7.1}
\]

This does **not** mean a counterexample exists. It says exactly that the present support-profile dual no longer certifies the source inequality. The missing information begins at support-four/five interactions among different triple codegrees, not at another tweak of the pair envelope.

That is the required stopping signal after two hard-target recoveries.

## 8. Mandatory hard-target switch / preserved handoff

The frozen metric is still

\[
\boxed{10\longrightarrow10}.
\]

The raw unchanged-run count moves `6 -> 7`. The hard-target recovery history is already `2/2`; therefore another same-target stuck recovery is forbidden. C30 now leaves this Sidorenko target in **HARD RESERVE / preserved handoff** rather than scheduling STUCK RECOVERY 3.

The handoff preserves:

1. complete exact host coverage through `n=10`;
2. the whole-image `n=11,m<=26` certificate;
3. `C30-N11-M27-STRUCTURAL-02`;
4. the new `C30-N11-M28-M30-SUPPORT-PROFILE-03` and exact dual/checker;
5. the exact first unsupported density `n=11,m=31`;
6. the precise next mathematical obstruction: a certificate that retains interactions among support-four/five cyclic words and the overlapping triple-codegree profile, rather than another independent marginal minimization.

I re-read the current queue/ownership surface before attempting a successor. The top apparent rows are not safely claimable from their stale queue positions alone: I0011 is in P16 admission work, I0035 is C31-owned/rotation-held, I0054 is now exclusively owned by R11, I0055 has current repository evidence of a 2020 positive answer, I0070/I0068/I0066/I0077/I0079/I0082 are owned by other tracks or otherwise dispositioned in newer reports. No source/current-status/history/ownership-complete unassigned HARD successor was established in this run. I therefore record **SUCCESSOR ADMISSION REQUIRED** and do not fabricate a canonical claim.

## 9. Directed C31 audit duty

The newest C31 report after its substantive theorem is a six-run rotation hold with no new theorem. The actual newest theorem-sized C31 claim is therefore

`C31-I0035-PAIR-RESISTANCE-05 = PROVED`

in

`proofnet24/C31-closure-kemeny/runs/2026-09-16/2026-09-16T22-08-30Z__report.md`.

I independently checked its proof and record

\[
\boxed{\texttt{C30-AUDIT-C31-I0035-PAIR-RESISTANCE-06 = PASS}}
\]

**claim-scoped**.

The proof chain is sound:

- the killed independent-set exclusion block lifts to labeled independent tuples because an attempted jump directly onto another occupied vertex cannot occur from an independent configuration;
- minimizing over the unlabeled/symmetric subspace can only raise the principal labeled Dirichlet eigenvalue;
- enlarging the labeled domain so that only labels 1 and 2 must remain distinct and nonadjacent gives Dirichlet-domain monotonicity and factors off the unrestricted remaining labels;
- swap symmetry supplies a symmetric ground state for the ordered two-particle problem, so its principal eigenvalue equals the unlabeled two-token Dirichlet eigenvalue;
- for a zero-extended pair test function, the resistance inequality
  \[
  |g_y(x)-g_y(y)|^2\le R_{xy}\sum_{\{u,v\}\in E}(g_y(u)-g_y(v))^2
  \]
  gives `||f||^2 <= 2 n R_* E_1` and the symmetric second-coordinate inequality;
- averaging the two yields
  \[
  \|f\|_2^2\le nR_*\mathcal E_{\rm pair}(f,f),
  \]
  hence
  \[
  \lambda_D^{(r)}\ge\lambda_D^{(2)}\ge\frac1{nR_*}.
  \]

The rate-`1/2` normalization is consistent: one coordinate's Dirichlet form is one half of the unoriented edge-gradient sum. This PASS covers only `C31-I0035-PAIR-RESISTANCE-05`; it does not certify Aldous--Fill 14.31, C31's saturated comparison metric, or any retired AF4.49(ii) paper extras.

## 10. Model/scheduler control

The exposed task interface still provides task title/prompt, schedule/timing, enabled state, timing mode, and notification behavior. It exposes **no model-family selector and no reasoning-effort selector**, and no authenticated applied-runtime telemetry. GPT-6/maximum therefore remains prompt-only. Making it enforceable requires scheduler/backend or authorized enclosing-runtime support that exposes, persists, and reports those settings.

The historical P26 `You cannot modify this task` event was a permission-context boundary; later repository state records a successful authorized P26 edit. The supported workaround remains owner/admin/coordinator action in the owning authorized workspace, or platform support if that context is defective. No permission bypass or duplicate task is appropriate.

## 11. Ledger delta for P26

```yaml
ledger_delta:
  track: C30
  target: "Sidorenko H=K_{5,5}\\setminus C_{10}"
  status: "PARTIAL / HARD HANDOFF; same-target research rotated out after 2/2 stuck recoveries"
  frozen_metric: "largest host order n completely verified for every simple host"
  metric_before: 10
  metric_after: 10
  movement: "NO MOVEMENT"
  raw_unchanged_run_count: 7
  methods_tried: [8, 11, 16]
  new_claim: "C30-N11-M28-M30-SUPPORT-PROFILE-03 = PROVED (PARTIAL)"
  new_coverage: "all n=11 hosts with m<=30 are now certified, combining retained m<=26, m=27, and new m=28,29,30 results"
  first_unproved_density: "n=11,m=31"
  recovery_count: "2/2 already consumed; no STUCK RECOVERY 3"
  next_state: "HARD RESERVE / successor admission required"
  directed_audit: "C30-AUDIT-C31-I0035-PAIR-RESISTANCE-06 = PASS (claim-scoped)"
  af449_audits_preserved:
    - "C30-AUDIT-C31-AF449-RAMANUJAN-CONE-01 = PASS"
    - "P26-AUDIT-C31-AF449-DIRECT-DUALITY-02 = PASS"
  artifacts:
    - "proofnet24/C30-sidorenko/artifacts/2026-09-16T23-14-50Z__check_n11_m28_m30_support_profile.py"
    - "proofnet24/C30-sidorenko/artifacts/2026-09-16T23-14-50Z__check_n11_m28_m30_support_profile.out"
```

No shared root ledger, peer file, email/Gmail item, Drive item, public post, paid compute setting, access control, or new schedule was changed in this run.
