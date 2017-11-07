#!/usr/bin/python3

import vim

start = vim.current.buffer.mark("<")[0]
end = vim.current.buffer.mark(">")[0]

# It's basically two long lines
# at least must be.
buffer_text = vim.current.buffer[s-1:e]

lines = []
for line in buffer_text:
    l = line.split('Depends:')[1]
    lines.append(l.split(','))

print(list(set(lines[0]) - set(lines[1])))
