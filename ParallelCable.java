public class ParallelCable extends Cable {
	private Cable right;
	private Cable left;
	
	public ParallelCable(Cable left, Cable right) {
		super();
		this.right = right;
		this.left = left;
	}
	
	public Cable getLeft() {
		return this.left;
	}
	
	public Cable getRight() {
		return this.right;
	}
	
	public double getResistance() {
		double r_resistance = this.right.getResistance();
		double l_resistance = this.left.getResistance();
		return 1/ (1/r_resistance + 1/l_resistance);
	}
}
