message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())

print("-------------------------------------")

message = 'hello world'
print(message.lower())
print(message.upper())

message = message.title()
print(message)
print(message.swapcase())

print("-------------------------------------")

location = 'Mississippi'
print(location.count('s'))

print("-------------------------------------")

print(len('how many letters in this string?'))

print("-------------------------------------")

message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

print("-------------------------------------")

message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))

print("-------------------------------------")

message = '    middle     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')

print("-------------------------------------")

message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)

print("-------------------------------------")

message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))