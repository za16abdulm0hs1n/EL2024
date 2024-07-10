#include <iostream>
#include <iomanip>

int main() {
       std::cout << "Multiplication Table from 1 to 10:\n\n";

    // Print the header row
    std::cout << std::setw(5) << " ";
    for (int i = 1; i <= 10; ++i) {
        std::cout << std::setw(5) << i;
    }
    std::cout << "\n";

    // Print the table
    for (int i = 1; i <= 10; ++i) {
        // Print the header column
        std::cout << std::setw(5) << i;
        for (int j = 1; j <= 10; ++j) {
            std::cout << std::setw(5) << i * j;
        }
        std::cout << "\n";
    }

    return 0;
} 

