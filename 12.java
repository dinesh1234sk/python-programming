BUILD A GUI LOGIN FORM USING SWING AND EVENT HANDLING
AIM:
To create a basic GUI-based login form using Java Swing and handle button click events.
ALGORITHM :
● Create a class that extends JFrame and implements ActionListener. ● Add Swing components: JLabel, JTextField, JPasswordField, and JButton. ● Set layout and position for components.
● Add an ActionListener to the Login button.
● In actionPerformed(), check if the username and password match predefined values. ● Show a message dialog for success or failure.
PROGRAM
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class LoginForm extends JFrame implements ActionListener { // Components
JLabel labelUser, labelPass;
JTextField textUser;
JPasswordField textPass;
JButton btnLogin;
// Constructor
LoginForm() {
// Frame setup
setTitle("Login Form");
setSize(300, 200);
setLayout(null);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
// Username label & field
labelUser = new JLabel("Username:");
labelUser.setBounds(30, 30, 80, 25);
add(labelUser);
textUser = new JTextField();
textUser.setBounds(120, 30, 130, 25);
add(textUser);
// Password label & field
labelPass = new JLabel("Password:");
labelPass.setBounds(30, 70, 80, 25);
add(labelPass);
textPass = new JPasswordField();
textPass.setBounds(120, 70, 130, 25);
add(textPass);
// Login button
btnLogin = new JButton("Login");
btnLogin.setBounds(100, 110, 80, 30);
btnLogin.addActionListener(this);
add(btnLogin);
setVisible(true);
}
// Event Handling
public void actionPerformed(ActionEvent e) {
String user = textUser.getText();
String pass = new String(textPass.getPassword());
if (user.equals("admin") && pass.equals("1234")) {
JOptionPane.showMessageDialog(this, "Login Successful!");
} else {
JOptionPane.showMessageDialog(this, "Invalid Credentials!");
}
}
// Main method
public static void main(String[] args) {
new LoginForm();
}
}
OUTPUT :
A small window will pop up with:
Username & password input fields
Login button
A message dialog on clicking the button (based on input)
