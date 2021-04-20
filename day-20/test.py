# import turtle
#
# class WatchedKey:
#     def __init__(self, key):
#         self.key = key
#         self.down = False
#         turtle.onkeypress(self.press, key)
#         turtle.onkeyrelease(self.release, key)
#
#     def press(self):
#         self.down = True
#
#     def release(self):
#         self.down = False
#
# # You can now create the watched keys you want to be able to check:
# a_key = WatchedKey('a')
# b_key = WatchedKey('b')
#
# # and you can check their state by looking at their 'down' attribute
# a_currently_pressed = a_key.down
#
#
# def print_state(x, y):
#     print(a_key.down, b_key.down)
#
#
# screen = turtle.Screen()
# screen.onclick(print_state)
#
# turtle.listen()
# turtle.mainloop()
# turtle.done()
#
#
# keys_to_watch = {'a', 'b', 'c', 'd', 'space']
#
# watched_keys = {key: WatchedKey(key) for key in keys_to_watch}
#
# b_pressed = watched_keys['b'].down
#
