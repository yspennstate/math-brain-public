# MOC4 account02/B08 r11 — exact boundary-core reduction and strict repeated-face collars

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal `4 x 4` Marcus–de Oliveira target  
**Worker:** account02/B08  
**Candidate:** `MOC4-BOUNDARY-CORE-AND-COLLAR-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; the unrestricted MOC4 target remains **OPEN**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`; no brain-assisted experiment is claimed.

## 1. Exact inputs consumed

Fresh owner control before this scientific write was `math-research-brain` main commit `de6ad5f5cd0c0a4de6ed991e24c15228ef29dc17`, OWNER CONTROL revision `2026-09-22.2`. The effective owner instruction stops benchmark/installation work and assigns account02/B08 to the MOC4 repeated-eigenvalue/common-block boundary. The current five-file control read preserved that assignment and contained no later B08 stop.

The mathematical dependencies actually used are:

1. **This worker's preceding boundary theorem**, `account02/B08`, run `B08-20260922T000415Z-f12b18`, candidate `MOC4-DOUBLE-EIGENVALUE-LIFT-v1`, scientific commit `14542c0b3258ea5763ed145dff8dd4d2e47b2136`. It proves MOC4 whenever either spectrum has a repeated eigenvalue, by an exact permutation lift, and for every pair with a nontrivial common reducing subspace, by block factorization into the known dimensions at most three.
2. **Named partner account03/B09**, run `20260921T235010Z-b09-moc4-r01`, candidate `MOC4-C2-COMPLEMENT-BOUND-v1`. It compresses the middle exterior-power layer into the exact complementary-pair variables `R,D`, preserving complex phases and common-unitary origin.
3. **account01/B07**, `MOC4-MIXED-ASSIGNMENT-v1`. It proves the exact identity `D=(HPH^T)_{1^\perp}` for `P=(|u_ij|^2)` and reduces the remaining support inequality to one structured mixed `(P,R)` assignment problem.
4. **account03/B20 r11**, `ESSENTIAL_REDUCTION_PLUS_CONDITIONAL_THEOREM`. It rewrites the remaining support inequality exactly as `A(U)+S(U)>=Delta`, with nonnegative assignment slack `A`, orientation/minor slack `S`, and spectral parity deficit `Delta`.
5. **account04/B09 r02**, which refutes an unrestricted common `(P,R)` permutation lift and proves the structured coefficient discriminant `det(\widetilde G)=-(1/2) Delta(a)Delta(b)`.
6. **account04/B08**, `MOC4-GENERIC-STRICT-SUPPORT-v1`, which proves that any genuine failure can be perturbed to simple nonzero spectra, an irreducible pair, strict compound inequalities, and a unique supporting permutation.

A bounded current-archive search did not locate a completed `account03/B07` lead report. I therefore did not invent one or wait; I used the newest complete integrated MOC4 state above. No benchmark data or held-out answer material was used.

## 2. Compact conditional end-to-end route

After diagonalizing one matrix, the target is

\[
D(a,b,U):=\det(\operatorname{diag}(a)+U\operatorname{diag}(b)U^*)
\in K(a,b):=\operatorname{conv}\left\{v_\sigma(a,b):=\prod_i(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

The current end-to-end route is now:

1. Repeated-spectrum pairs and common-reducing-block pairs are already proved by `MOC4-DOUBLE-EIGENVALUE-LIFT-v1`.
2. The exact scalar-shift lemma below removes **individual singularity** without approximation while preserving the determinant, every one of the 24 comparison vertices, spectral simplicity, and irreducibility. Hence the only indispensable core is: both spectra simple, both matrices invertible, and the pair irreducible. Singular `A+B` is *not* removed and remains part of that core.
3. On the core, account01/B07 and account03/B20 reduce MOC4 to the exact structured inequality `A(U)+S(U)>=Delta`.
4. The strict repeated-face theorem below shows more than boundary validity: a generic repeated-spectrum point is surrounded by an **open MOC4-safe collar**. Therefore a counterexample sequence cannot approach the spectral discriminant unless a separate unitary/minor or planar-hull degeneration occurs.
5. account04/B09 rules out solving step 3 by an arbitrary joint `(P,R)` lift. The first unpaid universal implication is therefore the structured mixed-assignment inequality on the simple-spectrum irreducible invertible core, not another boundary case.

## 3. Exact all-pairs reduction by opposite scalar shift

### Theorem 1 — `MOC4-SIMPLE-IRREDUCIBLE-INVERTIBLE-CORE`

MOC4 for all complex normal `4 x 4` pairs is equivalent to MOC4 restricted to pairs `(A,B)` satisfying all three conditions:

1. both spectra are simple;
2. `A` and `B` are both invertible;
3. `A` and `B` have no nontrivial common reducing subspace.

No assumption that `A+B` is invertible is made.

### Proof

The unrestricted theorem trivially implies the restricted one. Conversely take an arbitrary normal pair `(A,B)`.

If either spectrum is repeated, the preceding `MOC4-DOUBLE-EIGENVALUE-LIFT-v1` proves the target. If the spectra are simple but the pair has a nontrivial common reducing subspace, the same preceding result proves the target by block factorization into dimensions at most three.

It remains only a simple-spectrum irreducible pair. For any `t in C` define

\[
A_t=A+tI,\qquad B_t=B-tI.
\tag{1}
\]

Both matrices remain normal and

\[
A_t+B_t=A+B,
\qquad
\det(A_t+B_t)=\det(A+B).
\tag{2}
\]

If `a_i,b_j` are the eigenvalues of `A,B`, then the shifted spectra are `a_i+t` and `b_j-t`, so **every comparison vertex is unchanged term by term**:

\[
\prod_i\bigl((a_i+t)+(b_{\sigma(i)}-t)\bigr)
=\prod_i(a_i+b_{\sigma(i)})
=v_\sigma(a,b).
\tag{3}
\]

Spectral simplicity is unchanged because eigenvalue differences are unchanged. A subspace reduces `A_t` iff it reduces `A`, and reduces `B_t` iff it reduces `B`; hence irreducibility is unchanged.

Finally choose

\[
t\notin\{-a_1,\ldots,-a_4,b_1,\ldots,b_4\}.
\tag{4}
\]

Only finitely many values are excluded, and for every other `t`, both `A_t` and `B_t` are invertible. The restricted-core theorem applied to `(A_t,B_t)` gives MOC4 for exactly the same determinant and exactly the same 24-point hull as `(A,B)`, by (2)--(3). This proves the converse. QED.

### Consequence

Individual singularity is not a genuine MOC4 obstruction in dimension four: it is removable by an **exact gauge symmetry**, not merely by a limiting argument. A singular sum `A+B`, however, is invariant under (1) and remains a legitimate interior-core case.

## 4. Strict repeated-face lift

The preceding repeated-eigenvalue proof produced some probability measure on `S_4`. Here I strengthen it: under the natural nondegeneracy conditions, the representing law has **full support on all 24 permutations**. This yields an open safe collar transverse to the repeated-spectrum boundary.

Assume after relabeling that

\[
a_1=a_2.
\tag{5}
\]

Write

\[
p_{ij}=|u_{ij}|^2,
\qquad
q_{jk}=|\det U[\{1,2\},\{j,k\}]|^2\quad(1\le j<k\le4).
\tag{6}
\]

By Cauchy--Binet,

\[
\sum_{j<k}q_{jk}=1,
\qquad
\sum_{k\ne j}q_{jk}=p_{1j}+p_{2j}.
\tag{7}
\]

Assume the boundary point is **lift-nondegenerate**:

\[
p_{ij}>0\quad\text{for every }i,j,
\qquad q_{jk}>0\quad\text{for every }j<k.
\tag{8}
\]

### Lemma 2 — strict fractional orientation

There are numbers `x_{j->k}>0` for all ordered distinct `j,k` such that

\[
x_{j\to k}+x_{k\to j}=q_{jk},
\qquad
\sum_{k\ne j}x_{j\to k}=p_{1j}.
\tag{9}
\]

### Proof

The ordinary fractional-orientation/max-flow criterion used in the preceding run is

\[
q(E(S))\le p_1(S):=\sum_{j\in S}p_{1j}
\tag{10}
\]

for every `S subset [4]`, with equality for `S=[4]`. Under (8), every nonempty proper cut is actually strict.

For `|S|=1`, `q(E(S))=0<p_1(S)`. For `S={j,k}`, the determinant bound gives

\[
q_{jk}\le(p_{1j}+p_{1k})(p_{2j}+p_{2k})<p_{1j}+p_{1k},
\tag{11}
\]

because row 2 has positive mass on the two columns outside `S`. For `|S|=3`, with complement `{ell}`, (7) gives

\[
q(E(S))=1-(p_{1\ell}+p_{2\ell})<1-p_{1\ell}=p_1(S).
\tag{12}
\]

Choose `epsilon>0` so small that

\[
2\epsilon<\min_{j<k}q_{jk},\qquad
3\epsilon<\min_j p_{1j},
\tag{13}
\]

and, for every nonempty proper `S`,

\[
\epsilon\left(3|S|-2\binom{|S|}{2}\right)
<p_1(S)-q(E(S)).
\tag{14}
\]

Define residual edge masses and outdegrees

\[
q'_{jk}=q_{jk}-2\epsilon,
\qquad p'_j=p_{1j}-3\epsilon.
\tag{15}
\]

Their totals agree:

\[
\sum_{j<k}q'_{jk}=1-12\epsilon=\sum_jp'_j.
\]

For a proper `S`, (14) is exactly

\[
q'(E(S))\le p'(S).
\tag{16}
\]

Hence the same max-flow criterion gives a nonnegative residual orientation `y`. Put

\[
x_{j\to k}=\epsilon+y_{j\to k}.
\tag{17}
\]

Then both orientations of every edge are at least `epsilon`, their pair sum is `q_{jk}`, and their outgoing sums are `p_{1j}`. QED.

### Theorem 3 — full-support permutation representation on a generic repeated face

Under (5) and (8), there is a probability law `mu` on `S_4` such that

\[
\mu(\sigma)>0\quad\text{for all }\sigma\in S_4,
\tag{18}
\]

all one-point marginals equal `p_{ij}`, the unordered image law of rows `{1,2}` equals `q_{jk}`, and

\[
\boxed{
\det(A+B)=\sum_{\sigma\in S_4}\mu(\sigma)
\prod_i(a_i+b_{\sigma(i)}).
}
\tag{19}
\]

### Proof

Apply Lemma 2 to rows 1,2. For rows 3,4 use Jacobi complementarity for a `4 x 4` unitary:

\[
|\det U[\{3,4\},K]|^2=q_{K^c}.
\tag{20}
\]

Thus the bottom unordered-pair law `r_K=q_{K^c}` has degrees `p_{3j}+p_{4j}` and is also strictly positive. Repeating Lemma 2 gives strictly positive bottom orientation masses `z_{j->k}` with pair sums `r_K` and outgoing sums `p_{3j}`.

For a permutation `sigma`, set `J={sigma(1),sigma(2)}` and define

\[
\mu(\sigma)
=\frac{x_{\sigma(1)\to\sigma(2)}
       z_{\sigma(3)\to\sigma(4)}}{q_J}.
\tag{21}
\]

All factors are positive. Summing the four orientations over a fixed unordered `J` gives total mass `q_J`; summing over the six `J` gives one. The one-point marginals are exactly those encoded by `x` and `z`, and the top two-set marginal is exactly `q`.

The preceding `MOC4-DOUBLE-EIGENVALUE-LIFT-v1` proves that, when `a_1=a_2`, these exact one-point marginals plus this one designated two-set marginal reproduce every layer of the exterior-power determinant expansion. Its algebra therefore applies unchanged to the stronger full-support law (21), yielding (19). QED.

The construction is quantitative: with the same `epsilon`, every orientation mass is at least `epsilon`, so every `mu(sigma)` is strictly positive (indeed `mu(sigma)>=epsilon^2/q_J`).

## 5. Open safe collar around a nondegenerate repeated-spectrum point

### Corollary 4 — repeated-face collar

Under the hypotheses of Theorem 3, suppose in addition that the finite set

\[
\{v_\sigma(a,b):\sigma\in S_4\}\subset\mathbb C\cong\mathbb R^2
\tag{22}
\]

is not collinear. Then `D(a,b,U)` lies in the ordinary interior of `K(a,b)`. Consequently there is an open neighborhood of `(a,b,U)` in the full spectral/unitary parameter space, including perturbations that split `a_1=a_2`, on which MOC4 remains true.

### Proof

Equation (19) is a convex representation with positive mass on every listed point. If `D` lay on a proper supporting face of `K`, equality of the support functional at the positive-weight average would force every positively weighted `v_sigma` onto that face. Because every `mu(sigma)>0`, all 24 points would lie there, contradicting properness. Thus `D` is in `relint K`; noncollinearity makes this ordinary planar interior.

Define its support margin

\[
\gamma=\min_{|\eta|=1}
\left(h_K(\eta)-\Re(\eta D)\right)>0,
\quad
h_K(\eta)=\max_\sigma\Re(\eta v_\sigma).
\tag{23}
\]

For perturbed data `(a',b',U')`, write `D'` and `v'_sigma`. Continuity of the determinant and the 24 polynomial vertices gives a neighborhood where

\[
|D'-D|+\max_\sigma|v'_\sigma-v_\sigma|<\gamma.
\tag{24}
\]

For every unit `eta`,

\[
h_{K'}(\eta)-\Re(\eta D')
\ge
\gamma-\max_\sigma|v'_\sigma-v_\sigma|-|D'-D|>0.
\tag{25}
\]

Hence `D'` lies in the interior of `K'`. QED.

### Corollary 5 — how a counterexample may approach the spectral discriminant

Suppose a sequence of genuine counterexamples converges to data with `a_1=a_2`. Then at least one of the following must happen at the limit:

1. some entry of the limiting coupling unitary vanishes;
2. some designated `2 x 2` minor `det U[{1,2},{j,k}]` vanishes;
3. the 24 limiting permutation products are collinear (equivalently, the planar interior margin in (23) collapses).

Otherwise Corollary 4 supplies a full neighborhood of MOC4-valid data, contradicting the counterexample sequence.

This complements the account04/B09 discriminant identity: simple spectra correspond to the nonzero Vandermonde coefficient determinant, while the present result shows that approaching its zero set cannot support a failure unless another geometric/unitary degeneration accompanies it.

The symmetric result holds when the repeated eigenvalue is in `b`, either by the same proof after swapping the two normal matrices or by symmetry of the target.

## 6. A common-block collar for the genuine `2+2` boundary

The earlier boundary theorem covers every common reducing subspace exactly. One useful strict subcase also has an open collar.

### Proposition 6 — transverse collar at a nonmonomial `2+2` split

Assume `A,B` have a common reducing decomposition into two two-dimensional blocks. Diagonalize `A` inside each block and let the relative `2 x 2` unitary in block `r` have

\[
t_r=|v^{(r)}_{11}|^2\in(0,1),\qquad r=1,2.
\tag{26}
\]

Then the block determinants have the exact two-vertex representations

\[
d_r=t_r(a_{r1}+b_{r1})(a_{r2}+b_{r2})
 +(1-t_r)(a_{r1}+b_{r2})(a_{r2}+b_{r1}).
\tag{27}
\]

Therefore

\[
\det(A+B)=d_1d_2
\tag{28}
\]

is a convex combination of the four block-preserving `S_4` permutation products with the four strictly positive weights

\[
t_1t_2,\quad t_1(1-t_2),\quad(1-t_1)t_2,\quad(1-t_1)(1-t_2).
\tag{29}
\]

If those four products have two-dimensional convex hull, then `det(A+B)` lies in its interior and hence in the interior of the full 24-point MOC4 hull. The support-margin argument of Corollary 4 gives an open MOC4-safe neighborhood, even though nearby pairs need not share the reducing decomposition.

This proposition does **not** assert an analogous collar for every `1+3` split: the exact boundary theorem still covers those points, but a full-support interior representation for the three-dimensional block is an additional condition not established here.

## 7. Relation to the current mixed-assignment obstruction

The boundary work now yields an exact named all-pairs reduction, not merely a list of solved special cases:

> **Remaining core.** It is enough to prove the account01/B07 structured mixed `(P,R)` inequality, equivalently the account03/B20 scalar inequality
> \[
> A(U)+S(U)\ge\Delta,
> \tag{30}
> \]
> for simple-spectrum, individually invertible, common-reducing-subspace-free normal pairs.

Moreover, any hypothetical counterexample sequence trying to escape this core through a repeated-spectrum face must simultaneously hit one of the unitary/minor/hull degeneracies in Corollary 5. Thus a proof by degeneration may concentrate specifically on those coupled boundary strata rather than the entire spectral discriminant.

The named partner account03/B09 middle-layer compression is used here in the conceptual separation: the repeated-face lift exactly couples the relevant two-set law to all one-point marginals, whereas the general simple-spectrum problem cannot do so. account04/B09's exact no-go result confirms that promoting this boundary lift to an unrestricted common `(P,R)` lift would be false.

## 8. First essential missing implication and next attack

The parent target remains open. After the boundary-core reduction, the first essential universal implication is:

\[
\boxed{
A(U)+S(U)\ge\Delta
\quad\text{for every structured support functional arising from}
\quad
\text{simple-spectrum, invertible, irreducible MOC4 data.}
}
\tag{31}
\]

A boundary-focused next step is narrower and compatible with B08's assignment: analyze sequences for which a spectral gap `|a_1-a_2|` tends to zero while (31) is allegedly violated. Corollary 5 says such a sequence must drive an entry, a designated compound minor, or the planar vertex-hull margin to zero. Each of those is an explicit lower-dimensional stratum. The next B08 run should test whether the exact Pluecker constraints and the partner `R,D` variables force one of these strata into a common reducing block or another already solved boundary, rather than reopening the generic mixed-assignment proof.

## 9. Checks, failures, and status

- The scalar-shift reduction is exact; it does not use continuity and does not alter either side of MOC4.
- The strict-orientation proof uses only true unitary minors and Cauchy--Binet/Jacobi identities, never an arbitrary bistochastic surrogate.
- Complex phases are preserved because the proof changes only the probability representation of the exact determinant expansion, not the spectra or determinant.
- The collar conclusion is conditional on a two-dimensional comparison hull. Collinear repeated-face points remain boundary-valid but are not claimed to have a transverse open collar from this argument.
- The `2+2` collar requires both block-mixing parameters in `(0,1)` and a two-dimensional four-vertex hull. No unsupported `1+3` strictness claim is made.
- No code was needed or executed for the theorem-sized claims in this report; all finite-dimensional identities used are proved on the page or source-bound to the cited completed dependencies.
- Scoped privacy/secret review: the changed files contain mathematical formulas, logical account/slot labels, public-style commit identifiers, and control revision only; no credentials, machine paths, scheduler identifiers, unrelated private data, raw transcripts, benchmark gold, or decryption material are included. An automated local repository scanner was not available in this connector-only execution, so this is a scoped manual fallback review, not a claimed automated PASS.

**Target-level movement:** MOC4 remains open.  
**Mechanism-level movement:** exact all-pairs reduction to the simple/invertible/irreducible core; full-support repeated-face representation; generic repeated-face open collar; nonmonomial `2+2` common-block collar.  
**Outcome:** `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

## 10. Runtime/provenance snapshot

- model self-report: `GPT-5.6 Sol` (`self_report`)
- reasoning effort requested by owner control: `maximum actually supported`
- reasoning effort configured: `UNKNOWN` / not exposed by the scheduler inventory schema used here
- provider reasoning-token usage: `null` / not exposed
- provider thinking seconds: `null` / not exposed
- report-snapshot elapsed execution: about `498` seconds from observed `2026-09-22T00:40:41Z` to `2026-09-22T00:48:59Z`; this includes tool/network/output overhead and is **not pure thinking**
- full brain connected: `false`
- scheduler scope inspected: own account only; all twenty managed B01--B20 tasks were observed enabled and hourly-valid, with the current collective/FEI role split and quiet task-level flags; no managed-slot deficit and no scheduler mutation by B08
