# B14 — a universal high-influence selector reduction for a minimum FEI counterexample

**Date:** 22 September 2026  
**Run:** `20260922T063833Z-b14-fei-selector-r12`  
**Classification:** `ESSENTIAL_STEP_APPLIED / HIGH-INFLUENCE-SELECTOR-REDUCTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim.

## 0. Live target, margin units, and the exact new reduction

The current source candidate used by the FEI fleet is

\[
C^\dagger=6.521851214,
\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\]

For a balanced Boolean gate at uniform input biases, the owner's margin relative to the read-once center is

\[
c_G=4\left(\frac{H(G)}{I(G)-1}-C_0\right).
\tag{0.1}
\]

Thus `c_G>a^dagger` is exactly

\[
\frac{H(G)}{I(G)-1}>C^\dagger.
\tag{0.2}
\]

This run proves the following target-level structural reduction.

### Theorem 0.1 — high-influence selector reduction

If full FEI with constant `C^dagger` is false, let
\(f:\{0,1\}^n\to\{\pm1\}\) have **minimum possible dimension** among counterexamples
\[
H(f)>C^\dagger I(f).
\tag{0.3}
\]
Then every original coordinate satisfies

\[
\boxed{\operatorname{Inf}_i(f)<d_0:=\frac{1741}{10000}=0.1741.}
\tag{0.4}
\]

Moreover every one-coordinate cofactor \(f_{i=b}\) is a **noncharacter** (constants included as characters after the fresh-character lift):

\[
\boxed{f_{i=b}\text{ is not a character for every }i,b.}
\tag{0.5}
\]

Equivalently, any minimum-arity balanced uniform gate with margin
\(c_G>a^\dagger\) must be simultaneously **diffuse-influence** and **cofactor-prime** in the precise senses (0.4)--(0.5).

This supplies an actual physical selector policy for two large branches of the critical case: reveal any original coordinate with influence at least `0.1741`, or reveal a coordinate having a character cofactor. Either branch is paid. The first still-unpaid class is the one in which *every* original influence is below `0.1741` and *every* one-coordinate cofactor is noncharacter.

## 1. Exact source dependencies consumed

### 1.1 Sharp source-valid posterior credit

I use the completed account01/B15 result

`account01/B15/20260922T053153Z-sharp-biased-joint-credit/REPORT.md`.

For a physical pivot of bias `t`, Boolean restrictions \(g_0,g_1\), and
\(d=\Pr[g_0\ne g_1]\), it proves the exact gluing cocycle

\[
D_\Gamma(g)
=(1-t)D_\Gamma(g_0)+tD_\Gamma(g_1)
+\mathcal R_{\Gamma,i}+\mathcal C_i,
\tag{1.1}
\]
with the full favorable conditional-information credit retained,

\[
\mathcal C_i=H(B\mid S)+I(S;J)
\ge
\Theta\!\left(\sqrt{V_t}\,|1-2d|\right),
\tag{1.2}
\]
where

\[
\Theta(z)=h_2\!\left(\frac{1-\sqrt{1-z^2}}2\right),
\qquad V_t=4t(1-t).
\tag{1.3}
\]

For **balanced children** at the uniform physical pivot `t=1/2`, (1.1)--(1.3) give the source-valid scalar lower bound

\[
\boxed{
\mathcal R_{\Gamma^\dagger,i}+\mathcal C_i
\ge F(d):=C^\dagger d-1-h_2(d)+\Theta(|1-2d|).
}
\tag{1.4}
\]

No branch-label bit is charged for free: (1.2) is precisely the retained negative entropy / posterior information term.

### 1.2 Named compatible other-account result consumed and applied

I substantively consume account04/B17

`account04/B17/20260922T061604Z-character-cofactor-local-threshold/REPORT.md`.

At a uniform physical pivot with balanced restrictions, if one child is a character and the other is an arbitrary balanced Boolean function, that report derives an exact one-variable threshold \(Q(d)\) and proves

\[
\boxed{Q(d)<5.1\qquad(0<d\le1/2).}
\tag{1.5}
\]

More importantly for the present selector, if the character child has zero defect and the other child is denoted `h`, its exact cocycle gives

\[
\boxed{
D_C(g)=\frac12D_C(h)+d[C-Q(d)].
}
\tag{1.6}
\]

Consequently, at the live center `C^dagger>5.1`, a character-cofactor pivot can never be the first negative gluing node when its lower-dimensional noncharacter child is already safe. This is used directly in section 4; it is not merely cited.

## 2. New scalar theorem: every balanced split with disagreement at least 0.1741 pays

For \(0<d\le1/2\), write

\[
\phi(d):=\Theta(1-2d)
=h_2\!\left(\frac12-\sqrt{d(1-d)}\right).
\tag{2.1}
\]

Then

\[
F(d)=C^\dagger d-1-h_2(d)+\phi(d).
\tag{2.2}
\]

### Lemma 2.1 — derivative control

For every \(0<d<1/2\),

\[
\boxed{\phi'(d)\ge-\frac2{\ln2}.}
\tag{2.3}
\]

**Proof.** Put \(x=2\sqrt{d(1-d)}\in(0,1)\), so
\(1-2d=\sqrt{1-x^2}\). Direct differentiation gives

\[
|\phi'(d)|
=\frac{\sqrt{1-x^2}}{x\ln2}
\ln\frac{1+x}{1-x}
=\frac{2\sqrt{1-x^2}}{x\ln2}\operatorname{artanh}x.
\]

The elementary inequality

\[
\operatorname{artanh}x\le\frac{x}{\sqrt{1-x^2}}
\tag{2.4}
\]

follows because the difference between the right side and the left side is zero at `0` and has derivative

\[
\frac{1-\sqrt{1-x^2}}{(1-x^2)^{3/2}}\ge0.
\]

Thus \(|\phi'(d)|\le2/\ln2\), proving (2.3). `QED`

Let

\[
d_0=1741/10000.
\]

Because \(h_2'(d)=\log_2((1-d)/d)\), Lemma 2.1 yields on
\([d_0,1/2]\)

\[
F'(d)
\ge C^\dagger
-\log_2\frac{1-d_0}{d_0}
-\frac2{\ln2}.
\tag{2.5}
\]

The exact rational interval checker beside this report certifies

\[
\boxed{
C^\dagger
-\log_2\frac{1-d_0}{d_0}
-\frac2{\ln2}
>1.390410224556456926
}
\tag{2.6}
\]

and, independently,

\[
\boxed{F(d_0)>0.000124952707245502.}
\tag{2.7}
\]

Therefore \(F(d)>0\) throughout \([d_0,1/2]\).

For \(d\ge1/2\), both \(-h_2'(d)\) and the derivative of
\(\Theta(2d-1)\) are nonnegative, so

\[
F'(d)>C^\dagger>0,
\]
while

\[
F(1/2)=C^\dagger/2-2=1.260925607>0.
\]

We have proved:

### Theorem 2.2 — uniform high-disagreement payment

For every pair of balanced Boolean restrictions at a uniform physical pivot,

\[
\boxed{
\Pr[g_0\ne g_1]\ge0.1741
\quad\Longrightarrow\quad
\mathcal R_{\Gamma^\dagger,i}+\mathcal C_i>0.
}
\tag{2.8}
\]

This is an analytic all-dimensional statement; the finite computation is only the rigorous one-point certification (2.7) and derivative constant (2.6), both with exact rational enclosures.

## 3. Fresh-character lift turns every original-coordinate split into a balanced-child split

Let `f` be arbitrary, not necessarily balanced, and introduce one **actual fresh unbiased coordinate** `y`:

\[
\widetilde f(y,x)=(-1)^y f(x).
\tag{3.1}
\]

This is the standard character shift, not an affine relabeling and not an uncharged selector label. Its Fourier spectrum is translated by the fresh coordinate, hence exactly

\[
H(\widetilde f)=H(f),
\qquad
I(\widetilde f)-1=I(f).
\tag{3.2}
\]

The function \(\widetilde f\) is balanced. More importantly, for **every original coordinate** `i` and either branch `b`,

\[
\widetilde f_{i=b}(y,x_{\ne i})=(-1)^y f_{i=b}(x_{\ne i})
\tag{3.3}
\]

is also balanced, regardless of the output bias of \(f_{i=b}\). Thus every original-coordinate split of the fresh-character lift lies in the balanced-child regime of Theorem 2.2.

Moreover

\[
\Pr[\widetilde f_{i=0}\ne\widetilde f_{i=1}]
=\Pr[f_{i=0}\ne f_{i=1}]
=\operatorname{Inf}_i(f).
\tag{3.4}
\]

Finally, at uniform inputs the all-gate defect of a balanced Boolean function `g` is exactly

\[
D_{\Gamma^\dagger}(g)
=C^\dagger[I(g)-1]-H(g).
\tag{3.5}
\]

Equations (3.2)--(3.5) are the bridge from the local selector theorem back to the original uniform-cube FEI target.

## 4. Proof of Theorem 0.1 and the actual selector policy

Assume FEI at `C^dagger` is false and choose `f` of minimum dimension satisfying (0.3). Then every proper one-coordinate restriction obeys

\[
H(f_{i=b})\le C^\dagger I(f_{i=b}).
\tag{4.1}
\]

Lift to \(\widetilde f\) by (3.1). By (3.3), its two children at every original coordinate are balanced, and by (3.2), applied to the children,

\[
D_{\Gamma^\dagger}(\widetilde f_{i=b})
=C^\dagger I(f_{i=b})-H(f_{i=b})\ge0.
\tag{4.2}
\]

### Policy branch A: a high-influence original coordinate exists

If some original coordinate has

\[
d_i=\operatorname{Inf}_i(f)\ge d_0,
\]
choose the **physical singleton block** `A={i}`. The exact gluing cocycle (1.1), (4.2), and Theorem 2.2 give

\[
D_{\Gamma^\dagger}(\widetilde f)>0.
\]

Using (3.2) and (3.5), this says

\[
C^\dagger I(f)-H(f)>0,
\]
contradicting (0.3). Hence every coordinate satisfies (0.4).

### Policy branch B: a character cofactor exists

Suppose some `f_{i=b}` is a character or a constant. Then
\(\widetilde f_{i=b}=(-1)^y f_{i=b}\) is a genuine character. The opposite lifted cofactor is balanced by (3.3) and is safe by (4.2). Apply the **named account04/B17 theorem** (1.6) at the same original physical coordinate. Since

\[
C^\dagger>5.1>Q(d),
\]
we again obtain

\[
D_{\Gamma^\dagger}(\widetilde f)>0,
\]
contradicting (0.3). Therefore (0.5) holds.

This completes Theorem 0.1. `QED`

## 5. Stress against the required obstruction families

The reduction was checked against the mechanisms the campaign requires us not to ignore.

- **Addressing.** A genuine address bit of the standard unbiased addressing function has influence `1/2`, so branch A selects an actual address coordinate immediately. This is an existential/high-influence selector; it does **not** resurrect the false claim that every prescribed coordinate pays.
- **Majority.** Large odd majority has all influences tending to zero and noncharacter cofactors, so it can survive into the new hard core. This is correct: the theorem does not pretend the low-influence case is solved.
- **Tribes.** Balanced tribes likewise has small influences and noncharacter cofactors and therefore survives. Again this is a required hard-case retention, not a failure of the proved reduction.
- **Sparse defects.** Small-influence rare-gating constructions may survive (0.4), but account03/B18's exact rare-gating nonamplification theorem shows that rare gating cannot turn a `C>=4`-safe balanced core into an unsafe one. The present theorem does not infer safety from defect density alone, which account02/B17 refuted.
- **Tensor/self-composition.** Diffuse tensor constructions may survive both tests. No tensor-critical coverage assumption is made.
- **Biased limits.** The proof targets the original uniform-cube FEI through the exact fresh-character lift. It does not claim that the full off-center product-bias inequality for `Gamma^dagger` has been proved.

Thus the new selector removes exactly what it proves and leaves the known difficult diffuse mechanisms intact.

## 6. Old and new missing implications

**Old first missing implication.** A minimum counterexample to the live FEI constant could in principle have a single dominant physical coordinate, or a coordinate whose restriction immediately collapses to a character. The existing sharp posterior-credit theorem had not been turned into a universal original-coordinate selector statement for arbitrary uniform-cube `f`.

**New proved inference.** The fresh-character lift makes *every original-coordinate child balanced*. Retaining the exact posterior information term then proves that every original coordinate with influence at least `0.1741` pays. Consuming account04/B17 also proves that every character-cofactor coordinate pays. Hence any minimum counterexample must satisfy the simultaneous hard-core constraints (0.4)--(0.5).

In the owner's gate-margin units, any minimum-arity gate with

\[
c_G>a^\dagger=0.268204856
\]
can therefore be assumed to have all physical input influences below `0.1741` and no character cofactor.

**First remaining implication.** Construct a genuinely physical multi-coordinate block selector, or a bounded noncircular potential, for the remaining diffuse cofactor-prime class

\[
\max_i\operatorname{Inf}_i(f)<0.1741,
\qquad
f_{i=b}\text{ noncharacter for all }i,b.
\tag{6.1}
\]

That class still contains majority/tribes/tensor-like mechanisms, so (6.1) is not a hidden coverage assumption. A proof that some realizable block in every state (6.1) has nonnegative total gluing decrement would close the next target-level arrow; no such theorem is asserted here.

## 7. Rigorous scalar certificate

`CHECKER.py` uses only Python's standard library, exact `Fraction` arithmetic, integer square-root bracketing, and positive `atanh` series with explicit geometric tails. It certifies (2.6)--(2.7) and prints `PASS`.

Committed checker blob:

`2d7665e3b269ca9e92cd965465578ae8ce9ddc0c`

Committed output blob:

`0866fafef93c68ef03b3a891184e056e0df42061`

The executed output is

```text
PASS
d0 = 1741/10000 = 0.1741000000
certified F(d0) lower > 0.000124952707245502
certified derivative lower on [d0,1/2] > 1.390410224556456926
certified F(1/2) = 1.260925607000000000 > 0
```

The checker is support for the two scalar endpoints only; the fresh-character selector deduction is analytic.

## 8. Status

**Classification:** `ESSENTIAL_STEP_APPLIED`.

A real target-level branch has been removed: a minimum FEI counterexample cannot have any original influence at least `0.1741`, and cannot have any character cofactor. This is not a complete proof. The universal diffuse cofactor-prime block-selection implication (6.1) remains open, so **full FEI remains OPEN / NOT PROVED**.

Scoped privacy review: this report contains only FEI mathematics, logical account/slot labels, private-repository-relative scientific paths, and nonsecret constants. It contains no credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive actions, paid/remote compute, workflow dispatch, or permission changes.
