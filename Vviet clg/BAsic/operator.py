'''
operators: symbols are used to operate on variables
types of operators
1.Arithmetic operation:+,_,/,*,%,"",//;
2.logical operation:and ,or not,X-or,x-nor,nand;
3.relational operation:==,<,>,<=,>=,!,!=;  contral floew statements
4.increment or decriment  operation:++,--;
5.assignment operation:
membership operation: weather to cheCk the element is there are not
                            in,not in;
'''

a=1;
b=2;
c=15.6;
d=40;


output=a+b*(d/b)**b-a;
print(output);

'''
[BODMAS]
output 1+2*5**2-1
output 1+2*25-1
output 1+50-1
output  51-1
output  50
'''

output=a+b*(d/b*c+a)**b-a;
print(output);


output=d%c;
print(output);


output=d//c;
print(output);

print(c/b);
print(c//b);
print(type(c/d));

print(0 & 0);
print(0 & 1);
print(1 & 0);
print(1 & 1);
'''
to combine muliple if loop operator we use logicla operator along with relational operatot
'''
print(3==7);
print(3>=7);
print(3<=7);
print(3!=7);