import json, math

def interp(r):
    p = r/(r-1)
    Cp = 1/(2-p) + ((2-p)/(3*p-4))**((2-p)/2)
    b = 2/r - 0.5
    K3 = 2*math.sqrt(2)
    Mr = ((2*math.pi)**(1/r) * 2**(1/p) * (K3/2)**0.5
          * Cp**(1/p) * (2*math.sqrt(2))**b)
    Dr = math.pi*math.sqrt(2) * (2*(r-1))**((r-1)/r) * Mr
    Gamma = (r+1)/math.pi * (Dr/(2*r))**(r/(r+1))
    return {
        'r': r, 'p': p, 'Cp': Cp, 'Mr': Mr, 'Dr': Dr,
        'Gamma': Gamma,
        'rho_exp': r/(2*(r+1)),
        'lambda_exp': (r-2)/(2*(r+1)),
        'R_exp': (4-r)/(2*(r+1)),
    }

out = {'r3': interp(3.0), 'r11_5': interp(11/5)}
out['rho0'] = math.sqrt(29/3072)
r = out['r11_5']
out['fixed_branch_coefficient'] = (r['Gamma'] * out['rho0']**(-r['rho_exp'])
                                   * (1/64)**(-r['R_exp']))
out['Dprime_s3_1_64_h_2_3'] = 576*math.sqrt(3*math.e)
print(json.dumps(out, indent=2, sort_keys=True))
