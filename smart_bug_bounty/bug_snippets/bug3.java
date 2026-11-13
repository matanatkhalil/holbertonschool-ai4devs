public class Bug3 {
    private double balance;

    public Bug3(double initialBalance) {
        this.balance = initialBalance;
    }

    public boolean withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            return true;
        }

        return false;
    }

    public double getBalance() {
        return balance;
    }

    public static void main(String[] args) {
        Bug3 account = new Bug3(500);

        System.out.println(account.withdraw(-100));
        System.out.println("Balance: " + account.getBalance());
    }
}