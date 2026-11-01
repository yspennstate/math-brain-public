# Independent reconstruction of A072's finite conserved account

The target is A072-BOOKED-PHYSICAL-OWNER-TRANSFER@1, statement SHA256
97aec4ae0b2c60a06945a0779a0f32f981a19c1d74bb83fec9d227501eced624.
Its finite scope and hypotheses are unchanged. Entropy is in bits. No universal FEI conclusion follows.

## A different spectrum derivation

Encode a negative inner output by binary X_i=1. Write the actual gate truth table
J(X) as sum_U D_U product_(i in U) X_i, where
D_U=sum_(V subset U) (-1)^(|U|-|V|) J(1_V).
Thus, with independent core negative probabilities p_i,

    b_T = sum_(U superset T) D_U product_(i in U\T) p_i,
    J(X) = sum_T b_T product_(i in T) (X_i-p_i).

The checker obtains D directly by inclusion-exclusion of the 64 truth values.
It does not compute the outer sign-Walsh transform or import any source code.
Orthogonality gives occupied-block masses

    mu_T = b_T^2 product_(i in T) p_i(1-p_i).

For every nonempty physical inner set A, the Fourier coefficient of X_i-p_i
is -g_i_hat(A)/2. Therefore the coefficient of a full physical set with occupied
block pattern T is b_T product_(i in T) [-g_i_hat(A_i)/2]. This proves both
normalization and the conditional independence of its nonempty inner sets.

Let v_i=4p_i(1-p_i), and let E_i be the entropy of the normalized nonempty
inner spectrum, defined as zero when v_i=0. Independently sum the actual outer
pivotal edges with their product probabilities to obtain q_i. The checker
establishes sum_(T containing i) mu_T = v_i q_i. Hence the full entropy and
influence, including constant-core endpoints, are

    H(F) = H(mu) + sum_i v_i q_i E_i,
    I(F) = sum_i q_i I(g_i).

This is the entropy chain rule conditioned on occupied blocks, rather than the
source implementation's signed composition-correction formula. To reconstruct
the source owners, set C=H(F)-sum_i q_i H(g_i) only AFTER computing H(F).
Every original retained core contributes. At p=0 or1 the occupied probability
is zero and no division by a zero variance is made.

For a uniform physical query, direct inner edges give d=q_i Inf_j(g_i).
Physical conditioning gives I(parent)-mean I(children)=d. The checker verifies
this rational identity, and verifies the affine conditional conservation of
all six q weights on every prescribed query. The third spine query is a dummy:
the actual restricted truth tables agree, so its entropy decrement and debit
are exactly zero, while both children retain reach 1/2.

## The conserved debit, without a reset

Let S=K I-H at K=9/2. Initially retain the two original full rate-4 excesses
e1 and e2. The first nonconstant child receives first-label debit 2e1; the
constant selected-core child receives zero but retains the other five complete
cores. At the second query let A4_b=q0 S4(g_child_b) and B4=mean A4_b.
Each old label is allocated in proportion to A4_b/B4, separately. Direct
certificates give B4>0, 2e1+e2<(3/5)B4, and the required positive other-owner
rate-4 margins on all four prefix children. The old labels are never replaced
by smaller rate-9/2 labels.

For each subsequent query define e=Delta H-Kd and B=mean S_child. The physical
identity gives B=S_parent+e. Every old label a is transported as a*S_child/B;
the new signed label is e*S_child/B. Conditional means of every old label are
unchanged. If the incoming total is D, then exactly

    S_child - (D+e) S_child/B = S_child (S_parent-D)/B.

All denominators B are separately certified strictly positive, and each actual
child S is certified positive. Signed credits remain signed. This identity is
algebra, not a deduction of child positivity. Our Lean core submission only
targets its cross-multiplied numerator identity over integers; the helper
returned RUNTIME_UNVERIFIED after its bounded timeout, so no Lean verification
is asserted.

For the distinguished original block0 define A=q0 S_K(g0), M=S-A,
T=max(0,-M), U=A-T, O=max(M,0). Then S=U+O. The transfer T pays the negative
other-owner margin before liabilities are split between U and O, proportionally
to their share of S. Each positive bank retains its proportional positive
remainder. Zero banks receive zero debit. Every relevant sign is certified;
there is no interval-dependent ambiguous choice of max branch.

Preserving the old rate-4 bookings has the exact conservative tax

    tax=(1/2)[d_root+(1/2)d_second] = 85117875/8589934592.

Telescoping across the seven true-reach terminals gives

    mean_terminal(S_terminal - all labels) = S_root-tax.

The first label has unconditional final mean e1; the second has mean e2/2.
All five untouched original q_i weights have their root value as the final
reach-weighted mean. These identities and the owner decomposition establish
that the bank is neither renewed nor counted twice.

## Exact finite conclusions and hostile checks

The unchanged zero-spine order is [2,0,1,3,4,5]. At tag00000* the transfer is
strictly between 1/10 and 11/100 and the remaining account exceeds 12/25.
The root mean remaining account exceeds 11/10. Display values only are
T=0.10167805493729..., target remaining=0.48426873795677..., and root remaining
1.11428436780538.... The exact rational endpoint certificates decide the signs.

Alternatively replace the LAST query by block1 coordinate0 at the same parent.
The queried core's two children have negative probabilities 1/16 and1/32, both
nonconstant. All old labels and the five stopped siblings remain. The full new
rate-9/2 excess is strictly positive (display 0.02240298723663...), and the same
allocation pays it with positive remainders in both complete children. This is
an alternative seven-terminal history, not an additional debit on the first.

Five explicit smaller physical functions (dimensions12,11,11,10,10) verify
10,240 Fourier coefficients by direct character bitsets, every physical edge
influence, and full spectral entropy. Both constant selected-core signs are
included. Inner spectra use direct integer characters. The gate polynomial is
inverted at all64 binary vertices. Rational checks include Parseval, influences,
all q transport identities, every original label and every final reach. Saved
source-state and old-label intervals are compared only after the independent
calculation; no source numerical output is used to generate the account.
Adversarial controls show that dropping a terminal loses probability mass and
resetting the rate-4 prefix loses the strictly positive tax.

For every positive rational log argument, dyadically reduce to y in[1,2).
With z=(y-1)/(y+1), use the first48 terms of
ln(y)=2 sum_(k>=0) z^(2k+1)/(2k+1). The remaining positive tail is bounded above
by 2z^97/[97(1-z^2)], since 0<=z<=1/3. Divide by the independently enclosed
positive ln2 and round outward to112 binary fractional bits. Powers of two
are exact. All further interval operations are rational with checked positive
division denominators. An overlap with zero is a diagnostic of identities
proved algebraically above, never an equality proof from floating arithmetic.

Verdict: independently ACCEPT the source finite claim at unchanged version,
statement, hypotheses and hash. No repair was supplied. The certificate rung
is an independently reconstructed finite exact certificate with a written
derivation; it is not Lean-checked, a universal FEI bound or a counterexample.

The first unsupported universal line is obtaining the positive full child S_K
capacities from inherited signed component banks for arbitrary retained cores.
Assuming those capacities for all Boolean children would assume FEI itself.
