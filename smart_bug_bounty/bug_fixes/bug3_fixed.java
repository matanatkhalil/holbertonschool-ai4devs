public class Bug3Fixed {
    private double balance;

    public Bug3Fixed(double initialBalance) {
        this.balance = initialBalance;
    }

    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }

        return false;
    }

    public double getBalance() {
        return balance;
    }

    public static void main(String[] args) {
        Bug3Fixed account = new Bug3Fixed(500);

        System.out.println(account.withdraw(-100)); // false
        System.out.println("Balance: " + account.getBalance()); // 500.0

        System.out.println(account.withdraw(100)); // true
        System.out.println("Balance: " + account.getBalance()); // 400.0
    }
}
