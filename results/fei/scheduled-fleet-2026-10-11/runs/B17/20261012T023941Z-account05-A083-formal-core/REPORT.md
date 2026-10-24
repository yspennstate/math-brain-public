# exact target, quantifiers, hypotheses and units

A083, B17, run 20261012T023941Z-account05-A083-formal-core. Follow the stream lead's assignment to formalize the coefficient comparison in B17-JS-PACKET-SCALAR v1. Let O_0=E_0=1, O_(n+1)=(2n+1)O_n and E_(n+1)=(2n+2)E_n. For every natural n>=1, check E_n<=2nO_n and therefore 1/[2n(2n-1)]<=(O_n/E_n)/(2n-1). Check the factorial identifications and comparison of all finite partial sums for every rational t>=0. These exact arithmetic statements have no entropy units. The downstream scalar inequality uses natural logs; its JS application divides by ln2 to obtain bits.

The full scalar target is F(z)<=G(z) for all real z in [-1,1], where F(z)=((1+z)ln(1+z)+(1-z)ln(1-z))/2, G(z)=1-sqrt(1-z^2) and 0ln0=0. This report distinguishes a kernel-checked coefficient/finite-sum core from a paper reconstruction of the analytic extension. It does not claim full formal verification of the real scalar statement or FEI.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage start, snapshot 2026-10-12 02:43 UTC; B17 STREAM_NOTES.md v2, 2026-10-11 23:40 UTC; own STATUS.md; the stream lead's CLAIMS.json from 20261011T224300Z-claude-B17-erasure-census-affine-bridge; and EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2. Source byte hashes are saved in out/SOURCE_RECEIPTS.json. The key source is B17-JS-PACKET-SCALAR v1, proof_source derivation sections (1)-(3), particularly a_(k+1)=a_k(2k+1)/(2k+2) and a_k>=1/(2k). Its original REPORT.md was not saved by the lead's harness; the exact available claim and stream direction are used instead of claiming access to that missing report.

The board records completed n<=4 censuses, the B09 margin, affine bridges and later five-bit certificates. None is repeated. Prior A083 checked signed rational interval division, which is a different risk. This stage checks the lead's universal coefficient step, and preserves the distinction between C005's JS clause and the unpaid universal erasure term. The earlier stage read the protocol and campaign papers; this stage consumes the new source rather than restarting their unrelated audits.

# complete derivation or exact first unsupported line

Kernel core: O_n and E_n are positive products. At n=1, E_1=2=2O_1. If E_n<=2nO_n for n>=1, then

    E_(n+1)=(2n+2)E_n <= (2n+2)(2n)O_n
       <= (2n+2)(2n+1)O_n = 2(n+1)O_(n+1).

Natural arithmetic proves this by induction. Exact product identities, also checked by induction, give (2n)!=O_nE_n and E_n=2^n n!. Hence on paper O_n/E_n=(2n)!/[4^n(n!)^2]=binom(2n,n)/4^n. Rational order cancellation of positive E_n and 2n gives 1/(2n)<=O_n/E_n. Multiplication by positive 1/(2n-1) gives the coefficient inequality. Multiplication by nonnegative t^n and induction on the number of terms gives the formal theorem all_partial_sums. No finite maximum index is used.

Analytic extension, outside Lean: F(0)=F'(0)=0 and F''(z)=1/(1-z^2). For |z|<1 the geometric series for this second derivative converges uniformly on every compact subinterval. Integrating twice yields

    F(z)=sum_(n>=1) z^(2n)/[2n(2n-1)].

For completeness the required binomial expansion can be reconstructed without an external theorem: a_0=1 and a_(n+1)=a_n(2n+1)/(2n+2), so 0<a_n<=1. The series A(t)=sum_(n>=0)a_n t^n and its termwise derivative converge on compact subsets of |t|<1, dominated by geometric and differentiated geometric series. The recurrence gives 2(1-t)A'(t)=A(t) and A(0)=1. Differentiating sqrt(1-t)A(t) shows it is constant, hence A(t)=(1-t)^(-1/2). Integrating its half multiple from 0 to t and using a_n=a_(n-1)(2n-1)/(2n) yields

    1-sqrt(1-t)=sum_(n>=1) a_n t^n/(2n-1).

Set t=z^2. For each finite N the polynomial inequality extends from rational t>=0 to real t>=0 by density and continuity. For 0<=t<1 both partial sums converge to the displayed functions, so their order passes to the limit. At z=+-1, continuity of x ln x at 0 and of the square root gives the endpoint inequality by approaching from the interior. Evenness covers negative z. The first step outside the kernel certificate is the real-series identity for F; the binomial expansion, real-density transfer and endpoint limits are likewise not formalized here. They are complete analytic arguments on the page, not hidden formal premises.

Packet application, also outside Lean: for u=fhat(T), v=fhat(T+i), write s=u^2+v^2. When s>0, z=2uv/s lies in [-1,1]; at s=0 the packet is zero. The physical child/spectral joint masses are s(1+z)/2 and s(1-z)/2, and Boolean normalization makes the physical child marginal fair. Its contribution to JS_i is sF(z)/ln2. Since

    sG(z)=s-|u^2-v^2|=2min(u^2,v^2),

the scalar inequality gives JS_i<=(2/ln2)sum_T min(u^2,v^2)<=(2/ln2)min(I_i,1-I_i). This does not bound B_i=H(S_i|S_-i), and therefore does not finish C018 or C019.

# executed validation with domain, arithmetic, commands and outputs

code/JSCoefficients.lean imports only Init.Data.Rat.Lemmas. Its printed theorem scopes are coefficient_cross_comparison, rational_normalized_coefficient, scalar_series_coefficient, factorial_split, even_factorial and all_partial_sums. out/LEAN_CHECK.txt and out/LEAN_RESULT.json record the final compiler status, actual foundational axiom dependencies, elapsed time and peak process commit. No sorryAx or error is permitted by the finalizer. No additional axiom asserts a target, and there is no native evaluation bypass of the kernel.

Final validation passed with exit 0 in 21.113 seconds and 520,015,872 bytes peak process commit. The integer coefficient theorem and factorial identities depend on propext and Quot.sound; the rational coefficient and partial-sum theorems additionally depend on Classical.choice. No printed theorem depends on sorryAx.

Frozen specification: out/FROZEN_SPEC.json, generated before proof checking. Domain is all natural n>=1, with all rational t>=0 and natural partial-sum lengths for the extension; no finite cutoff or symmetry reduction. Arithmetic is exact Lean Nat/Rat. Memory estimate 550 MiB; hard process cap 1400 MiB; timeout 60 seconds. Commands, from A083:

```text
python -X utf8 runs/20261012T023941Z-account05-A083-formal-core/code/prepare.py
python -X utf8 ~/brain_workers/FEI100_20261011/tools/memok.py
python -X utf8 runs/20261012T023941Z-account05-A083-formal-core/code/check_lean.py
python -X utf8 runs/20261012T023941Z-account05-A083-formal-core/code/finalize.py
```

The initial Lean pass checked the integer bound and both factorial identities, but failed the rational comparison because an unreduced multiplication by 1 remained. The proof was corrected with Rat.mul_one; out/LEAN_ATTEMPT1.txt preserves the diagnostic and sorryAx of that failed draft. The next pass checked the rational comparisons but required an explicit exponent n+1 in the nonnegative power used by the finite-sum extension; out/LEAN_ATTEMPT2.txt preserves that diagnostic. Multiple memok exit 1 results postponed further checking: no proof process was started on those rejections. out/MEMORY_GATES.json records the latest bounded retry sequence. Compiler attempts are ordinary proof edits, not three substantive failed mechanisms. There is no Boolean search, GPU, library rebuild, package installation, shared-folder mutation or job outliving its command.

# proof dependencies and changed downstream conclusions

The formal statement uses no campaign theorem as a logical premise. B17-JS-PACKET-SCALAR v1 supplies its intended application and coefficient definitions; Lean's exact arithmetic proves the coefficient core directly. The factorial/binomial and real-series interface is documented explicitly. The exported claim is the checked arithmetic core, not a status upgrade for the entire B17 scalar theorem. Its statement hash is SHA256 of UTF-8 compact sorted JSON containing exact_statement and hypotheses.

A081 can replace the unverified coefficient step with this precise kernel-checked artifact, while retaining the real analytic steps as separate evidence. A085 must not read the formal check as certification of Fourier normalization, Shannon identities, Python checkers or all-dimensional FEI. C005's local JS contribution has an explicit constant; the dimension-independent bound for erasure/stopping debt remains the same unpaid target.

# one next mathematical action and independent reviewer

A090 should reconstruct the formal-to-analytic interface, especially the factorial identification and endpoints; A094 is the alternate reviewer. A081 should attach the precise coefficient/partial-sum scope to its C005 dependency node. Once reviewed, A083 should consume a concrete new proof objection in the unpaid C018/C019 residual instead of repeating the scalar proof or building a real-analysis library.

# actual persistence receipts or precise save blocker

The run saves REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, FORMAL_SCOPE.md, code/ and out/, only inside A083. finalize.py checks exact protocol claim/progress field sets and writes updated STATUS.md, an appended dated WORKLOG.md and durable LEARNED.md. out/ARTIFACT_RECEIPTS.json gives local sizes and SHA256 hashes after successful final checking. Independent acceptance, supervisor copy and Brain/GitHub mirror are pending; local persistence is not a mirror receipt.

**Universal bridge:** This stage moves the C018/C019 dependency chain by kernel-checking the all-index coefficient comparison and finite-sum passage that support C005's JS_i<=(2/ln2)I_i allowance. It changes no numerical constant and pays zero of the remaining erasure or terminal debt. The universal B<=KI or nonreusing stopping-tree residual remains open. NEXT is independent review of this exact interface, followed by a concrete objection in that unpaid residual, because another scalar baseline or isolated class census would not approach full FEI.
