# Description:
#Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#Some examples:
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # @param tokens, a list of string
    # @return an integer
    operator = ['+','-','*','/'] 
    
    @staticmethod
    def isOperator(token):
        if token in Solution.operator:
            return True
        else:
            return False
    
    @staticmethod
    def compute(operator, arg1, arg2):
        # evalute the operator and compute the arguments
        if operator is '+':
            return arg1 + arg2
        elif operator is '-':
            return arg2 - arg1
        elif operator is '/':
            return int(float(arg2)/float(arg1))
        elif operator is '*':
            return arg1*arg2
        else:
            print "Unknown operator"
            return None
        
    def evalRPN(self, tokens):
        token_stack = []
        input = tokens[::-1]
        while input:
            token = input.pop()
            if self.isOperator(token) is True:
                # find an operator. Get data from the stack and compute the result
                if len(token_stack) < 2:
                    # there are fewer than n values on the stack
                    print "Error: insufficient input values"
                else:
                    tmp = self.compute(token, token_stack.pop(), token_stack.pop())
                    if tmp is not None:
                        token_stack.append(tmp)
            else:
                # find a number
                token_stack.append(int(token))
        
        if len(token_stack) == 1:
            return token_stack.pop()
        else:
            print "The user input has too many values"
            
