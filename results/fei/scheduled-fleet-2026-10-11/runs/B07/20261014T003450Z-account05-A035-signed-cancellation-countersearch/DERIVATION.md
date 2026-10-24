# Point surgery: ambiguity, signed interference, and a full carrier

Uniform binary coordinates represent the sign cube; Fourier characters are (-1)^(S dot x). All entropy is in bits. The claims below concern genuine Boolean functions and actual physical restrictions, not arbitrary spectral vectors.

## 1. Actual family and an unchanged physical bill

Let m>=2 be even, L>=1, and b_m(y)=(-1)^(sum y_(2k)y_(2k+1)). Write chi(y)=(-1)^|y|, choose one point y*, e=2^-m, and a(y)=chi(y)(1-2 1_{y=y*}). Put p(y)=(1-a(y))/2 and pi=E p=1/2+chi(y*)e. On disjoint four-bit data blocks x_j and one-bit selectors z_j define

    f=b_m(y) product_j b_4(x_j) (-1)^(p(y) sum_j 1_{x_j=0} z_j).

Set c_+=b_m 1_{p=0}, c_-=b_m 1_{p=1}, G=product b_4, and T=product h_j, where h_j=b_4(x_j)(-1)^(1_{x_j=0}z_j). Then f=c_+G+c_-T. Physical branch supports are disjoint; Fourier branch supports need not be disjoint. Any selector prefix leaves this form with the corresponding h_j fixed at z_j=0 or 1; no core or data coordinate is exposed in this statement.

For every remaining selector, q=1/16 and its physical disagreement indicator is 1_{x_j=0}p(y). Thus

    d=q pi,  W=I(f|z=0 times f|z=1)/2
      =q[4 pi + I(a)/2],  I(a)=m(1-2e).                 (1)

The last identity follows because changing parity at one point removes precisely its m incident disagreeing edges, each with influence weight 2e. Equation (1) is unaffected by previous selector outcomes: all other factors cancel in the product of the two children. It is a signed convolution bill because the physical product retains the cancellations before Fourier squaring.

The total root influence is also exact. With t=(1-(15/16)^L)/2,

    I(f)=m/2-2e t(m-2|y*|)+L[2+5q pi].                (2)

Indeed data/selector blocks contribute 2+5q pi each. Conditional on the product of activated selectors being negative, the unperturbed core is b_m chi and the point flip reverses its m incident edge states. Exactly |y*| of those edges have a bent sign change, giving signed change -2e(m-2|y*|). The negative-product probability is t. This proves (2) for all the stated finite parameters, without truth-table extrapolation.

## 2. A probability identity separates two different corrections

Normalize all Fourier transforms. With retained frequency R and queried spectral sector Z, write

    hat f(Y,R,Z)=hat c_+(Y) hat G(R,Z)+hat c_-(Y) hat T(R,Z).

The true spectral probability is the square of this signed sum. Define the INCOHERENT probability law

    Pbar(Y,R,Z)=hat c_+^2 hat G^2 + hat c_-^2 hat T^2.

Both laws sum to one, since <c_+,c_->=0. Introduce J=+/- into Pbar by retaining its two summands. Given J=+, Z is deterministic 0. Given J=-, the queried module is h_j, independent of the other module and core spectral factors. Its selector erasure is beta, where

    beta=1+(39/64)log2(13)-(45/64)log2(3)-(25/32)log2(5).

Previously fixed modules remain normalized factors under J=-. Consequently

    Bbar=H_Pbar(Z|Y,R)=pi beta + I_Pbar(Z;J|Y,R).
    B=pi beta + A + C,
    A=I_Pbar(Z;J|Y,R)>=0,
    C=H_P(Z|Y,R)-H_Pbar(Z|Y,R).                         (3)

Equation (3) is a generic probability chain rule once the laws exist. It is NOT a new Boolean-specific entropy upper bound. The family and signed amplitudes realize it on actual Boolean inputs. The interference term C has no fixed sign; nonnegativity of A does not impose a sign on A+C. Replacing a signed sum by an unsigned square can bound an individual amplitude, but does not give either ordering of these normalized conditional entropies. No triangle inequality for entropy is used here.

## 3. Two exact seven-variable refutations

Take m=2,L=1 and query z. In the table each pair (u^2,v^2) is an integer Walsh pair for the two retained child amplitudes, with denominator 4096. The incoherent pair is expressed at the SAME child scale; full-parent arrays in validation.json use denominator 16384 and pairs four times larger.

| y* | pi | d | W | I(root) | coherent pairs: multiplicity | incoherent pairs: multiplicity |
|---|---|---|---|---|---|---|
| 0 | 3/4 | 3/64 | 7/32 | 205/64 | (25,9):10; (49,1):30; (121,9):6; (81,1):18 | (97,9):10; (241,9):6; (25,1):30; (41,1):18 |
| 1 | 1/4 | 1/64 | 3/32 | 197/64 | (49,1):36; (81,1):28 | (25,1):30; (41,1):18; (153,1):10; (169,1):6 |

For any such pair histogram,

    B=1/4096 sum_pair multiplicity [(u^2+v^2)log2(u^2+v^2)
                                  -u^2 log2(u^2)-v^2 log2(v^2)].

Factor the integers into primes. For y*=0, 1024(B-(3/4)beta) is log2 of

    (2^256 5^1420 41^369 17^85)/(3^990 7^735 11^363 13^273).

The numerator has bit length 5878 and the denominator 5899, proving B<(3/4)beta exactly. For y*=1, 512(B-(1/4)beta) is log2 of

    (2^384 5^550 41^287)/(3^1044 7^441 13^78).

The bit lengths are 3199 and 3182, proving B>(1/4)beta exactly. Independent direct-character sums reconstruct both histograms and the integer products. Therefore neither B>=pi beta nor B<=pi beta survives one-point phase surgery. These are refutations of hypothetical extensions of the OLD scoped disjoint-row formula, not of A035 stage2's actual statement or of an attributed peer claim.

The signed interference C itself is negative for y*=0 and positive for y*=1. Exact prime-product certificates, not just decimals, are in out/reproduction.json. Useful outward decimal intervals are:

    y*=0: B in [0.224380510424,0.224380510425],
           A in [0.020249555290,0.020249555291],
           C in [-0.040760822961,-0.040760822960].
    y*=1: B in [0.115418108553,0.115418108554],
           A in [0.027330420449,0.027330420450],
           C in [0.006457095406,0.006457095407].

## 4. Full derivative carrier: the missing credit is entirely internal

There is also a finite history-transfer failure beyond the minimal witnesses. For m=2,L=2,y*=1, querying the second selector after the first selector is fixed gives B in [0.115418108553,0.115418108554] when the earlier value is zero, and B in [0.107391116553,0.107391116555] when it is one. Thus erasure depends on the earlier physical selector outcome, even though pi=1/4, d=1/64, W=3/32 and full carrier rho=1 are identical. The two histories each have physical reach 1/2. This is an exact interval certificate from the full signed spectra in out/validation.json, not a claimed general monotonicity theorem. The old history-invariance relied on disjoint rows.

For even m, hat b_m takes only values +/-2^(-m/2); so does its character translate. The unperturbed c_- Fourier coefficients are either 0 or +/-2^(-m/2). The point perturbation adds or subtracts an amplitude of modulus e=2^-m in EVERY row. Since e<2^(-m/2), none of the perturbed coefficients vanishes. For the queried selector, the derivative contains c_-(y)1_{x_j=0}, times the other h factors. The queried point indicator has no zero Fourier coefficient. Every free h_4 has nonzero coefficients in both selector sectors: its zero sector is hat b_4-1/16 and its one sector is 1/16 up to sign. Fixed h_4(z=0)=b_4 and h_4(z=1)=b_4-2 1_{x=0} are also full-support (coefficients +/-1/4 and +/-1/4-1/8). Products of these factors stay nonzero. Thus EVERY retained derivative row is nonzero for all selector-prefix histories, all even m>=2, and every L>=1.

In A031's notation E is the whole retained spectrum and rho=1. Hence the carrier-membership credit is zero and

    M=h2(d)-B=mu,  B=h2(d)-mu.                        (4)

Signed Booleanity still gives sum u_R v_R=E AV=0. Both physical children put mass one on E. In the two minimal witnesses the within-carrier credits are, respectively, [0.048590347489,0.048590347490] and [0.000696966751,0.000696966752]. Full support alone therefore says little about the size of the surviving logarithmic credit. This tests A031 stage3 sections1-2 at their stated scope and supplies an infinite explicit family of full-carrier collisions; it does not accept its other claims by implication.

## 5. Terminal cost is retained and this is not an FEI counterfamily

After the core and all selectors are physically fixed, each data block is b_4 or b_4 with its origin flipped, independently conditional on that history. Let H*=6-(27/16)log2(3) be the entropy of that point-flipped bent function. Averaging under true physical reach probabilities gives

    I_terminal=L[2+pi/4],
    H_terminal=L[4+(pi/2)(H*-4)].                     (5)

The terminal spectrum is a product on every leaf, so entropies and influences add before physical averaging. H*<4 while each bent block has H=4,I=2 and each point-flipped block has I=5/2. Thus H_terminal<=2 I_terminal for every parameter; no terminal entropy is erased from the ledger. In the two witnesses (I_terminal,H_terminal) is (35/16, about 3.747015917512) and (33/16, about 3.915671972505). Root entropies are about 6.107018375740 and 6.071501960068 respectively, computed from the FULL signed root spectra.

There is no unbounded FEI ratio hidden in this family: H<=m+5L by the support-size bound and (2) gives I>=m/4+2L; hence H<=4I. This is only a guard on the countersearch, not the research target or a claimed advance in class constants.

## 6. First unsupported line and transfer target

The first unsupported universal line is an influence payment of the signed within-carrier entropy residual under arbitrary nonlinear shared phases and physical restrictions. Equation (3) neither pays that residual nor gives a beneficial sign to C. It only prevents incorrectly transporting the disjoint-row equality, or the nonnegative latent ambiguity, across coherent interference. NEXT should construct one normalized derivative reference for spectral levels >=2 and test its single owned logarithmic residual on these two opposite-sign rows, keeping (5) and every reference reset explicit. If such a reference cannot pass these seven-variable witnesses, the failure is a local payment/sign issue, not an FEI disproof.
