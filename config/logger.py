def read_apache_log(log_file_path, num_lines=10):
    try:
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.readlines()
            num_lines_to_read = num_lines

            for line in log_content[-num_lines_to_read:]:
                print(line.strip())

    except Exception as e:
        print(f"Xato: {e}")


# server log fayli nomi
apache_log_file_path = '../path/to/your/logfile.log'

num_lines_to_read = 10

read_apache_log(apache_log_file_path, num_lines_to_read)
