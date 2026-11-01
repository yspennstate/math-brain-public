// Agent 104 exact certificate; standard ECMAScript with BigInt.
// Run: node 104_diagonal_direction_certificate.js
function certificate() {
  let checks = 0;
  const abs = x => x < 0n ? -x : x;
  const gcd = (a,b) => { a=abs(a); b=abs(b); while(b){let r=a%b;a=b;b=r;} return a; };
  const Q = (a,b=1n) => { a=BigInt(a); b=BigInt(b); if(!b)throw Error("zero denominator"); if(b<0n){a=-a;b=-b;} const g=gcd(a,b);return [a/g,b/g]; };
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]];
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
  const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
  const str=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+a[1];
  const zero=Q(0),one=Q(1);
  const sum=xs=>xs.reduce(add,zero);
  const assert=(v,label)=>{checks++;if(!v)throw Error(label);};
  const C=(r,i=zero)=>[r,i];
  const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
  const cn=a=>[neg(a[0]),neg(a[1])];
  const cm=(a,b)=>[sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))];
  const conj=a=>[a[0],neg(a[1])];
  const ceq=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]);
  function det(A) {
    const n=A.length;if(!n)return C(one);
    let v=C(zero);
    for(let j=0;j<n;j++){
      const minor=A.slice(1).map(row=>row.filter((_,k)=>k!==j));
      let term=cm(A[0][j],det(minor));if(j%2)term=cn(term);v=ca(v,term);
    }
    return v;
  }
  const pop=x=>{let c=0;while(x){c+=x&1;x>>=1;}return c;};
  function atoms(K) {
    const n=K.length,out=[];
    for(let x=0;x<(1<<n);x++){
      let M=K.map(row=>row.slice());
      for(let i=0;i<n;i++)if(!(x>>i&1))M[i][i]=ca(M[i][i],C(neg(one)));
      let d=det(M);if((n-pop(x))%2)d=cn(d);
      assert(eq(d[1],zero),"atom is real");out.push(d[0]);
    }
    return out;
  }
  function marginal(p,n,indices,mask) {
    const outside=Array.from({length:n},(_,i)=>i).filter(i=>!indices.includes(i));
    return sum(p.filter((_,x)=>outside.every(i=>((x>>i)&1)===((mask>>i)&1))));
  }
  function D(p,n,i) {
    return p.map((_,x)=>mul(Q((x>>i&1)?1:-1),add(p[x&~(1<<i)],p[x|(1<<i)])));
  }
  function shift(K,h) {
    return K.map((row,i)=>row.map((z,j)=>i===j?ca(z,C(h[i])):z));
  }
  function direct_derivative(K,a,order) {
    const n=K.length,out=[];
    for(let x=0;x<(1<<n);x++){
      let M=K.map(row=>row.slice());
      for(let i=0;i<n;i++)if(!(x>>i&1))M[i][i]=ca(M[i][i],C(neg(one)));
      let value=C(zero);
      for(let T=0;T<(1<<n);T++)if(pop(T)===order){
        let N=M.map(row=>row.slice()),coef=order===2?Q(2):one;
        for(let i=0;i<n;i++)if(T>>i&1){
          coef=mul(coef,a[i]);
          for(let j=0;j<n;j++)N[j][i]=C(Q(j===i?1:0));
        }
        value=ca(value,cm(C(coef),det(N)));
      }
      if((n-pop(x))%2)value=cn(value);
      assert(eq(value[1],zero),"derivative is real");out.push(value[0]);
    }
    return out;
  }
  function log_interval(q,N=24) {
    if(lt(q,one)){const z=log_interval(div(one,q),N);return [neg(z[1]),neg(z[0])];}
    const x=div(sub(q,one),add(q,one)),x2=mul(x,x);let pow=x,lo=zero;
    for(let k=0;k<N;k++){lo=add(lo,div(mul(Q(2),pow),Q(2*k+1)));pow=mul(pow,x2);}
    const err=div(mul(Q(2),pow),mul(Q(2*N+1),sub(one,x2)));
    return [lo,add(lo,err)];
  }
  const K=[
    [C(Q(1,4)),C(zero,Q(1,20)),C(Q(1,25))],
    [C(zero,Q(-1,20)),C(Q(1,2)),C(zero,Q(1,30))],
    [C(Q(1,25)),C(zero,Q(-1,30)),C(Q(3,4))]
  ];
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)assert(ceq(K[i][j],conj(K[j][i])),"Hermitian");
  const p=atoms(K),n=3;
  assert(eq(sum(p),one),"normalization");
  p.forEach(q=>assert(lt(zero,q),"positive atom"));
  const d=Array.from({length:n},(_,i)=>D(p,n,i));
  for(let i=0;i<n;i++){
    D(d[i],n,i).forEach(q=>assert(eq(q,zero),"nilpotent D_i"));
    for(let x=0;x<p.length;x++)assert(eq(d[i][x],mul(Q(x>>i&1?1:-1),marginal(p,n,[i],x))),"first derivative marginal");
    for(let j=i+1;j<n;j++){
      const dij=D(d[i],n,j),dji=D(d[j],n,i);
      for(let x=0;x<p.length;x++){
        assert(eq(dij[x],dji[x]),"commuting shifts");
        const sign=((x>>i&1)+(x>>j&1))%2?-1:1;
        assert(eq(dij[x],mul(Q(sign),marginal(p,n,[i,j],x))),"second derivative marginal");
      }
    }
  }
  const h=[Q(1,100),Q(-1,80),Q(1,120)];
  let shifted=p.slice();
  for(let i=0;i<n;i++){const di=D(shifted,n,i);shifted=shifted.map((q,x)=>add(q,mul(h[i],di[x])));}
  const actual=atoms(shift(K,h));
  actual.forEach((q,x)=>assert(eq(q,shifted[x]),"finite exact signed shift identity"));
  const a=[Q(1),Q(-2),Q(3)],dp=direct_derivative(K,a,1),ddp=direct_derivative(K,a,2);
  for(let x=0;x<p.length;x++){
    assert(eq(dp[x],sum(d.map((row,i)=>mul(a[i],row[x])))),"direct score derivative");
    let rhs=zero;
    for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)rhs=add(rhs,mul(mul(Q(2),mul(a[i],a[j])),D(d[i],n,j)[x]));
    assert(eq(ddp[x],rhs),"direct Hessian derivative");
    let logcoef=zero;
    for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
      const mixed=((x>>i&1)!==(x>>j&1))?1:-1;
      logcoef=add(logcoef,mul(mul(Q(2*mixed),mul(a[i],a[j])),marginal(p,n,[i,j],x)));
    }
    assert(eq(logcoef,neg(ddp[x])),"Hessian log-atom coefficient");
  }
  assert(eq(sum(dp),zero)&&eq(sum(ddp),zero),"derivative normalization");
  for(let i=0;i<n;i++){
    const mean=sum(p.filter((_,x)=>x>>i&1));
    assert(eq(mean,K[i][i][0]),"one-site mean");
    for(let j=i+1;j<n;j++){
      const joint=sum(p.filter((_,x)=>(x>>i&1)&&(x>>j&1)));
      const cov=sub(joint,mul(K[i][i][0],K[j][j][0]));
      const abs2=cm(K[i][j],conj(K[i][j]))[0];
      assert(eq(cov,neg(abs2)),"occupation covariance");
    }
  }
  function two_site(u,v,b,expectedJ,positive) {
    const K2=[[C(u),C(b)],[C(b),C(v)]],p2=atoms(K2);
    assert(eq(sum(p2),one),"two-site normalization");
    p2.forEach(q=>assert(lt(zero,q),"two-site positivity"));
    const d1=D(p2,2,0),d2=D(p2,2,1);
    const Jij=sum(p2.map((q,x)=>div(mul(d1[x],d2[x]),q)));
    assert(eq(Jij,expectedJ),"exact mixed Fisher value");
    const odds=div(mul(p2[1],p2[2]),mul(p2[0],p2[3]));
    const log=log_interval(odds),hlo=sub(log[0],Jij),hhi=sub(log[1],Jij);
    assert(positive?lt(zero,hlo):lt(hhi,zero),"certified mixed Hessian sign");
    return {atoms:p2.map(str),J12:str(Jij),odds:str(odds),H12_sign:positive?"positive":"negative",log_series_terms:24};
  }
  const pos=two_site(Q(9,10),Q(1,10),Q(1,20),Q(592,2275),true);
  const negcase=two_site(Q(1,2),Q(1,2),Q(1,10),Q(25,156),false);
  assert(lt(Q(592,2275),Q(16,57)),"simple positive lower bound");
  assert(eq(sub(Q(16,57),Q(592,2275)),Q(2656,129675)),"positive margin");
  assert(lt(Q(25,9),Q(3)),"sqrt(3)>5/3");
  assert(lt(Q(16,11),Q(3,2)),"dimension-uniform row bound<3/2");
  return {status:"PASS",checks,arithmetic:"exact BigInt rational, including complex determinant checks",complex_three_site_atoms:p.map(str),positive_mixed_entry:pos,negative_mixed_entry:negcase,uniform_class:"condition_number(Gamma)<=3 implies H''[diag(a),diag(a)]<=-||a||^2/2; analytic matrix proof in report"};
}
console.log(JSON.stringify(certificate(), null, 2));
