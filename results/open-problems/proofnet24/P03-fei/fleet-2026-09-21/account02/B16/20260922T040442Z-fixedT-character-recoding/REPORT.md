# B16 — fixed-support signed host-character recoding theorem

**Run:** `20260922T035834Z-b16-fei-allgate-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / ADVERSARIAL_SOURCE_FAMILY_EXCLUDED`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and scientific sources were consumed directly, but no authenticated installed-brain retrieval/context was used.

## 0. Later control and last-three comparison

Fresh owner control revision `2026-09-22.2` supersedes the older Campaign-C half-band assignment mathematically and converges the FEI fleet on the all-gate inequality. I therefore do not reopen the retired positive-current-only route. The current stable post-falsifier candidate is

\[
C_*=6.5218512,
\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\]

with the universal missing statement `LIMIT-PRIME-GATE-LIFT-v1`: prove the all-gate slack nonnegative for every composition-prime Boolean gate and every interior product bias.

The last three completed substantive account02/B16 stages were: (i) the exact restriction-margin martingale, which retained all descendant slack and identified the all-depth Poincare-weighted margin barycenter; (ii) the source-bound arity-10 composition-prime falsifier of the old read-once potential; and (iii) the stable-candidate shared-core threat corridor, which excluded every adaptive integer one-branch depth and localized a heterogeneous fixed-core violation to an absolute defect below `3.846028304990334e-7` and a narrow singleton interval. The present run does not repeat any of those mechanisms.

**FULL-PROBLEM CHANGE: NONE.** Full FEI remains open.  
**MECHANISM CHANGE: YES.** The newest account03 adversary report explicitly left changed host-group sizes as a legitimate degree of freedom for the exact 18-cell source obstruction. Here that entire fixed-support degree of freedom is removed symbolically, including arbitrary row orientations and arbitrary nonzero host characters.

## 1. Named completed OTHER-account results consumed and applied

I use two completed peer results.

1. **account03/B18**, `20260922T032411Z-n18-host-repairing-barrier/REPORT.md`, blob `3acc87960b7179fa094c8a27d43f1f9beae5fb34`. It reconstructs the exact balanced 18-variable source gate, with core dimension nine, exceptional core set
\[
T=\{78,79,113,121,228,484,170,186,149,151,338,466,284,316,291,295,393,457\},
\tag{1.1}
\]
source pairing
\[
(78,79),(113,121),(228,484),(170,186),(149,151),(338,466),(284,316),(291,295),(393,457),
\tag{1.2}
\]
and the rigid fact that these nine pairs are **all** Hamming-distance-one edges induced by `T`. It proves the source entropy/influence data
\[
I_0=\frac{261}{128},
\]
\[
H_0\le
6.776605309005978082519790221891882314787235039,
\tag{1.3}
\]
and excludes all 34,459,425 re-pairings into two-cell host channels. Its stated next adversarial freedoms include changed host group sizes. The theorem below attacks exactly that freedom.

2. **account04/B12**, `20260922T031946Z-heterogeneous-shared-graft-exclusion/REPORT.md`, blob `e6854578d1cf8be7058847a80a558fc512f6f435`. It applies the preceding B16 threat-corridor theorem to exclude the whole known recursive hard family, all actual singleton re-markings, and all balanced self-compositions from the heterogeneous shared-core corridor. Thus recycling the record family is no longer a live attack; a fixed-support recoding of the prime source gate is a distinct remaining source-valid adversarial mechanism.

## 2. Arbitrary signed character recoding of the fixed exceptional support

Put `N=2^9=512`. Let `a:{0,1}^9->{-1,0,1}` be the fixed empty-host core obtained from the source construction by setting the eighteen rows in `T` to zero and keeping the source core elsewhere. The peer reconstruction implies `a` has zero mean.

Let `m>=1`. For every `x in T`, choose

- a nonzero host character label `lambda(x) in F_2^m \ {0}`;
- an arbitrary orientation `epsilon_x in {+1,-1}`.

Define the Boolean gate on nine core bits and `m` host bits by
\[
F_{\lambda,\epsilon}(x,y)=
\begin{cases}
\epsilon_x\,\chi_{\lambda(x)}(y),&x\in T,\\
a(x),&x\notin T.
\end{cases}
\tag{2.1}
\]
where on `x notin T` the value `a(x)` is the original `+-1` core value. Every such gate is balanced under uniform inputs because each nonzero host character has mean zero and the empty-host core has mean zero.

This family strictly contains arbitrary set partitions of the eighteen exceptional rows into host groups: equal labels form one group. It also permits arbitrary row signs and host characters of any positive degree. Distinct groups need not have size two, and the number of host bits need not be nine.

For a nonzero host character `u`, set
\[
A_u=\{x\in T:\lambda(x)=u\},\qquad r_u=|A_u|,
\]
and define the signed Walsh sum
\[
z_u(S)=\sum_{x\in A_u}\epsilon_x\chi_S(x).
\tag{2.2}
\]
Direct averaging over the host cube gives the exact Fourier decomposition
\[
\widehat F(S,U)=
\begin{cases}
\widehat a(S),&U=0,\\
N^{-1}z_U(S),&U\ne0.
\end{cases}
\tag{2.3}
\]
Thus all nonzero-host blocks remain orthogonal, and the empty-host block is identical for every recoding.

## 3. Exact block identities

Fix one nonempty block `A=A_u`, write `r=|A|`, `z_S=z_u(S)`, and let `d=|u|>=1`. Its squared Fourier masses are
\[
q_S=\frac{z_S^2}{N^2}.
\]
Parseval gives
\[
\boxed{\sum_S z_S^2=Nr.}
\tag{3.1}
\]
The block entropy is therefore
\[
H_A
=\sum_S q_S\log_2\frac1{q_S}
=\frac{18r}{N}-\frac2{N^2}\sum_{S:z_S\ne0}z_S^2\log_2|z_S|.
\tag{3.2}
\]

For influence, let `g(x)=epsilon_x 1_A(x)` on the nine-core cube. The standard gradient Parseval identity gives
\[
\sum_S |S|q_S
=\frac1{2N}\sum_{\{x,x'\}\in E(Q_9)}(g(x)-g(x'))^2.
\tag{3.3}
\]
Let `e(A)` be the number of cube edges induced by `A`, and let `e_opp(A)` count the induced edges whose endpoint signs are opposite. Since `g` is zero off `A`,
\[
\sum_S |S|q_S
=\frac{9r-2e(A)+4e_{\rm opp}(A)}{2N}.
\tag{3.4}
\]
Adding the host degree gives
\[
I_A
=\frac{dr}{N}
+\frac{9r-2e(A)+4e_{\rm opp}(A)}{2N}.
\tag{3.5}
\]
The consumed account03 edge-rigidity theorem says the graph induced by `T` is precisely the nine-edge matching (1.2), hence
\[
e(A)\le\lfloor r/2\rfloor.
\tag{3.6}
\]
Consequently
\[
I_A\ge
\begin{cases}
5r/N,&r\text{ even},\\
(10r+1)/(2N),&r\text{ odd}.
\end{cases}
\tag{3.7}
\]
This lower bound already retains arbitrary orientation: opposite signs can only increase the core Dirichlet term in (3.4).

## 4. New theorem: every host block pays at least the source-pair stable defect per row

Define
\[
q_*:=\frac{5C_*-16}{N}
=0.032439953125.
\tag{4.1}
\]

### Theorem 4.1
For every nonempty signed block `A` in (2.1),
\[
\boxed{C_*I_A-H_A\ge |A|q_*.}
\tag{4.2}
\]
If `|A|` is odd, the inequality is strict with a uniform positive excess.

### Proof: even blocks
If `r` is even, every integer `z_S` is even. Thus every nonzero `|z_S|>=2`, so
\[
\sum_{z_S\ne0}z_S^2\log_2|z_S|
\ge\sum_S z_S^2=Nr.
\]
Equation (3.2) gives
\[
H_A\le\frac{16r}{N}.
\tag{4.3}
\]
Combining (4.3) with the even case of (3.7),
\[
C_*I_A-H_A
\ge\frac{(5C_*-16)r}{N}=rq_*.
\]

### Proof: odd blocks
If `r` is odd, every `z_S` is an odd nonzero integer. Put
\[
c_0:=\frac{9\log_2 3}{8}>1.
\]
For every odd integer `z`,
\[
z^2\log_2|z|\ge c_0(z^2-1).
\tag{4.4}
\]
For `|z|=1` this is equality. For real `x>=3`, the ratio
\[
\frac{x^2\log x}{x^2-1}
\]
is increasing because its derivative has the sign of `x^2-1-2\log x>0`; hence the smallest nontrivial value occurs at `x=3`, giving (4.4).

Since there are `N` Walsh characters, (3.1) yields
\[
\sum_S(z_S^2-1)=N(r-1).
\]
Therefore
\[
H_A\le\frac{18r-2c_0(r-1)}{N}.
\tag{4.5}
\]
Using the odd case of (3.7) and subtracting `rq_*`,
\[
C_*I_A-H_A-rq_*
\ge
\frac{C_*/2+2(c_0-1)r-2c_0}{N}.
\tag{4.6}
\]
Because `c_0>1`, the right side is increasing in `r`; at `r=1` it equals
\[
\frac{C_*/2-2}{N}
=0.0024627453125>0.
\]
This proves the odd case and the theorem. `square`

The proof is fully symbolic. No enumeration, floating search, positive-part estimate, or assumption of pairwise grouping is used.

## 5. Corollary: arbitrary fixed-T signed character recoding cannot break the stable candidate

The eighteen exceptional rows partition among the nonzero host-character blocks, so summing (4.2) gives
\[
\sum_{u\ne0}(C_*I_{A_u}-H_{A_u})
\ge18q_*.
\tag{5.1}
\]
In the published source encoding, each of the nine source edges is one same-orientation degree-one host block. For such a pair, exactly 256 Walsh sums have magnitude two and the others vanish, so
\[
H_{\rm pair}=\frac1{16},
\qquad
I_{\rm pair}=\frac5{256},
\]
and hence the source host bank attains equality in (5.1): its contribution is exactly `18 q_*`.

Because the empty-host Fourier block is common to every recoding,
\[
\boxed{
\Delta_*(F_{\lambda,\epsilon})
:=C_*[I(F_{\lambda,\epsilon})-1]-H(F_{\lambda,\epsilon})
\ge
\Delta_*(F_{\rm source}).
}
\tag{5.2}
\]
Using the peer-certified source values (1.3),
\[
\Delta_*(F_{\rm source})
\ge
6.5218512\cdot\frac{133}{128}
-6.776605309005978082519790221891882314787235039
\]
\[
\boxed{
\Delta_*(F_{\rm source})
>5.703494021917480209778108117685212764961\times10^{-6}>0.
}
\tag{5.3}
\]
Therefore every gate of the form (2.1) obeys the stable balanced gate inequality
\[
\boxed{H(F_{\lambda,\epsilon})<C_*[I(F_{\lambda,\epsilon})-1].}
\tag{5.4}
\]

This removes not only the 34,459,425 pair rewirings covered by the peer theorem but **all 682,076,806,159 unsigned set partitions of the same eighteen rows**, all row-sign choices, and all choices of nonzero host characters of arbitrary positive degree. The conclusion is analytic and does not rely on that finite count.

## 6. What changed and exact remaining gap

Before this run, fixed exceptional support `T` was known safe only under re-pairing into nine two-cell host channels; the peer report explicitly left changed host group sizes as an adversarial degree of freedom. After Theorem 4.1, every source-valid recoding that keeps the same empty core and assigns each exceptional row to an arbitrary nonzero host character is no worse, in the exact `C_*I-H` currency, than the published source encoding. Arbitrary orientation is included rather than discarded.

This is **not** `LIMIT-PRIME-GATE-LIFT-v1`. The theorem is confined to the uniform balanced slice and the fixed exceptional support/empty core. The exact universal gap remains
\[
D_{\Gamma_*}(P;p)\ge0
\quad\text{for every composition-prime Boolean gate }P
\text{ and every interior product bias }p.
\]
Within this source family, the legitimate next adversarial freedoms are now **changed exceptional support / changed empty core / biased product inputs**, not another host regrouping, re-pairing, orientation, or host-character degree choice.

The result is also compatible with the previous B16 heterogeneous threat corridor: the published source already has absolute stable defect `>5.70e-6`, more than an order of magnitude above the `3.84603e-7` fixed-core threat ceiling. The present theorem strengthens that statement by showing the whole fixed-support character-recoding closure cannot reduce the defect at all.

## 7. Verification scope

The adjacent checker verifies the exact induced-edge matching on `T`, the algebraic constants in the odd/even proof, and—only as a redundant sanity test—enumerates all `2^18-1=262,143` **unsigned single-block subsets** and confirms the minimum per-row stable defect is attained by the nine source pairs. That enumeration is not used in the proof of Theorem 4.1 and does not cover or need to cover the signed theorem.

Scoped privacy review: this report contains only FEI mathematics, source-bound repository-relative provenance, hashes, and sanitized run metadata. It contains no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, unrelated private material, email/Drive content, paid compute instructions, remote workflow instructions, notification changes, or permission changes. No novelty or publication-priority claim is made.
