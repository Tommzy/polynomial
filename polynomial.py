from typing import Any


class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)

class Sub: 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2);

    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            if isinstance(self.p2, (Add, Sub, Mul, Div)):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)

    def evaluate(self, value):
        return self.p1.evaluate(value) / self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub)):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)

        

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
poly_with_sub = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), Sub(X(), Int(1))), Int(1)))))
poly_with_div = Add( Add( Int(4), Int(3)), Add( X(), Div( Mul(Add(X(), Int(1)), Sub(X(),Int(1))), Mul(X(), Add( Mul(X(), Sub(X(), Int(1))), Int(1))))))

print(poly)
print(poly.evaluate(-1))

print("Tests")
x = 1;
print("x = ", x);
print(poly)
print("=", poly.evaluate(x))
print(poly_with_sub)
print("=", poly_with_sub.evaluate(x))
print(poly_with_div)
print("=", poly_with_div.evaluate(x))