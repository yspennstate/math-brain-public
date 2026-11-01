# B18 — joint center/shape/AND-loss frontier for repairing the prime obstruction

**Run:** `20260922T074308Z-b18-fei-r21`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Change summary

The fixed all-gate candidate

\[
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\qquad \Gamma^\dagger(1/2)=6.521851214,
\]

is already source-exactly **REFUTED as a universal potential** by the composition-prime 18-input witness at
\(p_1=3/8\), \(p_2=\cdots=p_{18}=1/2\), output bias \(r=967/2048\). This does not refute FEI.

The preceding fleet04/B18 run proved a local shape barrier for an arbitrary additive repair \(\Gamma=\Gamma^\dagger+\eta\). Independently, the newest fleet02/B17 theorem proved that any center-preserving repair which fixes the same prime witness must spend a large amount of two-input-AND slack.

This run combines those two source-exact statements into one **universal repair frontier**. For every bounded symmetric additive repair, after removing its center component there is an explicit quantitative tradeoff between:

1. the amount by which the center is raised;
2. the mandatory local nonconcavity already identified by B18; and
3. the normalized amount of AND slack which the centered remainder must lose somewhere.

No concavity, differentiability, finite-dimensional ansatz or polynomial form is assumed for the repair.

## 1. Exact source inputs

### 1.1 Prime witness and B18 repair functional

From

`fleet04/B18/20260922T071537Z-prime-repair-shape-barrier/REPORT.md`

(report blob `10fe27f959269ff47003d1c27a17f7d6d36168f3`), let

\[
r={967\over2048},
\qquad
d:=-D_{\Gamma^\dagger}(P)>0.
\]

The source certificate gives

\[
d=0.0176114199558017537894958865691\ldots,
\qquad d>0.0176114.
\tag{1.1}
\]

For an arbitrary symmetric additive repair \(\eta\), the exact change in the prime witness defect is

\[
L_{\rm wit}(\eta)
={57\over256}\eta(3/8)
+{465\over256}\eta(1/2)
-\eta(r).
\tag{1.2}
\]

Repairing this witness requires

\[
L_{\rm wit}(\eta)\ge d.
\tag{1.3}
\]

The same B18 report defines, with \(E:=\eta(1/2)\),

\[
A=\bigl(\eta(3/8)-E\bigr)_+,
\qquad
B=\left({967\over1024}E-\eta(r)\right)_+,
\tag{1.4}
\]

and proves the necessary local-shape inequality

\[
\boxed{
{57\over256}A+B
\ge d-{1121\over1024}E.
}
\tag{1.5}
\]

### 1.2 Newest exact AND-slack rigidity theorem

From

`fleet02/B17/20260922T071234Z-and-slack-rigidity/REPORT.md`

(report blob `4a356a4ede8cadbf77347aac7cd746681048bbe4`), for a bounded symmetric center-zero perturbation \(\psi\), define the two-input AND correction

\[
L_{p,q}(\psi)=q\psi(p)+p\psi(q)-\psi(pq),
\tag{1.6}
\]

and

\[
M(p,q)=pq(1-p)(1-q).
\tag{1.7}
\]

If

\[
L_{p,q}(\psi)\ge-KM(p,q)
\quad\hbox{for every }p,q\in(0,1),
\tag{1.8}
\]

then the centered prime-witness correction

\[
R_{\rm wit}(\psi)
={57\over256}\psi(3/8)-\psi(r)
\tag{1.9}
\]

satisfies

\[
R_{\rm wit}(\psi)\le\kappa K,
\qquad
\kappa<0.069645.
\tag{1.10}
\]

This is an analytic finite-orbit theorem; no grid extrapolation is used.

## 2. Center normalization

Let

\[
q_*(u):=4u(1-u),
\qquad q_*(1/2)=1,
\tag{2.1}
\]

and decompose every bounded symmetric repair uniquely as

\[
\boxed{
\eta(u)=E q_*(u)+\psi(u),
\qquad E=\eta(1/2),
\qquad \psi(1/2)=0.
}
\tag{2.2}
\]

For the two-input AND,

\[
L_{p,q}(q_*)=4M(p,q).
\tag{2.3}
\]

For the prime witness, direct exact arithmetic gives

\[
\begin{aligned}
L_{\rm wit}(q_*)
&={57\over256}{15\over16}
+{465\over256}
-4{967\over2048}{1081\over2048}\\
&=\boxed{{1078193\over1048576}}
=1.0282449722290039\ldots .
\end{aligned}
\tag{2.4}
\]

Therefore

\[
\boxed{
L_{\rm wit}(\eta)
={1078193\over1048576}E+R_{\rm wit}(\psi).
}
\tag{2.5}
\]

This identity is the bridge between a center increase and the center-zero AND-loss theorem.

## 3. New theorem: universal center versus AND-loss frontier

For the centered remainder in (2.2), define its normalized AND-loss norm

\[
\mathcal K(\eta)
:=
\sup_{p,q\in(0,1)}
{[-L_{p,q}(\psi)]_+\over M(p,q)}
\in[0,+\infty].
\tag{3.1}
\]

If the supremum is infinite, all inequalities below are automatic. Otherwise, for every \(K>\mathcal K(\eta)\), condition (1.8) holds. Applying (1.10), then taking \(K\downarrow\mathcal K(\eta)\), gives

\[
R_{\rm wit}(\psi)\le\kappa\mathcal K(\eta)
<0.069645\,\mathcal K(\eta).
\tag{3.2}
\]

Combine (1.3), (2.5), and (3.2).

### Theorem 3.1 — repair frontier

Every bounded symmetric additive repair \(\eta\) of \(\Gamma^\dagger\) which repairs the exact biased composition-prime witness obeys

\[
\boxed{
{1078193\over1048576}E
+0.069645\,\mathcal K(\eta)
>d_0,
\qquad d_0:=0.0176114,
}
\tag{3.3}
\]

unless the left AND-loss norm is infinite, in which case the statement is trivial.

Equivalently, whenever

\[
E<{1048576\over1078193}d_0,
\]

one has the strict lower bound

\[
\boxed{
\mathcal K(\eta)
>
{d_0-(1078193/1048576)E\over0.069645}.
}
\tag{3.4}
\]

The zero-AND-loss endpoint of this frontier is

\[
\boxed{
E>
{1048576\over1078193}d_0
=0.01712763055074555\ldots,
}
\tag{3.5}
\]

so a repair whose centered remainder never worsens any AND inequality must raise the potential center above

\[
\boxed{
6.521851214+0.01712763055074555
=6.5389788445507455\ldots .
}
\tag{3.6}
\]

This reproduces the scale of the previously observed quadratic-center threshold, but now as a theorem for **arbitrary bounded symmetric repairs with zero normalized AND loss**, not just a one-parameter quadratic family.

For reference, the clean rigorous lower bounds from (3.4) are

\[
\begin{array}{c|c}
E & \mathcal K(\eta)\text{ must exceed}\\ \hline
0 & 0.2528738602\\
0.005 & 0.1790534157\\
0.010 & 0.1052329711\\
0.015 & 0.0314125266
\end{array}
\tag{3.7}
\]

They use only the coarse certified source deficit \(d>d_0\) and the rational coefficient in (2.4).

## 4. Joint shape-and-AND barrier

The preceding B18 shape inequality (1.5) and the new AND-loss frontier are simultaneous necessary conditions; neither pays the other.

### Corollary 4.1

Any bounded symmetric repair of the exact prime witness must satisfy both

\[
\boxed{
{57\over256}A+B
\ge d-{1121\over1024}E
}
\tag{4.1}
\]

and

\[
\boxed{
{1078193\over1048576}E
+0.069645\mathcal K(\eta)>d_0.
}
\tag{4.2}
\]

Thus a low-center repair must simultaneously introduce local shape distortion near the source points \(3/8,r,1/2\) **and** transport negative slack into at least one two-input AND inequality.

For example, if \(E=0.01\), then the source-exact shape theorem and the coarse deficit imply

\[
{57\over256}A+B>0.006664134375,
\tag{4.3}
\]

while independently

\[
\mathcal K(\eta)>0.1052329711.
\tag{4.4}
\]

This is stronger than either predecessor alone: the repair cannot choose between local nonconcavity and AND-slack transport; below the indicated center scale it needs both.

## 5. Integration with the current FEI proof state

The newest fleet01/B18 result

`fleet01/B18/20260922T065447Z-two-level-anti-amplification/REPORT.md`

proves a different, direct-FEI necessary condition: if FEI itself fails at \(C^\dagger\) and one chooses a minimum-dimensional counterexample, every original influence is below `0.1741`, every one-coordinate cofactor is noncharacter, no one-step conditional influence reaches `0.312`, and for each first pivot at least one child is `0.262`-diffuse. Its adaptive physical-tree inequality retains the posterior/joint-information credit. Those statements do **not** require \(\Gamma^\dagger\) to be a universal all-gate potential, so the prime-potential refutation does not invalidate them. Conversely, they do not repair the all-gate potential and are not used as closure credit in Theorem 3.1.

The newest compatible fleet04/B12 result (`20260922T0711Z-holevo-collar-slack-starvation`) proves a boundary starvation theorem for a negative balanced-child pivot of the **fixed** \(\Gamma^\dagger\) candidate. The newest B13 result (`20260922T0729Z-six-bit-dictator-collar`) closes a balanced six-bit near-character collar for that same fixed center. The newest B14 MUX collar (`20260922T062202Z-zero-credit-mux-collar`) likewise proves a true local safe region for the fixed candidate while retaining the selector-information credit. All three remain valid at their stated scopes, but because \(\Gamma^\dagger\) is now globally refuted they cannot be combined with an arbitrary repair \(\eta\) unless the repair's effect on their inequalities is separately paid. This report deliberately does not double-count them.

The older fleet04/B18 mixed-curvature identity remains unchanged:

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k.
\]

The exact zero-depth classification also remains unchanged: the all-zero-depth branch consists of a character times a signed one-point defect, up to irrelevant variables, and obeys its proved \(H<4J\) consequence. None of those facts implies \(\sum_k d_k=O(J)\), and no such refuted bridge is used here.

## 6. Smallest remaining universal arrow

The fixed candidate itself is no longer an open target; it is refuted. The smallest live all-gate problem is now a **slack-transport construction**:

> construct one symmetric nonnegative finite-cap potential \(\Gamma\) satisfying every gate inequality, while its difference from \(\Gamma^\dagger\) simultaneously satisfies the prime repair constraint, the AND family, and all remaining prime-gate constraints.

Theorem 3.1 shows that every bounded symmetric repair with center below `6.5389788445...` must spend a quantitatively nonzero amount of normalized AND slack. Corollary 4.1 additionally forces the local shape distortion from the preceding B18 run. A successor should therefore optimize the repair against the **actual source-certified AND slack profile**, not against a free-concavity or free-bump ansatz.

This is not full FEI, and no conditional input is promoted to unconditional closure.

## 7. Arithmetic check and scope

`CHECKER.py` verifies exactly that

\[
L_{\rm wit}(q_*)={1078193\over1048576}
\]

and reproduces the coarse-source frontier values (3.5)--(3.7) and the `E=0.01` shape residual (4.3). The theorem itself is analytic once the two cited source theorems are accepted.

Scoped privacy review: this report contains only FEI mathematics, source-bound repository paths/hashes, logical account/slot labels and nonsecret constants. It contains no credentials, private unrelated data, notification changes, email/Drive actions, paid/remote compute, workflow dispatch or permission changes.
