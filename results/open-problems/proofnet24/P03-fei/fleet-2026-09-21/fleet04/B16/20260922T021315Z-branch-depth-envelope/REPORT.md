# B16 — strong-concavity envelope for heterogeneous partial-branch shared grafts

**Outcome:** `AUXILIARY_ONLY / HETEROGENEOUS_BRANCH_DEPTH_CLOSED`. Full unrestricted uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Authenticated repository controls and mathematical sources were used directly; no authenticated mathematical-brain retrieval/context entered the derivation.  

## 1. Exact live target and peer versions consumed

The source-exact all-gate formulation is

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},\qquad V_u=4u(1-u),
\tag{1.1}
\]

and is constant-for-constant equivalent to full FEI. The old claim that the read-once potential is extremized by a decomposable/AND gate is already rigorously false, so this run does not redo that search.

The newest compatible exact inputs actually used are:

1. `fleet02/B15/20260922T015258Z-partial-branch-renormalization/REPORT.md`, blob `a8fd8e0a00b60ec8a4348d992f8df8d0365449b5`. It proves the repeated depth-four one-branch operator converges to
   \[
   6.5218511673478<R_*<6.5218511673480
   \tag{1.2}
   \]
   and names **heterogeneous branch depth and/or heterogeneous gate substitution** as the next adversarial optimization.
2. `fleet01/B17/20260922T014112Z-partial-branch-shared-core/REPORT.md`, blob `317694313bd078634b62d252fe9efa0085afcb14`. It proves the one-branch substitution calculus and the 5,805-variable strict improvement which motivated the renormalization.
3. `fleet02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`, blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`. It supplies the exact signed all-depth gate-margin/Poincare-currency identity; no positive-part replacement is legitimate.
4. `fleet03/B16/20260922T015509Z-numaro-two-step-block/REPORT.md`, commit `4b65fd3a49ec23454eaced80648d5b28e310cd42`. It shows that the 18-input Numaro obstruction's bad one-step selector margin is refunded by an authentic two-step adaptive block, so that source is not itself a depth-two obstruction.

For continuity only, the older user-named interface-C sources were freshly reread: `fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md` and `fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`. Their original-coordinate masks, signed orientation bank, negative-credit discipline and terminal accounting remain valid at their stated scopes, but they are not used below because the later owner message supersedes that mathematical assignment.

## 2. The exact shared-core scalar forcing function

The immutable shared-graft source compresses its 512 core Walsh amplitudes into nineteen triples `(A,Q,multiplicity)`. For a balanced monotone gadget whose distinguished singleton coefficient is `b`, the shared-core part has amplitudes

\[
\frac{A+bQ}{512}.
\]

Put

\[
\phi(u)=-u\log_2u,\qquad \alpha=\frac9{256},\qquad D_0=\frac{133}{128},
\]

\[
K(b)=H_{\rm core}(b)+\alpha\bigl[-\phi(b^2)+16(1-b^2)\bigr],
\qquad
T(b)=\frac{K(b)}{D_0}.
\tag{2.1}
\]

If a balanced gadget entering the shared-core operator has excess influence `D=I-1`, excess ratio `R=H/D`, and reusable singleton `b`, then exactly

\[
D'=D_0+\alpha D,
\qquad
R'=\frac{\alpha D}{D'}R+\frac{D_0}{D'}T(b).
\tag{2.2}
\]

Thus `T(b)` is the scalar forcing level of the source core. Controlling it controls every heterogeneous partial-branch step before any conjectural universal upper bound is invoked.

## 3. PROVED: an exact strong-concavity theorem for the source forcing

For the nineteen source classes one has exactly

\[
\sum mQ^2=9216,
\tag{3.1}
\]

and for every `0<=b<=1/4`, every nonzero amplitude satisfies

\[
|A+bQ|\ge1.
\tag{3.2}
\]

(The only class with `A=0` also has `Q=0`; for every other class `A` and `A+Q/4` have the same sign and endpoint magnitude at least one.) Hence

\[
\frac{(A+bQ)^2}{512^2}\ge2^{-18}.
\]

Differentiate `phi((A+bQ)^2/512^2)` twice. With `p=(A+bQ)^2/512^2`, the contribution is

\[
-2\left(\frac Q{512}\right)^2
\left(\log_2p+\frac3{\ln2}\right).
\tag{3.3}
\]

Using `p>=2^{-18}` and (3.1), the complete core contribution obeys

\[
H_{\rm core}''(b)
\le
\frac9{128}\left(18-\frac3{\ln2}\right).
\tag{3.4}
\]

The scalar term in (2.1) has second derivative

\[
\alpha\left(4\log_2b+\frac6{\ln2}-32\right)
\le
\frac9{256}\left(-40+\frac6{\ln2}\right)
\qquad (b\le1/4).
\tag{3.5}
\]

The `1/ln 2` terms cancel exactly. Therefore

\[
\boxed{K''(b)\le-\frac9{64}\qquad(0<b\le1/4).}
\tag{3.6}
\]

So the source forcing is not merely concave but uniformly strongly concave on the whole reusable-singleton range relevant to the current partial-branch family.

Exact rational atanh-series logarithm enclosures then give

\[
K'(0.002713295)>6.41967643\times10^{-10},
\]

\[
K'(0.002713296)<-8.09646492\times10^{-10}.
\tag{3.7}
\]

By (3.6), `K` has a **unique** maximizer `b_*` in

\[
\boxed{0.002713295<b_*<0.002713296.}
\tag{3.8}
\]

At the rational midpoint, strong concavity bounds the unobserved maximizer gain by `K'(b)^2/(2(9/64))`. This yields the certified forcing envelope

\[
\boxed{
T(b)\le T_{\max}<6.521851213012878
\qquad(0\le b\le1/4),
}
\tag{3.9}
\]

with the checker enclosing the maximum at `6.521851213012877723...` to the displayed digits.

This is an upper envelope for this **particular source-valid shared-core operator**, not an FEI upper bound.

## 4. PROVED: arbitrary heterogeneous integer branch depths have a tighter ceiling

Now solve the branch-depth part of the peer's heterogeneous optimization.

Suppose the current balanced monotone gate has reusable singleton `c`. Before applying the shared-core operator, form a one-branch chain of any integer depth `m>=1`. The chain preserves `R` exactly and has

\[
A_m(c)=1+c+\cdots+c^{m-1},
\qquad
D_{\rm chain}=A_m(c)D,
\qquad
b=c^m.
\tag{4.1}
\]

After the shared-core graft,

\[
c'=\frac{57}{256}+\frac{c^m}{256}.
\tag{4.2}
\]

Let

\[
a=\frac{57}{256},
\qquad
\bar c=\frac{57}{255}.
\]

The interval

\[
\boxed{a\le c\le\bar c}
\tag{4.3}
\]

is invariant under **every** integer choice `m>=1`, because

\[
a\le a+\frac{c^m}{256}
\le a+\frac{\bar c}{256}=\bar c.
\]

The certified starting singleton `14593/65536` lies in this interval.

Now use the unique maximizer (3.8). If `m>=4`,

\[
b=c^m\le\bar c^4
=0.002496540989691215\ldots<b_*.
\]

Since `K` is increasing to `b_*`,

\[
K(c^m)\le K(\bar c^4).
\tag{4.4}
\]

If `m<=3`,

\[
b=c^m\ge a^3
=0.011038362979888916\ldots>b_*.
\]

Since `K` decreases after `b_*`,

\[
K(c^m)\le K(a^3).
\tag{4.5}
\]

The exact log enclosure gives the strict comparison

\[
T(a^3)=6.521807145102301\ldots
<
T(\bar c^4)=6.521851180069835112\ldots .
\tag{4.6}
\]

Therefore every reachable integer-depth forcing level satisfies

\[
\boxed{
T(c^m)\le
T_{\rm int}:=T(\bar c^4)
<6.521851180069836.
}
\tag{4.7}
\]

For depth `m`, the exact ratio update is

\[
R'=
\frac{\alpha A_m(c)D}{D_0+\alpha A_m(c)D}R
+
\frac{D_0}{D_0+\alpha A_m(c)D}T(c^m),
\tag{4.8}
\]

a convex combination. Since the initial 162-input ratio is below `T_int`, induction on an **arbitrary adaptive sequence of integer depths** `m_0,m_1,...` gives

\[
\boxed{R_t\le T_{\rm int}<6.521851180069836\quad\text{for every finite heterogeneous-depth iterate}.}
\tag{4.9}
\]

This closes the branch-depth half of the peer's heterogeneous optimization: changing the one-branch depth from round to round can improve the presently certified lower bound only within this tiny operator-specific window. In particular, relative to the completed fixed-depth-four limiting upper endpoint `6.5218511673480`, the entire possible headroom is less than

\[
\boxed{1.3\times10^{-8}.}
\tag{4.10}
\]

No finite or infinite choice of integer branch depths inside this same construction can force a center cap above (4.7).

## 5. What remains and why this is not FEI

The theorem does **not** cover heterogeneous replacement by a genuinely different balanced gadget whose pair `(R,D,c)` lies outside the one-gate branch-depth recurrence. It also does not prove any all-gate upper potential. It proves a sharp source-valid envelope for the exact shared-core family that has generated the newest FEI lower-bound sequence.

The next nonredundant adversarial task is therefore no longer “try another branch length.” It is:

> construct a different balanced source gadget with a better joint tradeoff between `R=H/(I-1)` and its reusable singleton `c`, or prove a universal restriction/block inequality that upper-bounds all such gates while retaining the exact signed continuation credits of the fleet02/B16 martingale.

The fleet03/B16 two-step Numaro calculation strongly suggests the second direction should preserve adaptive descendant refunds; a pointwise one-coordinate margin is already known to be too strong.

Full unrestricted FEI remains **OPEN / NOT PROVED**.

## 6. Verification

`check_b16_branch_depth_envelope.py` is standard-library only. It verifies the nineteen compressed source classes, the exact identities `sum m=512` and `sum mQ^2=9216`, the amplitude lower bound needed for (3.6), exact rational log enclosures for both derivative signs in (3.7), the strong-concavity maximizer correction, the invariant interval (4.3), both forcing endpoints in (4.6), and the `1.3e-8` headroom statement. It exits `PASS`.

Checker SHA-256: `1a8a07f78d1fdf35d36792707676a6dcd9fe1e6d228118a60e3bb36f0b4ad2a2`.  
Captured output SHA-256: `57a83c206e4310c1478d38904b0e615f7bb8c2664f94d567369bdd51f7c976b8`.

No novelty or publication-priority claim is made.
