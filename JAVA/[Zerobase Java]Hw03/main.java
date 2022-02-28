/*
- Project : Calculrate distance from pos 
- 초기좌표와 10개의 좌표를 입력받아(중복허용x), 두 점 사이의 거리가 가장 짧은 값을 구해주는 프로그램
- Author : Hae-Yeon-Won
- Date of last update : 2022.02.28.
*/
import java.util.Scanner;
public class main {
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in); // Scanner 객체 생성
		Pos pNow = new Pos();
		Pos pNext = new Pos();
		Pos[] positions = new Pos[10];
		double minVal=Double.MAX_VALUE;
		int minIdx = 0;
		int i=0;
		
		for(int p=0;p<10;p++)
		{
			positions[p] = new Pos();
		}
		
		System.out.println("내 좌표 x값을 입력해 주세요.");
		pNow.x=in.nextInt();
		System.out.println("내 좌표 y값을 입력해 주세요.");
		pNow.y=in.nextInt();
		
		while(i!=10)
		{
			System.out.println(String.valueOf(i+1)+"/10 번째 입력");
			System.out.println("임의의 좌표 x값을 입력해 주세요.");
			pNext.x=in.nextInt();
			System.out.println("임의의 좌표 y값을 입력해 주세요.");
			pNext.y=in.nextInt();
			if(pNext.isExist(positions, i))
			{
				System.out.println("동일한 좌표값이 이미 존재합니다. 다시 입력해 주세요.");
				continue;
			}
			else
			{
				pNext.distance = pNext.getDistance(pNow);
				positions[i].update(pNext.x, pNext.y, pNext.distance);
				if (pNext.distance<minVal)
				{
					minVal=pNext.distance;
					minIdx=i;
				}
				i++;
			}
		}
		for(int j=0;j<10;j++)
		{
			positions[j].printPos();
		}
		System.out.println("제일 가까운 좌표:");
		System.out.printf("(%d, %d) => %f\n", positions[minIdx].x, positions[minIdx].y, positions[minIdx].distance);
	}

}
