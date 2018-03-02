import java.util.ArrayList;

public abstract class Cable implements PartsBehavior {
	ArrayList<Cable> c;
	
	public Cable() {
		c = new ArrayList<>();
	}
	
	public abstract double getResistance();
}
