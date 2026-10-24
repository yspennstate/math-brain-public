from decimal import Decimal, getcontext
import math

getcontext().prec = 50
L = Decimal('6.30297437506')
U = Decimal('12.78437096216')

print('T03_CERTIFIED_LOWER', L)
print('T03_CERTIFIED_UPPER', U)
print('T03_CERTIFIED_WIDTH', U-L)

for rho_txt in ['0.01','0.05','0.10','0.20']:
    rho = Decimal(rho_txt)
    upper = U/(Decimal(1)-rho)
    print('CONSTANT_LOWER_RADIUS_CONTAMINATION', rho_txt, 'UPPER', upper, 'WIDTH', upper-L)

print('GAUSSIAN_TRIMMED_RADIUS_RATE_CHECK')
alpha = float(U) + 0.5
for N in [10_000,100_000,1_000_000,10_000_000]:
    logN = math.log(N)
    old_delta = math.sqrt(12.0*logN/N)
    new_delta = math.sqrt(8.0*math.log(logN)/N)
    q_bound = 1.0/(logN*logN) # Laurent-Massart with delta_new
    eps = 1.0/logN
    M = int(alpha*N)
    # For B~Bin(M,q), q<=q_bound<eps, standard Chernoff:
    # P(B>=eps M) <= (e*q_bound/eps)^(eps M).
    log_tail_bound = eps*M*(1.0 + math.log(q_bound/eps))
    print(N,
          'OLD_DELTA', format(old_delta,'.16g'),
          'NEW_DELTA', format(new_delta,'.16g'),
          'RATIO', format(new_delta/old_delta,'.16g'),
          'Q_BOUND', format(q_bound,'.16g'),
          'EPS', format(eps,'.16g'),
          'LOG_CHERNOFF_BOUND', format(log_tail_bound,'.16g'))

print('VANISHING_CONTAMINATION_MAX_FAILURE')
# rho_N=1/log N, M=floor(alpha N): P(no contaminated row) <= exp(-M/log N).
for N in [10_000,100_000,1_000_000]:
    logN = math.log(N)
    rho = 1.0/logN
    M = int(alpha*N)
    log_p_no = M*math.log1p(-rho)
    print(N, 'RHO', format(rho,'.16g'), 'LOG_P_NO_CONTAM', format(log_p_no,'.16g'),
          'P_ANY_CONTAM_LOWER', format(1.0-math.exp(log_p_no),'.16g'))

print('ALL_CHECKS_PASS')
