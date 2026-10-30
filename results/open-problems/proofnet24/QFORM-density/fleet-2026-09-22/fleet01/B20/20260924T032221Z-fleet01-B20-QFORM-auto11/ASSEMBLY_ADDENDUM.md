# Assembly addendum: pull back to the tiny residual before applying the range-paving closure

After the first B20 report was written, the current fleet01/B19 assembly source was incorporated. This strengthens the same branch and should be used as the final endpoint of this run.

Source:

`yspennstate/math-open-problems@b4a77ade04e619a10fec5678d52d7c31480d54c5`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260924T024923Z-fleet01-B19-QFORM-auto11/REPORT.md`.

B19 proves that the active vector produced by the completed fleet02/B20 orthogonal peel can be pulled back to the **original** rank-42 carrier before the peeled increments were transferred into the residual. Thus the same fleet02/B20 active localization can be retained with the sharper exact decomposition

`A=D0+R0+E0`, `R0=V K V^T`, `rank(R0)<=42`,

`||D0||op < d0:=0.007619480067767874`,
`||E0||F < eps0:=4.808627781218889e-8`,                          (A.1)

and a unit `u` plus literal physical `H` such that

`|H|<=28224`,
`||(Vu)_H||^2>1/2`,
`||K u||>=0.0009524350084709843`.                               (A.2)

The B19 source displayed only the inherited carrier lower bound `s3(R0)>0.0533363...`. The original target again restores the actual scale:

`boxed: s3(R0) > gamma1:=1-d0-eps0
                     =0.9923804718459542... .`                   (A.3)

Indeed `s3(A)>=1` and `||A-R0||op<=||D0||op+||E0||op`.

## Stronger physical range-paving threshold

Let `P=VV^T`, `r=rank(R0)<=42`, and `q=max_iP_ii`. For a Bernoulli physical half-cut, the exact second-moment identity gives a literal partition `I sqcup J=[n]` with

`V_I^T V_I, V_J^T V_J >= g(q,r) I_r`,
`g(q,r)=(1-sqrt(qr))/2`,                                        (A.4)

whenever `qr<1`.

If

`q<=1/43`,                                                       (A.5)

then `r<=42` gives

`g(q,r)>=g43:=(1-sqrt(42/43))/2
             =0.005848154398237715... .`                         (A.6)

The same polar-factor argument as in `REPORT.md` gives

`s3(R0[I,J])>=g43 s3(R0)`.

The diagonal has zero physical cross block and the tiny nonzero residual is retained, hence the **actual** ambient physical cross block obeys

`boxed:
s3(A[I,J])
 > c43:=g43 gamma1-eps0
 =0.005803546134873324... .`                                     (A.7)

Therefore

`e3(A[I,J]A[I,J]^T)>c43^6`,

and the current source-valid physical-E3 theorem gives

`boxed: ||p_Q||infinity < C3/c43
                       <1782.546`,                               (A.8)

with a continuous `C0` density on this paid branch.

Thus every still-unpaid finite-active-localized state must satisfy

`boxed: max_i P_ii>1/43.`                                        (A.9)

The physical heavy-range set

`L43={i:P_ii>1/43}`

has

`boxed: |L43|<=1806`,                                             (A.10)

because `sum_iP_ii=r<=42`.

Set

`F=H union L43`.

Then

`boxed: |F|<=30030`,                                              (A.11)

and every unpaid state in this branch simultaneously satisfies

`||(Vu)_F||^2>1/2`,
`||Ku||>=0.0009524350084709843`,
`P_ii<=1/43 for i outside F`,
`s3(R0)>0.9923804718459542`,
`||D0||op<0.007619480067767874`,
`||E0||F<4.808627781218889e-8`.                                  (A.12)

This strictly strengthens both the `1/672` and `1/44` structural endpoints in the earlier files of this run. Their proofs remain valid; (A.9)-(A.12) are the final range-paving constants.

## Combine with the current B19 physical row reduction

The same B19 source independently reduces the active set `H`, after principal-minimal descent, to an exhaustive physical alternative:

- a finite physical hub `||A[H,H]||op>1/2`;
- a literal original-coordinate star `||A[i,H^c]||_2>=0.000744047619...` for some `i in H`; or
- a literal-coordinate signed near-threshold normalized row carrying at least `1/112896` of the weighted spectral energy described in B19, with exact threshold modes handled separately.

Accordingly, the strongest current unpaid finite-carrier packet is not merely “localized”: it has **all** of the following at once:

1. the exact tiny-tail decomposition (A.1);
2. almost-unit third carrier singular value (A.3);
3. the fleet02/B20 active vector (A.2);
4. a heavy physical carrier coordinate `P_ii>1/43` unless already paid by (A.8);
5. a universal finite union `F` of at most `30030` physical coordinates containing more than half of the active vector and every carrier row above leverage `1/43`;
6. after principal-minimal descent, one of B19's HUB / STAR / near-threshold normalized-row outputs.

The final first unresolved implication from this branch is therefore

`QFORM-R44-30030CORE-HUB/STAR/NORMALIZEDROW-PAYMENT-v1`:

> combine the finite heavy-range core with the B19 literal HUB/STAR/normalized-row output and the remaining two target-scale spectral resources to produce a source-valid physical E3, grouped-overlap, indefinite-pair, or finite principal-core payment, while retaining `D0`, `E0`, and all original-product provenance.

The common-hub curvature collar and giant near-rank-one/exterior-third-mode collar from fleet02/B20 remain separate unresolved endpoints. No claim of a full solution is made.

Full QFORM remains OPEN; full-target continuity remains OPEN separately.
