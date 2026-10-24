# B16 — a rigorous arity-nine gap for balanced direct restrictions of the 18-bit FEI seed

**Outcome:** `PROVED_FINITE_SOURCE_FAMILY_EXCLUSION`. Full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository sources were read directly; no authenticated brain retrieval or receiver-context use occurred.

## 1. Live target and peer artifact consumed

The current owner control (revision `2026-09-22.2`) supersedes the older interface-C signed-transport assignment and asks the FEI fleet to converge on the all-gate reformulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le \sum_i {\rm It}_i(G;p)\,{\Gamma(p_i)+h(V_{p_i})\over V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

or a decisive falsification/replacement step.  The source-exact equivalence of existence of some finite-cap symmetric nonnegative \(\Gamma\) satisfying (G) with full FEI is in `continuations/2026-09-22-gate-reformulation/REPORT.md`.

The old read-once fixed-point \(\Gamma\) / AND-extremality candidate is already refuted, so this run did **not** try to repair it.  I consumed the completed cross-account result

`account04/B13/20260922T0055Z-arity10-prime-falsifier/REPORT.md`

which gives an explicit balanced, composition-prime ten-input restriction \(G_{10}\) of the exact 18-input Numaro seed with

\[
I(G_{10})={257\over128},\qquad
{H(G_{10})\over I(G_{10})-1}>6.4593722816378554,
\]

hence a strict read-once-\(\Gamma\) violation.  Its report proposes searching arities 5--9 for a smaller prime obstruction.  I applied that result to the most immediate source-exact contraction: **fix one more or several different source coordinates and exhaust every balanced restriction having exactly nine free variables**.  This tests the entire balanced arity-nine direct-restriction family of the same 18-bit source, not merely the 20 one-bit restrictions of the displayed \(G_{10}\).

## 2. Exact source structure and balance equation

The source has nine core variables \(x_0,\ldots,x_8\) and nine auxiliary variables \(y_0,\ldots,y_8\).  Its reconstructed truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

On the 512-point core cube, let \(B\) be the base-negative set.  Each auxiliary variable \(y_j\) owns a disjoint two-point host set \(H_j\), disjoint also from \(B\); on a host point the value changes from \(+1\) to \(-1\) exactly when its owner auxiliary bit is one.

Consider an arbitrary restriction leaving exactly nine variables free.  Let

- \(r\) = number of free core variables;
- \(a=9-r\) = number of free auxiliary variables;
- \(X\) = the resulting \(r\)-dimensional core subcube;
- \(b=|B\cap X|\);
- \(h_j=|H_j\cap X|\in\{0,1,2\}\);
- \(F\) = set of free auxiliary indices, \(|F|=a\);
- \(H_1=\sum_{j\notin F:\ y_j\text{ fixed to }1}h_j\).

For each base-negative core point all \(2^a\) free-auxiliary assignments are negative.  For a host point belonging to a free auxiliary, exactly half of its \(2^a\) assignments are negative.  For a host point whose auxiliary is fixed to one, all assignments are negative.  Therefore the exact negative count is

\[
2^a b+2^{a-1}\sum_{j\in F}h_j+2^aH_1.
\]

The nine-variable restricted gate is balanced iff this equals \(2^8\), equivalently

\[
\boxed{
2b+\sum_{j\in F}h_j+2H_1=2^r.
}
\tag{2.1}
\]

This identity makes exhaustive balance filtering an integer calculation; no Fourier or floating-point quantity is involved.

## 3. Exact enumeration of every balanced nine-variable direct restriction

Enumerating every choice of the free core set, fixed core assignment, free auxiliary set and fixed auxiliary assignment subject to (2.1) gives:

| free core count \(r\) | balanced restrictions | non-dictators |
|---:|---:|---:|
| 9 | 0 | 0 |
| 8 | 0 | 0 |
| 7 | 0 | 0 |
| 6 | 133,056 | 133,056 |
| 5 | 270,144 | 124,992 |
| 4 | 703,584 | 90,720 |
| 3 | 588,672 | 0 |
| 2 | 150,912 | 0 |
| 1 | 8,226 | 0 |
| 0 | 18 | 0 |

Thus there are exactly

\[
\boxed{1,854,612}
\]

balanced nine-variable restrictions, of which exactly

\[
\boxed{348,768}
\]

are non-dictators.  In particular, **no balanced nine-variable restriction keeps seven or more core coordinates free**.  At the other end, every balanced restriction with at most three free core coordinates has total influence exactly one; since it is balanced, Poincare equality forces its Fourier support onto level one, and Booleanity then forces a signed dictator.

## 4. Rigorous entropy/influence certificate for all 348,768 non-dictators

For a balanced nine-bit gate let \(W_S\in\mathbb Z\) be its unnormalised Walsh coefficients, with \(N=512\).  Then

\[
\sum_SW_S^2=N^2,
\qquad
I={1\over N^2}\sum_S |S|W_S^2,
\]

and, because the spectral weights are \(q_S=W_S^2/N^2\),

\[
H
=18-{2\over N^2}\sum_{W_S\ne0}W_S^2\log_2|W_S|.
\tag{4.1}
\]

To avoid any floating-point sign decision, set \(Q=2^{16}\) and

\[
L_a=\lfloor Q\log_2 a\rfloor.
\]

The checker computes \(L_a\) **exactly** from

\[
L_a=\operatorname{bitlength}(a^Q)-1
\]

for every integer \(1\le a\le512\).  Hence

\[
H\le H_Q:=18-{2\over N^2Q}\sum_SW_S^2L_{|W_S|}.
\tag{4.2}
\]

The target bound

\[
H_Q<{1273\over200}(I-1)=6.365(I-1)
\tag{4.3}
\]

is then an integer inequality after clearing \(N^2Q\).  The exhaustive integer-Walsh scan has **zero failures** in every stratum.  The smallest cleared integer margin is still positive:

- \(r=6\): `2,301,034,496`; closest rigorous upper ratio `6.36397952125186`, at \(I=1.65625\);
- \(r=5\): `38,503,710,720`; closest rigorous upper ratio `6.3470703125`, at \(I=1.625\);
- \(r=4\): `38,503,710,720`; closest rigorous upper ratio `6.3470703125`, at \(I=1.625\).

Therefore:

### Theorem
Every balanced nine-variable gate obtained by fixing nine coordinates of this exact 18-variable source is either a dictator or satisfies

\[
\boxed{
{H(G)\over I(G)-1}<6.365.
}
\tag{4.4}
\]

The computation behind (4.4) is finite and sign-exact: balance, Walsh coefficients, influence, logarithm lower bounds and the final inequality are all decided by integers.  NumPy is used only to batch exact `int64` arithmetic; all intermediate magnitudes are far below the `int64` limit.

The exact checks were executed successfully stratum-by-stratum during this invocation.  `CHECKER.py` is the monolithic reproduction harness for the same calculation; `RESULT.json` records the verified per-stratum counts and integer margins.  A single-process end-to-end completion of the monolithic harness was not used as the evidentiary basis here.

## 5. What this refutes and what remains

**Attempted refutation mechanism:** descend the explicit ten-input prime falsifier one more arity by a direct restriction of its exact 18-input parent while retaining balance.  Since every such nine-variable balanced restriction lies below `6.365`, this mechanism cannot preserve the ten-input obstruction, whose ratio exceeds `6.45937`.

**Precise dead route:** a smaller **balanced-uniform** counterexample cannot be obtained at arity nine merely by fixing nine coordinates of this particular 18-variable source.  In particular, every balanced one-bit restriction of the explicit \(G_{10}\) is below the read-once-scale obstruction.

**Not proved:** this does not exclude unrelated nine-input gates, unbalanced nine-input restrictions, biased input vectors, or a different source construction.  It does not prove arity ten is globally minimal, and it does not prove FEI.

**Replacement obligation:** do not spend another run enumerating balanced direct restrictions of this source.  The next smaller-arity adversary should either (i) search genuinely new balanced nine-bit gates outside this source family, or (ii) leave the balanced-uniform slice and test unbalanced/bias-perturbed prime gates against the actual gate potential.  On the proof side, the global replacement obligation remains a dimension-independent upper bound for the balanced support-deficit ratio, equivalently a new finite-cap all-gate potential.

**Consumed peer artifact:** account04/B13 `20260922T0055Z-arity10-prime-falsifier/REPORT.md` (explicit ten-input composition-prime obstruction).  
**Applied to claim:** tested whether its exact 18-input source can yield a balanced arity-nine obstruction by direct coordinate restriction.  
**New result:** no; all 1,854,612 balanced arity-nine direct restrictions are dictators or satisfy (4.4).  
**Next recipient:** account04/B13 and the other FEI gate-reformulation adversary workers; skip this exhausted balanced direct-restriction family and change mechanism.  
**Full-FEI implication:** auxiliary narrowing only. **Full FEI remains OPEN / NOT PROVED.**
