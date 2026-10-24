SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-24T05:12:34Z.
attacking: the overlap-heavy third-exterior residue after the disjoint E3 exit — identify the exact Schur degree ladder, pay the one-anchor class through the marginal-free Z2 half-Riesz theorem, and route the two-anchor zero-pair class through the newest dependence-safe partner receiver.

# account02/B03 — Schur overlap ladder, paid E1 anchor branch, and E2 cycle stress

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: decoupled time integral / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING THEOREMS / ONE-ANCHOR OVERLAP BRANCH PAID / TWO-ANCHOR RESIDUE SHARPENED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Unrestricted continuity remains OPEN. No moment, support, log-concavity, iid, Gaussian, diagonal-basis, post-rotation-independence, or hidden small-random-perturbation hypothesis is introduced.

The first unpaid implication at the start of this run was the overlap-heavy residue left by the preceding disjoint-exterior theorem. With

\[
\mathcal E_r(A)=\sum_{\substack{|S|=|T|=3\\|S\cap T|=r}}
\det A[S,T]^2,
\]

one has

\[
\sum_{r=0}^3\mathcal E_r(A)=e_3(A^2)\ge1
\]

under the owner hypothesis `s_3(A)>=1`. The previous run paid `\mathcal E_0` by a literal disjoint physical cross cut. This run attacks `r=1,2` without pretending that a single large minor must exist.

## 1. Sources and live corrections actually used

Required pinned source, read at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`:

- `RESULTS.md`: exact square completion and the square-peel interface;
- `FOURIER_ROUTE_REPORT.md`: audited volume-sampling decoupling and fractional-potential framework;
- `COUNTEREXAMPLE_SEARCH.md`: completed localized Theorem A, in particular the `n=3` bound `||p||_infinity<=6 sqrt(pi)/sigma` when all three physical eigenvalues have modulus at least `sigma`.

The marginal-free residual theorem used below is the earlier account02/B03 result

`QFORM-Z2-HALFRIESZ-MARGINAL-FREE-v1`,

`yspennstate/math-open-problems@68e6d8f52d904033878f6f55c376c38fd214684e`,

which proves, for any literal physical residual cross block with

\[
Z_2=e_2(MM^T)>0,
\]

that

\[
H_{1/2}(R):=\sup_s\mathbb E|R-s|^{-1/2}
\le8e^{1/4}Z_2^{-1/8}. \tag{1.1}
\]

The newest compatible designated partner account03/B03 result read this run is r49,

`yspennstate/math-open-problems@77db4c4d258bc99671c78d54d069830f80e2f752`,

with the later normalization supplement

`yspennstate/math-open-problems@ce3fecfe02212f5db3f9993cea2a0bea2f9cef3e`.

The supplement explicitly leaves all r49 theorem statements and constants unchanged. The two r49 interfaces used below are:

1. the exact-rank-three null-pivot / near-coloop half-Riesz theorem; and
2. the outer physical zero-diagonal hyperbola transducer. In abstract form, if exact completion of a genuine physical pair gives

\[
Q=2\mu[U+a(W)][V+b(W)]+R(W), \qquad \mu\ne0, \tag{1.2}
\]

with `U,V` genuine independent cap-one source coordinates and `W` disjoint from them, then the translation-uniform hyperbola density envelope implies

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le \sqrt2\,|\mu|^{-1/2}H_{1/2}(R).
} \tag{1.3}
\]

No independence between a sum and its conjugate difference is asserted anywhere in this report. Whole-copy identities are used only for the scalar output `Q-Q'`.

For one refinement in Section 6 I also use the already completed account03/B03 r47 translation-uniform product envelope, whose `L^3` norm satisfies

\[
\|K_\mu\|_3\le72^{1/3}|\mu|^{-2/3}. \tag{1.4}
\]

## 2. Exact Schur overlap ladder

The first new deterministic point is that the overlap classes `r=1` and `r=2` become different exterior degrees after exact physical Schur complementation.

### 2.1 One common anchor

Fix an original coordinate `i` and define

\[
\mathcal E_{1,i}(A)=
\sum_{\substack{P,Q\subset[n]\setminus\{i\}\\|P|=|Q|=2\\P\cap Q=\varnothing}}
\det A[\{i\}\cup P,\{i\}\cup Q]^2. \tag{2.1}
\]

Then

\[
\mathcal E_1(A)=\sum_i\mathcal E_{1,i}(A). \tag{2.2}
\]

Suppose

\[
d=A_{ii}\ne0 \tag{2.3}
\]

and let

\[
S^{(i)}=A_{-i,-i}-A_{-i,i}d^{-1}A_{i,-i} \tag{2.4}
\]

be the exact physical Schur complement. For every disjoint two-sets `P,Q`, the block determinant identity gives, up to the harmless row/column ordering sign,

\[
\det A[\{i\}\cup P,\{i\}\cup Q]
=d\,\det S^{(i)}[P,Q]. \tag{2.5}
\]

Therefore

\[
\boxed{
\mathcal E_{1,i}(A)
=d^2\!\sum_{\substack{|P|=|Q|=2\\P\cap Q=\varnothing}}
\det S^{(i)}[P,Q]^2.
} \tag{2.6}
\]

Thus **one-anchor third-exterior mass becomes disjoint second-exterior mass of the scalar Schur residual**.

### 2.2 Two common anchors

Fix a physical pair `K={i,j}` whose principal block

\[
B=A[K,K] \tag{2.7}
\]

is invertible, and write its Schur complement on `L=K^c` as

\[
S^{(K)}=A[L,L]-A[L,K]B^{-1}A[K,L]. \tag{2.8}
\]

Define the two-anchor mass carried by this pair,

\[
\mathcal E_{2,K}(A)=
\sum_{\substack{p,q\in L\\p\ne q}}
\det A[K\cup\{p\},K\cup\{q\}]^2. \tag{2.9}
\]

Again block determinant gives

\[
\det A[K\cup\{p\},K\cup\{q\}]
=\det(B)\,S^{(K)}_{pq}, \tag{2.10}
\]

so

\[
\boxed{
\mathcal E_{2,K}(A)
=\det(B)^2\sum_{p\ne q}|S^{(K)}_{pq}|^2.
} \tag{2.11}
\]

For a zero-diagonal hyperbolic pair

\[
B=\begin{pmatrix}0&\mu\\\mu&0\end{pmatrix}, \tag{2.12}
\]

this is

\[
\boxed{
\mathcal E_{2,K}(A)
=|\mu|^4\sum_{p\ne q}|S^{(K)}_{pq}|^2.
} \tag{2.13}
\]

This is the crucial degree drop: **two-anchor third-exterior mass becomes only off-diagonal first-order energy of the pair Schur residual, not residual `Z_2`.** Consequently an `E_2`-heavy state cannot be sent to the marginal-free `Z_2` theorem by bookkeeping alone. An additional smoothing structure must be proved.

Equations (2.6) and (2.11) are `QFORM-OVERLAP-SCHUR-LADDER-v1`.

## 3. One-anchor overlap is paid whenever its physical square currency is nondegenerate

### Theorem 3.1 — `QFORM-E1-ANCHOR-SQUARE-COMPILER-v1`

For an original coordinate `i` with `d=A_ii!=0` and `\mathcal E_{1,i}>0`,

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le
8\sqrt2\,e^{1/4}
\bigl(d^2\mathcal E_{1,i}(A)\bigr)^{-1/8}.
} \tag{3.1}
\]

Numerically the outer constant is

\[
8\sqrt2\,e^{1/4}=14.52708926969255\ldots . \tag{3.2}
\]

Every interval `I` therefore obeys

\[
\Pr(Q\in I)
\le14.5270892697\ldots
\bigl(d^2\mathcal E_{1,i}\bigr)^{-1/8}|I|. \tag{3.3}
\]

No row-marginal condition remains.

#### Proof

Randomly assign every residual coordinate independently to `I` or `J` with probability `1/2`. Put

\[
Z_2(I,J)=e_2\!\left(S^{(i)}[I,J]S^{(i)}[I,J]^T\right). \tag{3.4}
\]

Each ordered disjoint pair `(P,Q)` of two-sets in (2.6) is captured by the event `P subset I, Q subset J`, of probability exactly `2^{-4}=1/16`. Hence

\[
\mathbb E_{I|J}Z_2(I,J)
=\frac1{16d^2}\mathcal E_{1,i}(A). \tag{3.5}
\]

Thus some literal original-coordinate residual cut satisfies

\[
Z_2\ge\frac{\mathcal E_{1,i}(A)}{16d^2}. \tag{3.6}
\]

Now apply the required pinned square completion to the genuine original coordinate `X_i`:

\[
Q=d[X_i+h(X_{-i})]^2+R(X_{-i}), \tag{3.7}
\]

whose residual quadratic part is exactly `S^(i)`. The completed marginal-free theorem (1.1) and the pinned square peel give

\[
\|p_Q\|_\infty
\le |d|^{-1/2}H_{1/2}(R)
\le8e^{1/4}|d|^{-1/2}Z_2^{-1/8}. \tag{3.8}
\]

Substituting (3.6),

\[
\|p_Q\|_\infty
\le8e^{1/4}|d|^{-1/2}
\left(\frac{\mathcal E_{1,i}}{16d^2}\right)^{-1/8}
=8\sqrt2 e^{1/4}(d^2\mathcal E_{1,i})^{-1/8}. \tag{3.9}
\]

This proves (3.1). All cuts and completions use original coordinates. QED.

The scale is correct: under `A -> cA`, the currency `d^2 E_{1,i}` scales as `c^8`, so its inverse eighth root scales as `|c|^{-1}`.

## 4. Assigned whole-copy weighted-time estimate on the E1 branch

Write

\[
\Gamma_i=d^2\mathcal E_{1,i}(A),
\qquad
H_i=8\sqrt2 e^{1/4}\Gamma_i^{-1/8}. \tag{4.1}
\]

Theorem 3.1 gives `||p_Q||_infinity<=H_i`. Therefore the whole scalar difference `Q-Q'` has density cap at most `H_i`. Layer cake gives

\[
\mathbb E|Q-Q'|^{-1/2}\le2\sqrt{2H_i}, \tag{4.2}
\]

and using only

\[
|\phi_Q(t)|^2=\mathbb E e^{it(Q-Q')} \tag{4.3}
\]

for the entire output,

\[
\boxed{
\int_{\mathbb R}|t|^{-1/2}|\phi_Q(t)|^2dt
\le
2^{15/4}\sqrt\pi\,e^{1/8}\Gamma_i^{-1/16}.
} \tag{4.4}
\]

Numerically,

\[
\boxed{
\int |t|^{-1/2}|\phi_Q(t)|^2dt
\le27.0224194114\ldots\,\Gamma_i^{-1/16}.
} \tag{4.5}
\]

Likewise

\[
\Pr(|Q-Q'|\le\varepsilon)
\le16\sqrt2 e^{1/4}\Gamma_i^{-1/8}\varepsilon. \tag{4.6}
\]

No coordinatewise sum/difference pair is separated.

## 5. Newest account03/B03 r49 applied to a zero-pair + residual `Z_2` branch

The latest partner r49 outer-hyperbola interface (1.3) composes directly with the marginal-free residual theorem (1.1).

### Corollary 5.1 — `QFORM-ZEROPAIR-PLUS-Z2-HALFRIESZ-v1`

Suppose genuine original coordinates `i,j` satisfy

\[
A_{ii}=A_{jj}=0,\qquad A_{ij}=\mu\ne0. \tag{5.1}
\]

Complete those two physical coordinates exactly, and let `R` be the Schur residual on the remaining original-coordinate bank. If some literal physical residual cut has

\[
Z_2=e_2(MM^T)>0, \tag{5.2}
\]

then

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le8\sqrt2 e^{1/4}
|\mu|^{-1/2}Z_2^{-1/8}.
} \tag{5.3}
\]

Thus every interval `I` satisfies the same coefficient times `|I|`, and

\[
\boxed{
\int |t|^{-1/2}|\phi_Q(t)|^2dt
\le27.0224194114\ldots\,
|\mu|^{-1/4}Z_2^{-1/16}.
} \tag{5.4}
\]

#### Proof

Exact physical pair completion has the form (1.2). The newest partner r49 transducer gives

\[
\|p_Q\|_\infty
\le\sqrt2|\mu|^{-1/2}H_{1/2}(R). \tag{5.5}
\]

Apply (1.1) to the actual Schur residual, preserving every same-residual curvature term and every affine term:

\[
H_{1/2}(R)\le8e^{1/4}Z_2^{-1/8}. \tag{5.6}
\]

Equations (5.5)-(5.6) give (5.3). The whole-copy time estimate follows exactly as in Section 4. QED.

This is an equation-level use of the **newest** completed account03/B03 theorem after its correction supplement, not a citation-only splice.

The exact two-anchor identity (2.13) also explains why (5.3) does not automatically pay all of `E_2`: `E_{2,K}` controls only `sum_{p!=q}|S_pq|^2`, whereas (5.3) needs genuine residual second exterior volume.

## 6. A second useful transducer: any paid residual density can be wrapped by a physical hyperbola

The r47 translation-uniform envelope (1.4) yields another composition rule which is useful when a residual has already reached an `L^infinity` receiver rather than a half-Riesz receiver.

### Theorem 6.1 — `QFORM-HYPERBOLA-PAID-RESIDUAL-L3-v1`

Under the exact zero-pair completion (1.2), suppose `R` has a density satisfying

\[
\|p_R\|_\infty\le H. \tag{6.1}
\]

Then

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le72^{1/3}|\mu|^{-2/3}H^{1/3}.
} \tag{6.2}
\]

#### Proof

Condition on the residual original-coordinate bank `W`. The conditional hyperbola density is bounded by the same translated-product envelope `K_mu`, regardless of the shifts `a(W),b(W)`. Hence

\[
p_Q(q)\le\mathbb E K_\mu(q-R(W))
=(K_\mu*p_R)(q). \tag{6.3}
\]

Since `p_R` has mass one and cap `H`,

\[
\|p_R\|_{3/2}^{3/2}
=\int p_R^{3/2}
\le H^{1/2},
\qquad
\|p_R\|_{3/2}\le H^{1/3}. \tag{6.4}
\]

Holder/Young with exponents `3` and `3/2`, followed by (1.4), proves (6.2). QED.

The shifts are allowed to depend on all residual variables; no independence between the hyperbola output and `R` is assumed.

## 7. Exact target-valid two-anchor stress: the 5-cycle

Let `A_5` be the adjacency matrix of the physical cycle `C_5`:

\[
A_5=
\begin{pmatrix}
0&1&0&0&1\\
1&0&1&0&0\\
0&1&0&1&0\\
0&0&1&0&1\\
1&0&0&1&0
\end{pmatrix}. \tag{7.1}
\]

Its exact spectrum is

\[
\boxed{
\left\{2,
\frac{\sqrt5-1}{2},\frac{\sqrt5-1}{2},
-\frac{\sqrt5+1}{2},-\frac{\sqrt5+1}{2}\right\}.
} \tag{7.2}
\]

Thus it lies in the exact owner target: three eigenvalues have modulus at least one.

Its third-exterior overlap ledger is

\[
\boxed{
\mathcal E_0=0,\qquad
\mathcal E_1=20,\qquad
\mathcal E_2=30,\qquad
\mathcal E_3=0.
} \tag{7.3}
\]

Indeed `E0=0` is forced by `n=5`: two disjoint triples do not exist. `E3=0` because every physical diagonal vanishes and `C5` has no triangle; a zero-diagonal `3x3` symmetric determinant is twice the product of its three edge entries. The total is

\[
e_3(A_5^2)=50, \tag{7.4}
\]

consistent with (7.3). More finely, by five-fold symmetry,

\[
\boxed{\mathcal E_{1,i}=4\quad\text{for every }i,} \tag{7.5}
\]

while the two-anchor mass is carried exactly by the five physical edges:

\[
\boxed{
\mathcal E_{2,K}=6\ \text{if }K\text{ is an edge of }C_5,
\qquad
\mathcal E_{2,K}=0\ \text{otherwise}.}
\tag{7.6}
\]

Because all physical diagonals are zero,

\[
A_{ii}^2\mathcal E_{1,i}=0 \tag{7.7}
\]

for every anchor. Hence Theorem 3.1 is genuinely unavailable despite the large one-anchor mass. This is a source-valid obstruction to treating the scalar-pivot E1 compiler as exhaustive.

Now choose the physical edge `K={0,1}`. Its pair block is

\[
B=\begin{pmatrix}0&1\\1&0\end{pmatrix}. \tag{7.8}
\]

Exact Schur complementation leaves on coordinates `(2,3,4)`

\[
S=
\begin{pmatrix}
0&1&-1\\
1&0&1\\
-1&1&0
\end{pmatrix}. \tag{7.9}
\]

Its eigenvalues are exactly

\[
\boxed{\{-2,1,1\}.} \tag{7.10}
\]

Equation (2.13) gives

\[
\mathcal E_{2,K}=1^4\sum_{p\ne q}|S_{pq}|^2=6, \tag{7.11}
\]

which is the edge contribution in (7.6).

### 7.1 Newest partner r49 pays the same physical cycle

The residual (7.9) is an exact-rank-three null-pivot form. Since it already lives on three physical coordinates, the spectral frame may be taken as the identity, so a null physical coordinate has leverage

\[
q=1, \tag{7.12}
\]

and the spectral floor is

\[
s=1. \tag{7.13}
\]

The newest account03/B03 r49 theorem therefore gives the actual residual half-Riesz estimate

\[
\boxed{H_{1/2}(R)\le8.} \tag{7.14}
\]

Applying its outer hyperbola transducer to the genuine physical edge pair with `mu=1` gives

\[
\boxed{
\|p_{X^T A_5 X}\|_{\infty,\mathrm{ess}}
\le8\sqrt2
=11.31370849898476\ldots .
} \tag{7.15}
\]

Hence every interval `I` obeys

\[
\Pr(X^T A_5 X\in I)\le8\sqrt2\,|I|. \tag{7.16}
\]

This is a literal target-valid equation-level use of the newest partner theorem.

The corresponding whole-copy time estimate is

\[
\boxed{
\int |t|^{-1/2}|\phi_{A_5}(t)|^2dt
\le4\sqrt{8\sqrt2\,\pi}
=23.8472014309\ldots .
} \tag{7.17}
\]

### 7.2 Required pinned `e5f71d79...` result gives a sharper residual route

Apply the completed pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A to the **actual residual matrix** (7.9). Because all three residual eigenvalues have modulus at least one, uniformly in the affine terms generated by pair completion,

\[
\boxed{\|p_R\|_\infty\le6\sqrt\pi.} \tag{7.18}
\]

Now apply Theorem 6.1 with `mu=1` and `H=6sqrt(pi)`:

\[
\boxed{
\|p_{X^T A_5 X}\|_\infty
\le
72^{1/3}(6\sqrt\pi)^{1/3}
=(432\sqrt\pi)^{1/3}
=9.14856323739925\ldots .
} \tag{7.19}
\]

Thus the required pinned source has been used at an actual new one-copy inequality, not merely cited.

The associated whole-copy time bound is

\[
\boxed{
\int |t|^{-1/2}|\phi_{A_5}(t)|^2dt
\le4\sqrt{\pi(432\sqrt\pi)^{1/3}}
=21.4442753415\ldots .
} \tag{7.20}
\]

The `C5` example is therefore **not** a QFORM counterexample. Its role is structural: it has no disjoint third-volume at all, no physical square anchor at all, no principal triple determinant at all, but a large two-anchor exterior reserve. A valid proof must contain a genuine two-anchor / residual mechanism such as r49, the zero-pair-plus-Z2 compiler, a pair theorem, or another aggregate receiver.

## 8. Sharpened global exterior fork

The preceding disjoint-exterior theorem may be combined with the present results as follows. Fix the convenient threshold

\[
\eta=1/64. \tag{8.1}
\]

If

\[
\mathcal E_0(A)\ge\eta, \tag{8.2}
\]

the already completed disjoint physical-E3 route gives a universal one-copy density bound.

If instead

\[
\mathcal E_0(A)<1/64, \tag{8.3}
\]
then, since total third-exterior energy is at least one,

\[
\mathcal E_1+\mathcal E_2+\mathcal E_3>63/64, \tag{8.4}
\]
so

\[
\boxed{
\max(\mathcal E_1,\mathcal E_2,\mathcal E_3)>21/64.
} \tag{8.5}
\]

On the one-anchor branch define

\[
\Gamma_1(A)=\max_i A_{ii}^2\mathcal E_{1,i}(A). \tag{8.6}
\]

If

\[
\Gamma_1(A)\ge1/64, \tag{8.7}
\]
then Theorem 3.1 gives the universal numerical bound

\[
\boxed{
\|p_Q\|_\infty
\le24.4315545819\ldots .
} \tag{8.8}
\]

Therefore a genuinely unpaid `E1`-heavy state must satisfy simultaneously

\[
\boxed{
\mathcal E_1>21/64,
\qquad
A_{ii}^2\mathcal E_{1,i}<1/64\quad\text{for every }i.
} \tag{8.9}
\]

This is a substantially narrower residue than merely saying that no disjoint `E3` cut was found.

On the two-anchor branch, (2.11) says the exact remaining currency is aggregate off-diagonal energy of pair Schur complements. For a zero pair, either a genuine residual `Z2` appears and Corollary 5.1 pays it, or another receiver is needed. The `C5` calculation shows concretely that residual `Z2` need not exist even when `E2` is very large; the newest r49 near-coloop mechanism can nevertheless close that finite-dimensional geometry.

The principal-overlap class `E3` and the diffuse/ill-conditioned `E2` class remain unpaid in general.

## 9. First unpaid implication after this run

The first unpaid B03 implication is now the following product-preserving structural statement.

Starting from an overlap-heavy survivor satisfying (8.3), prove that at least one of the following holds with universal parameters:

1. a one-anchor square currency `A_ii^2 E_{1,i}` is nondegenerate, already paid by Theorem 3.1;
2. an invertible/zero physical pair has a Schur residual with genuine `Z2`, paid by Corollary 5.1;
3. the pair Schur residual enters the newest r49 near-coloop/null-pivot class, a balanced-carrier E3 class, a localized three-coordinate class, or another already-paid finite-hub/low-rank receiver;
4. the aggregate principal-overlap `E3` mass has a valid product-preserving receiver.

The unresolved two-anchor core is now explicit: large

\[
\det(B)^2\sum_{p\ne q}|S^{(K)}_{pq}|^2
\]

with every usable pair/local residual receiver quantitatively weak. No selection of one large physical minor is justified from this aggregate alone.

The mechanism has changed from the previous run's random disjoint-third-volume extraction to a Schur-degree analysis and recursive fractional-potential transduction. The full conjecture remains OPEN.

## 10. Status and correction audit

This run does not use any live-refuted premise. In particular:

- no arbitrary-joint 3D coarea cap;
- no post-rotation independence;
- no conditional cap for one conjugate sum/difference variable given the other;
- no law-uniform pointwise quadratic decay;
- no assumption that a small matrix tail is a small random quadratic perturbation;
- no universal good single minor;
- no universal rank-three physical cross cut.

The one-copy density bounds are proved before the whole-copy weighted-time consequences. Essential boundedness is established only on the stated branches; continuity is not promoted across the square/hyperbola interfaces without a separate argument.

Full QFORM: **OPEN**. Full-target continuity: **OPEN**.
