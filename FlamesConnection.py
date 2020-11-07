def flames_connection(person1, person2):
    """
    Flames Prediction between two partners.
    """
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    relations = {'F': 'Friend', 'L': 'Love', 'A': 'Affection',
                 'M': 'Marriage', 'E': 'Enemey', 'S': 'Sister'}

    partner1 = person1.upper()
    partner2 = person2.upper()

    person1 = person1.replace(' ', '').lower()
    person2 = person2.replace(' ', '').lower()

    for i in person1.strip().lower():
        for j in person2.lower():
            if i == j:
                person1 = person1.replace(i, '')
                person2 = person2.replace(j, '')

    count = len(person1) + len(person2)

    if count == 0:
        return print('Names are in common, No prediction/compatibility found.')

    while len(flames) > 1:
        pop_relation = count - len(flames)
        pop_relation = pop_relation - 1

        while pop_relation > len(flames) - 1:
            pop_relation = pop_relation - len(flames)

        flames.pop(pop_relation)

    return print('According to Flames Prediction, \nThe relation between ' + partner1 + ' and ' + partner2 + ' is: ', relations[flames[0]])


person1 = input('Enter the 1st Person name: ')
person2 = input('Enter the 2nd Person name: ')

flames_connection(person1, person2)
