# Independent adversary audit of w504's mathematical draft

2026-10-10. Independent obstruction was saved in w505/ATTEMPT.md before the paired draft was read. The audited packet is w504/PROOF.md, sections 1-4, and claims w504-P0162-C001 through C005. This audits the mathematical argument, not a previous review.

Verdict: KEEP the stated conditional reduction and family bounds; FIX one Fourier-sign sentence in section 3b. The general suitable-coordinate premise is still explicitly unproved. No full FEI proof is present or certified.

For notation, use n=2m for the number of base bits in w505's family; w504 calls that number m. Put rho=2^(-n), a=sqrt(rho), and R(u)=u^2 log_2(u).

The two parametrizations of the entropy identity agree exactly: w504's w_T equals w505's r_T; w504's q_T equals b_T^2/r_T; and w504's p_T equals (1+t_T)/2. Thus its extra term 1-h_2(p_T) is nonnegative and cannot be discarded in an upper bound. Parseval normalizes the branch law without assuming the Fourier index is independent of the branch. Zero-weight indices are omitted correctly.

The conditional induction uses one universal constant for all Boolean functions and dimensions. Each restriction is Boolean and has smaller dimension. The statement is sufficient, not a necessity assertion. A positive-influence coordinate is needed for the ratio; constants have entropy and influence zero. No missing closure assumption is used in the full Boolean class.

For the main family claim, derive the spectra independently from the two-bit transform. On the restriction b_j=1, the exceptional point is absent; the partner gives a parity and the remaining n-2 variables give a flat spectrum, so its entropy is n-2. On b_j=0 the remaining quadratic core has N/4 Fourier indices; its normalized Walsh coefficient magnitude is 2a. Its sign frequencies are (1+2a)/2 and (1-2a)/2, including the endpoint n=2 where the core has no variables. The zero-control block has coefficients 2a sigma-2rho; the other three blocks have magnitude 2rho. Their masses are 1-3rho and rho,rho,rho.

Let L_-= (1-a)^2 log_2((1-a)^2) and L_+=(1+a)^2 log_2((1+a)^2). The main full-function spectral block uses sign weights (1+a)/2 and (1-a)/2; the b_j=0 block uses (1+2a)/2 and (1-2a)/2. Subtracting their exact entropy expressions cancels the terms odd in sigma and yields

Delta_j(F)=2-(n/2)rho-[R(1-a)+R(1+a)]/2.

Since a<=1/2, the two arguments lie in [1/2,3/2], where R''(u)=(2 ln u+3)/ln 2>0. Jensen gives R(1-a)+R(1+a)>=0. Therefore Delta_j<=2-(n/2)rho<4(1/2+rho)=4 I_j for every base coordinate. This confirms C003 with all endpoint, coefficient-count, and constant checks. The family is not claimed closed under arbitrary restrictions; its root coordinate estimate is not substituted for a general induction hypothesis.

C004's independent direct proof also agrees with w505's earlier derivation: selector mass rho gives H<=n+h_2(rho), and I=n/2+(n+1)rho. The scalar bound h_2(rho)<=rho(n+log_2 e)<=2(n+1)rho gives H<=2I. This bound is a family result; independent referee w506 has so far kept the selector counterexample, not explicitly this positive bound.

The exact literal correction is needed in the sentence asserting that all three nonzero control blocks have coefficient -2t. Under w504's stated bit Walsh convention, the exceptional control point is (partner,z)=(0,1). The three Fourier coefficients for control indices (1,0),(0,1),(1,1) are -2t,+2t,+2t, respectively. Their squares are all 4t^2, so this correction leaves every subsequent entropy calculation and inequality intact. A minimal unified diff is in patches/01_w504_control_signs.diff; only w504 or the reviewer should apply it to that worker's file.

The remaining single hardest input is now precisely localized: for a fixed tau=1/16, find one finite K_0 such that every nonconstant Boolean function with max_i I_i<tau has a positive-influence coordinate with Delta_i<=K_0 I_i. The exact identity gives Delta_i<=2; if some I_i>=tau, that coordinate costs at most 2/tau. This is a correct localization of the sufficient selection lemma. The displayed family's base influences are at least 1/2 and therefore do not address the hard regime. Choosing the most influential coordinate is not justified in general and was already refuted in prior owner work.

Validation: verify_obstruction.py checks the exact Delta_j formula against all 20 base-coordinate restrictions of the four explicit truth tables m=1..4, plus scalar bounds through m=8. Finite checks corroborate the analytic derivation; they are not a proof for arbitrary Boolean spectra.

NEXT: Apply the narrow sign correction and attempt the fixed-tau suitable-coordinate inequality on Boolean spectra with all influences below 1/16.
