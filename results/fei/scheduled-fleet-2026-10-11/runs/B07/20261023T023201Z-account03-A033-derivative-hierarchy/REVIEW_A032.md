# A032-SIGNED-TAG-VACUUM-TAIL-RESET@1: independent reconstruction

Source: A032 run 20261023T013017Z, PROOF.md sections 1--5 and CLAIMS.json.
Statement SHA256: a8eaef0443d2816feeef2b939d7fd28498792dd1561d0bd3da7168a2e134885e.
Verdict: HOLDS at its stated conditional source-reference scope. A033
supplied no repair and is an independent reviewer of this unchanged version.
This is local acceptance, not registry adoption or universal FEI acceptance.

Reconstruction: at tag0 the Fourier amplitude is a_U with empty seed label;
at tag1 it is b_U hhat(T). The physical tag children have vacuum amplitudes
a_U +/- mu b_U, with all signs preserved. The true tail remains b_U^2 p_T.
The full signed child reference therefore normalizes to one because
sum a_U b_U=0, and its relative entropy is exactly
beta(1-r)D(p_tail||M). The incoming relative entropy is
beta[d(r||t)+(1-r)D(p_tail||R_tail)]. Subtracting these expressions and
using H(parent)-mean H(children)=B_tag+JS_tag reproduces A032 equation (2)
with its negative JS and negative binary-KL terms. The mixture floor
gives the claimed sufficient condition. It is sufficient, not necessary.

For r=1/4,t=1/2,epsilon=1/8 the scalar slack is
(3/4)log2(21)-13/4>1/24 iff 21^18>2^79. At beta=3/8 this is >1/64.
The independent direct-character fixture verifies that integer inequality.
The support counterexample is also exact: a_empty=1/8,b_empty=3/8,
true mu=1/2 and substituted sqrt(t)=1/3 give true minus-child mass
(1/8-3/16)^2=1/256 and substituted mass (1/8-1/8)^2=0.
The supplied h=[-1,1,1,1] is Boolean with mu=1/2 and the displayed R is
positive and normalized. Thus finite parent CE does not justify that
phase substitution. It is not an FEI counterexample.

The source's endpoints are consistent: r=1 uses only true vacuum with
binary-KL credit for removing old tail; t=1 forces r=1 at finite CE;
beta=0 creates no seed cost. Normalized full references and the full
current marginalized-reference chain support its antichain replacement
argument. No arbitrary initial influence price follows from it.

No author code was imported or run. A033 code/check.py constructs actual
tagged truth tables, independent integer Walsh spectra and prime-log
identities for the source equation at every nonconstant frozen parent
case, as well as the NEW later seed-query formula. Its final coverage
and completed counts are exclusively those in out/targeted.json;
out/attempt1_timeout.json is incomplete and contributes no certificate.
The direct-character code/biased.py separately verifies the eligible
biased continuation and normalizers. New A033 extensions need their own
external review and are not accepted by this review of A032.
