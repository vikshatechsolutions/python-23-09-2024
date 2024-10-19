class Test:
    '''This is an example class to demonstrate different methods and variables of a class'''
    x=10
    def __init__(self):
        Test.b=20 # class or static varible declared inside the consrtuctor
        print(Test.b)
        
    def lakshmi(self):  # instance method
        Test.c=30
        
    @classmethod
    def sai(cls): # class method
        print("The value of x before modyfying", Test.x)
        print(cls.x)
        Test.d=40
        Test.x=100   # modifying a static variable/class varaible
        print("The value of x after modyfying", Test.x)
        
    @staticmethod    
    def naveen():      # static method
        Test.e=50
          
    @staticmethod    
    def sandhya(): # static method
        Test.f=60