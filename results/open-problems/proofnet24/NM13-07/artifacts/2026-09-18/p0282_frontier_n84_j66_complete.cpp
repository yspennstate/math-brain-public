#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cerr; using std::cout; using std::vector;

static cpp_int fact(int n){ cpp_int x=1; for(int i=2;i<=n;++i)x*=i; return x; }
static cpp_int hook_dim(const vector<int>& lam){
  int n=0; for(int x:lam)n+=x; if(n==0)return 1; cpp_int f=fact(n);
  int rows=(int)lam.size(), width=lam[0]; vector<int> colh(width,0);
  for(int c=0;c<width;++c) while(colh[c]<rows && lam[colh[c]]>c) ++colh[c];
  cpp_int h=1; for(int i=0;i<rows;++i) for(int c=0;c<lam[i];++c) h*= (lam[i]-c)+(colh[c]-i-1);
  if(f%h!=0){cerr<<"HOOK_DIV_FAIL\n"; std::exit(2);} return f/h;
}
struct TP{vector<int> lam; cpp_int f;};
static void parts(int rem,int maxp,vector<int>&cur,vector<TP>&out){
  if(rem==0){out.push_back({cur,hook_dim(cur)});return;}
  for(int a=std::min(rem,maxp);a>=1;--a){cur.push_back(a);parts(rem-a,a,cur,out);cur.pop_back();}
}
int main(){
  const int N=84, SOLD=30, SPREV=40, SNEW=47, JPREV=62, JNEW=66, NMAX=2*JNEW;
  vector<cpp_int> F(JNEW+3); F[0]=1; for(int i=1;i<(int)F.size();++i)F[i]=F[i-1]*i;
  vector<vector<cpp_int>> V(JNEW+2, vector<cpp_int>(NMAX+1));
  for(int n=0;n<=NMAX;++n){V[0][n]=1; V[1][n]=cpp_int(n-1)*(n-1);}
  for(int q=1;q<=JNEW;++q) for(int n=1;n<=NMAX;++n)
    V[q+1][n]=cpp_int(n)*n*(V[q][n-1]+cpp_int(q)*V[q-1][n-1])-cpp_int(2*n-q-1)*V[q][n];
  vector<vector<TP>> tails(SNEW+3); vector<int>cur; long long shapes=0;
  for(int r=0;r<=SNEW+2;++r){parts(r,r,cur,tails[r]); shapes+=tails[r].size();}
  long long amp_terms=0;
  auto err=[&](int j,int t,int s)->cpp_int{
    int q=j+t,n=2*j-s,Ntail=n-q,rmax=s+2*t-2; if(rmax<0)return 0; cpp_int total=0;
    for(int r=0;r<=rmax;++r){int M=q-r; for(const auto&tt:tails[r]){
      if(r && M<tt.lam[0])continue; cpp_int dim_num=tt.f;
      for(int a=1;a<=r;++a){int la=(a-1<(int)tt.lam.size()?tt.lam[a-1]:0); dim_num*=M+a-la;}
      if(dim_num%F[r]!=0){cerr<<"TAIL_DIM_DIV_FAIL\n";return -1;} cpp_int fmu=dim_num/F[r];
      cpp_int R=Ntail+1-M;
      for(int a=1;a<=r;++a){int la=(a-1<(int)tt.lam.size()?tt.lam[a-1]:0); R*=Ntail+a+1-la;}
      for(int i=r+2;i<=q;++i)R*=Ntail+i; if(R==0)continue;
      cpp_int num=fmu*R; if(num%F[q]!=0){cerr<<"TAIL_AMP_DIV_FAIL q="<<q<<" j="<<j<<" s="<<s<<" r="<<r<<"\n";return -1;}
      cpp_int a=num/F[q]; total+=a*a; ++amp_terms;
    }} return total;
  };
  long long checks=0; cpp_int minm=0; bool set=false; int minj=0,mins=0,minn=0; int depth[48]={0};
  for(int s=SOLD+1;s<=SNEW;++s) for(int j=4;j<=JNEW;++j){
    int n=2*j-s; if(n<j+2 || n<=N)continue;
    bool archived = (s<=SPREV && j<=JPREV); if(archived)continue;
    cpp_int E[3];
    for(int t=-1;t<=1;++t){int q=j+t; if(V[q][n]%F[q]!=0){cerr<<"COMP_DIV_FAIL\n";return 3;} cpp_int e=err(j,t,s); if(e<0)return 4; E[t+1]=V[q][n]/F[q]-e; if(E[t+1]<0){cerr<<"NEG_SOURCE_COUNT\n";return 5;}}
    cpp_int m=E[1]*E[1]-E[0]*E[2]; if(m<=0){cerr<<"NONPOS j="<<j<<" s="<<s<<" n="<<n<<"\n"; return 6;}
    if(!set||m<minm){set=true;minm=m;minj=j;mins=s;minn=n;} ++checks; ++depth[s];
  }
  cout<<"P0282 corrected sparse frontier certificate for complete defects j<=66\n";
  cout<<"archived_inputs=row_n<=83 + all relevant depth_s<=30 through j<=100 + predecessor adaptive s31..40 for j<=62 + current exact row84\n";
  cout<<"new_obligation_rule=s31..47, j<=66, n=2j-s>84, source-valid, excluding archived s<=40 j<=62\n";
  cout<<"tail_partition_atlas r=0..49 shapes="<<shapes<<"\n";
  cout<<"new_uncovered_seam_checks="<<checks<<" all_strictly_positive=True minimum_margin="<<minm<<" at_j="<<minj<<" s="<<mins<<" n="<<minn<<"\n";
  cout<<"depth_counts"; for(int s=31;s<=47;++s) if(depth[s])cout<<" s"<<s<<"="<<depth[s]; cout<<"\n";
  cout<<"tail_amplitude_terms_evaluated="<<amp_terms<<"\n";
  if(checks!=56){cerr<<"CHECK_COUNT_FAIL got="<<checks<<" expected=56\n";return 7;}
  cout<<"theorem_stitch=current row_n<=84 + archived/new depth obligations implies every source-valid point for defects j<=66\n";
  cout<<"ALL_EXACT_CHECKS_PASS\n";
}
