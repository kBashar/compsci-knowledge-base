# def _parse_lines_into_commands(cls, lines: List[str], strip_comments=True) -> List[str]:
#     commands = []
#     command = None

#     def finish_command():
#         nonlocal command
#         nonlocal commands
#         if command:
#             commands.append(command)
#         command = None

#     for line in lines:
#         line_s = line.strip()
#         line_r = line.rstrip()
#         is_comment = line_s.find("--") == 0
#         is_empty = not line_s

#         if is_empty:
#             continue

#         if is_comment and strip_comments:
#             continue
#         if command is None:
#             command = line_r
#         else:
#             command += "\n" + line_r
#         if not is_comment and line_r.endswith(";"):
#             finish_command()

#     finish_command()

#     return commands

def upper(nums):
    print("In upper fun")

    def lower():
        print("In Lower fun")

        for num in nums:
            print(f'working on {num}')
            if num%2 == 0:
                lower()
    lower()


if __name__ == "__main__":
    upper([1, 2, 3])