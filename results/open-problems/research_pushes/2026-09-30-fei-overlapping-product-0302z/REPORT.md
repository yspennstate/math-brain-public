# Overlapping Boolean products: an entropy-subadditivity counterexample and the exact averaged replacement

30 September 2026. **Full FEI remains OPEN.** This report retires one attempted full-Booleanity route. It gives two actual Boolean counterexamples to `H(fg)<=H(f)+H(g)` on shared coordinates, one with a single-point multiplier and one consisting of two elementary rare clauses sharing just one bit. Neither is an FEI counterexample.

**Attribution correction, 03:06 UTC.** The eleven-variable shared-clause construction in Section 2 is exactly the already archived September 20 directional-compression counterexample, after reversing its common control bit. That source's equation (7.6) explicitly identifies its decrement defect with `H(fg)-H(f)-H(g)`. Thus the broad overlapping-product subadditivity assertion was already refuted there. This continuation independently rediscovered that example; it must not be counted as a new theorem. The seven-variable single-point-multiplier certificate is a distinct witness, and Section 2 adds a directly derived all-width asymptotic and its stated influence-interaction consequence. Publication novelty for all additions remains unverified. See [the prior exact source](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-20-directional-compression/REPORT.md#7-an-explicit-obstruction-to-shared-control-subadditivity) and [CORRECTION.md](CORRECTION.md).

## 1. Seven-variable single-point certificate

Use `x in F_2^7`, identified with integers 0 through 127 by binary expansion. Let `g` be negative only at the origin. Let `f` be negative exactly on the following explicit set and positive elsewhere:

    2,3,6,7,8,9,11,13,16,17,19,20,21,22,26,27,28,31,32,36,37,38,
    42,43,44,49,50,52,53,56,57,59,60,61,62,64,65,68,69,70,71,72,
    73,75,76,82,86,88,89,92,94,97,100,101,102,104,105,106,107,
    110,111,113,115,118,119,123,127.

Write `W_f(S)=128 fhat(S)`. An integer Walsh transform of the complete truth table gives these exact **signed** histograms:

| Function | Walsh value : multiplicity |
|---|---|
| f | −6:48, −2:60, 26:16, 30:4 |
| g | −2:127, 126:1 |
| fg | −8:48, −4:60, 24:16, 28:4 |

The product differs from `f` only at the origin, where `f(0)=1`; consequently every Walsh coefficient changes by exactly `−2`. In each row the squared values sum to `128^2`, as required.

For an exact squared-numerator histogram `(u_j,c_j)`, its entropy is

\[
H=14-\frac1{16384}\sum_j c_j u_j\log_2u_j.
\tag{1.1}
\]

Substituting the table gives

\[
H(f)=5.063039875872696\ldots,\quad H(g)=0.4161015545062654\ldots,
\]
\[
H(fg)=5.642226630588523\ldots,
\]
\[
\boxed{\ H(fg)-H(f)-H(g)>0.1630852002095.\ }
\tag{1.2}
\]

The companion checker encloses each logarithm by rational atanh-series bounds and accepts (1.2) through a rational lower endpoint, not displayed floating-point digits. Thus overlapping-product entropy subadditivity is false even when the multiplier is a one-point defect. The related proposed point-flip bound `H(f')-H(f)<=H(one-point defect)` is false as well.

Tensoring this pair on disjoint blocks multiplies the excess by the number of blocks. Therefore no dimension-independent additive constant repairs `H(fg)<=H(f)+H(g)+C`. This does not rule out a multiplicative constant or an influence-dependent correction, neither of which is proved here.

## 2. A transparent eleven-variable rare-clause counterexample

The seven-variable witness is explicit but not structurally simple. The following family explains a second mechanism without a searched truth table.

Fix `m>=2`. There is one common bit `z`, a block `a` of `m-1` bits, and a disjoint block `b` of `m-1` bits. Define

\[
f_m(z,a,b)=1-2\mathbf1_{\{z=0,a=0\}},\qquad
g_m(z,a,b)=1-2\mathbf1_{\{z=0,b=0\}}.
\tag{2.1}
\]

Both are genuine one-point-defect functions on their own `m` coordinates. They share only `z`. Put `p=2^(1-m)` and `e(u)=u log_2(1/u)`, with `e(0)=0`. Their common entropy is

\[
H(f_m)=H(g_m)=e((1-p)^2)+(2/p-1)e(p^2).
\tag{2.2}
\]

The nonzero Fourier coefficients of `h_m=f_m g_m` fall into four classes:

| Frequency type | Coefficient | Multiplicity |
|---|---:|---:|
| empty | `1-2p+2p²` | 1 |
| shared bit only | `−2p(1-p)` | 1 |
| nonempty in exactly one private block, shared bit optional | `−p(1-2p)` | `4(1/p-1)` |
| nonempty in both private blocks, shared bit optional | `2p²` | `2(1/p-1)²` |

Some listed coefficients may vanish at the small endpoint `m=2`; zero weights contribute zero. For `m>=3` the stated classes are nonzero. All remaining coefficients vanish.

**Proof of the spectrum.** At `z=1`, the product is constant one. At `z=0`, it is the tensor product of two one-point-defect signs on `m-1` bits. Each child has constant Fourier coefficient `1-2p` and all its other coefficients `−2p`. The selector Fourier rule averages and differences the two restrictions. At nonempty private labels, both selector coefficients are half of the corresponding tensor coefficient. At the empty private label, they are `(1+(1-2p)^2)/2` and `((1-2p)^2-1)/2`. This gives the table. QED.

Consequently

\[
H(h_m)=e((1-2p+2p^2)^2)+e(4p^2(1-p)^2)
\]
\[
\hspace{1cm}+4(1/p-1)e(p^2(1-2p)^2)
+2(1/p-1)^2e(4p^4).
\tag{2.3}
\]

At `m=6`, the physical dimension is eleven. The exact formula, separately verified by a full integer Walsh transform on all 2,048 inputs, gives

\[
\boxed{\ H(h_6)-H(f_6)-H(g_6)>0.00239650700679.\ }
\tag{2.4}
\]

The failure occurs even for two width-six conjunction phases with only one shared physical bit. A sweep restricted to ambient dimension at most nine cannot see this example: overlap one at width six needs dimension eleven.

### All-width asymptotic

Let `L=log_2(1/p)=m-1`. Direct expansion of the four terms gives

\[
H(h_m)=8pL+\frac{4p}{\ln2}-24p^2+O(p^3L),
\]
\[
2H(f_m)=8pL+\frac{4p}{\ln2}-4p^2L-\frac{6p^2}{\ln2}+O(p^3),
\]
\[
\boxed{\ H(h_m)-2H(f_m)
=4p^2\log_2(1/p)+\left(\frac6{\ln2}-24\right)p^2
+O(p^3\log(1/p)).\ }
\tag{2.5}
\]

For example, for the first expansion, the heavy atom contributes `(4p-16p²)/ln2+O(p³)`; the shared-bit atom contributes `8p²L-8p²+O(p³L)`; the one-private-block terms contribute `8pL-40p²L+16p²/ln2+O(p³L)`; and the two-private-block terms contribute `32p²L-16p²+O(p³L)`. The `p²L` terms cancel in their sum. This also checks the constant in (2.5).

The positive `4p² log(1/p)` term dominates the bounded multiple of `p²`, proving that the subadditivity violation persists for every sufficiently large width. The finite certificate is independent of this eventual assertion; no unproved threshold width is substituted for an exact inequality.

### No fixed linear payment by the actual pivotal overlap

For this family, `I(f_m)=I(g_m)=mp` and `I(h_m)=2mp-2p²`. Indeed, every private coordinate remains pivotal with probability `p`; the common coordinate is pivotal in the product precisely when the two independent private one-point indicators disagree, with probability `2p(1-p)`. The only simultaneous pivotal event occurs on the common coordinate, with probability `p²`. Consequently

\[
\frac{H(h_m)-H(f_m)-H(g_m)}{I(f_m)+I(g_m)-I(h_m)}
=2\log_2(1/p)+\frac3{\ln2}-12+o(1)\longrightarrow\infty.
\tag{2.6}
\]

Thus even the influence-dependent repair `H(fg)<=H(f)+H(g)+C[I(f)+I(g)-I(fg)]` is false for every fixed finite `C`. This precise conclusion concerns the **actual common pivotal overlap**; it does not rule out a different global influence correction. A logarithmic overlap cost survives this calibration: the defect divided by `h_2(p²)` tends to two. No universal bound of that latter type is proved here.

## 3. The surviving averaged statement and its nonnegative ledger

The counterexamples do not invalidate translation averaging. Here is the exact all-Boolean replacement, with the interference retained.

Let `f,g` be arbitrary Boolean signs on the same `n`-cube. Let `S,T` be independent draws from their respective squared Fourier laws; put `U=S xor T`. For uniform physical translation `z`, set `h_z(x)=f(x)g(x+z)`. Then

\[
\boxed{\mathbb E_zH(h_z)\le H(S\oplus T)\le H(f)+H(g).}
\tag{3.1}
\]

More precisely, there is a physical/spectral joint law `(U,Z)` with `Z` uniform such that

\[
\boxed{\ H(f)+H(g)-\mathbb E_zH(h_z)
=H(S\mid U)+I(U;Z).\ }
\tag{3.2}
\]

Standard Walsh entropic uncertainty also gives

\[
0\le I(U;Z)\le H(S\mid U),
\tag{3.3}
\]

so the deficit in (3.2) lies between one and two times `H(S|U)`. This is the two-input form of the already archived self-derivative uncertainty identity; it is not claimed as a newly discovered entropic-uncertainty theorem.

**Proof.** Write `a_s=fhat(s)`, `b_s=ghat(s)`, and

\[
r_u(z)=\sum_s a_s b_{s\oplus u}(-1)^{s\cdot z},\qquad
q_u=\sum_s a_s^2b_{s\oplus u}^2.
\]

Up to the harmless sign `(-1)^(u dot z)`, `r_u(z)` is the Fourier coefficient of `h_z` at `u`. Booleanity gives `sum_u r_u(z)^2=1` at every `z`; Walsh orthogonality gives `E_z r_u(z)^2=q_u`. Thus

\[
\Pr(U=u,Z=z)=2^{-n}r_u(z)^2
\]

is a probability law with `Z` uniform and `U` distributed as `S xor T`. Its conditional entropy `H(U|Z)` equals `E_z H(h_z)`. Since `(S,T)` and `(S,U)` determine one another, `H(f)+H(g)=H(S,T)=H(U)+H(S|U)`, which proves (3.2). Nonnegative mutual information proves (3.1). For (3.3), normalize the vector `a_s b_(s xor u)` by `sqrt(q_u)` whenever `q_u>0`. Its squared amplitudes are the conditional law of `S` given `U=u`, and the squared amplitudes of its normalized Walsh transform are the law of `Z` given `U=u`. Entropic uncertainty gives `H(S|U=u)+H(Z|U=u)>=n`; average and use `H(Z)=n`. QED.

The matching influence identity is also exact:

\[
\boxed{\mathbb E_z I(fg(\cdot+z))
=I(f)+I(g)-2\sum_i\operatorname{Inf}_i(f)\operatorname{Inf}_i(g).\ }
\tag{3.4}
\]

Across an `i` edge, the product flips precisely when the two Boolean edge-flip indicators disagree. Under independent uniform `x,z`, the points `x` and `x+z` are independent uniform inputs. The two indicators therefore have respective probabilities `alpha_i,beta_i` and mismatch probability `alpha_i+beta_i-2alpha_i beta_i`. Sum over coordinates.

The checker verifies the averaged spectral identity with integers over all 128 translations of the seven-variable witness, as well as (3.4). It checks the entropy consequence with rational logarithm intervals.

### A valid bounded-overlap repair

If `f` and `g` share at most `k` physical variables and otherwise depend on disjoint blocks, then

\[
\boxed{H(fg)\le H(f)+H(g)+2k.}
\tag{3.5}
\]

Here is a short self-contained derivation of the needed restriction bound. For one physical split, let `a,b` be the normalized Fourier vectors of the two Boolean children. The parent coefficients are `(a+b)/2,(a-b)/2`; their marginal on the remaining spectral coordinates is `q=(a²+b²)/2`. The entropy chain rule therefore gives `H(parent)=H(q)+B`, where `0<=B<=1` is the binary conditional spectral entropy. The equal-weight mixture identity gives `average H(children)=H(q)-JS`, where `0<=JS<=1`. The entropy drop is thus `B+JS` and lies in `[0,2]`. Iterate over the `k` shared variables. Every resulting product has disjoint-variable factors and its entropy equals the sum of their entropies. The average restricted entropy of each factor is no greater than its original entropy. Consequently `H(fg)<=E_y[H(f_y)+H(g_y)]+2k<=H(f)+H(g)+2k`. This uses the standard restriction ledger rather than a new universal payment; `k` can grow and is not known to be controlled by influence.

## 4. Exact scope and next mathematical obligation

The rejected route tried to use the full Boolean involution to control every overlapping product by additive spectral entropy. Both examples satisfy full Booleanity, so adding more signed convolution constraints cannot rescue that exact inequality. This is distinct from the September 20 finite-order real-valued no-go, and stronger in this particular direction than the already archived failure of a conditionally negative definite kernel `H(fg)`.

The averaged inequalities remain valid. They do not automatically yield FEI: an adaptive proof must justify how its selected translates reconstruct or simplify the original function and preserve an affordable influence ledger. Selecting a favorable translate in one line and a different favorable energy outcome in another would be invalid. Uniform averages cannot be silently replaced by a chosen point flip or a chosen set of translations.

No universal constant for `H/I` has been obtained. No claim is made that the two counterexamples are minimal in dimension or globally optimal in the amount of violation. The seven-variable pair was found by a seeded single-point-flip entropy search after basic low-dimensional/random-pair screens missed it. The rare-clause family was then found in a structured affine-clause screen and reduced to the explicit construction (2.1). All final accepted signs were independently computed with integer Walsh transforms and rational logarithm bounds.

## 5. Sources and verification

- Earlier exact signed kernel and self-derivative uncertainty identities: [September 20 sharp-derivative report](https://github.com/yspennstate/math-open-problems/blob/2693ff00aa490a1cbfb3b35d4758fff0e43d659f/proofnet24/P03-fei/continuations/2026-09-20-sharp-derivative/REPORT.md), particularly Sections 2 and 7. Its positive sixth-order coefficient refutes negative type; it does not by itself refute the pointwise entropy triangle inequality, which is tested directly here.
- Direct predecessor recovered after the initial archive: [September 20 directional-compression report, Section 7](https://github.com/yspennstate/math-open-problems/blob/fe94de760ee2b47545419a7447b492816bd16045/proofnet24/P03-fei/continuations/2026-09-20-directional-compression/REPORT.md). It already proves the identical eleven-variable defect and its equality to the product-entropy defect; the current source's omission was corrected at 03:06 UTC.
- [Finite-order Booleanity no-go](https://github.com/yspennstate/math-open-problems/blob/2693ff00aa490a1cbfb3b35d4758fff0e43d659f/proofnet24/P03-fei/continuations/2026-09-20-booleanity-order/REPORT.md): read in full before the structural continuation; no relaxed source is called Boolean here.
- [Unrelated-variable composition theorem](https://arxiv.org/abs/1304.1347): its disjointness hypotheses are preserved. The examples share variables and do not contradict it.

`python verify.py` is standard-library-only. The output includes its executed-file SHA-256. Exact numerator histograms, closed spectra, influences and all averaged squared coefficients are checked as integer equalities; logarithms use 48-term rational atanh enclosures after range reduction. The printed decimal endpoints are summaries of rational bounds, not the acceptance arithmetic.

This is a self-contained analytic counterexample package and finite self-check, not an independent mathematical review, formalization, or publication-priority assertion. No schedules, fleet controls, peer files or repository visibility are modified.
