class MyThread extends Thread {
public void run() {
for (int i = 1; i <= 5; i++) {
System.out.println("Thread (Thread class): " + i);
}
}
}
// Runnable interface method
class MyRunnable implements Runnable {
public void run() {
for (int i = 1; i <= 5; i++) {
System.out.println("Thread (Runnable): " + i);
}
}
}
public class MultithreadDemo {
public static void main(String[] args) {
// Using Thread class
MyThread t1 = new MyThread();
// Using Runnable interface
MyRunnable r1 = new MyRunnable();
Thread t2 = new Thread(r1); // wrap in Thread object
// Start both threads
t1.start();
t2.start();
}
}
