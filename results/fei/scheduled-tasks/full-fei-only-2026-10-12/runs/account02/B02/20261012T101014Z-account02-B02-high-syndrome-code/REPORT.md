# B02/A008: bias-independent two-class code for linear-syndrome lifts
Status: AUTHOR-PROVED restricted-family theorem; independent review NOT_RUN; full FEI OPEN.
Date/source observation: 2026-10-12 UTC; no paid execution or schedule changes.
Scope: one new general coding lemma + growing-overlap family. This is NOT an actual posterior-forest/partition-run construction.

## Exact theorem and hypotheses
Let A be a full-row-rank t by N matrix over F_2, t>=1, and let d=min_{v != 0}|A^T v|. Let m>=0 and g:F_2^(m+t)->{+1,-1}. On independent uniform z in F_2^m and x in F_2^N define f(z,x)=g(z,Ax).
Let q=sum_{b in F_2^m, v != 0} hat g(b,v)^2 = E_z[Var_{u uniform}(g(z,u))].
For q>0 define C(A,m,q)=(m+1)/(d*q)+t/d.
Then a single explicit, bias-independent, normalized whole-Fourier-set reference Q_A satisfies
  H(f) <= E_{S~hat f^2}[-log_2 Q_A(S)] < (m+1)+t q <= C(A,m,q) I(f).
In particular, q>=eta>0 implies H(f) <= ((m+1)/(d*eta)+t/d) I(f).
No assumption on individual Fourier coefficients or bias; constant functions are outside q>0 but satisfy H=I=0.

## Decoder / normalizer
For any (b,v) in F_2^m x F_2^t, the physical Fourier support is
  S(b,v)= supp(b) union (m+supp(A^T v)),
an injective map because rank(A)=t.
Encode v=0 by bit 0 followed by m literal bits b (length 1+m).
Encode v!=0 by bit 1 followed by m bits b and t bits v (length 1+m+t).
These are distinct, prefix-free *binary* codewords. No coefficient or bias is used.
Their exact Kraft sum is
  Z=2^m*2^(-m-1)+2^m*(2^t-1)*2^(-m-t-1)=1-2^(-t-1).
Set Q_A(S(b,v))=2^(-ell(b,v))/Z and Q_A=0 off the image.
It is a normalized probability distribution, supported on every physically possible Fourier support.
For Fourier energy q on v!=0:
  E[-log_2 Q_A]=m+1+t*q+log_2(Z) < m+1+t*q.

## Exact spectral transfer / influence
Uniform Ax is uniform on F_2^t because A has full row rank.
Fourier transport: hat f(S(b,v))=hat g(b,v), and all other coefficients vanish.
Consequently H(f)=H(g) and
  I(f)=sum_{b,v} (|b|+|A^T v|) hat g(b,v)^2
      =I_z(g)+sum_{b,v!=0}|A^T v|hat g(b,v)^2 >= d*q.
Gibbs' inequality D(hat f^2||Q_A)>=0 gives H(f)<= E[-log_2 Q_A].
Combining proves the theorem. No finite experiment is used to prove the universal quantifiers.

## Growing-overlap corollary (new compared with single free control)
Let A_t have all nonzero t-bit columns (simplex dual, N=2^t-1). Every nonzero A_t^T v has weight d=2^(t-1).
For t>=4, m<=2^(t-2)=d/2 and any Boolean g with q>=1/2,
  H(g(z,A_t x)) <= (7/4)*I(g(z,A_t x)).
Proof: E[-log Q] < m+1+tq. Divide by I>=dq, use q>=1/2 and m<=d/2:
  E[-log Q]/I < 1+(t+2)/d <= 1+6/8=7/4.
The last ratio is nonincreasing for integer t>=4.
Here m may grow exponentially with t; g is otherwise arbitrary on all m+t latent bits.
Non-product examples exist for every t,m>=1: take any Boolean h(z) and let
  g(z,u)=h(z)*(-1)^{u_1*z_1}; then q=1/2.
This permits arbitrary Boolean h on the growing free block.

## Honest obstruction
For q=0 the model includes every arbitrary Boolean function h(z), by taking g(z,u)=h(z). Hence no uniform result for m unbounded can follow solely from the high-distance-code argument as q->0; an additional payment for the low-syndrome component would be required. The constructed Q_A is a genuine normalized prefix-code reference on full Fourier sets, NOT a verified probability distribution of actual partition-forest runs. This does not prove full FEI.

## Verification: executed 2026-10-12
Executed local Python standard-library exact integer Walsh-Hadamard script: python /tmp/b02_syndrome.py. RNG random.Random(101+t*37+m). Parameter cases (t,m)=(4,4),(5,8),(6,12), each with deterministic majority and seeded random h.
All six: exact integer Parseval, exact q=1/2, exact influence, prefix-code bound H<=L_norm<7I/4 PASSED (numerical log comparison for H, exact rational inequality L_upper<=7I/4).
Exact influence by case: 45/8,6,1333/128,1539/128,19437/1024,22511/1024.
Direct full physical Walsh transform for t=4,m=4: 2^19=524288 inputs; 256 candidate codewords; all 256 coefficient values matched latent Walsh scaling exactly, zero noncode coefficients and exact Parseval passed.
General theorem relies on proof, not these numerical checks. The local script was executed but is not claimed to be a committed artifact.

## Source pins / current controls
Brain repository: yspennstate/math-research-brain/main, inspected head 82320afa333f9059c664f9f432bcc69359d8e659.
- scheduled_tasks/CURRENT_OBJECTIVE.md blob 3bc19ac1c6850a797409c6d4ddd47d65a2ea0d7e (owner revision 2026-10-12.1).
- scheduled_tasks/README.md blob 2293391fec923119d8c2d829e374aaa784586960.
- scheduled_tasks/work/shared/full-fei-only-2026-10-12/ORDER.md blob 81b6d6f988aee4489512c6e62543253900620453.
- CASE_TARGETS.json blob 97e41262ebb4f09eec53630a918acae09efc9a48, B02 growth target.
- Owner inbox original REQ-20261012T031958Z-FULL-FEI-OWNER--owner-relay-fei-control--send-r1.json blob 3290aff155f63dbc1a5c58ae58c3dc3d6254b508.
Canonical math repository: yspennstate/math-open-problems/master, inspected head 996adb4e27850aff05d1f20082baced75551d955.
- reports/fei-2026-10-11/assignments/B02.json blob 29600a047ed321e39f4063c57f321dceeb387f13, A008 whole-set coding.
- reports/fei-2026-10-11/CURRENT_STATUS.md blob c416d4b4a83fc67965cb95d06a0cc80c5c29a520, full FEI open.
Independent review NOT_RUN; native Math Brain ingestion NOT_RUN; native retrieval NOT_RUN; receiver use/outcome UNVERIFIED.
Next step: seek actual disjoint posterior-forest runs whose induced whole-set law dominates Q_A uniformly, or exhibit the exact multiplicity/normalization obstruction. No guard is weakened.
