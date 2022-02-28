import java.lang.Math;
public class Pos 
{
	public int x;
	public int y;
	public double distance;
	
	public void Pos() 
	{
		this.x=0;
		this.y=0;
		this.distance=0;
	}
	public void Pos(int x, int y) 
	{
		this.x=x;
		this.y=y;
		this.distance=0;
	}
	public void update(int x, int y, double distance)
	{
		this.x =x;
		this.y =y;
		this.distance=distance;
	}
	public double getDistance(Pos p) 
	{
		// Math.pow() <- 제곱
		// Math.sqrt() <- 루트
		double d;
		int xd, yd;
		yd = (int) Math.pow((this.y-p.y),2);
		xd = (int) Math.pow((this.x-p.x),2);
		d = Math.sqrt(yd+xd);
		return d;
	}
	public boolean isExist(Pos[] pos, int round)
	{
		for(int i=0;i<round;i++)
		{
			int nx = pos[i].x;
			int ny = pos[i].y;
			if (nx==this.x && ny==this.y)
				return true;
		}
		return false;

	}
	public void printPos()
	{
		System.out.printf("(%d, %d) => %f\n", this.x, this.y, this.distance);
	}
	
	
}
