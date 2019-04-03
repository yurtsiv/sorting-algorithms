class Stack:
  _stack = []
  top = -1

  def __init__(self, size):
    self._stack = [None] * size
  
  def push(self, elem):
    if (self.top + 1 == len(self._stack)):
      raise Exception("Stack is full")

    self.top += 1 
    self._stack[self.top]  = elem   
  
  def pop(self):
    if (self.top == - 1):
      raise Exception("Stack is empty")
    
    res = self._stack[self.top]
    self.top -= 1
    return res

  def is_empty(self):
    return self.top == -1