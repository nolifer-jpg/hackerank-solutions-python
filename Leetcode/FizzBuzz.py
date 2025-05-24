class Solution(object):
    def interpret(self, command):
        if "()" in command and "(al)" in command:
            command = command.replace("()", "o")
            command = command.replace("(al)", "al")
        return command    
        