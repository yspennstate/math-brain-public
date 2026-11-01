Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE-LEVEL MOVEMENT since the previous P13 report is companion-derived: P02 tightened the exact repository-internal upper endpoint from `U_F` to `U_W<U_F`, while the rigorous lower endpoint `L=0.792665992` is unchanged. P13 MECHANISM MOVEMENT: for the true correlated width-6 strip (`m=12`), the proved finite-to-infinite additive constant improves from `44739246/7 = 6391320.857...` to the exact overlap-renewal value `365464514289599436188349306847299150185967435856 / 142953501131693084676406151816850886136787 = 2556527.202... < 2556528`.**

# P13 / T02 — all one-defect synchronizers and overlap-gap transfer

## 1. Scope, source and continuity

This run follows `operations/PROGRESS20_2026-09-20.md` and the current LIVE20 assignment of P13 to T02, the binary Chvatal--Sankoff constant

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The raw source letters remain the primitive randomness. In particular, the same incoming `Y` bit is used against every active `X` bit in a strip column; no independent Bernoulli matching array is substituted.

Fresh source navigation on 2026-09-20 recovered Alexander Tiskin, `arXiv:2212.01582v2` (the corrected version; earlier stochastic-process/`gamma` claims were removed), whose current source still describes the exact coefficient as unresolved. The rigorous public lower endpoint retained here is

\[
L=0.792665992=\frac{99083249}{125000000}
\]

from Heineman--Miller--Reichman--Salls--Sarkozy--Soiffer, `arXiv:2407.10925`.

Necessary repository dependencies only:

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`;
- previous P13 report `proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T04-17-26Z__width2-complete-reset-language-transfer.md`, blob `c75f518881bea4c4ccda98802c3abd2d99055d6c`;
- latest P02 companion report `proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T05-13-00Z__coefficient-weighted-two-step-report.md`, blob `7a7d068e4f35766ec13e09d8d72650c6ed7047c4`;
- R17's exact lower-side obstruction, already recovered in the preceding P13 run: widths `w<=5` cannot beat the retained lower endpoint.

Short pre-LIVE20 handoff, preserved and not reopened: P0342 had already been terminally handed off at frozen source metric `2/2`; the later P0205 screen admitted no successor because the source's `tau(infinity)` notation was not source-faithfully frozen. The retired I0051/clade work remains retired.

## 2. Source-level before/after, separate from the P13 mechanism

The previous P13 report inherited P02's Farey--Collatz endpoint

\[
U_F=\frac{\log(4t^2)}{\log\lambda_F}.
\]

Since then P02 proved a coefficient-weighted two-step defect using the minimum positive primitive transition weight of the actual C045 covering operator. Its exact theorem gives a rate `lambda_W<lambda_F`, hence

\[
\boxed{L\le\gamma_2\le U_W<U_F},
\qquad
U_W:=\frac{\log(4t^2)}{\log\lambda_W}.
\]

P02's exact positive-series enclosure proves the strict separator

\[
U_W<
0.826275942762282625015106581537296632823461996193190023880806183312562944430299564492
<U_F.
\]

Diagnostic high precision in the companion report places the endpoint decrease at about `7.10394e-84`. This source-level shrink belongs to P02's complementary variational/covering route. The P13 theorem below strengthens the lower-side finite-to-infinite mechanism but does **not** itself raise `L` in this run.

## 3. Exact dependence-preserving strip recursion

Fix strip half-width `w` and put `m=2w`. A formal boundary state is

\[
S=(x_1,\ldots,x_m;g_1,\ldots,g_m)\in\{0,1\}^{2m}.
\]

For one fresh true source pair `(u,v)`, define

\[
d_0=0,
\qquad
d_i=(1-g_i)\bigl(d_{i-1}\vee\mathbf 1_{\{x_i=v\}}\bigr),
\quad 1\le i\le m.
\tag{3.1}
\]

The next boundary is

\[
x'=(x_2,\ldots,x_m,u),
\tag{3.2}
\]

\[
g'_i=g_{i+1}+d_{i+1}-d_i,\quad 1\le i<m,
\tag{3.3}
\]

\[
g'_m=(1-d_m)\mathbf 1_{\{u=v\}}.
\tag{3.4}
\]

Write the four equiprobable actual source-pair letters as

\[
A=(0,1),\quad B=(1,0),\quad C=(0,0),\quad D=(1,1).
\]

The key dependence point is visible in (3.1): the same bit `v` appears in every comparison in a column.

## 4. New analytic theorem: every one-defect `A` word synchronizes

The preceding P13 run proved only one particular placement of a one-defect reset analytically. This run closes all placements.

### Lemma 4.1 — `A` extends a zero tail

If a state has

\[
x_{m-k+1}=\cdots=x_m=0,
\qquad
g_{m-k+1}=\cdots=g_m=0,
\]

then one `A=(0,1)` step produces a state with a zero tail of length `k+1` (up to the obvious cap `m`). In particular `A^m` maps every formal state to `(0^m;0^m)`.

**Proof.** Under `A`, the new terminal pair is `x'_m=0`, `g'_m=0` because `u!=v`. On an old zero-tail coordinate, `x_i=0!=v=1` and `g_i=0`, so (3.1) gives `d_i=d_{i-1}`. Hence on every output coordinate whose two adjacent carries lie inside that tail,

\[
g'_i=0+d_{i+1}-d_i=0.
\]

The shift (3.2) moves the old zero tail one position left and appends another zero. QED.

### Lemma 4.2 — localized marker transport under `A`

Consider two states `S^0,S^1` that agree everywhere except at one position `j`, with

\[
(x_j^0,g_j^0)=(0,0),
\qquad
(x_j^1,g_j^1)=(1,b),\quad b\in\{0,1\},
\]

and suppose all coordinates strictly to the right of `j` are `(x_i,g_i)=(0,0)` in both states. Drive both states by the same `A` step. If `j>1`, the two outputs again agree everywhere except at `j-1`, where

\[
(x_{j-1}^{0\prime},g_{j-1}^{0\prime})=(0,0),
\qquad
(x_{j-1}^{1\prime},g_{j-1}^{1\prime})=(1,1-c),
\]

with `c` the common carry entering position `j`, namely `c=d_{j-1}`. All coordinates to the right of `j-1` are again zero in both outputs.

**Proof.** Before position `j` the two carry recursions are identical, so their incoming carry there is the common value `c`. In the zero reference state at `j`, (3.1) gives `d_j^0=c`. In the marked state, `x_j^1=1=v`, so

\[
d_j^1=(1-b)(c\vee1)=1-b.
\]

Therefore (3.3) at output position `j-1` gives

\[
g_{j-1}^{0\prime}=0+c-c=0,
\]

\[
g_{j-1}^{1\prime}=b+(1-b)-c=1-c.
\]

The `x` marker shifts from `j` to `j-1`. To the right, both chains see only zero `x,g`; each carry is constant through that zero tail, so all carry differences cancel in `d_{i+1}-d_i`, leaving zero output gradients there. QED.

### Theorem 4.3 — complete one-defect family

For every `m>=1`, every `0<=r<=m`, and every `Z in {A,B,C,D}`, the word

\[
\boxed{A^rZA^{m-r}}
\tag{4.1}
\]

is synchronizing on **all formal states**. Its exact constant output is:

- `Z=A` or `Z=C`: `(0^m;0^m)`;
- `r=0`: `(0^m;0^m)` for every `Z`;
- `Z=B`, `1<=r<m`: `(e_r;e_r)`;
- `Z=B`, `r=m`: `(e_m;0^m)`;
- `Z=D`, `1<=r<=m`: `(e_r;e_r)`.

By bit-complement symmetry, every word `B^r Z B^{m-r}` is also synchronizing.

**Proof.**

`Z=A` is immediate from Lemma 4.1. For `Z=C=(0,0)`, after the first `r` copies of `A` there is a zero tail of length `r`. If `r=0`, the following `A^m` already resets everything. If `r>=1`, the `C` column has `v=0`, so at the first zero-tail coordinate the match indicator is one and (3.1) forces the carry to one; it remains one across the rest of that zero tail. Thus the `C` step preserves a zero tail of length `r`, including `g'_m=0` because `d_m=1`. The remaining `m-r` copies of `A` extend that zero tail to length `m` by Lemma 4.1. Hence every `A^rCA^{m-r}` maps to zero.

Now take `Z=B=(1,0)` with `1<=r<m`. Compare the `B` column with the `C` column after the same prefix `A^r`. They have the same `v=0`, hence exactly the same carry vector `d`. Because the input has a nonempty zero tail, that carry reaches `d_m=1`, so both terminal gradients are zero. The two post-defect states therefore agree everywhere except at `x_m`, which is `1` for `B` and `0` for `C`. Apply Lemma 4.2 for the first `m-r-1` subsequent `A` steps. The discrepancy remains one localized marker. Immediately before the final `A` step, the reference `C` trajectory has already processed exactly `m` source letters, all with `u=0`, so its entire `x` vector is zero; the marked trajectory differs only by the marker at position `r+1`. Consequently the common carry through positions `1,...,r` in that final `A` column is zero, starting from `d_0=0`, regardless of the `g` values there. Lemma 4.2 then gives marker gradient `1` at output position `r`. The reference `C` trajectory is zero by the preceding paragraph, hence the `B` output is `(e_r;e_r)`. If `r=m`, `A^m` first resets to zero and the final `B` gives `(e_m;0^m)`. The case `r=0` again ends with `A^m` and is zero.

For `Z=D=(1,1)`, compare instead with the all-`A` reference at the defect column. `A` and `D` have the same `v=1`, hence the same carry vector; their post-defect states differ only at terminal `x_m` and possibly terminal `g_m`, so they are exactly in the localized-marker configuration of Lemma 4.2. The same marker-transport argument applies. Before the last `A` step, the all-`A` reference has processed `m` source letters with `u=0`, hence has zero `x` to the left of the marker and therefore zero incoming carry. The final marker gradient is one. For `r=m`, the prefix `A^m` is already zero and a direct `D` step gives `(e_m;e_m)`; for `r=0`, the trailing `A^m` resets. This proves all cases. Bit complement exchanges `A<->B` and `C<->D`, proving the symmetric family. QED.

A useful reformulation is that **any length-`m+1` source window containing at least `m` copies of `A` is synchronizing**, and the same is true with `A` replaced by `B`.

## 5. Renewal structure from true source letters

The previous reset-time bounds treated only a sparse special reset language. Theorem 4.3 allows a much denser renewal analysis without breaking source dependence.

Focus only on `A`; using `B` as well can only make actual synchronization earlier. Let

\[
p=\Pr(A)=\frac14,
\qquad q=1-p=\frac34.
\]

Let `G_1,G_2,...` be the numbers of consecutive `A` letters before successive non-`A` source letters: `G_1` is the initial `A` run, and thereafter `G_{i+1}` is the `A` run between the `i`th and `(i+1)`st non-`A` letters. These are iid with

\[
\Pr(G_i=k)=q p^k,\qquad k\ge0.
\tag{5.1}
\]

If

\[
G_i+G_{i+1}\ge m,
\tag{5.2}
\]

then around the intervening non-`A` source letter `Z_i` there is a contiguous subword `A^r Z_i A^{m-r}` for some `0<=r<=m`. By Theorem 4.3 that subword synchronizes the full strip state.

### A simple analytic bound

Pair the gaps disjointly as `(G_1,G_2),(G_3,G_4),...`. A pair succeeds when its sum is at least `m`. Since

\[
\Pr(G_1+G_2=t)=(t+1)q^2p^t,
\]

its success probability is exactly

\[
s_m
=\Pr(G_1+G_2\ge m)
=p^m\bigl(q(m+1)+p\bigr)
=\frac{3m+4}{4^{m+1}}.
\tag{5.3}
\]

Each two-gap trial consumes on average `2/q=8/3` source letters through the second bounding non-`A`. Therefore the expected delayed synchronization time obeys

\[
\boxed{
\mathbf E\tau_m
\le \frac{8/3}{s_m}
=\frac{32\,4^m}{3(3m+4)}.
}
\tag{5.4}
\]

This already exhibits the new `4^m/m` scale, rather than the previous constant multiple of `4^m`.

## 6. Stronger overlap recurrence and exact width-6 constant

Disjoint pairing still throws away half the possible middle defects. The overlaps can be retained exactly.

Suppose a non-`A` letter has just been seen and the `A` run immediately before it had length `a<m`. Let `E_a` be the expected additional number of source letters until a delayed stopping time at which a synchronizing one-defect word has certainly already occurred. Draw the next gap `G=b`. We always spend `b+1` letters to the next non-`A`. If `a+b>=m`, synchronization occurred inside that right `A` run and we stop at the next non-`A`; if `a+b<m`, we continue from state `b`. Hence

\[
\boxed{
E_a=\frac1q+q\sum_{b=0}^{m-a-1}p^bE_b,
\qquad 0\le a<m.
}
\tag{6.1}
\]

The same formula with `a=0` is also the initial expectation before the first non-`A`: if the initial run already has length at least `m`, the pure word `A^m` synchronizes; otherwise the process arrives at the first non-`A` in state `G_1`. Thus the desired delayed-reset expectation is exactly `E_0` for the finite system (6.1).

The system is a finite absorbing first-step system with a unique finite nonnegative solution. The checker solves it over `fractions.Fraction` and substitutes the solution back into every equation exactly.

For the first currently relevant width not excluded by the inherited `w<=5` lower-side obstruction, namely `w=6`, `m=12`, it gives

\[
\boxed{
E_0^{(12)}=
\frac{365464514289599436188349306847299150185967435856}
{142953501131693084676406151816850886136787}
=2556527.2021768987\ldots<2556528.
}
\tag{6.2}
\]

The previous analytic one-defect constant was

\[
C_{12}^{\dagger}
=\frac{8\,4^{12}+10}{21}
=\frac{44739246}{7}
=6391320.857142857\ldots.
\tag{6.3}
\]

Therefore the width-6 additive transfer constant decreases by

\[
\boxed{
C_{12}^{\dagger}-E_0^{(12)}
=
\frac{3837380253664899258518120074116344688889931191610}
{1000674507921851592734843062717956202957509}
=3834793.6549\ldots
}
\tag{6.4}
\]

and the new/old ratio is about

\[
0.3999998215266813.
\]

The same exact recurrence is already better than the old general analytic constant at `m=6,8,10,12`; at `m=4` the previous width-two complete reset-language constant `<23` remains much stronger and is retained rather than overwritten.

## 7. Finite-to-infinite theorem

Let `tau` be the actual first ending time of any synchronizing source word furnished by Theorem 4.3. The delayed stopping construction above satisfies `tau<=sigma` and `E sigma=E_0^{(m)}`. Couple a strip chain started from any formal state `s` with a stationary copy by using the **same actual iid source-pair stream**. By time `tau` the two chains are identical forever. Since each one-step strip reward lies in `{0,1}`, their cumulative rewards differ by at most one per pre-coalescence step. Therefore

\[
\boxed{
|\mathbf E_sR_N-N\gamma_w|
\le \mathbf E\min(N,\tau)
\le E_0^{(m)},
\qquad m=2w.
}
\tag{7.1}
\]

Since the width-`w` strip restricts admissible LCS paths in the full grid,

\[
\gamma_w\le\gamma_2.
\]

Thus

\[
\boxed{
\gamma_2\ge\gamma_w
\ge \frac{\mathbf E_sR_N}{N}-\frac{E_0^{(2w)}}N.
}
\tag{7.2}
\]

In particular at `w=6`,

\[
\boxed{
\gamma_2\ge\gamma_6
\ge \frac{\mathbf E_sR_N}{N}-\frac{2556528}{N}.
}
\tag{7.3}
\]

This is a proved asymptotic transfer. A future exact finite-horizon computation may therefore use (7.3) as a legitimate lower certificate. No finite computation without such a transfer is being promoted to a statement about `gamma_2`.

## 8. Essential executed self-check

The exact checker independently does two things:

1. exhaustively verifies the full one-defect `A` and `B` families on **all formal states** through `m=6` (216 family words total); this is a self-check of the analytic proof, not its basis;
2. solves (6.1) over exact rationals for even `m=2,4,...,12` and verifies every first-step residual exactly.

For `m=12` it prints `OVERLAP_LT_OLD=True`, the exact fraction (6.2), and `WIDTH6_CERTIFIED_ERROR_LT_2556528=True`, ending `ALL_EXACT_CHECKS_PASS`.

Checker:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T05-16-37Z__one_defect_overlap_gap_checker.py`

creation commit `d6bf9cad97bcce0cc97e1c41cc35e9b2d411b15e`.

Executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T05-16-37Z__one_defect_overlap_gap_checker.out`

creation commit `7078837f123ca03c3956908be35e4f3f9391dbab`.

## 9. Honest obstruction and failed route accounting

This run makes a real mechanism gain but does **not** improve the source lower endpoint. The inherited exact Bellman obstruction says `gamma_w<L` for every `w<=5`, so the fact that the new recurrence is already stronger at `w=3,4,5` cannot move `L`. At `w=6`, the new transfer constant is much smaller than before but is still about `2.56e6`; a useful finite-horizon certificate must therefore control `E_sR_N/N` at a horizon large enough that this additive error does not erase the lower-side margin.

The preceding width-two complete synchronizing-language enumeration is not abandoned, but it is not a scalable general-width proof: complete enumeration of short reset words grows too quickly and, even at zero transfer error, widths through five are quantitatively below `L`. The present run therefore executed the genuinely different symbolic/renewal route promised in the previous report: prove a width-uniform reset language first, then exploit its overlap structure analytically.

No claim is made that the overlap recurrence is optimal. It uses only `A`-rich reset windows even though the symmetric `B` family is also available. Treating both colors jointly should decrease the coupling constant further, but the two renewal processes are dependent and I did not insert an unjustified factor of two.

## 10. Next attack

The next P13 attack should use the new exact reset structure at `w=6` rather than return to full short-word enumeration. The preferred route is a regenerative lower certificate for the boundary-event identity

\[
\gamma_w=\frac23+\frac13\pi_w(B_w),
\]

conditioning on the exact canonical state produced by a one-defect synchronizer. The goal is to bound the reward/event contribution over a regeneration cycle and combine it with the exact overlap-gap tail, so the computation tracks only post-reset evolution plus a rigorous remainder rather than the entire stationary state space. The concrete source-level threshold remains `pi_w(B_w)>0.377997976` for beating `L`.

A secondary route, if that cycle calculation remains too large, is to build the **two-color** (`A` and `B`) overlap automaton and solve its exact first-hit equations. That would improve the finite-to-infinite error without changing the strip state space, and it is now justified by Theorem 4.3.

## 11. ledger_delta

```yaml
ledger_delta:
  slot: P13
  target: T02-binary-LCS
  source_model: independent_iid_uniform_binary_strings
  independent_bernoulli_matching_substituted: false
  source_status: PARTIAL
  source_lower_before: 0.792665992
  source_lower_after: 0.792665992
  source_upper_before: U_F
  source_upper_after: U_W
  source_upper_movement_owner: P02
  source_strict_movement: true
  p13_new_theorem: all_words_A^r_Z_A^(m-r)_and_bit_complements_synchronize
  p13_old_width6_error: 44739246/7
  p13_new_width6_error_exact: 365464514289599436188349306847299150185967435856/142953501131693084676406151816850886136787
  p13_new_width6_error_integer_bound: 2556528
  p13_width6_error_ratio_new_over_old_approx: 0.3999998215266813
  finite_to_infinite_transfer_proved: true
  new_source_lower_bound_from_p13_this_run: false
  prior_width2_best_constant_retained: true
  next_attack: width6_regenerative_boundary_event_lower_certificate_then_two_color_overlap_if_needed
  previous_p13_successor_handoff: P0342_terminal_handoff_then_P0205_not_admitted
  retired_clade_reopened: false
  checker_commit: d6bf9cad97bcce0cc97e1c41cc35e9b2d411b15e
  output_commit: 7078837f123ca03c3956908be35e4f3f9391dbab
```
