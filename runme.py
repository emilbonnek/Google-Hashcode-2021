import sys, os
from code import do_stuff


def get_input_files():
    """ Get all files from directory ending with the .in extension
    """
    files = [f for f in os.listdir('./ins/')]
    inputfiles = []
    for f in files:
        if str(f).endswith('.txt'):
            inputfiles.append(str(f))
    return inputfiles


def parse_input_file(file_name):
    """ Reads input from specific file and puts each line into a list.
    """
    with open("./ins/"+file_name) as infile:
        content = infile.read().splitlines()
    return content


def put_output(output, infile):
    """Writes the count of lines + \n and then all elements (strings) in a list one after the other seperated by \n
    """
    with open('./outs/'+infile[:-3], 'w') as outfile:
        outfile.write(f'{len(output)}\n')
        for i in output:
            outfile.write("%s\n" % i)


def put_output_elements(output, infile):
    """Writes the count of lines + \n and then the count of elements in each line 
    followed by the elements seperated by ' ' ending with a newline
    """
    with open('./outs/'+infile[:-3], 'w') as outfile:
        outfile.write(f'{len(output)}')
        for line_elements in output:
            # print(line_elements)
            streets = line_elements['streets']
            outfile.write(f'\n{line_elements["id"]}\n{len(streets)}')
            for i in streets:
                outfile.write(f'\n{i[0]} {i[1]}')
            

if __name__ == "__main__":
    runfile = ''
    try:
        runfile = sys.argv[1]
    except IndexError:
        pass

    # If we passed a filename as argument, run with that file as input
    if runfile:
        print(f'Running for {runfile}')
        params = parse_input_file(runfile)
        output = do_stuff(params)
        put_output_elements(output, runfile)
        print(f'{runfile} done')
    # Otherwise, run for all input files in turn. 
    else:
        infiles = get_input_files()
        print(f'Runnig for all files in ./ins directory')
        for infile in infiles:
            print(f'Running for {infile}')
            params = parse_input_file(infile)
            output = do_stuff(params)
            # put_output(output, infile)
            put_output_elements(output, infile)
            print(f'{infile} Done')