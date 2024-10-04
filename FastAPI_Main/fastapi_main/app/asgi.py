# app/asgi.py

from fastapi import FastAPI
from .main import app  # Import your FastAPI instance

# The ASGI application is the same as the FastAPI instance
application = app


'''C:\Users\aktiwari\Desktop\FastAPI\FastAPI_Venv\Scripts\python.exe C:\Users\aktiwari\Desktop\FastAPI\FastAPI_Venv\Lib\site-packages\wfastcgi.py'''

'''
Hosting a FastAPI application on Windows Services and IIS involves several steps, including configuring your FastAPI application to run with a WSGI server and setting up IIS to serve it. Below is a step-by-step guide on how to do this.

### Step 1: Install Required Packages

First, you need to install the `daphne` server, which is an ASGI server that works well with FastAPI.

1. **Activate your Poetry environment**:
   ```bash
   poetry shell
   ```

2. **Install Daphne**:
   ```bash
   poetry add daphne
   ```

### Step 2: Create a WSGI/ASGI Entry Point

Create a file named `asgi.py` in your `app` directory:

```python
# app/asgi.py

from fastapi import FastAPI
from .main import app  # Import your FastAPI instance

# The ASGI application is the same as the FastAPI instance
application = app
```

### Step 3: Set Up Windows Services

You can use the `NSSM` (Non-Sucking Service Manager) to run your FastAPI application as a Windows Service.

1. **Download NSSM** from the [official site](https://nssm.cc/download) and extract it.

2. **Open Command Prompt as Administrator**.

3. **Navigate to the NSSM directory**:
   ```bash
   cd path\to\nssm\win64
   ```

4. **Install your FastAPI app as a service**:
   ```bash
   nssm install FastAPIService
   ```

   A dialog will open. Fill in the details:
   - **Path**: Path to your Python executable inside your virtual environment.
   - **Startup directory**: Path to your project directory.
   - **Arguments**: The command to run your FastAPI application, for example:
     ```
     -m daphne app.asgi:application
     ```
   - Ensure to set the "Start" option to "Automatic".

5. **Start the service**:
   ```bash
   nssm start FastAPIService
   ```

### Step 4: Set Up IIS

To serve your FastAPI app via IIS, follow these steps:

1. **Install the IIS web server** on Windows:
   - Go to Control Panel > Programs > Turn Windows features on or off.
   - Enable "Internet Information Services".

2. **Install the `wfastcgi` package**:
   ```bash
   poetry add wfastcgi
   ```

3. **Configure IIS to Use FastCGI**:
   - Open the IIS Manager.
   - Select your server or the specific site.
   - Go to "Handler Mappings".
   - Click on "Add Module Mapping".
     - **Request Path**: `*.py`
     - **Module**: `FastCgiModule`
     - **Executable**: Path to your Python executable inside the virtual environment followed by the path to `wfastcgi.py` (you may need to find where this file is installed). Example:
       ```
       C:\path\to\venv\Scripts\python.exe C:\path\to\your\project\venv\Lib\site-packages\wfastcgi.py
       ```
     - **Name**: `Python FastCGI`
   - Click "OK".

4. **Configure FastCGI Settings**:
   - Go to "FastCGI Settings" in IIS.
   - Click "Add Application".
   - **Full Path**: The path to your Python executable.
   - **Environment Variables**: Add the following:
     - `WSGI_SCRIPT`: The path to `app/asgi.py`.
     - `PYTHONPATH`: Path to your project directory.

5. **Add a Website**:
   - In IIS, right-click on "Sites" and choose "Add Website".
   - Set the site name, physical path (point to your project folder), and port.

### Step 5: Access Your Application

Now, you should be able to access your FastAPI application via the configured URL in IIS, such as `http://localhost:<port>/`.

### Step 6: Logging and Monitoring

Make sure to implement proper logging in your FastAPI application (as shown previously) to track errors and application performance. You can also monitor the Windows Services to check the status of your FastAPI service.

### Conclusion

You've now successfully set up your FastAPI application to run as a Windows Service and serve it through IIS. This will help you run your FastAPI application continuously and make it accessible via HTTP. If you have any further questions or run into issues, feel free to ask!
'''

'''
The error message "FastCgiModule is not a native module, specify at least one recognized native module" indicates that IIS requires a native module to process the requests, and it seems like the FastCGI module is not properly configured.

Here's how to properly set up IIS to host your FastAPI application:

### Step 1: Ensure FastCGI Is Installed

1. **Open the Windows Features dialog**:
   - Go to Control Panel > Programs > Turn Windows features on or off.
   
2. **Make sure the following features are checked**:
   - **Internet Information Services**
     - Web Management Tools
     - World Wide Web Services
       - Application Development Features
         - CGI (ensure this is checked)

3. **Restart your computer** if you made changes.

### Step 2: Configure FastCGI with IIS

1. **Open IIS Manager**:
   - Press `Win + R`, type `inetmgr`, and hit Enter.

2. **Configure FastCGI Settings**:
   - In the left panel, select your server node (the top node).
   - In the middle panel, double-click on **FastCGI Settings**.

3. **Add FastCGI Application**:
   - Click on "Add Application".
   - **Full Path**: Browse to your Python executable (e.g., `C:\path\to\your\venv\Scripts\python.exe`).
   - Click OK.

### Step 3: Create a Handler Mapping

1. **Go to Your Site**:
   - In the left panel, expand the "Sites" node and select your site.

2. **Go to Handler Mappings**:
   - In the middle panel, double-click on **Handler Mappings**.

3. **Add Module Mapping**:
   - Click on "Add Module Mapping" on the right panel.
   - Fill in the fields:
     - **Request Path**: `*.py`
     - **Module**: Choose `FastCgiModule`.
     - **Executable**: The path to your `wfastcgi.py` script. Example:
       ```
       C:\path\to\your\venv\Scripts\python.exe C:\path\to\your\venv\Lib\site-packages\wfastcgi.py
       ```
     - **Name**: `Python FastCGI`
   - Click OK.

4. **When prompted**, choose "Yes" to create a new FastCGI application.

### Step 4: Set Environment Variables

1. **Right-click on your new mapping** and select **Edit**.
2. **Add Environment Variables**:
   - Click on the "Environment Variables" button and add:
     - `WSGI_SCRIPT`: The path to your `asgi.py` file (e.g., `C:\path\to\your\project\app\asgi.py`).
     - `PYTHONPATH`: The path to your project directory (e.g., `C:\path\to\your\project`).

### Step 5: Restart IIS

After making these configurations, restart IIS:

1. **Open Command Prompt as Administrator**.
2. Run the following command:
   ```bash
   iisreset
   ```

### Step 6: Access Your Application

Now, you should be able to access your FastAPI application via your web browser at the specified URL.

### Troubleshooting

If you still encounter issues, consider:

- **Checking Event Viewer**: Look for any errors under Windows Logs > Application.
- **Reviewing IIS Logs**: Located at `C:\inetpub\logs\LogFiles`.
- **Firewall Settings**: Ensure your firewall allows traffic on the port being used.
- **Service Status**: Ensure that the FastAPI service is running properly.

If you have further questions or run into other issues, feel free to ask!
'''

'''
To access your FastAPI application running as a Windows Service, you'll typically use a web server like IIS (Internet Information Services) to route HTTP requests to your service. Here’s how you can access your application after setting it up:

### Step 1: Verify the Service is Running

1. **Open the Windows Services Manager**:
   - Press `Win + R`, type `services.msc`, and hit Enter.

2. **Locate Your Service**:
   - Find the service you created (e.g., `FastAPIService`).
   - Check that its status is "Running." If it's not running, right-click and select "Start."

### Step 2: Check IIS Configuration

If you set up IIS to serve your FastAPI application, make sure your site is configured correctly:

1. **Open IIS Manager**:
   - Press `Win + R`, type `inetmgr`, and hit Enter.

2. **Verify Your Site**:
   - In the left panel, expand your server node and click on "Sites."
   - Find the site you created for your FastAPI application.

3. **Check Binding**:
   - Right-click on your site and select "Edit Bindings."
   - Make sure it is bound to the appropriate IP address and port (e.g., `localhost:80` or `localhost:8000`).

### Step 3: Access Your Application

1. **Open a Web Browser**:
   - Enter the URL corresponding to your IIS site. For example:
     - If you set it up on the default port (80), go to: `http://localhost/`
     - If you set it on a different port (e.g., 8000), go to: `http://localhost:8000/`

2. **Test API Endpoints**:
   - If you have specific API endpoints (like `/api/products/`), you can access them directly in your browser or use tools like Postman or curl:
     ```bash
     curl http://localhost/api/products/
     ```

### Step 4: Troubleshooting

If you can't access your application:

- **Check Firewall Settings**: Ensure that Windows Firewall or any other firewall isn’t blocking the port you're using.
- **Review Application Logs**: Check the logs for any errors or issues.
- **Inspect IIS Logs**: Located typically in `C:\inetpub\logs\LogFiles`, these logs can provide insight into requests hitting your server.
- **Service Status**: Make sure your FastAPI service is running without errors.

### Summary

By following these steps, you should be able to access your FastAPI application running as a Windows Service through IIS. If you have any more questions or need further assistance, feel free to ask!
'''