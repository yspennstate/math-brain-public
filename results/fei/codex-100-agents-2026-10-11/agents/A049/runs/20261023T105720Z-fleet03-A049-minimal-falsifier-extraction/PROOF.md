# Minimal same-support reset obstruction, uniformly in the tilt

All functions are Boolean signs on finite uniform cubes. Entropy and KL are in bits. This refutes a reference-refresh sign assertion; full FEI remains OPEN.

## Exact circuit and reference

Let g(a,b,c)=-1 exactly when a+b+c=1, with bits in {0,1}. Its little-endian truth table is

    (1,-1,-1,1,-1,1,1,1).

Its Walsh coefficients, in mask order, are (1,-1,-1,1,-1,1,1,3)/4. Its three coordinate influences are each3/4. For 0<alpha<1 define the full-essential-block rule

    q_alpha(0)=p_g(0),
    q_alpha(T)=(1-alpha)p_g(T)+alpha(1-p_g(0))1[T=FULL], T!=0.

Constants and characters use their exact spectral laws. Thus the law is normalized, strictly positive on source support, and matches its empty mass. Query a and keep BOTH children. The a0 child is parity2 and the a1 child is a point defect on2bits. The coherent kernel at erased frequency T is p_child(T)/(2p_erased(T)); reference-only source-zero rows use1/2. Normalize each inherited reference by its OWN actual outcome mass.

For the pure core the inherited point-child law is

    (1/4,(1-alpha)/(2(2-alpha)),(1-alpha)/(2(2-alpha)),
      (2+alpha)/(4(2-alpha))).

The fresh point-child law is (1/4,(1-alpha)/4,(1-alpha)/4,(1+2alpha)/4); the other child is exact. Hence the physical average reset price is

    sigma_core=(1/8)log2[4(2+alpha)/((2-alpha)^3(1+2alpha))]>0.

The numerator minus denominator equals alpha^2(18-11alpha+2alpha^2)>0. At alpha1/2 this is simply (1/8)log2(40/27)>0. This part reconstructs A047's existing all-alpha core certificate; it is not a new core counterexample.

## Complete coherent activation

For either s=+/-1 let J_s(x,a,b,c)=s when x0 and g(a,b,c) when x1. Its exact truth table is obtained by interleaving s and the above eight entries. The reference copies BOTH actual zero-data masses (s+Eg)^2/4 and (s-Eg)^2/4, and puts q_alpha(T)/4 at each of the two controller copies of every nonempty T. No vacuum mass is restored during transport.

Query a, normalize the actual inherited laws, and replace both children by fresh laws with the SAME alpha and the same activation rule. Define

    A=1-alpha/26, B=1-alpha/10, C=1+alpha/2,
    D=1+2alpha, z=14alpha/65.

Direct erasure of the16 spectral atoms gives erased Q/P ratios A,B,1-alpha,C with source weights13/32,5/32,1/8,5/16, respectively. The reference outcome masses are (1+z)/2,(1-z)/2. Changing s swaps the two vacuum rows and preserves the answer. The average fresh-child KL is

    -(1/8)log2(1-alpha)-(1/16)log2 D.

The exact query chain gives average inherited KL = D(P_erased||Q_erased)-D(uniform||reference_outcomes). Consequently the two log(1-alpha) terms cancel in new-minus-inherited KL, leaving

    sigma_alpha=(13/32)log2 A+(5/32)log2 B
                +(5/16)log2 C-(1/16)log2 D
                -(1/2)log2(1-z^2).                         (1)

All outcome, vacuum and child terms are included. The exact replay obtains (1) directly from full truth tables and normalized child distributions; it does not assume the erased formula.

## New continuum certificate and quantitative obstruction

Put L(alpha)=32 ln(2) sigma_alpha. Differentiating (1),

    L'=10/(2+alpha)-4/(1+2alpha)-13/(26-alpha)-5/(10-alpha)
       +6272alpha/(4225-196alpha^2).

The first four terms equal

    alpha[(11-2alpha)/((2+alpha)(1+2alpha))
          -(1/2)(1/(26-alpha)+1/(10-alpha))].              (2)

For 0<=alpha<=1, the first fraction in (2) is at least1: numerator minus denominator is (1-alpha)(9+2alpha)>=0. The subtracted half-sum is at most (1/2)(1/25+1/9)=17/225. The final term of L' is nonnegative. Therefore

    L'(alpha)>=208alpha/225,
    L(alpha)>=104alpha^2/225,
    sigma_alpha>=13alpha^2/(900 ln2)>0, 0<alpha<1.          (3)

We used L(0)=0 and integration of an explicit continuous rational derivative. This proves strict positivity at EVERY allowed tilt, extending A047's activation sign at alpha1/6 to the entire interval. Near alpha0 the exact leading coefficient is L''(0)/(64 ln2), where

    L''(0)=-13/676-1/20-5/2+8+6272/4225>0.

No asymptotic expansion is needed for (3). At alpha1/6, exponentiating32sigma gives the single rational certificate

    K=(155/156)^13(59/60)^5(13/12)^10
       /[(4/3)^2(1-(7/195)^2)^16]>1.

Its reduced integer numerator and denominator, and all incoming/fresh child atoms, are in out/CHECK.json. Integer cross multiplication checks the sign. The continuum proof, rather than a finite grid, establishes the universal alpha quantifier.

## Minimum dimension within this declared rule

Every Boolean core on at most2bits is a signed character/constant or a signed point defect on2bits, with possible dummy variables. A character/constant has q=p, so coherent transport is exact and reset cost is zero. A2bit point defect, after any essential physical query, has only constant/character children. Fresh references are then exact, including their activation lifts. Its reset cost is minus the average complete inherited KL and is nonpositive. Dummy queries transport an unchanged law and cannot give a positive price. This proves nonpositivity for EVERY alpha in(0,1) at these dimensions. The separate FWHT classifier exhausts all22truth tables at dimensions0,1,2 and all26essential coordinate queries.

Therefore3core variables are minimal for a positive pure-core reset and4total variables are minimal for a positive activation reset within this full-essential-block same-alpha rule. The dimension assertion allows global signs, arbitrary truth tables, all essential queried coordinates, and the stated constant/character convention. It says nothing about other reference suppliers or minimal FEI falsifiers.

## Scope and first unsupported line

This is a complete truth-table certificate and rigorous sign comparison for a false hereditary nonpositive-reset assertion. Both old and fresh supports agree with actual source support. Smaller positive tilt, shared support, and matched vacuum mass do not repair that assertion. The first unsupported universal line remains payment of these positive arbitrary-Boolean reset prices from the SAME unused original source budget, retaining prior resets, the old quarter, both children, and all actual outcome/erasure terms. An influence-priced useful initial correlated supplier for arbitrary Boolean cores is also missing. This result neither refutes FEI nor resolves the separate all-width/all-load point-tensor two1/7-reset budget gap.
