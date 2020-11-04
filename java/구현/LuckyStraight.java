import java.util.Scanner;

public class LuckyStraight {


    public static void main(String[] args) {

        /**
         * 방법1_ascii
         * char형을 ascii 값으로 변환하는 대신 [str.charAt(index) - '0'] 으로 int값 변경 가능
         */
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        int mid = str.length() / 2;

        int summary = 0;
        for (int i = 0; i < mid; i++) {
            char c = str.charAt(i);
            summary += c - '0';
        }
        for (int i = mid; i < str.length(); i++) {
            char c = str.charAt(i);
            summary -= (c - '0');
        }
        if (summary == 0) {
            System.out.println("LUCKY");
        } else {
            System.out.println("READY");
        }

        /**
         * 방법2_정수로 입력받아 각 자리수 계산
         */
        Scanner sc2 = new Scanner(System.in);
        int N = sc2.nextInt();

        int leftSum = 0;
        int rightSum = 0;
        int len = Integer.toString(N).length() / 2;

        while (N != 0) {
            if (len > 0) {
                rightSum += (N % 10);
                N /= 10;
                len--;
            } else {
                leftSum += (N % 10);
                N /= 10;
            }
        }

        if (leftSum == rightSum)
            System.out.println("LUCKY");
        else
            System.out.println("READY");
    }
}