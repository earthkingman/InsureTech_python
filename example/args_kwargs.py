def functest(*args,**kwargs):
    print("args:",args)
    print("kwargs:",kwargs)

functest("일태일","이태일","삼태일")
functest(my = "일태일")
