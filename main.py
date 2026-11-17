Web VPython 3.2
box(texture = "https://i.postimg.cc/zXHg1CZp/geulim1.png", size = vec(20,20,1), pos = vec(0,0,-1))
box(size = vec(5,1,1), pos = vec(-3,5,1), opacity =1)
s= sphere(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9013NDPgRJy_s7teHHSmsYoXbvbAVgQiT-9NyTjMckQ&s=10")
vv = []
import random
for i in range(3) : 
    vv.append(sphere(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaE8oTpG6jbnFVxxY6JtNJ38zxzD1UZtuYi5eqyVeMIw&s=10",pos = vec(random.randint(-5,5),random.randint(-5,5),0)))

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        s.pos = vec(0,0,0)
    for v in vv : 
        v.pos = v.pos + (s.pos - v.pos) * 0.01 + vec(random.uniform(-0.1,0.1), random.uniform(-0.2,0.2), 0)
    if s.pos.x < 8 and 'd'in k :
        s.pos.x = s.pos.x + 0.1
    if s.pos.x > -8 and 'a' in k :
        s.pos.x = s.pos.x - 0.1
    if s.pos.y < 8 and'w' in k :
        s.pos.y = s.pos.y + 0.1
    if s.pos.y > -8 and's' in k :
        s.pos.y = s.pos.y - 0.1
