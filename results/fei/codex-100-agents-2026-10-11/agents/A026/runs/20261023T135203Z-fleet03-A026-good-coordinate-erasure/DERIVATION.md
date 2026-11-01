# Vacuum shielding: influence-priced nonempty DATA-row floors

Bits throughout; author proof, external review pending. Full FEI OPEN.

## 1. Supplied canonical interface
Use A029@4's independently supplied source/controller interface. For F=A+aD=(1-c)G+cH, p=Ec, V=Var(a), gamma=Pr(G!=H), let q=(1-p)PG+pPH, r=(1-p)RG+pRH, W=(1-p)KL(PG||RG)+p KL(PH||RH), Z=W-KL(q||r), Da=KL(Pa||Ra), Cvac=KL(Bern(V)||Bern(1-Ra(empty))). Then T=W+gamma Da and S=Z+gamma Cvac are nonnegative and the canonical complete reference Qstar, with true DATA-row empty/nonempty odds k_t and inherited nonempty controller shape B=Ra conditioned nonempty, has KL(PF||Qstar)=T-S. All source/controller references are supplied once and physically inherited through their OWN phase channels. T is a supermartingale under either physical query type. This follows separately from source/controller KL contraction, gamma harmonic on DATA, and p harmonic on controls. No universal influence-priced supplier is assumed proved.

## 2. New admissible target class
In the empty DATA Fourier row t=empty choose any real lambda_t in[1/2,2] and set ell=lambda k/[1+(lambda-1)k]. In EVERY NONEMPTY occupied DATA row choose any real epsilon_t in[0,1/16] and set ell=(1-epsilon)k+epsilon/2. Keep the same r and B. Zero-true rows retain the canonical empty-index completion and all reference mass; if no nonempty controller shape is defined, require no odds change. Targets can be chosen adaptively and changed repeatedly, including signed returns.

The complete target KL excess is C=sum_t q_t KL_Bern(k_t||ell_t). A029's scalar log identity bounds the empty-row part by q_empty k_empty/2<=eta/2, where eta=V gamma. For a nonempty row, the WHOLE target conditional reference is at least(15/16) its canonical reference, so its excess is <=q_t log2(16/15)<q_t/8. The last strict inequality is certified by16^8<2*15^8. Therefore

 C <= eta/2 + (1/8) sum_(t nonempty) q_t
   <= eta/2 + J/8 =: E,

where J=I_DATA(F)=(1-p)I(G)+p I(H). The second inequality follows from sum_nonempty q=(1-p)Var(G)+p Var(H)<=J by Parseval/Poincare. No independence between G and H is needed. Crucially the mixture can create positive nonempty-controller reference probability on a row with k=0; bounded relative odds cannot do that.

## 3. One original physical-energy envelope
J is a physical supermartingale. At DATA query j its release is EXACTLY I_j(F); at CONTROL query its release is0. Eta is harmonic on DATA and its CONTROL release is gamma ahat({j})^2. Consequently E=J/8+eta/2 is a supermartingale, with explicit release I_j(F)/8 on DATA and gamma ahat({j})^2/2 on controls. Moreover eta<=I_CONTROLS(F), hence E<=I_DATA(F)/8+I_CONTROLS(F)/2<=I(F)/2. This is one original influence-priced allowance, not a renewed descendant grant.

Define Tnew=T+E and Snew=S+E-C>=0. Exact target KL is Tnew-Snew. On EVERY finite adaptive mixed physical tree,

 physical entropy path + average terminal full CE
 = Hroot+Tnew_root - sum_nodes w (Tnew_parent-average Tnew_children)
                         - average_leaf Snew
 <=Hroot+Troot+Eroot.

CURRENT odds-changed output references are physically inherited first at every query. If a child is reconstructed canonically, its signed raw reset cost is included; erasure and output-normalizer KL refunds reconcile the raw reset ledger with the displayed endpoint expression. Raw positive parts are not bounded by E and are never summed in its place. All siblings and complete terminal references are retained. Default fair true-zero completions are used, matching A029's interface; A026@5 structural completions are not silently substituted.

Thus a supplied original H+T admission receives an OPTIONAL surcharge<=I/2, just as A029's smaller relative-odds class, now covering unbounded relative odds on nonempty DATA rows. This is not free inside a tight pre-existing K account. SAME-budget use must exhibit actual unused original admission.

## 4. Literal old prefix at SAME rate4
Use A029's common-character family F_m, m>=1: controller a negative at points0,1,2 of3bits, shared g negative only at000, h negative at popcount>=2, both multiplied by chi_m. Original sources uniform, U=4I(F_m), old unrelated debit1/8. Query shared DATA x0 and retain BOTH prescribed children. In child1 retain the already-paid theta1/8 controller shape B, with first cost C1<1/128. Query controller y0 and retain the literal first epsilon1/16 odds conversion in its child0, with sibling epsilon0. This changed row is the common-character DATA atom, which is NONEMPTY for m>=1. All other affected true rows have k=1/2. Hence the literal A029@3/@4 prefix belongs to the new class.

At the selected first-DATA child, J=m+3/8, eta=45/64, E=m/8+51/128. The original physical-source interface and both initial terminal references give

 payment <=Hroot+Wroot+(C1+E)/2
         <Hroot+Wroot+m/16+13/64.

Since Hroot<=6, Wroot<=m+3 and Iroot=m+29/16, the SAME original quota after old1/8 retains

 U-1/8-payment >47m/16-133/64 >=55/64.

This pays arbitrary further mixed histories of the new class, including the FIRST odds conversion, its signed later returns and every full terminal. The new envelope is booked from unused ORIGINAL WHOLE quota, not spent child Z. The smaller55/64 margin pays a larger class than A029's relative-only121/128 floor; rates and old debit are unchanged.

## 5. Exact outside-image, unbounded-relative-odds witness
Let delta=2^-n, a=y balanced dictator, G=z, H=z b_n(w), where b_n is negative only at0^n and z is a fresh DATA dictator. Supply exact source/controller spectra, so T=S=0 and source posteriors alpha=rho at every occupied row. Consequently A028@9's same posterior-channel image contains ONLY the true conditional profile: any changed target here is outside it.

At NONEMPTY DATA row {z}, q=1-2delta+2delta^2 and k=delta^2/q. The floor target epsilon1/16 has ell=(15/16)k+1/32. Its effective relative factor ell(1-k)/[k(1-ell)] tends to infinity; already for n>=3 it is>=49/19>2. Therefore it is outside A029's bounded relative-odds target class as well. For n>=4 the exact lower bound from binary KL curvature is q KL_Bern(k||ell)>27783/16777216>1/1024. Both source functions are nonconstant. The original energy E=(1+n delta)/8+delta/2 pays the full cost, and E<=I(F)/2 with I=1+(n+1)delta.

The DECLARED stopping-reference class requires every occupied NONEMPTY DATA row to have odds in[1/32,31/32]. This target enters it. The initial exact reference fails it on row{z}; every reference with the SAME row marginal and nonempty shape satisfying that class has excess at least q KL_Bern(k||1/32)>0, since k<1/32 and KL increases beyond k. For n>=4, q>=7/8, k<1/224 and binary KL>=2(parameter gap)^2, so this necessary cost exceeds (7/4)(1/32-1/224)^2=63/50176>1/1024. The KL lower bound follows from true-parameter curvature>=4/ln2>4 and Taylor's theorem. That is a necessary conversion for this explicitly declared class, not a proof that FEI requires that class. Tensoring a common character moves A029's unpaid vacuum floor to a nonempty row, but adds the real DATA influence that pays it; this is physical energy, not a relabeling for free.

## 6. Honest universal gap
The new theorem prices the extra row-odds liability, not Hroot+Troot for an arbitrary Boolean core. Vacuum fixed-strength floors still fail a universal influence price on the unlifted point family. Eligibility of the declared floor class as a useful universal stopping class is not proved. No universal C018 selection constant, all-coordinate B bound, or full FEI proof follows. NEXT: supply an influence-priced ORIGINAL full reference for an arbitrary indecomposable core compatible with this mixed-query account, or prove a necessity obstruction for its unavoidable vacuum conversion. Another reset sweep inside the newly paid class is closed and should not be repeated.
