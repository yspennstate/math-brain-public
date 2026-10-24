# Root continuation — the one-count four-scalar Schur form

Status: exact change of variables in X050's retained one-count identity. The ENTIRE two-parameter square is now proved by X069, X074, X083, X084 and the analytic-plus-interval completion in ROOT_ONE_COUNT_CORNER_COMPLETION.md. The historical derivation below records the earlier partial domains. The extra parameter for nonorthogonal balanced columns and the unrestricted Lyons conjecture remain open. This root note is not an additional sub-agent.

X050 Appendix considers the entropy envelope retaining (N_A,X_3,X_4). At a balanced singular-basis cross block with C=2Z=diag(sqrt(r),sqrt(s)), 0≤r,s<1, it forgets only one Fisher score direction. A Hadamard on the first measured pair makes the envelope touch the actual entropy for C=2Z=2^(-1/2)[[sqrt(r),sqrt(s)],[sqrt(r),-sqrt(s)]]. The columns are orthogonal and individually balanced in the ORIGINAL measured coordinates, while their magnitudes may differ. This extends the target beyond X044's four-equal-entry-modulus condition. General nonorthogonal balanced columns have an additional determinant parameter and are NOT described by this two-parameter form; the retained B occupations do not permit an arbitrary right-unitary rotation.

Let a,b,e,f denote the four diagonal tangent entries, and set

    u=a+r e, v=b+s f,
    A=1-r², B=1-s², C=1-r²s²,
    R=atanh(r), S=atanh(s), D=atanh(rs),
    k=(1/2)log[C/(AB)].

The full dimer Fisher becomes 4u²/A+4v²/B+4e²+4f². The exact lost Fisher is 2(Bu-Av)²/(ABC). Substituting a=u-r e and b=v-s f in X050's complete logarithmic acceleration gives the remaining negative-entropy-curvature form q=(u,v,e,f) Q (u,v,e,f)^T, where the symmetric matrix has entries

    Q11 = 2(2C-B)/(AC),
    Q22 = 2(2C-A)/(BC),
    Q12 = 2/C-2k,
    Q13 = -2(R+sD),
    Q14 = -2(S-sk),
    Q23 = -2(R-rk),
    Q24 = -2(S+rD),
    Q33 = 4[1+rR+rsD],
    Q44 = 4[1+sS+rsD],
    Q34 = 2[sR+rS-D-rs k].

These entries follow by exact formal algebra from X050; no logarithmic bound, Fisher term, or acceleration has been removed. In particular the large diagonal Fisher terms become constants in the lower two coordinates, while all singular rational coefficients remain in the upper block. The hyperbolic substitution r=tanh(a), s=tanh(b) also gives D=[log cosh(a+b)-log cosh(a-b)]/2 and k=[log cosh(a+b)+log cosh(a-b)]/2. The proposed next target is Q≥0 on [0,1)², using a lower-block Schur complement or a common hyperbolic shift as in ROOT_HYPERBOLIC_SCHUR_COMPARISON.md. X069 gives the exact inverse-free sufficient comparison U≥TT^T and proves that a direct common-shift monotonicity of that reduced matrix is false. X074 instead pays the integrated logarithms by a positive radial Fisher expansion, proving U−TT^T≥(7/10)(r²+s²)I on 0≤r,s≤3/5.

At r=s, the two-count and one-count envelopes both touch the same equal-modulus law. Since the two-count envelope majorizes the one-count envelope, their touching Hessian comparison and X044 prove the one-count full Hessian sign there. At a vanishing singular value, X030 supplies relevant rank-one base identities. X074 now supplies that promotion on its proved square: the within-part complex sector is 4D|w−sqrt(rs)z|²+4(k−rsD)|z|²≥0; X037 supplies the cross-block sector and the physical involution removes their mixed Hessian. Thus the full sixteen-direction measured theorem holds for the stated orthogonal balanced-column family on 0≤r,s≤3/5. Any further square extension can reuse those sector and touching arguments. X050 explicitly records the full four-variable form from which this matrix is derived.

A separate numerical exploration found that linear occupation information by itself cannot be expected to close all balanced bases: for Z approximately [[0.258522507288+0.337510094914i,0.187286679347+0.135967814716i],[-0.078920362632+0.047944957360i,-0.015320219157+0.098565033911i]], the least eigenvalue of Σ⁻¹-C_alpha is approximately -0.292589. This is only a diagnostic failure of an auxiliary certificate, not an entropy counterexample or a rigorous sign certificate. It motivates retaining the nonlinear count residual above.
