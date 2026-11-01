# MOC4 fleet02/B09 r12 — X-aware parity-excess compression and a robust no-go for decoupled fiber rescue

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal `4 x 4` Marcus–de Oliveira target  
**Worker:** fleet02/B09  
**Assignment:** alternative geometric/polarization mechanism for the exact support function, preserving complex phases and common-unitary compatibility  
**Outcome:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`. I derive a Birkhoff-free exact six-fiber scalar criterion for the support inequality, then give an exact generic true-unitary counterexample to the tempting **X-only / zero-parity-fiber repair**. The parent MOC4 target remains **OPEN**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live source state consumed

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\tag{MOC4}
\]

for all complex normal `4 x 4` pairs, including singular and repeated-spectrum cases.

This run read the campaign lead's latest complete fleet03/B07 report, `20260922T013930Z-fleet03-B07-MOC4-r11`, which refutes a zero-entry common-permutation lift and leaves two honest branches: a zero-entry support lemma and the pair-strict interior six-fiber problem. I also consumed the preceding lead reduction `MOC4-PARITY-SLACK-v1`, which writes the exact interior support inequality in the standard three-dimensional representation of `S_4`.

During this invocation, **fleet01/B07 r11b** appeared at scientific commit `a0fac94c9342ee4a2c18ed94f7fe770bdf0b12df`, blob `a27b3f761c111c45d39218ee58f5e7e7faf2e1c6`. I consumed it immediately rather than counting a duplicate discovery. That report independently refutes the universal parity-slack gate on a generic true-unitary datum and proves the exact `X`-aware decomposition identity. My own search had reached a different exact parity-slack-failing datum, so I retired that as duplicate mechanism-level evidence and used the new B07 identity to attack the next natural repair instead.

I also use the exact structured-coefficient/common-lift obstruction from fleet04/B09, scientific commit `6c116abdc4e257434eef09e52608ab5e34c3c49c`, as the rational orthogonal seed. No arbitrary bistochastic surrogate enters below.

## 2. Exact six-fiber support notation

Use the lead's exact reduction

\[
\langle D,K\rangle+\frac12\langle R,X\rangle
\le
\max_{\rho\in S_3}\left(F_\rho(K)+\frac12x_\rho\right),
\tag{SR}
\]

where `R` is the actual complementary-pair transport of one common unitary, `D` is its signed Hadamard block, and

\[
x_\rho=\sum_iX_{i,\rho(i)}.
\]

For a fiber `rho`, set

\[
m_\rho(K)=
\begin{cases}
0,&\prod_iK_{i,\rho(i)}\ge0,\\
\min_i|K_{i,\rho(i)}|,&\prod_iK_{i,\rho(i)}<0.
\end{cases}
\]

Then the tetrahedral sign constraint gives

\[
F_\rho(K)=\sum_i|K_{i,\rho(i)}|-2m_\rho(K).
\tag{1}
\]

Define the entrywise matrix

\[
T:=|K|+\frac12X
\tag{2}
\]

and the six ordinary assignment costs and parity-corrected costs

\[
c_\rho:=\langle R_\rho,T\rangle,
\qquad
q_\rho:=c_\rho-2m_\rho(K).
\tag{3}
\]

Finally put

\[
\mathcal S:=\langle R,|K|\rangle-\langle D,K\rangle.
\tag{4}
\]

Because `|D_ij|<=R_ij`, every summand in `(4)` is nonnegative, so `\mathcal S>=0`.

## 3. New exact compression: no Birkhoff decomposition is needed

### Theorem 1 — parity-excess identity

For every actual source datum in the six-fiber reduction, define

\[
\mathcal E
:=\langle R,T\rangle-\max_{\rho\in S_3}q_\rho.
\tag{5}
\]

Then the exact support gap is

\[
\boxed{
\max_\rho q_\rho-
\left(\langle D,K\rangle+\frac12\langle R,X\rangle\right)
=\mathcal S-\mathcal E.
}
\tag{6}
\]

Consequently `(SR)` is equivalent to the single scalar inequality

\[
\boxed{\mathcal E\le\mathcal S.}
\tag{7}
\]

Equivalently, `(SR)` holds iff at least one of the six fibers satisfies

\[
\boxed{
2m_\rho(K)
\le
\mathcal S+c_\rho-\langle R,T\rangle.
}
\tag{8}
\]

#### Proof

By `(1)`--`(3)`, the right side of `(SR)` is exactly `max_rho q_rho`. Also

\[
\langle D,K\rangle+rac12\langle R,X\rangle
=
\langle R,|K|\rangle-\mathcal S+rac12\langle R,X\rangle
=\langle R,T\rangle-\mathcal S.
\]

Subtracting gives `(6)`, hence `(7)`. Finally `(7)` is equivalent to

\[
\max_\rho(c_\rho-2m_\rho)
\ge \langle R,T\rangle-\mathcal S,
\]

which is exactly the existential six-check `(8)`. QED.

This is algebraically compatible with fleet01/B07's `X`-aware decomposition identity but removes the Birkhoff decomposition variable entirely. It exposes the actual obligation as a **joint payment**: the parity-corrected assignment excess `mathcal E` must be paid by the true-unitary orientation slack `mathcal S`.

### Corollary 2 — one zero-penalty above-average fiber closes the support direction

If some `rho` satisfies

\[
c_\rho\ge\langle R,T\rangle
\quad\text{and}\quad
\prod_iK_{i,\rho(i)}\ge0,
\tag{9}
\]

then `(SR)` holds.

Indeed `m_rho=0`, so `(8)` follows from `mathcal S>=0`. Since `R` is doubly stochastic, ordinary Birkhoff already guarantees that **some** fiber has `c_rho>=<R,T>`; the only issue is whether all such above-average fibers are parity-bad. Thus any genuine counterexample to `(SR)` must satisfy the sharper necessary condition:

> every above-average ordinary `T`-assignment has negative `K` transversal product, and every one of the six fibers violates `(8)`.

This is the first useful geometric screening condition I know that keeps the structured `X` term and the exact tetrahedral parity simultaneously.

## 4. A tempting X-only repair is false on a generic true-unitary datum

After the parity-slack gate failed, a natural decoupled repair would be to hope that the structured `X` term alone forces

\[
\mathcal E\le0.
\tag{X0}
\]

Then `(SR)` would follow immediately from `mathcal S>=0`, without using delicate orientation slack. The next exact witness shows `(X0)` is false even in the simple-spectrum, irreducible, strict-compound interior.

Start from the fleet04/B09 rational orthogonal seed

\[
U_0=\begin{pmatrix}
492/625&-31/625&-48/125&12/25\\
-9/25&12/25&-4/5&0\\
-36/125&48/125&9/25&4/5\\
-256/625&-492/625&-36/125&9/25
\end{pmatrix}
\]

and right-multiply columns 2 and 4 by the exact Givens rotation with

\[
c=99/101,\qquad s=20/101.
\]

The resulting matrix is

\[
U=\begin{pmatrix}
492/625&2931/63125&-48/125&6064/12625\\
-9/25&1188/2525&-4/5&-48/505\\
-36/125&6752/12625&9/25&1788/2525\\
-256/625&-44208/63125&-36/125&6423/12625
\end{pmatrix}.
\tag{10}
\]

Take support direction `eta=1` and spectra

\[
a=(-4-3i,\,-3-2i,\,4-4i,\,2i),
\qquad
b=(-2+2i,\,-4+i,\,-1-3i,\,-2-i).
\tag{11}
\]

The verifier checks exactly that `UU^T=I`, all sixteen entries of `U` are nonzero, **all 36 two-by-two minors are nonzero**, `R_ij>|D_ij|` in all nine cells, both spectra are simple and nonzero, and all off-diagonal entries of `B=U diag(b) U^T` are nonzero. Since `A` has simple diagonal spectrum, the latter excludes every proper common coordinate reducing block. Thus this is a genuine normal, irreducible, strict-compound true-unitary datum, not a bistochastic surrogate or solved boundary case.

The exact structured coefficient construction gives

\[
K=\begin{pmatrix}
191/2&-142&47/2\\
185/2&-143/2&-331/2\\
-315/2&135/2&273/2
\end{pmatrix},
\tag{12}
\]

\[
X=\begin{pmatrix}
145&88&-43\\
-126&-396&-294\\
-82&-214&-146
\end{pmatrix}.
\tag{13}
\]

In lexicographic fiber order

\[
123,132,213,231,312,321,
\]

the ordinary costs, parity penalties, and corrected costs are respectively

\[
(c_\rho)=(105,147,279,321,-8,-8),
\tag{14}
\]

\[
(m_\rho)=(143/2,135/2,185/2,142,0,0),
\tag{15}
\]

\[
(q_\rho)=(-38,12,94,37,-8,-8).
\tag{16}
\]

The actual unitary-derived `R` gives

\[
\langle R,T\rangle
=\frac{939823244619}{3984765625},
\]

so

\[
\boxed{
\mathcal E
=\frac{565255275869}{3984765625}>0.
}
\tag{17}
\]

Moreover the **only zero-penalty fibers**, `312` and `321`, both have cost `-8`, strictly below the actual `R`-average. Hence the easy Corollary 2 mechanism genuinely fails here; the ordinary above-average fibers are parity-bad.

Nevertheless the true-unitary orientation slack is

\[
\boxed{
\mathcal S
=\frac{2119488205727}{3984765625},
}
\tag{18}
\]

and therefore

\[
\boxed{
\mathcal S-\mathcal E
=\frac{1554232929858}{3984765625}>0.
}
\tag{19}
\]

So the exact support inequality is safely true. This datum refutes only the **decoupled X-only repair** `(X0)`, not MOC4.

As a direct source-level cross-check, the 24 complex permutation vertices are all distinct, the support maximum at `eta=1` is uniquely

\[
M=-48,
\]

while

\[
\Re\det(A+UBU^T)
=-\frac{1745501679858}{3984765625}.
\]

Their difference is exactly the same fraction `(19)`, as required by Theorem 1.

Because `(17)` is a strict inequality and all genericity conditions above are strict, continuity gives an open neighborhood of genuine source data on which `mathcal E>0`. Thus `(X0)` cannot be repaired merely by excluding isolated nongeneric points or by assuming simple spectra and strict compound minors.

## 5. What survives: the first missing implication is necessarily joint

Two attractive decouplings are now gone on source-valid generic data:

1. fleet01/B07 refutes **orientation slack alone** as a universal gate (`MOC4-PARITY-SLACK-v1`);
2. the witness above refutes **structured X-assignment surplus alone** (`mathcal E<=0`).

The exact surviving criterion is `(8)`, which makes the needed coupling explicit. A counterexample must have all six inequalities

\[
2m_\rho(K)
>
\mathcal S+c_\rho-\langle R,T\rangle.
\tag{20}
\]

This is substantially narrower than asking for an arbitrary mixed `(P,R)` inequality: it is six scalar failures tied to one common unitary and one structured spectral pair.

For the requested geometric/polarization route, the next interior statement is therefore:

> **`MOC4-MAXIMIZER-SIX-WITNESS-v1`.** At a pair-strict global maximizer of the fixed support functional, the twelve exact row/column pair-orbit north-pole conditions force at least one fiber `rho` to satisfy `(8)`.

This is the first place where my preceding pair-ellipse theorem can be used without throwing away either complex phases or the common-unitary constraint. It is also strictly more appropriately scoped than the now-refuted universal parity-slack assertion, because MOC4 only needs the inequality at a global support maximizer.

Combining the latest lead dichotomy gives a compact conditional end-to-end chain: close the lead's zero-face support lemma on the flat-pair branch; on the pair-strict branch prove `MOC4-MAXIMIZER-SIX-WITNESS-v1`; then `(8)` gives `(SR)` at every global maximizer, hence every support direction satisfies the permutation support bound, yielding MOC4. The repeated/singular boundary work remains preserved rather than silently re-proved.

## 6. Exact verification and failures

`verify_parity_excess.py` uses only Python's standard-library `fractions.Fraction` and exhaustive finite permutation arithmetic. It recomputes the structured `K,X,D,R` from `(10)`--`(11)`, checks exact orthogonality/genericity, verifies `(14)`--`(19)`, enumerates all 24 permutation products, and checks that the target support gap equals `mathcal S-mathcal E` exactly. `VERIFICATION.txt` is the captured output of that executed verifier.

An earlier branch of this run independently found a different exact generic failure of the parity-slack gate. Once fleet01/B07 r11b appeared with the same mechanism and a complete exact proof, I did **not** count the duplicate as new progress; I switched to the `X`-aware repair above. No benchmark material, held-out answers, credentials, scheduler identifiers, machine paths, email/Drive data, public posting, paid model/API, Codex, remote workflow, or permission bypass was used.

## 7. Status

- `MOC4-PARITY-EXCESS-v1` / Theorem 1: **PROVED exact reduction**.
- one-zero-penalty-above-average-fiber closure, Corollary 2: **PROVED**.
- `MOC4-X0` (`mathcal E<=0` universally): **REFUTED** by exact true-unitary generic source data.
- `MOC4-MAXIMIZER-SIX-WITNESS-v1`: **OPEN**, now the first interior geometric implication for B09.
- lead zero-face support branch: **OPEN** per latest fleet03/B07 report.
- full MOC4: **OPEN**.
