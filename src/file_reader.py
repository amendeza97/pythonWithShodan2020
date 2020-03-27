import os.path

class FileReader:
    
    path = None
    file = None

    def __init__(self, path):
        self.path = path
    
    def __assert_path(self):
        if not self.path:
            raise TypeError('file path is undefined')
        if not os.path.exists(self.path):
            raise FileExistsError('file not exists')
    
    def __close_path(self):
        if self.path:
            try:
                self.file.close()
                self.file = None
            except:
                raise BaseException('Exception ocurred to close file')

    def __execute_function(self, function):
        result = None
        self.__assert_path()
        try:
            self.file = open(self.path, 'r')
            result = function()
        except BaseException:
            raise BaseException('Exception ocurred to read from file')
        finally:
            self.__close_path()
        return result

    def read_first_line(self):
        read_line = lambda: self.file.readline()
        return self.__execute_function(read_line)
    
    def read_all_lines(self):
        read_all_lines = lambda: self.file.readlines()
        return self.__execute_function(read_all_lines)
