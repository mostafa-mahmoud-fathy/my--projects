#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

void Encryption() {
    string inserted_sentence;
    getline(cin, inserted_sentence);
    string final_result;
    for (int i = 0; i <  inserted_sentence.length() ; i++)
    {
        //converting to uppercase
        inserted_sentence[i] = toupper(inserted_sentence[i]);
        //checking if the character between or equal to A and Z
        if (inserted_sentence[i] >= 65 && inserted_sentence[i] <= 90)
        {
            char new_char = inserted_sentence[i];
            int ascii_value = int(new_char); // getting the ascii value of the character
            string binaryResult = ""; // an empty string variable
            int result = (ascii_value - 65);// calculating the decimal value that will be converted to binary
            //converting the value to binary of five digits
            if (result == 0) {
                binaryResult = "00000";
            }
            while (result > 0) {
                int decimal = result % 2;
                binaryResult += to_string(decimal);
                result = result / 2;
            }
            
            while (binaryResult.length() < 5)
            {
                binaryResult += '0';
            }

            // reversing the string
            reverse(binaryResult.begin(), binaryResult.end());
            // encrypting the binary result
            for (int i = 0; i < binaryResult.length(); i++)
            {
                if (binaryResult[i] == '0')
                {
                    binaryResult[i] = 'a';
                }
                else
                {
                    binaryResult[i] = 'b';
                }

            }
            // adding the encrypted character to the final result
            final_result += binaryResult;
            final_result += " ";
        }
        // adding the character as it is to the final result
        else
        {
            final_result += inserted_sentence[i];

        }
    }
    // displaying the final result
    cout << final_result << endl;
}
void Decryption() {
    string inserted_sentence;
    getline(cin, inserted_sentence);
    string final_result = "";
    // converting a and b to digits
    for (int j = 0; j < inserted_sentence.length(); j++) {
        if (inserted_sentence[j] == 'a') {
            inserted_sentence[j] = '0';
        }
        if (inserted_sentence[j] == 'b') {
            inserted_sentence[j] = '1';
        }
    }

    for (int j = 0; j < inserted_sentence.length(); j++) {
        // checking if there is a space then adding it to the final result
        if (inserted_sentence[j] == ' ' && inserted_sentence[j + 1] == ' ') {
            final_result += " ";
        }
        // taking a substring consist of alphabet characters only
        string binary = inserted_sentence.substr(j, 5);
        auto result = find(binary.begin(), binary.end(), ' ');
        if (result != binary.end()) {
            continue;
        }
        // Convert binary to decimal
        int decimal_result = 0;
        for (int i = 0; i < binary.length(); ++i) {
            decimal_result = (decimal_result << 1) | (binary[i] - '0');
        }
        // checking if the decimal value refer to an alphabet character
        if ((decimal_result <= 25) && (decimal_result >= 0))  {
            final_result += char(decimal_result + 'A');
        }
        // adiing special characters to the result
        else
        {
            final_result += inserted_sentence[j];
        }
    }
    // displaying the final result
    cout << final_result << endl;
}
int main() {

  Encryption();
  Decryption();
   

      return 0;
  }