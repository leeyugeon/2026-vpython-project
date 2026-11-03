Web VPython 3.2
box(texture = "https://i.postimg.cc/zXHg1CZp/geulim1.png", size = vec(20,20,1), pos = vec(0,0,-1))
s= sphere(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9013NDPgRJy_s7teHHSmsYoXbvbAVgQiT-9NyTjMckQ&s=10",make_trail = True)
while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        s.pos = vec(0,0,0)
    if 'r' in k :
        s.color = color.red
        s.opacity = 0.5
    if s.pos.x < 8 and 'd'in k :
        s.pos.x = s.pos.x + 0.1
    if s.pos.x > -8 and 'a' in k :
        s.pos.x = s.pos.x - 0.1
    if s.pos.y < 8 and'w' in k :
        s.pos.y = s.pos.y + 0.1
    if s.pos.y > -8 and's' in k :
        s.pos.y = s.pos.y - 0.1
    
