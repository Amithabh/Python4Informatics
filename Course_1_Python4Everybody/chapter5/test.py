while True:
    value = input('Value between 0 and 100:')
    try:
        value = int(value)
    except ValueError:
        print ('Valid number, please')
        continue
    if value=='done':
                
       break
    else:
       print ('Valid range, please: 0-100')
