Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 / maximum was requested, but this runtime exposes no authenticated model/effort selector or applied-effort receipt, so I do not claim otherwise.

**SOURCE-LEVEL MOVEMENT.** For the true Chvátal–Sankoff problem of two independent iid uniform binary strings, the exact repository-internal upper endpoint moves strictly from the previous P02 coefficient-weighted value

\[
U_W=\frac{\log(4t^2)}{\log\lambda_W}
\]

to

\[
\boxed{U_S=\frac{\log(4t^2)}{\log\lambda_S}<U_W},
\qquad
L=0.792665992.
\]

Thus the tracked metric moves strictly from `U_W-L` to `U_S-L`. An exact rational logarithm enclosure proves

\[
\boxed{
U_S<
0.826275942762282625015106581537296632823461996193190023880806183312562944430299551
<U_W.
}
\]

Diagnostic high precision gives an upper-endpoint decrease of about \(1.3768381478670\times10^{-80}\). This is still PARTIAL, not a determination of \(\gamma_2\), but it is a genuine original-problem interval shrink rather than a finite-only statistic.

# P02 / T02 — a label-support gap in the C045 cone forces a stronger two-step spectral defect

## 1. Source, status, continuity, and the prior P02 handoff

The target is

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E\,LCS(X_1^n,Y_1^n)}{n}
\]

for two independent iid uniform binary strings. The underlying match indicators are dependent because the same source letters recur across an LCS grid row or column; no independent Bernoulli matching model is substituted.

Fresh source navigation on 2026-09-20 recovered Alexander Tiskin, `arXiv:2212.01582v2`, last revised 2024-08-13. The arXiv record still calls the coefficient unresolved and explicitly says that claims in the original preprint about the stochastic process and `gamma` turned out to be incorrect and were removed from v2, while retaining a supported estimate. Heineman–Miller–Reichman–Salls–Sarkozy–Soiffer, `arXiv:2407.10925`, prove the rigorous lower bound

\[
L=0.792665992=\frac{99083249}{125000000}.
\]

Li–Ren–Wen, published online 2026-03-02, still describe determination of the two-string binary constant as open and summarize the public rigorous range as roughly `0.792665 <= gamma <= 0.826280`. The stronger C045/P02 upper endpoints below are repository-internal exact certificates pending later independent review and public-priority checking.

Controlling policy recovered: `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`.

Newest own substantive dependency recovered:

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T05-13-00Z__coefficient-weighted-two-step-report.md`, blob `7a7d068e4f35766ec13e09d8d72650c6ed7047c4`.

Newest companion report recovered:

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T05-17-52Z__all-one-defect-sync-overlap-gap-transfer.md`, blob `8b0c3e6c29e361a36e7c97455fb6dd4f1f7bec96`.

P13 remains on the true-source correlated boundary-carry/reset route. Its latest run improves a width-6 finite-to-infinite error constant but does not raise the retained source lower endpoint. P02 therefore remains nonduplicating on the covering/cone stationary-variational side.

Essential historical finite-operator dependency remains R17 C045:

`runs/R17/20260918_0926Z_fullcap6_c045_f7a1.md`,

with its exact all-row cone output

`artifacts/R17/20260918_0926Z_fullcap6_c045_f7a1_exact_cone_checker.out`, blob `0a00ececfdfe58ec85f5a7e6c29bf2559fd58539`.

The previous P02 target, Aldous–Fill Open Problem 2.34 on occupation-time portmanteau identities, was closure-packaged on 2026-09-17 at frozen `11/11`; publication novelty there remained explicitly unverified. It is preserved only as a handoff and is not reopened. Root `POSTED.md` contains no posting exclusion for T02.

## 2. Prior T02 attempts and the precise new opening

The relevant supported lineage is:

1. R17 C033–C035 were withdrawn after the complement-gauge bug; C036 repaired the cocycle transport.
2. R17 C045 completed the local-deficiency language through six factors on the gauge-correct `h=8` covering machine, producing an 11,614,187-state reachable product and an exact positive integer cone witness.
3. Earlier P02 runs converted that inherited witness into successively stronger strict bounds: algebraic-integrality separation, primitive-content normalization, two-step rational Collatz, bounded-denominator Farey, and then the coefficient-weighted two-step theorem.
4. The immediately preceding P02 theorem used only the smallest positive primitive transition coefficient `m0`. It proved that a tight cone row has at least one non-tight successor and therefore incurs two-step defect at least `m0` times its witness coordinate.

The unused structure is stronger: a tight row cannot choose an arbitrary single small edge into the non-tight set. Its thirty labelled transitions have a fixed finite coefficient multiset, and exact one-step equality imposes simultaneous interval and divisibility constraints on the total coefficient support leading to non-tight successors. This run exploits that support arithmetic.

## 3. Exact primitive operator and label multiset

At

\[
t=\frac{256717}{800000}=\frac pq,
\]

write the retained C045 operator as

\[
A=t^2H,\qquad B=SH,
\]

where

\[
S=q^6(q-p)=142418378752000000000000000000000000000000.
\]

The thirty canonical labels have eight distinct positive primitive coefficients. For `k=0,...,6`,

\[
c_k=q^{6-k}(q-p)p^k,
\]

and the two geometric-tail signs have coefficient

\[
c_7=p^7.
\]

Their multiplicities among the thirty labels are

\[
(m_0,m_1,\ldots,m_7)=(2,4,4,4,4,4,4,4).
\]

Numerically as exact integers,

\[
\begin{aligned}
c_0&=142418378752000000000000000000000000000000,\\
c_1&=45701523672596480000000000000000000000000,\\
c_2&=14665447565822438195200000000000000000000,\\
c_3&=4706087128444048582696448000000000000000,\\
c_4&=1510165711690963525005105051520000000000,\\
c_5&=484606513760211354060919441888824800000,\\
c_6&=155508412991225222725571320454216795227,\\
c_7&=73482242694633120311956186136958404773.
\end{aligned}
\]

Thus the old minimum-positive coefficient is

\[
m_{\min}=c_7=73482242694633120311956186136958404773.
\]

The inherited integer witness `V` satisfies

\[
1\le V_i\le M,
\qquad M=5000000000000000000,
\]

and

\[
BV\le \frac abV,
\]

where

\[
a=1995237757733917147310102692686664915858011319606812684127301,
\qquad
b=4220452010631561279,
\]

with

\[
\gcd(a,b)=1,\qquad b\le M<2b.
\]

## 4. New support-gap lemma for a tight row

Define the integer one-step slack

\[
s_i:=aV_i-b(BV)_i\ge0.
\]

If `s_i=0`, then `b | V_i`; since `b<=V_i<=M<2b`, necessarily

\[
V_i=b.
\tag{4.1}
\]

Likewise every tight successor `j` with `s_j=0` has `V_j=b`.

For a fixed tight row `i`, classify each of its thirty labels into three categories:

- rejected/absent from the product row;
- accepted and leading to a tight successor;
- accepted and leading to a non-tight successor.

Let `n_k` be the number of type-`k` labels in the third category and `t_k` the number in the second. Then

\[
0\le n_k+t_k\le m_k.
\]

Put

\[
W_N=\sum_k n_kc_k,
\qquad
W_T=\sum_k t_kc_k.
\]

Because a tight row has `(BV)_i=a`, and every tight successor has witness value `b`,

\[
\boxed{
a-bW_T=\sum_{\ell\in N_i} c_\ell V_{j(\ell)}.}
\tag{4.2}
\]

Consequently every possible pair of count vectors `(n,t)` must satisfy two necessary conditions:

\[
\boxed{W_N\le a-bW_T\le MW_N,}
\tag{4.3}
\]

and, if

\[
g(n)=\gcd\{c_k:n_k>0\},
\]

then

\[
\boxed{g(n)\mid a-bW_T.}
\tag{4.4}
\]

No assumption about distinct successors is used: if several labels lead to the same successor, (4.2) is still the same labelled sum, while (4.3) and (4.4) remain necessary.

Also `W_N>0`. Otherwise (4.2) would give `a=bW_T`, impossible because `gcd(a,b)=1` and `b>1`.

### Exact finite support gap

There are only

\[
3\cdot5^7=234375
\]

possible count vectors over the eight coefficient types. The exact checker enumerates every nonzero `n` with candidate weight below

\[
\boxed{
D:=c_0+c_7
=142491860994694633120311956186136958404773,
}
\tag{4.5}
\]

and, for each such `n`, every compatible tight count vector `t` whose `W_T` lies in the exact interval forced by (4.3). It rejects a candidate unless both (4.3) and (4.4) hold.

The executed exact search checks all **41,232** nonzero count vectors with `W_N<D`, scans `1,669,729,321` interval-compatible weight pairs before label-cap filtering and `49,925,505` compatible `(n,t)` pairs, and finds **none** satisfying the necessary conditions.

At `W_N=D`, the relaxed necessary test first has a survivor, so the finite certificate is not claiming more than it checked. Therefore every actual tight C045 row obeys

\[
\boxed{W_N\ge D.}
\tag{4.6}
\]

The scale gain over the previous theorem is exact:

\[
\boxed{1939\,m_{\min}<D<1940\,m_{\min}.}
\tag{4.7}
\]

This is the new finite structural fact.

## 5. New theorem: label-support two-step Collatz defect

The exact two-step identity from the previous P02 run is

\[
\boxed{
a^2V_i-b^2(B^2V)_i
=a s_i+b\sum_jB_{ij}s_j.}
\tag{5.1}
\]

### Case 1: `s_i>0`

Then `s_i>=1`, so

\[
a s_i+b\sum_jB_{ij}s_j\ge a.
\]

The endpoint checker verifies exactly that

\[
\boxed{a\ge DM.}
\tag{5.2}
\]

Since `V_i<=M`,

\[
a s_i+b\sum_jB_{ij}s_j\ge DV_i.
\tag{5.3}
\]

### Case 2: `s_i=0`

By (4.1), `V_i=b`. Every label leading to a non-tight successor `j` has `s_j>=1`; summing its primitive label coefficient over those labels gives precisely `W_N`. Hence

\[
\sum_jB_{ij}s_j\ge W_N\ge D.
\]

Therefore

\[
a s_i+b\sum_jB_{ij}s_j\ge bD=DV_i.
\tag{5.4}
\]

Combining both cases with (5.1) proves the new componentwise bound

\[
\boxed{
B^2V\le \frac{a^2-D}{b^2}V.
}
\tag{5.5}
\]

Thus

\[
\rho(B)\le\sqrt{\frac{a^2-D}{b^2}}.
\]

For an exact rational rate define

\[
\boxed{
\beta_S:=\frac ab-\frac{D}{2ab}.
}
\tag{5.6}
\]

Since

\[
\beta_S^2
=\frac{a^2-D}{b^2}+\frac{D^2}{4a^2b^2}
>\frac{a^2-D}{b^2},
\]

we have

\[
\boxed{\rho(B)<\beta_S.}
\tag{5.7}
\]

Rescaling back to the original C045 operator,

\[
\boxed{
\lambda_S:=\frac{t^2}{S}\beta_S,
\qquad
\rho(A)<\lambda_S.
}
\tag{5.8}
\]

The previous coefficient-weighted theorem used

\[
\beta_W=\frac ab-\frac{m_{\min}}{2ab}.
\]

Hence the exact improvement in the finite spectral correction is

\[
\boxed{
\frac{(a/b)-\beta_S}{(a/b)-\beta_W}
=\frac{D}{m_{\min}}
\in(1939,1940).
}
\tag{5.9}
\]

This is not a decimal/Farey polishing step: it uses the finite labelled support geometry of an actually tight C045 row.

## 6. Dependence-preserving transfer to the original binary LCS problem

The C027/C045 covering transfer is used with the original source-pair dependence intact.

For fixed positive fugacities `(x,y)`, the finite covering operator enumerates accepted collations of **actual ordered string pairs**. If its spectral radius is strictly below `z<1`, finite dimensionality gives a constant `K<infinity` such that the total accepted collation weight at order `m` is at most `K z^m`.

Every actual binary string pair of length `n` has probability exactly `4^{-n}`. Coefficient positivity and the covering property therefore give

\[
\Pr\{L_n\ge m\}\le K(4xy)^{-n}z^m.
\tag{6.1}
\]

No probability is ever assigned independently to the `n^2` match cells; the counted primitive objects are the two iid source strings themselves.

For any

\[
c>\frac{\log(4xy)}{\log z},
\]

substituting `m=floor(cn)` in (6.1) gives exponential decay. Summing the upper tail of `L_n`, dividing by `n`, and taking `n->infinity` yields

\[
\boxed{
\gamma_2\le\frac{\log(4xy)}{\log z}.
}
\tag{6.2}
\]

At the retained symmetric point `x=y=t`, (5.8) lets us take `z=lambda_S`, so

\[
\boxed{
\gamma_2\le U_S:=\frac{\log(4t^2)}{\log\lambda_S}.
}
\tag{6.3}
\]

Because `0<4t^2<1` and the map `z -> log(4t^2)/log z` is strictly increasing on `(0,1)`, `lambda_S<lambda_W` implies

\[
\boxed{U_S<U_W.}
\tag{6.4}
\]

This is the required source-level movement.

## 7. Exact endpoint separator and metric update

The endpoint checker uses the positive expansion

\[
-\log z
=2\sum_{k\ge0}\frac{u^{2k+1}}{2k+1},
\qquad
u=\frac{1-z}{1+z},
\]

with 160 exact rational terms and the rigorous remainder bound

\[
0<\mathrm{tail}\le
\frac{2u^{2K+1}}{(2K+1)(1-u^2)}.
\]

It proves

\[
U_S<Q<U_W
\]

for

\[
Q=
\frac{826275942762282625015106581537296632823461996193190023880806183312562944430299551}
{10^{81}}.
\]

Therefore the exact original-problem metric moves from

\[
W_{\rm before}=U_W-L
\]

to

\[
\boxed{W_{\rm after}=U_S-L<W_{\rm before}.}
\]

A simple decimal interval consequence is

\[
\boxed{
0.792665992\le\gamma_2
<0.826275942762282625015106581537296632823461996193190023880806183312562944430299551.
}
\]

The corresponding rational displayed width is less than

\[
0.033609950762282625015106581537296632823461996193190023880806183312562944430299551.
\]

The stronger exact endpoint is the logarithmic expression `U_S`, not the displayed rational `Q`.

## 8. Soundness, limits, and what remains open

This run does **not** determine `gamma_2`. It improves only the internally certified upper endpoint. The rigorous lower endpoint remains `0.792665992`.

The finite support enumeration is deliberately a relaxation: labels that share one matrix successor are allowed separate witness values when deriving the necessary conditions. That can only create extra candidate configurations, so excluding every relaxed configuration below `D` is safe for the true matrix row. The first relaxed survivor at `D` is not asserted to occur in the actual product graph.

No large C045 product or witness was regenerated. The new proof uses only already-certified one-step cone data plus the exact 30-label coefficient multiset and a new small finite support enumeration. This respects the progress-first instruction: the checker tests a new theorem rather than recreating the old 11.6-million-state certificate.

The public literature status is unchanged: the exact constant remains open. Tiskin v2 explicitly withdrew the incorrect earlier process/gamma claims; the 2024 lower-bound paper and the 2026 multiple-string paper still describe the two-string binary constant as unresolved. The C045/P02 upper endpoint therefore remains an internal candidate pending later independent mathematical review and priority checking.

The most promising next P02 attack is to tighten the relaxed support lemma itself: incorporate equality of witness values for labels that coalesce to one successor, or reconstruct only the short neighbourhood of a tight row to replace the necessary-condition threshold `D` by the true minimum non-tight support weight. That is a graph-specific continuation, not another generic arithmetic strictification.

## 9. Artifacts

Executed exact support enumeration:

- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T06-05-32Z__support_gap_checker.cpp`
- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T06-05-32Z__support_gap_checker.out`

The output ends

`ALL_BELOW_THRESHOLD_NECESSARY_CONFIGURATIONS_EXCLUDED=PASS`,
`EXACT_SUPPORT_GAP_CERTIFICATE_PASS`, and
`ALL_EXACT_CHECKS_PASS`.

Executed exact endpoint compiler:

- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T06-05-32Z__support_gap_endpoint_checker.py`
- `proofnet24/P02-progress-lcs/artifacts/2026-09-20T06-05-32Z__support_gap_endpoint_checker.out`

The output ends

`EXACT_SUPPORT_GAP_RATE_BEATS_WEIGHTED_RATE_PASS`,
`EXACT_TWO_STEP_SPECTRAL_MAJORANT_PASS`,
`EXACT_LOG_SEPARATOR_PASS`,
`SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS`, and
`ALL_EXACT_CHECKS_PASS`.

Artifact creation commits, respectively:

- support checker source: `0e32a60f424a24b8b1d17fcc290a42a7ea420062`;
- support checker output: `5388fd3796872a2e69580148d94290832ae2b05d`;
- endpoint checker source: `0ddf7f0fc3e6ab8131eca78f1b0a8aae57bde15a`;
- endpoint checker output: `dbda2a890691726f2598ddb3299c2a6a619c25d8`.

No historical or peer file was overwritten. No email, Drive, public posting, paid compute, access change, or schedule change was performed.

```yaml
ledger_delta:
  track: P02
  parent: T02
  source: "Chvatal-Sankoff constant for two independent iid uniform binary strings"
  metric: "certified interval width U-L under exact dependence-preserving assumptions"
  lower: 0.792665992
  upper_before: "U_W = log(4t^2)/log(lambda_W)"
  upper_after: "U_S = log(4t^2)/log(lambda_S)"
  exact_order: "U_S < 0.826275942762282625015106581537296632823461996193190023880806183312562944430299551 < U_W"
  width_before: "U_W - 0.792665992"
  width_after: "U_S - 0.792665992"
  movement: true
  status: PARTIAL
  source_status: OPEN
  mechanism_advance: "exact label-support exclusion forces every tight C045 row to send coefficient weight at least D=c0+c7 to non-tight successors; D/m_min is between 1939 and 1940"
  finite_transfer: "actual-string-pair covering transfer; no independent Bernoulli matching"
  companion_scope: "P13 retains correlated boundary-carry/reset lower-side route"
  next_attack: "coalesced-successor or short-neighbourhood tightening of the tight-row support gap"
```
