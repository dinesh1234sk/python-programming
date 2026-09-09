import java.io.*;
import java.util.*;
public class StudentManager {
public static void main(String[] args) throws IOException {
Scanner sc = new Scanner(System.in);
String file = "students.txt";
int choice;
do {
System.out.println("\n1. Add 2. View 3. Search 4. Exit"); System.out.print("Enter choice: ");
choice = sc.nextInt();
sc.nextLine(); // clear buffer
if (choice == 1) {
System.out.print("Roll No: ");
String roll = sc.nextLine();
System.out.print("Name: ");
String name = sc.nextLine();
System.out.print("Dept: ");
String dept = sc.nextLine();
FileWriter fw = new FileWriter(file, true);
fw.write(roll + "," + name + "," + dept + "\n");
fw.close();
System.out.println("Student added.");
}
else if (choice == 2) {
BufferedReader br = new BufferedReader(new FileReader(file)); String line;
System.out.println("\n-- Student List --");
while ((line = br.readLine()) != null)
System.out.println(line);
br.close();
}
else if (choice == 3) {
System.out.print("Enter Roll No: ");
String search = sc.nextLine();
BufferedReader br = new BufferedReader(new FileReader(file)); String line;
boolean found = false;
while ((line = br.readLine()) != null) {
if (line.startsWith(search + ",")) {
System.out.println("Found: " + line);
found = true;
break;
}
}
if (!found)
System.out.println("Not found.");
br.close();
}
} while (choice != 4);
sc.close();
}
}
