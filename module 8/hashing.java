import java.util.*;

class hashing{ 
    public static void main(String[] args) {
        Hashtable<Integer, Integer>
        ht = new Hashtable<>();

        ht.put(123, 4321);
        ht.put(12, 2345);
        ht.put(15, 5643);
        ht.put(3, 321);

        ht.remove(12);
        System.out.println(ht);
    }
}