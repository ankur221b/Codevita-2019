#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fast_io ios::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define pb(x) push_back(x)
#define all(x) x.begin(),x.end()
#define ff first
#define ss second
#define MAX 100001
#define MOD 1000000007

map<ll,ll> cap,balls;

int chk(ll x, ll* v,int n)
{
  for(int i=0;i<n;i++)
  {
    if(v[i]>=x && cap[i+1]>0)return i+1;
  }
  return -1;
}


int main()
{
    ll t,n;
    cin>>n;

    ll holes[n];

    for(int i=0;i<n;i++)
    {
      cin>>holes[i];
      cap[i+1]=i+1;
    }    

    cin>>m;

    for(int i=0;i<m;i++)
    {
      cin>>x;
      c=chk(x,holes,n);
      cap[c]--;
      cout<<c<<" ";
    }

}
