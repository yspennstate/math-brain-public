TASK: B15 ACCOUNT: account02 RUN: 2026-09-21T12:08:37.883178Z — FEI spectral remainder: exact global-credit decomposition and punctured-majority obstruction to packet-local payment

**Status: OPEN / PARTIAL. Full uniform-cube FEI is not proved here.**

**Execution context: WITHOUT_VERIFIED_BRAIN.** No genuine brain retrieval/context was used in this mathematics.

**Model self-report:** GPT-5.6 Sol. **Reasoning effort requested:** maximum actually supported. **Reasoning effort configured/self-reported:** UNKNOWN / not exposed. **Provider reasoning usage:** not exposed.

## 0. What moved

The inherited unequal-magnitude decomposition writes, for each nonzero Fourier magnitude `a`,

`A_a={S:|fhat(S)|=a}`, `p_a=|A_a|a^2`, `r_a=min nu_2(V_a(x))`, `b_a=a 2^{r_a}`, and

`D(f)=sum_a p_a log2(1/b_a)`.

The inherited exact identities are

`H(f)=2 sum_a p_a r_a + 2D(f)` and `H(f)<=4 Ifrak(f)+2D(f)`.

The preceding B15 runs showed (i) `2D=log N-D_KL,2(p||q)` with a large negative KL credit, and (ii) `D` itself is not product-subadditive because product-magnitude collisions can move valuation mass into `D`. This run attacks a more refined possibility: perhaps the positive packet normalizers can be paid by each packet's own exact affine-minimum Fourier geometry, rather than only by the crude centroid lower bound.

That attractive refinement is **false**. I prove an infinite explicit Boolean family with one genuine magnitude packet whose free-energy normalizer and arithmetic remainder grow logarithmically relative to that packet's own *best possible affine/character influence*. The packet has constant asymptotic spectral mass, so this is not a vanishing-mass artefact. Thus any successful arithmetic-remainder proof must use **cross-packet/global Boolean compensation**, not a sum of packet-local payments.

At the same time, I record an exact global decomposition that preserves the credits which a cross-packet proof must exploit.

Creative moves this run: **#2 attack the negation first** (construct an actual Boolean family defeating packet-local payment), **#18 say it in another language** (rewrite the residual as free energy minus local-geometry and global-coordinate credits), and **#24 find the extremal object** (use a punctured tie-majority whose low-frequency packet is an affine simplex).

Tracked quantity: the best constant in a packet-local inequality `D_a <= C I_a^*` changes from **unknown** to **infinite (refuted)**. The global target `sup_f D(f)/I(f)` remains unknown; full FEI remains OPEN.

## 1. Exact credit-preserving decomposition

Fix a Boolean `f:{0,1}^n->{-1,1}` and its magnitude packets. Put

`R = sum_a p_a r_a`.

For an invertible linear frequency map `T in GL(n,F_2)` and a character shift `c in F_2^n`, define the packet energy

`E_a(T,c)=a^2 sum_{S in A_a}|TS+c|`.

This is exactly the homogeneous Fourier influence of the packet after the corresponding invertible affine input change and output-character multiplication. Define its individual affine minimum

`e_a^* = min_{T,c} E_a(T,c)`,

and

`Q=sum_a e_a^*`, `Gamma=Ifrak(f)-Q`.

Because a minimum of a sum is at least the sum of the separate minima,

`Gamma>=0`.

The inherited centroid theorem applies after every such affine/character transformation and gives

`e_a^* >= p_a r_a/2`.

Hence the **local geometry credit**

`G = 2Q-R`

is nonnegative. `Gamma` is a second, genuinely global credit: it measures the incompatibility between the separately optimal coordinate systems for the different packets.

Now define

`N_a = |A_a| 4^{-r_a}`.

Since `p_a=|A_a|a^2=N_a b_a^2`,

`2D = sum_a p_a log2(1/b_a^2)`

`    = H(p) + sum_a p_a log2 N_a`,                                      (1)

where `H(p)=sum_a p_a log2(1/p_a)` is the entropy of the magnitude-packet index. This is the expanded form of the previous free-energy/KL identity.

### Theorem B15-GLOBAL-CREDIT-01

For every Boolean function,

`H(f) = 4 Ifrak(f) + H(p) + sum_a p_a log2 N_a - 2G - 4Gamma`.          (2)

All terms in (2) are exact; `G,Gamma>=0`.

**Proof.** `H=2R+2D`. Also

`4Ifrak=4(Q+Gamma)=2R+2(2Q-R)+4Gamma=2R+2G+4Gamma`.

Substitute (1). QED.

Equation (2) is not itself a FEI proof: the remaining positive free energy still needs a uniform global payment. Its point is that it preserves two negative credits that the loose inequality `H<=4Ifrak+2D` discards: the actual extra geometry of each packet (`G`) and the coordinate-incompatibility credit (`Gamma`). Together with the earlier KL form, it gives three equivalent views of the same unpaid arithmetic problem without dropping signs.

## 2. Infinite Boolean obstruction to packet-local payment

Let `n=2m>=6` with `m` odd, equivalently `n=2 mod 4`. Define a symmetric Boolean function `F_n` by Hamming weight:

`F_n(x)=-1` for `|x|<m`,

`F_n(x)=+1` for `m<=|x|<=n-1`,

`F_n(1,1,...,1)=-1`.

Thus `F_n` is the tie-positive middle threshold, punctured at the all-ones point.

Let `C=binom(n,m)`. I claim that `F_n` has one magnitude packet consisting **exactly** of the empty frequency and all `n` singleton frequencies, with common Walsh magnitude `C-2`.

### 2.1 Exact spectrum isolation

Let `G_n` be the unpunctured tie-positive threshold. For a frequency of size `t`, let `W_t(G_n)` be its unnormalized Walsh coefficient. The constant coefficient is

`W_0(G_n)=C`.

For `t>=1`, summing the Krawtchouk tail and using the elementary partial-sum identity gives

`W_t(G_n) = -2 K_{t-1}^{n-1}(m-1)`,                                  (3)

where `K_s^N(r)` is the character sum over all `r`-subsets against a fixed `s`-set.

For `t=1`, (3) gives `W_1(G_n)=-C`. Flipping the all-ones value subtracts `2(-1)^t`, hence

`W_0(F_n)=C-2`, `W_1(F_n)=-(C-2)`.                                    (4)

For `2<=t<=n-1`, put `N=n-1`, `r=m-1`, `s=t-1`, and `B=binom(N,r)=C/2`. Here `N>=5`, `2<=r<=N-3`, and `1<=s<=N-1`. Fix one element `u` in the `s`-set and one element `v` outside it. For every `(r-1)`-subset `R` of the remaining `N-2` points, the two `r`-subsets `R union {u}` and `R union {v}` have opposite intersection parity with the `s`-set. As `R` varies these sets are all distinct, and

`binom(N-2,r-1)>=3`.

Thus each parity class contains at least three `r`-subsets. Therefore

`|K_s^N(r)| <= B-6`.

Consequently

`|W_t(G_n)|<=C-12`, `|W_t(F_n)|<=C-10<C-2`.                           (5)

At `t=n`, the central character sum is `(-1)^m C=-C` because `m` is odd, and puncturing gives `W_n(F_n)=-C-2`. Thus level `n` also does not collide with (4).

Consequently the magnitude `a=(C-2)/2^n` has exactly

`A={empty,{1},...,{n}}`, `M=|A|=n+1`.                                 (6)

The exact verifier beside this report checks (3)-(6) and the influence identities for every `n=6,10,...,50`; that finite run supports but is not used in the analytic theorem.

### 2.2 Its packet divisibility is zero

The signs in (6) are `+` at the empty set and `-` at every singleton. Its signed mask is

`V(x)=1-sum_i chi_i(x)=2|x|-(n-1)`.

Since `n` is even, every value is odd. Hence

`r=0`, `b=a`, `N_a=M=n+1`.                                             (7)

The packet mass is

`p=(n+1)a^2`.                                                          (8)

### 2.3 Even the best affine geometry costs only constant order

Under an invertible linear frequency map and a character shift, (6) becomes an affine simplex

`{c,c+v_1,...,c+v_n}`

with `v_1,...,v_n` a basis. For each physical coordinate, the `n+1` bits cannot all be equal; otherwise every basis difference would have zero in that coordinate, contradicting spanning. Therefore each coordinate contributes at least one `1` to the total Hamming weight of the simplex. Summing over the `n` coordinates,

`sum_{S in A}|TS+c| >= n`.

The standard simplex attains equality. Thus this packet's individual affine-minimum energy is exactly

`e_A^* = n a^2 = p n/(n+1)`.                                          (9)

Since `r=0`, its entire local geometry credit is only

`G_A=2e_A^* = 2n a^2`.                                                 (10)

### 2.4 Logarithmic divergence of every packet-local payment

The positive free-energy normalizer of this one packet is

`p log2 N_a = p log2(n+1)`.

By (9),

`[p log2 N_a]/e_A^* = ((n+1)/n) log2(n+1) -> infinity`,                (11)

and by (10),

`[p log2 N_a]/G_A = ((n+1)/(2n)) log2(n+1) -> infinity`.               (12)

Its arithmetic-remainder contribution is

`D_A=p log2(1/a)`, so

`D_A/e_A^* = ((n+1)/n)[n-log2(C-2)]`.

Using `binom(n,n/2) ~ 2^n sqrt(2/(pi n))`,

`D_A/e_A^* = (1/2)log2 n + (1/2)log2(pi/2) + o(1) -> infinity`.        (13)

Moreover `p -> 2/pi` and `e_A^* -> 2/pi`: the obstruction carries constant spectral mass and constant packet influence.

Therefore there is **no universal C** for either of the packet-local statements

`D_a <= C e_a^*`

or

`p_a log2 N_a <= C (2e_a^*-p_a r_a)`.

This refutes not only the crude centroid-slack idea but any proof that tries to pay each packet separately using that packet's exact best affine/character geometry.

## 3. Why this does not refute global FEI or global D/I

The same family has total influence

`I(F_n) = [m binom(n,m)+n]/2^{n-1}`.                                  (14)

The first term is the middle-layer boundary; the second is the puncture boundary. Thus `I(F_n)~sqrt(2n/pi)`, while the bad packet contributes only `D_A=Theta(log n)`. Hence

`D_A/I(F_n) -> 0`.

So the family is **not** a counterexample to FEI, and it does not refute a global bound `D<=C I`. It says exactly where the payment must come from: the other magnitude packets and/or the global coordinate-compatibility credit in (2). The Boolean completion of the low-frequency affine-simplex packet carries much larger global influence than the packet itself.

This sharply changes the next obligation. A universal arithmetic proof cannot be of the form “prove a good inequality for every packet and sum it.” It needs a cross-packet theorem forced by `sum_a f_a=f in {+-1}`.

A concrete next target is to lower-bound the **external compensation**

`2 sum_{c != a} e_c^* + 4Gamma`

for any packet with large `p_a log N_a - 2G_a`, using the pointwise Boolean cancellation among the physical projections. Equivalently, prove a global inequality for the positive part

`sum_a [p_a log2 N_a - C G_a]_+`

against influence in the complementary packets plus `Gamma`, while retaining `H(p)` and the earlier KL credit with their exact signs. The punctured-majority family is a required stress test: any valid statement must allow the low-frequency packet's local deficit to grow like `log n` while its completion pays globally on scale `sqrt n`.

## 4. Coordination / non-overlap

At the inspected frontier, account02/B14 is on singleton/restriction erasure selection, B16 on q-flip syndrome transport, B17 on balanced-composition/rare-pair face boundaries, and B18 on product-phase KL stability. This report stays on unequal-magnitude packet arithmetic and affine-simplex local-vs-global compensation. The preceding account03/B15 punctured-subcube result killing the raw `v log N_perp` target is preserved and not repeated.

## 5. Literature check and priority status

Fresh primary-source search on 21 September 2026 rechecked:

- González--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246 (restriction/stopping-tree progress; full FEI remains open there).
- Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean Plateaued Functions*, arXiv:2609.21563, posted 18 September 2026 (plateaued class constant 4; not unrestricted FEI).
- Li--Han, arXiv:2512.03117, on Han-type information-theoretic Fourier entropy/influence inequalities with an additional influence-profile entropy term.

I found no source in this bounded search that turns the project-specific arithmetic remainder into a universal packet-local bound. I make **no publication-priority claim** for Theorem B15-GLOBAL-CREDIT-01 or for the punctured-majority calculation; both are elementary once this packet formalism is fixed.

## 6. Verification and before/after

The exact checker uses only integer binomial/Krawtchouk arithmetic and rational influence identities. It verifies `n=6,10,...,50`: the target magnitude occurs only at levels 0 and 1; the sign mask is odd (`r=0`); spectral influence equals the exact edge-boundary formula; and the displayed packet ratios grow. Saved checker SHA-256 before repository write: `36fc18797a3f3579b48b2c821219213d0956fc3108d79d88c7b3b79a8b8a4fbf`. Saved verification JSON SHA-256: `f0d4fa66c92bec3d3467f22593e55fd1a1a12eec1c57610a2fb47b7e8f608a21`. These hashes are local exact bytes for these newly generated harmless files.

**Before:** the route knew the arithmetic free-energy/KL identity and the exact product-collision transfer, but it was still plausible that one could keep the negative credits and pay each packet's positive normalizer from that packet's exact affine geometry.

**After:** equation (2) isolates all local and global geometry credits, and the explicit Boolean family proves packet-local payment impossible with an unbounded logarithmic gap, even after exact individual affine minimization. Full FEI remains OPEN.

**Next precise obligation:** prove a genuinely cross-packet Boolean compensation theorem for the residual in (2), or construct a Boolean family in which the positive packet deficits outrun *both* complementary-packet influence and the global coordination credit. Either outcome would decisively move the arithmetic route.
