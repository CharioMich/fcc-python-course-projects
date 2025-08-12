class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance() 

    def get_balance(self):
        return sum([move['amount'] for move in self.ledger])

    def transfer(self, amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {Category.category}')
            Category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False
    
    def __str__(self):
        total = 0
        string = self.category.center(30, '*') + '\n'
        for move in self.ledger:
            total += move['amount']
            move['amount'] = "{:.2f}".format(move['amount'])
            string += f"{move['description']:.23} {move['amount'].rjust(29 - len(move['description']))}\n"
        string += f"Total: {total}"
        return string


def create_spend_chart(categories):

    #Dictionary to be filled with the name of the category and its withdrawals
    spendings = {}
    total_spendings = 0
    for obj in categories:
        amount_spent = 0
        for move in obj.ledger:
            if int(move['amount']) < 0:
                amount_spent += abs(int(move['amount']))
        spendings[obj.category] = amount_spent
        total_spendings += amount_spent
    #Update the dictionary with the percentage value
    for category, amount in spendings.items():
        spendings[category] = int(((amount / total_spendings) * 100) // 10 * 10)

    #Start filling the chart bar string
    chart = 'Percentage spent by category\n'
    PERCENTAGE_GAP = '     '
    for tens in range(100, -1, -10):
        chart += f'{str(tens):>3}| '
        for name, amount in spendings.items():
            if amount >= tens:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    chart += '    ' + 10 * '-'
    chart += '\n' + PERCENTAGE_GAP

    #Find the category with the longer name to iterate over. 
    #Shorter category names will be filled with empty spaces while printing vertically.
    max_len = max(len(name) for name in spendings)
    char = 0
    while char < max_len:
        for name in spendings:
            try:
                chart += name[char] + '  '
            except IndexError:
                chart += '   '
        #This condition can be ommited but it's nessecary to pass the tests 
        if char != max_len-1:
            chart += '\n' + PERCENTAGE_GAP
        char += 1        
    return chart