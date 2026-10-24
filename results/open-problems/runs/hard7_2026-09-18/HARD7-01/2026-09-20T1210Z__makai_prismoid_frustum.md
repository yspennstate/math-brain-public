Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_Makai: 2 -> 2` (**NO MOVEMENT**). Methods: **B6 / B18 / B24**.

# HARD7-01 — exact prismoid fibre reduction and sharp Makai theorem for every positive-homothety frustum

**Status:** `PARTIAL / SOURCE OPEN / CLAIMED`.

This bounded iteration resumes the exclusive Makai Jr. polar difference-body target admitted in the preceding run. The source-level dimension does not move: arbitrary three-dimensional convex bodies remain open. The substantive progress is nevertheless all-parameter rather than numerical: (i) an exact planar support-function formula for the polar difference body of every three-dimensional prismoid, and (ii) a sharp proof of Makai's conjectured bound for every convex hull of two positively homothetic planar convex bodies in parallel planes, including all pyramids, all prisms, and every truncated cone/frustum between them.

## 1. Continuity, exclusions, ownership, and required reads

I resumed the current canonical claim

`operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md`

owned by `HARD7-01`; I did not restart admission or mint an equivalent alias.

At run start I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the current Makai claim;
- the newest own checkpoint `runs/hard7_2026-09-18/HARD7-01/2026-09-20T1150Z__mahler_df2_handoff_makai_all_pyramids.md`;
- the newest visible neighboring Gaussian HARD7 state, `HARD7-05` (its current target is integrated-fBM persistence, not an ownership collision);
- repository/intake alias searches for `Makai`, `difference body`, `polar difference body`, `Mahler`, and the exact source constant.

As in the preceding report, the connector does not make a literal byte-for-byte reread of every very large `probability_1000_intake_*/problems.jsonl` file practical inside one bounded invocation. I therefore do **not** claim such a bytewise reread. Targeted searches through repository/intake material found no competing Makai owner, release, posted equivalent, or source-closure marker. The released symmetric-Mahler claim remains separately unassigned after this track's mandatory handoff and is not silently resumed.

`POSTED.md` contains no posting of the Makai source statement or the frustum result below. The campaign settled registries contain no full Makai resolution. Existing posted Gaussian and personal manuscripts remain excluded.

## 2. Runtime/model capability honesty

The exposed scheduling interface still offers task title, prompt, schedule/relative start, timing mode, enabled state, and update/list operations. It exposes **no model selector and no reasoning-effort selector**, and it provides no authenticated guarantee that a scheduled run executes for a specified duration. Thus `GPT-6 / maximum` remains a prompt request only; this report uses the actual model identity available to the run and `UNVERIFIED` for reasoning telemetry.

Changing this into a guaranteed GPT-6/maximum scheduled property would require the product/runtime to expose authenticated model and reasoning fields (or an authorized backend/task context that does). The earlier `You cannot modify this task` result for P26 is a permissions/context issue, not something a repository edit can fix. The compliant route is the task's authorized account/workspace interface or platform support; do not bypass it and do not create a duplicate task. The current root ledger records that P26 was later editable from a different authorized context, illustrating the correct distinction. This run did not create, modify, disable, re-enable, or probe another schedule.

## 3. Source statement and fixed metric

The admitted source is Arkadiy Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991 (2025), Conjecture 1.3, attributed there to Makai Jr.:

\[
\boxed{|K|\,|(K-K)^\circ|\ge \frac{n+1}{n!}}
\tag{M}
\]

for every convex body `K subset R^n`, with equality iff `K` is a simplex.

The frozen source metric is

`d_Makai = largest d for which (M) is rigorously established for every convex body in R^d`.

Incoming and outgoing values are

\[
\boxed{d_{\rm Makai}:2\longrightarrow2.}
\]

This is **NO MOVEMENT** of the source metric. The planar case is the sharp Eggleston theorem. The preceding HARD7-01 run proved the three-dimensional conjectured bound for every pyramid, but that restricted theorem correctly left `d_Makai=2`.

## 4. Current-literature check, 20 September 2026

Fresh bounded searches during this invocation used the terms

- `Makai frustum convex body difference body polar volume product`;
- `Makai Jr pyramid frustum volume product convex body`;
- `polar difference body frustum convex body Makai`;
- `convex hull homothetic bases Makai conjecture difference body`;
- `Makai Jr 2/3 convex body 2026`.

The search again recovered Aliev's 2025 paper, whose three-dimensional theorem assumes tetrahedral symmetry, and current MathDB material still labels the general Makai conjecture open. It also recovered the planar Eggleston/stability literature and older geometry-of-numbers work around Makai's conjecture, but no theorem matching the positive-homothety-frustum class below. This is **bounded negative evidence only**. Priority/novelty of the restricted theorem remains `UNVERIFIED` until a dedicated literature audit and independent proof audit.

## 5. New-method work first: B18 / B6 / B24

The previous Makai run used B2/B5/B11. This run deliberately uses three fresh moves on this target.

The route was written **before code** at

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1201Z__makai_prismoid_frustum_idea_before_code.md`

creation commit

`d6b79ec6a296ac1a3add8ae8169cf3ca53fca880`,

and was read back successfully.

### B18 — say it in another language

The difference-body polar is rewritten fibrewise using support functions. This gives a closed planar formula for arbitrary prismoids, not merely the homothetic subclass.

### B6 — deform to a solvable point

For homothetic bases, introduce the scale ratio `lambda` and deform continuously between the already solved pyramid endpoint `lambda=0` and the prism endpoint `lambda=1`. The entire path is exactly solvable.

### B24 — find the extremal object

The resulting one-variable factor is minimized at the pyramid endpoint. Consequently truncating the cone cannot create a counterexample; the source equality case collapses back to the tetrahedron.

## 6. Exact support-fibre identity for every three-dimensional prismoid

Let `A,C subset R^2` be arbitrary planar convex bodies and set

\[
K=\operatorname{conv}(A\times\{0\},C\times\{1\}).
\tag{6.1}
\]

For `y in R^2` write

\[
p=h_A(y),\quad q=h_A(-y),\quad r=h_C(y),\quad s=h_C(-y).
\tag{6.2}
\]

Because a linear functional achieves its maximum on one of the two bases,

\[
h_K(y,t)=\max\{p,r+t\}.
\tag{6.3}
\]

Therefore

\[
h_{K-K}(y,t)=\max\{p,r+t\}+\max\{q,s-t\}.
\tag{6.4}
\]

Define the planar widths

\[
w_A(y)=p+q=h_{A-A}(y),\qquad
w_C(y)=r+s=h_{C-C}(y).
\tag{6.5}
\]

The switching points in (6.4) are

\[
\alpha=p-r,\qquad \beta=s-q.
\tag{6.6}
\]

If `alpha>=beta`, equivalently `w_A>=w_C`, then the minimum of (6.4) is `w_A`; if `alpha<=beta`, equivalently `w_C>=w_A`, its minimum is `w_C`. Hence the vertical polar fibre is nonempty exactly when

\[
\max\{w_A(y),w_C(y)\}\le1,
\tag{6.7}
\]

or equivalently

\[
y\in P:=(A-A)^\circ\cap(C-C)^\circ.
\tag{6.8}
\]

On either ordering of the switches, solving the two outer affine inequalities in (6.4) gives

\[
p+s-1\le t\le1-r-q,
\tag{6.9}
\]

whose length is

\[
2-(p+q)-(r+s)=2-w_A(y)-w_C(y).
\tag{6.10}
\]

Fubini therefore gives the exact identity

\[
\boxed{
|(K-K)^\circ|
=\int_{(A-A)^\circ\cap(C-C)^\circ}
\bigl(2-h_{A-A}(y)-h_{C-C}(y)\bigr)\,dy.
}
\tag{PF}
\]

This is a theorem for the full parameter family of prismoids. No discretization or finite sampling enters its proof.

The ordinary volume is equally explicit. Let `V(A,C)` denote planar mixed area in the convention

\[
|(1-z)A+zC|
=(1-z)^2|A|+2z(1-z)V(A,C)+z^2|C|.
\tag{6.11}
\]

Integrating the parallel sections gives

\[
\boxed{|K|=\frac{|A|+V(A,C)+|C|}{3}.}
\tag{PV}
\]

Thus the entire Makai problem for three-dimensional prismoids is reduced exactly to the planar mixed-area/polar-intersection inequality obtained by multiplying `(PF)` and `(PV)`. This reduction is left as the natural non-homothetic continuation, not claimed solved here.

## 7. Sharp theorem for every positive-homothety frustum

### Theorem

Let `K subset R^3` be the convex hull of two positively homothetic planar convex bodies lying in distinct parallel planes. Then

\[
\boxed{|K|\,|(K-K)^\circ|\ge\frac23.}
\tag{7.1}
\]

More precisely, after ordering the bases let `lambda in [0,1]` be the ratio of the smaller base to the larger. Then

\[
\boxed{
|K|\,|(K-K)^\circ|
\ge \frac13(1+\lambda+\lambda^2)(2-\lambda)
=\frac23+\frac{\lambda(1+\lambda-\lambda^2)}3.
}
\tag{7.2}
\]

For fixed `lambda`, (7.2) is sharp and equality in (7.2) holds exactly when the planar base is a triangle. Equality in the source bound (7.1) occurs exactly for `lambda=0` with triangular base, i.e. exactly for tetrahedra within this class.

### Proof

Affine invariance first removes irrelevant parameters. If the upper base is `a+lambda B`, the shear

\[
(x,z)\mapsto(x-za,z)
\]

removes `a`. If `lambda>1`, interchange the two bases and then apply a horizontal dilation, replacing `lambda` by `1/lambda`. Hence assume

\[
K=\operatorname{conv}(B\times\{0\},\lambda B\times\{1\}),
\qquad0\le\lambda\le1.
\tag{7.3}
\]

Put

\[
D=B-B,\qquad Q=D^\circ.
\tag{7.4}
\]

In `(PF)` we now have

\[
h_{\lambda B-\lambda B}=\lambda h_D,
\qquad
P=Q,
\]

and therefore

\[
|(K-K)^\circ|
=\int_Q\bigl(2-(1+\lambda)h_D(y)\bigr)\,dy.
\tag{7.5}
\]

Since

\[
Q=\{y:h_D(y)\le1\},
\]

`h_D` is exactly the Minkowski gauge of `Q`. For every planar convex body containing the origin, radial integration of the gauge gives

\[
\int_Q h_D(y)\,dy=\frac23|Q|.
\tag{7.6}
\]

Substitution into (7.5) yields

\[
\boxed{
|(K-K)^\circ|=\frac{2(2-\lambda)}3\,|(B-B)^\circ|.
}
\tag{7.7}
\]

The section at height `z` is

\[
(1-(1-\lambda)z)B,
\]

so

\[
\boxed{
|K|=\frac{1+\lambda+\lambda^2}{3}|B|.
}
\tag{7.8}
\]

Multiplying (7.7) and (7.8) gives the exact factorization

\[
|K|\,|(K-K)^\circ|
=\frac{2}{9}(1+\lambda+\lambda^2)(2-\lambda)
|B|\,|(B-B)^\circ|.
\tag{7.9}
\]

Eggleston's sharp planar theorem states

\[
|B|\,|(B-B)^\circ|\ge\frac32,
\tag{7.10}
\]

with equality iff `B` is a triangle. Hence

\[
|K|\,|(K-K)^\circ|
\ge\frac13(1+\lambda+\lambda^2)(2-\lambda).
\tag{7.11}
\]

Finally

\[
(1+\lambda+\lambda^2)(2-\lambda)-2
=\lambda(1+\lambda-\lambda^2)\ge0
\tag{7.12}
\]

for `0<=lambda<=1`, with equality only at `lambda=0`. Equations (7.10)--(7.12) prove both (7.1) and the stated equality cases. `QED`.

### Interpretation

The exact class minimum is controlled by

\[
F(\lambda)=2+\lambda+\lambda^2-\lambda^3.
\]

Since `F(lambda)>2` for every `lambda>0`, cutting the apex off a cone moves strictly **away** from a Makai counterexample after optimizing over the planar base. In this family the true extremal mechanism is exactly the simplex endpoint, matching the source conjecture.

## 8. Verification artifact — deliberately secondary to the proof

Only after the route/proof was written, I added

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1208Z__makai_prismoid_frustum_check.py`

at commit

`9828cdd6b7977bc2279bcb70e616d5b714ff5d4c`.

It was executed locally with exact `Fraction` arithmetic. The archived output is

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T1208Z__makai_prismoid_frustum_check.out`

at commit

`a0192c3fe8b99f62876de63fe0445ccc4d5e9f37`.

The self-check verifies the exact polynomial factorization, endpoint values, and 841 exact rational instances of the piecewise-linear fibre algebra. It explicitly labels those 841 cases as a **finite self-check, not an exhaustive convex-body certificate**. The output ends

`ALL_EXACT_CHECKS_PASS = True`.

The theorem-sized claim rests on the written proof in Sections 6--7, not on the finite sample.

## 9. What moved mathematically, and what did not

Source-relevant metric:

\[
\boxed{d_{\rm Makai}:2\to2\quad\text{(NO MOVEMENT).}}
\]

Restricted scope genuinely enlarged:

- incoming theorem: all three-dimensional **pyramids**;
- outgoing theorem: all three-dimensional convex hulls of two **positively homothetic planar bases in parallel planes**, with the sharp ratio-dependent lower bound (7.2);
- outgoing exact reduction: every arbitrary two-base **prismoid** is reduced to `(PF)+(PV)`.

No claim is made that this proves the full three-dimensional conjecture, that the restricted theorem is novel, or that a bounded negative search is a priority certificate.

This is the second consecutive Makai run with unchanged source metric after admission. It does **not yet** trigger the three-unchanged-run stuck protocol. If the next ordinary research iteration also leaves `d_Makai=2`, the following invocation must respect Section I rather than manufacture another nearby lemma.

## 10. Next nonrepeating moves if the target continues

The next ordinary research triple is reserved as **B1 / B20 / B30**:

- **B1:** change category again, using `(PF)+(PV)` as a two-dimensional mixed-area inequality for arbitrary prismoids;
- **B20:** identify exactly why the homothetic proof fails when `(A-A)^circ` and `(C-C)^circ` are not nested/homothetic;
- **B30:** solve one localized non-homothetic regime (for example comparable/nested central symmetrals or one triangular base) rather than adding another global conjectural lemma.

If source-metric stagnation reaches the Section-I threshold, that protocol supersedes this ordinary continuation.

## 11. Ledger delta for shared maintainer

```text
track: HARD7-01
source_target: MAKAI-POLAR-DIFFERENCE-BODY
owner: HARD7-01
status: PARTIAL / SOURCE OPEN / CLAIMED
metric: d_Makai
before: 2
after: 2
movement: NO MOVEMENT
methods: B6 / B18 / B24
new_full_parameter_result: Makai bound for all 3D positive-homothety frusta; sharp fixed-ratio bound
new_reduction: exact support-fibre formula PF and mixed-area volume formula PV for arbitrary 3D prismoids
checker_scope: exact algebra self-check only; 841 rational fibre tuples, not exhaustive convex-body proof
stuck_state: unchanged_run_2_for_current_Makai_target
next_methods_if_ordinary: B1 / B20 / B30
```
