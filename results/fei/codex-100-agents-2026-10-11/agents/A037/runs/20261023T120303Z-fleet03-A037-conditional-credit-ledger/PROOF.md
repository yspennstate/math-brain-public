# Repeated whole-core spike replenishment exhausts an admitted original owner

Full FEI is OPEN. All inputs are uniform Boolean bits, all entropies and divergences are bits. This refutes one prescribed hereditary-reference mechanism, not FEI and not factor-only point refresh. External independent review is pending.

## 1. Actual Boolean family and prescribed source

For r>=3 put d=2^-r, wstar=e_0+e_1 in the private r-bit cube, and

    A_r(j,w)=1-2*1{w=0 OR (j=1 AND w=wstar)}.

On disjoint blocks define v=chi_z product_(i=1)^k A_r(j_i,w_i). The z character makes v and every restriction considered here balanced. Each block has influences Inf_j=d, Inf_wl=3d, hence

    I(v)=1+k(3r+1)d.

The full coefficient of a parent block is d, and the full coefficients of its j=0,1 children are -2d,-4d. The two private points have equal parity, which is essential to these amplitudes. Consequently after l queried j bits, with n0 zero and n1 one outcomes, the ACTUAL remaining-full spectral mass is

    m_h=4^n0 16^n1 d^(2k)>0.

The core references in this theorem are WHOLE-core mixtures q_alpha=(1-alpha)p+alpha delta_full. They are not products of per-block references. Since p(empty)=0 and p(full)>0, every prescribed reference is normalized, matches the empty mass, and has exactly source support. This includes all children and all histories. No ghost row or source-zero support is deleted.

Use F=chi_a at x=0, v at x=b=1, and +1 otherwise. Its ORIGINAL source Q0 is the usual four-copy correlated sector lift of the WHOLE-core q_(1/8): copy the six actual zero-data/controller masses, and put q(T)/16 on the four nonempty-data controller copies. In particular this is the original admitted nonpoint source, not an unpaid return from another canonical law.

Query b, retain b0, query a in b1, retain BOTH signs, and ACTUALLY reset both a-child references to the coherent lift of q_(1/6). This signed conversion is sigma1. Next query j_1,...,j_k in order in EVERY a child. After BOTH outcomes of EVERY query ACTUALLY reset the ENTIRE remaining core to the SAME-alpha1/6 whole-core law, retaining all other private bits and z. All controller masses are their actual child masses. Denote the total physically weighted later reset by sigma_later. This is replenishment after every generation, not a single conversion postponed to the end.

## 2. A positive normalized cost at every generation

Write beta=1-alpha and

    f_alpha(m)=(1-m)log2(1/beta)
               +m log2(m/(alpha+beta*m)).

This is the complete core KL D(p||q_alpha) whenever the full mass is m. Its second derivative is

    f_alpha''(m)=alpha^2/[m(alpha+beta*m)^2 ln2]>0.

At an unqueried j_i, the child full masses are 4m,16m and their erased average is10m. The coherent physical kernel at the erased full row is therefore (1/5,4/5). All non-spike reference mass follows the actual source; the controller-only sector of mass1/2 remains exact. The ACTUAL normalized reference outcomes on either a sign are

    r=(1/2-3alpha/20,1/2+3alpha/20).

At alpha1/6 these are19/40,21/40, independent of k,r,history and sign. Thus kappa=D(fair||r)=log2(400/399)/2. The complete compensated identity, including the erased KL and the reference's OWN outcome normalizer, gives

    sigma_h = kappa
       +[f_alpha(4m)+f_alpha(16m)-2f_alpha(10m)]/4
       > kappa >1/600.                              (1)

Strict convexity gives the first inequality; exact integers400^300>2*399^300 give the second. All old/fresh laws obey the prescribed support and spike location. This repeats A040's local rare-query computation on different, still-unqueried blocks inside ONE actual whole-core target. The new result is its complete-tree accumulation, not a new local witness.

Both activation signs are retained and have total reach1/2. At each generation all their physical children are retained, so these reaches STILL sum to1/2, even though individual histories are exponentially rare. Hence

    sigma_later > k*kappa/2 >k/1200.                 (2)

There is no factor2^-generation in the COMPLETE generation bill. A single-path analysis would miss the obstruction. No initial source, variance or query credit is renewed in this calculation.

## 3. Cheap original source and genuinely paid first reset

Take k=2^s, r=2s+8, s>=12. These are actual finite Boolean functions on n=1+k(r+1) core bits and n+3 wrapper bits. This symbolic family is never materialized at its large dimensions.

Balanced core sectors give EXACTLY

    I(F)=3/2+k(3r+1)d/4,
    H(F)=3+H(v)/4,
    A0=D(P_F||Q0)=f_(1/8)(d^(2k))/4.

The ORIGINAL inclusive headroom M0=4I(F)-H(F)-A0 therefore satisfies

    M0 <3+k(3r+1)d
       =3+(6s+25)/2^(s+8) <49/16.                  (3)

For all s>=1 the last rational term is at most its s=1 value31/512<1/16; its next/old ratio is (6s+31)/(2(6s+25))<1.

This source really is admitted before the attempted series. A block's principal mass is (1-3d)^2>=1-6d. Entropy of a distribution with tail mass tau and at most2^(r+1) atoms is at most h2(tau)+tau(r+1). Using tau<=6d, h2(tau)<=tau(log2(1/tau)+log2(e)), and log2(e)<3/2 gives H(A_r)<16(r+1)d. Thus

    H(v)<16k(r+1)d=(2s+9)/2^(s+4)<=33/65536<1/1024.

The bound decreases for s>=12. The exact first conversion is

    sigma1=[f_(1/6)(d^(2k))-f_(1/8)(d^(2k))]/4>0,
    A0+sigma1=f_(1/6)(d^(2k))/4
              <=log2(6/5)/4<11/160.

The coherent b/a sector transport has fair outcomes and carries the initial whole-core law unchanged before that conversion. Thus M0-sigma1>3-1/4096-11/160>2. This is an actual first reset with its old source debit retained, not a hypothetical fresh bank.

At the first reset frontier the complete S=4If-Hf is greater than2-H(v)/4>2-1/4096. The original signed recovery after a genuine old booking0<=omega<=1/4 therefore leaves more than7/4-1/4096. This compares with A040's one-query payment on a different family/frontier; the new failure concerns the later unbounded sequence, not a reversal of that one-query result.

## 4. Complete terminal references and exact owner exhaustion

Every final core is still balanced and retains the z character, so I(core)>=1. Each block is now a one-point or two-point private defect with principal mass at least(1-4d)^2>=1-8d. The same tail-entropy bound gives H(block)<16rd. Hence every complete terminal core has H(core)<16krd<=1/2048 for s>=12. Its coherent a child has H=2+H(core)/2 and I=1/2+I(core)/2, so surplus4I-H>2-1/4096. The untouched b0 has surplus2 and reach1/2. Therefore the COMPLETE final S>2-1/8192>0. Both signs, all2^k histories, every entropy and every full reference KL are retained symbolically.

Common-kernel telescoping with EVERY actual reset is

    A0+sigma1+sigma_later
      = cumulative erased KL + cumulative outcome KL + final full KL.

With e=H0-Hf-4(I0-If), the SAME signed account is

    S-[A0+e+sigma1+sigma_later]_+
      =min(S,M0-sigma1-sigma_later)
      <49/16-2^s/1200.                              (4)

For s=12 this is -421/1200, and the deficit grows unboundedly with s. The SAME old omega only worsens it. Thus an actually admitted original source that pays the first reset cannot pay arbitrary repetitions of this prescribed whole-core refresh, even if there were no old booking. This is stronger than the local sigma/Inf divergence: it rules out repairing that rule solely by appealing to a bounded unused ancestor margin.

The initial H(F)/I(F) tends to2. This is NOT an FEI counterfamily. It is a counterfamily to unlimited SAME-alpha WHOLE-core full-spike replenishment from the original supplied source. It does NOT refute point-factor-only refresh, the monotone-profile theorem of our previous stage, a different reference supplier, or keeping posterior references without replenishing the spike. Those scopes differ explicitly.

## 5. First unsupported universal line and mechanism change

The local sign extension failed on A047/A039; the local influence-price extension failed on A040; the unrestricted ancestor-payment repair now fails on (4). This is the third substantive failure of the WHOLE-core full-spike hereditary mechanism, so it must not be resumed under renamed credit. A factor-aware source on this tensor may work because its spike mass is tied to each rare block rather than to the forced balanced character; that is a different reference, and any conversion from an already owed source must still be paid.

The universal first unsupported line is an influence-priced arbitrary-Boolean initial reference with hereditary normalized transport/payment that does not repeatedly replenish a constant spike on rare queries. The prior residual R=V(Lstar-L) remains a valid conditional no-respending lemma; this fixed-profile replenishment is not a monotone consumption of that bank. NEXT should expose a block-aware supplier or prove that necessary resets can be avoided, while keeping an actual original owner and all terminals. Full FEI and the universal constant remain unchanged.
