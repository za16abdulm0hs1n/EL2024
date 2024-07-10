#include <iostream>
#include <bitset>
#include <string>
#include <cctype>

bool isBinary(const std::string& str) {
    for (char c : str) {
        if (c != '0' && c != '1') {
            return false;
        }
    }
    return true;
}

bool isDecimal(const std::string& str) {
    for (char c : str) {
        if (!std::isdigit(c)) {
            return false;
        }
    }
    return true;
}

int main() {
    std::string input;
    char choice;

    // Ask user for the type of number
    std::cout << "Enter 'b' for binary or 'd' for decimal: ";
    std::cin >> choice;

    // Check user's choice and perform appropriate action
    if (choice == 'b' || choice == 'B') {
        std::cout << "Enter a binary number: ";
        std::cin >> input;

        if (isBinary(input)) {
            // Convert binary to decimal
            std::bitset<32> binarySet(input);
            unsigned long decimal = binarySet.to_ulong();
            std::cout << "Decimal: " << decimal << std::endl;
        } else {
            std::cout << "Invalid binary number." << std::endl;
        }
    } else if (choice == 'd' || choice == 'D') {
        std::cout << "Enter a decimal number: ";
        std::cin >> input;

        if (isDecimal(input)) {
            // Convert decimal to binary
            int decimal = std::stoi(input);
            std::bitset<32> binary(decimal);
            std::cout << "Binary: " << binary.to_string() << std::endl;
        } else {
            std::cout << "Invalid decimal number." << std::endl;
        }
    } else {
        std::cout << "Invalid choice. Please enter 'b' for binary or 'd' for decimal." << std::endl;
    }

    return 0;
}
