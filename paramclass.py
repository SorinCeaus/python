class A:
        def __init__(self,param1,param2):
            # a _ elotag privatta teszi az elemet
            self._Params={1:param1,2:param2}

        def getParams(self):
	    keys = self._Params.values()
            return keys

a=A(111,222)
print a.getParams()
