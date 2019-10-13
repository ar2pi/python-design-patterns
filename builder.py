class Indentor:
    def __init__(self, indent=0, step=2):
        self.indent = indent
        self.step = step

    def increment(self):
        self.indent += 1
        return self

    def decrement(self):
        self.indent -= 1
        return self

    def with_indent(self, message):
        return self.indent * self.step * ' ' + str(message)


class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f'self.{self.name} = {self.value}'


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []
        self.indentor = Indentor()

    def add_indent(self):
        return self.indentor.increment()

    def print(self, message):
        return self.indentor.with_indent(message)

    def __str__(self):
        lines = [f'class {self.name}:']
        self.add_indent()

        if not self.fields:
            lines += [self.print('pass')]

        else:
            lines += [self.print('def __init__(self):')]
            self.add_indent()
            lines += list(map(lambda field: self.print(field), self.fields))

        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, class_name):
        self.__class = Class(class_name)

    def add_field(self, name, value):
        self.__class.fields.append(Field(name, value))
        return self

    def __str__(self):
        return self.__class.__str__()


person_empty = CodeBuilder('PersonEmpty')

person = CodeBuilder('Person')\
    .add_field('name', '\"\"')\
    .add_field('age', '0')

print(person_empty)
print('---')
print(person)
