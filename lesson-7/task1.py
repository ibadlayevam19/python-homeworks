import math
class Vector:
    def __init__(self, *components):
        self.components=tuple(components)
    
    def __repr__(self):
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if len(self.components)!=len(other.components):
            raise ValueError("They should be in same size to add.")
        return Vector(*(a+b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        if len(self.components)!=len(other.components):
            raise ValueError("They should be in same size to subtract.")
        return Vector(*(a-b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")
        return Vector(*(a*scalar for a in self.components))
    
    def dot(self, other):
        if len(self.components)!=len(other.components):
            raise ValueError("They should be in same size to find dot product.")
        return sum(a*b for a, b in zip(self.components, other.components))
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self):
        if self.magnitude()==0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a/self.magnitude() for a in self.components))
    
if __name__=="__main__":
    v1=Vector(2,3,4)
    v2=Vector(5,6,7)
    print("v1:", v1)
    print("v2:", v2)
    print("Addition:", v1+v2)
    print("Subtraction:", v1-v2)
    print("Dot product:", v1.dot(v2))
    print("Scalar multiplication:", v1*3)
    print("Magnitude of v1:", v1.magnitude())
    print("Normalized v1:", v1.normalize())


