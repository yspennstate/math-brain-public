#include <algorithm>
#include <array>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_set>
#include <vector>
using namespace std;

static inline int psi12(int k){ k=abs(k); if(k==0) return 8; if(k==1) return 13; return 12*k; }
struct Tup { int a,b,c,d,e,f; bool operator==(Tup const&o) const {return tie(a,b,c,d,e,f)==tie(o.a,o.b,o.c,o.d,o.e,o.f);} };
struct TupHash { size_t operator()(Tup const&k) const { size_t h=0; int v[6]={k.a,k.b,k.c,k.d,k.e,k.f}; for(int x:v) h=h*1009+(x+500); return h; } };

static void hungarian11(const double cost[11][11], int assign[11]){
    const int n=11; double u[12]={},v[12]={}; int p[12]={},way[12]={};
    for(int i=1;i<=n;i++){
        p[0]=i; int j0=0; double minv[12]; bool used[12]={}; for(int j=1;j<=n;j++) minv[j]=1e100;
        do{
            used[j0]=true; int i0=p[j0],j1=0; double delta=1e100;
            for(int j=1;j<=n;j++) if(!used[j]){
                double cur=cost[i0-1][j-1]-u[i0]-v[j];
                if(cur<minv[j]){minv[j]=cur;way[j]=j0;}
                if(minv[j]<delta){delta=minv[j];j1=j;}
            }
            for(int j=0;j<=n;j++) if(used[j]){u[p[j]]+=delta;v[j]-=delta;} else if(j) minv[j]-=delta;
            j0=j1;
        }while(p[j0]!=0);
        do{int j1=way[j0]; p[j0]=p[j1]; j0=j1;}while(j0);
    }
    for(int j=1;j<=n;j++) assign[p[j]-1]=j-1;
}
vector<vector<pair<int,int>>> factorization10(vector<int> vv){
    vector<vector<pair<int,int>>> out;
    for(int r=0;r<9;r++){
        vector<pair<int,int>> ps; ps.push_back({vv[9],vv[r]});
        for(int i=1;i<5;i++) ps.push_back({vv[(r+i)%9],vv[(r-i+9)%9]});
        out.push_back(ps);
    }
    return out;
}
struct Slot{char typ;int z;};
using P13=array<unsigned char,13>;
P13 invp(const P13&p){P13 q;for(int i=0;i<13;i++)q[p[i]]=i;return q;}
P13 revc(const P13&p){P13 q;for(int i=0;i<13;i++)q[i]=12-p[12-i];return q;}
string enc(const P13&p){string s(13,'\0');for(int i=0;i<13;i++)s[i]=char(p[i]);return s;}

struct Mom { double ELQ,ELA,EHQ,EHA,EQ,EA,ETQ; };
Mom mom_for_k(int k){
  if(k==0) return {-0.38675585932813344,0.6132441406718666,0.1575922705342496,0.8280406602432294,-0.11458179439694192,0.720642400457548,0.036726857470608304};
  return {-0.25966451760925674,0.7403354823907433,0.25966451760925674,0.7403354823907433,0.0,0.7403354823907433,0.08927460489951043};
}

int main(int argc,char**argv){
    if(argc<5){cerr<<"usage: prog k fixed.csv adapt.csv reps.csv\n";return 2;}
    int k=atoi(argv[1]); if(k<0||k>1)return 2; Mom mm=mom_for_k(k);
    vector<int> rem; for(int q=1;q<11;q++) rem.push_back(q); auto fac=factorization10(rem); int rhsround[5]={0,1,2,3,5};
    vector<array<Slot,11>> tils;
    for(int rr:rhsround){array<Slot,11> sl; int c=0; for(auto [a,b]:fac[0])sl[c++]={'L',a+b-10}; for(auto [a,b]:fac[rr])sl[c++]={'H',a+b-10}; sl[c++]={'V',-10}; tils.push_back(sl);}

    array<int,11> sig; iota(sig.begin(),sig.end(),0);
    long long total=0,unipass=0,unifail=0,fixedpass=0,adaptpass=0,remain=0; int min_unipass=1e9,max_unifail=-1e9; long long uses[5]={};
    unordered_set<Tup,TupHash> fixedtuples, adapttuples; unordered_set<string> reps;
    const int N=13, rhs=8*N*N*N*N;
    do{
        ++total; int gp[13]; iota(gp,gp+13,0); for(int i=0;i<11;i++)gp[k+i]=k+sig[i];
        long long half=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){int d=i-j,e=gp[i]-gp[j];half += (long long)abs(d-e)*psi12(d+e);} long long margin=5*(2*half)-rhs;
        if(margin>=0){++unipass;min_unipass=min<long long>(min_unipass,margin);continue;} ++unifail;max_unifail=max<long long>(max_unifail,margin);
        struct Br{int j,s,d;}; vector<Br> br; for(int j=0;j<11;j++)br.push_back({j,j+sig[j],j-sig[j]}); sort(br.begin(),br.end(),[](auto&x,auto&y){if(x.s!=y.s)return x.s<y.s;if(x.d!=y.d)return x.d<y.d;return x.j<y.j;});
        vector<Br> low(br.begin(),br.begin()+5),high(br.begin()+6,br.end());Br vert=br[5];sort(low.begin(),low.end(),[](auto&x,auto&y){return x.d<y.d;});sort(high.begin(),high.end(),[](auto&x,auto&y){return x.d<y.d;});int nums[5]={-9,-5,0,5,9};int CSL=0,CSH=0,ZL=0,ZH=0;for(int i=0;i<5;i++){CSL+=low[i].s;ZL+=low[i].d*nums[i];CSH+=high[i].s-2;ZH+=high[i].d*nums[i];}int sV=vert.s,ZV=0;
        double T=CSL*mm.ELQ+CSH*mm.EHQ+sV*mm.EQ+(ZL/11.0)*mm.ELA+(ZH/11.0)*mm.EHA-200*mm.ETQ;
        if(T>1e-9){++fixedpass;fixedtuples.insert({CSL,CSH,sV,ZL,ZH,ZV});continue;}
        int s[11],d[11];for(int j=0;j<11;j++){s[j]=j+sig[j];d[j]=j-sig[j];}bool ok=false;
        for(int ti=0;ti<5&&!ok;ti++){
            double C[11][11];auto&sl=tils[ti];for(int j=0;j<11;j++)for(int c=0;c<11;c++){double z=sl[c].z/11.0,score;if(sl[c].typ=='L')score=s[j]*mm.ELQ+d[j]*z*mm.ELA;else if(sl[c].typ=='H')score=(s[j]-2)*mm.EHQ+d[j]*z*mm.EHA;else score=s[j]*mm.EQ+d[j]*z*mm.EA;C[j][c]=-score;}
            int asg[11];hungarian11(C,asg);CSL=CSH=sV=ZL=ZH=ZV=0;for(int j=0;j<11;j++){auto slot=sl[asg[j]];if(slot.typ=='L'){CSL+=s[j];ZL+=d[j]*slot.z;}else if(slot.typ=='H'){CSH+=s[j]-2;ZH+=d[j]*slot.z;}else{sV=s[j];ZV=d[j]*slot.z;}}
            T=CSL*mm.ELQ+CSH*mm.EHQ+sV*mm.EQ+(ZL/11.0)*mm.ELA+(ZH/11.0)*mm.EHA+(ZV/11.0)*mm.EA-200*mm.ETQ;
            if(T>1e-8){ok=true;++adaptpass;++uses[ti];adapttuples.insert({CSL,CSH,sV,ZL,ZH,ZV});}
        }
        if(ok)continue;
        ++remain;P13 p;for(int i=0;i<13;i++)p[i]=gp[i];P13 a=invp(p),b=revc(p),c=invp(b);P13 best=min(min(p,a),min(b,c));reps.insert(enc(best));
    }while(next_permutation(sig.begin(),sig.end()));

    ofstream f1(argv[2]), f2(argv[3]), f3(argv[4]);
    for(const auto &x: fixedtuples) f1<<x.a<<","<<x.b<<","<<x.c<<","<<x.d<<","<<x.e<<","<<x.f<<"\n";
    for(const auto &x: adapttuples) f2<<x.a<<","<<x.b<<","<<x.c<<","<<x.d<<","<<x.e<<","<<x.f<<"\n";
    for(const auto &s0: reps){ for(int i=0;i<13;i++){ if(i) f3<<","; f3<<(int)(unsigned char)s0[i]; } f3<<"\n"; }
    cout<<"k="<<k<<" total="<<total<<"\n";
    cout<<"universal_pass="<<unipass<<" universal_fail="<<unifail<<" min_pass="<<min_unipass<<" max_fail="<<max_unifail<<"\n";
    cout<<"fixed_pass="<<fixedpass<<" fixed_unique_tuples="<<fixedtuples.size()<<"\n";
    cout<<"adaptive_pass="<<adaptpass<<" uses=";for(int i=0;i<5;i++)cout<<(i?",":"")<<uses[i];cout<<" adaptive_unique_tuples="<<adapttuples.size()<<"\n";
    cout<<"remain="<<remain<<" canonical_reps="<<reps.size()<<"\n";
    bool okcounts=false;
    if(k==0) okcounts = total==39916800LL && unipass==37659311LL && unifail==2257489LL && min_unipass==2 && max_unifail==-8 && fixedpass==1995003LL && fixedtuples.size()==127855 && adaptpass==77697LL && adapttuples.size()==3342 && remain==184789LL && reps.size()==144849;
    if(k==1) okcounts = total==39916800LL && unipass==37109281LL && unifail==2807519LL && min_unipass==2 && max_unifail==-8 && fixedpass==2634546LL && fixedtuples.size()==165348 && adaptpass==68119LL && adapttuples.size()==2936 && remain==104854LL && reps.size()==58765;
    if(!okcounts){ cerr<<"ASSERTION FAILURE\n"; return 3; }
    cout<<"EXACT/LOCATOR S11 N13 PHASE1+DOMINO CENSUS PASSED\n";
    return 0;
}
