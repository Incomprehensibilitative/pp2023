import subprocess
# From hieplnc 

def parse(cmd_str):
    """Parse a command string into a list of tokens."""
    toks = cmd_str.split()
    # argument vector 
    argv = [] 

    # Structure of argv: {'prgram': ['prog', 'arg'], 'in': 'file', 'out': 'file'}
    in_flag = None
    out_flag = None
    cmd = {'program': [], 'in': None, 'out': None}
    for tok in toks:
        # for pipe
        if tok == "|":
            # append the old cmd program and create a new cmd process
            argv.append(cmd)
            cmd = {'program': [], 'in': None, 'out': None}
        else:
            # for redirection 
            if tok == "<":
                in_flag = 1
                continue
            elif tok == ">":
                out_flag = 1
                continue
            if in_flag:
                cmd['in'] = tok
            elif out_flag:
                cmd['out'] = tok

            # for single operation
            else:
                cmd['program'].append(tok)
            in_flag = out_flag = 0
    argv.append(cmd)
    return argv


def execvp(cmd, pipe_stdout=None):
    # To run subprocess
    rst = None

    # file in and out
    f_out = None
    f_in = None

    # capture output flag, if True -> already have output file, no need to capture
    #                      if Flase -> capture output from f_in to pipe_stdout
    cap = True

    if cmd['out']:
        f_out = open(cmd['out'], 'wb')
        cap = False
    if cmd['in']:
        f_in = open(cmd['in'], 'rb')
    elif pipe_stdout:
        f_in = pipe_stdout
    prog = cmd['program']

    # why input and not stdin? Because input command read str but stdin read file 
    rst = subprocess.run(prog, capture_output=cap, input=f_in, stdout=f_out)

    # closing 
    if f_in and not pipe_stdout:
        f_in.close()
    if f_out:
        f_out.close()
    return rst


while True:
    try: 
        cmd_str = input("shell> ")
        if cmd_str == "":
            continue
        if cmd_str == "exit":
            break
        argv = parse(cmd_str)
        pipe_stdout = None
        for cmd in argv:
            rst = execvp(cmd, pipe_stdout)
            pipe_stdout = rst.stdout
        
        if pipe_stdout:
            print(pipe_stdout.decode('utf-8'))
            
    except FileNotFoundError:
        cmd_str = input("shell> ")
        continue
    

