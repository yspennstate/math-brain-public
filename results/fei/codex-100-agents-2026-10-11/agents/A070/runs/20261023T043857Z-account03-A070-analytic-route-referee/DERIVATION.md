# A070 stage7: independent private-tree review and literal-only completion

Full FEI remains OPEN. Entropies and complete cross entropies use bits; influence means ordinary physical pivotal probability. All references below are inherited frequency marginals, including at constant outputs.

## 1. Reviewed claim and original account

The source is A069-INHERITED-PRIVATE-STOPPING-WITHOUT-NEW-BANK@1, statement hash 782c00ee932ecbcb576235ab56925977a27f6988633ec33dfa987d79a6cbf2a6, DERIVATION Sections3-5 in A069/run20261023T034731Z. Its supplied post-core, post-u reference has, for N=2^m, t=N^-2 and d in {0,1},

    A=(1+3td)/4, B=5(1-td)/16,
    r=7(1-td)/(32(N-1)).

A and B belong to empty and {c}; every other frequency has mass r. After k distinct physical private queries the inherited marginal has A_k=A+(2^k-1)r, B_k=B+(2^k-1)r and remaining tail atom r_k=2^k r. This law is independent of the actual outcomes; only on a zero prefix does the actual function remain q2 or c*q2. Every actual restriction retains both children.

On that continuing prefix put M=2^(m-k), eta=1/M. The actual squared spectrum is ((1-eta)^2,eta^2) or the reverse at the first two atoms, and eta^2 at each other atom. Direct Fourier transformation of 1-2*1{c=0,Z=0} proves this, and the physical private influence is eta. Partial Parseval therefore gives exactly

    Delta C=p0 log2(1+r_k/A_k)+p1 log2(1+r_k/B_k)
            +eta^2 log2[(1+A_k/r_k)(1+B_k/r_k)]
            +2(M-2)eta^2.

This identity includes the complete stopped constant/literal child costs. It is not a reset to entropy zero.

## 2. Independent all-width reconstruction

The source ratio corridor is correct: L=8(M-1)/7 <= A_k/r_k,B_k/r_k <= U=1+10M/7. For d0 use initial ratios 8(N-1)/7 and 10(N-1)/7. Marginalization sends a ratio x to 1+(x-1)/2^k. For d1 the B ratio is unchanged and the A ratio equals 8(1+3rho^2)/(7rho(1+rho)), with rho=1/N. The inequalities 1-rho <= (1+3rho^2)/(1+rho) <=5/4 hold on 0<rho<=1/2: the lower one reduces to 4rho^2>=0, and the upper follows from 12rho^2-5rho-1 <=rho-1<0. Thus the corridor holds at every width and prefix.

Consequently Delta C is at most

    V_l=(1-2eta+2eta^2)log2(1+1/L)
        +2eta^2 log2(1+U)+2(M-2)eta^2.

The three l=1,2,3 boundary signs V_l<4eta are independently interval-certified. For l>=4, ln2>2/3, 1+U<=2/eta and division of (1-2eta+2eta^2) by 1-eta give

    V_l/eta <53/16+(2l-53/16)eta
                      +(21/16)eta^2/(1-eta)
             <=53/16+1/2+21/3840=4887/1280<4.

Here 2l/2^l<=1/2 and eta^2/(1-eta)<=1/240. Thus each permitted private query has strictly negative excess Delta C-4Inf. Any ordering among remaining private bits, chosen from actual past physical outcomes and stopped no later than first1, adds ZERO positive debit. The all-width theorem does not follow by extrapolating the finite certificates.

The supplied original nine-bit account has a once-earmarked5/8 owner at first core child Y0=0, original weight1/2. Prior positive booking is<3/5+1/512 after u. Therefore all private stopping frontiers keep the SAME remainder>59/2560. Negative excess is never rebooked as fresh money. For arbitrary Boolean paired cores the local theorem is conditional on their supplied reference and paid preceding account; no arbitrary-core admission follows.

The m2 unrestricted obstruction also holds unchanged. For d0 after first private outcome1 the function is constant. Before that query A=24/96 and r=7/96; afterwards A_1=31/96 and r_1=14/96. Querying the other private coordinate costs exactly log2(45/31)>1/2 with zero influence, since 45^2>2*31^2. Its original physical weight is511/1024. The already independently certified core positive bill P alone, plus (511/1024)log2(45/31), exceeds5/8. This refutes only that fixed-earmark unrestricted continuation. The source statement and hypotheses require no repair.

## 3. New terminal completion, without a reset or bank renewal

Run the private tree fully until first1 or exhaustion (rather than stopping sooner). At an exit after first1 the actual output is constant for d0 and a c literal for d1. At the all-zero exhausted leaf it is a c literal for d0 and constant for d1. Global signs are irrelevant to squared spectra and influence. Query c ONLY at literal leaves, and stop the constant leaves immediately.

At every such literal leaf let A_k,B_k denote its actual inherited empty/{c} masses; other surviving private atoms are still present. Its sole occupied spectral frequency is {c}, so its physical influence is1 and its exact decrement, using both actual constant children and the full c-marginal reference, is

    Delta C_c=log2((A_k+B_k)/B_k)=log2(1+A_k/B_k).

The original A/B is4/5 for d0. For d1 it is 4(1+3t)/(5(1-t)) <=28/15, since t<=1/4. Adding the same nonnegative quantity to A and B moves their ratio toward1. Hence at every terminal literal, 0<A_k/B_k<=28/15, and

    Delta C_c<=log2(43/15)<log2(3)<2<4Inf_c.

Each selected c query therefore adds ZERO positive debit. The complete physical tree now has only constant Boolean output leaves, still with all original sibling branches and all full inherited terminal cross entropies. For the original nine-bit source the SAME bank remains>59/2560 at every chronological expected-tree prefix. No pathwise reserve is asserted. For arbitrary paired cores this is conditional on the same preceding paid account as the reviewed private theorem.

Even a constant output may retain nonzero cross entropy: after a literal query each constant child has empty reference mass A_k+B_k, so its bill is -log2(A_k+B_k), not zero unless that mass is1. Early d0 exits already constant retain -log2(A_k). Uniformly these terminal bills are at most2 because A_k>=1/4. At an exhausted d1 leaf A_k>=1/4 as well. Literal-query constants have mass A_k+B_k>=A+B>=9/16. This explicit bound does not create unused ancestral capacity or pay a universal source-reference admission.

## 4. Indispensable hypotheses and the unpaid line

The algebraic CE-marginal identity is generic, but physical Booleanity identifies unit child norms, the two exact terminal types and the pivotal influence eta. Root L2 normalization alone does not justify these lines. The previously checked real pair a(y)=(3+4y)/5,b(y)=1 has child squared norms37/25 and13/25 and empty-control mass t/5 instead of t*Pr(a!=b). This stage does not claim a new real-spectrum certificate. The independent normalized degree-one control has H=log2(n), I=1 and nonconstant coefficient2/n in its square, so an argument using only normalized spectra cannot prove a dimension-free FEI inequality. The present conditional theorem uses the explicit Boolean point-event shape, not only normalization or a support functional. It consequently does not assert a universal gain stable under arbitrary pad-and-flip edits. Historical cyclic-law Addendum11.51 remains unavailable at source-complete witness scope; no fresh cyclic replay is claimed.

The first unsupported universal line remains: construct or select, for arbitrary Boolean cores, a justified reference and once-owned influence budget paying their cumulative positive physical core excess and any required source conversions while retaining every original terminal bill. Reaching constant outputs in the supplied flat private geometry does not prove this. The next mathematical action is to test the occupied-source ratio corridor BEFORE full core exposure, using the original source law and debits and both actual children. That directly attacks C024/C019 admission instead of enumerating more private widths.
