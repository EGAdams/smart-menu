import datetime

def main():
    # Prompt the user for a log message
    log_message = input( "Enter the log message: " )
    
    # Get the current date and time
    now = datetime.datetime.now()
    
    # Format the date and time for the log file name
    log_file_name = now.strftime( "%b_%d_%Y_%H%M%S" ).lower() + ".log"
    
    # Create and write the log message to the file
    with open( "logs/" + log_file_name, 'w' ) as log_file:
        log_file.write( log_message )
    
    print( f"Log message saved to {log_file_name}" )

if __name__ == "__main__":
    main()
