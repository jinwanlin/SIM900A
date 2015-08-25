def test():
     clsname = "classname"
#     method = 
     params="jinwanlin"
     obj = __import__(clsname) # import module
     c = getattr(obj,clsname)
     obj = c() # new class
     mtd = getattr(obj,"echo")
     mtd(params) # call def
 
if __name__ == '__main__':
    test("classname.echo('jinwanlin')") 
    