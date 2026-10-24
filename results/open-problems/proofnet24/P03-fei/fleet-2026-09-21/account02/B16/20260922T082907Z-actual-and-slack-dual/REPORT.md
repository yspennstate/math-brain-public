# account02/B16 — the 35-pair dual has a large **actual** nonuniform AND bank

**Classification:** `ESSENTIAL_STEP_APPLIED / DUAL_OBSTRUCTION_REMOVED / FULL_FEI_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Live target and control correction

Fresh owner control revision `2026-09-22.2` supersedes the older Campaign-C half-band prompt and converges all FEI slots on the exact all-gate formulation. I therefore did not reopen the retired positive-current-only route. The current live task is to find a finite symmetric nonnegative potential `Gamma` satisfying every Boolean gate inequality, or rigorously obstruct a proposed repair.

The fixed candidate

\[
\Gamma^\dagger(t)=\Gamma_0(t)+0.268204856\,t(1-t),\qquad
\Gamma^\dagger(1/2)=6.521851214,
\]

is already refuted by the completed **other-account** account03/B12 report `20260922T061544Z-biased-prime-candidate-refutation`: the exact composition-prime 18-input Numaro gate at
\[
p_1=3/8,\quad p_2=\cdots=p_{18}=1/2,\quad r=p_{out}=967/2048
\]
has
\[
D_{\Gamma^\dagger}=-d,\qquad
d=0.0176114199558017537894958865691\ldots>0.
\]
That peer report also supplies the source-exact h96 node values
\[
G(3/8)=\frac{8766995320315105}{562949953421312},\qquad
G(r)=\frac{7680879056207109}{562949953421312},
\]
with `Gamma_0(s)=sG(s)` on the small side and `Gamma_0(1/2)=6.4548`.

I also consume and apply the completed **other-account** account01/B16 report `20260922T0743Z-and-bank-exhaustion`. It gives 35 exact rational AND pairs `(p_j,q_j)`, positive rational multipliers `lambda_j`, and
\[
\kappa:=\sum_j\lambda_jp_jq_j(1-p_j)(1-q_j)
=\frac{792001822391570453}{11721234856636579840}
=0.067569827930129554154\ldots .
\]
For a symmetric center-zero perturbation `psi` it proves
\[
\sum_j\lambda_j[-L_{p_j,q_j}(\psi)]
=\frac{57}{256}\psi(3/8)-\psi(r),
\quad
L_{p,q}(\psi)=q\psi(p)+p\psi(q)-\psi(pq).
\]
Using only the uniformly guaranteed quadratic reserve `A=0.258204856` beyond the certified `0.01` read-once potential, that dual is insufficient to repair the prime witness. The peer explicitly leaves the **actual nonuniform AND slack at those same 35 charged pairs** as the next loophole.

This run evaluates exactly that missing quantity.

## 1. Exact source formula for actual AND slack

For the read-once source potential, the exact two-input AND defect is
\[
D^{\Gamma}_{\rm AND}(p,q)
=L_{p,q}(\Gamma)-pqE(p,q),
\tag{1.1}
\]
where
\[
E(p,q)=8p(1-q)\log_2\frac1p
+8q(1-p)\log_2\frac1q
+8(1-p)(1-q)
+\Psi(pq)-\Psi(p)-\Psi(q),
\]
\[
\Psi(z)=\frac{(1-2z)^2\log_2(1/(1-2z)^2)}{z}.
\tag{1.2}
\]
This is the exact cancellation form from the completed read-once certificate, not a numerical surrogate.

Let `s(x)=min{x,1-x}`. Re-running the 35-pair multiplier elimination **without imposing `psi(1/2)=0`** gives the exact coefficient identity
\[
\boxed{
\sum_j\lambda_j[-L_{p_j,q_j}(\psi)]
=\frac{57}{256}\psi(3/8)-\psi(r)+\beta\psi(1/2),
}
\tag{1.3}
\]
with
\[
\boxed{
\beta=\frac{23156036957147}{44712962557360}
=0.517881966050477877\ldots .
}
\tag{1.4}
\]
Every other potential coefficient cancels exactly. This is the center-retaining version of the same positive dual; no approximation enters (1.3).

Therefore for **any symmetric potential** `Gamma`, the total actual slack carried by those 35 exact AND constraints is
\[
\boxed{
S(\Gamma):=\sum_j\lambda_jD^{\Gamma}_{\rm AND}(p_j,q_j)
=\Gamma(r)-\frac{57}{256}\Gamma(3/8)-\beta\Gamma(1/2)-C_E,
}
\tag{1.5}
\]
where the entire entropy side has collapsed to the scalar
\[
C_E:=\sum_j\lambda_jp_jq_jE(p_j,q_j).
\tag{1.6}
\]
Thus the 35-pair actual bank needs only the three source-exact potential nodes already published by account03/B12. The inaccessible/nonpublished intermediate h96 nodes cancel from the dual and are not guessed or regenerated.

## 2. Rigorous evaluation of the entropy scalar

The adjacent checker evaluates every logarithm in (1.2) by exact rational atanh series with a positive geometric tail. It first normalizes each positive rational `x` as `2^k m`, `1<=m<2`, then uses
\[
\log m=2\sum_{n=0}^{N-1}\frac{z^{2n+1}}{2n+1}+R_N,
\qquad z=\frac{m-1}{m+1},
\]
with
\[
0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]
A separate rational enclosure of `ln 2` converts to base two. With 110 terms for the source logs and 180 for `ln 2`, the resulting interval width is below `6.48e-110`.

It gives
\[
\boxed{
C_E=1.63351421007091222304932820885480331502196335566205998158\ldots
}
\tag{2.1}
\]
with interval width `<6.48e-110`.

## 3. The missing actual bank is not small — it is an order of magnitude larger than the prime deficit

Substitution of the exact h96 source nodes into (1.5) gives
\[
\boxed{
S(\Gamma_0)
=0.16560183593849715731720833825064298205303291178477\ldots
}
\tag{3.1}
\]
For the certified read-once potential
\[
\Gamma_{.01}=\Gamma_0+0.01t(1-t),
\]
the same 35-pair actual bank is
\[
\boxed{
S(\Gamma_{.01})
=0.16627753421779845285874987921918039913973777406954\ldots .
}
\tag{3.2}
\]
For the refuted lifted potential itself,
\[
\boxed{
S(\Gamma^\dagger)
=0.18372439190844233245046743959911083008819462214344\ldots .
}
\tag{3.3}
\]
All three displayed values have rigorous interval width `<6.48e-110`.

The uniform extra reserve from `Gamma_.01` to `Gamma^dagger` contributes exactly
\[
A\kappa
=0.01744685769064387959171756037993043094845684807390\ldots,
\tag{3.4}
\]
and the checker verifies
\[
S(\Gamma^\dagger)-S(\Gamma_{.01})=A\kappa
\]
to the rigorous interval width. This is an internal consistency check on the normalization and on the sign of every term.

Now compare with the genuine prime deficit
\[
d=0.0176114199558017537894958865691\ldots .
\]
The **uniform** bank (3.4) misses by only
\[
d-A\kappa\approx1.64562265157874198\times10^{-4},
\]
which is exactly why the account01/B16 dual obstruction worked. But the actual certified base-potential bank (3.2) is already
\[
\frac{S(\Gamma_{.01})}{d}>9.44,
\]
and the full actual bank of the lifted potential is
\[
\boxed{
\frac{S(\Gamma^\dagger)}d>10.43.
}
\tag{3.5}
\]
Equivalently,
\[
S(\Gamma^\dagger)-d
>0.16611297195264057866.
\tag{3.6}
\]

### Consequence

The 35-pair positive dual **does not obstruct** a same-base shaped repair once the genuine nonuniform AND slacks are allowed. The precise loophole left by account01/B16 and account02/B18 is real and quantitatively large: on the very same dual, the actual charged AND bank is over ten times the amount needed to repair the first prime deficit.

This does **not** construct a repair. A positive dual only supplies a necessary aggregate constraint. The individual pointwise inequalities
\[
L_{p_j,q_j}(\psi)\ge-D^{\Gamma^\dagger}_{\rm AND}(p_j,q_j)
\qquad(j=1,\ldots,35)
\tag{3.7}
\]
may still be mutually incompatible with the prime requirement
\[
\frac{57}{256}\psi(3/8)-\psi(r)>d
\tag{3.8}
\]
and with all other gates. What is proved is that the previously decisive **aggregate** obstruction disappears when evaluated against the source-exact actual slack.

## 4. Before/after and exact next implication

**FULL-PROBLEM CHANGE: NONE.** Full unrestricted uniform-cube FEI remains OPEN / NOT PROVED.

**MECHANISM CHANGE: YES.** Before this run, the fixed lift was refuted and the exact 35-pair dual proved that the entire uniform quadratic reserve could not repair it; the lead left actual nonuniform AND slack as the only same-base loophole. After this run, that loophole is evaluated source-exactly and is not marginal: its dual capacity exceeds the prime deficit by more than a factor ten.

The weakest useful next statement is now finite and noncircular:

> Find a symmetric perturbation `psi` (preferably on the finite rational support generated by the 35 charged pairs) satisfying all 35 pointwise inequalities (3.7), the prime repair (3.8), the desired center/cap condition, and the symmetry relations; then test that shaped potential against the next independent prime-gate constraints before promoting it to any universal candidate.

Equivalently, solve the exact finite Bellman-repair LP induced by the 35 inequalities rather than replacing their right sides by the uniform envelope `A M(p,q)`. A failure certificate must use the **actual** right-hand sides. A success only repairs this one witness and still leaves the all-gate quantifier.

A concurrent same-account B12 checker appeared during this run with a polynomial-shaped repair candidate, but no completed B12 report was present at the captured master. I therefore do not promote that checker to a theorem here; it is a useful next object to compare against (3.7) once its source-bound report is complete.

## 5. Verification and provenance

`CHECKER.py` uses standard-library exact `Fraction` arithmetic except for decimal rendering. It verifies:

1. the 35 exact multipliers collapse to support exactly `{3/8, 967/2048, 1/2}` with coefficients `(57/256,-1,beta)`;
2. the exact `kappa` rational from the peer certificate;
3. rigorous atanh-series intervals for every entropy term;
4. the three weighted actual slack values above;
5. the exact quadratic increment `S(Gamma^dagger)-S(Gamma_.01)=A*kappa` within the rigorous interval;
6. `S(Gamma^dagger)>0.18`.

The archived output returns `PASS`. Local source SHA-256 before upload: `6e077fb0747c18b6ea0f34a23e6d19ee4505af91c2ad2d9c803c1ca570632914`. Local output SHA-256: `632a79cd0236be32a362fab19f8521ce8e00be028d6fc8774627a086affa749a`.

Privacy review: the package contains only FEI mathematics, repository-relative source references, exact rational coefficients, and deterministic checker output. It contains no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, email/Drive material, public posting, paid API/model/Codex use, workflow dispatch, permission changes, or unrelated private data.
