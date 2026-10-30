# B17 FEI creative attempt: signed-autocorrelation point processes and an antichain-spectrum FEI theorem

**Status:** full Friedgut--Kalai Fourier entropy-influence conjecture remains **OPEN / NOT PROVED**.  
**Run label:** `WITHOUT_VERIFIED_BRAIN`.  
**Primary routes:** APPROACH 3 / 7 / 14.  
**Novelty:** no literature-priority claim is made. The 1- and 2-dimensional pivotal/spectral marginal identities are known (Garban--Pete--Schramm / Garban--Steif); Fourier granularity is also standard. The useful point here is to combine these facts with the preceding B17 Palm obstruction and isolate a strictly larger FEI-good spectral class plus a sharper target for the remaining multilevel problem.

## 1. Starting point from the preceding B17 run

The previous run showed that the scalar coordinate-Palm relaxation is unbounded: a uniform law on the `k`-slice can satisfy every scalar Palm-size hypercontractive inequality while `H(S)/E|S|` diverges. A finite `n=161,k=3` slice even beats Hod's `beta(1/2)`. That run excluded the slice by a signed two-coordinate Boolean convolution identity.

The first correction in this run is that, for a *pure-level Boolean spectrum*, there is an even more primitive obstruction: **Fourier granularity already forbids a large uniform slice.** This leads to a clean FEI theorem for every antichain-supported Boolean spectrum.

## 2. Exact point-process characterization by perfect signed autocorrelation

Write `G=(Z_2)^n`, identify subsets with elements of `G`, and let

`a_A = fhat(A)` and `mu(A)=a_A^2`.

### Proposition 1 (exact characterization)

A probability law `mu` on subsets of `[n]` is the spectral law of some Boolean `f:{-1,1}^n->{-1,1}` if and only if one can choose signs on its square roots,

`a_A = eps_A sqrt(mu(A))`,

such that

`sum_A a_A a_{A xor U} = 1[U=empty]`                                             (1)

for every `U subseteq [n]`.

**Proof.** For a Boolean `f`, the left side is the Fourier coefficient `widehat(f^2)(U)`, hence it is `delta_{U,empty}`. Conversely, given `a` satisfying (1), define `f(x)=sum_A a_A chi_A(x)`. The Fourier coefficients of `f^2` are exactly the left sides of (1), so `f^2=1` pointwise and `f` is Boolean. QED.

Equivalently, the group-circulant matrix

`O_{U,A}=a_{A xor U}`

is orthogonal. Therefore the matrix of squared entries `O_{U,A}^2=mu(A xor U)` is a **group-circulant orthostochastic matrix**. FEI can be restated as an entropy-versus-Hamming-moment theorem for first rows of precisely these signed-perfect-autocorrelation point processes.

This formulation keeps exactly the Boolean information that the scalar Palm relaxation discarded.

## 3. Actual Boolean spectra are not negatively associated

A generic negative-dependence or determinantal route is not merely insufficient; universal negative association is false already for a 3-bit Boolean function.

Take the one-point defect with one value `+1` and the other seven values `-1`. Its spectral law is

`mu(empty)=9/16`, and `mu(S)=1/16` for every nonempty `S subseteq [3]`.

Thus for distinct `i,j`,

`P(i in S)=1/4`, `P(j in S)=1/4`, but `P(i,j in S)=1/8`,

so

`Cov(1[i in S],1[j in S]) = 1/8 - 1/16 = 1/16 > 0`.

Hence the spectral sample of a Boolean function need not even be pairwise negatively correlated. APPROACH 14 must exploit the signed autocorrelation structure (1), not generic negative dependence / DPP technology.

## 4. Sensitivity bridge: exact agreement through order two, but not in law

Let `L_i` be the Fourier projection onto sets containing `i`:

`L_i f = sum_{A: i in A} fhat(A) chi_A`.

For Boolean `f`, pointwise

`Z_i(x):=1[i in Sens(x)] = f(x) L_i f(x)`.

Therefore

`E Z_i = <f,L_i f> = sum_{A: i in A} fhat(A)^2 = P(i in S)`,

and for `i != j`,

`E Z_i Z_j = <L_i f,L_j f> = sum_{A: i,j in A} fhat(A)^2 = P(i,j in S)`.          (2)

The equality of the 1- and 2-dimensional pivotal/spectral marginals is known (see Garban--Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Corollary IX.7, attributed there to GPS/Kalai). In the present route it says that every coordinate-Palm spectral law and the corresponding sensitivity Palm law have the same first inclusion moments.

A tempting strengthening is false even in the cleanest homogeneous setting.

### Exact 6-bit counterexample to equality in law

Encode a Boolean truth table by the 64-bit mask

`0xe22755acca551bb8`

(`bit x = 1` means `f(x)=+1`, otherwise `-1`). Exact Walsh transform gives a spectrum supported **only at level 3**, with 13 atoms:

- one atom, `011001`, has mass `1/4`;
- twelve other level-3 atoms have mass `1/16`.

Hence `H(S)=3.5` bits and `|S|=3` surely.

Because `f` is a level-3 adjacency eigenfunction, every input has exactly three sensitive coordinates (equivalently, Euler's identity gives `sum_i f L_i f = 3`). Thus `|Sens(X)|=3` surely as well. The sensitivity-set law has 14 atoms, however, and differs from the spectral law by total variation exactly `1/4`; for example

`P(S=011001)=1/4`, while `P(Sens=011001)=3/16`,

and `P(S=100110)=0`, while `P(Sens=100110)=1/16`.

All singleton and pair inclusion probabilities nevertheless agree exactly, as required by (2). In particular, even **fixed-size + exact 1/2-marginal agreement does not produce an equality-in-law coupling**.

The same example has positive spectral covariances for the pairs `(0,5),(1,4),(2,3)`, each equal to `1/64`.

## 5. Local maximal-support granularity

The useful positive result is an elementary but strong Boolean restriction that the preceding scalar Palm relaxation omitted.

### Lemma 2 (maximal-support atom)

Let `S` be inclusion-maximal in the nonzero Fourier support of a Boolean function `f`. Then

`|fhat(S)| >= 2^(1-|S|)`                                                        (3)

for `S != empty`.

**Proof.** Apply the normalized discrete derivative in all coordinates of `S`. Its Fourier expansion is

`D_S f = sum_{T superseteq S} fhat(T) chi_{T\S}`.

By inclusion-maximality only `T=S` survives, so `D_S f` is the constant `fhat(S)`. On the other hand `D_S f` is an alternating average of the `2^|S|` Boolean values on an `S`-subcube. Such an alternating sum is an even integer, divided by `2^|S|`; hence every nonzero value is a multiple of `2^(1-|S|)`. QED.

Consequently every inclusion-maximal spectral atom `p_S=fhat(S)^2` satisfies

`log_2(1/p_S) <= 2(|S|-1)`.

Therefore the entropy carried by *all inclusion-maximal atoms* is already paid with FEI constant 2:

`sum_{S maximal} p_S log_2(1/p_S) <= 2 sum_{S maximal} |S| p_S`.                 (4)

So any obstruction to FEI beyond constant 2 must live in **buried coefficients**, i.e. support elements having strict support supersets.

## 6. Corollary: FEI with constant 2 for every antichain Fourier support

### Theorem 3

If the nonzero Fourier support of a nonconstant Boolean function is an antichain under inclusion, then

`H(f) <= 2 I(f)`.                                                                (5)

Indeed every nonzero support set is maximal, so sum (4) over the whole spectrum.

A particularly transparent case is a homogeneous Boolean spectrum supported on level `k>=1`. Then `I(f)=k` and

`H(f) <= 2(k-1) < 2 I(f)`.                                                       (6)

This class contains arbitrary Boolean adjacency eigenfunctions / balanced perfect 2-colorings, not only formulas or product constructions.

The exact 6-bit example above has `k=3`, `H=3.5`, and the theorem gives `H<=4`.

### Consequence for the previous uniform-slice relaxation

A pure level-`k` Boolean spectral law can have at most `4^(k-1)` atoms, because every nonzero coefficient has magnitude at least `2^(1-k)`. The previous `n=161,k=3` uniform slice has `binom(161,3)=682640` atoms, whereas a Boolean level-3 spectrum can have at most `16`. Thus the Palm-feasible slice is excluded by coefficient granularity long before one needs its odd signed Johnson cancellation. The signed constraints remain relevant for laws that survive this arithmetic screen.

## 7. A wider high-floor spectral theorem

The same idea gives a dimension-free FEI bound whenever the nonconstant spectrum lies in a high band.

Let `d=deg(f)` and

`m=min{|S|: S != empty, fhat(S) != 0}`.

Standard Fourier granularity (and the direct `{0,1}`-polynomial proof) gives every nonzero Fourier coefficient of a degree-`d`, `{-1,1}`-valued function as an integer multiple of `2^(1-d)`. Let

`r=sum_{S != empty} fhat(S)^2 = 1-fhat(empty)^2`.

Each nonzero nonempty atom has mass at least `4^(1-d)`, so the number `N` of such atoms satisfies `N <= r 4^(d-1)`. For the normalized nonempty law,

`sum_{S != empty} p_S log_2(1/p_S) <= (2d-2) r`.

Also

`-p_empty log_2 p_empty = -(1-r)log_2(1-r) <= (log_2 e) r`,

while `I(f) >= m r`. Hence

### Theorem 4

`H(f) <= [(2d-2 + log_2 e)/m] I(f)`.                                            (7)

In particular if the nonconstant spectrum is supported only on levels `[alpha d,d]`, FEI holds with constant at most `2/alpha + o_d(1)`.

This does not approach full FEI for broad multiscale spectra (`m=1 << d`), but it isolates the only regime the granularity route still has to understand.

## 8. What this changes in APPROACH 3 / 14

The scalar Palm counterexample from the preceding run looked as though signed Johnson cancellation was the first missing ingredient. This run sharpens that diagnosis:

1. actual Boolean spectra are signed-perfect-autocorrelation / group-circulant orthostochastic laws;
2. they can have **positive** pair correlations, so negative-association/DPP routes are dead as universal mechanisms;
3. spectral and sensitivity sets agree exactly through order two, but even homogeneous fixed-size examples need not agree in law;
4. all inclusion-maximal Fourier atoms are individually FEI-good with constant 2;
5. therefore the genuinely hard entropy is carried by **nonmaximal, multilevel coefficients**.

A useful next target is consequently a *buried-atom charging theorem*: exploit the autocorrelation equations (1) to charge the entropy excess of a coefficient `S` that is much smaller than `2^(-|S|)` to Fourier mass on strict supersets of `S`, with a congestion bound that sums to `O(I)`. A one-step Hasse-edge charge is too naive (support may skip levels); any viable transport has to allow long support jumps and use the signed cancellations, not just support containment.

This target is substantially narrower than an arbitrary point-process entropy inequality and is automatically correct on the antichain/homogeneous class.

## 9. Exact computation

`verify_b17_antichain_pointprocess.py` performs exact integer Walsh transforms and rational checks. It verifies:

- the 3-bit one-point defect has pair covariance `+1/16`;
- the 6-bit mask above has pure level-3 spectrum, constant sensitivity 3, exact singleton/pair marginal matching, spectral/sensitivity total variation `1/4`, `H_spec=3.5`, `H_sens=3.561278124459...`;
- the smallest nonzero coefficient in that example is `1/4`, and `H_spec<=4`;
- exhaustive stress testing of every Boolean function through `n=4` that has antichain Fourier support finds no violation of `H<=2I`; at `n=4` the largest observed ratio is `1.0`.

Executed script SHA-256: `5fa69e143d9730478b2ed026243fa48a0ed52200fcbac9ab52729af85263fdef`.  
Executed stdout SHA-256: `94ca00842a46b068023bd69c9190bf06564b55ca2a9248e273daacff9a83af4e`.

The proofs of Propositions 1, Lemma 2, Theorems 3 and 4 are analytic; the computation is a stress test, not a proof substitute.
