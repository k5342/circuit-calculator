

public class Main {
	public static void main(String[] args){
		ParallelCable pc2 = new ParallelCable(new SerialCable(), new SerialCable());
		((SerialCable) pc2.getLeft()).append(new Resistance(30));
		((SerialCable) pc2.getRight()).append(new Resistance(15));
		((SerialCable) pc2.getRight()).append(new Resistance(15));
		
		SerialCable pc1_right = new SerialCable();
		pc1_right.append(new Resistance(15));
		pc1_right.append(pc2);
		
		ParallelCable pc1 = new ParallelCable(new SerialCable(), pc1_right);
		((SerialCable) pc1.getLeft()).append(new Resistance(30));
		
		SerialCable c = new SerialCable();
		c.append(new Resistance(15));
		c.append(pc1);
		
		System.out.printf("gousei teikou: %f [ohm]\n", c.getResistance());
	}
}
