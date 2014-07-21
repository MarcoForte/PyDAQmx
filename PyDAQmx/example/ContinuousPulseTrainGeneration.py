from PyDAQmx.DAQmxFunctions import *
from PyDAQmx.DAQmxConstants import *

try:
    input = raw_input
except NameError:
    pass

class ContinuousPulseTrainGeneration():
    """ Class to create a continuous pulse train on a counter
    
    Usage:  pulse = ContinuousTrainGeneration(period [s],
                duty_cycle (default = 0.5), counter (default = b"dev1/ctr0"),
                reset = True/False)
            pulse.start()
            pulse.stop()
            pulse.clear()
    """
    def __init__(self, period=1., duty_cycle=0.5, counter=b"Dev1/ctr0", reset=False):
        if reset:
            DAQmxResetDevice((counter.decode('utf-8').split('/')[0]).encode('utf-8'))
        taskHandle = TaskHandle(0)
        DAQmxCreateTask(b"",byref(taskHandle))
        DAQmxCreateCOPulseChanFreq(taskHandle,counter,b"",DAQmx_Val_Hz,DAQmx_Val_Low,
                                                                   0.0,1/float(period),duty_cycle)
        DAQmxCfgImplicitTiming(taskHandle,DAQmx_Val_ContSamps,1000)
        self.taskHandle = taskHandle
    def start(self):
        DAQmxStartTask(self.taskHandle)
    def stop(self):
        DAQmxStopTask(self.taskHandle)
    def clear(self):
        DAQmxClearTask(self.taskHandle)


if __name__=="__main__":
    pulse_gene1 = ContinuousPulseTrainGeneration(1.,0.5, b"dev1/ctr0", reset=True)
    pulse_gene1.start()
    a = input("Generating pulse train. Press Enter to interrupt\n")
    pulse_gene1.stop()
    pulse_gene1.clear()
   


