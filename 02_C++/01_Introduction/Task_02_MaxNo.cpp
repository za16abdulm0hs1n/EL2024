#include <algorithm>
#include<iostream>
#include <cmath>

int main(){
    int num1 = 0, num2 = 0, num3 = 0, maxnum = 0;

    std::cout << "Please enter three numbers: " << std::endl;
    std::cin >> num1 >> num2 >> num3;
    maxnum = std::max(std::max(num1,num2),num3);
    std::cout << "The maximum number is: " << maxnum <<std::endl;

    return 0;

}