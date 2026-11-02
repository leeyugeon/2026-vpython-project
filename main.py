Web VPython 3.2
s= sphere(texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-1GDgoU_D_6Ha3PoLsqWLjEcxZyyGvzaeeopedkCdZg&s=10")

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        s.pos = vec(0,0,0)
    if 'r' in k :
        s.color = color.red
        s.opacity = 0.5
    if 'd' in k :
        s.pos.x = s.pos.x + 0.1
    if 'a' in k :
        s.pos.x = s.pos.x - 0.1
    if 'w' in k :
        s.pos.y = s.pos.y + 0.1
    if 's' in k :
        s.pos.y = s.pos.y - 0.1
    
