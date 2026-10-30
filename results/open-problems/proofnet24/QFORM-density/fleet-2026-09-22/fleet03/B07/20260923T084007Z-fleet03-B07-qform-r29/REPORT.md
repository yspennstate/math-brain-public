SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T08:40:07Z.
attacking: the r28 four-hub curvature survivor — turn a large hub-times-far-core motif into either a genuine transverse product-star bank, a quantitative rank-two tube, a paid diffuse third-volume branch, or a double-anchored third-compound bank.

# fleet03/B07 QFORM r29 — hub-core cancellation forces stars or incident compound mass

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / GEOMETRY  
Run: `20260923T084007Z-fleet03-B07-qform-r29`  
Start control: `yspennstate/math-research-brain@a542faeda86360f93013ee1ad4c35389bf2eb4e9`  
Pre-publication refresh: `yspennstate/math-research-brain@ccd3fbb7b759f2cadf33171e69b4fc48ebfdad88`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: `NEW SUPPORTING PHYSICAL-CORE/LOW-TAIL ALTERNATIVE / ONE SUBBRANCH CONTINUOUSLY PAID / FULL QFORM OPEN`.

## 1. Scope and correction boundary

The target remains the full unrestricted statement: for every dimension, independent real ORIGINAL coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a dimension-free essential-supremum bound for the density of `Q=X^TAX`, or give a valid counterexample. Continuity is tracked separately.

No Gaussianity, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation independence assumption is used. The calculation does not use law-uniform pointwise quadratic-phase decay, an arbitrary-joint coarea estimate, a positive conditional projection-height moment, naive fiber-supremum integration, deletion of a small nonzero quadratic coefficient, or an assertion that one small coordinate minor controls the target.

The live correction ledger was refreshed immediately before publication. The designated `fleet04/B07` QFORM handoff/archive path was also checked fresh and remained absent, so no partner theorem is fabricated. Section 6 applies instead a compatible completed `fleet04/B18` rearrangement result at an actual new inequality.

## 2. Incoming r28 four-hub packet

Use this slot's completed r28 report

`yspennstate/math-open-problems@1ffce50d452b85f4f080ce0b61c68023e8f0d66c`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T073755Z-fleet03-B07-qform-r28/REPORT.md`.

In its determinant-concentrated survivor, after physical row/column permutations only, the relevant ORIGINAL-coordinate cross block has the form

`N = [[A,B],[C,D]]`,                                           (2.1)

where `A` is a `2 x 2` physical hub block, `B` is the outgoing hub-row bank, `C` the incoming hub-column bank, and `D` the far physical core. All four coordinate groups are inherited from the original independent-coordinate partition.

The r28 positive-motif ledger proves that one of

`M1=det(A)^2`,
`M2=||A||_F^2 ||B||_F^2`,
`M3=||A||_F^2 ||C||_F^2`,
`M4=||A||_F^2 ||D||_F^2`,
`M5=||B||_F^2 ||C||_F^2`                                    (2.2)

satisfies

`M_j > theta^4 F^4 / 286654464`,                              (2.3)

where `F` is the inherited parent cross-block Frobenius scale. The present run attacks the previously unpaid `M4` hub-times-far-core motif. The point is to remove its possible determinant cancellation without selecting or reciprocating a single tiny local minor.

Put

`mu := theta^4 / 286654464`.                                  (2.4)

Thus the live `M4` state is

`M4 > mu F^4`.                                                 (2.5)

## 3. New deterministic cancellation lemma

For `h` one of the two hub rows, `l` one of the two hub columns, `r` a far row and `t` a far column, define

`Delta_(h,l;r,t)=A_hl D_rt-B_ht C_rl`.                         (3.1)

Let

`W_11 := sum_(h,l,r,t) Delta_(h,l;r,t)^2`.                     (3.2)

This is exactly the squared `2 x 2` minor mass using one hub row, one hub column, one far row and one far column.

### Lemma 3.1 — `QFORM-FOURHUB-M4-CANCELLATION-DICHOTOMY-v1`

For every `0<delta<1`, either

`M5 >= delta^2 M4`,                                           (3.3)

or

`W_11 > (1-delta)^2 M4`.                                      (3.4)

Moreover in the second branch there is one actual physical hub row/column anchor `(h,l)` whose complete incident second-minor mass

`H2^(h,l)(N)
 := sum_(|R|=|T|=2, h in R, l in T) det N[R,T]^2`              (3.5)

obeys

`H2^(h,l)(N) > (1-delta)^2 M4/4`.                             (3.6)

#### Proof

Regard the two four-index arrays

`U_(h,l,r,t)=A_hl D_rt`,
`V_(h,l,r,t)=B_ht C_rl`

as vectors in Euclidean space. Their squared norms factor exactly:

`||U||_2^2=||A||_F^2||D||_F^2=M4`,
`||V||_2^2=||B||_F^2||C||_F^2=M5`.                           (3.7)

Also `W_11=||U-V||_2^2`. Hence the reverse triangle inequality gives

`sqrt(W_11) >= |sqrt(M4)-sqrt(M5)|`.                          (3.8)

If (3.3) fails, `sqrt(M5)<delta sqrt(M4)`, so (3.4) follows. Finally write

`W_11=sum_(h,l) W_(h,l)`,
`W_(h,l)=sum_(r,t) Delta_(h,l;r,t)^2`.                         (3.9)

There are exactly four anchor pairs `(h,l)`, so one has `W_(h,l)>=W_11/4`. Every minor counted in `W_(h,l)` is included in the full incident bank (3.5), yielding (3.6). QED.

This lemma identifies exactly where the apparent `A*D` determinant cancellation can hide: only in a comparably large transverse `B*C` product bank. It is therefore an aggregate-before-inversion statement, not a one-good-minor statement.

## 4. Lift the incident E2 bank before selecting a determinant

Use the completed anchored-compound theorem

`QFORM-ANCHORED-COMPOUND-TAIL-LADDER-v1`,

source

`yspennstate/math-open-problems@33b7581b6dc153541b2aa4f6c706192bd8a81eaa`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T050509Z-r16/REPORT.md`.

For every real matrix and fixed physical row/column anchor it proves

`H_(k+1) >= [T_k/k] H_k`,                                     (4.1)

where `T_k=sum_(j>k)s_j^2` is the squared Frobenius tail beyond rank `k`. In particular,

`H3^(h,l)(N) >= [T2(N)/2] H2^(h,l)(N)`.                       (4.2)

This completed worker result is applied to the actual incident bank (3.6).

### Theorem 4.1 — `QFORM-FOURHUB-M4-ANCHOR-TRANSDUCER-v1`

Assume the r28 `M4` branch (2.5). Fix arbitrary parameters `0<delta<1` and `tau>0`. Then at least one of the following four alternatives holds:

**(S) transverse-star bank**

`M5 >= delta^2 M4 > delta^2 mu F^4`;                          (4.3)

**(R2) quantitative rank-two tube**

`T2(N) < tau F^2`;                                             (4.4)

**(V3) diffuse third-volume payment**: the full ambient quadratic form has a continuous density with

`||p_Q||_infinity
 < (9sqrt(3)e/2)
   [ tau(1-delta)^2 mu/8 ]^(-1/6) F^(-1)`;                    (4.5)

**(H3) double-anchored third-volume bank**: there are an actual physical row `i` and physical column `a` of `N` for which

`G3^(i,a)(N)
 :=sum_(|R|=|T|=3, i in R, a in T) det N[R,T]^2
 > [tau(1-delta)^2 mu/24] F^6`.                               (4.6)

#### Proof

Apply Lemma 3.1. If (3.3) holds, (S) holds. Otherwise select the physical anchor `(h,l)` from (3.6). If (4.4) holds, stop at (R2). Otherwise `T2(N)>=tau F^2`; (4.2), (3.6) and (2.5) give

`H3^(h,l)(N)
 > [tau(1-delta)^2/8] M4 F^2
 > [tau(1-delta)^2 mu/8] F^6`.                                (4.7)

In particular

`E3(N)>=H3^(h,l)(N)>nu F^6`,
`nu:=tau(1-delta)^2 mu/8`.                                    (4.8)

Now use the current fractional-volume theorem from

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Normalize the squared `3 x 3` minors of `N` to a probability law. If the maximum inclusion marginal on either physical side is at most `2/3`, apply the theorem with `q=4/3` (transposing `N` if needed). It retains arbitrary same-bank curvature, affine terms, outside couplings and additional spectrum, and yields a continuous full-ambient density

`||p_Q||_infinity <=(9sqrt(3)e/2) E3(N)^(-1/6)`,               (4.9)

which together with (4.8) proves (4.5).

It remains that both physical sides have an inclusion marginal `>2/3`. Choose a row `i` and column `a` attaining such marginals. Under the same determinant-squared probability law,

`P(i in R and a in T)
 >=P(i in R)+P(a in T)-1 >1/3`.                               (4.10)

Therefore their double-anchor bank satisfies

`G3^(i,a)(N)>E3(N)/3>nu F^6/3`,                               (4.11)

which is (4.6). QED.

This is the desired physical-core/low-tail alternative: a large hub-times-far-core motif is not left as a raw product norm. It either exposes genuine product stars, forces the whole physical block near rank two at a chosen scale, is paid by a full-ambient integrated-Fourier theorem, or collapses to a fixed physical row/column carrying a definite fraction of an aggregate third-compound bank.

## 5. Concrete standard collar

Take the standard r28 high-tail value `theta=1/16` and choose

`delta=1/4`, `tau=1/16`.                                      (5.1)

Then

`mu=1/18786186952704`,                                        (5.2)

and Theorem 4.1 gives one of:

1. **transverse stars**

`M5 > F^4/300578991243264`;                                   (5.3)

2. **rank-two tube**

`T2(N)<F^2/16`;                                               (5.4)

3. **continuous-density payment**

`boxed: ||p_Q||_infinity <8535.362494 F^(-1)`;                (5.5)

4. **double-anchor third-volume bank**

`boxed:
 G3^(i,a)(N) > F^6/12824703626379264.`                        (5.6)

The constants are exact consequences of

`nu=1/4274901208793088`.                                      (5.7)

The large numerical coefficient in (5.5) is immaterial to the structural objective of this slot; the point is that it is dimension-free and arises before any reciprocal local determinant.

## 6. Compatible fleet04 result applied to the star alternative

The designated `fleet04/B07` current-QFORM directory is still absent. The compatible completed fleet04 result used here is

`fleet04/B18`, `QFORM` r2,

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

Its Juškevičius--Lee rearrangement transfer says that for an original-coordinate linear bank with coefficient vector `u`, the density is bounded by the centered-uniform rearrangement extremal `R(u)`. Together with the standard sharp one-dimensional cube-slicing bound used in r28,

`R(u)<=sqrt(2)/||u||_2`.                                      (6.1)

In branch (S), choose one of the two physical rows of `B` and one of the two physical columns of `C` so that

`||b||_2>=||B||_F/sqrt(2)`,
`||c||_2>=||C||_F/sqrt(2)`.                                   (6.2)

The two banks use disjoint ORIGINAL-coordinate sets. Hence their linear forms are genuinely independent, and (4.3) implies

`||b||_2||c||_2
 >=(1/2)sqrt(M5)
 >[delta sqrt(mu)/2]F^2`.                                     (6.3)

Applying the completed rearrangement result to both banks at this actual inequality gives

`boxed:
 ||p_(b^T X, c^T Y)||_infinity
 <= R(b)R(c)
 <=2/(||b||_2||c||_2)
 <4/[delta sqrt(mu)] F^(-2).`                                 (6.4)

At the concrete values (5.1),

`||p_(b^T X,c^T Y)||_infinity
 <69348856.226273 F^(-2).`                                    (6.5)

This is deliberately retained only as genuine product-provenance currency. The correction ledger forbids promoting a bounded projected density by itself to a bound for an arbitrary curved indefinite quadratic pushforward.

## 7. Regression checks

`CHECKS.py` and captured `CHECKS.txt` are beside this report. They verify the exact constants and test the reverse-triangle/hub-anchor inequalities on 10,000 deterministic-seed integer block matrices. The output ends

`STATUS=PASS`.

These checks are algebraic regression only; the proof is Sections 3--6.

## 8. Remaining implication

This run closes the raw `M4` motif as a structural dead end: it is now replaced by the explicit four-way transducer (S)/(R2)/(V3)/(H3). It does **not** close the whole r28 four-hub receiver.

The first B07 debt is now

`QFORM-FOURHUB-ANCHOR-H3-AND-R2-RECEIVER-v1`:

* pay the genuine rank-two tube (4.4) without deleting its nonzero tail and while retaining arbitrary within-bank curvature;
* or consume the double-anchored third-volume bank (4.6) by a product-preserving finite-core / scalar-pair / volume-disjointness receiver;
* separately handle the r28 `M1,M2,M3` siblings.

The `M5` branch has genuine disjoint-product projection currency but still requires a justified nonlinear curved receiver unless an already-paid source matches its full ambient geometry.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Full-target continuity remains open; continuity is proved here only in branch (V3).

## 9. Review and provenance status

- `QFORM-FOURHUB-M4-CANCELLATION-DICHOTOMY-v1`: proved in this run; independent review pending.
- `QFORM-FOURHUB-M4-ANCHOR-TRANSDUCER-v1`: proved in this run from r28 + the completed anchored-compound ladder + current fractional-volume theorem; independent review pending.
- fleet04/B18 rearrangement result: applied at the explicit bank inequality (6.4); it is not mislabelled as the unavailable designated fleet04/B07 result.
- Full conjecture: open, so no end-to-end review claim is made.

Repository transport is not native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.
