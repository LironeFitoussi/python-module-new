name = "michael "
# print(len(name))

# booleans
is_user_logged_in = True
print(type(is_user_logged_in))

# Usage of Quotes "" and ''
str1 = "Python"
str2 = 'DevOps'

# Muliline String
command_template = """
    line one
line two
"""
# print(len(command_template))
# print(command_template)

# f-string
result = 7 / 2
# print(result)
# print(f"Result {result}")
# echo "Result: ${result}"

# print(type(name))

## Methods
# .strip()
course_title = "   Python for DevOps   "
# print(course_title)
# print(f"the current lenght is {len(course_title)}")

# Remove spcae in both side
course_title = course_title.strip() 
# print(course_title)
# print(f"the current lenght NOW is {len(course_title)}")


# .lstrip()
course_title = "   Python for DevOps   "
# print(course_title)
# print(f"the current lenght is {len(course_title)}")
course_title = course_title.lstrip() 
# print(course_title)
# print(f"the current lenght NOW is {len(course_title)}")


# .rstrip()
course_title = "   Python for DevOps   "
# print(course_title)
# print(f"the current lenght is {len(course_title)}")
course_title = course_title.rstrip()
# print(course_title)
# print(f"the current lenght NOW is {len(course_title)}")


# .upper() | .lower()
course_title = "Python for DevOps"
# print(course_title.upper())
# print(course_title.lower())

# startswith / endswith
filename = "file.yaml"

# print(filename.startswith("file"))
# print(filename.startswith("baba"))

# print(filename.endswith("#yaml"))
# print(filename.endswith(".yaml"))
# print(filename.endswith("ml")) #True

# Indexing
path = "/home/lirone"
# print(path[6])

# Slicing
path = "/home/lirone"
print(path[3:10])
print(path[3:])
print(path[:1])
print(path[1])

# Immutable - לא ניתן לשינוי
course_title = "Python for DevOps"
course_title = "python for DevOps"
course_title[0] = "p" # not allowed