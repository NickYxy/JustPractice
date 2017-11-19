# #元祖的不可变与可变性
# T = (1,[2,3],4)
# # T[1] = 'spam'
# # print(T)
# T[1][0] = 'spam'
# print(T)
#
# class Play():
#
#     pass
#
#
# print(type(Play.__class__))
#
# string = """Howdy, world!"""
# print(isinstance(string,str))


# a = "He said, \"Don't\""
# b = 'He said, "Don\'t"'
# print(a)
# print(b)
#
# # string = """Hello "world\""""
# string = "\n"
# print(len(string))
#
# original = "Hello, "
# hi = original
# there = "world"
# hi += there
# # print(hi)
# # print(original)
#
# print(isinstance(None, object))


# def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
#     """
#     What is the Exception that is thrown when you call a method that does
#     not exist?
#
#     Hint: launch python command console and try the code in the block below.
#
#     Don't worry about what 'try' and 'except' do, we'll talk about this later
#     """
#     try:
#         None.some_method_none_does_not_know_about()
#     except Exception as ex:
#         ex2 = ex
#         print(ex2.args[0])
#
# test_what_exception_do_you_get_when_calling_nonexistent_methods(self=1)

#
# print(none11(1))
# print(None is None)
# # print(ex2.__class__)
# print(help(AttributeError))
# import math
# print(len([]))
# noms = ['peanut', 'butter', 'and', 'jelly']
# print(noms[2:2])
# print(noms[2:2])
#
# stack = [10, 20, 30, 40]
# stack.append('last')
# print(stack)
#
# popped_value = stack.pop()
# print(popped_value)
# print(stack)
#
# print(math.sqrt(5))
# print(len("bacon, "))
# sting = "Bacon, lettuce and tomato"
# print(sting[1:3])
# print(ord('a'))



# count_of_three = (1, 2, 5)
# count_of_three[1] = "three"
#
#
# def test_tuple_constructor_can_be_surprising(self):
#     self.assertEqual(('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!'), tuple("Surprise!"))

def test(self, a, b = 'a'):
    return [a, b]

def test1(self):

    print(self.test(1))