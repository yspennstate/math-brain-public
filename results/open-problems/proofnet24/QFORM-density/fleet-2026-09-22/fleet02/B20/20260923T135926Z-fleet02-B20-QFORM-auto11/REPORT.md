SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T13:59:26Z.
attacking: the first unpaid global N3 low-rank/double-anchor packet; extend the one-anchor three-volume receiver beyond the 1/2 secondary-marginal gate, then splice the newest fleet03/B20 finite near-coloop compiler back into physical star/cross-cut geometry.

# fleet02/B20 — Jensen one-anchor extension and double-double-anchor reduction

Programme: `QFORM-DENSITY-3EIG-20260922`.
Execution label: `WITHOUT_VERIFIED_BRAIN`.
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**.

## 1. Scope and source pins

The owner target is unchanged: for every finite `n`, independent real original-coordinate variables `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite essential-supremum bound for the density of `X^TAX`, or give a valid target counterexample. No moment, support, iid, Gaussian, log-concavity, diagonal-basis, or post-rotation independence assumption is used.

The required interactive source package was reread in its latest compatible state at
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`
(`RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`). Its proved D5 theorem is used at an actual inequality below; its counterexample search still reports no target-valid counterexample.

The fresh global synthesis source is fleet01/B20 run
`20260923T135635Z-fleet01-B20-QFORM-auto11`,
canonical `yspennstate/math-open-problems@936b0f0bad22de82921c2a743fb0738226270348`.
It proves the leverage-free N3 cross-cut and tail compiler. Put
`c_*=(63/128)^2=3969/16384`.
For every `A in N3(1/64)` there is an original-coordinate cross block `N=A[J,K]` with
`E=||N||_F^2>c_*`.
The paid D5 branch is
`e_5(N^TN)>=E^5/(120*64^4)`.

The newest compatible completed designated partner is fleet03/B20 r31,
canonical `yspennstate/math-open-problems@c6e058c3d4aa36e89ad433c1f4d41b6f82739bf8`.
For exact rank three `A=RMR^T`, `R^TR=I_3`, `s_min(M)>=1`, it proves:
either `||p_Q||_infinity<=192e<522` with continuous density, or there are at most 18 original coordinates `S` and a unit spectral vector `v` with
`sum_(i in S)<r_i,v>^2>63/64`.

A second compatible source used below is fleet02/B09 r13,
canonical `yspennstate/math-open-problems@59ccddd0766b466b30abd645926887f907b0bcd7`.
Its theorem `QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1` is the `q=1` endpoint of the extension proved here.

All conditioning in this report is on literal original coordinates. Spectral/frame coordinates are used only for deterministic matrix identities.

## 2. Required pinned D5 source applied to an actual inequality

On the fleet01/B20 cross-cut, if the top four squared singular values carry at most `63/64` of `E`, the distinct-draw argument gives
`Z_5=e_5(N^TN)>=E^5/(120*64^4)`.

The proved D5 theorem from `FOURIER_ROUTE_REPORT.md` gives, with no marginal gate and with arbitrary same-side/outside curvature retained,
`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10)`.

Therefore
`||p_Q||_infinity
 <=5 sqrt(2e)(120*64^4)^(1/10) E^(-1/2)
 <5 sqrt(2e)(120*64^4)^(1/10)c_*^(-1/2)
 =201.7863466627... <201.787`.

Thus every D5-diffuse cross-cut branch is already paid linearly and continuously. The new work concerns a survivor of the fleet01 tail compiler.

## 3. New theorem: Jensen extension of the compulsory-row receiver

Let `I,J` be disjoint original-coordinate banks and `N=A[I,J]`.
Condition on all remaining original coordinates; the two same-side quadratic blocks and all induced affine terms remain arbitrary.

Fix `h in I`, write `a=N[h,:]`, and let `Omega` be any selected family of physical `3x3` minors `(R,C)` such that `h in R` for every member.
Put
`Z=sum_(Omega) det N[R,C]^2>0`,
and normalize by these squared determinants.
For every `i!=h`, let `alpha_i=P(i in R)`.

### Theorem `QFORM-ONE-ANCHOR-JENSEN-q-v1`

Let `1<=q<5/4`.
If
`max_(i!=h) alpha_i <= q/2`,
then the full quadratic-plus-affine output has a continuous density and

`||p_Q||_infinity
 <= C(q) ||a||_2^(1/5) Z^(-1/5)`,                         (3.1)

where

`C(q)=[5/(5-4q)] 2^(4/5) sqrt(e) q^(-2/5)`.                (3.2)

The same coefficient gives the linear interval bound
`P{Q in L}<=C(q)||a||_2^(1/5)Z^(-1/5)|L|`.

For `q=1`, (3.1) is exactly fleet02/B09 r13's
`5*2^(4/5)*sqrt(e)||a||^(1/5)Z^(-1/5)` theorem.

### Proof

Use source-coordinate quadratic decoupling on bank `I`.
For `W=X_J-X'_J`, whose coordinates are independent with densities `g_j<=1`, let
`h_i(s)=|psi_i(2ts)|`.
Then

`|phi_Q(t)|^2 <= F(t)`,
`F(t)=int H(w)R(w) prod_j g_j(w_j)dw`,

where
`H=h_h(<a,w>)` and `R=prod_(i!=h) h_i(<N[i,:],w>)`.

Cauchy-Schwarz under the probability measure `prod g_j` gives

`F^2 <= F_2 F_0`,                                             (3.3)

with
`F_2=int H^2 R prod g_j` and `F_0=int R prod g_j`.

Because the measure is a probability measure, Jensen/Lyapunov gives

`F_2 <= [int H^(2q) R^q prod g_j]^(1/q)`,                     (3.4)
`F_0 <= [int R^q prod g_j]^(1/q)`.                            (3.5)

For (3.4), use the same selected three-volume Brascamp-Lieb determinant weight as in B09.
The compulsory row has exponent one.
Since `|psi_h|<=1`,
`int h_h(s)^(2q) ds <= int h_h(s)^2 ds <= pi/|t|`
by Plancherel and `f_h<=1`.
For every other active row,
`q/alpha_i>=2`, so the proved cap-one characteristic-function lemma gives

`int h_i(s)^(q/alpha_i) ds
 <= (2pi/|t|) sqrt(alpha_i/q)`.

The row entropy factors cancel; `sum_(i!=h)alpha_i=2`.
The column entropy factor is at most `e^(3/2)`.
Hence

`int H^(2q)R^q prod g_j
 <=4 pi^3 e^(3/2) q^(-1) Z^(-1/2)|t|^(-3)`.                 (3.6)

For (3.5), use the B09 derived two-volume measure on low-row pairs.
Its effective determinant mass satisfies
`Z_eff>=Z/||a||_2^2`.
Now `sum alpha_i=2`, the column entropy factor is at most `e`, and the same `q/alpha_i` Fourier norm gives

`int R^q prod g_j
 <=4 pi^2 e q^(-1) ||a||_2 Z^(-1/2)|t|^(-2)`.               (3.7)

Combining (3.3)--(3.7),

`F(t)
 <=[16 pi^5 e^(5/2) q^(-2) ||a||_2 Z^(-1)]^(1/(2q))
   |t|^(-5/(2q))`.

Taking the decoupling square root,

`|phi_Q(t)|
 <=K |t|^(-5/(4q))`,                                         (3.8)

where

`K=[16 pi^5 e^(5/2) q^(-2)||a||_2 Z^(-1)]^(1/(4q))`.

Because `q<5/4`, the exponent `b=5/(4q)` is strictly greater than one.
Integrating `min(1,K|t|^(-b))` exactly gives

`||p_Q||_infinity
 <=[b/(pi(b-1))] K^(1/b)
 =[5/(5-4q)]2^(4/5)sqrt(e)q^(-2/5)
   ||a||_2^(1/5)Z^(-1/5)`,

which is (3.1). The integrable characteristic-function majorant gives continuity on this branch. QED.

## 4. Application: the nested double-anchor branch is paid unless both sides have a second heavy atom

In fleet01/B20's concentrated third-volume survivor, after disjointization there are fixed physical anchors
`i in J`, `j in K`
and four disjoint banks `J1,J2,K1,K2`.
Let `Omega` consist of the nested minors
`({i,a,b},{j,c,d})` with
`a in J1`, `b in J2`, `c in K1`, `d in K2`.
The proof there retains the sharper energy-scaled mass

`Z_nested > E^3/707788800`.                                  (4.1)

Normalize the selected squared determinants.
The row anchor `i` and column anchor `j` are compulsory.

Take `q=6/5`.
Then the secondary-marginal threshold is `q/2=3/5`.
If every non-anchor row marginal is at most `3/5`, apply Theorem (3.1) with `h=i`.
Since `||N[i,:]||_2<=sqrt(E)`,

`||p_Q||_infinity
 < C(6/5) (707788800)^(1/5) E^(-1/2)
 < C(6/5) (707788800)^(1/5)c_*^(-1/2)
 =7981.5806282... <7981.581`.                                (4.2)

The same statement holds if every non-anchor column marginal is at most `3/5`, by applying the theorem to `N^T` with distinguished row `j`.

Therefore every still-unpaid nested-anchor state contains an actual physical row `r!=i` and actual physical column `s!=j` with

`alpha_r>3/5`, `beta_s>3/5`.                                  (4.3)

By the union bound under the normalized selected-minor law,

`P(r in R and s in C) >= alpha_r+beta_s-1 >1/5`.              (4.4)

Hence the squared-minor mass with both row anchors `i,r` and both column anchors `j,s` is

`Z_22 > Z_nested/5 > E^3/3538944000`.                          (4.5)

This is a genuine quantitative two-by-two physical anchor; it is not an inference of one good local minor.

There is also an exact aggregate wedge consequence.
Let `u=N[i,:]`, `v=N[r,:]`.
For each third row `b`, summing squared `3x3` determinants over any subset of third columns is at most the full Cauchy-Binet sum

`sum_(|C|=3) det N[{i,r,b},C]^2
 = ||u wedge v wedge N[b,:]||_2^2
 <= ||u wedge v||_2^2 ||N[b,:]||_2^2`.

Summing in `b` and using `sum_b||N[b,:]||_2^2=E` gives

`Z_22 <= E ||u wedge v||_2^2`.

Thus

`boxed: ||N[i,:] wedge N[r,:]||_2^2 > E^2/3538944000`.       (4.6)

Transposing gives simultaneously

`boxed: ||N[:,j] wedge N[:,s]||_2^2 > E^2/3538944000`.       (4.7)

In particular

`s_1(N)s_2(N) > E/sqrt(3538944000)
              =1.6809823551e-5 E`.                            (4.8)

The diffuse-side nested-anchor packet has therefore been closed. The only remaining nested packet is a quantitatively double-concentrated physical two-row/two-column anchor.

## 5. Newest fleet03/B20 r31 applied at an exact expression

Now restrict to the exact-rank-three slice
`A=RMR^T`, `R^TR=I_3`, `s_min(M)>=1`,
inside `N3(1/64)`.

Apply the fresh fleet03/B20 r31 theorem.
Either `||p_Q||_infinity<522` with continuous density, or there are `|S|<=18` and a unit `v` with

`sum_(i in S)<r_i,v>^2>63/64`.                                (5.1)

By pigeonhole, some actual physical coordinate `h in S` satisfies

`|<r_h,v>|^2 > (63/64)/18 = 7/128`.                           (5.2)

Hence `||r_h||^2>7/128`.
Using the exact Parseval expression

`sum_j A_hj^2
 = sum_j (r_h^T M r_j)^2
 = r_h^T M (sum_j r_jr_j^T) M r_h
 = ||Mr_h||^2
 >=||r_h||^2`,                                                (5.3)

and the N3 diagonal bound `|A_hh|<1/64`, we obtain the physical star-energy floor

`boxed: sum_(j!=h) A_hj^2 > 7/128 - 1/4096
                              =223/4096`.                      (5.4)

The N3 pair determinant bound gives, for every leaf `j`,

`A_hj^2
 <= |A_hh A_jj| + |A_hhA_jj-A_hj^2|
 <1/4096+1/64
 =65/4096`.                                                    (5.5)

A greedy partition therefore produces three disjoint banks of original physical leaves `L1,L2,L3` with

`boxed: sum_(j in L_k) A_hj^2 >31/4096,  k=1,2,3`.            (5.6)

Indeed, build `L1` until its mass first exceeds `31/4096`; by (5.5) its mass is below `96/4096`. Repeat for `L2`; after two such banks the remaining star mass is strictly above
`223/4096-2(96/4096)=31/4096`.

This is `QFORM-EXACTR3-R31-THREEBANK-STAR-SPLICE-v1`.
It is a literal equation-level use of the newest designated partner result and keeps all smoothing banks in original coordinates.

Moreover, fleet01/B20's leverage-free cross-cut theorem can be applied to this same physical hub `h`.
Thus `h^c=J disjoint_union K` can be chosen with
`||A[J,K]||_F^2>c_*`.
All paid D5 / collective-tail / diffuse-third-volume exits retain the arbitrary hub couplings, so every unpaid exact-rank-three r31 near-coloop survivor now carries **both**
the three-bank star (5.6) and one of the low-rank/double-anchor survivors of the global cross-cut compiler.

## 6. Strongest conditional proof graph and first unpaid implication

The no-pivot reduction still makes `N3(1/64)` sufficient for the full target.
On every N3 state the fresh leverage-free cross-cut gives `E>c_*`.
The following branches are source-pinned and paid:

- D5 diffuse fifth-volume: `||p_Q||_infinity<201.787`;
- collective-tail branch: `<344.372`;
- diffuse third-volume branch: `<1030.245`;
- nested double-anchor with either row or column secondary selected-minor marginals at most `3/5`: `<7981.581`;
- in exact rank three, r31's diffuse deletion branch: `<522`.

The first unpaid global implication can now be sharpened to

`QFORM-N3-LOWRANK-OR-2x2ANCHOR-PAYMENT-v1`:

> Under the full original independent cap-one product laws and `A in N3(1/64)`, take the guaranteed physical cross-cut `N` with `E>c_*`. Prove one universal linear small-ball/density estimate in the remaining exact near-rank-one / near-rank-two tubes, or in the concentrated branch possessing fixed original physical indices `i,r` and `j,s` with (4.5)--(4.7), while retaining arbitrary same-bank and outside curvature; alternatively reduce source-preservingly to an already-paid grouped-square, mixed-hub, ridge, pair, or finite-core receiver.

For the exact-rank-three subproblem, the r31 near-coloop survivor additionally has the fixed physical three-bank star (5.6); this extra resource should be spent together with the low-rank/two-by-two-anchor cross-cut rather than by rotating the input law.

The full QFORM theorem is still OPEN. No target counterexample was found. Global continuity is still OPEN; continuity has only been asserted on branches with an integrable Fourier majorant. A full candidate does not yet exist, so the required two independent end-to-end reviews have not begun.

## 7. Regression checks

- No pointwise law-uniform quadratic-phase decay is used.
- No worst-fibre conditional density supremum is used except legitimate conditioning on literal original coordinates followed by a uniform receiver.
- No spectral/post-rotation random coordinates are declared independent.
- No small quadratic tail is deleted.
- No aggregate minor mass is converted into one good minor.
- The `q`-extension is Fourier-integrable exactly for `q<5/4`; the chosen `q=6/5` is safely inside that range.
- All new star and anchor banks consist of original physical coordinates.
