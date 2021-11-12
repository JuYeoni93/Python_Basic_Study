# List, Tuple, Dictionary #
# List, Dictionary -> 수정 가능, Tuple -> 수정 불가
my_list = ['Kim','Ju','Yeon']
my_tuple = ('Kim','Ju','Yeon')
my_dict = {'Kim':'남','Ju':'여','Yeon':'남'}

my_list[0] = 'Park' #수정 가능
print(my_list)

#my_tuple[0] = 'Park' #수정 불가
print(my_tuple)

my_dict['Kim'] = '여' #수정 가능
print(my_dict)

# 자료형 변환 #
my_int = 1
my_int = str(my_int)
print(type(my_int))

# String #
# "" -> 문자열 1줄, '' , """"" -> 문자열 2+줄
my_str = "김씨가족"
my_str = """행복
하세요
안녕"""
print(my_str)

# Fommatting #
# %d %f %s
my_str = 'My name is %s' % 'Kim Ju Yeon'
print(my_str)

# Fomat #
# '{}'.format()
my_str = 'My name is {}'.format('Kim Ju Yeon')
my_str = '{} x {} = {}'.format(2,3,2*3)
print(my_str)

# Indexing #
# 문자열의 위치, 주소
my_name = "김왼손의 왼손코딩"
print(my_name[-1])
