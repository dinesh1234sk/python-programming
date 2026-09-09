import java.util.*;
public class StudentList {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
ArrayList<String> names = new ArrayList<>(); int choice;
do {
System.out.println("\n1. Add Name");
System.out.println("2. View Names");
System.out.println("3. Exit");
System.out.print("Enter choice: ");
try {
choice = sc.nextInt();
sc.nextLine(); // clear buffer
if (choice == 1) {
System.out.print("Enter name: ");
String name = sc.nextLine();
names.add(name);
System.out.println("Name added.");
} else if (choice == 2) {
System.out.println("\nStudent Names:");
for (String n : names)
System.out.println(n);
} else if (choice == 3) {
System.out.println("Exiting...");
} else {
System.out.println("Invalid choice.");
}
} catch (InputMismatchException e) {
System.out.println("Please enter a valid number!"); sc.nextLine(); // clear invalid input
choice = 0; // reset choice to continue loop
}
} while (choice != 3);
sc.close();
}
}
