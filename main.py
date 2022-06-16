# list_num = []
# for i in 'bla23bla1bla8bla2':
#     try:
#         num = int(i)
#         list_num.append(num)
#     except ValueError:
#         continue
# print(list_num)

# s = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(" ".join(map(lambda x: '"%s"' % __import__('re').sub('\d+', lambda x: f'{x[0]}'.zfill(2), x) if any(map(str.isdigit, x)) else x, s)))
# a = '0123456789qwerty'
# for x in a:
#     print('= ', x, ' =')
# print(a[::-1])


# arr = ['директор Aэлитa']
# str_arr = ''
# count = -1
# for i in arr:
#     while i[count] != ' ':
#        str_arr += str(i[count]).lower()
#        count -= +1
# str_arr = str_arr[::-1]
# print('Привет, ' + str_arr.title() + '!')

# a = '1.02'
# a.isdigit()
# a_new = str(a[a.find('.')+1:])
#
# print(a_new) # 02