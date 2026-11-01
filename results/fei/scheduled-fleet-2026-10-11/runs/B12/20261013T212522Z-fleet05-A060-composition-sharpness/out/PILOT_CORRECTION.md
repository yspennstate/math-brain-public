# Pilot correction

The first pilot stopped on assertion 2432: the physical composite singleton
coefficient was incorrectly asserted to be (1-delta)/2. That is its queried
influence, not its singleton coefficient. For F=D+h(b-D), the coefficient
is hhat({i})*(E b-E D)=(sqrt(delta)-delta)/2. The direct FWHT already
computed the correct coefficient, and the erasure/influence/entropy identities
passed before this assertion. Corrected the assertion; the original domain
and mathematical target are unchanged. No passing run is inferred from the
failed pilot. Its exception is preserved here.
