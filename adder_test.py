import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random

@cocotb.test()
def adder_test(dut):
    """Test for 5 + 1"""
    yield Timer(2)
    
    dut.A = 5
    dut.B = 1
    
    yield Timer(2)
    
    if dut.X != 6:
        raise TestFailure(
            "Adder result is incorrect: %s != 15" % str(dut.X)) 
    else: # these last two lines are not strictly necessary
        dut.log.info("Ok!")
