import sys 

from classes import Calc
from classes import Animation_Writer

calc = Calc()
ani = Animation_Writer()

if sys.argv[1] == "NsolveODE":

    y_prime: str = sys.argv[2]
    point: tuple = eval(sys.argv[3])
    end: float = float(sys.argv[4]) 
    step: float = float(sys.argv[5])

    #print(y_prime, type(y_prime))
    print(point, type(point))
    #print(end, type(end))
    #print(step, type(step))

    x,y = calc.NsolveODE(y_prime, point, end, step)
    ani.generate_Graf(x,y)
    ani.generate_Axis()

    # for i in (1,0.5):

    #     x,y = calc.NsolveODE(y_prime, (0,1),5,i)
    #     ani.generate_Graf(x,y)
    print(f"y({end}) is about {round(y[-1], 4)}")
#    ani.run_Animation()
    ani.generate_Plot()