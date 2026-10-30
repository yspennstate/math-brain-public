# fleet03/B18 — source-exact refutation of AND/decomposable margin extremality

**Run:** `20260922T100641Z-fleet03-B18-auto11b`  
**Classification:** `CANDIDATE_REFUTED / ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Fresh-control reconciliation

A fresh owner-control reread during this invocation retains B12--B18 on FEI but explicitly says all FEI workers must converge on the all-gate potential target and either prove or falsify the proposed AND/decomposable extremality. An earlier same-invocation auxiliary attack on a low-level I-projection mechanism is therefore preserved as a false-start artifact but is **not** the active handoff from this run.

The immutable target for this report is

`FEI-ALL-GATE-MARGIN-v1`:

for the committed read-once potential `Gamma_0`, define

\[
D_{\Gamma_0}(G;p)
=\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
   [\Gamma_0(p_i)+h_2(V_{p_i})]
 -\Gamma_0(p_{out})-\widetilde H_G(p),
\]

\[
M(G;p)={I(G;p)\over4}-p_{out}(1-p_{out})\ge0,
\]

and, when `M>0`, report the owner's required scalar margin

\[
\boxed{c_G(p)=-{D_{\Gamma_0}(G;p)\over M(G;p)}.}
\tag{0.1}
\]

Adding `c p(1-p)` to `Gamma_0` changes gate slack by exactly `cM`, so `c_G` is the coefficient the gate actually asks for.

The exact claim attacked is

`AND-DECOMPOSABLE-EXTREMALITY-v1`:

> the worst required scalar margin is attained by the binary AND/read-once decomposable class, so larger genuinely prime gates do not ask for more.

This claim is **REFUTED** below by an actual composition-prime Boolean gate at an interior product bias.

## 1. Named completed cross-account theorem consumed substantively

The completed other-account artifact used here is fleet02/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`.

It proves, for a disjoint gate composition

\[
K=F(G_1,\ldots,G_m),
\]

with induced inner output biases and nonnegative physical weights

\[
b_j={\operatorname{It}_j(F)\over V_{q_j}},
\]

the exact cocycles

\[
D_{\Gamma}(K)=D_{\Gamma}(F)+\sum_j b_jD_{\Gamma}(G_j),
\tag{1.1}
\]

\[
M(K)=M(F)+\sum_j b_jM(G_j).
\tag{1.2}
\]

Consequently, wherever the denominators are positive,

\[
\boxed{
c_K
={M(F)c_F+\sum_j b_jM(G_j)c_{G_j}
 \over M(F)+\sum_j b_jM(G_j)}
\le \max\{c_F,c_{G_1},\ldots,c_{G_m}\}.}
\tag{1.3}
\]

The zero-denominator cases are handled without division by the corrected slack `D+cM`, which obeys the same cocycle. Repeated factorization therefore terminates at composition-prime gates and **decomposable composition cannot manufacture a margin larger than its factors**.

This theorem is applied below, not merely cited: it converts a single source-exact prime obstruction into a structural refutation of the idea that accumulation of mild AND/read-once pieces explains the worst gate margin.

## 2. The same base potential has a certified AND/read-once margin at most 0.01

The proved read-once certificate uses exactly the same committed numerical base `Gamma_0` (`cert_vi_h96k40`) and the candidate

\[
\widehat\Gamma(p)=\Gamma_0(p)+0.01\,p(1-p).
\tag{2.1}
\]

Its full interval certificate over the binary AND/OR inequality succeeds with positive enclosure margins in every region and yields the published read-once theorem

\[
H(f)\le6.4573\,I(f).
\]

Therefore, relative to `Gamma_0`, every binary AND/OR constraint satisfies

\[
\boxed{c_{AND/OR}\le0.01.}
\tag{2.2}
\]

By the cocycle (1.1)--(1.3), every disjoint read-once composition made only from these binary gates also has required scalar margin at most `0.01`.

This uses the rigorous certificate bound, not the non-rigorous grid estimates near `0.0044`.

## 3. Strong source-exact composition-prime Numaro witness

The source-bound 18-input Numaro gate has already been certified composition-prime. The completed fleet03/B17 source reconstruction evaluates it at

\[
p_1={223\over456},\qquad p_2=\cdots=p_{18}={1\over2},
\qquad p_{out}={1019\over2048}.
\tag{3.1}
\]

For

\[
\Gamma^\dagger(p)=\Gamma_0(p)+a_0p(1-p),
\qquad a_0=0.268204856,
\tag{3.2}
\]

the source-exact biased Walsh calculation gives the certified bracket

\[
-0.038023735
< D_{\Gamma^\dagger}(G;p)
< -0.038023734.
\tag{3.3}
\]

The same calculation gives the exact Poincare-margin currency

\[
\boxed{
M(G;p)={62098577\over239075328}
=0.2597448156591047\ldots .}
\tag{3.4}
\]

Because

\[
D_{\Gamma^\dagger}=D_{\Gamma_0}+a_0M,
\]

the owner's normalized margin (0.1) is

\[
c_G=a_0-{D_{\Gamma^\dagger}\over M}.
\tag{3.5}
\]

Using only the weaker endpoint in the certified bracket (3.3),

\[
\boxed{
 c_G
>0.268204856+{0.038023734\over62098577/239075328}
={3218209572490583\over7762322125000000}
>0.4145936641982.
}
\tag{3.6}
\]

The tighter source computation gives `c_G=0.4145936656...`; (3.6) is the rigorous comparison needed here.

Thus this genuine composition-prime gate asks for **more than 41.45 times** the entire rigorously certified binary-AND margin budget `0.01`.

## 4. Decisive falsification

Combining (2.2) and (3.6),

\[
\boxed{
\sup_{\text{binary AND/OR read-once}}c_G\le0.01
<0.4145936641982
<c_{\rm Numaro\ prime}.
}
\tag{4.1}
\]

Therefore the current proposed statement that the binary AND/read-once decomposable class is extremal for the owner's scalar gate margin is **false**.

Moreover, by the exact composition max principle (1.3), this cannot be explained by many mild decomposable constraints accumulating: any disjoint composite's normalized margin is a nonnegative weighted average of its factors' margins. The obstruction is genuinely prime somewhere, and here the actual 18-input truth table itself is independently certified composition-prime.

The quadratic-only center forced by this one source would be

\[
\Gamma_0(1/2)+{c_G\over4}
>6.4548+{0.4145936641982\over4}
=6.55844841604955\ldots .
\tag{4.2}
\]

Equation (4.2) is **not** a lower bound on the true FEI constant: a shaped universally safe repair can pay the biased source more efficiently than a pure quadratic lift. It is only the exact scalar-margin consequence of the owner's `c_G` normalization.

## 5. What remains after the falsification

This run settles the owner's falsification branch for `AND-DECOMPOSABLE-EXTREMALITY-v1`: the conjectured AND extremality is not compatible with the later source-exact prime evidence.

The surviving all-gate route is therefore the **prime-gate** problem. The cocycle theorem reduces any fixed corrected potential to composition-prime gates. A current source-valid shaped repair from fleet02/B17 has center `6.55844529582746` and repairs the strongest known Numaro witness while worsening no gate, but its universal prime-gate inequality is still unproved.

The smallest honest remaining implication is:

\[
\boxed{
D_{\Gamma^{shape}}(P;p)\ge0
\quad\text{for every finite composition-prime Boolean gate }P
\text{ and every interior product bias }p,
}
\tag{5.1}
\]

or else produce another actual prime falsifier and update the same candidate rather than returning to AND extremality.

Full unrestricted FEI remains **OPEN / NOT PROVED**.

## 6. Required ledger

- **common target version:** `FEI-ALL-GATE-MARGIN-v1`.
- **candidate attacked:** `AND-DECOMPOSABLE-EXTREMALITY-v1`.
- **old missing implication:** prove that no genuine higher-arity gate asks for more scalar margin than the binary AND/read-once class.
- **new proved inference / failed claim:** source-exact 18-input composition-prime Numaro has `c_G>0.4145936641982`, while the rigorous binary AND/read-once certificate pays all such constraints with `c=0.01`; hence AND/read-once extremality is REFUTED.
- **replacement obligation:** prove the all-bias inequality for a repaired potential on every composition-prime gate, or produce the next genuine prime falsifier.
- **consumed peer artifact:** fleet02/B17 `20260922T004442Z-gate-composition-cocycle/REPORT.md`.
- **applied to claim:** exact max principle showing decomposable composition cannot amplify normalized gate margin above its factors.
- **next recipients:** fleet02/B17 for prime adversarial search; fleet04/B18 for prime-potential/Bellman integration; fleet03/B15 for source-exact Gibbs/KL payment on the same repaired prime target.
- **implication to full FEI:** AND extremality cannot close FEI; the exact all-gate problem reduces to universal control of composition-prime gates for one finite-center potential.

## 7. Verification and scope

The adjacent checker uses exact rational arithmetic for (3.4), the coarse certified interval (3.3), and the read-once certified upper budget `0.01`. It verifies the strict margin separation in (4.1) and the pure-quadratic center consequence (4.2). The composition max principle is analytic and inherited from the named completed peer theorem.

No novelty claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive content, paid model/API/Codex call, remote workflow, or permission change is used.
