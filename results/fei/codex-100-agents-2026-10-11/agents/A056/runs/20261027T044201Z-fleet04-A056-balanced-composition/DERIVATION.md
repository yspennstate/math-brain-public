# Fixed-influence source test

All logarithms are base two. These statements concern reference cost, not a counterexample to FEI. The fixed-order Renyi obstruction is an established campaign baseline. The refinement here freezes balance and influence exactly, identifies the necessary and sufficient variable-exponent threshold, retains two full physical children, and supplies a cheap contrasting original reference.

## 1. Actual balanced Boolean family with exactly I=2

For each integer k>=2, set delta=2^(-k) and m=2(2^k-k). On m binary inputs let b_m=(-1)^(u_1 u_2+...+u_(m-1)u_m). Its Walsh coefficients all have modulus 2^(-m/2): the two-bit factor has four coefficients of modulus 1/2, and disjoint products multiply coefficients. Thus I(b_m)=m/2. Put h_m=y b_m on an independent sign y. Then h_m is balanced, all its 2^m nonzero coefficients have modulus 2^(-m/2), and I(h_m)=1+m/2.

Let A_k be the indicator that k independent guard signs are all +1, and let z be one more independent sign. Define

    f_k=(1-A_k)z+A_k h_m.

This is Boolean, balanced, and every input is essential. The z influence is 1-delta, the y influence is delta, each bent input has influence delta/2, and each guard has influence delta (the other guards pass with probability 2delta, and independent balanced z,h_m differ with probability 1/2). Therefore

    I(f_k)=1+delta(m/2+k)=2.                         (1)

There are three disjoint Fourier strata:

* One atom {z}, probability a=(1-delta)^2.
* M=2^k-1 atoms {z} union U, nonempty guard U, each probability delta^2.
* N=2^(k+m) atoms {y} union B union U, arbitrary bent B and guard U, each probability 2^(-2k-m).

They are disjoint because the third stratum contains y and not z. Their masses are a, delta-delta^2, delta and sum to one. In particular the empty atom is zero, so all references below are already empty-calibrated. Full Boolean convolution follows from the actual Boolean formula; it is also checked for all 256 Fourier shifts at k=2.

The exact entropy is

    H(f_k)=eta(a)+2+2k delta(1-delta),               (2)

where eta(a)=a log(1/a). Since a>=9/16>1/2, eta(a)<=1. The induction k<=2^(k-1) gives 2k delta<=1. Consequently H(f_k)<=4, and in fact H(f_k)->2. All denominators are positive; k>=2 gives m>=4, M>0 and N>0.

## 2. A sharp variable-exponent threshold

For 0<=q<=1 define a normalized power reference on the positive support only:

    R_q(S)=P(S)^q/Z_q,  Z_q=sum_(P(S)>0) P(S)^q.

At q=0 this is the uniform support law; zero-probability atoms are excluded. At q=1 it is P itself. Its true-law cross-entropy is

    CE(P,R_q)=q H(P)+log Z_q.                       (3)

The exact normalizer, with t=1-q, is

    Z_q=a^q+M 2^(-2kq)+2^[t 2^(k+1)-k].           (4)

The last exponent uses m+2k=2^(k+1); no high-degree multiplicity is dropped. Write E_k=t_k 2^(k+1)-k. Since q H>=0 and the last summand is positive,

    CE(P,R_(q_k))>=E_k.                            (5)

Conversely, if E_k<=B uniformly, then t_k<=(k+B)/2^(k+1), so eventually t_k<=1/2. For such k, a^q<=1 and M 2^(-2kq)<=2^(-k+2kt_k)<=1. Hence

    CE(P,R_(q_k))<=4+log(2+2^B).                   (6)

The finitely many excluded k have finite cost. Thus, for an arbitrary sequence q_k in [0,1], the source costs are uniformly bounded if and only if sup_k E_k is finite. This is stronger than the necessary statement q_k->1: its precise scale is

    1-q_k <= (k+O(1))/2^(k+1).

For every fixed q<1, E_k grows without bound, although I=2, Var=1, mean=0 and H<=4. Consequently ANY exponent policy depending only on mean, variance and total influence, whose value at (0,1,2) is strictly below one, fails a universal CE<=K I source bound. No continuity of the policy is assumed or used. Allowing q=1 evades this obstruction but returns the true-spectrum source; a universal O(I) price for that choice is precisely FEI. Policies using additional structural information or other reference families are not refuted.

## 3. Both physical terminal entropies and the original source remain

On disjoint copies X,Y, introduce a fresh physical sign s and set

    F_k(s,X,Y)=(1+s)f_k(X)/2+(1-s)f_k(Y)/2.

Both children are balanced and nonconstant with I=2. Independence and balance give Inf_s=1/2. Thus I(F_k)=5/2. Each positive child spectral atom has four disjoint root copies of probability P(S)/4: two copies for each data block, with and without s. Disjointness uses child balance; a shared empty atom would require recentering and this calculation would not apply. Therefore, for the SAME q,

    H(F_k)=H(f_k)+2,
    Z_q(F_k)=4^(1-q) Z_q(f_k),
    CE(P_F,R_(q,F))=CE(P_f,R_(q,f))+2.             (7)

The physical s query has actual outcomes 1/2,1/2. In each equal-magnitude Fourier pair, the physical kernel sends the X pair to the + child and the Y pair to the - child. The reference pair weights are R_(q,f)/4 on each root copy, so its outcome probabilities are also 1/2 and its normalized inherited children are exactly R_(q,f). There is no reset and no forgotten outcome normalizer. In particular the exact full-terminal bill is

    CE_root=2+(CE_child+ + CE_child-)/2.            (8)

Both complete terminal CE costs diverge for fixed q<1, while both terminal Shannon entropies remain <=4. The corresponding root exponent policy based only on (mean,Var,I) also fails if its value at (0,1,5/2) is below one. Equation (8) uses that root value at BOTH children; it does not silently choose a different exponent there. Already-spent debits and any bounded O(I_root) transport charge cannot repair an unbounded original source bill. The known v9 mark transport remains conditional on its original source and is not contradicted.

## 4. A cheap original reference explains the failure

Place reference mass 1/2 on {z}, mass 1/4 uniformly on the M guard-z atoms, and mass 1/4 uniformly on the N bent-activation atoms. Call this normalized law Q. It uses the explicit physical decomposition, not a global power normalizer. It supports all P-positive atoms. Its CE is exactly

    CE(P,Q)=a+(delta-delta^2)(2+log M)+delta(2+k+m).

Using log M<=k gives

    CE(P,Q)<=3+2delta-(k+1)delta^2<=7/2.           (9)

Thus this family DOES have an original influence-priced source (rate 7/4). On F_k use four disjoint Q/4 copies; this original reference has CE<=11/2, and its exact s-query ledger is again (8). No fresh descendant source is issued. This comparison isolates the defect: the global power normalizer charges the vast rare stratum to the common atom; the three-stratum prior retains the rare probability in the invoice. The same macro prior gives CE<=2I for the unrestricted balanced activation family with r>=1 remaining guards and any even m, by CE<=2I-1+2delta-(r+1)delta^2<=2I. That latter inequality is a root supplier statement, not permission to replace an inherited reference after each query.

## 5. Checks that could fail

The checks independently test Boolean signs, balance, all essential influences, all signed-convolution shifts, Fourier stratum multiplicities, and actual plus/minus selector amplitudes. The large cases use compressed exact powers, not enumeration. The power CE upper bound needs q>=0; the three-term normalizer upper bound eventually needs q>=1/2, derived from E_k<=B. The entropy bound uses k>=2. Physical four-copy disjointness needs balanced children. Q requires M>0 and no missing support. Neither q>1 nor dimension-aware structural priors are excluded. Dropping the normalization term in (3), deleting either full child in (8), or changing q at a child would invalidate the conclusion being tested.

## 6. Unpaid universal line

No rule selecting a bounded-cost decomposition/reference for every Boolean function is supplied. Full signed convolution identities hold on this family and do not justify a global power-source normalization charge. The useful next supplier must exploit a whole-set structural decomposition, retain its mixing normalizer, and pay that ORIGINAL mixture from unused influence. The v9 transport theorem, balanced composition baseline, and independent-review status are unchanged. The new statements have an analytic author proof plus exact finite checks; independent review is requested, not claimed. Only a separately named algebraic lemma is eligible for a Lean certificate.
