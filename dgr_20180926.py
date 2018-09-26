Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienījamais lietotāj, lūdzu ievadi skaitli: ")
Cienījamais lietotāj, lūdzu ievadi skaitli: 100
100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienijamais lietotāj, lūdzu, ievadi skatilis: ")
Cienijamais lietotāj, lūdzu, ievadi skatilis: 100
>>> vars();
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 100, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
100
>>> mans_mainigais = input("Cienijamais lietotāj, lūdzu, ievadi skatilis: ")
Cienijamais lietotāj, lūdzu, ievadi skatilis: 200
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 200, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais = input("Cienijamais lietotāj, lūdzu, ievadi skatilis: ")
Cienijamais lietotāj, lūdzu, ievadi skatilis: 100
>>> mans_mainigais = input("Cienijamais lietotāj, lūdzu, ievadi skatilis: ")
Cienijamais lietotāj, lūdzu, ievadi skatilis: 200
>>> mans_mainigais = input("Cienijamais lietotāj, lūdzu, ievadi skatilis: ")
Cienijamais lietotāj, lūdzu, ievadi skatilis: 100
>>> x = mans_mainigais * mans_mainigais
>>> 
================= RESTART: /home/user/RTR105/test_1_20180926 =================
Cienījamais lietotāj, lūdzu ievadi skaitlis100
>>> 
================= RESTART: /home/user/RTR105/test_1_20180926 =================
Cienījamais lietotāj, lūdzu ievadi skaitlis: 100
>>> x = mans_mainigais * mans_mainigais

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x = mans_mainigais * mans_mainigais
NameError: name 'mans_mainigais' is not defined
>>> 
================= RESTART: /home/user/RTR105/test_1_20180926 =================
Cienījamais lietotāj, lūdzu ievadi skaitlis: 100
>>> vars()
{'mans_mainiigais': 100, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180926', '__package__': None, 'x': 10000, '__name__': '__main__', '__doc__': None}
>>> 
================= RESTART: /home/user/RTR105/test_1_20180926 =================
Cienījamais lietotāj, lūdzu ievadi skaitlis: 100
Lietotāj, TU esi Ievadījis vērtibu: 100
Kā arī tagad atmiņā ir ari x = 10000
>>> 
================= RESTART: /home/user/RTR105/test_1_20180926 =================
Cienījamais lietotāj, lūdzu ievadi skaitlis: 1.1000
Lietotāj, TU esi Ievadījis vērtibu: 1.1000
Kā arī tagad atmiņā ir ari x = 1.210
>>> type(mans_mainiigais)
<type 'float'>
>>> 
================= RESTART: /home/user/RTR105/test_1_20180926 =================
Cienījamais lietotāj, lūdzu ievadi skaitlis: 1.
Lietotāj, TU esi Ievadījis vērtibu: 1.0000
Kā arī tagad atmiņā ir ari x = 1.000
>>> 
