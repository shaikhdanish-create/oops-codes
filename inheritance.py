
#inherit code ex in teacher strt or end time 

class employee:
    start_time = "10am"
    end_time = "6pm"

class teacher(employee):
    def __init__(self, subject):
        self.subject = subject
        
t1 = teacher("math")


print(t1.subject, t1.start_time, t1.end_time)
