package threads;

public class Main{
    public static void main(String args[]){
        Campanai camp = new Campanai("din", 5);
        Thread thread = new Thread(camp);
        thread.start();

        Thread thread2 = new Thread(new Campanai("don", 5));
        thread2.start();

        new Thread(new Campanai("dan", 5)).start();
    }
}