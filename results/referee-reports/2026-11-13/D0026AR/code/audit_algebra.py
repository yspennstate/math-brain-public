import json,math,pathlib
out=[]
for q in [.5001,.55,.7,.99]:
    p=1-q;theta=math.sqrt(q/p);a=math.log(theta)
    lam=(theta-1)*(q/theta-p); B=q/(q-p*theta);c=q*(theta-1)/theta
    printed_lam=(theta*theta-1)/theta*(q-theta/(theta+1))
    n=9; worst=-1e100; nchecks=0
    for state in range(2**n-1):
        zero=[j for j in range(n) if not ((state>>j)&1)]
        for x in range(n):
            g=theta**min(abs(x-j) for j in zero); Lg=0.
            for j in range(n):
                enabled=(j>0 and not ((state>>(j-1))&1)) or (j+1<n and not ((state>>(j+1))&1))
                if not enabled:continue
                zeros_new=[k for k in range(n) if not (((state^(1<<j))>>k)&1)]
                assert zeros_new
                gnew=theta**min(abs(x-k) for k in zeros_new)
                Lg+=(q if (state>>j)&1 else p)*(gnew-g)
            worst=max(worst,Lg+lam*g-c); nchecks+=1
    assert worst<1e-11
    delta=lam/(2*(lam+100*a));cancel=100*a*delta-lam*(1-delta)+lam/2
    assert abs(cancel)<1e-13
    assert abs(lam-printed_lam)<1e-14
    assert abs(B-c/lam)<1e-10*max(1,B)
    out.append(dict(q=q,theta=theta,lam=lam,B=B,delta=delta,exhaustive_generator_checks=nchecks,max_drift_residual=worst,split_identity_residual=cancel,BCMRT_lambda_residual=lam-printed_lam))
root=pathlib.Path(__file__).resolve().parents[1]
(root/'data'/'algebra_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
n=1024; T=100; rho=2*math.e*T/n
print('boundary log upper bound', n*math.log(rho)-math.log1p(-rho))
print('A4 c0',100*math.log(100/(2*math.e)))
