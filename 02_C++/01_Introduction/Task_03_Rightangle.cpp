#include<iostream>


int main(){
    double angle1 = 0, angle2 = 0, angle3 = 0;
    
    std::cout << "Please enter three angles of triangle:" << std::endl;
    std::cin >> angle1 >> angle2 >> angle3;

    if ((angle1 + angle2 + angle3) == 180) {
        if (angle1 == 90 || angle2 == 90 || angle3 == 90){
            std::cout << "The given angles form a right angle triangle" << std::endl; 
        }
        else{
            std::cout << "The given angles do not form a right angle triangle, but a triangle" << std::endl; 
        }
    }
    else {
    std::cout << "The given angles do not form a triangle" << std::endl; 
    }
    return 0;
}