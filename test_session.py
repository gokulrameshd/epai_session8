import pytest
from math import *
from session8 import *
from test_utils import *

# def test_function_names():
#     assert function_name_had_cap_letter(session8) == False, "One of your function has a capitalized alphabet!"

def test_check_doc_string_1():
    assert True == check_doc_string(check_doc_string) ,'Worked!!!!'

def test_check_doc_string_2():
    assert True == check_doc_string(get_next_fib) ,'Worked!!!!'

def test_check_doc_string_3():
    assert True == check_doc_string(add) ,'Worked!!!!'

def test_check_doc_string_4():
    assert True == check_doc_string(mul) ,'Worked!!!!'

def test_check_doc_string_5():
    assert True == check_doc_string(div) ,'Worked!!!!'

def test_check_doc_string_6():
    assert True == check_doc_string(counter_1) ,'Worked!!!!'

def test_check_doc_string_7():
    assert True == check_doc_string(counter_2) ,'Worked!!!!'

def test_get_next_fib_1():
    g = get_next_fib() 
    assert 2 == g(), 'worked!!!'
    assert 3 == g() , 'worked!!!'

def test_add_1():
    assert 4 == add(3,1), 'worked!!'

def test_mul_1():
    assert 6 ==mul(2,3),'worked!!'

def test_div_1():
    assert 3 == div(6,2),'worked!!'

# counters = {}

counter_add1 = counter_1(add)
counter_mul1 = counter_1(mul)
counter_div1 = counter_1(div)

def test_counter_1_1():
    counter_add1(6,4)
    assert counters == {'add':1},'worked!!'

def test_counter_1_2():
    counter_mul1(6,4)
    assert counters == {'add':1,'mul':1},'worked!!'

def test_counter_1_3():
    counter_div1(6,4)
    assert counters == {'add':1,'mul':1,'div':1},'worked!!'

def test_counter_1_4():
    counter_add1(6,4)
    assert counters == {'add':2,'mul':1,'div':1},'worked!!'


c1 = {}
c2 = {}
c3 = {}

counter_add2_1 = counter_2(add,c1)
counter_add2_2 = counter_2(add,c2)
counter_add2_3 = counter_2(add,c3)
counter_mul2_1 = counter_2(mul,c1)
counter_mul2_2 = counter_2(mul,c2)
counter_mul2_3 = counter_2(mul,c3)
counter_div2_1 = counter_2(div,c1)
counter_div2_2 = counter_2(div,c2)
counter_div2_3 = counter_2(div,c3)

def test_counter_2_1_1():
    counter_add2_1(5,4)
    assert c1 == {'add': 1}

def test_counter_2_1_2():
    counter_mul2_1(5,4)
    assert c1 == {'add': 1,'mul':1}

def test_counter_2_1_3():
    counter_div2_1(5,4)
    assert c1 == {'add': 1,'mul':1,'div':1}


def test_counter_2_2_1():
    counter_add2_2(5,4)
    assert c2 == {'add': 1}

def test_counter_2_2_2():
    counter_mul2_2(5,4)
    assert c2 == {'add': 1,'mul':1}

def test_counter_2_2_3():
    counter_div2_2(5,4)
    assert c2 == {'add': 1,'mul':1,'div':1}


def test_counter_2_3_1():
    counter_add2_3(5,4)
    assert c3 == {'add': 1}

def test_counter_2_3_2():
    counter_mul2_3(5,4)
    assert c3 == {'add': 1,'mul':1}

def test_counter_2_3_3():
    counter_div2_3(5,4)
    assert c3 == {'add': 1,'mul':1,'div':1}

def test_counter_2_3_4():
    counter_div2_3(5,4)
    assert c3 == {'add': 1,'mul':1,'div':2}