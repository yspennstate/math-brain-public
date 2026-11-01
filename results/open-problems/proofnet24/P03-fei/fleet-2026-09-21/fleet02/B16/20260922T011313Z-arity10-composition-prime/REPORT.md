# B16 — a source-bound 10-input composition-prime gate already defeats the read-once gate margin

**Run:** `20260922T011231Z-b16-fei-gate-extremal-r11`  
**Status:** **ESSENTIAL_STEP_APPLIED / CANDIDATE_REFUTED for the old read-once potential. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Authenticated repository sources were consumed, but no native cognitive-brain retrieval was available.  
**Publication/novelty:** not assessed; no external priority claim is made.

## 0. Fresh control and target change

Fresh owner control was reread before the scientific write at brain main
fleet02/B16 Campaign-C half-band prompt: every FEI worker must converge on the
all-gate reformulation and either prove decomposable/AND extremality or falsify
it by a gate whose normalized required margin is larger. I therefore do not
continue the older positive/negative half-band ledger in this run.

The live gate margin is

\[
c_G(p)=-\frac{D_G(p)}{Q_G(p)},\qquad
Q_G(p)=I(G;p)/4-p_{\rm out}(1-p_{\rm out})\ge0.
\]

For the read-once base potential, `C0=Gamma(1/2)=6.4548`. Larger `c_G` is worse.
The proved read-once theorem remains `H <= 6.4573 I` and full FEI remains open.

**Tracked quantity.** Before this run, the consumed source state had an explicit
**composition-prime** falsifier at arity 18. This run lowers the certified upper
bound for an explicit source-bound prime falsifier to **arity 10**. This is not a
proof that 10 is minimal.

The three within-route moves used from the standing research rules were: **#2
attack the negation first** (seek a smaller prime falsifier), **#20 find why the
algorithm fails** (test whether the 10-input witness hides a disjoint block
composition), and **#30 one scale/direction at a time** (apply the complete block
criterion to the exact arity-10 restriction rather than launch another global
search).

## 1. Named completed other-account results consumed

### 1.1 fleet03/B12: exact 10-input gate and certified margin

I consume

`fleet03/B12/20260922T004418Z-arity10-gate-refutation/REPORT.md`, blob
`d12fe592f4fa6db16cb571557f6cc41392dd5860`.

It source-exactly restricts the balanced 18-input Numaro seed by fixing parent
coordinates

\[
(x_9,\ldots,x_{16})=(0,0,0,1,1,0,1,1)
\]

and leaving parent coordinates `0,...,8,17` free. The resulting 10-input truth
table has SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`.

The peer proves balance, monotonicity, essentiality of all ten variables,

\[
I(G)=\frac{257}{128},
\]

and the certified entropy interval

\[
6.509836127588151479 < H(G) < 6.509836127588151480.
\]

Therefore

\[
\frac{H(G)}{I(G)-1}>6.459372281637855731
\]

and, at uniform bias,

\[
\boxed{c_G>0.018289126551422926.}\tag{1.1}
\]

The same report notes that the complete two-input AND family is already
certified at quadratic margin `c=0.01`; hence (1.1) is a rigorous all-gate
violation of the old read-once potential. What that report did **not** prove was
that this 10-input gate is composition-prime: it excluded AND/OR read-once root
partitions, a strictly narrower structural claim.

### 1.2 fleet04/B14 and fleet04/B15: the correct prime notion

I also consume

`fleet04/B14/20260922T003849Z-prime-gate-falsifier/REPORT.md`, blob
`43ad8483eb8a56cb7141a33821ab89e4119dbc49`,

which proves the source-bound 18-input Numaro seed is composition-prime, and

`fleet04/B15/20260922T004054Z-gate-margin-composition/REPORT.md`,

which proves the exact physical block-composition laws

\[
D_{A(B_1,\ldots,B_m)}=D_A+\sum_i\lambda_iD_{B_i},\qquad
Q_{A(B_1,\ldots,B_m)}=Q_A+\sum_i\lambda_iQ_{B_i},
\]

with the same nonnegative weights, so `c_G` is their exact weighted barycenter.
Thus composition-prime gates are the correct structural atoms for the owner’s
extremal problem; excluding only AND/OR read-once decompositions is insufficient.

## 2. Complete cofactor criterion for one Boolean block

Let `f:{0,1}^{A disjoint_union B}->{-1,+1}`. For each assignment `a` to the
variables in `A`, write the cofactor

\[
f_a(b)=f(a,b),\qquad b\in\{0,1\}^B.
\]

### Lemma 2.1 — exact one-bit compression criterion

There are Boolean functions

\[
g:\{0,1\}^A\to\{0,1\},\qquad
H:\{0,1\}^{\{t\}\sqcup B}\to\{-1,+1\}
\]

such that

\[
f(a,b)=H(g(a),b)\tag{2.1}
\]

if and only if the family of cofactors `{f_a}` contains at most two distinct
functions.

**Proof.** If (2.1) holds, `f_a` is either `H(0,.)` or `H(1,.)`, so there are at
most two cofactors. Conversely, if the cofactors assume at most two values
`u_0,u_1`, define `g(a)=j` when `f_a=u_j` and define `H(j,b)=u_j(b)`. The
one-cofactor degenerate case is included by taking one unused value of `t`.
`QED`.

### Corollary 2.2 — complete test for disjoint composition-primality

Assume every input of an `n`-variable gate is essential. If it has a nontrivial
disjoint Boolean block decomposition with fewer than `n` outer inputs, then at
least one inner block contains at least two original variables, and that block
has at most two distinct cofactors. Conversely, any proper block of size at
least two with at most two cofactors gives a nontrivial decomposition by Lemma
2.1, using the remaining original variables as singleton outer inputs.

Hence an essential gate is composition-prime exactly when **every** proper block
`A` with `2 <= |A| <= n-1` induces at least three distinct cofactors.

This criterion is equivalent to the ANF rank-one criterion in the consumed
fleet04/B14 report, but is especially cheap at arity ten.

## 3. Exact application to the source-bound 10-input gate

The checker reconstructs the complete 18-input parent from the inherited exact
slice encoding, rejects it unless the parent truth-table SHA-256 equals

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,

then applies exactly the coordinate restriction in section 1.1 and rejects the
child unless its SHA-256 is the inherited 10-input hash above.

All ten child variables are essential. Therefore Corollary 2.2 requires testing
exactly

\[
\sum_{r=2}^{9}{10\choose r}=1012
\]

candidate blocks. The exact numbers of candidate blocks by size are

`45, 120, 210, 252, 210, 120, 45, 10`.

The minimum number of distinct complement-cofactors found at block sizes
`2,3,...,9` is respectively

\[
\boxed{3,5,8,9,7,6,4,3.}\tag{3.1}
\]

Thus no block comes close to the required value at most two. In particular,

\[
\boxed{\text{the 10-input gate is composition-prime}.}\tag{3.2}
\]

The deterministic rejection stream over all 1012 blocks has SHA-256

`354cf7d8a22dc986ef8ed33b0850eb0d08bdce99a195a33b24627d09e3be2073`.

As a separate exact locality check, none of the `20` one-coordinate cofactors and
none of the `180` two-coordinate cofactors is balanced; balanced descendants
first occur at codimension three (`40` among `960` restrictions). This is not a
minimality theorem, but it shows that the balanced-uniform obstruction does not
merely descend immediately to a balanced arity-9 or arity-8 cofactor.

The checker also independently recovers the inherited exact Walsh absolute-value
histogram and `I=257/128`; the peer's rational logarithm enclosure remains the
source for the entropy bound (1.1), so no floating logarithm is promoted to a
certificate here.

## 4. Direct consequence for the live owner target

Combining (3.2) with the inherited certified margin (1.1) gives

\[
\boxed{
\text{There is an explicit composition-prime 10-input balanced monotone gate}
\quad G\quad\text{with}\quad c_G>0.018289126551422926.
}\tag{4.1}
\]

Since the complete two-input AND constraint is certified at `c=0.01`, this gate
asks for strictly more margin. Therefore the old read-once `Gamma` is refuted on
a **prime gate already at arity ten**. The previous explicit source-bound prime
witness had arity 18; the structural obstruction is not an artifact of that
larger arity.

This does **not** refute FEI, and it does not improve the strongest known lower
bound on a universal cap: the 18-input and 162-input balanced constructions have
larger `H/(I-1)` ratios. Its contribution is narrower and exact: the explicit
prime arity of the old-potential falsifier drops from 18 to 10.

The current all-gate programme therefore cannot be repaired by proving only that
large bad gates decompose into paid smaller factors. A replacement potential
must survive genuinely composition-prime gates, and any bounded-arity search
below ten must include prime, non-read-once structure rather than only the
AND/OR formula classes.

## 5. Full-problem and mechanism change

**FULL-PROBLEM CHANGE: NONE.** Full uniform-cube FEI remains OPEN / NOT PROVED.
No finite dimension-independent universal constant is proved here.

**MECHANISM CHANGE: YES, within the owner-selected gate route.** Before: the
smallest explicit source-bound gate known in the consumed state to be both a
margin falsifier and fully composition-prime had arity 18. After: the exact
10-input restriction already has both properties. The missing universal
implication remains: construct a finite-cap symmetric potential satisfying (G)
for **all composition-prime gate/bias instances**, or prove a finite universal
margin bound by an equivalent signed recursion. The previous B16 exact
restriction-margin martingale remains valid, but this run does not claim its
block condition is paid universally.

## 6. Reproducibility and limitations

`check_b16_arity10_composition_prime.py` is standard-library only. It reconstructs
both truth tables source-exactly, checks all ten coordinates, recomputes the
integer Walsh histogram and exact influence, exhausts all 1012 candidate blocks,
and checks the shallow balanced restrictions described above.

Executed source SHA-256:

`3f5e7329b489c0da1d1f99cb3936f3d5cfb16320002fdaf82ce34874a2d60167`.

Captured output SHA-256:

`85ce8971d3b57fd00b666850b02a3af58974b1fd375b56a04360c02f5004ebc1`.

The finite execution is a self-check of the source-bound structural statement;
the cofactor criterion itself is proved above. The entropy/margin certificate is
inherited from fleet03/B12 and was not replaced by floating-point evidence.
No independent end-to-end FEI verification is claimed.

A scoped manual privacy/secret review of the files in this run found only
mathematical truth-table encodings, hashes, formulas and logical account/slot
labels; no credentials, scheduler identifiers, machine paths, personal data,
email or unrelated material are included.
