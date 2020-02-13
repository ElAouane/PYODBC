import os

working_dir = os.getcwd()

print(working_dir)

# def return_current_user_id():
#     print(os.getuid())
#
#
# return_current_user_id()

def encode_path_file(file):
    return os.fsencode(file)


def decode_path_file(encoded_files):
    return os.fsdecode(encoded_files)
