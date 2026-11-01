# Global affinity envelope without an atomwise floor

Bits throughout; full FEI remains OPEN. This is a conditional ancestor-account theorem.

## 1. Exact scalar certificate and separate exhaustiveness theorem

For any two normalized finite laws p,q put M_i=(p_i+q_i)/2 and t_i=(p_i-q_i)/(p_i+q_i), ignoring zero-denominator atoms. Set V=sum M_i*t_i^2 and a=sum sqrt(p_i*q_i). Then sum M=1, sum M*t=0, 0<=V<=1, and a=E_M sqrt(1-t^2).

The elementary inequalities 1-z<=sqrt(1-z) for0<=z<=1 and Jensen for the concave square root give the SHARP global envelope

    1-V <= a <= sqrt(1-V).

For V<1 this is equivalently

    -(1/2)log2(1-V) <= -log2 a <= -log2(1-V).       (1)

No atomwise relative-discrepancy bound is required. At V=1 both laws have disjoint supports and a=0, so the cost is infinite. On the mean-variance domain V<=1/2, convexity and the endpoint chord of -log2(1-V) imply

    -log2 a <= 2V.                                (2)

The constant2 is sharp: p=(1-v,v,0), q=(1-v,0,v) have V=v and a=1-v, giving equality at v=1/2. These laws have zero entries; strictly positive approximations show the same optimal supremum in finite-CE applications. The lower envelope is attained by p=((1+sqrt(v))/2,(1-sqrt(v))/2), q with entries reversed: V=v and a=sqrt(1-v). Thus both envelope endpoints are exact for every v in[0,1]. Probability laws in this scalar argument are reference laws, not asserted arbitrary Boolean spectra.

EXHAUSTIVENESS THEOREM. Every pair of normalized finite reference laws, on ANY finite alphabet, reduces EXACTLY to the probability weights M and scalars z_i=t_i^2 in[0,1]. The two scalar inequalities above hold on that ENTIRE interval. Summing and Jensen therefore exhaust all finite alphabets and every reference pair, rather than extrapolating from a grid. The 1225 executed pairs below are independent arithmetic checks, not the proof of this all-dimensional quantifier. For any fixed scalar v, the displayed two/three-atom examples certify the exact extrema; hence no larger alphabet improves either bound.

The previous stage's sharper bound -log2 a<=V remains valid under its atomwise z_i<=1/2 hypothesis. This stage removes that hypothesis with the sharp nonlinear bound(1), or the sharp factor2 bound(2) using only the MEAN V<=1/2. Replacing the old hypothesis while retaining constant1 would be false.

## 2. Retain the entire original-account bill

On a finite complete adaptive isospectral physical Boolean query tree, occupied frequency deletion is a probability-preserving bijection pi_l to each leaf. Pull the COMPLETE terminal reference back to root occupied support Omega, q_l(S)=Q_l(pi_l(S)); let m_l=sum q_l<=1 and R_l=q_l/m_l. Positivity on actual occupied atoms follows from finite CE. Define at internal binary nodes

    a_v=sum sqrt(R_left R_right), R_v=sqrt(R_left R_right)/a_v.

The unnormalized subtree geometric mean has normalizer Z_v=sqrt(Z_left Z_right)*a_v, with leaf Z_l=m_l. Induction gives

    -log2 Z=G+sum_internal w_v*(-log2 a_v),
    G=sum_leaves w_l*(-log2 m_l).

Here all w are ORIGINAL physical reaches, and G retains every reference-only mass loss. The normalized root geometric mean is Rstar. Expanding CE, with zero queried erasures, gives the exact full conversion debit

    Delta=D(P||Rstar)-D(P||Q0)+G+sum_v w_v*(-log2 a_v).

Therefore the floor-free sufficient original-account test is

    D(P||Rstar)-D(P||Q0)+G+sum_v w_v[-log2(1-V_v)] <= U,    (3)

where U=A-W-CE(P,Q0) is the ACTUAL unused ORIGINAL allowance, and W is every already booked debit. If every V_v<=1/2, the simpler sufficient test replaces the final sum by 2 sum_v w_v V_v. Both full physical branches and all complete terminal costs remain. The lower envelope in(1) supplies a necessary test with half the nonlinear sum. These are bounds on the exact retained geometric-normalizer liability, not fresh refunds or a new source price. Account data cannot be reissued after a conversion.

This connects directly to A09720261023T121505Z PROOF2--4: declaring a floor class can make a conversion necessary, but log-sum gives its actual minimum KL price. A claimed root allowance must still be supplied compatibly. No floor requirement or its necessity for arbitrary cores is inferred from our scalar certificate.

## 3. Actual finite Boolean control beyond the old atomwise domain

Take f=-1 at three-bit truth indices0,7 and+1 otherwise. Its actual spectrum P is uniform on{empty,12,13,23}, with H=2. Query bit0; both full child spectra are uniform on their four remaining labels and equal the inherited marginal. The queried erasure is0; with incoming Q0=P all occupancy/refund credit is0.

On the two full children prescribe the transported root-label references

    p=(3/8,3/8,15/64,1/64), q=(3/8,3/8,1/64,15/64).

They are complete, strictly positive on actual support. Their tail relative discrepancies include t^2=49/64>1/2: the old atomwise certificate is INADMISSIBLE. Nevertheless V=49/256<1/2, so(2) applies. Keep the root KL term! The actual mean complete CE increment is

    Delta=(10-log2 135)/4 <3/4,

where the strict sign is the exact integer135>128. The root geometric-reference mismatch equals Delta-N, where N=-log2 a. Since N>=V/(2 ln2)>5V/7 (using the rational certificate ln2<7/10), the NEW sufficient bill root-KL+2V is

    <3/4 + (9/7)*(49/256)=1785/1792=255/256.

SUPPLIED incoming A=13/4, old booking W=1/4 and initial CE2 give U=1, so the new test leaves reserve>1/256 on the SAME declared original account. No preceding physical prefix generating W or A is constructed; those are explicit incoming premises, not a new influence-price theorem. The chosen targets are a stress test, not proved necessary for an FEI invariant. This fixture demonstrates genuine additional coverage without hiding the root KL or inventing query credit.

## 4. Honest universal obstruction

Neither a floor-free local normalizer estimate nor a finite paid fixture supplies O(I) initial reference capacity for arbitrary Boolean cores. A required compatible target family must still satisfy(3) against its ACTUAL unused original account at all histories; target necessity and that hereditary price are unpaid. A097 supplies a scoped declared-class example with a finite-core source, not this universal premise. Universal FEI constant improvement is zero. Independent review of the new global envelope/tree certificate remains pending.
