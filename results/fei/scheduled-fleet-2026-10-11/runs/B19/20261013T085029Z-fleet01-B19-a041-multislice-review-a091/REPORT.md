# B19 / A091 independent review of A041: one-exceptional theorem accepted; multi-slice entropy remains open

Run ID: `20261013T085029Z-fleet01-B19-a041-multislice-review-a091`  
Primary packet: `A091` (Composition referee)  
Reviewed target: `A041-COHERENT-TWO-WEIGHT-SLICE-APPLICATION-v1`  
Stable gap: `G-BIASED-LTF / MULTISLICE_COHERENT_ENTROPY`  
Full FEI status: **OPEN**

## Verdict

The A041 package contains two mathematically different claims. They survive independent reconstruction at exactly the following scopes.

1. **One exceptional physical input — ACCEPT.** Let
   \[
   F=2\mathbf 1\{wX+\textstyle\sum_{j=1}^nY_j\ge t\}-1
   \]
   under an arbitrary interior product law, with arbitrary `n`, `w>0`, and real `t`. Put `v_i=4q_i(1-q_i)`, `P(S)=\widehat F(S)^2`,
   \[
   E_{\ge2}(F)=\sum_{|S|\ge2}P(S)\ln\frac{v_S}{P(S)},
   \qquad \Delta(F)=I(F)-\operatorname{Var}(F).
   \]
   With `c=460+80 ln 2`, A041 correctly proves
   \[
   E_{\ge2}(F)\le(4c+12+4/e)\Delta(F)
   \]
   and corrected `FEI+` constant `(4c+16+4/e)/ln 2<3000`. The constants are independent of arity, weight, threshold, and biases. Deterministic inputs are handled by contraction.

2. **Arbitrary two-weight groups — ACCEPT AS AN ENERGY LEDGER ONLY.** After merging identical light-variable threshold slices, the stated deficit Gram matrix is positive semidefinite, the mixed `B`-energy identity is exact, and the two ledger pieces spend each root deficit coefficient once. These identities do **not** control the logarithmic entropy of the coherent multi-slice Fourier sum.

3. **Prime family — ACCEPT.** The family
   \[
   F_n=2\mathbf1\{2X+Y_1+\cdots+Y_n\ge3\}-1,\qquad n\ge3,
   \]
   is essential and prime against nontrivial disjoint one-bit substitution by the cofactor-row criterion. It is an unbounded-arity nonsymmetric prime family covered by item 1, not an all-prime theorem.

No substantive repair was needed for these claims, so `fleet05/A041` remains the sole mathematical contributor. The original `CLAIMS.json` should eventually replace its null `first_unproved_line` with the explicit coherent multi-slice entropy gap already stated in its report; that is a metadata correction, not a proof repair.

## Sources read

### Candidate package

At open-problems default-branch snapshot `159f88b6f25301137bb73a7c78a75e2894969541`:

* `reports/fei-2026-10-11/runs/B09/20261011T232825Z-fleet05-A041-weighted-threshold-fei/REPORT.md`, blob `4387025e808cc16f2df3c62ac2ed75891b7a7299`;
* `SLICE_DEFICIT_PAYMENT.tex`, blob `d12d4588a848827d670df946a9eb86b6ab7bb62c`;
* `WEIGHTED_GUARD_LEDGER.md`, blob `73598483072bd1732369a860be8737f036590f50`;
* `CLAIMS.json`, blob `266abaaeccd241ed35dbe90c4dd35e1a752cb4c4`;
* `FROZEN_SPEC.json`, blob `81209dab5d6e85e793ffe811ce424cf7f1504d14`;
* `PROGRESS.json`, blob `ea56e5ce2e6d644f11f413b8e1d3f0a206fd8861`.

### Source theorem

The product-biased symmetric-threshold premise was checked in the owner-approved public source `yspennstate/fourier-entropy-threshold-functions`, commit `b38ba0ab49618ccbe6d1518a34c141dcec9f247c`, `paper/main.tex`, Theorem `bias:strong`. It states
\[
\mathcal E_\mu(g)\le(460+80\ln2)\Delta_\mu(g)
\]
for every symmetric threshold under every product law. The same source's coefficient inequality `bias:eq-5-9` is the scalar inequality used by A041. No O'Donnell--Tan composition theorem, sharp endpoint-tax claim, or unreviewed all-prime assertion is used in the proof reviewed here.

## Independent reconstruction

### 1. Normalization and the singleton charge

For a Boolean sign under a product law, repeated half-differences give
\[
|\widehat f(S)|\le\sqrt{v_S}.
\]
Thus every corrected-entropy summand is nonnegative. If `rho_i` is the pivotal probability and
\[
a_i=\mathbb E[(f(X^{i=1})-f(X^{i=0}))/2],
\]
then
\[
I_i=v_i\rho_i,\qquad P(\{i\})=v_i a_i^2,\qquad |a_i|\le\rho_i.
\]
Using `-x ln x<=1-x`,
\[
P(\{i\})\ln\frac{v_i}{P(\{i\})}
\le2v_i(|a_i|-a_i^2)
\le2(I_i-P(\{i\})).
\]
Since
\[
\sum_i(I_i-P(\{i\}))
=\sum_{|S|\ge2}|S|P(S)\le2\Delta(f),
\]
the full singleton corrected entropy is at most `4 Delta(f)` nats. This argument is valid for the later nonmonotone interval sign.

### 2. Two distinct threshold tails

Let `f_0=2 1{N>=k_0}-1` and `f_1=2 1{N>=k_1}-1` with `k_1<k_0`. For every coordinate their pivotal boundary events are disjoint, hence
\[
\sum_{S\ne\varnothing}|S|\widehat f_0(S)\widehat f_1(S)=0.
\]
Writing `C=Cov(f_0,f_1)>=0` and subtracting its unweighted Fourier expansion gives
\[
C=-\sum_{|S|\ge2}(|S|-1)\widehat f_0(S)\widehat f_1(S)
\le\sqrt{\Delta_0\Delta_1}.
\]
For the interval sign `g=f_1-f_0-1`, disjointness also gives
\[
I(g)=I(f_0)+I(f_1),\qquad
\Delta(g)=\Delta_0+\Delta_1+2C
\le2(\Delta_0+\Delta_1).
\]

Apply the source inequality
\[
\Phi_s((a-b)^2)\le2\Phi_s(a^2)+2\Phi_s(b^2)+2a^2+2b^2,
\quad \Phi_s(x)=x\ln(s/x),
\]
only to sets of degree at least two. Their total squared mass is at most the deficit. Combining this with the symmetric-threshold baseline yields
\[
E_{\ge2}(g)\le(2c+2)(\Delta_0+\Delta_1),
\qquad
E(g)\le(2c+10)(\Delta_0+\Delta_1).
\]
The factor two in the deficit comparison cannot be reduced to one: uniform `AND_2` and `OR_2` tails have deficits `1/4`, covariance `1/4`, and their interval sign is parity with deficit one.

### 3. One exceptional input

Let `f_0,f_1` be the restrictions at `X=0,1`. They are symmetric thresholds, possibly constant or identical. In the nontrivial case define
\[
d=(f_1-f_0)/2,\quad \rho=\mathbb E d,\quad v=4p(1-p),
\]
and
\[
D=(1-p)\Delta(f_0)+p\Delta(f_1),
\qquad \delta=v\rho(1-\rho).
\]
The exact biased Fourier formulas are
\[
\widehat F(B)=(1-p)\widehat f_0(B)+p\widehat f_1(B),
\qquad
\widehat F(\{X\}\cup B)=\sqrt v\,\widehat d(B).
\]
The law of total variance and physical influence averaging give the exact non-overcounting ledger
\[
\Delta(F)=D+\delta.
\]

For `B` of degree at least two, the coherent scalar inequality applied to `(1-p)\widehat f_0(B)` and `-p\widehat f_1(B)` gives the avoiding-`X` charge
\[
(2c+2+4/e)D.
\]
Here the scaling identity
\[
\Phi_s(z^2a^2)=z^2\Phi_s(a^2)+2z^2a^2\ln(1/z)
\]
and `z^2 ln(1/z)<=z/e` are used with the actual weighted deficit `D`.

For coefficients containing `X` and a nonempty `B`, since `\widehat d(B)=\widehat g(B)/2`, their charge is exactly
\[
\frac v4\left[E(g)+(\ln4)\operatorname{Var}(g)\right].
\]
The first term is at most `(2c+10)D`, because
`p(1-p)(Delta_0+Delta_1)<=D`; the second is `(ln4)delta`. Therefore
\[
E_{\ge2}(F)
\le(4c+12+4/e)D+(\ln4)\delta
\le(4c+12+4/e)\Delta(F).
\]
Adding the independently reconstructed singleton bound proves the stated corrected `FEI+` constant. The elementary estimates `e>8/3` and the first four positive terms of the `atanh(1/3)` series for `ln 2` certify it is strictly below 3000.

### 4. The prime family

For a nontrivial disjoint substitution through a block, all cofactor rows on the complement can take at most two values. In `F_n`, any block of at least two light variables has three different rows from block light-counts `0,1,2` when a light variable remains outside, and from counts `0,1,3` when only `X` remains outside. A proper block containing `X` and at least one light variable leaves a light variable outside; block scores `0,1,2,3` generate at least three distinct outside threshold rows. Every input is essential. Thus every proper candidate block of size at least two has at least three cofactor rows, proving primality.

### 5. Arbitrary multi-slice identities

Merge equal light-variable slices `f_s` into heavy-variable cells `c_s` with probabilities `pi_s`. Distinct symmetric threshold slices have disjoint pivotal boundaries. Hence the vectors
\[
u_s(T)=\sqrt{|T|-1}\,\widehat f_s(T),\qquad |T|\ge2,
\]
have Gram matrix
\[
G_{ss}=\Delta(f_s),\qquad G_{su}=-\operatorname{Cov}(f_s,f_u).
\]
It is positive semidefinite, and applying it to `pi` yields
\[
2\sum_{s<u}\pi_s\pi_u\operatorname{Cov}(f_s,f_u)
\le\sum_s\pi_s^2\Delta(f_s).
\]

Parseval over the heavy coordinates and the same disjoint-boundary identity give
\[
\sum_{S_A\ne\varnothing,S_B\ne\varnothing}|S_B|P_F(S_A,S_B)
=\sum_s\pi_s(1-\pi_s)I(f_s)\le\Delta(F).
\]
Finally,
\[
\Delta(F)=\sum_s\pi_s\Delta(f_s)+\delta_A,
\qquad
\delta_A=I_A(F)-\operatorname{Var}_A(\mathbb E_BF)\ge0.
\]
The first term assigns `(|S_B|-1)P(S)` to every set meeting `B`; `delta_A` assigns `|S_A|P(S)` to mixed sets and `(|S_A|-1)P(S)` to pure-heavy sets. Their sum is exactly the root deficit, with no extra reserve.

## Exact remaining obstruction

For arbitrary heavy arity,
\[
\widehat F(S_A,S_B)=\sum_s\widehat c_s(S_A)\widehat f_s(S_B)
\]
is a coherent sum. The accepted Gram and energy identities control quadratic mass but do not provide a normalized reference distribution whose logarithmic cost is bounded by the same single-use deficit. A generic repeated two-term bound introduces a factor depending on the number of slices and also leaves the pure-heavy sector; it therefore does not give a dimension-independent constant.

The first unsupported universal line remains:
\[
\sum_{S_A,S_B:\ |S_A|+|S_B|\ge2}
P_F(S_A,S_B)\ln\frac{v_{S_A}v_{S_B}}{P_F(S_A,S_B)}
\le K\Delta(F)
\]
with one absolute `K` for all two-weight thresholds and arbitrary `|A|`. Neither the PSD Gram matrix nor the one-exceptional theorem proves this line. This is the precise multi-slice entropy payment still owed.

## Independent validation

`CHECK.py` does not import A041 code. It represents every biased Fourier coefficient as `sqrt(r_S) q_S` and checks all algebraic identities in exact `Fraction` arithmetic. Eighty-digit decimal logarithms are used only for finite entropy corroboration.

Command:

```text
python3 CHECK.py
```

Observed runtime: 3.15 seconds. Randomness: none. Results:

* 522 one-exceptional threshold cases: coefficient formulas and `Delta(F)=D+delta` exact;
* 83 multi-slice cases, up to four distinct slices: cross Dirichlet cancellation, Gram entries, mixed-energy identity, and root deficit ledger exact;
* 957 proper blocks for `F_n`, `3<=n<=8`: at least three cofactor rows each;
* maximum observed `E_ge2/Delta = 2.70045841965...`, far below the proved unoptimized constant.

This finite pass corroborates the all-parameter proof; it is not the continuum proof and does not address the open arbitrary-slice entropy inequality.

## Claim and dependency delta

* `A041-COHERENT-TWO-WEIGHT-SLICE-APPLICATION-v1` becomes **INDEPENDENTLY_REVIEWED_ACCEPT_AT_STATED_SPLIT_SCOPE**.
* The one-exceptional entropy theorem, the arbitrary-group energy ledger, and the prime-family admission must remain separately labeled when consumed.
* No all-two-weight, all-prime, shared-variable composition, or full-FEI conclusion is accepted.
* The public symmetric-threshold theorem is a proved dependency; the B09 restriction-uncertainty lemma is not needed for this proof.

## Next action and routing

Route acceptance to B09, A042, A044, A045, A084, A090, and B20. A090 should independently challenge the general matrix ledger if a second review is required.

The next mathematical action is to freeze one candidate normalized reference for all coherent mixed coefficients and test it analytically on the sharp three-bit majority fixture and the recovered rare two-branch families. The test must include the pure-heavy sector and must charge each coefficient's `(|S_A|+|S_B|-1)P(S)` credit only once. Failure should be recorded as a precise reference-measure obstruction, not as failure of the accepted energy identities.

No protected evaluation material, held request, scheduler change, live graph mutation, email, public release, new worker, or paid compute was used. Native downstream ingestion is not claimed.

