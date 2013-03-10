import data as g
import environ

class Ship():
    def __init__(self,model):
        self.layout =[]
        if model == 1:
             self.makeShip([
                ["\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","."],
                ["\u0114","\u00B7","\u00B7","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u00B7","\u0114","\u0114","."],
                ["\u0114","\u00B7","\u00B7","\u00B7","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u0114","\u0114","\u0114"],
                ["\u0114","\u00B7","\u00B7","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u0114","\u0114"],
                ["\u0114","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u0114"],
                ["\u0114","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u0114"],
                ["\u0114","\u00B7","\u00B7","\u00B7","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u0114","\u0114"],
                ["\u0114","\u00B7","\u00B7","\u00B7","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u00B7","\u00B7","\u00B7","\u00B7","\u00B7","\u0114","\u0114","\u0114"],
                ["\u0114","\u00B7","\u00B7","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u00B7","\u0114","\u0114","."],
                ["\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","\u0114","."],
])
        elif model == 2:
            self.makeShip([ ["\u00B7" if i % 2 ==1 else "\u00AA" for i in range (55)] for i in range (30)] )
            
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
            g.playMap.append([environ.Environ('.') for i in range(width+10)])   
        for y in range(len(text)):
            g.playMap.append([])##new y row
            for i in range(xfiller):##left filler
                g.playMap[y+yfiller].append(environ.Environ('.'))
            for x in range(len(text[0])):#content
                g.playMap[y+yfiller].append(environ.Environ(text[y][x]))
                
            for i in range(xfiller):#right filler
                g.playMap[y+yfiller].append(environ.Environ('.'))
        for i in range(yfiller):# bottom filler stars
            g.playMap.append([environ.Environ('.') for i in range(width+10)])
        
        MWIDTH = width+10
        MHEIGHT = height+10
