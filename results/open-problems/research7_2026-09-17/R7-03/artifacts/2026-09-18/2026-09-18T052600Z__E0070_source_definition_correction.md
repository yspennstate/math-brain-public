Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# E0070 / Björklund Problem 2 — correction of the quasiharmonic source interface

Date: 2026-09-18 UTC  
Worker: R7-03 Boundary-Case Research  
Canonical target: E0070  
Source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2 (2014), Appendix II §7.1, Problem 2, printed p.24.

## 1. Purpose and correction

The earlier immutable R7-03 artifact

`research7_2026-09-17/R7-03/artifacts/2026-09-18/2026-09-18T003800Z__E0070_source_normalization_addendum.md`

contains an overstatement of Björklund's definition. It identifies the quasiharmonic defect with the integral at the identity and consequently claims that the source definition forces the basepoint value to vanish. That is **not** the general definition printed in the source.

The current arXiv v2 HTML states in §4.1 that a `mu`-integrable function `phi` is left `mu`-quasiharmonic when **there exists a constant** `ell(phi)` such that

\[
\int_G \phi(sg)\,d\check\mu(s)=\phi(g)+\ell(\phi),\qquad g\in G.
\tag{1.1}
\]

Putting `g=e` into (1.1) gives only

\[
\ell(\phi)=\int_G\phi(s)\,d\check\mu(s)-\phi(e),
\tag{1.2}
\]

not `ell(phi)=int phi(s) d check(mu)(s)` unless one separately normalizes `phi(e)=0`. In particular, nonzero constant functions are harmonic and hence quasiharmonic, exactly as they should be.

This correction **does not invalidate the E0070 construction or its main proof**. The main theorem was deliberately proved for an arbitrary constant defect `c`, which is stronger than the actual source definition. The only material that must be removed from the paper package is the unnecessary basepoint-normalization assertion.

## 2. Correct source-to-quotient interface

Let

\[
G=\operatorname{Sym}_{\mathrm{fin}}(\mathbb N_0),\qquad
H=\operatorname{Stab}_G(0),\qquad
\tau_n=(0\ n),\qquad
\mu(\tau_n)=p_n>0,
\]

where `sum_{n>=1} p_n=1`. The explicit paper choice is `p_n=2^{-n}`.

Let `u:G/H -> C` and define the right-`H`-invariant pullback

\[
\widetilde u(g)=u(gH).
\tag{2.1}
\]

Because every `tau_n` is an involution, `check(mu)=mu`. Because left convolution preserves right-`H`-invariance,

\[
\int_G\widetilde u(sgh)\,d\mu(s)
=
\int_G\widetilde u(sg)\,d\mu(s)
\qquad(h\in H),
\tag{2.2}
\]

so the group equation descends unambiguously to the quotient.

Under the equivariant bijection

\[
G/H\longrightarrow\mathbb N_0,\qquad gH\longmapsto g(0),
\tag{2.3}
\]

left multiplication by `tau_n` acts exactly as the transposition `(0 n)`. Therefore source equation (1.1) is **exactly**

\[
Pu=u+\ell,
\tag{2.4}
\]

for some arbitrary constant `ell in C`, where

\[
(Pu)(0)=\sum_{n\ge1}p_nu(n),
\tag{2.5}
\]

and, for `k>=1`,

\[
(Pu)(k)=p_ku(0)+(1-p_k)u(k).
\tag{2.6}
\]

At the basepoint, (2.4) says

\[
\ell=\sum_{n\ge1}p_nu(n)-u(0),
\tag{2.7}
\]

which is the quotient version of (1.2). No normalization `u(0)=0` is needed or asserted.

## 3. The source theorem survives unchanged

Assume `u` is source-valid and satisfies (2.4). From the leaf equation,

\[
p_k u(0)+(1-p_k)u(k)=u(k)+\ell,
\]

hence

\[
p_k\bigl(u(0)-u(k)\bigr)=\ell
\quad\text{and}\quad
u(k)=u(0)-\frac{\ell}{p_k}.
\tag{3.1}
\]

The source requires `mu`-integrability of the pullback, which in this construction is

\[
\sum_{n\ge1}p_n|u(n)|<\infty.
\tag{3.2}
\]

If `ell != 0`, then from (3.1)

\[
p_n|u(n)|=|p_nu(0)-\ell|\longrightarrow|\ell|>0,
\tag{3.3}
\]

because every positive summable sequence satisfies `p_n -> 0`. Thus the summands in (3.2) do not tend to zero, a contradiction. Therefore

\[
\boxed{\ell=0}.
\tag{3.4}
\]

Equation (3.1) then gives

\[
\boxed{u(k)=u(0)\text{ for every }k\ge1},
\tag{3.5}
\]

so `u` is constant. Nonzero constants are allowed; the source asks only that there be no **nonconstant** left (quasi-)harmonic functions.

This is precisely the conclusion required by Problem 2.

## 4. Integrability and well-definedness at every quotient state

The only infinite sum in the star kernel that requires a tail condition is the center row (2.5). Source `mu`-integrability gives exactly (3.2), so that sum is absolutely convergent.

At a leaf `k`,

\[
\sum_{n\ge1}p_n|u(\tau_n k)|
=p_k|u(0)|+\sum_{n\ne k}p_n|u(k)|
=p_k|u(0)|+(1-p_k)|u(k)|<\infty.
\tag{4.1}
\]

Thus once the source integrability condition at the pullback is satisfied, every quotient convolution appearing in (2.4) is well-defined. No conditional-convergence convention is used.

## 5. B23 — do what the proposer/source actually says

The adversarial source read found a **real interface error in our exposition**: the earlier normalization addendum promoted a special normalization into Björklund's general definition. The source's actual definition is the arbitrary-defect equation (1.1).

Outcome: the exposition must be corrected, but the theorem does not weaken because the existing main argument already treats arbitrary `c`. In fact this check increases confidence in the core proof: the core theorem had more latitude than the erroneous source-normalization paragraph.

## 6. B20 — enumerate exact failure modes

The five source-interface failure modes isolated by STUCK1 now resolve as follows.

1. **Left versus right convolution.** The source uses left convolution with `check(mu)`. Here `mu=check(mu)` because all support elements are involutions.
2. **Left versus right cosets.** `G/H` is the left homogeneous space of right cosets `gH`; `gH -> g(0)` is well-defined and equivariant for left multiplication.
3. **Defect normalization.** Corrected above: the defect is an arbitrary constant `ell`, not the integral itself. The main theorem already covers arbitrary `ell`.
4. **Integrability.** The source's `mu`-integrability becomes `sum p_n|u(n)|<infinity`, exactly the hypothesis used in the contradiction; leaf rows are automatically integrable by (4.1).
5. **Measured-group generation.** The star transpositions semigroup-generate `Sym_fin(N_0)`: they are involutions, and `tau_i tau_j tau_i=(i j)` for distinct positive `i,j`; every finitary permutation is a finite product of transpositions.

Outcome: one exposition bug was found and isolated; none of the five checks invalidates the source-level construction.

## 7. B22 — failures and later literature

A bounded dated search on 2026-09-18 rechecked the current arXiv v2 source, later Björklund work on countable-group random walks and stationary actions, homogeneous-space literature surfaced by the citation graph, finitary symmetric groups, star transpositions, and the exact Problem 2 wording. No later source was found in this bounded search that states a resolution of Appendix II Problem 2 or the infinite-star construction above.

This is **negative evidence only**. It is not a proof of worldwide openness and not a publication-novelty certificate.

## 8. Corrected verdict and protocol status

The mathematical candidate remains

**PROVED CANDIDATE / protocol closure open.**

Frozen metric:

```text
C_E0070 before: 1
C_E0070 after:  1
movement: NO MOVEMENT
```

The source-interface audit did uncover and correct a genuine flaw in the write-up, but not in the theorem. Independent P26 and distinct OTHER-track full-proof audits are still absent from the repository evidence recovered this run. Therefore audit-complete closure is not claimed.

The earlier normalization addendum is retained immutably as historical evidence and should be treated as **superseded by this correction** on the point that source quasiharmonicity forces `u(H)=0`. The central arbitrary-defect theorem in the original proof artifact remains valid.