# B15 — KL-refunded radius-one transfer for the arithmetic/Shannon remainder

**Status:** OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.

**Execution context:** WITHOUT_VERIFIED_BRAIN. No authenticated brain retrieval or receiver-context use entered this mathematics.

**Role:** account04/B15, interface D: construct or refute the weakest missing arithmetic/Shannon transfer while retaining negative information credits.

## 1. Exact peer inputs consumed

This run uses the joint four-account FEI interface-D state and substantively consumes the newest applicable account02/B15 result:

- `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260921T190147Z-self-xor-low-slice-payment/REPORT.md`, REPORT blob `ccec4aab612e94fa670a41f1f42923cff4cc14f6`.

For a Boolean function, write `a_s=fhat(s)`, `p_s=a_s^2`, take independent `S,S'~p`, and put `D=S xor S'`. Define

`c_d = Pr[D=d] = sum_s p_s p_(s+d)`,

`A_d = sum_s sqrt(p_s p_(s+d))`,

`b_d = c_d log_2(A_d/c_d)` when `c_d>0`, and `b_d=0` when `c_d=0`.

The consumed result proves `H(f)<=B(f):=sum_d b_d` and pays the zero-plus-singleton slice by

`b_0 + sum_i b_(e_i) <= (2+2/ln 2) J(f)`.

It leaves the multi-coordinate remainder `B_(>=2)=sum_(|d|>=2)b_d`.

This run also consumes the exact negative-information refinement from account04/B17:

- `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260921T201333Z-selfxor-kl-refund/REPORT.md`, REPORT blob `cd3f85f7ba871f0e09be10efa4022bb5b6869f19`.

For `c_d>0`, let

`q_d(s)=p_s p_(s+d)/c_d`,

`e_d(s)=sqrt(p_s p_(s+d))/A_d`.

The B17 identity is

`G(f):=B(f)-H(f)=sum_d c_d D_KL,2(q_d||e_d)>=0`.

Thus the actual refund-aware remainder left after the low slice is

`R_*(f):=B_(>=2)(f)-G(f)=H(f)-b_0-sum_i b_(e_i)`.                  (1.1)

The current strongest open target is `R_*(f)<=4J(f)`. This run keeps `G`; it does not return to credit-free packet interpolation or assume physical packet integrality.

A compatible account01/B15 handoff, `20260921T2003Z-kl-softmax-collision-credit/REPORT.md` (blob `4c1049ef0c4495991a48b556eedadde912d87503`), independently shows that a packet collision cost splits into an information-projection KL term plus a soft-max infection term. That is consistent with retaining the KL before any scalar payment, but it is not needed for the theorem below.

## 2. PROVED: exact fibre KL removal gives a radius-one Shannon quantity

For each `d` with `c_d>0`, define the refunded atom

`r_d := b_d - c_d D_KL,2(q_d||e_d)`.

### Theorem B15-REFUNDED-FIBRE-01

For every probability law `p` on the Boolean cube and every `d` with `c_d>0`,

`boxed{ r_d = (c_d/2)[ H(q_d) + log_2(1/c_d) ] }`.                  (2.1)

Consequently, for every Boolean `f`, if

`T_2(f):=sum_(|d|>=2) r_d`,

then

`boxed{ T_2(f) = (1/2) sum_(s,s': |s xor s'|>=2) p_s p_s' log_2(1/(p_s p_s')) }`,   (2.2)

and equivalently

`boxed{ T_2(f) = sum_s p_s log_2(1/p_s) [1-p_s-sum_i p_(s xor e_i)] }`.             (2.3)

Moreover

`boxed{ R_*(f) = T_2(f) - G_(<=1)(f) <= T_2(f) }`,                  (2.4)

where

`G_(<=1)=c_0D(q_0||e_0)+sum_i c_(e_i)D(q_(e_i)||e_(e_i))>=0`.

### Proof

B17 gives, fibrewise,

`D_KL,2(q_d||e_d)=log_2 A_d-(1/2)log_2 c_d-(1/2)H(q_d)`.

Since `b_d=c_d(log_2 A_d-log_2 c_d)`, subtraction yields (2.1).

On the event `D=d`, the ordered pair `(S,S')` has law `c_d q_d(s)=p_s p_(s+d)`. Therefore

`c_d[H(q_d)+log_2(1/c_d)]`

is exactly the Shannon entropy contribution of the ordered-pair atoms on that fibre. Summing (2.1) over `|d|>=2` proves (2.2). For fixed `s`, the excluded partners are exactly `s` and the `n` Hamming-neighbours `s xor e_i`; symmetry of the two logarithmic factors converts (2.2) into (2.3).

Finally, split the exact global refund `G=G_(<=1)+G_(>=2)`. Then

`B_(>=2)-G = [B_(>=2)-G_(>=2)]-G_(<=1)=T_2-G_(<=1)`,

which proves (2.4). QED.

### Interpretation

After the collision-fibre relative-entropy credit is spent exactly, the remaining high-shift cost is no longer a packet depth or escort normalizer. It is a literal **radius-one entropy exposure**: each spectral atom's Shannon contribution is multiplied by the spectral mass outside its closed Hamming radius-one neighbourhood.

This is an exact change of representation, not FEI closure.

## 3. The weakest new sufficient transfer

By (1.1)--(2.4), the single universal implication

`boxed{ T_2(f) <= 4 J(f) }`                                         (3.1)

would imply the refund-aware target `R_*<=4J`. Combining that with the consumed account02/B15 low-slice theorem gives

`H(f) <= [4+2+2/ln2] J(f) = (6+2/ln2)J(f) < 8.886 J(f) <= 8.886 I(f)`.   (3.2)

Thus (3.1), if proved, would prove full uniform-cube FEI with one finite dimension-independent constant.

**Equation (3.1) is OPEN, not proved here.** The point of this run is that the exact source remainder is now written as a local Shannon exposure after all collision-fibre KL credits are retained. No physical packet integrality, packet tensor subadditivity, or credit-free arithmetic/product interpolation is used.

## 4. PROVED obstruction: constant four is sharp for both refunded targets

Consider the one-point-defect Boolean family

`f_n = 1 - 2 1_{0}` on `F_2^n`, `N=2^n`.

Its squared Fourier law has

`p_0=((N-2)/N)^2=:P`,

`p_s=4/N^2=:u` for every nonzero `s`,

and its folded influence is

`J(f_n)=2n/N`.                                                        (4.1)

For every singleton shift `e_i`, direct counting gives

`c_(e_i)=8(N-2)/N^3`,

`A_(e_i)=8(N-2)/N^2`,

hence

`A_(e_i)/c_(e_i)=N`

and

`sum_i b_(e_i)=8n^2(N-2)/N^3`.                                      (4.2)

Also

`c_0=P^2+(N-1)u^2=1-8/N+24/N^2-16/N^3`,

`b_0=c_0 log_2(1/c_0)`.                                              (4.3)

The entropy is exactly

`H(f_n)=P log_2(1/P)+(N-1)u*2(n-1)`.                                (4.4)

The small-atom term in (4.4) is `<8(n-1)/N`. With `x=2/N`,

`P log_2(1/P)=2(1-x)^2[-ln(1-x)]/ln2 <= 2x(1-x)/ln2 < 8/N`,

so `H(f_n)<8n/N=4J(f_n)` for every `n>=2`.

But asymptotically

`H(f_n)/J(f_n) -> 4`,

`b_0/J -> 0`,

`[sum_i b_(e_i)]/J -> 0`.

Therefore, using the exact identity (1.1),

`boxed{ R_*(f_n)/J(f_n) -> 4 }`.                                    (4.5)

Since `R_*<=T_2<=H` and the direct radius-one formula (2.3) has the same limit,

`boxed{ T_2(f_n)/J(f_n) -> 4 }`.                                    (4.6)

Hence any universal inequality either of the exact refunded form

`R_*(f)<=C J(f)`

or of the sufficient radius-one form

`T_2(f)<=C J(f)`

must have

`boxed{ C>=4 }`.                                                     (4.7)

This is a rigorous obstruction to improving the present interface-D constant below four. It is not a counterexample to FEI; rather, it says the B17 constant-four target, if true, is asymptotically sharp.

## 5. Exact finite verification

`verify_b15_refunded_radius1.py` is standard-library only. It exhausts all 65,812 Boolean truth tables through dimension four and directly verifies:

- the fibre identity (2.1) through the aggregate equality `T_2` fibre representation = radius-one representation;
- the identity `R_*=H-b_0-sum_i b_(e_i)`;
- `R_*<=T_2`;
- the OPEN candidate `T_2<=4J` on this finite search only;
- the OPEN refunded target `R_*<=4J` on this finite search only.

Results:

- Boolean functions checked: `65,812`;
- maximum numerical identity discrepancy: `4.441e-16`;
- largest observed `T_2/J` through dimension four: `2.131675485362257`;
- largest observed `R_*/J` through dimension four: `1.687346805595270`.

For the one-point family, direct closed-form evaluations give:

- `n=16`: `H/J=3.930271404540879`, `T_2/J=3.749038252236465`, `R_*/J=3.568659634447173`;
- `n=32`: `H/J=3.965168439111353`, `T_2/J=3.874999970310757`, `R_*/J=3.784831529701766`;
- `n=48`: `H/J=3.976778960037025`, `T_2/J=3.916666666665985`, `R_*/J=3.856554373295602`.

Checker SHA-256:

`dadc84857034c5a59a77e3a434e31e6450259ea6954e8e0615ffb4fdbbbf5b51`.

Recorded output SHA-256:

`f97ab7a97569ea6e64a91bc6c4c2499301624b3b372a2bde9231b0da6de300de`.

The finite search is sanity evidence only. The identities and asymptotic lower bound above are analytic.

## 6. What changed and next exact obligation

**Before:** valuation depth and its tails were influence-paid, but the unequal-magnitude residual could remain hard at valuation zero. Account02/B15 moved to the self-XOR/Hellinger representation and paid the zero/singleton slice. Account04/B17 showed the unrefunded constant-four multi-shift estimate is false and identified the exact collision-fibre KL refund.

**After:** the actual refund-aware remainder is converted exactly into a radius-one Shannon exposure minus a nonnegative low-fibre KL credit. The only new universal transfer needed by this representation is (3.1), and the one-point defect proves the coefficient four is the best possible coefficient for this transfer and for the exact refunded target.

**Next exact implication:** prove or refute `T_2<=4J`. A proof must exploit Boolean signed convolution/physical constraints beyond the probability-law identity, because arbitrary probability laws are not Boolean spectra. A counterexample must exceed four in the radius-one entropy-exposure ratio while satisfying the full Boolean signed self-convolution system. Mandatory stress tests include the one-point-defect sharp sequence, the L-shaped three-point defect from B17, and the near-3/2 Numaro magnitude-flow compositions from the parallel unequal-magnitude work.

## 7. Literature boundary

A fresh primary-source check on 21 September 2026 found no unrestricted uniform-cube FEI proof in the inspected sources. Potapov's 18 September 2026 preprint proves FEI for plateaued and partially bent classes; González--MacManus--Pereyra's May 2026 work develops restriction/stopping-tree progress and retains a missing universal restriction step; Li--Han's general information-theoretic inequality retains an additional influence-profile entropy term. No publication-priority claim is made for the radius-one representation or sharpness result in this report.
