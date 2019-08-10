//
//  main.cpp
//  LEETCODE Practice
//
//  Created by Mayank Raj on 1/17/19.
//  Copyright © 2019 Mayank Raj. All rights reserved.
//

#include <iostream>
#include <stdlib.h>

using namespace std;

int numJewelsInStones(string J, string S) {
    int Jcount = J.size();
    int Scount = S.size();
    int count = 0;
    int i = 0, m = 0;
    for( i = 0; i < Scount; i++){
        for(m = 0; m < Jcount; m++){
            if (S[i] == J[m])
                count++;
        }
    }
    return count;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int count = 0;
    string J = "aA";
    string S = "aAAsdasf";
    count = numJewelsInStones(J, S);
    cout<<count;
    return 0;
}
