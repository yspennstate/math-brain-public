# Exact two-vacuum transport and scoped cumulative-budget review

All logarithms are base two. Finite uniform cubes and physical data queries only are used. A full reference, including its source-zero rows, is retained. Full FEI remains OPEN.

## 1. Frozen live candidate and review verdict

The reviewed statement is A050-CUMULATIVE-CORRELATED-RESET-BUDGET@1, SHA256 d24cb307a6bd1f20ff135868e18b1c273544908fd5ca7297294aeaa93d3059bb, in A050 run 20261023T042019Z-fleet03-A050-repair-with-scope. Its exact quantifiers and initial source are copied, unchanged, to out/REVIEWED_CLAIM.json. Review accepts its analytic sufficient-budget and paired-frontier clauses without repair. A046 supplied the earlier first-reset theorem, so this is a dependency contributor's reconstruction, NOT a fully independent review of the whole chain. A049/A092 remain suitable independent reviewers. A050's separate 302956 computational assertions have not been rerun here or accepted by count alone.

Here is a reconstruction of the load-bearing estimates. For an original width-r point sign, d=2^-r, v=4d(1-d), I=2rd. Its nonempty entropy is 8(r-1)d(1-d), while its empty entropy is at most v/ln2. The original matched-empty 1/8-spike law has KL at most v log(8/7). Subtracting their sum from 4I and dividing by four gives

    B_r=d(1-d)(2-1/ln2-log(8/7))+2r d^2.

The original full lifted source consequently has M0=4I(F)-CE(F,Q)>=1+2t+sum B_r. Each fresh reset generation of tilt alpha costs, before any inherited-KL refund, at most sum d(1-d)log(1/(1-alpha)). This follows from finite total variance, conditional inside every first stopping cell and then summed against its ORIGINAL reach. Two generations use two such costs; no variance bank is renewed.

For an activation J_s(g), direct pivots give I(J_s)=(1-s Eg)/2+I(g)/2. Erasure of its controller bounds H(J_s)<=2+H(g)/2. Thus 4I(J_s)-H(J_s)>=-2s Eg+(4I(g)-H(g))/2. At complete data frontiers in either sign, the mean of Eg is its entry mean. The two signed terms therefore cancel even for different physical policies. Point-tensor restrictions have H<=4I; b0 retains its weighted surplus one. Hence the complete terminal S>=1, without asserting nonnegative surplus at each individual terminal.

If sigma1,sigma2 are the ACTUAL signed full-reference changes, ordinary likelihood telescoping and entropy/influence algebra give

    S-[A0+e+sigma1+sigma2]_+=min(S,M0-sigma1-sigma2).

The stated cumulative condition makes the latter >=1; subtracting the ONE eligible old booking omega<=1/4 leaves >=3/4. It does not establish separate positive-part bounds for each reset.

For the advertised scopes, ln2>56/81 follows by taking the first two positive terms of 2 atanh(1/3). The integer inequality 22^56<2^31 15^56 then pays first1/7 plus second1/11 at every width/load. For two1/7 resets, 14^20<2^13 9^20 gives combined logarithm <13/20. Widths2..7 satisfy 31/56+2r/(2^r-1)>13/20. For arbitrary widths with lambda=sum d<=9, product(1-2d)<=1/(1+2lambda) implies 2t>=2lambda/(1+2lambda)>=2lambda/19; this exceeds the remaining 27lambda/280 excess. Every bound spends the ORIGINAL root margin. The checker verifies the integer/rational certificates separately.

## 2. New exact recurrence: two vacuum masses suffice

Let g be ANY finite Boolean sign with Fourier coefficients a_T and p_T=a_T^2. Fix s in {-1,1}, and J_s(x,z)=s on x=0, g(z) on x=1. Label its spectral controller bit c in {0,1}, so

    P(c,T)=(s 1_{T=empty}+(-1)^c a_T)^2/4.

Consider any complete normalized reference of the form

    R(c,empty)=V_c;
    R(c,T)=r_T/4 for T nonempty,
    V_0+V_1+(1/2)sum_nonempty r_T=1.

Require R>0 wherever P>0. The r_T may be positive on source-zero rows: they are NOT silently discarded. Every full matched-empty activation reset has this form. The statement also applies to arbitrary references of this form, without assuming a product or a point core.

Query data coordinate i. For physical sign b in {-1,1}, the restricted coefficients are a^b_T=a_T+b a_{T union i}, for T not containing i. Write p^b_T=(a^b_T)^2 and P_b(c,T) for the resulting selector spectrum. Define the actual coherent kernel as P_b(c,T)/(2E(c,T)) when E(c,T)=P(c,T)+P(c,T union i)>0, and 1/2 when E=0. The factor 2 is the FAIR physical outcome probability denominator. Transport R with this kernel, sum all its rows to get its own outcome mass Z_b, then normalize by Z_b.

This full operation closes exactly on the two-vacuum representation. Its UNNORMALIZED update is

    E_c=P(c,empty)+p_{i}/4,
    D_c=V_c+r_{i}/4,
    k_c=P_b(c,empty)/(2E_c) if E_c>0, else 1/2,
    V'_c=D_c k_c.

For every nonempty T not containing i, put

    k_T=p^b_T/[2(p_T+p_{T union i})] if denominator>0,
        =1/2 otherwise;
    r'_T=(r_T+r_{T union i}) k_T.

Then Z_b=V'_0+V'_1+(1/2)sum_nonempty r'_T; the normalized successor is (V'_0/Z_b,V'_1/Z_b,r'_T/Z_b). Positivity on actual support ensures Z_b>0. Induction proves closure under ANY finite adaptive data tree, with its actual sequential normalizers. Different a-sign branches may follow different trees.

Proof: at nonempty T, the two controller copies of both parent source rows equal p/4, so their erasure masses and kernels coincide. Their reference erasure masses equal (r_T+r_Ti)/4. At the vacuum, the erased singleton is nonempty and therefore contributes r_i/4 to EACH distinct vacuum mass. These are precisely the displayed updates. If an erased source mass is zero, both child source masses are zero, but the prescribed fair fallback still propagates any reference-only mass. This explains why deleting those rows or restoring the vacuum masses to their physical values would change Z_b and is invalid. No cumulative marginal-conditioning shortcut is used.

## 3. Exact reset price retaining both vacuum corrections

At any node let a prescribed replacement Q* copy the ACTUAL vacuum masses P(c,empty), and have Q*(c,T)=q*_T/4 for nonempty T. Require q* positive on nonempty actual support and sum_nonempty q*=sum_nonempty p. The full KL and reset increment are exactly

    Kold=sum_c P(c,empty) log(P(c,empty)/V_c)
           +(1/2)sum_nonempty p_T log(p_T/r_T),

    sigma_node=Knew-Kold
       =(1/2)sum_nonempty p_T log(r_T/q*_T)
          +sum_c P(c,empty) log(V_c/P(c,empty)).

Terms with zero source weight are zero, with no logarithm evaluated there. Reference-only masses still enter all prior normalizers. The two vacuum terms need not have a favorable sign separately. Neither may be dropped without an inequality. Reach-weighted sums of this identity compute a second FULL changed-profile reset against the SAME inherited law. This is the requested recurrence, NOT a proof that every such reset is affordable.

## 4. Known falsifiers and rejected numerical repairs

The campaign has already retired tax-free root taxes, O(p) point-entropy taxes, fixed Renyi shortcuts, and unpriced product-source conversions; none is reintroduced. Here the exact obstruction is the COARSE sufficient budget, not an actual Boolean counterexample. At width8, 14^8>2^5 9^8 gives log(14/9)>5/8, while 31/56+16/255<5/8. Thus dropping the original2t cannot certify two1/7 resets for all widths. The unchanged two1/7 ALL-width/ALL-load statement has neither been proved nor falsified. Changing second tilt to1/11 is a valid scoped theorem, not evidence that the unchanged1/7 theorem holds. Negative finite reset signs do not prove universal negativity. One cannot renew oldquarter, delete one activation branch, replace sequential transport by cumulative erasure, omit source-zero rows, or reset the vacuum for free.

The first unpaid local inequality is to control the COMPLETE reach-weighted formula in section3 after the first reset, outside A050's aggregate admissibility condition (not merely width>=8/load>9, since the condition can cover further mixtures). The universal unpaid line is still an influence-priced complete useful correlated INITIAL source for an arbitrary Boolean core.
