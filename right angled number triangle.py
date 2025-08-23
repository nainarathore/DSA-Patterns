#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,num=1;
    cin>>n;
    for(int i=0;i<=n;i++){
        for(int j=1;j<=i;j++){
            cout<<num<<" ";
            num=num+1;
        }
        cout<<endl;
    }
}


output:

5

1
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
