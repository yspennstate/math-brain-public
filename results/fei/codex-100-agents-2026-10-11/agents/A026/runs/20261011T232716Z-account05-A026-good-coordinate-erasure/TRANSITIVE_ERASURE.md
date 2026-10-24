# True erasure on transitive families

All entropy is in bits. Write h(x)=-x log2 x, h2(x)=h(x)+h(1-x), and Phi(a,b)=h(a)+h(b)-h(a+b). Zero terms have their continuous values. For a transitive Boolean sign function, each B_i is equal, each I_i is equal, and the actual selectable root price is B_i/I_i=B/I. Transitivity is a root property, not a hereditary assumption.

## 1. Exact singleton tribes law

Let w,m>=1, p=2^-w, b=1-p, a=b^m, t=b^(m-1). Let f be +1 if at least one of m disjoint width-w blocks is all +1, and -1 otherwise. A076 STRUCTURED_CONTROLS.tex (5)-(9) supplies the existing exact spectrum and H,I formulas; we reconstruct them here only as inputs to the singleton calculation. Coefficients in a nonempty Fourier set meeting k blocks have magnitude 2 p^k b^(m-k), with multiplicity binom(m,k)(2^w-1)^k. The empty coefficient is 1-2a. Thus

I_i=2pt, I=2mwpt,

H=h((1-2a)^2)+8wmpa-8m(ba-a^2) log2 b-8(a-a^2).

Fix a bit i in block 1. Its residual spectral label is (U,R), where U is a subset of the other w-1 bits in block 1 and R is a label on the other m-1 blocks. There are three cases:

* U nonempty: the adjacent coefficients have equal magnitude. Summing their pair mass gives 4p(1-2p)t bits of erasure.
* U empty and R nonempty: the two magnitudes have ratio b:p. Parseval for the other blocks, minus their empty squared coefficient, gives total erasure 4(t-t^2) Phi(b^2,p^2).
* U=R=empty: the two squared coefficients are (1-2a)^2 and 4p^2t^2.

Consequently, the new exact singleton formula is

**B_i=4p(1-2p)t + 4(t-t^2) Phi(b^2,p^2) + Phi((1-2a)^2,4p^2t^2).**

The formula includes m=1 and w=1, and treats the empty packet even at balance. B=mw B_i. This is not A076's entire-tribe conditional erasure: the singleton price has a different limit.

## 2. Uniform all-m limit, with error bounds

Phi(A,E)<=E log2(e(A+E)/E), because -(1-u)ln(1-u)<=u. Also b^2+p^2<=1, and every spectral packet has mass at most one. Divide the exact formula by d=I_i=2pt.

The first term is exactly 2(1-2p). The second term is at most

2p(1-t)(2w+1/ln2) <=4pw+2p/ln2.

The third is at most

2pt log2(e/(4p^2t^2))
 <=4pw+2p/ln2+4p/(e ln2),

using 0<t<=1 and t log2(1/t)<=1/(e ln2). Therefore, simultaneously for **every** m>=1,

2(1-2p) <= B/I <= 2(1-2p)+8pw+(4+4/e)p/ln2.                         (E)

For entropy, use the exact H formula. Its main term divided by I is exactly 4b. The logarithmic term is nonnegative and at most 4/(w ln2), since -ln b<=p/b. The negative term has magnitude at most 4b/w, since 1-b^m<=mp. Finally h((1-2a)^2)<=4(a-a^2)/ln2, so its contribution is at most 2b/(w ln2). Hence

4b(1-1/w) <= H/I <=4b+6/(w ln2).                                  (H)

These are analytic inequalities, not fitted errors. They imply, **uniformly over arbitrary m=m(w)>=1**,

B/I ->2, H/I ->4, B/H ->1/2 as w->infinity.

For w>=2, explicit B/H bounds follow by dividing the lower bound in (E) by the upper bound in (H), and conversely. The denominator of the lower H bound is positive. No assumption mp->lambda or bounded tribe count is required. This strengthens the calibration beyond the fixed-lambda asymptotic already recorded by A076.

## 3. Recursive majority is a contrasting input, not a new claim

A075 REPORT.md (1)-(5) already proves for depth d recursive Maj3:

I_d=(3/2)^d, H_d=4((3/2)^d-1), B_d=0.

Its rooted-tree automorphism group acts transitively on leaves. It is odd under global negation, so all Fourier support has odd cardinality; no support edge differs by one bit. Thus B/H=0 at every d>=1 while H/I->4. We independently check the d=1,2 spectra in the finite ledger, credit the infinite formula to A075, and do not create a duplicate recursive-majority claim. A075 also exhibits an AND3 restriction with a positive all-coordinate erasure price; root zero erasure does not identify an easy hereditary class.

This already answers the lead's yes/no question negatively: B/H need not stay bounded below on transitive sequences with H/I approaching four. Tribes and recursive majority have the same limiting H/I and different limiting root erasure fractions.

## 4. Cyclic threshold definition and finite certificates

Here 'cyclic threshold' means an explicitly defined threshold on overlapping windows: f=+1 iff at least t of the n length-w cyclic windows are all +1. It is invariant under rotations, hence transitive. It is not identified with a weighted linear threshold of the original bits. Frozen cases are n=6,8,10; w=2,3; t=1,...,n. Four extra odd cyclic controls use sign(sum_j x_j x_(j+1) x_(j+2)) at n=5,7,9,11; the odd number of summands prevents a zero score, and global oddness gives B=0.

Integer Walsh spectra, physical edge counts, exact prime-log H and B expressions, and rational outward intervals are saved for all 69 functions. The highest H/I in this finite ledger is the overlapping cyclic window function n=10,w=2,t=1. Its certified values are near H/I=3.89243855524, B/I=3.15519599472, B/H=0.81059622392. Decimals in this paragraph are explanatory only; use out/transitive_certificates.json for exact rational enclosures. An independent direct character-sum transform checks this benchmark. No universal limit for overlapping cyclic windows is claimed.

## 5. The first-child update that a hereditary analysis must retain

If the queried parent coordinate i has B_i=0, its adjacent Fourier coefficients never coexist. Each child's squared spectrum is exactly the pushforward p under deletion of i, independently of the physical branch. For any remaining j,

B_j(f_(i=+1))=B_j(f_(i=-1))=H(S_i,S_j | S_[n] minus {i,j}).          (P)

Indeed, at each residual label the allowed original atoms have at most one value of S_i for each S_j, so the conditional pair entropy equals the child's conditional entropy of S_j. This is a conditional-entropy update under a zero-erasure physical query, not a replacement of general block entropy by singleton sums. Other coordinate influences are preserved, H is preserved, and I loses exactly I_i. Formula (P) can expose positive erasure after a free query. It does not give a universal bound on those pair entropies.

The code checks both coordinate-0 physical children of every ledger parent, without assuming child transitivity, and uses parent/child entropy expressions as a second representation of B_0. The cyclic benchmark's minimum child prices are about 3.033739939 and 2.647247133. Recursive Maj3 depth two has positive minimum child price about 0.842929269 after one root-free query; the odd cyclic n=11 case has about 0.596501531 on either branch. Rational enclosures are in out/child_certificates.json. Its scope is one revealed coordinate. Full hereditary payment remains unproved.

The certificate engine reduces log2(v), for integer v>0, to k+ln(v/2^k)/ln2 with 1<=v/2^k<2. For z=(x-1)/(x+1), ln x is enclosed by 2 sum_(r=0)^47 z^(2r+1)/(2r+1) and that sum plus 2 z^97/[97(1-z^2)]. Each positive series term is rounded down at scale 2^140, charging 48 units upward plus an outward-rounded tail. ln2 is enclosed the same way. Positive interval division followed by outward dyadic rounding bounds each log2(v). Signed rational prime-log coefficients choose the correct lower/upper endpoints. Thus all reported ratio boxes and the finite maximum separation are exact certificates, not floating evidence.

## 6. Honest frontier

For C018, the first unsupported line remains a finite universal bound on min_relevant_i B_i/I_i at every unrestricted nonconstant residual. A positive B/H fraction is not a theorem paying B<=KI; root transitivity is lost under restriction; and the two transitive H/I->4 calibrations cannot be used to infer a universal B/H fraction. This run proves a singleton tribes identity and uniform errors, independently consumes A075's odd-family obstruction, and measures overlapping cyclic roots and their first children. It does not improve the unknown universal upper constant or prove FEI.

The shortest next mathematical action is to use the saved first-child profiles to formulate a restriction-stable payment for the **positive-erasure residual** rather than classify more roots. When the current root has B_i=0, use (P) to compute the actual newly exposed pair cost without any marginal-entropy surcharge. The key unpaid part is a universal influence charge for that exposed cost or a leaf reserve that pays it once. This directly targets the hereditary bottleneck required by C018/C019, rather than producing another independent class theorem.
