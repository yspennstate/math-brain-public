"use strict";
(() => {
  // Exact rational-complex checks for Agent096's independent audit of Agent081.
  // Standalone JavaScript; no dependencies, floating-point arithmetic, or network.
  // This is a finite algebra check, not a proof assistant certificate.
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
  class F{
    constructor(n=0n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
    add(b){return new F(this.n*b.d+b.n*this.d,this.d*b.d);}
    neg(){return new F(-this.n,this.d);}
    sub(b){return this.add(b.neg());}
    mul(b){return new F(this.n*b.n,this.d*b.d);}
    div(b){return new F(this.n*b.d,this.d*b.n);}
    eq(b){return this.n===b.n&&this.d===b.d;}
    str(){return this.d===1n?String(this.n):this.n+"/"+this.d;}
  }
  const f=(n,d=1)=>new F(n,d),fz=f(0),fo=f(1);
  class Z{
    constructor(r=fz,i=fz){this.r=r;this.i=i;}
    add(b){return new Z(this.r.add(b.r),this.i.add(b.i));}
    neg(){return new Z(this.r.neg(),this.i.neg());}
    sub(b){return this.add(b.neg());}
    mul(b){return new Z(this.r.mul(b.r).sub(this.i.mul(b.i)),this.r.mul(b.i).add(this.i.mul(b.r)));}
    conj(){return new Z(this.r,this.i.neg());}
    norm2(){return this.r.mul(this.r).add(this.i.mul(this.i));}
    div(b){const d=b.norm2();const t=this.mul(b.conj());return new Z(t.r.div(d),t.i.div(d));}
    eq(b){return this.r.eq(b.r)&&this.i.eq(b.i);}
    zero(){return this.r.n===0n&&this.i.n===0n;}
    str(){return this.i.n===0n?this.r.str():"("+this.r.str()+","+this.i.str()+")";}
  }
  const z=(n,d=1,im=0,id=1)=>new Z(f(n,d),f(im,id)),zz=z(0),zo=z(1);
  const copy=A=>A.map(r=>r.slice());
  const zeros=(m,n)=>Array.from({length:m},()=>Array.from({length:n},()=>zz));
  const eye=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?zo:zz));
  const add=(A,B)=>A.map((r,i)=>r.map((x,j)=>x.add(B[i][j])));
  const scale=(s,A)=>A.map(r=>r.map(x=>s.mul(x)));
  const star=A=>A[0].map((_,j)=>A.map(r=>r[j].conj()));
  function mul(A,B){return A.map(r=>B[0].map((_,j)=>r.reduce((s,x,k)=>s.add(x.mul(B[k][j])),zz)));}
  const trace=A=>A.reduce((s,r,i)=>s.add(r[i]),zz);
  function det(A){
    if(!A.length)return zo;
    let d=zz;
    for(let j=0;j<A.length;j++){
      const minor=A.slice(1).map(r=>r.filter((_,k)=>k!==j));
      const term=A[0][j].mul(det(minor));d=j%2?d.sub(term):d.add(term);
    }
    return d;
  }
  function inv(A){
    const n=A.length;if(!n)return [];
    const M=A.map((r,i)=>r.concat(eye(n)[i]));
    for(let j=0;j<n;j++){
      let p=j;while(p<n&&M[p][j].zero())p++;if(p===n)throw Error("singular");
      [M[p],M[j]]=[M[j],M[p]];const piv=M[j][j];M[j]=M[j].map(x=>x.div(piv));
      for(let i=0;i<n;i++)if(i!==j){const t=M[i][j];M[i]=M[i].map((x,k)=>x.sub(t.mul(M[j][k])));}
    }return M.map(r=>r.slice(n));
  }
  const real=x=>{if(x.i.n!==0n)throw Error("not real "+x.str());return x.r;};
  let checks=0;
  function eq(a,b,label){checks++;if(!a.eq(b))throw Error(label+": "+a.str()+" != "+b.str());}
  function matrixEq(A,B,label){A.forEach((r,i)=>r.forEach((x,j)=>eq(x,B[i][j],label+"["+i+","+j+"]")));}
  function positive(q,label){checks++;if(q.n<=0n)throw Error(label+" not positive");}
  function atoms(K){
    const n=K.length;return Array.from({length:1<<n},(_,mask)=>{
      const Q=K.map((r,i)=>r.map((v,j)=>i===j&&!(mask&(1<<i))?v.sub(zo):v));
      let p=det(Q);if((n-popcount(mask))%2)p=p.neg();
      const pr=real(p);positive(pr,"atom");return {mask,p:pr,R:inv(Q)};
    });
  }
  function popcount(mask){let k=0;for(;mask;mask>>=1)k+=mask&1;return k;}
  function features(K){
    const out=[];
    for(let i=0;i<K.length;i++){
      const prefix=K.slice(0,i).map(r=>r.slice(0,i));
      const histories=i?atoms(prefix):[{mask:0,p:fo}];
      for(const h of histories){
        const v=Array.from({length:K.length},()=>zz);v[i]=zo;
        let q=K[i][i];
        if(i){
          const Q=prefix.map((r,a)=>r.map((x,b)=>a===b&&!(h.mask&(1<<a))?x.sub(zo):x));
          const column=K.slice(0,i).map(r=>[r[i]]);
          const vF=mul(inv(Q),column).map(r=>r[0].neg());
          for(let j=0;j<i;j++)v[j]=vF[j];
          q=q.add(K[i].slice(0,i).reduce((s,x,j)=>s.add(x.mul(vF[j])),zz));
        }
        const qr=real(q);positive(qr,"q");positive(fo.sub(qr),"1-q");
        out.push({stage:i,mask:h.mask,p:h.p,q:qr,v,omega:h.p.div(qr.mul(fo.sub(qr)))});
      }
    }return out;
  }
  function evalForm(v,A,w=v){
    return v.reduce((s,x,i)=>s.add(x.conj().mul(A[i].reduce((t,y,j)=>t.add(y.mul(w[j])),zz))),zz);
  }
  function hermitianBasis(n){
    const out=[];for(let i=0;i<n;i++){const A=zeros(n,n);A[i][i]=zo;out.push(A);}
    for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
      const A=zeros(n,n);A[i][j]=zo;A[j][i]=zo;out.push(A);
      const B=zeros(n,n);B[i][j]=z(0,1,1);B[j][i]=z(0,1,-1);out.push(B);
    }return out;
  }
  function verifyFisher(K,label){
    const aa=atoms(K),ff=features(K),basis=hermitianBasis(K.length);
    eq(aa.reduce((s,a)=>s.add(a.p),fz),fo,label+" normalization");
    let mean=zeros(K.length,K.length);
    for(const a of aa)mean=add(mean,scale(new Z(a.p),a.R));
    matrixEq(mean,zeros(K.length,K.length),label+" mean R");
    for(const h of ff){
      const allowed=aa.filter(a=>(a.mask&((1<<h.stage)-1))===h.mask);
      const den=allowed.reduce((s,a)=>s.add(a.p),fz);
      const num=allowed.filter(a=>a.mask&(1<<h.stage)).reduce((s,a)=>s.add(a.p),fz);
      eq(den,h.p,label+" history probability");
      eq(num.div(den),h.q,label+" conditional inclusion probability");
    }
    for(const A of basis){
      for(const h of ff){
        const allowed=aa.filter(a=>(a.mask&((1<<h.stage)-1))===h.mask);
        const den=allowed.reduce((s,a)=>s.add(a.p),fz);
        const num=allowed.filter(a=>a.mask&(1<<h.stage)).reduce((s,a)=>s.add(a.p),fz);
        const denPrime=allowed.reduce((s,a)=>s.add(a.p.mul(real(trace(mul(a.R,A))))),fz);
        const numPrime=allowed.filter(a=>a.mask&(1<<h.stage)).reduce((s,a)=>s.add(a.p.mul(real(trace(mul(a.R,A))))),fz);
        const dq=numPrime.mul(den).sub(num.mul(denPrime)).div(den.mul(den));
        eq(dq,real(evalForm(h.v,A)),label+" rank-one conditional derivative");
      }
      for(const a of aa){
        let score=fz;
        for(let i=0;i<K.length;i++){
          const h=ff.find(h=>h.stage===i&&h.mask===(a.mask&((1<<i)-1)));
          const dq=real(evalForm(h.v,A));
          const xi=(a.mask&(1<<i))?fo:fz;
          score=score.add(xi.sub(h.q).mul(dq).div(h.q.mul(fo.sub(h.q))));
        }
        eq(score,real(trace(mul(a.R,A))),label+" martingale score");
      }
      for(const C of basis){
        const lhs=aa.reduce((s,a)=>s.add(a.p.mul(real(trace(mul(a.R,A)))).mul(real(trace(mul(a.R,C))))),fz);
        const rhs=ff.reduce((s,h)=>s.add(h.omega.mul(real(evalForm(h.v,A))).mul(real(evalForm(h.v,C)))),fz);
        eq(lhs,rhs,label+" Fisher bilinear");
      }
    }
    return {atoms:aa.length,features:ff.length,basis:basis.length};
  }
  const M=[
    [z(2,5),z(1,10,1,15)],
    [z(1,10,-1,15),z(3,5)]
  ];
  const N=[
    [z(1,3),z(1,12,-1,20)],
    [z(1,12,1,20),z(2,3)]
  ];
  const K3=[
    [z(1,2),z(1,20,1,30),z(-1,25,1,40)],
    [z(1,20,-1,30),z(2,5),z(1,35,-1,45)],
    [z(-1,25,-1,40),z(1,35,1,45),z(3,5)]
  ];
  // Strict row diagonal dominance of K and I-K also independently proves
  // these chosen Hermitian kernels are interior contractions.
  const fisher=[verifyFisher(M,"M"),verifyFisher(N,"N"),verifyFisher(K3,"K3")];
  const B=[[z(1,3,1,7),z(-2,5,1,11)],[z(3,8,-1,9),z(1,4,2,13)]];
  const C=[[z(-1,6,2,9),z(1,5,-1,12)],[z(2,7,1,10),z(-3,11,1,8)]];
  function atomQuartic(Ablock,Bblock,X){
    return atoms(Ablock).reduce((s,a)=>s.add(atoms(Bblock).reduce((t,b)=>{
      const v=real(trace(mul(mul(mul(a.R,X),b.R),star(X))));
      return t.add(a.p.mul(b.p).mul(v).mul(v));
    },fz)),fz);
  }
  function featureQuartic(Ablock,Bblock,X){
    let out=fz;for(const a of features(Ablock))for(const b of features(Bblock)){
      const norm=evalForm(a.v,X,b.v).norm2();
      out=out.add(a.omega.mul(b.omega).mul(norm).mul(norm));
    }return out;
  }
  for(let t=-2;t<=2;t++){
    const X=add(B,scale(z(t),C));
    eq(atomQuartic(M,N,X),featureQuartic(M,N,X),"quartic polynomial at t="+t);
  }
  // Five distinct parameter checks certify equality of the degree <=4
  // polynomials along this particular affine line.
  let featureHessian=fz,atomHessian=fz;
  for(const a of features(M))for(const b of features(N)){
    const v=evalForm(a.v,B,b.v),u=evalForm(a.v,C,b.v);
    const mixed=v.conj().mul(u).r;
    const term=f(4).mul(v.norm2()).mul(u.norm2()).add(f(8).mul(mixed).mul(mixed));
    featureHessian=featureHessian.add(a.omega.mul(b.omega).mul(term));
  }
  for(const a of atoms(M))for(const b of atoms(N)){
    const r0=real(trace(mul(mul(mul(a.R,B),b.R),star(B))));
    const r2=real(trace(mul(mul(mul(a.R,C),b.R),star(C))));
    const r1=real(trace(add(mul(mul(mul(a.R,C),b.R),star(B)),mul(mul(mul(a.R,B),b.R),star(C)))));
    atomHessian=atomHessian.add(a.p.mul(b.p).mul(f(2).mul(r1.mul(r1).add(f(2).mul(r0).mul(r2)))));
  }
  eq(atomHessian,featureHessian,"quartic Hessian");positive(featureHessian,"sample Hessian");
  function checkTwoSiteIdentities(K,label){
    const pp=atoms(K).map(a=>a.p),[x,y,u,w]=pp,s=K[0][1].norm2();
    eq(y.mul(u).sub(x.mul(w)),s,label+" yu-xw");
    const adjM=[[K[1][1],K[0][1].neg()],[K[1][0].neg(),K[0][0]]];
    const adjI=[[zo.sub(K[1][1]),K[0][1]],[K[1][0],zo.sub(K[0][0])]];
    eq(real(det(adjM)),w,label+" det adjM");
    eq(real(det(adjI)),x,label+" det adj(I-M)");
    const cross=adjM[0][0].mul(adjI[1][1]).add(adjM[1][1].mul(adjI[0][0]))
      .sub(adjM[0][1].mul(adjI[1][0])).sub(adjM[1][0].mul(adjI[0][1]));
    eq(real(cross),y.add(u),label+" determinant cross coefficient");
    // This is the coefficient identity behind det(P+Q)=2+(y+u)/sqrt(xw);
    // no approximate square root is used.
    const directions=hermitianBasis(2).concat([
      eye(2),
      [[z(2,7),z(1,8,1,9)],[z(1,8,-1,9),z(-3,10)]],
      [[zo,z(1,1,1)],[z(1,1,-1),z(2)]]
    ]);
    for(const D of directions){
      const delta=real(det(D));
      for(let mask=0;mask<4;mask++){
        function atomAt(t){
          const J=add(K,scale(z(t),D));
          const Q=J.map((r,i)=>r.map((v,j)=>i===j&&!(mask&(1<<i))?v.sub(zo):v));
          let p=det(Q);if((2-popcount(mask))%2)p=p.neg();return real(p);
        }
        const dd=atomAt(1).add(atomAt(-1)).sub(f(2).mul(atomAt(0)));
        const expected=f(mask===0||mask===3?2:-2).mul(delta);
        eq(dd,expected,label+" atom second derivative");
      }
    }
  }
  checkTwoSiteIdentities(M,"M");checkTwoSiteIdentities(N,"N");
  const half=[[z(1,2),zz],[zz,z(1,2)]],E11=[[zo,zz],[zz,zz]],E22=[[zz,zz],[zz,zo]];
  eq(atomQuartic(half,half,E11),f(16),"disconnected coefficient");
  eq(atomQuartic(half,half,add(E11,E22)),f(32),"disconnected disjoint support");
  // kappa(E11+t E22)=16(1+t^4), verified as a degree <=4 polynomial.
  for(let t=-2;t<=2;t++){
    eq(atomQuartic(half,half,add(E11,scale(z(t),E22))),f(16*(1+t*t*t*t)),
       "disconnected zero Hessian polynomial t="+t);
  }
  const diagonal3=[[z(2,5),zz,zz],[zz,z(1,3),zz],[zz,zz,z(3,7)]];
  const off3=[
    [zz,z(1,4,1,7),z(-1,6,1,8)],
    [z(1,4,-1,7),zz,z(2,9,-1,10)],
    [z(-1,6,-1,8),z(2,9,1,10),zz]
  ];
  let degreeFive=fz,pairCovariance=fz;
  for(const a of atoms(diagonal3)){
    const X=mul(a.R,off3);
    const F2=real(trace(mul(X,X))).mul(f(-1,2));
    const F3=real(trace(mul(mul(X,X),X))).mul(f(1,3));
    degreeFive=degreeFive.add(a.p.mul(F2).mul(F3));
    const T01=real(a.R[0][0].mul(a.R[1][1])).mul(off3[0][1].norm2());
    const T12=real(a.R[1][1].mul(a.R[2][2])).mul(off3[1][2].norm2());
    pairCovariance=pairCovariance.add(a.p.mul(T01).mul(T12));
  }
  eq(degreeFive,fz,"all-block fifth-order cancellation");
  eq(pairCovariance,fz,"distinct-pair orthogonality");
  const report={
    status:"PASS",
    arithmetic:"Exact BigInt rational complex arithmetic",
    assertions:checks,
    fisher,
    quartic_line_parameter_checks:5,
    quartic_hessian_match:true,
    internal_determinant_and_atom_derivative_identities:true,
    all_block_fifth_order_and_pair_cancellation:true,
    disconnected_flat_hessian_counterexample:"kappa(E11+t E22)=16(1+t^4)",
    limitation:"Finite exact algebra checks supplement the written general proof; they do not prove the analytic estimates or universal statements."
  };
  if(typeof console!=="undefined")console.log(JSON.stringify(report,null,2));
  return report;
})();
