# B17 — a global ceiling for the source-valid shared-graft semigroup

**Run:** `20260922T021328Z-b17-fei-r16`  
**Outcome:** `ESSENTIAL_STEP_APPLIED` — the fixed-depth-four tail closure is strengthened to a cap for **every** iteration that uses the same source-valid nine-host shared-core transform, interspersed with arbitrary balanced disjoint compositions.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Authenticated repository sources were read through the authorized connector; no authenticated mathematical-brain retrieval/context was consumed.

## 1. Live owner target and named peer input

The latest owner message supersedes the stale packet-only/interface-D wording and asks all FEI workers to converge on the equivalent all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{1.1}
\]

for every Boolean gate and product bias vector.  At uniform bias for a balanced gate this specializes exactly to

\[
H(G)\le \Gamma(1/2)\,[I(G)-1].
\tag{1.2}
\]

Thus

\[
R(G):=\frac{H(G)}{I(G)-1}
\tag{1.3}
\]

is the correct balanced obstruction to the center cap.

The named newest compatible other-account B15 result consumed in this run is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T012556Z-iterated-shared-graft/REPORT.md`, blob `aff93b999538a8b8baeab270ff739f405c79ee7c`.

It uses the exact source-valid shared-coordinate construction and certifies an actual finite balanced monotone Boolean gate `F6` with

\[
R(F_6)>6.5218509495504481848401605388605.
\tag{1.4}
\]

Its explicit replacement obligation is to control the **whole iterated shared-core obstruction** before freezing another all-gate center cap.  The immediately preceding B17 run then pushed once more to `F7`, proving

\[
R(F_7)>
6.521850949550448184840160538860511501350329679
\tag{1.5}
\]

and closed only the unchanged depth-four tail.  This run changes the argument: it derives a one-dimensional cap that applies to **all self-composition depths and all balanced disjoint-composition histories** using the same shared core.

No KL/relative-entropy credit from the older arithmetic-remainder representation is discarded or set to zero here.  The later owner target evaluates the source-valid Boolean gate directly in the exact all-gate normalization, so that older representation is bypassed rather than weakened.

## 2. Exact source transform

Write

\[
\alpha=\frac9{256},\qquad d_0=\frac{133}{128},
\qquad B=\frac{257}{256},
\]

and

\[
\phi(t)=-t\log_2t.
\]

For the fixed nine-bit source core let

\[
K(b)
=H_{\rm core}(b)
+\alpha\bigl[-\phi(b^2)+16(1-b^2)\bigr].
\tag{2.1}
\]

The source-exact shared-host theorem applies to any balanced monotone Boolean gadget `h` with selected singleton Fourier coefficient `b` and produces another actual balanced monotone Boolean gate `T(h,b)` satisfying

\[
\boxed{H(T(h,b))=\alpha H(h)+K(b),}
\tag{2.2}
\]

\[
\boxed{I(T(h,b))-1=\alpha\,[I(h)-1]+d_0.}
\tag{2.3}
\]

For a Boolean singleton coefficient of a monotone balanced gate we have `0<=b<=1`.  These are exact coefficient-by-coefficient identities; no spectral probability-law relaxation is introduced.

## 3. Cap-preserving shared-graft lemma

The key replacement observation is elementary once (2.2)--(2.3) are kept in their exact normalization.

**Lemma.** Fix `C>0`.  If a balanced monotone Boolean gadget `h` satisfies

\[
H(h)\le C[I(h)-1]
\tag{3.1}
\]

and its selected coefficient `b` satisfies

\[
K(b)\le d_0 C,
\tag{3.2}
\]

then

\[
H(T(h,b))\le C[I(T(h,b))-1].
\tag{3.3}
\]

**Proof.** Substitute (3.1) and (3.2) in (2.2):

\[
H(T)
\le \alpha C[I(h)-1]+d_0C
=C\{\alpha[I(h)-1]+d_0\}
=C[I(T)-1].
\]

This proof does not depend on the size of `I(h)`, the previous number of grafts, or a chosen self-composition depth.  Therefore a **uniform scalar upper bound on `K(b)/d_0` closes the entire source transform**, not merely one recurrence.

## 4. Exact closure under heterogeneous balanced disjoint composition

The other operation used to amplify these gates is also cap-preserving at the same `C`.

Let a balanced Boolean outer gate `f` receive balanced Boolean gates `g_i` on pairwise disjoint variable blocks, and set

\[
w_i=\operatorname{Inf}_i(f).
\]

The standard balanced composition identities are

\[
H(f(g_1,\ldots,g_m))
=H(f)+\sum_iw_iH(g_i),
\]

\[
I(f(g_1,\ldots,g_m))
=\sum_iw_iI(g_i).
\]

Since `sum_i w_i=I(f)`, the balanced excess

\[
E_C(g):=H(g)-C[I(g)-1]
\]

obeys the exact cocycle

\[
\boxed{
E_C(f(g_1,\ldots,g_m))
=E_C(f)+\sum_iw_iE_C(g_i).
}
\tag{4.1}
\]

All weights are nonnegative.  Hence arbitrary **heterogeneous** balanced disjoint compositions of gates with `R<=C` again have `R<=C`.

Combining (3.3) and (4.1), it remains only to certify one scalar inequality for the fixed shared core.

## 5. Rigorous scalar ceiling for the shared core

The checker proves

\[
\boxed{
K(b)<\frac{133}{128}\,(6.5218513)
\qquad\text{for every }0\le b\le1.
}
\tag{5.1}
\]

Equivalently,

\[
\boxed{
\sup_{0\le b\le1}\frac{K(b)}{133/128}<6.5218513.
}
\tag{5.2}
\]

The certificate uses the exact 19 multiplicity classes `(A_S,Q_S)` of the source nine-bit core.  Each core mass has the form

\[
p_S(b)=\left(\frac{A_S+bQ_S}{512}\right)^2.
\]

For a rational center `b_0`, concavity of `phi` gives the global tangent bound

\[
\phi(p_S(b))
\le
\phi(p_S(b_0))
+\phi'(p_S(b_0))[p_S(b)-p_S(b_0)].
\tag{5.3}
\]

All chosen centers have nonzero `p_S(b_0)<1/4` for every nonzero source class, hence `phi'(p_S(b_0))>0`.  The right side of (5.3) is therefore a convex quadratic in `b`.

The remaining scalar term

\[
g(b):=-\phi(b^2)+16(1-b^2)
=b^2\log_2(b^2)+16(1-b^2)
\]

is globally concave on `(0,1]`, because

\[
g''(b)=2\log_2(b^2)+\frac6{\ln2}-32<0.
\tag{5.4}
\]

Its tangent at `b_0` is therefore a global upper bound and is linear in `b`.  Adding all source-class tangents produces a **convex quadratic majorant** `Q_{b_0}(b)` for `K(b)`.  Consequently the maximum of `Q_{b_0}` on any interval occurs at an endpoint.

An 18-interval rational cover of `[0,1]`, with outward-rounded 100-digit logarithm intervals, checks those endpoint inequalities.  The target threshold is exactly

\[
\frac{133}{128}\,6.5218513
=6.77661111640625.
\]

The worst certified tangent endpoint is

\[
6.7766111126321052741643755806071340935940561682871\ldots,
\]

leaving the rigorous positive gap

\[
3.7741447258356244193928659064059438317\times10^{-9}.
\tag{5.5}
\]

A separate near-maximizer probe at the rational point

\[
b=\frac{2713295}{10^9}
\]

gives

\[
\frac{K(b)}{133/128}
\in
[6.52185121301287772303367087870651222674036118827359\ldots,
 6.52185121301287772303367087870651222674036118827360\ldots].
\tag{5.6}
\]

The probe is not used to prove (5.2); it shows the certified `6.5218513` cap is already within about `8.7e-8` of the scalar source-core optimum.

## 6. New theorem: the whole source-valid semigroup is capped

Define `S` to be any class of finite balanced monotone Boolean gates such that every seed in `S` has

\[
R=H/(I-1)\le6.5218513.
\]

Close `S` under the following two source-valid operations:

1. arbitrary balanced disjoint functional composition, with different children allowed;
2. the fixed nine-host shared-core transform `T(h,b)` from the source construction, using any selected singleton coefficient of the current gate.

Then Sections 3--5 prove by induction on the finite construction history that **every** resulting gate satisfies

\[
\boxed{
\frac{H(G)}{I(G)-1}<6.5218513.
}
\tag{6.1}
\]

This is stronger than the preceding fixed-depth-four tail estimate.  It excludes every future attempt that merely changes the self-composition depth, alternates depths, uses heterogeneous disjoint children, or otherwise changes the order of these two operations while keeping the same nine-host source transform.

The existing actual Boolean gate `F7` supplies the lower side

\[
6.521850949550448184840160538860511501350329679
< R(F_7)
<6.5218513.
\tag{6.2}
\]

Thus the **entire remaining room for this source-valid mechanism** is less than

\[
\boxed{
3.50449551815159839461139488498649670321\times10^{-7}.
}
\tag{6.3}
\]

In the owner's historical `C_0=6.4548` margin units, every gate in this semigroup asks for

\[
c_G=4(R-C_0)<0.2682052,
\tag{6.4}
\]

while `F7` already gives the certified lower margin

\[
c_{F_7}>0.2682037982017927393606421554420460054.
\tag{6.5}
\]

So the possible old-reference margin improvement remaining inside this entire mechanism is below about `1.402e-6`.

## 7. What is closed, and what remains

**Closed at the stated exact scope.**  Computing further `F8,F9,...` at depth four is unnecessary, and so is changing only the self-composition depth or mixing disjoint balanced copies before applying the same nine-host shared core.  None of those operations can cross `R=6.5218513` from seeds already below it.

**Not closed.**  This is not a universal FEI upper bound and does not prove a finite all-gate potential.  A stronger adversary may still come from a different shared host/core, a biased product point, a composition-prime interference mechanism outside this semigroup, or another exact Boolean construction.  The owner target therefore remains the all-gate extremal/falsification problem, but one large family of candidate amplifiers is now eliminated globally rather than one depth at a time.

## 8. Verification and provenance

`CHECKER.py` is a standard-library exact/interval certificate.  Its source uses exact `Fraction` data for the 19 source multiplicity classes and outward-rounded `Decimal` intervals for every logarithm.  It verifies the complete rational cover, the global concavity calculation for `g`, the positive worst endpoint gap (5.5), and the near-maximizer enclosure (5.6).  `CHECK_OUTPUT.txt` records `PASS` and the quoted values.

The calculation is source-bound and self-checked; no independent end-to-end peer review is claimed here.  No novelty or publication-priority claim is made.  Scoped content review found only mathematical formulas, sanitized repository-relative provenance, and nonsecret hashes/identifiers; no credentials, scheduler identifiers, machine paths, unrelated private material, benchmark gold, email/Drive action, paid compute, workflow dispatch, or public-release instruction is present.

**Final status:** `ESSENTIAL_STEP_APPLIED` for the shared-graft replacement obligation; **full FEI remains OPEN / NOT PROVED**.
