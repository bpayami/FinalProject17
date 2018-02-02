import cmd


class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    def do_quit(self, arg):
        return True

    def do_look(self, item):
        item = item.lower()
        if item not in ground:
            print('You do not see that item.')
        else:
            print('were getting somewhere')
        print('\n')


print('pretend you\'ve played up until here')

location = 'Start'
ground = ['sign', 'button']

print(f'\n' + location)
print(f'You see a sign and a button \n \n')

TextAdventureCmd().cmdloop()