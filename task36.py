a = input("введите здесь вашу фразу  ").split()
res = lambda a: tuple(tuple(a[i].split('=')) for i in range (len(a)))