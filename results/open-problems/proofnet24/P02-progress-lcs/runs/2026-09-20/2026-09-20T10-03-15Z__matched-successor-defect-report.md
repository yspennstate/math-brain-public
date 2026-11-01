Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum reasoning was requested, but this runtime exposes no authenticated applied-effort receipt or model-selector control, so I do not claim otherwise.

# P02 / T02 — matched successor-defect amplification beyond the residue-optimal bound

## 0. Source-level movement

Target:
\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}n
\]
for two independent iid uniform binary strings. The dependent match array induced by the two source strings is retained throughout; the independent Bernoulli matching model is not substituted.

Retain the rigorous public lower endpoint
\[
L=0.792665992=\frac{99083249}{125000000}.
\]
The preceding P02 report,
`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T09-05-20Z__residue-optimal-defect-report.md`,
proved an internal exact C045 upper endpoint
\[
U_*:=\frac{\log(4t^2)}{\log\lambda_*}
\]
using the two-step defect `D_*=a/v_*` below.

This run proves a stronger exact finite dual rate `lambda_new < lambda_*`, and therefore
\[
\boxed{L\le\gamma_2\le U_{new}<U_*},
\qquad
U_{new}:=\frac{\log(4t^2)}{\log\lambda_{new}}.
\]
An exact positive-series logarithm enclosure proves the strict decimal separator
\[
\boxed{
U_{new}<
0.82627594276228262501510658153729663282346199619319002388080618331256294443029952
<U_*.
}
\]
Thus the certified interval width strictly moves from `U_*-L` to `U_new-L`.
Diagnostic high precision, not used as proof, gives
\[
U_*-U_{new}\approx1.0655909281446033\times10^{-80}.
\]
The absolute source movement remains tiny. The finite dual mechanism movement is much larger: the universal two-step defect increases by about 27.22%.

Status: **PARTIAL / source OPEN / candidate internal certificate pending later independent review and public-priority checking.**

## 1. Source, current literature status, exclusions, and coordination

Controlling policy is `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`. Root `POSTED.md` was checked; no posting exclusion covers T02.

Fresh source navigation on 2026-09-20 recovered Alexander Tiskin, `arXiv:2212.01582v2`, last revised 2024-08-13. Its current abstract still states that the binary Chvatal-Sankoff coefficient is unresolved. The comments explicitly state that claims in the earlier preprint concerning the stochastic process and `gamma` turned out to be incorrect and were omitted from v2, while a supported estimate was retained. None of the removed claims is used here.

The rigorous public lower endpoint remains `0.792665992` from Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`. Their paper still quotes Lueker's `0.826280` as the public rigorous upper endpoint. Li--Ren--Wen, published online by Cambridge University Press on 2026-03-02, likewise describe the two-string binary constant as open and summarize the public range at roughly `0.792665 <= gamma <= 0.826280`. The stronger C045/P02 upper endpoint is repository-internal and is not represented as a published bound.

Prior rigorous/semirigorous LCS attempts relevant to this lane include the original Chvatal--Sankoff bounds, Dancik--Paterson finite-state/covering bounds, Lueker's 2009 improvement, later computational lower bounds culminating in `0.792665992`, and Tiskin's corrected stochastic-process estimate. The C045 repository route is a covering-operator continuation of the finite-state upper-bound philosophy, but the new theorem below is an arithmetic Collatz-dual strictification of a frozen exact cone witness.

Newest own substantive dependency recovered in full: the 09:05 residue-optimal report named above. Its exact C045 constants and proof dependencies are retained, not re-audited wholesale.

Newest P13 companion recovered:
`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T09-18-50Z__extremal-boundary-band-bracket.md`, blob `251221b18f3dfe30043804adee5a2df7b880f627`. P13 proves an extremal-boundary finite bracket for the genuine dependent strip recursion, shrinking its generic finite-to-stationary width to at most `w/N`; it remains a lower-side/boundary-recursion mechanism and does not duplicate the covering/cone dual work here.

Current R17 same-source history recovered:
`runs/prob10_2026-09-20/PROB10-02/20260920T0837Z_r17_sharp_centered_path_span_a4d2.md`, blob `5ed147f73654da435da33832ec33c2a8633e19ec`. R17 proves the sharp centered path-span `m` and a factor-two finite-to-stationary transfer but reports no source endpoint movement. P02 therefore stays on the complementary finite covering/cone variational route.

Short handoff of P02's actual former target: Aldous--Fill Open Problem 2.34 remains closure-packaged at frozen `11/11`; publication novelty there was not certified. It is not reopened.

## 2. Frozen C045 operator and preceding residue-optimal defect

Put
\[
t=\frac pq=\frac{256717}{800000},\qquad d=q-p=543283,
\]
\[
S=q^6d,
\qquad
A=t^2H,
\qquad
B=SH.
\]
The primitive coefficient types are
\[
c_k=q^{6-k}dp^k\quad(0\le k\le6),
\qquad c_7=p^7,
\]
with multiplicities `(2,4,4,4,4,4,4,4)`. In particular
\[
\boxed{c_7=73482242694633120311956186136958404773}
\]
is the smallest positive primitive coefficient.

The inherited positive integer cone witness satisfies
\[
1\le V_i\le M=5\cdot10^{18},
\qquad
BV\le\frac abV,
\]
where
\[
a=1995237757733917147310102692686664915858011319606812684127301,
\]
\[
b=4220452010631561279,
\qquad \gcd(a,b)=1,
\qquad b\le M<2b.
\]
Define the integer one-step slack
\[
\boxed{s_i=aV_i-b(BV)_i\ge0.}
\tag{2.1}
\]
Let
\[
\alpha=a\bmod b=1884560463669269501,
\qquad
h=707440146652911839,
\]
so that `alpha*h == 1 (mod b)`, and put
\[
\boxed{v_*=h+b=4927892157284473118.}
\]
The preceding report proved for every non-tight row
\[
\frac{s_i}{V_i}\ge\frac1{v_*}
\]
and matched the tight-row branch above the exact rational defect
\[
\boxed{D_*:=\frac a{v_*}}.
\tag{2.2}
\]
Thus it had
\[
B^2V\le\frac{a^2-D_*}{b^2}V.
\]
Its explicit residual obstruction was that the range-plus-congruence relaxation allows the extremal pair `s=1,V=v_*`. This run attacks exactly that extremal pair by propagating slack one step farther through the actual integer operator.

## 3. New non-tight-row theorem: the residue optimum cannot have small successor slack

For every row define
\[
T_i:=(Bs)_i=\sum_jB_{ij}s_j.
\tag{3.1}
\]
The exact two-step defect identity is
\[
\boxed{
a^2V_i-b^2(B^2V)_i=a s_i+bT_i.
}
\tag{3.2}
\]
We prove that every non-tight row has normalized defect far above `D_*`.

### 3.1 All non-extremal residue cases are automatically large

Since `s_i == alpha V_i (mod b)` and `h alpha == 1 (mod b)`,
\[
V_i\equiv h s_i\pmod b.
\tag{3.3}
\]
If `s_i>=2`, then simply using `V_i<=M` gives
\[
\frac{a s_i}{V_i}\ge\frac{2a}{M}.
\tag{3.4}
\]
If `s_i=1`, (3.3), `1<=V_i<2b`, and `h<b` imply
\[
V_i\in\{h,h+b\}=\{h,v_*\}.
\tag{3.5}
\]
The branch `V_i=h` has first-term defect `a/h`, again much larger than the new target below. Therefore only the exact extremal case
\[
\boxed{s_i=1,\qquad V_i=v_*}
\tag{3.6}
can remain near `D_*`.

### 3.2 Successor-slack congruence in the extremal case

Assume (3.6). Then from (2.1)
\[
u:=(BV)_i=\frac{a v_*-1}{b}\in\mathbb Z.
\tag{3.7}
\]
Applying (2.1) after one multiplication by `B` gives
\[
T_i=(Bs)_i=a(BV)_i-b(B^2V)_i,
\]
so
\[
\boxed{T_i\equiv a u\pmod b.}
\tag{3.8}
\]
Exact arithmetic gives
\[
\boxed{a u\bmod b=488687687567202178.}
\tag{3.9}
\]
Because every entry of `B` is a nonnegative integer combination of the eight primitive label coefficients, the quantity `T_i` belongs to the relaxed unrestricted semigroup
\[
T_i=\sum_{k=0}^7 c_k S_k,
\qquad S_k\in\mathbb Z_{\ge0}.
\tag{3.10}
\]
Allowing every coefficient type even if a specific actual row omits it is a relaxation, hence exclusion in (3.10) is safe for the actual operator.

The executed exact meet-in-the-middle checker exhausts every relaxed vector satisfying
\[
0<T\le5000c_7,
\qquad
T\equiv488687687567202178\pmod b.
\]
It builds all `5,910,302` feasible `(S_6,S_7)` pairs, all with distinct residues in this range, and performs `41,070,180` exact prefix lookups over `(S_0,...,S_5)`. It finds no solution. Therefore every actual extremal non-tight row satisfies
\[
\boxed{T_i>5000c_7.}
\tag{3.11}
\]
This is the first new mechanism of the run: the scalar residue optimum `s=1,V=v_*` cannot persist with a small second-generation slack.

## 4. Tight-row branch pushed in parallel by 1500 coefficient units

For a tight row `s_i=0`, coprimality in (2.1) and `1<=V_i<2b` give
\[
V_i=b,
\qquad
(BV)_i=a.
\tag{4.1}
\]
The inherited four-band theorem says its positive successor slack has the representation
\[
T_i=\sum_{k=0}^7c_kS_k
\tag{4.2}
\]
with
\[
S_0\ge1,
\qquad S_7\ge1,
\qquad S_1+S_2+S_3\ge1,
\qquad S_4+S_5+S_6\ge1.
\tag{4.3}
\]
Also
\[
\boxed{T_i\equiv a^2\pmod b},
\qquad
a^2\bmod b=3275530027931543170.
\tag{4.4}
\]

Write
\[
D_{\rm floor}:=\left\lfloor\frac a{v_*}\right\rfloor
=404886652152996330056570759820082466026328.
\tag{4.5}
\]
This run raises the exact tight-row exclusion threshold to
\[
D_{\rm floor}+1500c_7
=515110016194946010524505039025520073185828.
\tag{4.6}
\]
The exact four-band meet-in-the-middle checker covers `5,926,417` feasible `(S_6,S_7)` pairs, `5,921,410` residues with `S_6>0`, and `43,854,732` exact prefix/residue lookups. It finds no relaxed tuple satisfying (4.2)--(4.4) at or below (4.6). Hence every actual tight row obeys
\[
\boxed{T_i\ge D_{new}},
\tag{4.7}
\]
where
\[
\boxed{
D_{new}:=D_{\rm floor}+1500c_7+1
=515110016194946010524505039025520073185829.
}
\tag{4.8}
\]

An exploratory attempt to extend this same exact tight-row search to `2500 c_7` did not finish inside the local execution window. No claim beyond the executed `1500 c_7` threshold is made.

## 5. Matched universal two-step defect theorem

We now show that the same `D_new` works for every row.

### Tight rows

If `s_i=0`, then by (4.1), (3.2), and (4.7),
\[
\frac{a^2V_i-b^2(B^2V)_i}{V_i}
=T_i\ge D_{new}.
\tag{5.1}
\]

### Non-tight rows

If `s_i>=2`, the exact arithmetic checker verifies
\[
\frac{2a}{M}>D_{new}.
\tag{5.2}
\]
If `s_i=1,V_i=h`, it verifies
\[
\frac ah>D_{new}.
\tag{5.3}
\]
In the only remaining case `s_i=1,V_i=v_*`, (3.2) and (3.11) give
\[
\frac{a^2V_i-b^2(B^2V)_i}{V_i}
=
\frac a{v_*}+\frac{bT_i}{v_*}
>
\frac a{v_*}+\frac{5000bc_7}{v_*}.
\tag{5.4}
\]
Exact arithmetic verifies that the right side of (5.4) is strictly larger than `D_new`.

Therefore every row satisfies
\[
\boxed{
B^2V\le\frac{a^2-D_{new}}{b^2}V.
}
\tag{5.5}
\]
This is the main new dual theorem.

Relative to the preceding exact rational defect,
\[
\frac{D_{new}}{D_*}
=1.2722326445088614\ldots,
\tag{5.6}
\]
so the finite dual defect increases by approximately 27.22%.

By Collatz monotonicity applied to the positive vector `V`,
\[
\rho(B)^2\le\frac{a^2-D_{new}}{b^2}.
\tag{5.7}
\]
Define the convenient rational strict majorant
\[
\boxed{
\beta_{new}:=\frac ab-\frac{D_{new}}{2ab}.
}
\tag{5.8}
\]
Then
\[
\beta_{new}^2
=
\frac{a^2-D_{new}}{b^2}
+
\frac{D_{new}^2}{4a^2b^2}
>
\frac{a^2-D_{new}}{b^2},
\]
so
\[
\rho(B)<\beta_{new}.
\tag{5.9}
\]
The preceding rate was
\[
\beta_*:=\frac ab-\frac1{2bv_*},
\]
and `D_new>D_*=a/v_*` gives
\[
\boxed{\beta_{new}<\beta_*}.
\tag{5.10}
\]
Since `A=(t^2/S)B`, put
\[
\boxed{
\lambda_{new}:=\frac{t^2}{S}\beta_{new}.
}
\tag{5.11}
\]
Then
\[
\boxed{ho(A)<\lambda_{new}<\lambda_*<1.}
\tag{5.12}
\]

## 6. Dependence-preserving finite-to-infinite transfer

For completeness, the exact transfer used by C045 is restated under the assumptions needed here.

At fugacities `(x,y)`, the finite covering operator enumerates accepted collations of **actual ordered source-string pairs**. Let `F_m(x,y)` be the total positive weight of accepted `m`-factor collations. If `z>rho(A)` then finite dimensionality gives a constant `K_z<infinity` such that
\[
F_m(x,y)\le K_z z^m.
\tag{6.1}
\]
The covering property says that every actual pair `(X_1^n,Y_1^n)` with `LCS>=m` contributes at least one accepted collation. Since coefficients are nonnegative, coefficient extraction and evaluation at positive `(x,y)` give
\[
\#\{(X,Y)\in\{0,1\}^n\times\{0,1\}^n:LCS(X,Y)\ge m\}
\le
K_z x^{-n}y^{-n}z^m.
\tag{6.2}
\]
Every actual ordered binary pair has probability exactly `4^{-n}`, hence
\[
\boxed{
\Pr\{L_n\ge m\}
\le
K_z(4xy)^{-n}z^m.
}
\tag{6.3}
\]
No independent probability is assigned to any match cell; dependence is preserved because the count is over the underlying source-string pairs.

For any
\[
c>\frac{\log(4xy)}{\log z},
\]
the right side of (6.3) is exponentially small uniformly for `m>=cn`. Splitting the tail-sum identity for `E L_n` at `cn` and summing the geometric upper tail yields
\[
\limsup_{n\to\infty}\frac{\mathbf E L_n}{n}\le c.
\]
Letting `c` decrease to the threshold proves
\[
\boxed{
\gamma_2\le\frac{\log(4xy)}{\log z}.
}
\tag{6.4}
\]
Finally let `z` decrease to any certified strict spectral majorant. At
\[
x=y=t=\frac{256717}{800000},
\qquad z=\lambda_{new},
\]
(6.4) gives `U_new`. Since `lambda_new<lambda_*` and the function `z -> log(4t^2)/log z` is strictly increasing on `(0,1)`,
\[
\boxed{U_{new}<U_*}.
\tag{6.5}
\]
Thus the finite theorem genuinely shrinks the original-problem interval.

## 7. Exact endpoint enclosure

The endpoint checker uses
\[
-\log z=2\sum_{k=0}^{K-1}\frac{u^{2k+1}}{2k+1}+R_K,
\qquad
u=\frac{1-z}{1+z},
\]
with the exact positive remainder bound
\[
0<R_K<\frac{2u^{2K+1}}{(2K+1)(1-u^2)}.
\]
At `K=260`, exact rational arithmetic proves
\[
U_{new}<Q<U_*,
\]
where
\[
Q=
\frac{82627594276228262501510658153729663282346199619319002388080618331256294443029952}{10^{80}}.
\]
The executed output ends
`NON_TIGHT_BRANCH_COMPARISONS=PASS`,
`D_NEW_STRICTLY_BEATS_D_STAR=PASS`,
`TWO_STEP_SPECTRAL_MAJORANT_STRICTLY_IMPROVES=PASS`,
`EXACT_LOG_SEPARATOR_PASS`,
`SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS`, and
`ALL_EXACT_CHECKS_PASS`.

## 8. Soundness boundaries and residual obstruction

The two semigroup computations deliberately use relaxations, never hidden graph assumptions. The extremal non-tight checker allows arbitrary nonnegative slack mass in every primitive coefficient type. The tight checker uses only the previously proved four-band support and the exact congruence. Therefore a negative relaxed search is safe for the actual C045 rows.

This run does **not** claim to identify an actual extremizing row, compute the true spectral radius, or determine `gamma_2`. It does not certify novelty or publication priority. Full independent review remains pending.

The present bottleneck is now quantitative rather than conceptual: the exact relaxed semigroup searches become expensive when the threshold is pushed much beyond the executed `1500c_7` tight window. A stronger next attack should either compress the four-band semigroup arithmetically, use actual successor identities/coincidences from the C045 graph, or derive a multistep residue recurrence that bypasses raw threshold enumeration. Repeating decimal endpoint polishing is not useful.

## 9. Exact artifacts

All files are under `proofnet24/P02-progress-lcs/artifacts/` and are new immutable files; no historical or peer file was overwritten.

1. `2026-09-20T10-03-15Z__extremal_successor_semigroup_checker.cpp`
   - creation commit `713258a4e884bf116b5940dd25d779f8b2f31006`
   - verified blob `bacbe78781591ab0c103cfd47dc90c40aa1f9b84`.
2. `2026-09-20T10-03-15Z__extremal_successor_semigroup_checker.out`
   - creation commit `8bb68f255c3b49345909e5894feb29137911f66d`
   - verified blob `c67e8ee6f000eb80d1c20edb44787f46616009f2`.
3. `2026-09-20T10-03-15Z__tight_four_band_1500c7_checker.cpp`
   - creation commit `73a1d27b05340c02d332c5c416d1be9e087d69d8`
   - verified blob `62d44b1a2414084d6b1c0e39dfa6041956a60286`.
4. `2026-09-20T10-03-15Z__tight_four_band_1500c7_checker.out`
   - creation commit `8063f29218894925f87bfc10251333069547ac08`
   - verified blob `3fad1e06288e4dd6d6024a8c2e18d3dccd25d366`.
5. `2026-09-20T10-03-15Z__matched_defect_endpoint_checker.py`
   - creation commit `a5de4c73b61a313655f42b8f1ee52dd975b4d28d`
   - verified blob `e381d0dc3dfe253f8653ed038d125e508d6fc8c1`.
6. `2026-09-20T10-03-15Z__matched_defect_endpoint_checker.out`
   - creation commit `08f7587689e57435e331cb78f527ffa407c93ae0`
   - verified blob `28878c3484922b94791c92533a65637da3cf0543`.

No email, Drive, public posting, paid compute, permission change, workflow execution, scheduler change, or access change was attempted.

```yaml
ledger_delta:
  slot: P02
  parent: T02
  source: "Chvatal-Sankoff binary LCS constant for two independent iid uniform binary strings"
  model_requested: GPT-6_maximum
  model_actual: GPT-5.6_Sol
  reasoning_level: UNVERIFIED
  source_status: OPEN
  status: PARTIAL
  lower: 0.792665992
  upper_before_symbolic: "U_* = log(4t^2)/log(lambda_*)"
  upper_after_symbolic: "U_new = log(4t^2)/log(lambda_new)"
  exact_separator: "U_new < 0.82627594276228262501510658153729663282346199619319002388080618331256294443029952 < U_*"
  width_before_symbolic: "U_* - 0.792665992"
  width_after_symbolic: "U_new - 0.792665992"
  width_strictly_decreased: true
  diagnostic_upper_decrease: "1.0655909281446033e-80"
  finite_defect_before: "D_* = a/v_*"
  finite_defect_after: 515110016194946010524505039025520073185829
  finite_defect_ratio_diagnostic: 1.2722326445088614
  new_theorem: "B^2 V <= ((a^2-D_new)/b^2) V"
  new_mechanism:
    - "extremal non-tight residue pair s=1,V=v_* forces successor slack T=B s into a new exact congruence"
    - "unrestricted coefficient-semigroup exclusion proves T>5000*c7"
    - "parallel four-band exact exclusion proves every tight-row T>=floor(a/v_*)+1500*c7+1"
    - "matched two-step defect transfers through the actual-string covering operator"
  dependence_preserved: true
  independent_bernoulli_matching_used: false
  companion_P13_scope: "extremal-boundary genuine-source strip bracket / lower-side finite-to-stationary transfer"
  R17_scope: "centered path-span / correlated strip geometry"
  failed_extension: "tight relaxed search at 2500*c7 did not finish in the local execution window; no claim made"
  residual_obstruction: "compress the semigroup or use actual C045 successor identities to move beyond threshold enumeration"
  full_independent_review_pending: true
  posted_claim_overwrite: false
```
