interface PaymentGateway {
void pay(double amount);
}
abstract class Payment {
String transactionId;
Payment(String id) {
transactionId = id;
}
void showTransactionDetails() {
System.out.println("Transaction ID: " + transactionId);
}
abstract void validate();
}
class CreditCardPayment extends Payment implements PaymentGateway { String card;
CreditCardPayment(String id, String card) {
super(id);
this.card = card;
}
public void pay(double amount) {
System.out.println("Paid ₹" + amount + " using Credit Card"); }
void validate() {
System.out.println("Credit Card validated: " + card);
}
}
class UPIPayment extends Payment implements PaymentGateway { String upi;
UPIPayment(String id, String upi) {
super(id);
this.upi = upi;
}
public void pay(double amount) {
System.out.println("Paid ₹" + amount + " using UPI");
}
void validate() {
System.out.println("UPI ID validated: " + upi);
}
}
public class PaymentDemo {
public static void main(String[] args) {
CreditCardPayment cc = new CreditCardPayment("T001", "1234-5678-9012"); UPIPayment upi = new UPIPayment("T002", "abc@upi");
cc.showTransactionDetails();
cc.validate();
cc.pay(1000);
upi.showTransactionDetails();
upi.validate();
upi.pay(500);
}
}
