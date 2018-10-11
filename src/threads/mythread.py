import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)


def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      # print('inside thread run')
      counter -= 1


    # [Touraj] :: Following is useful Thread Methods

    # run() − The run() method is the entry point for a thread.
    #
    # start() − The start() method starts a thread by calling the run method.
    #
    # join([time]) − The join() waits for threads to terminate.
    #
    # isAlive() − The isAlive() method checks whether a thread is still executing.
    #
    # getName() − The getName() method returns the name of a thread.
    #
    # setName() − The setName() method sets the name of a thread.
