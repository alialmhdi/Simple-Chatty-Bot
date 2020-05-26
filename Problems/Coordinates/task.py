x_position = float(input())
y_position = float(input())
if x_position > 0 and y_position > 0:
    print('I')
elif x_position > 0 and y_position < 0:
    print('IV')
elif x_position < 0 and y_position > 0:
    print('II')
elif x_position < 0 and y_position < 0:
    print('III')