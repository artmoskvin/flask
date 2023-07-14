import pytest
from main import function1, function2, function3

def test_function1():
    assert function1('input1') == 'expected_output1'
    assert function1('input2') == 'expected_output2'

def test_function2():
    assert function2('input1') == 'expected_output1'
    assert function2('input2') == 'expected_output2'

def test_function3():
    assert function3('input1') == 'expected_output1'
    assert function3('input2') == 'expected_output2'