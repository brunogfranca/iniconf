INICONF
=======

Iniconf is a simple and easy to use tool for creating and parsing INI files.


To create an INI file:
----------------------

    from iniconf.creator import IniCreator
    cfg = IniCreator('/path/to/template/file.ini', '/path/to/destination/file.ini')
    cfg.generate_file()


To read a configuration:
------------------------

    from iniconf.config import Config
    cfg = Config(['/path/to/file1.ini', '/path/to/file2.ini', '/path/to/folder/full/of/files'])
    print cfg.config