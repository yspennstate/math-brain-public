# One original account pays a concrete coherent-profile conversion

All laws are normalized squared Walsh spectra on finite uniform cubes; entropy and KL use base2. This is an author proof, independent external review pending. It does not prove full FEI.

## 1. Universal finite-label conversion interface

Let C_j(y)=1_{L(y)=j} partition an independent control cube, and let Boolean g_j(x) share arbitrary data. Write c_j(U)=hat C_j(U), b_j(t)=hat g_j(t), pi_j=E C_j, and F(y,x)=g_{L(y)}(x). The actual joint law and an explicitly prescribed incoherent reference are

 P(U,t)=(sum_j c_j(U)b_j(t))^2,
 Qinc(U,t)=sum_j c_j(U)^2 b_j(t)^2.

Both normalize to1. Indeed sum_U c_j(U)c_k(U)=E C_j C_k=0 for j!=k, and sum_U c_j(U)^2=pi_j. Therefore their common data marginal is q(t)=sum_j pi_j b_j(t)^2. Qinc keeps all its mass, including rows where P vanishes. It has positive mass wherever P does.

For q(t)>0 this is a change only of the conditional control profile: true k=P/q is changed to ell=Qinc/q. The exact conversion bill is

 C=D(P||Qinc)=sum_t q(t)D(k(.|t)||ell(.|t)).                 (1)

If k_t is the number of source indices with b_j(t)!=0, Cauchy gives P(U,t)<=k_t Qinc(U,t). For each positive-q row its conditional KL is nonnegative and at most log2(k_t). Thus

 0<=C<=sum_t q(t)log2(k_t)<=log2(number of sources).        (2)

This proof uses no FEI assumption and allows shared source data, signs, cancellation, empty rows and zero-probability labels. Remove identically zero indicators when counting sources if desired. For L=2^k equal-probability address labels and all sources the same Boolean g, F=g, while Qinc(empty,t)=P_g(t)/L. Hence C=log2 L exactly. Dropping this conversion bill, even for a dummy controller, is false.

Equation(2) pays a specified reference conversion only. It does not bound the full terminal cross-entropy H(F)+C by influence for arbitrary Boolean inputs. In particular C=0 for a one-label controller leaves the entire FEI problem on its source.

## 2. The previous rare-label bent family

Use exactly A030@3's controller: even r>=4, epsilon=2^-r, t=2^(-r/2), g(z)=(-1)^(sum z_(2j)z_(2j+1)). At s=0 choose label1 for g=+1, label2 otherwise. At s=1 relabel only z=0 from1 to0. All coordinates are actual physical bits. The label probabilities are

 pi0=epsilon/2, pi1=(1+t)/2-epsilon/2, pi2=(1-t)/2.

Let v be the two-bit point defect (1,1,1,-1), and M be three-bit majority. At the ROOT the independent source blocks are a*v, M, b*v, with two fresh fair tags a,b. Every source has mean0 and entropy2. After querying a and b, the outcome (+,-) of reach1/4 has sources v,M,-v, the exact unequal-mean obstruction in A030@3. All four tag outcomes are retained.

At that selected node, private nonempty Fourier sets identify a unique source. Their terms in(2) vanish. Only the empty private set is shared, and only by sources0 and2, both of mean magnitude1/2. Its actual mass is

 qvac=(pi0+pi2)/4=(1-t+epsilon)/8 <1/8,                    (3)

because epsilon=t^2<t. Thus the prescribed conversion to Qinc costs

 C<=qvac<1/8. A sharper bound also retains the rare-event scale. On the vacuum row put x=c_0/2, y=-c_2/2. Then P=(x+y)^2, Qinc=x^2+y^2, so

 (P-Qinc)^2/Qinc=c_0^2 c_2^2/(c_0^2+c_2^2)<=c_0^2.

Only rows with s absent can have c_2!=0. On those EXACTLY2^r rows c_0=epsilon/2, hence the full chi-square divergence is at most epsilon/4. The elementary ln u<=u-1 and normalization imply D(P||Qinc)<=chi-square/ln2. Since ln2>2/3 (the strict midpoint bound for integral_1^2 dx/x),

 0<C<3epsilon/8=(3/4)Inf_s(F). Its ROOT cost C/4<3epsilon/32<=3/512. (4)

All other tag outcomes retain their complete true spectral reference. The selected conversion changes actual conditional control rows wherever the coherent law differs from the incoherent sum; it is not just an empty/nonempty scalar renaming. For example at U=empty, coherent amplitude is(pi0-pi2)/2 whereas Qinc mass is(pi0^2+pi2^2)/4. Both pi0,pi2 are positive, so these differ strictly. KL is strictly positive, since the normalized laws differ.

## 3. Explicit admission from ONE original rate4 quota

This section supplies a real owner for the conversion. It does not spend the cut slack or frontier J. At the original balanced tagged root the private nonempty spectra of the three sources are disjoint. The actual spectrum is the disjoint union of source-labelled products. Consequently

 Hroot=H(pi)+sum_j pi_j H(c_j^2/pi_j)+2 <= r+5,            (5)

using H(pi)<=log2 3<2 and the r+1 control coordinates. No source cost is dropped: the final2 is the average full source entropy.

Every distinct source output pair disagrees with probability1/2, because the independent sources have mean0. Each z_i has label-disagreement probability1/2+epsilon: the bent baseline has pivotal probability1/2, g(0)=g(e_i)=+1, and the relabelling adds rather than removes the two endpoints at s=1. Therefore

 I_controls=r/4+(r+1)epsilon/2.

Source influences are2,3/2,2 (tags count as real data coordinates). Their contribution is 2-pi1/2=7/4-t/4+epsilon/4>=27/16 for r>=4. Thus

 Iroot>=r/4+27/16, and U:=4 Iroot satisfies U-Hroot>=7/4. (6)

Set ONE old unrelated debit b=1/4 at the root. It stays booked. From(4)--(6), the full cost after both tag queries and the prescribed selected reset satisfies

 b + old entropy path + E full terminal CE
 = b+Hroot+C/4 < U-765/512.                              (7)

The reserve765/512 comes from 7/4-1/4-3/512. It is a guaranteed unused part of the original U, not a child rate4 reissue, new JS allowance, or positive-part cut reserve. Tags, all four histories, and both physical children at every query remain in the cost. Earlier A030@3's bad E/Inf_s is unchanged; this is a different, explicitly funded global account.

## 4. Every later physical no-reset continuation keeps the CURRENT reference

Start with the true spectral reference P at the root. It transports to each actual true child under the actual-phase channel. For a physical query, take each Fourier pair of real amplitudes a,b. On the pair's merged index its outcome kernel is

 K_s=(a+(-1)^s b)^2/[2(a^2+b^2)],

and K_s=1/2 if both amplitudes vanish. Transport ALL reference mass using this same kernel. Normalize each reference child by its own outcome mass rho_s, not the physical1/2. Support positivity is preserved, rho_s>0, and true outcomes are fair. KL disintegration/data processing gives

 D(Pparent||Rparent)>=average_s D(Pchild_s||Rchild_s)
                         +D(Bernoulli(1/2)||rho).         (8)

The omitted conditional-pair erasure divergence is nonnegative; no actual refund is counted as a new bank. Combining(8) with the exact entropy decrement shows

 CEparent>=DeltaH+average CEchild.

Telescoping preserves(7) for EVERY finite adaptive physical stopping tree after the selected conversion, with the current changed reference inherited thereafter. This includes later source and controller queries, even the locally expensive s query. Full terminal CE, original debit and all prior releases are retained. There is no second reset for free. The unchanged sibling branches likewise retain full true-reference terminal bills.

## 5. What this closes and the first unsupported line

The universal conversion bound(2) provides a phase-independent conditional-profile target with a concrete cost. The all-r tagged example pays one genuine conversion and every later no-reset mixed physical history at the SAME original rate4, old debit1/4 and reserve>765/512. This answers the prior stage's next question on this exact obstruction without pretending its zero cut slack can fund the transaction.

With the chosen exact source references R_j=P_j, W_root=0 and inherited Z=0, including after the tag exposures. Yet C>0. Hence payment from Z alone is impossible here; eligibility is explicitly from unused ORIGINAL admission surplus(6). This is a required failure control, not a contradiction of A029@2's sufficient condition C<=Z. Its references and eligibility hypothesis must be retained.

The first unsupported universal line is an influence-priced initial full source/structural admission U for every Boolean input. The general log-label conversion cost does not supply that admission; setting one label already includes arbitrary source FEI. A second externally prescribed conversion must likewise use the already diminished account and the currently changed reference, not reset to true profiles for free.
