# import the builtin time module, this is always available
import time

 

def main():
# initialize the t0 variable, "starting the stopwatch"
  t0 = time.time()


  run = True
  while run:
    # calculate the time since some reference point (here the Unix Epoch)
    t1 = time.time()

    # calculate the difference, i.e. the time elapsed
    dt = t1 - t0

    #if dt >= 5:
      #print ("Three seconds reached, resetting timer")
      #t0 = t1
    
    #else:
    print (format(dt,'.2f'))
    
    
  


