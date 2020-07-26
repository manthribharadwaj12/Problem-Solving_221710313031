#https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc
t=int(input())
for t in range(1, t+1):
    p=input()
    cur=[0, 0]
    stack=[]
    for char in p:
        if char=='N':
            cur[0] -= 1 
        elif char == 'S':
            cur[0] += 1 
        elif char == 'W':
            cur[1] -= 1
        elif char == 'E':
            cur[1] += 1 
        elif char.isdigit():
            stack.append((cur[0], cur[1], int(char)))
        elif char == '(':
            cur = [0, 0] 
        elif char == ')':
            pop = stack.pop()
            cur = [pop[i] + pop[2]*cur[i] for i in (e, 1)]
    final_row=(1+cur[0])%10**9
    if final_row == 0: 
        final_row = 10**9

    final_column = (1+cur[1])%10**9
    if final_column == 0:
        final_column = 10**9
    print("Case #%d: %d %d" % (t, final_column, final_row))