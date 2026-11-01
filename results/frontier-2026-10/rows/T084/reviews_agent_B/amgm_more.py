# T084, agent B: the AM-GM certificate on AG(3,2) (3-transitive: one pair is all pairs) and S8 (the control with basis
# Rayleigh difference -16; Potts-Rayleigh status unknown).
exec(open('amgm_cert.py').read().split("if __name__")[0])
certify('AG(3,2)', [8 | v for v in range(8)], 0, 1)
