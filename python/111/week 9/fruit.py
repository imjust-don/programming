def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"{fruit_list}")
    fruit_list.append('orange')
    print(fruit_list)
    thing = fruit_list.index('apple')
    fruit_list.insert(thing, 'cherry')
    print(fruit_list)
    fruit_list.remove('banana')
    print(fruit_list)
    print(fruit_list.pop(-1))
    print(fruit_list)
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(fruit_list)
main()