
public class ZeroSum {
    //a simple java multithreaded program for my CS602 class where you can see that when balance calories is synchronzied,
    //the threads are always alternated. However, when not synchronized there is no guarantee that it will be so.
    public static int balance =0;
    //list of calories for two threads throughout day (total = 1000)
    public static int[] meals = {50,100,300,50,150,75,150,75,50};
    //main method starts two threads, one which uses gainCalories() and one which uses burnCalories()
    public static void main(String[] args) {
        new Thread(ZeroSum::gainCalories).start();
        new Thread(ZeroSum::burnCalories).start();
    }

    public static void burnCalories()
    {
        //takes ints from the "meals"array, make them negative for burning and send them to balanceCalories()
        //then sleep for 100ms
        for(int i =0; i<meals.length; i++) {
            balanceCalories(meals[i]*-1);

            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("burn calories thread (" +Thread.currentThread().getName() +") has finished" );
    }
    public static void gainCalories()
    {
        //takes ints from the array and send them to balanceCalories()
        //then sleep for 100ms
        for(int i =0; i<meals.length; i++) {
            balanceCalories(meals[i]);

            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("gain calories thread (" +Thread.currentThread().getName() +") has finished" );
    }
    public static synchronized void balanceCalories(int calories)
    {
        System.out.println(Thread.currentThread().getName() + " counted " + (balance += calories));
    }
    public static void balanceCaloriesWithoutSync(int calories)
    {
        System.out.println(Thread.currentThread().getName() + " counted " + (balance += calories));
    }
}
