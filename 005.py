##t1 = (1, )
##t2 = (4, 5, 6)
##print(t1 + t2)
##print(t2 * 2)
##print(t2[0])
##print(t2[1:3])
##del t2[0]
##a = "Carpe Diem!"
##b = [1, 2, 3, 4, 5, 6]
##print(len(a))
##print(len(b))
##d = {'name' : 'Jane', 'name' :'Mason', 'age' : 12 , 'number'  : 123456}
##print(d)
##print(d['age'])
##s1 = set([1, 2, 3, 4, 5, 6])
##s2 = set([4, 5, 6, 7, 8, 9])
##print(s1 - s2)
##print(s1 & s2)
##print(s1 | s2)
##a = {'a' : 1, 'b' : 2, 'c' : 3, 'd' :4}
##print(a.keys())
##print(a.values())
##print(a.items())
##a.clear()
##print(a)
##a = {'name' :'Minsu', 'address' : 'seoul','phone' :'010-1234-1234'}
##print(a.keys())
##a = set([1, 2, 3])
##a.add(4)
##print(a)
##a.update('abc')
##print(a)
##a.remove('c')
##print(a)
##n = int(input('몇 단? '))
##a = 1
##print('%d * %d = %d ' % (n, a, n*a))
##a += 1
##print('%d * %d = %d ' % (n, a, n*a))
##a += 1
##print('%d * %d = %d ' % (n, a, n*a))
##a += 1
##print('%d * %d = %d ' % (n, a, n*a))
##a += 1
##print('%d * %d = %d ' % (n, a, n*a))
##a += 1
##print('%d * %d = %d ' % (n, a, n*a))
##a += 1
##print('%d * %d = %d ' % (n, a, n*a))
##a += 1
##print('%d * %d = %d ' % (n, a, n*a))
##a += 1
##print('%d * %d = %d ' % (n, a, n*a))
##import turtle

##t = turtle.Turtle()

##t.fillcolor('red')
##t.begin_fill()
##t.right(60)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.right(120)
##t.circle(25, 180)
##t.end_fill()

##t.fillcolor('yellow')
##t.begin_fill()
##t.right(60)
##t.circle(50)
##t.end_fill()

##turtle.done()
##import turtle

##t = turtle.Turtle()

##s = turtle.textinput('즐거운 씨큐브 코딩','이름을 알려주세요')

##t.write("%s님 반갑습니다^^" % s)

##turtle.done()
##import turtle

##t = turtle.Turtle(shape = "turtle")

##s = "즐거운 씨큐브 코딩"

##n = turtle.numinput(s, "앞으로 얼마나 이동할까요?")
##t.forward(n)

##ang = turtle.numinput(s, "앞으로 얼마나 이동할까요? :", default = 0, minval = 0, maxval = 360)
##t.right(ang)

##turtle.done()

a ={'a': 90, 'b': 85, 'c': 95}
a['a'] = 100
print(a['a'])
a['e'] = 70
print(a)












