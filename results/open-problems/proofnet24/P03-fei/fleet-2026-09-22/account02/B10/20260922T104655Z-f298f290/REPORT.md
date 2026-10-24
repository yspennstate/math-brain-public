# account02/B10 — Near-dictator deficit payment

**Run:** `20260922T104655Z-f298f290`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-account02-B10` / pathway B  
**Classification:** `ESSENTIAL_STEP_APPLIED / UNIFORM_NEAR_DICTATOR_PAYMENT`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact target and source state

The assignment target is to prove, on an explicit balanced near-dictator regime, the exact influence-I-projection payment

\[
K_{\rm occ}\ge -B_{\rm inf}^\Gamma
\]

whenever the right side is positive, retaining the full binary-entropy logarithm and the actual Boolean source structure.

The source-exact I-projection identity used here is the pinned account02/B15 report at commit
`4bd6d05f1eb8325d665f2748f4d74dcee2550a04`:

\[
R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ},
\qquad
K_{\rm occ}=H_{\max}(r)-H(P).
\]

At a balanced uniform gate with center `C=Gamma(1/2)` this becomes

\[
R_\Gamma=C(I-1)-H(f)
        =B_{\rm inf}^\Gamma+K_{\rm occ}.
\tag{0.1}
\]

Thus, on any balanced source family, the desired payment is exactly equivalent to
`H(f) <= C(I(f)-1)`.

Two further source pins are used exactly:

* account04/B15 commit `7ec649dfb3d1ab2f92855f2069590fca2ac956dd`: the sparse one-point-defect suspension has an indispensable `Theta(epsilon log(1/epsilon))` KL scale, while full unweighted convolution L2 is only `Theta(I)`. This rules out replacing the logarithmic source cost by the retired unweighted-L2 mechanism.
* account02/B18 two-flip endpoint at repository snapshot `3739dd232ab781de9e899a5caf364a7144cf5bef`, path `proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T090632Z-safe-ray-zero-set/SPARSE_TWO_FLIP_ENDPOINT.md`: the Hamming-distance-two balanced two-point flip has an exact equal-small-atom spectrum.

The all-team correction ledger also marks fixed-depth retained-level KL plus one merged tail as refuted universally by recursive ternary majority. The theorem below does not use such a compression: it computes the **entire exact spectrum** of a restricted genuine Boolean source family, so the recursive-majority preflight does not apply to its conclusion.

The named partner is account03/B10. At the final partner preflight before this report, the current FEI fleet directory had no completed `account03/B10` FEI report or source-bound handoff; the available account03/B10 completions were from the retired POS3 programme and were therefore incompatible. No stale POS3 result is imported. Work proceeds asynchronously as the assignment requires.

## 1. New theorem: every balanced two-point flip of a dictator

Let `k>=3` and let `chi_1(x)=x_1` on `{-1,+1}^k`. Choose two vertices `a,b` with opposite dictator signs,
`chi_1(a)=-chi_1(b)`, and obtain `f` by flipping the values of `chi_1` **only** at `a,b`.
Then `f` is balanced.

Let

\[
d=d_H(a,b),\qquad q=2^{2-k},\qquad
C_*:=4+\frac1{\ln2}= 5.442695040888964\ldots .
\tag{1.1}
\]

### Theorem 1.1 — uniform exact deficit payment on the two-point near-dictator face

For every such `f`,

\[
\boxed{H(f)<C_*\,[I(f)-1].}
\tag{1.2}
\]

Consequently, for every symmetric potential whose balanced center obeys
`Gamma(1/2)=C>=C_*`,

\[
\boxed{K_{\rm occ}(f)\ge -B_{\rm inf}^\Gamma(f)}
\tag{1.3}
\]

(with strict inequality whenever `-B_inf^Gamma>0`).

If `d=1`, the stronger estimate holds:

\[
\boxed{H(f)<4[I(f)-1],}
\tag{1.4}
\]

so `C>=4` already pays the exact I-projection deficit on that subfamily.

This is a nontrivial infinite regime: all dimensions `k>=3`, all choices of opposite-sign flipped vertices, and every Hamming separation allowed by that sign condition.

## 2. Exact Walsh spectrum

Cube automorphisms preserving the dictator let us take

\[
a=(1,\ldots,1),\qquad
b_i=
\begin{cases}
-1,&i\in D,\\
+1,&i\notin D,
\end{cases}
\]

where `1 in D` and `|D|=d`.

Flipping a single vertex `z` changes the Walsh coefficient at `S` by

\[
-2^{1-k}\chi_1(z)\chi_S(z).
\]

Since `chi_1(a)=1`, `chi_1(b)=-1`, and
`chi_S(b)=(-1)^{|S\cap D|}`, the two perturbations sum to

\[
\Delta\widehat f(S)
=-2^{1-k}\left(1-(-1)^{|S\cap D|}\right).
\tag{2.1}
\]

Therefore

\[
\widehat f(S)=
\begin{cases}
1-q,&S=\{1\},\\
-q,&|S\cap D|\text{ is odd and }S\ne\{1\},\\
0,&\text{otherwise}.
\end{cases}
\tag{2.2}
\]

There are exactly `2^(k-1)-1` non-dominant nonzero coefficients. Hence the squared spectrum consists of

\[
(1-q)^2\quad\text{once},\qquad
q^2\quad\text{with multiplicity }2^{k-1}-1.
\tag{2.3}
\]

In particular, **the spectral entropy is independent of the Hamming separation `d`**.

Put

\[
s:=1-(1-q)^2=2q-q^2.
\]

The entropy in bits is exactly

\[
\boxed{
H(f)
=(1-q)^2\log_2\frac1{(1-q)^2}
 +(2q-q^2)\,2(k-2).
}
\tag{2.4}
\]

Equivalently, retaining the full binary-entropy form,

\[
\boxed{
H(f)=h_2(s)+s\log_2\left(\frac2q-1\right).
}
\tag{2.5}
\]

No logarithmic rare-event term has been discarded.

## 3. Exact influence and the geometry split

The total influence is the spectral first moment.

If `d>=2`, parity on `D` is nondegenerate after conditioning on any one coordinate, so each coordinate belongs to exactly `2^(k-2)` odd-parity subsets. Thus

\[
\sum_{|S\cap D|\ {\rm odd}}|S|=k2^{k-2}.
\]

Using (2.2),

\[
\boxed{I(f)-1=(k-2)q,\qquad d\ge2.}
\tag{3.1}
\]

If `d=1`, the odd-parity subsets are exactly those containing coordinate 1. Their total cardinality is
`(k+1)2^(k-2)`, and therefore

\[
\boxed{I(f)-1=(k-1)q,\qquad d=1.}
\tag{3.2}
\]

The `d=1` branch is exactly the sparse suspension geometry after renaming the dictator coordinate as the suspension bit.

## 4. Proof of the uniform constant

For `k=3`, (2.3) is the uniform four-atom spectrum, so `H(f)=2`.
Equation (3.1) gives `I-1=1/2` for `d>=2`, hence `H/(I-1)=4`; for `d=1`,
`I-1=1`, giving ratio 2. Thus (1.2) holds.

Now let `k>=4`. The elementary bound

\[
-\ln(1-q)\le \frac q{1-q}
\]

gives

\[
(1-q)^2\log_2\frac1{(1-q)^2}
\le \frac{2q(1-q)}{\ln2}.
\tag{4.1}
\]

For every `d`, (3.1)-(3.2) imply

\[
I(f)-1\ge(k-2)q.
\tag{4.2}
\]

Divide (2.4) by `(k-2)q` and use (4.1):

\[
\frac{H(f)}{I(f)-1}
\le
4-2q+\frac{2(1-q)}{(k-2)\ln2}
<
4+\frac1{\ln2},
\tag{4.3}
\]

because `k-2>=2`. This proves (1.2).

For `d=1`, divide instead by `(k-1)q`. The non-dominant part of (2.4) is strictly below `4(k-2)q`, while the dominant term in (4.1) is below `4q`; therefore

\[
H(f)<4(k-1)q=4[I(f)-1],
\]

proving (1.4).

Finally substitute (1.2) in the exact balanced identity (0.1). If `C>=C_*`, then
`R_Gamma=C(I-1)-H>0`, hence
`K_occ>-B_inf^Gamma`; when `B_inf^Gamma>=0` the requested inequality is automatic because `K_occ>=0`.
This proves (1.3). `QED`

## 5. Explicit logarithmic source certificate

Let `epsilon` be the fraction of cube vertices at which the dictator was changed. Here

\[
\epsilon=2^{1-k},\qquad q=2\epsilon,
\qquad \log_2\frac1\epsilon=k-1.
\tag{5.1}
\]

Therefore the exact influence deficits are

\[
\boxed{
I-1=
\begin{cases}
2\epsilon\log_2(1/\epsilon),&d=1,\\
2\epsilon[\log_2(1/\epsilon)-1],&d\ge2.
\end{cases}
}
\tag{5.2}
\]

Thus the payment currency itself retains the rare-event
`epsilon log(1/epsilon)` scale. This is precisely the logarithm lost by the refuted fixed unweighted-L2 compression on sparse suspensions.

The theorem therefore does more than re-check one witness: it proves that the exact logarithmic payment survives **every** balanced two-vertex dictator defect, regardless of separation.

## 6. Exact self-check

A standard-library checker exhaustively reconstructs the Walsh transform for all
`3<=k<=7` and every `1<=d<=k`, verifies (2.2), the exact nonzero multiplicity, and the exact rational influence formulas (3.1)-(3.2). It checks 25 `(k,d)` instances. The largest numerical entropy ratio in that finite self-check is approximately `4.5366340682647825`; the analytic theorem uses the larger rigorous constant `C_*`.

The checker is only a falsification/self-consistency test. The proof above is analytic and arbitrary-dimensional.

## 7. Scope, failed shortcut, and next unpaid implication

**What is proved:** a uniform `K_occ >= -B_inf` theorem on the complete balanced two-point dictator-defect regime, with a dimension-independent explicit center threshold `C_*`, and the sharper constant 4 on the distance-one suspension branch.

**What is not proved:** full FEI, a universal all-gate potential, or a payment theorem for an arbitrary near-dictator defect set.

**Rejected shortcut:** replacing the exact logarithmic source statistic by full unweighted convolution L2 remains invalid by the pinned account04/B15 sparse-suspension obstruction. This report does not revive it.

**First unpaid implication:** enlarge the defect set beyond one point in each dictator half while preserving the actual rare-event logarithm. A useful next target is a source-valid theorem of the form

\[
H(f)\le C\,[I(f)-1]
\]

for balanced dictator perturbations with defect set `A` satisfying an explicit geometric condition (for example, controlled overlap of the two half-cube defects or an exact edge-boundary condition), with all `h_2` terms retained. This would turn the two-point face into a genuine near-dictator neighbourhood rather than a one-dimensional obstruction family.

The named partner action remains pending only because no compatible completed account03/B10 FEI artifact existed at this run's publication preflight; no synchronous wait is required. The next compatible completed partner result should be tested against the exact identities (2.4), (3.1), and (3.2), not against a coarsened L2 surrogate.

No claim of publication novelty or full FEI closure is made.
