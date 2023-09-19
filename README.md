# Network File List Application

## Goal of the Application

The Network File List Application is designed to facilitate the task of listing all files with a specified extension from a connected network. It automates the process of iterating over different servers, directories, and files, and then compiles a comprehensive list of the selected files. Only directories and files with read permissions will be processed.

## How to Use the Application

Follow these steps to effectively use the Network File List Application:

### Step 1: Download the Application

- Download the `network-file-list.exe` executable file.
- Also, download the `settings.ini` configuration file.

### Step 2: Configure the `settings.ini` File

Open the `settings.ini` file using a text editor and configure the following parameters:

- **FileExtensions**: Specify the file extensions you want to list, separated by commas. For example, if you want to list all `.txt` and `.pdf` files, set it as follows:

  ```
  FileExtensions = .txt,.pdf,.jpg
  ```

- **Servers**: List all the servers you want to include in the search, separated by commas. Provide the server names or IP addresses. For example:

  ```
  Servers = Server1,Server2,192.168.1.100
  ```

- **OutFile**: Define the path to the result file where the list of files will be saved. By default, it is set to `result.txt`. You can change it to any desired file path.

  ```
  OutFile = C:\path\to\your\output\file.txt
  ```

- **Verbose**: Set this option to either 'yes' or 'no' based on your preference.
  - If set to 'yes', the application will display progress information while scanning the network.
  - If set to 'no', no progress information will be displayed on the screen. This is useful for a silent operation.
  ```
  Verbose = yes
  ```

### Step 3: Run the Application

Execute the `network-file-list.exe` executable with the configured `settings.ini` file. The application will start scanning the network based on your specified parameters and will write the list of files into the result file you defined in `OutFile`.

**Note**: If you want to stop the scanning process at any time, you can press `CTRL+C` to interrupt it.

Now you can easily list files with specific extensions from your network with the Network File List Application. Enjoy efficient and automated file searching!
