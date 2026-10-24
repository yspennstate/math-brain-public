# Independent adversarial audit of w594

Auditor: w595. Original author proof snapshot: w594_ATTEMPT_as_read.md, SHA256 51222970b025b710f9405f9314f8d448618e7d3e8301711a10db93df1fe5a261.
Independent material was first saved in ../INDEPENDENT_DERIVATION.md before accessing this proof.

Verdict: KEEP_SCOPED for Lemma 2, the finite-graph quotient estimate. The parent C0049 remains unresolved. No served-model/account evidence is inferred from requested settings.

The relative FK configuration weight is c^(o+2k) after a common factor cancels, with c=cos(pi*h/2), o<=m and k<=v even after the fixed wiring. Consequently 0<=o+2k<=N=m+2v. Its normalized Radon-Nikodym density lies in [c^N,c^(-N)], so the stated bounded-observable expectation difference is valid. The exponential Taylor remainder has magnitude at most h^2*W^2/2 before division by h. The factor of i and sign of the quotient correctly recover W*exp(iW). Finally sec^2(x)<=2 for x<=pi/4 implies -log cos(x)<=x^2. All constants in the displayed finite-graph estimate check. The parameter laws and exploration map remain fixed as required.

The proof's use of a linear local relation in the finite-graph limit is also sound: both F_(h,1-h) at its matching q_h and F_(h,1) by pathwise flux obey that relation. Subtract, divide and take the fixed-graph limit. It does not multiply dependent conditional events.

Lemma 1's displayed directions give the correct flux signs, and its statement excludes endpoints. The deterministic path-law example addresses only the stated equation/terminal-normalization/boundedness bridge; it need not be a critical FK law or satisfy additional crossing controls. The abstract W_n=2*pi*n example correctly gives D_n=-4*i*n and relative error sqrt(1+4/pi^2). Its lack of asserted FK realizability is essential to its scope.

Minimal missing premises for any proposed strengthening: if the target normalization is a_delta, even the explicit finite-graph estimate would require a_delta*h_delta*L_delta^2 -> 0 and a_delta*L_delta*(exp(pi^2*N_delta*h_delta^2/4)-1) -> 0 along the chosen diagonal. Picking h_delta very small can make this finite-graph error vanish; it does not supply the continuum limit of the quotient or its martingale property. Pointwise convergence for each fixed h does not justify a joint h/delta limit. Control is needed in the random slit domains and in the limiting driver filtration. For example, f(h,delta)=exp[-(h/delta)^2] tends to 0 as delta->0 for each h>0 but is 1 at h=0; finite-delta continuity in h alone does not transfer a fixed-h limit to the endpoint. This is a quantifier counterexample, not an FK construction.

The ordinary spin-one discrete identity being insensitive to p does not contradict the conditional continuum driver lemma: if the scaled continuum power really is a true stopped martingale, two Laurent coefficients force kappa=4. Establishing that scaling limit is the missing substantive premise. The winding-weighted replacement must be treated with its own correctly normalized continuum limit; it cannot be substituted for the power observable without a derivation.

No correction is required to the finite-graph theorem as written. Do not promote it to a mesh-uniform FK theorem or a solved parent problem. The main independent referee is w596; this supplementary audit does not supply response-side model provenance or discharge the campaign's distinct-model gate.

NEXT: Obtain w596's narrow mathematical verdict, then close the normalized random-slit/martingale gap before any FK-to-SLE claim.
