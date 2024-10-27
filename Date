public class Date {
    int day;
    int month;
    int year;
    static int[] monthDays = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public Date(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public int getDay() {
        return day;
    }

    public int getMonth() {
        return month;
    }

    public int getYear() {
        return year;
    }

    public String toString() {
        String s = "";
        if (day < 10) s += "0" + day + "/";
        else s += day + "/";
        if (month < 10) s += "0" + month + "/";
        else s += month + "/";
        s += year;
        return s;
    }

    public void updateDate() {
        if (day == monthDays[month - 1]) {
            day = 1;
            if (month == 12) {
                month = 1;
                year++;
            } else {
                month++;
            }
        } else {
            day++;
        }
    }
}

public class VacationDays {
    Date[] dateList;
    int numEntries = 0;

    public VacationDays(Date[] d) {
        dateList = new Date[d.length];
        for (int i = 0; i < d.length && d[i] != null; i++) {
            dateList[i] = new Date(d[i].getDay(), d[i].getMonth(), d[i].getYear());
            numEntries++;
        }
    }

    public boolean inOrder() {
        for (int i = 0; i < dateList.length - 1 && dateList[i] != null && dateList[i + 1] != null; i++) {
            if (dateList[i].getYear() > dateList[i + 1].getYear()) return false;
            if (dateList[i].getMonth() > dateList[i + 1].getMonth() && dateList[i].getYear() >= dateList[i + 1].getYear()) return false;
            if (dateList[i].getDay() > dateList[i + 1].getDay() && dateList[i].getMonth() >= dateList[i + 1].getMonth()) return false;
        }
        return true;
    }

    public String toString() {
        System.out.println("You have vacation days in:");
        for (int i = 0; i < dateList.length && dateList[i] != null; i++) {
            System.out.println("day " + dateList[i].getDay() + " in month " + dateList[i].getMonth() + " in year " + dateList[i].getYear());
        }
        return "";
    }

    public static void main(String[] args) {
        Date[] d = new Date[3];
        d[0] = new Date(11, 5, 2003);
        d[1] = new Date(1, 3, 2006);
        d[2] = new Date(13, 6, 2004);
        VacationDays v = new VacationDays(d);
        System.out.println(v.inOrder());
        System.out.println(v);
        v.dateList[0].updateDate();
        System.out.println(v.dateList[0]);
    }
}
