public class SerialCable extends Cable {
	public void append(Cable p) {
		this.c.add(p);
	}
	
	public double getResistance() {
		double resistance_sum = 0.0;
		for (Cable p : c){
			resistance_sum += p.getResistance();
		}
		return resistance_sum;
	}
}
