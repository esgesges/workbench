package threads;
public class Campanai implements Runnable{
    private String suono;
    private int volte;
    public Campanai(String suono, int volte){
        this.suono = suono;
        this.volte = volte;
    }
    @Override
    public void run(){
        for(int i = 0; i < volte; i++){
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println((i+1) + suono);
            System.out.println((i+1) + " dun");
        }
    }
}