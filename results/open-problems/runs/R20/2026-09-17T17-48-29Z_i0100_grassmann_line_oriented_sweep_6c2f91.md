Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model or reasoning-effort receipt, so I do not claim GPT-6 / maximum. **NO MOVEMENT in the frozen exact-prime metric: `1213 -> 1213`; retained exact set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`; unchanged count `2 -> 3`; status PARTIAL / SOURCE OPEN. Section-B moves: second-pass #19 MAKE IT AN ALGORITHM, #21 ASK WHO ELSE HAS THIS SHAPE, #29 ADD THE POINTS AT INFINITY.**

# R20 / I0100 — a projective Grassmann line, affine Plucker sweep, and the exact oriented-matroid crossing certificate

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim: `operations/claims/I0100.md`.
Outside source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.

For `p == 1 (mod 4)` prime put
\[
n=(p-1)/2,
\qquad
T_p:=\vartheta(\overline{G_{p,1}}).
\]
The source target is
\[
T_p\sim\sqrt{p/2}=\sqrt{n+1/2},
\]
equivalently `T_p ~ sqrt(n)`.

## 1. Continuity, ownership, and required repository recovery

I continued from the newest immutable R20 report

`runs/R20/2026-09-17T16-48-05Z_i0100_rankone_statdim_fixedmargin_f3a71c.md`

rather than restarting. Before doing new mathematics I reread or targeted-recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operative follow-up implementation manifest, the canonical I0100 ownership file, the newest R20 state, and neighboring Paley tracks. Large root/intake files are connector-truncated, so this is a current-state plus exact-targeted dependency read, not a claim that every unrelated byte of every intake row rendered in one response.

The canonical ownership remains non-overlapping:

- I0100 / Conjecture 26 / one-localization is R20;
- P04 / I0101 remains the distinct Conjecture 27 two-localization problem; its newest located report remains PARTIAL and has its own exact-prime metric `4049`;
- R12 has already handed off its former I0102 degree-four SoS problem and rotated elsewhere; that old Conjecture-28 scope is still distinct and is not reassigned here;
- the former C28 / I0103 Paley-ETF / Conjecture-29 work has likewise rotated away from that target; its scope remains distinct and is not imported here.

No shared root, peer report, or other track's file is edited by this run.

## 2. Fresh source and literature check — 2026-09-17

Primary source checked directly today:

`https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/`

The page still defines `G_{p,1}` as the induced graph on the neighbors of zero, notes that it is circulant so its theta SDP reduces to an LP, and still states Conjecture 26 as
\[
\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}.
\]
The same page separately states Conjectures 27, 28, and 29, matching the scope exclusions above. A bounded dated web/arXiv search found no source-matching resolution. This is evidence for current source status, not a worldwide novelty certificate.

Method #21 led to three nearby literatures:

1. Javier Pena and Vera Roshchina, *On the Grassmann condition number*, arXiv:1604.04637 (2016): conic feasibility `L cap K`, distance in the Grassmann manifold to ill-posed instances, and equivalence with an alternative-margin quantity. This is direct prior art for generic distance-to-ill-posedness; I do not claim that mechanism as new.
2. Dennis Amelunxen and Peter Burgisser, *Probabilistic analysis of the Grassmann condition number*, arXiv:1112.2603: random-subspace condition analysis. This is background for the previous random-cone comparison.
3. Steven N. Karp, *Moment curves and cyclic symmetry for positive Grassmannians*, BLMS 51 (2019), 900--916: cyclic-shift fixed points on Grassmannians and the unique totally nonnegative fixed point. The complexified Paley Fourier half is itself a cyclic-shift-invariant Fourier subspace, so Grassmann/Plucker language is natural. Karp's `q`-deformation is a different construction from the rank-one stretch parameter below; no identification is claimed.

The bounded search did not locate the exact rank-one projective-line crossing formula below in the Paley-theta setting. That negative search is not a novelty certificate.

## 3. Frozen finite metric

The exact-certified frontier entering and leaving this run is
\[
\boxed{p_{\max}=1213}
\]
with complete retained exact-certified set
\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213\}}.
\]
No new finite prime is claimed and no numerical SDP output is promoted. The previous `p=1213` exact primal/dual certificate remains the finite frontier. Because the metric does not move, the unchanged count becomes three; Section I therefore governs the *next* invocation.

## 4. Idea before code

The preceding run reduced the theta asymptotic to a rank-one-stretched orthant. Put
\[
m=n-1,
\qquad
d=m^{-1/2}{\bf1}\in\mathbb R^m,
\qquad
P=dd^\top=\frac1m{\bf1}{\bf1}^\top,
\]
and for `q>0`
\[
A_q:=I+(q-1)P.
\tag{4.1}
\]
Then `A_q` fixes `d^perp` and multiplies the diagonal direction `d` by `q`. The regular cone from the previous report is
\[
C_m(s)=A_{e^s}\mathbb R_+^m.
\]

For a real subspace `E subset R^m`, let `F=E^perp`. The radial condition can be written
\[
F\cap A_q\mathbb R_+^m\ne\{0\}.
\tag{4.2}
\]
Choose a full-row-rank matrix `B` whose row space is `E`. Then (4.2) is exactly
\[
\exists x\ge0,\ x\ne0:\quad BA_qx=0.
\tag{4.3}
\]

The new idea is to stop treating `q` as a scalar perturbation of a cone and instead move the *dual subspace*
\[
E(q):=A_qE.
\tag{4.4}
\]
Because `A_q` changes only one ambient direction, this entire high-dimensional path lives on one projective line in the Grassmannian. Every maximal Plucker coordinate is therefore affine in `q`. The theta threshold is consequently an exact oriented-matroid wall crossing on a one-dimensional parameter line.

No checker is appropriate for the theorem-sized linear-algebra claims below. Their burden is a proof on the page. I did not spend the run manufacturing a finite certificate for an unchanged prime.

## 5. Method #29 — add `q=0` and `q=infinity`: the whole deformation is one Grassmann projective line

Let `r=dim(E)` and assume
\[
0<\alpha:=\|P_Ed\|<1.
\tag{5.1}
\]
This is the nondegenerate case relevant to both Paley Fourier halves. Define
\[
K:=E\cap d^\perp,
\qquad
W:=E+\operatorname{span}\{d\}.
\tag{5.2}
\]
Then `dim K=r-1` and `dim W=r+1`.

### Theorem R20-GRASSLINE1 — exact compactified Grassmann line

For every `q>0`,
\[
\boxed{K\subset E(q)=A_qE\subset W.}
\tag{5.3}
\]
Hence `q -> E(q)` lies in the projective line of `r`-planes between `K` and `W`, canonically isomorphic to
\[
\mathbb P(W/K)\cong\mathbb{RP}^1.
\]
It has the two compactification endpoints
\[
\boxed{E(0)=(I-P)E\subset d^\perp,}
\tag{5.4}
\]
\[
\boxed{E(\infty)=K+\operatorname{span}\{d\}.}
\tag{5.5}
\]
Moreover, for `F=E^perp`,
\[
\boxed{(A_qE)^\perp=A_{1/q}F.}
\tag{5.6}
\]
Thus the previous exact complement symmetry `s <-> -s` is simply projective inversion `q <-> 1/q` on this line.

#### Proof

For `u in d^perp`, `A_qu=u`; hence every vector in `K` belongs to every `E(q)`. For arbitrary `u in E`,
\[
A_qu=u+(q-1)\langle d,u\rangle d\in E+\operatorname{span}\{d\}=W,
\]
which proves (5.3). Since `P_Ed` is nonzero, `K` has codimension one in `E`; since `alpha<1`, `d notin E`, so `W` has dimension `r+1`. The family of `r`-planes containing fixed `K` and contained in fixed `W` is exactly the projective line of one-dimensional subspaces in the two-dimensional quotient `W/K`.

At `q=0`, `A_0=I-P`. Its restriction to `E` is injective because its kernel is `span{d}` and `d notin E`; therefore `(I-P)E` still has dimension `r`, proving (5.4). For the other endpoint choose `u_0 in E` with `<d,u_0> != 0`. After rescaling the single transverse generator of `E(q)` by `q^{-1}`, it converges to a nonzero multiple of `d`, while the common `K` is fixed. Hence (5.5).

Finally `A_q` is symmetric and `A_q^{-1}=A_{1/q}`. Therefore
\[
(A_qE)^\perp=A_q^{-1}E^\perp=A_{1/q}F,
\]
proving (5.6). QED.

This is the literal use of “points at infinity”: the theta deformation closes to two explicit boundary subspaces rather than ending at an analytic singularity.

## 6. Every maximal Plucker coordinate is affine in `q`

Let `B` be any `r x m` full-row-rank matrix with row space `E`. Put
\[
v:=B{\bf1}.
\]
By (4.1),
\[
BA_q=B+\frac{q-1}{m}v{\bf1}^\top.
\tag{6.1}
\]
For an `r`-subset `I subset {1,...,m}`, write
\[
\Delta_I(q):=\det((BA_q)_I).
\]
The matrix in (6.1) is a rank-one update, so determinant multilinearity gives
\[
\boxed{
\Delta_I(q)
=\Delta_I(1)+\frac{q-1}{m}\Gamma_I,
\qquad
\Gamma_I:={\bf1}_r^\top\operatorname{adj}(B_I)v.
}
\tag{6.2}
\]
Equivalently, without assuming `B_I` invertible,
\[
\boxed{
\Delta_I(q)=\Delta_I(0)+q\bigl(\Delta_I(1)-\Delta_I(0)\bigr).
}
\tag{6.3}
\]
Thus the Plucker embedding sends the whole deformation to a literal projective line.

Every nonconstant Plucker coordinate has at most one finite root,
\[
\boxed{
q_I
=-\frac{\Delta_I(0)}{\Delta_I(1)-\Delta_I(0)}
=\frac{\Delta_I(0)}{\Delta_I(0)-\Delta_I(1)}.
}
\tag{6.4}
\]
The Plucker coordinates at the point `q=infinity` are proportional to the slopes
\[
\Delta_I(1)-\Delta_I(0).
\tag{6.5}
\]
No high-degree continuation polynomial occurs: the only possible oriented-matroid wall locations are these exact endpoint-minor ratios.

## 7. Method #19 — make it an algorithm: exact parametric oriented-matroid sweep

For the R20 radial problem define
\[
\mathcal F(q):\quad
\exists x\in\mathbb R_+^m\setminus\{0\}
\text{ such that }BA_qx=0.
\tag{7.1}
\]
Because `a(q)=(1+sqrt(n) q)/(n-1)` is increasing in `q`, the exact radial definition gives one threshold `q_*` such that
\[
\mathcal F(q)\text{ holds for }0<q\le q_*,
\qquad
\mathcal F(q)\text{ fails for }q>q_*.
\tag{7.2}
\]
For the Paley `N`-half, the preceding run identified
\[
\boxed{
q_*=q_p=e^{s_p}
=\frac{\sqrt n\,(T_p-1)}{n-T_p}.
}
\tag{7.3}
\]
Hence the source conjecture is exactly `q_p -> 1`.

### Theorem R20-OMSWEEP1 — the theta threshold is an exact Plucker wall

After contracting any maximal minors that vanish identically for every `q`, the threshold `q_*` is a positive root `q_I` of at least one non-identically-zero maximal minor (6.3). Moreover at `q=q_*` there exist

- a nonzero positive circuit `x_*>=0` with `BA_{q_*}x_*=0`, and
- a nonzero nonnegative cocircuit/separator `z_* in row(BA_{q_*})`,

with
\[
\boxed{z_*\cdot x_*=0.}
\tag{7.4}
\]
The circuit may be chosen with support of size at most `r`, so an `r x r` maximal minor vanishes on a set containing its support.

#### Proof

On any open interval containing no root of a non-identically-zero maximal minor, the sign of every Plucker coordinate is constant. Therefore the oriented matroid of the columns of `BA_q` is constant on that interval. In particular, the existence or nonexistence of a positive circuit is constant there. Since (7.2) changes truth value at `q_*`, at least one non-identically-zero Plucker coordinate must vanish at `q_*`; by (6.3) its root is exactly one of the ratios (6.4).

At `q_*`, choose a positive kernel vector of minimal support. Its support is a circuit. A circuit of size `r+1` whose support columns have rank `r` has a unique dependence up to scale. If all `r`-subsets of those `r+1` columns were nonsingular, every coefficient in that dependence would be nonzero; strict positivity of all coefficients would then persist for `q` in a neighborhood of `q_*`, contradicting the fact that `q_*` is the boundary of feasibility. Hence a boundary positive circuit can be chosen on at most `r` columns, or equivalently some maximal minor containing its support vanishes.

For `q>q_*`, the Gordan--Stiemke alternative supplies a strictly positive vector in the row space of `BA_q`. Normalize these separators to have Euclidean norm one and take `q downarrow q_*`. Compactness and continuity of `row(BA_q)` give a nonzero limit `z_*>=0` in `row(BA_{q_*})`. Since `x_*>=0`, `z_*>=0`, and `z_*` lies in the row space while `x_*` lies in the kernel,
\[
z_*\cdot x_*=0.
\]
This proves the stated compatible circuit/cocircuit certificate. QED.

### Exact finite algorithm implied by the theorem

The theorem converts a continuous SDP/LP threshold into a finite exact sweep:

1. represent the Paley Fourier subspace `E` exactly in the real cyclotomic field;
2. obtain endpoint Plucker pairs `(Delta_I(0), Delta_I(1))` only as needed by the current basis/circuit, rather than enumerating every minor;
3. form the exact candidate wall `q_I` from (6.4);
4. pivot the oriented matroid across successive positive roots; between roots no sign data change;
5. stop at the first wall carrying a nonnegative circuit on the feasible side and a nonnegative cocircuit on the infeasible side;
6. recover
   \[
   T_p=\sqrt n\,\frac{q_p\sqrt n+1}{q_p+\sqrt n}
   \]
   exactly from the certified root.

This is not a polynomial-time claim; in the worst case an oriented-matroid sweep can still be exponentially large. The gain is conceptual and certificate-theoretic: every wall is a degree-one exact algebraic event in `q`, and a single sign-compatible circuit/cocircuit pair certifies the crossing. This is different from the earlier R20 `p=1021` determinant/simplex report, which pivoted bases at one fixed LP; here the *entire theta deformation* is an affine-Plucker homotopy on one Grassmann projective line.

## 8. Method #21 — exact directional Grassmann condition along the Paley line

Generic Grassmann condition numbers minimize distance over all ill-posed subspaces. Here the rank-one path gives a much sharper one-direction quantity that can be calculated exactly.

Let
\[
\alpha=\|P_Ed\|,
\qquad
\beta=\sqrt{1-\alpha^2}.
\tag{8.1}
\]
Choose unit vectors
\[
\hat f=P_Ed/\alpha\in E,
\qquad
\hat e=P_Fd/\beta\in F.
\]
Then
\[
d=\alpha\hat f+\beta\hat e.
\]
The subspaces `E` and `E(q)=A_qE` share the fixed `(r-1)`-plane `K=E cap d^perp`, so only one principal angle can be nonzero. Directly,
\[
A_q\hat f
=(\beta^2+q\alpha^2)\hat f
 +(q-1)\alpha\beta\hat e,
\tag{8.2}
\]
and
\[
\|A_q\hat f\|^2=\beta^2+q^2\alpha^2.
\tag{8.3}
\]
Therefore the projection-metric Grassmann distance is
\[
\boxed{
d_{\rm dir}(q)
:=d_{\rm Gr}(E,E(q))
=\frac{|q-1|\alpha\beta}
{\sqrt{\beta^2+q^2\alpha^2}}.
}
\tag{8.4}
\]

### Paley specialization

Under the self-dual isometry, `d` corresponds to the normalized centered coordinate vector
\[
\sqrt{\frac n{n-1}}\left(e_0-\frac1n{\bf1}\right).
\]
Its unitary DFT has equal squared magnitude `1/(n-1)` on every nonzero Fourier frequency. Hence for the two real Paley Fourier halves
\[
\boxed{
\alpha_N^2=\frac{|N|}{n-1}=\frac{n}{2(n-1)},
\qquad
\alpha_S^2=\frac{|S|}{n-1}=\frac{n-2}{2(n-1)}.
}
\tag{8.5}
\]
In both cases
\[
\boxed{
\alpha_Z\beta_Z
=\frac{\sqrt{n(n-2)}}{2(n-1)}
\longrightarrow\frac12.
}
\tag{8.6}
\]

At `q=q_p`, the Paley subspace `E_N(q_p)` is exactly an orthant-ill-posed point: the primal positive circuit and dual nonnegative cocircuit coexist. Therefore
\[
\boxed{
T_p/\sqrt n\to1
\iff
q_p\to1
\iff
d_{\rm dir}(q_p)\to0.
}
\tag{8.7}
\]

This should be distinguished carefully from the generic Grassmann condition number of Pena--Roshchina. If `Sigma` denotes all ill-posed subspaces, then
\[
\operatorname{dist}(E,\Sigma)
\le d_{\rm dir}(q_p),
\]
so generic ill-conditioning can only give a lower bound on how near *some* bad subspace is. R20 needs the stronger arithmetic assertion that the specific rank-one Paley projective line meets the orthant ill-posed set at distance `o(1)`.

## 9. What the asymptotic has now become

The Plucker-line theorem turns the source conjecture into a sharply sign-sensitive determinant statement. By R20-OMSWEEP1, for every prime there is at least one maximal minor `I_p` whose exact affine root is the true crossing:
\[
q_p
=1-
\frac{\Delta_{I_p}(1)}
{\Delta_{I_p}(1)-\Delta_{I_p}(0)}.
\tag{9.1}
\]
Therefore it would suffice to produce a *sign-compatible* crossing minor/circuit/cocircuit family satisfying
\[
\boxed{
\frac{\Delta_{I_p}(1)}
{\Delta_{I_p}(1)-\Delta_{I_p}(0)}
=o(1).
}
\tag{9.2}
\]
The sign-compatible qualifier is essential: an arbitrary small-ratio minor can cross zero without changing positive-cone feasibility.

This exposes the exact remaining arithmetic obstruction more sharply than the previous fixed-margin separator statement:

> Find an orientation-positive Paley Fourier basis wall whose endpoint Plucker ratio is `o(1)`, and certify the adjacent positive circuit and complementary nonnegative cocircuit.

Magnitude-only determinant bounds, Jacobi one-point equidistribution, and generic Grassmann condition estimates do not enforce the needed circuit/cocircuit signs. The earlier arcsine obstruction explains why a scalar one-point profile cannot do this. The next useful input must control a coherent *oriented* family of Paley Fourier minors or an equivalent sign-compatible circuit.

There is a possible structural reason to pursue this. The complexified Paley Fourier subspace is a cyclic-shift fixed point in the Grassmannian. Karp's work classifies cyclic-shift fixed points and identifies the unique totally nonnegative one. The Paley fixed point is not being claimed totally nonnegative; rather, the hope is that its arithmetic cyclic symmetry may organize the signs of the particular one-parameter minor sweep enough to locate a crossing near the self-dual point. That is a proposed route, not a theorem.

## 10. Audit and prior-art boundary

The new claims

- `R20-GRASSLINE1`,
- affine-Plucker identity (6.2)--(6.4),
- `R20-OMSWEEP1`,
- directional-distance identity (8.4)--(8.7)

have written proofs above and are **SELF_CHECK_ONLY**. No OTHER-track audit has reconstructed them yet. Existing independent audits concern earlier finite primes / earlier narrow algebraic cores and do not certify this new asymptotic route.

Generic conic feasibility alternatives, oriented matroid sign constancy, parametric LP ideas, Plucker coordinates, and Grassmann condition numbers are established background. Karp's cyclic-Grassmannian fixed-point machinery is also prior art. No novelty claim is made for those mechanisms. The potentially new content is their exact specialization to the R20 rank-one theta deformation and the identification of the source asymptotic with an orientation-compatible affine-Plucker wall at `q=1+o(1)`; this remains subject to a proper prior-art audit.

## 11. Stagnation state and next-run obligation

The frozen exact-prime metric has now failed to move for **three consecutive runs**. Under the controlling Section-I rule, the next R20 invocation must therefore be a **thinking-only stuck recovery**: no new theorem claim merely to create activity, no new finite prime checker, and no extension of the current route by another routine lemma.

That next report must contain, explicitly:

1. the exact blocking statement in one displayed formula;
2. every route tried and the precise reason each failed;
3. what a successful proof would need that no current route contains;
4. the simplest unproved special case;
5. the nearest solved problem in the literature and the ingredient it has that Paley lacks;
6. exactly one selected action among the five Section-I options, followed by a new three-move plan.

This run does not pre-empt that required choice.

## 12. Model/scheduler control status

The model-control limitation remains unresolved. The exposed scheduler create/update schema offers title, prompt, schedule / relative-start fields, enabled state, and timing mode. It exposes no native model-family selector, no reasoning-effort selector, no guaranteed full-hour runtime field, and no authenticated completed-run routing receipt. GPT-6 / maximum is therefore still prompt-only.

The repository's implementation receipts also preserve the context-specific permission history: one earlier P26 edit returned the literal error `You cannot modify this task`, while a different later authorized context successfully updated P26. The legitimate remedy for unavailable model routing or task ownership is an authorized product/workspace surface or platform/API support that exposes those controls; it is not a duplicate task or a permission bypass. No scheduler change was attempted in this run.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R20
  intake: I0100
  source: "Afonso S. Bandeira et al., Randomstrasse101 2025, Conjecture 26"
  target: "theta(complement G_{p,1}) ~ sqrt(p/2)"
  fixed_metric: "largest admissible prime with matching exact primal and dual source-normalized theta certificates"
  metric_before: 1213
  metric_after: 1213
  covered_primes:
    - 5
    - 13
    - 17
    - 29
    - 41
    - 181
    - 241
    - 317
    - 421
    - 541
    - 601
    - 661
    - 1009
    - 1021
    - 1033
    - 1049
    - 1061
    - 1093
    - 1201
    - 1213
  status: PARTIAL
  source_status: OPEN
  unchanged_count_before: 2
  unchanged_count_after: 3
  tried_moves:
    - 19
    - 21
    - 29
  pass: second
  new_claims:
    - "R20-GRASSLINE1: exact compactified rank-one Grassmann projective line"
    - "affine Plucker coordinates and exact candidate roots"
    - "R20-OMSWEEP1: source threshold is a sign-compatible oriented-matroid wall"
    - "R20-DIRCOND1: one-principal-angle directional Grassmann distance formula"
  evidence:
    finite: "no new finite claim; p=1213 exact frontier retained"
    theorem_proofs: "written on page; self-check only"
    fresh_source_check: "2026-09-17 Randomstrasse PaleyGraph page plus bounded current search"
  audits:
    new_claims: SELF_CHECK_ONLY
    source_asymptotic: NONE
  remaining_obligation: "construct or control a sign-compatible Paley Fourier Plucker wall q_p=1+o(1), equivalently an adjacent positive circuit/nonnegative cocircuit with endpoint minor ratio o(1)"
  next_run: "MANDATORY SECTION-I THINKING-ONLY STUCK RECOVERY because unchanged_count reached 3"
```

**NO CLOSURE CLAIM.**
