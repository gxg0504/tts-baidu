file_name = '1.txt'
time_min =  26
time_sec = 22


try:
    with open(file_name, encoding='utf8') as file_obj:
    #由于书名不是英文，要加上 encoding='utf8'
        contents = file_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file' + file_name + ' does not exist.'
    print(msg)
else:
    words = contents.rstrip()
    num_words = len(words)
    print('The file ' + file_name + ' has about ' + str(num_words) + ' words.')

perWordTime = (time_min*60+time_sec)*1000/num_words
print(perWordTime)

import re
pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
pattern = r'[,.;?:，。；？：]'
pattern = r'(?:[\n,.;?:，。；？：\s])'
test_text = 'b,b.b/b;b\'b`b[b]b<b>b?b:b"b{b}b~b!b@b#b$b%b^b&b(b)b-b=b_b+b，b。b、b；b‘b’b【b】b·b！b b…b（b）b'
test_text = contents
result_list = re.split(pattern, test_text)
filter(None, result_list)
print(result_list)
while '' in result_list:
    result_list.remove('')
print(result_list)

with open('2.srt','w', encoding='utf8') as w:
    time_start_min = 0
    time_start_sec = 0
    time_start_mrc = 0
    time_end_min = 0
    time_end_sec = 0
    time_end_mrc = 0
    value = 0
    for x in result_list:
        a = str(result_list.index(x)+1)+'\n'
        w.write(a)
        value += (len(x)+1)*perWordTime
        time_end_mrc = value%1000
        time_end_sec = (value/1000)%60
        time_end_min = value/(60*1000)

        b = '00:%02d:%02d.%03d'%(time_start_min,time_start_sec,time_start_mrc)+ ' --> ' + '00:%02d:%02d.%03d'%(time_end_min,time_end_sec,time_end_mrc) + '\n'
        w.write(b)
        time_start_min = time_end_min
        time_start_sec = time_end_sec
        time_start_mrc = time_end_mrc
        c = x + '\n' +'\n'
        w.write(c)
        print(result_list.index(x)+1,len(x))


