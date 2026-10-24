"use strict";
// Agent097 reconstruction certificate. Pure JavaScript; no dependencies.
// Exact rational arithmetic verifies the numerical constants and rational center.
// Analytic inequalities used by the proof are stated in the accompanying report.
// This does not audit the unavailable Agent070 bytes or certify global concavity.
const certificate097 = (() => {
  const abs = a => a < 0n ? -a : a;
  const gcd = (a,b) => { a=abs(a); b=abs(b); while(b){const c=a%b; a=b; b=c;} return a; };
  const q = (a,b=1n) => { a=BigInt(a); b=BigInt(b); if(!b)throw Error("zero denominator"); if(b<0n){a=-a;b=-b;} const g=gcd(a,b);return [a/g,b/g]; };
  const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>[-a[0],a[1]];
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
  const pow=(a,n)=>{let z=q(1);while(n--)z=mul(z,a);return z;};
  const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
  const lt=(a,b)=>a[0]*b[1]<b[0]*a[1];
  const show=a=>a[1]===1n?String(a[0]):String(a[0])+"/"+String(a[1]);
  const assert=(a,msg)=>{if(!a)throw Error(msg);};
  const c=(r,i=q(0))=>[r,i], cadd=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
  const cneg=a=>[neg(a[0]),neg(a[1])], csub=(a,b)=>cadd(a,cneg(b));
  const cmul=(a,b)=>[sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))];
  const ceq=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]);
  const cshow=a=>({real:show(a[0]),imag:show(a[1])});
  const mmul=(A,B)=>A.map((row,i)=>B[0].map((_,j)=>row.reduce((z,v,k)=>cadd(z,cmul(v,B[k][j])),c(q(0)))));
  const Id=[0,1,2].map(i=>[0,1,2].map(j=>c(q(i===j?1:0))));
  const a=q(13,125), b=q(53,500), z=q(21,200);
  const L=[[c(q(1)),c(a),c(q(0),neg(z))],[c(a),c(q(1)),c(b)],[c(q(0),z),c(b),c(q(1))]];
  const den=7933846;
  const K=[
    [c(q(3945082,den)),c(q(208000,den),q(11130,den)),c(q(-11024,den),q(-210000,den))],
    [c(q(208000,den),q(-11130,den)),c(q(3944871,den)),c(q(212000,den),q(10920,den))],
    [c(q(-11024,den),q(210000,den)),c(q(212000,den),q(-10920,den)),c(q(3944662,den))]
  ];
  const IpL=L.map((row,i)=>row.map((v,j)=>cadd(v,Id[i][j])));
  const ImK=K.map((row,i)=>row.map((v,j)=>csub(Id[i][j],v)));
  const product=mmul(IpL,ImK), kProduct=mmul(IpL,K);
  for(let i=0;i<3;i++)for(let j=0;j<3;j++){
    assert(ceq(product[i][j],Id[i][j]),"(I+L)(I-K)=I");
    assert(ceq(kProduct[i][j],L[i][j]),"(I+L)K=L");
  }
  const r=q(11,100), x=pow(r,2);
  const Dlo=sub(sub(q(1),mul(q(3),x)),mul(q(2),pow(r,3)));
  const Qlo=pow(sub(q(1),x),3);
  const gap=add(add(mul(q(3),pow(x,2)),pow(x,3)),mul(q(2),pow(r,3)));
  assert(lt(q(24,25),Dlo),"D lower bound");
  assert(lt(q(24,25),Qlo),"Q lower bound");
  assert(lt(div(x,sub(q(1),x)),q(1,80)),"pair coefficient upper bound");
  assert(lt(gap,q(97,31250)),"determinant-product gap below .003104");
  assert(lt(div(gap,q(24,25)),q(1,250)),"triple coefficient magnitude below .004");
  const m=sub(q(1,100),q(1,250)), u=add(q(1,80),q(1,250));
  const alpha=div(add(m,u),q(2)), eta=div(sub(mul(q(3),m),u),q(2));
  const traceCoefficient=sub(q(4,3),alpha);
  assert(eq(m,q(3,500))&&eq(u,q(33,2000)),"M interval");
  assert(eq(alpha,q(9,800))&&eq(eta,q(3,4000)),"frozen coefficients");
  assert(eq(traceCoefficient,q(3173,2400)),"entropy trace coefficient");
  const radius=q(1,200000), ellerr=mul(q(5),radius);
  const kmin=q(789,1789), kmax=q(1211,2211);
  assert(lt(q(2,5),sub(kmin,radius)),"ball K lower bound");
  assert(lt(add(kmax,radius),q(11,20)),"ball K upper bound");
  const inverseProduct=mul(q(20,9),q(2211,1000));
  assert(lt(inverseProduct,q(5)),"L perturbation Lipschitz constant");
  const edgeLo=div(sub(a,ellerr),add(q(1),ellerr));
  const edgeHi=div(add(b,ellerr),sub(q(1),ellerr));
  assert(eq(edgeLo,q(4159,40001))&&eq(edgeHi,q(4241,39999)),"normalized band endpoints");
  assert(lt(q(1,10),edgeLo)&&lt(edgeHi,q(11,100)),"ball remains in normalized band");
  const maxEdgeChange=div(mul(ellerr,add(q(1),b)),sub(q(1),ellerr));
  assert(lt(maxEdgeChange,q(3,100000)),"normalized edge change below .00003");
  return {
    status:"PASS; exact rational certificate for the stated reconstruction",
    centerK:K.map(row=>row.map(cshow)),
    DLower:show(Dlo), QLower:show(Qlo), determinantProductGapBound:show(gap),
    tripleLogMagnitudeBound:show(div(gap,q(24,25))),
    m:show(m),u:show(u),alpha:show(alpha),eta:show(eta),
    entropyTraceCoefficient:show(traceCoefficient),
    radiusFrobenius:show(radius), LErrorBound:show(ellerr),
    inverseProductBound:show(inverseProduct),
    normalizedEdgeLower:show(edgeLo),normalizedEdgeUpper:show(edgeHi),
    normalizedEdgeChangeBound:show(maxEdgeChange)
  };
})();
if(typeof console!=="undefined" && typeof console.log==="function") console.log(JSON.stringify(certificate097,null,2));
certificate097;


"use strict";
// Floating-point diagnostics for the exact theorem and remaining scalar test.
// These outputs are evidence about finitely many inputs, never a universal proof.
const diagnostics097=(()=>{
 const z=(r=0,i=0)=>[r,i],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[0],-a[1]],
 sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],
 conj=a=>[a[0],-a[1]],norm=a=>a[0]*a[0]+a[1]*a[1],
 div=(a,b)=>{const n=norm(b);return [(a[0]*b[0]+a[1]*b[1])/n,(a[1]*b[0]-a[0]*b[1])/n];};
 const zero=(n,m=n)=>Array.from({length:n},()=>Array.from({length:m},()=>z()));
 const eye=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>z(i===j?1:0)));
 const mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,a,k)=>add(s,mul(a,B[k][j])),z())));
 const tr=A=>A.reduce((s,row,i)=>add(s,row[i]),z());
 const inv=A=>{
  const n=A.length;if(!n)return [];
  const T=A.map((row,i)=>[...row.map(a=>a.slice()),...eye(n)[i]]);
  for(let j=0;j<n;j++){
   let p=j;for(let i=j+1;i<n;i++)if(norm(T[i][j])>norm(T[p][j]))p=i;
   if(norm(T[p][j])<1e-100)throw Error("singular pivot");
   [T[j],T[p]]=[T[p],T[j]];const v=T[j][j];
   T[j]=T[j].map(a=>div(a,v));
   for(let i=0;i<n;i++)if(i!==j){const f=T[i][j];T[i]=T[i].map((a,k)=>sub(a,mul(f,T[j][k])));}
  }
  return T.map(row=>row.slice(n));
 };
 const det=A=>{
  const n=A.length;if(!n)return z(1);const T=A.map(row=>row.map(a=>a.slice()));let d=z(1);
  for(let j=0;j<n;j++){
   let p=j;for(let i=j+1;i<n;i++)if(norm(T[i][j])>norm(T[p][j]))p=i;
   if(norm(T[p][j])<1e-100)return z();
   if(p!==j){[T[j],T[p]]=[T[p],T[j]];d=neg(d);}
   const v=T[j][j];d=mul(d,v);
   for(let i=j+1;i<n;i++){const f=div(T[i][j],v);for(let k=j+1;k<n;k++)T[i][k]=sub(T[i][k],mul(f,T[j][k]));}
  }
  return d;
 };
 const quad=(u,A,v=u)=>u.reduce((s,a,i)=>add(s,mul(conj(a),A[i].reduce((r,b,j)=>add(r,mul(b,v[j])),z()))),z());
 const rsolve=(A,b)=>{
  const T=A.map((row,i)=>[...row,b[i]]),n=b.length;
  for(let j=0;j<n;j++){
   let p=j;for(let i=j+1;i<n;i++)if(Math.abs(T[i][j])>Math.abs(T[p][j]))p=i;
   if(Math.abs(T[p][j])<1e-100)throw Error("singular real pivot");
   [T[j],T[p]]=[T[p],T[j]];const v=T[j][j];for(let k=j;k<=n;k++)T[j][k]/=v;
   for(let i=0;i<n;i++)if(i!==j){const f=T[i][j];for(let k=j;k<=n;k++)T[i][k]-=f*T[j][k];}
  }
  return T.map(row=>row[n]);
 };
 const dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
 const frobReal=(A,B)=>tr(mm(A,B))[0];
 const basis=[];
 for(let i=0;i<3;i++){const E=zero(3);E[i][i]=z(1);basis.push(E);}
 for(let i=0;i<3;i++)for(let j=i+1;j<3;j++){
  const R=zero(3),J=zero(3);R[i][j]=R[j][i]=z(1/Math.sqrt(2));
  J[i][j]=z(0,1/Math.sqrt(2));J[j][i]=conj(J[i][j]);basis.push(R,J);
 }
 const cases=[
  {name:"certified_center",a:.104,b:.106,c:z(0,.105),scales:[1,1,1]},
  {name:"large_real_triangle",a:.8,b:.8,c:z(.8),scales:[1,1,1]},
  {name:"large_complex_triangle",a:.45,b:.5,c:z(0,.55),scales:[1,1,1]},
  {name:"unequal_complex_triangle",a:.8,b:.15,c:z(0,.2),scales:[1,1,1]},
  {name:"two_edge_path",a:.8,b:.5,c:z(0),scales:[1,1,1]},
  {name:"near_two_plus_one",a:.8,b:.01,c:z(0,.01),scales:[1,1,1]},
  {name:"near_boundary_unequal",a:.99,b:.01,c:z(0,.01),scales:[1,1,1]},
  {name:"unequal_diagonal_scales",a:.7,b:.4,c:z(0,.3),scales:[.01,1,100]},
  {name:"very_near_boundary_pair",a:.999,b:.0001,c:z(0,.0001),scales:[1,1,1]},
  {name:"extremely_near_boundary_pair",a:.999999,b:.0001,c:z(0,.0001),scales:[1,1,1]},
  {name:"large_equal_diagonal_scales",a:.9,b:.05,c:z(0,.05),scales:[100,100,1]},
  {name:"opposite_diagonal_scales",a:.9,b:.05,c:z(0,.05),scales:[.01,100,1]},
  {name:"near_boundary_real_cycle",a:.99,b:.5,c:z(.5),scales:[1,1,1]},
  {name:"near_boundary_real_cycle_scaled",a:.99,b:.5,c:z(.5),scales:[10,10,.1]},
  {name:"boundary_pair_moderate_coupling",a:.999999,b:.0005,c:z(0,.0005),scales:[1,1,1]},
  {name:"boundary_pair_stronger_coupling",a:.999999,b:.0009,c:z(0,.0009),scales:[1,1,1]},
  {name:"boundary_pair_less_extreme",a:.9999,b:.009,c:z(0,.009),scales:[1,1,1]}
 ];
 const results=[];
 for(const spec of cases){
  const {a,b,c,scales}=spec;
  const L=[[z(1),z(a),conj(c)],[z(a),z(1),z(b)],[c,z(b),z(1)]].map((row,i)=>row.map((v,j)=>mul(z(Math.sqrt(scales[i]*scales[j])),v)));
  if(det(L)[0]<=0)throw Error("nonpositive L input "+spec.name);
  const inverse=inv(L.map((row,i)=>row.map((v,j)=>add(v,z(i===j?1:0)))));
  const K=inverse.map((row,i)=>row.map((v,j)=>sub(z(i===j?1:0),v)));
  const x=a*a,y=b*b,zz=norm(c),D=1-x-y-zz+2*a*b*c[0];
  const cp=[-Math.log1p(-y),-Math.log1p(-zz),-Math.log1p(-x)];
  const ct=Math.log1p(-x)+Math.log1p(-y)+Math.log1p(-zz)-Math.log(D);
  const M=K.map((row,i)=>row.map((v,j)=>add(mul(z(ct),v),z(i===j?cp[i]:0))));
  const delta=det(M)[0];if(!(delta>0))throw Error("M not positive in connected case");
  const features=[];
  for(let i=0;i<3;i++)for(let mask=0;mask<(1<<i);mask++){
   const Q=K.slice(0,i).map((row,j)=>row.slice(0,i).map((v,k)=>sub(v,z(j===k&&!(mask&(1<<j))?1:0))));
   const R=inv(Q);const w=Array.from({length:3},()=>z());w[i]=z(1);
   for(let j=0;j<i;j++)w[j]=neg(R[j].reduce((s,v,k)=>add(s,mul(v,K[k][i])),z()));
   let conditional=K[i][i][0];
   for(let j=0;j<i;j++)conditional+=mul(K[i][j],w[j])[0];
   let omitted=0;for(let j=0;j<i;j++)if(!(mask&(1<<j)))omitted++;
   const pi=(omitted%2?-1:1)*det(Q)[0],omega=pi/(conditional*(1-conditional));
   if(!(pi>0&&conditional>0&&conditional<1&&omega>0))throw Error("invalid history");
   features.push({w,omega,gradient:basis.map(E=>quad(w,E)[0])});
  }
  const F=Array.from({length:9},()=>Array(9).fill(0)),Fatom=Array.from({length:9},()=>Array(9).fill(0));
  for(const f of features)for(let i=0;i<9;i++)for(let j=0;j<9;j++)F[i][j]+=f.omega*f.gradient[i]*f.gradient[j];
  let probabilitySum=0;
  for(let mask=0;mask<8;mask++){
   let omitted=0;for(let j=0;j<3;j++)if(!(mask&(1<<j)))omitted++;
   const Q=K.map((row,i)=>row.map((v,j)=>sub(v,z(i===j&&!(mask&(1<<i))?1:0))));
   const p=(omitted%2?-1:1)*det(Q)[0],R=inv(Q),scores=basis.map(E=>frobReal(R,E));probabilitySum+=p;
   for(let i=0;i<9;i++)for(let j=0;j<9;j++)Fatom[i][j]+=p*scores[i]*scores[j];
  }
  let fisherError=0,fisherScale=0;
  for(let i=0;i<9;i++)for(let j=0;j<9;j++){fisherError=Math.max(fisherError,Math.abs(F[i][j]-Fatom[i][j]));fisherScale=Math.max(fisherScale,Math.abs(Fatom[i][j]));}
  const bet=features.map(f=>quad(f.w,M)[0]);
  const C=features.map((f,i)=>features.map((g,j)=>norm(quad(f.w,M,g.w))+(i===j?delta/f.omega:0)));
  const seven=dot(bet,rsolve(C,bet));
  const Sinv=inv(M),ell=basis.map(E=>frobReal(Sinv,E));
  const N=basis.map((E,i)=>basis.map((V,j)=>F[i][j]+delta*tr(mm(mm(mm(Sinv,E),Sinv),V))[0]));
  const nine=delta*dot(ell,rsolve(N,ell));
  const Sigma=K.map((row,i)=>row.map((v,j)=>i===j?K[i][i][0]*(1-K[i][i][0]):-norm(v)));
  const d=K.map((_,i)=>M[i][i][0]);
  const C3=M.map((row,i)=>row.map((v,j)=>norm(v)+delta*Sigma[i][j]));
  const three=dot(d,rsolve(C3,d));
  const variance=Sigma.reduce((s,row)=>s+row.reduce((t,v)=>t+v,0),0);
  const trM=tr(M)[0],trM2=tr(mm(M,M))[0];
  const traceOnly=trM*trM/(trM2+variance*delta);
  if(Math.abs(probabilitySum-1)>1e-10)throw Error("probability normalization");
  if(fisherError/Math.max(1,fisherScale)>1e-9)throw Error("conditional Fisher discrepancy");
  if(Math.abs(nine-(3-seven))>1e-7)throw Error("Schur criterion discrepancy");
  results.push({case:spec.name,sevenFeatureValue:seven,threeMarginalValue:three,traceOnlyValue:traceOnly,
   requiredThreshold:2,rankOneScalar:nine,rankOneRequiredUpperBound:1,
   conditionalFisherRelativeError:fisherError/Math.max(1,fisherScale),SchurDiscrepancy:Math.abs(nine-(3-seven))});
 }
 return {status:"PASS; bounded floating-point diagnostics only",cases:results};
})();
if(typeof console!=="undefined" && typeof console.log==="function") console.log(JSON.stringify(diagnostics097,null,2));
diagnostics097;
