#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
n = int(input('enter how many phone numbers you want to check:'))                                
for i in range(1,n+1):
    print('')
    x = input('Enter Phone Number:')
    a = re.findall('[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$',x)
    b =str(x)
    c = re.findall('[a-zA-Z]',x)
    d = re.findall('[+]',x)
    e = re.findall('^[0-5]',x)
    f = re.findall('[0-9]',x)
    ap1 = re.findall('^[9][0][0][0]|^[9][0][1][0|4]|^[9][0][6][3]|^[9][0][3][0|2]|^[9][0][5][2|9]|^[9][2][4][7|8]|^[9][3][4][6|7]|^[9][3][8][1]|^[9][3][9][0|1|2|4|5|6|7|8]|^[9][4][4][0|1]',x)
    ap2 = re.findall('^[9][4][9][0|1|2|3|4]|^[9][5][0][2|5]|^[9][5][1][5]|^[9][5][4][2]|^[9][5][5][0|3]|^[9][5][7][3]|^[9][6][0][3]|^[9][6][1][8]|^[9][6][4][0|2]|^[9][6][5][2]',x)
    ap3 = re.findall('^[9][6][6|7][6]|^[9][7][0][1|3|4|5]|^[9][8][4][8|9]|^[9][8][6][6]|^[9][9][0][8]|^[9][9][1][2]|^[9][9][4][8|9]|^[9][9][5][1|9]|^[9][9][6][6]|^[9][9][8][5|9]',x)
    ap4 = re.findall('^[9][1][0][0]|^[9][1][2][1]|^[9][1][3][3]|^[9][1][5][4]|^[9][1][6][0]|^[9][1][7][7]|^[9][1][8][0|2]|^[8][0][0][8]|^[8][0][1][9]|^[8][0][7][4]',x)
    ap5 = re.findall('^[8][0][9][6|9]|^[8][1][0][6]|^[8][1][2][5]|^[8][1][4][2|3]|^[8][1][8][4|5|6|7]|^[8][2][9][7]|^[8][3][0][9]|^[8][3][2][8]|^[8][3][4][1]|^[8][3][7][4]',x)
    ap6 = re.findall('^[8][4][6][5]|^[8][5][0][0|1]|^[8][5][2][2]|^[8][5][5][5]|^[8][6][3][9]|^[8][6][8][6|8]|^[8][7][1][2]|^[8][7][5][2]|^[8][7][9][0]|^[8][8][0][1]|^[8][8][8][5|6]',x)
    ap7 = re.findall('^[8][8][9][7]|^[8][9][1][9]|^[8][9][7][7]|^[8][9][8][5]|^[6][3][0][1-5]|^[7][0][1][3]|^[7][0][3][2|6]|^[7][0][9][5]|^[7][2][0][7]|^[7][3][8|9][6]',x)
    ap8 = re.findall('^[7][4][1][6]|^[7][5][6][9]|^[7][6][5][8|9]|^[7][6][7][0|1]|^[7][6][7][5]|^[7][7][0][2]|^[7][7][3][1]|^[7][7][9][4|9]|^[7][8][4][2]|^[7][8][9][3]',x)
    ap9 = re.findall('^[7][9][0|8][1]|^[7][9][8][9]|^[7][9][9][3|5]|^[7][9][9][7] ',x)
    tn1 = re.findall('^[9][0][0][3]|^[9][0][2][5]|^[9][0][4][2|3]|^[9][0][4][7]|^[9][0][8][0|7]|^[9][0][9][2|5]|^[9][1][5][0|9]|^[9][1][9][5]|^[9][2][4][4|5]|^[9][3][4][4|5]',x)
    tn2 = re.findall('^[9][3][6][0|1|2|3|4|5]|^[9][3][6][7]|^[9][3][8][4|5]|^[9][4][4][2|3|5]|^[9][4][8][6|7|8|9]|^[9][5][0][0]|^[9][5][1|2][4]|^[9][5][6][6]|^[9][5][7][8]',x)
    tn3 = re.findall('^[9][5][8][5]|^[9][5][9][7]|^[9][6][0][0]|^[9][6][2][6]|^[9][6][2][9]|^[9][6][7][7]|^[9][6][8|9][8]|^[9][7][1][5]|^[9][7][5][0|1]|^[9][7][8][6|7|8|9]',x)
    tn4 = re.findall('^[9][7][9][0|1]|^[9][8][4][2|3]|^[9][8][6][5]|^[9][8][9][4]|^[9][9][4][2|3|4]|^[9][9][5][2]|^[9][9][6][5]|^[9][9][7][6]|^[9][9][9][4]|^[8][0][1][2|5]',x)
    tn5 = re.findall('^[8][0][5][6]|^[8][0][7][2]|^[8][0][9][8]|^[8][1][2][2]|^[8][1][2][4]|^[8][1][4][8]|^[8][2][2][0]|^[8][2][4][8]|^[8][3][4][4]|^[8][4][2][8]|^[8][4][3][8]',x)
    tn6 = re.findall('^[8][4][8][9]|^[8][5][0][8]|^[8][5][2][6]|^[8][6][1][0]|^[8][6][6][7|8]|^[8][6][7][5]|^[8][6][8][0|1|2]|^[8][6][9][5]|^[8][7][5][4]|^[8][7][6][0]',x)
    tn7 = re.findall('^[8][8][0][7]|^[8][8][2][5]|^[8][8][3][8]|^[8][8][7][0]|^[8][8][8][3]|^[8][9][0|7][3]|^[8][9][9][4]|^[7][0][1][0]|^[7][0][9][2|4]|^[7][1][3][8]|^[7][2][0][0]',x)
    tn8 = re.findall('^[7][3][0][5]|^[7][3][5][8]|^[7][3][7][3]|^[7][4][0][1]|^[7][4][1][8]|^[7][5][0][2|^[7][5][4][0|8]|^[7][6][0][4]|^[7][6][3][9]|^[7][6][6][7]',x)
    tn9 = re.findall('^[7][7][0][8]|^[7][8][1][0]|^[7][8][4][5]|^[7][8][7][1]|^[7][9][0][4]|^[6][0][0][3]|^[6][3][8][0]|^[6][3][8][1]',x)
    jk1 = re.findall('^[9][0][1][8]|^[9][0][5][5]|^[9][0][7][0]|^[9][0][8][6]|^[9][1][0][7]|^[9][1][8][6]|^[9][4][6][9]|^[9][4][8][4]|^[9][5][4][1]|^[9][5][9][6]',x)
    jk2 = re.findall('^[9][6][2][2]|^[9][6][9][7]|^[9][7][9][6|7]|^[9][8][5][8]|^[9][9][0][6]|^[8][4][9][2]|^[8][7][1][3|5|6]|^[8][8][0][3]|^[7][0][0][6]|^[7][0][5][1]|^[7][2][9][8]|^[6][0][0][5|6]',x)
    ka1 = re.findall('^[9][0][3][5|6]|^[9][0][6][6]|^[9][0][7][1]|^[9][1][0][8]|^[9][1][1][0]|^[9][1][4][1]|^[9][1][4][8]|^[9][1][6][4]|^[9][1][8][7]|^[9][3][4][2|3]',x)
    ka2 = re.findall('^[9][3][7][9]|^[9][3][8][0]|^[9][4][4][8|9]|^[9][4][8][1|2|3]|^[9][5][1][3]|^[9][5][3][5|9]|^[9][5][9][0|1]|^[9][6][0][6]|^[9][6][1][1]|^[9][6][3][2]',x)
    ka3 = re.findall('^[9][6][6][3]|^[9][6][8][6]|^[9][7][3][8|9]|^[9][7][4][0|1|2|3]|^[9][8][4][4|5]|^[9][8][8][6]|^[9][9][0][0|1|2]|^[9][9][1][6]|^[9][9][4][5]|^[9][9][6][4]|^[9][9][7][2]',x)
    ka4 = re.findall('^[9][9][8][0]|^[8][0][5][0]|^[8][0][7][3]|^[8][0][8][8]|^[8][0][9][5]|^[8][1][0][5]|^[8][1][2][3]|^[8][1][4][7]|^[8][1][5][0|1|2]|^[8][2][1|7][7]',x)
    ka5 = re.findall('^[8][3][1][0]|^[8][4][3][1]|^[8][4][5][3]|^[8][4][9][4|5|6|7]|^[8][5][4][6|8|9]|^[8][5][5][0|3]|^[8][6][1][8]|^[8][6][6][0]|^[8][7][1][1]|^[8][7][2][2]',x)
    ka6 = re.findall('^[8][7][4][6|7|8|9]|^[8][7][9][2]|^[8][8][6][1|7]|^[8][8][8][4]|^[8][8][9][2]|^[8][9][0][4]|^[8][9][5][1]|^[8][9][7][0|1]',x)
    ka7 = re.findall('^[7][0][1][9]|^[7][0][2][2|6]|^[7][0][9][0]|^[7][2][0][4]|^[7][3][3][7|8]|^[7][3][4][8|9]|^[7][3][5][3]|^[7][4][0][6]|^[7][4][1][1]|^[7][4][8][3]',x)
    ka8 = re.findall('^[7][6][1][9]|^[7][6][2][4|5]|^[7][6][7][6]|^[7][7][6][0]|^[7][7][9][5]|^[7][8][1][3]|^[7][8][2][9]|^[7][8][4][6|9]|^[7][8][9][2]|^[7][8][9][9]|^[7][9][7][5]|^[7][9][9][6]|^[6][3][6][0|1|2|3|4|6]',x)
    bj1 = re.findall('^[9][0][0][6]|^[9][0][3][1]|^[9][0][6][0|5]|^[9][0][9][7]|^[9][1][0][2]|^[9][1][2][2|3|8]|^[9][1][3][5]|^[9][1][4][2]|^[9][1][5][5]|^[9][1][6][2]',x)
    bj2 = re.findall('^[9][1][9][9]|^[9][2][6][2]|^[9][3][0|3][4]|^[9][3][4][1]|^[9][3][8][6]|^[9][4][3][0|1]|^[9][4][7][0|1|2]|^[9][5][0][4|7|8]|^[9][5][2][3|5]|[9][5][3][4]',x)
    bj3 = re.findall('^[9][5][4][6]|^[9][5][7][0|6]|^[9][6][0][8]|^[9][6][3|6][1]|^[9][6][9][3]|^[9][7][0][8|9]|^[9][7][7][1]|^[9][7][9][8]|^[9][8][0][1]|^[9][8][5][2]',x)
    bj4 = re.findall('^[9][9][0][5]|^[9][9][3][1|4|9]|^[9][9][7][3]|^[8][0][0][2]|^[8][0][5][1]|^[8][0][8][3|4]|^[8][0][9][2]|^[8][1][0][2]|^[8][2][0][7]|^[8][2][1][0]',x)
    bj5 = re.findall('^[8][2][2][7|8|9]|^[8][2][3][5]|^[8][2][5][2]|^[8][2][7][1]|^[8][2][9][2|4|8]|^[8][3][0][0]|^[8][3][4][0]|^[8][4][0][4|5|6|7|9]|^[8][4][3][4]|^[8][5][0][7]',x)
    bj6 = re.findall('^[8][5][2][1]|^[8][5][3][8|9]|^[8][5][4][0|4]|^[8][6][0][3]|^[8][6][5][1]|^[8][6][7][4|6|7]|^[8][7][0][9]|^[8][7][5][7]|^[8][7][8][9]|^[8][7][9][7]',x)
    bj7 = re.findall('^[8][8][0][4|9]|^[8][8][6|7][3]|^[8][9][6][9]|^[8][9][8][6|7]|^[7][0][0][4]|^[7][0][5][0]|^[7][0][6][1]|^[7][0][7][7|9]|^[7][0][9][1]|^[7][2][0][9]',x)
    bj8 = re.findall('^[7][2][5][0|4|5|6|7]|^[7][2][7][3|7]|^[7][2][8][0|1|2|3]|^[7][3][0][1]|^[7][3][1][9]|^[7][3][2][2|3|4]|^[7][3][5][2]|^[7][3][6][0|1|2]|[7][3][7][0]',x)
    bj9 = re.findall('^[7][4][6][3]|^[7][4][8][8]|^[7][4][9][3|4]|^[7][5][2][0]|^[7][5][4][3|4|6|7|9]|[7][5][5][7]|^[7][5][6][2|3|4]|^[7][6][5][4]|^[7][6][7][7]|^[7][7][0][0|7]',x)
    bj10= re.findall('^[7][7][1][7]|^[7][7][3][9]|^[7][7][6][2|3|4]|^[7][7][8][0|8]|^[7][8][7][0]|^[7][9][0][3]|^[7][9][7][9]|^[7][9][9][1|2]|^[6][0][0][0]|^[6][2][0][1|2|3|4|5|6|7|9]',x)
    rj1 = re.findall('^[9][0][0][1]|^[9][0][2][4]|^[9][0][7][9]|^[9][1][1][6]|^[9][1][6][6]|^[9][1][9][4]|^[9][3][1][4]|^[9][3][5][1|2|8]|^[9][3][7][4|5|6]|^[9][4][1][3|4]',x)
    rj2 = re.findall('^[9][4][6][0|1|2]|^[9][5][0][9]|^[9][5][3][0]|^[9][5][4][9]|^[9][5][7][1]|^[9][6][0][2]|^[9][6][1][0]|^[9][6][6][0]|^[9][6][7][2]|^[9][6][8][0]|^[9][6][9][4]',x)
    rj3 = re.findall('^[9][7][7][2]|^[9][7][8][2|3|5]|^[9][7][9][9]|^[9][8][2][8|9]|^[9][8][8][7]|^[9][9][2][8|9]|^[9][9][5][0]|^[9][9][8][2|3]|^[8][0][0][3]|^[8][0][5][8]',x)
    rj4 = re.findall('^[8][0][9][4]|^[8][1][0][7]|^[8][1][1][2|8]|^[8][2][3][3|9]|^[8][2][9][0]|^[8][3][0][2]|^[8][4][2][6]|^[8][4][3][2|3]|^[8][5][0][1|3|4]|^[8][5][6][0|1]',x)
    rj5 = re.findall('^[8][6][9][0|6]|^[8][7][4][1]|^[8][7][6][4|9]|^[8][8][7][5]|^[8][8][9][0]|^[8][9][0][5]|^[8][9][5][5]|^[8][9][9][3|7]|^[7][0][1][4]|^[7][0][2][3]',x)
    rj6 = re.findall('^[7][3][5][7]|^[7][5][6][8]|^[7][5][9][7]|^[7][6][6][5]|^[7][7][2][7]|^[7][7][4][2]|^[7][7][9][0]|^[7][8][7][7]|^[7][8][9][1]|^[7][9][7][6]|^[6][3][7][7]',x)
    am1 = re.findall('^[9][0][6][4]|^[9][0][8][5]|^[9][1][0][1]|^[9][1][2][7]|^[9][1][3][4]|^[9][1][8][1]|^[9][4][0][1]|^[9][5][7][7]|^[9][6][0][7]|^[9][6][1][3]|^[9][6][7][8]',x)
    am2 = re.findall('^[9][7][0][6|7]|^[9][8][5][4|9]|^[9][8][6][4]|^[9][9][5][4|7]|^[8][0][1][1]|^[8][4][0][2|3]|^[8][4][8][6]|^[8][7][2][4]|^[8][8][1][1]|^[8][8][2][2]',x)
    am3 = re.findall('^[8][8][7][6]|^[7][0][0][2]|^[7][0][3][5]|^[7][0][8][6]|^[7][0][9][9]|^[7][5][7][7]|^[7][6][3][6]|^[7][8][9][6]|^[6][0][0][1|2]',x)    
    gj1 = re.findall('^[9][0][1][6]|^[9][0][2|3][3]|^[9][0][6][7]|^[9][0][9][9]|^[9][1][0][4]|^[9][1][5][7]|^[9][1][7][3]|^[9][1][8][4]|^[9][3][1][3|6]|^[9][3][2][7|8]',x)
    gj2 = re.findall('^[9][3][7][7]|^[9][4][0][8|9]|^[9][4][2][6|7|8|9]|^[9][5][1][0|2]|^[9][5][5][8]|^[9][5][7][4]|^[9][5][8][6]|^[9][6][0][1]|^[9][6][2][4]|^[9][6][3][8]',x)
    gj3 = re.findall('^[9][6][6][2]|^[9][6][8][7]|^[9][7][1][2|4]|^[9][7][2][2|3|4|5|6|7]|^[9][8][2][4|5]|^[9][8][7][9]|^[9][9][0][4|9]|^[9][9][1][3]|^[9][9][2][4|5]|^[9][9][7][4|8|9]',x)
    gj4 = re.findall('^[9][9][9][8]|^[8][0][0][0]|^[8][1][2][8]|^[8][1][4][0|1]|^[8][2][0][0]|^[8][2][3][8]|^[8][2][6][4]|^[8][4][0][1]|^[8][4][6][0|9]|^[8][4][8][7]',x)
    gj5 = re.findall('^[8][5][1][1]|^[8][5][3][0]|^[8][7][5][8]|^[8][8][4][9]|^[8][8][6][6]|^[8][9][8][0]|^[7][0][1][6]|^[7][0][4][1|3|6]|^[7][0][7][2]|^[7][0][9][6]',x)
    gj6 = re.findall('^[7][1][1][1]|^[7][1][7][1]|^[7][2][2][2]|^[7][3][3][3]|^[7][3][5][9]|^[7][4][7][4]|^[7][4][9][0]|^[7][5][6][7]|^[7][5][7][5]|^[7][6][0][0]|^[7][6][9][8]',x)
    gj7 = re.findall('^[7][7][1][1]|^[7][7][2][2]|^[7][7][3][3]|^[7][7][7][1|2|3|6|7|8|9]|^[7][7][8][8]|^[7][8][1][7]|^[7][8][7][4]|^[7][8][7][8]|^[7][8][1][7]|^[7][8][7][4]|^[7][8][7][8]|^[7][9][8][4]|^[7][9][9][0]|^[6][3][5][1|2|4|9]',x)
    ne1 = re.findall('^[9][0][7][7]|^[9][0][8][9]|^[9][1][4][7]|^[9][1][9][1]|^[9][3][7][8]|^[9][4][0][2]|^[9][4][8][5]|^[9][6][1][2]|^[9][6][1][5]|^[9][7][7][4]|^[9][8][5][6]',x)
    ne2 = re.findall('^[9][8][6][2|3]|^[8][0][1][4]|^[8][1][1][9]|^[8][4][1][4]|^[8][5][7][5]|^[8][7][9][4]|^[8][8][8][0]|^[8][9][5][2]|^[7][0][0][5]|^[7][0][8][5]|^[7][3][0][8]|^[6][0][0][9]|^[6][9][0][9]',x)
    kl1 = re.findall('^[9][0][2][0]|^[9][0][3][7]|^[9][0][6][1]|^[9][0][4][8]|^[9][0][7][4]|^[9][1][8][8]|^[9][2][0][7]|^[9][3][4][9]|^[9][3][8][3|7|8]|^[9][4][0][0]',x)
    kl2 = re.findall('^[9][4][4][6|7]|^[9][4][9][5|6|7]|^[9][5][1|2][6]|^[9][5][6][2|7]|^[9][6][0|4][5]|^[9][6][3][3]|^[9][6][5][6]|^[9][7][4][4|5|7]|^[9][8][0][9]|^[9][8][4][6|7]',x)
    kl3 = re.findall('^[9][8][9][5]|^[9][9][6][1]|^[9][9][9][5]|^[8][0][7][5]|^[8][0][8][6]|^[8][0][8][9]|^[8][1][1][1|3]|^[8][1][2][9]|^[8][1][3][6|7|8]|^[8][1][5][7]|^[8][2][3][0|1|2]',x)
    kl4 = re.findall('^[8][2][8][1]|^[8][3][0][1|4]|^[8][5][4][7]|^[8][5][4][7]|^[8][5][9][0|2]|^[8][6][0][6]|^[8][8][4][8]|^[8][8][9][1|3]|^[8][9][0][1]|^[8][9][2][1]|^[8][9][4][3]',x)
    kl5 = re.findall('^[7][0][1][2]|^[7][0][2][5]|^[7][0][3][4]|^[7][1][0][2]|^[7][2][9][3]|^[7][3][0|5][6]|^[7][4][2][9]|^[7][5][1][0]|^[7][5][5][9]|^[7][5][9][2]|^[7][7][3][6]',x)
    kl6 = re.findall('^[7][9][0][2|7]|^[7][9][9][4]|^[6][2][3][5]|^[6][2][3][8]|^[6][2][8][2]|^[8][7][1][4]',x)
    od1 = re.findall('^[9][0][4][0]|^[9][0][7][8]|^[9][0][9][0]|^[9][1][1|2][4]|^[9][1][3][2]|^[9][1][7][8]|^[9][1][9][2]|^[9][3][3][7|8]|^[9][4][3][8|9]|^[9][5][5][6]',x)
    od2 = re.findall('^[9][5][8][3]|^[9][6][5|6][8]|^[9][6][9][2]|^[9][7][7][6|7|8]|^[9][8][5][3]|^[9][8][6][1]|^[9][9][3][7|8]|^[8][0][1][8]|^[8][0][9][3]|^[8][2][4][9]',x)
    od3 = re.findall('^[8][2][6|7|8][0]|^[8][3][3][8|9]|^[8][4][8][0]|^[8][5][9][9]|^[8][6][5][8]|^[8][7][6][3]|^[8][8][9][5]|^[8][9][0][8]|^[8][9][1][7]|^[8][9][8][4]|^[7][0][0][8]',x)
    od4 = re.findall('^[7][0][6][4]|^[7][0][7][7]|^[7][2][0][5]|^[7][3][2][5]|^[7][3][7][7]|^[7][3][8][1]|^[7][7][3][5]|^[7][8][0][9]|^[7][8][7][3]|^[7][8][9][4]|^[7][9][7][8]',x)
    hp1 = re.findall('^[9][0][1][5]|^[9][0][5][4]|^[9][1][0][6]|^[9][1][3][9]|^[9][1][8][5]|^[9][3][1][7]|^[9][4][5][9]|^[9][7][3][6]|^[9][8][0][5]|^[9][8][1][6]|^[9][8][5][7]',x)
    hp2 = re.findall('^[9][8][8][2]|^[8][0][9][1]|^[8][2][6][1|2|3]|^[8][2][1][9]|^[8][6][7][9]|^[8][8][9][4]|^[8][9][8][8]|^[7][8][0][7]|^[7][8][3][3]',x)
    hr1 = re.findall('^[9][0][1][7]|^[9][0][3][4]|^[9][0][5][0|3]|^[9][1][0][5]|^[9][1][3][8]|^[9][3][0][6]|^[9][3][5][0]|^[9][4][1|6][6]|^[9][4][6][7|8]|^[9][5][1|8][8]',x)
    hr2 = re.findall('^[9][6][7][1]|^[9][6][8][3]|^[9][7][2][8|9]|^[9][8][0|1][2]|^[9][8][1][3|7]|^[9][8][9][6]|^[9][9][9][1|2|6]|^[8][0][5][3|9]|^[8][1][2][1]|^[8][1][6][8]',x)
    hr3 = re.findall('^[8][1][9][9]|^[8][2][2][1|2]|^[8][2][9][5]|^[8][3][9][6|7|8]|^[8][5][7][0|1|2]|^[8][6][0][7]|^[8][6][8][3|4|5]|^[8][7][0][8]|^[8][8][1][3|4|6]|^[8][9][0][1]',x)
    hr4 = re.findall('^[8][9][3|5][0]|^[7][0][1][5]|^[7][0][2][7]|^[7][0][5][6]|^[7][0][8][2]|^[7][1][0][0]|^[7][2][0][6]|^[7][4][0][0|4]|^[7][4][1][9]|^[7][8][7][6]|^[7][9][0][0]|^[7][9][8][8]',x)
    dl1 = re.findall('^[9][0][1][3]|^[9][0][6][9]|^[9][2][0][5]|^[9][3][1][0|1|2|5|8]|^[9][3][5][4|5]|^[9][5][4|6][0]|^[9][5][8][2]|^[9][5][9][9]|^[9][6][2][5]|^[9][6][4][3]',x)
    dl2 = re.findall('^[9][6][5][0|4]|^[9][7][1][1|6|7|8]|^[9][8][1][0|1|8]|^[9][8][2][1]|^[9][8][6][8]|^[9][8][6][8]|^[9][8][7][0|1|3]|^[9][8][9][1|9]|^[9][9][1][0|1]|^[9][9][5][3|8]',x)
    dl3 = re.findall('^[9][9][6][8]|^[9][9][7][1]|^[9][9][9][0]|^[8][0][7][6]|^[8][1][3][0]|^[8][2][8][5|7]|^[8][3][2][0]|^[8][3][6][8]|^[8][3][7][3|5|6|7]|^[8][3][8][3|4]|^[8][4][4][7|8]',x)
    dl4 = re.findall('^[8][4][5][9]|^[8][4][6][7|8]|^[8][4][7][0|1]|^[8][5][0][5|6]|^[8][5][1][0|2]|^[8][5][2][7]|^[8][5][8][5|6|7|8]|^[8][5][9][5]|^[8][7][0][0]|^[8][7][4][2|3|4|5]|^[8][7][5][0]',x)
    dl5 = re.findall('^[8][7][6][6]|^[8][8][0][0|2]|^[8][8][1][0]|^[8][8][2][6]|^[8][8][5][1]|^[8][8][6][2]|^[8][8][8][2]|^[8][9][2][0|9]|^[7][0][1][1]|^[7][0][4][2]|^[7][0][5][3]',x)
    dl6 = re.findall('^[7][0][6][5]|^[7][2][1][0|7]|^[7][2][8][9]|^[7][2][9][0|1|2]|^[7][3][0][3]|^[7][4][2][8]|^[7][5][0][3]|^[7][5][3][0|1|2|3]|^[7][6][7][8]|^[7][7][0][1|3]',x)
    dl7 = re.findall('^[7][8][2][7]|^[7][8][3][4|5|6|8]|^[7][8][4][0]|^[7][8][5][9]|^[7][8][6][1|2|3]|^[7][8][9][2]|^[6][2][3][0]',x)
    pb1 = re.findall('^[9][0][4][1]|^[9][0][5][6]|^[9][1][1][5]|^[9][1][4][9]|^[9][1][4][9]|^[9][1][9][3]|^[9][2][1][6]|^[9][3][5][7]|^[9][4][1][7]|^[9][4][6][3|4|5]|^[9][5][0][1]',x)
    pb2 = re.findall('^[9][5][1][7]|^[9][5][9][2]|^[9][6][4][6]|^[9][7][7][9]|^[9][7][8][0|1]|^[9][8][0][3]|^[9][8][1][4|5]|^[9][8][5][5]|^[9][8][7][2|6|7|8]|^[9][8][8][8]',x)
    pb3 = re.findall('^[9][9][1][4|5]|^[9][9][8][8]|^[8][0][5][4]|^[8][1][4][6]|^[8][1][9][4|5|6|8]|^[8][2][8][3|4|8|9]|^[8][3][6][0]|^[8][4][2][7]|^[8][5][5][7|8]|^[8][5][6][6|7|8|9]',x)
    pb4 = re.findall('^[8][5][9][1]|^[8][6][9][9]|^[8][7][2][8|9]|^[8][8][7][2]|^[8][9][9][2]|^[7][0][0][9]|^[7][0][8][7]|^[7][3][4][7]|^[7][3][8][0]|^[7][5][0][8]|^[7][5][8][9]',x)
    pb5 = re.findall('^[7][9][9][6]|^[7][8][1][4]|^[7][8][3][7]|^[7][8][8][8|9]|^[7][9][7][3]|^[7][9][8][6]|^[6][2][8][0|3|4]',x)
    ko1 = re.findall('^[9][0][0][7]|^[9][0][3][8]|^[9][0][5][1]|^[9][0][6][2]|^[9][0][7][3]|^[9][0][8][8]|^[9][1][4|5|6][3]|^[9][1][8][9]|^[9][3][3][0|1|9]|^[9][4][3][2|3]|^[9][4][7][7]',x)
    ko2 = re.findall('^[9][6][7][4]|^[9][6][8][1]|^[9][7][4][8]|^[9][8][0][4]|^[9][8][3][0|1|6]|^[9][8][7][4|5]|^[9][9][0][3]|^[8][0][1][3|7]|^[8][1][0][0]|^[8][2][4][0]|^[8][2][9][6]',x)
    ko3 = re.findall('^[8][3][3][4|5|6|7]|^[8][3][4][8]|^[8][4][2][0]|^[8][5][8][2|3|4]|^[8][6][1][7]|^[8][6][2][1|2]|^[8][6][9][7]|^[8][7][7][7]|^[8][9][0][2]|^[8][9][1][0]|^[8][9][6|8][1]',x)
    ko4 = re.findall('^[7][0][0][3]|^[7][0][4][4]|^[7][0][5][9]|^[7][2][7][8]|^[7][4][3|4][9]|^[7][4|5][5][0]|^[7][6][8][7]|^[7][8][9][0]|^[7][9][8][0]|^[7][9][9][8]',x)
    mh1 = re.findall('^[9][0][1|2][1]|^[9][0][2][2|8]|^[9][0][4][9]|^[9][0][7][5]|^[9][0][9][6]|^[9][1][1][2]|^[9][1][3][0]|^[9][1][4][5]|^[9][1][5][6|8]|^[9][1][6][8]|^[9][1][7][5]',x)
    mh2 = re.findall('^[9][2][8][4]|^[9][3][0][9]|^[9][3][2][2|5]|^[9][3][5][6]|^[9][3][7][0|1|3]|^[9][4][0][3|4|5]|^[9][4][2][0|1|2|3]|^[9][5][0][3]|^[9][5][1][1]|^[9][5][2][7|9]',x)
    mh3 = re.findall('^[9][5][4][5]|^[9][5][5][2]|^[9][5][6][1]|^[9][5][7][9]|^[9][5][9][5]|^[9][6][0][4]|^[9][6][2][3]|^[9][6][3|5][7]|^[9][6][6][5]|^[9][6][7][3]|^[9][6][8][4]',x)
    mh4 = re.findall('^[9][7][3][0|1]|^[9][7][6][2|3|4|5|6|7]|^[9][8][2][2|3]|^[9][8][3][4]|^[9][8][6][0]|^[9][8][8][1]|^[9][8][9][0]|^[9][9][2][1|2|3]|^[9][9][6][0]|^[9][9][7][5]',x)
    mh5 = re.findall('^[8][0][0][7]|^[8][0][1][0]|^[8][0][5][5]|^[8][1][4][9]|^[8][1][7][7]|^[8][1][8][0]|^[8][2][0][8]|^[8][2][7][5]|^[8][3][0][8]|^[8][3][2|7][9]|^[8][3][8|9][0]',x)
    mh6 = re.findall('^[8][4][0][8]|^[8][4][1][1|2]|^[8][4][2][1]|^[8][4][4][6]|^[8][4][8][3|4|5]|^[8][5][5][1|2]|^[8][6][0][5]|^[8][6][5][2]|^[8][7][8][6|7|8]|^[8][7][9][3|6]',x)
    mh7 = re.findall('^[8][8][0][5|6]|^[8][8][5][5]|^[8][8][6][2]|^[8][8][8][8]|^[8][9][2][8]|^[8][9][5][6]|^[8][9][7][5]|^[8][9][8][3]|^[8][9][9][1]|^[8][9][9][9]|^[7][0][2][0]',x)
    mh8 = re.findall('^[7][0][2][8]|^[7][0][3][0|8]|^[7][0][4][0]|^[7][0][5][7|8]|^[7][0][6][6]|^[7][0][8][3]|^[7][1][0][3]|^[7][2][1][9]|^[7][2][6][2]|^[7][2][7][6]|^[7][3][0][4]|^[7][3][5][0]|^[7][3][8][5|7]|^[7][5][0|1][7]',x)
    mh9 = re.findall('^[7][5][8][8]|^[7][6][2][0]|^[7][7][0|1][9]|^[7][7][2][0|1]|^[7][7][4][1|5]|^[7][7][5][6|7]|^[7][7][6][7|8]|^[7][7][7][0|4|5]|^[7][7][9][8]|^[7][8][7][5]|^[7][9][3][0]|^[7][9][7][2]',x)
    mp1 = re.findall('^[9][0][0][9]|^[9][0][3][9]|^[9][1][0][9]|^[9][1][1][1]|^[9][1][3][1]|^[9][1][4][4]|^[9][1][6][5]|^[9][1][7][4|9]|^[9][1][9][0]|^[9][2|3][0][0]',x)
    mp2 = re.findall('^[9][3][0][1|2|3]|^[9][3][2][9]|^[9][3][4][0]|^[9][3][9][9]|^[9][4][0][6|7]|^[9][4][2][4|5]|^[9][4][7][9]|^[9][5][5][2]|^[9][5][7][5]|^[9][5][8][4|9]',x)
    mp3 = re.findall('^[9][6][9][1]|^[9][6][8][5]|^[9][6][6][9]|^[9][6][4][4]|^[9][6][3][0]|^[9][6][1][7]|^[9][7][1][3]|^[9][7][5][2|3|4|5]|^[9][7][7][0]|^[9][8][9][3]|^[9][8][2][7|6]|^[9][8][0][6]',x)
    mp4 = re.findall('^[9][9][2][6]|^[9][9][7][7]|^[9][9][9][3]|^[8][0][8][5]|^[8][1][2][0]|^[8][1][0][9|3]|^[8][2][2][3|4|5|6]|^[8][2][3][4|6]|^[8][2][6][9]|^[8][3][5][7|8|9]',x)
    mp5 = re.findall('^[8][3][4|1][9]|^[8][3][0][5]|^[8][4][3][5]|^[8][5][1][6]|^[8][6][0][0|2]|^[8][7][7][0]|^[8][8][1][5|7]|^[8][8][2][3|7]|^[8][8][3][9]|^[8][8][7][1]|^[8][8][8][9]',x)
    mp6 = re.findall('^[8][9][9][0]|^[8][9][8][9|2]|^[8][9][6][5|2]|^[8][9][5][9]|^[7][0][0][0]|^[7][0][2][4]|^[7][0][4][9]|^[7][0][6][7]|^[7][0|3][8][9]|^[7][3][5][4]|^[7][4][1][5]',x)
    mp7 = re.findall('^[7][4][8][9]|^[7][5][8][7]|^[7][5][6][6]|^[7][6][1][2|7]|^[7][6][9][7]|^[7][8][2][8]|^[7][8][6][9]|^[7][9][7][4]|^[7][8][7][9]|^[7][9][7][4]|^[7][8][7][9]|^[7][9][8][7]',x)
    mp8 = re.findall('^[7][9][9][8]|^[7][9][9][9]|^[6][2][3][2]|^[6][2][6][0|1|2|3|4|5|6|7|8|9]',x)
    mu1 = re.findall('^[9][7][0][2]|^[9][0][0][4]|^[9][3|8|9][2][0]|^[9][3][2][1|3]|^[9][2|3][2][4]|^[9][3][2][6]|^[9][0][2][9]|^[9][9][3][0]|^[9][8][3][3]|^[9][1][3][6|7]',x)
    mu2 = re.findall('^[9][1][4][6]|^[9][1][5][2]|^[9][7][5][7]|^[9][6][6][4]|^[9][1|8|9][6][7]|^[9][7][6][8]|^[9][8|9][6][9]|^[9][1|3][7][2]|^[9][0][7][6]|^[9][9][8][7]|^[9][8][9][2]',x)
    mu3 = re.findall('^[9][5][9][4]|^[9][6][9][9]|^[8][1][0][4|8]|^[8][3][1][3]|^[8][0][2][0|4]|^[8][4][2][5]|^[8][8][2][8]|^[8][0][3][0]|^[8][4|8][4][4]|^[8][4][5][1]|^[8][6][5][5|7]',x)
    mu4 = re.findall('^[8][7][6][7]|^[8][2][6][8]|^[8][1|3][6][9]|^[8][9][7][6]|^[8][8][7][9]|^[8][0][8][0|2]|^[8][2][8][6]|^[8][2|6][9][1]|^[8][0][9][7]|^[8][8][9][8]|^[8][4][9][9]',x)
    mu5 = re.findall('^[7][5][0][6]|^[7][2][0][8]|^[7][7][1][0|8]|^[7][0][2][1]|^[7][7][3][8]|^[7][0][3][9]|^[7][0][4][5]|^[7][6][6][6]|^[7][8][6][7]|^[7][9][7][7]|^[7][4][9][8]',x)
    wb1 = re.findall('^[9][0][0][2]|^[9][0][4][6]|^[9][0][8][3]|^[9][0][9][1|3]|^[9][1][9][7]|^[9][3][3][2|3]|^[9][3][8][2]|^[9][4][3][4]|^[9][4][7][4|5|6]|^[9][5][6][4|3]',x)
    wb2 = re.findall('^[9][5][9][3]|^[9][6][0][9]|^[9][6][1][4]|^[9][6][4][1]|^[9][6][4][7]|^[9][7][3][2|3|4]|^[9][7][4][9]|^[9][7][7][5]|^[9][8][0][0]|^[9][8][5][1]|^[9][8][8][3]',x)
    wb3 = re.findall('^[9][9][0][7]|^[9][9][3][2|3]|^[8][0][0][1]|^[8][0][1][6]|^[8][1][0][1]|^[8][1][1][6]|^[8][1][4][5]|^[8][1][5][8|9]|^[8][2][5][0]|^[8][2][9][3]|^[8][3][4][5|6]',x)
    wb4 = re.findall('^[8][5][0][9]|^[8][5][1][3|4|5]|^[8][6][0][9]|^[8][6][4][2]|^[8][6][5][3]|^[8][6][7][0]|^[8][7][6|9][8]|^[8][7][5][9]|^[8][9][0][0|6]|^[8][9][1][8]',x)
    wb5 = re.findall('^[8][9][2][6]|^[8][9][7][2]|^[7][0][0|3][1]|^[7][0][4][7]|^[7][0][7][6]|^[7][0][9][8]|^[7][3][8][4]|^[7][4][0][7]|^[7][5][0][1]|^[7][5][8][5]|^[7][6][0][2]',x)
    wb6 = re.findall('^[7][6][7|9][9]|^[7][7][9][7]|^[7][8][7][2]|^[7][9][0][8]',x)
    ue1 = re.findall('^[9][0|3][0][5]|^[9][5][0][6]|^[9][3|8][0][7]|^[9][4][1][5]|^[9][6][1][6]|^[9][1|9][1][8]|^[9][1|2|5|9][1][9]|^[9][1][2][0]|^[9][6|7][2][1]|^[9][1][2][5]',x)
    ue2 = re.findall('^[9][0][2][6]|^[9][6][2][8]|^[9][1][2][9]|^[9][5][3][2]|^[9][2|9][3][5]|^[9][3|9][3][6]|^[9][8][3][8|9]|^[9][1][4][0]|^[9][0][4][4]|^[9][6][4][8]|^[9][4][5][0]',x)
    ue3 = re.findall('^[9][1|4|6][5][1]|^[9][4|5][5][4]|^[9][4|5][5][5]|^[9][9][5][6]|^[9][5][5][9]|^[9][1][6][1]|^[9][5][6][5]|^[9][1|3|5][6][9]|^[9][1|6][7][0]|^[9][4][7][3]',x)
    ue4 = re.findall('^[9][5][8][0]|^[9][0][8][1]|^[9][9][8][4]|^[9][8][8][9]|^[9][7][9][2|3|4|5]|^[9][6][9][5]|^[9][1|5][9][8]|^[8][4][0][0]|^[8][6][0][1]|^[8][3][0][3]|^[8][0|6][0][4]',x)
    ue5 = re.findall('^[8][0][0][5]|^[8][7][0][7]|^[8][8][0][8]|^[8][0][0][9]|^[8][1][1][5]|^[8][3|4][1][8]|^[8][4][2][3]|^[8][7][2][6]|^[8][1][2][7]|^[8][5][2][8]|^[8][9][3][3|4|5]',x)
    ue6 = re.findall('^[8][8][4][0]|^[8][5][4][3]|^[8][9][4][8]|^[8][0][5][2]|^[8][8|9][5][3]|^[8][9][5][4]|^[8][7][5][6]|^[8][9][5][7]|^[8][8][5][8]|^[8][9][6][0]|^[8][5|7][6][5]',x)
    ue7 = re.findall('^[8][5|8][7][4]|^[8][0|1|8][8][1]|^[8][1][8][2]|^[8][6|8][8][7]|^[8][0][9][0]|^[8][7][9][5]|^[8][8][9][6]|^[8][2|7][9][9]|^[7][8][0][0]|^[7][5|9][0][5]',x)
    ue8 = re.findall('^[7][0|3|6][0][7]|^[7][4][0][8]|^[7][3][0][9]|^[7][5][1][8]|^[7][2][3][7]|^[7][8][3][9]|^[7][8][4][3|4]|^[7][0][5][2]|^[7][0|7][5][4]|^[7][3|7][5][5]',x)
    ue9 = re.findall('^[7][8][6][0]|^[7][0|6][6][8]|^[7][5][7][0]|^[7][0][7][1]|^[7][2][7][2|5]|^[7][3][7][6|9]|^[7][0|8][8][0]|^[7][0][8][1]|^[7][7][8][3]|^[7][0|7][8][4]',x)
    ue10 = re.findall('^[7][9][8][5]|^[7][7][8][6]|^[7][3][8][8]|^[7][8][9][7]|^[7][3][9][8]|^[7][4][9][9]|^[6][3][0][6|7]|^[6][3][8][8]',x)
    uw1 = re.findall('^[9][8][0][8]|^[9][4][1][0|1]|^[9][0|4][1][2]|^[9][9][1][7]|^[9][5|7][2][0]|^[9][0|6|9][2][7]|^[9][5][2][8]|^[9][6][3][4]|^[9][5][3][6]|^[9][8][3][7]|^[9][6][3][9]',x)
    uw2 = re.findall('^[9][0][4][5]|^[9][5][4][8]|^[9][4|7][5][6]|^[9][4|5][5][7]|^[9][0|4|7][5][8]|^[9][7][5][9]|^[9][7][6][0|1]|^[9][0|3|5][6][8]|^[9][6][7][5]|^[9][0|6][8][2]',x)
    uw3 = re.findall('^[9][0][8][4]|^[9][3][8][9]|^[9][6][9][0]|^[9][8|9][9][7]|^[8][0][0][6]|^[8][3][0][7]|^[8][9][0][9]|^[8][3][1][7]|^[8][2][1][8]|^[8][9][2][3]|^[8][1][2][6]',x)
    uw4 = re.findall('^[8][4|6][3][0]|^[8][5][3][2]|^[8][9][3][8]|^[8][4][3][9]|^[8][4][4][9|5]|^[8][6][5][0]|^[8][7][5][5]|^[8][0][5][7]|^[8][9][5][8]|^[8][8][5][9]|^[8][2][6][5|6|7]',x)
    uw5 = re.findall('^[8][1][7][1]|^[8][2|4][7][3]|^[8][4][7][6]|^[8][0|4|5][7][7]|^[8][2|7][7][9]|^[8][1|7][9][1]|^[8][3][9][2]|^[8][2][9][3|4|5]|^[8][9][9][5|6]|^[8][8][9][9]',x)
    uw6 = re.findall('^[7][3|5][0][0]|^[7][3][0][2]|^[7][9][0][6]|^[7][4|6][0][9]|^[7][3][1][0]|^[7][0][1][7]|^[7][4][1][7]|^[7][8][3][0]|^[7][0][3][7]|^[7][3][5][1]|^[7][0][5][5]',x)
    uw7 = re.findall('^[7][0][6][0]|^[7][6][6][9]|^[7][0][7][8]|^[7][5][7][9]|^[7][9][8][3]|^[7][0][8][8]|^[7][8][9][5]|^[7][5][9][9]',x)
    if len(b)>10:
        print('The number you entered contains',len(b),'digits, enter 10 digits')
        print(x,' is an invalid phone number')
    elif a:
        print('     ',x,' is a valid phone number')
        if ap1 or ap2 or ap3 or ap4 or ap5 or ap6 or ap7 or ap8 or ap9:
            print('The phone number belongs to the state Andhra Pradesh or Telangana')
        elif tn1 or tn2 or tn3 or tn4 or tn5 or tn6 or tn7 or tn8 or tn9:
            print('The phone number belongs to the state Tamil Nadu or Pudecherry')
        elif jk1 or jk2:
            print('The phone number belongs to Union Territory Jammu and Kashmir or Ladakh')
        elif ka1 or ka2 or ka3 or ka4 or ka5 or ka6 or ka7 or ka8:
            print('The phone number belongs to the state Karnataka')
        elif bj1 or bj2 or bj3 or bj4 or bj5 or bj6 or bj7 or bj8 or bj9 or bj10:
            print('The phone number belong to the state Bihar or Jharkhand')
        elif rj1 or rj2 or rj3 or rj4 or rj5:
            print('The phone number belongs to the state Rajasthan')
        elif am1 or am2 or am3:
            print('The phone number belongs to the state Assam')
        elif gj1 or gj2 or gj3 or gj4 or gj5 or gj6 or gj7:
            print('The phone number belongs to the State of Gujarat or Union Territory of Dadra and Nagar Haveli or Daman and Diu')
        elif ne1 or ne2:
            print('The phone number belongs to North Eastren States')
        elif kl1 or kl2 or kl3 or kl4 or kl5 or kl6:
            print('The phone number belongs to the state Kerala or Union Territory of Lakshyadweep Islands')
        elif od1 or od2 or od3 or od4:
            print('The phone number belongs to the state of Odisha')
        elif hp1 or hp2:
            print('The phone number belongs to the state Himachal Pradesh')
        elif hr1 or hr2 or hr3 or hr4:
            print('The phone number belongs to the state Haryana')
        elif dl1 or dl2 or dl3 or dl4 or dl5 or dl6 or dl7:
            print('The phone number belongs to the Union Territory of Delhi')
        elif pb1 or pb2 or pb3 or pb4 or pb5:
            print('The phone number belongs to the state Punjab and Union Territory of Chandigarh')
        elif ko1 or ko2 or ko3 or ko4:
            print('The phone number belong to Kolkata, West Bengal') 
        elif mh1 or mh2 or mh3 or mh4 or mh5 or mh6 or mh7 or mh8 or mh9:
            print('The phone number belong to the state Maharashtra or Goa')
        elif mp1 or mp2 or mp3 or mp4 or mp5 or mp6 or mp7 or mp8:
            print('The phone number belong to the State of Madhya Pradesh or State of Chattisgarh')
        elif mu1 or mu2 or mu3 or mu4 or mu5:
            print('The phone number belong to Mumbai, Maharashtra')
        elif ue1 or ue2 or ue3 or ue4 or ue5 or ue6 or ue7 or ue8 or ue9 or ue10:
            print('The phone number belong to Eastren part of Uttar Pradesh')
        elif wb1 or wb2 or wb3 or wb4 or wb5 or wb6:
            print('The phone number belongs to the state West Bengal or sikkim or Andaman Nicobar Islands ')
        elif uw1 or uw2 or uw3 or uw4 or uw5 or uw6 or uw7:
            print('The phone number belong to the Westren Uttar Pradesh or State of Uttarakhand')
        else:
            print('')
            print('Choosen number is inactive or not registered')
            print('')
            print('Check the following link:-')
            print('https://en.wikipedia.org/wiki/Mobile_telephone_numbering_in_India')
            print('')
            print('If you find your number in the above link, please inform through mail sanjanavelma27@gmail.com')
            print('I will be thankful if you find and inform me about any mistakes')
    else:
        print(x,' is an invalid phone number')
        if c:
            print('you entered alphabets in your number please enter digits')
        elif e:
            print('you entered phone number starting with number less than 6')
        elif d:
            print('please enter digits, special characters are not permitted')
        elif len(b)<10 and f:
            print('you entered',len(b),'digits please enter',10-len(b),'more digits')
            #print('Please enter',10-len(b),'more digits')
        else:
            print('please enter digits, special characters are1 not permitted')
print('')
print('               Thank you')
if n>2:
    print('')
    print('By Sanjana')


# In[ ]:




