

import random
import time


current_time = time.localtime()
myday = time.strftime("%A", current_time)
mymonthanddate = time.strftime("%B %d", current_time)


generate_random = list(range(2, 90))

random.seed()  
for i in range(8):
    random_value = random.choice(generate_random) 
    print(f"The Lucky numbers for {myday} ,{mymonthanddate} are {random_value} " ) 
    
