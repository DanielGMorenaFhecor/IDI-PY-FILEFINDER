# Imports
import os
import io
import configparser
import win32net
import pathlib
import typing


def main() -> None:

    # Print init info
    print_init_info()

    # Read settings
    config = configparser.ConfigParser()
    try:
        config.read('settings.ini')
        servers = config['DEFAULT']['Servers'].split(',')
        exts = config['DEFAULT']['FileExt'].split(',')
        outfile = config['DEFAULT']['OutFile']
        verbose = config['DEFAULT'].getboolean('Verbose')
    except Exception:
        print('ERROR: could not load config file settings.ini')
        input('Press any key to close...')
        return

    # Open a file for the output
    with open(rf'{outfile}', 'w') as stream:
        # Get the files and write them on the run
        print_cancel_msg()
        try:
            _ = get_files(servers, exts,
                          lambda filepath: print_result(filepath, stream),
                          verbose=verbose)
            print('Finished!')

        except KeyboardInterrupt:
            print('Process interrupted!')
            stream.close()

    input('Press any key to close...')


def get_files(
        servers: typing.Iterable[str],
        exts: typing.Iterable[str],
        callback: typing.Callable[[str], None] = None,
        verbose: bool = True,
        ) -> list[str]:
    '''Returns a list with all files in all servers with a set of extensions'''
    # Iterates through servers
    for server in servers:

        if verbose:
            print(f'Search on server {server} started')

        # Get the shared folders
        for share in win32net.NetShareEnum(server):

            path = rf'//{server}/{share[0]}/'

            if verbose:
                print(f'Search on share {path} started')

            # Walk through the folder
            for root, _, files in os.walk(path):
                for file in files:
                    filepath = os.path.join(root, file)

                    # Check file extension
                    ext = pathlib.Path(file).suffix
                    if ext not in exts:
                        continue

                    # Add to list if not exists
                    if filepath in files:
                        continue

                    # Print the result in the screen
                    if verbose:
                        print(f'File found: {filepath}')

                    # Callback function
                    callback(filepath)
                    files.append(filepath)

    return files


def print_result(filepath: str, stream: io.TextIOWrapper) -> None:
    '''Callback function for the found results'''
    # Write file in text file
    stream.write(filepath + '\n')
    stream.flush()


def print_init_info():
    '''Prints initial logo info'''
    print("========================FHECOR INGENIEROS CONSULTORES=========================")  # noqa: E501
    print("==============================IDI-PY-FILEFINDER===============================")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&                                                       ")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&                                                       ")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&      %&&&&, &    /#  &&&&&  *&&&%   #&&&#   %&&&#     ")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&      %,     &    /#  &     &      *%     #/ %.  ))    ")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&      %,&&&  &&&&&/#  &,&&  &      *%     %* %. &.     ")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&      %,     %    /#  &     &       %.    %  %.  %     ")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&      %,     %    /#  &&&&&  %&&&%(  #&&&#   %.   %    ")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&                                                       ")  # noqa: E501
    print("     &&&&&&&&&&&&&&&&&&                                                       ")  # noqa: E501
    print("==============================================================================")  # noqa: E501
    print("==============================================================================")  # noqa: E501
    print("Daniel González de la Morena (dgm@fhecor.es)                                  ")  # noqa: E501
    print("==============================================================================")  # noqa: E501
    print()
    print()


def print_cancel_msg():
    '''Prints how to cancel the process'''
    print('--------------------------------------------------------')
    print('Press CTRL+C to CANCEL the process and write the results')
    print('--------------------------------------------------------')
    print()


if __name__ == "__main__":
    main()
