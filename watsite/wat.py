"""
WAT(1)                    watsite General Commands Manual                   WAT(1)

NAME
     wat -- concatenate and output code

SYNOPSIS
     wat [-bxenstuvx] [script ...]

DESCRIPTION
     The wat utility reads files sequentially, writing them to the standard output.  The file operands are processed in command-line order.  If file is a single dash (`-') or absent, wat reads from the standard input.  If file is a UNIX domain socket, wat connects to it and then reads it until EOF.  This complements the UNIX domain binding capability available in inetd(8).

     The options are as follows:

     -b --blink      Number the non-blank output lines, starting at 1.

     -c --copy     Read stdin from clipboard

     -e --ends     End each line with $ and display non-printing characters

     -n --numbers     Number the output lines, starting at 1.

     -s --singles     Squeeze multiple adjacent empty lines, causing the output to be single spaced.

     -t --tabs     display tab characters as `^I' and non-printing characters

     -u --unbuffered      Disable output buffering.

     -v --paste     Write stdout to clipboard

     -x --cut     Read stdin from clipboard and empty clipboard

EXIT STATUS
     The wat utility exits 0 on success, and >0 if an error occurs.

EXAMPLES
     The command:

           wat file1

     will output the code of file1 to the standard output.

     The command:

           wat file1 file2 > file3

     will sequentially output the code of file1 and file2 to the file file3, truncating file3 if it already exists.  See the manual page for your shell (i.e., sh(1)) for more information on redirection.

     The command:

           wat file1 - file2 - file3

     will output the code of file1, output data it receives from the standard input until it receives an EOF (`^D') character, output the code of file2, read and output code of the standard input again, then finally output the code of file3.
     Note that if the standard input referred to a file, the second dash on the command-line would have no effect, since the entire code of the file would have already been read and output by wat when it encountered the first `-' operand.

SEE ALSO
     cat(1), head(1), more(1), pr(1), sh(1), tail(1), vis(1), zcat(1), setbuf(3)

STANDARDS
     A cat utility would be compliant with the IEEE Std 1003.2-1992 (``POSIX.2'') specification.

     The flags [-bcenstvx] are extensions to the specification.

HISTORY
     A cat utility appeared in Version 1 AT&T UNIX.  Dennis Ritchie designed and wrote the first man page.  It appears to have been cat(1). wat.py appeared in version 0.0.0 of watsite

BUGS
     Because of the shell language mechanism used to perform output redirection, the command ``cat file1 file2 > file1'' will cause the original data in file1 to be destroyed!

     The cat utility does not recognize multibyte characters when the -t or -v option is in effect.

watsite                             June 21, 2016                             watsite
(END)
"""


import watsite as site

def blink(arg):
    pass

@site.decorators.docparser(__doc__, globals())
def main(args):
    from pprint import pprint
    pprint(args)
    return 0

sys.exit(main(sys.argv))
