/*
문제)
알파벳 대문자와 숫자로만 구성된 문자열이 있을 때 모든 알파벳을 오름차순으로 정렬하여 출력한 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
예를 들어, K1KA5CB7 = ABCKK13이다.
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class StringResort {
    public static String str;
    public static List<Character> result = new ArrayList<>();
    public static int value = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        str = sc.next();

        for (int i = 0; i < str.length(); i++) {
            if (Character.isLetter(str.charAt(i))) {
                result.add(str.charAt(i));
            } else {
                value += str.charAt(i) - '0';
            }
        }
        Collections.sort(result);
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
        }
        if (value != 0) System.out.print(value);

    }
}
