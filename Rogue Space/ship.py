import data as g
import environ

class Ship():
    def __init__(self,model):
        self.type = model
        if model == 1:
            self.makeShip([
                [g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1],
                [g.E.WALL1,g.E.FLOOR,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.FLOOR,g.E.WALL1,g.E.WALL1,g.E.SPACE],
                [g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.WALL1,g.E.SPACE],
])
        elif model == 2:
            self.makeShip([ [g.E.FLOOR if i % 2 ==1 else g.E.FLOOR for i in range (55)] for i in range (30)] )
            
    def makeShip(self,text):
        g.MWIDTH
        g.MHEIGHT

        width = len(text[0])
        height = len(text)
        xfiller = yfiller = 5
        if width < g.Xt:
            xfiller = (g.Xt-len(text[0])) // 2 + 5
            width = g.Xt

        if height < g.Yt:
            yfiller = (g.Yt-len(text))//2 + 5
            height = g.Yt 
        
        for i in range(yfiller):## top filler stars
            g.playMap.append([environ.Environ(g.E.SPACE) for i in range(width+10)])   
        for y in range(len(text)):
            g.playMap.append([])##new y row
            for i in range(xfiller):##left filler
                g.playMap[y+yfiller].append(environ.Environ(g.E.SPACE))
            for x in range(len(text[0])):#content
                g.playMap[y+yfiller].append(environ.Environ(text[y][x]))
                
            for i in range(xfiller):#right filler
                g.playMap[y+yfiller].append(environ.Environ(g.E.SPACE))
        for i in range(yfiller):# bottom filler stars
            g.playMap.append([environ.Environ(g.E.SPACE) for i in range(width+10)])
        
        g.MWIDTH = width+10
        g.MHEIGHT = height+10
