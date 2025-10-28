colors=['Red','Blue','Green','yellow','indigo']
states=['a','b','c','d','e']
n={}
n['a']=['b','c','d']
n['b']=['a','d','c']
n['c']=['a','d','b']
n['d']=['c','b','a']
n['e']=['a','b','c']
c={}
def prom(state,color):
    for n1 in n.get(state):
        cn=c.get(n1)
        if cn==color:
            return False
    return True
def get_s(state):
    for color in colors:
        if prom(state,color):
            return color
def main():
    for state in states:
        c[state]=get_s(state)
    print(c)
main()

#output:{'a': 'Red', 'b': 'Blue', 'c': 'Green', 'd': 'yellow', 'e': 'yellow'}
