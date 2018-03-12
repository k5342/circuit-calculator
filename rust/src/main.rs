
pub trait HasResist {
    fn get_resistance(&self) -> f64;
}

pub struct Resistance {
    v: f64,
}

impl HasResist for Resistance {
    fn get_resistance(&self) -> f64 {
        self.v
    }
}

struct Parallel<L,R> {
    l: L,
    r: R,
}

impl<L: HasResist, R: HasResist> HasResist for Parallel<L,R> {
    fn get_resistance(&self) -> f64 {
        let l2 = self.l.get_resistance();
        let r2 = self.r.get_resistance();
        1.0/(1.0/l2 + 1.0/r2)
    }
}

struct Serial<T> {
    v: Vec<T>,
}

impl<T: HasResist> HasResist for Serial<T> {
    fn get_resistance(&self) -> f64 {
        let mut sum = 0.0;
        for i in &self.v {
            sum += i.get_resistance();
        }
        sum
    }
}

fn main() {

    let pc2 = Parallel{
        l: Resistance{v:30.0},
        r: Serial{v:vec![ Resistance{v:15.0}, Resistance{v:15.0} ]},
    };

    let pc1_right = Serial{v:vec![ Resistance{v:15.0}, Resistance{v:pc2.get_resistance()}]};
    
    let pc1 = Parallel{
        l: Resistance{v: 30.0},
        r: Resistance{v: pc1_right.get_resistance()}
    };

    let c = Serial{v:vec![ Resistance{v:15.0}, Resistance{v:pc1.get_resistance()} ]};

    println!("gousei teikou: {} [ohm]", c.get_resistance());

}
