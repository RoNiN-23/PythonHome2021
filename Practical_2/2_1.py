def f21(mass):
    for i in range(4):
        if mass[i] == 'pan':
            return 11
            break
        elif mass[i] == 'sage':
            for j in range(4):
                if mass[j] == 'stata':
                    return 6
                    break
                elif mass[j] == 'red':
                    return 7
                    break
                elif mass[j] == 'hcl':
                    for m in range(4):
                        if mass[m] == 1976:
                            return 8
                            break
                        elif mass[m] == 2015:
                            return 9
                            break
                        elif mass[m] == 1982:
                            return 10
                            break
        elif mass[i] == 'ebnf':
            for j in range(4):
                if mass[j] == 'red':
                    return 2
                    break
                elif mass[j] == 'hcl':
                    for m in range(4):
                        if mass[m] == 1976:
                            return 3
                            break
                        elif mass[m] == 2015:
                            return 4
                            break
                        elif mass[m] == 1982:
                            return 5
                            break
                    break
                elif mass[j] == 'stata':
                    for m in range(4):
                        if mass[m] == 'eagle':
                            return 0
                            break
                        elif mass[m] == 'tea':
                            return 1
                            break
