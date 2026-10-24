# B13 — the fixed shared-core semigroup has the sharp scalar ceiling

**Outcome:** `ESSENTIAL_STEP_APPLIED / FIXED_SHARED_CORE_SEMIGROUP_SHARPENED`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were used, but no authenticated mathematical/cognitive receiver context was retrieved.

## 1. Live target and why this is not another lower-bound recurrence

The live owner target is the all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for one symmetric nonnegative finite-centre potential and every Boolean gate/product bias. On balanced gates at uniform input this requires

\[
H(G)\le \Gamma(1/2)[I(G)-1],
\qquad
R(G):=\frac{H(G)}{I(G)-1}\le \Gamma(1/2).
\tag{1.1}
\]

The old read-once centre/decomposable-AND extremality is already refuted, so this run does not repeat that falsification. The current lower-bound family uses the same exact nine-host shared-coordinate core together with balanced disjoint compositions and partial spines. Two recent peer results left a small but real mismatch:

1. account04/B15, `20260922T020955Z-adaptive-depth-shared-core-ceiling/REPORT.md` (reported blob `f5347c63a8ab43f9c6a4b58850643b69bc50d551`), proves a **sharp scalar maximum only on** `0<=b<=1/4`:
   \[
   \sup_{0\le b\le1/4}\frac{K(b)}{133/128}
   <M_+:=
   6.5218512130128777236515044002391819664714641388011273386\ldots .
   \tag{1.2}
   \]
   It also certifies the unique maximizer in
   \[
   0.002713295<b_*<0.002713296.
   \tag{1.3}
   \]
2. account04/B17, `20260922T021328Z-shared-graft-semigroup-ceiling/REPORT.md` (blob `d79b4923409f6856c5408bf6d45225750a736abc`), proves closure under **arbitrary heterogeneous balanced disjoint composition plus the same shared-core transform**, but uses the coarser full-range scalar cap `6.5218513` on `0<=b<=1`.

The missing implication is therefore precise: does a selected singleton coefficient `b>1/4` hide a larger forcing value and prevent (1.2) from being used for the entire semigroup? This run answers **no** with a rigorous interval certificate.

## 2. Exact shared-core forcing and the peer lower point

Write

\[
\alpha=\frac9{256},\qquad d_0=\frac{133}{128},
\]

\[
K(b)=H_{\rm core}(b)
+\alpha\bigl[-\phi(b^2)+16(1-b^2)\bigr],
\qquad \phi(t)=-t\log_2 t.
\tag{2.1}
\]

For the fixed source-valid shared-core transform `T(h,b)`, account04/B17 proves exactly

\[
H(T)=\alpha H(h)+K(b),
\qquad
I(T)-1=\alpha[I(h)-1]+d_0.
\tag{2.2}
\]

The account04/B15 checker gives at
\(
\ell=0.002713295
\)

the rigorous lower endpoint

\[
K(\ell)>
6.7766110260211932590896736474059853605974065471905310\ldots .
\tag{2.3}
\]

Thus it is enough to certify

\[
\sup_{1/4\le b\le1}K(b)
<6.7766110260211932590,
\tag{2.4}
\]

because the right side of (2.4) is already strictly below the source-certified value (2.3).

## 3. PROVED: there is no hidden maximum for `b>=1/4`

The source core has nineteen exact Walsh numerator classes `(A,Q,multiplicity)`, with amplitudes

\[
\frac{A+bQ}{512}.
\]

For a rational tangent centre `b_0`, concavity of
\(
\phi(p)=-p\log_2p
\)
gives

\[
\phi(p(b))
\le
\phi(p(b_0))
+\phi'(p(b_0))[p(b)-p(b_0)].
\tag{3.1}
\]

At the three centres used below every nonzero source mass is below `1/4`, so \(\phi'(p(b_0))>0\). Since each `p(b)` is a square of an affine function, the right side of (3.1) is a convex quadratic in `b`. The scalar term

\[
g(b)=-\phi(b^2)+16(1-b^2)
\]

has

\[
g''(b)=2\log_2(b^2)+\frac6{\ln2}-32<0
\qquad(0<b\le1),
\tag{3.2}
\]

so its tangent is a global upper bound. Therefore the sum of all nineteen spectral tangents plus the `g` tangent is a convex quadratic majorant for `K` on each row, and it suffices to check row endpoints.

The standard-library exact/interval checker covers the stronger interval `[0.19,1]` using only

\[
[0.19,0.36],\quad[0.36,0.65],\quad[0.65,1]
\tag{3.3}
\]

with tangent centres `0.1,0.2,0.4`, respectively. Every endpoint majorant is strictly below the rational threshold

\[
L:=6.7766110260211932590.
\tag{3.4}
\]

The worst endpoint is `b=0.36`, where the rigorous upper majorant is

\[
6.77571616838039545360767082649034415683734093388943956905862846\ldots,
\tag{3.5}
\]

leaving the positive gap

\[
L-Q(0.36)
>
0.00089485764079780539232917350965584316265906611056043.
\tag{3.6}
\]

Hence

\[
\boxed{
\sup_{1/4\le b\le1}K(b)<L<K(\ell).
}
\tag{3.7}
\]

This is not a grid observation. It is a complete interval certificate on the whole outer range.

Combining (3.7) with the account04/B15 theorem on `[0,1/4]` proves the global scalar statement

\[
\boxed{
\sup_{0\le b\le1}\frac{K(b)}{d_0}
<
M_+
=
6.5218512130128777236515044002391819664714641388011273386\ldots .
}
\tag{3.8}
\]

The exact failed possibility is therefore **REFUTED**: a selected singleton `b>1/4` cannot produce a larger forcing level for this fixed shared core.

## 4. PROVED: sharp cap for the whole fixed-core semigroup

Now apply the account04/B17 semigroup theorem, rather than merely citing it. For a balanced Boolean outer gate `f` with balanced disjoint children `g_i`, define

\[
E_C(g)=H(g)-C[I(g)-1].
\]

The peer theorem proves the exact cocycle

\[
E_C(f(g_1,\dots,g_m))
=
E_C(f)+\sum_i \operatorname{Inf}_i(f)E_C(g_i).
\tag{4.1}
\]

All weights are nonnegative, so disjoint composition preserves `E_C<=0`. For the shared transform, (2.2) gives

\[
E_C(T(h,b))
=
\alpha E_C(h)+K(b)-d_0C.
\tag{4.2}
\]

Set `C=M_+`. By (3.8), the second term in (4.2) is strictly negative for every possible Boolean singleton coefficient `0<=b<=1`. Thus any seed family with `R<=M_+`, closed under arbitrary heterogeneous balanced disjoint composition and the exact fixed nine-host shared-core transform, stays below `M_+` for every finite construction history.

### Theorem 4.1 — sharp fixed-shared-core semigroup ceiling

For the entire source-valid semigroup generated from the known balanced monotone seeds by arbitrary balanced disjoint functional composition and the fixed nine-host shared-core transform,

\[
\boxed{
R(G)=\frac{H(G)}{I(G)-1}
<6.52185121301287772365150440023918196647146413881.
}
\tag{4.3}
\]

This strictly sharpens the previous semigroup-wide certified cap `6.5218513`. It covers full self-composition, changing self-composition depths, distinguished spines, heterogeneous children, arbitrary orderings of those operations, and shared-core applications using **any** selected singleton coefficient in `[0,1]`.

It does not cover a different shared core, a new prime seed outside the cap, or a biased product obstruction.

## 5. How little room remains in this mechanism

The newest compatible explicit/adaptive lower construction is account02/B17,

`20260922T021155Z-spine-shared-graft/REPORT.md`, blob `6b891bc8972db1bc9f55a5b3f49e6501a625fed4`.

Its source-valid finite iterates converge to a forcing level with rigorous lower endpoint

\[
R_{\rm spine,lim}>
6.5218511673423727025654896282010361877746102003501.
\tag{5.1}
\]

Every finite iterate belongs to the semigroup above, so the semigroup supremum lies in the interval implied by (4.3)-(5.1), whose width is less than

\[
\boxed{
4.5670505021086014772038145778696854\times10^{-8}.
}
\tag{5.2}
\]

In the owner's old read-once-centre margin units

\[
c_G=4(R(G)-6.4548),
\tag{5.3}
\]

the same entire mechanism is trapped between

\[
 c_{\rm lower}>0.2682046693694908102619585128041447510984408014004
\tag{5.4}
\]

and

\[
 c_{\rm upper}<0.26820485205151089460601760095672786588585655524,
\tag{5.5}
\]

with margin headroom below

\[
\boxed{1.8268202008434405908815258311478742\times10^{-7}.}
\tag{5.6}
\]

This is a structured-family statement, not a universal FEI upper bound.

## 6. Exact old/new implication and next attack

- `exact_candidate_version`: the live all-gate inequality `(G)`; within the falsification programme, the fixed nine-host shared-core semigroup generated under balanced disjoint composition.
- `prior_missing_implication`: account04/B15 had the sharp scalar forcing ceiling only on `b in [0,1/4]`, while account04/B17's semigroup closure allowed arbitrary selected `b in [0,1]` and therefore used the coarser `6.5218513` cap.
- `new_proved_inference`: the interval certificate (3.7) proves the global scalar maximum is already in `[0,1/4]`; consequently the sharp B15 ceiling applies to the entire B17 semigroup, yielding (4.3).
- `exact_failed_claim`: a coefficient `b>1/4` might hide a larger fixed-core forcing value and invalidate the sharp scalar cap for the whole semigroup. **REFUTED.**
- `replacement_obligation`: further falsification must change the source core/host geometry, inject a genuinely stronger seed/prime gate, or use a nonuniform bias; repeating or heterogenizing this fixed-core semigroup is now quantitatively exhausted to (5.2).
- `consumed_peer_artifact`: account04/B15 `20260922T020955Z-adaptive-depth-shared-core-ceiling/REPORT.md`, account04/B17 `20260922T021328Z-shared-graft-semigroup-ceiling/REPORT.md`, and account02/B17 `20260922T021155Z-spine-shared-graft/REPORT.md`.
- `applied_to_claim`: B15's strong-concavity/maximizer certificate is extended from `[0,1/4]` to the global Boolean singleton range by the new outer-range tangent certificate, then inserted into B17's exact `E_C` semigroup cocycle.
- `remaining_implication`: full FEI still needs one finite all-gate potential/upper bound, or a stronger counterexample mechanism. Nothing here bounds gates outside this fixed-core semigroup.
- `next_recipient`: primary `account03/B18` (all-gate integrator), secondary `account04/B17` (semigroup owner) and `account02/B17` (spine construction owner).
- `full_problem_change`: **OPEN -> OPEN**; one large falsifier mechanism is sharply capped, but no universal dimension-independent upper constant is proved.

## 7. Verification and scope

`CHECKER.py` is standard-library only. It reuses the exact nineteen source multiplicity classes and directed-rounding rational atanh logarithm enclosures. It independently checks the three tangent-majorant rows covering `[0.19,1]`, verifies every endpoint lies below (3.4), and records `PASS`. The finite certificate is used only for (3.7); the semigroup closure is the analytic argument (4.1)-(4.2).

Executed checker SHA-256: `527246958beda10948226fc0f36f5ec4bbe5202e7c323bdb1ea9618f9fedb303`.  
Captured output SHA-256: `b8b7f7bdabb79cb8dd9e2c8deb7d1e803987b9f1a0920c3d2619cbf229ac8c43`.

Manual scoped privacy/provenance review: mathematical formulas and sanitized repository-relative provenance only; no credentials, scheduler identifiers, machine paths, raw private transcripts, benchmark gold, unrelated private data, email/Drive action, paid API/model call, remote workflow dispatch, or permission changes. No publication-priority or novelty claim is made.
