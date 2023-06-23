#include <stdio.h>

struct BankAccount {
    int accountNumber;
    float balance;
};

void displayMenu() {
    printf("\nBank Account Management System\n");
    printf("1. Create New Account\n");
    printf("2. Deposit Amount\n");
    printf("3. Withdraw Amount\n");
    printf("4. Check Balance\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
}

void createAccount(struct BankAccount *account) {
    printf("Enter the account number: ");
    scanf("%d", &(account->accountNumber));
    printf("Enter initial balance: ");
    scanf("%f", &(account->balance));
    printf("Account created successfully!\n");
}

void deposit(struct BankAccount *account) {
    float amount;
    printf("Enter the amount to deposit: ");
    scanf("%f", &amount);
    account->balance += amount;
    printf("Amount deposited successfully!\n");
}

void withdraw(struct BankAccount *account) {
    float amount;
    printf("Enter the amount to withdraw: ");
    scanf("%f", &amount);
    if (amount > account->balance) {
        printf("Insufficient balance!\n");
    } else {
        account->balance -= amount;
        printf("Amount withdrawn successfully!\n");
    }
}

void checkBalance(struct BankAccount *account) {
    printf("Account Number: %d\n", account->accountNumber);
    printf("Balance: %.2f\n", account->balance);
}

int main() {
    struct BankAccount account;
    int choice;

    while (1) {
        displayMenu();
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                createAccount(&account);
                break;
            case 2:
                deposit(&account);
                break;
            case 3:
                withdraw(&account);
                break;
            case 4:
                checkBalance(&account);
                break;
            case 5:
                printf("Thank you for using the Bank Account Management System!\n");
                return 0;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}

