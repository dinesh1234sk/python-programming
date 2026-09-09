CREATE A MULTI-THREADED COUNTDOWN TIMER WITH GUI
AIM:
To develop a GUI-based countdown timer in Java using Swing and multithreading. ALGORITHM:
● Create a class that extends JFrame.
● Add components: JLabel, JTextField, and JButton.
● On button click, create and start a new thread.
● Inside the thread, decrease the number every second.
● Update the label after each second using SwingUtilities.invokeLater() or Swing Timer. PROGRAM
import javax.swing.*;
import java.awt.event.*;
public class CountdownTimer extends JFrame implements ActionListener { JTextField inputField;
JLabel timerLabel;
JButton startButton;
CountdownTimer() {
setTitle("Countdown Timer");
setSize(300, 150);
setLayout(null);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
JLabel inputLabel = new JLabel("Enter seconds:");
inputLabel.setBounds(20, 20, 100, 25);
add(inputLabel);
inputField = new JTextField();
inputField.setBounds(130, 20, 120, 25);
add(inputField);
timerLabel = new JLabel("Time left: ");
timerLabel.setBounds(20, 60, 200, 25);
add(timerLabel);
startButton = new JButton("Start");
startButton.setBounds(100, 90, 80, 30);
startButton.addActionListener(this);
add(startButton);
setVisible(true);
}
public void actionPerformed(ActionEvent e) {
int seconds;
try {
seconds = Integer.parseInt(inputField.getText());
} catch (NumberFormatException ex) {
JOptionPane.showMessageDialog(this, "Please enter a valid number."); return;
}
// Start countdown in a new thread
Thread t = new Thread(() -> {
for (int i = seconds; i >= 0; i--) {
int timeLeft = i;
SwingUtilities.invokeLater(() -> timerLabel.setText("Time left: " + timeLeft + " sec")); try {
Thread.sleep(1000);
} catch (InterruptedException ex) {
ex.printStackTrace();
}
}
SwingUtilities.invokeLater(() -> JOptionPane.showMessageDialog(this, "Time's up!")); });
t.start();
}
public static void main(String[] args) {
new CountdownTimer();
}
}
