# B18 — the known shared-core obstruction class is globally safe at C† = 6.521851214

**Classification:** `ESSENTIAL_STEP_APPLIED / SOURCE-MECHANISM_CLOSED_AT_FIXED_CENTER`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live target and exact inherited dependencies

Fresh owner control revision `2026-09-22.2` converges all FEI workers on the all-gate potential inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for one symmetric nonnegative finite-cap potential and every Boolean gate, every arity, and every interior product bias vector. The source-exact gate reformulation proves that this is equivalent to full FEI. Nothing below claims `(G)` for arbitrary gates.

This run consumes the following exact completed dependencies rather than reopening their proofs.

1. `account01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`, report blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`. It fixes the stable candidate
   \[
   C_*=6.5218512,
   \qquad
   \Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p),
   \qquad a_*=0.2682048,
   \]
   and reduces its proposed universal closure to the still-open composition-prime all-bias gate inequality.

2. `account04/B13/20260922T0224Z-decomposition-prime-localization/REPORT.md`, report blob `8fc90907a671d5a7aadc565c0a903fc7786d2390`. For balanced disjoint composition it proves the exact defect conservation
   \[
   D(F)=D(G)+\sum_i \operatorname{Inf}_i(G)D(H_i),
   \]
   and therefore exact convexity of the balanced excess ratio and additive conservation of `C D-H`.

3. `account04/B15/20260922T020955Z-adaptive-depth-shared-core-ceiling/REPORT.md`, report blob `f5347c63a8ab43f9c6a4b58850643b69bc50d551`. For the exact source-bound nine-host shared-core transform it proves strict concavity of the scalar forcing function on `[0,1/4]` and the rigorous global bound on that interval
   \[
   \frac{K(b)}{d_0}<M_+
   :=6.52185121301287772365150440023918196647146413881,
   \qquad d_0=\frac{133}{128}.
   \tag{1.1}
   \]

4. `account02/B18/20260922T030354Z-global-shared-core-ceiling/CHECKER_GLOBAL.py`, checker blob `5c267837d86d4d8c18d53faad99e09b89dfd8149`, with preserved output blob `087edddbf95400a4bdb349507a115c984bd53ab3`. Its rational interval certificate proves
   \[
   K'(b)>0\quad(-1\le b\le0),
   \qquad
   K'(b)<0\quad(1/4\le b\le1).
   \tag{1.2}
   \]
   Together with item 3 this makes (1.1) a global bound for every signed singleton coefficient `b in [-1,1]`.

5. `account02/B16/20260922T031545Z-limit-prime-shared-core-threat-corridor/REPORT.md`, report blob `7b8836311af20ce7c0342e3deaeb4869651d2cfe`. It records the exact shared-core defect cocycle at `C_*` and localizes any `C_*` heterogeneous counterexample to a tiny near-tight input/singleton corridor.

6. `account04/B12/20260922T0254Z-and-atom-stopping/REPORT.md` and `account04/B14/20260922T024035Z-common-gamma-terminal-subtraction/REPORT.md`, report blobs `8a35d08850c8bf38a36c58af4ee3dcd670fa0de9` and `71523d7c82657e78141eea99278f3efb82680713`. They close the explicit prime `G10` physical stopping corridor under the same quadratic-lift framework.

The older mixed-curvature identity and exact zero-depth one-point classification remain valid and are preserved. No step below assumes the false bridge `sum d_i=O(J)`, the false prescribed-coordinate erasure bound, or the refuted old AND/read-once universal candidate.

## 2. Raise the center by only 1.4e-8

Define

\[
\boxed{C^\dagger:=6.521851214}
\tag{2.1}
\]

and

\[
\Gamma^\dagger(p)
:=\Gamma_{\rm RO}(p)+a^\dagger p(1-p),
\qquad
\boxed{a^\dagger=4(C^\dagger-6.4548)=0.268204856.}
\tag{2.2}
\]

Thus

\[
C^\dagger-C_*=1.4\times10^{-8},
\qquad
a^\dagger-a_*=5.6\times10^{-8}.
\tag{2.3}
\]

The global scalar certificate gives the strict numerical gap

\[
\boxed{
C^\dagger-M_+
=9.8712227634849559976081803352853586119\times10^{-10}>0.
}
\tag{2.4}
\]

This tiny increase is enough to remove the entire heterogeneous-singleton threat left at `C_*`.

## 3. Exact shared-core cocycle at an arbitrary center

Let `h` be a balanced Boolean input gadget to the exact nine-host shared-core transform. Put

\[
\delta(h)=I(h)-1,
\qquad
\Delta_C(h)=C\delta(h)-H(h).
\]

For a designated singleton Fourier coefficient `b`, the source transform has the exact identities

\[
H(T(h,b))=\alpha H(h)+K(b),
\qquad
\delta(T(h,b))=\alpha\delta(h)+d_0,
\tag{3.1}
\]

where

\[
\alpha=\frac9{256},
\qquad d_0=\frac{133}{128}.
\]

Therefore for **every real center C**, not only `C_*`,

\[
\boxed{
\Delta_C(T(h,b))
=
\alpha\Delta_C(h)+d_0\left(C-\frac{K(b)}{d_0}\right).
}
\tag{3.2}
\]

This is an identity obtained by subtracting the two equalities in (3.1). It has no hidden positive-part estimate and no discarded terminal term.

## 4. New theorem — global fixed-center safety of the source-bound shared-core transform

### Theorem 4.1

For every balanced Boolean input gadget `h`, every source-valid designated singleton coefficient `b` (hence automatically `-1<=b<=1`), if

\[
\Delta_{C^\dagger}(h)\ge0,
\]

then

\[
\boxed{
\Delta_{C^\dagger}(T(h,b))
>
1.0256817402683587091264749879632442932\times10^{-9}.
}
\tag{4.1}
\]

In particular the output is strictly `C^dagger`-safe, even if the input is exactly tight.

### Proof

By the global signed-scalar certificate, (1.1)-(1.2),

\[
\frac{K(b)}{d_0}<M_+<C^\dagger
\qquad(-1\le b\le1).
\]

Apply (3.2):

\[
\Delta_{C^\dagger}(T(h,b))
\ge d_0(C^\dagger-M_+).
\]

Direct exact-decimal propagation gives

\[
\frac{133}{128}(C^\dagger-M_+)
=1.025681740268358709126474987963244293267734375\times10^{-9},
\]

which proves (4.1). QED.

### What this closes

The account02/B16 `C_*` threat corridor required simultaneously

\[
0\le\Delta_*(h)<3.84603\times10^{-7}
\]

and a singleton near the scalar maximizer. At `C^dagger` the corridor disappears completely: no amount of tuning `b`, and no exactly tight input gadget, can make one source-bound shared-core application negative.

This is stronger than the earlier integer-depth safety theorem because `h` may now be an **arbitrary balanced Boolean gadget**, not an iterate of the same shared-core family, and `b` may have either sign anywhere in its full Boolean range.

## 5. New closure theorem — arbitrary alternation with balanced disjoint composition

Let `C=C^dagger`. The exact account04/B13 composition theorem gives, for a balanced disjoint composition

\[
F=G(H_1,\ldots,H_m),
\]

with every factor balanced,

\[
\boxed{
\Delta_C(F)
=
\Delta_C(G)+
\sum_i \operatorname{Inf}_i(G)\Delta_C(H_i).
}
\tag{5.1}
\]

All coefficients are nonnegative. Hence balanced disjoint composition preserves `C^dagger`-safety.

Combine (5.1) with Theorem 4.1.

### Corollary 5.1

Start from any finite collection of balanced Boolean seed gates satisfying

\[
H(h)\le C^\dagger[I(h)-1].
\]

Generate new balanced gates by any finite sequence, in any order, of

1. arbitrary disjoint balanced composition of previously generated gates, and
2. the exact source-bound nine-host shared-core transform with **any** source-valid designated singleton coefficient.

Then every generated gate satisfies

\[
\boxed{H(F)\le C^\dagger[I(F)-1].}
\tag{5.2}
\]

Moreover every actual shared-core application contributes a strict positive defect of at least the amount in (4.1), before subsequent nonnegative composition weights are applied.

Thus the two mechanisms that generated the strongest current explicit balanced lower-bound family — disjoint balanced composition and the nine-host shared-core graft — cannot bootstrap past `C^dagger`, even when they are heterogeneously interleaved with arbitrary safe balanced gadgets. This strictly extends the earlier fixed-depth, adaptive-integer-depth, and same-family tail closures.

## 6. Compatibility with the explicit G10 physical corridor

The B14 common-potential terminal-subtraction theorem already proves the `G10` stopped block has positive slack under `a_*=0.2682048`. Since

\[
a^\dagger-a_*=5.6\times10^{-8}>0
\]

and the exact block Poincare currency is

\[
Q_{\rm block}=\frac{229}{1024}>0,
\]

the `C^dagger` lift increases that block slack by exactly

\[
\boxed{
(a^\dagger-a_*)Q_{\rm block}
=1.25234375\times10^{-8}>0.
}
\tag{6.1}
\]

So the newer center is compatible with, and slightly strengthens, the already-closed explicit `G10` corridor. No terminal slack is reused in proving Theorem 4.1; these are separate source mechanisms.

## 7. Honest universal remainder

The resulting compact proof chain is now:

- **PROVED:** all-gate formulation `(G)` is equivalent to full FEI.
- **PROVED:** balanced disjoint composition localizes center obstructions to composition-prime factors.
- **PROVED:** the known source-bound shared-core transform is globally `C^dagger`-safe on every balanced `C^dagger`-safe input and every signed singleton `b in [-1,1]`.
- **PROVED:** arbitrary finite alternation of balanced disjoint composition and this shared-core transform preserves the center `C^dagger`.
- **PROVED:** the explicit `G10` physical stopping corridor is also strictly safe at this same slightly larger quadratic lift.
- **PRESERVED PROVED:** the exact zero-depth derivative branch is the character-twisted one-point family and has `H<4J`.
- **OPEN:** prove `(G)` for arbitrary composition-prime Boolean gates at arbitrary interior product bias vectors for one finite-cap `Gamma` (whether `Gamma^dagger` or a later envelope), or produce a source-valid counterexample to the candidate.

The theorem above therefore closes the **known shared-core obstruction mechanism**, not full FEI. It does not classify all composition-prime gates, does not show every balanced near-extremizer is generated by this transform, and does not control arbitrary biased prime gates.

The smallest next integration target is now to use the new arity-5 structural reductions and prime-gate localization to prove a finite-bias envelope for genuine prime gates, rather than spend another run optimizing the already-closed shared-core scalar recurrence.

## 8. Arithmetic check

The run independently propagated the certified constants:

```text
PASS
C_dagger 6.521851214
a_dagger 0.268204856
M_plus 6.52185121301287772365150440023918196647146413881
C_minus_M 9.8712227634849559976081803352853586119E-10
d0_times_gap 1.025681740268358709126474987963244293267734375E-9
extra_vs_Cstar 1.4E-8
extra_a_vs_astar 5.6E-8
G10_extra_block_slack 1.25234375000E-8
```

These arithmetic lines only combine already certified interval endpoints and exact rational coefficients; the substantive global scalar certificate is the inherited exact interval checker cited in Section 1.

**Privacy / execution scope:** mathematics and repository-relative provenance only; no email/Drive, benchmark gold, credentials, unrelated private data, paid/remote compute, workflows, notification changes, or permission changes. No novelty or publication-priority claim. `full_brain_connected=false`.
