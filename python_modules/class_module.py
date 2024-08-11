#!/usr/bin/env python
# coding: utf-8

# In[1]:


class maths_p():
    def __init__(self,a,b):
        self.param1=a
        self.param2=b
        print("the parameter values is,",a ,b)
    def add_p(self):
        new_value=self.param1+self.param2
        return new_value
    def sub_p(self):
        new_value=self.param1 - self.param2
        return new_value
    def mul_p(self):
        new_value=self.param1 * self.param2
        return new_value
    def pwer_p(self):
        new_value=self.param1 ** self.param2
        return new_value
    

