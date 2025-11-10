class item:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.ratio=value/weight

def greedy(items,capacity):
    items.sort(reverse=True,key=lambda  x: x.ratio)
    total_weight=0.0
    total_value=0.0
    for item in items:
        if (item.weight+total_weight<=capacity):
            total_value+=item.value
            total_weight+=item.weight
        else:
            remain=capacity-total_weight
            total_value+=remain*item.ratio
            break
    return total_value

if __name__=="__main__":
    n=int(input('Enter total no. of items: '))
    items=[]
    for i in range(n):
        w=float(input(f"Enter wight of item no. {i+1} :" ))
        v=float(input(f"Enter value of item no. {i+1} :" ))
        items.append(item(w,v))
    capacity=float(input("Enter maximum capacity of the knapsack: "))
    print("The maximum value in knapsack = ",greedy(items,capacity))
