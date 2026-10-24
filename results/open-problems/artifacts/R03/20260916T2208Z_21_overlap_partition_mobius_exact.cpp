#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

static cpp_int absbi(cpp_int x){ return x<0?-x:x; }
static cpp_int gcdbi(cpp_int a, cpp_int b){ a=absbi(a); b=absbi(b); while(b!=0){ cpp_int r=a%b; a=b; b=r;} return a; }
struct Rat { cpp_int n,d; Rat(cpp_int N=0, cpp_int D=1):n(N),d(D){ norm(); } void norm(){ if(d<0){d=-d;n=-n;} cpp_int g=gcdbi(n,d); if(g!=0){n/=g;d/=g;} } };
Rat operator+(Rat a,Rat b){ return Rat(a.n*b.d+b.n*a.d,a.d*b.d); }
Rat operator-(Rat a,Rat b){ return Rat(a.n*b.d-b.n*a.d,a.d*b.d); }
Rat operator*(Rat a,Rat b){ return Rat(a.n*b.n,a.d*b.d); }
long double to_ld(const cpp_int& x){ return x.convert_to<long double>(); }
long double to_ld(Rat a){ return to_ld(a.n)/to_ld(a.d); }

cpp_int fall_int(int a,int m){ if(a<m) return 0; cpp_int r=1; for(int j=0;j<m;j++) r*=a-j; return r; }
long long factll(int n){ long long r=1; for(int i=2;i<=n;i++)r*=i; return r; }
long long C(int n,int k){ if(k<0||k>n)return 0; k=min(k,n-k); long long r=1; for(int i=1;i<=k;i++) r=r*(n-k+i)/i; return r; }
long long Ls(int s){ return s%2?C(s,s/2):C(s,s/2)/2; }

struct Cl{ string lab; long long cnt; vector<int> coeff; };
vector<Cl> classes(int s){
    vector<Cl> o;
    if(s%2==0){ int a=s/2; vector<int> c{1}; c.insert(c.end(),a-1,1); c.insert(c.end(),a,-1); o.push_back({"even",Ls(s),c}); }
    else { int a=s/2; vector<int> cm{1}; cm.insert(cm.end(),a-1,1); cm.insert(cm.end(),a+1,-1); vector<int> cj{1}; cj.insert(cj.end(),a,1); cj.insert(cj.end(),a,-1); o.push_back({"min",C(s-1,a-1),cm}); o.push_back({"maj",C(s-1,a),cj}); }
    return o;
}
vector<int> canonical_bal(int m,int s,int start){ vector<int> v(m); auto cs=classes(s).back().coeff; for(int j=0;j<s;j++) v[start+j]=cs[j]; return v; }

struct PlaneEval { vector<int> v,w; cpp_int exact_count=0; };
static int M,P; static vector<int> rgs; static vector<PlaneEval>* evals_ptr;

void process_partition(){
    auto &evals=*evals_ptr;
    int nb=*max_element(rgs.begin(),rgs.end())+1;
    vector<int> sz(nb); for(int x:rgs) sz[x]++;
    long long mu=1; for(int z:sz){ long long f=factll(z-1); if((z-1)&1)f=-f; mu*=f; }
    for(auto &e:evals){
        vector<pair<int,int>> ag(nb-1,{0,0});
        for(int i=1;i<=M;i++) if(rgs[i]){
            int b=rgs[i]-1;
            ag[b].first=(ag[b].first+e.v[i-1])%P; if(ag[b].first<0)ag[b].first+=P;
            ag[b].second=(ag[b].second+e.w[i-1])%P; if(ag[b].second<0)ag[b].second+=P;
        }
        int h=0, bcnt=nb-1, lim=1<<bcnt;
        for(int mask=0;mask<lim;mask++){
            int x=0,y=0; for(int j=0;j<bcnt;j++) if(mask>>j&1){x+=ag[j].first;y+=ag[j].second;}
            if(x%P==0 && y%P==0) h++;
        }
        cpp_int term=fall_int(h-1,M);
        if(mu<0) e.exact_count -= term*(-mu); else e.exact_count += term*mu;
    }
}
void gen_part(int i,int maxv){ if(i==M+1){process_partition(); return;} for(int x=0;x<=maxv+1;x++){rgs[i]=x;gen_part(i+1,max(maxv,x));} }
void eval_exact_counts(int m,int p, vector<PlaneEval>& evals){ M=m;P=p;rgs.assign(m+1,0);evals_ptr=&evals; gen_part(1,0); }

bool in_G(const vector<vector<int>>& A){ int m=A.size();
    for(int i=0;i<m;i++){ bool nz=false; for(int j=0;j<m;j++) nz|=A[i][j]; if(!nz)return false; for(int k=0;k<i;k++) if(A[i]==A[k])return false; }
    for(int j=0;j<m;j++){ bool nz=false; for(int i=0;i<m;i++) nz|=A[i][j]; if(!nz)return false; for(int k=0;k<j;k++){ bool eq=true; for(int i=0;i<m;i++) if(A[i][j]!=A[i][k]){eq=false;break;} if(eq)return false; } }
    return true;
}
bool null_contains(const vector<vector<int>>& A,const vector<int>& v,int p){ int m=A.size(); for(int j=0;j<m;j++){ long long s=0; for(int i=0;i<m;i++)s+=1LL*v[i]*A[i][j]; if(((s%p)+p)%p) return false;} return true; }
long long direct_count_small(int m,int p,const vector<int>&v,const vector<int>&w){ long long cnt=0; int bits=m*m; for(unsigned long long mask=0;mask<(1ULL<<bits);mask++){ vector<vector<int>>A(m,vector<int>(m)); for(int z=0;z<bits;z++)A[z/m][z%m]=(mask>>z)&1; if(!in_G(A))continue; if(null_contains(A,v,p)&&null_contains(A,w,p))cnt++; } return cnt; }

vector<int> support_spectrum(const vector<int>&v,const vector<int>&w,int p){ int m=v.size(); vector<int>s; auto supp=[&](const vector<int>&a){int z=0;for(int x:a) if((x%p+p)%p)z++;return z;}; s.push_back(supp(v));s.push_back(supp(w)); for(int lam=1;lam<p;lam++){vector<int>a(m);for(int i=0;i<m;i++)a[i]=(v[i]+lam*w[i])%p;s.push_back(supp(a));} sort(s.begin(),s.end());return s; }

struct Orbit {int s,t; string ls,lt; long long cv,cw; int eval_id;};
struct FamilyResult { cpp_int disjoint=0, overlap1=0; long long overlap_planes=0; };

FamilyResult compute_families(int m,int p){
    vector<PlaneEval> evals; vector<tuple<int,int,int,long long>> dis_meta; vector<Orbit> ov_meta;
    // exact disjoint families retained from run20: 3<=s<=t, max>=5, s+t<=m.
    for(int s=3;s<=m;s++) for(int t=s;t<=m;t++) if(s+t<=m && max(s,t)>=5){
        vector<int>v=canonical_bal(m,s,0), w=canonical_bal(m,t,s); int id=evals.size();evals.push_back({v,w,0});
        long long N; if(s<t)N=C(m,s)*C(m-s,t)*Ls(s)*Ls(t); else N=C(m,s)*C(m-s,s)*Ls(s)*Ls(s)/2;
        dis_meta.push_back({s,t,id,N});
    }
    // new overlap-one families with one low-support line s=3 or4 and t>=5.
    for(int s: {3,4}) for(int t=5;s<t && s+t-1<=m;t++){
        auto cs=classes(s), ct=classes(t);
        for(auto a:cs) for(auto b:ct){
            vector<int>v(m),w(m); for(int j=0;j<s;j++)v[j]=a.coeff[j]; w[0]=b.coeff[0]; for(int j=1;j<t;j++)w[s+j-1]=b.coeff[j];
            auto spec=support_spectrum(v,w,p); vector<int> expected; expected.push_back(s);expected.push_back(t);expected.push_back(s+t-2);for(int z=0;z<p-2;z++)expected.push_back(s+t-1);sort(expected.begin(),expected.end()); if(spec!=expected){cerr<<"spectrum fail\n";exit(2);} int low=0;for(int x:spec)low+=(x<=4);if(low!=1){cerr<<"low-support fail\n";exit(3);} int id=evals.size();evals.push_back({v,w,0});ov_meta.push_back({s,t,a.lab,b.lab,a.cnt,b.cnt,id});
        }
    }
    eval_exact_counts(m,p,evals);
    FamilyResult fr;
    cout<<"CASE m="<<m<<" p="<<p<<"\n";
    for(auto [s,t,id,N]:dis_meta){ cpp_int cont=evals[id].exact_count*N; fr.disjoint+=cont; cout<<"DISJOINT "<<s<<","<<t<<" N="<<N<<" C="<<evals[id].exact_count<<" contrib="<<cont<<"\n"; }
    map<pair<int,int>,cpp_int> fam;
    for(auto&o:ov_meta){ long long supports=C(m,o.s)*o.s*C(m-o.s,o.t-1); long long mult=supports*o.cv*o.cw; cpp_int cont=evals[o.eval_id].exact_count*mult; fr.overlap1+=cont;fr.overlap_planes+=mult;fam[{o.s,o.t}]+=cont; cout<<"OVERLAP1 "<<o.s<<","<<o.t<<" "<<o.ls<<","<<o.lt<<" mult="<<mult<<" C="<<evals[o.eval_id].exact_count<<" contrib="<<cont<<"\n"; }
    for(auto &kv:fam)cout<<"OVERLAP1_FAMILY "<<kv.first.first<<","<<kv.first.second<<" contrib="<<kv.second<<"\n";
    cout<<"DISJOINT_TOTAL "<<fr.disjoint<<"\nOVERLAP1_PLANES "<<fr.overlap_planes<<"\nOVERLAP1_TOTAL "<<fr.overlap1<<"\n";
    return fr;
}

int main(){
    cout<<"R03 run21 exact partition/overlap checker\n";
    // exact small validations of partition-lattice formula: one nonzero line case and one plane case.
    {
      int m=4,p=7; vector<int>v={1,1,-1,0},z={0,0,0,0}; vector<PlaneEval> e{{v,z,0}};eval_exact_counts(m,p,e); long long d=direct_count_small(m,p,v,z);cout<<"SMALL_DIRECT_LINE m=4 exact="<<e[0].exact_count<<" direct="<<d<<"\n"; if(e[0].exact_count!=d || d!=120){cerr<<"small line exact mismatch\n";return 4;}
    }
    {
      int m=4,p=7; vector<int>v={1,1,-1,0},w={0,1,1,-1}; vector<PlaneEval> e{{v,w,0}};eval_exact_counts(m,p,e); long long d=direct_count_small(m,p,v,w);cout<<"SMALL_DIRECT_PLANE m=4 exact="<<e[0].exact_count<<" direct="<<d<<"\n"; if(e[0].exact_count!=d){cerr<<"small plane exact mismatch\n";return 5;}
    }
    auto f9=compute_families(9,7); auto f10=compute_families(10,11);
    // retained run18 exact first-incidence values and old support<=4 two-plane lower bounds.
    cpp_int M1_9("651685823418402269683200"), oldM2_9("2942127020232812160000");
    cpp_int M1_10("325043331888785398807391827200"), oldM2_10("807305539038902680414176000");
    Rat c9(7,50), c10(132,16105);
    Rat r9 = (Rat(M1_9)-c9*Rat(oldM2_9+f9.disjoint+f9.overlap1))*Rat(cpp_int(1)<<10, cpp_int(1)<<81);
    Rat r10= (Rat(M1_10)-c10*Rat(oldM2_10+f10.disjoint+f10.overlap1))*Rat(cpp_int(1)<<11, cpp_int(1)<<100);
    cout<<"METRIC r10="<<r9.n<<"/"<<r9.d<<" decimal="<<setprecision(18)<<(double)to_ld(r9)<<"\n";
    cout<<"METRIC r11="<<r10.n<<"/"<<r10.d<<" decimal="<<setprecision(18)<<(double)to_ld(r10)<<"\n";
    Rat prev9(cpp_int("2543992837313541331977"),cpp_int("9223372036854775808"));
    Rat prev10(cpp_int("4089616823085565073184729848925"),cpp_int("7787900129957441143457185792"));
    Rat gain9=prev9-r9,gain10=prev10-r10;
    cout<<"GAIN r10="<<gain9.n<<"/"<<gain9.d<<" decimal="<<(double)to_ld(gain9)<<"\n";
    cout<<"GAIN r11="<<gain10.n<<"/"<<gain10.d<<" decimal="<<(double)to_ld(gain10)<<"\n";
    cout<<"SELF-CHECK PASS\n";
}
