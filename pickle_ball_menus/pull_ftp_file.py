# module to pull zip file from the jewelry machine
# create the ftp object, get the zip file and close the ftp object
import ftplib
import os
import sys

class PullFtpFile:
    def __init__( self, file_name_arg, path_arg, server_name_arg = "AMERICAN",):
        self.file_name      = file_name_arg
        self.path         = path_arg
        self.SERVER_NAME  = server_name_arg
        print( "pull object initialized." )
     
    def execute( self ):
        try:
            ftp = ftplib.FTP( self.SERVER_NAME + "_SERVER_NAME" )  # connect to host, default port
            print( "Connected to " +  self.SERVER_NAME + "_SERVER_NAME" )  # connection message from server is printed on stdout (screen)
            try:  # login with username and password - passwd is being sent in clear text
                ftp_user     = os.environ.get( self.SERVER_NAME + "_FTP_USER"     )  # get the login an password from the environment variables
                ftp_password = os.environ.get( self.SERVER_NAME + "_FTP_PASSWORD" )
                ftp.login( ftp_user, ftp_password )  
                print( "Logged into " +  self.SERVER_NAME + "_SERVER_NAME" )  # connection message from server is printed on stdout (screen)
                try:  
                    ftp.set_pasv( True )  # set passive mode on.  jewelry machine picky about this lately..
                    print( "Set passive mode on" )  # connection message from server is printed on stdout (screen)
                    try:
                        ftp.cwd( self.path_arg )  # change to directory where the file exists
                        ftp.retrbinary( 'RETR ' + self.file_name, open( self.file_name, 'wb' ).write ) # ftp get file_name
                    except ftplib.error_perm:  # catch exception if directory does not exist on server
                        print( "Error: " + self.path_arg + " does not exist on server" )  # connection message from server is printed on stdout (screen)
                except ftplib.error_perm:  # catch exception if directory does not exist on server
                    print( "Error: could not set passive mode on" )  # connection message from server is printed on stdout (screen)
            except ftplib.error_perm:  # catch exception if username or password are incorrect
                print( "Error: could not log in" )  # connection message from server is printed on stdout (screen)
        except ftplib.all_errors as e:  # catch all other exceptions, including socket errors and timeout errors, etc.
            print( "Error connecting to " +  self.SERVER_NAME + "_SERVER_NAME" )  # connection message from server is printed on stdout (screen)
            print( e )  # print exception error message
        ftp.quit()  # close ftp connection
        print( "Closed FTP connection" )  # connection message from server is printed on stdout (screen)

