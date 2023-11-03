from functools import singledispatch

@singledispatch
def print_only(input: object) -> None:
    pass

@print_only.register(str)  ## this allows us
def _(input: str) -> None:
    print(f'string is {input}')

@print_only.register(list)
def _(input: list) -> None:
    print(f'list is {input}')

if __name__ == '__main__':
    print_only('rishabh')
    print_only([1,2,3,4])
