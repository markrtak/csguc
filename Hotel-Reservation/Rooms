public class Room {
    int number;
    String name;
    int bed;
    double rentRate;
    int days;

    public Room(int number, String name, int bed, double rentRate, int days) {
        this.number = number;
        this.name = name;
        this.bed = bed;
        this.rentRate = rentRate;
        this.days = days;
    }

    public String toString() {
        String m = "Guest’s name: " + name + "\n";
        m += "Room number: " + number + "\n";
        m += "Room beds: " + bed + "\n";
        m += "Rate: " + rentRate + "\n";
        m += "Rented for: " + days + " days";
        return m;
    }
}
public class Hotel {
    String name;
    Room[] theRooms;
    int roomsRented = 0;

    public Hotel(String name, int numRooms) {
        this.name = name;
        this.theRooms = new Room[numRooms];
    }

    public double getTotalRentalSales() {
        double s = 0;
        for (int i = 0; i < roomsRented; i++) {
            s += theRooms[i].rentRate * theRooms[i].days;
        }
        return s;
    }

    public double getAvgDays() {
        double s = 0;
        for (int i = 0; i < roomsRented; i++) {
            s += theRooms[i].days;
        }
        return s / roomsRented;
    }

    public void printRentalList() {
        for (int i = 0; i < roomsRented; i++) {
            System.out.println(theRooms[i]);
        }
    }

    public void addReservation(Room a) {
        if (roomsRented < theRooms.length) {
            theRooms[roomsRented] = a;
            roomsRented++;
        } else {
            System.out.println("Cannot add more rooms");
        }
    }

    public void findReservation(int n) {
        boolean flag = false;
        int x = -1;
        for (int i = 0; i < roomsRented && !flag; i++) {
            if (theRooms[i].number == n) {
                flag = true;
                x = i;
            }
        }
        if (flag) {
            System.out.println("Reservation found: " + theRooms[x]);
        } else {
            System.out.println("Reservation not found");
        }
    }
public void findReservation(int n) {
    boolean flag = false;
    int x = -1;
    
    
    for (int i = 0; i < roomsRented && !flag; i++) {
        if (theRooms[i].number == n) {
            flag = true;
            x = i;
        }
    }

    if (flag) {
        System.out.println("Found reservation for room number: " + n + "\n"
                + "Room information:" + "\n" + theRooms[x]);
    } else {
        System.out.println("Could not find reservation for room number: " + n);
    }
}
}
public static void main(String[] args) {
    Hotel h = new Hotel("Montage", 100);

   
    Room r1 = new Room(123, "Blake", 1, 123.50, 5);
    Room r2 = new Room(222, "Smith", 2, 144.50, 4);
    Room r3 = new Room(352, "Joe", 2, 155.00, 7);
    Room r4 = new Room(333, "Jane", 1, 140.00, 5);

    
    h.addReservation(r1);
    h.addReservation(r2);
    h.addReservation(r3);
    h.addReservation(r4);

   
    h.printRentalList();

    
    System.out.println("Average days rented out is: " + h.getAvgDays());
    System.out.println("Total rental income is: " + h.getTotalRentalSales());

   
    h.findReservation(222); 
    h.findReservation(200);  }
